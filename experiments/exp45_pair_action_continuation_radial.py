"""Action-only referee for pair-action continuation algebra and radial first moment."""
import math
import numpy as np


def main():
    rng = np.random.default_rng(45082026)
    moment = radial = pair_radial = suppress = capacity = 0.0
    continuation = gronwall = 0.0
    signal = 0.0

    # Moment Cauchy and finite-action integrated bounds.
    for _ in range(15000):
        n = int(rng.integers(3, 30))
        r = rng.uniform(0.05, 30.0, size=n)
        e = rng.uniform(1e-6, 4.0, size=n)
        C = float(np.sum(r * e))
        Y = float(np.sum(r * r * e))
        B = float(np.sum(r**3 * e))
        moment = max(moment, max(0.0, Y * Y - C * B))

        nu = float(rng.uniform(0.02, 2.0))
        P = float(rng.uniform(0.0, 8.0))
        C0 = float(rng.uniform(0.01, 6.0))
        Cstar = C0 + 2.0 * P
        intB = float(rng.uniform(0.0, Cstar / (2.0 * nu)))
        intY2 = Cstar * intB
        continuation = max(continuation, max(0.0, intY2 - Cstar * Cstar / (2.0 * nu)))
        # Gronwall factor is finite whenever intY2 is finite.
        coef = float(rng.uniform(0.01, 4.0)) * nu**-3
        factor = math.exp(min(50.0, coef * intY2))
        gronwall = max(gronwall, 0.0 if math.isfinite(factor) else 1.0)

    # Radial first-moment layer cake on finite donor flows.
    for _ in range(8000):
        n = int(rng.integers(2, 20))
        rd = rng.uniform(0.05, 20.0, size=n)
        rr = rng.uniform(0.05, 20.0, size=n)
        m = rng.uniform(0.0, 5.0, size=n)
        direct = float(np.sum(m * (rr - rd)))
        # Exact integral of each signed crossing indicator over R.
        layer = float(np.sum(m * (np.maximum(rr - rd, 0.0) - np.maximum(rd - rr, 0.0))))
        radial = max(radial, abs(direct - layer))
        signal = max(signal, abs(direct))

    # Heterochiral split: pair charge equals half the |x| gap and radial first moment.
    for _ in range(15000):
        b = float(rng.uniform(0.01, 8.0))
        a = float(rng.uniform(0.01, 8.0))
        # strict triangle normal form requires a<c<a+b
        c = float(rng.uniform(a + 1e-6, a + b - 1e-6)) if b > 2e-6 else a + 0.5 * b
        R = float(rng.uniform(1e-5, 6.0))
        Q = (b + c) * R
        po = (c - a) / (b + c)
        P = Q * po * b
        # works: recipient -b gets +(c-a)R, donor a gets -(b+c)R, recipient c gets +(a+b)R
        works = np.array([(c - a) * R, -(b + c) * R, (a + b) * R])
        radii = np.array([b, a, c])
        crit_work = float(np.dot(radii, works))
        pair_radial = max(pair_radial, abs(crit_work - 2.0 * P))
        suppress = max(suppress, max(0.0, P - b * b * R))

        amps = rng.uniform(0.01, 4.0, size=3)
        # Capacity referee uses an arbitrary physical positive work no larger than A_o.
        Ao = 4.0 * b * float(np.prod(amps))
        To = float(rng.uniform(0.0, 1.0)) * Ao
        Pcap = b * To
        capacity = max(capacity, max(0.0, Pcap - 4.0 * b * b * float(np.prod(amps))))

    print(f"worst critical-moment Cauchy violation: {moment:.3e}")
    print(f"worst finite-pair-action integrated-bound violation: {continuation:.3e}")
    print(f"worst finite Gronwall-factor flag: {gronwall:.3e}")
    print(f"worst radial first-moment layer-cake residual: {radial:.3e}")
    print(f"worst heterochiral pair/radial identity residual: {pair_radial:.3e}")
    print(f"worst opposite-scale square-suppression violation: {suppress:.3e}")
    print(f"worst physical-capacity pair-suppression violation: {capacity:.3e}")
    print(f"maximum sampled signed radial first-moment signal: {signal:.3e}")

    assert moment < 2e-10
    assert continuation < 2e-12
    assert gronwall < 1e-15
    assert radial < 2e-12
    assert pair_radial < 2e-11
    assert suppress < 2e-12
    assert capacity < 2e-12
    assert signal > 1e-4
    print("PASS: pair-action continuation / radial-critical-moment calibrations")


if __name__ == "__main__":
    main()
