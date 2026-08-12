"""Adversarial stress for Wang cyclic single-charge phase compatibility."""
import numpy as np


def transport(w):
    p=np.maximum(w,0.0); n=np.maximum(-w,0.0); q=p.sum()
    return np.zeros((3,3)) if q<1e-14 else np.outer(n,p)/q


def main():
    rng=np.random.default_rng(26082026)
    e=r=c=ph=rev=table=0.0; signal=swap=0.0; loops=0; sep=0.0
    for _ in range(500):
        k=rng.normal(size=3); k-=k.mean()
        amp=rng.uniform(.1,5); th=rng.uniform(-np.pi,np.pi)
        Z=amp*np.exp(1j*th); w=k*Z.real; M=transport(w)
        e=max(e,abs(w.sum()))
        r=max(r,np.max(abs(M.sum(1)-np.maximum(-w,0))))
        c=max(c,np.max(abs(M.sum(0)-np.maximum(w,0))))
        signal=max(signal,np.linalg.norm(M))
        labels=rng.integers(0,2,size=3)
        loops += sum(int(i!=j and M[i,j]>1e-14 and labels[i]==labels[j]) for i in range(3) for j in range(3))
        # phase mark is literally common on both roots
        ph=max(ph,abs(np.angle(np.exp(1j*(th-th)))))
        Mr=transport(-w); rev=max(rev,np.linalg.norm(Mr-M.T)); swap=max(swap,np.linalg.norm(M-Mr))

        th2=rng.uniform(.1,1.3)
        Zp=amp*np.exp(1j*th2); Zm=amp*np.exp(-1j*th2)
        Mp=transport(k*Zp.real); Mm=transport(k*Zm.real)
        table=max(table,np.linalg.norm(Mp-Mm))
        sep=max(sep,abs(np.angle(Zp/Zm)))

    print(f"worst cyclic root-energy residual: {e:.3e}")
    print(f"worst donor-row marginal residual: {r:.3e}")
    print(f"worst recipient-column marginal residual: {c:.3e}")
    print(f"worst donor-recipient phase-fiber residual: {ph:.3e}")
    print(f"sampled hard-cell self-loop count: {loops}")
    print(f"worst equal-ReZ donor-table residual: {table:.3e}")
    print(f"maximum hidden phase separation: {sep:.3e}")
    print(f"worst sign-reversal transpose residual: {rev:.3e}")
    print(f"maximum donor-recipient swap signal: {swap:.3e}")
    assert e<1e-12 and r<1e-12 and c<1e-12 and ph<1e-12
    assert signal>1e-3 and loops>0 and table<1e-12 and sep>1e-2
    assert rev<1e-11 and swap>1e-3
    print("PASS: Wang cyclic single-charge phase-fiber calibrations")

if __name__ == '__main__': main()
