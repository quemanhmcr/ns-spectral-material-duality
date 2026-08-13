"""Action-only referee for record-contact pressure-trace tax and renewal funding identities."""
import numpy as np


def rel(a,b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def fro(A):
    return float(np.linalg.norm(A))


def main():
    rng=np.random.default_rng(10213082026)
    strain_decomp_res=0.0
    pressure_split_res=0.0
    core_split_res=0.0
    funding_res=0.0
    pressure_bound_violation=-np.inf
    pressure_sharp_res=0.0
    positive_gate_margin=np.inf
    positive_gate_count=0

    for _ in range(1500):
        xi=rng.normal(size=3); xi/=np.linalg.norm(xi)
        Pi=np.eye(3)-np.outer(xi,xi)
        R=rng.normal(size=(3,3))
        S=0.5*(R+R.T)
        S=S-(np.trace(S)/3.0)*np.eye(3)
        alpha=float(xi@S@xi)
        if alpha < 0.0:
            S=-S; alpha=-alpha
        M=0.4+3.0*rng.random()
        b=Pi@S@xi
        T=Pi@S@Pi+0.5*alpha*Pi
        B=float(b@b/M)
        Theta=float(np.sum(T*T)/M)
        Sigma=alpha/np.sqrt(M)
        strain_rhs=1.5*alpha*alpha+2.0*(b@b)+np.sum(T*T)
        strain_decomp_res=max(strain_decomp_res, rel(np.sum(S*S),strain_rhs))

        Z=rng.normal(size=(3,3))
        Pdev=0.5*(Z+Z.T)
        Pdev=Pdev-(np.trace(Pdev)/3.0)*np.eye(3)
        lap_p=-np.sum(S*S)+M
        Hp=Pdev+(lap_p/3.0)*np.eye(3)
        pi_p=float(xi@Pdev@xi/M)
        pressure_direct=-float(xi@Hp@xi/M)
        pressure_formula=0.5*Sigma*Sigma+(2.0/3.0)*B+(1.0/3.0)*Theta-1.0/3.0-pi_p
        pressure_split_res=max(pressure_split_res, rel(pressure_direct,pressure_formula))

        V=float(rng.normal(scale=0.35))
        core_direct=B+pressure_direct+V
        core_formula=0.5*Sigma*Sigma+(5.0/3.0)*B+(1.0/3.0)*Theta-1.0/3.0-pi_p+V
        core_split_res=max(core_split_res, rel(core_direct,core_formula))

        # Positive record contact: choose defect below 2 Sigma.  Add a signed sweep.
        delta=(1.6*rng.random())*Sigma
        rho=2.0*Sigma-delta
        sweep=float(rng.normal(scale=0.35))
        norm=-0.5*Sigma*rho
        nrec=core_direct+sweep+norm
        funding_formula=-(0.5*Sigma*Sigma+1.0/3.0)+(5.0/3.0)*B+(1.0/3.0)*Theta-pi_p+V+sweep+0.5*Sigma*delta
        funding_res=max(funding_res,rel(nrec,funding_formula))

        qpnorm=fro(Pdev)/M
        pressure_bound_violation=max(pressure_bound_violation,abs(pi_p)-np.sqrt(2.0/3.0)*qpnorm)
        if nrec > 0.0:
            cap=(5.0/3.0)*B+(1.0/3.0)*Theta+np.sqrt(2.0/3.0)*qpnorm+max(V,0.0)+max(sweep,0.0)+0.5*Sigma*delta
            tax=0.5*Sigma*Sigma+1.0/3.0
            positive_gate_margin=min(positive_gate_margin,cap-tax)
            positive_gate_count+=1

        # Sharp directional pressure bound at this xi.
        Psharp=np.outer(xi,xi)-np.eye(3)/3.0
        sharp_ratio=abs(float(xi@Psharp@xi))/fro(Psharp)
        pressure_sharp_res=max(pressure_sharp_res,rel(sharp_ratio,np.sqrt(2.0/3.0)))

    # Exact one-mode heat shear: transverse shape pays the trace tax, core=0.
    amp=1.37; k=3.0
    wy=amp*k
    M=0.5*wy*wy
    S=np.array([[0.0,0.5*wy,0.0],[0.5*wy,0.0,0.0],[0.0,0.0,0.0]])
    xi=np.array([0.0,0.0,1.0]); Pi=np.eye(3)-np.outer(xi,xi)
    alpha=float(xi@S@xi); bvec=Pi@S@xi; T=Pi@S@Pi+0.5*alpha*Pi
    shear_B=float(bvec@bvec/M); shear_theta=float(np.sum(T*T)/M)
    shear_core=0.5*(alpha*alpha/M)+(5.0/3.0)*shear_B+(1.0/3.0)*shear_theta-1.0/3.0

    # Constant affine strain-spin: trace-free pressure anisotropy saturates the funding tax.
    a0=0.23; om0=0.81
    const_pi_res=0.0; const_nrec_res=0.0; const_tax_signal=np.inf
    for t in np.linspace(0.0,1.5,31):
        om=om0*np.exp(2.0*a0*t)
        M=2.0*om*om
        sigma=np.sqrt(2.0)*a0/om
        Hp=np.diag([om*om-a0*a0,om*om-a0*a0,-4.0*a0*a0])
        Pdev=Hp-(np.trace(Hp)/3.0)*np.eye(3)
        pi=Pdev[2,2]/M
        target_pi=-1.0/3.0-0.5*sigma*sigma
        const_pi_res=max(const_pi_res,rel(pi,target_pi))
        nrec=-(0.5*sigma*sigma+1.0/3.0)-pi
        const_nrec_res=max(const_nrec_res,abs(nrec))
        const_tax_signal=min(const_tax_signal,0.5*sigma*sigma+1.0/3.0)

    # Accelerating affine: positive renewal equals pressure-anisotropy excess a'/Omega^2.
    Tfinal=3.0; b0=0.71
    accel_pi_res=0.0; accel_nrec_res=0.0; accel_sigma_res=0.0; accel_signal=np.inf
    for t in np.linspace(0.0,2.7,55):
        s=Tfinal-t
        a=1.0/(2.0*s); adot=1.0/(2.0*s*s); om=b0/s
        M=2.0*om*om; sigma=np.sqrt(2.0)*a/om
        Hp=np.diag([om*om-a*a+adot,om*om-a*a+adot,-2.0*adot-4.0*a*a])
        Pdev=Hp-(np.trace(Hp)/3.0)*np.eye(3)
        pi=Pdev[2,2]/M
        target_pi=-1.0/3.0-0.5*sigma*sigma-adot/(om*om)
        accel_pi_res=max(accel_pi_res,rel(pi,target_pi))
        nrec=-(0.5*sigma*sigma+1.0/3.0)-pi
        target=adot/(om*om)
        accel_nrec_res=max(accel_nrec_res,rel(nrec,target))
        accel_sigma_res=max(accel_sigma_res,rel(target,sigma*sigma))
        accel_signal=min(accel_signal,nrec)

    print(f"vorticity-adapted strain decomposition residual: {strain_decomp_res:.3e}")
    print(f"pressure trace/deviator split residual: {pressure_split_res:.3e}")
    print(f"record-contact core decomposition residual: {core_split_res:.3e}")
    print(f"positive-contact funding identity residual: {funding_res:.3e}")
    print(f"sharp pressure-capacity bound maximum violation: {pressure_bound_violation:.3e}")
    print(f"sharp pressure coefficient saturation residual: {pressure_sharp_res:.3e}")
    print(f"positive-renewal random gate sample count: {positive_gate_count}")
    print(f"minimum positive-renewal capacity margin: {positive_gate_margin:.6e}")
    print(f"heat-shear B/Theta/core: {shear_B:.6e} / {shear_theta:.6e} / {shear_core:.3e}")
    print(f"constant-affine pressure-anisotropy residual: {const_pi_res:.3e}")
    print(f"constant-affine zero-renewal funding residual: {const_nrec_res:.3e}")
    print(f"constant-affine minimum tax signal: {const_tax_signal:.6e}")
    print(f"accelerating-affine pressure-anisotropy residual: {accel_pi_res:.3e}")
    print(f"accelerating-affine renewal-excess residual: {accel_nrec_res:.3e}")
    print(f"accelerating-affine renewal equals sigma^2 residual: {accel_sigma_res:.3e}")
    print(f"accelerating-affine minimum positive renewal signal: {accel_signal:.6e}")

    assert strain_decomp_res < 3e-13
    assert pressure_split_res < 3e-13
    assert core_split_res < 3e-13
    assert funding_res < 4e-13
    assert pressure_bound_violation < 3e-13
    assert pressure_sharp_res < 3e-14
    assert positive_gate_count > 100
    assert positive_gate_margin > -3e-13
    assert abs(shear_B) < 2e-14
    assert rel(shear_theta,1.0) < 2e-14
    assert abs(shear_core) < 2e-14
    assert const_pi_res < 3e-14
    assert const_nrec_res < 3e-14
    assert const_tax_signal > 1.0/3.0
    assert accel_pi_res < 3e-14
    assert accel_nrec_res < 3e-14
    assert accel_sigma_res < 3e-14
    assert accel_signal > 0.1
    print("PASS: incompressibility imposes a universal record-contact funding tax; positive renewal must be paid by named strain/pressure/viscous/geometry channels, with exact affine zero-versus-positive pressure-anisotropy calibrations")


if __name__ == '__main__':
    main()
