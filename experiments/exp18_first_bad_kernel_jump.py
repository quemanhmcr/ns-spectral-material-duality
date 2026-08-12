"""Adversarial calibration for first-bad Boolean realizability and finite cubic jumps.

GitHub Actions stress test only; proofs are in docs/29-30.
"""

import numpy as np


def triple(z0, z1, z2):
    return np.vdot(z0, np.cross(z1, z2))


def random_sl3_shear(rng):
    U = np.eye(3)
    U[0, 1], U[0, 2], U[1, 2] = rng.normal(size=3)
    L = np.eye(3)
    L[1, 0], L[2, 0], L[2, 1] = rng.normal(size=3)
    return U @ L


def boolean_pair_realizability(rng):
    worst = 0.0
    max_mixed = 0.0
    min_misclassification = 1.0

    for _ in range(300):
        n = rng.integers(3, 15)
        w = rng.random(n)
        w /= w.sum()
        chi = rng.integers(0, 2, size=n).astype(float)
        beta = float(w @ chi)
        pair = 0.0
        for i in range(n):
            for j in range(n):
                pair += 0.5 * w[i] * w[j] * (chi[i] - chi[j]) ** 2
        worst = max(worst, abs(beta * (1.0 - beta) - pair))
        if 1e-8 < beta < 1.0 - 1e-8:
            max_mixed = max(max_mixed, beta * (1.0 - beta))
            min_misclassification = min(
                min_misclassification,
                min(beta, 1.0 - beta),
            )

    return worst, max_mixed, min_misclassification


def finite_jump_identities(rng):
    worst_raw = 0.0
    worst_norm = 0.0
    max_phase_jump = 0.0

    for _ in range(300):
        n = 12
        w = rng.random(n)
        w /= w.sum()
        Zstate = rng.normal(size=n) + 1j * rng.normal(size=n)
        minus = rng.integers(0, 2, size=n).astype(float)
        plus = rng.integers(0, 2, size=n).astype(float)
        if w @ minus < 0.05 or w @ plus < 0.05:
            continue

        Zm = w @ (minus * Zstate)
        Zp = w @ (plus * Zstate)
        dchi = plus - minus
        worst_raw = max(worst_raw, abs((Zp - Zm) - w @ (dchi * Zstate)))

        am = float(w @ minus)
        ap = float(w @ plus)
        Zhm = Zm / am
        Zhp = Zp / ap
        rhs = (w @ (dchi * (Zstate - Zhm))) / ap
        worst_norm = max(worst_norm, abs((Zhp - Zhm) - rhs))

        if abs(Zhm) > 1e-8 and abs(Zhp) > 1e-8:
            max_phase_jump = max(max_phase_jump, abs(np.angle(Zhp / Zhm)))

    return worst_raw, worst_norm, max_phase_jump


def cauchy_event_jump_cancellation(rng):
    worst = 0.0
    max_jump = 0.0

    for _ in range(100):
        n = 10
        wgt = rng.random(n)
        wgt /= wgt.sum()
        Ds = [random_sl3_shear(rng) for _j in range(n)]
        ws = [
            [rng.normal(size=3) + 1j * rng.normal(size=3) for _j in range(n)]
            for _i in range(3)
        ]
        minus = rng.integers(0, 2, size=n).astype(float)
        plus = rng.integers(0, 2, size=n).astype(float)
        dchi = plus - minus

        jump_D = 0.0j
        jump_w = 0.0j
        for j in range(n):
            zD = triple(Ds[j] @ ws[0][j], Ds[j] @ ws[1][j], Ds[j] @ ws[2][j])
            zw = triple(ws[0][j], ws[1][j], ws[2][j])
            jump_D += wgt[j] * dchi[j] * zD
            jump_w += wgt[j] * dchi[j] * zw
        worst = max(worst, abs(jump_D - jump_w))
        max_jump = max(max_jump, abs(jump_w))

    return worst, max_jump


def main():
    rng = np.random.default_rng(18082026)
    pair_res, mixed_signal, min_misclass = boolean_pair_realizability(rng)
    raw_res, norm_res, phase_signal = finite_jump_identities(rng)
    cauchy_res, jump_signal = cauchy_event_jump_cancellation(rng)

    print(f"worst bad-flag pair-realizability residual: {pair_res:.3e}")
    print(f"maximum sampled mixed bad-flag variance: {mixed_signal:.3e}")
    print(f"minimum sampled unavoidable Boolean misclassification mass: {min_misclass:.3e}")
    print(f"worst unnormalized finite-selector jump residual: {raw_res:.3e}")
    print(f"worst normalized finite-selector jump residual: {norm_res:.3e}")
    print(f"maximum sampled finite event phase jump: {phase_signal:.3e}")
    print(f"worst Cauchy cancellation through selector jump residual: {cauchy_res:.3e}")
    print(f"maximum sampled finite cubic jump magnitude: {jump_signal:.3e}")

    assert pair_res < 1e-12
    assert mixed_signal > 1e-3
    assert min_misclass > 0.0
    assert raw_res < 1e-12
    assert norm_res < 1e-11
    assert phase_signal > 1e-2
    assert cauchy_res < 1e-10
    assert jump_signal > 1e-2
    print("PASS: first-bad Boolean-kernel / finite-cubic-jump calibrations")


if __name__ == "__main__":
    main()
