# Parabolic scale progress forces viscous killing, yielding a conditional finite-depth theorem

Status: **EXACT PATHWISE HEAT-CLOCK IDENTITY** plus a **RIGOROUS CONDITIONAL TERMINATION THEOREM**.  This is not yet a Navier--Stokes regularity proof because the literal first-bad event has not been proved to satisfy the hypotheses.

The stopped-lineage budget controls energy-weighted continuation.  A stronger fact appears when the continuation itself is required to remain in the physical parabolic corridor.

## 1. The parabolic coordinate has only two ways to change

Along an alive energy lineage define

\[
\boxed{a(t)=2\nu |k(t)|^2(T-t).}
\]

Between nonlinear transfer events the mode label is fixed, so

\[
\boxed{\dot a=-2\nu|k|^2=-d_k.}
\]

Thus continuous decrease of `a` is exactly the viscous killing hazard density.

At a nonlinear transfer event `i -> j` occurring at fixed physical time,

\[
\boxed{
\Delta a
=(d_j-d_i)(T-t).
}
\]

If the continuation event has actual forward scale progress

\[
|k_j|\ge\lambda |k_i|,
\qquad \lambda>1,
\]

and the donor lies above the parabolic lower face

\[
a_i^-\ge\alpha>0,
\]

then

\[
\boxed{
\Delta a
\ge(\lambda^2-1)\alpha
=:c_{\rm jump}>0.
}
\]

No estimate of the Navier--Stokes nonlinearity is involved.  The jump raises the heat coordinate; physical time plus viscosity are the only continuous mechanism that can lower it again.

## 2. Depth forces cumulative viscous hazard

Suppose one stopped lineage undergoes `n` continuation jumps before exit/killing, every jump satisfying the forward relation above, and suppose the alive lineage remains below a fixed parabolic upper face

\[
0\le a(t)\le\beta.
\]

Let

\[
\mathcal K_n
=\int d_{k(r)}\,dr
=\int 2\nu|k(r)|^2\,dr
\]

be its cumulative viscous killing hazard.  Summing the exact continuous/jump identity gives

\[
a(t)-a(s)
=-\mathcal K_n+\sum_{j=1}^n\Delta a_j.
\]

Hence

\[
\boxed{
\mathcal K_n
\ge n c_{\rm jump}-\beta.
}
\]

Therefore the viscous survival factor on every such depth-`n` path obeys

\[
\boxed{
e^{-\mathcal K_n}
\le e^{\beta}e^{-n c_{\rm jump}}.}
\]

This is the central mechanism: **bounded parabolic state + repeated forward scale jumps forces linear growth of physical killing hazard**.

## 3. Energy mass reaching deep forward depth decays exponentially

Let `M_0` be the total selected energy mass at the root of the stopped lineage.  The un-killed jump process has total path probability at most one, while physical viscosity multiplies each path by its survival factor.  Therefore the total selected energy mass capable of reaching depth at least `n` while staying in the corridor satisfies

\[
\boxed{
M_{\ge n}
\le M_0 e^{\beta-nc_{\rm jump}}.
}
\]

This is a deterministic mass estimate on the exact energy-lineage representation.  It does not count events and does not assign a synthetic reset cost.

## 4. Add a scale-critical physical event floor

Assume a literal continuing physical event at scale `N_j` requires selected-lineage energy

\[
\boxed{N_jE_j\ge\eta>0.}
\]

Assume also the actual continuation scale ratios are bounded on both sides,

\[
\boxed{
1<\lambda
\le\frac{N_{j+1}}{N_j}
\le\Lambda<\infty.
}
\]

Then

\[
N_n\le \Lambda^nN_0,
\]

so any depth-`n` event requires

\[
\boxed{
E_n\ge\frac{\eta}{N_0\Lambda^n}.}
\]

On the other hand the same selected lineage can supply at most

\[
E_n\le M_0 e^{\beta-nc_{\rm jump}}.
\]

If

\[
\boxed{
c_{\rm jump}>\log\Lambda,}
\]

then the two inequalities are incompatible beyond finite depth.  Explicitly,

\[
\boxed{
 n
\le
\frac{
\log(M_0N_0/\eta)+\beta
}{
c_{\rm jump}-\log\Lambda
}
}
\]

whenever the right-hand side is nonnegative.

**Classification: RIGOROUS CONDITIONAL FINITE-DEPTH THEOREM.**

## 5. Signed-good numerical geometry shows the condition is non-vacuous

Current Wang signed-good scale geometry certifies

\[
\frac85<\frac{N_{child}}{N_{parent}}<\frac53.
\]

If one were additionally to prove for the **same physical lineage** a parabolic lower face `a>=alpha`, then

\[
c_{\rm jump}
\ge\left[\left(\frac85\right)^2-1\right]\alpha
=\frac{39}{25}\alpha.
\]

The depth denominator becomes positive once

\[
\boxed{
\alpha>
\frac{25}{39}\log\frac53
\approx0.3274.
}
\]

This calculation is only a compatibility check.  It does **not** import Wang's recursive architecture or prove that the third-repo first-bad state lies in this corridor.

## 6. Why this is closer to a proof mechanism than a bridge dictionary

The theorem has the shape required for actual termination:

\[
\boxed{
\text{forward physical scale progress}
+\text{parabolic state confinement}
\Longrightarrow
\text{exponential viscous survival loss}.
}
\]

A scale-critical event floor then converts survival loss into finite depth.  The missing question is no longer “find a norm estimate.”  It is the literal PDE-definition problem:

> Does every genuinely dangerous first-bad continuation either satisfy this parabolic-lineage criterion, or exit through one of the already named phase/interface/source/reset/reentry owners?

Until that is proved, no recurrence termination or global regularity claim is made.
