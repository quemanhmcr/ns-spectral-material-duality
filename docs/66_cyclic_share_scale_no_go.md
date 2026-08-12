# Cyclic charge share and scale advance alone cannot terminate the local energy lineage

Status: **EXACT COUNTEREXAMPLE / NO-GO**.  This note prevents replacing the branch-variance law by a false scalar contraction.

## 1. A tempting shortcut

For an energy donor `d` and one recipient `r`, let

\[
p_{d\to r}=M_{d\to r}/N_d
\]

be the canonical fraction of that donor's same-time work sent to the recipient.  One might hope that every upward local atom satisfies a scale-contraction law such as

\[
p_{d\to r}\frac{|k_r|}{|k_d|}<1
\]

or even `p lambda^alpha<1` for some universal `alpha>0`.

This is false before additional branch/amplitude information is used.

## 2. Exact homochiral two-donor family

Fix `L>1` and `0<delta<1`, and choose a nondegenerate closed triangle with side magnitudes

\[
r_0=1,
\qquad
r_1=L,
\qquad
r_2=L+\delta.
\]

The strict triangle inequality holds because `delta<1`.  Take all helicities positive, so

\[
x_0=1,
\quad x_1=L,
\quad x_2=L+\delta.
\]

Choose the common phase orientation with `R_triangle>0`.  The exact root works are

\[
T_0=-\delta R_\triangle,
\]

\[
T_1=(L+\delta-1)R_\triangle>0,
\]

\[
T_2=(1-L)R_\triangle<0.
\]

Thus roots `0` and `2` are two donors and root `1` is the **unique recipient**.  The canonical transport table has only one recipient column, so

\[
\boxed{p_{0\to1}=1.}
\]

But

\[
\boxed{|k_1|/|k_0|=L.}
\]

Therefore

\[
\boxed{p_{0\to1}L^\alpha=L^\alpha>1}
\]

for every `alpha>0`.

The Waleffe coupling is nonzero for a nondegenerate triangle; this is a genuine helical-triad geometry, not a zero-work collinear artifact.

## 3. The counterexample already fits the BQ comparable window

Take, for example,

\[
L=16,
\qquad
\delta=1/2.
\]

At radial boundary `R=4`, the three magnitudes are

\[
1,
\quad16,
\quad16.5,
\]

which all lie in

\[
[R/4,5R)=[1,20).
\]

So even inside the corrected BQ comparable branch, a low donor can send **all** its donor charge to a recipient sixteen times higher in frequency.

There is no universal share-times-scale contraction available from cyclic geometry alone.

## 4. What the example is really telling us

The event is not structureless.  It is a **two-donor merge**.  By Theorem BR it destroys, rather than creates, signed-frequency variance.

Thus the failed scalar contraction points directly to the correct object:

- do not follow one rooted upward edge and forget the rest of the triad;
- first classify the whole closed event as `1->2` split or `2->1` merge;
- only split events can fund an enstrophy record.

The geometry-only no-go therefore strengthens the case for the branch-variance ledger rather than reopening an untyped escape.
