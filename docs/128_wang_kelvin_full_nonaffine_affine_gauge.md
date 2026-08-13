# Wang and Kelvin full non-affine velocity fields are two affine gauges of the same physical defect

Status: **EXACT CROSS-UPSTREAM AFFINE-QUOTIENT IDENTITY / ALL-HIGHER-JET CONSEQUENCE**.

Current Wang and current Kelvin normalize the same physical velocity near a packet/current frame `x=X+Lz`, but they remove the affine part by different rules.  This note identifies the exact relation.  It replaces any need to guess a separate Wang/Kelvin correspondence jet by jet.

## 1. The common normalized physical velocity

Current Wang uses

\[
\boxed{v_W(z)=L^{-1}[u(X+Lz)-\dot X].}
\]

Put

\[
c=L^{-1}[u(X)-\dot X],
\qquad
A_L=L^{-1}(\nabla u(X))L.
\]

Current Kelvin's codeforming non-affinity field is

\[
\boxed{
\mathcal N_L(z)
=L^{-1}[u(X+Lz)-u(X)-(\nabla u(X))Lz].}
\]

Therefore, identically for every smooth physical velocity field,

\[
\boxed{v_W(z)=c+A_Lz+\mathcal N_L(z).}
\]

No Taylor truncation has been used.

## 2. Wang Gaussian affine gauge

Current Wang removes the Gaussian-weighted least-squares affine fit

\[
\bar v,\qquad \bar A
\]

and defines the full non-affine remainder

\[
\boxed{R_W(z)=v_W(z)-\bar v-\bar A z.}
\]

Its gauge conditions are the Gaussian affine orthogonality relations

\[
\int R_W\,d\rho=0,
\qquad
\int R_W z^T\,d\rho=0.
\]

## 3. Kelvin local-Taylor affine gauge

Kelvin instead fixes the affine gauge at the physical anchor:

\[
\boxed{
\mathcal N_L(0)=0,
\qquad
D\mathcal N_L(0)=0.}
\]

The two gauges are generally different.

## 4. Exact affine difference

Substituting the common normalized velocity identity into Wang's remainder gives

\[
\boxed{
R_W(z)-\mathcal N_L(z)
=(c-\bar v)+(A_L-\bar A)z.}
\]

Hence

\[
\boxed{R_W-\mathcal N_L\in\mathrm{Aff}(\mathbb R^3,\mathbb R^3).}
\]

Equivalently,

\[
\boxed{[R_W]_{/\mathrm{Aff}}=[\mathcal N_L]_{/\mathrm{Aff}}.}
\]

This is the exact common full non-affine object of the two programmes.

## 5. Every higher spatial jet agrees automatically

Because the difference is affine,

\[
D^pR_W(z)=D^p\mathcal N_L(z)
\qquad\text{for every }p\ge2.
\]

At the anchor,

\[
\boxed{
D^pR_W(0)
=D^p\mathcal N_L(0)
=L^{-1}(\nabla^pu(X))L^{\otimes p}
=\mathfrak J_p(L),
\qquad p\ge2.}
\]

Thus Kelvin's entire codeforming jet tower and the higher spatial derivatives of Wang's full Gaussian non-affine remainder are already the same physical jets before programme-specific Hermite/moment quotients.

This statement does **not** claim Wang has separately proved a closed packet-normal formula for every `p`.  It only identifies the common physical derivatives of the full remainder field.

## 6. Why `p=2` was the first visible bridge

At `p=2`, the common jet is exactly

\[
B=\mathfrak J_2(L).
\]

Wang then takes a Gaussian tangent quotient and its first genuine transverse packet-shape observable depends on `Sym B`; Kelvin keeps the full `B` inside its codeforming position/area/moment dynamics.

At higher order, the same principle holds at the **input-jet** level, while the programme-specific projections must still be audited theorem by theorem.

## 7. Physical meaning

The two upstream constructions are not using different non-affine physics.  They are choosing different affine reference gauges for the same physical velocity field:

- Wang: best Gaussian affine fit to the grain;
- Kelvin: local value and local gradient at the current anchor.

The quotient by affine motions is common.  What each programme does **after** that quotient remains different and must stay typed separately.
