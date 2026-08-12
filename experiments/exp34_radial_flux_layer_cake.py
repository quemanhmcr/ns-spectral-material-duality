"""Adversarial stress for radial mode-set layer-cake flux identities."""
import numpy as np


def main():
    rng = np.random.default_rng(34082026)
    up_res = down_res = net_res = heat_res = 0.0
    outward_signal = inward_signal = heat_signal = 0.0

    for _ in range(1200):
        n = int(rng.integers(3, 10))
        kappa = np.sort(rng.uniform(0.05, 50.0, size=n))
        E = rng.uniform(0.02, 3.0, size=n)
        Rrates = rng.uniform(0.0, 1.5, size=(n, n))
        np.fill_diagonal(Rrates, 0.0)
        K = E[:, None] * Rrates

        delta = kappa[None, :] - kappa[:, None]
        Fup = float(np.sum(np.maximum(delta, 0.0) * K))
        Fdown = float(np.sum(np.maximum(-delta, 0.0) * K))
        Fnet = float(np.sum(delta * K))

        # Exact layer cake on the finite set: currents are constant between sorted kappa nodes.
        bounds = np.concatenate(([0.0], kappa, [kappa[-1] + 1.0]))
        int_up = int_down = 0.0
        for l, r in zip(bounds[:-1], bounds[1:]):
            if r <= l:
                continue
            mid = 0.5 * (l + r)
            up = 0.0
            down = 0.0
            for i in range(n):
                for j in range(n):
                    if kappa[i] <= mid < kappa[j]:
                        up += K[i, j]
                    if kappa[j] <= mid < kappa[i]:
                        down += K[i, j]
            int_up += (r - l) * up
            int_down += (r - l) * down
        up_res = max(up_res, abs(int_up - Fup))
        down_res = max(down_res, abs(int_down - Fdown))
        net_res = max(net_res, abs((int_up - int_down) - Fnet))
        outward_signal = max(outward_signal, Fup)
        inward_signal = max(inward_signal, Fdown)

        c = float(rng.uniform(0.02, 3.0))
        w = 1.0 - np.exp(-c * kappa)
        direct_heat = float(np.sum((w[None, :] - w[:, None]) * K))
        int_heat = 0.0
        for l, r in zip(bounds[:-1], bounds[1:]):
            if r <= l:
                continue
            mid = 0.5 * (l + r)
            up = down = 0.0
            for i in range(n):
                for j in range(n):
                    if kappa[i] <= mid < kappa[j]:
                        up += K[i, j]
                    if kappa[j] <= mid < kappa[i]:
                        down += K[i, j]
            # integrate c exp(-c R) exactly over interval
            weight_int = np.exp(-c * l) - np.exp(-c * r)
            int_heat += weight_int * (up - down)
        heat_res = max(heat_res, abs(int_heat - direct_heat))
        heat_signal = max(heat_signal, abs(direct_heat))

    print(f"worst outward radial layer-cake residual: {up_res:.3e}")
    print(f"worst inward radial layer-cake residual: {down_res:.3e}")
    print(f"worst net enstrophy-moment layer-cake residual: {net_res:.3e}")
    print(f"worst heat-weighted radial flux residual: {heat_res:.3e}")
    print(f"maximum sampled outward radial flux moment: {outward_signal:.3e}")
    print(f"maximum sampled inward radial flux moment: {inward_signal:.3e}")
    print(f"maximum sampled heat-weighted radial signal: {heat_signal:.3e}")

    assert up_res < 3e-11
    assert down_res < 3e-11
    assert net_res < 4e-11
    assert heat_res < 3e-11
    assert outward_signal > 1e-3
    assert inward_signal > 1e-3
    assert heat_signal > 1e-4
    print("PASS: radial mode-flux layer-cake calibrations")


if __name__ == "__main__":
    main()
