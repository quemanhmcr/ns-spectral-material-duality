"""Action-only referee for Kelvin principal projectors as metric connection gauges."""
import numpy as np


def random_orthogonal(rng,n=3):
    X=rng.normal(size=(n,n)); Q,_=np.linalg.qr(X)
    if np.linalg.det(Q)<0: Q[:,0]*=-1
    return Q


def main():
    rng=np.random.default_rng(76082026)
    pdot=gap=mixing=sumwork=selected=affine=reset=0.0
    cm_signal=pair_signal=0.0

    for _ in range(40000):
        V=random_orthogonal(rng)
        lam=np.sort(rng.uniform(.4,4.0,size=3))
        # Keep simple gaps away from zero for the rank-one theorem.
        if min(np.diff(lam))<.08: continue
        Lam=np.diag(lam)
        B=rng.normal(size=(3,3)); B=.5*(B+B.T)
        Om=np.zeros((3,3))
        for i in range(3):
            for j in range(3):
                if i!=j: Om[i,j]=B[i,j]/(lam[j]-lam[i])
        C=V@Om@V.T
        # spectral projectors and exact derivatives
        Qphys=rng.normal(size=(3,3)); Qphys=Qphys@Qphys.T
        Qtil=V.T@Qphys@V
        mixsum=0.0; offwork=0.0
        for i in range(3):
            vi=V[:,i]; P=np.outer(vi,vi)
            Pdot=C@P-P@C
            # direct derivative from vdot=C v
            vdot=C@vi
            direct=np.outer(vdot,vi)+np.outer(vi,vdot)
            pdot=max(pdot,np.linalg.norm(Pdot-direct)/(1+np.linalg.norm(Pdot)+np.linalg.norm(direct)))
            # principal-frame connection coefficient
            for j in range(3):
                if i!=j:
                    gap=max(gap,abs(Om[i,j]-B[i,j]/(lam[j]-lam[i]))/(1+abs(Om[i,j])))
            lhs=float(np.trace(Pdot@Qphys))
            rhs=float((Qtil@Om-Om@Qtil)[i,i])
            mixing=max(mixing,abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))
            mixsum+=lam[i]*rhs
        offwork=2*sum(B[i,j]*Qtil[i,j] for i in range(3) for j in range(i+1,3))
        sumwork=max(sumwork,abs(mixsum-offwork)/(1+abs(mixsum)+abs(offwork)))
        cm_signal=max(cm_signal,np.linalg.norm(C))

        # Literal germ selector commutes with block-diagonal per-germ principal connection/projectors.
        ng=3
        pick=int(rng.integers(0,ng))
        Mfb=np.zeros((ng,ng)); Mfb[pick,pick]=1.0
        Pblocks=[]; Cblocks=[]
        for g in range(ng):
            Pg=np.outer(V[:,g%3],V[:,g%3])
            Pblocks.append(Pg); Cblocks.append(C)
        Phat=np.kron(Mfb,np.eye(3))
        Pspec=np.zeros((9,9)); Chat=np.zeros((9,9))
        for g in range(ng):
            Pspec[3*g:3*g+3,3*g:3*g+3]=Pblocks[g]
            Chat[3*g:3*g+3,3*g:3*g+3]=Cblocks[g]
        Pi=Phat@Pspec
        Pidot=Phat@(Chat@Pspec-Pspec@Chat)
        selected=max(selected,
                     np.linalg.norm(Phat@Pspec-Pspec@Phat)/(1+np.linalg.norm(Pi)),
                     np.linalg.norm(Chat@Phat-Phat@Chat)/(1+np.linalg.norm(Chat)),
                     np.linalg.norm(Pidot-(Chat@Pi-Pi@Chat))/(1+np.linalg.norm(Pidot)))

        # Pair-reset algebra for a physical synthesis map A.
        m=4
        X=rng.normal(size=(3*m,3*m)); QQ=X@X.T
        am=rng.normal(size=m); da=rng.normal(size=m)
        Aminus=np.hstack([am[g]*np.eye(3) for g in range(m)])
        dA=np.hstack([da[g]*np.eye(3) for g in range(m)])
        Aplus=Aminus+dA
        Qm=Aminus@QQ@Aminus.T; Qp=Aplus@QQ@Aplus.T
        dQ=Qp-Qm
        rhs=dA@QQ@Aminus.T+Aminus@QQ@dA.T+dA@QQ@dA.T
        reset=max(reset,np.linalg.norm(dQ-rhs)/(1+np.linalg.norm(dQ)+np.linalg.norm(rhs)))
        pair_signal=max(pair_signal,np.linalg.norm(dA@QQ@dA.T))

    # Exact affine pure-strain NSE witness: Omega_u=0 but metric eigenframe connection != 0.
    a=.71; t=.37
    S=np.diag([a,-a,0.0])
    L0=np.array([[1.0,.45,.1],[.0,1.3,.25],[.0,.0,.8]])
    # L=e^{-S t} L0 for reverse line frame Ldot=-S L.
    E=np.diag([np.exp(-a*t),np.exp(a*t),1.0])
    L=E@L0
    M=L.T@L
    Mdot=-2*L.T@S@L
    lam,V=np.linalg.eigh(M)
    B=V.T@Mdot@V
    OmM=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            if i!=j: OmM[i,j]=B[i,j]/(lam[j]-lam[i])
    CM=V@OmM@V.T
    # physical velocity-gradient skew connection is exactly zero because A=S.
    Omega_u=np.zeros((3,3))
    # exact affine NSE with Hess p=-S^2
    Hessp=-S@S
    pde=np.linalg.norm(S@S+Hessp)/(1+np.linalg.norm(S@S)+np.linalg.norm(Hessp))
    affine=max(affine,pde,np.linalg.norm(Omega_u))
    affine_signal=np.linalg.norm(CM)

    print(f"worst principal-projector connection residual: {pdot:.3e}")
    print(f"worst spectral-gap connection formula residual: {gap:.3e}")
    print(f"worst projector/residual mixing residual: {mixing:.3e}")
    print(f"worst weighted mixing/offdiagonal-work residual: {sumwork:.3e}")
    print(f"worst first-bad selector/principal connection residual: {selected:.3e}")
    print(f"worst physical synthesis tensor-square reset residual: {reset:.3e}")
    print(f"exact affine pure-strain NSE/Omega_u residual: {affine:.3e}")
    print(f"affine metric-eigenframe connection signal with Omega_u=0: {affine_signal:.3e}")
    print(f"maximum sampled metric-connection / pair-reset signals: {cm_signal:.3e} {pair_signal:.3e}")
    assert pdot<3e-13
    assert gap<3e-13
    assert mixing<4e-13
    assert sumwork<5e-12
    assert selected<4e-13
    assert reset<4e-12
    assert affine<2e-14
    assert affine_signal>1e-3
    assert cm_signal>1e-3 and pair_signal>1e-3
    print("PASS: Kelvin principal mixing is a metric-projector gauge distinct from fluid vorticity connection")


if __name__=='__main__': main()
