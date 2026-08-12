# Convex spectral moments see one-donor splits as dispersion and two-donor merges as concentration

Status: **EXACT CONVEX-ORDER HIERARCHY**.

## 1. One affine barycenter law controls every convex moment

Let `phi:R->R` be convex.  All global moment statements below are made on a smooth interval for convex `phi` whose moment and triad-work integrals are finite (or first for bounded/truncated `phi`, followed by a justified limit).  On a one-donor split, Theorem BR gives

\[
x_d=p_1x_1+p_2x_2.
\]

Therefore Jensen gives

\[
\boxed{
Q[p_1\phi(x_1)+p_2\phi(x_2)-\phi(x_d)]\ge0.
}
\]

On a two-donor merge,

\[
x_r=q_1x_1+q_2x_2,
\]

so

\[
\boxed{
Q[\phi(x_r)-q_1\phi(x_1)-q_2\phi(x_2)]\le0.
}
\]

Thus the closed-triad nonlinear event is a convex-order spread in the `1->2` orientation and a convex-order contraction in the `2->1` orientation.

## 2. Global moment law

Whenever the indicated sums/integrals are finite, define

\[
M_\phi(t)=\sum_{k,s}\phi(s|k|)E_{k,s}(t).
\]

Integrating the exact triad work law gives

\[
\boxed{
\frac d{dt}M_\phi
+2\nu\sum_{k,s}|k|^2\phi(s|k|)E_{k,s}
=
\mathcal J_{split}^\phi-\mathcal J_{merge}^\phi,
}
\]

where the two Jensen-gap ledgers are nonnegative for convex `phi`.

Affine functions have zero Jensen gap.  Therefore:

- `phi=1` recovers nonlinear energy conservation;
- `phi=x` recovers nonlinear helicity conservation;
- `phi=x^2` recovers BR/enstrophy;
- `phi=|x|^p`, `p>=1`, gives a full hierarchy of convex spectral moments whose nonlinear positive owner is always splitting dispersion.

## 3. Strongly convex quantitative gap

If `phi''>=m>0` on the interval containing the donor and recipient signed frequencies, then for a two-point split

\[
\boxed{
Q[p_1\phi(x_1)+p_2\phi(x_2)-\phi(x_d)]
\ge
\frac m2 Qp_1p_2(x_1-x_2)^2.
}
\]

If `phi''<=M`, the same gap is at most `(M/2)Q Var(x)`.  Identical bounds hold for the magnitude of a merge Jensen gap.

Thus BR is the constant-curvature case `phi=x^2`, for which the variance identity is exact with no curvature distortion.

## 4. Scope

Convex order does not bound the split rate.  It reveals a rigid hierarchy beneath every Sobolev-moment estimate and identifies exactly where additional PDE information must enter: the rate `Q_triangle`, not the sign of the moment production.
