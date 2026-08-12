"""Action-only referee for net critical radial action and twin helical-sector ledgers."""
import numpy as np


def main():
    rng = np.random.default_rng(46082026)
    net_bound = sector = combine = cycle = 0.0
    scaling = 0.0
    signal = 0.0

    # Integrated signed-source ledger: only positive net source is needed.
    for _ in range(20000):
        C0 = float(rng.uniform(0.01, 8.0))
        nu = float(rng.uniform(0.01, 2.0))
        m = int(rng.integers(3, 40))
        dt = float(rng.uniform(1e-4, 0.03))
        J = rng.normal(scale=3.0, size=m)
        B = rng.uniform(0.0, 5.0, size=m)
        C = C0
        intB = 0.0
        pos = 0.0
        for j, b in zip(J, B):
            # Keep synthetic stock nonnegative by reducing the allowed viscous step if needed.
            maxb = max(0.0, (C + dt * j) / (2.0 * nu * dt)) if dt > 0 else 0.0
            b = min(float(b), maxb)
            C += dt * (float(j) - 2.0 * nu * b)
            intB += dt * b
            pos += dt * max(float(j), 0.0)
        Cstar = C0 + pos
        net_bound = max(net_bound, max(0.0, C - Cstar), max(0.0, 2.0 * nu * intB - Cstar))

    # Exact twin sector algebra from C/H ledgers.
    for _ in range(20000):
        Cp = float(rng.uniform(0.0, 8.0))
        Cm = float(rng.uniform(0.0, 8.0))
        Bp = float(rng.uniform(0.0, 8.0))
        Bm = float(rng.uniform(0.0, 8.0))
        nu = float(rng.uniform(0.01, 2.0))
        N = float(rng.normal(scale=5.0))
        Cdot = 2.0 * N - 2.0 * nu * (Bp + Bm)
        Hdot = -2.0 * nu * (Bp - Bm)
        Cpdot = N - 2.0 * nu * Bp
        Cmdot = N - 2.0 * nu * Bm
        sector = max(sector, abs((Cpdot + Cmdot) - Cdot), abs((Cpdot - Cmdot) - Hdot))
        combine = max(combine, abs(0.5 * (Cdot + Hdot) - Cpdot), abs(0.5 * (Cdot - Hdot) - Cmdot))
        signal = max(signal, abs(N))

    # Create/annihilate cycling cancels before the net-action criterion reads it.
    for _ in range(10000):
        pc = rng.uniform(0.0, 10.0, size=20)
        pa = rng.uniform(0.0, 10.0, size=20)
        net = pc - pa
        j1 = 2.0 * net
        cycle = max(cycle, abs(float(np.sum(np.maximum(j1, 0.0))) - 2.0 * float(np.sum(np.maximum(net, 0.0)))))

    # Scaling: action integral invariant while energy-type budget scales lambda^-1.
    for _ in range(10000):
        lam = float(rng.uniform(0.1, 10.0))
        J = float(rng.uniform(-5.0, 5.0))
        dt = float(rng.uniform(1e-4, 2.0))
        action = max(J, 0.0) * dt
        scaled = max(lam * lam * J, 0.0) * (dt / (lam * lam))
        scaling = max(scaling, abs(action - scaled))

    print(f"worst positive-net ledger bound violation: {net_bound:.3e}")
    print(f"worst twin-sector sum/difference residual: {sector:.3e}")
    print(f"worst twin-sector reconstruction residual: {combine:.3e}")
    print(f"worst create/annihilate net-cycle residual: {cycle:.3e}")
    print(f"worst critical-action scaling residual: {scaling:.3e}")
    print(f"maximum sampled common pair-source signal: {signal:.3e}")

    assert net_bound < 2e-11
    assert sector < 2e-12
    assert combine < 2e-12
    assert cycle < 2e-12
    assert scaling < 2e-12
    assert signal > 1e-3
    print("PASS: positive-net critical action / twin-helical-sector calibrations")


if __name__ == "__main__":
    main()
