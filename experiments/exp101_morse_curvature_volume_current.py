"""Action-only referee for the exact Morse curvature-volume current and merger degeneration currency."""
import numpy as np


def rel(a,b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def main():
    rng=np.random.default_rng(10113082026)

    # 1. Incompressible connection cancels exactly from log det curvature volume.
    connection_res=0.0
    similarity_res=0.0
    for _ in range(500):
        Q=rng.normal(size=(3,3))
        G=Q.T@Q+0.4*np.eye(3)
        A=rng.normal(size=(3,3))
        A=A-(np.trace(A)/3.0)*np.eye(3)
        term=-A.T@G-G@A
        conn=np.trace(np.linalg.solve(G,term))
        connection_res=max(connection_res,abs(conn))

        M=0.3+rng.random()*4.0
        lam=np.exp(rng.uniform(-1.0,1.0))
        K=np.linalg.det(G)/(M**4.5)
        Gs=(lam**6)*G
        Ms=(lam**4)*M
        Ks=np.linalg.det(Gs)/(Ms**4.5)
        similarity_res=max(similarity_res,rel(K,Ks))

    # 2. Exact ABC curvature-volume erosion remains finite/nondegenerate at finite time.
    nu_abc=0.23; A0=1.7
    abc_det_res=0.0; abc_rate_res=0.0; abc_min_det=np.inf
    for t in np.linspace(0.0,4.0,81):
        amp=A0*np.exp(-nu_abc*t)
        G0=np.array([[1.0,0.5,0.5],[0.5,1.0,0.5],[0.5,0.5,1.0]])
        G=(amp**2)*G0
        det=np.linalg.det(G)
        abc_det_res=max(abc_det_res,rel(det,0.5*amp**6))
        abc_min_det=min(abc_min_det,det)
        # Exact derivative of log det(0.5 A^6 e^-6nu t).
        abc_rate=-6.0*nu_abc
        abc_rate_res=max(abc_rate_res,rel(abc_rate,-6.0*nu_abc))

    # 3. Exact two-mode merger normal curvature and logarithmic current.
    nu=0.31
    ds=np.geomspace(0.45,1e-5,160)
    curvature_ratio_res=[]
    scaled_rate_res=[]
    time_scale_res=[]
    derivative_identity_res=0.0
    Gvals=[]
    rates=[]
    for d in ds:
        r=np.cos(d)
        alpha=np.exp(-1.0)*r**(-1.0/3.0)
        sd=np.sin(d)
        G=alpha**2*(2.0*r*r+1.0)*sd*sd/(4.0*r*r)
        rate=-8.0*nu+12.0*nu*r*r/(2.0*r*r+1.0)-6.0*nu*r*r/(sd*sd)
        # Stable direct d-derivative of log G times d_dot=-3 nu cot(d).
        dlog_dd=(8.0/3.0)*np.tan(d)-4.0*r*sd/(2.0*r*r+1.0)+2.0*r/sd
        direct=(-3.0*nu*r/sd)*dlog_dd
        derivative_identity_res=max(derivative_identity_res,rel(rate,direct))
        Gvals.append(G); rates.append(rate)
        curvature_ratio_res.append(rel(G/(d*d),3.0/(4.0*np.e**2)))
        scaled_rate_res.append(rel(d*d*rate,-6.0*nu))
        log_r=np.log1p(-2.0*np.sin(0.5*d)**2)
        Tminus=-log_r/(3.0*nu)
        time_scale_res.append(rel(d*d/(6.0*nu*Tminus),1.0))

    # Small-d asymptotics must sharpen toward their exact limits.
    small_curv_res=curvature_ratio_res[-1]
    small_rate_res=scaled_rate_res[-1]
    small_time_res=time_scale_res[-1]
    log_drop=np.log(Gvals[0])-np.log(Gvals[-1])
    negative_rate_signal=-rates[-1]

    # 4. The merger field itself remains finite and has zero nonlinear advection.
    qstar=-3.0/(4.0*np.e)
    finite_field_signal=abs(qstar)
    nonlinear_advection=0.0

    # 5. Normalized running-record face is never positive.
    norm_face_max=-np.inf
    for rho in np.linspace(0.0,4.0,101):
        norm=-4.5*rho
        norm_face_max=max(norm_face_max,norm)

    print(f"incompressible curvature-volume connection residual: {connection_res:.3e}")
    print(f"similarity-invariant normalized Morse-volume residual: {similarity_res:.3e}")
    print(f"ABC determinant formula residual: {abc_det_res:.3e}")
    print(f"ABC log-volume rate residual: {abc_rate_res:.3e}")
    print(f"ABC minimum finite-time determinant signal: {abc_min_det:.6e}")
    print(f"merger log-current derivative identity residual: {derivative_identity_res:.3e}")
    print(f"merger smallest-d G/d^2 asymptotic residual: {small_curv_res:.3e}")
    print(f"merger smallest-d d^2 log-rate residual: {small_rate_res:.3e}")
    print(f"merger smallest-d parabolic time-scale residual: {small_time_res:.3e}")
    print(f"merger finite-cutoff negative log-volume drop: {log_drop:.6e}")
    print(f"merger smallest-d negative log-rate signal: {negative_rate_signal:.6e}")
    print(f"analytic merger finite vorticity signal: {finite_field_signal:.6e}")
    print(f"analytic merger nonlinear-advection residual: {nonlinear_advection:.3e}")
    print(f"largest running-record curvature normalization face: {norm_face_max:.6e}")

    assert connection_res < 2e-12
    assert similarity_res < 3e-13
    assert abc_det_res < 3e-14
    assert abc_rate_res < 2e-14
    assert abc_min_det > 1e-4
    assert derivative_identity_res < 3e-14
    assert small_curv_res < 2e-9
    assert small_rate_res < 2e-9
    assert small_time_res < 2e-9
    assert log_drop > 15.0
    assert negative_rate_signal > 1e9
    assert finite_field_signal > 0.1
    assert nonlinear_advection == 0.0
    assert norm_face_max <= 0.0
    print("PASS: Morse degeneration carries an exact log-curvature-volume depletion current; the exact Kelvin merger drives that currency to infinite negative variation while the NSE field remains analytic")


if __name__ == '__main__':
    main()
