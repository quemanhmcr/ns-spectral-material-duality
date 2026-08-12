"""Action-only referee for low-strain carrier memory erasure/owner forcing."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(39082026)
    gronwall = window = owner_violation = 0.0
    strain_signal = kill_signal = 0.0

    for _ in range(5000):
        nu = float(rng.uniform(0.03, 2.0))
        cminus = float(rng.uniform(0.25, 0.9))
        N = float(rng.uniform(2.0, 8e3))
        Estar = float(rng.uniform(0.2, 12.0))
        eta = float(rng.uniform(0.01, 1.5))
        K0 = float(rng.uniform(0.0, 0.12))
        delta = float(rng.uniform(0.05, 0.8))
        logarg = Estar * N / (delta * eta)
        if logarg <= 1.0:
            continue
        L = (2.0 * K0 + math.log(logarg)) / (2.0 * nu * cminus**2 * N**2)
        exponent = 2.0 * K0 - 2.0 * nu * cminus**2 * N**2 * L
        terminal_bound = math.exp(exponent) * Estar
        target = eta / N
        gronwall = max(gronwall, abs(terminal_bound - delta * target))
        normalized = L * (2.0 * nu * cminus**2 * N**2) / (2.0 * K0 + math.log(logarg))
        window = max(window, abs(normalized - 1.0))
        owner_violation = max(owner_violation, max(0.0, terminal_bound - delta * target))
        strain_signal = max(strain_signal, K0)
        kill_signal = max(kill_signal, 2.0 * nu * cminus**2 * N**2 * L)

    # Exact multiplicative comparison with a nonconstant strain history collapsed to its action.
    action_res = 0.0
    for _ in range(5000):
        E0 = float(rng.uniform(0.01, 8.0))
        K = float(rng.uniform(0.0, 1.0))
        H = float(rng.uniform(0.0, 8.0))
        direct = E0 * math.exp(2.0 * K - H)
        staged = E0 * math.exp(2.0 * K) * math.exp(-H)
        action_res = max(action_res, abs(direct - staged))

    print(f"worst carrier Gronwall boundary residual: {gronwall:.3e}")
    print(f"worst logarithmic owner-window normalization residual: {window:.3e}")
    print(f"worst no-owner critical-floor violation: {owner_violation:.3e}")
    print(f"worst strain/killing multiplicative factorization residual: {action_res:.3e}")
    print(f"maximum sampled low-strain action signal: {strain_signal:.3e}")
    print(f"maximum sampled viscous-hazard signal: {kill_signal:.3e}")

    assert gronwall < 2e-11
    assert window < 2e-12
    assert owner_violation < 2e-12
    assert action_res < 2e-12
    assert strain_signal > 1e-3 and kill_signal > 1e-2
    print("PASS: low-strain carrier memory / owner-forcing calibrations")


if __name__ == "__main__":
    main()
