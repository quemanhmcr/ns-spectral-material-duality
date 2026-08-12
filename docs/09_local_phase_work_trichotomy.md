# Local phase/work trichotomy: a first exact no-free-escape theorem

Status: **Rigorous calculus consequence of the exact complex material interaction ledger.**  It is local and conditional on a geometry corridor; it is not a recurrence-termination theorem.

Let

\[
\mathcal Z(t)=R(t)e^{i\vartheta(t)},
\qquad R(t)>0,
\]

be the complex oriented material-flux interaction of one selected role triple on an interval `I=[0,T]`.  Suppose its exact source decomposition is

\[
\dot{\mathcal Z}
=\dot{\mathcal Z}_{\rm int}
+\dot{\mathcal Z}_{\rm strain}
+\dot{\mathcal Z}_{\rm visc}.
\]

The actual signed edge work has the form

\[
W(t)=\kappa(t)\operatorname{Re}\mathcal Z(t),
\]

where `kappa(t)` is the real frequency/helicity/geometric prefactor supplied by the physical edge representation.

## 1. Separate geometry before phase

Assume a **geometry corridor**

\[
\kappa(t)\ge\kappa_*>0.
\]

If this fails, that is a geometry/frequency/helicity exit and must be routed by the metric/triad ledger.  It is not called phase loss.

Within the corridor define the normalized alignment

\[
c(t)=\frac{\operatorname{Re}\mathcal Z(t)}{|\mathcal Z(t)|}=\cos\vartheta(t).
\]

Fix

\[
0<c_{\rm lo}<c_{\rm hi}<1,
\qquad 0<\rho<1,
\]

and assume initially

\[
c(0)\ge c_{\rm hi}.
\]

## 2. Exact trichotomy

Before the geometry corridor exits, at least one of the following occurs:

1. **amplitude loss:** for some `t`,
   \[
   R(t)\le\rho R(0);
   \]
2. **phase/dephasing loss:** while `R>rho R(0)`, for some `t`,
   \[
   c(t)\le c_{\rm lo};
   \]
3. **persistent favorable work:** neither loss occurs, and therefore for all such times
   \[
   \boxed{
   W(t)\ge
   \kappa_*\,c_{\rm lo}\,\rho R(0)>0.
   }
   \]

This is simply exhaustive: favorable work cannot disappear while geometry, amplitude and phase alignment all remain favorable.

## 3. Amplitude loss has an exact physical action price

Where `Z != 0`,

\[
\frac{d}{dt}\log R
=\operatorname{Re}\frac{\dot{\mathcal Z}}{\mathcal Z}.
\]

Define channel amplitude actions

\[
A_j=\int_I
\left|
\operatorname{Re}\frac{\dot{\mathcal Z}_j}{\mathcal Z}
\right|dt.
\]

If the amplitude first reaches `rho R(0)`, then

\[
\boxed{
A_{\rm int}+A_{\rm strain}+A_{\rm visc}
\ge \log\frac1\rho.
}
\]

Hence at least one physical channel pays

\[
\boxed{
A_j\ge\frac13\log\frac1\rho.
}
\]

No positive reservoir was invented; this is the exact logarithmic amplitude change of the actual cubic interaction.

## 4. Phase loss has an exact physical action price

Similarly

\[
\dot\vartheta
=\operatorname{Im}\frac{\dot{\mathcal Z}}{\mathcal Z}.
\]

The angular distance between the favorable set `cos theta >= c_hi` and the bad set `cos theta <= c_lo` is

\[
\boxed{
\delta_\vartheta
=\arccos(c_{\rm lo})-\arccos(c_{\rm hi})>0.
}
\]

Define

\[
P_j=\int_I
\left|
\operatorname{Im}\frac{\dot{\mathcal Z}_j}{\mathcal Z}
\right|dt.
\]

At the first phase-loss time,

\[
\boxed{
P_{\rm int}+P_{\rm strain}+P_{\rm visc}
\ge\delta_\vartheta,
}
\]

so at least one channel satisfies

\[
\boxed{
P_j\ge\frac{\delta_\vartheta}{3}.
}
\]

For an exact monochromatic resonant edge `P_visc=0`, so the phase price must be carried by nonlinear transport/stretching descendants.

## 5. Why this is useful and why it is not enough

This theorem upgrades the bridge from a dictionary to a local obstruction:

\[
\boxed{
\text{good geometry + no amplitude payment + no phase payment}
\Rightarrow
\text{persistent positive physical work}.
}
\]

What remains hard is not this trichotomy but converting `A_j` and `P_j` for the **literal localized role operators** into the scale-sensitive physical currencies needed by the two upstream programmes, with no double counting and with moving-cut time faces retained.  A phase action is not by itself a globally bounded reset budget.
