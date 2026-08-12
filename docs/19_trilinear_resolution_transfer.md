# Trilinear carré-du-champ is the exact stochastic transfer owner for reduced cubic phase

Status: **Exact generator/product-rule identity.**

The preceding note identified the cubic resolution object

\[
\Delta_3^{res}=R\mathcal T(\Phi_0,\Phi_1,\Phi_2)
-\mathcal T(R\Phi_0,R\Phi_1,R\Phi_2).
\]

This note derives its evolution before any estimate.  The result is the third-order analogue of the upstream law-of-total-covariance/carré-du-champ transfer identity.

---

## 1. The trilinear carré-du-champ

Let `L` be a Markov diffusion generator and let

\[
\mathcal T(z_0,z_1,z_2)
=\overline{z_0}\cdot(z_1\times z_2).
\]

Define the exact trilinear product defect

\[
\boxed{
\Gamma_L^{(3)}[f_0,f_1,f_2]
:=
L\mathcal T(f_0,f_1,f_2)
-\sum_{i=0}^2
\mathcal T(f_0,\ldots,Lf_i,\ldots,f_2).
}
\]

First-order drift contributes nothing to `Gamma^(3)`.  It is entirely a second-order diffusion cross term.

For

\[
L=b\cdot\nabla+\frac12a^{\alpha\beta}\partial_{\alpha\beta},
\]

with symmetric diffusion tensor `a`, direct product differentiation gives

\[
\boxed{
\begin{aligned}
\Gamma_L^{(3)}
=a^{\alpha\beta}\big[&
\overline{\partial_\alpha f_0}\cdot
((\partial_\beta f_1)\times f_2)\\
&+\overline{\partial_\alpha f_0}\cdot
(f_1\times\partial_\beta f_2)\\
&+\overline{f_0}\cdot
((\partial_\alpha f_1)\times(\partial_\beta f_2))
\big].
\end{aligned}
}
\]

**Classification: EXACT DIFFUSION PRODUCT IDENTITY.**

This is the precise sense in which stochastic q.v. can enter a cubic phase observable: not as a standalone second-order scalar, but as a pair cross-variation **contracted with the third interaction leg**.

---

## 2. Homogeneous cubic resolution transfer

Use horizon operators

\[
\mathfrak H_Y=\partial_\tau-L_Y,
\qquad
\mathfrak H_y=\partial_\tau-L_y.
\]

Suppose the conditional lift intertwines exactly,

\[
\boxed{
\mathfrak H_yR=R\mathfrak H_Y,
}
\]

and each full leg is homogeneous,

\[
\mathfrak H_Y\Phi_i=0.
\]

Then `m_i=R Phi_i` obeys `H_y m_i=0`.  Product differentiation gives

\[
\mathfrak H_Y\mathcal T(\Phi_0,\Phi_1,\Phi_2)
=-\Gamma_{L_Y}^{(3)}[\Phi_0,\Phi_1,\Phi_2],
\]

and similarly for the reduced means.  Therefore

\[
\boxed{
\mathfrak H_y\Delta_3^{res}
=
\Gamma_{L_y}^{(3)}[m_0,m_1,m_2]
-
R\Gamma_{L_Y}^{(3)}[\Phi_0,\Phi_1,\Phi_2].
}
\]

**Classification: EXACT TRILINEAR RESOLUTION-TRANSFER IDENTITY.**

It is structurally parallel to

\[
\mathfrak H_y C_{res}
=\Gamma_y[m]-R\Gamma_Y[\Phi]
\]

for covariance, but it retains the oriented third leg required by signed Navier--Stokes interaction phase.

---

## 3. Inhomogeneous physical sources remain separately typed

Now allow

\[
\mathfrak H_Y\Phi_i=S_i.
\]

Exact intertwining gives

\[
\mathfrak H_y m_i=RS_i.
\]

Define the source-resolution trilinear defect

\[
\boxed{
\begin{aligned}
\mathcal S_3^{res}
:={}&R\Big[
\mathcal T(S_0,\Phi_1,\Phi_2)
+\mathcal T(\Phi_0,S_1,\Phi_2)
+\mathcal T(\Phi_0,\Phi_1,S_2)
\Big]\\
&-\Big[
\mathcal T(RS_0,m_1,m_2)
+\mathcal T(m_0,RS_1,m_2)
+\mathcal T(m_0,m_1,RS_2)
\Big].
\end{aligned}
}
\]

Then

\[
\boxed{
\mathfrak H_y\Delta_3^{res}
=
\mathcal S_3^{res}
+\Gamma_{L_y}^{(3)}[m]
-R\Gamma_{L_Y}^{(3)}[\Phi].
}
\]

**Classification: EXACT SOURCE + DIFFUSION OWNER DECOMPOSITION.**

The terms must not be merged:

- `S_3^res` is hidden-state correlation between physical source action and the other interaction legs;
- the `Gamma^(3)` difference is stochastic pair cross-variation transfer;
- a nonzero kernel intertwining defect `D_R` would be an additional state-map/resolution owner;
- finite first-bad resets remain jumps, not continuous `Gamma^(3)` production.

---

## 4. Common finite-variation deformation and stochastic cross-variation are different owners

The common real incompressible Cauchy generator contributes zero to the pathwise cubic by the `SL(3)` theorem.  That is a **first-order finite-variation** cancellation.

`Gamma^(3)` is instead a **second-order state-diffusion** product term.  It can be nonzero when the interaction-leg observables vary across noisy ancestry/full-state directions.

There is no contradiction:

\[
\boxed{
\text{common Cauchy stretch is phase-neutral,}
\qquad
\text{shared state diffusion may transfer cubic content through }\Gamma^{(3)}.
}
\]

But `Gamma^(3)` still cannot be replaced by covariance alone because its sign/phase depends on how the pair derivative contraction is oriented relative to the third leg.

**Classification: EXACT PHYSICAL TYPE SEPARATION.**

---

## 5. Independent variance replicas are not the same stochastic object

The Kelvin conditional-variance construction branches two independent future replicas after a common ancestor.  Its generator is `L^(1)+L^(2)` with no cross-noise term between replicas.

The trilinear `Gamma^(3)` above concerns three legs that are observables of the **same full stochastic state** before any independent-replica factorization.  Replacing them by independent replicas removes precisely the same-state cross structure and produces the cubic of conditional means discussed in the preceding note.

Thus a phase theorem must not import the variance-replica coupling by analogy.  It must specify whether the physical interaction legs share the full state/noise or are genuinely independent.

**Classification: COUNTEREXAMPLE/NO-GO against untyped replica substitution.**

---

## 6. Refined Kelvin phase-owner ledger

On a fixed typed interval, the continuous owners visible after the current audit are now:

1. relative finite-variation deformation/current generators between interaction legs;
2. physical localization/interface and state-map/kernel intertwining defects;
3. trilinear diffusion cross transfer `Gamma^(3)`;
4. explicit viscosity/nonlinear/source correlations through `S_3^res`;
5. amplitude loss through separately typed physical channels.

Common incompressible Cauchy deformation and orientation-blind frozen first-bad selection are not continuous phase owners.  First-bad reselection/reset is a finite typed stop.

This is still a local owner calculus.  It does not provide a global bank bound, recurrence termination, or regularity theorem.
