from __future__ import annotations

import math
import numpy as np


def run_case(rates: np.ndarray, dt: float, z0: complex, c_hi: float, c_lo: float, rho: float):
    # rates[t,j] are exact channel logarithmic derivatives R_j/Z = a+ib.
    z = complex(z0)
    amp_actions = np.zeros(3)
    phase_actions = np.zeros(3)
    amp_hit = phase_hit = False
    for row in rates:
        amp_actions += np.abs(np.real(row)) * dt
        phase_actions += np.abs(np.imag(row)) * dt
        total = np.sum(row)
        z *= np.exp(total * dt)
        R = abs(z)
        c = z.real / R
        if R <= rho * abs(z0):
            amp_hit = True
            break
        if c <= c_lo:
            phase_hit = True
            break
    persistent = not amp_hit and not phase_hit
    return z, amp_actions, phase_actions, amp_hit, phase_hit, persistent


def main() -> None:
    c_hi, c_lo, rho = 0.9, 0.5, 0.6
    delta = math.acos(c_lo) - math.acos(c_hi)
    theta0 = 0.5 * math.acos(c_hi)
    z0 = np.exp(1j * theta0)
    dt = 1e-3
    steps = 2000

    # Case 1: geometry corridor + tiny source action -> favorable work persists.
    r1 = np.zeros((steps, 3), dtype=complex)
    r1[:, 0] = 0.01j
    z1, A1, P1, ah1, ph1, keep1 = run_case(r1, dt, z0, c_hi, c_lo, rho)
    assert keep1 and z1.real > rho * c_lo * abs(z0)

    # Case 2: pure physical dephasing in one channel.  Its action must cross delta.
    r2 = np.zeros((steps, 3), dtype=complex)
    r2[:, 1] = 0.55j
    z2, A2, P2, ah2, ph2, keep2 = run_case(r2, dt, z0, c_hi, c_lo, rho)
    assert ph2 and not ah2 and not keep2
    assert P2.sum() + 2e-3 >= delta

    # Case 3: real damping only.  Its amplitude action pays log(1/rho), with no phase action.
    r3 = np.zeros((steps, 3), dtype=complex)
    r3[:, 2] = -0.5
    z3, A3, P3, ah3, ph3, keep3 = run_case(r3, dt, z0, c_hi, c_lo, rho)
    assert ah3 and not ph3 and not keep3
    assert A3.sum() + 2e-3 >= math.log(1.0 / rho)
    assert P3.sum() == 0.0

    print("alignment thresholds c_hi,c_lo / rho:", c_hi, c_lo, rho)
    print("certified minimum phase displacement delta_theta:", delta)
    print("persistence case final normalized work:", z1.real / abs(z0), "phase action:", P1.sum())
    print("phase-loss case accumulated channel actions:", P2.tolist(), "sum:", P2.sum())
    print("amplitude-loss case accumulated channel actions:", A3.tolist(), "sum:", A3.sum())
    print("log(1/rho):", math.log(1.0 / rho))
    print("conclusion: favorable signed work cannot disappear inside a good geometry corridor without an exact amplitude or phase action payment")


if __name__ == "__main__":
    main()
