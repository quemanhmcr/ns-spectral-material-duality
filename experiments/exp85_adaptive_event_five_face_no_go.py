"""Action-only referee for the general adaptive-event five-face identity."""
import numpy as np


def relerr(a,b):
    return np.linalg.norm(a-b)/(1.0+np.linalg.norm(a)+np.linalg.norm(b))


def mean(xs):
    return sum(xs)/len(xs)


def main():
    rng=np.random.default_rng(85082026)
    first_order=second_order=two_replica=cubic_parity=disp_psd=0.0
    cubic_signal=four_face_failure=0.0

    # General finite-ensemble exact identities with PSD payloads.
    for _ in range(500):
        nrep=5; m=3; n=4
        Cs=[rng.normal(size=(m,n)) for _ in range(nrep)]
        xs=[rng.normal(size=n) for _ in range(nrep)]
        Rs=[rng.normal(size=(n,n)) for _ in range(nrep)]
        Qs=[R@R.T for R in Rs]

        Cbar=mean(Cs); xbar=mean(xs); Qbar=mean(Qs)
        dCs=[C-Cbar for C in Cs]
        dxs=[x-xbar for x in xs]
        dQs=[Q-Qbar for Q in Qs]

        lhs1=mean([C@x for C,x in zip(Cs,xs)])
        rhs1=Cbar@xbar+mean([dC@dx for dC,dx in zip(dCs,dxs)])
        first_order=max(first_order,relerr(lhs1,rhs1))

        lhs2=mean([C@Q@C.T for C,Q in zip(Cs,Qs)])
        meanface=Cbar@Qbar@Cbar.T
        disp=mean([dC@Qbar@dC.T for dC in dCs])
        left=Cbar@mean([dQ@dC.T for dQ,dC in zip(dQs,dCs)])
        right=mean([dC@dQ for dC,dQ in zip(dCs,dQs)])@Cbar.T
        cubic=mean([dC@dQ@dC.T for dC,dQ in zip(dCs,dQs)])
        rhs2=meanface+disp+left+right+cubic
        second_order=max(second_order,relerr(lhs2,rhs2))
        cubic_signal=max(cubic_signal,np.linalg.norm(cubic))
        eig=np.linalg.eigvalsh((disp+disp.T)/2)
        disp_psd=max(disp_psd,max(0.0,-float(np.min(eig))))

    # Exact equal-weight two-replica specialization: cubic odd face cancels.
    for _ in range(500):
        m=3; n=4
        C1=rng.normal(size=(m,n)); C2=rng.normal(size=(m,n))
        R1=rng.normal(size=(n,n)); R2=rng.normal(size=(n,n))
        Q1=R1@R1.T; Q2=R2@R2.T
        Cbar=(C1+C2)/2; Qbar=(Q1+Q2)/2
        dC=(C1-C2)/2; dQ=(Q1-Q2)/2
        cubic=(dC@dQ@dC.T + (-dC)@(-dQ)@(-dC).T)/2
        cubic_parity=max(cubic_parity,np.linalg.norm(cubic))

        lhs=(C1@Q1@C1.T+C2@Q2@C2.T)/2
        DC=C1-C2; DQ=Q1-Q2
        rhs=(Cbar@Qbar@Cbar.T
             +.25*DC@Qbar@DC.T
             +.25*Cbar@DQ@DC.T
             +.25*DC@DQ@Cbar.T)
        two_replica=max(two_replica,relerr(lhs,rhs))

    # Irreducible scalar three-replica PSD witnesses.
    C=np.array([0.,1.,2.])
    Qplus=np.array([4.,1.,4.])
    Qminus=np.array([2.,5.,2.])
    Cbar=float(np.mean(C)); dC=C-Cbar

    def faces(Q):
        Qbar=float(np.mean(Q)); dQ=Q-Qbar
        meanface=Cbar*Cbar*Qbar
        disp=float(np.mean(dC*dC))*Qbar
        corr=float(np.mean(dC*dQ))
        left=Cbar*corr; right=corr*Cbar
        cubic=float(np.mean(dC*dQ*dC))
        actual=float(np.mean(C*C*Q))
        return meanface,disp,left,right,cubic,actual

    fp=faces(Qplus); fm=faces(Qminus)
    expected_common=np.array([3.,2.,0.,0.])
    common_res=max(relerr(np.array(fp[:4]),expected_common),
                   relerr(np.array(fm[:4]),expected_common))
    cubic_exact=max(abs(fp[4]-2/3)/(1+abs(fp[4])+2/3),
                    abs(fm[4]+2/3)/(1+abs(fm[4])+2/3))
    actual_exact=max(abs(fp[5]-17/3)/(1+abs(fp[5])+17/3),
                     abs(fm[5]-13/3)/(1+abs(fm[5])+13/3))
    truncated_plus=sum(fp[:4]); truncated_minus=sum(fm[:4])
    four_face_failure=max(abs(fp[5]-truncated_plus),abs(fm[5]-truncated_minus))
    witness_gap=abs(fp[5]-fm[5])

    print(f"general adaptive first-moment identity residual: {first_order:.3e}")
    print(f"general adaptive five-face identity residual: {second_order:.3e}")
    print(f"event-dispersion PSD violation: {disp_psd:.3e}")
    print(f"maximum sampled cubic mixed-face signal: {cubic_signal:.3e}")
    print(f"two-replica four-face specialization residual: {two_replica:.3e}")
    print(f"two-replica cubic parity residual: {cubic_parity:.3e}")
    print(f"three-replica common-four-face residual: {common_res:.3e}")
    print(f"three-replica cubic +/-2/3 residual: {cubic_exact:.3e}")
    print(f"three-replica exact-output residual: {actual_exact:.3e}")
    print(f"four-face truncation failure signal: {four_face_failure:.3e}")
    print(f"same-four-faces opposite-cubic output gap: {witness_gap:.3e}")

    assert first_order < 3e-13
    assert second_order < 5e-13
    assert disp_psd < 3e-12
    assert cubic_signal > 1e-3
    assert two_replica < 5e-13
    assert cubic_parity < 3e-13
    assert common_res < 2e-14
    assert cubic_exact < 2e-14
    assert actual_exact < 2e-14
    assert four_face_failure > .5
    assert witness_gap > 1.0
    print("PASS: general adaptive quadratic synthesis has an irreducible fifth mixed correlation face")


if __name__ == "__main__":
    main()
