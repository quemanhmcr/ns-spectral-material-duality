"""Action-only full-vector referee for spin-2 azimuthal polarization cancellation."""
import numpy as np


def rotz(phi):
    c=np.cos(phi); s=np.sin(phi)
    return np.array([[c,-s,0.0],[s,c,0.0],[0.0,0.0,1.0]])


def h_from_normal(k,s,n):
    k=np.asarray(k,float); kh=k/np.linalg.norm(k)
    e1=np.asarray(n,float); e1=e1-kh*np.dot(kh,e1); e1/=np.linalg.norm(e1)
    e2=np.cross(kh,e1)
    return (e1+1j*s*e2)/np.sqrt(2.0)


def leray(k,v):
    k=np.asarray(k,float)
    return v-k*np.dot(k,v)/np.dot(k,k)


def source(p,up,q,uq):
    k=p+q
    return -1j*leray(k,np.dot(q,up)*uq+np.dot(p,uq)*up)


def main():
    rng=np.random.default_rng(57082026)
    plus=minus=cancel=work=0.0
    signal=0.0
    for _ in range(15000):
        c=float(rng.uniform(1.0,8.0))
        z1=float(rng.uniform(.15*c,.85*c))
        r=float(rng.uniform(.2*c,1.5*c))
        k=np.array([0.0,0.0,c])
        p0=np.array([r,0.0,z1]); q0=k-p0
        n0=np.cross(p0,q0); n0/=np.linalg.norm(n0)
        hp0=h_from_normal(p0,+1,n0)
        hq0=h_from_normal(q0,-1,n0)
        F0=source(p0,hp0,q0,hq0)
        # fixed child basis using y as transverse e1
        hplus=h_from_normal(k,+1,np.array([0.0,1.0,0.0]))
        hminus=h_from_normal(k,-1,np.array([0.0,1.0,0.0]))
        fp0=np.vdot(hplus,F0); fm0=np.vdot(hminus,F0)
        if abs(fp0)<1e-10 or abs(fm0)<1e-10:
            continue
        signal=max(signal,abs(fp0),abs(fm0))
        vals=[]
        for phi in [0.0,np.pi/2]:
            R=rotz(phi)
            p=R@p0; q=R@q0
            hp=R@hp0; hq=R@hq0
            F=np.exp(1j*phi)*source(p,hp,q,hq)
            fp=np.vdot(hplus,F); fm=np.vdot(hminus,F)
            plus=max(plus,abs(fp-fp0)/(1+abs(fp0)))
            minus=max(minus,abs(fm-np.exp(2j*phi)*fm0)/(1+abs(fm0)))
            vals.append((fp,fm))
        fp_sum=vals[0][0]+vals[1][0]
        fm_sum=vals[0][1]+vals[1][1]
        cancel=max(cancel,abs(fp_sum-2*fp0)/(1+2*abs(fp0)),abs(fm_sum)/(1+abs(fm0)))
        # Choose child scalar phase equal to fp0: both plus works positive and equal.
        achild=fp0
        w0=float(np.real(np.conjugate(achild)*vals[0][0]))
        w1=float(np.real(np.conjugate(achild)*vals[1][0]))
        work=max(work,max(0.0,-w0),max(0.0,-w1),abs(w0-w1)/(1+abs(w0)+abs(w1)))

    print(f"worst aligned plus-source rotation residual: {plus:.3e}")
    print(f"worst spin-2 minority rotation residual: {minus:.3e}")
    print(f"worst two-atom polarization-cancellation residual: {cancel:.3e}")
    print(f"worst simultaneous positive-work violation: {work:.3e}")
    print(f"maximum sampled nondegenerate source signal: {signal:.3e}")
    assert plus<2e-11
    assert minus<2e-11
    assert cancel<2e-11
    assert work<2e-11
    assert signal>1e-3
    print("PASS: edgewise mixed birth can cancel by exact spin-2 azimuthal organization")


if __name__=='__main__': main()
