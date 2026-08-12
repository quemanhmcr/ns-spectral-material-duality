"""Adversarial stress for stopped parabolic-lineage and finite-depth identities."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(28082026)
    mass_res = stopped_res = price_res = hazard_res = depth_res = 0.0
    progress_signal = collapse_signal = reverse_signal = 0.0

    # Instantaneous stopped-lineage ledger.
    for _ in range(1000):
        n = int(rng.integers(3, 8))
        m = rng.uniform(0.02, 2.0, size=n)
        d = rng.uniform(0.1, 8.0, size=n)
        tau = float(rng.uniform(0.05, 1.5))
        q = np.exp(-d * tau)
        w = 1.0 - q
        wdot = -d * q
        r = rng.uniform(0.0, 1.2, size=(n, n))
        np.fill_diagonal(r, 0.0)

        # Only nondecreasing heat-defect jumps continue; all others are absorbing exits.
        cont = w[None, :] >= w[:, None]
        np.fill_diagonal(cont, False)
        incoming = np.sum((m[:, None] * r * cont), axis=0)
        total_out = r.sum(axis=1)
        mdot = incoming - m * total_out - d * m

        exit_mask = ~cont
        np.fill_diagonal(exit_mask, False)
        X = np.sum(m[:, None] * r * exit_mask)
        D = np.dot(d, m)
        mass_res = max(mass_res, abs(mdot.sum() + D + X))

        F = np.sum((w[None, :] - w[:, None]) * (m[:, None] * r * cont))
        Xw = np.sum(w[:, None] * (m[:, None] * r * exit_mask))
        Bdot = np.dot(wdot, m) + np.dot(w, mdot)
        stopped_res = max(stopped_res, abs(Bdot - (F - D - Xw)))
        progress_signal = max(progress_signal, F)

    # Uniform parabolic price on a signed-good-compatible corridor.
    alpha = 0.50
    beta = 1.60
    lam = 8.0 / 5.0
    Lam = 5.0 / 3.0
    grid = np.linspace(alpha, beta, 20001)
    c_price = float(np.min(np.exp(-grid) - np.exp(-(lam * lam) * grid)))
    for _ in range(2000):
        a = float(rng.uniform(alpha, beta))
        ratio = float(rng.uniform(lam, Lam))
        delta_w = math.exp(-a) - math.exp(-(ratio * ratio) * a)
        price_res = max(price_res, max(0.0, c_price - delta_w))

    # Exact pathwise hazard identity: donor event coordinate is reset by clock drift.
    for _ in range(500):
        n = int(rng.integers(2, 30))
        a_event = float(rng.uniform(alpha, 0.55))
        ratios = rng.uniform(lam, Lam, size=n)
        jumps = (ratios * ratios - 1.0) * a_event
        # After every jump except the last, continuous heat-clock drift returns a to a_event.
        hazard = float(np.sum(jumps[:-1]))
        a_start = a_event
        a_end = a_event + jumps[-1]
        identity = a_start - a_end + float(np.sum(jumps))
        hazard_res = max(hazard_res, abs(hazard - identity))
        c_jump = (lam * lam - 1.0) * alpha
        lower = n * c_jump - beta
        # Our explicit path has donor a_event >= alpha and terminal a <= beta.
        if a_end <= beta + 1e-12:
            hazard_res = max(hazard_res, max(0.0, lower - hazard))

    # Finite-depth critical-floor contradiction.
    c_jump = (lam * lam - 1.0) * alpha
    gap = c_jump - math.log(Lam)
    assert gap > 0.0
    for _ in range(500):
        M0 = float(rng.uniform(0.5, 20.0))
        N0 = float(rng.uniform(1.0, 20.0))
        eta = float(rng.uniform(0.01, 0.4))
        bound = (math.log(M0 * N0 / eta) + beta) / gap
        n = max(0, int(math.floor(bound)) + 2)
        survival_upper = M0 * math.exp(beta - c_jump * n)
        critical_lower = eta / (N0 * (Lam ** n))
        depth_res = max(depth_res, max(0.0, survival_upper - critical_lower))

    # No-go if the lower parabolic face collapses: infinitely many geometric jumps can have finite hazard.
    lam0 = 1.6
    nu = 0.7
    N0 = 1.3
    C = 0.8
    hazards = []
    total = 0.0
    for n in range(80):
        N = N0 * (lam0 ** n)
        tau_n = C * (lam0 ** (-4 * n))
        tau_next = C * (lam0 ** (-4 * (n + 1)))
        total += 2.0 * nu * N * N * (tau_n - tau_next)
        hazards.append(total)
    collapse_signal = hazards[-1]
    collapse_tail = hazards[-1] - hazards[39]

    # A forward jump followed immediately by its reverse refunds the heat coordinate with zero clock hazard.
    a = 0.7
    forward = (lam0 * lam0 - 1.0) * a
    a_high = lam0 * lam0 * a
    reverse = (1.0 / (lam0 * lam0) - 1.0) * a_high
    reverse_signal = abs(forward)
    reverse_res = abs(forward + reverse)

    # Without an upper scale-ratio bound, a super-exponential critical floor can outrun survival loss.
    c = 0.8
    n = 30
    survival = math.exp(-c * n)
    floor_no_upper = math.exp(-2.0 * c * n)
    no_upper_margin = survival - floor_no_upper

    print(f"worst stopped-lineage mass residual: {mass_res:.3e}")
    print(f"worst stopped heat-defect identity residual: {stopped_res:.3e}")
    print(f"worst uniform parabolic-price violation: {price_res:.3e}")
    print(f"worst pathwise killing-hazard residual: {hazard_res:.3e}")
    print(f"worst finite-depth contradiction residual: {depth_res:.3e}")
    print(f"maximum sampled internal progress signal: {progress_signal:.3e}")
    print(f"collapsed-lower-face finite hazard after 80 jumps: {collapse_signal:.6f}")
    print(f"collapsed-lower-face tail hazard after jump 40: {collapse_tail:.3e}")
    print(f"reverse-jump refund residual: {reverse_res:.3e}")
    print(f"forward/reverse heat-coordinate signal: {reverse_signal:.3e}")
    print(f"no-upper-ratio survival-minus-floor margin: {no_upper_margin:.3e}")
    print(f"signed-good c_jump-log(Lambda) gap: {gap:.6f}")

    assert mass_res < 2e-11
    assert stopped_res < 3e-11
    assert price_res < 1e-12
    assert hazard_res < 1e-10
    assert depth_res < 1e-12
    assert progress_signal > 1e-3
    assert collapse_signal > 0.0 and collapse_tail < 1e-8
    assert reverse_res < 1e-12 and reverse_signal > 1e-2
    assert no_upper_margin > 0.0
    print("PASS: stopped parabolic-lineage / killing-depth calibrations")


if __name__ == "__main__":
    main()
