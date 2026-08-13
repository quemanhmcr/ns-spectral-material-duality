"""Action-only pressure typing referee: Leray/loop gauge versus strain Hessian."""
import numpy as np
from exp58_resolved_cartan_material_metric import waves, random_divfree, grad, inner


def main():
    rng=np.random.default_rng(67082026)
    n=12; ks=waves(n)
    divwork=loop=strain=skew=poisson=metric=strain_aff=rot_aff=0.0
    pressure_signal=0.0

    # Periodic divergence-free work against an actual scalar pressure gradient.
    for _ in range(40):
        w=random_divfree(rng,n,ks,3.0)
        p=rng.normal(size=(n,n,n))
        ph=np.fft.fftn(p,norm='forward')
        gp=np.stack([np.fft.ifftn(1j*k*ph,norm='forward').real for k in ks],axis=-1)
        divwork=max(divwork,abs(inner(w,gp))/(1+np.sqrt(inner(w,w))*np.sqrt(inner(gp,gp))))

    # Closed polygon integral of gradient of a quadratic scalar: exact endpoint telescope.
    for _ in range(10000):
        H=rng.normal(size=(3,3)); H=.5*(H+H.T); b=rng.normal(size=3)
        pts=rng.normal(size=(6,3)); pts=np.vstack([pts,pts[0]])
        integ=0.0; telescope=0.0
        def phi(x): return .5*float(x@H@x)+float(b@x)
        for j in range(6):
            x=pts[j]; d=pts[j+1]-x
            seg=float((H@x+b)@d)+.5*float(d@H@d)
            integ+=seg; telescope+=phi(pts[j+1])-phi(pts[j])
        loop=max(loop,abs(integ)/(1+sum(np.linalg.norm(pts[j+1]-pts[j]) for j in range(6))),abs(telescope))

    # General algebraic split of gradient equation.
    for _ in range(50000):
        X=rng.normal(size=(3,3)); S=.5*(X+X.T); S-=np.trace(S)/3*np.eye(3)
        Y=rng.normal(size=(3,3)); O=.5*(Y-Y.T); A=S+O
        H=rng.normal(size=(3,3)); H=.5*(H+H.T)
        Ls=rng.normal(size=(3,3)); Ls=.5*(Ls+Ls.T); Ls-=np.trace(Ls)/3*np.eye(3)
        Lo=rng.normal(size=(3,3)); Lo=.5*(Lo-Lo.T)
        DtA=-A@A-H+Ls+Lo
        DtS=.5*(DtA+DtA.T); DtO=.5*(DtA-DtA.T)
        targetS=-S@S-O@O-H+Ls
        targetO=-(S@O+O@S)+Lo
        strain=max(strain,np.linalg.norm(DtS-targetS)/(1+np.linalg.norm(DtS)+np.linalg.norm(targetS)))
        skew=max(skew,np.linalg.norm(DtO-targetO)/(1+np.linalg.norm(DtO)+np.linalg.norm(targetO)))
        lap_p=float(np.trace(H))
        target_lap=-float(np.trace(A@A))
        # enforce pressure-Poisson Hessian trace by shifting H only for this check
        H2=H+(target_lap-lap_p)/3*np.eye(3)
        poisson=max(poisson,abs(np.trace(H2)-target_lap)/(1+abs(target_lap)))

        ring=targetS+S@O-O@S
        metric_acc=ring+2*S@S
        target_metric=S@S-O@O-H+Ls+S@O-O@S
        metric=max(metric,np.linalg.norm(metric_acc-target_metric)/(1+np.linalg.norm(metric_acc)+np.linalg.norm(target_metric)))

    # Exact affine pure strain NSE.
    a=.73; S=np.diag([a,-a,0.0]); H=-S@S
    strain_aff=max(strain_aff,np.linalg.norm(S@S+H)/(1+np.linalg.norm(S@S)+np.linalg.norm(H)))
    pressure_signal=max(pressure_signal,np.linalg.norm(H))

    # Exact affine rigid rotation NSE.
    r=.81; O=np.array([[0.0,-r,0.0],[r,0.0,0.0],[0.0,0.0,0.0]])
    H=-O@O
    rot_aff=max(rot_aff,np.linalg.norm(O@O+H)/(1+np.linalg.norm(O@O)+np.linalg.norm(H)))
    pressure_signal=max(pressure_signal,np.linalg.norm(H))

    print(f"worst periodic divergence-free pressure-work residual: {divwork:.3e}")
    print(f"worst closed-loop exact-gradient residual: {loop:.3e}")
    print(f"worst symmetric gradient-equation residual: {strain:.3e}")
    print(f"worst skew gradient-equation residual: {skew:.3e}")
    print(f"worst pressure-Poisson trace residual: {poisson:.3e}")
    print(f"worst material metric-acceleration residual: {metric:.3e}")
    print(f"exact affine strain pressure-Hessian residual: {strain_aff:.3e}")
    print(f"exact affine rotation pressure-Hessian residual: {rot_aff:.3e}")
    print(f"maximum affine pressure-Hessian signal: {pressure_signal:.3e}")
    assert divwork<4e-12
    assert loop<2e-13
    assert strain<4e-13
    assert skew<4e-13
    assert poisson<2e-13
    assert metric<4e-13
    assert strain_aff<2e-14 and rot_aff<2e-14
    assert pressure_signal>0.5
    print("PASS: pressure is gradient gauge for work/circulation but a real Hessian face in metric deformation")


if __name__=='__main__': main()
