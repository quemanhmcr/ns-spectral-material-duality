# Cauchy replica averaging has an exact exterior-volume resolution defect

Status: **Exact stochastic-Cauchy / exterior-algebra identity.**

This note re-audits the current Kelvin upstream at
`c1773ffa8fa5cc4bfa8fb5aa461dd4b43dbed1c1`, where the full vectorized stochastic
Cauchy-deformation covariance

\[
\Sigma_D=\operatorname{Cov}(\operatorname{vec}D)
\]

and its connected reverse-age PDE are now literal.  The bridge below is derived
from the incompressible Cauchy deformation itself.  It does not identify the
upstream deterministic first-bad packet with a stochastic replica, and it does not
modify either upstream repository.

---

## 1. Same replica and independent replicas are different cubic objects

Fix one current physical state and one reverse-age horizon.  Let the real random
Cauchy deformation satisfy

\[
D\in SL(3),\qquad \det D=1\quad\text{pathwise},
\]

and let

\[
\bar D=\mathbb E D.
\]

For fixed complex terminal vectors `z_0,z_1,z_2`, define the oriented cubic

\[
\mathcal T(z_0,z_1,z_2)
=\overline{z_0}\cdot(z_1\times z_2),
\qquad
\mathcal Z_0=\mathcal T(z_0,z_1,z_2).
\]

If all three legs use the **same stochastic replica**, then reality of `D` and the
ordinary determinant law give pathwise

\[
\mathcal T(Dz_0,Dz_1,Dz_2)
=\det(D)\,\mathcal Z_0
=\mathcal Z_0.
\]

Therefore

\[
\boxed{\mathcal Z_{\rm same}=\mathcal Z_0.}
\]

If instead three replicas are conditionally independent and one forms the cubic of
the three conditional means, then

\[
m_i=\mathbb E[Dz_i]=\bar D z_i,
\]

so

\[
\boxed{
\mathcal Z_{\rm ind}
=\mathcal T(\bar Dz_0,\bar Dz_1,\bar Dz_2)
=\det(\bar D)\,\mathcal Z_0.
}
\]

Hence the exact exterior-volume resolution defect is

\[
\boxed{
\Delta_{\Lambda^3}
:=\mathcal Z_{\rm same}-\mathcal Z_{\rm ind}
=(1-\det\bar D)\,\mathcal Z_0.
}
\]

**Classification: EXACT STOCHASTIC / MATERIAL 3-FORM IDENTITY.**

This is the stochastic-Cauchy specialization of the conditional cubic-resolution
theorem.  It makes the missing coupling completely explicit in the sector where
the terminal vectors themselves are not random.

---

## 2. Expectation does not commute with the top exterior power

The identity can be written invariantly as

\[
\boxed{
\mathbb E[\Lambda^3D]=1,
\qquad
\Lambda^3(\mathbb ED)=\det\bar D.
}
\]

Thus

\[
1-\det\bar D
\]

is not pathwise volume change.  Every replica is exactly volume preserving.  It is
the failure of **averaging replicas first** to commute with the physical top
exterior power.

The physical type is therefore:

> conditional/replica exterior-volume resolution, not compressibility and not
> pathwise Cauchy volume production.

**Classification: EXACT TYPE IDENTITY.**

---

## 3. Pure common-deformation dispersion is radial, not a continuous phase owner

Set

\[
J_D:=\det\bar D\in\mathbb R.
\]

Then

\[
\mathcal Z_{\rm ind}=J_D\mathcal Z_0.
\]

On every interval on which `J_D>0`,

\[
\boxed{
\arg\mathcal Z_{\rm ind}=\arg\mathcal Z_0.
}
\]

Thus stochastic dispersion of a **common real incompressible deformation** can
change the amplitude of the independent-replica cubic without producing any
continuous `U(1)` phase velocity.

If `J_D` changes sign, continuity forces it through zero first.  Therefore the
independent-replica cubic loses all amplitude before acquiring the possible `pi`
orientation flip.

\[
\boxed{
\text{common real deformation dispersion}
\Longrightarrow
\text{amplitude-resolution before any sign flip, not continuous phase rotation}.
}
\]

**Classification: RIGOROUS CONSEQUENCE.**

This places the pure common-deformation replica defect in the amplitude branch of
the local phase/work alternative.  It cannot be charged as phase action merely
because deformation covariance is nonzero.

---

## 4. Central-moment anatomy of the volume defect

Write the random columns as

\[
d_j=\bar d_j+\xi_j,
\qquad
\mathbb E\xi_j=0.
\]

Since `det D=1` pathwise, multilinearity gives the exact decomposition

\[
\boxed{
\begin{aligned}
1-\det\bar D
={}&\mathbb E\det(\xi_1,\xi_2,\bar d_3)
+\mathbb E\det(\xi_1,\bar d_2,\xi_3)\\
&+\mathbb E\det(\bar d_1,\xi_2,\xi_3)
+\mathbb E\det(\xi_1,\xi_2,\xi_3).
\end{aligned}
}
\]

The first three terms are oriented contractions of cross-column second moments,
which are contained in the full `9 x 9` deformation covariance `Sigma_D`.  The
last term is a genuinely third-centered deformation moment.

So even though the **total** defect is already known from the first moment `bar D`,
its hidden-state anatomy is not a scalar covariance.  The pathwise `SL(3)`
constraint couples pair-resolution and third-order resolution exactly.

**Classification: EXACT CENTRAL-MOMENT IDENTITY.**

---

## 5. Scope

For the full stochastic Cauchy payoff

\[
Y_i=D\,w_i(A_s),
\]

the terminal vectors can themselves vary with the random anchor and can be
correlated with `D`.  Pathwise common deformation still cancels:

\[
\mathcal T(Dw_0,Dw_1,Dw_2)
=\mathcal T(w_0,w_1,w_2),
\]

but the conditional cubic then contains the terminal/role resolution terms already
identified in Theorems S--T.  Those terms can rotate phase.

Therefore the theorem above is deliberately sharp rather than universal:

- common real Cauchy deformation alone is phase-neutral pathwise;
- averaging that deformation before a cubic creates the real exterior-volume factor
  `det bar D`;
- genuine continuous phase rotation requires terminal/role variability, relative
  generators, localization/interface sources, explicit forcing/viscosity, or a typed
  reset.

No recurrence, continuation, or regularity conclusion is made.
