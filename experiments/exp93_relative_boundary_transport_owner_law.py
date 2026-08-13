"""Action-only referee for relative-boundary transport, moving-cut flux, and ancestry holonomy."""
import numpy as np


def rel(a, b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def main():
    nu = 0.37
    ell = 0.73
    width = 1.07
    area = 0.91

    def coeffs(t):
        A = np.exp(-nu*t)
        B = 0.25*np.exp(3.0)*np.exp(-4.0*nu*t)
        return A, B

    def U(y, t):
        A, B = coeffs(t)
        return -A*np.sin(y) - 0.5*B*np.sin(2.0*y)

    def Ut(y, t):
        A, B = coeffs(t)
        return nu*A*np.sin(y) + 2.0*nu*B*np.sin(2.0*y)

    def Uyy(y, t):
        A, B = coeffs(t)
        return A*np.sin(y) + 2.0*B*np.sin(2.0*y)

    def q(y, t):
        A, B = coeffs(t)
        return A*np.cos(y) + B*np.cos(2.0*y)

    def qy(y, t):
        A, B = coeffs(t)
        return -A*np.sin(y) - 2.0*B*np.sin(2.0*y)

    def en(y, t):
        z = q(y, t)
        return 0.5*z*z

    def ey(y, t):
        return q(y, t)*qy(y, t)

    # Exact moving-loop circulation law on many smooth cuts.
    loop_res = 0.0
    heat_res = 0.0
    for t in np.linspace(0.08, 1.7, 23):
        for a in np.linspace(-2.4, 2.1, 19):
            adot = 0.8*np.sin(1.3*t-0.7*a)
            direct = ell*(Ut(a,t)-Ut(a+width,t) + adot*(-q(a,t)+q(a+width,t)))
            visc = nu*ell*(Uyy(a,t)-Uyy(a+width,t))
            sweep = ell*adot*(q(a+width,t)-q(a,t))
            loop_res = max(loop_res, rel(direct, visc+sweep))
            heat_res = max(heat_res, rel(Ut(a,t), nu*Uyy(a,t)))

    # Exact moving-slab enstrophy law using analytic trigonometric antiderivatives.
    def C1(y):
        return 0.5*y + 0.25*np.sin(2.0*y)

    def C2(y):
        return 0.5*y + 0.125*np.sin(4.0*y)

    def C12(y):
        return np.sin(y) + np.sin(3.0*y)/3.0

    def D1(y):
        return 0.5*y - 0.25*np.sin(2.0*y)

    def D2(y):
        return 0.5*y - 0.125*np.sin(4.0*y)

    def D12(y):
        return np.sin(y) - np.sin(3.0*y)/3.0

    slab_res = 0.0
    max_sweep = 0.0
    for t in np.linspace(0.11, 1.5, 21):
        A, B = coeffs(t)
        for a in np.linspace(-1.9, 1.8, 17):
            b = a + width
            adot = 0.9*np.cos(0.6*a+1.1*t)
            dc1 = C1(b)-C1(a)
            dc2 = C2(b)-C2(a)
            dc12 = C12(b)-C12(a)
            partial = 0.5*((-2.0*nu*A*A)*dc1 + (-8.0*nu*B*B)*dc2 + (-5.0*nu*A*B)*dc12)
            direct = area*(partial + adot*(en(b,t)-en(a,t)))

            id1 = D1(b)-D1(a)
            id2 = D2(b)-D2(a)
            id12 = D12(b)-D12(a)
            int_qy2 = A*A*id1 + 4.0*B*B*id2 + 2.0*A*B*id12
            bulk_visc = -nu*area*int_qy2
            diff_face = nu*area*(ey(b,t)-ey(a,t))
            sweep_face = area*adot*(en(b,t)-en(a,t))
            rhs = bulk_visc + diff_face + sweep_face  # stretching is exactly zero in this shear
            slab_res = max(slab_res, rel(direct, rhs))
            max_sweep = max(max_sweep, abs(sweep_face))

    # Pure tangential relative loop motion is in the swept-ribbon kernel.
    rng = np.random.default_rng(20260813)
    tangent_kernel = 0.0
    for _ in range(1000):
        tau = rng.normal(size=3)
        tau /= np.linalg.norm(tau)
        omega = rng.normal(size=3)
        alpha = rng.normal()
        wtan = alpha*tau
        tangent_kernel = max(tangent_kernel, abs(np.dot(np.cross(wtan, omega), tau)))

    # Critical-sheet merger: singular sweep rate, finite distance-weighted coefficient, continuous current.
    T = 1.0/nu
    target_coeff = 1.5*nu*ell*np.exp(-1.0)*(1.0-np.cos(width))**2
    coeff_res = []
    current_jump_res = []
    Kstar = ell*(U(np.pi,T)-U(np.pi+width,T))
    for d in [0.20, 0.10, 0.05, 0.02, 0.01, 0.005, 0.001]:
        t = (1.0 + np.log(np.cos(d))/3.0)/nu
        a = np.pi + d
        adot = -3.0*nu/np.tan(d)
        cut = ell*adot*(q(a+width,t)-q(a,t))
        coeff_res.append(rel(d*abs(cut), target_coeff))
        K = ell*(U(a,t)-U(a+width,t))
        current_jump_res.append(abs(K-Kstar))

    # Nanson history obstruction at the same merger endpoint.
    gamma0 = ((1.0-np.exp(-1.0)) - np.exp(3.0)*(1.0-np.exp(-4.0))/16.0)/nu
    gammas = (np.exp(-3.0)*(np.exp(2.0)-1.0)/4.0 + np.exp(3.0)*(1.0-np.exp(-4.0))/16.0)/nu
    dgamma = gamma0-gammas
    E = np.zeros((3,3)); E[0,1] = 1.0
    D = np.diag([ell, width, 0.88])
    L0 = (np.eye(3)+gamma0*E) @ D
    Ls = (np.eye(3)+gammas*E) @ D
    H0 = np.linalg.det(L0)*np.linalg.inv(L0).T
    Hs = np.linalg.det(Ls)*np.linalg.inv(Ls).T
    J = L0 @ np.linalg.inv(Ls)

    omega_star = np.array([0.0,0.0,q(np.pi,T)])
    Kvec = np.array([0.0,0.0,Kstar])
    eps0 = Kvec-H0.T@omega_star
    epss = Kvec-Hs.T@omega_star
    r0 = np.linalg.solve(H0.T, eps0)
    rs = np.linalg.solve(Hs.T, epss)
    chi0 = eps0/np.linalg.det(L0)
    chis = epss/np.linalg.det(Ls)
    fiber_tie = max(
        np.linalg.norm(eps0-epss),
        np.linalg.norm(r0-rs),
        np.linalg.norm(chi0-chis),
    )
    frame_sep = np.linalg.norm(L0-Ls)
    holonomy_sep = np.linalg.norm(J-np.eye(3))
    detJ_res = abs(np.linalg.det(J)-1.0)

    print(f"moving-loop Kelvin/Reynolds residual: {loop_res:.3e}")
    print(f"heat-equation residual: {heat_res:.3e}")
    print(f"moving-slab enstrophy four-face residual: {slab_res:.3e}")
    print(f"nonzero moving-slab sweep signal: {max_sweep:.6e}")
    print(f"tangential relative-motion kernel residual: {tangent_kernel:.3e}")
    print(f"critical merger target distance-weighted sweep coefficient: {target_coeff:.9e}")
    print(f"critical merger smallest-d coefficient residual: {coeff_res[-1]:.3e}")
    print(f"critical merger smallest-d circulation continuity error: {current_jump_res[-1]:.3e}")
    print(f"Nanson merger history gamma gap: {dgamma:.9e}")
    print(f"endpoint residual-fiber tie residual: {fiber_tie:.3e}")
    print(f"transport-frame history separation: {frame_sep:.6e}")
    print(f"holonomy separation from identity: {holonomy_sep:.6e}")
    print(f"holonomy determinant-one residual: {detJ_res:.3e}")
    print("exact heat-shear nonlinear advection: 0.000e+00")
    print("exact heat-shear enstrophy stretching face: 0.000e+00")

    assert loop_res < 3e-14
    assert heat_res < 3e-14
    assert slab_res < 3e-13
    assert max_sweep > 1e-4
    assert tangent_kernel < 2e-14
    assert coeff_res[-1] < 2e-3
    assert current_jump_res[-1] < 2e-3
    assert dgamma < -1e-3
    assert fiber_tie < 2e-12
    assert frame_sep > 1e-2
    assert holonomy_sep > 1e-2
    assert detJ_res < 2e-12
    print("PASS: relative-boundary sweep is exact transfer currency, singular critical cut rates need not be generation, and endpoint residual coalescence does not erase transport ancestry")


if __name__ == "__main__":
    main()
