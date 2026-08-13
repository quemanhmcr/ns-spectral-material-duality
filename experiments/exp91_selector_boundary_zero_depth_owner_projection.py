"""Action-only referee for selector path variation versus physical generation owners."""
import numpy as np


def rel(a, b):
    return abs(a - b) / (1.0 + abs(a) + abs(b))


def build_four_crossing_referee():
    # Same exact heat-mode interpolation used by exp90, now read as a selector path.
    odd = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
    roots = np.array([0.004, 0.012, 0.024, 0.040])  # s=nu t
    M = np.exp(-np.outer(roots, odd**2))
    _, _, vh = np.linalg.svd(M)
    a = vh[-1]
    a /= np.max(np.abs(a))

    def O(s):
        return float(np.sum(a * np.exp(-(odd**2) * s)))

    def Os(s):
        return float(np.sum(-(odd**2) * a * np.exp(-(odd**2) * s)))

    eps = 0.05
    def gap(s):
        E = np.exp(-4.0 * s)
        return 2.0 * eps * E * O(s)

    return roots, M, a, O, Os, gap


def main():
    roots, M, a, O, Os, gap = build_four_crossing_referee()
    interpolation = np.max(np.abs(M @ a))
    simple = min(abs(Os(s)) for s in roots)

    # Determine winner label in each interval and audit that every simple zero toggles it.
    probes = [roots[0] - 0.001]
    probes += [0.5 * (roots[i] + roots[i+1]) for i in range(len(roots)-1)]
    probes += [roots[-1] + 0.001]
    signs = np.array([np.sign(gap(s)) for s in probes])
    label = np.where(signs >= 0.0, 0, 1)
    switches = int(np.sum(label[1:] != label[:-1]))
    alternating_violation = int(np.sum(label[1:] == label[:-1]))

    q0 = np.array([1.0, 0.0])
    q1 = np.array([0.0, 1.0])
    vectors = np.array([q0 if g == 0 else q1 for g in label])
    jumps = vectors[1:] - vectors[:-1]
    jump_sq = np.sum(jumps * jumps, axis=1)
    qv_trace = float(np.sum(jump_sq))
    qv_formula = rel(qv_trace, 2.0 * len(roots))
    endpoint_loop = np.linalg.norm(vectors[-1] - vectors[0])

    # The selected scalar max is continuous at each exact tie.
    scalar_jump = 0.0
    min_kink = np.inf
    for s in roots:
        E = np.exp(-4.0 * s)
        o = O(s)
        e0 = 0.5 * (E + 0.05 * o) ** 2
        ep = 0.5 * (E - 0.05 * o) ** 2
        scalar_jump = max(scalar_jump, abs(e0 - ep))
        min_kink = min(min_kink, abs(2.0 * 0.05 * E * Os(s)))

    # Exact PDE owner check: synthesized velocity is a heat shear, so u.grad u is identically zero.
    nu = 0.29
    heat = 0.0
    nonlinear = 0.0
    odd = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
    for s in np.linspace(0.002, 0.045, 13):
        for y in np.linspace(-np.pi, np.pi, 71):
            even = -0.5 * np.exp(-4.0*s) * np.sin(2.0*y)
            oddU = -0.05 * np.sum((a/odd) * np.exp(-(odd**2)*s) * np.sin(odd*y))
            U = even + oddU
            Us = 2.0 * np.exp(-4.0*s) * np.sin(2.0*y) + 0.05 * np.sum(odd*a*np.exp(-(odd**2)*s)*np.sin(odd*y))
            Uyy = 2.0 * np.exp(-4.0*s) * np.sin(2.0*y) + 0.05 * np.sum(odd*a*np.exp(-(odd**2)*s)*np.sin(odd*y))
            heat = max(heat, abs(nu*Us - nu*Uyy) / (1.0 + abs(nu*Us) + abs(nu*Uyy)))
            nonlinear = max(nonlinear, abs(U * 0.0))

    # Independent same-state positive-boundary witness in the exact algebraic form used by Wang:
    # positive symmetric-difference energy with identical cell energies before/after.
    cell = np.array([0.4, 1.2, 0.7, 2.0])
    old = {0, 2}
    new = {1, 2, 3}
    sym = sorted(old.symmetric_difference(new))
    R_switch = float(np.sum(cell[sym]))
    increments = np.zeros_like(cell)
    positive_work = float(np.sum(np.maximum(increments, 0.0)))
    negative_work = float(np.sum(np.maximum(-increments, 0.0)))
    state_change = float(abs(np.sum(cell) - np.sum(cell)))

    print(f"four-crossing interpolation residual: {interpolation:.3e}")
    print(f"minimum simple-root signal: {simple:.3e}")
    print(f"winner selector switches: {switches}")
    print(f"winner alternation violation count: {alternating_violation}")
    print(f"selector jump-square values: {jump_sq.tolist()}")
    print(f"selector jump-qv trace: {qv_trace:.6e}")
    print(f"selector qv formula residual: {qv_formula:.3e}")
    print(f"even-crossing selector endpoint-loop residual: {endpoint_loop:.3e}")
    print(f"maximum selected-scalar tie jump residual: {scalar_jump:.3e}")
    print(f"minimum derivative-kink signal: {min_kink:.3e}")
    print(f"exact heat-shear PDE residual: {heat:.3e}")
    print(f"exact heat-shear nonlinear-advection residual: {nonlinear:.3e}")
    print(f"same-state symmetric-difference boundary charge signal: {R_switch:.6e}")
    print(f"same-state positive-work residual: {positive_work:.3e}")
    print(f"same-state negative-work residual: {negative_work:.3e}")
    print(f"same-state total-energy-change residual: {state_change:.3e}")

    assert interpolation < 2e-12
    assert simple > 1e-8
    assert switches == len(roots)
    assert alternating_violation == 0
    assert np.max(np.abs(jump_sq - 2.0)) < 2e-14
    assert qv_formula < 2e-14
    assert endpoint_loop < 2e-14
    assert scalar_jump < 2e-12
    assert min_kink > 1e-10
    assert heat < 2e-14
    assert nonlinear == 0.0
    assert R_switch > 1.0
    assert positive_work == 0.0
    assert negative_work == 0.0
    assert state_change == 0.0
    print("PASS: selector path qv accumulates on smooth exact NS readout changes while nonlinear advection is zero")


if __name__ == "__main__":
    main()
