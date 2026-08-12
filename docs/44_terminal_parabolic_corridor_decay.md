# A selected parabolic corridor cannot carry scale-critical energy all the way to a first singular time

Status: **EXACT KILLING INEQUALITY / RIGOROUS TERMINAL NON-ACCUMULATION THEOREM** for a stopped selected energy population.  The missing programme step is to prove that the literal first-bad continuation is such a population.

Fix a candidate terminal time `T` and let

\[
\tau=T-t.
\]

Use the exact donor-kernel killed-energy representation from Theorem AR.

## 1. Corridor confinement turns physical viscosity into logarithmic terminal hazard

Let `m_i(t)` be a stopped selected energy population with no incoming mass after typed exit, and suppose every alive state belongs to the parabolic corridor

\[
\boxed{
\alpha
\le
2\nu |k_i|^2\tau
\le
\beta,
\qquad
0<\alpha<\beta<\infty.
}
\]

Its exact mass law is

\[
\dot M=-D_m-X,
\qquad
M=\sum_im_i,
\qquad
D_m=\sum_i2\nu|k_i|^2m_i,
\qquad X\ge0.
\]

The lower parabolic face implies

\[
D_m
\ge
\frac{\alpha}{\tau}M.
\]

Hence

\[
\boxed{
\dot M
\le
-\frac{\alpha}{T-t}M.
}
\]

Integrating from `s` to `t<T` gives

\[
\boxed{
M(t)
\le
M(s)
\left(\frac{T-t}{T-s}\right)^\alpha.
}
\]

This is physical viscous killing, not an auxiliary norm estimate.  The logarithmic divergence of `int dt/(T-t)` is supplied by the first-singular-time clock itself.

## 2. A scale-critical event in the same corridor needs square-root terminal mass

Suppose a genuine continuing event at scale `N` requires the same selected population to contain energy

\[
\boxed{NE_{event}\ge\eta>0.}
\]

At an event inside the corridor,

\[
2\nu N^2\tau\le\beta,
\]

therefore

\[
N\le\sqrt{\frac{\beta}{2\nu\tau}}
\]

and so

\[
\boxed{
E_{event}
\ge
\frac\eta N
\ge
\eta\sqrt{\frac{2\nu}{\beta}}\,\tau^{1/2}.
}
\]

Since `E_event<=M(t)`, every such event must satisfy

\[
M(s)\left(\frac\tau{T-s}\right)^\alpha
\ge
\eta\sqrt{\frac{2\nu}{\beta}}\,\tau^{1/2}.
\]

## 3. If alpha > 1/2, scale-critical corridor events stop before T

If

\[
\boxed{\alpha>\frac12,}
\]

then the viscously surviving selected mass decays faster than the smallest corridor-compatible scale-critical event mass.  Consequently there is an explicit terminal exclusion window: no same-lineage scale-critical continuation event can occur once

\[
\boxed{
\tau^{\alpha-1/2}
<
\frac{\eta\sqrt{2\nu/\beta}\,(T-s)^\alpha}{M(s)}.
}
\]

Equivalently the event sequence cannot accumulate at `T` while remaining inside this stopped parabolic corridor.

**Classification: RIGOROUS TERMINAL NON-ACCUMULATION CONSEQUENCE.**

Unlike Theorem AV, this result needs neither a lower forward jump ratio nor an upper jump ratio **inside the corridor**.  It uses only physical viscous killing, no incoming re-entry, the parabolic faces, and the same-population critical energy floor.

## 4. The exponent 1/2 is structurally sharp for this argument

At `alpha=1/2`, survival and the critical floor have the same terminal power and constants decide.  For `alpha<1/2`, the survival upper `tau^alpha` decays more slowly than the required `tau^(1/2)` floor, so this comparison alone gives no contradiction.

Thus one cannot replace `alpha>1/2` by merely `alpha>0` without bringing in another physical currency.

## 5. Scope

This theorem does not prove that an actual NSE first-bad population remains in the corridor, nor that a selected energy population cannot leave and later re-enter.  Those are exactly the next semantic/owner questions.
