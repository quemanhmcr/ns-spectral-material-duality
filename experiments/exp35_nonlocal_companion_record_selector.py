"""Adversarial stress for nonlocal triad companion geometry and record-shell selector algebra."""
import numpy as np


def main():
    rng = np.random.default_rng(35082026)
    triad_res = skip_res = selector_res = 0.0
    companion_signal = skip_companion_signal = 0.0

    for _ in range(5000):
        kd = rng.normal(size=3)
        kr = rng.normal(size=3)
        nd = np.linalg.norm(kd)
        nr = np.linalg.norm(kr)
        if nd < 1e-8 or nr < 1e-8:
            continue
        kc = -(kd + kr)
        nc = np.linalg.norm(kc)
        triad_res = max(triad_res, max(0.0, abs(nr - nd) - nc))
        Lam = nr / nd
        if Lam > 1.05:
            lower = (1.0 - 1.0 / Lam) * nr
            triad_res = max(triad_res, max(0.0, lower - nc))
            companion_signal = max(companion_signal, lower)

    for _ in range(3000):
        alpha = float(rng.uniform(0.05, 0.8))
        beta = float(rng.uniform(alpha + 0.2, alpha + 4.0))
        ad = float(rng.uniform(1e-8, 0.999 * alpha))
        ar = float(rng.uniform(1.001 * beta, 8.0 * beta))
        ratio = np.sqrt(ar / ad)
        frac = 1.0 - np.sqrt(alpha / beta)
        # Minimal companion ratio from exact triangle inequality under this skip.
        actual_lower = 1.0 - 1.0 / ratio
        skip_res = max(skip_res, max(0.0, frac - actual_lower))
        skip_companion_signal = max(skip_companion_signal, frac)

    # Finite highest-active-shell selector on a synthetic smooth tail sequence.
    for _ in range(2000):
        Q = int(rng.integers(4, 30))
        Astar = float(rng.uniform(0.1, 2.0))
        amps = np.zeros(Q + 30)
        # Smooth tail decays; force at least one active shell.
        active_q = int(rng.integers(0, Q + 1))
        for q in range(len(amps)):
            amps[q] = Astar * 3.0 * np.exp(-0.35 * abs(q - active_q)) * np.exp(-0.015 * q * q)
        amps[active_q] = max(amps[active_q], 1.2 * Astar)
        active = np.flatnonzero(amps >= Astar)
        qstar = int(active.max())
        selector_res = max(selector_res, max(0.0, Astar - amps[qstar]))
        if qstar + 1 < len(amps):
            selector_res = max(selector_res, max(0.0, np.max(amps[qstar + 1:]) - Astar))

    print(f"worst closed-triad companion lower-bound violation: {triad_res:.3e}")
    print(f"worst parabolic-skip companion-fraction violation: {skip_res:.3e}")
    print(f"worst highest-critical-shell selector residual: {selector_res:.3e}")
    print(f"maximum sampled nonlocal companion lower-bound signal: {companion_signal:.3e}")
    print(f"maximum sampled skip companion fraction: {skip_companion_signal:.3e}")

    assert triad_res < 1e-12
    assert skip_res < 1e-12
    assert selector_res < 1e-12
    assert companion_signal > 1e-2
    assert skip_companion_signal > 1e-2
    print("PASS: nonlocal companion / record critical-shell selector calibrations")


if __name__ == "__main__":
    main()
