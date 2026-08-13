"""Action-only referee for the resolved Cartan/material-metric bridge."""
import numpy as np


def waves(n):
    w=np.fft.fftfreq(n)*n
    return np.meshgrid(w,w,w,indexing='ij')


def project_hat(uh, ks):
    kx,ky,kz=ks
    k2=kx*kx+ky*ky+kz*kz
    out=uh.copy()
    dot=kx*out[...,0]+ky*out[...,1]+kz*out[...,2]
    mask=k2>0
    for j,kj in enumerate(ks):
        out[...,j][mask]-=kj[mask]*dot[mask]/k2[mask]
    out[~mask]=0.0
    return out


def random_divfree(rng,n,ks,cutoff):
    x=rng.normal(size=(n,n,n,3))
    uh=np.stack([np.fft.fftn(x[...,j],norm='forward') for j in range(3)],axis=-1)
    kx,ky,kz=ks
    keep=(kx*kx+ky*ky+kz*kz<=cutoff*cutoff)
    uh[~keep]=0.0
    uh=project_hat(uh,ks)
    return np.stack([np.fft.ifftn(uh[...,j],norm='forward').real for j in range(3)],axis=-1)


def grad(u,ks):
    uh=np.stack([np.fft.fftn(u[...,i],norm='forward') for i in range(3)],axis=-1)
    out=np.zeros(u.shape+(3,),float)
    for i in range(3):
        for j,kj in enumerate(ks):
            out[...,i,j]=np.fft.ifftn(1j*kj*uh[...,i],norm='forward').real
    return out


def leray(v,ks):
    vh=np.stack([np.fft.fftn(v[...,i],norm='forward') for i in range(3)],axis=-1)
    vh=project_hat(vh,ks)
    return np.stack([np.fft.ifftn(vh[...,i],norm='forward').real for i in range(3)],axis=-1)


def apply(V,g,ks,kind):
    A=grad(V,ks); G=grad(g,ks)
    S=0.5*(A+np.swapaxes(A,-1,-2))
    O=0.5*(A-np.swapaxes(A,-1,-2))
    adv=np.einsum('...j,...ij->...i',V,G)
    if kind=='L': raw=adv+np.einsum('...ij,...j->...i',A,g)
    elif kind=='K': raw=adv+np.einsum('...ij,...j->...i',O,g)
    elif kind=='S': raw=np.einsum('...ij,...j->...i',S,g)
    else: raise ValueError(kind)
    return leray(raw,ks)


def inner(a,b):
    return float(np.mean(np.sum(a*b,axis=-1)))


def rel(a,b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def cross_matrix(w):
    x,y,z=w
    return np.array([[0.0,-z,y],[z,0.0,-x],[-y,x,0.0]])


def main():
    rng=np.random.default_rng(58082026)
    n=8; ks=waves(n)
    split=adjk=adjs=energy=metric=curlres=0.0
    signal=0.0
    for _ in range(32):
        V=random_divfree(rng,n,ks,2.0)
        f=random_divfree(rng,n,ks,3.0)
        g=random_divfree(rng,n,ks,3.0)
        Lg=apply(V,g,ks,'L'); Kg=apply(V,g,ks,'K'); Sg=apply(V,g,ks,'S')
        Kf=apply(V,f,ks,'K'); Sf=apply(V,f,ks,'S')
        den=1.0+np.linalg.norm(Lg)+np.linalg.norm(Kg)+np.linalg.norm(Sg)
        split=max(split,np.linalg.norm(Lg-Kg-Sg)/den)
        adjk=max(adjk,abs(inner(f,Kg)+inner(Kf,g))/(1+abs(inner(f,Kg))+abs(inner(Kf,g))))
        adjs=max(adjs,abs(inner(f,Sg)-inner(Sf,g))/(1+abs(inner(f,Sg))+abs(inner(Sf,g))))
        Lf=apply(V,f,ks,'L')
        A=grad(V,ks); S=0.5*(A+np.swapaxes(A,-1,-2))
        direct=float(np.mean(np.einsum('...i,...ij,...j->...',f,S,f)))
        energy=max(energy,rel(inner(f,Lf),direct),abs(inner(f,Kf))/(1+abs(direct)))
        signal=max(signal,abs(direct))

        # Material-metric congruence at sampled actual spatial strain states.
        q=float(rng.uniform(-0.5,0.5)); sh=float(rng.uniform(-0.4,0.4))
        F=np.array([[np.exp(q),sh,0.0],[0.0,np.exp(-q),0.0],[0.0,0.0,1.0]])
        H=np.linalg.inv(F).T
        for idx in [(1,2,3),(4,1,5),(6,6,2)]:
            Sm=S[idx]; af=f[idx]; bg=g[idx]
            Mdot=2.0*F.T@Sm@F
            pa=H.T@af; pb=H.T@bg
            metric=max(metric,rel(float(af@Sm@bg),0.5*float(pa@Mdot@pb)))

        # A-A^T=[curl V]_x.
        for idx in [(0,1,2),(3,4,5),(7,2,6)]:
            Am=A[idx]
            omg=np.array([Am[2,1]-Am[1,2],Am[0,2]-Am[2,0],Am[1,0]-Am[0,1]])
            curlres=max(curlres,np.linalg.norm((Am-Am.T)-cross_matrix(omg))/(1+np.linalg.norm(Am)))

    print(f"worst L=K+S field residual: {split:.3e}")
    print(f"worst K skew-adjoint residual: {adjk:.3e}")
    print(f"worst S self-adjoint residual: {adjs:.3e}")
    print(f"worst energy/strain residual: {energy:.3e}")
    print(f"worst material-metric bilinear residual: {metric:.3e}")
    print(f"worst vorticity cross-matrix residual: {curlres:.3e}")
    print(f"maximum sampled resolved-strain work signal: {signal:.3e}")
    assert split<2e-11
    assert adjk<2e-11
    assert adjs<2e-11
    assert energy<2e-11
    assert metric<2e-12
    assert curlres<2e-11
    assert signal>1e-5
    print("PASS: resolved linearized NSE Cartan split is exact material-metric strain geometry")


if __name__=='__main__': main()
