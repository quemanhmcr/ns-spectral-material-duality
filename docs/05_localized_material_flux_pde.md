# Localized material-flux PDE: exact source classification before estimates

Status: **Exact smooth Navier--Stokes identity.**  The CI experiment evaluates it on a random smooth real periodic divergence-free state using the instantaneous untruncated NSE vorticity RHS.

## 1. The full material flux law

Let

\[
A=\nabla u,
\qquad
D_t\omega=A\omega+\nu\Delta\omega,
\qquad
D_tH=-A^TH.
\]

For the full flux `Phi=H^T omega`, Nanson cancellation gives

\[
D_t\Phi=\nu H^T\Delta\omega.
\]

Pressure is absent because curl removed the exact gauge sector.  Common material stretching is absent because the material area frame carries precisely the dual deformation.

## 2. What localization really reintroduces

Let `Q(t)` be any linear spatial role/localization operator for which the expressions below are defined, and set

\[
\Phi_Q=H^TQ\omega.
\]

Use the exact operator product rule

\[
D_t(Q\omega)
=Q D_t\omega
+\big(\partial_tQ+[u\cdot\nabla,Q]\big)\omega.
\]

Then

\[
\boxed{
D_t\Phi_Q
=H^T\Big[
\underbrace{(\partial_tQ+[u\cdot\nabla,Q])\omega}_{\text{moving/interface transport}}
+
\underbrace{(QA-AQ)\omega}_{\text{strain--selection mismatch}}
+
\underbrace{\nu Q\Delta\omega}_{\text{viscosity}}
\Big].
}
\]

This is an identity, not an estimate.

Three immediate calibrations follow.

1. `Q=I`: both commutators vanish and the full Kelvin/Nanson law is recovered.
2. A co-moving role satisfying `partial_t Q+[u.grad,Q]=0` has no observer/interface leakage from common transport.
3. A moving sharp or smooth cut that is not co-moving necessarily carries the explicit `partial_t Q` time-face.  It cannot be represented only by a static spatial commutator.

The third item is exactly the structural slot required for moving quantile/shell localization.

## 3. Cubic oriented flux inherits the same physical ledger

For three localized roles define

\[
\mathcal C_H
=\frac1{\det H}
\operatorname{Re}[\overline{\Phi_3}\cdot(\Phi_1\times\Phi_2)].
\]

In incompressible flow `D_t det H=0`.  Writing

\[
R_i=D_t\Phi_i
=R_i^{\rm int}+R_i^{\rm strain}+R_i^{\rm visc},
\]

Leibniz gives

\[
\boxed{
D_t\mathcal C_H
=\mathfrak D(R_1,R_2,R_3),
}
\]

where

\[
\mathfrak D(R_1,R_2,R_3)
=\frac1{\det H}\operatorname{Re}\Big[
\overline{R_3}\cdot(\Phi_1\times\Phi_2)
+\overline{\Phi_3}\cdot(R_1\times\Phi_2+\Phi_1\times R_2)
\Big].
\]

By linearity,

\[
D_t\mathcal C_H
=\mathfrak D_{\rm interface}
+\mathfrak D_{\rm strain-selection}
+\mathfrak D_{\rm viscosity}.
\]

There is no fourth positive `metric production` term.  The material metric is already part of the exact Nanson coordinate change; passive packet motion cannot manufacture cubic work.

## 4. Interpretation for the bridge programme

This identity gives a common PDE-first traffic law:

- full material transport/stretching is the road geometry and cancels in full flux coordinates;
- localization creates explicit interface/moving-cut traffic;
- selecting a role that does not commute with local stretching creates an actual role-exchange term;
- viscosity remains a physical differential source/payment;
- pressure is gauge at vorticity level;
- signed nonlinear edge work is represented by the oriented cubic flux itself, not by a covariance proxy.

The next frontier is to choose the **actual localized role operators used by the two upstream programmes** and identify these two commutators with their named physical interface/SGS/relative-polarization objects without double counting.
