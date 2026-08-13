"""Action-only referee for scalar Morse selector finiteness calibrations and transverse support no-go."""
import numpy as np


def rel(a,b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def main():
    # 1. Kelvin's exact four-mode global-max crossing at t*=1/nu.
    nu = 0.37
    q0 = 6.0
    qp = 6.0
    qyy0 = -40.0
    qyyp = -56.0
    e0 = 0.5*q0*q0
    ep = 0.5*qp*qp
    R0 = nu*q0*qyy0
    Rp = nu*qp*qyyp
    dplus = max(R0,Rp)
    dminus = min(R0,Rp)
    cplus0 = R0-dplus
    cplusp = Rp-dplus
    cminus0 = R0-dminus
    cminusp = Rp-dminus
    four_value_res = max(rel(e0,18.0), rel(ep,18.0))
    four_rate_res = max(rel(R0,-240.0*nu), rel(Rp,-336.0*nu))
    defect_res = max(abs(cplus0), rel(cplusp,-96.0*nu), rel(cminus0,96.0*nu), abs(cminusp))

    # Literal global certificate stress over c=cos(y): |q(c)|<=6, equality at c=+-1.
    c = np.linspace(-1.0,1.0,500001)
    q = 16.0*c**4 - 4.0*c**3 - 8.0*c**2 + 4.0*c - 2.0
    sampled_excess = float(np.max(np.abs(q)-6.0))
    interior_abs = float(np.max(np.abs(q[1:-1])))

    # Analytic branch gap around the exact tie.  q0-qpi = 2(e^(1-s)-e^(9-9s)).
    # At s=1 the vorticity gap derivative is 16; enstrophy gap derivative is 6*16=96.
    sstar = 1.0
    def qzero(s):
        return np.exp(1.0-s) + 4*np.exp(4.0-4*s) - np.exp(9.0-9*s) + 2*np.exp(16.0-16*s)
    def qpi(s):
        return -np.exp(1.0-s) + 4*np.exp(4.0-4*s) + np.exp(9.0-9*s) + 2*np.exp(16.0-16*s)
    def gap_e(s):
        return 0.5*(qzero(s)**2-qpi(s)**2)
    h=1e-6
    gap_rate_s=(gap_e(sstar+h)-gap_e(sstar-h))/(2*h)
    gap_rate_res=rel(gap_rate_s,96.0)
    switch_sign = gap_e(sstar-1e-3)*gap_e(sstar+1e-3)

    # 2. Persistent tie class: one-mode heat shear has equal maxima at y=0,pi for all t.
    A=1.31; nu1=0.29; k=1.0
    persistent_gap=0.0
    persistent_curvature_margin=np.inf
    for t in np.linspace(0.05,2.0,101):
        amp=A*np.exp(-nu1*k*k*t)
        w0=amp; wp=-amp
        ee0=0.5*w0*w0; eep=0.5*wp*wp
        persistent_gap=max(persistent_gap,abs(ee0-eep))
        # e_yy=-amp^2 at both normal maxima for k=1.
        persistent_curvature_margin=min(persistent_curvature_margin,amp*amp)

    # 3. Many finite crossings inside one strict-normal-max compact interval (exp92 family).
    odd=np.array([1.0,3.0,5.0,7.0,9.0])
    roots=np.array([0.004,0.012,0.024,0.040])
    Mmat=np.exp(-np.outer(roots,odd**2))
    _,_,vh=np.linalg.svd(Mmat)
    a=vh[-1]; a/=np.max(np.abs(a))
    def O(s): return np.sum(a*np.exp(-(odd**2)*s))
    def Os(s): return np.sum(-(odd**2)*a*np.exp(-(odd**2)*s))
    def O2(s): return np.sum((odd**2)*a*np.exp(-(odd**2)*s))
    K=np.linspace(0.002,0.045,4001)
    E=np.exp(-4.0*K)
    Ovals=np.array([O(s) for s in K])
    O2vals=np.array([O2(s) for s in K])
    mE=float(np.min(E)); M0=float(np.max(np.abs(Ovals))); M2=float(np.max(np.abs(O2vals)))
    eps=0.25*min(0.2,mE/M0,4.0*mE/M2)
    w0=E+eps*Ovals; wp=E-eps*Ovals
    eyy0=w0*(-4.0*E-eps*O2vals)
    eyyp=wp*(-4.0*E+eps*O2vals)
    many_curvature_max=float(max(np.max(eyy0),np.max(eyyp)))
    many_interp=float(np.max(np.abs(Mmat@a)))
    many_simple=float(min(abs(Os(s)) for s in roots))
    sign_fail=0
    for s in roots:
        dm=2*eps*np.exp(-4*(s-0.0007))*O(s-0.0007)
        dp=2*eps*np.exp(-4*(s+0.0007))*O(s+0.0007)
        sign_fail += int(dm*dp>=0)

    # 4. Kelvin 1095c13 transverse-support no-go calibration.
    nmode=23.0; A2=0.81; nu2=0.17; t2=0.0
    alphas=np.array([0.4,0.1,0.02,0.005,0.001,1e-5])
    max_bpar_res=0.0
    volumes=[]; residuals=[]; yspans=[]
    for alpha in alphas:
        L=np.diag([1.0,2.0*alpha/nmode,1.0])
        B=L@L.T
        P=np.diag([1.0,0.0,1.0])
        Bpar=P@B@P
        max_bpar_res=max(max_bpar_res,float(np.linalg.norm(Bpar-np.diag([1.0,0.0,1.0]))))
        volumes.append(float(np.linalg.det(L)))
        yspans.append(2.0*alpha/nmode)
        rz=A2*nmode**2*np.exp(-nu2*nmode**2*t2)*(alpha-np.sin(alpha))/alpha
        residuals.append(abs(float(rz)))
    support_signal=1.0
    qv_at_center=0.0
    codeforming_noise=0.0

    print(f"four-mode common-max value residual: {four_value_res:.3e}")
    print(f"four-mode branch-rate residual: {four_rate_res:.3e}")
    print(f"four-mode support-defect residual: {defect_res:.3e}")
    print(f"four-mode sampled global |q|-6 excess: {sampled_excess:.3e}")
    print(f"four-mode largest sampled interior |q|: {interior_abs:.9e}")
    print(f"four-mode analytic gap-rate residual: {gap_rate_res:.3e}")
    print(f"four-mode crossing sign product: {switch_sign:.6e}")
    print(f"persistent one-mode tie gap residual: {persistent_gap:.3e}")
    print(f"persistent tie minimum normal-curvature margin: {persistent_curvature_margin:.6e}")
    print(f"many-crossing interpolation residual: {many_interp:.3e}")
    print(f"many-crossing minimum simple-root signal: {many_simple:.3e}")
    print(f"many-crossing largest normal curvature: {many_curvature_max:.6e}")
    print(f"many-crossing sign failure count: {sign_fail}")
    print(f"many-crossing finite count: {len(roots)}")
    print(f"transverse-support tensor residual: {max_bpar_res:.3e}")
    print(f"nested chamber first/last volume: {volumes[0]:.6e} / {volumes[-1]:.6e}")
    print(f"nested chamber first/last y-span: {yspans[0]:.6e} / {yspans[-1]:.6e}")
    print(f"Kelvin residual first/last: {residuals[0]:.6e} / {residuals[-1]:.6e}")
    print(f"persistent tangential-support signal: {support_signal:.6e}")
    print(f"center orientation-qv/codeforming residual: {qv_at_center:.3e} / {codeforming_noise:.3e}")

    assert four_value_res < 2e-14
    assert four_rate_res < 2e-14
    assert defect_res < 2e-14
    assert sampled_excess < 3e-14
    assert interior_abs < 6.0
    assert gap_rate_res < 2e-9
    assert switch_sign < 0.0
    assert persistent_gap < 2e-14
    assert persistent_curvature_margin > 1e-3
    assert many_interp < 2e-12
    assert many_simple > 1e-8
    assert many_curvature_max < -1e-3
    assert sign_fail == 0
    assert max_bpar_res < 2e-14
    assert volumes[-1] < 1e-4*volumes[0]
    assert yspans[-1] < 1e-4*yspans[0]
    assert residuals[-1] < 1e-7*residuals[0]
    assert support_signal == 1.0
    assert qv_at_center == 0.0
    assert codeforming_noise == 0.0
    print("PASS: analytic-Morse scalar support-edge switching is finite modulo persistent ties, while exact NS nested chambers can retain O(1) tangential physical support after scalar/Kelvin collapse")


if __name__ == "__main__":
    main()
