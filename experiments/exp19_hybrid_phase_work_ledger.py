"""Adversarial calibration for the hybrid continuous/event phase-work ledger.

GitHub Actions stress test only; proof is in docs/31_hybrid_phase_work_ledger.md.
"""

import numpy as np


def build_history(rng, n_intervals=5):
    z = rng.normal() + 1j * rng.normal()
    if abs(z) < 0.5:
        z += 1.0 + 0.3j
    initial = z
    continuous_log = 0.0j
    event_logs = []
    owner_abs_amp = 0.0
    owner_abs_phase = 0.0
    event_abs_amp = 0.0
    event_abs_phase = 0.0

    for j in range(n_intervals):
        # Each interval uses three constant logarithmic owner rates over dt.
        dt = rng.uniform(0.1, 1.0)
        rates = rng.normal(size=3) + 1j * rng.normal(size=3)
        total_rate = rates.sum()
        z = z * np.exp(total_rate * dt)
        continuous_log += total_rate * dt
        owner_abs_amp += np.abs(rates.real).sum() * dt
        owner_abs_phase += np.abs(rates.imag).sum() * dt

        if j < n_intervals - 1:
            # Finite nonzero event multiplier, allowing large phase jumps.
            amp = np.exp(rng.normal(scale=0.8))
            phase = rng.uniform(-np.pi, np.pi)
            q = amp * np.exp(1j * phase)
            z_before = z
            z = q * z
            event_logs.append(np.log(amp) + 1j * phase)
            event_abs_amp += abs(np.log(abs(z / z_before)))
            event_abs_phase += abs(np.angle(z / z_before))

    return {
        "initial": initial,
        "final": z,
        "continuous_log": continuous_log,
        "event_logs": event_logs,
        "owner_abs_amp": owner_abs_amp,
        "owner_abs_phase": owner_abs_phase,
        "event_abs_amp": event_abs_amp,
        "event_abs_phase": event_abs_phase,
    }


def exact_hybrid_log_identities(rng):
    worst_amp = 0.0
    worst_phase_mod = 0.0
    worst_amp_payment = 0.0
    worst_phase_metric = 0.0
    max_event_phase = 0.0

    for _ in range(500):
        h = build_history(rng)
        z0, z1 = h["initial"], h["final"]
        cont = h["continuous_log"]
        evt = sum(h["event_logs"], 0.0j)

        lhs_amp = np.log(abs(z1) / abs(z0))
        rhs_amp = cont.real + evt.real
        worst_amp = max(worst_amp, abs(lhs_amp - rhs_amp))

        # Phase identity is exact modulo 2pi if principal endpoint Arg is used.
        lhs_phase = np.angle(z1 / z0)
        rhs_phase = cont.imag + evt.imag
        phase_mod_res = abs(np.angle(np.exp(1j * (lhs_phase - rhs_phase))))
        worst_phase_mod = max(worst_phase_mod, phase_mod_res)

        total_amp_action = h["owner_abs_amp"] + h["event_abs_amp"]
        worst_amp_payment = max(
            worst_amp_payment,
            max(0.0, abs(lhs_amp) - total_amp_action),
        )

        endpoint_dist = abs(np.angle(z1 / z0))
        total_phase_action = h["owner_abs_phase"] + h["event_abs_phase"]
        worst_phase_metric = max(
            worst_phase_metric,
            max(0.0, endpoint_dist - total_phase_action),
        )
        if h["event_logs"]:
            max_event_phase = max(max_event_phase, max(abs(v.imag) for v in h["event_logs"]))

    return worst_amp, worst_phase_mod, worst_amp_payment, worst_phase_metric, max_event_phase


def threshold_payment_examples():
    c_hi = 0.95
    c_lo = 0.5
    rho = 0.4
    delta_theta = np.arccos(c_lo) - np.arccos(c_hi)

    # Pure discrete amplitude loss.
    z0 = 1.0 + 0.0j
    z1 = rho * z0
    amp_action = abs(np.log(abs(z1) / abs(z0)))
    amp_res = abs(amp_action - np.log(1.0 / rho))

    # Pure discrete phase exit from the edge of high-favorable set to low edge.
    theta0 = np.arccos(c_hi)
    theta1 = np.arccos(c_lo)
    q = np.exp(1j * (theta1 - theta0))
    phase_action = abs(np.angle(q))
    phase_res = abs(phase_action - delta_theta)

    # Favorable persistence if neither threshold is crossed.
    kappa_star = 1.7
    Zmag0 = 2.3
    Zmag = 0.8 * Zmag0
    c = 0.7
    work = kappa_star * c * Zmag
    lower = kappa_star * c_lo * rho * Zmag0
    persistence_margin = work - lower

    return amp_res, phase_res, persistence_margin, delta_theta


def event_reweighting_complex_jump(rng):
    worst = 0.0
    max_jump = 0.0
    for _ in range(200):
        n = 10
        p = rng.random(n)
        p /= p.sum()
        Z = rng.normal(size=n) + 1j * rng.normal(size=n)
        before = rng.integers(0, 2, size=n).astype(float)
        after = rng.integers(0, 2, size=n).astype(float)
        d = after - before
        Zm = p @ (before * Z)
        Zp = p @ (after * Z)
        rhs = p @ (d * Z)
        worst = max(worst, abs((Zp - Zm) - rhs))
        max_jump = max(max_jump, abs(rhs))
    return worst, max_jump


def main():
    rng = np.random.default_rng(19082026)
    amp_res, phase_res, amp_pay_res, phase_metric_res, event_phase = exact_hybrid_log_identities(rng)
    threshold_amp_res, threshold_phase_res, persistence_margin, delta_theta = threshold_payment_examples()
    event_res, event_signal = event_reweighting_complex_jump(rng)

    print(f"worst hybrid log-amplitude identity residual: {amp_res:.3e}")
    print(f"worst hybrid lifted-phase modulo residual: {phase_res:.3e}")
    print(f"worst hybrid amplitude path-length deficit: {amp_pay_res:.3e}")
    print(f"worst hybrid phase geodesic path-length deficit: {phase_metric_res:.3e}")
    print(f"maximum sampled discrete phase jump: {event_phase:.3e}")
    print(f"pure-event amplitude threshold residual: {threshold_amp_res:.3e}")
    print(f"pure-event phase threshold residual: {threshold_phase_res:.3e}")
    print(f"favorable-work persistence margin: {persistence_margin:.3e}")
    print(f"angular threshold payment delta_theta: {delta_theta:.6f}")
    print(f"worst event reweighting jump residual: {event_res:.3e}")
    print(f"maximum sampled event reweighting jump magnitude: {event_signal:.3e}")

    assert amp_res < 1e-12
    assert phase_res < 1e-12
    assert amp_pay_res < 1e-12
    assert phase_metric_res < 1e-12
    assert event_phase > 1.0
    assert threshold_amp_res < 1e-12
    assert threshold_phase_res < 1e-12
    assert persistence_margin > 0.0
    assert event_res < 1e-12
    assert event_signal > 1e-2
    print("PASS: hybrid continuous/event phase-work ledger calibrations")


if __name__ == "__main__":
    main()
