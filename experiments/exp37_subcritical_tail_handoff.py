"""Action-only referee for the exact UV owner split and tail self-interaction scaling."""
import itertools
import math
import numpy as np


def half_lattice(k):
    for x in k:
        if x > 0:
            return True
        if x < 0:
            return False
    return False


def lattice(K):
    return [k for k in itertools.product(range(-K, K + 1), repeat=3) if k != (0, 0, 0)]


def random_div_free(rng, keys):
    keyset = set(keys)
    u = {k: np.zeros(3, dtype=complex) for k in keys}
    for k in keys:
        if not half_lattice(k):
            continue
        kv = np.array(k, dtype=float)
        z = rng.normal(size=3) + 1j * rng.normal(size=3)
        z -= kv * (np.dot(kv, z) / np.dot(kv, kv))
        u[k] = z
        nk = tuple(-np.array(k, dtype=int))
        if nk in keyset:
            u[nk] = np.conjugate(z)
    return u


def add(a, b):
    return {k: a[k] + b[k] for k in a}


def scale(a, c):
    return {k: c * a[k] for k in a}


def split(u, Q):
    v = {}
    h = {}
    for k, z in u.items():
        r = float(np.linalg.norm(k))
        if r <= Q:
            v[k], h[k] = z, np.zeros(3, dtype=complex)
        else:
            v[k], h[k] = np.zeros(3, dtype=complex), z
    return v, h


def bilinear(a, b):
    keys = list(a)
    keyset = set(keys)
    out = {k: np.zeros(3, dtype=complex) for k in keys}
    active_a = [(p, z) for p, z in a.items() if np.linalg.norm(z) > 1e-14]
    active_b = [(q, z) for q, z in b.items() if np.linalg.norm(z) > 1e-14]
    for p, ap in active_a:
        pv = np.array(p, dtype=int)
        for q, bq in active_b:
            k = tuple(pv + np.array(q, dtype=int))
            if k not in keyset:
                continue
            qv = np.array(q, dtype=float)
            out[k] += 1j * np.dot(qv, ap) * bq
    return out


def high_work(B, h, Q):
    w = 0.0
    for k, hk in h.items():
        if np.linalg.norm(k) <= Q or np.linalg.norm(hk) < 1e-14:
            continue
        kk = float(np.dot(k, k))
        w += float(np.vdot(B[k], -kk * hk).real)
    return w


def ztail(h, Q):
    z = 0.0
    for k, hk in h.items():
        r = float(np.linalg.norm(k))
        if r > Q:
            z += r**4 * float(np.vdot(hk, hk).real)
    return z


def btail(h, Q):
    shells = {}
    for k, hk in h.items():
        r = float(np.linalg.norm(k))
        if r <= Q:
            continue
        e = float(np.vdot(hk, hk).real)
        if e == 0.0:
            continue
        q = int(math.ceil(math.log(max(r, 1.0), 2.0)))
        upper = 2.0**q
        shells[upper] = shells.get(upper, 0.0) + e
    return math.sqrt(max((N * e for N, e in shells.items()), default=0.0))


def max_field_res(a, b):
    return max((np.linalg.norm(a[k] - b[k]) for k in a), default=0.0)


def main():
    rng = np.random.default_rng(37082026)
    keys = lattice(3)
    decomp = work_decomp = ll_support = scale_res = ratio_res = 0.0
    self_signal = ext_signal = ratio_signal = 0.0

    for _ in range(90):
        u = random_div_free(rng, keys)
        Q = float(rng.uniform(1.25, 2.2))
        v, h = split(u, Q)
        Bvv = bilinear(v, v)
        Bvh = bilinear(v, h)
        Bhv = bilinear(h, v)
        Bhh = bilinear(h, h)
        Bfull = bilinear(u, u)
        Bsum = add(add(Bvv, Bvh), add(Bhv, Bhh))
        decomp = max(decomp, max_field_res(Bfull, Bsum))

        Wfull = high_work(Bfull, h, Q)
        Whhh = high_work(Bhh, h, Q)
        Wext = high_work(add(add(Bvv, Bvh), Bhv), h, Q)
        work_decomp = max(work_decomp, abs(Wfull - Whhh - Wext))
        self_signal = max(self_signal, abs(Whhh))
        ext_signal = max(ext_signal, abs(Wext))

        # Low-low convolution cannot jump beyond twice the low support radius.
        for k, z in Bvv.items():
            if np.linalg.norm(k) > 2.0 * Q + 1e-12:
                ll_support = max(ll_support, np.linalg.norm(z))

        Z = ztail(h, Q)
        B = btail(h, Q)
        if B * Z > 1e-12:
            ratio = abs(Whhh) / (B * Z)
            ratio_signal = max(ratio_signal, ratio)

            amp = float(rng.uniform(0.15, 3.5))
            ha = scale(h, amp)
            Bhha = bilinear(ha, ha)
            Wa = high_work(Bhha, ha, Q)
            Za = ztail(ha, Q)
            Ba = btail(ha, Q)
            if abs(Whhh) > 1e-10:
                scale_res = max(scale_res, abs(Wa / Whhh - amp**3) / (1.0 + amp**3))
            if Za * Ba > 1e-12:
                ratio_a = abs(Wa) / (Ba * Za)
                ratio_res = max(ratio_res, abs(ratio_a - ratio))

    # Pure algebra of the record-growth handoff after a proved absorption bound.
    handoff = 0.0
    for _ in range(3000):
        nu = float(rng.uniform(0.05, 3.0))
        Z = float(rng.uniform(0.01, 20.0))
        whhh = float(rng.uniform(-0.25, 0.25)) * nu * Z
        surplus = float(rng.uniform(0.0, 4.0)) * nu * Z
        wext = nu * Z - whhh + surplus
        ydot_half = wext + whhh - nu * Z
        assert ydot_half >= -1e-12
        handoff = max(handoff, max(0.0, 0.75 * nu * Z - wext))

    print(f"worst exact bilinear owner-decomposition residual: {decomp:.3e}")
    print(f"worst exact high-tail work-decomposition residual: {work_decomp:.3e}")
    print(f"worst low-low beyond-2Q support leakage: {ll_support:.3e}")
    print(f"worst pure-tail cubic scaling residual: {scale_res:.3e}")
    print(f"worst |W_hhh|/(B_tail Z_tail) scale-invariance residual: {ratio_res:.3e}")
    print(f"worst post-absorption 3nu/4 handoff violation: {handoff:.3e}")
    print(f"maximum sampled pure-tail self-work signal: {self_signal:.3e}")
    print(f"maximum sampled external-incidence work signal: {ext_signal:.3e}")
    print(f"maximum sampled tail work ratio signal: {ratio_signal:.3e}")

    assert decomp < 2e-11
    assert work_decomp < 2e-10
    assert ll_support < 2e-11
    assert scale_res < 2e-11
    assert ratio_res < 2e-11
    assert handoff < 2e-12
    assert self_signal > 1e-5 and ext_signal > 1e-5 and ratio_signal > 1e-8
    print("PASS: subcritical-tail owner split / S-handoff calibrations")


if __name__ == "__main__":
    main()
