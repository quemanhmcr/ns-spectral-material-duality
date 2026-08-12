# Oriented material-flux 3-form and signed helical edge work

Status: **Exact algebraic bridge candidate; CI stress-tested independently from the upstream repositories.**

## 1. Start from the physical NSE interaction

For incompressible Navier--Stokes,

\[
\partial_tu=P(u\times\omega)+\nu\Delta u,
\qquad \omega=\nabla\times u.
\]

Take one resonant Fourier edge `k_1+k_2=q`.  Its unordered parent source is

\[
F_q=P(u_1\times\omega_2+u_2\times\omega_1),
\]

and the actual signed child-energy work is

\[
T_e=2\operatorname{Re}\langle u_q,F_q\rangle.
\]

Because `u_q` is transverse to `q`, the Leray projector disappears in this pairing.  No norm or capacity is substituted for this work.

## 2. Pass to material vorticity-flux coordinates

Let `H` be any common invertible oriented area frame and define

\[
\Phi_j=H^T\omega_j.
\]

For a helical mode,

\[
\omega_j=s_j|k_j|u_j,
\qquad
u_j:=|k_j|,
\]

so

\[
u_j=s_j\nu_j^{-1}H^{-T}\Phi_j.
\]

The scalar triple-product transformation

\[
(H^{-T}a)\cdot[(H^{-T}b)\times(H^{-T}c)]
=\frac1{\det H}a\cdot(b\times c)
\]

gives the exact identity

\[
\boxed{
T_e=
2\frac{s_q}{\nu_q}
\left(\frac{s_1}{\nu_1}-\frac{s_2}{\nu_2}\right)
\frac1{\det H}
\operatorname{Re}
\big[\overline{\Phi_q}\cdot(\Phi_1\times\Phi_2)\big].
}
\]

Define the oriented material-flux 3-form

\[
\boxed{
\mathcal C_H(\Phi_1,\Phi_2,\Phi_q)
:=\frac1{\det H}
\operatorname{Re}
\big[\overline{\Phi_q}\cdot(\Phi_1\times\Phi_2)\big].
}
\]

Then the signed physical work is a frequency/helicity coefficient times `C_H`.

## 3. Why this is a genuinely material invariant

Under a passive packet reparameterization

\[
H\mapsto HL,
\qquad
\Phi_j\mapsto L^T\Phi_j,
\]

the numerator picks up `det L` while `det(HL)` picks up the same factor.  Hence

\[
\boxed{\mathcal C_{HL}(L^T\Phi_1,L^T\Phi_2,L^T\Phi_q)=\mathcal C_H.}
\]

So rotation, dilation and shear of the observer packet do not create signed work.

For a physical spatial translation by `a`, the Fourier vectors transform as

\[
\omega_j\mapsto e^{ik_j\cdot a}\omega_j.
\]

Since `q=k_1+k_2`, the phase in the resonant cubic product cancels exactly.  The 3-form is therefore translation invariant as required of physical edge work.

## 4. Resolution of the metric-phase no-go

The previous no-go theorem remains correct: `M= (H^TH)^{-1}` and every second-order covariance built only from magnitudes cannot determine the sign of `T_e`.  The missing information is not another scalar function of the metric.  It is genuinely **third-order oriented flux information**.

Changing only the child phase by `pi` leaves metric, frequencies, helicities and modal magnitudes unchanged but sends

\[
\mathcal C_H\mapsto-\mathcal C_H,
\qquad T_e\mapsto-T_e.
\]

Thus the natural material hierarchy is now

\[
\text{metric }M \quad\text{(deformation)},
\]

\[
\text{covariance / q.v. }C \quad\text{(second-order stochastic information)},
\]

\[
\boxed{\text{oriented flux 3-form }\mathcal C_H\quad\text{(signed nonlinear interaction)}}.
\]

These objects must not be collapsed into one reservoir.

## 5. Dynamic frontier

For incompressible material evolution `det H` is constant.  If three flux roles obey

\[
D_t\Phi_j=R_j,
\]

then ordinary Leibniz differentiation yields

\[
D_t\mathcal C_H
=\frac1{\det H}\operatorname{Re}\Big[
\overline{R_q}\cdot(\Phi_1\times\Phi_2)
+\overline{\Phi_q}\cdot(R_1\times\Phi_2+\Phi_1\times R_2)
\Big].
\]

There is no separate passive metric-production term.  The next PDE problem is therefore to derive the literal `R_j` supplied by localized Navier--Stokes roles and classify each contribution before estimating it: common transport, strain/connection, viscosity, pressure/gauge, SGS/cross-role forcing, interface flux, and true nonlinear regeneration.

That dynamic theorem is **not yet proved here**.
