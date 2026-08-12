"""Adversarial calibration for the full stochastic Cauchy payoff factorization.

GitHub Actions stress test only; not proof.
"""

import numpy as np


def triple(z0, z1, z2):
    return np.vdot(z0, np.cross(z1, z2))


def random_sl3_shear(rng):
    a, b, c = rng.normal(size=3)
    U = np.eye(3)
    U[0, 1] = a
    U[0, 2] = b
    U[1, 2] = c
    d, e, f = rng.normal(size=3)
    L = np.eye(3)
    L[1, 0] = d
    L[2, 0] = e
    L[2, 1] = f
    return U @ L


def mixed_polynomial(B, r):
    B0, B1, B2 = B
    r0, r1, r2 = r
    return (
        triple(r0, B1, B2)
        + triple(B0, r1, B2)
        + triple(B0, B1, r2)
        + triple(r0, r1, B2)
        + triple(r0, B1, r2)
        + triple(B0, r1, r2)
        + triple(r0, r1, r2)
    )


def full_factorization(rng):
    worst_pathwise = 0.0
    worst_mean_leg = 0.0
    worst_factor = 0.0
    max_nonradial_mixed = 0.0

    for _ in range(150):
        n = 9
        weights = rng.random(n)
        weights /= weights.sum()
        Ds = [random_sl3_shear(rng) for _j in range(n)]

        # Terminal vectors are deliberately correlated with D through its entries.
        ws = [[], [], []]
        for D in Ds:
            base = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
            ws[0].append(base[0] + (0.4 + 0.3j) * D[:, 0])
            ws[1].append(base[1] + (-0.2 + 0.5j) * D[:, 1])
            ws[2].append(base[2] + (0.1 - 0.6j) * D[:, 2])

        Dbar = sum(w * D for w, D in zip(weights, Ds))
        wbar = [sum(weights[j] * ws[i][j] for j in range(n)) for i in range(3)]

        m = []
        r = []
        B = []
        for i in range(3):
            mi = sum(weights[j] * (Ds[j] @ ws[i][j]) for j in range(n))
            Bi = Dbar @ wbar[i]
            ri = sum(
                weights[j] * ((Ds[j] - Dbar) @ (ws[i][j] - wbar[i]))
                for j in range(n)
            )
            m.append(mi)
            B.append(Bi)
            r.append(ri)
            worst_mean_leg = max(worst_mean_leg, np.linalg.norm(mi - Bi - ri))

        Zsame_D = sum(
            weights[j] * triple(Ds[j] @ ws[0][j], Ds[j] @ ws[1][j], Ds[j] @ ws[2][j])
            for j in range(n)
        )
        Zsame_w = sum(
            weights[j] * triple(ws[0][j], ws[1][j], ws[2][j]) for j in range(n)
        )
        worst_pathwise = max(worst_pathwise, abs(Zsame_D - Zsame_w))

        Zbarw = triple(*wbar)
        Delta_w = Zsame_w - Zbarw
        C = mixed_polynomial(B, r)
        Zind = triple(*m)
        rhs_gap = (1.0 - np.linalg.det(Dbar)) * Zbarw + Delta_w - C
        worst_factor = max(worst_factor, abs((Zsame_D - Zind) - rhs_gap))

        if abs(Zbarw) > 1e-7:
            max_nonradial_mixed = max(max_nonradial_mixed, abs(np.imag(C / Zbarw)))

    return worst_pathwise, worst_mean_leg, worst_factor, max_nonradial_mixed


def weighted_selection_identity(rng):
    worst = 0.0
    min_selected = 1000
    max_selected_phase_change = 0.0

    for _ in range(100):
        n = 12
        Ds = [random_sl3_shear(rng) for _j in range(n)]
        ws = [
            [rng.normal(size=3) + 1j * rng.normal(size=3) for _j in range(n)]
            for _i in range(3)
        ]

        # Hard event can depend on deformation itself.
        chi = np.array([1.0 if D[0, 1] + D[2, 0] > 0.0 else 0.0 for D in Ds])
        if chi.sum() == 0 or chi.sum() == n:
            continue
        min_selected = min(min_selected, int(chi.sum()))
        weights = chi / chi.sum()

        ZD = sum(
            weights[j] * triple(Ds[j] @ ws[0][j], Ds[j] @ ws[1][j], Ds[j] @ ws[2][j])
            for j in range(n)
        )
        Zw = sum(weights[j] * triple(ws[0][j], ws[1][j], ws[2][j]) for j in range(n))
        worst = max(worst, abs(ZD - Zw))

        # Selection is allowed to change terminal phase distribution; verify signal.
        Zall = sum(triple(ws[0][j], ws[1][j], ws[2][j]) for j in range(n)) / n
        if abs(Zall) > 1e-8 and abs(Zw) > 1e-8:
            phase_delta = abs(np.angle(Zw / Zall))
            max_selected_phase_change = max(max_selected_phase_change, phase_delta)

    return worst, min_selected, max_selected_phase_change


def radial_deformation_owner(rng):
    worst = 0.0
    for _ in range(100):
        z = [rng.normal(size=3) + 1j * rng.normal(size=3) for _i in range(3)]
        Z = triple(*z)
        if abs(Z) < 1e-8:
            continue
        J = rng.uniform(0.1, 2.5)
        pure = (1.0 - J) * Z
        worst = max(worst, abs(np.imag(pure / Z)))
    return worst


def main():
    rng = np.random.default_rng(24082026)
    path_res, mean_res, factor_res, mixed_signal = full_factorization(rng)
    select_res, min_selected, select_phase = weighted_selection_identity(rng)
    radial_res = radial_deformation_owner(rng)

    print(f"worst full-payoff common-SL(3) cancellation residual: {path_res:.3e}")
    print(f"worst mean-leg mixed-correlation residual: {mean_res:.3e}")
    print(f"worst three-owner cubic factorization residual: {factor_res:.3e}")
    print(f"maximum sampled nonradial mixed-correlation signal: {mixed_signal:.3e}")
    print(f"worst hard-selection Cauchy cancellation residual: {select_res:.3e}")
    print(f"minimum sampled selected hidden-state count: {min_selected}")
    print(f"maximum sampled selection-induced terminal phase change: {select_phase:.3e}")
    print(f"worst pure exterior-volume radial residual: {radial_res:.3e}")

    assert path_res < 1e-10
    assert mean_res < 1e-10
    assert factor_res < 1e-9
    assert mixed_signal > 1e-2
    assert select_res < 1e-10
    assert min_selected < 1000
    assert select_phase > 1e-2
    assert radial_res < 1e-12
    print("PASS: full Cauchy payoff / selected-event factorization calibrations")


if __name__ == "__main__":
    main()
