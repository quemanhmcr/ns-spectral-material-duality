from __future__ import annotations

import math
import numpy as np

from src.bridge_geometry import edge_work, helical_basis


def unit(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def tangent_pair(area_vec: np.ndarray, r: float) -> tuple[np.ndarray, np.ndarray]:
    mag = np.linalg.norm(area_vec)
    n = area_vec / mag
    refs = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]
    ref = min(refs, key=lambda x: abs(float(x @ n)))
    t1 = unit(ref - (ref @ n) * n)
    t2 = np.cross(n, t1)
    scale = r * math.sqrt(mag)
    return scale * t1, scale * t2


def exp_segment_factor(theta: float) -> complex:
    if abs(theta) < 1e-10:
        return 1.0 + 0.5j * theta - theta * theta / 6.0
    return np.expm1(1j * theta) / (1j * theta)


def segment_integral(x0: np.ndarray, d: np.ndarray, k: np.ndarray, U: np.ndarray) -> complex:
    theta = float(k @ d)
    return complex((U @ d) * np.exp(1j * float(k @ x0)) * exp_segment_factor(theta))


def loop_circulation(center: np.ndarray, area_vec: np.ndarray, r: float, k: np.ndarray, U: np.ndarray) -> complex:
    p, q = tangent_pair(area_vec, r)
    x = center - 0.5 * p - 0.5 * q
    total = 0.0j
    for d in (p, q, -p, -q):
        total += segment_integral(x, d, k, U)
        x = x + d
    return total


def circulation_vector(center: np.ndarray, H: np.ndarray, r: float, k: np.ndarray, U: np.ndarray) -> np.ndarray:
    return np.array([loop_circulation(center, H[:, j], r, k, U) for j in range(3)], dtype=complex)


def main() -> None:
    k1 = np.array([1.3, -0.4, 0.7])
    k2 = np.array([-0.2, 1.1, 0.6])
    q = k1 + k2
    s1, s2, sq = 1, -1, 1
    a1 = 0.9 * np.exp(0.37j)
    a2 = 1.1 * np.exp(-0.61j)
    aq = 0.8 * np.exp(1.23j)
    u1 = a1 * helical_basis(k1, s1)
    u2 = a2 * helical_basis(k2, s2)
    uq = aq * helical_basis(q, sq)
    w1 = 1j * np.cross(k1, u1)
    w2 = 1j * np.cross(k2, u2)
    wq = 1j * np.cross(q, uq)

    H = np.array([[1.0, 0.25, -0.10], [0.15, 1.20, 0.30], [-0.20, 0.10, 0.95]])
    assert np.linalg.det(H) > 0.2
    center = np.array([0.31, -0.27, 0.44])

    phi1 = H.T @ w1
    phi2 = H.T @ w2
    phiq = H.T @ wq
    Z_exact = np.vdot(phiq, np.cross(phi1, phi2)) / np.linalg.det(H)

    n1, n2, nq = np.linalg.norm(k1), np.linalg.norm(k2), np.linalg.norm(q)
    coeff = 2.0 * (sq / nq) * (s1 / n1 - s2 / n2)
    work_direct = edge_work(k1, u1, k2, u2, uq)
    work_exact = coeff * float(np.real(Z_exact))
    assert abs(work_direct - work_exact) < 1e-12

    rs = [0.40, 0.20, 0.10, 0.05, 0.025]
    errors = []
    works = []
    phases = []
    for r in rs:
        c1 = circulation_vector(center, H, r, k1, u1)
        c2 = circulation_vector(center, H, r, k2, u2)
        cq = circulation_vector(center, H, r, q, uq)
        Hr_det = (r ** 6) * np.linalg.det(H)
        Zr = np.vdot(cq, np.cross(c1, c2)) / Hr_det
        err = abs(Zr - Z_exact) / max(1.0, abs(Z_exact))
        errors.append(float(err))
        works.append(float(coeff * np.real(Zr)))
        phases.append(float(np.angle(Zr)))

    # Centered loops have a second-order small-loop error for a smooth plane wave.
    assert errors[-1] < 2e-4
    assert errors[-1] < errors[0] / 100.0
    ratios = [errors[i] / errors[i + 1] for i in range(len(errors) - 1)]
    assert min(ratios[-2:]) > 3.0
    assert abs(works[-1] - work_direct) < 3e-4

    phase_exact = float(np.angle(Z_exact))
    phase_err = abs(np.angle(np.exp(1j * (phases[-1] - phase_exact))))
    assert phase_err < 2e-4

    print("exact complex material interaction 3-form Z_H:", Z_exact)
    print("direct signed edge work:", work_direct)
    print("small-loop radii:", rs)
    print("Kelvin circulation-triple relative errors:", errors)
    print("successive error ratios:", ratios)
    print("smallest-loop reconstructed work:", works[-1])
    print("interaction phase exact / smallest-loop:", phase_exact, phases[-1])
    print("conclusion: the missing U(1) interaction phase is realized by an oriented triple of role-filtered Kelvin circulation vectors")


if __name__ == "__main__":
    main()
