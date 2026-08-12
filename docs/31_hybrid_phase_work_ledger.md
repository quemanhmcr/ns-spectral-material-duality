# Continuous PDE owners and finite selector events form one exact hybrid phase/work ledger

Status: **Exact complex-logarithm/event identity plus a rigorous hybrid local alternative.**

The earlier phase/work theorem was deliberately stated only on a fixed typed
continuous interval.  The first-bad audit now supplies an exact finite complex jump
at entry/resolve/reselection events.  These two pieces can be joined without
smearing jumps into a fake time density and without assuming that the event sequence
terminates.

---

## 1. Piecewise-smooth complex interaction history

Let

\[
0=t_0<\tau_1<\cdots<\tau_N<t_{N+1}=T
\]

be finitely many typed event times on a compact observation interval.  Assume the
complex interaction `Z(t)` is absolutely continuous on every open interval
`(tau_j,tau_{j+1})`, has nonzero one-sided limits at the event times, and is nonzero
on the continuous pieces under discussion.

On each continuous piece write the exact owner decomposition

\[
\dot Z=\sum_{o\in\mathcal O}\dot Z_o.
\]

At event `j` define

\[
Z_j^-=Z(\tau_j^-),
\qquad
Z_j^+=Z(\tau_j^+).
\]

For a legitimate selector reset these are given by the exact reweighting law in
`docs/30_finite_selector_cubic_jump.md`; other typed hard events may have their own
exact re-registration map.

---

## 2. Exact hybrid logarithmic-amplitude identity

On every nonzero continuous piece,

\[
\frac{d}{dt}\log|Z|
=\operatorname{Re}\frac{\dot Z}{Z}.
\]

Therefore telescoping across the event times gives

\[
\boxed{
\log\frac{|Z(T^-)|}{|Z(0^+)|}
=
\sum_{j=0}^{N}
\int_{\tau_j}^{\tau_{j+1}}
\operatorname{Re}\frac{\dot Z}{Z}\,dt
+
\sum_{j=1}^{N}
\log\frac{|Z_j^+|}{|Z_j^-|}.
}
\]

Substituting the continuous owner split,

\[
\boxed{
\log\frac{|Z(T^-)|}{|Z(0^+)|}
=
\sum_o\sum_j
\int_{\tau_j}^{\tau_{j+1}}
\operatorname{Re}\frac{\dot Z_o}{Z}\,dt
+
\sum_j \Delta a_j,
}
\]

where

\[
\Delta a_j:=\log\frac{|Z_j^+|}{|Z_j^-|}.
\]

**Classification: EXACT HYBRID AMPLITUDE IDENTITY.**

A selector event is not assigned an infinitesimal owner.  Its entire contribution
is the finite number `Delta a_j`.

---

## 3. Exact lifted-phase identity and branch-free variation form

Choose on each nonzero continuous piece a continuous lift `theta(t)` of
`arg Z(t)`.  At event `j` choose a lifted event angle `Delta theta_j` satisfying

\[
e^{i\Delta\theta_j}
=
\frac{Z_j^+/|Z_j^+|}{Z_j^-/|Z_j^-|}.
\]

Then

\[
\boxed{
\theta(T^-)-\theta(0^+)
=
\sum_j\int_{\tau_j}^{\tau_{j+1}}
\operatorname{Im}\frac{\dot Z}{Z}\,dt
+
\sum_j\Delta\theta_j.
}
\]

The lift carries the usual integer winding choice.  For coercive phase-loss
statements no branch choice is needed.  Let

\[
d_{S^1}(z_1,z_2)
:=|\operatorname{Arg}(z_2/z_1)|
\]

for unit complex numbers, with principal `Arg` in `(-pi,pi]`.  The total phase path
length

\[
\boxed{
\mathcal P_{\rm hyb}
:=
\sum_o\sum_j
\int_{\tau_j}^{\tau_{j+1}}
\left|
\operatorname{Im}\frac{\dot Z_o}{Z}
\right|dt
+
\sum_j
\left|
\operatorname{Arg}\frac{Z_j^+}{Z_j^-}
\right|
}
\]

bounds the geodesic displacement of the normalized interaction on `S^1`.

**Classification: EXACT PHASE IDENTITY / RIGOROUS METRIC CONSEQUENCE.**

---

## 4. Hybrid amplitude-loss payment

Define the continuous owner amplitude action

\[
A_o^{\rm cont}
=
\sum_j
\int_{\tau_j}^{\tau_{j+1}}
\left|
\operatorname{Re}\frac{\dot Z_o}{Z}
\right|dt
\]

and the discrete event amplitude action

\[
A^{\rm evt}
=
\sum_j|\Delta a_j|.
\]

If, before a zero of `Z`,

\[
|Z(t_*)|\le \rho |Z(0^+)|,
\qquad 0<\rho<1,
\]

then the exact logarithmic identity and the triangle inequality give

\[
\boxed{
\sum_o A_o^{\rm cont}+A^{\rm evt}
\ge \log(1/\rho).
}
\]

**Classification: RIGOROUS HYBRID AMPLITUDE CONSEQUENCE.**

Amplitude can therefore disappear through continuous PDE/source action, a finite
reset/reselection jump, or an actual zero.  A reset cannot make the loss free.

---

## 5. Hybrid phase-loss payment

Let

\[
c(t)=\frac{\operatorname{Re}Z(t)}{|Z(t)|}
\]

where `Z` is nonzero.  Fix

\[
0<c_{lo}<c_{hi}<1
\]

and suppose initially

\[
c(0^+)\ge c_{hi}.
\]

Let `t_*` be the first time, including an event jump, at which

\[
c(t_*)\le c_{lo}.
\]

The geodesic distance on the unit circle from the initial favorable set
`{Re z >= c_hi}` to the exit set `{Re z <= c_lo}` is

\[
\delta_\theta
=
\arccos(c_{lo})-\arccos(c_{hi}).
\]

Hence

\[
\boxed{
\mathcal P_{\rm hyb}
\ge
\delta_\theta.
}
\]

**Classification: RIGOROUS HYBRID PHASE CONSEQUENCE.**

A finite event may pay most or all of this angular displacement.  It is not
legitimate to charge such a jump to the neighboring continuous phase source.

---

## 6. Hybrid local no-free-escape alternative

Assume a chosen physical root remains in a real signed-work geometry corridor

\[
\kappa(t)\ge\kappa_*>0
\]

on every continuous piece and is re-registered after each finite event.  Suppose
also `Z` remains nonzero wherever the phase is read.

Then before geometry exits, at least one of the following happens:

1. **amplitude loss:** `|Z| <= rho |Z(0)|`, forcing total continuous-plus-event
   amplitude action at least `log(1/rho)`;
2. **phase loss:** `Re Z/|Z| <= c_lo`, forcing total continuous-plus-event phase
   path length at least `delta_theta`;
3. **persistent favorable work:** while neither loss has occurred,
   \[
   W(t)=\kappa(t)\operatorname{Re}Z(t)
   \ge
   \kappa_* c_{lo}\rho |Z(0)|>0;
   \]
4. **typed structural exit:** geometry corridor failure, `Z=0`, loss of physical
   selector realizability, unresolved state-map/clock semantics, or an event for
   which the post-event interaction has not yet been physically re-registered.

**Classification: RIGOROUS HYBRID LOCAL ALTERNATIVE.**

This theorem closes the bookkeeping seam across a **finite** number of already
legitimate events on a fixed observation interval.  It does not prove that event
counts are finite uniformly in time, that reset actions have a finite global bank,
that favorable work recurs, or that Navier--Stokes is regular.

---

## 7. Event owner refinement

For a selector jump, the exact event increment is

\[
Z_j^+-Z_j^-
=
\mathbb E[\Delta\chi_j\,\mathcal Z].
\]

Thus its discrete amplitude and phase data are not arbitrary bookkeeping labels;
they are determined by the physical states entering/leaving the selected law.
Common same-replica `SL(3)` Cauchy deformation cancels inside this event formula.
The discrete owner is therefore **selection/reweighting of interaction content**,
not deformation metric spread.

For Wang hard events, the hard event phase is re-read exactly from the full carrier
on the event plateau rather than propagated as a persistent hard scalar phase.  The
same hybrid ledger can treat such re-registration as an event boundary without
identifying Wang and Kelvin selector architectures.

**Classification: EXACT EVENT INTERPRETATION; architectures remain distinct.**
