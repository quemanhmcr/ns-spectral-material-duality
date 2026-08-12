"""Adversarial calibration for the vectorized Cauchy inverse dictionary.

GitHub Actions stress test only; proofs are in docs/35_vectorized_cauchy_inverse_dictionary.md.
"""

import numpy as np


def cross_matrix(v):
    x, y, z = v
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def exact_partial_trace_identity(rng):
    worst_row = 0.0
    worst_col = 0.0
    for _ in range(100):
        n = 7
        weights = rng.random(n)
        weights /= weights.sum()
        Ds = rng.normal(size=(n, 3, 3))
        Dbar = np.tensordot(weights, Ds, axes=(0, 0))
        vecs = Ds.reshape(n, 9)
        vbar = weights @ vecs
        centered = vecs - vbar
        Sigma = sum(w * np.outer(v, v) for w, v in zip(weights, centered))
        S4 = Sigma.reshape(3, 3, 3, 3)

        Crow_from_sigma = np.zeros((3, 3))
        Ccol_from_sigma = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                Crow_from_sigma[i, j] = sum(S4[i, a, j, a] for a in range(3))
        for a in range(3):
            for b in range(3):
                Ccol_from_sigma[a, b] = sum(S4[i, a, i, b] for i in range(3))

        Crow = sum(w * (D @ D.T) for w, D in zip(weights, Ds)) - Dbar @ Dbar.T
        Ccol = sum(w * (D.T @ D) for w, D in zip(weights, Ds)) - Dbar.T @ Dbar
        worst_row = max(worst_row, np.linalg.norm(Crow_from_sigma - Crow))
        worst_col = max(worst_col, np.linalg.norm(Ccol_from_sigma - Ccol))
    return worst_row, worst_col


def short_horizon_duality(rng):
    worst_even = 0.0
    worst_odd = 0.0
    worst_strain_recovery = 0.0
    max_odd_signal = 0.0
    nu = 0.8
    h = 0.2

    for _ in range(200):
        row = np.zeros((3, 3))
        col = np.zeros((3, 3))
        strain = np.zeros((3, 3))
        Gamma = np.zeros((3, 3))
        cross = np.zeros((3, 3))
        for _mu in range(3):
            P = rng.normal(size=(3, 3))
            P = 0.5 * (P + P.T)
            g = rng.normal(size=3)
            Q = 0.5 * cross_matrix(g)
            G = P + Q
            row += G.T @ G
            col += G @ G.T
            strain += P @ P
            Gamma += 2.0 * nu * np.outer(g, g)
            cross += P @ Q - Q @ P

        pref = (2.0 * nu / 3.0) * h**3
        Crow = pref * row
        Ccol = pref * col
        Ceven = 0.5 * (Crow + Ccol)
        Codd = 0.5 * (Crow - Ccol)
        Crot = (h**3 / 12.0) * (np.trace(Gamma) * np.eye(3) - Gamma)
        Cstrain = pref * strain
        Ccross = pref * cross

        worst_even = max(worst_even, np.linalg.norm(Ceven - (Cstrain + Crot)))
        worst_odd = max(worst_odd, np.linalg.norm(Codd - Ccross))
        worst_strain_recovery = max(worst_strain_recovery, np.linalg.norm((Ceven - Crot) - Cstrain))
        max_odd_signal = max(max_odd_signal, np.linalg.norm(Codd))

    return worst_even, worst_odd, worst_strain_recovery, max_odd_signal


def scalar_inverse_dictionary(rng):
    worst_gamma = 0.0
    worst_strain = 0.0
    max_delta = 0.0
    nu = 0.65
    h = 0.17

    for _ in range(300):
        a = 0.0
        b = 0.0
        row_trace_sum = 0.0
        Gamma = np.zeros((3, 3))
        for _mu in range(3):
            P = rng.normal(size=(3, 3))
            P = 0.5 * (P + P.T)
            g = rng.normal(size=3)
            Q = 0.5 * cross_matrix(g)
            G = P + Q
            a += np.linalg.norm(P, "fro") ** 2
            b += np.linalg.norm(Q, "fro") ** 2
            row_trace_sum += np.trace(G.T @ G)
            Gamma += 2.0 * nu * np.outer(g, g)

        T = (2.0 * nu / 3.0) * h**3 * row_trace_sum
        delta = (nu / 3.0) * h**3 * (b - a)
        gamma_rec = (3.0 * T + 6.0 * delta) / h**3
        strain_rec = (3.0 * T - 6.0 * delta) / (4.0 * h**3)
        worst_gamma = max(worst_gamma, abs(gamma_rec - np.trace(Gamma)))
        worst_strain = max(worst_strain, abs(strain_rec - nu * a))
        max_delta = max(max_delta, abs(delta))

    return worst_gamma, worst_strain, max_delta


def shear_dual_projection(rng):
    worst_row = 0.0
    worst_col = 0.0
    worst_odd = 0.0
    max_signal = 0.0
    for _ in range(150):
        c = rng.normal()
        G = np.zeros((3, 3))
        G[0, 1] = c
        row = G.T @ G
        col = G @ G.T
        target_row = c * c * np.diag([0.0, 1.0, 0.0])
        target_col = c * c * np.diag([1.0, 0.0, 0.0])
        target_odd = 0.5 * c * c * np.diag([-1.0, 1.0, 0.0])
        worst_row = max(worst_row, np.linalg.norm(row - target_row))
        worst_col = max(worst_col, np.linalg.norm(col - target_col))
        worst_odd = max(worst_odd, np.linalg.norm(0.5 * (row - col) - target_odd))
        max_signal = max(max_signal, np.linalg.norm(target_odd))
    return worst_row, worst_col, worst_odd, max_signal


def main():
    rng = np.random.default_rng(23082026)
    row_res, col_res = exact_partial_trace_identity(rng)
    even_res, odd_res, strain_res, odd_signal = short_horizon_duality(rng)
    gamma_res, scalar_strain_res, delta_signal = scalar_inverse_dictionary(rng)
    shear_row_res, shear_col_res, shear_odd_res, shear_signal = shear_dual_projection(rng)

    print(f"worst exact row partial-trace residual: {row_res:.3e}")
    print(f"worst exact column partial-trace residual: {col_res:.3e}")
    print(f"worst transpose-even sector residual: {even_res:.3e}")
    print(f"worst transpose-odd sector residual: {odd_res:.3e}")
    print(f"worst strain-square tensor recovery residual: {strain_res:.3e}")
    print(f"maximum sampled orientation-coupling sector magnitude: {odd_signal:.3e}")
    print(f"worst scalar Kelvin-qv trace inverse residual: {gamma_res:.3e}")
    print(f"worst scalar strain-gradient inverse residual: {scalar_strain_res:.3e}")
    print(f"maximum sampled signed determinant-defect coefficient signal: {delta_signal:.3e}")
    print(f"worst shear row-Gram projection residual: {shear_row_res:.3e}")
    print(f"worst shear column-Gram projection residual: {shear_col_res:.3e}")
    print(f"worst shear orientation-coupling recovery residual: {shear_odd_res:.3e}")
    print(f"maximum sampled shear orientation-coupling signal: {shear_signal:.3e}")

    assert row_res < 1e-11
    assert col_res < 1e-11
    assert even_res < 1e-11
    assert odd_res < 1e-11
    assert strain_res < 1e-11
    assert odd_signal > 1e-3
    assert gamma_res < 1e-10
    assert scalar_strain_res < 1e-10
    assert delta_signal > 1e-5
    assert shear_row_res < 1e-12
    assert shear_col_res < 1e-12
    assert shear_odd_res < 1e-12
    assert shear_signal > 1e-3
    print("PASS: vectorized Cauchy dual-partial-trace inverse calibrations")


if __name__ == "__main__":
    main()
