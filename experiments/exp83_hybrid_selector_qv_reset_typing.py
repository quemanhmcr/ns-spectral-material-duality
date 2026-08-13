"""Action-only referee for hybrid selector q.v./reset physical typing."""
import numpy as np


def relerr(a,b):
    return np.linalg.norm(a-b)/(1.0+np.linalg.norm(a)+np.linalg.norm(b))


def main():
    rng=np.random.default_rng(83082026)
    I=np.eye(3); Z=np.zeros((3,3))
    E0=np.hstack((I,Z)); E1=np.hstack((Z,I))

    continuous=dyad=closed_state=closed_pair=combined=split1=split2=cross_recon=0.0
    closed_qv_signal=linear_face_signal=split_cross_signal=0.0

    for _ in range(600):
        nu=.05+rng.random()
        S0=rng.normal(size=(3,3)); S1=rng.normal(size=(3,3))
        Sigma=np.vstack((S0,S1)); Gamma=2*nu*Sigma@Sigma.T
        continuous=max(continuous,relerr(E0@Gamma@E0.T,2*nu*S0@S0.T),
                       relerr(E1@Gamma@E1.T,2*nu*S1@S1.T))

        X=rng.normal(size=6)
        Y0=E0@X; Y1=E1@X; J=Y1-Y0
        lhs=np.outer(Y1,Y1)-np.outer(Y0,Y0)
        left=np.outer(J,Y0); right=np.outer(Y0,J); quad=np.outer(J,J)
        dyad=max(dyad,relerr(lhs,left+right+quad))
        linear_face_signal=max(linear_face_signal,np.linalg.norm(left+right))

        # Closed readout excursion on a frozen library.
        J01=J; J10=-J
        Yfinal=Y0+J01+J10
        closed_state=max(closed_state,np.linalg.norm(Yfinal-Y0))
        closed_pair=max(closed_pair,relerr(np.outer(Yfinal,Yfinal),np.outer(Y0,Y0)))
        qv=np.outer(J01,J01)+np.outer(J10,J10)
        closed_qv_signal=max(closed_qv_signal,np.trace(qv))

        # Simultaneous physical event and selector: only E1 A is the literal post map.
        A=np.eye(6)+.3*rng.normal(size=(6,6))
        total=E1@A@X-E0@X
        jsel_pre=(E1-E0)@X
        jevent_post=E1@(A-np.eye(6))@X
        jevent_old=E0@(A-np.eye(6))@X
        jsel_post=(E1-E0)@A@X
        split1=max(split1,relerr(total,jsel_pre+jevent_post))
        split2=max(split2,relerr(total,jevent_old+jsel_post))
        combined=max(combined,relerr(E1@A@X,E0@X+total))

        total_sq=np.outer(total,total)
        square_sum=np.outer(jsel_pre,jsel_pre)+np.outer(jevent_post,jevent_post)
        cross=np.outer(jsel_pre,jevent_post)+np.outer(jevent_post,jsel_pre)
        cross_recon=max(cross_recon,relerr(total_sq,square_sum+cross))
        split_cross_signal=max(split_cross_signal,np.linalg.norm(cross))

    # Exact periodic NSE half-period codeforming sign-flip calibration.
    nu=.31; t=.47; k=1.6
    E=np.exp(-nu*k*k*t); rho=np.pi/(2*k)
    def U(Y): return E*np.cos(k*Y)
    def Uy(Y): return -E*k*np.sin(k*Y)
    def chi(Y): return (U(Y)-U(Y+rho)+rho*Uy(Y))/(rho*rho)
    chi0=chi(0.0)
    chi1=chi(np.pi/k)
    chi_formula=4*E*k*k/np.pi**2
    chi_resid=max(abs(chi0-chi_formula)/(1+abs(chi0)+abs(chi_formula)),
                  abs(chi1+chi_formula)/(1+abs(chi1)+abs(chi_formula)))
    chi_opposite=abs(chi0+chi1)/(1+abs(chi0)+abs(chi1))

    ez=np.array([0.,0.,1.]); Y0=chi0*ez; Y1=chi1*ez; J=Y1-Y0
    jump_qv=np.outer(J,J)
    pair_jump=np.outer(Y1,Y1)-np.outer(Y0,Y0)
    left=np.outer(J,Y0); right=np.outer(Y0,J)
    ns_pair=relerr(pair_jump,np.zeros((3,3)))
    ns_face=relerr(left+right+jump_qv,np.zeros((3,3)))
    ns_jump_signal=np.trace(jump_qv)
    ns_jump_expected=4*chi0*chi0
    ns_jump_formula=abs(ns_jump_signal-ns_jump_expected)/(1+abs(ns_jump_signal)+abs(ns_jump_expected))

    excursion_qv=2*jump_qv
    excursion_trace=np.trace(excursion_qv)
    excursion_expected=8*chi0*chi0
    ns_excursion=abs(excursion_trace-excursion_expected)/(1+abs(excursion_trace)+abs(excursion_expected))
    ns_excursion_formula=128*E*E*k**4/np.pi**4
    ns_excursion_closed=abs(excursion_trace-ns_excursion_formula)/(1+abs(excursion_trace)+abs(ns_excursion_formula))

    pde=0.0
    for y in np.linspace(-np.pi,np.pi,2001):
        U=E*np.cos(k*y); Ut=-nu*k*k*U; Uyy=-k*k*U
        pde=max(pde,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))

    print(f"frozen-selector continuous-qv selection residual: {continuous:.3e}")
    print(f"selector endpoint-dyad face residual: {dyad:.3e}")
    print(f"maximum sampled signed linear-face signal: {linear_face_signal:.3e}")
    print(f"closed selector net-state residual: {closed_state:.3e}")
    print(f"closed selector endpoint-pair residual: {closed_pair:.3e}")
    print(f"closed selector jump-qv signal: {closed_qv_signal:.3e}")
    print(f"combined physical-event/selector map residual: {combined:.3e}")
    print(f"prestate-selector decomposition residual: {split1:.3e}")
    print(f"poststate-selector decomposition residual: {split2:.3e}")
    print(f"jump-square cross-face reconstruction residual: {cross_recon:.3e}")
    print(f"maximum sampled event/selector cross-face signal: {split_cross_signal:.3e}")
    print(f"exact NSE half-period residual-amplitude residual: {chi_resid:.3e}")
    print(f"exact NSE half-period opposite-residual: {chi_opposite:.3e}")
    print(f"exact NSE single-switch pair-revaluation residual: {ns_pair:.3e}")
    print(f"exact NSE single-switch signed-face cancellation residual: {ns_face:.3e}")
    print(f"exact NSE single-switch positive jump-qv signal: {ns_jump_signal:.3e}")
    print(f"exact NSE single-switch jump-qv formula residual: {ns_jump_formula:.3e}")
    print(f"exact NSE closed-excursion qv residual: {ns_excursion:.3e}")
    print(f"exact NSE closed-excursion analytic-trace residual: {ns_excursion_closed:.3e}")
    print(f"worst exact periodic NSE residual: {pde:.3e}")

    assert continuous < 3e-13
    assert dyad < 3e-13
    assert linear_face_signal > 1e-3
    assert closed_state < 1e-14
    assert closed_pair < 1e-14
    assert closed_qv_signal > 1e-3
    assert combined < 3e-13
    assert split1 < 3e-13
    assert split2 < 3e-13
    assert cross_recon < 3e-13
    assert split_cross_signal > 1e-3
    assert chi_resid < 2e-14
    assert chi_opposite < 2e-14
    assert ns_pair < 2e-14
    assert ns_face < 2e-14
    assert ns_jump_signal > 1e-5
    assert ns_jump_formula < 2e-14
    assert ns_excursion < 2e-14
    assert ns_excursion_closed < 2e-14
    assert pde < 2e-14
    print("PASS: continuous qv, selector jump variation, pair reset, and physical event composition remain correctly typed")


if __name__ == "__main__":
    main()
