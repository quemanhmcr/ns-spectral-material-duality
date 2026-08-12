"""Adversarial calibration for growth/covariance non-equivalence.

GitHub Actions stress test only; proofs are in docs/33_growth_covariance_two_flow_no_go.md.
"""

import numpy as np


def affine_vortex_branch(rng):
    worst_growth = 0.0
    max_growth = 0.0
    covariance_norm = 0.0
    for _ in range(150):
        a = rng.uniform(0.05, 1.5)
        r0 = rng.uniform(0.1, 3.0)
        t = rng.uniform(0.0, 2.0)
        r = r0 * np.exp(2.0 * a * t)
        omega = np.array([0.0, 0.0, 2.0 * r])
        S = np.diag([-a, -a, 2.0 * a])
        stretching = omega @ S @ omega
        expected = 8.0 * a * r0 * r0 * np.exp(4.0 * a * t)
        worst_growth = max(worst_growth, abs(stretching / expected - 1.0))
        max_growth = max(max_growth, stretching)
        # Spatially uniform A means every conditional D sample is identical.
        Ds = np.repeat(np.eye(3)[None, :, :], 5, axis=0)
        vecs = Ds.reshape(5, 9)
        covariance_norm = max(covariance_norm, np.linalg.norm(np.cov(vecs, rowvar=False, bias=True)))
    return worst_growth, max_growth, covariance_norm


def shear_peak_branch(rng):
    worst_growth = 0.0
    min_decay = 0.0
    min_var = np.inf
    worst_var_formula = 0.0

    for _ in range(200):
        nu = rng.uniform(0.05, 1.0)
        k = rng.uniform(0.4, 3.0)
        t = rng.uniform(0.0, 2.0)
        h = rng.uniform(0.02, 1.5)
        alpha = nu * k * k
        E = np.exp(-alpha * t)

        # y*=pi/(2k): stretching=0, grad omega=0, Delta e=-k^4 E^2.
        growth = -nu * (k**4) * (E**2)
        expected = -nu * (k**4) * (E**2)
        worst_growth = max(worst_growth, abs(growth / expected - 1.0))
        min_decay = min(min_decay, growth)

        var = (k**2) * np.exp(-2.0 * alpha * t) * (
            (np.cosh(2.0 * alpha * h) - 1.0) / (2.0 * alpha * alpha) - h * h
        )
        min_var = min(min_var, var)

        # Equivalent positive series witness after factoring h^2.
        x = alpha * h
        scaled = (np.cosh(2.0 * x) - 1.0) / (2.0 * x * x) - 1.0
        reconstructed = (k**2) * np.exp(-2.0 * alpha * t) * h * h * scaled
        scale = max(1.0, abs(var))
        worst_var_formula = max(worst_var_formula, abs(var - reconstructed) / scale)

    return worst_growth, min_decay, min_var, worst_var_formula


def orientation_separation():
    e2 = np.array([0.0, 1.0, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])
    C = np.outer(e2, e2)
    return abs(e3 @ C @ e3), np.linalg.norm(C)


def main():
    rng = np.random.default_rng(21082026)
    aff_res, aff_growth, aff_cov = affine_vortex_branch(rng)
    shear_res, shear_decay, shear_var, shear_formula_res = shear_peak_branch(rng)
    vorticity_cov_proj, cov_norm = orientation_separation()

    print(f"worst affine positive-growth relative residual: {aff_res:.3e}")
    print(f"maximum sampled affine positive peak-growth signal: {aff_growth:.3e}")
    print(f"affine deformation covariance norm: {aff_cov:.3e}")
    print(f"worst shear peak-decay relative residual: {shear_res:.3e}")
    print(f"most negative sampled shear peak-growth rate: {shear_decay:.3e}")
    print(f"minimum sampled positive shear deformation variance: {shear_var:.3e}")
    print(f"worst shear variance formula reconstruction residual: {shear_formula_res:.3e}")
    print(f"shear covariance projection onto vorticity direction: {vorticity_cov_proj:.3e}")
    print(f"shear covariance normalized tensor norm: {cov_norm:.3e}")

    assert aff_res < 1e-12
    assert aff_growth > 1e-2
    assert aff_cov < 1e-14
    assert shear_res < 1e-12
    assert shear_decay < -1e-4
    assert shear_var > 0.0
    assert shear_formula_res < 1e-10
    assert vorticity_cov_proj < 1e-14
    assert cov_norm > 0.5
    print("PASS: exact NS growth/covariance two-flow no-go calibrations")


if __name__ == "__main__":
    main()
