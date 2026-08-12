# Finite positive net critical radial action implies continuation

Status: **RIGOROUS CONTINUATION CRITERION / SHARPENING OF CC**.  Pair creation and annihilation are cancelled at their exact physical sign before the criterion is read.

## 1. The exact net degree-one radial owner

Let

\[
F(R,t)=\Phi_\uparrow(R,t)-\Phi_\downarrow(R,t)
\]

be the net physical kinetic-energy current through the Fourier sphere of radius `R`.  Theorem CD gives, whenever the first radial moment is defined by truncation/limit,

\[
\boxed{
J_1(t):=\int_0^\infty F(R,t)dR
=2\bigl(\mathcal P_{create}(t)-\mathcal P_{ann}(t)\bigr).
}
\]

The absolute helical critical stock

\[
\mathcal C=\sum |k|E
\]

therefore obeys

\[
\boxed{
\mathcal C'+2\nu\mathcal B=J_1,
\qquad
\mathcal B=\sum |k|^3E.
}
\]

This is one signed physical current law.  There is no gross pair-count or second Hahn split.

## 2. Only the positive part of the net action matters

Assume

\[
\boxed{
A_1(T):=\int_0^T[J_1(t)]_+dt<\infty.
}
\]

From the exact ledger,

\[
\mathcal C(t)
=\mathcal C(0)+\int_0^tJ_1ds-2\nu\int_0^t\mathcal Bds,
\]

hence

\[
\boxed{
\sup_{t<T}\mathcal C(t)
\le \mathcal C(0)+A_1(T)=:\mathcal C_*.
}
\]

Also

\[
2\nu\int_0^T\mathcal Bdt
=\mathcal C(0)-\mathcal C(T^-)+\int_0^T J_1dt
\le \mathcal C(0)+A_1(T),
\]

with the same bound understood through `limsup` on preterminal times if a terminal trace is not assumed.  Therefore

\[
\boxed{
2\nu\int_0^T\mathcal Bdt\le\mathcal C_*.
}
\]

Pair-creation/annihilation cycles which cancel in `J_1` cannot fake a positive budget requirement.

## 3. Continuation

The modal moment inequality

\[
Y^2\le\mathcal C\mathcal B,
\qquad
Y=\|\nabla u\|_2^2,
\]

gives

\[
\int_0^T Y^2dt
\le\frac{\mathcal C_*^2}{2\nu}<\infty.
\]

Only after this exact physical reduction use the usual enstrophy estimate

\[
Y'\le C\nu^{-3}Y^3
=(C\nu^{-3}Y^2)Y.
\]

Gronwall bounds `Y` on `[0,T)`, so the `H^1` solution restarts through `T`.

Thus every finite first singular time must satisfy

\[
\boxed{
\int_0^T
\left[
\int_0^\infty F(R,t)dR
\right]_+dt
=\infty.
}
\]

Equivalently,

\[
\boxed{
\int_0^T
[\mathcal P_{create}-\mathcal P_{ann}]_+dt
=\infty.
}
\]

**Classification: RIGOROUS CONSEQUENCE / NECESSARY BLOW-UP ACTION.**

## 4. Why this is sharper than gross pair creation

CC used `int P_create<infinity`, which is sufficient but counts create/annihilate cycling even when the two effects cancel in the state ledger.  The present theorem reads the physical state equation first and keeps only the positive variation of its actual signed nonlinear source.

The remaining global problem is therefore not gross heterochiral traffic.  It is finiteness of the **positive net critical radial moment action**.
