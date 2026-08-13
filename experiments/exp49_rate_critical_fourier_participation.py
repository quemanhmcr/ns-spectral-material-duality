"""Action-only referee for convolution participation and sparse-ladder rate no-go."""
import numpy as np


def conv3(c):
    # exact cyclic convolution is enough to stress l1*l2 Young; zero padding avoids wrap in the tested support
    n=len(c)
    out=np.zeros(2*n-1)
    for i,x in enumerate(c):
        for j,y in enumerate(c):
            out[i+j]+=x*y
    return out


def main():
    rng=np.random.default_rng(49082026)
    young=participation=rate=0.0
    sparse_signal=0.0
    for _ in range(12000):
        n=int(rng.integers(4,50))
        c=rng.uniform(0.0,3.0,size=n)
        cv=conv3(c)
        # Triple sum with a third sequence supported on the convolution output.
        d=rng.uniform(0.0,3.0,size=len(cv))
        triple=float(np.dot(cv,d))
        rhs=float(np.sum(c)*np.linalg.norm(c)*np.linalg.norm(d))
        young=max(young,max(0.0,triple-rhs))

        E=float(np.dot(c,c))
        if E>1e-15:
            Meff=float(np.sum(c)**2/E)
            participation=max(participation,max(0.0,Meff-n))

    # Algebraic rate-gate inversion with the safe constants from CL.
    for _ in range(12000):
        nu=float(rng.uniform(0.02,2.0))
        N=float(2.0**int(rng.integers(1,10)))
        E=float(rng.uniform(1e-5,4.0))
        lower=nu*N**3*E/128.0
        required=(27.0*nu*N/(8192.0*np.sqrt(E)))**2
        upper_at_required=(64.0/27.0)*N**2*np.sqrt(required)*E**1.5
        rate=max(rate,abs(lower-upper_at_required)/(1.0+abs(lower)+abs(upper_at_required)))

        M0=float(rng.uniform(1.0,64.0))
        mu=nu*nu
        req=729.0*nu*nu*N**3/(8192.0**2*mu)
        if req>M0:
            sparse_signal=max(sparse_signal,req/M0)

    print(f"worst discrete Young convolution violation: {young:.3e}")
    print(f"worst effective-participation <= support violation: {participation:.3e}")
    print(f"worst inverted rate-gate algebra violation: {rate:.3e}")
    print(f"maximum sparse-ladder participation deficit factor: {sparse_signal:.3e}")
    assert young<2e-11
    assert participation<2e-11
    assert rate<2e-12
    assert sparse_signal>1.0
    print("PASS: rate-critical Fourier participation / sparse-ladder no-go calibrations")


if __name__=='__main__': main()
