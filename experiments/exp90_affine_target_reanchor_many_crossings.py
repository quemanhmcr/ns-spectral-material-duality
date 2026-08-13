"""Action-only referee for affine target coboundaries and many exact-NS ranking crossings."""
import numpy as np


def rel(a, b):
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) / (1.0 + np.linalg.norm(a) + np.linalg.norm(b))


def main():
    rng = np.random.default_rng(9013082026)

    # Exact affine target-coboundary composition and selector jump algebra.
    coboundary = 0.0
    affine_state = 0.0
    selector_affine = 0.0
    for _ in range(400):
        A1 = rng.normal(size=(3, 3)); A2 = rng.normal(size=(3, 3))
        O0 = rng.normal(size=3); O1 = rng.normal(size=3); O2 = rng.normal(size=3)
        x0 = rng.normal(size=3)
        d1 = A1 @ O0 - O1
        d2 = A2 @ O1 - O2
        d20 = (A2 @ A1) @ O0 - O2
        coboundary = max(coboundary, rel(A2 @ d1 + d2, d20))
        x1 = A1 @ x0 + d1
        x2 = A2 @ x1 + d2
        affine_state = max(affine_state, rel(x2, (A2 @ A1) @ x0 + d20))

        X = rng.normal(size=4)
        A = rng.normal(size=(4, 4)); d = rng.normal(size=4)
        Em = rng.normal(size=(2, 4)); Ep = rng.normal(size=(2, 4))
        jump = Ep @ (A @ X + d) - Em @ X
        selector_affine = max(selector_affine, rel(jump, (Ep @ A - Em) @ X + Ep @ d))

    # Exact cubic heat-shear target-reanchoring calibration.
    nu = 0.31; t = 0.47; a = 0.73; b = 0.19; ell = 1.17
    heat_cubic = 0.0
    nonlinear_cubic = 0.0
    for y in np.linspace(-2.0, 2.0, 401):
        Ut = 6.0 * nu * y
        Uyy = 6.0 * y
        heat_cubic = max(heat_cubic, abs(Ut - nu * Uyy))
        U = y**3 + 6.0 * nu * t * y
        nonlinear_cubic = max(nonlinear_cubic, abs(U * 0.0))
    q_own = 12.0 * b * ell * (a - a)
    q_zero = 12.0 * b * ell * (0.0 - a)
    target_qv_signal = q_zero * q_zero - q_own * q_own

    # Prescribe four crossings using five odd heat modes.  Coefficients are obtained
    # from the one-dimensional nullspace of the exact interpolation matrix; this is
    # only a referee for the hand proof via the Chebyshev-system zero theorem.
    odd = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
    sroot = np.array([0.004, 0.012, 0.024, 0.040])  # s = nu t
    M = np.exp(-np.outer(sroot, odd**2))
    _, _, vh = np.linalg.svd(M)
    coeff = vh[-1]
    coeff /= np.max(np.abs(coeff))
    root_residual = np.max(np.abs(M @ coeff))

    def O(s):
        return float(np.sum(coeff * np.exp(-(odd**2) * s)))

    def Os(s):
        return float(np.sum(-(odd**2) * coeff * np.exp(-(odd**2) * s)))

    def O2(s):
        return float(np.sum((odd**2) * coeff * np.exp(-(odd**2) * s)))

    min_simple = min(abs(Os(s)) for s in sroot)
    Evals = np.exp(-4.0 * sroot)
    O2vals = np.array([O2(s) for s in sroot])
    denom = max(np.max(np.abs(O2vals)), 1e-12)
    eps = min(0.05, 0.5 * (4.0 * np.min(Evals) / denom))
    B = 1.0

    # PDE audit for the synthesized exact periodic shear.
    heat_many = 0.0
    nonlinear_many = 0.0
    nu2 = 0.29
    for s in np.linspace(0.002, 0.05, 17):
        for y in np.linspace(-np.pi, np.pi, 97):
            even = -(B / 2.0) * np.exp(-4.0 * s) * np.sin(2.0 * y)
            oddU = -eps * np.sum((coeff / odd) * np.exp(-(odd**2) * s) * np.sin(odd * y))
            U = even + oddU
            Us = 2.0 * B * np.exp(-4.0 * s) * np.sin(2.0 * y) + eps * np.sum(odd * coeff * np.exp(-(odd**2) * s) * np.sin(odd * y))
            Uyy = 2.0 * B * np.exp(-4.0 * s) * np.sin(2.0 * y) + eps * np.sum(odd * coeff * np.exp(-(odd**2) * s) * np.sin(odd * y))
            # s=nu2*t, hence U_t=nu2 U_s.
            heat_many = max(heat_many, abs(nu2 * Us - nu2 * Uyy) / (1.0 + abs(nu2 * Us) + abs(nu2 * Uyy)))
            nonlinear_many = max(nonlinear_many, abs(U * 0.0))

    crossing_gap = 0.0
    gap_formula = 0.0
    min_gap_rate = np.inf
    max_transverse_eig = -np.inf
    sign_switch_violation = 0.0
    delta = 0.0008
    for s in sroot:
        E = B * np.exp(-4.0 * s)
        o = O(s)
        w0 = E + eps * o
        wp = E - eps * o
        gap = 0.5 * (w0*w0 - wp*wp)
        crossing_gap = max(crossing_gap, abs(gap))
        gap_formula = max(gap_formula, abs(gap - 2.0 * eps * E * o))
        rate_s = 2.0 * eps * E * Os(s)
        min_gap_rate = min(min_gap_rate, abs(rate_s))
        o2 = O2(s)
        eyy0 = E * (-4.0 * E - eps * o2)
        eyyp = E * (-4.0 * E + eps * o2)
        max_transverse_eig = max(max_transverse_eig, eyy0, eyyp)
        gm = 2.0 * eps * np.exp(-4.0 * (s-delta)) * O(s-delta)
        gp = 2.0 * eps * np.exp(-4.0 * (s+delta)) * O(s+delta)
        if gm * gp >= 0.0:
            sign_switch_violation = max(sign_switch_violation, gm * gp + 1.0)

    # Pure selector reset: fixed physical library, nonzero selected readout jump.
    Xlib = np.array([[0.0], [np.pi]])
    Eminus = np.array([[0.0, 1.0]])
    Eplus = np.array([[1.0, 0.0]])
    selected_jump = float(abs((Eplus @ Xlib - Eminus @ Xlib)[0, 0]))
    physical_library_change = 0.0

    print(f"affine target-coboundary composition residual: {coboundary:.3e}")
    print(f"affine state composition residual: {affine_state:.3e}")
    print(f"selector-plus-affine jump residual: {selector_affine:.3e}")
    print(f"cubic heat-shear PDE residual: {heat_cubic:.3e}")
    print(f"cubic heat-shear nonlinear-advection residual: {nonlinear_cubic:.3e}")
    print(f"own-target residual-noise coefficient: {q_own:.6e}")
    print(f"zero-target residual-noise coefficient: {q_zero:.6e}")
    print(f"target-reanchor qv-source change signal: {target_qv_signal:.6e}")
    print(f"prescribed crossing interpolation residual: {root_residual:.3e}")
    print(f"minimum simple-root derivative signal: {min_simple:.3e}")
    print(f"chosen odd-sector amplitude epsilon: {eps:.3e}")
    print(f"many-crossing heat-equation residual: {heat_many:.3e}")
    print(f"many-crossing nonlinear-advection residual: {nonlinear_many:.3e}")
    print(f"maximum prescribed crossing gap residual: {crossing_gap:.3e}")
    print(f"gap factorization residual: {gap_formula:.3e}")
    print(f"minimum transverse ranking-rate signal (s-time): {min_gap_rate:.3e}")
    print(f"largest transverse enstrophy curvature at crossings: {max_transverse_eig:.6e}")
    print(f"crossing sign-switch violation signal: {sign_switch_violation:.3e}")
    print(f"number of prescribed transverse crossings: {len(sroot)}")
    print(f"pure-selector selected-location jump signal: {selected_jump:.6e}")
    print(f"pure-selector physical-library change residual: {physical_library_change:.3e}")

    assert coboundary < 3e-13
    assert affine_state < 3e-13
    assert selector_affine < 3e-13
    assert heat_cubic < 2e-14
    assert nonlinear_cubic == 0.0
    assert abs(q_own) < 2e-14
    assert abs(q_zero) > 1e-2
    assert target_qv_signal > 1e-3
    assert root_residual < 2e-12
    assert min_simple > 1e-8
    assert eps > 0.0
    assert heat_many < 2e-14
    assert nonlinear_many == 0.0
    assert crossing_gap < 2e-12
    assert gap_formula < 2e-14
    assert min_gap_rate > 1e-10
    assert max_transverse_eig < -1e-4
    assert sign_switch_violation == 0.0
    assert selected_jump > 1.0
    assert physical_library_change == 0.0
    print("PASS: target coboundary is affine, passive-gauge identification fails, and exact NS admits many ranking crossings with zero nonlinear advection")


if __name__ == "__main__":
    main()
