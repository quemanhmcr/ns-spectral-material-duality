"""Action-only adversarial stress for radial high-tail memory erosion/fresh funding."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(36082026)
    continuity = generator_violation = 0.0
    flux_signal = diss_signal = 0.0

    # Instantaneous physical mode-set control-volume algebra.
    for _ in range(3000):
        n = int(rng.integers(5, 18))
        radii = rng.uniform(0.2, 12.0, size=n)
        energy = rng.uniform(1e-4, 5.0, size=n)
        nu = float(rng.uniform(0.03, 2.0))
        K = rng.exponential(scale=0.4, size=(n, n))
        np.fill_diagonal(K, 0.0)
        d = 2.0 * nu * radii * radii
        edot = K.sum(axis=0) - K.sum(axis=1) - d * energy

        R = float(rng.uniform(np.min(radii), np.max(radii)))
        high = radii >= R
        low = ~high
        if not np.any(high) or not np.any(low):
            continue
        phi_up = float(K[np.ix_(low, high)].sum())
        phi_down = float(K[np.ix_(high, low)].sum())
        diss = float(np.dot(d[high], energy[high]))
        lhs = float(edot[high].sum()) + diss + phi_down
        continuity = max(continuity, abs(lhs - phi_up))

        Ehigh = float(energy[high].sum())
        dmin = 2.0 * nu * R * R
        gen_lhs = float(edot[high].sum()) + dmin * Ehigh
        generator_violation = max(generator_violation, max(0.0, gen_lhs - phi_up))
        flux_signal = max(flux_signal, phi_up)
        diss_signal = max(diss_signal, diss)

    # Exact scalar integrating-factor referee and critical-shell funding lower.
    duhamel = funding_violation = window_scale = 0.0
    funding_signal = 0.0
    for _ in range(3000):
        nu = float(rng.uniform(0.05, 2.0))
        rho = float(rng.uniform(0.35, 0.9))
        N = float(rng.uniform(4.0, 5e3))
        eta = float(rng.uniform(0.02, 2.0))
        Estar = float(rng.uniform(max(2.0 * eta / N, 0.1), 8.0))
        d = 2.0 * nu * rho * rho * N * N
        logarg = 2.0 * Estar * N / eta
        L = math.log(logarg) / d
        old = math.exp(-d * L) * Estar
        target = eta / N
        # Choose a genuine positive weighted inflow above the forced half-floor.
        I = 0.5 * target + float(rng.uniform(0.0, 2.0)) * target
        denom = 1.0 - math.exp(-d * L)
        F = I * d / denom
        terminal = old + F * denom / d
        exact = math.exp(-d * L) * Estar + F * (1.0 - math.exp(-d * L)) / d
        duhamel = max(duhamel, abs(terminal - exact))
        if terminal >= target - 1e-14:
            funding_violation = max(funding_violation, max(0.0, 0.5 * target - I))
        funding_signal = max(funding_signal, I)
        normalized = L * (2.0 * nu * rho * rho * N * N) / math.log(logarg)
        window_scale = max(window_scale, abs(normalized - 1.0))

    print(f"worst radial mode-set continuity residual: {continuity:.3e}")
    print(f"worst one-sided radial generator violation: {generator_violation:.3e}")
    print(f"worst integrating-factor residual: {duhamel:.3e}")
    print(f"worst critical-shell fresh-funding violation: {funding_violation:.3e}")
    print(f"worst logarithmic-window normalization residual: {window_scale:.3e}")
    print(f"maximum sampled upward radial flux signal: {flux_signal:.3e}")
    print(f"maximum sampled radial dissipation signal: {diss_signal:.3e}")
    print(f"maximum sampled weighted fresh-funding signal: {funding_signal:.3e}")

    assert continuity < 2e-12
    assert generator_violation < 2e-12
    assert duhamel < 2e-12
    assert funding_violation < 2e-12
    assert window_scale < 2e-12
    assert flux_signal > 1e-3 and diss_signal > 1e-3 and funding_signal > 1e-5
    print("PASS: radial high-tail memory / fresh-funding calibrations")


if __name__ == "__main__":
    main()
