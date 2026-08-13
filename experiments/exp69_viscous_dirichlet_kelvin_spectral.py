"""Action-only Parseval/NSE referee for spectral killing = Kelvin q.v. trace."""
import numpy as np
from exp58_resolved_cartan_material_metric import waves, random_divfree, grad


def main():
    rng=np.random.default_rng(69082026)
    n=12; ks=waves(n); k2=sum(k*k for k in ks); nu=.27
    vel=ens=qv=local=0.0
    signal=0.0
    for _ in range(40):
        u=random_divfree(rng,n,ks,3.0)
        uh=np.stack([np.fft.fftn(u[...,i],norm='forward') for i in range(3)],axis=-1)
        # vorticity in Fourier space i k x uhat
        kx,ky,kz=ks
        wh=np.empty_like(uh)
        wh[...,0]=1j*(ky*uh[...,2]-kz*uh[...,1])
        wh[...,1]=1j*(kz*uh[...,0]-kx*uh[...,2])
        wh[...,2]=1j*(kx*uh[...,1]-ky*uh[...,0])
        w=np.stack([np.fft.ifftn(wh[...,i],norm='forward').real for i in range(3)],axis=-1)
        Gu=grad(u,ks); Gw=grad(w,ks)
        phys_u=nu*float(np.mean(np.sum(Gu*Gu,axis=(-1,-2))))
        spec_u=nu*float(np.sum(k2[...,None]*np.abs(uh)**2))
        vel=max(vel,abs(phys_u-spec_u)/(1+abs(phys_u)+abs(spec_u)))
        phys_w=nu*float(np.mean(np.sum(Gw*Gw,axis=(-1,-2))))
        spec_w=nu*float(np.sum(k2[...,None]*np.abs(wh)**2))
        ens=max(ens,abs(phys_w-spec_w)/(1+abs(phys_w)+abs(spec_w)))
        Gamma=2*nu*np.einsum('...ij,...lj->...il',Gw,Gw)
        halftrace=.5*float(np.mean(np.trace(Gamma,axis1=-2,axis2=-1)))
        qv=max(qv,abs(halftrace-phys_w)/(1+abs(halftrace)+abs(phys_w)))
        point_half=.5*np.trace(Gamma,axis1=-2,axis2=-1)
        point_dir=nu*np.sum(Gw*Gw,axis=(-1,-2))
        local=max(local,float(np.max(np.abs(point_half-point_dir)/(1+np.abs(point_half)+np.abs(point_dir)))))
        signal=max(signal,phys_w)
    print(f"worst velocity spectral/Dirichlet killing residual: {vel:.3e}")
    print(f"worst enstrophy spectral/Dirichlet killing residual: {ens:.3e}")
    print(f"worst integrated Kelvin-qv trace residual: {qv:.3e}")
    print(f"worst pointwise half-trace Dirichlet residual: {local:.3e}")
    print(f"maximum sampled enstrophy killing signal: {signal:.3e}")
    assert vel<3e-11
    assert ens<3e-11
    assert qv<3e-11
    assert local<2e-13
    assert signal>1e-3
    print("PASS: spectral viscous killing and Kelvin q.v. trace are the same full-state Dirichlet form")


if __name__=='__main__': main()
