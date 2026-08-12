# Kelvin q.v. feeds the stochastic Cauchy rotation sector through the exterior-power ladder

Status: **Exact three-dimensional exterior-representation identity and rigorous short-horizon consequence.**

The previous gradient decomposition showed two formulas with the same coefficient:

\[
C_\Omega(h)
=\frac{h^3}{12}
[(\operatorname{tr}\Gamma_K)I-\Gamma_K]+O(h^4),
\]

and the vorticity-gradient part of the mean exterior-volume defect is

\[
\delta_\omega(h)
=\frac{h^3}{12}\operatorname{tr}\Gamma_K+O(h^4),
\]

where

\[
\Gamma_K=2\nu(\nabla\omega)(\nabla\omega)^T.
\]

These are the degree-two and degree-three representations of the **same** physical
Kelvin q.v. tensor.

---

## 1. Exterior-power representation of a linear map

Let `G:R^3->R^3`.  Its induced Lie-algebra action on `Lambda^p R^3` is

\[
G^{[p]}(v_1\wedge\cdots\wedge v_p)
=\sum_{j=1}^p
v_1\wedge\cdots\wedge Gv_j\wedge\cdots\wedge v_p.
\]

For `p=1`,

\[
\boxed{G^{[1]}=G.}
\]

For `p=2`, after the Euclidean Hodge identification

\[
*: \Lambda^2\mathbb R^3\to\mathbb R^3,
\]

one has

\[
\boxed{
*G^{[2]}*^{-1}
=(\operatorname{tr}G)I-G^T.
}
\]

For the one-dimensional top exterior power,

\[
\boxed{G^{[3]}=\operatorname{tr}G.}
\]

**Classification: EXACT EXTERIOR-ALGEBRA REPRESENTATION IDENTITY.**

For symmetric `G`, transpose disappears from the degree-two formula.

---

## 2. Apply the ladder to the Kelvin q.v. tensor

The physical instantaneous orientation-complete Kelvin q.v. tensor is symmetric
positive semidefinite:

\[
\Gamma_K=2\nu(\nabla\omega)(\nabla\omega)^T.
\]

Its three exterior representations are therefore

\[
\boxed{
\begin{aligned}
\mathcal R_1(\Gamma_K)
&=\Gamma_K,\\
\mathcal R_2(\Gamma_K)
&=(\operatorname{tr}\Gamma_K)I-\Gamma_K,\\
\mathcal R_3(\Gamma_K)
&=\operatorname{tr}\Gamma_K.
\end{aligned}
}
\]

**Classification: EXACT 3D HODGE/EXTERIOR DICTIONARY.**

No probability or norm inequality is involved in passing between the three degrees.

---

## 3. The Cauchy rotation sector uses degrees two and three with one coefficient

The stochastic Cauchy short-horizon calculation gives exactly

\[
\boxed{
C_\Omega(h)
=\frac{h^3}{12}\mathcal R_2(\Gamma_K)+O(h^4).
}
\]

Meanwhile the vorticity-gradient contribution to

\[
\delta_D=1-\det\bar D
\]

is

\[
\boxed{
\delta_\omega(h)
=\frac{h^3}{12}\mathcal R_3(\Gamma_K)+O(h^4).
}
\]

Thus the same physical q.v. tensor controls

- degree `1`: loop-orientation covariance itself;
- degree `2`: rotation-induced material two-plane/deformation dispersion;
- degree `3`: the rotation-gradient contribution to mean top-volume resolution.

**Classification: RIGOROUS SHORT-HORIZON EXTERIOR-POWER CONSEQUENCE.**

The common factor `h^3/12` is forced by the reverse-age Cauchy covariance onset,
not chosen by normalization.

---

## 4. Rank-one q.v. makes the Hodge complement literal

If

\[
\Gamma_K=\lambda nn^T,
\qquad |n|=1,
\]

then

\[
\boxed{
\mathcal R_2(\Gamma_K)
=\lambda(I-nn^T).
}
\]

So degree-one Kelvin q.v. lives along `n`, while the degree-two Cauchy rotation
sector lives exactly in the orthogonal two-plane.

At degree three,

\[
\boxed{\mathcal R_3(\Gamma_K)=\lambda.}
\]

The top exterior degree forgets orientation and retains only the total q.v. trace,
which is why the vorticity-gradient contribution to the determinant defect is a
scalar.

**Classification: EXACT RANK-ONE GEOMETRIC CONSEQUENCE.**

---

## 5. Isotropic q.v. and anisotropic q.v. remain distinguishable

If

\[
\Gamma_K=\gamma I,
\]

then

\[
\mathcal R_2(\Gamma_K)=2\gamma I,
\qquad
\mathcal R_3(\Gamma_K)=3\gamma.
\]

If instead q.v. is anisotropic, degree two preserves that anisotropy through the
complement eigenvalues

\[
\lambda_j^{(2)}
=\operatorname{tr}\Gamma_K-\lambda_j.
\]

Thus reducing immediately to `tr Gamma_K` retains the top-volume contribution but
loses the two-plane orientation geometry.

**Classification: RIGOROUS SPECTRAL CONSEQUENCE.**

---

## 6. The strain-gradient sector is a separate exterior owner

The full mean-volume defect is not merely the degree-three Kelvin q.v. term.  It is

\[
\boxed{
\delta_D(h)
=\frac{h^3}{12}\mathcal R_3(\Gamma_K)
-\frac{\nu h^3}{3}|\nabla S|_F^2
+O(h^4).
}
\]

Likewise the full row-Gram covariance contains strain-gradient and
strain/rotation-coupling sectors in addition to `R_2(Gamma_K)`.

Therefore the exterior ladder identifies the **rotation/vorticity-gradient branch**
exactly, but it does not erase the separate strain-gradient physics.

**Classification: EXACT TYPE SEPARATION.**

---

## 7. Relation to the broader exterior-algebra spine

Earlier results found:

- a `Lambda^2` determinant/wedge law for spectral parent polarization;
- a `Lambda^3` material interaction volume carrying signed triad phase/work;
- common incompressible deformation cancelling through exterior powers.

The present theorem adds a stochastic differential layer: the Kelvin q.v. tensor
itself propagates into material deformation resolution by the induced exterior
representations `R_2` and `R_3`.

So the exterior-algebra spine is not merely a convenient common language.  It is an
actual transport rule connecting instantaneous vorticity-gradient stochastic
payment to two-plane and volume-level Cauchy geometry.

**Classification: EXACT STRUCTURAL BRIDGE.**
