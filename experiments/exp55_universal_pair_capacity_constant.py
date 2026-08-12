"""Action-only adversarial referee for eta_pair <= 4sqrt(2)/27."""
import math
import numpy as np


def area(a,b,c):
    s=.5*(a+b+c)
    return math.sqrt(max(0.0,s*(s-a)*(s-b)*(s-c)))


def main():
    rng=np.random.default_rng(55082026)
    bound=casec=caseb=0.0
    signal=0.0
    C=4.0*math.sqrt(2.0)/27.0
    for _ in range(120000):
        a=float(rng.uniform(.01,20.0)); b=float(rng.uniform(.01,20.0))
        lo=max(a+1e-8,abs(a-b)+1e-8); hi=a+b-1e-8
        if hi<=lo: continue
        c=float(rng.uniform(lo,hi))
        K=max(b,c); D=area(a,b,c)
        eta=math.sqrt(2.0)*D*(c-a)*(a+c-b)/(a*c*K*K)
        bound=max(bound,max(0.0,eta-C)); signal=max(signal,eta)
        if c>=b:
            t=a/c; r=b/c
            rhs=(math.sqrt(2.0)/2.0)*r*(1-t)*(1+t-r)
            casec=max(casec,max(0.0,eta-rhs))
        else:
            t=a/b; r=c/b
            rhs=(math.sqrt(2.0)/2.0)*(r-t)*(t+r-1)
            caseb=max(caseb,max(0.0,eta-rhs))
    print(f"worst universal 4sqrt2/27 capacity violation: {bound:.3e}")
    print(f"worst K=c analytic-envelope violation: {casec:.3e}")
    print(f"worst K=b analytic-envelope violation: {caseb:.3e}")
    print(f"maximum sampled eta_pair: {signal:.9f}")
    print(f"proved universal envelope 4sqrt2/27: {C:.9f}")
    assert bound<2e-12
    assert casec<2e-12
    assert caseb<2e-12
    assert signal>0.1
    print("PASS: universal heterochiral pair-capacity envelope calibrations")


if __name__=='__main__': main()
