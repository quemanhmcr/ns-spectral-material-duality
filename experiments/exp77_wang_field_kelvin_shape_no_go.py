"""Action-only exact periodic NS referee for field/Hessian insufficiency of finite Kelvin shape."""
import numpy as np


def residual(a,b,nu,t):
    E=np.exp(-nu*t)
    exact=-4*a*E*np.sin(b)
    local=-4*a*b*E
    return exact-local


def main():
    nu=.29; t=.43
    pde=hessian=stokes=area_pair=series=0.0
    signal=0.0

    # Exact periodic NSE equation over the full y-period.
    for y in np.linspace(-np.pi,np.pi,6001):
        E=np.exp(-nu*t)
        U=E*np.sin(y); Ut=-nu*U; Uyy=-U
        pde=max(pde,abs(Ut-nu*Uyy)/(1+abs(Ut)+abs(nu*Uyy)))

    # Anchor Hessian vanishes exactly.
    y0=0.0; E=np.exp(-nu*t)
    d2=-E*np.sin(y0)
    hessian=abs(d2)

    # Direct numerical surface flux agrees with closed formula for many rectangles.
    for b in np.linspace(.05,1.4,80):
        a=.37
        ys=np.linspace(-b,b,20001)
        omega=-E*np.cos(ys)
        numeric=2*a*np.trapezoid(omega,ys)
        exact=-4*a*E*np.sin(b)
        stokes=max(stokes,abs(numeric-exact)/(1+abs(numeric)+abs(exact)))
        eps=residual(a,b,nu,t)
        signal=max(signal,abs(eps))

    # Same area and orientation, different aspect ratio -> different residual.
    A0=1.6
    b1=.35; b2=1.05
    a1=A0/(4*b1); a2=A0/(4*b2)
    e1=residual(a1,b1,nu,t); e2=residual(a2,b2,nu,t)
    area_pair=abs(e1-e2)

    # Small-b expansion begins at b^3 although the Hessian jet is zero.
    a=.51
    for b in [1e-2,2e-2,4e-2,8e-2]:
        eps=residual(a,b,nu,t)
        approx=(2.0/3.0)*a*E*b**3-(1.0/30.0)*a*E*b**5
        series=max(series,abs(eps-approx)/(1+abs(eps)+abs(approx)))

    print(f"worst exact periodic NSE residual: {pde:.3e}")
    print(f"anchor common Hessian-jet signal: {hessian:.3e}")
    print(f"worst direct Stokes surface-flux residual: {stokes:.3e}")
    print(f"same-area different-shape Kelvin residual separation: {area_pair:.3e}")
    print(f"worst small-shape higher-jet expansion residual: {series:.3e}")
    print(f"maximum finite Kelvin descent-residual signal with B=0: {signal:.3e}")
    assert pde<2e-14
    assert hessian==0.0
    assert stokes<2e-9
    assert area_pair>1e-2
    assert series<2e-11
    assert signal>1e-2
    print("PASS: identical Eulerian field/local Hessian can carry different nonzero Kelvin finite-shape residuals")


if __name__=='__main__': main()
