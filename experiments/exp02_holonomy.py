from __future__ import annotations

import math
import numpy as np


def exp_D1(d: float, eps: float) -> np.ndarray:
    return np.diag([math.exp(d * eps), math.exp(-d * eps)])


def exp_D2(b: float, eps: float) -> np.ndarray:
    c, s = math.cosh(b * eps), math.sinh(b * eps)
    return np.array([[c, s], [s, c]])


def polar_angle(F: np.ndarray) -> float:
    return math.atan2(F[1, 0] - F[0, 1], F[0, 0] + F[1, 1])


def main() -> None:
    for b, d in ((1.0, 1.0), (0.7, 1.3), (1.8, 0.4)):
        for eps in (1e-3, 3e-3, 1e-2, 3e-2, 0.1):
            F = exp_D2(b, eps) @ exp_D1(d, eps)
            theta = polar_angle(F)
            exact = math.atan(math.tanh(b * eps) * math.tanh(d * eps))
            assert abs(theta - exact) < 1e-13
            leading = b * d * eps * eps
            if eps <= 1e-2:
                assert abs(theta - leading) <= 2.0 * (abs(b) + abs(d) + 1.0) ** 4 * eps ** 4
    eps = 0.1
    theta = polar_angle(exp_D2(1.0, eps) @ exp_D1(1.0, eps))
    print("exact polar holonomy at b=d=1, eps=.1 [deg]:", theta * 180.0 / math.pi)
    print("second-Magnus leading angle [deg]:", eps * eps * 180.0 / math.pi)


if __name__ == "__main__":
    main()
