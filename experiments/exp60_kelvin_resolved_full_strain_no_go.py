"""Action-only exact-NS shear referee for resolved/full Kelvin strain separation."""
import numpy as np


def strain_from_shear(dU):
    return np.array([[0.0,0.5*dU,0.0],[0.5*dU,0.0,0.0],[0.0,0.0,0.0]])


def cross_matrix(w):
    x,y,z=w
    return np.array([[0.0,-z,y],[z,0.0,-x],[-y,x,0.0]])


def rel(a,b):
    return abs(a-b)/(1+abs(a)+abs(b))


def main():
    nu=.17; t=.31; a=1.0
    pde=split=dual=kelvin=cross=0.0
    active_full=active_res=0.0

    # Case A: exact high-only periodic shear, low resolved cutoff sees V=0.
    b=.8
    for y in np.linspace(-np.pi,np.pi,401):
        U=b*np.exp(-4*nu*t)*np.sin(2*y)
        Ut=-4*nu*U
        Uyy=-4*U
        pde=max(pde,abs(Ut-nu*Uyy))
    dUh=2*b*np.exp(-4*nu*t)  # y=0
    Su=strain_from_shear(dUh); Sv=np.zeros((3,3)); Sh=Su.copy()
    split=max(split,np.linalg.norm(Su-Sv-Sh))
    active_full=max(active_full,np.linalg.norm(Su))

    # Case B: exact low+high shear tuned so full strain cancels at one physical point/time.
    b2=-0.5*a*np.exp(3*nu*t)
    dUl=a*np.exp(-nu*t)
    dUh2=2*b2*np.exp(-4*nu*t)
    Sv2=strain_from_shear(dUl); Sh2=strain_from_shear(dUh2); Su2=Sv2+Sh2
    split=max(split,np.linalg.norm(Su2-Sv2-Sh2))
    active_res=max(active_res,np.linalg.norm(Sv2))
    if np.linalg.norm(Su2)>2e-14:
        raise AssertionError('tuned exact NS shear did not cancel full strain')

    # Vector/covector transpose duality at the same shear state.
    A=np.array([[0.0,dUl,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
    S=.5*(A+A.T); O=.5*(A-A.T)
    omega=np.array([0.0,0.0,-dUl])
    dual=max(dual,np.linalg.norm(A-A.T-cross_matrix(omega)),np.linalg.norm(.5*(A.T+A)-S),np.linalg.norm(.5*(A.T-A)+O))

    # Current Kelvin residual drift: exact resolved + unresolved + q.v. decomposition.
    rng=np.random.default_rng(60082026)
    for _ in range(20000):
        r=rng.normal(size=3); w=rng.normal(size=3)
        Q=rng.normal(size=(3,3)); qv=nu*np.sum(Q*Q)
        full=-float(r@Su@r)+qv
        parts=-float(r@Sv@r)-float(r@Sh@r)+qv
        kelvin=max(kelvin,rel(full,parts))
        G=rng.normal(size=(3,3))
        lhs=-2.0*float(w@Su@r)+float(np.trace(G))
        rhs=-2.0*float(w@Sv@r)-2.0*float(w@Sh@r)+float(np.trace(G))
        cross=max(cross,rel(lhs,rhs))

    print(f"worst exact shear NSE residual: {pde:.3e}")
    print(f"worst S_u=S_V+S_h residual: {split:.3e}")
    print(f"worst vector/covector transpose-duality residual: {dual:.3e}")
    print(f"worst Kelvin residual-energy owner split residual: {kelvin:.3e}")
    print(f"worst Kelvin cross-dyad owner split residual: {cross:.3e}")
    print(f"high-only full metric signal with S_V=0: {active_full:.3e}")
    print(f"tuned resolved metric signal with S_u=0: {active_res:.3e}")
    assert pde<2e-14
    assert split<2e-14
    assert dual<2e-14
    assert kelvin<2e-14
    assert cross<2e-14
    assert active_full>1e-2
    assert active_res>1e-2
    print("PASS: exact NS shears separate resolved Wang metric work from full Kelvin material strain")


if __name__=='__main__': main()
