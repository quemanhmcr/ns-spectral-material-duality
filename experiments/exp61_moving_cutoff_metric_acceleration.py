"""Action-only actual Galerkin-NSE referee for cutoff metric-velocity/acceleration faces."""
import numpy as np
from exp58_resolved_cartan_material_metric import waves, random_divfree, grad, leray, inner


def symbol_apply(arr,sym):
    out=np.empty_like(arr,float)
    tail=arr.shape[3:]
    if not tail:
        ah=np.fft.fftn(arr,norm='forward')
        return np.fft.ifftn(sym*ah,norm='forward').real
    for ind in np.ndindex(tail):
        sl=(slice(None),slice(None),slice(None))+ind
        ah=np.fft.fftn(arr[sl],norm='forward')
        out[sl]=np.fft.ifftn(sym*ah,norm='forward').real
    return out


def advect_tensor(v,T,ks):
    out=np.zeros_like(T)
    tail=T.shape[3:]
    for ind in np.ndindex(tail):
        sl=(slice(None),slice(None),slice(None))+ind
        th=np.fft.fftn(T[sl],norm='forward')
        acc=np.zeros(T.shape[:3],float)
        for j,kj in enumerate(ks):
            der=np.fft.ifftn(1j*kj*th,norm='forward').real
            acc+=v[...,j]*der
        out[sl]=acc
    return out


def lap(u,ks):
    k2=sum(k*k for k in ks)
    out=np.zeros_like(u)
    for i in range(3):
        uh=np.fft.fftn(u[...,i],norm='forward')
        out[...,i]=np.fft.ifftn(-k2*uh,norm='forward').real
    return out


def ns_rhs(u,nu,ks):
    G=grad(u,ks)
    adv=np.einsum('...j,...ij->...i',u,G)
    return -leray(adv,ks)+nu*lap(u,ks)


def sym_skew(A):
    return .5*(A+np.swapaxes(A,-1,-2)), .5*(A-np.swapaxes(A,-1,-2))


def mat_comm(S,O):
    return np.einsum('...ij,...jk->...ik',S,O)-np.einsum('...ij,...jk->...ik',O,S)


def nrel(a,b):
    return np.linalg.norm(a-b)/(1+np.linalg.norm(a)+np.linalg.norm(b))


def main():
    rng=np.random.default_rng(61082026)
    n=12; ks=waves(n); k2=sum(k*k for k in ks)
    nu=.11
    metric=cartan=timeface=obj=reset=energy=0.0
    face_signal=[0.0,0.0,0.0,0.0]
    for _ in range(18):
        u=random_divfree(rng,n,ks,2.0)
        ut=ns_rhs(u,nu,ks)
        Au=grad(u,ks); Su,Ou=sym_skew(Au)
        Sut,_=sym_skew(grad(ut,ks))

        alpha=float(rng.uniform(.015,.055)); adot=float(rng.uniform(-.03,.04))
        R=np.exp(-alpha*k2); Rdot=-adot*k2*R
        V=symbol_apply(u,R); h=u-V
        Vt=symbol_apply(ut,R)+symbol_apply(u,Rdot)
        Av=grad(V,ks); Sv,Ov=sym_skew(Av)
        Ah=grad(h,ks); Sh,Oh=sym_skew(Ah)

        metric=max(metric,nrel(Su,Sv+Sh),nrel(Sv,symbol_apply(Su,R)),nrel(Ov,symbol_apply(Ou,R)))

        # Cartan type increments under a second fixed cutoff.
        alpha2=alpha+float(rng.uniform(.005,.025)); R2=np.exp(-alpha2*k2)
        V2=symbol_apply(u,R2); h2=u-V2; dV=V2-V
        S2,O2=sym_skew(grad(V2,ks)); Sh2,Oh2=sym_skew(grad(h2,ks)); Sd,Od=sym_skew(grad(dV,ks))
        cartan=max(cartan,nrel(S2-Sv,Sd),nrel(O2-Ov,Od),nrel(Sh2-Sh,-Sd),nrel(Oh2-Oh,-Od))

        # Moving-cut time face.
        Svt,_=sym_skew(grad(Vt,ks))
        timeface=max(timeface,nrel(Svt,symbol_apply(Sut,R)+symbol_apply(Su,Rdot)))

        ring_u=Sut+advect_tensor(u,Su,ks)+mat_comm(Su,Ou)
        ring_v=Svt+advect_tensor(V,Sv,ks)+mat_comm(Sv,Ov)
        Rring=symbol_apply(ring_u,R)
        face_t=symbol_apply(Su,Rdot)
        comm=advect_tensor(V,symbol_apply(Su,R),ks)-symbol_apply(advect_tensor(V,Su,ks),R)
        unresolved=-symbol_apply(advect_tensor(h,Su,ks),R)
        rot=mat_comm(symbol_apply(Su,R),symbol_apply(Ou,R))-symbol_apply(mat_comm(Su,Ou),R)
        rhs=face_t+comm+unresolved+rot
        obj=max(obj,nrel(ring_v-Rring,rhs))
        for j,x in enumerate((face_t,comm,unresolved,rot)):
            face_signal[j]=max(face_signal[j],np.linalg.norm(x))

        # Finite reset is representation-only at fixed physical u.
        reset=max(reset,nrel(S2-Sv,symbol_apply(Su,R2-R)))

        # Actual Galerkin NSE energy law at this state.
        G=grad(u,ks)
        diss=nu*float(np.mean(np.sum(G*G,axis=(-1,-2))))
        energy=max(energy,abs(inner(u,ut)+diss)/(1+abs(inner(u,ut))+abs(diss)))

    print(f"worst instantaneous metric repartition residual: {metric:.3e}")
    print(f"worst fixed-cutoff Cartan transfer residual: {cartan:.3e}")
    print(f"worst moving-cut time-face residual: {timeface:.3e}")
    print(f"worst objective-strain face decomposition residual: {obj:.3e}")
    print(f"worst finite-reset metric-velocity residual: {reset:.3e}")
    print(f"worst actual Galerkin NSE energy-law residual: {energy:.3e}")
    print("maximum face signals:"," ".join(f"{x:.3e}" for x in face_signal))
    assert metric<4e-11
    assert cartan<4e-11
    assert timeface<5e-11
    assert obj<8e-10
    assert reset<4e-11
    assert energy<3e-10
    assert all(x>1e-7 for x in face_signal)
    print("PASS: moving spectral resolution has exact metric-acceleration time/interface faces")


if __name__=='__main__': main()
