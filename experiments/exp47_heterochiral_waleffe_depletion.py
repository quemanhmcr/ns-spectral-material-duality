"""Action-only referee for exact heterochiral Waleffe pair-action depletion/no-go."""
import math
import numpy as np


def area(a, b, c):
    s = 0.5 * (a + b + c)
    return math.sqrt(max(0.0, s * (s-a) * (s-b) * (s-c)))


def eta_pair(a, b, c):
    K = max(a, b, c)
    return math.sqrt(2.0) * area(a,b,c) * (c-a) * (a+c-b) / (a*c*K*K)


def main():
    rng = np.random.default_rng(47082026)
    formula = low_donor = low_opp = comparable = 0.0
    signal = 0.0

    for _ in range(50000):
        # Generate a strict triangle in normal form a<c.
        a = float(rng.uniform(0.02, 10.0))
        b = float(rng.uniform(0.02, 10.0))
        lo = abs(a-b) + 1e-5
        hi = a+b-1e-5
        if hi <= max(a, lo):
            continue
        c = float(rng.uniform(max(a+1e-5, lo), hi))
        D = area(a,b,c)
        g = D * (a+c-b) / (2.0 * math.sqrt(2.0) * a*b*c)
        prod = float(rng.uniform(1e-4, 5.0))
        Rabs = 4.0 * g * prod
        P = b * (c-a) * Rabs
        rhs = math.sqrt(2.0) * D * (c-a) * (a+c-b) / (a*c) * prod
        formula = max(formula, abs(P-rhs))
        K = max(a,b,c)
        signal = max(signal, P/(K*K*prod))

        if a == min(a,b,c):
            low_donor = max(low_donor, max(0.0, P - math.sqrt(2.0)*a*K*prod))
        if b == min(a,b,c):
            low_opp = max(low_opp, max(0.0, P - math.sqrt(2.0)*b*b*prod))

    # Explicit comparable witness a=b=3/4, c=1.
    a=b=0.75
    c=1.0
    eta = eta_pair(a,b,c)
    target = math.sqrt(10.0)/24.0
    comparable = abs(eta-target)

    print(f"worst exact heterochiral pair-capacity formula residual: {formula:.3e}")
    print(f"worst low-donor aK depletion violation: {low_donor:.3e}")
    print(f"worst low-opposite b^2 depletion violation: {low_opp:.3e}")
    print(f"explicit comparable eta residual: {comparable:.3e}")
    print(f"explicit comparable eta_pair: {eta:.9f}")
    print(f"maximum sampled dimensionless pair-capacity signal: {signal:.3e}")

    assert formula < 2e-12
    assert low_donor < 2e-12
    assert low_opp < 2e-12
    assert comparable < 2e-12
    assert eta > 0.13
    assert signal > 0.02
    print("PASS: heterochiral Waleffe depletion / comparable-core no-go calibrations")


if __name__ == '__main__':
    main()
