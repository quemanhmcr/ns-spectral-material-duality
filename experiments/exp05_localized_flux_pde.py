from __future__ import annotations

import numpy as np


def modes(n: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    k = np.fft.fftfreq(n, d=1.0 / n)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    return kx, ky, kz, kx * kx + ky * ky + kz * kz


def project_div_free(k: np.ndarray, z: np.ndarray) -> np.ndarray:
    return z - k * (np.dot(k, z) / np.dot(k, k))


def random_real_div_free_field(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    uhat = np.zeros((3, n, n, n), dtype=complex)
    for a in range(-2, 3):
        for b in range(-2, 3):
            for c in range(-2, 3):
                if (a, b, c) == (0, 0, 0):
                    continue
                # One representative of each +/- pair.
                first = next(v for v in (a, b, c) if v != 0)
                if first < 0:
                    continue
                k = np.array([a, b, c], dtype=float)
                z = rng.normal(size=3) + 1j * rng.normal(size=3)
                z = 8.0 * project_div_free(k, z) / np.sqrt(np.dot(k, k))
                i = (a % n, b % n, c % n)
                j = ((-a) % n, (-b) % n, (-c) % n)
                uhat[:, i[0], i[1], i[2]] = z
                uhat[:, j[0], j[1], j[2]] = np.conjugate(z)
    return np.stack([np.fft.ifftn(uhat[r]).real for r in range(3)])


def fft_vec(v: np.ndarray) -> np.ndarray:
    return np.stack([np.fft.fftn(v[r]) for r in range(3)])


def ifft_vec(vhat: np.ndarray) -> np.ndarray:
    return np.stack([np.fft.ifftn(vhat[r]).real for r in range(3)])


def grad_vec(v: np.ndarray, K: tuple[np.ndarray, np.ndarray, np.ndarray]) -> np.ndarray:
    vh = fft_vec(v)
    out = np.empty((3, 3) + v.shape[1:], dtype=float)
    for a in range(3):
        for j in range(3):
            out[a, j] = np.fft.ifftn(1j * K[j] * vh[a]).real
    return out


def lap_vec(v: np.ndarray, k2: np.ndarray) -> np.ndarray:
    vh = fft_vec(v)
    return ifft_vec(-k2[None, ...] * vh)


def curl(v: np.ndarray, K: tuple[np.ndarray, np.ndarray, np.ndarray]) -> np.ndarray:
    g = grad_vec(v, K)
    return np.stack([g[2, 1] - g[1, 2], g[0, 2] - g[2, 0], g[1, 0] - g[0, 1]])


def advect(u: np.ndarray, v: np.ndarray, K: tuple[np.ndarray, np.ndarray, np.ndarray]) -> np.ndarray:
    gv = grad_vec(v, K)
    return np.einsum("j...,aj...->a...", u, gv)


def matvec(A: np.ndarray, v: np.ndarray) -> np.ndarray:
    return np.einsum("aj...,j...->a...", A, v)


def project(v: np.ndarray, mask: np.ndarray) -> np.ndarray:
    return ifft_vec(fft_vec(v) * mask[None, ...])


def role_masks(K: tuple[np.ndarray, np.ndarray, np.ndarray]) -> list[np.ndarray]:
    ax, ay, az = (np.abs(x) for x in K)
    nonzero = (ax + ay + az) > 0
    m1 = nonzero & (ax >= ay) & (ax >= az)
    m2 = nonzero & (~m1) & (ay >= az)
    m3 = nonzero & (~m1) & (~m2)
    assert np.all((m1.astype(int) + m2.astype(int) + m3.astype(int))[nonzero] == 1)
    return [m1, m2, m3]


def triple(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.einsum("a...,a...->...", c, np.cross(a, b, axisa=0, axisb=0, axisc=0))


def triple_derivative(phi: list[np.ndarray], R: list[np.ndarray]) -> np.ndarray:
    p1, p2, p3 = phi
    r1, r2, r3 = R
    return (
        triple(p1, p2, r3)
        + triple(r1, p2, p3)
        + triple(p1, r2, p3)
    )


def relerr(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.abs(a - b)) / max(1.0, float(np.max(np.abs(a))), float(np.max(np.abs(b)))))


def main() -> None:
    n = 16
    nu = 0.17
    kx, ky, kz, k2 = modes(n)
    K = (kx, ky, kz)
    u = random_real_div_free_field(n, 2026081205)
    A = grad_vec(u, K)
    omega = curl(u, K)
    adv_full = advect(u, omega, K)
    stretch_full = matvec(A, omega)
    lap_full = lap_vec(omega, k2)
    dt_omega = -adv_full + stretch_full + nu * lap_full

    phis: list[np.ndarray] = []
    R_direct: list[np.ndarray] = []
    R_transport: list[np.ndarray] = []
    R_strain: list[np.ndarray] = []
    R_visc: list[np.ndarray] = []
    worst_role = 0.0

    for mask in role_masks(K):
        wi = project(omega, mask)
        dt_wi = project(dt_omega, mask)
        material_wi = dt_wi + advect(u, wi, K)
        # H=I at the observation instant and D_t H^T = -A.
        direct = material_wi - matvec(A, wi)

        transport = advect(u, wi, K) - project(adv_full, mask)
        strain = project(stretch_full, mask) - matvec(A, wi)
        visc = nu * project(lap_full, mask)
        classified = transport + strain + visc

        worst_role = max(worst_role, relerr(direct, classified))
        phis.append(wi)
        R_direct.append(direct)
        R_transport.append(transport)
        R_strain.append(strain)
        R_visc.append(visc)

    d_direct = triple_derivative(phis, R_direct)
    d_transport = triple_derivative(phis, R_transport)
    d_strain = triple_derivative(phis, R_strain)
    d_visc = triple_derivative(phis, R_visc)
    d_sum = d_transport + d_strain + d_visc
    cubic_res = relerr(d_direct, d_sum)

    C = triple(phis[0], phis[1], phis[2])
    idx = np.unravel_index(np.argmax(np.abs(C)), C.shape)
    values = {
        "C": float(C[idx]),
        "dC": float(d_direct[idx]),
        "transport": float(d_transport[idx]),
        "strain_selection": float(d_strain[idx]),
        "viscosity": float(d_visc[idx]),
    }

    # Full Q=I Kelvin/Nanson specialization: commutators vanish, leaving viscosity only.
    full_direct = (dt_omega + adv_full) - matvec(A, omega)
    full_visc = nu * lap_full
    full_res = relerr(full_direct, full_visc)

    assert worst_role < 2e-11
    assert cubic_res < 2e-11
    assert full_res < 2e-11
    print("localized material-flux role identity worst residual:", worst_role)
    print("oriented cubic derivative classified-sum residual:", cubic_res)
    print("full Q=I Kelvin/Nanson specialization residual:", full_res)
    print("sample point with largest |oriented cubic flux|:", idx)
    print("C, dC, transport, strain-selection, viscosity:", values)
    print("conclusion: after common material stretching is removed, localized roles evolve only through interface transport, selection/strain mismatch, and viscosity")


if __name__ == "__main__":
    main()
