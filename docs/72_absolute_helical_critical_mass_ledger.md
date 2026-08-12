# Absolute helical critical mass has an exact opposite-helicity pair creation/annihilation ledger

Status: **EXACT NSE / HELICAL CONVEX-MOMENT IDENTITY**.  No norm estimate is used in the identity.  The observable is the literal absolute signed-frequency first moment of modal kinetic energy.

## 1. The critical mass observable

For a helical mode `m=(k,s)` write

\[
x_m=s|k|,
\qquad E_m=|a_{k,s}|^2.
\]

Define

\[
\boxed{
\mathcal C(t)=\sum_m |x_m|E_m(t)
=\sum_{k,s}|k|E_{k,s}(t).
}
\]

This is the absolute helical critical-mass stock.  It has the Navier--Stokes scaling of the homogeneous `H^(1/2)` energy, but its role here is fixed physically before any estimate: it is the first absolute moment of the signed-frequency energy law.

Viscosity contributes exactly

\[
-2\nu\sum_m |x_m|^3E_m.
\]

## 2. One-donor split: same sign creates no critical mass

For one closed-triad split, order the recipient signed frequencies as

\[
x_-<x_d<x_+,
\]

and let the donor work be `Q`, with recipient probabilities `p_-`,`p_+`.  Helicity conservation gives

\[
p_-x_-+p_+x_+=x_d.
\]

The nonlinear contribution to `C` is the Jensen gap

\[
J_{|x|}^{split}
=Q\,[p_-|x_-|+p_+|x_+|-|x_d|].
\]

If `x_-` and `x_+` have the same sign, `|x|` is affine on the whole event interval and

\[
\boxed{J_{|x|}^{split}=0.}
\]

Thus a homochiral one-donor split can redistribute critical mass in signed frequency but cannot create it.

## 3. Cross-sign split creates an equal helicity-cancellation pair

If

\[
x_-<0<x_+,
\]

define the opposite-helicity pair charge

\[
\boxed{
\mathcal P_\triangle^{create}
=Q\min\{p_-|x_-|,\;p_+x_+\}.
}
\]

If `x_d>=0`, the minimum is `Qp_-|x_-|`; if `x_d<=0`, it is `Qp_+x_+`.  In either case the barycenter identity gives

\[
\boxed{
J_{|x|}^{split}=2\mathcal P_\triangle^{create}.
}
\]

So a heterochiral split creates equal positive and negative absolute-helicity charges.  The factor two is physical: one copy is the gain in the donor-helicity sector and the other is the newly populated opposite-helicity sector.

## 4. Two-donor merge annihilates the same pair charge

For a two-donor merge the recipient is the signed-frequency barycenter of the two donors.  If the donor signed frequencies do not straddle zero, the `|x|` Jensen gap again vanishes.  If they straddle zero, define

\[
\mathcal P_\triangle^{ann}
=Q\min\{q_-|x_-|,\;q_+x_+\}.
\]

Then the merge contribution is

\[
\boxed{
J_{|x|}^{merge}=-2\mathcal P_\triangle^{ann}.
}
\]

Thus heterochiral merging annihilates exactly the same kind of opposite-helicity critical pair that heterochiral splitting creates.

## 5. Global exact ledger

Push the certified closed-triad law through these two charges.  With

\[
\mathcal P_{create}\ge0,
\qquad
\mathcal P_{ann}\ge0,
\]

one obtains

\[
\boxed{
\frac d{dt}\mathcal C
+2\nu\sum_m|x_m|^3E_m
=2(\mathcal P_{create}-\mathcal P_{ann}).
}
\]

Homochiral split/merge traffic is invisible to the source term because `|x|` is affine on one sign half-line.  Only helicity-sign crossing changes the total critical-mass stock.

This is the degree-one convex-moment companion to the degree-two split-variance ledger

\[
\frac12Y'+\nu Z=\mathcal V_{split}-\mathcal V_{merge}.
\]

**Classification: EXACT NSE/PDE IDENTITY.**

## 6. Scope

The identity does not bound `C`, and it does not by itself prove regularity.  Its purpose is structural: any global increase of absolute helical critical mass has one and only one nonlinear source -- opposite-helicity pair creation by a one-donor split.  Homochiral variance production must be paid by redistribution rather than creation of this critical stock.
