# Wang Gaussian residual is the minimal Gaussian-norm representative of the common Wang/Kelvin affine-equivalence class

Status: **RIGOROUS CONSEQUENCE AFTER EXACT AFFINE-GAUGE TYPING / GAUSSIAN PROJECTION IDENTITY**.

This theorem deliberately uses a norm **after** Theorem FE has identified the exact physical affine-equivalence class.  The norm is therefore measuring a typed quotient rather than being used to discover the physics.

## 1. Start from the exact common affine class

Theorem FE gives

\[
R_W(z)-\mathcal N_L(z)
=(c-\bar v)+(A_L-\bar A)z.
\]

Write

\[
a_g=\bar v-c,
\qquad
B_g=\bar A-A_L.
\]

Then

\[
\boxed{\mathcal N_L=R_W+a_g+B_gz.}
\]

## 2. Wang's gauge is orthogonal to every affine direction

By the current Wang Gaussian least-squares construction,

\[
\int R_W\,d\rho=0,
\qquad
\int R_Wz^T\,d\rho=0.
\]

For a centered Gaussian with covariance

\[
C_\rho=\int zz^T\,d\rho,
\]

`R_W` is therefore orthogonal in `L^2(rho)` to the whole affine space

\[
\mathrm{Aff}=\{a+Bz\}.
\]

## 3. Exact Pythagorean decomposition of Kelvin's anchor residual

The affine pieces have

\[
\int |a_g+B_gz|^2d\rho
=|a_g|^2+\operatorname{tr}(B_gC_\rho B_g^T),
\]

because the Gaussian is centered.  Orthogonality then gives

\[
\boxed{
\|\mathcal N_L\|_{L^2(\rho)}^2
=\|R_W\|_{L^2(\rho)}^2
+|\bar v-c|^2
+\operatorname{tr}\!\left[(\bar A-A_L)C_\rho(\bar A-A_L)^T\right].
}
\]

No inequality has yet been used.

## 4. Wang defect is the affine-gauge-invariant minimum

Let

\[
v_W(z)=c+A_Lz+\mathcal N_L(z).
\]

Since `R_W` is the orthogonal residual of the Gaussian affine projection,

\[
\boxed{
\|R_W\|_{L^2(\rho)}^2
=\inf_{a,B}\|v_W-a-Bz\|_{L^2(\rho)}^2.
}
\]

Equivalently, it is the squared Gaussian norm of the common class

\[
[v_W]_{/\mathrm{Aff}}.
\]

Thus the **Gaussian residual norm** has an exact cross-programme meaning:

\[
\boxed{
\|R_W\|_{L^2(\rho)}
=\text{minimal Gaussian non-affinity of the common Wang/Kelvin affine class}.
}
\]

This quantity must not be confused with Wang's coherent deformation variance
\(\mathcal K_C^2=\mathbb E_\gamma\|\nabla W-\bar A\|_F^2\).  The latter is a gradient-level observable; Wang's OU spectral-gap theorem relates the two but does not identify them.

## 5. Kelvin anchor residual contains an additional affine-gauge mismatch

Kelvin's `N_L` is not trying to minimize a Gaussian norm.  It fixes the physically local gauge

\[
\mathcal N_L(0)=0,
\qquad
D\mathcal N_L(0)=0.
\]

Therefore

\[
\boxed{
\|\mathcal N_L\|_\rho^2
-\|R_W\|_\rho^2
=|\bar v-c|^2
+\operatorname{tr}[(\bar A-A_L)C_\rho(\bar A-A_L)^T]
\ge0.
}
\]

The excess is **not extra physical non-affinity**.  It is the exact mismatch between two affine gauge choices.

Kelvin still needs its local anchor gauge for current/shape dynamics; this theorem does not recommend replacing it by Wang's Gaussian gauge.

## 6. Exact periodic Navier--Stokes shear calibration

For

\[
u=(E\sin y,0,0),\qquad E=e^{-\nu t},
\]

at `X=0,L=I`, using the normalized Gaussian

\[
d\rho=\pi^{-1/2}e^{-y^2}dy,
\qquad C_\rho=\frac12,
\]

Theorem FG gives

\[
\mathcal N_I=E(\sin y-y)e_1,
\qquad
R_W=E(\sin y-\kappa y)e_1,
\qquad
\kappa=e^{-1/4}.
\]

Hence

\[
\boxed{
\|\mathcal N_I\|_\rho^2
-\|R_W\|_\rho^2
=\frac12E^2(1-e^{-1/4})^2.
}
\]

The two residual norms differ in an exact NSE state even though their affine-equivalence class and every derivative of order at least two coincide.

## 7. Research use

This identity allows the Gaussian and Kelvin residual magnitudes to be compared without confusing:

1. **true non-affine quotient content** (`R_W`);
2. **choice of local versus Gaussian affine reference** (the explicit Pythagorean remainder).

It is an example of the repository discipline: exact physical quotient first, norm only afterward.
