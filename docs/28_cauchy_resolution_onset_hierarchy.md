# Smooth fixed-past Cauchy resolution has a rigid h, h^2, h^3 onset hierarchy

Status: **Exact connected identities plus rigorous smooth short-horizon consequences.**

The preceding results expose three different hidden-state mechanisms in a common
Cauchy representation.  Their first allowed short-horizon orders are not the same.
This note derives the hierarchy directly from the reverse-age diffusion product
rules.

---

## 1. Terminal-anchor cubic resolution is generated immediately

Let `w_i` be fixed-past deterministic terminal vector fields and let

\[
\bar w_i=P_h w_i
\]

be their conditional means under the reverse anchor semigroup.  Define

\[
\Delta_w
=P_h\mathcal T(w_0,w_1,w_2)
-\mathcal T(\bar w_0,\bar w_1,\bar w_2).
\]

The first term is a conditional mean of a fixed terminal scalar and therefore is
homogeneous under `H_h`.  Since each `bar w_i` is also homogeneous, the diffusion
product rule gives

\[
\boxed{
\mathcal H_h\Delta_w
=\mathcal G_w^{(3)},
}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal G_w^{(3)}
=2\nu\sum_\mu\big[&
\mathcal T(\partial_\mu\bar w_0,
           \partial_\mu\bar w_1,
           \bar w_2)\\
&+\mathcal T(\partial_\mu\bar w_0,
             \bar w_1,
             \partial_\mu\bar w_2)\\
&+\mathcal T(\bar w_0,
             \partial_\mu\bar w_1,
             \partial_\mu\bar w_2)
\big].
\end{aligned}
}
\]

This is the reverse-anchor specialization of the trilinear carré-du-champ theorem.
It is complex and can rotate phase.

At `h=0`,

\[
\boxed{
\Delta_w(h)
=2\nu h\sum_\mu
\big[
\mathcal T(\partial_\mu w_0,\partial_\mu w_1,w_2)
+\mathcal T(\partial_\mu w_0,w_1,\partial_\mu w_2)
+\mathcal T(w_0,\partial_\mu w_1,\partial_\mu w_2)
\big]
+O(h^2).
}
\]

**Classification: EXACT PDE IDENTITY / RIGOROUS `O(nu h)` CONSEQUENCE.**

---

## 2. Mixed deformation--terminal correlation starts one integration later

From the exact mixed law,

\[
\boxed{
r_i(h)
=\nu h^2
\sum_\mu
(\partial_\mu A)^T\partial_\mu w_i
+O(h^3).
}
\]

Thus the corresponding mixed cubic polynomial `C_D-w` can generically enter at
order

\[
\boxed{O(\nu h^2).}
\]

It is also complex and phase capable.

---

## 3. Pure deformation exterior-volume resolution starts at cubic horizon order

The mean-deformation determinant theorem gives

\[
\boxed{
1-\det\bar D
=-\frac{\nu h^3}{3}
\sum_\mu\operatorname{tr}((\partial_\mu A)^2)
+O(h^4).
}
\]

Hence the pure common-deformation exterior-volume contribution starts at

\[
\boxed{O(\nu h^3)}
\]

and is radial while `det bar D>0`.

---

## 4. The hierarchy

Whenever the displayed leading coefficients do not vanish by symmetry, the first
possible onsets are

\[
\boxed{
\begin{array}{ccl}
O(\nu h)   &:& \text{terminal-anchor cubic resolution }\Delta_w,\\
O(\nu h^2) &:& \text{deformation--terminal mixed correlation }r_i,\\
O(\nu h^3) &:& \text{pure deformation exterior-volume defect }1-\det\bar D.
\end{array}
}
\]

This is not a hierarchy of norm sizes for long times.  It is a local causal-order
statement forced by the actual mechanisms:

1. Brownian anchor branching can separate terminal values immediately;
2. one reverse-age integration of spatially varying strain is needed before
   deformation can correlate with terminal variation;
3. two deformation fluctuations are needed before pure deformation covariance can
   feed the mean exterior volume.

**Classification: RIGOROUS STRUCTURAL CONSEQUENCE.**

Special geometries can annihilate any leading coefficient and postpone that owner;
the theorem does not assert lower bounds.

---

## 5. Refined phase frontier

For a smooth fixed-past homogeneous Cauchy sector, common deformation is therefore
not the first stochastic place to look for phase rotation.  The earliest phase
owner is the same-anchor terminal cubic resolution.  Mixed deformation--terminal
correlation comes next.  Pure deformation dispersion is later and radial at its
first exterior-volume appearance.

For actual localized Navier--Stokes roles, explicit interface, nonlinear, viscous,
clock and reset sources must be superposed according to their own exact PDE laws.
No recurrence or regularity conclusion follows from the local hierarchy alone.
