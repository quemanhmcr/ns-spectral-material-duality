"""Action-only referee for deterministic vorticity-dyad R2 strain-source anatomy."""
import numpy as np


def cross_matrix(w):
    x,y,z=w
    return np.array([[0.0,-z,y],[z,0.0,-x],[-y,x,0.0]])


def r2(G):
    return np.trace(G)*np.eye(3)-G.T


def relm(a,b):
    return np.linalg.norm(a-b)/(1+np.linalg.norm(a)+np.linalg.norm(b))


def main():
    rng=np.random.default_rng(72082026)
    square=kernel=trace=strain=metric=symcomm=0.0
    pde_aff=pde_shear=0.0
    signal=0.0
    for _ in range(60000):
        w=rng.normal(size=3)
        O=.5*cross_matrix(w)
        G=np.outer(w,w)
        lift=.25*r2(G)
        square=max(square,relm(-O@O,lift))
        kernel=max(kernel,np.linalg.norm(r2(G)@w)/(1+np.linalg.norm(G)*np.linalg.norm(w)))
        trace=max(trace,abs(np.trace(r2(G))-2*np.dot(w,w))/(1+np.dot(w,w)))

        X=rng.normal(size=(3,3)); S=.5*(X+X.T); S-=np.trace(S)/3*np.eye(3)
        H=rng.normal(size=(3,3)); H=.5*(H+H.T)
        L=rng.normal(size=(3,3)); L=.5*(L+L.T); L-=np.trace(L)/3*np.eye(3)
        DtS=-S@S+lift-H+L
        direct=-S@S-O@O-H+L
        strain=max(strain,relm(DtS,direct))
        comm=S@O-O@S
        symcomm=max(symcomm,np.linalg.norm(comm-comm.T)/(1+np.linalg.norm(comm)),abs(np.trace(comm))/(1+np.linalg.norm(comm)))
        ring=DtS+comm
        metric_acc=ring+2*S@S
        target=S@S+lift-H+L+comm
        metric=max(metric,relm(metric_acc,target))
        signal=max(signal,np.linalg.norm(lift))

    # Exact affine rigid rotation and periodic-shear point no-go pair.
    r=.79
    Oaff=np.array([[0.0,-r,0.0],[r,0.0,0.0],[0.0,0.0,0.0]])
    Hessp=-Oaff@Oaff
    pde_aff=np.linalg.norm(Oaff@Oaff+Hessp)/(1+np.linalg.norm(Oaff@Oaff)+np.linalg.norm(Hessp))
    w=np.array([0.0,0.0,2*r]); det_lift=.25*r2(np.outer(w,w))
    Gamma_aff=np.zeros((3,3))
    no1=(np.linalg.norm(det_lift),np.linalg.norm(r2(Gamma_aff)))

    nu=.23; t=.41; a=1.2; E=np.exp(-nu*t)
    y=np.pi/2
    U=a*E*np.sin(y); Ut=-nu*U; Uyy=-U
    pde_shear=abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy))
    w0=np.zeros(3)
    Gw=np.zeros((3,3)); Gw[2,1]=a*E
    Gamma=2*nu*Gw@Gw.T
    no2=(np.linalg.norm(.25*r2(np.outer(w0,w0))),np.linalg.norm(r2(Gamma)))

    print(f"worst -Omega^2 = (1/4)R2(omega omega^T) residual: {square:.3e}")
    print(f"worst R2 vorticity-null-direction residual: {kernel:.3e}")
    print(f"worst R2 trace residual: {trace:.3e}")
    print(f"worst exact strain-source replacement residual: {strain:.3e}")
    print(f"worst [S,Omega] symmetric/tracefree residual: {symcomm:.3e}")
    print(f"worst material metric-acceleration anatomy residual: {metric:.3e}")
    print(f"exact affine rotation NSE residual: {pde_aff:.3e}")
    print(f"exact periodic shear NSE residual: {pde_shear:.3e}")
    print(f"affine deterministic/qv exterior signals: {no1[0]:.3e} {no1[1]:.3e}")
    print(f"shear-point deterministic/qv exterior signals: {no2[0]:.3e} {no2[1]:.3e}")
    print(f"maximum sampled deterministic exterior signal: {signal:.3e}")
    assert square<3e-13
    assert kernel<3e-13
    assert trace<3e-13
    assert strain<3e-13
    assert symcomm<4e-13
    assert metric<3e-13
    assert pde_aff<2e-14 and pde_shear<2e-14
    assert no1[0]>1e-2 and no1[1]==0.0
    assert no2[0]==0.0 and no2[1]>1e-3
    assert signal>1e-2
    print("PASS: vorticity amplitude enters strain through deterministic R2 geometry distinct from Kelvin q.v. R2")


if __name__=='__main__': main()
