"""Action-only referee for passive packet gauge and physical residual ranking."""
import numpy as np


def relerr(a,b):
    return np.linalg.norm(a-b)/(1.0+np.linalg.norm(a)+np.linalg.norm(b))


def inv_random(rng):
    # QR times a strictly positive diagonal: every sampled matrix is invertible.
    q,_=np.linalg.qr(rng.normal(size=(3,3)))
    scales=np.exp(rng.uniform(-1.0,1.0,size=3))
    return q@np.diag(scales)


def main():
    rng=np.random.default_rng(87082026)
    residual=gauge_energy=gram=0.0
    raw_change_signal=0.0

    for _ in range(800):
        H=inv_random(rng)
        S=inv_random(rng)
        eps=rng.normal(size=3)
        r=np.linalg.solve(H.T,eps)
        Hp=H@S
        epsp=S.T@eps
        rp=np.linalg.solve(Hp.T,epsp)
        residual=max(residual,relerr(r,rp))

        G=H.T@H
        Gp=Hp.T@Hp
        gram=max(gram,relerr(Gp,S.T@G@S))
        e=float(eps@np.linalg.solve(G,eps))
        ep=float(epsp@np.linalg.solve(Gp,epsp))
        gauge_energy=max(gauge_energy,abs(e-ep)/(1+abs(e)+abs(ep)))
        raw_change_signal=max(raw_change_signal,abs(float(epsp@epsp)-float(eps@eps)))

    # Exact two-candidate raw-ranking reversal under a passive gauge.
    e1=np.array([1.,0.,0.]); e2=np.array([2.,0.,0.])
    H1=np.eye(3); H2=np.eye(3)
    phys1=float(e1@e1); phys2=float(e2@e2)
    S1=3*np.eye(3); S2=np.eye(3)
    ep1=S1.T@e1; ep2=S2.T@e2
    Hp1=H1@S1; Hp2=H2@S2
    r1p=np.linalg.solve(Hp1.T,ep1); r2p=np.linalg.solve(Hp2.T,ep2)
    ranking_res=max(relerr(r1p,e1),relerr(r2p,e2))
    raw_before=(float(e1@e1),float(e2@e2))
    raw_after=(float(ep1@ep1),float(ep2@ep2))
    ranking_flip_signal=(raw_after[0]-raw_after[1])-(raw_before[0]-raw_before[1])

    # Exact periodic NSE half-period residual tie represented in two gauges.
    nu=.21; t=.53; k=1.8
    E=np.exp(-nu*k*k*t); rho=np.pi/(2*k)
    def U(Y): return E*np.cos(k*Y)
    def Uy(Y): return -E*k*np.sin(k*Y)
    def chi(Y): return (U(Y)-U(Y+rho)+rho*Uy(Y))/(rho*rho)
    chi0=chi(0.0); chi1=chi(np.pi/k)
    target=4*E*k*k/np.pi**2
    chi_exact=max(abs(chi0-target)/(1+abs(chi0)+abs(target)),
                  abs(chi1+target)/(1+abs(chi1)+abs(target)))
    opposite=abs(chi0+chi1)/(1+abs(chi0)+abs(chi1))

    ez=np.array([0.,0.,1.])
    r0=chi0*ez; r1=chi1*ez
    physical_tie=abs(float(r0@r0)-float(r1@r1))/(1+float(r0@r0)+float(r1@r1))

    H0=np.eye(3); H1=np.eye(3); eps0=r0.copy(); eps1=r1.copy()
    S0=3*np.eye(3)
    H0p=H0@S0; eps0p=S0.T@eps0
    r0p=np.linalg.solve(H0p.T,eps0p)
    ns_residual=relerr(r0p,r0)
    G0p=H0p.T@H0p
    phys0p=float(eps0p@np.linalg.solve(G0p,eps0p))
    phys1=float(eps1@np.linalg.solve(H1.T@H1,eps1))
    ns_metric_tie=abs(phys0p-phys1)/(1+abs(phys0p)+abs(phys1))
    raw_ratio=float(eps0p@eps0p)/float(eps1@eps1)

    pde=0.0
    for y in np.linspace(-np.pi,np.pi,2001):
        val=E*np.cos(k*y); Ut=-nu*k*k*val; Uyy=-k*k*val
        pde=max(pde,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))

    print(f"passive-gauge physical-residual residual: {residual:.3e}")
    print(f"passive-gauge inverse-Gram energy residual: {gauge_energy:.3e}")
    print(f"packet-Gram congruence residual: {gram:.3e}")
    print(f"maximum sampled raw-coefficient change signal: {raw_change_signal:.3e}")
    print(f"two-candidate physical-residual invariance residual: {ranking_res:.3e}")
    print(f"two-candidate raw ranking-flip signal: {ranking_flip_signal:.3e}")
    print(f"exact NSE half-period amplitude residual: {chi_exact:.3e}")
    print(f"exact NSE opposite-residual residual: {opposite:.3e}")
    print(f"exact NSE physical-energy tie residual: {physical_tie:.3e}")
    print(f"exact NSE gauged physical-residual residual: {ns_residual:.3e}")
    print(f"exact NSE inverse-Gram energy tie residual: {ns_metric_tie:.3e}")
    print(f"exact NSE raw-coefficient energy ratio after gauge: {raw_ratio:.6f}")
    print(f"worst exact periodic NSE residual: {pde:.3e}")

    assert residual < 2e-12
    assert gauge_energy < 2e-12
    assert gram < 2e-12
    assert raw_change_signal > 1e-3
    assert ranking_res < 2e-14
    assert raw_before[0] < raw_before[1]
    assert raw_after[0] > raw_after[1]
    assert ranking_flip_signal > 1.0
    assert chi_exact < 2e-14
    assert opposite < 2e-14
    assert physical_tie < 2e-14
    assert ns_residual < 2e-14
    assert ns_metric_tie < 2e-14
    assert abs(raw_ratio-9.0) < 2e-13
    assert pde < 2e-14
    print("PASS: passive packet gauge leaves physical residual/metric fixed while raw ranking changes")


if __name__ == "__main__":
    main()
