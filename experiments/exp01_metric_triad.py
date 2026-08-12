from __future__ import annotations

import math
import numpy as np

from src.bridge_geometry import RSTAR, j_env, j_star, metric_parent_ratios, metric_uv, planar_optimal_triad, planar_strain_F, deform_covector


def main() -> None:
    ka0, kb0, kc0 = planar_optimal_triad()
    na, nb, nc = ka0 / np.linalg.norm(ka0), kb0 / np.linalg.norm(kb0), kc0 / np.linalg.norm(kc0)
    JSTAR = j_star()
    worst_uv = 0.0
    min_def_over_h = float("inf")
    min_def_over_z2 = float("inf")
    rows = []
    for z in (0.005, 0.01, 0.02, 0.04):
        local = 0
        local_total = 0
        for j in range(720):
            ang = math.pi * j / 720.0
            F = planar_strain_F(z, ang)
            M = F.T @ F
            u, v = metric_uv(M, na, nb, nc)
            x_m, y_m = metric_parent_ratios(M, na, nb, nc)
            ka, kb, kc = (deform_covector(F, k) for k in (ka0, kb0, kc0))
            x_d = np.linalg.norm(ka) / np.linalg.norm(kc)
            y_d = np.linalg.norm(kb) / np.linalg.norm(kc)
            worst_uv = max(worst_uv, abs(x_m - x_d), abs(y_m - y_d))
            H = 0.5 * u * u + 2.0 * v * v
            if max(abs(u), abs(v)) <= 2.0 / 25.0:
                local += 1
                J = j_env(x_m, y_m)
                Def = 1.0 - J / JSTAR
                if H > 1e-16:
                    min_def_over_h = min(min_def_over_h, Def / H)
                min_def_over_z2 = min(min_def_over_z2, Def / (z * z))
            local_total += 1
        rows.append((z, local, local_total))
    assert worst_uv < 2e-12
    assert min_def_over_h > 0.5 - 1e-10
    print("metric↔direct parent-ratio residual:", worst_uv)
    print("minimum sampled Def/H on certified local region:", min_def_over_h)
    print("minimum sampled Def/z^2 on certified local region:", min_def_over_z2)
    for row in rows:
        print("z/local:", row)


if __name__ == "__main__":
    main()
