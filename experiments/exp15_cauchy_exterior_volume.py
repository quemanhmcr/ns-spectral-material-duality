"""Adversarial calibration for Cauchy exterior-volume resolution.

This file is a numerical/algebraic stress test only.  The proofs are in docs/21-23.
It must be run by GitHub Actions, not used as proof.
"""

import numpy as np


def triple(z0, z1, z2):
    return np.vdot(z0, np.cross(z1, z2))


def det3_cols(a, b, c):
    return np.linalg.det(np.column_stack([a, b, c]))


def same_vs_independent_identity(rng):
    worst_same = 0.0
    worst_ind = 0.0
    max_defect = 0.0

    # Diagonal SL(3) mixtures make det(E D) genuinely nontrivial while each
    # replica stays exactly volume preserving.
    for _ in range(200):
        a1, b1, a2, b2 = np.exp(rng.normal(size=4))
        D1 = np.diag([a1, b1, 1.0 / (a1 * b1)])
        D2 = np.diag([a2, b2, 1.0 / (a2 * b2)])
        p = rng.uniform(0.05, 0.95)
        Dbar = p * D1 + (1.0 - p) * D2

        z = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(3)]
        Z0 = triple(*z)
        Zsame = p * triple(D1 @ z[0], D1 @ z[1], D1 @ z[2])
        Zsame += (1.0 - p) * triple(D2 @ z[0], D2 @ z[1], D2 @ z[2])
        Zind = triple(Dbar @ z[0], Dbar @ z[1], Dbar @ z[2])

        worst_same = max(worst_same, abs(Zsame - Z0))
        worst_ind = max(worst_ind, abs(Zind - np.linalg.det(Dbar) * Z0))
        max_defect = max(max_defect, abs((1.0 - np.linalg.det(Dbar)) * Z0))

    return worst_same, worst_ind, max_defect


def central_moment_volume_identity(rng):
    worst = 0.0
    for _ in range(100):
        # A finite mixture of simple determinant-one diagonal matrices.
        Ds = []
        for _j in range(5):
            a, b = np.exp(rng.normal(size=2))
            Ds.append(np.diag([a, b, 1.0 / (a * b)]))
        w = rng.random(len(Ds))
        w /= w.sum()
        Dbar = sum(wi * Di for wi, Di in zip(w, Ds))
        xis = [Di - Dbar for Di in Ds]
        cols = [Dbar[:, j] for j in range(3)]

        rhs = 0.0
        for wi, Xi in zip(w, xis):
            x = [Xi[:, j] for j in range(3)]
            rhs += wi * (
                det3_cols(x[0], x[1], cols[2])
                + det3_cols(x[0], cols[1], x[2])
                + det3_cols(cols[0], x[1], x[2])
                + det3_cols(x[0], x[1], x[2])
            )
        worst = max(worst, abs((1.0 - np.linalg.det(Dbar)) - rhs))
    return worst


def determinant_hessian_source_identity(rng):
    worst = 0.0
    max_signal = 0.0
    for _ in range(200):
        D = rng.normal(size=(3, 3))
        if abs(np.linalg.det(D)) < 0.2:
            D += 2.0 * np.eye(3)
        Es = [rng.normal(size=(3, 3)) for _ in range(3)]

        # Exact pair-column formula: (1/2) Hess(det):Gamma with nu=1.
        pair_source = 0.0
        for E in Es:
            d = [D[:, j] for j in range(3)]
            e = [E[:, j] for j in range(3)]
            pair_source += 2.0 * (
                det3_cols(e[0], e[1], d[2])
                + det3_cols(e[0], d[1], e[2])
                + det3_cols(d[0], e[1], e[2])
            )

        # Central second difference evaluates Hess(det)[E,E].
        eps = 1.0e-4
        hess_source = 0.0
        for E in Es:
            hess_EE = (
                np.linalg.det(D + eps * E)
                - 2.0 * np.linalg.det(D)
                + np.linalg.det(D - eps * E)
            ) / (eps * eps)
            hess_source += hess_EE

        worst = max(worst, abs(pair_source - hess_source))
        max_signal = max(max_signal, abs(pair_source))
    return worst, max_signal


def shear_covariance_without_volume_defect():
    # Exact upstream one-mode shear deformation has D=I+c E21.
    cs = np.array([-3.0, -0.5, 1.0, 4.0])
    w = np.array([0.1, 0.2, 0.3, 0.4])
    E21 = np.zeros((3, 3))
    E21[1, 0] = 1.0
    Ds = np.array([np.eye(3) + c * E21 for c in cs])
    Dbar = np.tensordot(w, Ds, axes=(0, 0))
    vecs = Ds.reshape(len(Ds), 9)
    zbar = np.tensordot(w, vecs, axes=(0, 0))
    centered = vecs - zbar
    Sigma = sum(wi * np.outer(v, v) for wi, v in zip(w, centered))
    return np.linalg.norm(Sigma), abs(np.linalg.det(Dbar) - 1.0)


def exact_ns_two_mode_coefficient():
    # psi=e^{-5 nu t}[cos(k.x)+a cos(l.x)], k=(1,2), l=(2,1).
    # At x=y=pi/6 both phases are pi/2.  Remove the common exponential
    # and coefficient a here; the geometric coefficient must be -72.
    k = np.array([1.0, 2.0])
    ell = np.array([2.0, 1.0])
    J = np.array([[0.0, 1.0], [-1.0, 0.0]])
    Mk = J @ np.outer(k, k)
    Ml = J @ np.outer(ell, ell)

    total = 0.0
    for mu in range(2):
        E = k[mu] * Mk + ell[mu] * Ml
        total += np.trace(E @ E)
    expected = -2.0 * np.dot(k, ell) * (np.linalg.det(np.column_stack([k, ell])) ** 2)
    delta_coefficient = -total / 3.0
    return abs(total - expected), total, delta_coefficient


def phase_radial_identity(rng):
    worst = 0.0
    for _ in range(100):
        z = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(3)]
        Z0 = triple(*z)
        if abs(Z0) < 1e-8:
            continue
        J = rng.uniform(0.05, 3.0)
        Z = J * Z0
        radial = np.imag(Z / Z0)
        worst = max(worst, abs(radial))
    return worst


def main():
    rng = np.random.default_rng(20260812)
    same_res, ind_res, max_defect = same_vs_independent_identity(rng)
    central_res = central_moment_volume_identity(rng)
    hess_res, hess_signal = determinant_hessian_source_identity(rng)
    sigma_norm, shear_det_res = shear_covariance_without_volume_defect()
    ns_res, ns_trace, ns_delta_coeff = exact_ns_two_mode_coefficient()
    radial_res = phase_radial_identity(rng)

    print(f"worst same-replica SL(3) cubic residual: {same_res:.3e}")
    print(f"worst independent-replica determinant residual: {ind_res:.3e}")
    print(f"maximum sampled exterior-volume cubic defect: {max_defect:.3e}")
    print(f"worst central-moment volume decomposition residual: {central_res:.3e}")
    print(f"worst determinant-Hessian source residual: {hess_res:.3e}")
    print(f"maximum sampled signed determinant source magnitude: {hess_signal:.3e}")
    print(f"shear deformation covariance norm: {sigma_norm:.3e}")
    print(f"shear mean-determinant defect residual: {shear_det_res:.3e}")
    print(f"two-mode exact-NS coefficient residual: {ns_res:.3e}")
    print(f"two-mode sum tr((dA)^2) coefficient: {ns_trace:.6f}")
    print(f"two-mode normalized delta h^3 coefficient: {ns_delta_coeff:.6f}")
    print(f"worst positive-real radial phase residual: {radial_res:.3e}")

    assert same_res < 1e-10
    assert ind_res < 1e-10
    assert max_defect > 1e-2
    assert central_res < 1e-10
    assert hess_res < 2e-5
    assert hess_signal > 1e-2
    assert sigma_norm > 1e-2
    assert shear_det_res < 1e-12
    assert ns_res < 1e-12
    assert abs(ns_trace + 72.0) < 1e-12
    assert abs(ns_delta_coeff - 24.0) < 1e-12
    assert radial_res < 1e-12
    print("PASS: Cauchy exterior-volume / deformation-covariance adversarial calibrations")


if __name__ == "__main__":
    main()
