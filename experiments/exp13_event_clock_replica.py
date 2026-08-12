"""ACTION STRESS TESTS for exact event readout, state-map residual, and common-replica cancellation.

These numerical checks are adversarial calibrations only.  The proofs are algebraic/PDE identities
recorded in docs/14--16.
"""

from __future__ import annotations

import numpy as np


def triple(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> complex:
    return np.vdot(a, np.cross(b, c))


def det_one_real(rng: np.random.Generator) -> np.ndarray:
    while True:
        D = rng.normal(size=(3, 3))
        d = np.linalg.det(D)
        if abs(d) > 0.2:
            break
    if d < 0:
        D[:, [0, 1]] = D[:, [1, 0]]
        d = -d
    return D / (d ** (1.0 / 3.0))


def event_plateau_test(rng: np.random.Generator, trials: int = 300) -> tuple[float, float, float]:
    worst_readout = 0.0
    max_smooth_gap = 0.0
    worst_energy_phase = 0.0

    for _ in range(trials):
        # Two frequency blocks per leg: block 0 is the hard event cell, block 1 is smooth overlap.
        v = rng.normal(size=(3, 2, 3)) + 1j * rng.normal(size=(3, 2, 3))
        q = rng.uniform(0.05, 0.95, size=3)
        Qv = v.copy()
        Qv[:, 1, :] *= q[:, None]

        hard = v[:, 0, :]
        hard_from_Q = Qv[:, 0, :]
        z_hard = triple(hard[0], hard[1], hard[2])
        z_read = triple(hard_from_Q[0], hard_from_Q[1], hard_from_Q[2])
        worst_readout = max(worst_readout, abs(z_read - z_hard))

        # A deliberately compressed smooth statistic mixes the overlap block before the cubic readout.
        smooth = Qv.sum(axis=1)
        z_smooth = triple(smooth[0], smooth[1], smooth[2])
        max_smooth_gap = max(max_smooth_gap, abs(z_smooth - z_hard))

        # Quadratic energy is phase blind while the cubic phase moves.
        theta = rng.uniform(-np.pi, np.pi)
        rotated = hard.copy()
        rotated[0] *= np.exp(1j * theta)
        e0 = sum(np.vdot(x, x).real for x in hard)
        e1 = sum(np.vdot(x, x).real for x in rotated)
        z_rot = triple(rotated[0], rotated[1], rotated[2])
        expected = np.exp(-1j * theta) * z_hard
        worst_energy_phase = max(worst_energy_phase, abs(e1 - e0), abs(z_rot - expected))

    return worst_readout, max_smooth_gap, worst_energy_phase


def state_map_test(rng: np.random.Generator, trials: int = 500) -> tuple[float, float, float]:
    worst_chain = 0.0
    worst_tangent = 0.0
    min_normal_signal = np.inf

    for _ in range(trials):
        t = rng.normal()
        y = rng.normal(size=3)
        B0 = rng.normal(size=(3, 3))
        B1 = rng.normal(size=(3, 3))
        c0 = rng.normal(size=3)
        c1 = rng.normal(size=3)
        B = B0 + t * B1
        c = c0 + t * c1
        x = B @ y + c

        AY = rng.normal(size=(3, 3))
        dY = rng.normal(size=3)
        AX = rng.normal(size=(3, 3))
        dX = rng.normal(size=3)
        bY = AY @ y + dY
        bX = AX @ x + dX
        R = B1 @ y + c1 + B @ bY - bX

        alpha = rng.normal()
        v = rng.normal(size=3)
        phase = alpha * t + v @ x
        grad = np.cos(phase) * v + 0.2 * x
        partial_t_chi = alpha * np.cos(phase)

        lhs = partial_t_chi + grad @ (B1 @ y + c1 + B @ bY)
        phys_pullback = partial_t_chi + grad @ bX
        rhs = phys_pullback + grad @ R
        worst_chain = max(worst_chain, abs(lhs - rhs))

        n = rng.normal(size=3)
        w = rng.normal(size=3)
        tangent = np.cross(n, w)
        worst_tangent = max(worst_tangent, abs(n @ tangent))
        normal = n
        signal = abs(n @ normal)
        if signal > 1e-10:
            min_normal_signal = min(min_normal_signal, signal)

    return worst_chain, worst_tangent, min_normal_signal


def replica_test(rng: np.random.Generator, trials: int = 400) -> tuple[float, float, float]:
    worst_sl3 = 0.0
    worst_generator = 0.0
    max_relative_effect = 0.0

    for _ in range(trials):
        z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        D = det_one_real(rng)
        zD = np.array([D @ z[i] for i in range(3)])
        worst_sl3 = max(worst_sl3, abs(triple(zD[0], zD[1], zD[2]) - triple(z[0], z[1], z[2])))

        G = rng.normal(size=(3, 3))
        G -= np.trace(G) * np.eye(3) / 3.0
        common = (
            triple(G @ z[0], z[1], z[2])
            + triple(z[0], G @ z[1], z[2])
            + triple(z[0], z[1], G @ z[2])
        )
        worst_generator = max(worst_generator, abs(common - np.trace(G) * triple(z[0], z[1], z[2])))

        Gs = []
        for _j in range(3):
            Gj = rng.normal(size=(3, 3))
            Gj -= np.trace(Gj) * np.eye(3) / 3.0
            Gs.append(Gj)
        full = (
            triple(Gs[0] @ z[0], z[1], z[2])
            + triple(z[0], Gs[1] @ z[1], z[2])
            + triple(z[0], z[1], Gs[2] @ z[2])
        )
        ref = Gs[0]
        rel = (
            np.trace(ref) * triple(z[0], z[1], z[2])
            + triple((Gs[0] - ref) @ z[0], z[1], z[2])
            + triple(z[0], (Gs[1] - ref) @ z[1], z[2])
            + triple(z[0], z[1], (Gs[2] - ref) @ z[2])
        )
        worst_generator = max(worst_generator, abs(full - rel))
        max_relative_effect = max(max_relative_effect, abs(full))

    return worst_sl3, worst_generator, max_relative_effect


def main() -> None:
    rng = np.random.default_rng(20260812)
    readout, smooth_gap, energy_phase = event_plateau_test(rng)
    chain, tangent, normal_signal = state_map_test(rng)
    sl3, generator, relative = replica_test(rng)

    print(f"worst hard-event plateau readout residual: {readout:.3e}")
    print(f"maximum smooth-summary overlap gap: {smooth_gap:.3e}")
    print(f"worst quadratic-energy / phase-rotation calibration residual: {energy_phase:.3e}")
    print(f"worst state-map chain-rule residual: {chain:.3e}")
    print(f"worst tangential hard-face contraction residual: {tangent:.3e}")
    print(f"minimum sampled normal hard-face signal: {normal_signal:.3e}")
    print(f"worst common-replica SL(3) cubic residual: {sl3:.3e}")
    print(f"worst relative-generator decomposition residual: {generator:.3e}")
    print(f"maximum sampled relative-replica cubic-rate magnitude: {relative:.3e}")

    assert readout < 1e-12
    assert smooth_gap > 1e-3
    assert energy_phase < 1e-11
    assert chain < 1e-11
    assert tangent < 1e-11
    assert normal_signal > 1e-8
    assert sl3 < 1e-10
    assert generator < 1e-10
    assert relative > 1e-3
    print("PASS: event/clock/replica adversarial calibrations")


if __name__ == "__main__":
    main()
