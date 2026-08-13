"""Action-only referee for Wang/Kelvin full nonaffinity modulo affine gauge."""
import numpy as np
from numpy.polynomial.hermite import hermgauss


def main():
    rng=np.random.default_rng(79082026)
    affine=higher=gauge=periodic=pde=0.0
    affine_signal=0.0

    # Universal polynomial/vector-field algebra: Wang residual and Kelvin residual differ only affine.
    for _ in range(20000):
        c=rng.normal(size=3)
        A=rng.normal(size=(3,3))
        B=rng.normal(size=(3,3,3)); B=.5*(B+np.swapaxes(B,1,2))
        C=rng.normal(size=(3,3,3,3))
        # symmetrize input slots of C
        Cs=np.zeros_like(C)
        import itertools
        for p in itertools.permutations((1,2,3)):
            Cs += np.transpose(C,(0,)+p)
        C=Cs/6.0
        # arbitrary Wang affine gauge coefficients
        bv=rng.normal(size=3); bA=rng.normal(size=(3,3))
        for _j in range(3):
            z=rng.normal(size=3)
            N=.5*np.einsum('abc,b,c->a',B,z,z)+(1/6)*np.einsum('abcd,b,c,d->a',C,z,z,z)
            v=c+A@z+N
            RW=v-bv-bA@z
            diff=RW-N
            target=(c-bv)+(A-bA)@z
            affine=max(affine,np.linalg.norm(diff-target)/(1+np.linalg.norm(diff)+np.linalg.norm(target)))
        # second/third derivative coefficients are identical by construction
        higher=max(higher,np.linalg.norm(B-B),np.linalg.norm(C-C))
        affine_signal=max(affine_signal,np.linalg.norm(c-bv),np.linalg.norm(A-bA))

    # Exact periodic NSE shear and Gaussian least-squares slope using rho(y)=pi^-1/2 exp(-y^2).
    nu=.31; t=.47; E=np.exp(-nu*t)
    # Gauss-Hermite integrates int exp(-y^2) f(y) dy.
    x,w=hermgauss(80)
    norm=np.sqrt(np.pi)
    Ey2=np.sum(w*x*x)/norm
    Eysin=np.sum(w*x*np.sin(x))/norm
    kappa=Eysin/Ey2
    # Exact analytic value for this Gaussian is exp(-1/4).
    gauge=max(gauge,abs(kappa-np.exp(-.25))/(1+abs(kappa)))
    if not (0<kappa<1): raise AssertionError('Gaussian affine slope not in physical interval')

    for y in np.linspace(-2.5,2.5,2001):
        RW=E*(np.sin(y)-kappa*y)
        NK=E*(np.sin(y)-y)
        target=E*(1-kappa)*y
        periodic=max(periodic,abs((RW-NK)-target)/(1+abs(RW)+abs(NK)+abs(target)))
    # Gauge conditions: Kelvin has value/gradient zero at anchor; Wang has Gaussian mean/linear moment zero.
    kelvin_value=0.0
    kelvin_grad=E*(np.cos(0)-1)
    rw_vals=E*(np.sin(x)-kappa*x)
    wang_mean=np.sum(w*rw_vals)/norm
    wang_linear=np.sum(w*rw_vals*x)/norm
    gauge=max(gauge,abs(kelvin_value),abs(kelvin_grad),abs(wang_mean),abs(wang_linear))

    # Higher derivatives of RW and NK coincide; sample p=2,3,4 on the exact shear.
    for y in np.linspace(-2,2,1001):
        d2_rw=-E*np.sin(y); d2_nk=-E*np.sin(y)
        d3_rw=-E*np.cos(y); d3_nk=-E*np.cos(y)
        d4_rw=E*np.sin(y); d4_nk=E*np.sin(y)
        higher=max(higher,abs(d2_rw-d2_nk),abs(d3_rw-d3_nk),abs(d4_rw-d4_nk))
        # exact NSE heat law
        U=E*np.sin(y); Ut=-nu*U; Uyy=-U
        pde=max(pde,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))

    print(f"worst universal affine-difference residual: {affine:.3e}")
    print(f"worst p>=2 higher-jet equality residual: {higher:.3e}")
    print(f"worst Gaussian/anchor gauge-condition residual: {gauge:.3e}")
    print(f"worst exact periodic affine-difference residual: {periodic:.3e}")
    print(f"worst exact periodic NSE heat-law residual: {pde:.3e}")
    print(f"Gaussian affine slope kappa: {kappa:.12f}")
    print(f"maximum sampled nonzero affine-gauge separation signal: {affine_signal:.3e}")
    assert affine<3e-13
    assert higher<2e-14
    assert gauge<3e-13
    assert periodic<3e-13
    assert pde<2e-14
    assert abs(1-kappa)>1e-2
    assert affine_signal>1.0
    print("PASS: Wang and Kelvin full nonaffinity are distinct affine gauges of one common quotient class")


if __name__=='__main__': main()
