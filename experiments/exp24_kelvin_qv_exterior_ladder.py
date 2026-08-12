"""Adversarial calibration for the Kelvin-qv exterior-power ladder.

GitHub Actions stress test only; proof is in docs/36_kelvin_qv_exterior_power_ladder.md.
"""

import numpy as np


def exterior_two_matrix(G):
    # Under the standard Hodge identification of (e2^e3,e3^e1,e1^e2) with
    # (e1,e2,e3), the induced two-vector generator is tr(G)I-G^T.
    return np.trace(G) * np.eye(3) - G.T


def random_psd_ladder(rng):
    worst_r2 = 0.0
    worst_r3 = 0.0
    worst_cauchy = 0.0
    max_anisotropy = 0.0
    h = 0.23

    for _ in range(300):
        B = rng.normal(size=(3, 3))
        Gamma = B @ B.T
        R2 = exterior_two_matrix(Gamma)
        R3 = np.trace(Gamma)

        # Eigenvalue representation check.
        lam = np.linalg.eigvalsh(Gamma)
        lam2 = np.linalg.eigvalsh(R2)
        expected2 = np.sort(np.trace(Gamma) - lam)
        worst_r2 = max(worst_r2, np.max(np.abs(np.sort(lam2) - expected2)))
        worst_r3 = max(worst_r3, abs(R3 - lam.sum()))

        Crot = (h**3 / 12.0) * R2
        delta_rot = (h**3 / 12.0) * R3
        # Trace R2 = 2 trace Gamma in dimension three.
        worst_cauchy = max(worst_cauchy, abs(np.trace(Crot) - 2.0 * delta_rot))
        max_anisotropy = max(max_anisotropy, np.ptp(lam2))

    return worst_r2, worst_r3, worst_cauchy, max_anisotropy


def rank_one_complement(rng):
    worst = 0.0
    worst_null = 0.0
    max_plane = 0.0
    for _ in range(200):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        lam = rng.uniform(0.01, 10.0)
        Gamma = lam * np.outer(n, n)
        R2 = exterior_two_matrix(Gamma)
        target = lam * (np.eye(3) - np.outer(n, n))
        worst = max(worst, np.linalg.norm(R2 - target))
        worst_null = max(worst_null, abs(n @ R2 @ n))
        max_plane = max(max_plane, np.trace(R2))
    return worst, worst_null, max_plane


def isotropic_branch(rng):
    worst_r2 = 0.0
    worst_r3 = 0.0
    for _ in range(100):
        gamma = rng.uniform(0.01, 20.0)
        Gamma = gamma * np.eye(3)
        R2 = exterior_two_matrix(Gamma)
        R3 = np.trace(Gamma)
        worst_r2 = max(worst_r2, np.linalg.norm(R2 - 2.0 * gamma * np.eye(3)))
        worst_r3 = max(worst_r3, abs(R3 - 3.0 * gamma))
    return worst_r2, worst_r3


def direct_cross_matrix_bridge(rng):
    worst = 0.0
    nu = 0.9
    h = 0.31
    for _ in range(200):
        g = rng.normal(size=3)
        x, y, z = g
        Q = 0.5 * np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])
        Gamma = 2.0 * nu * np.outer(g, g)
        C_direct = -(2.0 * nu / 3.0) * h**3 * (Q @ Q)
        C_ext = (h**3 / 12.0) * exterior_two_matrix(Gamma)
        worst = max(worst, np.linalg.norm(C_direct - C_ext))
    return worst


def main():
    rng = np.random.default_rng(24082026)
    r2_res, r3_res, trace_res, anis_signal = random_psd_ladder(rng)
    rank_res, null_res, plane_signal = rank_one_complement(rng)
    iso_r2_res, iso_r3_res = isotropic_branch(rng)
    direct_res = direct_cross_matrix_bridge(rng)

    print(f"worst exterior-square eigenvalue residual: {r2_res:.3e}")
    print(f"worst top-exterior trace residual: {r3_res:.3e}")
    print(f"worst Cauchy R2/R3 common-coefficient trace residual: {trace_res:.3e}")
    print(f"maximum sampled exterior-square anisotropy signal: {anis_signal:.3e}")
    print(f"worst rank-one Hodge-complement residual: {rank_res:.3e}")
    print(f"worst rank-one qv-direction null residual: {null_res:.3e}")
    print(f"maximum sampled rank-one transverse-plane signal: {plane_signal:.3e}")
    print(f"worst isotropic exterior-square residual: {iso_r2_res:.3e}")
    print(f"worst isotropic top-exterior residual: {iso_r3_res:.3e}")
    print(f"worst direct cross-matrix / exterior-lift residual: {direct_res:.3e}")

    assert r2_res < 1e-10
    assert r3_res < 1e-10
    assert trace_res < 1e-12
    assert anis_signal > 1e-3
    assert rank_res < 1e-11
    assert null_res < 1e-11
    assert plane_signal > 1e-2
    assert iso_r2_res < 1e-12
    assert iso_r3_res < 1e-12
    assert direct_res < 1e-12
    print("PASS: Kelvin-qv exterior-power ladder calibrations")


if __name__ == "__main__":
    main()
