# The final net critical action cannot be bounded by the subcritical kinetic-energy budget alone

Status: **SCALING NO-GO / ARCHITECTURAL CONSTRAINT**.

## 1. Critical scaling of the final action

On `R^3`, Navier--Stokes scaling is

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t).
\]

The absolute critical stock

\[
\mathcal C=\|u\|_{\dot H^{1/2}}^2
\]

is invariant.  Therefore its nonlinear source `J_1` scales as one inverse time,

\[
J_{1,\lambda}(t)=\lambda^2J_1(\lambda^2t),
\]

and the time-integrated positive action is invariant:

\[
\boxed{
\int[J_{1,\lambda}]_+dt
=
\int[J_1]_+dt.
}
\]

The same holds for integrated net pair action.

## 2. Kinetic energy dissipation is subcritical to this action

The kinetic-energy scale is

\[
\|u_\lambda\|_2^2
=\lambda^{-1}\|u\|_2^2,
\]

and likewise

\[
\nu\int\|\nabla u_\lambda\|_2^2dt
=\lambda^{-1}
\nu\int\|\nabla u\|_2^2dt.
\]

Hence no scale-independent universal inequality of the form

\[
\int[J_1]_+dt
\le C\Bigl(\|u_0\|_2^2+
u\int\|\nabla u\|_2^2dt\Bigr)
\]

can hold over the scaling class unless the left side vanishes identically.

## 3. Consequence for the proof search

The remaining critical action cannot be closed by renaming the ordinary energy inequality as a larger budget.  Any successful finiteness theorem must use additional **critical structure** already exposed by the PDE, for example:

- heterochiral split/merge cancellation;
- radial first-moment geometry;
- low-opposite quadratic suppression;
- low-donor/high-pair strain or backreaction geometry;
- comparable pair creation/annihilation structure;
- exact phase/event/state constraints if they genuinely control the same action.

This no-go is useful because it prevents the programme from returning to a dimensionally impossible norm estimate at the final step.

**Classification: COUNTEREXAMPLE/NO-GO BY NSE SCALING.**
