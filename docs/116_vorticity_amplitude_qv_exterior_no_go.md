# Vorticity amplitude curvature and Kelvin q.v. curvature are non-equivalent despite sharing `R_2`

Status: **EXACT NSE COUNTEREXAMPLE PAIR / NO-GO AGAINST REPRESENTATION-CONFLATION**.

Sharing one exterior representation does not make two physical inputs equivalent.  Exact Navier--Stokes solutions show both directions of failure.

## 1. Affine rigid rotation: deterministic `R_2(omega omega^T)` active, Kelvin q.v. zero

Take

\[
u=\Omega x,
\qquad
\Omega=\begin{pmatrix}0&-r&0\\r&0&0\\0&0&0\end{pmatrix},
\]

with the centrifugal quadratic pressure from Theorem DY.  This is an exact smooth affine NSE solution.

Its vorticity is spatially uniform,

\[
\omega=(0,0,2r),
\qquad
\nabla\omega=0.
\]

Therefore

\[
\boxed{R_2(\omega\omega^T)\ne0,}
\]

while

\[
\boxed{\Gamma_K=0,\qquad R_2(\Gamma_K)=0.}
\]

The deterministic rotation-curvature face is active with no Kelvin gradient q.v.

## 2. Periodic shear symmetry point: Kelvin q.v. active, deterministic amplitude curvature zero

Take the exact periodic shear

\[
u=(a e^{-\nu t}\sin y,0,0).
\]

Then

\[
\omega=(0,0,-a e^{-\nu t}\cos y).
\]

At

\[
y=\frac\pi2,
\]

one has

\[
\boxed{\omega=0,}
\]

but

\[
\partial_y\omega_z=a e^{-\nu t}\ne0.
\]

Hence

\[
\boxed{R_2(\omega\omega^T)=0,}
\]

while

\[
\boxed{\Gamma_K\ne0,\qquad R_2(\Gamma_K)\ne0.}
\]

The Kelvin q.v./gradient geometry is active with zero deterministic vorticity-amplitude curvature.

## 3. No-go

Therefore neither object determines the other:

\[
\boxed{
R_2(\omega\omega^T)
\not\Longleftrightarrow
R_2(\Gamma_K).
}
\]

The common `R_2` is a representation law, not a physical equivalence of the inputs.
