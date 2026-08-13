"""Action-only referee for stock-vs-path memory and simultaneous-owner no-go."""
import numpy as np


def relerr(a,b):
    return np.linalg.norm(a-b)/(1.0+np.linalg.norm(a)+np.linalg.norm(b))


def jump_qv(path):
    d=path[0].shape[0]
    out=np.zeros((d,d))
    for x,y in zip(path,path[1:]):
        j=y-x
        out += np.outer(j,j)
    return out


def main():
    rng=np.random.default_rng(86082026)
    endpoint_stock=endpoint_pair=loop_formula=stationary=0.0
    loop_signal=hidden_owner_signal=mixed_face_signal=naive_event_failure=0.0

    # Generic endpoint-stock/path-variation obstruction.
    for _ in range(700):
        a=rng.normal(size=3)
        b=rng.normal(size=3)
        loop=[a,b,a]
        still=[a,a,a]
        qloop=jump_qv(loop)
        qstill=jump_qv(still)
        target=2*np.outer(b-a,b-a)
        loop_formula=max(loop_formula,relerr(qloop,target))
        stationary=max(stationary,np.linalg.norm(qstill))
        endpoint_stock=max(endpoint_stock,abs(np.dot(loop[-1],loop[-1])-np.dot(still[-1],still[-1])))
        endpoint_pair=max(endpoint_pair,relerr(np.outer(loop[-1],loop[-1]),np.outer(still[-1],still[-1])))
        loop_signal=max(loop_signal,np.trace(qloop))

        # Component quotient: same stock component does not determine hidden owners.
        S=float(rng.normal())
        Rminus=rng.normal(size=4); Rplus=rng.normal(size=4)
        zminus=np.concatenate(([S],Rminus)); zplus=np.concatenate(([S],Rplus))
        assert zminus[0] == zplus[0]
        hidden_owner_signal=max(hidden_owner_signal,np.linalg.norm(zplus-zminus))

        # Simultaneous physical event + selector: mixed DeltaE DeltaA is mandatory.
        I=np.eye(3); Z=np.zeros((3,3))
        E0=np.hstack((I,Z)); E1=np.hstack((Z,I)); dE=E1-E0
        A=np.eye(6)+.25*rng.normal(size=(6,6)); dA=A-np.eye(6)
        D=E1@A-E0
        exact=E0@dA+dE+dE@dA
        mixed_face_signal=max(mixed_face_signal,np.linalg.norm(dE@dA))
        naive=E0@dA+dE
        naive_event_failure=max(naive_event_failure,np.linalg.norm(D-naive))
        assert relerr(D,exact) < 2e-13

    # Exact periodic NSE/Kelvin half-period residual loop.
    nu=.24; t=.49; k=1.7
    E=np.exp(-nu*k*k*t); rho=np.pi/(2*k)
    def U(Y): return E*np.cos(k*Y)
    def Uy(Y): return -E*k*np.sin(k*Y)
    def chi(Y): return (U(Y)-U(Y+rho)+rho*Uy(Y))/(rho*rho)
    chi0=chi(0.0); chi1=chi(np.pi/k)
    target_chi=4*E*k*k/np.pi**2
    chi_exact=max(abs(chi0-target_chi)/(1+abs(chi0)+abs(target_chi)),
                  abs(chi1+target_chi)/(1+abs(chi1)+abs(target_chi)))
    opposite=abs(chi0+chi1)/(1+abs(chi0)+abs(chi1))

    ez=np.array([0.,0.,1.]); a=chi0*ez; b=chi1*ez
    still=[a,a,a]; loop=[a,b,a]
    q0=jump_qv(still); q1=jump_qv(loop)
    ns_endpoint=relerr(np.outer(still[-1],still[-1]),np.outer(loop[-1],loop[-1]))
    ns_stationary=np.linalg.norm(q0)
    ns_signal=np.trace(q1)
    ns_expected=8*chi0*chi0
    ns_formula=abs(ns_signal-ns_expected)/(1+abs(ns_signal)+abs(ns_expected))
    analytic=128*E*E*k**4/np.pi**4
    ns_analytic=abs(ns_signal-analytic)/(1+abs(ns_signal)+abs(analytic))

    pde=0.0
    for y in np.linspace(-np.pi,np.pi,2001):
        val=E*np.cos(k*y); Ut=-nu*k*k*val; Uyy=-k*k*val
        pde=max(pde,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))

    print(f"generic closed-loop jump-qv formula residual: {loop_formula:.3e}")
    print(f"generic stationary jump-qv residual: {stationary:.3e}")
    print(f"same-endpoint scalar-stock residual: {endpoint_stock:.3e}")
    print(f"same-endpoint pair-stock residual: {endpoint_pair:.3e}")
    print(f"maximum sampled positive path-variation signal: {loop_signal:.3e}")
    print(f"same-stock hidden-owner separation signal: {hidden_owner_signal:.3e}")
    print(f"simultaneous event mixed-face signal: {mixed_face_signal:.3e}")
    print(f"naive selector-plus-event omission signal: {naive_event_failure:.3e}")
    print(f"exact NSE half-period residual-amplitude residual: {chi_exact:.3e}")
    print(f"exact NSE opposite-readout residual: {opposite:.3e}")
    print(f"exact NSE same-endpoint pair-stock residual: {ns_endpoint:.3e}")
    print(f"exact NSE stationary-history jump-qv residual: {ns_stationary:.3e}")
    print(f"exact NSE loop jump-qv trace signal: {ns_signal:.3e}")
    print(f"exact NSE loop chi-formula residual: {ns_formula:.3e}")
    print(f"exact NSE loop analytic-trace residual: {ns_analytic:.3e}")
    print(f"worst exact periodic NSE residual: {pde:.3e}")

    assert loop_formula < 3e-13
    assert stationary < 2e-14
    assert endpoint_stock < 2e-14
    assert endpoint_pair < 2e-14
    assert loop_signal > 1e-3
    assert hidden_owner_signal > 1e-3
    assert mixed_face_signal > 1e-3
    assert naive_event_failure > 1e-3
    assert chi_exact < 2e-14
    assert opposite < 2e-14
    assert ns_endpoint < 2e-14
    assert ns_stationary < 2e-14
    assert ns_signal > 1e-5
    assert ns_formula < 2e-14
    assert ns_analytic < 2e-14
    assert pde < 2e-14
    print("PASS: inherited stock, selector path variation, and simultaneous owners remain distinct")


if __name__ == "__main__":
    main()
