# Finite opposite-helicity pair-creation action is a continuation criterion

Status: **RIGOROUS CONTINUATION CRITERION BUILT AFTER EXACT PHYSICAL OWNER CLASSIFICATION**.  This is not a global-regularity theorem.  It says exactly which physical action must diverge if a finite singular time exists.

## 1. Exact input: the absolute-helical critical-mass ledger

Write

\[
\mathcal C(t)=\sum_{k,s}|k|E_{k,s}(t),
\qquad
\mathcal B(t)=\sum_{k,s}|k|^3E_{k,s}(t).
\]

Theorem BY gives

\[
\boxed{
\mathcal C'+2\nu\mathcal B
=2(\mathcal P_{create}-\mathcal P_{ann}),
}
\]

with both pair actions nonnegative and physically defined from the closed-triad donor law.

Assume on `[0,T)` that

\[
\boxed{
P_T:=\int_0^T\mathcal P_{create}(t)\,dt<\infty.
}
\]

Then, since annihilation only lowers the stock,

\[
\boxed{
\sup_{t<T}\mathcal C(t)
\le
\mathcal C(0)+2P_T
=:\mathcal C_*<\infty.
}
\]

Integrating the same exact ledger gives

\[
\boxed{
2\nu\int_0^T\mathcal B(t)dt
\le
\mathcal C(0)+2P_T
=\mathcal C_*.
}
\]

## 2. Moment geometry turns the physical ledger into an `L^2_t H^1_x`-squared control

Let

\[
Y(t)=\sum |k|^2E_{k,s}=\|\nabla u(t)\|_2^2.
\]

Cauchy on the same modal energy measure gives

\[
\boxed{
Y(t)^2
\le
\mathcal C(t)\mathcal B(t).
}
\]

Therefore

\[
\boxed{
\int_0^T Y(t)^2dt
\le
\mathcal C_*\int_0^T\mathcal B(t)dt
\le
\frac{\mathcal C_*^2}{2\nu}<\infty.
}
\]

This estimate is deliberately applied only after the nonlinear mechanism has been classified exactly: the finite quantity is a consequence of finite physical pair creation, not an assumed norm budget.

## 3. Late-stage enstrophy Gronwall closes continuation

The exact enstrophy equation is

\[
\frac12Y'+\nu Z=\mathcal W_{ens},
\qquad
Z=\|\Delta u\|_2^2.
\]

Sobolev/interpolation only now gives

\[
|\mathcal W_{ens}|
\le
C\|u\|_6\|\nabla u\|_3\|\Delta u\|_2
\le
C Y^{3/4}Z^{3/4}.
\]

Young implies

\[
Y'\le C\nu^{-3}Y^3
=
\bigl(C\nu^{-3}Y^2\bigr)Y.
\]

Since `int_0^T Y^2<infinity`, Gronwall yields

\[
\boxed{
\sup_{t<T}Y(t)<\infty.
}
\]

The standard local `H^1` Navier--Stokes construction can therefore restart at times approaching `T`; `T` is not a first singular time.

## 4. Contrapositive: a singularity needs infinite physical pair creation

Hence every finite first singular time must satisfy

\[
\boxed{
\int_0^T\mathcal P_{create}(t)\,dt=\infty.
}
\]

This is much sharper than saying that a critical norm becomes large.  The PDE must execute an infinite total amount of one specific nonlinear physical action: creation of opposite-helicity absolute-critical-mass pairs by one-donor helical splits.

Homochiral splitting cannot supply this action.  Pair annihilation cannot help because it has the opposite sign in the exact ledger.

**Classification: RIGOROUS CONSEQUENCE / NECESSARY BLOW-UP ACTION.**

## 5. What is now left

The global problem is reduced to a single finiteness question:

> Can actual Navier--Stokes heterochiral pair creation have infinite total critical-mass action in finite time?

The comparable branch is already quantified by Theorems CA/CB.  The separated branch must use its exact low/high geometry.  Phase, radial crossing and material theorems are now auxiliary ways to prove this one action finite; they are not additional global sources.
