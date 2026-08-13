"""Action-only Fourier referee for HH Cartan/material role row identity."""
import numpy as np
from exp58_resolved_cartan_material_metric import waves, random_divfree, grad, leray, inner, apply
from exp59_role_space_cartan_gauge import matrices


def role_fields(h,ks):
    hh=np.stack([np.fft.fftn(h[...,i],norm='forward') for i in range(3)],axis=-1)
    k2=sum(k*k for k in ks)
    out=[]
    for val in (1,2,3,4):
        mask=np.isclose(k2,float(val))
        part=np.zeros_like(hh)
        part[mask]=hh[mask]
        out.append(np.stack([np.fft.ifftn(part[...,i],norm='forward').real for i in range(3)],axis=-1))
    return out


def main():
    rng=np.random.default_rng(62082026)
    n=12; ks=waves(n)
    bilinear=row=global_energy=kskew=ssym=stotal=metric=0.0
    connection_signal=hh_signal=0.0
    for _ in range(40):
        h=random_divfree(rng,n,ks,2.0)
        W=role_fields(h,ks)
        recon=sum(W,start=np.zeros_like(h))
        if np.linalg.norm(recon-h)>2e-10*(1+np.linalg.norm(h)):
            raise AssertionError('roles do not reconstruct h')

        G=grad(h,ks)
        adv=np.einsum('...j,...ij->...i',h,G)
        B=leray(adv,ks)
        Lh=apply(h,h,ks,'L')
        bilinear=max(bilinear,np.linalg.norm(Lh-2*B)/(1+np.linalg.norm(Lh)+2*np.linalg.norm(B)))

        K,S=matrices(h,W,ks)
        T=np.array([inner(w,B) for w in W])
        rows=.5*np.sum(K+S,axis=1)
        row=max(row,np.linalg.norm(T-rows)/(1+np.linalg.norm(T)+np.linalg.norm(rows)))
        global_energy=max(global_energy,abs(np.sum(T))/(1+np.linalg.norm(T)))
        kskew=max(kskew,np.linalg.norm(K+K.T)/(1+np.linalg.norm(K)))
        ssym=max(ssym,np.linalg.norm(S-S.T)/(1+np.linalg.norm(S)))
        one=np.ones(4)
        stotal=max(stotal,abs(float(one@S@one))/(1+np.linalg.norm(S)))
        connection_signal=max(connection_signal,np.max(np.abs(np.sum(K,axis=1))))
        hh_signal=max(hh_signal,np.max(np.abs(T)))

        # Entire unresolved symmetric role matrix is one material-metric form.
        A=grad(h,ks); Sh=.5*(A+np.swapaxes(A,-1,-2))
        q=.19; sh=.13
        F=np.array([[np.exp(q),sh,0.0],[0.0,np.exp(-q),0.0],[0.0,0.0,1.0]])
        H=np.linalg.inv(F).T
        Mdot=np.einsum('ji,...jk,kl->...il',F,Sh,F)*2.0
        for a in range(4):
            pa=np.einsum('ij,...j->...i',H.T,W[a])
            for b in range(4):
                pb=np.einsum('ij,...j->...i',H.T,W[b])
                met=.5*float(np.mean(np.einsum('...i,...ij,...j->...',pa,Mdot,pb)))
                metric=max(metric,abs(S[a,b]-met)/(1+abs(S[a,b])+abs(met)))

    print(f"worst L_h h=2B(h,h) residual: {bilinear:.3e}")
    print(f"worst HH role row Cartan residual: {row:.3e}")
    print(f"worst global HH energy conservation residual: {global_energy:.3e}")
    print(f"worst unresolved K skew residual: {kskew:.3e}")
    print(f"worst unresolved S symmetry residual: {ssym:.3e}")
    print(f"worst complete-field S_h self-work residual: {stotal:.3e}")
    print(f"worst unresolved material-metric matrix residual: {metric:.3e}")
    print(f"maximum nonzero unresolved K row signal: {connection_signal:.3e}")
    print(f"maximum signed HH role-work signal: {hh_signal:.3e}")
    assert bilinear<3e-11
    assert row<3e-11
    assert global_energy<3e-11
    assert kskew<3e-11
    assert ssym<3e-11
    assert stotal<3e-11
    assert metric<3e-11
    assert connection_signal>1e-5
    assert hh_signal>1e-5
    print("PASS: actual HH child work is the row-sum of unresolved connection and metric tensors")


if __name__=='__main__': main()
