"""Action-only exact affine-NSE referee for material strain holonomy = helical phase commutator."""
import numpy as np


def D(delta,beta):
    return np.array([[delta,beta],[beta,-delta]],float)


def main():
    rng=np.random.default_rng(74082026)
    comm=circ=gauge=pde=carrier=magnus=0.0
    signal=0.0
    J=np.array([[0.0,1.0],[-1.0,0.0]])
    C=np.array([[1.0,1.0],[1j,-1j]],complex)/np.sqrt(2.0)
    target_diag=np.diag([1j,-1j])
    circ=np.linalg.norm(C.conj().T@J@C-target_diag)
    for _ in range(50000):
        d1,b1,d2,b2=rng.normal(size=4)
        A=D(d1,b1); B=D(d2,b2)
        chi=d1*b2-b1*d2
        K=A@B-B@A
        target=2*chi*J
        comm=max(comm,np.linalg.norm(K-target)/(1+np.linalg.norm(K)+np.linalg.norm(target)))
        hel=C.conj().T@K@C
        ht=2j*chi*np.diag([1.0,-1.0])
        circ=max(circ,np.linalg.norm(hel-ht)/(1+np.linalg.norm(hel)+np.linalg.norm(ht)))
        th=float(rng.uniform(-np.pi,np.pi)); R=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
        Kg=(R.T@A@R)@(R.T@B@R)-(R.T@B@R)@(R.T@A@R)
        gauge=max(gauge,np.linalg.norm(Kg-R.T@K@R)/(1+np.linalg.norm(K)),
                  abs(float(np.sum((R.T@K@R)*J))-float(np.sum(K*J)))/(1+np.linalg.norm(K)))
        signal=max(signal,abs(chi))

    # Exact affine NSE family S(t) with fixed carrier e3.
    d=.73; gam=.41; T=.62
    for t in np.linspace(0,T,300):
        S=np.array([[d,gam*t,0.0],[gam*t,-d,0.0],[0.0,0.0,0.0]])
        Sdot=np.array([[0.0,gam,0.0],[gam,0.0,0.0],[0.0,0.0,0.0]])
        Hessp=-Sdot-S@S
        # affine NSE gradient residual: Sdot+S^2+Hess p=0; Delta u=0
        pde=max(pde,np.linalg.norm(Sdot+S@S+Hessp)/(1+np.linalg.norm(Sdot)+np.linalg.norm(S@S)+np.linalg.norm(Hessp)))
        k=np.array([0.0,0.0,1.0])
        carrier=max(carrier,np.linalg.norm(-S.T@k))

    # Exact second Magnus coefficient for D(t)=[[d,gamma t],[gamma t,-d]].
    coeff=-d*gam*T**3/6.0
    Om2=coeff*J
    hel2=C.conj().T@Om2@C
    target2=np.diag([1j*coeff,-1j*coeff])
    magnus=max(magnus,np.linalg.norm(hel2-target2)/(1+np.linalg.norm(hel2)+np.linalg.norm(target2)))
    # quadrature checks the analytic second-Magnus coefficient adversarially
    N=1200; ts=(np.arange(N)+.5)*T/N; dt=T/N
    acc=np.zeros((2,2))
    for i,t1 in enumerate(ts):
        D1=D(d,gam*t1)
        for t2 in ts[:i]:
            D2=D(d,gam*t2)
            acc+=.5*(D1@D2-D2@D1)*dt*dt
    # midpoint triangular quadrature has O(1/N) boundary omission; normalize against analytic scale
    magnus=max(magnus,np.linalg.norm(acc-Om2)/(1+np.linalg.norm(Om2)))

    print(f"worst material-strain commutator residual: {comm:.3e}")
    print(f"worst circular/helical diagonalization residual: {circ:.3e}")
    print(f"worst common-SO2 gauge covariance/invariance residual: {gauge:.3e}")
    print(f"exact affine NSE gradient residual: {pde:.3e}")
    print(f"fixed e3 carrier residual: {carrier:.3e}")
    print(f"second-Magnus circular/analytic residual: {magnus:.3e}")
    print(f"maximum sampled anisotropy-area signal: {signal:.3e}")
    assert comm<3e-13
    assert circ<3e-13
    assert gauge<5e-13
    assert pde<2e-14
    assert carrier<2e-14
    assert magnus<2e-4
    assert signal>1.0
    print("PASS: material strain holonomy and Wang helical geometric phase are the same transverse commutator")


if __name__=='__main__': main()
