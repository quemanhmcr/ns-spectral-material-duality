"""Action-only referee for the exact enstrophy record-owner and first-hit laws."""
import numpy as np


def rel(a, b):
    return abs(a-b)/(1.0+abs(a)+abs(b))


def main():
    # ------------------------------------------------------------
    # 1. Exact periodic heat shear: no stretching, record decays.
    # ------------------------------------------------------------
    nu = 0.37
    amp = 1.41
    k = 3.0
    heat_res = 0.0
    owner_res = 0.0
    max_record_rate = -np.inf
    curvature_loss_min = np.inf
    for t in np.linspace(0.0, 1.4, 31):
        decay = np.exp(-nu*k*k*t)
        for y in np.linspace(-np.pi, np.pi, 101):
            U = amp*decay*np.sin(k*y)
            Ut = -nu*k*k*U
            Uyy = -k*k*U
            heat_res = max(heat_res, rel(Ut, nu*Uyy))
        C = amp*k*decay
        M = 0.5*C*C
        Mdot = -2.0*nu*k*k*M
        stretching = 0.0
        gradomega2 = 0.0
        deltae = -(C*C*k*k)
        defect = nu*(gradomega2-deltae)
        owner_res = max(owner_res, rel(Mdot, stretching-defect))
        max_record_rate = max(max_record_rate, Mdot)
        curvature_loss_min = min(curvature_loss_min, defect)

    # ------------------------------------------------------------
    # 2. Exact affine strain-spin NSE: pure stretching record growth.
    # ------------------------------------------------------------
    a = 0.23
    Om0 = 0.81
    matrix_ns_res = 0.0
    affine_owner_res = 0.0
    min_stretch_margin = np.inf
    for t in np.linspace(0.0, 2.0, 41):
        Om = Om0*np.exp(2.0*a*t)
        Omdot = 2.0*a*Om
        A = np.array([[-a,-Om,0.0],[Om,-a,0.0],[0.0,0.0,2.0*a]])
        Ap = np.array([[0.0,-Omdot,0.0],[Omdot,0.0,0.0],[0.0,0.0,0.0]])
        B = Ap + A@A
        target = np.diag([a*a-Om*Om, a*a-Om*Om, 4.0*a*a])
        matrix_ns_res = max(matrix_ns_res, np.linalg.norm(B-target)/(1.0+np.linalg.norm(B)+np.linalg.norm(target)))
        omega2 = (2.0*Om)**2
        M = 0.5*omega2
        Mdot = 4.0*a*M
        stretch = 2.0*a*omega2
        defect = 0.0
        affine_owner_res = max(affine_owner_res, rel(Mdot, stretch-defect))
        min_stretch_margin = min(min_stretch_margin, stretch-defect)

    # Exact first-hit formula in the affine calibration.
    M0 = 2.0*Om0*Om0
    L = 7.3*M0
    tau = np.log(L/M0)/(4.0*a)
    Om_tau = Om0*np.exp(2.0*a*tau)
    M_tau = 2.0*Om_tau*Om_tau
    first_hit_res = rel(M_tau, L)
    hit_stretch = 8.0*a*Om_tau*Om_tau
    hit_owner_res = rel(hit_stretch, 4.0*a*L)

    # ------------------------------------------------------------
    # 3. Exact three-mode periodic ranking crossing: selector switches
    #    while both candidate enstrophy rates are negative.
    # ------------------------------------------------------------
    tstar = 1.0/nu
    def shear_jets(y, t):
        a1 = np.exp(-nu*t)
        a2 = np.exp(3.0)*np.exp(-4.0*nu*t)
        a3 = np.exp(8.0)*np.exp(-9.0*nu*t)
        Uy = -a1*np.cos(y)-3.0*a2*np.cos(2.0*y)+a3*np.cos(3.0*y)
        Uyy = a1*np.sin(y)+6.0*a2*np.sin(2.0*y)-3.0*a3*np.sin(3.0*y)
        Uyyy = a1*np.cos(y)+12.0*a2*np.cos(2.0*y)-9.0*a3*np.cos(3.0*y)
        w = -Uy
        wy = -Uyy
        wyy = -Uyyy
        e = 0.5*w*w
        eyy = wy*wy+w*wyy
        return w, wy, e, eyy

    w0, wy0, e0, eyy0 = shear_jets(0.0, tstar)
    wp, wyp, ep, eyyp = shear_jets(np.pi, tstar)
    rate0 = -nu*wy0*wy0 + nu*eyy0
    ratep = -nu*wyp*wyp + nu*eyyp
    tie_res = rel(e0, ep)
    both_decay_signal = max(rate0, ratep)
    gap_rate = rate0-ratep

    dt = 0.02/nu
    em0 = shear_jets(0.0, tstar-dt)[2]
    emp = shear_jets(np.pi, tstar-dt)[2]
    ep0 = shear_jets(0.0, tstar+dt)[2]
    epp = shear_jets(np.pi, tstar+dt)[2]
    pre_gap = em0-emp
    post_gap = ep0-epp

    # ------------------------------------------------------------
    # 4. Discrete running-record audit: label oscillations below an old
    #    physical record cannot increment the record clock.
    # ------------------------------------------------------------
    physical_values = np.array([1.0, 0.92, 0.95, 0.91, 0.99, 0.88, 1.0, 0.97])
    labels = np.array([0,1,0,1,0,1,0,1])
    running = np.maximum.accumulate(physical_values)
    record_increment = running[-1]-running[0]
    selector_switches = int(np.sum(labels[1:] != labels[:-1]))

    print(f"heat-shear PDE residual: {heat_res:.3e}")
    print(f"heat-shear active-record owner residual: {owner_res:.3e}")
    print(f"heat-shear largest record rate: {max_record_rate:.6e}")
    print(f"heat-shear minimum curvature/viscous defect: {curvature_loss_min:.6e}")
    print(f"affine strain-spin NSE matrix residual: {matrix_ns_res:.3e}")
    print(f"affine pure-stretching owner residual: {affine_owner_res:.3e}")
    print(f"affine minimum positive owner margin: {min_stretch_margin:.6e}")
    print(f"affine exact first-hit residual: {first_hit_res:.3e}")
    print(f"affine first-hit stretching formula residual: {hit_owner_res:.3e}")
    print(f"ranking-crossing active tie residual: {tie_res:.3e}")
    print(f"ranking-crossing largest candidate rate: {both_decay_signal:.6e}")
    print(f"ranking-crossing gap-rate signal: {gap_rate:.6e}")
    print(f"ranking-crossing pre/post gaps: {pre_gap:.6e} / {post_gap:.6e}")
    print(f"closed below-record selector switch count: {selector_switches}")
    print(f"closed below-record physical record increment: {record_increment:.3e}")

    assert heat_res < 2e-14
    assert owner_res < 2e-14
    assert max_record_rate < 0.0
    assert curvature_loss_min > 0.0
    assert matrix_ns_res < 2e-14
    assert affine_owner_res < 2e-14
    assert min_stretch_margin > 0.0
    assert first_hit_res < 2e-14
    assert hit_owner_res < 2e-14
    assert tie_res < 2e-14
    assert both_decay_signal < 0.0
    assert gap_rate > 0.0
    assert pre_gap < 0.0 and post_gap > 0.0
    assert selector_switches == 7
    assert abs(record_increment) < 2e-14
    print("PASS: the enstrophy running record has an intrinsic stretching owner, while ranking/selector activity and viscous curvature decay do not mint record-generation depth")


if __name__ == "__main__":
    main()
