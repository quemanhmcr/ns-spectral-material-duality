"""Action-only referee for the deterministic Cartan exterior-power physical ladder."""
import numpy as np


def cross_matrix(w):
    x,y,z=w
    return np.array([[0.0,-z,y],[z,0.0,-x],[-y,x,0.0]])


def det3(a,b,c):
    return float(np.linalg.det(np.column_stack([a,b,c])))


def main():
    rng=np.random.default_rng(64082026)
    wedge=strain2=skew2=pair=pairS=pairO=top=topS=topO=0.0
    signal=0.0
    for _ in range(50000):
        X=rng.normal(size=(3,3)); S=.5*(X+X.T); S-=np.trace(S)/3.0*np.eye(3)
        w=rng.normal(size=3); O=cross_matrix(w)
        A=S+O
        a,b,c=[rng.normal(size=3) for _ in range(3)]
        n=np.cross(a,b)

        lhs=np.cross(A@a,b)+np.cross(a,A@b)
        rhs=-A.T@n
        wedge=max(wedge,np.linalg.norm(lhs-rhs)/(1+np.linalg.norm(lhs)+np.linalg.norm(rhs)))

        lhsS=np.cross(S@a,b)+np.cross(a,S@b)
        strain2=max(strain2,np.linalg.norm(lhsS+S@n)/(1+np.linalg.norm(lhsS)+np.linalg.norm(S@n)))
        lhsO=np.cross(O@a,b)+np.cross(a,O@b)
        skew2=max(skew2,np.linalg.norm(lhsO-O@n)/(1+np.linalg.norm(lhsO)+np.linalg.norm(O@n)))

        x=rng.normal(size=3); m=rng.normal(size=3)
        pair=max(pair,abs(float((A@x)@m+x@(-A.T@m)))/(1+np.linalg.norm(A)*np.linalg.norm(x)*np.linalg.norm(m)))
        pairS=max(pairS,abs(float((S@x)@m-x@(S@m)))/(1+np.linalg.norm(S)*np.linalg.norm(x)*np.linalg.norm(m)))
        pairO=max(pairO,abs(float((O@x)@m+x@(O@m)))/(1+np.linalg.norm(O)*np.linalg.norm(x)*np.linalg.norm(m)))

        z1,z2,z3=[rng.normal(size=3) for _ in range(3)]
        dA=det3(A@z1,z2,z3)+det3(z1,A@z2,z3)+det3(z1,z2,A@z3)
        dS=det3(S@z1,z2,z3)+det3(z1,S@z2,z3)+det3(z1,z2,S@z3)
        dO=det3(O@z1,z2,z3)+det3(z1,O@z2,z3)+det3(z1,z2,O@z3)
        scale=1+abs(det3(z1,z2,z3))*(1+np.linalg.norm(A))
        top=max(top,abs(dA)/scale); topS=max(topS,abs(dS)/scale); topO=max(topO,abs(dO)/scale)
        signal=max(signal,np.linalg.norm(S),np.linalg.norm(O))

    # Exact periodic NS shear calibration of viscous material-vorticity flux.
    nu=.23; t=.37
    flux=0.0
    for y in np.linspace(-np.pi,np.pi,1001):
        E=np.exp(-nu*t)
        dU=E*np.cos(y)
        A=np.array([[0.0,dU,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
        omega=np.array([0.0,0.0,-E*np.cos(y)])
        lapomega=np.array([0.0,0.0,E*np.cos(y)])
        n=np.array([0.3,-0.4,1.2])
        Domega=A@omega+nu*lapomega
        Dn=-A.T@n
        lhs=float(Domega@n+omega@Dn)
        rhs=float(nu*lapomega@n)
        flux=max(flux,abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))

    print(f"worst Lambda2 Hodge generator residual: {wedge:.3e}")
    print(f"worst strain sign-flip residual on Lambda2: {strain2:.3e}")
    print(f"worst skew same-sign residual on Lambda2: {skew2:.3e}")
    print(f"worst full line/area pairing residual: {pair:.3e}")
    print(f"worst separate strain pairing residual: {pairS:.3e}")
    print(f"worst separate connection pairing residual: {pairO:.3e}")
    print(f"worst full/strain/skew top-form residuals: {top:.3e} {topS:.3e} {topO:.3e}")
    print(f"worst exact NS viscous material-flux residual: {flux:.3e}")
    print(f"maximum sampled Cartan signal: {signal:.3e}")
    assert wedge<4e-13
    assert strain2<4e-13
    assert skew2<4e-13
    assert pair<4e-13 and pairS<4e-13 and pairO<4e-13
    assert top<2e-12 and topS<2e-12 and topO<2e-12
    assert flux<2e-14
    assert signal>1.0
    print("PASS: incompressible Cartan generator has the rigid line/area/volume exterior sign ladder")


if __name__=='__main__': main()
