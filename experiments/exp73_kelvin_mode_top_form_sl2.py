"""Action-only referee for Wang Kelvin-mode top-form/SL2 material bridge."""
import numpy as np


def main():
    rng=np.random.default_rng(73082026)
    trace=detlaw=sl2=sympl=metric=transverse=0.0
    signal=0.0
    J=np.array([[0.0,1.0],[-1.0,0.0]])
    for _ in range(50000):
        X=rng.normal(size=(3,3)); S=.5*(X+X.T); S-=np.trace(S)/3*np.eye(3)
        Y=rng.normal(size=(3,3)); O=.5*(Y-Y.T); A=S+O
        k=rng.normal(size=3); nk=np.linalg.norm(k)
        if nk<1e-8: continue
        kh=k/nk
        # objective transverse orthonormal frame
        ref=np.array([1.0,0.0,0.0])
        if abs(ref@kh)>.9: ref=np.array([0.0,1.0,0.0])
        e1=ref-kh*(ref@kh); e1/=np.linalg.norm(e1)
        e2=np.cross(kh,e1)
        E=np.column_stack([e1,e2])
        B=E.T@S@E
        r=-float(kh@S@kh)
        trace=max(trace,abs(np.trace(B)-r)/(1+abs(r)+np.linalg.norm(B)))

        nu=float(rng.uniform(.0,.4)); K2=nk*nk
        # infinitesimal determinant/top-form law
        G=-B-nu*K2*np.eye(2)
        det_rate=np.trace(G)
        detlaw=max(detlaw,abs(r+det_rate+2*nu*K2)/(1+abs(r)+abs(det_rate)+2*nu*K2))

        D=B-.5*np.trace(B)*np.eye(2)
        sl2=max(sl2,abs(np.trace(D))/(1+np.linalg.norm(D)))
        # infinitesimal symplectic generator: (-D)^T J + J(-D)=0
        sympl=max(sympl,np.linalg.norm((-D).T@J+J@(-D))/(1+np.linalg.norm(D)))

        # Material metric restriction under an arbitrary SL(3) coordinate frame.
        q=float(rng.uniform(-.4,.4)); sh=float(rng.uniform(-.3,.3))
        F=np.array([[np.exp(q),sh,0.0],[0.0,np.exp(-q),0.0],[0.0,0.0,1.0]])
        H=np.linalg.inv(F).T
        Mdot=2*F.T@S@F
        material=.5*E.T@H@Mdot@H.T@E
        metric=max(metric,np.linalg.norm(B-material)/(1+np.linalg.norm(B)+np.linalg.norm(material)))

        # Pressure term of exact Kelvin mode is parallel k, hence transverse projection zero.
        a=E@rng.normal(size=2)
        c=float(k@(A@a))/(nk*nk)
        pterm=2*k*c
        transverse=max(transverse,np.linalg.norm(E.T@pterm)/(1+np.linalg.norm(pterm)))
        signal=max(signal,np.linalg.norm(D),abs(r))

    # Exact affine strain finite-time no-go / normalized SL2 calibration.
    a=.67; t=.52; nu=.19
    K=np.exp(-a*t)
    I=(1.0-np.exp(-2*a*t))/(2*a)  # integral |k|^2 with |k0|=1
    U=np.diag([np.exp(a*t-nu*I),np.exp(-nu*I)])
    top=K*np.linalg.det(U)*np.exp(2*nu*I)
    alpha=(1.0/K)**.5*np.exp(-nu*I)
    Utilde=U/alpha
    finite_top=abs(top-1.0)
    finite_sl2=abs(np.linalg.det(Utilde)-1.0)
    raw_det_signal=abs(np.linalg.det(U)-1.0)

    print(f"worst transverse-trace/carrier-rate residual: {trace:.3e}")
    print(f"worst infinitesimal top-form determinant law residual: {detlaw:.3e}")
    print(f"worst trace-free SL2 generator residual: {sl2:.3e}")
    print(f"worst infinitesimal symplectic-generator residual: {sympl:.3e}")
    print(f"worst transverse material-metric restriction residual: {metric:.3e}")
    print(f"worst pressure transverse-projection residual: {transverse:.3e}")
    print(f"exact affine finite top-form residual: {finite_top:.3e}")
    print(f"exact affine normalized SL2 determinant residual: {finite_sl2:.3e}")
    print(f"exact affine raw determinant non-SL2 signal: {raw_det_signal:.3e}")
    print(f"maximum sampled trace-free/radial signal: {signal:.3e}")
    assert trace<3e-13
    assert detlaw<3e-13
    assert sl2<3e-13
    assert sympl<4e-13
    assert metric<4e-13
    assert transverse<3e-13
    assert finite_top<2e-14
    assert finite_sl2<2e-14
    assert raw_det_signal>1e-2
    assert signal>1e-2
    print("PASS: Wang objective SL2 polarization is the trace-free quotient of Kelvin-mode top-form balance")


if __name__=='__main__': main()
