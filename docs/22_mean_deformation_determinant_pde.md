# The determinant of mean Cauchy deformation has an exact trilinear diffusion law

Status: **Exact reverse-age PDE identity plus a rigorous short-horizon Navier--Stokes consequence.**

The current Kelvin upstream `c1773ffa8fa5cc4bfa8fb5aa461dd4b43dbed1c1`
proves for the conditional mean Cauchy deformation

\[
\bar D(h,x,t)=\mathbb E_{x,t}D_h
\]

the exact connected equation

\[
\mathcal H_h\bar D=A^T\bar D,
\qquad
\mathcal H_h=\partial_h+\partial_t+u\cdot\nabla-\nu\Delta,
\qquad
A=\nabla u,
\]

and the full vectorized covariance source

\[
\Gamma_D^{\rm vec}
=2\nu\sum_\mu
\operatorname{vec}(\partial_\mu\bar D)
\operatorname{vec}(\partial_\mu\bar D)^T.
\]

The question here is what this literal stochastic deformation source does to the
oriented cubic volume factor `det bar D`.

---

## 1. Exact determinant PDE

Write the columns of `bar D` as

\[
\bar D=(\bar d_1,\bar d_2,\bar d_3),
\]

and set

\[
e_{\mu j}:=\partial_\mu\bar d_j.
\]

Define

\[
J_D:=\det\bar D.
\]

The first-order connected term contributes

\[
D(\det)_{\bar D}[A^T\bar D]
=(\operatorname{tr}A)J_D=0
\]

by incompressibility.  The only remaining term is the diffusion product defect.
The exact result is

\[
\boxed{
\begin{aligned}
\mathcal H_hJ_D
=-2\nu\sum_\mu\big[&
\det(e_{\mu1},e_{\mu2},\bar d_3)
+\det(e_{\mu1},\bar d_2,e_{\mu3})\\
&+\det(\bar d_1,e_{\mu2},e_{\mu3})
\big].
\end{aligned}
}
\]

Equivalently, regarding determinant as a cubic polynomial of `vec D`,

\[
\boxed{
\mathcal H_hJ_D
=-\frac12\,
\nabla^2_{\!\operatorname{vec}D}\det(\bar D)
:\Gamma_D^{\rm vec}.
}
\]

For the exterior-volume defect

\[
\delta_D:=1-J_D,
\]

this becomes

\[
\boxed{
\mathcal H_h\delta_D
=\frac12\,
\nabla^2_{\!\operatorname{vec}D}\det(\bar D)
:\Gamma_D^{\rm vec}.
}
\]

**Classification: EXACT NSE/STOCHASTIC PDE IDENTITY.**

The source is an oriented trilinear contraction of the full deformation
carré-du-champ.  It is not the positive trace of `Sigma_D`, not packet-metric energy,
and not pathwise q.v. of `D`.

---

## 2. The determinant source is not positive

`Gamma_D^vec` is positive semidefinite, but the Hessian of determinant is
indefinite.  Therefore

\[
\frac12\nabla^2\det(\bar D):\Gamma_D^{\rm vec}
\]

has no fixed sign.

This matters physically.  Brownian anchor sampling creates a positive deformation
covariance sector, but its induced **oriented volume of the conditional mean** can
move in either direction.  Treating the determinant defect as a positive covariance
reservoir would destroy the orientation information that makes the cubic work
signed.

**Classification: COUNTEREXAMPLE/NO-GO against a positive-reservoir reading.**

---

## 3. Short-horizon onset is a local gradient-of-gradient invariant

At a smooth current point the upstream mean law gives

\[
\bar D=I+hA^T+O(h^2),
\qquad
\partial_\mu\bar D
=h(\partial_\mu A)^T+O(h^2).
\]

At the identity,

\[
D^2\det(I)[E,E]
=(\operatorname{tr}E)^2-\operatorname{tr}(E^2).
\]

Since incompressibility gives

\[
\operatorname{tr}(\partial_\mu A)=0,
\]

integration of the exact determinant PDE yields

\[
\boxed{
\delta_D(h,x,t)
=-\frac{\nu h^3}{3}
\sum_\mu\operatorname{tr}\big((\partial_\mu\nabla u)^2\big)
+O(h^4).
}
\]

**Classification: RIGOROUS SHORT-HORIZON CONSEQUENCE.**

Unlike the row-Gram covariance onset

\[
\frac{2\nu}{3}h^3
\sum_\mu(\partial_\mu\nabla u)^T(\partial_\mu\nabla u),
\]

the exterior-volume onset retains the signed matrix-square trace.  The two
observables therefore see different physical geometry from the first nontrivial
order.

---

## 4. Exact periodic Navier--Stokes calibration with nonzero volume defect onset

Take the two-dimensional monochromatic streamfunction, embedded in 3D,

\[
\psi(x,y,t)
=e^{-5\nu t}\big[\cos(x+2y)+a\cos(2x+y)\big],
\]

and

\[
u=(\partial_y\psi,-\partial_x\psi,0).
\]

Both wavevectors

\[
k=(1,2),\qquad \ell=(2,1)
\]

have squared length `5`.  Hence `-Delta psi=5 psi`, scalar vorticity is
proportional to `psi`, and `u.grad omega=0`; this is an exact smooth periodic
Navier--Stokes solution with viscous decay.

At

\[
x=y=\frac{\pi}{6},
\]

both phases equal `pi/2`, so `A=grad u=0` but its spatial derivatives are nonzero.
Direct exterior algebra gives

\[
\boxed{
\sum_{\mu=x,y}
\operatorname{tr}\big((\partial_\mu A)^2\big)
=-2a e^{-10\nu t}
(k\cdot\ell)\det(k,\ell)^2
=-72a e^{-10\nu t}.
}
\]

Therefore

\[
\boxed{
\delta_D(h)
=24\nu a e^{-10\nu t}h^3+O(h^4)
}
\]

for `a>0` at that current point.

This is a genuine Navier--Stokes referee showing that the mean-deformation exterior
volume defect can turn on at the same `nu h^3` order as deformation covariance, but
through a signed oriented contraction rather than a norm.

**Classification: EXACT NSE CALIBRATION of the local coefficient; the asymptotic
conclusion is the rigorous consequence of Section 3.**

---

## 5. Owner placement

The exact chain is now

\[
\text{spatial variation of }\nabla u
\to
\Gamma_D^{\rm vec}
\to
\text{deformation dispersion}
\to
J_D=\det\bar D
\to
\text{independent-replica cubic amplitude}.
\]

The first arrow is Brownian-anchor resolution of finite-variation deformation.  The
second is full matrix covariance.  The third is an oriented exterior contraction.
The fourth is a real amplitude factor in the fixed-terminal common-deformation
sector.

None of these arrows is a license to identify `Sigma_D`, the packet metric, or a
future covariance bank with signed cubic phase.
