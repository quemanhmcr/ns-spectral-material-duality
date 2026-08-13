"""Action-only referee for selector nonclosure and pair/Gram event functor."""
import numpy as np


def blockdiag(*blocks):
    rows=sum(b.shape[0] for b in blocks)
    cols=sum(b.shape[1] for b in blocks)
    out=np.zeros((rows,cols))
    r=c=0
    for b in blocks:
        rr,cc=b.shape
        out[r:r+rr,c:c+cc]=b
        r+=rr; c+=cc
    return out


def relerr(a,b):
    return np.linalg.norm(a-b)/(1.0+np.linalg.norm(a)+np.linalg.norm(b))


def main():
    rng=np.random.default_rng(81082026)
    I=np.eye(3); Z=np.zeros((3,3))
    E0=np.hstack((I,Z)); E1=np.hstack((Z,I))

    selector_block=selector_kernel=pair_switch=pair_functor=qv_functor=cross_block=0.0
    pair_hidden_signal=independent_signal=0.0

    # Exact selector obstruction and PSD pair-block nonclosure.
    for _ in range(500):
        T=rng.normal(size=(3,3))
        defect=E1-T@E0
        selector_block=max(selector_block,np.linalg.norm(defect[:,3:]-I))

        h=rng.normal(size=3)
        xh=np.concatenate((np.zeros(3),h))
        selector_kernel=max(selector_kernel, np.linalg.norm(E0@xh),
                            relerr(E1@xh,h))

        a=rng.normal(size=3); b1=rng.normal(size=3); b2=rng.normal(size=3)
        x1=np.concatenate((a,b1)); x2=np.concatenate((a,b2))
        P1=np.outer(x1,x1); P2=np.outer(x2,x2)
        pair_switch=max(pair_switch,relerr(E0@P1@E0.T,E0@P2@E0.T))
        pair_hidden_signal=max(pair_hidden_signal,
                               np.linalg.norm(E1@P1@E1.T-E1@P2@E1.T))

        # Exact switch expansion on an honest PSD pair state.
        x=rng.normal(size=6); P=np.outer(x,x); dE=E1-E0
        lhs=E1@P@E1.T-E0@P@E0.T
        rhs=dE@P@E0.T+E0@P@dE.T+dE@P@dE.T
        pair_switch=max(pair_switch,relerr(lhs,rhs))

    # Deterministic state-pair and same-replica q.v. share A P A^T functor.
    for _ in range(500):
        n=4; d=3
        X=rng.normal(size=n*d)
        A=rng.normal(size=(d,n*d))
        P=np.outer(X,X)
        pair_functor=max(pair_functor,relerr(np.outer(A@X,A@X),A@P@A.T))

        nu=.05+rng.random()
        Sigma=rng.normal(size=(n*d,3))
        Gamma=2*nu*Sigma@Sigma.T
        lhs=2*nu*(A@Sigma)@(A@Sigma).T
        rhs=A@Gamma@A.T
        qv_functor=max(qv_functor,relerr(lhs,rhs))

        # One common replica has genuine ordered cross-germ blocks.
        g,hidx=0,1
        block=Gamma[g*d:(g+1)*d,hidx*d:(hidx+1)*d]
        target=2*nu*Sigma[g*d:(g+1)*d]@Sigma[hidx*d:(hidx+1)*d].T
        cross_block=max(cross_block,relerr(block,target))

    # Exact one-mode periodic NSE calibration from the analytic Kelvin formula.
    nu=.29; t=.43; k=1.7
    E=np.exp(-nu*k*k*t)
    rho=np.pi/(2*k)
    Y1=np.pi/(2*k); Y2=3*np.pi/(2*k)

    def Uy(Y): return -E*k*np.sin(k*Y)
    def Uyy(Y): return -E*k*k*np.cos(k*Y)
    def q(Y): return (Uy(Y)-Uy(Y+rho)+rho*Uyy(Y))/(rho*rho)

    q1=q(Y1); q2=q(Y2)
    qtarget=4*E*k**3/np.pi**2
    opposite=abs(q1+q2)/(1+abs(q1)+abs(q2))
    exactq=max(abs(q1+qtarget)/(1+abs(q1)+abs(qtarget)),
               abs(q2-qtarget)/(1+abs(q2)+abs(qtarget)))

    S1=np.zeros((3,3)); S2=np.zeros((3,3))
    S1[2,1]=q1; S2[2,1]=q2
    Sigma=np.vstack((S1,S2))
    Gamma=2*nu*Sigma@Sigma.T
    Asum=np.hstack((I,I))
    synth_common=Asum@Gamma@Asum.T
    Gind=blockdiag(2*nu*S1@S1.T,2*nu*S2@S2.T)
    synth_ind=Asum@Gind@Asum.T
    common_cancel=np.linalg.norm(synth_common)/(1+np.linalg.norm(Gamma))
    independent_signal=np.linalg.norm(synth_ind)
    cross_exact=relerr(Gamma[:3,3:],-Gamma[:3,:3])

    pde=0.0
    for y in np.linspace(-np.pi,np.pi,2001):
        U=E*np.cos(k*y)
        Ut=-nu*k*k*U
        Uyyv=-k*k*U
        pde=max(pde,abs(Ut-nu*Uyyv)/(1+abs(Ut)+abs(nu*Uyyv)))

    print(f"selector h-block identity residual: {selector_block:.3e}")
    print(f"selector kernel-witness residual: {selector_kernel:.3e}")
    print(f"selected pair switch/old-block residual: {pair_switch:.3e}")
    print(f"maximum sampled hidden new-pair separation signal: {pair_hidden_signal:.3e}")
    print(f"deterministic tensor-square event residual: {pair_functor:.3e}")
    print(f"same-replica qv congruence residual: {qv_functor:.3e}")
    print(f"same-replica cross-germ block residual: {cross_block:.3e}")
    print(f"exact one-mode opposite-noise residual: {opposite:.3e}")
    print(f"exact one-mode analytic-q residual: {exactq:.3e}")
    print(f"exact one-mode cross-qv residual: {cross_exact:.3e}")
    print(f"same-replica synthesized qv cancellation residual: {common_cancel:.3e}")
    print(f"independent-noise synthesized qv signal: {independent_signal:.3e}")
    print(f"worst exact periodic NSE residual: {pde:.3e}")

    assert selector_block < 1e-14
    assert selector_kernel < 1e-14
    assert pair_switch < 2e-13
    assert pair_hidden_signal > 1e-3
    assert pair_functor < 3e-13
    assert qv_functor < 3e-13
    assert cross_block < 3e-13
    assert opposite < 2e-14
    assert exactq < 3e-14
    assert cross_exact < 3e-13
    assert common_cancel < 3e-13
    assert independent_signal > 1e-4
    assert pde < 2e-14
    print("PASS: selector readout requires persistent pair state and pair/qv share the exact event functor")


if __name__ == "__main__":
    main()
