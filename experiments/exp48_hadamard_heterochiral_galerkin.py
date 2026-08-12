"""Actual Fourier-Galerkin NSE adversary for the Hadamard heterochiral ladder.

This is a stress test only.  It evolves the full cubic-cutoff Galerkin vector field,
not an isolated hand-written shell model.
"""
import numpy as np


def hbasis(k, s):
    k = np.asarray(k, dtype=float)
    n = np.linalg.norm(k)
    kh = k / n
    refs = [np.array([0.0,0.0,1.0]), np.array([0.0,1.0,0.0]), np.array([1.0,0.0,0.0])]
    for ref in refs:
        e1 = np.cross(ref, kh)
        ne = np.linalg.norm(e1)
        if ne > 1e-10:
            e1 /= ne
            break
    e2 = np.cross(kh, e1)
    return (e1 + 1j * s * e2) / np.sqrt(2.0)


def idx(k, n):
    return tuple(int(x) % n for x in k)


def put_real_mode(uh, k, s, amp):
    n = uh.shape[0]
    h = hbasis(k, s)
    v = amp * h
    uh[idx(k,n)] += v
    uh[idx(tuple(-np.asarray(k,dtype=int)),n)] += np.conjugate(v)


def project_helical(uh, k, s):
    n=uh.shape[0]
    return np.vdot(hbasis(k,s), uh[idx(k,n)])


def make_waves(n):
    w = np.fft.fftfreq(n) * n
    kx,ky,kz=np.meshgrid(w,w,w,indexing='ij')
    return kx,ky,kz


def rhs(uh, nu, waves, cutoff):
    n=uh.shape[0]
    kx,ky,kz=waves
    ks=(kx,ky,kz)
    u=np.stack([np.fft.ifftn(uh[...,i], norm='forward') for i in range(3)],axis=-1)
    non=np.zeros_like(u)
    for j,kj in enumerate(ks):
        for i in range(3):
            grad=np.fft.ifftn(1j*kj*uh[...,i], norm='forward')
            non[...,i] += u[...,j]*grad
    nh=np.stack([np.fft.fftn(non[...,i], norm='forward') for i in range(3)],axis=-1)
    k2=kx*kx+ky*ky+kz*kz
    dot=kx*nh[...,0]+ky*nh[...,1]+kz*nh[...,2]
    proj=nh.copy()
    mask=k2>0
    for i,ki in enumerate(ks):
        proj[...,i][mask] -= ki[mask]*dot[mask]/k2[mask]
    out=-proj-nu*k2[...,None]*uh
    keep=(np.abs(kx)<=cutoff)&(np.abs(ky)<=cutoff)&(np.abs(kz)<=cutoff)&mask
    out[~keep]=0.0
    return out


def energy(uh):
    return float(np.sum(np.abs(uh)**2).real)


def div_res(uh,waves):
    kx,ky,kz=waves
    d=kx*uh[...,0]+ky*uh[...,1]+kz*uh[...,2]
    return float(np.max(np.abs(d)))


def main():
    n=16
    cutoff=3
    nu=0.01
    waves=make_waves(n)
    uh=np.zeros((n,n,n,3),dtype=complex)
    p0=(1,0,0); q0=(0,1,0)
    p1=(1,1,0); q1=(1,-1,0)
    p2=(2,0,0); q2=(0,2,0)
    put_real_mode(uh,p0,+1,1.0)
    put_real_mode(uh,q0,-1,1.0)

    r0=rhs(uh,nu,waves,cutoff)
    birth_p1=abs(project_helical(r0,p1,+1))
    birth_q1=abs(project_helical(r0,q1,-1))
    wrong_p1=abs(project_helical(r0,p1,-1))
    wrong_q1=abs(project_helical(r0,q1,+1))

    e0=energy(uh)
    dt=5e-4
    steps=160
    max_p1=max_q1=max_p2=max_q2=0.0
    for _ in range(steps):
        k1=rhs(uh,nu,waves,cutoff)
        k2=rhs(uh+0.5*dt*k1,nu,waves,cutoff)
        k3=rhs(uh+0.5*dt*k2,nu,waves,cutoff)
        k4=rhs(uh+dt*k3,nu,waves,cutoff)
        uh=uh+(dt/6.0)*(k1+2*k2+2*k3+k4)
        max_p1=max(max_p1,abs(project_helical(uh,p1,+1)))
        max_q1=max(max_q1,abs(project_helical(uh,q1,-1)))
        max_p2=max(max_p2,abs(project_helical(uh,p2,+1)))
        max_q2=max(max_q2,abs(project_helical(uh,q2,-1)))

    ef=energy(uh)
    dr=div_res(uh,waves)
    amp_factor=4.0-2.0*np.sqrt(2.0)
    p_high=2.0/(1.0+np.sqrt(2.0))
    p_opp=3.0-2.0*np.sqrt(2.0)

    print(f"first-generation desired + birth source: {birth_p1:.6e}")
    print(f"first-generation desired - birth source: {birth_q1:.6e}")
    print(f"first-generation wrong-helicity source p1-: {wrong_p1:.6e}")
    print(f"first-generation wrong-helicity source q1+: {wrong_q1:.6e}")
    print(f"max |a_(p1,+)|: {max_p1:.6e}")
    print(f"max |a_(q1,-)|: {max_q1:.6e}")
    print(f"max |a_(p2,+)|: {max_p2:.6e}")
    print(f"max |a_(q2,-)|: {max_q2:.6e}")
    print(f"energy ratio final/initial: {ef/e0:.9f}")
    print(f"worst final divergence residual: {dr:.3e}")
    print(f"static high energy fraction: {p_high:.9f}")
    print(f"static opposite fraction: {p_opp:.9f}")
    print(f"static high critical amplification: {amp_factor:.9f}")

    # Algebraic ladder geometry and static split laws.
    assert abs(p_high+p_opp-1.0)<1e-14
    assert amp_factor>1.0
    assert abs(np.dot(np.array(p1),np.array(q1)))<1e-14
    assert abs(np.linalg.norm(p1)-np.sqrt(2.0))<1e-14
    assert abs(np.linalg.norm(q1)-np.sqrt(2.0))<1e-14
    # Actual NSE adversary: desired first generation must be genuinely born.
    assert birth_p1>1e-5 and birth_q1>1e-5
    assert max_p1>1e-5 and max_q1>1e-5
    # Do not require dominance; merely test whether the second Hadamard generation is dynamically reachable.
    assert max_p2>1e-9 and max_q2>1e-9
    assert dr<1e-9
    assert ef<=e0*(1.0+1e-8)
    print("PASS: actual Galerkin NSE permits two-generation Hadamard heterochiral birth signal")


if __name__=='__main__':
    main()
