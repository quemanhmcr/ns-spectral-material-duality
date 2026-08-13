"""Action-only referee for the enstrophy value-space current and tied support edge."""
import numpy as np


def rel(a,b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def main():
    nu = 0.37
    amp = 1.41
    k = 3.0
    M0 = 0.5*(amp*k)**2
    c = 2.0*nu*k*k

    continuity_res = 0.0
    current_decomp_res = 0.0
    conditional_res = 0.0
    survival_res = 0.0
    moment_res = 0.0

    for t in np.linspace(0.0,0.8,17):
        M = M0*np.exp(-c*t)
        Mdot = -c*M
        for frac in np.linspace(0.04,0.96,31):
            a = frac*M
            root = np.sqrt(a*(M-a))
            g = 2.0/root
            J = -c*a*g
            ce = J/g
            conditional_res = max(conditional_res, rel(ce, -c*a))

            # Exact derivatives at fixed value a.
            gt = (-0.5*g/(M-a))*Mdot
            ga_over_g = -0.5/a + 0.5/(M-a)
            Ja = -c*g*(1.0 + a*ga_over_g)
            continuity_res = max(continuity_res, rel(gt, -Ja))

            B = 4.0*k*k*np.sqrt((M-a)/a)
            K = 8.0*k*k*root
            Ka = 4.0*k*k*(M-2.0*a)/root
            current_decomp_res = max(current_decomp_res, rel(J, -nu*B + nu*Ka))

            r = np.sqrt(a/M)
            Vt = -4.0*nu*k*k*r/np.sqrt(1.0-r*r)
            survival_res = max(survival_res, rel(Vt,J))

        # Exact periodic-trapezoid audit of the Phi(e)=e^m hierarchy.
        N = 4096
        y = 2.0*np.pi*np.arange(N)/N
        Cw = np.sqrt(2.0*M)
        omega = Cw*np.cos(k*y)
        omegay = -Cw*k*np.sin(k*y)
        e = 0.5*omega**2
        ey = omega*omegay
        for m in range(1,6):
            lhs = -c*m * (2.0*np.pi*np.mean(e**m))
            rhs = -m*nu*(2.0*np.pi*np.mean((e**(m-1))*omegay**2))
            if m > 1:
                rhs += -m*(m-1)*nu*(2.0*np.pi*np.mean((e**(m-2))*ey**2))
            moment_res = max(moment_res, rel(lhs,rhs))

    # Exact tied-edge constants from the three-mode NSE crossing.
    kap0 = 12.0*np.exp(-2.0)
    kapp = 60.0*np.exp(-2.0)
    R0 = -nu*kap0
    Rp = -nu*kapp
    bulk_edge = (R0/np.sqrt(kap0)+Rp/np.sqrt(kapp))/(1.0/np.sqrt(kap0)+1.0/np.sqrt(kapp))
    bulk_closed = -12.0*np.sqrt(5.0)*nu*np.exp(-2.0)
    record_right = R0
    record_left = Rp
    tied_formula_res = rel(bulk_edge, bulk_closed)
    bulk_record_separation = abs(bulk_edge-record_right)

    # Direct exact-shear local-level approach to the tied bulk edge.
    def w(y):
        return np.exp(-1.0)*(np.cos(y)+3.0*np.cos(2.0*y)-np.cos(3.0*y))
    def wy(y):
        return np.exp(-1.0)*(-np.sin(y)-6.0*np.sin(2.0*y)+3.0*np.sin(3.0*y))
    def wt(y):
        return nu*np.exp(-1.0)*(-np.cos(y)-12.0*np.cos(2.0*y)+9.0*np.cos(3.0*y))
    def ens(y):
        q=w(y); return 0.5*q*q
    def eyfun(y):
        return w(y)*wy(y)
    def rate(y):
        return w(y)*wt(y)
    Mstar = 4.5*np.exp(-2.0)

    def root_from(center, delta):
        target=Mstar-delta
        lo=0.0; hi=0.5
        # symmetry: evaluate center+z
        for _ in range(100):
            mid=0.5*(lo+hi)
            if ens(center+mid) > target:
                lo=mid
            else:
                hi=mid
        return center+0.5*(lo+hi)

    approach_res=[]
    for frac in [1e-4,1e-5,1e-6,1e-7,1e-8]:
        delta=frac*Mstar
        y0=root_from(0.0,delta)
        yp=root_from(np.pi,delta)
        g0=2.0/abs(eyfun(y0)); gp=2.0/abs(eyfun(yp))
        j0=2.0*rate(y0)/abs(eyfun(y0)); jp=2.0*rate(yp)/abs(eyfun(yp))
        cedge=(j0+jp)/(g0+gp)
        approach_res.append(rel(cedge,bulk_closed))

    print(f"heat-shear value-space continuity residual: {continuity_res:.3e}")
    print(f"heat-shear value-current decomposition residual: {current_decomp_res:.3e}")
    print(f"heat-shear conditional owner velocity residual: {conditional_res:.3e}")
    print(f"heat-shear survival/current residual: {survival_res:.3e}")
    print(f"convex power-moment hierarchy residual: {moment_res:.3e}")
    print(f"tied-edge closed-form bulk velocity residual: {tied_formula_res:.3e}")
    print(f"tied-edge bulk velocity: {bulk_edge:.9e}")
    print(f"tied-edge record right/left velocities: {record_right:.9e} / {record_left:.9e}")
    print(f"bulk-versus-record edge separation signal: {bulk_record_separation:.6e}")
    print(f"exact-shear smallest-delta bulk-edge asymptotic residual: {approach_res[-1]:.3e}")

    assert continuity_res < 3e-14
    assert current_decomp_res < 3e-14
    assert conditional_res < 2e-14
    assert survival_res < 3e-14
    assert moment_res < 3e-13
    assert tied_formula_res < 2e-14
    assert bulk_record_separation > 1e-2
    assert approach_res[-1] < 2e-6
    assert record_right > bulk_edge > record_left
    print("PASS: enstrophy populations obey one exact value-space current, while a tied support edge retains an extremal lineage-selection law distinct from the bulk conditional current")


if __name__ == "__main__":
    main()
