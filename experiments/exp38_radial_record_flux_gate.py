"""Action-only adversarial referee for the exact radial record-flux gate."""
import math
import numpy as np


def radial_values(radii, energy, K, R):
    high = radii > R
    low = ~high
    hi = [i for i in range(len(radii)) if high[i]]
    lo = [i for i in range(len(radii)) if low[i]]
    up = math.fsum(float(K[i, j]) for i in lo for j in hi)
    down = math.fsum(float(K[i, j]) for i in hi for j in lo)
    G = math.fsum(float(radii[i] ** 2 * energy[i]) for i in hi)
    return up - down, G


def main():
    rng = np.random.default_rng(38082026)
    work_layer = pal_layer = gate_violation = 0.0
    gate_signal = current_signal = 0.0

    for _ in range(2500):
        n = int(rng.integers(4, 16))
        radii = np.sort(rng.uniform(0.2, 10.0, size=n))
        energy = rng.uniform(1e-4, 4.0, size=n)
        nu = float(rng.uniform(0.03, 1.5))

        # Upward-biased physical donor flow plus genuine downward traffic.
        K = np.zeros((n, n), dtype=float)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if radii[j] > radii[i]:
                    K[i, j] = float(rng.exponential(0.5))
                else:
                    K[i, j] = 0.18 * float(rng.exponential(0.5))

        # Scale nonlinear flow so the state is at/above the record-growth work gate.
        W0 = math.fsum(
            float((radii[j] ** 2 - radii[i] ** 2) * K[i, j])
            for i in range(n) for j in range(n)
        )
        Z = math.fsum(float(radii[i] ** 4 * energy[i]) for i in range(n))
        if W0 <= 1e-12 or Z <= 1e-12:
            continue
        factor = float(rng.uniform(1.0, 3.0)) * nu * Z / W0
        K *= factor
        W = W0 * factor

        # Exact piecewise radial layer cake on intervals between modal radii.
        bounds = [0.0] + [float(x) for x in radii]
        intF = 0.0
        intG = 0.0
        best_margin = -float("inf")
        best_signal = 0.0
        for a, b in zip(bounds[:-1], bounds[1:]):
            if b <= a:
                continue
            R = 0.5 * (a + b)
            F, G = radial_values(radii, energy, K, R)
            weight = b * b - a * a  # integral 2R dR
            intF += weight * F
            intG += weight * G
            best_margin = max(best_margin, F - nu * G)
            best_signal = max(best_signal, F)

        work_layer = max(work_layer, abs(intF - W))
        pal_layer = max(pal_layer, abs(intG - Z))
        gate_violation = max(gate_violation, max(0.0, -best_margin))
        gate_signal = max(gate_signal, best_margin)
        current_signal = max(current_signal, best_signal)

    print(f"worst net-current radial layer-cake residual: {work_layer:.3e}")
    print(f"worst tail-gradient radial layer-cake residual: {pal_layer:.3e}")
    print(f"worst record radial-gate existence violation: {gate_violation:.3e}")
    print(f"maximum sampled F-nuG gate margin: {gate_signal:.3e}")
    print(f"maximum sampled net outward radial-current signal: {current_signal:.3e}")

    assert work_layer < 2e-10
    assert pal_layer < 2e-10
    assert gate_violation < 2e-11
    assert gate_signal > 1e-5 and current_signal > 1e-5
    print("PASS: radial record-flux / tail-killing gate calibrations")


if __name__ == "__main__":
    main()
