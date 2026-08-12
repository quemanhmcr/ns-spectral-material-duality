# A donor-anchored plateau cutoff binds every genuinely deep pair-creation edge to actual resolved mixed work

Status: **EXACT FOURIER SUPPORT / NSE REPARTITION THEOREM**.  This uses a repo-3 transporter chosen for this theorem; it does not strengthen or modify Wang's cutoff theorem.

## 1. Anchor the dyadic scale to the actual energy donor

For one heterochiral pair-creation event in normal form

\[
-b<a<c,
\]

choose the unique donor dyadic scale `N` with

\[
\boxed{N/2<a\le N.}
\]

Let the high same-helicity recipient belong to

\[
\boxed{M/2<c\le M}
\]

with dyadic `M>N`.

## 2. Choose a literal plateau transporter at the recipient scale

Fix once and for all a smooth radial scalar symbol `s_M(k)` satisfying

\[
\boxed{
s_M(k)=1\quad(|k|\le M/8),
\qquad
s_M(k)=0\quad(|k|\ge M/4),
\qquad
0\le s_M\le1.}
\]

Put

\[
V=S_Mu,
\qquad
h=u-V.
\]

This is a standard smooth Fourier repartition of the actual NSE state.  No causal weight is defined from `S_M`.

## 3. Deep pair creation has one exactly resolved parent

If

\[
\boxed{M\ge8N,}
\]

then

\[
a\le N\le M/8,
\]

so the donor mode lies on the exact plateau:

\[
\boxed{V_a=u_a,\qquad h_a=0.}
\]

The other interaction parent may lie anywhere.

Meanwhile

\[
\operatorname{supp}\widehat V\subset B_{M/4}
\]

implies

\[
\operatorname{supp}\widehat{\mathcal B(V,V)}
\subset B_{M/2}.
\]

Since the recipient hard shell has `c>M/2`, low--low work is exactly absent at that child.

Therefore the physical quadratic source of the deep pair edge is contained entirely in

\[
\boxed{
\mathcal B(V,h)+\mathcal B(h,V),}
\]

the actual resolved mixed operator.  It is **not** a pure-UV HH edge and not a cutoff-transition artefact.

## 4. Shallow remainder has bounded donor/recipient scale ratio

If the deep condition fails,

\[
M<8N.
\]

Using `a>N/2` and `c<=M`,

\[
\boxed{
\frac ca<16.}
\]

Thus every pair-creation event obeys the exact donor-anchored alternative

\[
\boxed{
\text{actual resolved mixed work}
\quad\text{or}\quad
c/a<16.}
\]

There is no arbitrarily nonlocal third branch.

## 5. Energy-side typing of the deep branch

For the mixed linearized operator

\[
\mathcal L_V f=\mathcal B(V,f)+\mathcal B(f,V),
\]

use its exact adjoint split

\[
\mathcal L_V=K_V+S_V,
\qquad
K_V^*=-K_V,
\qquad
S_V^*=S_V.
\]

The positive mixed work on any complete hard-role partition satisfies

\[
W_{mix}^+
\le W_K^++W_S^+.
\]

Hence at least half of a positive deep mixed sublaw is carried by

1. conservative skew role redistribution `K_V`, or
2. symmetric resolved strain/deformation work `S_V`.

The skew branch is same-time redistribution and is donor-traceable inside the complete role system; it is not a new energy source.  The symmetric branch is the existing physical strain owner.

This is the same operator typing used by the upstream resolved-interface quotient, but the **positive binding** here is supplied by the plateau support theorem rather than assumed from contact.

## 6. Consequence for the final owner graph

Genuinely deep heterochiral pair creation no longer remains an untyped UV owner.  After same-event conservative skew tracing, it routes to resolved strain/deformation.  The only pair-creation branch not captured this way has a bounded donor/high-recipient scale ratio `c/a<16`; the pure-UV Wang branch is sharper still (`M=2N`).

No global bound on repeated strain/local alternation is claimed here.
