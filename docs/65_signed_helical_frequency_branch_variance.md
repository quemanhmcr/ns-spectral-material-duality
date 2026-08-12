# Closed-triad energy transport is a signed-frequency martingale split/merge; enstrophy is its variance ledger

Status: **EXACT NSE / HELICITY-ENERGY IDENTITY**.  This theorem is algebraic on each physical closed helical triad before any norm estimate, packetization, or hard-cell compression.

## 1. Two conserved linear moments on one triad

For a closed helical triad let

\[
x_i=s_i|k_i|,
\qquad s_i\in\{\pm1\},
\]

be the signed helical frequencies.  Current Wang cyclic registration gives

\[
T_0=(x_1-x_2)R_\triangle,
\quad
T_1=(x_2-x_0)R_\triangle,
\quad
T_2=(x_0-x_1)R_\triangle.
\]

The energy identity is

\[
\boxed{T_0+T_1+T_2=0.}
\]

A second exact cancellation is

\[
\boxed{x_0T_0+x_1T_1+x_2T_2=0.}
\]

This is the closed-triad nonlinear helicity conservation law, since modal helicity is signed frequency times modal energy.  Direct expansion cancels every quadratic monomial in the `x_i`.

Thus nonlinear triad transport preserves both

- total energy mass;
- the barycenter of signed helical frequency.

## 2. One donor and two recipients form a martingale split

Suppose one root `d` has negative work and the other two roots `r_1,r_2` have positive work.  Put

\[
Q=N_d=P_{r_1}+P_{r_2},
\qquad
p_j=P_{r_j}/Q.
\]

Then

\[
p_1+p_2=1
\]

and helicity conservation gives

\[
\boxed{p_1x_{r_1}+p_2x_{r_2}=x_d.}
\]

So the signed frequency of the donor is exactly the barycenter of its two recipient frequencies.  The canonical same-time energy split is literally a two-point martingale split in `x`.

The nonlinear squared-frequency/enstrophy work of this triad is

\[
\begin{aligned}
\mathcal V_2
&=\sum_i x_i^2T_i\\
&=Q\left(p_1x_{r_1}^2+p_2x_{r_2}^2-x_d^2\right)\\
&=Q\,p_1p_2(x_{r_1}-x_{r_2})^2.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal V_2
=Q\operatorname{Var}_p(x)
\ge0.}
\]

A one-donor split can only increase the second signed-frequency moment.

## 3. Two donors and one recipient form a martingale merge

Suppose roots `d_1,d_2` are donors and `r` is the unique recipient.  Put

\[
Q=P_r=N_{d_1}+N_{d_2},
\qquad
q_j=N_{d_j}/Q.
\]

Then

\[
\boxed{q_1x_{d_1}+q_2x_{d_2}=x_r.}
\]

The recipient is the barycenter of the two donor signed frequencies.  Therefore

\[
\begin{aligned}
\mathcal V_2
&=Qx_r^2-Q(q_1x_{d_1}^2+q_2x_{d_2}^2)\\
&=-Qq_1q_2(x_{d_1}-x_{d_2})^2,
\end{aligned}
\]

so

\[
\boxed{
\mathcal V_2
=-Q\operatorname{Var}_q(x)
\le0.}
\]

A two-donor merge can only destroy signed-frequency variance.

If one root has exactly zero work, energy plus helicity conservation force the two nonzero-work roots to have the same signed frequency; the second-moment transfer is zero.

## 4. Global nonlinear enstrophy is split variance minus merge variance

Push the exact closed-triad quotient measure through the two sign-pattern classes and define

\[
\mathcal V_{split}(t)
=
\int_{1\to2}
Q_\triangle\operatorname{Var}(x)\,d\Lambda_\triangle,
\]

\[
\mathcal V_{merge}(t)
=
\int_{2\to1}
Q_\triangle\operatorname{Var}(x)\,d\Lambda_\triangle.
\]

Both are nonnegative physical quantities in units of nonlinear enstrophy work.  Theorem BC then sharpens to

\[
\boxed{
\frac12Y'(t)+\nu Z(t)
=
\mathcal V_{split}(t)-\mathcal V_{merge}(t).
}
\]

Therefore at every enstrophy record-growth time,

\[
\boxed{
\mathcal V_{split}
\ge
\nu Z+\mathcal V_{merge}
\ge
\nu Z.}
\]

**Only one-donor branching splits can create nonlinear enstrophy.**  Two-donor merging, however violent its gross energy traffic, acts against enstrophy growth.

## 5. This is stronger than an upward-current slogan

Radial outward energy current and branching variance are related but not identical.

- A split may send one recipient down and one up in physical `|k|` while still increasing signed-frequency variance.
- A merge may contain an individual upward donor-to-recipient atom while the complete triad destroys variance.

Thus the triad variance law sees the **complete energy/helicity-constrained physical event**, not only one rooted edge.

This is why the donor kernel must be reconstructed on the closed triad before assigning an enstrophy owner.

## 6. Binary entropy is already encoded in the same physical split

For a nondegenerate one-donor split with recipient fraction `p` and `1-p`, let

\[
h_2(p)=-p\log p-(1-p)\log(1-p).
\]

The elementary two-point inequality

\[
\boxed{h_2(p)\ge2p(1-p)}
\]

implies

\[
Qh_2(p)
\ge
\frac{2\mathcal V_2}{(x_{r_1}-x_{r_2})^2}.
\]

If a physically typed comparable triad has all `|x_i|<5R`, then `|x_{r_1}-x_{r_2}|<10R`, so

\[
\boxed{
Qh_2(p)
\ge
\frac{\mathcal V_2}{50R^2}.}
\]

This is a **canonical donor-kernel branching entropy**, derived from actual energy/helicity transport.  It is not an analyst cell entropy and is not yet declared a finite global budget.

## 7. Scope

The theorem identifies the exact branching mechanism behind nonlinear enstrophy production.  It does not bound the total split rate, prove non-explosion of the resulting energy genealogy, or establish global regularity.

The next problem becomes sharper: can one-donor signed-frequency martingale splitting produce unbounded second moment before viscous killing, once repeated branch renewal/reuse is treated through the actual PDE state?
