"""Action-only algebra referee for radial high-tail fresh amplitude funding."""
import math
import numpy as np


def main():
    rng=np.random.default_rng(56082026)
    old=fresh=window=0.0
    signal=0.0
    for _ in range(30000):
        nu=float(rng.uniform(.01,2.0)); rho=float(rng.uniform(.2,1.0)); N=float(rng.uniform(1.0,100.0))
        R=rho*N; Estar=float(rng.uniform(.1,20.0)); eta=float(rng.uniform(.001,Estar*N*.5))
        x=4.0*math.sqrt(Estar*N/eta)
        if x<=1: continue
        L=math.log(x)/(nu*R*R)
        oldnorm=math.exp(-nu*R*R*L)*math.sqrt(Estar)
        target=math.sqrt(eta/N)
        old=max(old,abs(oldnorm-.25*target)/(1+target))
        # Worst aligned old vector has same direction as terminal; reverse triangle fresh is terminal-old.
        Grequired=max(0.0,target-oldnorm)
        fresh=max(fresh,max(0.0,.75*target-Grequired))
        window=max(window,abs(nu*R*R*L-math.log(x)))
        signal=max(signal,Grequired)
    print(f"worst old-amplitude normalization residual: {old:.3e}")
    print(f"worst 3/4 fresh-amplitude lower violation: {fresh:.3e}")
    print(f"worst amplitude-window identity residual: {window:.3e}")
    print(f"maximum sampled forced fresh-amplitude signal: {signal:.3e}")
    assert old<2e-12
    assert fresh<2e-12
    assert window<2e-12
    assert signal>1e-4
    print("PASS: radial critical shell forces recent nonlinear Duhamel amplitude")


if __name__=='__main__': main()
