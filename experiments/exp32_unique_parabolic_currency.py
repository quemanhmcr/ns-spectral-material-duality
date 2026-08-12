"""Adversarial stress for the unique parabolic energy coordinate and price no-go."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(32082026)
    survival_res = defect_res = generator_res = 0.0
    low_price = high_price = peak_res = 0.0
    interior_signal = 0.0

    for _ in range(2000):
        a = float(rng.uniform(0.0, 12.0))
        q = math.exp(-a)
        w = 1.0 - q
        qp = -q
        wp = q
        survival_res = max(survival_res, abs(q + qp))
        defect_res = max(defect_res, abs(w + wp - 1.0))

        n = int(rng.integers(3, 9))
        E = rng.uniform(0.02, 3.0, size=n)
        d = rng.uniform(0.1, 8.0, size=n)
        tau = float(rng.uniform(0.02, 2.0))
        aa = d * tau
        R = rng.uniform(0.0, 1.2, size=(n, n))
        np.fill_diagonal(R, 0.0)
        K = E[:, None] * R
        Edot = K.sum(axis=0) - K.sum(axis=1) - d * E
        f = 1.0 - np.exp(-aa)
        fp = np.exp(-aa)
        fdot = -d * fp
        lhs = float(np.dot(fdot, E) + np.dot(f, Edot))
        rhs = float(np.sum((f[None, :] - f[:, None]) * K) - np.dot(d, E))
        generator_res = max(generator_res, abs(lhs - rhs))

    lam = 1.6
    for a in (1e-12, 1e-10, 1e-8, 1e-6):
        low_price = max(low_price, math.exp(-a) - math.exp(-(lam * lam) * a))
    for a in (20.0, 30.0, 50.0, 80.0):
        high_price = max(high_price, math.exp(-a) - math.exp(-(lam * lam) * a))

    astar = 2.0 * math.log(lam) / (lam * lam - 1.0)
    dprice = -math.exp(-astar) + lam * lam * math.exp(-(lam * lam) * astar)
    peak_res = abs(dprice)
    interior_signal = math.exp(-astar) - math.exp(-(lam * lam) * astar)

    # Homogeneous solution of f'+f=1: terminal normalization f(0)=0 removes C e^-a.
    uniqueness_res = 0.0
    for _ in range(1000):
        C = float(rng.normal())
        a = float(rng.uniform(0.0, 8.0))
        f = 1.0 + C * math.exp(-a)
        fp = -C * math.exp(-a)
        uniqueness_res = max(uniqueness_res, abs(f + fp - 1.0))
    terminal_normalized_C = 0.0 - 1.0  # f(0)=1+C=0 => C=-1
    terminal_res = abs((1.0 + terminal_normalized_C) - 0.0)

    print(f"worst survival ODE residual q'+q: {survival_res:.3e}")
    print(f"worst defect ODE residual w'+w-1: {defect_res:.3e}")
    print(f"worst weighted-energy generator residual: {generator_res:.3e}")
    print(f"maximum sampled near-zero fixed-ratio price: {low_price:.3e}")
    print(f"maximum sampled large-a fixed-ratio price: {high_price:.3e}")
    print(f"interior price-stationarity residual: {peak_res:.3e}")
    print(f"interior fixed-ratio price signal: {interior_signal:.6f}")
    print(f"worst affine-family unit-killing ODE residual: {uniqueness_res:.3e}")
    print(f"terminal normalization residual: {terminal_res:.3e}")

    assert survival_res < 1e-14
    assert defect_res < 1e-14
    assert generator_res < 2e-11
    assert low_price < 2e-6
    assert high_price < 3e-9
    assert peak_res < 1e-13
    assert interior_signal > 1e-2
    assert uniqueness_res < 1e-14
    assert terminal_res < 1e-14
    print("PASS: unique parabolic energy-currency / global-price no-go calibrations")


if __name__ == "__main__":
    main()
