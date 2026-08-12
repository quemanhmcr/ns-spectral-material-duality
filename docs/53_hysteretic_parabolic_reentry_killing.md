# Hysteretic parabolic reentry has an exact viscous killing cost unless a reverse owner fires

Status: **EXACT PATHWISE PARABOLIC/KILLING IDENTITY** and **RIGOROUS HYSTERETIC CYCLE CONSEQUENCE**.

Current Kelvin first-bad implementation is hysteretic at the selector level, although its physical bad/resolve predicates remain open.  This note records what a genuine parabolic hysteresis gap would buy without identifying the two architectures.

## 1. A physical hysteresis gap

Choose

\[
0<\alpha_-<\alpha_+.
\]

Suppose a selected energy lineage is declared subparabolic/exited once

\[
a\le\alpha_-,
\]

and can be re-admitted as matched continuation only by an actual nonlinear/relink transition reaching

\[
a\ge\alpha_+.
\]

The gap is

\[
\delta_a=\alpha_+-\alpha_->0.
\]

This is a conditional event semantics, not a proposed numerical choice for the programme's still-undefined bad/resolve predicate.

## 2. One completed cycle costs physical killing hazard

Immediately after one reentry let `a_start>=alpha_+`.  Before the lineage can be eligible for another reentry it must first reach `a_end<=alpha_-`.

Along each continuous segment,

\[
\dot a=-d_k,
\]

and at nonlinear scale jumps `a` changes by `Delta a_j`.  Therefore over the cycle

\[
\boxed{
a_{end}-a_{start}
=-\int d_kdt+\sum_j\Delta a_j.}
\]

If every internal continuation jump is nonnegative in the parabolic coordinate,

\[
\Delta a_j\ge0,
\]

then

\[
\boxed{
\int d_kdt
=a_{start}-a_{end}+\sum_j\Delta a_j
\ge\alpha_+-\alpha_-
=\delta_a.}
\]

Thus one completed hysteretic return to the lower face costs at least `delta_a` of actual viscous killing hazard.

## 3. Repeated cycles have exponentially small energy survival

After `n` such completed cycles with no reverse-parabolic jump,

\[
\boxed{
\mathcal K_n
=\int d_kdt
\ge n\delta_a,
\qquad
\text{survival}\le e^{-n\delta_a}.}
\]

Hence an energy-weighted lineage has infinitely many clean hysteretic reentries with probability zero.

If a negative-`Delta a` jump shortcuts the return, this is not free: an actual reverse/down-frequency transfer owner has fired.  It belongs to the donor transport ledger rather than being hidden inside the reset.

## 4. Why hysteresis is structurally useful

Without a gap (`alpha_+=alpha_-`), arbitrarily many grazing crossings can carry arbitrarily small parabolic price.  A finite selector jump in label space alone does not repair that physical degeneracy.

A literal bad/resolve theorem therefore has two possible routes:

1. derive a genuine physical hysteresis gap, after which the killing theorem above prices repeated reentry;
2. allow gapless crossing but then control the resulting interface/reverse current by a different exact owner law.

**Classification: OPEN BRIDGE for actual first-bad semantics; exact consequence once a physical gap is supplied.**
