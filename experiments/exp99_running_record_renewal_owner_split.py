"""Action-only referee for running-record renewal core/sweep/norm splitting."""
import numpy as np


def rel(a, b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def abc_unit_tensors_at_max():
    s = np.sqrt(0.5)
    u = np.array([2.0*s, 2.0*s, 2.0*s])
    A = s*np.array([[0.0,-1.0,1.0],[1.0,0.0,-1.0],[-1.0,1.0,0.0]])
    Hu = np.zeros((3,3,3))
    Hu[0,1,1] = -s
    Hu[0,2,2] = -s
    Hu[1,0,0] = -s
    Hu[1,2,2] = -s
    Hu[2,0,0] = -s
    Hu[2,1,1] = -s
    S = 0.5*(A+A.T)
    He = A.T@A + sum(u[i]*Hu[i] for i in range(3))
    Hp = -He
    xi = u/np.linalg.norm(u)
    grad_alpha = np.zeros(3)
    for k in range(3):
        dA = Hu[:,:,k]
        dS = 0.5*(dA+dA.T)
        grad_alpha[k] = xi@dS@xi
    return u, S, He, Hp, xi, grad_alpha


def main():
    nu = 0.37

    # Constant-strain affine: positive local pressure face is exactly paid by record normalization.
    a0 = 0.23
    om0 = 0.81
    const_split_res = 0.0
    const_norm_max = -np.inf
    for t in np.linspace(0.0, 1.7, 31):
        om = om0*np.exp(2.0*a0*t)
        sigma = np.sqrt(2.0)*a0/om
        rho_rec = 2.0*sigma
        core = sigma*sigma
        norm = -0.5*sigma*rho_rec
        total = core+norm
        const_split_res = max(const_split_res, abs(total))
        const_norm_max = max(const_norm_max, norm)

    # Accelerating affine: local core exceeds the negative normalization face.
    T = 3.0
    b = 0.71
    accel_split_res = 0.0
    accel_core_min = np.inf
    accel_norm_max = -np.inf
    for t in np.linspace(0.0, 2.7, 55):
        s = T-t
        a = 1.0/(2.0*s)
        adot = 1.0/(2.0*s*s)
        om = b/s
        sigma = np.sqrt(2.0)*a/om
        rho_rec = 2.0*sigma
        core = (adot+2.0*a*a)/(om*om)
        norm = -0.5*sigma*rho_rec
        total = core+norm
        target = adot/(om*om)
        accel_split_res = max(accel_split_res, rel(total, target))
        accel_core_min = min(accel_core_min, core)
        accel_norm_max = max(accel_norm_max, norm)

    # Periodic ABC: suppressive local pressure face + positive geometry harvesting.
    u0, S0, He0, Hp0, xi0, grad_alpha0 = abc_unit_tensors_at_max()
    abc_tensor_res = max(
        np.linalg.norm(S0),
        rel(np.linalg.det(He0), -0.5),
        rel(xi0@Hp0@xi0, 2.0),
        rel(u0@grad_alpha0, -2.0),
    )
    abc_split_res = 0.0
    abc_morse_res = 0.0
    abc_sweep_min = np.inf
    abc_cauchy_gap = np.inf
    Mrec = 3.0
    for t in np.linspace(0.0, 1.4, 29):
        amp = np.exp(-nu*t)
        u = amp*u0
        Hp = amp*amp*Hp0
        He = amp*amp*He0
        G = -He
        grad_alpha = amp*grad_alpha0
        grad_R = amp**3 * He0@u0
        w = np.linalg.solve(G, grad_R)

        core = -(xi0@Hp@xi0)/Mrec
        sweep = w@grad_alpha/Mrec
        target_mag = 2.0*amp*amp/3.0
        abc_split_res = max(
            abc_split_res,
            rel(core, -target_mag),
            rel(sweep, target_mag),
            abs(core+sweep),
            np.linalg.norm(w+u)/(1.0+np.linalg.norm(w)+np.linalg.norm(u)),
        )
        abc_sweep_min = min(abc_sweep_min, sweep)

        Ghat = G/(Mrec**1.5)
        gahat = grad_alpha/(Mrec**0.75)
        gRhat = grad_R/(Mrec**1.75)
        what = np.linalg.solve(Ghat, gRhat)
        metric_sweep = gahat@what
        abc_morse_res = max(
            abc_morse_res,
            rel(metric_sweep, sweep),
            np.linalg.norm(what-w/(Mrec**0.25))/(1.0+np.linalg.norm(what)+np.linalg.norm(w/(Mrec**0.25))),
        )
        invGhat = np.linalg.inv(Ghat)
        bound = np.sqrt(gahat@invGhat@gahat)*np.sqrt(gRhat@invGhat@gRhat)
        abc_cauchy_gap = min(abc_cauchy_gap, bound-abs(sweep))

    # Exact x-shear geometry: alpha is identically zero even when a critical speed is huge.
    d = 1.0e-7
    critical_speed = 3.0*nu/d
    Uy = 2.7
    S_shear = np.array([[0.0,0.5*Uy,0.0],[0.5*Uy,0.0,0.0],[0.0,0.0,0.0]])
    xi = np.array([0.0,0.0,1.0])
    alpha = xi@S_shear@xi
    grad_alpha = np.zeros(3)
    sweep_fast = np.array([0.0, critical_speed, 0.0])@grad_alpha

    print(f"constant-affine running-record split residual: {const_split_res:.3e}")
    print(f"constant-affine largest normalization face: {const_norm_max:.6e}")
    print(f"accelerating-affine running-record split residual: {accel_split_res:.3e}")
    print(f"accelerating-affine minimum positive core face: {accel_core_min:.6e}")
    print(f"accelerating-affine largest normalization face: {accel_norm_max:.6e}")
    print(f"ABC tensor/pressure/alpha-gradient residual: {abc_tensor_res:.3e}")
    print(f"ABC core-sweep cancellation residual: {abc_split_res:.3e}")
    print(f"ABC inverse-Morse sweep residual: {abc_morse_res:.3e}")
    print(f"ABC minimum positive sweep signal: {abc_sweep_min:.6e}")
    print(f"ABC minimum Cauchy bound gap: {abc_cauchy_gap:.3e}")
    print(f"singular heat-shear critical-speed signal: {critical_speed:.6e}")
    print(f"x-shear alpha / sweep residual: {abs(alpha):.3e} / {abs(sweep_fast):.3e}")

    assert const_split_res < 2e-14
    assert const_norm_max < 0.0
    assert accel_split_res < 3e-14
    assert accel_core_min > 1e-2
    assert accel_norm_max < 0.0
    assert abc_tensor_res < 3e-14
    assert abc_split_res < 4e-14
    assert abc_morse_res < 4e-14
    assert abc_sweep_min > 1e-2
    assert abc_cauchy_gap > -3e-14
    assert critical_speed > 1e6
    assert abs(alpha) < 2e-14
    assert abs(sweep_fast) < 2e-14
    print("PASS: running-record normalization never creates positive renewal; exact NSE separates local core renewal from geometry harvesting, and singular critical speed alone has zero harvesting")


if __name__ == "__main__":
    main()
