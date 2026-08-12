"""Action-only referee for convex-order split/merge hierarchy and heat-defect half-face."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(42082026)
    affine = convex_violation = strong_violation = heat_curv = heat_gap = 0.0
    convex_signal = heat_signal = 0.0

    # Generic two-point martingale splits/merges.
    powers = [1.0, 1.5, 2.0, 3.0, 4.0]
    for _ in range(20000):
        x1, x2 = sorted(rng.uniform(-8.0, 8.0, size=2))
        if abs(x2 - x1) < 1e-9:
            continue
        p = float(rng.uniform(1e-5, 1.0 - 1e-5))
        xm = p * x1 + (1.0 - p) * x2
        Q = float(rng.uniform(0.01, 8.0))

        # Affine energy/helicity observables have zero Jensen gap.
        affine = max(
            affine,
            abs(Q * (p + (1.0 - p) - 1.0)),
            abs(Q * (p * x1 + (1.0 - p) * x2 - xm)),
        )

        var = p * (1.0 - p) * (x1 - x2) ** 2
        for q in powers:
            phi1, phi2, phim = abs(x1) ** q, abs(x2) ** q, abs(xm) ** q
            gap = Q * (p * phi1 + (1.0 - p) * phi2 - phim)
            convex_violation = max(convex_violation, max(0.0, -gap))
            convex_signal = max(convex_signal, gap)

        # Constant-curvature x^2 identity.
        sqgap = Q * (p * x1 * x1 + (1.0 - p) * x2 * x2 - xm * xm)
        strong_violation = max(strong_violation, abs(sqgap - Q * var))

    # Unique heat-defect curvature and strong-convexity lower inside a<alpha<1/2.
    for _ in range(20000):
        nu = float(rng.uniform(0.02, 2.0))
        tau = float(rng.uniform(1e-4, 2.0))
        alpha = float(rng.uniform(0.01, 0.49))
        xmax = math.sqrt(alpha / (2.0 * nu * tau))
        x1, x2 = rng.uniform(-xmax, xmax, size=2)
        p = float(rng.uniform(1e-5, 1.0 - 1e-5))
        xm = p * x1 + (1.0 - p) * x2
        Q = float(rng.uniform(0.01, 8.0))

        def w(x):
            return 1.0 - math.exp(-2.0 * nu * tau * x * x)

        gap = Q * (p * w(x1) + (1.0 - p) * w(x2) - w(xm))
        varwork = Q * p * (1.0 - p) * (x1 - x2) ** 2
        lower = 2.0 * nu * tau * math.exp(-alpha) * (1.0 - 2.0 * alpha) * varwork
        heat_gap = max(heat_gap, max(0.0, lower - gap))
        heat_signal = max(heat_signal, gap)

        # Analytic inflection formula checked directly at the sampled endpoint.
        x = float(rng.uniform(-xmax, xmax))
        a = 2.0 * nu * tau * x * x
        wpp = 4.0 * nu * tau * math.exp(-a) * (1.0 - 2.0 * a)
        heat_curv = max(heat_curv, max(0.0, -wpp))

    # Exact half-face curvature is zero.
    nu, tau = 0.7, 0.9
    xhalf = math.sqrt(0.5 / (2.0 * nu * tau))
    ahalf = 2.0 * nu * tau * xhalf * xhalf
    half_res = abs(4.0 * nu * tau * math.exp(-ahalf) * (1.0 - 2.0 * ahalf))

    print(f"worst affine energy/helicity Jensen residual: {affine:.3e}")
    print(f"worst convex-order sign violation: {convex_violation:.3e}")
    print(f"worst quadratic variance-gap residual: {strong_violation:.3e}")
    print(f"worst sub-half-face curvature sign violation: {heat_curv:.3e}")
    print(f"worst heat-defect strong-convexity lower violation: {heat_gap:.3e}")
    print(f"exact half-face inflection residual: {half_res:.3e}")
    print(f"maximum sampled convex Jensen signal: {convex_signal:.3e}")
    print(f"maximum sampled heat-defect split signal: {heat_signal:.3e}")

    assert affine < 2e-12
    assert convex_violation < 2e-11
    assert strong_violation < 2e-10
    assert heat_curv < 2e-12
    assert heat_gap < 2e-11
    assert half_res < 2e-12
    assert convex_signal > 1e-4 and heat_signal > 1e-8
    print("PASS: convex helical branching / parabolic half-face calibrations")


if __name__ == "__main__":
    main()
