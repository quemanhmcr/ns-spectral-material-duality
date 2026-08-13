# Pressure is gauge for divergence-free work and closed circulation, but its Hessian is physical strain curvature

Status: **EXACT NSE PRESSURE-TYPING LADDER / MATERIAL-METRIC CONSEQUENCE**.

Calling pressure simply "gauge" is too coarse.  Navier--Stokes uses pressure differently at different physical readouts.  The exact PDE tells us where it disappears and where it returns.

## 1. Divergence-free Eulerian work kills the pressure gradient

For any periodic/decaying divergence-free probe `w`,

\[
\boxed{\langle w,\nabla p\rangle=0.}
\]

This is the Eulerian reason Leray projection can remove pressure from Wang's divergence-free energy/transfer pairing.  Pressure gradient performs no net `L^2` work on a solenoidal role.

## 2. Closed Kelvin circulation kills the same exact gradient

For any closed loop `C`,

\[
\boxed{\oint_C\nabla p\cdot d\ell=0.}
\]

Thus the pressure force is also absent from the closed Kelvin circulation law.  Leray annihilation and closed-loop annihilation are two representations of the same exact-gradient fact.

## 3. Curl/vorticity also removes pressure at first derivative level

Taking curl of NSE gives

\[
D_t\omega=A\omega+\nu\Delta\omega,
\]

with no pressure term because

\[
\nabla\times\nabla p=0.
\]

Together with material area transport this yields the pressure-free local vorticity-flux law of Theorem DO.

## 4. But the velocity-gradient equation contains the pressure Hessian

Differentiate the actual NSE:

\[
\boxed{
D_tA+A^2=-\nabla^2p+\nu\Delta A,
\qquad A=\nabla u.
}
\]

Write `A=S+Omega`.  Since

\[
\operatorname{sym}A^2=S^2+\Omega^2,
\]

the symmetric equation is

\[
\boxed{
D_tS+S^2+\Omega^2
=-\nabla^2p+\nu\Delta S.
}
\]

Pressure Hessian is therefore a real source/constraint in local strain dynamics even though pressure gradient did no divergence-free energy work.

The skew equation is

\[
\boxed{
D_t\Omega+S\Omega+\Omega S=\nu\Delta\Omega,
}
\]

with no direct pressure Hessian because `Hess p` is symmetric.

## 5. Pressure is the incompressibility curvature constraint

Taking trace of the gradient equation and using `tr A=0` gives

\[
\boxed{
\Delta p=-\operatorname{tr}(A^2)
=-|S|_F^2+|\Omega|_F^2
=-|S|_F^2+\frac12|\omega|^2.
}
\]

Thus pressure redistributes the local deformation needed to preserve incompressible volume.  It is not a kinetic-energy source, but it is not absent from metric deformation.

## 6. Objective strain and material metric acceleration

Define

\[
\mathring S=D_tS+S\Omega-\Omega S.
\]

Then

\[
\boxed{
\mathring S
=-S^2-\Omega^2-\nabla^2p+\nu\Delta S
+(S\Omega-\Omega S).
}
\]

For the material metric `M` and inverse-transpose frame `H`,

\[
\frac12H\ddot MH^T=\mathring S+2S^2,
\]

so

\[
\boxed{
\frac12H\ddot MH^T
=S^2-\Omega^2-\nabla^2p+\nu\Delta S
+(S\Omega-\Omega S).
}
\]

Pressure Hessian is therefore literally a material metric-acceleration face.

## 7. Two exact affine Navier--Stokes calibrations

### Pure strain

Let

\[
u=Ax,\qquad A=S=\operatorname{diag}(a,-a,0).
\]

With

\[
p=-\frac12x^TA^2x,
\]

one has `Delta u=0`, `A_t=0`, and

\[
A^2=-\nabla^2p.
\]

The flow is an exact smooth affine NSE solution.  Pressure Hessian exactly balances strain self-curvature.

### Rigid rotation

Let

\[
A=\Omega=
\begin{pmatrix}
0&-r&0\\r&0&0\\0&0&0
\end{pmatrix},
\qquad u=Ax.
\]

With

\[
p=\frac12r^2(x^2+y^2),
\]

again `Delta u=0` and

\[
\Omega^2=-\nabla^2p.
\]

Here `S=0`, but pressure Hessian balances centrifugal connection curvature.

## 8. Cross-programme meaning

- Wang energy/edge work may legitimately quotient pressure through Leray.
- Kelvin closed circulation may legitimately quotient the pressure gradient.
- Wang objective-strain/material metric modules and Kelvin finite-shape/metric dynamics must retain the pressure Hessian when differentiating deformation.

Therefore pressure has a **typed degree-dependent role**, not a universal "zero owner" label.
