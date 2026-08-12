"""Adversarial stress for donor-kernel energy transport and future-heat identities."""
import numpy as np


def main():
    rng = np.random.default_rng(27082026)
    master = dynkin = mass = heat = defect = rate = 0.0
    signal = heat_signal = 0.0

    for _ in range(1200):
        n = int(rng.integers(3, 9))
        E = rng.uniform(0.05, 4.0, size=n)
        nu = float(rng.uniform(0.03, 1.7))
        k2 = rng.uniform(0.2, 30.0, size=n)
        d = 2.0 * nu * k2

        R = rng.uniform(0.0, 1.8, size=(n, n))
        np.fill_diagonal(R, 0.0)
        K = E[:, None] * R
        inflow = K.sum(axis=0)
        outflow = K.sum(axis=1)
        Edot = inflow - outflow - d * E

        master = max(master, np.max(np.abs(Edot - (inflow - outflow - d * E))))
        mass = max(mass, abs(Edot.sum() + np.dot(d, E)))
        signal = max(signal, float(np.linalg.norm(K)))

        f = rng.normal(size=n)
        fdot = rng.normal(size=n)
        lhs = np.dot(fdot, E) + np.dot(f, Edot)
        transfer = np.sum((f[None, :] - f[:, None]) * K)
        rhs = np.dot(fdot, E) + transfer - np.dot(d * f, E)
        dynkin = max(dynkin, abs(lhs - rhs))

        tau = float(rng.uniform(0.02, 2.5))
        q = np.exp(-d * tau)
        qdot = d * q
        Hdot = np.dot(qdot, E) + np.dot(q, Edot)
        Hrhs = np.sum((q[None, :] - q[:, None]) * K)
        heat = max(heat, abs(Hdot - Hrhs))
        heat_signal = max(heat_signal, abs(Hrhs))

        w = 1.0 - q
        wdot = -d * q
        Bdot = np.dot(wdot, E) + np.dot(w, Edot)
        Brhs = np.sum((w[None, :] - w[:, None]) * K) - np.dot(d, E)
        defect = max(defect, abs(Bdot - Brhs))

        rates = K / E[:, None]
        rate = max(rate, np.max(np.abs(rates - R)))

    # Explicit zero-energy row: nonnegative donor row must vanish and the rate convention is safe.
    E = np.array([1.0, 0.0, 2.0])
    K = np.array([[0.0, 0.4, 0.1], [0.0, 0.0, 0.0], [0.2, 0.3, 0.0]])
    rates = np.zeros_like(K)
    mask = E > 0
    rates[mask] = K[mask] / E[mask, None]
    zero_row = np.max(np.abs(K[1])) + np.max(np.abs(rates[1]))

    # Closed three-root donor/recipient table: exact row/column marginals.
    triad = 0.0
    for _ in range(400):
        a, b = rng.normal(size=2)
        works = np.array([a, b, -a - b])
        pos = np.maximum(works, 0.0)
        neg = np.maximum(-works, 0.0)
        qtot = pos.sum()
        if qtot < 1e-14:
            continue
        table = np.outer(neg, pos) / qtot
        triad = max(
            triad,
            np.max(np.abs(table.sum(axis=1) - neg)),
            np.max(np.abs(table.sum(axis=0) - pos)),
        )

    print(f"worst modal master-equation residual: {master:.3e}")
    print(f"worst total nonlinear-conservation residual: {mass:.3e}")
    print(f"worst universal Dynkin residual: {dynkin:.3e}")
    print(f"worst future-heat cancellation residual: {heat:.3e}")
    print(f"worst heat-defect/dissipation residual: {defect:.3e}")
    print(f"worst donor-rate reconstruction residual: {rate:.3e}")
    print(f"zero-energy donor-row/rate residual: {zero_row:.3e}")
    print(f"worst closed-triad transport-marginal residual: {triad:.3e}")
    print(f"maximum sampled physical transport-table norm: {signal:.3e}")
    print(f"maximum sampled future-heat transport signal: {heat_signal:.3e}")

    assert master < 1e-12
    assert mass < 2e-12
    assert dynkin < 2e-11
    assert heat < 2e-11
    assert defect < 2e-11
    assert rate < 1e-12
    assert zero_row < 1e-14
    assert triad < 1e-12
    assert signal > 1e-2 and heat_signal > 1e-4
    print("PASS: donor-kernel transport/killing and future-heat calibrations")


if __name__ == "__main__":
    main()
