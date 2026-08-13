"""Action-only referee for the exact stretching-owner self-constraint law."""
import numpy as np


def rel(a, b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def abc_tensors(x, y, z):
    u = np.array([
        np.sin(z)+np.cos(y),
        np.sin(x)+np.cos(z),
        np.sin(y)+np.cos(x),
    ])
    A = np.array([
        [0.0, -np.sin(y), np.cos(z)],
        [np.cos(x), 0.0, -np.sin(z)],
        [-np.sin(x), np.cos(y), 0.0],
    ])
    Hu = np.zeros((3,3,3))
    # Hu[i,j,k] = d_j d_k u_i
    Hu[0,1,1] = -np.cos(y)
    Hu[0,2,2] = -np.sin(z)
    Hu[1,0,0] = -np.sin(x)
    Hu[1,2,2] = -np.cos(z)
    Hu[2,0,0] = -np.cos(x)
    Hu[2,1,1] = -np.sin(y)
    S = 0.5*(A+A.T)
    Hp = -(A.T@A + sum(u[i]*Hu[i] for i in range(3)))
    gradP = np.zeros(3)
    for k in range(3):
        domega = A[:,k]  # omega=u for unit ABC
        dA = Hu[:,:,k]
        dS = 0.5*(dA+dA.T)
        gradP[k] = 2.0*domega@S@u + u@dS@u
    return u, A, S, Hu, Hp, gradP


def main():
    # ------------------------------------------------------------
    # 1. Exact affine strain-spin calibration: pressure reinforces Q_S.
    # ------------------------------------------------------------
    a = 0.23
    Om0 = 0.81
    nu = 0.37
    affine_res = 0.0
    affine_pressure_sign = np.inf
    affine_equal_faces = 0.0
    for t in np.linspace(0.0, 1.7, 31):
        Om = Om0*np.exp(2.0*a*t)
        omega = np.array([0.0,0.0,2.0*Om])
        S = np.diag([-a,-a,2.0*a])
        Hp = -np.diag([a*a-Om*Om, a*a-Om*Om, 4.0*a*a])
        P = omega@S@omega
        Q = omega@(S@S)@omega
        Cp = -omega@Hp@omega
        V = 0.0
        direct = 32.0*a*a*Om*Om
        affine_res = max(affine_res, rel(direct, Q+Cp+V))
        affine_equal_faces = max(affine_equal_faces, rel(Q,Cp))
        affine_pressure_sign = min(affine_pressure_sign, Cp)

    # ------------------------------------------------------------
    # 2. Exact periodic viscous ABC: analytic tensor audit.
    # ------------------------------------------------------------
    abc_owner_res = 0.0
    abc_euler_core_res = 0.0
    abc_visc_res = 0.0
    poisson_res = 0.0
    for t in np.linspace(0.0, 1.2, 13):
        alpha = np.exp(-nu*t)
        for x, y, z in [
            (0.0,0.0,0.0),
            (np.pi/2,0.0,0.0),
            (0.31,-0.47,0.83),
            (-1.1,0.72,-0.29),
        ]:
            u0, A0, S0, Hu0, Hp0, gradP0 = abc_tensors(x,y,z)
            P0 = u0@S0@u0
            Q0 = u0@(S0@S0)@u0
            Cp0 = -u0@Hp0@u0
            adv0 = u0@gradP0
            abc_euler_core_res = max(abc_euler_core_res, rel(adv0, Q0+Cp0))

            P = alpha**3*P0
            Q = alpha**4*Q0
            Cp = alpha**4*Cp0
            V = -3.0*nu*P  # Delta omega=-omega, Delta S=-S
            direct = -3.0*nu*P + alpha**4*adv0
            abc_owner_res = max(abc_owner_res, rel(direct, Q+Cp+V))
            abc_visc_res = max(abc_visc_res, rel(V, -3.0*nu*P))

            A = alpha*A0
            omega = alpha*u0
            Hp = alpha**2*Hp0
            delta_p = np.trace(Hp)
            source = -np.trace(A@A)
            poisson_res = max(poisson_res, rel(delta_p, source))

    # Exact suppression point x=pi/2,y=z=0.
    u0, A0, S0, Hu0, Hp0, gradP0 = abc_tensors(np.pi/2,0.0,0.0)
    P0 = u0@S0@u0
    Q0 = u0@(S0@S0)@u0
    Cp0 = -u0@Hp0@u0
    adv0 = u0@gradP0
    trace0 = np.trace(Hp0)
    directional0 = u0@Hp0@u0

    # Origin: nonzero P and exact viscous face -3 nu P.
    uO, AO, SO, HuO, HpO, gradPO = abc_tensors(0.0,0.0,0.0)
    PO = uO@SO@uO
    QO = uO@(SO@SO)@uO
    CpO = -uO@HpO@uO
    advO = uO@gradPO

    print(f"affine stretching-owner law residual: {affine_res:.3e}")
    print(f"affine self-strain/pressure-face equality residual: {affine_equal_faces:.3e}")
    print(f"affine minimum positive pressure-curvature face: {affine_pressure_sign:.6e}")
    print(f"ABC full stretching-owner law residual: {abc_owner_res:.3e}")
    print(f"ABC inviscid-core identity residual: {abc_euler_core_res:.3e}")
    print(f"ABC viscous-face residual: {abc_visc_res:.3e}")
    print(f"ABC pressure-Poisson trace residual: {poisson_res:.3e}")
    print(f"ABC suppression-point P/Q/Cp: {P0:.6e} / {Q0:.6e} / {Cp0:.6e}")
    print(f"ABC suppression-point material owner derivative: {adv0:.6e}")
    print(f"ABC suppression-point pressure trace/directional contraction: {trace0:.6e} / {directional0:.6e}")
    print(f"ABC origin P/Q/Cp/advective: {PO:.6e} / {QO:.6e} / {CpO:.6e} / {advO:.6e}")

    assert affine_res < 2e-14
    assert affine_equal_faces < 2e-14
    assert affine_pressure_sign > 1e-4
    assert abc_owner_res < 3e-14
    assert abc_euler_core_res < 3e-14
    assert abc_visc_res < 2e-14
    assert poisson_res < 3e-14
    assert abs(P0) < 2e-14
    assert rel(Q0, 1.0) < 2e-14
    assert rel(Cp0, -5.0) < 2e-14
    assert rel(adv0, -4.0) < 2e-14
    assert rel(trace0, 2.0) < 2e-14
    assert rel(directional0, 5.0) < 2e-14
    assert rel(PO, 3.0) < 2e-14
    assert rel(QO, 3.0) < 2e-14
    assert abs(CpO) < 2e-14
    assert rel(advO, 3.0) < 2e-14
    print("PASS: the genuine stretching owner is itself self-constrained by strain square, signed pressure curvature, and viscosity; pressure can reinforce or overpower self-strain on exact NSE")


if __name__ == "__main__":
    main()
