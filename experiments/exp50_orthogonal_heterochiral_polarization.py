"""Action-only adversarial referee for the exact orthogonal heterochiral polarization law."""
import numpy as np


def hbasis_pq(ep,eq,n,s,which):
    if which=='p':
        return (eq + 1j*s*n)/np.sqrt(2.0)
    # choose e1=-ep so q x e1 = n
    return (-ep + 1j*s*n)/np.sqrt(2.0)


def leray(k,v):
    k=np.asarray(k,dtype=float)
    return v-k*np.dot(k,v)/np.dot(k,k)


def unordered_source(k1,u1,k2,u2):
    k=k1+k2
    raw=1j*(np.dot(k2,u1)*u2+np.dot(k1,u2)*u1)
    return -leray(k,raw)


def main():
    rng=np.random.default_rng(50082026)
    normal=helicity_equal=sibling_zero=scale=0.0
    signal=0.0
    for _ in range(20000):
        # random orthonormal frame
        a=rng.normal(size=3); a/=np.linalg.norm(a)
        b=rng.normal(size=3); b-=a*np.dot(a,b); b/=np.linalg.norm(b)
        n=np.cross(a,b)
        N=float(rng.uniform(0.1,20.0))
        p=N*a; q=N*b
        hp=hbasis_pq(a,b,n,+1,'p')
        hq=hbasis_pq(a,b,n,-1,'q')
        A=(rng.normal()+1j*rng.normal())
        B=(rng.normal()+1j*rng.normal())
        um=unordered_source(p,A*hp,q,B*hq)
        # reality partner at -q uses conjugate vector/amplitude
        ul=unordered_source(p,A*hp,-q,np.conjugate(B*hq))
        normal=max(normal,np.linalg.norm(um-n*np.dot(n,um)),np.linalg.norm(ul-n*np.dot(n,ul)))
        signal=max(signal,np.linalg.norm(um),np.linalg.norm(ul))

        m=p+q; l=p-q
        # any normal vector has equal +/- helical projection magnitudes for planar m/l
        for k,u in [(m,um),(l,ul)]:
            kh=k/np.linalg.norm(k)
            e1=np.cross(n,kh); e1/=np.linalg.norm(e1)
            e2=np.cross(kh,e1)
            hplus=(e1+1j*e2)/np.sqrt(2.0)
            hminus=(e1-1j*e2)/np.sqrt(2.0)
            ap=abs(np.vdot(hplus,u)); am=abs(np.vdot(hminus,u))
            helicity_equal=max(helicity_equal,abs(ap-am))

        nextsrc=unordered_source(m,um,l,ul)
        sibling_zero=max(sibling_zero,np.linalg.norm(nextsrc))

        # source is bilinear in amplitude and linear in N
        lam=float(rng.uniform(0.2,4.0))
        um2=unordered_source(lam*p,A*hp,lam*q,B*hq)
        if np.linalg.norm(um)>1e-13:
            scale=max(scale,abs(np.linalg.norm(um2)/np.linalg.norm(um)-lam))

    print(f"worst first-generation off-normal source residual: {normal:.3e}")
    print(f"worst +/- helical birth-magnitude mismatch: {helicity_equal:.3e}")
    print(f"worst generated-sibling mutual-source residual: {sibling_zero:.3e}")
    print(f"worst wavenumber-scaling residual: {scale:.3e}")
    print(f"maximum sampled first-generation source signal: {signal:.3e}")
    assert normal<2e-11
    assert helicity_equal<2e-11
    assert sibling_zero<2e-10
    assert scale<2e-11
    assert signal>1e-3
    print("PASS: orthogonal equal-scale heterochiral source is normal-polarized and self-composition-null")


if __name__=='__main__': main()
