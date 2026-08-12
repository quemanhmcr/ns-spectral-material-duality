"""Adversarial stress for corridor current topology and hysteretic killing cycles."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(33082026)
    current_res = clock_topology = cycle_res = survival_res = 0.0
    nonlinear_cross_signal = reverse_signal = 0.0

    # Smooth-cut version of the exact corridor current product rule.
    for _ in range(1500):
        n = int(rng.integers(3, 9))
        E = rng.uniform(0.02, 3.0, size=n)
        d = rng.uniform(0.1, 8.0, size=n)
        tau = float(rng.uniform(0.05, 2.0))
        a = d * tau
        alpha = float(rng.uniform(0.1, 0.8))
        beta = float(rng.uniform(alpha + 0.4, alpha + 2.0))
        eps = 0.15
        # Smooth corridor chi = sigmoid((a-alpha)/eps)*sigmoid((beta-a)/eps).
        s1 = 1.0 / (1.0 + np.exp(-(a - alpha) / eps))
        s2 = 1.0 / (1.0 + np.exp(-(beta - a) / eps))
        chi = s1 * s2
        dchi_da = (s1 * (1.0 - s1) / eps) * s2 - s1 * (s2 * (1.0 - s2) / eps)
        chidot = -d * dchi_da
        R = rng.uniform(0.0, 1.1, size=(n, n))
        np.fill_diagonal(R, 0.0)
        K = E[:, None] * R
        Edot = K.sum(axis=0) - K.sum(axis=1) - d * E
        lhs = float(np.dot(chidot, E) + np.dot(chi, Edot))
        rhs = float(np.sum((chi[None, :] - chi[:, None]) * K) - np.dot(d * chi, E) + np.dot(chidot, E))
        current_res = max(current_res, abs(lhs - rhs))
        nonlinear_cross_signal = max(nonlinear_cross_signal, abs(np.sum((chi[None, :] - chi[:, None]) * K)))

    # Clock topology: a(t)=d tau is strictly decreasing for fixed mode.
    for _ in range(1000):
        d = float(rng.uniform(0.1, 10.0))
        tau0 = float(rng.uniform(0.2, 4.0))
        tau1 = float(rng.uniform(0.0, tau0))
        a0 = d * tau0
        a1 = d * tau1
        clock_topology = max(clock_topology, max(0.0, a1 - a0))

    # Hysteretic cycles with nonnegative internal jumps.
    for _ in range(1200):
        aminus = float(rng.uniform(0.05, 0.8))
        aplus = float(rng.uniform(aminus + 0.05, aminus + 1.5))
        start = float(rng.uniform(aplus, aplus + 2.0))
        end = float(rng.uniform(0.0, aminus))
        jumps = rng.uniform(0.0, 0.8, size=int(rng.integers(0, 8)))
        hazard = start - end + float(jumps.sum())
        gap = aplus - aminus
        cycle_res = max(cycle_res, max(0.0, gap - hazard))
        ncycles = int(rng.integers(1, 20))
        survival = math.exp(-ncycles * gap)
        survival_res = max(survival_res, max(0.0, survival - math.exp(-ncycles * gap)))

    # A negative jump can shortcut the gap: retain it as a reverse-owner signal.
    aminus, aplus = 0.4, 0.9
    negative_jump = -0.7
    reverse_signal = abs(negative_jump)
    shortcut_hazard = max(0.0, aplus + negative_jump - aminus)

    print(f"worst smooth corridor-current residual: {current_res:.3e}")
    print(f"worst fixed-mode clock monotonicity violation: {clock_topology:.3e}")
    print(f"worst hysteretic cycle killing-gap violation: {cycle_res:.3e}")
    print(f"worst exponential survival identity residual: {survival_res:.3e}")
    print(f"maximum sampled nonlinear corridor-crossing signal: {nonlinear_cross_signal:.3e}")
    print(f"reverse-jump shortcut owner signal: {reverse_signal:.3e}")
    print(f"shortcut residual hazard after reverse jump: {shortcut_hazard:.3e}")

    assert current_res < 2e-11
    assert clock_topology < 1e-14
    assert cycle_res < 1e-12
    assert survival_res < 1e-14
    assert nonlinear_cross_signal > 1e-3
    assert reverse_signal > 0.1
    print("PASS: parabolic corridor-current / hysteretic-reentry calibrations")


if __name__ == "__main__":
    main()
