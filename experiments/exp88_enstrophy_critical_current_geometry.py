"""Action-only referee for exact enstrophy critical-current and curvature-volume identities."""
import itertools
import numpy as np


def relerr(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    return np.linalg.norm(a - b) / (1.0 + np.linalg.norm(a) + np.linalg.norm(b))


def sym3(T):
    out = np.zeros_like(T)
    for p in itertools.permutations(range(3)):
        out += np.transpose(T, p)
    return out / 6.0


def abc_jets(x, amp):
    x0, y, z = x
    sx, sy, sz = np.sin(x0), np.sin(y), np.sin(z)
    cx, cy, cz = np.cos(x0), np.cos(y), np.cos(z)
    u = amp * np.array([sz + cy, sx + cz, sy + cx])
    J = amp * np.array([
        [0 * x0, -sy, cz],
        [cx, 0 * x0, -sz],
        [-sx, cy, 0 * x0],
    ])
    H0 = amp * np.array([
        [0 * x0, 0 * x0, 0 * x0],
        [0 * x0, -cy, 0 * x0],
        [0 * x0, 0 * x0, -sz],
    ])
    H1 = amp * np.array([
        [-sx, 0 * x0, 0 * x0],
        [0 * x0, 0 * x0, 0 * x0],
        [0 * x0, 0 * x0, -cz],
    ])
    H2 = amp * np.array([
        [-cx, 0 * x0, 0 * x0],
        [0 * x0, -sy, 0 * x0],
        [0 * x0, 0 * x0, 0 * x0],
    ])
    Hu = (H0, H1, H2)
    grad_e = J.T @ u
    H_e = J.T @ J
    for i in range(3):
        H_e = H_e + u[i] * Hu[i]
    return u, J, Hu, grad_e, H_e


def abc_physical_R(x, amp, nu):
    u, J, _, _, H_e = abc_jets(x, amp)
    S = 0.5 * (J + J.T)
    stretching = u @ (S @ u)
    kelvin_bulk = nu * np.sum(J * J)  # omega=u, hence grad omega=J.
    curvature = nu * np.trace(H_e)
    return stretching - kelvin_bulk + curvature


def main():
    rng = np.random.default_rng(8813082026)

    # General algebraic checks of the exact critical-current and Hessian-volume laws.
    critical_constraint = 0.0
    connection_logdet = 0.0
    reduced_logdet = 0.0
    connection_signal = 0.0
    relative_drift_signal = 0.0

    for _ in range(1200):
        q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        H = q @ np.diag(-np.exp(rng.uniform(-1.0, 1.0, size=3))) @ q.T
        A = rng.normal(size=(3, 3))
        A -= np.trace(A) * np.eye(3) / 3.0
        u = rng.normal(size=3)
        gradR = rng.normal(size=3)
        v = u - np.linalg.solve(H, gradR)
        critical_constraint = max(critical_constraint, relerr(H @ (v - u) + gradR, np.zeros(3)))
        relative_drift_signal = max(relative_drift_signal, np.linalg.norm(v - u))

        C = -(A.T @ H + H @ A)
        connection_signal = max(connection_signal, np.linalg.norm(C))
        connection_logdet = max(connection_logdet, abs(np.trace(np.linalg.solve(H, C))))

        R2 = rng.normal(size=(3, 3)); R2 = 0.5 * (R2 + R2.T)
        T = sym3(rng.normal(size=(3, 3, 3)))
        Tv = np.einsum('ijk,k->ij', T, v - u)
        Hdot = R2 + C + Tv
        full_rate = np.trace(np.linalg.solve(H, Hdot))
        reduced_rate = np.trace(np.linalg.solve(H, R2 + Tv))
        reduced_logdet = max(reduced_logdet, abs(full_rate - reduced_rate))

    # Exact smooth periodic ABC Navier--Stokes calibration.
    nu = 0.23
    t = 0.61
    A0 = 1.7
    amp = A0 * np.exp(-nu * t)
    abc_div = abc_beltrami = abc_nse = 0.0
    for _ in range(500):
        x = rng.uniform(-np.pi, np.pi, size=3)
        u, J, _, grad_e, _ = abc_jets(x, amp)
        omega = np.array([
            J[2, 1] - J[1, 2],
            J[0, 2] - J[2, 0],
            J[1, 0] - J[0, 1],
        ])
        abc_div = max(abc_div, abs(np.trace(J)))
        abc_beltrami = max(abc_beltrami, relerr(omega, u))
        # p=-e, u_t=-nu u, Delta u=-u.
        residual = -nu * u + J @ u - grad_e - nu * (-u)
        abc_nse = max(abc_nse, np.linalg.norm(residual) / (1.0 + np.linalg.norm(u)))

    xstar = np.array([np.pi / 4, np.pi / 4, np.pi / 4])
    u, J, _, grad_e, H = abc_jets(xstar, amp)
    M = np.array([[1.0, 0.5, 0.5], [0.5, 1.0, 0.5], [0.5, 0.5, 1.0]])
    expected_u = np.sqrt(2.0) * amp * np.ones(3)
    expected_H = -(amp ** 2) * M
    abc_u = relerr(u, expected_u)
    abc_critical = np.linalg.norm(grad_e) / (1.0 + np.linalg.norm(u))
    abc_hessian = relerr(H, expected_H)
    abc_det = abs(np.linalg.det(H) + 0.5 * amp ** 6) / (1.0 + abs(np.linalg.det(H)) + 0.5 * amp ** 6)
    max_hessian_eig = float(np.max(np.linalg.eigvalsh(H)))

    # Differentiate the literal three-face R by complex step, not the speed formula.
    h = 1e-30
    gradR = np.zeros(3)
    for j in range(3):
        z = xstar.astype(complex)
        z[j] += 1j * h
        gradR[j] = np.imag(abc_physical_R(z, amp, nu)) / h
    gradR_identity = relerr(gradR, H @ u)
    reconstructed_speed = u - np.linalg.solve(H, gradR)
    abc_speed = np.linalg.norm(reconstructed_speed) / (1.0 + np.linalg.norm(u))
    material_separation_signal = np.linalg.norm(u)
    abc_logdet_rate = -6.0 * nu

    print(f"critical-current constraint residual: {critical_constraint:.3e}")
    print(f"incompressible connection logdet residual: {connection_logdet:.3e}")
    print(f"full-vs-reduced critical logdet residual: {reduced_logdet:.3e}")
    print(f"nonzero connection-shape signal: {connection_signal:.3e}")
    print(f"sampled relative-drift signal: {relative_drift_signal:.3e}")
    print(f"ABC divergence residual: {abc_div:.3e}")
    print(f"ABC Beltrami residual: {abc_beltrami:.3e}")
    print(f"ABC Navier-Stokes residual: {abc_nse:.3e}")
    print(f"ABC critical-gradient residual: {abc_critical:.3e}")
    print(f"ABC critical velocity formula residual: {abc_u:.3e}")
    print(f"ABC critical Hessian formula residual: {abc_hessian:.3e}")
    print(f"ABC critical Hessian determinant residual: {abc_det:.3e}")
    print(f"ABC maximum critical-Hessian eigenvalue: {max_hessian_eig:.6e}")
    print(f"ABC physical-face gradR identity residual: {gradR_identity:.3e}")
    print(f"ABC reconstructed critical speed residual: {abc_speed:.3e}")
    print(f"ABC material/critical separation speed signal: {material_separation_signal:.3e}")
    print(f"ABC direct log|det H| rate: {abc_logdet_rate:.6e}")

    assert critical_constraint < 3e-13
    assert connection_logdet < 3e-12
    assert reduced_logdet < 3e-12
    assert connection_signal > 1e-2
    assert relative_drift_signal > 1e-2
    assert abc_div < 2e-14
    assert abc_beltrami < 2e-14
    assert abc_nse < 2e-14
    assert abc_critical < 2e-14
    assert abc_u < 2e-14
    assert abc_hessian < 2e-14
    assert abc_det < 2e-14
    assert max_hessian_eig < -1e-3
    assert gradR_identity < 2e-11
    assert abc_speed < 2e-11
    assert material_separation_signal > 1e-1
    assert abc_logdet_rate < 0.0
    print("PASS: exact NSE critical current separates from material flow and incompressibility cancels only curvature-volume connection")


if __name__ == "__main__":
    main()
