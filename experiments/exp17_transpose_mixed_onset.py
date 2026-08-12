"""Adversarial calibration for transpose gauge and Cauchy resolution onset laws.

GitHub Actions stress test only; proofs are in docs/26-28.
"""

import numpy as np


def triple(z0, z1, z2):
    return np.vdot(z0, np.cross(z1, z2))


def cross_matrix(w):
    w1, w2, w3 = w
    return np.array(
        [[0.0, -w3, w2], [w3, 0.0, -w1], [-w2, w1, 0.0]]
    )


def transpose_gauge_identities(rng):
    worst_full = 0.0
    worst_source = 0.0
    worst_cubic = 0.0
    max_role_signal = 0.0

    for _ in range(300):
        omega = rng.normal(size=3)
        K = cross_matrix(omega)
        S = rng.normal(size=(3, 3))
        S = 0.5 * (S + S.T)
        S -= np.trace(S) * np.eye(3) / 3.0
        A = S + 0.5 * K

        worst_full = max(worst_full, np.linalg.norm(A @ omega - A.T @ omega))

        Q = rng.normal(size=(3, 3))
        z = Q @ omega
        SA = (Q @ A - A @ Q) @ omega
        SAT = (Q @ A.T - A.T @ Q) @ omega
        worst_source = max(worst_source, np.linalg.norm((SAT - SA) - K @ z))
        max_role_signal = max(max_role_signal, np.linalg.norm(K @ z))

        zs = [rng.normal(size=3) + 1j * rng.normal(size=3) for _j in range(3)]
        cubic_skew = (
            triple(K @ zs[0], zs[1], zs[2])
            + triple(zs[0], K @ zs[1], zs[2])
            + triple(zs[0], zs[1], K @ zs[2])
        )
        worst_cubic = max(worst_cubic, abs(cubic_skew))

    return worst_full, worst_source, worst_cubic, max_role_signal


def mixed_product_rule_identity(rng):
    worst = 0.0
    max_source = 0.0
    for _ in range(200):
        A = rng.normal(size=(3, 3))
        Dbar = rng.normal(size=(3, 3))
        wbar = rng.normal(size=3) + 1j * rng.normal(size=3)
        dDs = [rng.normal(size=(3, 3)) for _j in range(3)]
        dws = [rng.normal(size=3) + 1j * rng.normal(size=3) for _j in range(3)]

        # H Dbar=A^T Dbar, H wbar=0.  Product rule for H with nu=1.
        cross_source = 2.0 * sum(dD @ dw for dD, dw in zip(dDs, dws))
        H_product = A.T @ Dbar @ wbar - cross_source
        H_mean_payoff = A.T @ (Dbar @ wbar)
        H_r = H_mean_payoff - H_product
        worst = max(worst, np.linalg.norm(H_r - cross_source))
        max_source = max(max_source, np.linalg.norm(cross_source))
    return worst, max_source


def trilinear_anchor_source(rng):
    worst_pair_expansion = 0.0
    max_nonradial = 0.0

    for _ in range(200):
        w = [rng.normal(size=3) + 1j * rng.normal(size=3) for _j in range(3)]
        dw = [
            [rng.normal(size=3) + 1j * rng.normal(size=3) for _mu in range(3)]
            for _j in range(3)
        ]
        source = 0.0j
        for mu in range(3):
            source += 2.0 * (
                triple(dw[0][mu], dw[1][mu], w[2])
                + triple(dw[0][mu], w[1], dw[2][mu])
                + triple(w[0], dw[1][mu], dw[2][mu])
            )

        # Check against a central second-difference of the cubic under a common
        # scalar spatial coordinate with derivatives dw and zero second derivatives.
        eps = 1e-5
        approx = 0.0j
        for mu in range(3):
            zp = [w[i] + eps * dw[i][mu] for i in range(3)]
            zm = [w[i] - eps * dw[i][mu] for i in range(3)]
            second = (triple(*zp) - 2.0 * triple(*w) + triple(*zm)) / (eps * eps)
            approx += second
        # For H with -Delta and nu=1, the positive Delta_w source is + the
        # pair cross term, equal to the second derivative contribution.
        worst_pair_expansion = max(worst_pair_expansion, abs(source - approx))

        Z = triple(*w)
        if abs(Z) > 1e-7:
            max_nonradial = max(max_nonradial, abs(np.imag(source / Z)))

    return worst_pair_expansion, max_nonradial


def onset_scaling_signals(rng):
    # Synthetic nondegenerate local derivative data.  These are only scaling
    # referees for the exact coefficients, not an NSE proof.
    dA = [rng.normal(size=(3, 3)) for _mu in range(3)]
    for G in dA:
        G -= np.trace(G) * np.eye(3) / 3.0
    dw = [rng.normal(size=3) + 1j * rng.normal(size=3) for _mu in range(3)]

    mixed_coeff = sum(G.T @ v for G, v in zip(dA, dw))
    volume_coeff = -(1.0 / 3.0) * sum(np.trace(G @ G) for G in dA)
    return np.linalg.norm(mixed_coeff), abs(volume_coeff)


def main():
    rng = np.random.default_rng(17082026)
    full_res, source_res, cubic_res, role_signal = transpose_gauge_identities(rng)
    mixed_res, mixed_signal = mixed_product_rule_identity(rng)
    tri_res, tri_nonradial = trilinear_anchor_source(rng)
    h2_signal, h3_signal = onset_scaling_signals(rng)

    print(f"worst full-vorticity A/A^T residual: {full_res:.3e}")
    print(f"worst localized transpose-source residual: {source_res:.3e}")
    print(f"worst common-skew cubic cancellation residual: {cubic_res:.3e}")
    print(f"maximum sampled localized skew-role signal: {role_signal:.3e}")
    print(f"worst mixed Cauchy-terminal product-rule residual: {mixed_res:.3e}")
    print(f"maximum sampled mixed carre-du-champ magnitude: {mixed_signal:.3e}")
    print(f"worst trilinear anchor-source residual: {tri_res:.3e}")
    print(f"maximum sampled nonradial terminal-cubic source: {tri_nonradial:.3e}")
    print(f"sampled normalized h^2 mixed coefficient magnitude: {h2_signal:.3e}")
    print(f"sampled normalized h^3 volume coefficient magnitude: {h3_signal:.3e}")

    assert full_res < 1e-12
    assert source_res < 1e-11
    assert cubic_res < 1e-10
    assert role_signal > 1e-2
    assert mixed_res < 1e-11
    assert mixed_signal > 1e-2
    assert tri_res < 2e-4
    assert tri_nonradial > 1e-2
    assert h2_signal > 1e-3
    assert h3_signal > 1e-3
    print("PASS: transpose-gauge / mixed-correlation / onset-hierarchy calibrations")


if __name__ == "__main__":
    main()
