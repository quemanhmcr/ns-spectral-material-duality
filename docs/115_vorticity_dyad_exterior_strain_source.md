# Vorticity enters the exact strain equation through a deterministic exterior-square transverse lift

Status: **EXACT NSE CARTAN/EXTERIOR IDENTITY / CROSS-KELVIN DETERMINISTIC-STOCHASTIC DICTIONARY**.

## 1. Rotation tensor is the vorticity cross-product representation

For incompressible Navier--Stokes,

\[
A=\nabla u=S+\Omega,
\qquad
A-A^T=[\omega]_\times,
\qquad
\Omega=\frac12[\omega]_\times.
\]

The cross-product matrix satisfies

\[
[\omega]_\times^2
=\omega\omega^T-|\omega|^2I.
\]

Therefore

\[
\boxed{
-\Omega^2
=\frac14\left(|\omega|^2I-\omega\omega^T\right)
=\frac14R_2(\omega\omega^T),
}
\]

where the three-dimensional exterior-square/Hodge representation on a symmetric tensor `G` is

\[
R_2(G)=(\operatorname{tr}G)I-G.
\]

The tensor is positive semidefinite, rank two when `omega!=0`, with

\[
\boxed{R_2(\omega\omega^T)\,\omega=0.}
\]

Thus local rotation curvature acts on the plane transverse to vorticity.

## 2. Exact strain source anatomy

The differentiated NSE is

\[
D_tA+A^2=-\nabla^2p+\nu\Delta A.
\]

Taking the symmetric part gives

\[
D_tS+S^2+\Omega^2=-\nabla^2p+\nu\Delta S.
\]

Using the exterior identity,

\[
\boxed{
D_tS
=-S^2
+\frac14R_2(\omega\omega^T)
-\nabla^2p
+\nu\Delta S.
}
\]

The four faces are literal:

1. `-S^2`: strain self-interaction;
2. `+(1/4)R_2(omega omega^T)`: transverse vorticity/rotation geometry;
3. `-Hess p`: incompressibility pressure curvature;
4. `+nu Delta S`: viscous diffusion of strain.

No norm remainder is present.

## 3. Trace consistency is exactly pressure Poisson

Taking trace and using `tr D_tS=tr Delta S=0`,

\[
0=-|S|_F^2+rac14\operatorname{tr}R_2(\omega\omega^T)-\Delta p.
\]

Since

\[
\operatorname{tr}R_2(\omega\omega^T)=2|\omega|^2,
\]

one recovers

\[
\boxed{
\Delta p=-|S|_F^2+\frac12|\omega|^2.
}
\]

So pressure is exactly what restores the trace-free incompressibility constraint after strain and rotation curvature act.

## 4. Material metric acceleration source anatomy

The exact objective/material identity is

\[
\frac12H\ddot MH^T=\mathring S+2S^2,
\qquad
\mathring S=D_tS+S\Omega-\Omega S.
\]

Hence

\[
\boxed{
\frac12H\ddot MH^T
=S^2
+\frac14R_2(\omega\omega^T)
-\nabla^2p
+\nu\Delta S
+[S,\Omega].
}
\]

Here

\[
[S,\Omega]=S\Omega-\Omega S
\]

is symmetric and trace-free.  It is the orientation-coupling face between metric deformation and connection, not a positive source.

## 5. Deterministic and stochastic exterior-square lifts are structurally parallel but physically different

Repo 3/Kelvin already has the instantaneous q.v. tensor

\[
\Gamma_K=2\nu(\nabla\omega)(\nabla\omega)^T
\]

and its exterior-square lift

\[
R_2(\Gamma_K)
=(\operatorname{tr}\Gamma_K)I-\Gamma_K.
\]

The present deterministic strain equation contains

\[
R_2(\omega\omega^T).
\]

Thus both vorticity amplitude and vorticity-gradient q.v. enter geometry through the **same exterior representation** `R_2`, but at different differential orders and with different physical units:

\[
\boxed{
\begin{array}{ccl}
\omega\omega^T &\xrightarrow{R_2}& \text{deterministic rotation curvature in }D_tS,\\
\Gamma_K=2\nu\nabla\omega\nabla\omega^T &\xrightarrow{R_2}& \text{stochastic/finite-horizon rotation-gradient geometry}.
\end{array}}
\]

They must not be identified as one covariance or one budget.

## 6. Physical interpretation for the bridge programme

Wang's resolved/material strain owner evolves under an exact local source anatomy that includes transverse vorticity geometry and pressure curvature.  Kelvin's q.v. exterior ladder probes the spatial variation of vorticity through the same representation functor.  Repo 3 therefore supplies a common geometric language without collapsing deterministic state, stochastic q.v., pressure, or viscosity.
