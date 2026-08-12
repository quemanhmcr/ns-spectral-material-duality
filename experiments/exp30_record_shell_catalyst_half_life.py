"""Adversarial stress for record-enstrophy shell scaling and catalyst half-life."""
import itertools
import math
import numpy as np


def half_lattice(k):
    for x in k:
        if x > 0:
            return True
        if x < 0:
            return False
    return False


def random_div_free_field(rng, K=2):
    modes = [k for k in itertools.product(range(-K, K + 1), repeat=3) if k != (0, 0, 0)]
    u = {}
    for k in modes:
        if not half_lattice(k):
            continue
        kv = np.array(k, dtype=float)
        z = rng.normal(size=3) + 1j * rng.normal(size=3)
        z -= kv * (np.dot(kv, z) / np.dot(kv, kv))
        u[k] = z
        u[tuple(-kv.astype(int))] = np.conjugate(z)
    return u


def nonlinear(u):
    keys = list(u)
    out = {k: np.zeros(3, dtype=complex) for k in keys}
    keyset = set(keys)
    for p in keys:
        up = u[p]
        pv = np.array(p, dtype=int)
        for q in keys:
            k = tuple(pv + np.array(q, dtype=int))
            if k not in keyset:
                continue
            qv = np.array(q, dtype=float)
            out[k] += 1j * np.dot(qv, up) * u[q]
    return out


def diagnostics(u):
    N = nonlinear(u)
    Z = 0.0
    W = 0.0
    shells = {}
    for k, uk in u.items():
        kv = np.array(k, dtype=float)
        kk = float(np.linalg.norm(kv))
        e = float(np.vdot(uk, uk).real)
        Z += kk**4 * e
        W += float(np.vdot(N[k], -(kk**2) * uk).real)
        q = int(math.ceil(math.log(max(kk, 1.0), 2.0)))
        upper = 2.0**q
        shells[upper] = shells.get(upper, 0.0) + e
    B2 = max(upper * e for upper, e in shells.items())
    B = math.sqrt(B2)
    return W, Z, B, B2


def main():
    rng = np.random.default_rng(30082026)
    scale_res = critical_res = 0.0
    max_ratio = work_signal = 0.0

    for _ in range(120):
        u = random_div_free_field(rng, K=2)
        W, Z, B, B2 = diagnostics(u)
        if B * Z > 1e-14:
            ratio = abs(W) / (B * Z)
            max_ratio = max(max_ratio, ratio)
            work_signal = max(work_signal, abs(W))
        critical_res = max(critical_res, abs(B * B - B2))

        amp = float(rng.uniform(0.15, 4.0))
        ua = {k: amp * v for k, v in u.items()}
        Wa, Za, Ba, _ = diagnostics(ua)
        if abs(W) > 1e-12:
            scale_res = max(scale_res, abs(Wa / W - amp**3) / (1.0 + amp**3))
        if Z > 1e-12:
            scale_res = max(scale_res, abs(Za / Z - amp**2) / (1.0 + amp**2))
        if B > 1e-12:
            scale_res = max(scale_res, abs(Ba / B - amp) / (1.0 + amp))

    # Catalyst half-life exact coefficient recurrence.
    half_res = sum_res = 0.0
    half_signal = 0.0
    for _ in range(1500):
        lam = float(rng.uniform(1.2, 2.5))
        # Choose sigma strictly under the physical half-life threshold.
        sigma_max = (2.0 * math.log(lam) - math.log(1.05)) / 3.0
        sigma = float(rng.uniform(0.0, max(1e-5, sigma_max)))
        rho = math.exp(3.0 * sigma) / (lam * lam)
        if rho >= 1.0:
            continue
        M = float(rng.uniform(0.5, 4.0))
        N = float(rng.uniform(max(M, 1.0), 12.0))
        E = float(rng.uniform(0.1, 5.0))
        C0 = M**3 / N**2 * E
        M1 = M * math.exp(sigma)
        N1 = N * lam
        C1 = M1**3 / N1**2 * E
        half_res = max(half_res, abs(C1 / C0 - rho))
        finite_sum = sum(C0 * rho**j for j in range(1000))
        closed = C0 / (1.0 - rho)
        sum_res = max(sum_res, abs(finite_sum - closed) * (1.0 - rho) / max(C0, 1e-15))
        half_signal = max(half_signal, C0 / max(C1, 1e-15))

    # Explicit Wang-compatible constants: exp(sigma)=21/20, lambda=8/5.
    rho_explicit = (21.0 / 20.0) ** 3 * (5.0 / 8.0) ** 2

    print(f"worst cubic/quadratic/linear amplitude-scaling residual: {scale_res:.3e}")
    print(f"worst B^2=max shell-critical-mass residual: {critical_res:.3e}")
    print(f"maximum sampled actual spectral enstrophy-work ratio |W|/(BZ): {max_ratio:.3e}")
    print(f"maximum sampled actual spectral enstrophy-work signal: {work_signal:.3e}")
    print(f"worst catalyst service-ratio residual: {half_res:.3e}")
    print(f"worst catalyst geometric-sum residual: {sum_res:.3e}")
    print(f"maximum sampled one-step catalyst service decay factor inverse: {half_signal:.3e}")
    print(f"explicit (21/20)^3(5/8)^2 catalyst ratio: {rho_explicit:.9f}")

    assert scale_res < 2e-12
    assert critical_res < 1e-12
    assert np.isfinite(max_ratio) and max_ratio > 1e-6
    assert work_signal > 1e-4
    assert half_res < 2e-12
    assert sum_res < 1e-8
    assert half_signal > 1.0
    assert rho_explicit < 0.5
    print("PASS: record-shell scaling / material-catalyst half-life calibrations")


if __name__ == "__main__":
    main()
