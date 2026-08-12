# The full vectorized Cauchy covariance has two exact Gram projections and an inverse Kelvin/strain dictionary

Status: **Exact covariance-contraction identities plus rigorous short-horizon inverse consequences.**

The Kelvin upstream now carries the full

\[
\Sigma_D=\operatorname{Cov}(\operatorname{vec}D)\in\mathbb R^{9\times9}.
\]

Keeping the full tensor, rather than immediately taking one scalar norm or one Gram
projection, exposes two natural partial traces.  Their sum/difference separate the
short-horizon strain/rotation geometry, and together with the mean exterior-volume
defect they invert back to instantaneous physical gradient currencies.

---

## 1. Two exact partial traces of `Sigma_D`

Write deformation indices as `D_{ia}`.  The vectorized covariance has components

\[
(\Sigma_D)_{ia,jb}
=\operatorname{Cov}(D_{ia},D_{jb}).
\]

Contract the material/column index:

\[
\boxed{
(C_{\rm row})_{ij}
:=\sum_a(\Sigma_D)_{ia,ja}
=\mathbb E[DD^T]_{ij}-(\bar D\bar D^T)_{ij}.
}
\]

Contract the spatial/row index instead:

\[
\boxed{
(C_{\rm col})_{ab}
:=\sum_i(\Sigma_D)_{ia,ib}
=\mathbb E[D^TD]_{ab}-(\bar D^T\bar D)_{ab}.
}
\]

**Classification: EXACT COVARIANCE CONTRACTION IDENTITIES.**

The current upstream packet metric uses `C_row`.  `C_col` is not a replacement; it
is the dual Gram projection already contained in the same literal `9 x 9`
covariance.

---

## 2. Short-horizon row/column duality

Let

\[
G_\mu=\partial_\mu A,
\qquad
A=\nabla u.
\]

The vectorized Cauchy law gives

\[
\boxed{
C_{\rm row}
=\frac{2\nu}{3}h^3\sum_\mu G_\mu^TG_\mu+O(h^4),
}
\]

while the second partial trace gives

\[
\boxed{
C_{\rm col}
=\frac{2\nu}{3}h^3\sum_\mu G_\mu G_\mu^T+O(h^4).
}
\]

Decompose

\[
G_\mu=P_\mu+Q_\mu,
\qquad
P_\mu=\partial_\mu S,
\qquad
Q_\mu=\frac12[\partial_\mu\omega]_\times.
\]

Then

\[
G_\mu^TG_\mu
=P_\mu^2-Q_\mu^2+(P_\mu Q_\mu-Q_\mu P_\mu),
\]

\[
G_\mu G_\mu^T
=P_\mu^2-Q_\mu^2-(P_\mu Q_\mu-Q_\mu P_\mu).
\]

Therefore

\[
\boxed{
C_+
:=\frac12(C_{\rm row}+C_{\rm col})
=\frac{2\nu h^3}{3}\sum_\mu(P_\mu^2-Q_\mu^2)+O(h^4),
}
\]

and

\[
\boxed{
C_-
:=\frac12(C_{\rm row}-C_{\rm col})
=\frac{2\nu h^3}{3}\sum_\mu(P_\mu Q_\mu-Q_\mu P_\mu)+O(h^4).
}
\]

**Classification: RIGOROUS SHORT-HORIZON MATRIX CONSEQUENCE.**

`C_+` is transpose-even strain-plus-rotation dispersion.  `C_-` is the exact
transpose-odd, symmetric trace-free orientation-coupling sector.

---

## 3. Kelvin q.v. removes the rotation sector and leaves strain-gradient square

From the preceding Hodge bridge,

\[
C_\Omega
=\frac{h^3}{12}
[(\operatorname{tr}\Gamma_K)I-\Gamma_K]+O(h^4),
\]

where

\[
\Gamma_K=2\nu(\nabla\omega)(\nabla\omega)^T.
\]

Since

\[
C_+=C_S+C_\Omega+O(h^4),
\]

we obtain

\[
\boxed{
C_S
:=C_+-\frac{h^3}{12}
[(\operatorname{tr}\Gamma_K)I-\Gamma_K]
=rac{2\nu h^3}{3}
\sum_\mu(\partial_\mu S)^2+O(h^4).
}
\]

Thus full vectorized Cauchy covariance plus the instantaneous Kelvin q.v. tensor
separates, at leading order,

1. the PSD strain-gradient square tensor;
2. the PSD Hodge-lifted rotation-gradient tensor;
3. the signed symmetric trace-free strain/rotation orientation coupling.

**Classification: RIGOROUS LOCAL INVERSE MATRIX DICTIONARY.**

No norm bound is required to perform the separation.

---

## 4. Scalar inverse dictionary from Cauchy statistics alone

Let

\[
T_h:=\operatorname{tr}C_{\rm row}
=\operatorname{tr}C_{\rm col}
\]

and

\[
\delta_h:=1-\det\bar D.
\]

Set

\[
a:=|\nabla S|_F^2,
\qquad
b:=|\nabla\Omega|_F^2
=\frac12|\nabla\omega|^2.
\]

The short-horizon laws give

\[
T_h
=\frac{2\nu h^3}{3}(a+b)+O(h^4),
\]

\[
\delta_h
=\frac{\nu h^3}{3}(b-a)+O(h^4).
\]

The sum and difference invert this `2 x 2` system exactly at leading order.  Since

\[
\operatorname{tr}\Gamma_K
=2\nu|\nabla\omega|^2
=4\nu b,
\]

one gets

\[
\boxed{
\operatorname{tr}\Gamma_K
=\lim_{h\downarrow0}
\frac{3T_h+6\delta_h}{h^3}.
}
\]

Likewise

\[
\boxed{
\nu|\nabla S|_F^2
=\lim_{h\downarrow0}
\frac{3T_h-6\delta_h}{4h^3}.
}
\]

Equivalently,

\[
\boxed{
|\nabla\omega|^2
=\lim_{h\downarrow0}
\frac{3T_h+6\delta_h}{2\nu h^3}.
}
\]

**Classification: RIGOROUS INFINITESIMAL INVERSE CONSEQUENCE.**

This is a genuine inverse bridge: the positive trace of finite-horizon deformation
covariance and the signed failure of mean exterior volume carry complementary
information.  Neither statistic alone separates strain-gradient from
vorticity-gradient variation.

---

## 5. Exact one-mode shear illustrates both partial traces

For the one-mode shear, at a point with

\[
c=\partial_y^2u_1,
\]

one has

\[
G=\partial_yA
=ce_1e_2^T.
\]

Hence

\[
\boxed{G^TG=c^2e_2e_2^T,}
\qquad
\boxed{GG^T=c^2e_1e_1^T.}
\]

Thus the two Cauchy Gram projections point in orthogonal directions even though
they come from the same vectorized covariance source.  Their average contains the
transpose-even strain/rotation content, while their half-difference is exactly the
orientation-coupling tensor.

The determinant defect vanishes because `a=b`, and the scalar inverse formulas
return the equal strain/rotation-gradient magnitudes.

**Classification: EXACT NAVIER--STOKES CALIBRATION.**

---

## 6. Consequence for data reduction

The full `Sigma_D` contains physically meaningful information that is destroyed by
keeping only `tr Sigma_D`, only `C_row`, or only a scalar metric capacity.  At the
first nontrivial horizon order:

- one partial trace knows physical row-Gram spread;
- the dual partial trace knows material-column Gram spread;
- their difference knows strain/rotation orientation coupling;
- the Kelvin q.v. tensor identifies the rotation/Hodge sector;
- the mean determinant supplies the signed scalar needed to invert strain versus
  rotation magnitudes even without the full Kelvin tensor.

This is exactly the kind of reduction that should happen **after** the PDE geometry
is exposed, not before.

**Classification: STRUCTURAL CONSEQUENCE.**
