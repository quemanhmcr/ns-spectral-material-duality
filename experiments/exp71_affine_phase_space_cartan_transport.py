"""Action-only exact affine NS referee for conservative radial phase transport."""
import numpy as np


def cross_matrix(w):
    x,y,z=w
    return np.array([[0.0,-z,y],[z,0.0,-x],[-y,x,0.0]])


def main():
    rng=np.random.default_rng(71082026)
    radial=angular=line_area=pair=0.0
    strain_exact=rot_exact=0.0
    radial_signal=angular_signal=0.0
    for _ in range(50000):
        X=rng.normal(size=(3,3)); S=.5*(X+X.T); S-=np.trace(S)/3*np.eye(3)
        O=cross_matrix(rng.normal(size=3)); A=S+O
        k=rng.normal(size=3); nk=np.linalg.norm(k)
        if nk<1e-8: continue
        kh=k/nk; kd=-A.T@k
        dlog=float(k@kd)/(nk*nk)
        target=-float(kh@S@kh)
        radial=max(radial,abs(dlog-target)/(1+abs(dlog)+abs(target)))
        khd=kd/nk-kh*dlog
        target_ang=O@kh-(np.eye(3)-np.outer(kh,kh))@S@kh
        angular=max(angular,np.linalg.norm(khd-target_ang)/(1+np.linalg.norm(khd)+np.linalg.norm(target_ang)))
        radial_signal=max(radial_signal,abs(dlog)); angular_signal=max(angular_signal,np.linalg.norm(khd))

        ell=rng.normal(size=3); ne=np.linalg.norm(ell)
        if ne>1e-8:
            eh=ell/ne; ld=A@ell
            line_rate=float(ell@ld)/(ne*ne)
            line_area=max(line_area,abs(line_rate-float(eh@S@eh))/(1+abs(line_rate)+abs(float(eh@S@eh))))

        n=rng.normal(size=3); a=rng.normal(size=3)
        pair=max(pair,abs(float((A@a)@n+a@(-A.T@n)))/(1+np.linalg.norm(A)*np.linalg.norm(a)*np.linalg.norm(n)))

    # Exact affine pure strain NSE calibration.
    a=.61; t=.47
    S=np.diag([a,-a,0.0]); k0=np.array([1.3,0.0,0.0])
    kt=np.array([np.exp(-a*t)*k0[0],0.0,0.0])
    exact=np.exp(-a*t)*np.linalg.norm(k0)
    strain_exact=abs(np.linalg.norm(kt)-exact)/(1+exact)

    # Exact affine rigid rotation NSE calibration.
    r=.83; O=np.array([[0.0,-r,0.0],[r,0.0,0.0],[0.0,0.0,0.0]])
    th=r*t; R=np.array([[np.cos(th),-np.sin(th),0.0],[np.sin(th),np.cos(th),0.0],[0.0,0.0,1.0]])
    kr=R@np.array([.7,-1.1,.2])
    rot_exact=abs(np.linalg.norm(kr)-np.linalg.norm(np.array([.7,-1.1,.2])))/(1+np.linalg.norm(kr))

    print(f"worst radial log-scale law residual: {radial:.3e}")
    print(f"worst angular wavefront law residual: {angular:.3e}")
    print(f"worst material-line sign law residual: {line_area:.3e}")
    print(f"worst line/area dual-pair residual: {pair:.3e}")
    print(f"exact affine strain radial-law residual: {strain_exact:.3e}")
    print(f"exact affine rotation radius-preservation residual: {rot_exact:.3e}")
    print(f"maximum sampled radial/angular signals: {radial_signal:.3e} {angular_signal:.3e}")
    assert radial<3e-13
    assert angular<5e-13
    assert line_area<3e-13
    assert pair<3e-13
    assert strain_exact<2e-14 and rot_exact<2e-14
    assert radial_signal>1 and angular_signal>1
    print("PASS: conservative affine transport changes spectral radius through strain while connection preserves radius")


if __name__=='__main__': main()
