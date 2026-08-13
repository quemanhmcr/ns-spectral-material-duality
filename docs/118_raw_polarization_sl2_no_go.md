# Raw transverse polarization is not `SL(2)` when the Kelvin carrier changes radius

Status: **EXACT AFFINE NSE CALIBRATION / NO-GO AGAINST PREMATURE `SL(2)` NORMALIZATION**.

## 1. Exact affine pure strain

Take the exact affine Navier--Stokes solution

\[
A=S=\operatorname{diag}(a,-a,0)
\]

with its quadratic pressure.  Start with carrier

\[
k(0)=e_1.
\]

Then

\[
|k(t)|=e^{-at}.
\]

The transverse plane is spanned by `e_2,e_3`, and

\[
B_\perp=\begin{pmatrix}-a&0\\0&0\end{pmatrix}.
\]

Inviscidly the raw transverse fundamental map is

\[
\boxed{
U_\perp(t)
=\begin{pmatrix}e^{at}&0\\0&1\end{pmatrix},
\qquad
\det U_\perp=e^{at}\ne1
}
\]

for `a t !=0`.

Yet

\[
|k(t)|\det U_\perp(t)=1.
\]

## 2. Only the correctly normalized trace-free map is `SL(2)`

The scalar factor is

\[
\left(\frac{|k(0)|}{|k(t)|}\right)^{1/2}=e^{at/2}.
\]

Thus

\[
\widetilde U
=e^{-at/2}U_\perp
=\begin{pmatrix}e^{at/2}&0\\0&e^{-at/2}\end{pmatrix},
\]

and

\[
\boxed{\det\widetilde U=1.}
\]

Therefore a theorem that applies `SL(2)`/symplectic neutrality directly to the **raw** transverse amplitude map while the carrier radius changes has silently dropped a physical scalar dilation.

Wang's own objective polarization calculus correctly factors this scalar sector; repo 3 records why that factor is forced by exterior/top-form geometry.
