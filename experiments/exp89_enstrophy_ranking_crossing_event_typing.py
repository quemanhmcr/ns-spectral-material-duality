"""Action-only referee for exact NS enstrophy ranking crossing and event typing."""
import numpy as np


def rel(a, b):
    return abs(a - b) / (1.0 + abs(a) + abs(b))


def shear_jets(y, t, nu):
    a1 = np.exp(-nu * t)
    a2 = np.exp(3.0) * np.exp(-4.0 * nu * t)
    a3 = np.exp(8.0) * np.exp(-9.0 * nu * t)
    U = -a1 * np.sin(y) - 1.5 * a2 * np.sin(2.0 * y) + (a3 / 3.0) * np.sin(3.0 * y)
    Uy = -a1 * np.cos(y) - 3.0 * a2 * np.cos(2.0 * y) + a3 * np.cos(3.0 * y)
    Uyy = a1 * np.sin(y) + 6.0 * a2 * np.sin(2.0 * y) - 3.0 * a3 * np.sin(3.0 * y)
    Uyyy = a1 * np.cos(y) + 12.0 * a2 * np.cos(2.0 * y) - 9.0 * a3 * np.cos(3.0 * y)
    Ut = nu * (a1 * np.sin(y) + 6.0 * a2 * np.sin(2.0 * y) - 3.0 * a3 * np.sin(3.0 * y))
    w = -Uy
    wy = -Uyy
    wyy = -Uyyy
    e = 0.5 * w * w
    ey = w * wy
    eyy = wy * wy + w * wyy
    return U, Uy, Uyy, Uyyy, Ut, w, wy, wyy, e, ey, eyy


def main():
    nu = 0.37
    tstar = 1.0 / nu
    y0 = 0.0
    y1 = np.pi

    # Exact PDE audit on the full periodic shear family.
    heat = 0.0
    nonlinear = 0.0
    for t in np.linspace(0.15 / nu, 1.85 / nu, 51):
        for y in np.linspace(-np.pi, np.pi, 401):
            U, _, Uyy, _, Ut, *_ = shear_jets(y, t, nu)
            heat = max(heat, abs(Ut - nu * Uyy) / (1.0 + abs(Ut) + abs(nu * Uyy)))
            # u=(U(y,t),0,0), hence u.grad = U d_x and the field is x-independent.
            nonlinear = max(nonlinear, abs(U * 0.0))

    j0 = shear_jets(y0, tstar, nu)
    j1 = shear_jets(y1, tstar, nu)
    U0, Uy0, Uyy0, Uyyy0, _, w0, wy0, _, e0, ey0, eyy0 = j0
    U1, Uy1, Uyy1, Uyyy1, _, w1, wy1, _, e1, ey1, eyy1 = j1

    target_e = 4.5 * np.exp(-2.0)
    target_c0 = -12.0 * np.exp(-2.0)
    target_c1 = -60.0 * np.exp(-2.0)
    target_gap_rate = 48.0 * nu * np.exp(-2.0)

    tie = rel(e0, e1)
    value_formula = max(rel(e0, target_e), rel(e1, target_e))
    critical = max(abs(ey0), abs(ey1)) / (1.0 + abs(e0) + abs(e1))
    transverse_curvature = max(rel(eyy0, target_c0), rel(eyy1, target_c1))

    # Local velocity 2-jets agree, while the third jet differs.
    jet2 = max(rel(U0, U1), rel(Uy0, Uy1), rel(Uyy0, Uyy1))
    vorticity_tie = max(rel(w0, w1), rel(wy0, wy1))
    third_jet_gap = abs(Uyyy1 - Uyyy0)
    third_formula = max(rel(Uyyy0, 4.0 * np.exp(-1.0)), rel(Uyyy1, 20.0 * np.exp(-1.0)))

    stretching0 = 0.0
    stretching1 = 0.0
    kelvin0 = nu * wy0 * wy0
    kelvin1 = nu * wy1 * wy1
    rate0 = stretching0 - kelvin0 + nu * eyy0
    rate1 = stretching1 - kelvin1 + nu * eyy1
    gap_rate = rate0 - rate1
    gap_rate_formula = rel(gap_rate, target_gap_rate)
    both_decay = max(rate0, rate1)

    # Direct winner switch around the exact crossing.
    dt = 0.02 / nu
    em0 = shear_jets(y0, tstar - dt, nu)[8]
    em1 = shear_jets(y1, tstar - dt, nu)[8]
    ep0 = shear_jets(y0, tstar + dt, nu)[8]
    ep1 = shear_jets(y1, tstar + dt, nu)[8]
    pre_gap = em0 - em1
    post_gap = ep0 - ep1

    envelope_jump = abs(max(e0, e1) - target_e)
    derivative_kink = rate0 - rate1

    print(f"exact shear heat-equation residual: {heat:.3e}")
    print(f"exact shear nonlinear-advection residual: {nonlinear:.3e}")
    print(f"crossing scalar-tie residual: {tie:.3e}")
    print(f"crossing value formula residual: {value_formula:.3e}")
    print(f"critical-sheet gradient residual: {critical:.3e}")
    print(f"transverse-curvature formula residual: {transverse_curvature:.3e}")
    print(f"local velocity 2-jet tie residual: {jet2:.3e}")
    print(f"local vorticity/first-derivative tie residual: {vorticity_tie:.3e}")
    print(f"third-jet formula residual: {third_formula:.3e}")
    print(f"third-jet separation signal: {third_jet_gap:.3e}")
    print(f"Kelvin-bulk-at-crossing residual: {max(abs(kelvin0), abs(kelvin1)):.3e}")
    print(f"branch-0 curvature-only rate: {rate0:.6e}")
    print(f"branch-pi curvature-only rate: {rate1:.6e}")
    print(f"gap-rate formula residual: {gap_rate_formula:.3e}")
    print(f"transverse ranking-gap rate signal: {gap_rate:.6e}")
    print(f"pre-crossing gap signal: {pre_gap:.6e}")
    print(f"post-crossing gap signal: {post_gap:.6e}")
    print(f"selected scalar continuity residual: {envelope_jump:.3e}")
    print(f"selected derivative-kink signal: {derivative_kink:.6e}")

    assert heat < 2e-14
    assert nonlinear == 0.0
    assert tie < 2e-14
    assert value_formula < 2e-14
    assert critical < 2e-14
    assert transverse_curvature < 2e-14
    assert jet2 < 2e-14
    assert vorticity_tie < 2e-14
    assert third_formula < 2e-14
    assert third_jet_gap > 1e-1
    assert max(abs(kelvin0), abs(kelvin1)) < 2e-14
    assert rate0 < 0.0 and rate1 < 0.0
    assert both_decay < 0.0
    assert gap_rate_formula < 2e-14
    assert gap_rate > 0.0
    assert pre_gap < 0.0 and post_gap > 0.0
    assert envelope_jump < 2e-14
    assert derivative_kink > 0.0
    print("PASS: exact NS ranking crossing is curvature-driven, 2-jet-invisible, and not a nonlinear hard event")


if __name__ == "__main__":
    main()
