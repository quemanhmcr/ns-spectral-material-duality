"""Action-only referee for support-edge compatibility and Riccati owner renewal."""
import numpy as np


def rel(a, b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def affine_matrix(a, om):
    return np.array([[-a, -om, 0.0], [om, -a, 0.0], [0.0, 0.0, 2.0*a]])


def main():
    nu = 0.37

    # ------------------------------------------------------------
    # 1. Exact four-mode periodic heat-shear global-max crossing.
    # ------------------------------------------------------------
    y = np.linspace(-np.pi, np.pi, 200001)
    c = np.cos(y)
    q = 16.0*c**4 - 4.0*c**3 - 8.0*c**2 + 4.0*c - 2.0
    e = 0.5*q*q
    global_max_res = rel(np.max(e), 18.0)
    interior_excess = max(0.0, np.max(e[1:-1])-18.0)

    R0 = -240.0*nu
    Rp = -336.0*nu
    Dright = max(R0, Rp)
    Dleft = min(R0, Rp)
    right_defects = np.array([R0-Dright, Rp-Dright])
    left_defects = np.array([R0-Dleft, Rp-Dleft])
    right_defect_res = max(rel(right_defects[0], 0.0), rel(right_defects[1], -96.0*nu))
    left_defect_res = max(rel(left_defects[0], 96.0*nu), rel(left_defects[1], 0.0))

    # ------------------------------------------------------------
    # 2. Constant-strain affine strain-spin: N=0 and exact saturation
    #    of the no-renewal intrinsic-time bound.
    # ------------------------------------------------------------
    a0 = 0.23
    om0 = 0.81
    const_matrix_res = 0.0
    const_alpha_res = 0.0
    const_riccati_res = 0.0
    const_renewal_res = 0.0
    const_bound_res = 0.0
    for t in np.linspace(0.0, 2.0, 41):
        om = om0*np.exp(2.0*a0*t)
        omdot = 2.0*a0*om
        A = affine_matrix(a0, om)
        Ap = np.array([[0.0, -omdot, 0.0], [omdot, 0.0, 0.0], [0.0, 0.0, 0.0]])
        B = Ap + A@A
        const_matrix_res = max(const_matrix_res, np.linalg.norm(B-B.T)/(1.0+np.linalg.norm(B)))

        M = 2.0*om*om
        sqM = np.sqrt(M)
        sigma = np.sqrt(2.0)*a0/om
        rho = 4.0*a0/sqM
        delta = 0.0
        const_renewal_res = max(const_renewal_res, rel(rho, 2.0*sigma-delta))

        # Exact alpha material law.  Hp=-(A'+A^2), xi=e_z.
        Hpzz = -B[2,2]
        alpha = 2.0*a0
        alpha_dot = 0.0
        rhs_alpha = (2.0*a0)**2 - 2.0*alpha**2 - Hpzz
        const_alpha_res = max(const_alpha_res, rel(alpha_dot, rhs_alpha))

        # Normalized Riccati law: sigma_tau=-sigma^2 and N=0.
        sigma_t = -2.0*a0*sigma
        sigma_tau = sigma_t/sqM
        renewal = sigma_tau + sigma*sigma
        const_riccati_res = max(const_riccati_res, rel(sigma_tau, -sigma*sigma))
        const_renewal_res = max(const_renewal_res, abs(renewal))

        tau = np.sqrt(2.0)*om0*(np.exp(2.0*a0*t)-1.0)/(2.0*a0)
        sigma_init = np.sqrt(2.0)*a0/om0
        M_bound = 2.0*om0*om0*(1.0+sigma_init*tau)**2
        const_bound_res = max(const_bound_res, rel(M, M_bound))

    # ------------------------------------------------------------
    # 3. Accelerating affine strain-spin: exact positive renewal and
    #    finite physical-time blow-up calibration.
    # ------------------------------------------------------------
    T = 3.0
    b = 0.71
    accel_matrix_res = 0.0
    accel_alpha_res = 0.0
    accel_riccati_res = 0.0
    accel_renewal_res = 0.0
    accel_blowup_res = 0.0
    accel_sigma_const = []
    for t in np.linspace(0.0, 2.7, 55):
        s = T-t
        a = 1.0/(2.0*s)
        adot = 1.0/(2.0*s*s)
        om = b/s
        omdot = b/(s*s)
        A = affine_matrix(a, om)
        Ap = np.array([
            [-adot, -omdot, 0.0],
            [omdot, -adot, 0.0],
            [0.0, 0.0, 2.0*adot],
        ])
        B = Ap + A@A
        accel_matrix_res = max(accel_matrix_res, np.linalg.norm(B-B.T)/(1.0+np.linalg.norm(B)))

        M = 2.0*om*om
        sqM = np.sqrt(M)
        sigma = np.sqrt(2.0)*a/om
        rho = 4.0*a/sqM
        delta = 0.0
        accel_sigma_const.append(sigma)

        Hpzz = -B[2,2]
        alpha = 2.0*a
        alpha_dot = 2.0*adot
        rhs_alpha = (2.0*a)**2 - 2.0*alpha**2 - Hpzz
        accel_alpha_res = max(accel_alpha_res, rel(alpha_dot, rhs_alpha))

        renewal = adot/(om*om)
        target_renewal = sigma*sigma
        accel_renewal_res = max(
            accel_renewal_res,
            rel(renewal, target_renewal),
            rel(rho, 2.0*sigma-delta),
        )
        sigma_t = 0.0
        sigma_tau = sigma_t/sqM
        accel_riccati_res = max(accel_riccati_res, rel(sigma_tau, -sigma*sigma+renewal))
        accel_blowup_res = max(accel_blowup_res, rel(M*s*s, 2.0*b*b))

    accel_sigma_variation = max(accel_sigma_const)-min(accel_sigma_const)

    print(f"four-mode global-max residual: {global_max_res:.3e}")
    print(f"four-mode sampled interior excess above M=18: {interior_excess:.3e}")
    print(f"right support-edge defect residual: {right_defect_res:.3e}")
    print(f"left support-edge defect residual: {left_defect_res:.3e}")
    print(f"constant-affine NSE symmetry residual: {const_matrix_res:.3e}")
    print(f"constant-affine specific-stretching law residual: {const_alpha_res:.3e}")
    print(f"constant-affine Riccati residual: {const_riccati_res:.3e}")
    print(f"constant-affine zero-renewal residual: {const_renewal_res:.3e}")
    print(f"constant-affine no-renewal bound saturation residual: {const_bound_res:.3e}")
    print(f"accelerating-affine NSE symmetry residual: {accel_matrix_res:.3e}")
    print(f"accelerating-affine specific-stretching law residual: {accel_alpha_res:.3e}")
    print(f"accelerating-affine positive-renewal residual: {accel_renewal_res:.3e}")
    print(f"accelerating-affine Riccati residual: {accel_riccati_res:.3e}")
    print(f"accelerating-affine M(T-t)^2 residual: {accel_blowup_res:.3e}")
    print(f"accelerating-affine sigma variation: {accel_sigma_variation:.3e}")
    print(f"accelerating-affine renewal signal: {1.0/(2.0*b*b):.6e}")

    assert global_max_res < 3e-13
    assert interior_excess < 3e-10
    assert right_defect_res < 2e-14
    assert left_defect_res < 2e-14
    assert const_matrix_res < 2e-14
    assert const_alpha_res < 2e-14
    assert const_riccati_res < 2e-14
    assert const_renewal_res < 2e-14
    assert const_bound_res < 3e-14
    assert accel_matrix_res < 3e-14
    assert accel_alpha_res < 3e-14
    assert accel_renewal_res < 3e-14
    assert accel_riccati_res < 3e-14
    assert accel_blowup_res < 3e-14
    assert accel_sigma_variation < 3e-14
    assert 1.0/(2.0*b*b) > 0.1
    print("PASS: the support edge self-selects by zero compatibility defect, while finite-time affine amplification requires positive scale-free renewal beyond intrinsic Riccati dilution")


if __name__ == "__main__":
    main()
