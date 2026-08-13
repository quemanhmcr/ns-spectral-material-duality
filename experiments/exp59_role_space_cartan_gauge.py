"""Action-only role-gauge referee: K is a 2-form and S a metric-velocity form."""
import numpy as np
from exp58_resolved_cartan_material_metric import waves, random_divfree, apply, grad, inner


def orthonormalize(fields):
    out=[]
    for f in fields:
        v=f.copy()
        for q in out:
            v-=inner(q,v)*q
        n=np.sqrt(inner(v,v))
        if n<1e-9: raise RuntimeError('degenerate role basis')
        out.append(v/n)
    return out


def matrices(V,W,ks):
    m=len(W); K=np.zeros((m,m)); S=np.zeros((m,m))
    KW=[apply(V,w,ks,'K') for w in W]
    SW=[apply(V,w,ks,'S') for w in W]
    for a in range(m):
        for b in range(m):
            K[a,b]=inner(W[a],KW[b])
            S[a,b]=inner(W[a],SW[b])
    return K,S


def main():
    rng=np.random.default_rng(59082026)
    n=8; ks=waves(n)
    kskew=ssym=congk=congs=traceq=quad=metric=0.0
    signal=0.0
    for _ in range(24):
        V=random_divfree(rng,n,ks,2.0)
        W=orthonormalize([random_divfree(rng,n,ks,3.0) for _ in range(4)])
        K,S=matrices(V,W,ks)
        kskew=max(kskew,np.linalg.norm(K+K.T)/(1+np.linalg.norm(K)))
        ssym=max(ssym,np.linalg.norm(S-S.T)/(1+np.linalg.norm(S)))
        X=rng.normal(size=(4,4)); O,_=np.linalg.qr(X)
        Wp=[]
        for a in range(4):
            w=sum((O[b,a]*W[b] for b in range(4)),start=np.zeros_like(W[0]))
            Wp.append(w)
        Kp,Sp=matrices(V,Wp,ks)
        congk=max(congk,np.linalg.norm(Kp-O.T@K@O)/(1+np.linalg.norm(Kp)))
        congs=max(congs,np.linalg.norm(Sp-O.T@S@O)/(1+np.linalg.norm(Sp)))
        traceq=max(traceq,abs(np.trace(Sp)-np.trace(S))/(1+abs(np.trace(S))))
        c=rng.normal(size=4)
        h=sum((c[a]*W[a] for a in range(4)),start=np.zeros_like(W[0]))
        q1=float(c@K@c); q2=float(c@S@c); direct=inner(h,apply(V,h,ks,'L'))
        quad=max(quad,abs(q1)/(1+abs(q2)),abs(q2-direct)/(1+abs(q2)+abs(direct)))
        signal=max(signal,np.linalg.norm(S),np.linalg.norm(K))

        # One fixed SL(3) material coordinate frame: entire S role matrix is metric velocity.
        A=grad(V,ks); Sv=0.5*(A+np.swapaxes(A,-1,-2))
        q=.23; sh=-.17
        F=np.array([[np.exp(q),sh,0.0],[0.0,np.exp(-q),0.0],[0.0,0.0,1.0]])
        H=np.linalg.inv(F).T
        for a in range(4):
            for b in range(4):
                wa=W[a]; wb=W[b]
                # vectorized local congruence
                pa=np.einsum('ij,...j->...i',H.T,wa)
                pb=np.einsum('ij,...j->...i',H.T,wb)
                Mdot=np.einsum('ji,...jk,kl->...il',F,Sv,F)*2.0
                met=.5*float(np.mean(np.einsum('...i,...ij,...j->...',pa,Mdot,pb)))
                metric=max(metric,abs(S[a,b]-met)/(1+abs(S[a,b])+abs(met)))

    print(f"worst role-K skew residual: {kskew:.3e}")
    print(f"worst role-S symmetry residual: {ssym:.3e}")
    print(f"worst K congruence residual: {congk:.3e}")
    print(f"worst S congruence residual: {congs:.3e}")
    print(f"worst S trace-gauge residual: {traceq:.3e}")
    print(f"worst role quadratic reconstruction residual: {quad:.3e}")
    print(f"worst whole-matrix material metric residual: {metric:.3e}")
    print(f"maximum sampled role tensor signal: {signal:.3e}")
    assert kskew<3e-11
    assert ssym<3e-11
    assert congk<4e-11
    assert congs<4e-11
    assert traceq<4e-11
    assert quad<4e-11
    assert metric<4e-11
    assert signal>1e-4
    print("PASS: Wang role K/S is a skew 2-form plus one material metric-velocity form")


if __name__=='__main__': main()
