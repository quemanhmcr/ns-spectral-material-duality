# First-bad entry and resolve events carry an exact finite complex cubic jump

Status: **Exact event/reweighting identity.**

The local phase/work theorem deliberately stops at hard reselection and first-bad
reset because those are finite typed events, not smooth source densities.  The
reset need not remain an unspecified black box, however: once the physical event
selector is legitimate, its instantaneous effect on the selected complex cubic can
be written exactly.

---

## 1. Unnormalized selected cubic jump

At one physical event time hold the underlying full-state interaction observable
fixed and let

\[
\mathcal Z(Y)\in\mathbb C
\]

be the same-state oriented cubic.  Let the scalar event weights immediately before
and after the selector event be

\[
\chi^-(Y),\qquad \chi^+(Y).
\]

Define

\[
Z^\pm=\mathbb E[\chi^\pm\mathcal Z],
\qquad
\Delta\chi=\chi^+-\chi^-.
\]

Then exactly

\[
\boxed{
Z^+-Z^-
=\mathbb E[\Delta\chi\,\mathcal Z].
}
\]

**Classification: EXACT FINITE EVENT IDENTITY.**

There is no time derivative and no positive density.  This is the complex
interaction carried by the states added to or removed from the selected event law.

---

## 2. Exact normalized selected-law jump

Let

\[
\alpha^\pm=\mathbb E\chi^\pm>0,
\qquad
\widehat Z^\pm=\frac{Z^\pm}{\alpha^\pm}.
\]

Using `alpha^+=alpha^-+E Delta chi`, one obtains

\[
\boxed{
\widehat Z^+-\widehat Z^-
=
\frac{\mathbb E[\Delta\chi\,(\mathcal Z-\widehat Z^-)]}
{\alpha^+}.
}
\]

Thus the normalized event jump is the reweighting correlation between selector
change and deviation from the old selected interaction mean.

**Classification: EXACT CONDITIONAL REWEIGHTING IDENTITY.**

---

## 3. The phase jump is a discrete owner, not continuous phase action

If both selected cubics are nonzero, define the principal finite event phase jump

\[
\boxed{
\Delta\theta_{\rm evt}
=\operatorname{Arg}\left(\frac{\widehat Z^+}{\widehat Z^-}\right).
}
\]

Likewise the finite logarithmic amplitude change is

\[
\boxed{
\Delta a_{\rm evt}
=\log\frac{|\widehat Z^+|}{|\widehat Z^-|}.
}
\]

These are exact event data.  Neither has a fixed sign and neither is automatically
bounded by a pre-existing positive reservoir.

Therefore a first-bad reset can change phase abruptly, but that jump must be
recorded as a **finite selection/reweighting face**, not integrated into the smooth
phase-action density from a neighboring interval.

**Classification: EXACT EVENT TYPING / NO-GO against continuous smearing.**

---

## 4. Common Cauchy deformation still cancels through the event

If

\[
\mathcal Z(Y)
=\mathcal T(Dw_0,Dw_1,Dw_2),
\qquad
D\in SL(3),
\]

then pathwise

\[
\mathcal Z(Y)=\mathcal T(w_0,w_1,w_2).
\]

Hence

\[
\boxed{
\mathbb E[\Delta\chi\,\mathcal T(Dw_0,Dw_1,Dw_2)]
=
\mathbb E[\Delta\chi\,\mathcal T(w_0,w_1,w_2)].
}
\]

So even at a finite first-bad entry/resolve event, common incompressible Cauchy
deformation is not the reset phase owner.  The jump comes from which terminal/role
hidden states are reweighted.

**Classification: EXACT CAUCHY / EVENT IDENTITY.**

---

## 5. Extended typed phase/work ledger

The local interaction history can now be decomposed without pretending resets are
smooth:

\[
\text{continuous typed interval}
\to
\text{finite event jump}
\to
\text{new continuous typed interval}.
\]

On each continuous interval, the existing owner-resolved amplitude/phase action
calculus applies.  At the event, the exact `Delta chi` formula above applies.  The
post-event role must then be re-registered before the next continuous theorem.

This extends the ledger across selector events, but it does **not** prove that the
sum of finite jumps is bounded, terminates, or yields recurrence/regularity.
