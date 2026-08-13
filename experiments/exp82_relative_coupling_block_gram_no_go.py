"""Action-only referee for the relative-coupling block-Gram no-go."""
import numpy as np


def relerr(a,b):
    return np.linalg.norm(a-b)/(1.0+np.linalg.norm(a)+np.linalg.norm(b))


def orthogonal(rng,n=3):
    q,r=np.linalg.qr(rng.normal(size=(n,n)))
    # QR sign convention is irrelevant; any orthogonal q is acceptable.
    return q


def main():
    rng=np.random.default_rng(82082026)
    I=np.eye(3)
    Asum=np.hstack((I,I))

    wang_common=wang_diag=kelvin_common=kelvin_diag=0.0
    wang_cross_signal=wang_synth_signal=0.0
    kelvin_cross_signal=kelvin_synth_signal=0.0

    # Wang complex pair state: common phase leaves the full pair, relative phase does not.
    for _ in range(500):
        f1=rng.normal(size=3)+1j*rng.normal(size=3)
        f2=rng.normal(size=3)+1j*rng.normal(size=3)
        X=np.concatenate((f1,f2))
        G=np.outer(X,np.conjugate(X))

        theta=rng.uniform(-np.pi,np.pi)
        Xc=np.exp(1j*theta)*X
        Gc=np.outer(Xc,np.conjugate(Xc))
        wang_common=max(wang_common,relerr(G,Gc))

        t1,t2=rng.uniform(-np.pi,np.pi,2)
        f1p=np.exp(1j*t1)*f1; f2p=np.exp(1j*t2)*f2
        Xp=np.concatenate((f1p,f2p))
        Gp=np.outer(Xp,np.conjugate(Xp))
        wang_diag=max(wang_diag,
                      relerr(G[:3,:3],Gp[:3,:3]),
                      relerr(G[3:,3:],Gp[3:,3:]))
        wang_cross_signal=max(wang_cross_signal,np.linalg.norm(G[:3,3:]-Gp[:3,3:]))
        wang_synth_signal=max(wang_synth_signal,
                              np.linalg.norm(Asum@G@Asum.T.conj()-Asum@Gp@Asum.T.conj()))

    # Deterministic two-child phase witness: same diagonals, synthesis 4 vv* versus 0.
    v=np.array([1+2j,-.5+.3j,.7-1.1j])
    Gplus=np.outer(np.concatenate((v,v)),np.conjugate(np.concatenate((v,v))))
    Gminus=np.outer(np.concatenate((v,-v)),np.conjugate(np.concatenate((v,-v))))
    wang_witness_diag=max(relerr(Gplus[:3,:3],Gminus[:3,:3]),
                          relerr(Gplus[3:,3:],Gminus[3:,3:]))
    wang_witness_plus=Asum@Gplus@Asum.T.conj()
    wang_witness_minus=Asum@Gminus@Asum.T.conj()
    wang_witness_zero=np.linalg.norm(wang_witness_minus)
    wang_witness_signal=np.linalg.norm(wang_witness_plus)

    # Kelvin one-common-driver Gram: common O(3) is gauge; independent O_g changes cross blocks.
    nu=.37
    for _ in range(500):
        S1=rng.normal(size=(3,3)); S2=rng.normal(size=(3,3))
        Sigma=np.vstack((S1,S2)); Gamma=2*nu*Sigma@Sigma.T

        O=orthogonal(rng)
        Sigmac=np.vstack((S1@O,S2@O)); Gammac=2*nu*Sigmac@Sigmac.T
        kelvin_common=max(kelvin_common,relerr(Gamma,Gammac))

        O1=orthogonal(rng); O2=orthogonal(rng)
        Sigmap=np.vstack((S1@O1,S2@O2)); Gammap=2*nu*Sigmap@Sigmap.T
        kelvin_diag=max(kelvin_diag,
                        relerr(Gamma[:3,:3],Gammap[:3,:3]),
                        relerr(Gamma[3:,3:],Gammap[3:,3:]))
        kelvin_cross_signal=max(kelvin_cross_signal,
                                np.linalg.norm(Gamma[:3,3:]-Gammap[:3,3:]))
        kelvin_synth_signal=max(kelvin_synth_signal,
                                np.linalg.norm(Asum@Gamma@Asum.T-Asum@Gammap@Asum.T))

    # Two-germ Gram witness S,S versus S,-S.
    S=np.array([[1.,.2,0.],[-.3,.7,.1],[.4,0.,.9]])
    Sigplus=np.vstack((S,S)); Sigminus=np.vstack((S,-S))
    Kplus=2*nu*Sigplus@Sigplus.T; Kminus=2*nu*Sigminus@Sigminus.T
    kelvin_witness_diag=max(relerr(Kplus[:3,:3],Kminus[:3,:3]),
                            relerr(Kplus[3:,3:],Kminus[3:,3:]))
    kelvin_plus=Asum@Kplus@Asum.T
    kelvin_minus=Asum@Kminus@Asum.T
    kelvin_witness_zero=np.linalg.norm(kelvin_minus)
    kelvin_witness_signal=np.linalg.norm(kelvin_plus)

    # Exact one-mode NSE/Kelvin negative-coupling activation.
    nu_ns=.23; t=.51; k=1.4
    E=np.exp(-nu_ns*k*k*t); rho=np.pi/(2*k)
    Y1=np.pi/(2*k); Y2=3*np.pi/(2*k)
    def Uy(Y): return -E*k*np.sin(k*Y)
    def Uyy(Y): return -E*k*k*np.cos(k*Y)
    def q(Y): return (Uy(Y)-Uy(Y+rho)+rho*Uyy(Y))/(rho*rho)
    q1=q(Y1); q2=q(Y2)
    S1=np.zeros((3,3)); S2=np.zeros((3,3)); S1[2,1]=q1; S2[2,1]=q2
    Sig=np.vstack((S1,S2)); G=2*nu_ns*Sig@Sig.T
    ns_diag=relerr(G[:3,:3],G[3:,3:])
    ns_cross=relerr(G[:3,3:],-G[:3,:3])
    ns_cancel=np.linalg.norm(Asum@G@Asum.T)/(1+np.linalg.norm(G))
    ns_signal=np.linalg.norm(G[:3,:3])

    pde=0.0
    for y in np.linspace(-np.pi,np.pi,2001):
        U=E*np.cos(k*y); Ut=-nu_ns*k*k*U; Uyyv=-k*k*U
        pde=max(pde,abs(Ut-nu_ns*Uyyv)/(1+abs(Ut)+abs(nu_ns*Uyyv)))

    print(f"Wang common-phase full-pair residual: {wang_common:.3e}")
    print(f"Wang independent-phase diagonal residual: {wang_diag:.3e}")
    print(f"Wang sampled relative-phase cross signal: {wang_cross_signal:.3e}")
    print(f"Wang sampled synthesis sensitivity signal: {wang_synth_signal:.3e}")
    print(f"Wang two-child witness diagonal residual: {wang_witness_diag:.3e}")
    print(f"Wang destructive-synthesis residual: {wang_witness_zero:.3e}")
    print(f"Wang constructive-synthesis signal: {wang_witness_signal:.3e}")
    print(f"Kelvin common-O3 full-Gram residual: {kelvin_common:.3e}")
    print(f"Kelvin independent-O3 diagonal residual: {kelvin_diag:.3e}")
    print(f"Kelvin sampled relative-orientation cross signal: {kelvin_cross_signal:.3e}")
    print(f"Kelvin sampled synthesis sensitivity signal: {kelvin_synth_signal:.3e}")
    print(f"Kelvin two-germ witness diagonal residual: {kelvin_witness_diag:.3e}")
    print(f"Kelvin destructive-synthesis residual: {kelvin_witness_zero:.3e}")
    print(f"Kelvin constructive-synthesis signal: {kelvin_witness_signal:.3e}")
    print(f"exact NSE equal-diagonal qv residual: {ns_diag:.3e}")
    print(f"exact NSE negative-cross qv residual: {ns_cross:.3e}")
    print(f"exact NSE synthesized cancellation residual: {ns_cancel:.3e}")
    print(f"exact NSE nonzero diagonal qv signal: {ns_signal:.3e}")
    print(f"worst exact periodic NSE residual: {pde:.3e}")

    assert wang_common < 3e-14
    assert wang_diag < 3e-14
    assert wang_cross_signal > 1e-3
    assert wang_synth_signal > 1e-3
    assert wang_witness_diag < 2e-14
    assert wang_witness_zero < 2e-14
    assert wang_witness_signal > 1e-3
    assert kelvin_common < 3e-13
    assert kelvin_diag < 3e-13
    assert kelvin_cross_signal > 1e-3
    assert kelvin_synth_signal > 1e-3
    assert kelvin_witness_diag < 2e-14
    assert kelvin_witness_zero < 2e-14
    assert kelvin_witness_signal > 1e-3
    assert ns_diag < 3e-13
    assert ns_cross < 3e-13
    assert ns_cancel < 3e-13
    assert ns_signal > 1e-5
    assert pde < 2e-14
    print("PASS: diagonal marginals erase the relative coupling required by coherent/common-driver synthesis")


if __name__ == "__main__":
    main()
