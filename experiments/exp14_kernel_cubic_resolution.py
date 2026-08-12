"""ACTION stress tests for kernel selector purity and cubic resolution identities.

These calibrations are adversarial checks only, never proof.
"""

import numpy as np


def triple(z0, z1, z2):
    return np.vdot(z0, np.cross(z1, z2))


def selector_pair_identity(rng):
    worst = 0.0
    min_mixed = np.inf
    for _ in range(1000):
        n = int(rng.integers(2, 9))
        w = rng.random(n)
        w /= w.sum()
        chi = rng.integers(0, 2, size=n).astype(float)
        alpha = float(w @ chi)
        var = alpha * (1.0 - alpha)
        pair = 0.0
        for i in range(n):
            for j in range(n):
                pair += 0.5 * w[i] * w[j] * (chi[i] - chi[j]) ** 2
        worst = max(worst, abs(var - pair))
        if 1e-12 < alpha < 1.0 - 1e-12:
            min_mixed = min(min_mixed, var)
    return worst, min_mixed


def cubic_resolution_identity(rng):
    worst = 0.0
    max_gap = 0.0
    for _ in range(400):
        n = int(rng.integers(2, 7))
        w = rng.random(n)
        w /= w.sum()
        phi = rng.normal(size=(3, n, 3)) + 1j * rng.normal(size=(3, n, 3))
        m = np.einsum("n,knc->kc", w, phi)
        same = sum(w[j] * triple(phi[0, j], phi[1, j], phi[2, j]) for j in range(n))
        ind = triple(m[0], m[1], m[2])
        xi = phi - m[:, None, :]
        corr = (
            sum(w[j] * triple(xi[0, j], xi[1, j], m[2]) for j in range(n))
            + sum(w[j] * triple(xi[0, j], m[1], xi[2, j]) for j in range(n))
            + sum(w[j] * triple(m[0], xi[1, j], xi[2, j]) for j in range(n))
            + sum(w[j] * triple(xi[0, j], xi[1, j], xi[2, j]) for j in range(n))
        )
        worst = max(worst, abs(same - ind - corr))
        max_gap = max(max_gap, abs(same - ind))
    return worst, max_gap


def parity_no_go(rng):
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    even = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=float)
    odd = even.copy()
    odd[:, 2] *= -1.0

    def moments(signs):
        phi = signs.T[:, :, None] * z[:, None, :]
        mean = phi.mean(axis=1)
        pair_sign = (signs.T @ signs) / len(signs)
        same = np.mean([triple(phi[0, j], phi[1, j], phi[2, j]) for j in range(len(signs))])
        second = np.mean(np.abs(phi) ** 2, axis=1)
        return mean, pair_sign, same, second

    me, pe, ze, se = moments(even)
    mo, po, zo, so = moments(odd)
    first_second_res = max(
        np.max(np.abs(me - mo)),
        np.max(np.abs(pe - po)),
        np.max(np.abs(se - so)),
    )
    flip_res = abs(ze + zo)
    signal = abs(ze - zo)
    return first_second_res, flip_res, signal


def triple_from_derivatives(v, g, h, b, a):
    # Direct generator evaluation of T using analytic first/second derivatives.
    drift = 0j
    diff_single = 0j
    diff_cross = 0j
    for alpha in range(len(b)):
        drift += b[alpha] * (
            triple(g[0, alpha], v[1], v[2])
            + triple(v[0], g[1, alpha], v[2])
            + triple(v[0], v[1], g[2, alpha])
        )
    for alpha in range(len(b)):
        for beta in range(len(b)):
            c = 0.5 * a[alpha, beta]
            diff_single += c * (
                triple(h[0, alpha, beta], v[1], v[2])
                + triple(v[0], h[1, alpha, beta], v[2])
                + triple(v[0], v[1], h[2, alpha, beta])
            )
            # Hessian product rule has both alpha-beta cross orderings.
            diff_cross += c * (
                triple(g[0, alpha], g[1, beta], v[2])
                + triple(g[0, beta], g[1, alpha], v[2])
                + triple(g[0, alpha], v[1], g[2, beta])
                + triple(g[0, beta], v[1], g[2, alpha])
                + triple(v[0], g[1, alpha], g[2, beta])
                + triple(v[0], g[1, beta], g[2, alpha])
            )
    return drift + diff_single + diff_cross


def carre_du_champ_identity(rng):
    worst = 0.0
    max_gamma = 0.0
    d = 4
    for _ in range(300):
        v = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        g = rng.normal(size=(3, d, 3)) + 1j * rng.normal(size=(3, d, 3))
        h = rng.normal(size=(3, d, d, 3)) + 1j * rng.normal(size=(3, d, d, 3))
        h = 0.5 * (h + np.swapaxes(h, 1, 2))
        b = rng.normal(size=d)
        B = rng.normal(size=(d, d))
        a = B @ B.T

        direct = triple_from_derivatives(v, g, h, b, a)

        L = np.empty((3, 3), dtype=complex)
        for i in range(3):
            L[i] = np.tensordot(b, g[i], axes=(0, 0)) + 0.5 * np.einsum("ab,abc->c", a, h[i])
        singles = triple(L[0], v[1], v[2]) + triple(v[0], L[1], v[2]) + triple(v[0], v[1], L[2])

        gamma = 0j
        for alpha in range(d):
            for beta in range(d):
                gamma += a[alpha, beta] * (
                    triple(g[0, alpha], g[1, beta], v[2])
                    + triple(g[0, alpha], v[1], g[2, beta])
                    + triple(v[0], g[1, alpha], g[2, beta])
                )
        worst = max(worst, abs(direct - singles - gamma))
        max_gamma = max(max_gamma, abs(gamma))
    return worst, max_gamma


def finite_state_resolution_transfer(rng):
    # Symmetric 4-state continuous-time chain; uniform weights are stationary.
    worst = 0.0
    max_transfer = 0.0
    n = 4
    w = np.ones(n) / n
    for _ in range(300):
        rates = rng.random((n, n))
        rates = 0.5 * (rates + rates.T)
        np.fill_diagonal(rates, 0.0)
        Q = rates.copy()
        np.fill_diagonal(Q, -Q.sum(axis=1))
        phi = rng.normal(size=(3, n, 3)) + 1j * rng.normal(size=(3, n, 3))
        dphi = np.einsum("ij,kjc->kic", Q, phi)
        m = np.einsum("n,knc->kc", w, phi)
        dm = np.einsum("n,knc->kc", w, dphi)
        same_dot = sum(
            w[j]
            * (
                triple(dphi[0, j], phi[1, j], phi[2, j])
                + triple(phi[0, j], dphi[1, j], phi[2, j])
                + triple(phi[0, j], phi[1, j], dphi[2, j])
            )
            for j in range(n)
        )
        ind_dot = triple(dm[0], m[1], m[2]) + triple(m[0], dm[1], m[2]) + triple(m[0], m[1], dm[2])
        delta_dot = same_dot - ind_dot

        gamma_full = np.empty(n, dtype=complex)
        for j in range(n):
            Tstate = np.array([triple(phi[0, k], phi[1, k], phi[2, k]) for k in range(n)])
            L_T = Q[j] @ Tstate
            singles = (
                triple(dphi[0, j], phi[1, j], phi[2, j])
                + triple(phi[0, j], dphi[1, j], phi[2, j])
                + triple(phi[0, j], phi[1, j], dphi[2, j])
            )
            gamma_full[j] = L_T - singles
        rhs = -w @ gamma_full  # reduced one-state Gamma^(3)=0
        worst = max(worst, abs(delta_dot - rhs))
        max_transfer = max(max_transfer, abs(rhs))
    return worst, max_transfer


def main():
    rng = np.random.default_rng(20260812)
    pair_res, min_mixed = selector_pair_identity(rng)
    cubic_res, max_gap = cubic_resolution_identity(rng)
    moment_res, flip_res, parity_signal = parity_no_go(rng)
    gamma_res, max_gamma = carre_du_champ_identity(rng)
    transfer_res, max_transfer = finite_state_resolution_transfer(rng)

    print(f"worst selector pair-disagreement residual: {pair_res:.3e}")
    print(f"minimum sampled genuinely mixed selector variance: {min_mixed:.3e}")
    print(f"worst conditional cubic-resolution residual: {cubic_res:.3e}")
    print(f"maximum sampled same-state/independent cubic gap: {max_gap:.3e}")
    print(f"even/odd parity first-second-moment residual: {moment_res:.3e}")
    print(f"even/odd parity cubic sign-flip residual: {flip_res:.3e}")
    print(f"even/odd parity signed-cubic separation: {parity_signal:.3e}")
    print(f"worst trilinear carre-du-champ residual: {gamma_res:.3e}")
    print(f"maximum sampled trilinear diffusion transfer magnitude: {max_gamma:.3e}")
    print(f"worst finite-state cubic-resolution transfer residual: {transfer_res:.3e}")
    print(f"maximum sampled finite-state cubic transfer magnitude: {max_transfer:.3e}")

    assert pair_res < 1e-12
    assert cubic_res < 1e-11
    assert moment_res < 1e-12
    assert flip_res < 1e-11
    assert parity_signal > 1e-3
    assert gamma_res < 1e-10
    assert transfer_res < 1e-10
    assert max_gap > 1e-2
    assert max_gamma > 1e-2
    assert max_transfer > 1e-2
    print("PASS: kernel selector/cubic-resolution adversarial calibrations")


if __name__ == "__main__":
    main()
