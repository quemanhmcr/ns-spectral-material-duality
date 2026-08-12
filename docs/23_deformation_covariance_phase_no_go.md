# Deformation covariance and cubic phase are non-equivalent physical owners

Status: **Exact no-go plus an exact Navier--Stokes calibration inherited from the literal Cauchy deformation law.**

The current Kelvin upstream supplies an exact one-mode periodic Navier--Stokes shear
for which stochastic Cauchy deformation covariance is strictly positive.  Combined
with the exterior-volume identities in `docs/21_cauchy_exterior_volume_resolution.md`,
this produces a sharp separation between metric spread and cubic phase.

---

## 1. Exact shear: positive deformation covariance, zero exterior-volume defect

For the exact periodic shear

\[
u=(e^{-\nu k^2t}\cos ky,0,0),
\]

the stochastic Cauchy deformation has the exact form

\[
D_h=I+c_hE_{21}.
\]

Hence every replica is in `SL(3)` and

\[
\bar D=I+\bar c_hE_{21}
\]

also satisfies

\[
\boxed{\det\bar D=1}
\]

for every horizon and anchor.

At the symmetry anchor `y=0`, the upstream exact formula gives

\[
\bar D=I,
\]

while

\[
\operatorname{Var}(c_h)>0
\]

for every `h>0`.  Thus

\[
\boxed{
\Sigma_D>0,
\qquad
C_D^{\rm Gram}>0,
\qquad
\delta_D=1-\det\bar D=0.
}
\]

For any fixed terminal interaction triple,

\[
\boxed{
\mathcal Z_{\rm same}
=\mathcal Z_{\rm ind}
=\mathcal Z_0
}
\]

although stochastic deformation replicas genuinely disperse and the mean packet
metric differs from the deterministic selected metric.

**Classification: COUNTEREXAMPLE/NO-GO.**

Therefore

\[
\boxed{
\text{nonzero full deformation covariance}
\not\Rightarrow
\text{cubic amplitude loss or phase rotation}.
}
\]

---

## 2. Metric mismatch is not phase mismatch

The literal same-replica metric identity is

\[
\rho^4\mathbb E[M_H]
=\bar D\bar D^T+C_D^{\rm Gram}.
\]

The shear has `C_D^Gram>0`, so the mean stochastic packet metric differs from the
metric built from the mean deformation and from the deterministic symmetry-line
packet.  Yet the top exterior interaction is unchanged.

Thus the following three statements are distinct:

\[
\text{replicas have different metrics},
\qquad
\text{mean metric differs from selected metric},
\qquad
\text{cubic phase/work changes}.
\]

Neither of the first two implies the third.

**Classification: RIGOROUS CONSEQUENCE / TYPE SEPARATION.**

---

## 3. The exact exterior hierarchy

For common real stochastic deformation there are now three literal levels:

\[
\begin{aligned}
&\text{pathwise volume:} &&\Lambda^3D=1,\\
&\text{mean-deformation volume:} &&\Lambda^3\bar D=\det\bar D,\\
&\text{metric spread:} &&\rho^4\mathbb E[M_H]-\bar D\bar D^T=C_D^{\rm Gram}.
\end{aligned}
\]

The last line is second-order and positive semidefinite.  The middle line is cubic,
real, and governed by an indefinite determinant Hessian contraction.  The first
line is exactly fixed by incompressibility.

This hierarchy is not an analyst-imposed decomposition.  It is forced by the three
ways Navier--Stokes deformation enters line, metric, and oriented-volume geometry.

**Classification: EXACT STRUCTURAL CONSEQUENCE.**

---

## 4. Refined phase-owner ledger

In the fixed-terminal common-deformation sector, `Sigma_D` belongs to deformation
resolution and packet-metric spread.  Its exterior contraction `delta_D` belongs to
cubic **amplitude** resolution while `det bar D>0`.  Neither is a continuous phase
owner.

Continuous phase rotation can still occur when the actual localized Navier--Stokes
legs are not common fixed vectors: hidden terminal field variation, role-dependent
localization, relative Cauchy/current generators, moving interfaces, viscosity or
other explicit sources feed the third-order resolution law from Theorem T.

Hence the physically typed statement is

\[
\boxed{
\text{common deformation dispersion}
\neq
\text{relative interaction-phase dynamics}.
}
\]

The latter begins only after common real deformation has been quotiented.

---

## 5. Consequence for selected-support / replica alignment

The deterministic first-bad packet cannot be identified with a stochastic replica
ensemble merely because their material metrics use the same Nanson geometry.
Even if one chooses the mean deformation `bar D` as a deterministic representative,

\[
\rho^4\mathbb E[M_H]
=\bar D\bar D^T+C_D^{\rm Gram}
\]

retains a covariance face.  Meanwhile cubic interaction sees `det bar D`, not the
metric correction itself.

Therefore a future selected-support coupling theorem must state separately which
object is transported:

- a single replica;
- mean deformation;
- mean packet metric;
- same-state cubic interaction;
- or a reduced conditional kernel carrying explicit second- and third-order
  resolution faces.

No equality among these objects is inferred by analogy.  No recurrence or
regularity conclusion is made.
