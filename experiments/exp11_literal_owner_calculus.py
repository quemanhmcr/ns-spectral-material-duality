"""Adversarial stress tests for the literal localization owner calculus.

These checks are not proofs.  They test finite-dimensional shadows of exact
operator identities and explicit counterexamples recorded in docs/11.
"""
from __future__ import annotations

import numpy as np


def comm(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def rel_residual(A: np.ndarray, B: np.ndarray) -> float:
    scale = max(1.0, np.linalg.norm(A), np.linalg.norm(B))
    return float(np.linalg.norm(A - B) / scale)


def cubic_det(v1: np.ndarray, v2: np.ndarray, v3: np.ndarray) -> complex:
    # Real examples below are enough to expose smooth-envelope overlap pollution.
    return complex(np.linalg.det(np.column_stack([v1, v2, np.conjugate(v3)])))


def main() -> None:
    rng = np.random.default_rng(20260812)

    worst_covariant = 0.0
    worst_wang_split = 0.0
    worst_low_support = 0.0
    worst_hh_repartition = 0.0
    worst_quantile_total = 0.0
    max_nontrivial_local_face = 0.0

    for _ in range(5000):
        n = int(rng.integers(4, 10))
        q = rng.uniform(0.0, 1.0, size=n)
        Q = np.diag(q).astype(complex)
        G = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        R = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        H = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        K = G + R + H
        Qdot = -comm(G, Q)

        lhs = Qdot + comm(K, Q)
        rhs = comm(K - G, Q)
        worst_covariant = max(worst_covariant, rel_residual(lhs, rhs))

        split = comm(R, Q) + comm(H, Q)
        worst_wang_split = max(worst_wang_split, rel_residual(lhs, split))

        # Literal support shadow: Q kills the low block exactly.
        low = max(1, n // 3)
        qs = rng.uniform(0.1, 1.0, size=n)
        qs[:low] = 0.0
        Qs = np.diag(qs).astype(complex)
        Omega = np.zeros(n, dtype=complex)
        Omega[:low] = rng.normal(size=low) + 1j * rng.normal(size=low)
        support_identity = comm(H, Qs) @ Omega
        support_rhs = -(Qs @ (H @ Omega))
        worst_low_support = max(worst_low_support, rel_residual(support_identity, support_rhs))

        # High-generator repartition: [H,Q]zeta = H(Qzeta) - Q(H zeta).
        zeta = rng.normal(size=n) + 1j * rng.normal(size=n)
        total = comm(H, Qs) @ zeta
        transported_selected = H @ (Qs @ zeta)
        explicit_hh_shadow = -(Qs @ (H @ zeta))
        worst_hh_repartition = max(
            worst_hh_repartition,
            rel_residual(total, transported_selected + explicit_hh_shadow),
        )

        # Fixed-mass quantile: weighted integrated face is zero, but local faces
        # are generically nonzero when material rates vary along the boundary.
        m = int(rng.integers(2, 8))
        weights = rng.uniform(0.1, 3.0, size=m)
        rates = rng.normal(size=m)
        adot = float(np.dot(weights, rates) / np.sum(weights))
        faces = weights * (adot - rates)
        worst_quantile_total = max(worst_quantile_total, abs(float(np.sum(faces))))
        max_nontrivial_local_face = max(
            max_nontrivial_local_face,
            float(np.max(np.abs(faces))),
        )

    # One-boundary calibration: fixed mass makes the single face vanish exactly.
    q_boundary = 2.3
    material_rate = -0.7
    one_face = q_boundary * (material_rate - material_rate)

    # Hard-event vs smooth-envelope counterexample with Q_i P_i=P_i.
    P1 = np.diag([1.0, 0.0, 0.0])
    P2 = np.diag([0.0, 1.0, 0.0])
    P3 = np.diag([0.0, 0.0, 1.0])
    Q1 = np.diag([1.0, 0.30, 0.20])
    Q2 = np.diag([0.40, 1.0, 0.10])
    Q3 = np.diag([0.20, 0.50, 1.0])
    v = np.ones(3)
    hard = cubic_det(P1 @ v, P2 @ v, P3 @ v)
    smooth = cubic_det(Q1 @ v, Q2 @ v, Q3 @ v)
    registration = max(
        np.linalg.norm(Q1 @ P1 - P1),
        np.linalg.norm(Q2 @ P2 - P2),
        np.linalg.norm(Q3 @ P3 - P3),
    )
    overlap_gap = abs(smooth - hard)

    tol = 2e-12
    assert worst_covariant < tol
    assert worst_wang_split < tol
    assert worst_low_support < tol
    assert worst_hh_repartition < tol
    assert worst_quantile_total < 2e-12
    assert abs(one_face) < tol
    assert registration < tol
    assert overlap_gap > 1e-2
    assert max_nontrivial_local_face > 0.1

    print("ACTION STRESS TEST: literal localization owner calculus")
    print(f"worst covariant quotient residual: {worst_covariant:.3e}")
    print(f"worst Wang relative-generator split residual: {worst_wang_split:.3e}")
    print(f"worst low-support source residual: {worst_low_support:.3e}")
    print(f"worst HH repartition residual: {worst_hh_repartition:.3e}")
    print(f"worst fixed-mass integrated-face residual: {worst_quantile_total:.3e}")
    print(f"maximum sampled nonzero local-face magnitude: {max_nontrivial_local_face:.3e}")
    print(f"hard/smooth cubic overlap gap: {overlap_gap:.6f}")
    print("PASS")


if __name__ == "__main__":
    main()
