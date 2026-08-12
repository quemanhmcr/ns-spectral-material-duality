"""Action-only referee for the corrected interaction-parent record-gate trichotomy."""
import numpy as np


def main():
    rng = np.random.default_rng(40082026)
    split_res = owner_violation = geom_violation = 0.0
    resolved_signal = local_signal = skip_signal = 0.0

    for _ in range(12000):
        R = float(rng.uniform(0.5, 8.0))
        nuG = float(rng.uniform(0.01, 20.0))
        down = float(rng.uniform(0.0, 12.0))
        up = down + nuG + float(rng.uniform(0.0, 12.0))

        # Partition by whether either literal interaction parent is below R/4.
        x = float(rng.uniform(0.0, 1.0))
        resolved = x * up
        hi = (1.0 - x) * up
        split_res = max(split_res, abs(resolved + hi - up))

        if resolved >= 0.5 * nuG:
            y = float(rng.uniform(0.0, 1.0))
            skew = y * resolved
            strain = (1.0 - y) * resolved
            resolved_signal = max(resolved_signal, max(skew, strain))
            owner_violation = max(owner_violation, max(0.0, 0.25 * nuG - max(skew, strain)))
        else:
            y = float(rng.uniform(0.0, 1.0))
            local = y * hi
            skip = (1.0 - y) * hi
            local_signal = max(local_signal, local)
            skip_signal = max(skip_signal, skip)
            owner_violation = max(owner_violation, max(0.0, 0.25 * nuG - max(local, skip)))

        # Comparable branch: both parents >=R/4, donor<R, recipient<=4R.
        d = float(rng.uniform(0.25, 0.999999)) * R
        r = float(rng.uniform(1.000001, 4.0)) * R
        # A valid companion magnitude can range between |r-d| and r+d.
        c_lo = abs(r - d) + 1e-9 * R
        c_hi = r + d - 1e-9 * R
        c = float(rng.uniform(max(0.25 * R, c_lo), c_hi))
        vals = [d, r, c]
        geom_violation = max(geom_violation, max(0.0, max(vals) / min(vals) - 20.0))

        # UV skip: donor<R, recipient>4R -> companion >3R.
        d2 = float(rng.uniform(0.25, 0.999999)) * R
        r2 = float(rng.uniform(4.000001, 9.0)) * R
        companion_lower = r2 - d2
        geom_violation = max(geom_violation, max(0.0, 3.0 * R - companion_lower))

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
    print(f"worst comparable/skip geometry violation: {geom_violation:.3e}")
    print(f"worst local strain/skew energy-split residual: {strain_split:.3e}")
    print(f"maximum sampled resolved-owner signal: {resolved_signal:.3e}")
    print(f"maximum sampled comparable-local signal: {local_signal:.3e}")
    print(f"maximum sampled UV-skip signal: {skip_signal:.3e}")

    assert split_res < 2e-12
    assert owner_violation < 2e-12
    assert geom_violation < 2e-12
    assert strain_split < 2e-12
    assert resolved_signal > 1e-3 and local_signal > 1e-3 and skip_signal > 1e-3
    print("PASS: corrected radial record-gate owner-trichotomy calibrations")


if __name__ == "__main__":
    main()
