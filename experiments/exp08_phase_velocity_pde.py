from __future__ import annotations

import itertools
import math
import numpy as np

from experiments.exp05_localized_flux_pde import (
    advect,
    curl,
    fft_vec,
    grad_vec,
    lap_vec,
    matvec,
    modes,
    random_real_div_free_field,
)
from src.bridge_geometry import edge_work, helical_basis


def idx(k: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    return tuple(x % n for x in k)


def coeff(vhat: np.ndarray, k: tuple[int, int, int], n: int) -> np.ndarray:
    i = idx(k, n)
    return vhat[:, i[0], i[1], i[2]]


def hproj(v: np.ndarray, k: tuple[int, int, int], s: int) -> np.ndarray:
    kv = np.array(k, dtype=float)
    h = helical_basis(kv, s)
    return np.vdot(h, v) * h


def Z3(w1: np.ndarray, w2: np.ndarray, wq: np.ndarray) -> complex:
    return complex(np.vdot(wq, np.cross(w1, w2)))


def Zdot(
    w1: np.ndarray,
    w2: np.ndarray,
    wq: np.ndarray,
    d1: np.ndarray,
    d2: np.ndarray,
    dq: np.ndarray,
) -> complex:
    return complex(
        np.vdot(dq, np.cross(w1, w2))
        + np.vdot(wq, np.cross(d1, w2) + np.cross(w1, d2))
    )


def find_triad(what: np.ndarray, n: int) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], int, int, int]:
    ks = [k for k in itertools.product(range(-2, 3), repeat=3) if k != (0, 0, 0)]
    best = None
    best_abs = -1.0
    for k1 in ks:
        for k2 in ks:
            q = tuple(k1[j] + k2[j] for j in range(3))
            if q == (0, 0, 0) or any(abs(x) > 2 for x in q):
                continue
            if np.linalg.norm(np.cross(k1, k2)) < 0.5:
                continue
            for s1, s2, sq in itertools.product((-1, 1), repeat=3):
                w1 = hproj(coeff(what, k1, n), k1, s1)
                w2 = hproj(coeff(what, k2, n), k2, s2)
                wq = hproj(coeff(what, q, n), q, sq)
                z = Z3(w1, w2, wq)
                if abs(z) > best_abs:
                    best_abs = abs(z)
                    best = (k1, k2, q, s1, s2, sq)
    if best is None or best_abs < 1e-8:
        raise RuntimeError("no nondegenerate resonant helical triad found")
    return best


def main() -> None:
    n = 16
    nu = 0.19
    kx, ky, kz, k2grid = modes(n)
    K = (kx, ky, kz)
    u = random_real_div_free_field(n, 2026081208)
    A = grad_vec(u, K)
    omega = curl(u, K)
    adv = advect(u, omega, K)
    stretch = matvec(A, omega)
    lap = lap_vec(omega, k2grid)

    what = fft_vec(omega)
    advhat = fft_vec(-adv)
    stretchhat = fft_vec(stretch)
    vischat = fft_vec(nu * lap)
    dthat = advhat + stretchhat + vischat

    k1, k2, q, s1, s2, sq = find_triad(what, n)

    roles = []
    for k, s in ((k1, s1), (k2, s2), (q, sq)):
        w = hproj(coeff(what, k, n), k, s)
        da = hproj(coeff(advhat, k, n), k, s)
        ds = hproj(coeff(stretchhat, k, n), k, s)
        dv = hproj(coeff(vischat, k, n), k, s)
        dt = hproj(coeff(dthat, k, n), k, s)
        roles.append((w, da, ds, dv, dt))

    w1, w2, wq = (r[0] for r in roles)
    z = Z3(w1, w2, wq)
    assert abs(z) > 1e-8

    zd_adv = Zdot(w1, w2, wq, roles[0][1], roles[1][1], roles[2][1])
    zd_strain = Zdot(w1, w2, wq, roles[0][2], roles[1][2], roles[2][2])
    zd_visc = Zdot(w1, w2, wq, roles[0][3], roles[1][3], roles[2][3])
    zd_total = Zdot(w1, w2, wq, roles[0][4], roles[1][4], roles[2][4])
    zd_sum = zd_adv + zd_strain + zd_visc

    zscale = max(1.0, abs(zd_total), abs(zd_sum))
    sum_res = abs(zd_total - zd_sum) / zscale

    rates = {
        "total": float(np.imag(zd_total / z)),
        "transport": float(np.imag(zd_adv / z)),
        "stretching": float(np.imag(zd_strain / z)),
        "viscosity": float(np.imag(zd_visc / z)),
    }
    phase_sum_res = abs(rates["total"] - rates["transport"] - rates["stretching"] - rates["viscosity"])

    # For an exact Fourier mode, viscosity is scalar real damping.  It cannot rotate Z.
    ksq = sum(x * x for x in k1) + sum(x * x for x in k2) + sum(x * x for x in q)
    visc_exact = -nu * ksq * z
    visc_res = abs(zd_visc - visc_exact) / max(1.0, abs(visc_exact), abs(zd_visc))

    # Recover the instantaneous signed helical edge work from the selected vorticity roles.
    u1 = (s1 / np.linalg.norm(k1)) * w1
    u2 = (s2 / np.linalg.norm(k2)) * w2
    uq = (sq / np.linalg.norm(q)) * wq
    work = edge_work(np.array(k1, float), u1, np.array(k2, float), u2, uq)

    assert sum_res < 2e-11
    assert phase_sum_res < 2e-11
    assert visc_res < 2e-11
    assert abs(rates["viscosity"]) < 2e-11
    assert abs(rates["transport"]) + abs(rates["stretching"]) > 1e-6

    print("selected resonant helical triad k1,k2,q / helicities:", k1, k2, q, (s1, s2, sq))
    print("complex interaction 3-form Z:", z, "phase:", float(np.angle(z)))
    print("instantaneous signed edge work:", work)
    print("Zdot physical-channel sum residual:", sum_res)
    print("phase-velocity channel sum residual:", phase_sum_res)
    print("phase velocities total/transport/stretching/viscosity:", rates)
    print("exact scalar viscous damping residual:", visc_res)
    print("conclusion: on a monochromatic resonant edge, viscosity damps interaction amplitude but cannot rotate its phase; phase rotation is nonlinear")


if __name__ == "__main__":
    main()
