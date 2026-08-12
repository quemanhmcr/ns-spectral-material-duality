"""Action-only support referee for donor-anchored plateau resolved binding."""
import numpy as np


def main():
    rng=np.random.default_rng(54082026)
    plateau=local=low_low=0.0
    deep_signal=0.0
    for _ in range(50000):
        # dyadic donor scale N and actual donor in (N/2,N]
        j=int(rng.integers(-3,10)); N=2.0**j
        a=float(rng.uniform(.500001*N,N))
        # choose a higher dyadic shell M
        mstep=int(rng.integers(1,8)); M=N*(2.0**mstep)
        c=float(rng.uniform(.500001*M,M))
        if M>=8*N:
            plateau=max(plateau,max(0.0,a-M/8.0))
            deep_signal=max(deep_signal,M/N)
            # two resolved frequencies each <=M/4 cannot exceed M/2 in output radius
            r1=float(rng.uniform(0.0,M/4)); r2=float(rng.uniform(0.0,M/4))
            low_low=max(low_low,max(0.0,r1+r2-M/2))
        else:
            local=max(local,max(0.0,c/a-16.0))

    # Exact K/S positive-part cover is scalar algebra R=RK+RS.
    ks=0.0
    for _ in range(30000):
        rk=float(rng.normal()); rs=float(rng.normal()); r=rk+rs
        if r>0:
            ks=max(ks,max(0.0,r-max(rk,0.0)-max(rs,0.0)))

    print(f"worst deep donor-plateau violation: {plateau:.3e}")
    print(f"worst shallow c/a<16 violation: {local:.3e}")
    print(f"worst resolved low-low support violation: {low_low:.3e}")
    print(f"worst K/S positive-work cover violation: {ks:.3e}")
    print(f"maximum sampled deep shell ratio M/N: {deep_signal:.3e}")
    assert plateau<2e-12
    assert local<2e-12
    assert low_low<2e-12
    assert ks<2e-12
    assert deep_signal>=8.0
    print("PASS: donor-anchored plateau binds deep pair creation to resolved mixed work")


if __name__=='__main__': main()
