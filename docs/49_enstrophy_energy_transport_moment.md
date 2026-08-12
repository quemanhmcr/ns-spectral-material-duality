# Enstrophy production is exactly the first squared-frequency moment of actual energy transport

Status: **EXACT NSE / DONOR-KERNEL MOMENT IDENTITY** and **RIGOROUS PARABOLIC OWNER PARTITION**.

The active-shell theorem localizes nonlinear enstrophy work after the fact.  The donor-kernel representation gives an even more direct physical statement: global enstrophy production is the upward first moment of the same kinetic-energy transport that already carries single-charge donor provenance.

## 1. Enstrophy is a spectral moment of kinetic energy

Let

\[
E_i=\frac12|\widehat u_i|^2,
\qquad
\kappa_i=|k_i|^2.
\]

Then

\[
\boxed{
\frac12Y
=\sum_i\kappa_iE_i,
\qquad
Y=\|\nabla u\|_2^2.
}
\]

The exact donor-kernel energy equation is

\[
\dot E_i
=\sum_jK_{ji}-\sum_jK_{ij}-2\nu\kappa_iE_i.
\]

Multiply by `kappa_i` and sum.  Conservative donor/recipient transport telescopes by its first moment:

\[
\boxed{
\frac12Y'
=
\sum_{i,j}(\kappa_j-\kappa_i)K_{ij}
-2\nu\sum_i\kappa_i^2E_i.
}
\]

Since

\[
Z=\|\Delta u\|_2^2
=2\sum_i\kappa_i^2E_i,
\]

we obtain

\[
\boxed{
\frac12Y'+\nu Z
=
\sum_{i,j}(\kappa_j-\kappa_i)K_{ij}.
}
\]

This is exactly the global nonlinear enstrophy work from `docs/47_record_enstrophy_critical_shell.md`, now disintegrated by actual same-time energy donor/recipient provenance.

**Classification: EXACT NSE / ENERGY-TRANSPORT MOMENT IDENTITY.**

## 2. Record growth requires actual up-frequency energy transport

Define

\[
F_\kappa^+
=\sum_{\kappa_j>\kappa_i}
(\kappa_j-\kappa_i)K_{ij},
\]

and

\[
F_\kappa^-
=\sum_{\kappa_j<\kappa_i}
(\kappa_i-\kappa_j)K_{ij}.
\]

Then

\[
\frac12Y'+\nu Z=F_\kappa^+-F_\kappa^-.
\]

At every enstrophy record-growth time `Y'>=0`,

\[
\boxed{
F_\kappa^+
\ge
\nu Z+F_\kappa^-
\ge\nu Z.
}
\]

Thus positive enstrophy growth literally requires enough kinetic-energy transfer toward larger `|k|^2` to overcome both physical viscosity and any simultaneous down-frequency transfer.

Negative donor work is not renamed dissipation; it is already the source side of the conservative table.  Backscatter appears here only through the sign of the squared-frequency displacement.

## 3. The terminal parabolic coordinate is the same moment in dimensionless units

Fix `T`, `tau=T-t`, and define

\[
a_i=2\nu\tau\kappa_i.
\]

At a same-time nonlinear transfer,

\[
\boxed{
a_j-a_i=2\nu\tau(\kappa_j-\kappa_i).}
\]

Hence the nonlinear drift of the parabolic coordinate is

\[
\boxed{
F_a
:=\sum_{i,j}(a_j-a_i)K_{ij}
=2\nu\tau\left(\frac12Y'+\nu Z\right).
}
\]

At record growth,

\[
\boxed{F_a^+\ge2\nu^2\tau Z.}
\]

The same `a` already governs the physical viscous survival factor in Theorems AU--AX.

## 4. Corridor up-frequency work pays future-heat currency pointwise

Let

\[
w(a)=1-e^{-a}.
\]

For a forward transfer with both endpoint parabolic coordinates in

\[
0\le a_i<a_j\le\beta,
\]

the mean-value theorem gives

\[
\boxed{
\Delta w
=e^{-\xi}(a_j-a_i)
\ge e^{-\beta}(a_j-a_i)
}
\]

for some `xi in (a_i,a_j)`.

Therefore the forward enstrophy-transport moment restricted to a bounded parabolic corridor is controlled by the exact future-heat progress currency:

\[
\boxed{
\sum_{corr}(\kappa_j-\kappa_i)K_{ij}
\le
\frac{e^\beta}{2\nu\tau}
\sum_{corr}(w_j-w_i)K_{ij}.
}
\]

On a stopped one-sided lineage the integral of the right-hand progress is finite by Theorem AT.

## 5. Exact record-owner partition

For any `0<alpha<beta`, split positive up-frequency transport into:

1. **subparabolic**: at least one relevant continuing endpoint lies below `alpha`;
2. **matched corridor**: both lie in `[alpha,beta]`;
3. **superparabolic/nonlocal crossing**: an endpoint lies above `beta` or one jump skips the corridor.

At a record-growth time their positive squared-frequency moments sum to at least `nu Z` plus simultaneous backward moment.

Thus if the corridor sector is bounded by future-heat currency, a candidate singular mechanism must repeatedly force one of the other two physical sectors or another typed phase/interface/reset/relink exit.  This is a routing theorem, not yet a proof that those sectors terminate.

## 6. Why this identity matters for the proof architecture

The new picture separates two questions that were previously mixed:

\[
\boxed{
\text{Why does enstrophy grow?}
\quad\Longleftrightarrow\quad
\text{actual energy moved upward in }|k|^2,
}
\]

while

\[
\boxed{
\text{Can that upward route recur to }T?
\quad\Longleftrightarrow\quad
\text{parabolic killing/corridor/exit analysis}.
}
\]

The first statement is exact.  The second is where the remaining first-bad and mixed-owner work belongs.
