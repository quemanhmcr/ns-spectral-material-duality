# Local peak enstrophy growth is directional material-metric work versus Kelvin q.v. and curvature flux

Status: **Exact Navier--Stokes/material-metric identity plus a scoped exact affine calibration no-go.**

The Kelvin upstream retains one physically meaningful local necessary condition after
excluding many naive raw first-bad thresholds.  At a spatial local maximum of
enstrophy, positive material growth requires

\[
\omega\cdot S\omega>\nu|\nabla\omega|^2.
\]

The third-repo material dictionary now identifies exactly what the left side is.
This makes the gate geometric rather than norm-based, while also showing why it is
not by itself a restart/continuation event.

---

## 1. Exact local enstrophy ledger

Let

\[
e=\frac12|\omega|^2,
\qquad
S=\operatorname{sym}\nabla u.
\]

The vorticity equation gives

\[
\boxed{
D_t e
=\omega\cdot S\omega
+\nu\Delta e
-\nu|\nabla\omega|^2,
\qquad
D_t=\partial_t+u\cdot\nabla.
}
\]

No estimate has been used.  The three non-transport terms are respectively

1. physical vortex-stretching/strain work;
2. signed spatial curvature/viscous flux density;
3. bulk viscous vorticity-gradient payment.

**Classification: EXACT NSE/PDE IDENTITY.**

---

## 2. Stretching is exactly directional material-metric velocity

For the material area frame `H` and inverse area metric `M` from the common
deformation dictionary, the exact objective identity is

\[
\boxed{H\dot M H^T=2S}
\]

on a fixed physical material scale.  Define the material vorticity covector

\[
\Phi=H^T\omega.
\]

Then

\[
\boxed{
\omega\cdot S\omega
=\frac12\Phi^T\dot M\Phi.
}
\]

Hence the enstrophy equation becomes

\[
\boxed{
D_t e
=\frac12\Phi^T\dot M\Phi
+\nu\Delta e
-\nu|\nabla\omega|^2.
}
\]

**Classification: EXACT NSE/MATERIAL-METRIC IDENTITY.**

The producer is not a norm of `S`; it is the actual directional metric work along
the physical vorticity covector.

---

## 3. Kelvin q.v. is the competing bulk payment

For an orientation-complete orthonormal microframe, the Kelvin upstream identifies

\[
\boxed{
\frac12\sum_{j=1}^3\gamma_{\rm dens}(n_j)
=\nu|\nabla\omega|^2.
}
\]

Therefore

\[
\boxed{
D_t e
=\frac12\Phi^T\dot M\Phi
-\frac12\sum_j\gamma_{\rm dens}(n_j)
+\nu\Delta e.
}
\]

This is the same physical ledger written in material geometry and Kelvin stochastic
currency:

\[
\boxed{
\text{directional strain/metric work}
-\text{Kelvin bulk q.v.}
+\text{signed spatial curvature flux}.
}
\]

**Classification: EXACT CROSS-DICTIONARY IDENTITY.**

No covariance bank has been identified with the stretching term; they remain
different physical mechanisms.

---

## 4. The local-maximum growth gate is a directional metric-versus-q.v. gate

At a spatial local maximum of `e`,

\[
\Delta e\le0.
\]

Thus

\[
D_t e>0
\]

implies

\[
\boxed{
\frac12\Phi^T\dot M\Phi
>
\nu|\nabla\omega|^2
=
\frac12\sum_j\gamma_{\rm dens}(n_j).
}
\]

**Classification: RIGOROUS NECESSARY CONSEQUENCE.**

The converse is not forced: the negative curvature term `nu Delta e` may still
outweigh the positive margin.

For incompressible material deformation at fixed reference scale,

\[
\det F=1
\]

and the corresponding material metric determinant is constant.  Hence positive
vorticity-direction metric work is anisotropic shape redistribution, not isotropic
volume inflation.

**Classification: EXACT INCOMPRESSIBLE GEOMETRIC CONSEQUENCE.**

---

## 5. Exact affine-vortex Navier--Stokes referee

Use the exact smooth affine Navier--Stokes solution already audited upstream:

\[
r(t)=r_0e^{2at},
\qquad
A(t)=
\begin{pmatrix}
-a&-r(t)&0\\
r(t)&-a&0\\
0&0&2a
\end{pmatrix},
\qquad
u(x,t)=A(t)x,
\]

with quadratic pressure Hessian

\[
\nabla^2p=-(A'+A^2).
\]

It has

\[
\omega=(0,0,2r_0e^{2at}),
\qquad
S=\operatorname{diag}(-a,-a,2a),
\]

so spatially

\[
\nabla\omega=0,
\qquad
\Delta e=0.
\]

Enstrophy is constant in space, so every point is a non-strict spatial local
maximum and minimum.  For `a>0`,

\[
\boxed{
\mathfrak G
:=\omega\cdot S\omega-\nu|\nabla\omega|^2
=8ar_0^2e^{4at}>0,
}
\]

and in fact

\[
\boxed{D_t e=\mathfrak G.}
\]

The material-metric form gives the same value:

\[
\boxed{
\frac12\Phi^T\dot M\Phi
=8ar_0^2e^{4at}.
}
\]

**Classification: EXACT NAVIER--STOKES CALIBRATION.**

---

## 6. Scoped no-go for finite growth-margin thresholds

For every finite threshold `Theta>0`, the exact affine family can make

\[
\mathfrak G>\Theta
\]

at a non-strict spatial local enstrophy maximum while the affine Navier--Stokes
solution remains smooth at every finite time.  One may achieve this either by
choosing `r_0` large at the initial time or by evolving to a sufficiently large but
finite time.

Therefore

\[
\boxed{
\mathfrak G>\Theta
\quad\text{at a non-strict local enstrophy maximum}
}
\]

cannot, by itself, be a universal finite-time continuation-failure flag on any
admissible solution class that contains these exact affine flows.

**Classification: COUNTEREXAMPLE/NO-GO, with explicit scope.**

This does not exclude a theorem posed on a narrower global class such as a periodic
or finite-energy class that excludes affine flows, nor does it exclude a
nondegenerate/strict-maximum condition.  It shows that the local PDE mechanism
alone is not a singularity oracle.

---

## 7. Relation to cubic phase/work

The peak-growth gate is quadratic/directional:

\[
\frac12\Phi^T\dot M\Phi
\quad\text{versus}\quad
\frac12\sum_j\gamma_j.
\]

The signed spectral interaction is cubic/oriented:

\[
\kappa\operatorname{Re}\mathcal Z_H.
\]

The material metric velocity enters both physical stories, but in different jobs:

- in the local enstrophy gate it is actual vorticity-direction stretching;
- in the spectral bridge it changes geometry/polarization and the real edge
  coefficient, while the missing signed interaction information remains the
  oriented complex cubic.

Thus a future first-bad definition may legitimately use the local peak-growth gate
as one physical event sector, but it may not silently identify that gate with
favorable/backscatter cubic phase or with a covariance reservoir.

**Classification: EXACT TYPE SEPARATION; first-bad definition remains OPEN BRIDGE.**
