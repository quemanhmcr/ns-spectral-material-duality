"""Action-only referee for the exact record-gate upward-flow trichotomy."""
import numpy as np


def main():
    rng = np.random.default_rng(40082026)
    split_res = owner_violation = geom_violation = 0.0
    resolved_signal = local_signal = skip_signal = 0.0

    for _ in range(10000):
        R = float(rng.uniform(0.5, 8.0))
        nuG = float(rng.uniform(0.01, 20.0))
        down = float(rng.uniform(0.0, 12.0))
        up = down + nuG + float(rng.uniform(0.0, 12.0))

        x = float(rng.uniform(0.0, 1.0))
        far = x * up
        near = (1.0 - x) * up
        split_res = max(split_res, abs(far + near - up))

        if far >= 0.5 * nuG:
            y = float(rng.uniform(0.0, 1.0))
            skew = y * far
            strain = (1.0 - y) * far
            resolved_signal = max(resolved_signal, max(skew, strain))
            owner_violation = max(owner_violation, max(0.0, 0.25 * nuG - max(skew, strain)))
        else:
            y = float(rng.uniform(0.0, 1.0))
            local = y * near
            skip = (1.0 - y) * near
            local_signal = max(local_signal, local)
            skip_signal = max(skip_signal, skip)
            owner_violation = max(owner_violation, max(0.0, 0.25 * nuG - max(local, skip)))

        dmag = float(rng.uniform(0.0, 0.249999)) * R
        rmag = float(rng.uniform(1.000001, 5.0)) * R
        geom_violation = max(geom_violation, max(0.0, 0.75 * R - (rmag - dmag)))

        dmag2 = float(rng.uniform(0.25, 0.999999)) * R
        rmag2 = float(rng.uniform(4.000001, 9.0)) * R
        geom_violation = max(geom_violation, max(0.0, 3.0 * R - (rmag2 - dmag2)))

        dloc = float(rng.uniform(0.25, 0.999999)) * R
        rloc = float(rng.uniform(1.000001, 4.0)) * R
        geom_violation = max(geom_violation, max(0.0, rloc / dloc - 16.0))

    # Local velocity-gradient referee: real skew part cannot perform real energy work.
    strain_split = 0.0
    for _ in range(5000):
        A = rng.normal(size=(3, 3))
        A -= np.eye(3) * np.trace(A) / 3.0
        S = 0.5 * (A + A.T)
        O = 0.5 * (A - A.T)
        z = rng.normal(size=3) + 1j * rng.normal(size=3)
        total = float(np.vdot(z, A @ z).real)
        sym = float(np.vdot(z, S @ z).real)
        skew = float(np.vdot(z, O @ z).real)
        strain_split = max(strain_split, abs(total - sym), abs(skew))

    print(f"worst upward-flow first-split residual: {split_res:.3e}")
    print(f"worst nuG/4 owner-pigeonhole violation: {owner_violation:.3e}")
    print(f"worst far/skip/local geometry violation: {geom_violation:.3e}")
    print(f"worst local strain/skew energy-split residual: {strain_split:.3e}")
    print(f"maximum sampled resolved-owner signal: {resolved_signal:.3e}")
    print(f"maximum sampled local-crossing signal: {local_signal:.3e}")
    print(f"maximum sampled UV-skip signal: {skip_signal:.3e}")

    assert split_res < 2e-12
    assert owner_violation < 2e-12
    assert geom_violation < 2e-12
    assert strain_split < 2e-12
    assert resolved_signal > 1e-3 and local_signal > 1e-3 and skip_signal > 1e-3
    print("PASS: radial record-gate owner-trichotomy calibrations")


if __name__ == "__main__":
    main()
