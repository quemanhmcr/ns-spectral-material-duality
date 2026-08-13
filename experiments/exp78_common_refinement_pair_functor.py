"""Action-only referee for common linear-refinement tensor-square law."""
import numpy as np
from exp58_resolved_cartan_material_metric import waves, random_divfree, inner
from exp61_moving_cutoff_metric_acceleration import symbol_apply


def main():
    rng=np.random.default_rng(78082026)
    pair=energy=reset=overlap=orth=0.0
    cross_signal=reset_signal=0.0

    # Universal finite-dimensional pair functor / Kelvin reset algebra.
    for _ in range(30000):
        n=6; m=4
        Y=[rng.normal(size=n) for _ in range(m)]
        y=sum(Y,start=np.zeros(n))
        lhs=np.outer(y,y)
        rhs=sum((np.outer(a,b) for a in Y for b in Y),start=np.zeros((n,n)))
        pair=max(pair,np.linalg.norm(lhs-rhs)/(1+np.linalg.norm(lhs)+np.linalg.norm(rhs)))
        e=float(y@y)
        er=sum(float(a@a) for a in Y)+2*sum(float(Y[i]@Y[j]) for i in range(m) for j in range(i+1,m))
        energy=max(energy,abs(e-er)/(1+abs(e)+abs(er)))

        d=5; qdim=12
        X=rng.normal(size=(qdim,qdim)); Q=X@X.T
        A0=rng.normal(size=(d,qdim)); dA=rng.normal(size=(d,qdim))
        A1=A0+dA
        lhs=A1@Q@A1.T-A0@Q@A0.T
        rhs=dA@Q@A0.T+A0@Q@dA.T+dA@Q@dA.T
        reset=max(reset,np.linalg.norm(lhs-rhs)/(1+np.linalg.norm(lhs)+np.linalg.norm(rhs)))
        reset_signal=max(reset_signal,np.linalg.norm(dA@Q@dA.T))

    # Actual divergence-free Fourier state with overlapping smooth resolution partition.
    n=12; ks=waves(n); k2=sum(k*k for k in ks)
    for _ in range(30):
        u=random_divfree(rng,n,ks,3.0)
        alpha=float(rng.uniform(.02,.08))
        R1=np.exp(-alpha*k2); R2=1.0-R1
        u1=symbol_apply(u,R1); u2=symbol_apply(u,R2)
        rec=np.linalg.norm(u-u1-u2)/(1+np.linalg.norm(u))
        c=inner(u1,u2)
        lhs=inner(u,u)
        rhs=inner(u1,u1)+inner(u2,u2)+2*c
        overlap=max(overlap,rec,abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))
        cross_signal=max(cross_signal,abs(c))

        # Hard disjoint Fourier masks are orthogonal and kill cross energy exactly.
        mask1=(k2<=4.0).astype(float); mask2=(k2>4.0).astype(float)
        h1=symbol_apply(u,mask1); h2=symbol_apply(u,mask2)
        orth=max(orth,abs(inner(h1,h2))/(1+np.sqrt(inner(h1,h1)*inner(h2,h2))))

    print(f"worst deterministic pair-functor residual: {pair:.3e}")
    print(f"worst quadratic-energy cross-term residual: {energy:.3e}")
    print(f"worst Kelvin finite tensor-square reset residual: {reset:.3e}")
    print(f"worst overlapping smooth-refinement reconstruction/energy residual: {overlap:.3e}")
    print(f"worst hard-disjoint orthogonality residual: {orth:.3e}")
    print(f"maximum smooth cross-pair / reset-quadratic signals: {cross_signal:.3e} {reset_signal:.3e}")
    assert pair<4e-13
    assert energy<4e-13
    assert reset<4e-12
    assert overlap<3e-12
    assert orth<3e-12
    assert cross_signal>1e-5
    assert reset_signal>1e-3
    print("PASS: Wang-style linear refinement and Kelvin residual synthesis share the exact tensor-square pair functor")


if __name__=='__main__': main()
