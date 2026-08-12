"""Action-only algebra referee for fixed-critical efficiency and polarization mixing."""
import numpy as np


def main():
    rng=np.random.default_rng(53082026)
    avg=half=geom=mix=0.0
    signal=0.0
    for _ in range(20000):
        V0=float(rng.uniform(.2,20.0)); M0=float(rng.uniform(.2,20.0))
        rho=27.0/(8192.0*np.sqrt(V0*M0))
        n=int(rng.integers(4,80))
        A=rng.uniform(1e-8,5.0,size=n)
        # Manufacture efficiencies with A-weighted mean at least rho.
        e=rng.uniform(0.0,1.0,size=n)
        mean=float(np.dot(A,e)/A.sum())
        if mean<rho:
            e=np.minimum(1.0,e+(rho-mean))
        P=A*e
        mean=float(P.sum()/A.sum())
        avg=max(avg,max(0.0,rho-mean))
        G=e>=rho/2.0
        half=max(half,max(0.0,.5*P.sum()-P[G].sum()))
        signal=max(signal,float(P[G].sum()))

        # Edge geometry consequence from eta >= rho/sqrt2.
        eta=rho/np.sqrt(2.0)
        # Worst allowed |delta| from eta <=4sqrt2 sqrt(1-d^2).
        d2=max(0.0,1.0-eta*eta/32.0)
        d=np.sqrt(d2)
        geom=max(geom,max(0.0,rho*rho/64.0-(1.0-d*d)))
        rmin=(1.0-d)**2/(2.0*(1.0+d*d))
        mix=max(mix,max(0.0,rho**4/65536.0-rmin))

    print(f"worst average-efficiency lower violation: {avg:.3e}")
    print(f"worst efficient-sublaw half-action violation: {half:.3e}")
    print(f"worst nondegeneracy implication violation: {geom:.3e}")
    print(f"worst minority-polarization lower violation: {mix:.3e}")
    print(f"maximum sampled efficient pair-action signal: {signal:.3e}")
    assert avg<2e-12
    assert half<2e-12
    assert geom<2e-12
    assert mix<2e-12
    assert signal>1e-5
    print("PASS: fixed-critical rate gate forces efficient mixed-polarization action sublaw")


if __name__=='__main__': main()
