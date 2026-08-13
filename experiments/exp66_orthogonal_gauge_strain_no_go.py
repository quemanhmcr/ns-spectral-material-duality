"""Action-only referee for orthogonal-gauge invariance of physical strain."""
import numpy as np


def main():
    rng=np.random.default_rng(66082026)
    sym=skew=eigs=frob=work=shear=0.0
    strain_signal=connection_signal=0.0
    for _ in range(50000):
        X=rng.normal(size=(3,3)); S=.5*(X+X.T); S-=np.trace(S)/3*np.eye(3)
        Y=rng.normal(size=(3,3)); Om=.5*(Y-Y.T)
        A=S+Om
        Z=rng.normal(size=(3,3)); O,_=np.linalg.qr(Z)
        W=rng.normal(size=(3,3)); C=.5*(W-W.T)
        At=O.T@A@O-C
        St=.5*(At+At.T); Ot=.5*(At-At.T)
        targetS=O.T@S@O; targetO=O.T@Om@O-C
        sym=max(sym,np.linalg.norm(St-targetS)/(1+np.linalg.norm(St)+np.linalg.norm(targetS)))
        skew=max(skew,np.linalg.norm(Ot-targetO)/(1+np.linalg.norm(Ot)+np.linalg.norm(targetO)))
        eigs=max(eigs,np.linalg.norm(np.sort(np.linalg.eigvalsh(St))-np.sort(np.linalg.eigvalsh(S)))/(1+np.linalg.norm(S)))
        frob=max(frob,abs(np.linalg.norm(St)-np.linalg.norm(S))/(1+np.linalg.norm(S)))
        a=rng.normal(size=3); b=rng.normal(size=3)
        lhs=float((O.T@a)@St@(O.T@b)); rhs=float(a@S@b)
        work=max(work,abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))
        strain_signal=max(strain_signal,np.linalg.norm(S))
        connection_signal=max(connection_signal,np.linalg.norm(C))

    # Exact periodic NS shear supplies a physical nonzero S which no rotation can erase.
    nu=.19; t=.43; E=np.exp(-nu*t); dU=E
    A=np.array([[0.0,dU,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
    S=.5*(A+A.T)
    spec=np.sort(np.linalg.eigvalsh(S))
    for _ in range(2000):
        Z=rng.normal(size=(3,3)); O,_=np.linalg.qr(Z)
        W=rng.normal(size=(3,3)); C=.5*(W-W.T)
        At=O.T@A@O-C; St=.5*(At+At.T)
        shear=max(shear,np.linalg.norm(np.sort(np.linalg.eigvalsh(St))-spec)/(1+np.linalg.norm(S)))
        if np.linalg.norm(St)<0.5*np.linalg.norm(S):
            raise AssertionError('orthogonal gauge spuriously removed exact NS strain')

    print(f"worst transformed-strain residual: {sym:.3e}")
    print(f"worst transformed-connection residual: {skew:.3e}")
    print(f"worst strain-spectrum invariance residual: {eigs:.3e}")
    print(f"worst strain-Frobenius invariance residual: {frob:.3e}")
    print(f"worst metric-work frame-invariance residual: {work:.3e}")
    print(f"worst exact-NS shear spectrum residual: {shear:.3e}")
    print(f"maximum sampled strain/observer-connection signals: {strain_signal:.3e} {connection_signal:.3e}")
    assert sym<2e-13
    assert skew<2e-13
    assert eigs<3e-13
    assert frob<2e-13
    assert work<3e-13
    assert shear<3e-13
    assert strain_signal>1 and connection_signal>1
    print("PASS: orthogonal observer gauge moves connection but cannot remove physical strain")


if __name__=='__main__': main()
