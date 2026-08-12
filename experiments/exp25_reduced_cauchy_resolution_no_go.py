"""Adversarial calibration for reduced-state Cauchy inverse contamination.

GitHub Actions stress test only; proofs are in docs/37_reduced_cauchy_inverse_resolution_no_go.md.
"""

import numpy as np


def covariance_gram(Ds, w):
    Dbar = np.tensordot(w, Ds, axes=(0, 0))
    Crow = sum(wi * (D @ D.T) for wi, D in zip(w, Ds)) - Dbar @ Dbar.T
    Ccol = sum(wi * (D.T @ D) for wi, D in zip(w, Ds)) - Dbar.T @ Dbar
    return Dbar, Crow, Ccol


def strain_pair(rng):
    worst_T = 0.0
    worst_delta = 0.0
    max_false = 0.0
    min_qv_combo = np.inf
    for _ in range(200):
        a = rng.uniform(0.2, 3.0)
        h = rng.uniform(1e-3, 0.2)
        x = a * h
        Dp = np.diag([np.exp(x), np.exp(-x), 1.0])
        Dm = np.diag([np.exp(-x), np.exp(x), 1.0])
        Dbar, Crow, _ = covariance_gram(np.array([Dp, Dm]), np.array([0.5, 0.5]))
        T = np.trace(Crow)
        delta = 1.0 - np.linalg.det(Dbar)
        expected_T = 2.0 * np.sinh(x) ** 2
        expected_delta = -np.sinh(x) ** 2
        worst_T = max(worst_T, abs(T - expected_T))
        worst_delta = max(worst_delta, abs(delta - expected_delta))
        qv_combo = abs(3.0 * T + 6.0 * delta)
        min_qv_combo = min(min_qv_combo, qv_combo)
        false_strain = (3.0 * T - 6.0 * delta) / (4.0 * h**3)
        max_false = max(max_false, false_strain)
    return worst_T, worst_delta, max_false, min_qv_combo


def rotation_pair(rng):
    worst_T = 0.0
    worst_delta = 0.0
    max_false = 0.0
    min_strain_combo = np.inf
    for _ in range(200):
        a = rng.uniform(0.2, 3.0)
        h = rng.uniform(1e-3, 0.2)
        x = a * h
        c, s = np.cos(x), np.sin(x)
        Rp = np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])
        Rm = np.array([[c, s, 0.0], [-s, c, 0.0], [0.0, 0.0, 1.0]])
        Dbar, Crow, _ = covariance_gram(np.array([Rp, Rm]), np.array([0.5, 0.5]))
        T = np.trace(Crow)
        delta = 1.0 - np.linalg.det(Dbar)
        expected_T = 2.0 * np.sin(x) ** 2
        expected_delta = np.sin(x) ** 2
        worst_T = max(worst_T, abs(T - expected_T))
        worst_delta = max(worst_delta, abs(delta - expected_delta))
        strain_combo = abs(3.0 * T - 6.0 * delta)
        min_strain_combo = min(min_strain_combo, strain_combo)
        false_qv = (3.0 * T + 6.0 * delta) / h**3
        max_false = max(max_false, false_qv)
    return worst_T, worst_delta, max_false, min_strain_combo


def total_covariance_partial_trace(rng):
    worst_row = 0.0
    worst_col = 0.0
    for _ in range(100):
        n = 6
        w = rng.random(n)
        w /= w.sum()
        means = rng.normal(size=(n, 3, 3))
        intrinsic_row = []
        intrinsic_col = []
        # Random PSD vector covariance per hidden state, realized by samples.
        total_samples = []
        for i in range(n):
            eps = rng.normal(size=(30, 3, 3)) * 0.2
            samples = means[i] + eps
            total_samples.append(samples)
            centered = samples - samples.mean(axis=0)
            intrinsic_row.append(sum(E @ E.T for E in centered) / len(centered))
            intrinsic_col.append(sum(E.T @ E for E in centered) / len(centered))

        mred = np.tensordot(w, means, axes=(0, 0))
        row_avg = sum(wi * C for wi, C in zip(w, intrinsic_row))
        col_avg = sum(wi * C for wi, C in zip(w, intrinsic_col))
        row_res = sum(wi * ((M - mred) @ (M - mred).T) for wi, M in zip(w, means))
        col_res = sum(wi * ((M - mred).T @ (M - mred)) for wi, M in zip(w, means))

        # Construct exact mixture second moments from the same chosen intrinsic moments.
        row_total = row_avg + row_res
        col_total = col_avg + col_res
        row_direct = sum(wi * (C + M @ M.T) for wi, C, M in zip(w, intrinsic_row, means)) - mred @ mred.T
        col_direct = sum(wi * (C + M.T @ M) for wi, C, M in zip(w, intrinsic_col, means)) - mred.T @ mred
        worst_row = max(worst_row, np.linalg.norm(row_total - row_direct))
        worst_col = max(worst_col, np.linalg.norm(col_total - col_direct))
    return worst_row, worst_col


def h2_dominates_h3():
    a = 1.2
    hs = np.array([1e-1, 5e-2, 2.5e-2, 1.25e-2])
    strain_vals = []
    rotation_vals = []
    for h in hs:
        x = a * h
        # Exact false inverse numerators scale h^2, so divided by h^3 scale ~1/h.
        strain_vals.append(3.0 * np.sinh(x) ** 2 / h**3)
        rotation_vals.append(12.0 * np.sin(x) ** 2 / h**3)
    strain_ratios = np.array(strain_vals[1:]) / np.array(strain_vals[:-1])
    rotation_ratios = np.array(rotation_vals[1:]) / np.array(rotation_vals[:-1])
    # Halving h should approximately double the false h^-1 signal.
    return np.max(abs(strain_ratios - 2.0)), np.max(abs(rotation_ratios - 2.0)), strain_vals[-1], rotation_vals[-1]


def main():
    rng = np.random.default_rng(25082026)
    sT, sd, sfalse, sqv = strain_pair(rng)
    rT, rd, rfalse, rstrain = rotation_pair(rng)
    row_res, col_res = total_covariance_partial_trace(rng)
    sscale, rscale, ssignal, rsignal = h2_dominates_h3()

    print(f"worst affine-strain resolution-trace residual: {sT:.3e}")
    print(f"worst affine-strain top-volume residual: {sd:.3e}")
    print(f"maximum false reduced strain-gradient inverse signal: {sfalse:.3e}")
    print(f"minimum affine-strain false Kelvin-qv numerator: {sqv:.3e}")
    print(f"worst rigid-rotation resolution-trace residual: {rT:.3e}")
    print(f"worst rigid-rotation top-volume residual: {rd:.3e}")
    print(f"maximum false reduced Kelvin-qv inverse signal: {rfalse:.3e}")
    print(f"minimum rigid-rotation false strain numerator: {rstrain:.3e}")
    print(f"worst reduced row total-covariance residual: {row_res:.3e}")
    print(f"worst reduced column total-covariance residual: {col_res:.3e}")
    print(f"strain h^-1 scaling ratio residual: {sscale:.3e}")
    print(f"rotation h^-1 scaling ratio residual: {rscale:.3e}")
    print(f"small-h false strain inverse signal: {ssignal:.3e}")
    print(f"small-h false Kelvin-qv inverse signal: {rsignal:.3e}")

    assert sT < 1e-12
    assert sd < 1e-12
    assert sfalse > 1.0
    assert sqv < 1e-10
    assert rT < 1e-12
    assert rd < 1e-12
    assert rfalse > 1.0
    assert rstrain < 1e-10
    assert row_res < 1e-11
    assert col_res < 1e-11
    assert sscale < 5e-2
    assert rscale < 5e-2
    assert ssignal > 10.0
    assert rsignal > 10.0
    print("PASS: reduced Cauchy inverse-resolution no-go calibrations")


if __name__ == "__main__":
    main()
