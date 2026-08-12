from __future__ import annotations

import numpy as np

from experiments.exp05_localized_flux_pde import (
    advect,
    curl,
    fft_vec,
    grad_vec,
    ifft_vec,
    lap_vec,
    matvec,
    modes,
    random_real_div_free_field,
    relerr,
)


def smooth_project(v: np.ndarray, m: np.ndarray) -> np.ndarray:
    return ifft_vec(fft_vec(v) * m[None, ...])


def main() -> None:
    n = 16
    nu = 0.13
    alpha = 1.1  # Ndot/N for the moving spectral radius.
    N0 = 2.35
    kx, ky, kz, k2 = modes(n)
    K = (kx, ky, kz)
    u = random_real_div_free_field(n, 2026081206)
    A = grad_vec(u, K)
    omega = curl(u, K)
    adv_full = advect(u, omega, K)
    stretch_full = matvec(A, omega)
    lap_full = lap_vec(omega, k2)
    dt_omega = -adv_full + stretch_full + nu * lap_full

    r4 = (k2 * k2) / (N0 ** 4)
    m = np.exp(-r4)
    mdot = 4.0 * alpha * r4 * m

    wi = smooth_project(omega, m)
    q_dtomega = smooth_project(dt_omega, m)
    q_adv = smooth_project(adv_full, m)
    q_stretch = smooth_project(stretch_full, m)
    q_lap = smooth_project(lap_full, m)
    time_face = smooth_project(omega, mdot)

    # Literal derivative of H^T Q(t) omega at H=I along the material trajectory.
    direct = -matvec(A, wi) + time_face + q_dtomega + advect(u, wi, K)

    interface = advect(u, wi, K) - q_adv
    strain_selection = q_stretch - matvec(A, wi)
    viscosity = nu * q_lap
    classified = time_face + interface + strain_selection + viscosity
    without_time_face = interface + strain_selection + viscosity

    exact_res = relerr(direct, classified)
    omitted_res = relerr(direct, without_time_face)
    missing_equals_face = relerr(direct - without_time_face, time_face)
    face_scale = float(np.max(np.abs(time_face)))
    direct_scale = float(np.max(np.abs(direct)))

    assert exact_res < 2e-11
    assert missing_equals_face < 2e-11
    assert omitted_res > 1e-5
    assert face_scale > 1e-6
    print("moving-cut identity residual with Qdot retained:", exact_res)
    print("residual when Qdot is deliberately omitted:", omitted_res)
    print("omitted residual ↔ literal time-face residual:", missing_equals_face)
    print("max |Qdot omega| / max |direct role derivative|:", face_scale / max(direct_scale, 1e-30))
    print("conclusion: a moving spectral observer has an exact time-face source; a static commutator is not exhaustive")


if __name__ == "__main__":
    main()
