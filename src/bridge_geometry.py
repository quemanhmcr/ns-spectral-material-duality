from __future__ import annotations

import math
import numpy as np

RSTAR = 0.61090410159


def unit(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=float)
    n = np.linalg.norm(v)
    if n == 0:
        raise ValueError("zero vector")
    return v / n


def leray(k: np.ndarray, v: np.ndarray) -> np.ndarray:
    k = np.asarray(k, dtype=float)
    v = np.asarray(v, dtype=complex)
    return v - k * (np.dot(k, v) / np.dot(k, k))


def transverse_frame(k: np.ndarray) -> np.ndarray:
    n = unit(k)
    refs = [np.array([0.0, 0.0, 1.0]), np.array([0.0, 1.0, 0.0]), np.array([1.0, 0.0, 0.0])]
    ref = min(refs, key=lambda r: abs(float(np.dot(n, r))))
    e1 = unit(ref - np.dot(ref, n) * n)
    e2 = np.cross(n, e1)
    return np.column_stack([e1, e2])


def helical_basis(k: np.ndarray, sign: int) -> np.ndarray:
    if sign not in (-1, 1):
        raise ValueError("helicity sign must be ±1")
    E = transverse_frame(k)
    h = (E[:, 0] + 1j * sign * E[:, 1]) / math.sqrt(2.0)
    residual = 1j * np.cross(np.asarray(k, dtype=float), h) - sign * np.linalg.norm(k) * h
    if np.linalg.norm(residual) > 1e-10:
        raise AssertionError("helical basis convention failure")
    return h


def edge_force(k1: np.ndarray, u1: np.ndarray, k2: np.ndarray, u2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    q = np.asarray(k1, dtype=float) + np.asarray(k2, dtype=float)
    w1 = 1j * np.cross(k1, u1)
    w2 = 1j * np.cross(k2, u2)
    raw = np.cross(u1, w2) + np.cross(u2, w1)
    return q, leray(q, raw)


def edge_work(k1: np.ndarray, u1: np.ndarray, k2: np.ndarray, u2: np.ndarray, uq: np.ndarray) -> float:
    q, Fq = edge_force(k1, u1, k2, u2)
    if np.linalg.norm(np.dot(q, uq)) > 1e-9:
        raise ValueError("child mode is not divergence-free")
    return float(2.0 * np.real(np.vdot(uq, Fq)))


def planar_optimal_triad() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    y = math.sqrt(RSTAR * RSTAR - 0.25)
    ka = np.array([0.5, y, 0.0])
    kb = np.array([0.5, -y, 0.0])
    kc = ka + kb
    return ka, kb, kc


def metric_uv(M: np.ndarray, na: np.ndarray, nb: np.ndarray, nc: np.ndarray) -> tuple[float, float]:
    Minv = np.linalg.inv(np.asarray(M, dtype=float))
    qa = float(na @ Minv @ na)
    qb = float(nb @ Minv @ nb)
    qc = float(nc @ Minv @ nc)
    u = 0.5 * math.log(qb / qa)
    v = 0.25 * math.log((qc * qc) / (qa * qb))
    return u, v


def metric_parent_ratios(M: np.ndarray, na: np.ndarray, nb: np.ndarray, nc: np.ndarray) -> tuple[float, float]:
    Minv = np.linalg.inv(np.asarray(M, dtype=float))
    qa = float(na @ Minv @ na)
    qb = float(nb @ Minv @ nb)
    qc = float(nc @ Minv @ nc)
    return RSTAR * math.sqrt(qa / qc), RSTAR * math.sqrt(qb / qc)


def j_env(x: float, y: float) -> float:
    x, y = sorted((float(x), float(y)))
    if not (0 < x <= y < 1 and x + y > 1):
        return 0.0
    s = x + y
    d = y - x
    L = math.log(1.0 / y)
    val = L * L * s * s * (s * s - 1.0) * (1.0 + d) ** 3 * (1.0 - d)
    den = 8.0 * (s * s - d * d) ** 2
    return math.sqrt(max(0.0, val / den))


def j_star() -> float:
    r = RSTAR
    return math.sqrt(4.0 * r * r - 1.0) * math.log(1.0 / r) / (4.0 * math.sqrt(2.0) * r)


def planar_strain_F(z: float, angle: float) -> np.ndarray:
    c, s = math.cos(angle), math.sin(angle)
    R = np.array([[c, -s], [s, c]])
    D = np.diag([math.exp(z), math.exp(-z)])
    F2 = R @ D @ R.T
    F = np.eye(3)
    F[:2, :2] = F2
    return F


def deform_covector(F: np.ndarray, k: np.ndarray) -> np.ndarray:
    return np.linalg.solve(F.T, np.asarray(k, dtype=float))
