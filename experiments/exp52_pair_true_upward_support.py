"""Action-only algebra referee for pair-action / true-upward first-shell support."""
import numpy as np


def main():
    rng=np.random.default_rng(52082026)
    moment=rn=workgate=0.0
    signal=0.0
    for _ in range(40000):
        N=float(rng.uniform(.1,20.0))
        # first-shell pure-UV-compatible radii: donor a in (N/2,N], recipient c in (N,2N], other parent b>N/2
        a=float(rng.uniform(.500001*N,N))
        c=float(rng.uniform(1.000001*N,2.0*N))
        blo=abs(c-a)+1e-8
        b=float(rng.uniform(max(.500001*N,blo),min(3*N,a+c-1e-8)))
        R=float(rng.uniform(1e-6,5.0))
        Th=(a+b)*R
        To=(c-a)*R
        P=b*To
        net=(c-a)*Th+(b-a)*To
        moment=max(moment,abs(net-2*P))
        signal=max(signal,P)
        # normalized RN range follows b in [N/2,3N] and mean b in same range; stress arbitrary samples by batch below

        nu=float(rng.uniform(.01,2.0)); Z=float(rng.uniform(.01,20.0))
        Pgate=nu*Z/(128*N)
        Togate=Pgate/b
        workgate=max(workgate,max(0.0,nu*Z/(384*N*N)-Togate))

    # Batch-normalized Radon-Nikodym ratios.
    for _ in range(5000):
        N=float(rng.uniform(.1,20.0)); n=int(rng.integers(3,30))
        b=rng.uniform(.5*N,3*N,size=n)
        T=rng.uniform(1e-8,5.0,size=n)
        P=b*T
        th=T/T.sum(); ph=P/P.sum()
        ratio=ph/th
        rn=max(rn,max(0.0,1/6-ratio.min()),max(0.0,ratio.max()-6))

    print(f"worst heterochiral first-radial-moment identity residual: {moment:.3e}")
    print(f"worst normalized pair/work RN-bound violation: {rn:.3e}")
    print(f"worst actual-work gate violation: {workgate:.3e}")
    print(f"maximum sampled pair-action signal: {signal:.3e}")
    assert moment<2e-11
    assert rn<2e-12
    assert workgate<2e-12
    assert signal>1e-4
    print("PASS: pair action contains true-upward work and is first-shell work-equivalent")


if __name__=='__main__': main()
