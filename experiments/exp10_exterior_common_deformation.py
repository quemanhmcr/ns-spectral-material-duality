from __future__ import annotations

import numpy as np


def det2(u: np.ndarray, v: np.ndarray) -> complex:
    return complex(u[0] * v[1] - u[1] * v[0])


def det3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> complex:
    return complex(np.dot(c, np.cross(a, b)))


def main() -> None:
    rng = np.random.default_rng(2026081210)
    worst2 = worst3 = worst_relative = 0.0

    for _ in range(3000):
        # 2D parent polarization wedge: common trace-free generator cancels.
        D = rng.normal(size=(2, 2))
        D -= 0.5 * np.trace(D) * np.eye(2)
        u = rng.normal(size=2) + 1j * rng.normal(size=2)
        v = rng.normal(size=2) + 1j * rng.normal(size=2)
        w = det2(u, v)
        dw = det2(-D @ u, v) + det2(u, -D @ v)
        target = -np.trace(D) * w
        worst2 = max(worst2, abs(dw - target) / max(1.0, abs(dw), abs(target)))

        # 3D oriented complex interaction volume: common incompressible generator cancels.
        A = rng.normal(size=(3, 3))
        A -= np.trace(A) * np.eye(3) / 3.0
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        b = rng.normal(size=3) + 1j * rng.normal(size=3)
        c = rng.normal(size=3) + 1j * rng.normal(size=3)
        z = det3(a, b, np.conjugate(c))
        dz = (
            det3(A @ a, b, np.conjugate(c))
            + det3(a, A @ b, np.conjugate(c))
            + det3(a, b, A @ np.conjugate(c))
        )
        target3 = np.trace(A) * z
        worst3 = max(worst3, abs(dz - target3) / max(1.0, abs(dz), abs(target3)))

        # Different generators: subtract any common reference A0; only relative generators remain,
        # plus the trace of the common reference.
        A0 = rng.normal(size=(3, 3))
        A1 = rng.normal(size=(3, 3))
        A2 = rng.normal(size=(3, 3))
        A3 = rng.normal(size=(3, 3))
        direct = (
            det3(A1 @ a, b, np.conjugate(c))
            + det3(a, A2 @ b, np.conjugate(c))
            + det3(a, b, A3 @ np.conjugate(c))
        )
        rel = (
            np.trace(A0) * z
            + det3((A1 - A0) @ a, b, np.conjugate(c))
            + det3(a, (A2 - A0) @ b, np.conjugate(c))
            + det3(a, b, (A3 - A0) @ np.conjugate(c))
        )
        worst_relative = max(worst_relative, abs(direct - rel) / max(1.0, abs(direct), abs(rel)))

    assert worst2 < 2e-12
    assert worst3 < 2e-12
    assert worst_relative < 2e-12
    print("2D common trace-free wedge cancellation worst residual:", worst2)
    print("3D common incompressible interaction-volume cancellation worst residual:", worst3)
    print("different-generator relative-source identity worst residual:", worst_relative)
    print("conclusion: both parent polarization and material interaction phase are exterior-power invariants; common incompressible deformation is geometry, relative generators create change")


if __name__ == "__main__":
    main()
