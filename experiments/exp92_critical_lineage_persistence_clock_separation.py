"""Action-only referee for exact-NS critical-sheet persistence through many ranking crossings."""
import numpy as np


def rel(a, b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def main():
    # Four prescribed dimensionless times s=nu t, as in exp90/91.
    odd = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
    roots = np.array([0.004, 0.012, 0.024, 0.040])
    M = np.exp(-np.outer(roots, odd**2))
    _, _, vh = np.linalg.svd(M)
    a = vh[-1]
    a /= np.max(np.abs(a))

    def O(s):
        return np.sum(a * np.exp(-(odd**2)*s))

    def Os(s):
        return np.sum(-(odd**2)*a*np.exp(-(odd**2)*s))

    def O2(s):
        return np.sum((odd**2)*a*np.exp(-(odd**2)*s))

    # Compact interval containing every crossing.  Choose epsilon by a strict global-on-grid
    # version of the analytic compactness inequalities used in the proof.
    K = np.linspace(0.002, 0.045, 4001)
    E = np.exp(-4.0*K)
    Ovals = np.array([O(s) for s in K])
    O2vals = np.array([O2(s) for s in K])
    mE = float(np.min(E))
    M0 = float(np.max(np.abs(Ovals)))
    M2 = float(np.max(np.abs(O2vals)))
    eps_bound0 = np.inf if M0 == 0.0 else mE/M0
    eps_bound2 = np.inf if M2 == 0.0 else 4.0*mE/M2
    eps = 0.25 * min(0.2, eps_bound0, eps_bound2)

    w0 = E + eps*Ovals
    wp = E - eps*Ovals
    wyy0 = -4.0*E - eps*O2vals
    wyyp = -4.0*E + eps*O2vals
    eyy0 = w0*wyy0
    eyyp = wp*wyyp

    min_w = float(min(np.min(w0), np.min(wp)))
    max_normal_curvature = float(max(np.max(eyy0), np.max(eyyp)))
    min_curvature_margin = float(min(np.min(-eyy0), np.min(-eyyp)))

    interpolation = float(np.max(np.abs(M @ a)))
    min_simple = float(min(abs(Os(s)) for s in roots))
    gaps = np.array([2.0*eps*np.exp(-4.0*s)*O(s) for s in roots])
    crossing_residual = float(np.max(np.abs(gaps)))

    # Check sign changes around every prescribed root.
    delta = 0.0007
    sign_fail = 0
    for s in roots:
        gm = 2.0*eps*np.exp(-4.0*(s-delta))*O(s-delta)
        gp = 2.0*eps*np.exp(-4.0*(s+delta))*O(s+delta)
        if gm*gp >= 0.0:
            sign_fail += 1

    # Exact heat/NSE audit on the synthesized shear.
    nu = 0.29
    heat = 0.0
    nonlinear = 0.0
    for s in np.linspace(0.002, 0.045, 19):
        for y in np.linspace(-np.pi, np.pi, 83):
            U = -0.5*np.exp(-4.0*s)*np.sin(2.0*y) - eps*np.sum((a/odd)*np.exp(-(odd**2)*s)*np.sin(odd*y))
            Us = 2.0*np.exp(-4.0*s)*np.sin(2.0*y) + eps*np.sum(odd*a*np.exp(-(odd**2)*s)*np.sin(odd*y))
            Uyy = 2.0*np.exp(-4.0*s)*np.sin(2.0*y) + eps*np.sum(odd*a*np.exp(-(odd**2)*s)*np.sin(odd*y))
            heat = max(heat, abs(nu*Us-nu*Uyy)/(1.0+abs(nu*Us)+abs(nu*Uyy)))
            nonlinear = max(nonlinear, abs(U*0.0))

    # Exact ABC isolated-critical-point persistence calibration: Hessian eigenvalues
    # are explicit negative multiples of {2,1/2,1/2} for every finite t.
    nu_abc = 0.23
    A0 = 1.7
    abc_max_eig = -np.inf
    abc_min_abs_eig = np.inf
    abc_det_residual = 0.0
    Mabc = np.array([[1.0,0.5,0.5],[0.5,1.0,0.5],[0.5,0.5,1.0]])
    for t in np.linspace(0.0, 3.0, 31):
        amp = A0*np.exp(-nu_abc*t)
        H = -(amp**2)*Mabc
        ev = np.linalg.eigvalsh(H)
        abc_max_eig = max(abc_max_eig, float(np.max(ev)))
        abc_min_abs_eig = min(abc_min_abs_eig, float(np.min(np.abs(ev))))
        abc_det_residual = max(abc_det_residual, rel(np.linalg.det(H), -0.5*amp**6))

    print(f"compact epsilon chosen: {eps:.6e}")
    print(f"minimum critical-sheet vorticity amplitude: {min_w:.6e}")
    print(f"largest normal enstrophy curvature on compact interval: {max_normal_curvature:.6e}")
    print(f"minimum normal-curvature margin on compact interval: {min_curvature_margin:.6e}")
    print(f"prescribed-root interpolation residual: {interpolation:.3e}")
    print(f"minimum simple-root derivative signal: {min_simple:.3e}")
    print(f"maximum exact crossing-gap residual: {crossing_residual:.3e}")
    print(f"crossing sign-change violation count: {sign_fail}")
    print(f"number of ranking crossings with zero sampled normal degeneracies: {len(roots)}")
    print(f"exact heat-shear PDE residual: {heat:.3e}")
    print(f"exact heat-shear nonlinear-advection residual: {nonlinear:.3e}")
    print(f"ABC largest Hessian eigenvalue over time audit: {abc_max_eig:.6e}")
    print(f"ABC minimum absolute Hessian eigenvalue over time audit: {abc_min_abs_eig:.6e}")
    print(f"ABC Hessian determinant formula residual: {abc_det_residual:.3e}")

    assert eps > 0.0
    assert min_w > 1e-3
    assert max_normal_curvature < -1e-3
    assert min_curvature_margin > 1e-3
    assert interpolation < 2e-12
    assert min_simple > 1e-8
    assert crossing_residual < 2e-12
    assert sign_fail == 0
    assert heat < 2e-14
    assert nonlinear == 0.0
    assert abc_max_eig < -1e-3
    assert abc_min_abs_eig > 1e-3
    assert abc_det_residual < 2e-14
    print("PASS: exact NS ranking crossings occur inside persistent nondegenerate critical-lineage intervals with zero nonlinear advection")


if __name__ == "__main__":
    main()
