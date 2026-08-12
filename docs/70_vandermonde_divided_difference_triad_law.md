# Every helical triad moment is one signed-frequency Vandermonde times one divided difference

Status: **EXACT ALGEBRAIC NSE IDENTITY**.  This is the compressed form of BR/BU.

## 1. The determinant identity

For a closed helical triad write

\[
x_i=s_i|k_i|
\]

and

\[
T_0=(x_1-x_2)R_\triangle,
\quad
T_1=(x_2-x_0)R_\triangle,
\quad
T_2=(x_0-x_1)R_\triangle.
\]

For any scalar function `phi` defined on the three signed frequencies, the triad contribution to the `phi`-moment is

\[
\mathcal W_\triangle^\phi
=
\sum_{i=0}^2\phi(x_i)T_i.
\]

For distinct `x_i`, let `phi[x_0,x_1,x_2]` denote the symmetric second divided difference.  Direct Lagrange interpolation gives

\[
\boxed{
\mathcal W_\triangle^\phi
=
-R_\triangle
(x_0-x_1)(x_1-x_2)(x_2-x_0)
\,\phi[x_0,x_1,x_2].
}
\]

The repeated-node cases are obtained by the ordinary derivative limit whenever `phi` is smooth.

## 2. Enstrophy is the bare Vandermonde

For `phi(x)=x^2`,

\[
\phi[x_0,x_1,x_2]=1.
\]

Therefore

\[
\boxed{
\mathcal V_{2,\triangle}
=
-R_\triangle
(x_0-x_1)(x_1-x_2)(x_2-x_0).
}
\]

So nonlinear enstrophy work factors into exactly two pieces:

1. the common physical cubic amplitude/phase `R_triangle`;
2. the signed-frequency Vandermonde geometry.

The split/merge sign in BR is the sign of this single product.

## 3. Energy and helicity vanish because affine divided differences vanish

For `phi=1` or `phi=x`, the second divided difference is zero.  The determinant law therefore gives

\[
\mathcal W_\triangle^1=0,
\qquad
\mathcal W_\triangle^x=0,
\]

which are exactly triad energy and helicity conservation.

For convex `phi`, `phi[x_0,x_1,x_2]>=0`, so every convex spectral moment has the same triad sign as enstrophy.  BU is therefore not a collection of separate Jensen arguments: it is one divided-difference multiplier law.

## 4. Exact geometric capacity of the Vandermonde

Suppose

\[
|x_i|\le K.
\]

Order the three points as `y_0<=y_1<=y_2` and set

\[
a=y_1-y_0,
\qquad
b=y_2-y_1.
\]

Then `a,b>=0`, `a+b<=2K`, and

\[
\prod_{i<j}|x_i-x_j|
=ab(a+b).
\]

Since `ab<=(a+b)^2/4`,

\[
\boxed{
\left|
(x_0-x_1)(x_1-x_2)(x_2-x_0)
\right|
\le2K^3.
}
\]

Equality occurs at the signed-frequency configuration `(-K,0,K)` up to permutation.

Consequently

\[
\boxed{|\mathcal V_{2,\triangle}|\le2K^3|R_\triangle|.}
\]

This is the exact geometry capacity before any amplitude estimate on `R_triangle`.

## 5. Helical-frequency collision is enstrophy-neutral

If any two signed frequencies coincide, the Vandermonde vanishes.  The triad may still exchange energy between roots, but

\[
\boxed{\mathcal V_{2,\triangle}=0.}
\]

Thus gross energy traffic near a signed-helicity collision cannot be promoted to enstrophy production.

## 6. Relation to the parabolic curvature theorem

For the unique heat defect `w_tau`, the divided difference `w_tau[x_0,x_1,x_2]` is the exact triad multiplier converting enstrophy Vandermonde work into heat-defect work.  BV gives its sign and quantitative lower when all three nodes lie below the convex half-face.

No new currency is introduced.  The entire hierarchy is one common triad cubic times one geometry determinant times one observable curvature.
