# Cyclic closed-triad work has one common material interaction phase

Status: **Exact Navier--Stokes/helical/material identity.**  This note was triggered by re-auditing current `wang-ns-triad-diamond` HEAD `a55ea1faa192427c22ba4e8141beb8c29bb3f263`, which added the certified cyclic helical-triad donor/recipient kernel.  The bridge below is re-derived from the exact physical edge-work formula and the material interaction 3-form before comparison with that architecture.

No recurrence termination or regularity claim is made.

---

## 1. One closed triad, three physical rootings

Let

\[
k_0+k_1+k_2=0,
\]

with helical signs `s_i in {+1,-1}`.  For a real Navier--Stokes field and a real material area frame `H`, put

\[
\Phi_i=H^T\omega_{k_i}.
\]

Reality gives

\[
\Phi_{-k_i}=\overline{\Phi_i}.
\]

Root the same closed triad at mode `i`, so the child is `q_i=-k_i` and the other two modes are its parents in cyclic order.  The material interaction for root zero is

\[
\mathcal Z_0
=\frac1{\det H}
\overline{\Phi_{-k_0}}\cdot(\Phi_1\times\Phi_2)
=\frac1{\det H}\Phi_0\cdot(\Phi_1\times\Phi_2).
\]

Cyclic invariance of the scalar triple product gives

\[
\boxed{
\mathcal Z_0=\mathcal Z_1=\mathcal Z_2
=: \mathcal Z_\triangle.
}
\]

Thus one closed physical triad has **one common complex interaction amplitude and one common gauge-invariant phase**, independent of which of its three energies is called the child.

**Classification: EXACT NSE/PDE / MATERIAL 3-FORM IDENTITY.**

This is stronger than saying the three works conserve energy.  It says cyclic re-rooting does not rotate the nonlinear interaction phase at all.

---

## 2. The three child-energy works differ only by real root coefficients

The exact physical edge theorem gives, for a resonant child `q` with parents `p,r`,

\[
T=2\frac{s_q}{|q|}
\left(\frac{s_p}{|p|}-\frac{s_r}{|r|}\right)
\operatorname{Re}\mathcal Z.
\]

Define

\[
x_i:=\frac{s_i}{|k_i|}.
\]

For the three cyclic rootings,

\[
\boxed{
\begin{aligned}
T_0&=\kappa_0\operatorname{Re}\mathcal Z_\triangle,
&\kappa_0&=2x_0(x_1-x_2),\\
T_1&=\kappa_1\operatorname{Re}\mathcal Z_\triangle,
&\kappa_1&=2x_1(x_2-x_0),\\
T_2&=\kappa_2\operatorname{Re}\mathcal Z_\triangle,
&\kappa_2&=2x_2(x_0-x_1).
\end{aligned}
}
\]

The coefficients telescope algebraically:

\[
\boxed{
\kappa_0+\kappa_1+\kappa_2=0.
}
\]

Therefore

\[
\boxed{T_0+T_1+T_2=0.}
\]

The nonlinear energy conservation of one closed triad is thus the product of two rigid facts:

1. all roots carry the **same** oriented cubic phase `Z_triangle`;
2. the three real helicity/frequency coefficients sum to zero.

**Classification: EXACT NSE/PDE IDENTITY.**

No norm estimate, capacity, or probabilistic coupling is involved.

---

## 3. Match to the current Wang cyclic donor theorem

The current Wang theorem writes the same three root works in velocity/helical coordinates as

\[
T_i=\lambda_i R_\triangle,
\]

where the `lambda_i` are cyclic differences of `s_j|k_j|` and `R_triangle` is one common real cubic helical factor.  The two coefficient systems are proportional by the same root-independent factor:

\[
\boxed{
\kappa_i
=-\frac{2s_0s_1s_2}{|k_0||k_1||k_2|}\,\lambda_i.
}
\]

Consequently, in the shared physical-work orientation,

\[
\boxed{
R_\triangle
=-\frac{2s_0s_1s_2}{|k_0||k_1||k_2|}
\operatorname{Re}\mathcal Z_\triangle.
}
\]

Thus the Wang common real factor is the velocity/helical coordinate representative of the same common material cubic work factor.  If a different helical-basis sign convention is chosen, both the basis coefficient and this displayed conversion change together while every physical `T_i` remains invariant.

**Classification: EXACT REPRESENTATION CONVERSION after the physical NSE work identity.**

The important invariant content is independent of normalization: there is one common complex `Z_triangle`, while the root choice changes only a real coefficient.

---

## 4. Negative work is not the same thing as bad phase

Because the three `kappa_i` generally have mixed signs while `Z_triangle` is common, the same favorable phase can produce

- positive work at one root,
- negative donor work at another root,
- positive side-recipient work at the third.

Thus

\[
\boxed{
\text{negative child-energy work}
\not\Longleftrightarrow
\text{phase dephasing}.
}
\]

A negative root can be caused entirely by the real helicity/frequency coefficient while the interaction phase is identical to that of a positive root.

**Classification: COUNTEREXAMPLE/NO-GO against identifying backscatter/donor work with phase loss.**

This is why the local phase/work theorem must retain its positive-real-coefficient geometry corridor.  Dropping the sign of `kappa` would misclassify a cyclic energy donor as a dephased interaction.

---

## 5. Donor/recipient routing is same-time redistribution of one cubic event

At fixed triad/time define

\[
P_i=[T_i]_+,
\qquad
N_i=[-T_i]_+.
\]

Since `sum T_i=0`,

\[
\sum_iP_i=\sum_iN_i.
\]

The current Wang donor kernel routes the Hahn-negative root work into the Hahn-positive roots on the same closed triad and same physical time.  The common-phase identity identifies what is being routed:

\[
\boxed{
\text{one }\operatorname{Re}\mathcal Z_\triangle
\times
\text{three real root coefficients}.
}
\]

No new phase source is created by the donor/recipient coupling.  Cyclic re-rooting is a change of **energy owner**, not a change of interaction phase.

**Classification: RIGOROUS CONSEQUENCE.**

This also explains why same-time side-recipient work cannot be treated as recurrence termination.  It is conservative redistribution within the same cubic NSE event; a recipient mode may participate in later interactions.

---

## 6. Refined local owner alternative on a closed triad

On a fixed localized closed-triad packet with good geometry for a chosen root, write

\[
\dot{\mathcal Z}_\triangle
=\sum_o\dot{\mathcal Z}_{\triangle,o}
\]

using the exact localized owner calculus.  The amplitude/phase action theorem applies to the **single common** `Z_triangle`.  At the same time, root work is read through `kappa_i Re Z_triangle`.

Therefore a phase-action payment changes the common interaction phase for all three cyclic roots simultaneously, while a donor/recipient sign difference at one instant can occur with zero phase difference and is charged to the real root coefficients instead.

**Classification: RIGOROUS CONSEQUENCE.**

This separates two mechanisms that should never be merged:

- **phase evolution:** caused by the named localized PDE owners of `Z_triangle`;
- **cyclic energy redistribution at fixed phase:** caused by the root-dependent real helicity/frequency coefficients and exact triad conservation.

That separation is the current Wang bridge contribution.  It does not prove a global donor telescope or recurrence termination.
