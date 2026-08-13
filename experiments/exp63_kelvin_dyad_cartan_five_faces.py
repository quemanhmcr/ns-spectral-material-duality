"""Action-only full-state referee for Kelvin dyad Cartan five-face decomposition."""
import numpy as np
from exp58_resolved_cartan_material_metric import waves, random_divfree, grad
from exp61_moving_cutoff_metric_acceleration import symbol_apply, sym_skew


def comm(R,O):
    return R@O-O@R


def anti(S,R):
    return S@R+R@S


def relmat(a,b):
    return np.linalg.norm(a-b)/(1+np.linalg.norm(a)+np.linalg.norm(b))


def main():
    rng=np.random.default_rng(63082026)
    n=10; ks=waves(n); k2=sum(k*k for k in ks)
    base=split=symmetry=trace_conn=power2=power3=energy=0.0
    strain_signal=conn_signal=qv_signal=0.0
    for _ in range(40):
        u=random_divfree(rng,n,ks,2.0)
        alpha=float(rng.uniform(.02,.08))
        Rcut=np.exp(-alpha*k2)
        V=symbol_apply(u,Rcut); h=u-V
        Au=grad(u,ks); Av=grad(V,ks); Ah=grad(h,ks)
        Su,Ou=sym_skew(Au); Sv,Ov=sym_skew(Av); Sh,Oh=sym_skew(Ah)

        for idx in [(1,2,3),(4,5,1),(7,3,6),(2,8,4)]:
            A=Au[idx]; S=Su[idx]; O=Ou[idx]
            Sv0=Sv[idx]; Sh0=Sh[idx]; Ov0=Ov[idx]; Oh0=Oh[idx]
            X=rng.normal(size=(3,3)); Rd=X@X.T
            Q=rng.normal(size=(3,3)); Gamma=Q@Q.T

            lhs=-A@Rd-Rd@A.T+Gamma
            rhs=-anti(S,Rd)+comm(Rd,O)+Gamma
            base=max(base,relmat(lhs,rhs))

            rhs5=-anti(Sv0,Rd)-anti(Sh0,Rd)+comm(Rd,Ov0)+comm(Rd,Oh0)+Gamma
            split=max(split,relmat(lhs,rhs5))
            symmetry=max(symmetry,np.linalg.norm(lhs-lhs.T)/(1+np.linalg.norm(lhs)))

            Dconn=comm(Rd,O)
            trace_conn=max(trace_conn,abs(np.trace(Dconn))/(1+np.linalg.norm(Dconn)))
            power2=max(power2,abs(2*np.trace(Rd@Dconn))/(1+np.linalg.norm(Rd)**2+np.linalg.norm(Dconn)))
            power3=max(power3,abs(3*np.trace(Rd@Rd@Dconn))/(1+np.linalg.norm(Rd)**3+np.linalg.norm(Dconn)))

            r=rng.normal(size=3); Rr=np.outer(r,r)
            D=-anti(S,Rr)+comm(Rr,O)+Gamma
            lhsE=.5*float(np.trace(D))
            rhsE=-float(r@S@r)+.5*float(np.trace(Gamma))
            energy=max(energy,abs(lhsE-rhsE)/(1+abs(lhsE)+abs(rhsE)))

            strain_signal=max(strain_signal,np.linalg.norm(anti(S,Rd)))
            conn_signal=max(conn_signal,np.linalg.norm(Dconn))
            qv_signal=max(qv_signal,np.linalg.norm(Gamma))

    print(f"worst Kelvin dyad Cartan residual: {base:.3e}")
    print(f"worst resolved/unresolved five-face residual: {split:.3e}")
    print(f"worst dyad symmetry residual: {symmetry:.3e}")
    print(f"worst pure-connection trace residual: {trace_conn:.3e}")
    print(f"worst pure-connection tr(R^2) derivative residual: {power2:.3e}")
    print(f"worst pure-connection tr(R^3) derivative residual: {power3:.3e}")
    print(f"worst residual-energy trace law residual: {energy:.3e}")
    print(f"maximum strain/connection/qv signals: {strain_signal:.3e} {conn_signal:.3e} {qv_signal:.3e}")
    assert base<2e-13
    assert split<3e-13
    assert symmetry<2e-13
    assert trace_conn<2e-13
    assert power2<3e-12
    assert power3<5e-12
    assert energy<2e-13
    assert strain_signal>1e-5 and conn_signal>1e-5 and qv_signal>1e-5
    print("PASS: Kelvin dyad dynamics split into resolved/unresolved deformation, connection, and q.v. faces")


if __name__=='__main__': main()
