"""Action-only referee for selector jump-q.v. history/coboundary no-go."""
import numpy as np


def relerr(a,b):
    return np.linalg.norm(a-b)/(1.0+np.linalg.norm(a)+np.linalg.norm(b))


def jump_qv(path):
    d=path[0].shape[0]
    out=np.zeros((d,d))
    for a,b in zip(path,path[1:]):
        j=b-a
        out += np.outer(j,j)
    return out


def pair_revaluation_sum(path):
    d=path[0].shape[0]
    out=np.zeros((d,d))
    for a,b in zip(path,path[1:]):
        out += np.outer(b,b)-np.outer(a,a)
    return out


def main():
    rng=np.random.default_rng(84082026)
    pair_tel=loop_pair=loop_formula=endpoint_match=0.0
    loop_signal=trace_coboundary_signal=state_nonclosure_signal=0.0

    for _ in range(800):
        a=rng.normal(size=3)
        b=rng.normal(size=3)
        c=rng.normal(size=3)

        path=[a,b,c]
        pair_tel=max(pair_tel,
                     relerr(pair_revaluation_sum(path),np.outer(c,c)-np.outer(a,a)))

        loop=[a,b,a]
        qloop=jump_qv(loop)
        target=2*np.outer(b-a,b-a)
        loop_formula=max(loop_formula,relerr(qloop,target))
        loop_pair=max(loop_pair,np.linalg.norm(pair_revaluation_sum(loop)))
        loop_signal=max(loop_signal,np.linalg.norm(qloop))
        trace_coboundary_signal=max(trace_coboundary_signal,np.trace(qloop))

        # Same instantaneous endpoint state/library readout, different selector histories.
        stationary=[a,a,a]
        q0=jump_qv(stationary)
        q1=jump_qv(loop)
        endpoint_match=max(endpoint_match,np.linalg.norm(stationary[-1]-loop[-1]))
        state_nonclosure_signal=max(state_nonclosure_signal,np.linalg.norm(q1-q0))

    # Exact periodic NSE half-period residual library from the codeforming formula.
    nu=.27; t=.58; k=1.5
    E=np.exp(-nu*k*k*t); rho=np.pi/(2*k)
    def U(Y): return E*np.cos(k*Y)
    def Uy(Y): return -E*k*np.sin(k*Y)
    def Uyy(Y): return -E*k*k*np.cos(k*Y)
    def chi(Y): return (U(Y)-U(Y+rho)+rho*Uy(Y))/(rho*rho)
    def qnoise(Y): return (Uy(Y)-Uy(Y+rho)+rho*Uyy(Y))/(rho*rho)

    chi0=chi(0.0); chi1=chi(np.pi/k)
    chi_target=4*E*k*k/np.pi**2
    chi_exact=max(abs(chi0-chi_target)/(1+abs(chi0)+abs(chi_target)),
                  abs(chi1+chi_target)/(1+abs(chi1)+abs(chi_target)))
    opposite=abs(chi0+chi1)/(1+abs(chi0)+abs(chi1))

    ez=np.array([0.,0.,1.])
    a=chi0*ez; b=chi1*ez
    stationary=[a,a,a]
    excursion=[a,b,a]
    q_stationary=jump_qv(stationary)
    q_excursion=jump_qv(excursion)
    pair_excursion=pair_revaluation_sum(excursion)
    ns_endpoint=np.linalg.norm(stationary[-1]-excursion[-1])
    ns_pair=np.linalg.norm(pair_excursion)
    ns_stationary=np.linalg.norm(q_stationary)
    ns_signal=np.trace(q_excursion)
    ns_expected=8*chi0*chi0
    ns_formula=abs(ns_signal-ns_expected)/(1+abs(ns_signal)+abs(ns_expected))
    analytic=128*E*E*k**4/np.pi**4
    ns_analytic=abs(ns_signal-analytic)/(1+abs(ns_signal)+abs(analytic))

    # Exact half-period noise responses are opposite, hence their diagonal source rates agree;
    # after the closed loop the active selector is again 0, so the current source rate is identical.
    q0=qnoise(0.0); q1=qnoise(np.pi/k)
    noise_opposite=abs(q0+q1)/(1+abs(q0)+abs(q1))
    S0=np.zeros((3,3)); S1=np.zeros((3,3)); S0[2,1]=q0; S1[2,1]=q1
    Gamma0=2*nu*S0@S0.T; Gamma1=2*nu*S1@S1.T
    ns_readout_rate_equal=relerr(Gamma0,Gamma1)
    ns_current_rate=relerr(Gamma0,Gamma0)

    pde=0.0
    for y in np.linspace(-np.pi,np.pi,2001):
        Uy0=E*np.cos(k*y)
        Ut=-nu*k*k*Uy0
        Uyy=-k*k*Uy0
        pde=max(pde,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))

    print(f"pair-revaluation telescoping residual: {pair_tel:.3e}")
    print(f"closed-loop pair-revaluation residual: {loop_pair:.3e}")
    print(f"closed-loop jump-qv formula residual: {loop_formula:.3e}")
    print(f"maximum sampled positive loop-qv signal: {loop_signal:.3e}")
    print(f"maximum sampled trace coboundary-obstruction signal: {trace_coboundary_signal:.3e}")
    print(f"same-endpoint selector-history residual: {endpoint_match:.3e}")
    print(f"same-endpoint accumulated-qv nonclosure signal: {state_nonclosure_signal:.3e}")
    print(f"exact NSE residual-amplitude residual: {chi_exact:.3e}")
    print(f"exact NSE opposite-readout residual: {opposite:.3e}")
    print(f"exact NSE same-endpoint history residual: {ns_endpoint:.3e}")
    print(f"exact NSE closed-loop pair residual: {ns_pair:.3e}")
    print(f"exact NSE stationary-history jump-qv residual: {ns_stationary:.3e}")
    print(f"exact NSE loop jump-qv trace signal: {ns_signal:.3e}")
    print(f"exact NSE loop jump-qv chi formula residual: {ns_formula:.3e}")
    print(f"exact NSE loop jump-qv analytic residual: {ns_analytic:.3e}")
    print(f"exact NSE half-period opposite-noise residual: {noise_opposite:.3e}")
    print(f"exact NSE equal readout source-rate residual: {ns_readout_rate_equal:.3e}")
    print(f"exact NSE same-current-source-rate residual: {ns_current_rate:.3e}")
    print(f"worst exact periodic NSE residual: {pde:.3e}")

    assert pair_tel < 3e-13
    assert loop_pair < 2e-14
    assert loop_formula < 3e-13
    assert loop_signal > 1e-3
    assert trace_coboundary_signal > 1e-3
    assert endpoint_match < 2e-14
    assert state_nonclosure_signal > 1e-3
    assert chi_exact < 2e-14
    assert opposite < 2e-14
    assert ns_endpoint < 2e-14
    assert ns_pair < 2e-14
    assert ns_stationary < 2e-14
    assert ns_signal > 1e-5
    assert ns_formula < 2e-14
    assert ns_analytic < 2e-14
    assert noise_opposite < 2e-14
    assert ns_readout_rate_equal < 3e-13
    assert ns_current_rate < 2e-14
    assert pde < 2e-14
    print("PASS: selector jump qv has nonzero loop circulation and requires path/history data")


if __name__ == "__main__":
    main()
