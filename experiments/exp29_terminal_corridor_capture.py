"""Adversarial stress for terminal parabolic corridor decay and capture algebra."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(29082026)
    ode_res = exclusion_violation = capture_violation = lower_face_res = 0.0
    decay_signal = cheap_signal = skip_signal = 0.0

    # Exact corridor ODE M=C tau^alpha and critical floor comparison.
    for _ in range(1000):
        alpha = float(rng.uniform(0.51, 2.0))
        beta = float(rng.uniform(1.0, 5.0))
        nu = float(rng.uniform(0.05, 2.0))
        eta = float(rng.uniform(0.02, 1.0))
        tau_s = float(rng.uniform(0.2, 4.0))
        M_s = float(rng.uniform(0.5, 10.0))
        tau = float(rng.uniform(1e-6, 0.9 * tau_s))
        M = M_s * (tau / tau_s) ** alpha
        dMdt = -alpha * M / tau
        ode_res = max(ode_res, abs(dMdt + alpha * M / tau))

        C = eta * math.sqrt(2.0 * nu / beta) * (tau_s ** alpha) / M_s
        if C > 0:
            tau_cut = C ** (1.0 / (alpha - 0.5))
            tau_test = min(0.25 * tau_cut, 0.25 * tau_s)
            if tau_test > 0:
                surv = M_s * (tau_test / tau_s) ** alpha
                floor = eta * math.sqrt(2.0 * nu / beta) * math.sqrt(tau_test)
                exclusion_violation = max(exclusion_violation, max(0.0, surv - floor))
                decay_signal = max(decay_signal, floor / max(surv, 1e-300))

    # Exact capture under bounded scale ratio.
    for _ in range(3000):
        alpha = float(rng.uniform(0.1, 1.0))
        Lam = float(rng.uniform(1.05, 3.0))
        beta = float(rng.uniform(1.001 * Lam * Lam * alpha, 2.5 * Lam * Lam * alpha))
        a_minus = float(rng.uniform(0.0, 0.999999 * alpha))
        ratio = float(rng.uniform(1.0, Lam))
        a_plus = ratio * ratio * a_minus
        if a_plus >= alpha:
            capture_violation = max(capture_violation, max(0.0, a_plus - beta))

    # Without scale-ratio bound one jump skips the corridor.
    alpha = 0.4
    beta = 2.0
    a_minus = 0.1
    ratio = math.sqrt(3.2 / a_minus)
    a_plus = ratio * ratio * a_minus
    skip_signal = a_plus - beta

    # Conditional own-scale lifespan -> lower parabolic face.
    for _ in range(1000):
        nu = float(rng.uniform(0.02, 3.0))
        N = float(rng.uniform(0.2, 50.0))
        cstar = float(rng.uniform(0.01, 2.0))
        lifespan = cstar / (nu * N * N)
        tau = lifespan * float(rng.uniform(1.0, 5.0))
        a = 2.0 * nu * N * N * tau
        lower_face_res = max(lower_face_res, max(0.0, 2.0 * cstar - a))

    # At alpha<1/2 the pure terminal-power comparison cannot close.
    alpha = 0.30
    beta = 2.0
    nu = 1.0
    eta = 0.2
    tau_s = 1.0
    M_s = 1.0
    ratios = []
    for tau in (1e-2, 1e-4, 1e-8, 1e-12):
        surv = M_s * tau**alpha
        floor = eta * math.sqrt(2.0 * nu / beta) * math.sqrt(tau)
        ratios.append(surv / floor)
    cheap_signal = ratios[-1] / ratios[0]

    print(f"worst exact corridor-decay ODE residual: {ode_res:.3e}")
    print(f"worst terminal exclusion-window violation: {exclusion_violation:.3e}")
    print(f"worst bounded-ratio corridor-capture violation: {capture_violation:.3e}")
    print(f"worst conditional first-bad lower-face violation: {lower_face_res:.3e}")
    print(f"maximum sampled terminal floor/survival separation: {decay_signal:.3e}")
    print(f"unbounded-jump corridor-skip signal: {skip_signal:.3e}")
    print(f"alpha<1/2 cheap-survival ratio growth: {cheap_signal:.3e}")

    assert ode_res < 1e-13
    assert exclusion_violation < 1e-12
    assert capture_violation < 1e-12
    assert lower_face_res < 1e-12
    assert decay_signal > 1.0
    assert skip_signal > 0.5
    assert cheap_signal > 10.0
    print("PASS: terminal parabolic-corridor / first-bad reduction calibrations")


if __name__ == "__main__":
    main()
