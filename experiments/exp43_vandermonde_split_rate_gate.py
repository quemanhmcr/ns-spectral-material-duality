"""Action-only referee for the Vandermonde/divided-difference law and rate-critical split shell."""
import math
import numpy as np


def divided2(x, f):
    return sum(
        f[i] / ((x[i] - x[(i + 1) % 3]) * (x[i] - x[(i + 2) % 3]))
        for i in range(3)
    )


def main():
    rng = np.random.default_rng(43082026)
    vand = dd_res = cap_violation = collision = 0.0
    shell_gate = branch_gate = work_gate = geom_violation = 0.0
    vand_signal = rate_signal = 0.0

    # Generic exact determinant/divided-difference law.
    for _ in range(25000):
        x = np.sort(rng.uniform(-10.0, 10.0, size=3))
        if min(abs(x[1] - x[0]), abs(x[2] - x[1])) < 1e-4:
            continue
        Rtri = float(rng.uniform(-5.0, 5.0))
        T = np.array([
            (x[1] - x[2]) * Rtri,
            (x[2] - x[0]) * Rtri,
            (x[0] - x[1]) * Rtri,
        ])
        D = (x[0] - x[1]) * (x[1] - x[2]) * (x[2] - x[0])
        V2 = float(np.dot(x * x, T))
        vand = max(vand, abs(V2 + Rtri * D))
        vand_signal = max(vand_signal, abs(V2))

        # Several observables, including convex and non-convex polynomials.
        for power in [0, 1, 2, 3, 4, 5]:
            f = x ** power
            direct = float(np.dot(f, T))
            dd = divided2(x, f)
            rhs = -Rtri * D * dd
            dd_res = max(dd_res, abs(direct - rhs))

        K = float(np.max(np.abs(x)))
        cap_violation = max(cap_violation, max(0.0, abs(D) - 2.0 * K**3))

    # Signed-frequency collision: enstrophy transfer vanishes exactly.
    for _ in range(2000):
        a = float(rng.uniform(-5.0, 5.0))
        b = float(rng.uniform(-5.0, 5.0))
        Rtri = float(rng.uniform(-3.0, 3.0))
        x = np.array([a, b, b])
        T = np.array([(x[1]-x[2])*Rtri, (x[2]-x[0])*Rtri, (x[0]-x[1])*Rtri])
        collision = max(collision, abs(float(np.dot(x*x, T))))

    # Dyadic rate localization and branch work lower, using synthetic positive ledger blocks.
    for _ in range(8000):
        m = int(rng.integers(3, 18))
        Z = rng.uniform(0.01, 20.0, size=m)
        nu = float(rng.uniform(0.03, 2.0))
        V = rng.uniform(0.0, 2.0, size=m) * nu * Z
        # Force record inequality by boosting one physical block if needed.
        deficit = nu * float(Z.sum()) - float(V.sum())
        if deficit > 0.0:
            V[int(rng.integers(0, m))] += deficit + float(rng.uniform(0.0, 4.0))
        margins = V - nu * Z
        shell_gate = max(shell_gate, max(0.0, -float(np.max(margins))))
        q = int(np.argmax(margins))
        N = 2.0 ** int(rng.integers(-2, 8))
        frac = float(rng.uniform(0.0, 1.0))
        Vsep = frac * V[q]
        Vcmp = (1.0-frac) * V[q]
        ownerV = max(Vsep, Vcmp)
        branch_gate = max(branch_gate, max(0.0, 0.5 * nu * Z[q] - ownerV))
        Qowner = ownerV / (4.0 * N * N)  # worst-case variance capacity on block
        work_gate = max(work_gate, max(0.0, nu * Z[q] / (8.0 * N * N) - Qowner))
        rate_signal = max(rate_signal, Qowner)

        # Triangle geometry: second largest >= K/2; if min>=K/4 all comparable.
        K = float(rng.uniform(1.0, 10.0))
        second = float(rng.uniform(0.5, 1.0)) * K
        low = float(rng.uniform(max(1e-4, K-second+1e-6), second))
        # Enforce strict triangle low+second>K.
        if low + second <= K:
            low = K - second + 1e-5
        vals = sorted([low, second, K])
        geom_violation = max(geom_violation, max(0.0, K/2.0 - vals[1]))
        if vals[0] < K/4.0:
            geom_violation = max(geom_violation, max(0.0, 0.75*K - vals[1]))
        else:
            geom_violation = max(geom_violation, max(0.0, vals[-1]/vals[0] - 4.0))

    print(f"worst enstrophy-Vandermonde residual: {vand:.3e}")
    print(f"worst divided-difference triad residual: {dd_res:.3e}")
    print(f"worst |Vandermonde|<=2K^3 violation: {cap_violation:.3e}")
    print(f"worst signed-frequency-collision enstrophy residual: {collision:.3e}")
    print(f"worst rate-critical shell existence violation: {shell_gate:.3e}")
    print(f"worst sep/comparable variance pigeonhole violation: {branch_gate:.3e}")
    print(f"worst owner donor-work lower violation: {work_gate:.3e}")
    print(f"worst triangle second-high/comparable geometry violation: {geom_violation:.3e}")
    print(f"maximum sampled Vandermonde enstrophy signal: {vand_signal:.3e}")
    print(f"maximum sampled rate-owner work signal: {rate_signal:.3e}")

    assert vand < 2e-10
    assert dd_res < 2e-8
    assert cap_violation < 2e-12
    assert collision < 2e-12
    assert shell_gate < 2e-12
    assert branch_gate < 2e-12
    assert work_gate < 2e-12
    assert geom_violation < 2e-12
    assert vand_signal > 1e-4 and rate_signal > 1e-7
    print("PASS: Vandermonde triad / rate-critical split-scale calibrations")


if __name__ == "__main__":
    main()
