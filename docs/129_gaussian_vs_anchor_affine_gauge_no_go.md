# Wang Gaussian and Kelvin anchor gauges are generally different even when their non-affine class is identical

Status: **EXACT PERIODIC NSE CALIBRATION / NO-GO AGAINST IDENTIFYING THE TWO FULL REMAINDER FIELDS**.

The affine-quotient theorem must not be simplified into `R_W=N_L`.

## 1. Exact periodic one-mode Navier--Stokes shear

Take

\[
\boxed{u=(E\sin y,0,0),\qquad E=e^{-\nu t}.}
\]

At `X=0`, choose `L=I` and `\dot X=0`.  Then

\[
v_W(z)=(E\sin z_2,0,0).
\]

Kelvin's anchor affine data are

\[
u(0)=0,
\qquad
\nabla u(0)e_2=Ee_1,
\]

so

\[
\boxed{
\mathcal N_I(z)
=E(\sin z_2-z_2)e_1.}
\]

## 2. Wang Gaussian affine fit has a different slope

For any centered nondegenerate Gaussian weight `rho`, symmetry gives

\[
\bar v=0.
\]

The only nonzero affine-fit coefficient is

\[
\bar A_{12}
=E\,\kappa_\rho,
\qquad
\kappa_\rho
=\frac{\int z_2\sin z_2\,d\rho}
{\int z_2^2\,d\rho}.
\]

For a genuine Gaussian,

\[
0<\kappa_\rho<1.
\]

Thus

\[
\boxed{
R_W(z)=E(\sin z_2-\kappa_\rho z_2)e_1,}
\]

and

\[
\boxed{
R_W(z)-\mathcal N_I(z)
=E(1-\kappa_\rho)z_2e_1\ne0.}
\]

The difference is exactly affine, as Theorem FE requires.

## 3. The higher derivatives are nevertheless identical

For all `p>=2`,

\[
\boxed{D^pR_W=D^p\mathcal N_I.}
\]

Therefore the two full residual fields are **not equal**, but their affine-equivalence class and every higher spatial jet are equal.

This calibration protects both programme semantics:

- Wang's residual remains Gaussian-orthogonal to affine tangent directions;
- Kelvin's residual remains anchored to zero value/gradient at the physical current point.
