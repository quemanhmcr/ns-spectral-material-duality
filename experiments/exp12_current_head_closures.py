"""Action-only adversarial tests for the current-upstream exact closures.

The proofs are algebraic/PDE identities in docs/12 and docs/13.  These numerical
checks only stress cyclic-root phase conservation and same-replica metric algebra.
"""
from __future__ import annotations

import numpy as np


def rel(A: np.ndarray, B: np.ndarray) -> float:
    return float(np.linalg.norm(A - B) / max(1.0, np.linalg.norm(A), np.linalg.norm(B)))


def triple(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> complex:
    return complex(np.dot(a, np.cross(b, c)))


def main() -> None:
    rng = np.random.default_rng(2026081202)
    worst_cyclic_z = 0.0
    worst_work_conservation = 0.0
    worst_metric = 0.0
    worst_metric_rate = 0.0
    worst_objective_strain = 0.0
    worst_det_rate = 0.0

    for _ in range(5000):
        phis = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(3)]
        z0 = triple(phis[0], phis[1], phis[2])
        z1 = triple(phis[1], phis[2], phis[0])
        z2 = triple(phis[2], phis[0], phis[1])
        worst_cyclic_z = max(worst_cyclic_z, abs(z0-z1), abs(z0-z2))

        mags = rng.uniform(0.5, 3.0, size=3)
        signs = rng.choice(np.array([-1.0, 1.0]), size=3)
        x = signs / mags
        kappas = np.array([
            2*x[0]*(x[1]-x[2]),
            2*x[1]*(x[2]-x[0]),
            2*x[2]*(x[0]-x[1]),
        ])
        works = kappas * z0.real
        worst_work_conservation = max(worst_work_conservation, abs(float(np.sum(works))))

        D = rng.normal(size=(3, 3))
        while abs(np.linalg.det(D)) < 0.15:
            D = rng.normal(size=(3, 3))
        # Normalize only to stress incompressible determinant geometry; the metric identity
        # itself does not require det D=1.
        det = np.linalg.det(D)
        D = D / np.cbrt(det)
        rho = float(rng.uniform(0.2, 2.0))
        F = D.T
        H = rho**2 * np.linalg.inv(F).T
        M = np.linalg.inv(H.T @ H)
        gram = D @ D.T
        worst_metric = max(worst_metric, rel(gram, rho**4 * M))

        A = rng.normal(size=(3, 3))
        A -= np.trace(A)/3.0 * np.eye(3)
        S = 0.5*(A+A.T)
        Ddot = D @ A.T
        gramdot = Ddot @ D.T + D @ Ddot.T
        expected_gramdot = 2 * D @ S @ D.T
        worst_metric_rate = max(worst_metric_rate, rel(gramdot, expected_gramdot))

        Mdot = gramdot / rho**4
        objective = H @ Mdot @ H.T
        worst_objective_strain = max(worst_objective_strain, rel(objective, 2*S))
        worst_det_rate = max(worst_det_rate, abs(float(np.trace(A))))

    # Deterministic mixed-sign root works with one common phase factor.
    mags = np.array([1.0, 1.2, 1.5])
    x = 1.0 / mags
    kappas = np.array([
        2*x[0]*(x[1]-x[2]),
        2*x[1]*(x[2]-x[0]),
        2*x[2]*(x[0]-x[1]),
    ])
    assert np.any(kappas > 0) and np.any(kappas < 0)

    tol = 2e-12
    assert worst_cyclic_z < tol
    assert worst_work_conservation < tol
    assert worst_metric < tol
    assert worst_metric_rate < tol
    assert worst_objective_strain < tol
    assert worst_det_rate < tol

    print("ACTION STRESS TEST: current-upstream exact closures")
    print(f"worst cyclic interaction-phase residual: {worst_cyclic_z:.3e}")
    print(f"worst cyclic work-conservation residual: {worst_work_conservation:.3e}")
    print(f"worst Cauchy/packet-metric residual: {worst_metric:.3e}")
    print(f"worst Cauchy metric-rate residual: {worst_metric_rate:.3e}")
    print(f"worst objective-strain residual: {worst_objective_strain:.3e}")
    print(f"worst incompressible trace residual: {worst_det_rate:.3e}")
    print("PASS")


if __name__ == "__main__":
    main()
