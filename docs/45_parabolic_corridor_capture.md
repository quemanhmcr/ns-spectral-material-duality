# Bounded physical scale jumps make the parabolic corridor a capture region

Status: **EXACT SCALE-CLOCK KINEMATICS** and **COUNTEREXAMPLE/NO-GO** against skipping the corridor by observer relabeling.

Let

\[
a(t)=2\nu N(t)^2(T-t).
\]

Between physical transfer events the mode/shell label is fixed, so `a` decreases continuously.  At one same-time transfer event,

\[
a^+=\left(\frac{N^+}{N^-}\right)^2a^-.
\]

## 1. Low-to-high crossing cannot skip a wide enough corridor

Assume every typed continuing scale jump obeys the physical upper ratio

\[
\boxed{
\frac{N^+}{N^-}\le\Lambda<\infty.
}
\]

Choose `0<alpha<beta` such that

\[
\boxed{\beta>\Lambda^2\alpha.}
\]

If before a jump

\[
a^-<\alpha,
\]

then

\[
a^+\le\Lambda^2a^-<\Lambda^2\alpha<\beta.
\]

Therefore an upward jump which crosses the lower face `alpha` necessarily lands inside `(alpha,beta)` rather than above the corridor.

Since continuous motion only decreases `a`, every transition from the subparabolic region `a<alpha` to the superparabolic region `a>beta` must visit the corridor.

\[
\boxed{
\text{subparabolic}\to\text{superparabolic}
\quad\Longrightarrow\quad
\text{parabolic-corridor visit}.
}
\]

**Classification: EXACT PARABOLIC CAPTURE KINEMATICS.**

## 2. Why a bound on the physical scale ratio matters

If no upper ratio is available, one jump can send

\[
a^-\ll\alpha
\]

directly to

\[
a^+\gg\beta.
\]

Such a jump is not a failure of the heat coordinate.  It is a genuine nonlocal/ultraviolet transfer and must be typed as its own physical owner.  Current Wang high-tail theory does exactly this rather than pretending that generic HH work has bounded signed-good scale geometry.

**Classification: COUNTEREXAMPLE/NO-GO against universal corridor capture without a scale-locality theorem.**

## 3. Consequence for proof architecture

The capture lemma allows a sharp three-region classification:

1. `a<alpha`: subparabolic continuation;
2. `alpha<=a<=beta`: matched parabolic corridor, where Theorems AT/AU/AV/AX supply finite budgets or terminal exclusion;
3. `a>beta`: superparabolic/high-tail state, which must be handled by physical dissipation/UV ownership rather than silently folded into the corridor.

Thus the remaining first-bad problem is not to estimate every frequency simultaneously.  It is to prove that the actual bad event cannot remain forever in the cheap subparabolic region without the PDE giving a local continuation interval.
