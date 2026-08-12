"""Action-only referee for the exact heterochiral child-birth polarization law."""
import math
import numpy as np


def area(a,b,c):
    s=.5*(a+b+c)
    return math.sqrt(max(0.0,s*(s-a)*(s-b)*(s-c)))


def main():
    rng=np.random.default_rng(51082026)
    ratio=stokes=minority=source=purity=0.0
    signal=0.0
    for _ in range(60000):
        a=float(rng.uniform(.05,12.0)); b=float(rng.uniform(.05,12.0))
        lo=abs(a-b)+1e-6; hi=a+b-1e-6
        if hi<=lo: continue
        c=float(rng.uniform(lo,hi))
        d=(a-b)/c
        D=area(a,b,c)
        amp=float(rng.uniform(1e-4,5.0))
        pref=(a+b)*D/(math.sqrt(2.0)*a*b*c)*amp
        fp=pref*(c+a-b)
        fm=pref*(c-a+b)
        if fm>1e-15:
            ratio=max(ratio,abs(fp/fm-(1+d)/(1-d)))
        den=fp*fp+fm*fm
        if den>1e-20:
            pol=(fp*fp-fm*fm)/den
            stokes=max(stokes,abs(pol-2*d/(1+d*d)))
            rmin=min(fp*fp,fm*fm)/den
            target=(1-abs(d))**2/(2*(1+d*d))
            minority=max(minority,abs(rmin-target))
            if rmin<=0.05:
                purity=max(purity,max(0.0,(1-abs(d))-2*math.sqrt(rmin)))
        lhs=fp*fp+fm*fm
        rhs=((a+b)**2*c*c*((a+b)**2-c*c)/(16*a*a*b*b))*(1-d**4)*amp*amp
        source=max(source,abs(lhs-rhs)/(1+abs(rhs)))
        signal=max(signal,math.sqrt(max(lhs,0.0)))

    print(f"worst child-helicity amplitude-ratio residual: {ratio:.3e}")
    print(f"worst fresh-source Stokes-polarization residual: {stokes:.3e}")
    print(f"worst minority-helicity fraction residual: {minority:.3e}")
    print(f"worst total-source Heron formula relative residual: {source:.3e}")
    print(f"worst near-pure degeneracy implication violation: {purity:.3e}")
    print(f"maximum sampled heterochiral birth-source signal: {signal:.3e}")
    assert ratio<3e-10
    assert stokes<3e-12
    assert minority<3e-12
    assert source<3e-10
    assert purity<3e-12
    assert signal>1e-3
    print("PASS: heterochiral fresh-birth polarization / purity-coupling tradeoff calibrations")


if __name__=='__main__': main()
