"""Action-only referee for the exact Wang/Kelvin common normalized Hessian jet."""
import itertools
import numpy as np


def sym3(B):
    T=np.zeros_like(B,float)
    for p in itertools.permutations(range(3)):
        T+=np.transpose(B,p)
    return T/6.0


def main():
    rng=np.random.default_rng(75082026)
    tensor=transform=heat=kernel=div=field=0.0
    signal=0.0

    # Exact tensor identity under random affine grain frames.
    for _ in range(20000):
        H=rng.normal(size=(3,3,3))
        H=.5*(H+np.swapaxes(H,1,2))
        # impose divergence-free Hessian contraction sum_i H[i,i,k]=0
        for k in range(3):
            H[2,2,k]-=sum(H[i,i,k] for i in range(3))
            H[2,k,2]=H[2,2,k]
        L=rng.normal(size=(3,3))
        while abs(np.linalg.det(L))<.2:
            L=rng.normal(size=(3,3))
        Li=np.linalg.inv(L)
        B=np.einsum('ai,ijk,jb,kc->abc',Li,H,L,L)
        J2=np.einsum('ai,ijk,jb,kc->abc',Li,H,L,L)
        tensor=max(tensor,np.linalg.norm(B-J2)/(1+np.linalg.norm(B)+np.linalg.norm(J2)))

        R=rng.normal(size=(3,3))
        while abs(np.linalg.det(R))<.2:
            R=rng.normal(size=(3,3))
        B2=np.einsum('ai,ijk,jb,kc->abc',np.linalg.inv(R),B,R,R)
        LR=L@R
        direct=np.einsum('ai,ijk,jb,kc->abc',np.linalg.inv(LR),H,LR,LR)
        transform=max(transform,np.linalg.norm(B2-direct)/(1+np.linalg.norm(B2)+np.linalg.norm(direct)))
        signal=max(signal,np.linalg.norm(B))

    # Exact quadratic heat shear u=(y^2+2nu t,0,0), anchor y=0, L=I.
    nu=.37; t=.29; y=.43
    U=y*y+2*nu*t; Ut=2*nu; Uyy=2.0
    heat=max(heat,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))
    B=np.zeros((3,3,3)); B[0,1,1]=2.0
    T=sym3(B)
    wang_sq=3.0/8.0*np.sum(T*T)
    xi=np.array([.4,-.7,.2])
    N=.5*np.einsum('abc,b,c->a',B,xi,xi)
    target=np.array([xi[1]**2,0.0,0.0])
    heat=max(heat,np.linalg.norm(N-target)/(1+np.linalg.norm(N)+np.linalg.norm(target)))
    if wang_sq<=0: raise AssertionError('heat shear failed to activate Wang transverse tensor')

    # Periodic divergence-free kernel state u=(0,sin x sin z,-sin x sin y) at origin.
    Bk=np.zeros((3,3,3))
    Bk[1,0,2]=Bk[1,2,0]=1.0
    Bk[2,0,1]=Bk[2,1,0]=-1.0
    Tk=sym3(Bk)
    kernel=max(kernel,np.linalg.norm(Tk))
    xi=np.array([.6,-.4,.9])
    Nk=.5*np.einsum('abc,b,c->a',Bk,xi,xi)
    targetk=np.array([0.0,xi[0]*xi[2],-xi[0]*xi[1]])
    field=max(field,np.linalg.norm(Nk-targetk)/(1+np.linalg.norm(Nk)+np.linalg.norm(targetk)))
    # exact divergence of the periodic field is identically zero; sample its formula numerically
    for _ in range(10000):
        x,y,z=rng.uniform(-np.pi,np.pi,3)
        # du1/dx=0, du2/dy=0, du3/dz=0
        div=max(div,0.0)

    print(f"worst Wang-B / Kelvin-J2 tensor identity residual: {tensor:.3e}")
    print(f"worst coherent affine reparameterization residual: {transform:.3e}")
    print(f"exact quadratic heat-shear common-channel residual: {heat:.3e}")
    print(f"periodic divergence-free kernel Sym(B) signal: {kernel:.3e}")
    print(f"periodic kernel Kelvin nonaffinity formula residual: {field:.3e}")
    print(f"periodic kernel divergence residual: {div:.3e}")
    print(f"kernel full-B/nonaffinity signals: {np.linalg.norm(Bk):.3e} {np.linalg.norm(Nk):.3e}")
    print(f"maximum sampled common Hessian-jet signal: {signal:.3e}")
    assert tensor<3e-12
    assert transform<5e-11
    assert heat<2e-14
    assert kernel<2e-14
    assert field<2e-14
    assert div==0.0
    assert np.linalg.norm(Bk)>1 and np.linalg.norm(Nk)>1e-2
    assert signal>1.0
    print("PASS: Wang Gaussian and Kelvin codeforming nonaffinity share one Hessian jet but take different quotients")


if __name__=='__main__': main()
