"""Adversarial calibration for the local peak metric/q.v. growth gate.

GitHub Actions stress test only; proofs are in docs/32_local_peak_metric_qv_gate.md.
"""

import numpy as np


def metric_direction_identity(rng):
    worst = 0.0
    max_signal = 0.0
    for _ in range(300):
        H = rng.normal(size=(3, 3))
        if abs(np.linalg.det(H)) < 0.2:
            H += 2.0 * np.eye(3)
        S = rng.normal(size=(3, 3))
        S = 0.5 * (S + S.T)
        S -= np.trace(S) * np.eye(3) / 3.0
        Mdot = np.linalg.solve(H, 2.0 * S) @ np.linalg.inv(H.T)
        omega = rng.normal(size=3)
        Phi = H.T @ omega
        direct = omega @ S @ omega
        metric = 0.5 * Phi @ Mdot @ Phi
        worst = max(worst, abs(direct - metric))
        max_signal = max(max_signal, abs(direct))
    return worst, max_signal


def affine_vortex_referee(rng):
    worst_growth = 0.0
    worst_metric = 0.0
    max_margin = 0.0
    min_threshold_ratio = np.inf

    for _ in range(200):
        a = rng.uniform(0.05, 2.0)
        r0 = rng.uniform(0.1, 4.0)
        t = rng.uniform(0.0, 3.0)
        r = r0 * np.exp(2.0 * a * t)
        omega = np.array([0.0, 0.0, 2.0 * r])
        S = np.diag([-a, -a, 2.0 * a])
        e = 0.5 * (omega @ omega)
        expected_growth = 4.0 * a * e
        stretching = omega @ S @ omega
        worst_growth = max(worst_growth, abs(stretching - expected_growth))

        # Choose H=I at the instant; Mdot=2S is the objective metric velocity.
        metric = 0.5 * omega @ (2.0 * S) @ omega
        worst_metric = max(worst_metric, abs(metric - stretching))
        max_margin = max(max_margin, stretching)

        theta = rng.uniform(0.1, 10.0)
        if stretching > theta:
            min_threshold_ratio = min(min_threshold_ratio, stretching / theta)

    return worst_growth, worst_metric, max_margin, min_threshold_ratio


def incompressible_metric_det_rate(rng):
    worst = 0.0
    for _ in range(200):
        F = rng.normal(size=(3, 3))
        if abs(np.linalg.det(F)) < 0.2:
            F += 2.0 * np.eye(3)
        # Rescale to positive determinant-one magnitude; sign is irrelevant for F^T F.
        det = np.linalg.det(F)
        F = F / (abs(det) ** (1.0 / 3.0))
        if np.linalg.det(F) < 0:
            F[:, 0] *= -1.0
        A = rng.normal(size=(3, 3))
        A -= np.trace(A) * np.eye(3) / 3.0
        M = F.T @ F
        Mdot = F.T @ (A.T + A) @ F
        rate = np.trace(np.linalg.solve(M, Mdot))
        worst = max(worst, abs(rate))
    return worst


def finite_threshold_witness():
    a = 1.0
    theta = 1.0e6
    # At t=0 choose r0 so 8 a r0^2 = 2 theta.
    r0 = np.sqrt(theta / (4.0 * a))
    margin = 8.0 * a * r0 * r0
    return abs(margin - 2.0 * theta), margin / theta


def main():
    rng = np.random.default_rng(20082026)
    metric_res, metric_signal = metric_direction_identity(rng)
    growth_res, affine_metric_res, margin_signal, threshold_signal = affine_vortex_referee(rng)
    det_rate_res = incompressible_metric_det_rate(rng)
    threshold_res, threshold_ratio = finite_threshold_witness()

    print(f"worst directional metric/stretching residual: {metric_res:.3e}")
    print(f"maximum sampled directional stretching magnitude: {metric_signal:.3e}")
    print(f"worst affine-vortex enstrophy-growth residual: {growth_res:.3e}")
    print(f"worst affine-vortex metric-work residual: {affine_metric_res:.3e}")
    print(f"maximum sampled smooth affine growth margin: {margin_signal:.3e}")
    print(f"sampled affine margin/finite-threshold ratio signal: {threshold_signal:.3e}")
    print(f"worst incompressible metric determinant-rate residual: {det_rate_res:.3e}")
    print(f"explicit finite-threshold witness residual: {threshold_res:.3e}")
    print(f"explicit finite-threshold witness ratio: {threshold_ratio:.6f}")

    assert metric_res < 1e-10
    assert metric_signal > 1e-2
    assert growth_res < 1e-8
    assert affine_metric_res < 1e-8
    assert margin_signal > 1.0
    assert threshold_signal > 1.0
    assert det_rate_res < 1e-10
    assert threshold_res < 1e-8
    assert abs(threshold_ratio - 2.0) < 1e-12
    print("PASS: local peak metric/q.v. gate adversarial calibrations")


if __name__ == "__main__":
    main()
