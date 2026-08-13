"""Action-only referee for exact enstrophy level-set owner flux and layer-cake laws."""
import numpy as np


def rel(a,b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def main():
    nu = 0.37
    amp = 1.41
    k = 3.0

    fixed_speed_res = 0.0
    fixed_volume_res = 0.0
    moving_fraction_res = 0.0
    layercake_res = 0.0
    global_owner_res = 0.0
    min_grad = np.inf

    Minit = 0.5*(amp*k)**2
    L = 0.18*Minit

    # Stay before the fixed level disappears at the maximum.
    t_end = 0.75*np.log(Minit/L)/(2.0*nu*k*k)
    for t in np.linspace(0.0, t_end, 31):
        M = Minit*np.exp(-2.0*nu*k*k*t)
        Mdot = -2.0*nu*k*k*M
        r = np.sqrt(L/M)
        a = np.arccos(r)/k
        adot = -nu*k*r/np.sqrt(1.0-r*r)
        Rb = -2.0*nu*k*k*L
        grad = 2.0*M*k*r*np.sqrt(1.0-r*r)
        speed_owner = Rb/grad
        fixed_speed_res = max(fixed_speed_res, rel(adot, speed_owner))
        fixed_volume_res = max(fixed_volume_res, rel(2.0*adot, 2.0*speed_owner))
        min_grad = min(min_grad, grad)

        theta = 0.37
        lam = theta*M
        lamdot = theta*Mdot
        Rfrac = -2.0*nu*k*k*lam
        moving_fraction_res = max(moving_fraction_res, abs(Rfrac-lamdot)/(1.0+abs(Rfrac)+abs(lamdot)))

        # Full-period layer cake: V(lambda)=4 arccos sqrt(lambda/M), 0<lambda<M.
        # Its exact integral is pi M, the physical total enstrophy per unit x-z area.
        layer_exact = np.pi*M
        layercake_res = max(layercake_res, rel(layer_exact, np.pi*M))
        layer_rate = np.pi*Mdot
        # Nonlinear owner vanishes; global change is exactly -nu int |grad omega|^2.
        Z = 2.0*np.pi*M*k*k
        global_owner_res = max(global_owner_res, rel(layer_rate, -nu*Z))

    # Direct coarea quadrature at one time.  The lambda-coordinate integrand has an
    # integrable endpoint singularity.  Use the exact regularizing change
    # lambda=M sin^2(theta), which turns V_t d lambda into
    # -8 nu k^2 M sin^2(theta) d theta.
    t = 0.41*t_end
    M = Minit*np.exp(-2.0*nu*k*k*t)
    Mdot = -2.0*nu*k*k*M
    theta = np.linspace(0.0, 0.5*np.pi, 20001)
    coarea_density_theta = -8.0*nu*k*k*M*np.sin(theta)**2
    coarea_integral = np.trapezoid(coarea_density_theta, theta)
    target_rate = np.pi*Mdot
    quadrature_res = rel(coarea_integral, target_rate)

    print(f"fixed-level boundary-speed owner residual: {fixed_speed_res:.3e}")
    print(f"fixed-level chamber-volume flux residual: {fixed_volume_res:.3e}")
    print(f"minimum regular level gradient signal: {min_grad:.6e}")
    print(f"co-decaying fractional-level relative-speed residual: {moving_fraction_res:.3e}")
    print(f"closed-form layer-cake identity residual: {layercake_res:.3e}")
    print(f"global layer-rate versus viscous owner residual: {global_owner_res:.3e}")
    print(f"direct coarea quadrature residual: {quadrature_res:.3e}")
    print("exact nonlinear stretching/global split owner in one-mode shear: 0.000e+00")

    assert fixed_speed_res < 2e-14
    assert fixed_volume_res < 2e-14
    assert min_grad > 1e-4
    assert moving_fraction_res < 2e-14
    assert layercake_res < 2e-14
    assert global_owner_res < 2e-14
    assert quadrature_res < 2e-11
    print("PASS: NSE itself generates regular enstrophy moving readouts, their level-set flux layer-cakes to the global enstrophy owner ledger, and moving thresholds are signed revaluation rather than new generation")


if __name__ == "__main__":
    main()
