# Cauchy deformation dispersion splits into strain-gradient, vorticity-gradient, and orientation-coupling geometry

Status: **Exact short-horizon Navier--Stokes/Cauchy algebra and rigorous consequence.**

The current Kelvin vectorized Cauchy law gives

\[
C_D^{\rm Gram}(h)
=\frac{2\nu}{3}h^3
\sum_\mu(\partial_\mu A)^T(\partial_\mu A)
+O(h^4),
\qquad
A=\nabla u.
\]

The mean-deformation exterior-volume theorem gives

\[
1-\det\bar D
=-\frac{\nu h^3}{3}
\sum_\mu\operatorname{tr}((\partial_\mu A)^2)
+O(h^4).
\]

These expressions can be resolved into actual strain-gradient and
vorticity-gradient geometry before any norm estimate.

---

## 1. Differentiate the physical strain/rotation split

Write

\[
A=S+\Omega,
\qquad
S^T=S,
\qquad
\Omega^T=-\Omega.
\]

For incompressible three-dimensional flow,

\[
2\Omega=A-A^T=[\omega]_\times.
\]

For each spatial direction `mu` define

\[
P_\mu:=\partial_\mu S,
\qquad
Q_\mu:=\partial_\mu\Omega
=\frac12[\partial_\mu\omega]_\times.
\]

Then

\[
\partial_\mu A=P_\mu+Q_\mu.
\]

This is a physical split: `P_mu` is strain-gradient variation and `Q_mu` is
rotation/vorticity-gradient variation.

---

## 2. Exact row-Gram covariance decomposition

Because `P_mu` is symmetric and `Q_mu` skew,

\[
\boxed{
(\partial_\mu A)^T(\partial_\mu A)
=P_\mu^2-Q_\mu^2+(P_\mu Q_\mu-Q_\mu P_\mu).
}
\]

The three pieces have different types:

- `P_mu^2` is positive semidefinite strain-gradient dispersion;
- `-Q_mu^2` is positive semidefinite rotation-gradient dispersion;
- `P_mu Q_mu-Q_mu P_mu` is symmetric and trace free, an orientation-coupling
  sector with no fixed sign.

Thus the leading Cauchy row-Gram covariance is

\[
\boxed{
C_D^{\rm Gram}
=C_S+C_\Omega+C_{S\Omega}+O(h^4)
}
\]

with

\[
C_S=\frac{2\nu h^3}{3}\sum_\mu P_\mu^2,
\]

\[
C_\Omega=-\frac{2\nu h^3}{3}\sum_\mu Q_\mu^2,
\]

\[
C_{S\Omega}=\frac{2\nu h^3}{3}\sum_\mu(P_\mu Q_\mu-Q_\mu P_\mu).
\]

**Classification: EXACT MATRIX ALGEBRA / RIGOROUS SHORT-HORIZON CONSEQUENCE.**

The total is PSD because it is the Gram matrix of the full velocity-gradient
variation.  Its physical subpieces need not each behave like scalar reservoirs.

---

## 3. Rotation-gradient dispersion is the transverse complement of Kelvin q.v.

For any vector `g`,

\[
-[g]_\times^2
=|g|^2I-gg^T.
\]

Since

\[
Q_\mu=\frac12[\partial_\mu\omega]_\times,
\]

one obtains

\[
\boxed{
C_\Omega(h)
=\frac{\nu h^3}{6}
\left[
|\nabla\omega|^2I
-(\nabla\omega)(\nabla\omega)^T
\right]
+O(h^4).
}
\]

The instantaneous physical Kelvin q.v. tensor in an orthonormal orientation frame
is

\[
\boxed{
\Gamma_K
=2\nu(\nabla\omega)(\nabla\omega)^T.
}
\]

Therefore

\[
\boxed{
C_\Omega(h)
=\frac{h^3}{12}
\left[(\operatorname{tr}\Gamma_K)I-\Gamma_K\right]
+O(h^4).
}
\]

**Classification: EXACT CROSS-DICTIONARY SHORT-HORIZON IDENTITY.**

There is a sharper exterior-algebra reading.  For any linear map `G` on `R^3`,
the induced Lie-algebra action on two-vectors satisfies, after Hodge identifying
`Lambda^2 R^3` with `R^3`,

\[
\boxed{
*\,G^{[2]}\,*^{-1}
=(\operatorname{tr}G)I-G^T.
}
\]

Since `Gamma_K` is symmetric,

\[
\boxed{
C_\Omega(h)
=\frac{h^3}{12}
*\,\Gamma_K^{[2]}\,*^{-1}
+O(h^4).
}
\]

Thus the rotation-gradient part of Cauchy deformation dispersion is literally the
**Hodge/exterior-square lift** of the Kelvin q.v. tensor at leading order.  Kelvin
q.v. records the directions occupied by vorticity-gradient variation on vectors;
Cauchy rotation-gradient dispersion records the induced complementary action on
material two-plane geometry.  They are related by exterior algebra, not by scalar
identification.

**Classification: EXACT 3D HODGE / LAMBDA^2 REPRESENTATION IDENTITY.**

---

## 4. Exterior-volume onset is strain-gradient versus vorticity-gradient competition

The trace relevant to the determinant has a different algebra.  Since the trace of
a symmetric-skew product vanishes,

\[
\operatorname{tr}((P_\mu+Q_\mu)^2)
=\operatorname{tr}(P_\mu^2)+\operatorname{tr}(Q_\mu^2).
\]

Moreover

\[
\operatorname{tr}(P_\mu^2)=|P_\mu|_F^2,
\]

and

\[
\operatorname{tr}(Q_\mu^2)
=-\frac12|\partial_\mu\omega|^2.
\]

Hence

\[
\boxed{
1-\det\bar D
=
\frac{\nu h^3}{6}|\nabla\omega|^2
-
\frac{\nu h^3}{3}
\sum_\mu|\partial_\mu S|_F^2
+O(h^4).
}
\]

Equivalently, using the Kelvin q.v. tensor,

\[
\boxed{
1-\det\bar D
=
\frac{h^3}{12}\operatorname{tr}\Gamma_K
-
\frac{\nu h^3}{3}|\nabla S|_F^2
+O(h^4).
}
\]

**Classification: RIGOROUS SHORT-HORIZON NSE CONSEQUENCE.**

This explains the indefinite determinant source physically.  Vorticity-gradient
variation pushes the mean exterior-volume defect in one direction; strain-gradient
variation pushes it in the opposite direction.  No positive covariance
interpretation can retain this sign competition.

---

## 5. Exact one-mode shear explains its zero exterior-volume defect

For

\[
u=(E(t)\cos ky,0,0),
\]

let `c=partial_y^2 u_1`.  The only nonzero velocity-gradient derivative is

\[
\partial_y A_{12}=c.
\]

The strain-gradient matrix has off-diagonal entries `c/2`, so

\[
\boxed{|\partial_yS|_F^2=\frac12c^2.}
\]

The vorticity derivative has magnitude

\[
\boxed{|\partial_y\omega|^2=c^2.}
\]

Therefore

\[
\boxed{
|\nabla\omega|^2
=2|\nabla S|_F^2
}
\]

and the two exterior-volume onset terms cancel exactly.  This is the local
gradient explanation for the stronger exact fact

\[
\det\bar D=1
\]

at every horizon in the shear family.

**Classification: EXACT NAVIER--STOKES CALIBRATION.**

---

## 6. The shear covariance direction requires the cross sector

For the same shear, the strain-gradient and rotation-gradient PSD pieces each
occupy the active `x-y` plane.  Their symmetric trace-free coupling
`P Q-Q P` cancels the `e_1` component and doubles the `e_2` component, yielding

\[
\boxed{
(\partial_yA)^T(\partial_yA)
=c^2e_2e_2^T.
}
\]

Thus

\[
C_D^{\rm Gram}
\sim\frac{2\nu}{3}h^3c^2e_2e_2^T
\]

away from the symmetry points where `c=0`.

This exact calibration shows why the cross strain/rotation term cannot be discarded
merely because it has zero trace: it determines the actual orientation of the
stochastic deformation spread.

**Classification: EXACT ORIENTATION CONSEQUENCE.**

---

## 7. Consequence for the restart frontier

The local physical currencies now form a sharper hierarchy:

- `S` itself gives current directional metric/vortex-stretch work;
- `grad omega` gives instantaneous Kelvin q.v.;
- `grad S` and `grad omega` together generate finite-horizon Cauchy deformation
  dispersion;
- their signed difference controls the first exterior-volume resolution coefficient;
- their commutator controls orientation of the row-Gram covariance without changing
  its trace.

A first-bad/restart predicate that collapses these to one scalar norm loses exactly
the directional and signed information exposed by the PDE.

**Classification: STRUCTURAL CONSEQUENCE; first-bad definition remains OPEN.**
