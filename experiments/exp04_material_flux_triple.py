from __future__ import annotations

import math
import numpy as np

from src.bridge_geometry import edge_work, helical_basis


def random_invertible(rng: np.random.Generator) -> np.ndarray:
    for _ in range(100):
        H = rng.normal(size=(3, 3))
        if abs(np.linalg.det(H)) > 0.2:
            return H
    raise RuntimeError("failed to sample invertible frame")


def flux_work_formula(
    H: np.ndarray,
    k1: np.ndarray,
    s1: int,
    u1: np.ndarray,
    k2: np.ndarray,
    s2: int,
    u2: np.ndarray,
    q: np.ndarray,
    sq: int,
    uq: np.ndarray,
) -> tuple[float, float]:
    n1, n2, nq = np.linalg.norm(k1), np.linalg.norm(k2), np.linalg.norm(q)
    w1 = 1j * np.cross(k1, u1)
    w2 = 1j * np.cross(k2, u2)
    wq = 1j * np.cross(q, uq)

    # Material vorticity-flux coordinates in a common oriented area frame.
    p1 = H.T @ w1
    p2 = H.T @ w2
    pq = H.T @ wq
    triple = float(np.real(np.vdot(pq, np.cross(p1, p2))) / np.linalg.det(H))

    # u_j = s_j |k_j|^{-1} omega_j for a helical mode.
    coeff = 2.0 * (sq / nq) * (s1 / n1 - s2 / n2)
    return coeff * triple, triple


def one_state(rng: np.random.Generator) -> tuple[float, float, float, float]:
    for _ in range(100):
        k1 = rng.normal(size=3)
        k2 = rng.normal(size=3)
        q = k1 + k2
        if min(np.linalg.norm(k1), np.linalg.norm(k2), np.linalg.norm(q)) < 0.4:
            continue
        if np.linalg.norm(np.cross(k1, k2)) < 0.2:
            continue
        break
    else:
        raise RuntimeError("failed to sample nondegenerate triad")

    s1, s2, sq = (int(rng.choice([-1, 1])) for _ in range(3))
    a1 = (0.2 + rng.random()) * np.exp(1j * rng.uniform(-math.pi, math.pi))
    a2 = (0.2 + rng.random()) * np.exp(1j * rng.uniform(-math.pi, math.pi))
    aq = (0.2 + rng.random()) * np.exp(1j * rng.uniform(-math.pi, math.pi))
    u1 = a1 * helical_basis(k1, s1)
    u2 = a2 * helical_basis(k2, s2)
    uq = aq * helical_basis(q, sq)

    H = random_invertible(rng)
    direct = edge_work(k1, u1, k2, u2, uq)
    pred, triple = flux_work_formula(H, k1, s1, u1, k2, s2, u2, q, sq, uq)
    scale = max(1.0, abs(direct), abs(pred))
    work_res = abs(direct - pred) / scale

    # Passive GL(3) reparameterization H -> H L must not change the scalar.
    L = random_invertible(rng)
    pred_L, triple_L = flux_work_formula(H @ L, k1, s1, u1, k2, s2, u2, q, sq, uq)
    gl_res = max(abs(pred_L - pred), abs(triple_L - triple)) / max(1.0, abs(pred), abs(triple))

    # Physical spatial translation: resonant phases cancel because q=k1+k2.
    shift = rng.normal(size=3)
    u1_t = np.exp(1j * float(k1 @ shift)) * u1
    u2_t = np.exp(1j * float(k2 @ shift)) * u2
    uq_t = np.exp(1j * float(q @ shift)) * uq
    direct_t = edge_work(k1, u1_t, k2, u2_t, uq_t)
    pred_t, triple_t = flux_work_formula(H, k1, s1, u1_t, k2, s2, u2_t, q, sq, uq_t)
    trans_res = max(abs(direct_t - direct), abs(pred_t - pred), abs(triple_t - triple)) / max(
        1.0, abs(direct), abs(pred), abs(triple)
    )

    # Same second-order magnitudes but reverse only child phase by pi: cubic orientation flips sign.
    uq_flip = -uq
    pred_flip, triple_flip = flux_work_formula(H, k1, s1, u1, k2, s2, u2, q, sq, uq_flip)
    phase_res = max(abs(pred_flip + pred), abs(triple_flip + triple)) / max(1.0, abs(pred), abs(triple))
    return work_res, gl_res, trans_res, phase_res


def main() -> None:
    rng = np.random.default_rng(2026081204)
    worst_work = worst_gl = worst_translation = worst_phase = 0.0
    for _ in range(1200):
        wr, gr, tr, pr = one_state(rng)
        worst_work = max(worst_work, wr)
        worst_gl = max(worst_gl, gr)
        worst_translation = max(worst_translation, tr)
        worst_phase = max(worst_phase, pr)

    assert worst_work < 3e-11
    assert worst_gl < 3e-11
    assert worst_translation < 3e-11
    assert worst_phase < 3e-11
    print("direct Fourier-Leray work ↔ material flux triple worst relative residual:", worst_work)
    print("passive GL(3) frame invariance worst residual:", worst_gl)
    print("resonant spatial-translation invariance worst residual:", worst_translation)
    print("child-phase pi flip ↔ oriented-flux sign flip worst residual:", worst_phase)
    print("conclusion: signed edge work is carried by a cubic oriented material-flux invariant, not by metric/covariance alone")


if __name__ == "__main__":
    main()
