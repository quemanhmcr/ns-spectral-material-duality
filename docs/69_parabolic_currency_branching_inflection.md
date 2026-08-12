# The unique future-heat defect changes branching curvature exactly at the parabolic half-face

Status: **EXACT DIFFERENTIAL GEOMETRY / RIGOROUS LOCAL JENSEN CONSEQUENCE**.  This theorem links the unique parabolic currency to the signed-frequency branch law; it does not create a new global budget.

## 1. Read the unique defect as a function of signed helical frequency

Fix terminal time `T` and write `tau=T-t>0`.  The unique bounded unit-killing energy coordinate from Theorem BD is

\[
w_\tau(x)=1-e^{-2\nu\tau x^2}.
\]

Put

\[
a=2\nu\tau x^2.
\]

Direct differentiation gives

\[
\boxed{
w_\tau''(x)
=4\nu\tau e^{-a}(1-2a).
}
\]

Therefore

\[
\boxed{
\begin{array}{ll}
a<1/2:&w_\tau\text{ is strictly convex},\\
a=1/2:&w_\tau''=0,\\
a>1/2:&w_\tau\text{ is locally concave along a same-sign branch}.
\end{array}}
\]

The number `1/2` is forced by the unique NSE heat/killing coordinate; it is not a chosen threshold.

## 2. Sub-half-face split variance must increase the heat-defect observable

Consider a one-donor split whose donor and both recipient signed frequencies obey

\[
2\nu\tau x_i^2\le\alpha<1/2.
\]

The entire interval between the two recipient signed frequencies lies inside the convex region.  Since

\[
e^{-a}(1-2a)
\ge e^{-\alpha}(1-2\alpha),
\]

we have

\[
w_\tau''\ge
4\nu\tau e^{-\alpha}(1-2\alpha).
\]

Applying the strong-convexity gap to BR gives the exact lower

\[
\boxed{
Q\left[
\mathbb E_p w_\tau(x_r)-w_\tau(x_d)
\right]
\ge
2\nu\tau e^{-\alpha}(1-2\alpha)
\,\mathcal V_2.
}
\]

Thus every entirely sub-half-face martingale split converts a definite fraction of its signed-frequency variance production into the unique future-heat defect currency.

## 3. Merge has the opposite convex-order sign

For a two-donor merge staying in the same sub-half-face region,

\[
\boxed{
Q\left[
w_\tau(x_r)-\mathbb E_qw_\tau(x_d)
\right]
\le
-2\nu\tau e^{-\alpha}(1-2\alpha)
\,|\mathcal V_2|.
}
\]

So subparabolic split/merge events move the unique heat defect in the same positive/negative orientation as enstrophy variance.

## 4. Why the half-face matters and why it does not solve recurrence

The same numerical face `a=1/2` appeared independently in Theorem BF: an old matched population with lower face `alpha>1/2` decays too rapidly to carry the standard `H^1` blow-up lower rate.  Here `1/2` is the exact inflection of the unique parabolic defect under martingale branching.

This is a structural alignment, but not a proof that all relevant triads remain on one side of the inflection.  Wide/opposite-sign splits can cross regions of different curvature, and repeated split/merge cycles can recycle the bounded defect.  The theorem therefore identifies the correct local geometry without promoting it to a global reset.
