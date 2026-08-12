"""Adversarial calibration for strain/rotation-gradient Cauchy decomposition.

GitHub Actions stress test only; proof is in docs/34_cauchy_gradient_geometry_decomposition.md.
"""

import numpy as np


def cross_matrix(v):
    x, y, z = v
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def matrix_decomposition(rng):
    worst_gram = 0.0
    worst_sym = 0.0
    worst_trace_cross = 0.0
    worst_rot_complement = 0.0
    worst_det_trace = 0.0
    max_cross_signal = 0.0

    nu = 0.7
    h = 0.3
    for _ in range(300):
        P = rng.normal(size=(3, 3))
        P = 0.5 * (P + P.T)
        g = rng.normal(size=3)
        Q = 0.5 * cross_matrix(g)
        G = P + Q

        direct = G.T @ G
        cross = P @ Q - Q @ P
        split = P @ P - Q @ Q + cross
        worst_gram = max(worst_gram, np.linalg.norm(direct - split))
        worst_sym = max(worst_sym, np.linalg.norm(cross - cross.T))
        worst_trace_cross = max(worst_trace_cross, abs(np.trace(cross)))
        max_cross_signal = max(max_cross_signal, np.linalg.norm(cross))

        Gamma = 2.0 * nu * np.outer(g, g)
        Crot_direct = -(2.0 * nu / 3.0) * (h**3) * (Q @ Q)
        Crot_kelvin = (h**3 / 12.0) * (np.trace(Gamma) * np.eye(3) - Gamma)
        worst_rot_complement = max(worst_rot_complement, np.linalg.norm(Crot_direct - Crot_kelvin))

        trG2 = np.trace(G @ G)
        rhs = np.linalg.norm(P, "fro") ** 2 - 0.5 * (g @ g)
        worst_det_trace = max(worst_det_trace, abs(trG2 - rhs))

    return (
        worst_gram,
        worst_sym,
        worst_trace_cross,
        worst_rot_complement,
        worst_det_trace,
        max_cross_signal,
    )


def shear_calibration(rng):
    worst_metric_relation = 0.0
    worst_full_orientation = 0.0
    worst_det_cancel = 0.0
    max_cov_signal = 0.0

    for _ in range(200):
        c = rng.normal()
        P = np.array([[0.0, c / 2.0, 0.0], [c / 2.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        # omega_z=-u_y under the row-component Jacobian convention, so d_y omega_z=-c.
        g = np.array([0.0, 0.0, -c])
        Q = 0.5 * cross_matrix(g)
        G = P + Q

        strain_norm2 = np.linalg.norm(P, "fro") ** 2
        vort_grad2 = g @ g
        worst_metric_relation = max(worst_metric_relation, abs(vort_grad2 - 2.0 * strain_norm2))

        gram = G.T @ G
        target = (c * c) * np.diag([0.0, 1.0, 0.0])
        worst_full_orientation = max(worst_full_orientation, np.linalg.norm(gram - target))
        max_cov_signal = max(max_cov_signal, np.linalg.norm(gram))

        det_coeff = (1.0 / 6.0) * vort_grad2 - (1.0 / 3.0) * strain_norm2
        worst_det_cancel = max(worst_det_cancel, abs(det_coeff))

    return worst_metric_relation, worst_full_orientation, worst_det_cancel, max_cov_signal


def determinant_coefficient_identity(rng):
    worst = 0.0
    max_signed = 0.0
    for _ in range(300):
        Ps = []
        gs = []
        direct = 0.0
        for _mu in range(3):
            P = rng.normal(size=(3, 3))
            P = 0.5 * (P + P.T)
            g = rng.normal(size=3)
            Q = 0.5 * cross_matrix(g)
            direct += -(1.0 / 3.0) * np.trace((P + Q) @ (P + Q))
            Ps.append(P)
            gs.append(g)
        rhs = (1.0 / 6.0) * sum(g @ g for g in gs) - (1.0 / 3.0) * sum(
            np.linalg.norm(P, "fro") ** 2 for P in Ps
        )
        worst = max(worst, abs(direct - rhs))
        max_signed = max(max_signed, abs(rhs))
    return worst, max_signed


def main():
    rng = np.random.default_rng(22082026)
    gram_res, sym_res, cross_trace_res, rot_res, det_trace_res, cross_signal = matrix_decomposition(rng)
    shear_relation_res, shear_orient_res, shear_det_res, shear_signal = shear_calibration(rng)
    coeff_res, coeff_signal = determinant_coefficient_identity(rng)

    print(f"worst strain/rotation Gram decomposition residual: {gram_res:.3e}")
    print(f"worst cross-sector symmetry residual: {sym_res:.3e}")
    print(f"worst cross-sector trace residual: {cross_trace_res:.3e}")
    print(f"worst Kelvin-qv transverse-complement residual: {rot_res:.3e}")
    print(f"worst determinant strain/vorticity trace residual: {det_trace_res:.3e}")
    print(f"maximum sampled orientation-coupling signal: {cross_signal:.3e}")
    print(f"worst one-mode shear gradient-balance residual: {shear_relation_res:.3e}")
    print(f"worst one-mode shear covariance-orientation residual: {shear_orient_res:.3e}")
    print(f"worst one-mode shear determinant-onset residual: {shear_det_res:.3e}")
    print(f"maximum sampled one-mode shear covariance signal: {shear_signal:.3e}")
    print(f"worst signed exterior-volume coefficient residual: {coeff_res:.3e}")
    print(f"maximum sampled signed exterior-volume coefficient magnitude: {coeff_signal:.3e}")

    assert gram_res < 1e-11
    assert sym_res < 1e-12
    assert cross_trace_res < 1e-12
    assert rot_res < 1e-12
    assert det_trace_res < 1e-11
    assert cross_signal > 1e-2
    assert shear_relation_res < 1e-12
    assert shear_orient_res < 1e-12
    assert shear_det_res < 1e-12
    assert shear_signal > 1e-2
    assert coeff_res < 1e-11
    assert coeff_signal > 1e-2
    print("PASS: Cauchy strain/rotation-gradient geometry calibrations")


if __name__ == "__main__":
    main()
