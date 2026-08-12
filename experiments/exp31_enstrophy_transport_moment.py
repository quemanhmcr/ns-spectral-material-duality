"""Adversarial stress for exact enstrophy-as-energy-transport moment algebra."""
import numpy as np


def main():
    rng = np.random.default_rng(31082026)
    moment_res = split_res = parabolic_res = corridor_violation = 0.0
    forward_signal = backward_signal = corridor_signal = 0.0

    for _ in range(2000):
        n = int(rng.integers(3, 10))
        E = rng.uniform(0.02, 4.0, size=n)
        kappa = rng.uniform(0.1, 40.0, size=n)
        nu = float(rng.uniform(0.02, 1.8))
        R = rng.uniform(0.0, 1.5, size=(n, n))
        np.fill_diagonal(R, 0.0)
        K = E[:, None] * R
        Edot = K.sum(axis=0) - K.sum(axis=1) - 2.0 * nu * kappa * E

        Yhalf_dot = float(np.dot(kappa, Edot))
        Z = 2.0 * float(np.dot(kappa * kappa, E))
        drift = float(np.sum((kappa[None, :] - kappa[:, None]) * K))
        moment_res = max(moment_res, abs(Yhalf_dot + nu * Z - drift))

        delta = kappa[None, :] - kappa[:, None]
        Fp = float(np.sum(np.maximum(delta, 0.0) * K))
        Fm = float(np.sum(np.maximum(-delta, 0.0) * K))
        split_res = max(split_res, abs(drift - (Fp - Fm)))
        forward_signal = max(forward_signal, Fp)
        backward_signal = max(backward_signal, Fm)

        tau = float(rng.uniform(0.01, 2.0))
        a = 2.0 * nu * tau * kappa
        adrift = float(np.sum((a[None, :] - a[:, None]) * K))
        parabolic_res = max(parabolic_res, abs(adrift - 2.0 * nu * tau * drift))

        beta = float(rng.uniform(0.4, 3.0))
        w = 1.0 - np.exp(-a)
        for i in range(n):
            for j in range(n):
                if 0.0 <= a[i] < a[j] <= beta and K[i, j] > 0:
                    lhs = w[j] - w[i]
                    rhs = np.exp(-beta) * (a[j] - a[i])
                    corridor_violation = max(corridor_violation, max(0.0, rhs - lhs))
                    corridor_signal = max(corridor_signal, lhs * K[i, j])

    print(f"worst enstrophy transport-moment residual: {moment_res:.3e}")
    print(f"worst forward/backward moment-split residual: {split_res:.3e}")
    print(f"worst parabolic-coordinate drift residual: {parabolic_res:.3e}")
    print(f"worst corridor heat-price violation: {corridor_violation:.3e}")
    print(f"maximum sampled up-frequency transport moment: {forward_signal:.3e}")
    print(f"maximum sampled down-frequency transport moment: {backward_signal:.3e}")
    print(f"maximum sampled corridor heat-progress signal: {corridor_signal:.3e}")

    assert moment_res < 3e-11
    assert split_res < 2e-11
    assert parabolic_res < 3e-11
    assert corridor_violation < 1e-12
    assert forward_signal > 1e-3
    assert backward_signal > 1e-3
    assert corridor_signal > 1e-5
    print("PASS: enstrophy / donor-energy transport-moment calibrations")


if __name__ == "__main__":
    main()
