# Mixed Cauchy--terminal correlation has an exact connected carré-du-champ source

Status: **Exact connected-semigroup identity for a homogeneous Cauchy payoff.**

After common `SL(3)` deformation is quotiented from the same-replica cubic, the
full-payoff factorization leaves the mixed vectors

\[
r_i=\mathbb E[(D-\bar D)(w_i-\bar w_i)].
\]

This note derives their literal reverse-age source before any estimate.  The theorem
is for a homogeneous fixed-past terminal observable under the same Cauchy/anchor
semigroup.  Localized Navier--Stokes roles add their separately typed source terms
from `docs/26_vorticity_transpose_connection_gauge.md` and the earlier localization
owner calculus.

---

## 1. Three exact connected means

Use the current Kelvin reverse-age operator

\[
\mathcal H_h
=\partial_h+\partial_t+u\cdot\nabla-\nu\Delta.
\]

For the mean deformation,

\[
\boxed{
\mathcal H_h\bar D=A^T\bar D,
\qquad
\bar D(0)=I.
}
\]

Let `w_i` be a fixed-past terminal vector observable transported only by the reverse
anchor Markov semigroup.  Its conditional mean satisfies

\[
\boxed{
\mathcal H_h\bar w_i=0.
}
\]

The homogeneous Cauchy payoff mean

\[
m_i=\mathbb E[D w_i]
\]

has the same Cauchy connection,

\[
\boxed{
\mathcal H_hm_i=A^Tm_i.
}
\]

These are connected semigroup identities; they do not claim that an arbitrary
localized physical vorticity role is homogeneous.

---

## 2. Exact mixed-correlation PDE

Define

\[
\boxed{
r_i=m_i-\bar D\,\bar w_i.
}
\]

The diffusion product rule gives

\[
\mathcal H_h(\bar D\bar w_i)
=(\mathcal H_h\bar D)\bar w_i
+\bar D(\mathcal H_h\bar w_i)
-2\nu\sum_\mu
(\partial_\mu\bar D)(\partial_\mu\bar w_i).
\]

Subtracting from the Cauchy-payoff equation yields

\[
\boxed{
\mathcal H_hr_i
=A^Tr_i
+2\nu\sum_\mu
(\partial_\mu\bar D)(\partial_\mu\bar w_i),
\qquad
r_i(0)=0.
}
\]

**Classification: EXACT CONNECTED CROSS-COVARIANCE IDENTITY.**

The source

\[
\boxed{
\mathcal G_{D,w_i}
=2\nu\sum_\mu
(\partial_\mu\bar D)(\partial_\mu\bar w_i)
}
\]

is the contraction of the full mixed carré-du-champ between deformation and
terminal-vector conditional means.

It is a complex vector in general.  It is not positive, not a metric tensor, and
not determined by `Sigma_D` alone.

---

## 3. Short-horizon onset

At a smooth current point,

\[
\partial_\mu\bar D
=h(\partial_\mu A)^T+O(h^2),
\]

while

\[
\partial_\mu\bar w_i
=\partial_\mu w_i+O(h).
\]

Hence

\[
\mathcal G_{D,w_i}
=2\nu h
\sum_\mu
(\partial_\mu A)^T\partial_\mu w_i
+O(h^2),
\]

and therefore

\[
\boxed{
r_i(h)
=\nu h^2
\sum_\mu
(\partial_\mu\nabla u)^T\partial_\mu w_i
+O(h^3).
}
\]

**Classification: RIGOROUS SHORT-HORIZON CONSEQUENCE.**

The mixed deformation--terminal sector can therefore turn on one order earlier than
the pure deformation covariance/volume defect, because only one deformation
fluctuation has to be accumulated.

---

## 4. Physical role sources must be added, not hidden in the mixed term

If a localized physical leg obeys

\[
\mathcal H_hm_i=A^Tm_i+S_i,
\]

then `S_i` is an explicit role/interface/nonlinear/viscous source and must remain a
separate owner.  The mixed carré-du-champ above records stochastic anchor correlation
between **homogeneous deformation and terminal data**; it must not absorb `S_i` by
notation.

Thus the dynamic phase-capable owner ledger separates

\[
\mathcal G_{D,w_i}
\quad\text{from}\quad
S_i.
\]

**Classification: TYPE SEPARATION.**
