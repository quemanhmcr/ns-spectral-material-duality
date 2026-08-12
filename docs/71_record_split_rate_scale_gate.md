# Enstrophy records contain a scale where split-variance production beats that shell's viscous palinstrophy

Status: **RIGOROUS DYADIC RATE LOCALIZATION / EXACT TRIANGLE GEOMETRY**.  The dyadic partition is an analysis registration of the full-state BR measure, not a new physical owner.

## 1. Localize the positive owner by the triad's actual maximum frequency

At a fixed smooth time, assign every one-donor split triad the physical scale

\[
K_\triangle=\max_i|k_i|.
\]

For `N_q=2^q`, let

\[
\mathcal V_q
=
\mathcal V_{split}
\{N_q\le K_\triangle<2N_q\}.
\]

For the modal palinstrophy, let

\[
Z_q
=
\sum_{N_q\le|k|<2N_q,s}|k|^4E_{k,s}.
\]

Then

\[
\sum_q\mathcal V_q=\mathcal V_{split},
\qquad
\sum_qZ_q=Z.
\]

At an enstrophy record BR gives

\[
\sum_q\mathcal V_q
\ge
\nu\sum_qZ_q.
\]

Therefore at least one shell with `Z_q>0` satisfies

\[
\boxed{\mathcal V_q\ge\nu Z_q.}
\]

This is a PDE-derived **rate-critical split scale**.  It uses the actual positive enstrophy owner rather than an abstract bad flag.

## 2. Every triad at that scale has only two frequency geometries

For any nondegenerate closed triangle with largest side `K`, strict triangle inequality gives `K<r_(2)+r_(3)`.  Hence the second-largest side is always greater than `K/2`.  More sharply, if the smallest side is below `K/4`, then the second-largest side is greater than `3K/4`.

Hence every split triad has either

### separated two-high/one-low geometry

\[
\boxed{
\min_i|k_i|<K/4,
\qquad
\text{the other two radii lie in }(3K/4,K],
}
\]

or

### fully comparable geometry

\[
\boxed{
K/4\le |k_i|\le K
\quad\text{for all three roots}.
}
\]

No third scale geometry exists.

Split

\[
\mathcal V_q
=
\mathcal V_q^{sep}
+
\mathcal V_q^{cmp}.
\]

At the rate-critical shell,

\[
\boxed{
\mathcal V_q^{sep}\ge\frac{\nu Z_q}{2}
\quad\text{or}\quad
\mathcal V_q^{cmp}\ge\frac{\nu Z_q}{2}.}
\]

## 3. Variance lower forces actual donor-work rate

For any one-donor split with all `|x_i|<=K_triangle`, the recipient variance is at most `K_triangle^2`: a random variable supported in `[-K,K]` has variance at most `K^2`.  Hence

\[
\mathcal V_{2,\triangle}
=Q_\triangle\operatorname{Var}(x)
\le
K_\triangle^2Q_\triangle.
\]

On the dyadic block `K_triangle<2N_q`,

\[
\boxed{
\mathcal V_{2,\triangle}
<4N_q^2Q_\triangle.}
\]

Let `Q_q^sep`, `Q_q^cmp` be the actual total donor-work masses of the two split classes.  If either class owns half the rate-critical variance, then

\[
\boxed{
Q_q^{owner}
\ge
\frac{\nu Z_q}{8N_q^2}.}
\]

Since

\[
Z_q\ge N_q^4E_q,
\]

where `E_q` is shell kinetic energy,

\[
\boxed{
Q_q^{owner}
\ge
\frac\nu8N_q^2E_q.}
\]

Thus the owner branch supplies actual positive donor work at a fixed fraction of the shell's natural viscous energy rate.

## 4. Physical meaning of the two rate branches

- **Separated split:** two high roots plus one genuinely low root.  This is the exact place for low--high strain/relink versus high--high backreaction analysis.
- **Comparable split:** all three roots lie within a factor four.  This is the exact place for local helical geometry, branch entropy, phase, and physical pair-productivity.

The split is made only after BR has proved that the complete triad is enstrophy-producing.  A two-donor merge never enters either positive branch even if one of its rooted donor-to-recipient atoms crosses upward.

## 5. Scope

The theorem localizes the rate problem but does not bound the duration or number of rate-critical events.  The remaining main question is now sharply typed:

> Can separated or comparable one-donor split work sustain `Q >= c nu N^2 E_N` along a candidate singular sequence without forcing a previously certified strain/reuse/productivity/initial-boundary mechanism?
