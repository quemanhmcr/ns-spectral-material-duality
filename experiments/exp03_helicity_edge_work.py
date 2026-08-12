from __future__ import annotations

import math
import numpy as np

from src.bridge_geometry import (
    deform_covector,
    edge_work,
    helical_basis,
    metric_parent_ratios,
    metric_uv,
    planar_optimal_triad,
    planar_strain_F,
    transverse_frame,
)


def helicity_conversion_check() -> float:
    rng = np.random.default_rng(20260812)
    worst = 0.0
    C = np.array([[1.0, 1.0], [1.0j, -1.0j]]) / math.sqrt(2.0)
    for _ in range(500):
        k = rng.normal(size=3)
        X = rng.normal(size=(3, 3))
        S = 0.5 * (X + X.T)
        S -= np.trace(S) * np.eye(3) / 3.0
        E = transverse_frame(k)
        # At H=I, material metric velocity is Mdot=2S.
        B_metric = 0.5 * E.T @ (2.0 * S) @ E
        B_direct = E.T @ S @ E
        worst = max(worst, float(np.linalg.norm(B_metric - B_direct)))
        D = B_metric - 0.5 * np.trace(B_metric) * np.eye(2)
        delta, beta = D[0, 0], D[0, 1]
        Ghel = C.conj().T @ (-B_direct.astype(complex)) @ C
        pred_pm = -(delta - 1j * beta)
        pred_mp = -(delta + 1j * beta)
        worst = max(worst, abs(Ghel[0, 1] - pred_pm), abs(Ghel[1, 0] - pred_mp))
    return worst


def fixed_metric_phase_sweep() -> dict[str, float]:
    ka0, kb0, kc0 = planar_optimal_triad()
    F = planar_strain_F(0.03, 0.37)
    M = F.T @ F
    ka, kb, kc = (deform_covector(F, k) for k in (ka0, kb0, kc0))
    # Covector transport preserves the triad relation exactly up to floating error.
    assert np.linalg.norm(ka + kb - kc) < 1e-12

    na, nb, nc = ka0 / np.linalg.norm(ka0), kb0 / np.linalg.norm(kb0), kc0 / np.linalg.norm(kc0)
    x_m, y_m = metric_parent_ratios(M, na, nb, nc)
    x_d, y_d = np.linalg.norm(ka) / np.linalg.norm(kc), np.linalg.norm(kb) / np.linalg.norm(kc)
    assert abs(x_m - x_d) < 1e-12 and abs(y_m - y_d) < 1e-12
    u, v = metric_uv(M, na, nb, nc)

    u1 = helical_basis(ka, +1)
    u2 = helical_basis(kb, -1)
    hq = helical_basis(kc, +1)

    works = []
    phases = np.linspace(0.0, 2.0 * math.pi, 1441)
    for phi in phases:
        uq = np.exp(1j * phi) * hq
        works.append(edge_work(ka, u1, kb, u2, uq))
    works = np.asarray(works)
    wmax, wmin = float(works.max()), float(works.min())
    wabs = float(np.max(np.abs(works)))
    wzero = float(np.min(np.abs(works)))
    assert wmax > 1e-6
    assert wmin < -1e-6
    assert abs(wmax + wmin) < 2e-5 * wabs + 1e-12
    assert wzero < 5e-3 * wabs

    # Same metric, same wavevectors, same helicities, same magnitudes: phase alone flips work sign.
    return {
        "u": u,
        "v": v,
        "x": x_m,
        "y": y_m,
        "work_max": wmax,
        "work_min": wmin,
        "min_abs_work": wzero,
        "work_envelope": wabs,
    }


def main() -> None:
    worst = helicity_conversion_check()
    assert worst < 2e-12
    out = fixed_metric_phase_sweep()
    print("metric-velocity ↔ helicity-conversion worst residual:", worst)
    print("fixed material metric Hodge coordinates u,v:", out["u"], out["v"])
    print("fixed material metric parent ratios x,y:", out["x"], out["y"])
    print("same metric/helicities/magnitudes, phase-swept edge work min/max:", out["work_min"], out["work_max"])
    print("closest sampled work to zero:", out["min_abs_work"])
    print("conclusion: metric geometry fixes shape but not signed physical work")


if __name__ == "__main__":
    main()
