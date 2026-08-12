# State-map descent and clock mismatch have one exact interface residual

Status: **Exact chain-rule identity for the Kelvin ancestry-to-physical localization bridge.**

The Kelvin upstream currently keeps three objects correctly distinct:

- an ancestry/reverse-age state space `Y` carrying first-bad and moving quantile/shell selectors;
- a physical Kelvin/current state space `X`;
- an as-yet open programme-specific state map from ancestry to physical state.

The previous descent theorem identified when a scalar ancestry selector can even be a physical selector.  This note derives the exact residual that remains after descent but before clock/generator intertwining.

---

## 1. Typed state map and two transport clocks

Let

\[
\Pi_t:Y\to X
\]

be a sufficiently regular time-dependent state map.  Let `b_Y(t,y)` and `b_X(t,x)` be the ancestry/reverse-age and physical transport vector fields in the chosen clock conventions.

For a physical scalar selector `chi_X(t,x)`, define its ancestry pullback

\[
\chi_Y(t,y)=\chi_X(t,\Pi_t(y)).
\]

This formula is meaningful only after the earlier **fiber descent** requirement has been met for a selector originally specified on `Y`.

Define the state-map transport residual

\[
\boxed{
R_\Pi(t,y)
:=
\partial_t\Pi_t(y)
+D\Pi_t(y)b_Y(t,y)
-b_X(t,\Pi_t(y)).
}
\]

Its physical meaning is precise: `R_Pi` is the velocity with which the ancestry realization misses the physical transport after being pushed through the state map.

---

## 2. Exact chain-rule residual

Let

\[
L_Y=\partial_t+b_Y\cdot\nabla_y,
\qquad
L_X=\partial_t+b_X\cdot\nabla_x.
\]

Then the chain rule gives

\[
\boxed{
L_Y(\chi_X\circ\Pi)
-
(L_X\chi_X)\circ\Pi
=
\nabla_x\chi_X(\Pi)\cdot R_\Pi.
}
\]

**Classification: EXACT PDE/STATE-MAP IDENTITY.**

Thus state-map and clock compatibility are not qualitative side conditions.  Every failure of intertwining appears as one explicit localization source.

If

\[
\boxed{R_\Pi=0,}
\]

then ancestry transport and physical transport intertwine exactly for every scalar observable.

Conversely, if the displayed transport identity holds for every smooth scalar `chi_X`, then `R_Pi=0` pointwise; coordinate test functions recover every component.

---

## 3. Hard moving cuts expose only the normal mismatch

Let the physical selector be

\[
\chi_X=1_{\{g(t,x)<a(t)\}}.
\]

Distributionally,

\[
L_X\chi_X
=
\delta_{g=a}
\bigl(\dot a-\partial_tg-b_X\cdot\nabla g\bigr).
\]

Pulling back through `Pi` and using the exact residual gives

\[
\boxed{
L_Y\chi_Y
-
(L_X\chi_X)\circ\Pi
=
-\delta_{g(\Pi)=a}
\nabla g(\Pi)\cdot R_\Pi.
}
\]

Therefore a particular hard interface does not require the full vector residual to vanish.  It requires only

\[
\boxed{
\nabla g(\Pi)\cdot R_\Pi=0
\quad\text{on the interface}.
}
\]

Tangential state-map/clock mismatch merely reparameterizes the interface; the normal component is the true crossing/time-face owner.

**Classification: EXACT DISTRIBUTIONAL INTERFACE IDENTITY.**

This is the state-space analogue of quotienting a common tangential/material motion before charging an interface flux.

---

## 4. A frozen ancestry selector need not be physically frozen

For the literal hysteretic first-bad selector, `Mdot_fb=0` on an unresolved branch in its own germ clock.  That fact alone does not imply zero physical moving-face work after realization.

After descent through `Pi`, the physical face is frozen only if the appropriate normal component of `R_Pi` vanishes.  Otherwise the ancestry label can remain constant while the represented physical support moves across the physical transport.

\[
\boxed{
\dot M_{fb}=0
\not\Rightarrow
\text{zero physical interface owner}
}
\]

without state-map/clock intertwining.

**Classification: COUNTEREXAMPLE/NO-GO against identifying frozen ancestry support with frozen physical support.**

---

## 5. Fixed-mass quantile cancellation remains a different statement

The Kelvin fixed-mass quantile law cancels a weighted **integral** of its own moving face.  The present residual concerns whether that ancestry face is even the pullback of the physical face.

These are logically ordered questions:

1. **descent:** is the selector constant on fibers of `Pi`?
2. **intertwining:** what is `R_Pi`, and in particular its interface-normal component?
3. **mass constraint:** does the resulting ancestry/physical face have zero weighted integral?

A zero integral at step 3 cannot repair a failure at steps 1 or 2.

**Classification: RIGOROUS TYPING CONSEQUENCE.**

---

## 6. Consequence for localized phase/work owners

If a physical localized interaction uses a cut `chi_X`, then an ancestry calculation may be charged to the same physical owner only after descent and the residual identity above are accounted for.

When `R_Pi` has nonzero interface-normal component, the extra term

\[
-\delta_{g(\Pi)=a}\nabla g(\Pi)\cdot R_\Pi
\]

is the exact **state-map/clock mismatch face**.  It is neither viscosity, nor martingale q.v., nor first-bad reset, nor a free observer gauge.

This converts the Kelvin “clock compatibility” frontier into a literal PDE owner.  What remains open upstream is the actual construction of the programme-specific `Pi_t`, `b_Y`, and `b_X` for which the residual can be evaluated.
