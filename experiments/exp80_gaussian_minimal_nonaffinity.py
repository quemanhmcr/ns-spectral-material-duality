"""Action-only referee for Gaussian-minimal nonaffinity after affine-gauge quotient."""
import numpy as np
from numpy.polynomial.hermite import hermgauss


def main():
    rng=np.random.default_rng(80082026)
    pyth=minimal=periodic=pde=0.0
    gauge_signal=0.0

    # Finite Gaussian weighted least-squares in vector polynomial states.
    # Use product Gauss-Hermite nodes, enough to integrate degree <= 8 exactly.
    x,w=hermgauss(7)
    nodes=[]; weights=[]
    norm=np.pi**1.5
    for i,xi in enumerate(x):
        for j,xj in enumerate(x):
            for k,xk in enumerate(x):
                nodes.append([xi,xj,xk]); weights.append(w[i]*w[j]*w[k]/norm)
    Z=np.asarray(nodes); W=np.asarray(weights)
    C=(Z.T*W)@Z

    for _ in range(300):
        c=rng.normal(size=3); A=rng.normal(size=(3,3))
        B=rng.normal(size=(3,3,3)); B=.5*(B+np.swapaxes(B,1,2))
        # physical normalized velocity with a quadratic nonaffine part
        V=np.empty((len(Z),3))
        for n,z in enumerate(Z):
            N=.5*np.einsum('abc,b,c->a',B,z,z)
            V[n]=c+A@z+N
        vbar=np.sum(W[:,None]*V,axis=0)
        centered=V-vbar
        Abar=((centered.T*W)@Z)@np.linalg.inv(C)
        RW=V-vbar-Z@Abar.T
        NK=V-c-Z@A.T
        ag=vbar-c; Bg=Abar-A
        rhs=RW+ag+Z@Bg.T
        pyth=max(pyth,np.linalg.norm(NK-rhs)/(1+np.linalg.norm(NK)+np.linalg.norm(rhs)))
        nr=np.sum(W*np.sum(RW*RW,axis=1))
        nn=np.sum(W*np.sum(NK*NK,axis=1))
        mismatch=float(ag@ag+np.trace(Bg@C@Bg.T))
        pyth=max(pyth,abs(nn-nr-mismatch)/(1+abs(nn)+abs(nr)+abs(mismatch)))
        # Adversarial random affine gauges cannot beat the orthogonal projection.
        for _j in range(8):
            da=rng.normal(size=3); dB=rng.normal(size=(3,3))
            cand=RW-da-Z@dB.T
            nc=np.sum(W*np.sum(cand*cand,axis=1))
            minimal=max(minimal,max(0.0,nr-nc)/(1+nr+nc))
        gauge_signal=max(gauge_signal,mismatch)

    # Exact periodic NSE shear with rho=pi^-1/2 exp(-y^2).
    nu=.28; t=.39; E=np.exp(-nu*t)
    x1,w1=hermgauss(100); W1=w1/np.sqrt(np.pi)
    Ey2=np.sum(W1*x1*x1)
    Eysin=np.sum(W1*x1*np.sin(x1))
    kappa=Eysin/Ey2
    NK=E*(np.sin(x1)-x1)
    RW=E*(np.sin(x1)-kappa*x1)
    nn=np.sum(W1*NK*NK); nr=np.sum(W1*RW*RW)
    target=.5*E*E*(1-np.exp(-.25))**2
    periodic=max(periodic,abs((nn-nr)-target)/(1+abs(nn)+abs(nr)+abs(target)),
                 abs(kappa-np.exp(-.25))/(1+abs(kappa)))
    for y in np.linspace(-np.pi,np.pi,2001):
        U=E*np.sin(y); Ut=-nu*U; Uyy=-U
        pde=max(pde,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))

    print(f"worst Gaussian Pythagorean affine-gauge residual: {pyth:.3e}")
    print(f"worst affine-minimality violation: {minimal:.3e}")
    print(f"exact periodic shear gauge-excess residual: {periodic:.3e}")
    print(f"worst exact periodic NSE residual: {pde:.3e}")
    print(f"maximum sampled affine-gauge mismatch energy: {gauge_signal:.3e}")
    assert pyth<3e-12
    assert minimal<2e-12
    assert periodic<3e-13
    assert pde<2e-14
    assert gauge_signal>1e-3
    print("PASS: Wang Gaussian residual is the minimal norm representative of the common affine-equivalence class")


if __name__=='__main__': main()
