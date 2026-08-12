"""Action-only referee for absolute-helical critical mass and comparable split compensation."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(44082026)
    abs_gap = pair_gap = homo_share = homo_leak = 0.0
    hetero_gain = hetero_ratio = hetero_bounds = 0.0
    gate_homo = gate_hetero = 0.0
    signal = 0.0

    # Generic binary martingale splits/merges on signed frequency.
    for _ in range(25000):
        xm = float(rng.uniform(-8.0, 2.0))
        xp = float(rng.uniform(max(xm + 1e-3, -1.0), 10.0))
        p = float(rng.uniform(1e-4, 1.0 - 1e-4))
        xd = p * xm + (1.0 - p) * xp
        Q = float(rng.uniform(1e-4, 8.0))
        gap = Q * (p * abs(xm) + (1.0 - p) * abs(xp) - abs(xd))
        charge = Q * min(p * abs(xm), (1.0 - p) * abs(xp)) if xm < 0.0 < xp else 0.0
        abs_gap = max(abs_gap, abs(gap - 2.0 * charge))
        signal = max(signal, abs(gap))

        # Reverse sign is the corresponding merge convexity loss.
        merge = Q * (abs(xd) - (p * abs(xm) + (1.0 - p) * abs(xp)))
        pair_gap = max(pair_gap, abs(merge + 2.0 * charge))

    # Fully comparable homochiral split.
    for _ in range(20000):
        c = float(rng.uniform(1.0, 12.0))
        a = float(rng.uniform(c / 4.0, 0.98 * c))
        b = float(rng.uniform(a + 1e-6, c - 1e-6))
        if not (a < b < c):
            continue
        Q = float(rng.uniform(1e-4, 6.0))
        pl = (c - b) / (c - a)
        ph = (b - a) / (c - a)
        rho = c * ph / b
        leak = a * pl * Q
        V = Q * (b - a) * (c - b)
        lam = c / b
        homo_share = max(homo_share, abs((rho + a * pl / b) - 1.0))
        homo_leak = max(homo_leak, max(0.0, V / (4.0 * c) - leak))
        homo_leak = max(homo_leak, max(0.0, 0.25 * math.log(lam) - (1.0 - rho)))

    # Fully comparable heterochiral split, positive donor normal form.
    for _ in range(20000):
        K = float(rng.uniform(1.0, 12.0))
        a = float(rng.uniform(K / 4.0, K))
        b = float(rng.uniform(K / 4.0, K))
        c = float(rng.uniform(max(a + 1e-6, K / 4.0), K))
        Kact = max(a, b, c)
        if min(a, b, c) < Kact / 4.0 or c <= a:
            continue
        Q = float(rng.uniform(1e-4, 6.0))
        ph = (a + b) / (b + c)
        po = (c - a) / (b + c)
        P = Q * po * b
        V = Q * (a + b) * (c - a)
        hetero_gain = max(hetero_gain, abs(Q * ph * c - (Q * a + P)), abs(Q * po * b - P))
        ratio = V / P
        exact_ratio = (a + b) * (b + c) / b
        hetero_ratio = max(hetero_ratio, abs(ratio - exact_ratio))
        hetero_bounds = max(
            hetero_bounds,
            max(0.0, Kact / 4.0 - ratio),
            max(0.0, ratio - 16.0 * Kact),
        )

    # Rate-gate constants from a synthetic BX comparable owner block.
    for _ in range(10000):
        nu = float(rng.uniform(0.02, 2.0))
        N = float(2.0 ** int(rng.integers(-1, 9)))
        Z = float(rng.uniform(0.01, 20.0))
        Vcmp = float(rng.uniform(0.5, 2.0)) * nu * Z
        frac = float(rng.uniform(0.0, 1.0))
        Vh = frac * Vcmp
        Vx = (1.0 - frac) * Vcmp
        owner = max(Vh, Vx)
        if owner == Vh:
            leak_lower = owner / (8.0 * N)  # K<2N and L>=V/(4K)
            gate_homo = max(gate_homo, max(0.0, nu * Z / (32.0 * N) - leak_lower))
        else:
            pair_lower = owner / (32.0 * N)  # K<2N and P>=V/(16K)
            gate_hetero = max(gate_hetero, max(0.0, nu * Z / (128.0 * N) - pair_lower))

    print(f"worst |x| split-pair identity residual: {abs_gap:.3e}")
    print(f"worst |x| merge-pair identity residual: {pair_gap:.3e}")
    print(f"worst homochiral critical-share conservation residual: {homo_share:.3e}")
    print(f"worst homochiral comparable leakage violation: {homo_leak:.3e}")
    print(f"worst heterochiral high-gain/pair residual: {hetero_gain:.3e}")
    print(f"worst heterochiral variance/pair ratio residual: {hetero_ratio:.3e}")
    print(f"worst heterochiral comparable ratio-bound violation: {hetero_bounds:.3e}")
    print(f"worst BX homochiral compensation-gate violation: {gate_homo:.3e}")
    print(f"worst BX heterochiral compensation-gate violation: {gate_hetero:.3e}")
    print(f"maximum sampled critical-pair signal: {signal:.3e}")

    assert abs_gap < 2e-11
    assert pair_gap < 2e-11
    assert homo_share < 2e-12
    assert homo_leak < 2e-12
    assert hetero_gain < 2e-11
    assert hetero_ratio < 2e-10
    assert hetero_bounds < 2e-12
    assert gate_homo < 2e-12
    assert gate_hetero < 2e-12
    assert signal > 1e-4
    print("PASS: absolute-helical critical-mass / comparable-split compensation calibrations")


if __name__ == "__main__":
    main()
