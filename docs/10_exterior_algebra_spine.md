# Exterior-algebra spine: common incompressible deformation is geometry, not generation

Status: **Exact finite-dimensional identity with direct relevance to both bridge endpoints.**

A surprisingly small algebraic law sits underneath two objects that originally looked unrelated.

## 1. The Fourier polarization wedge is a 2D determinant

For two transverse polarization spinors `U,V`,

\[
U^TJV=\det[U,V]
\]

(up to the fixed orientation convention).  If both obey the same trace-free generator

\[
\dot U=GU,
\qquad
\dot V=GV,
\qquad \operatorname{tr}G=0,
\]

then

\[
\boxed{
\frac d{dt}\det[U,V]
=(\operatorname{tr}G)\det[U,V]=0.
}
\]

Thus an arbitrarily large common `SL(2)` deformation cannot by itself change the parent wedge.  Only differential generators or forcing can do so.

## 2. The material interaction 3-form is a 3D determinant

The complex interaction object can be written

\[
\mathcal Z
=\overline{\omega_3}\cdot(\omega_1\times\omega_2)
=\det[\omega_1,\omega_2,\overline{\omega_3}].
\]

If three vectors undergo the same real incompressible linear deformation

\[
\dot\omega_j=A\omega_j,
\qquad \operatorname{tr}A=0,
\]

then

\[
\boxed{
\dot{\mathcal Z}
=(\operatorname{tr}A)\mathcal Z=0.
}
\]

So common incompressible stretching/rotation can make the individual vectors large and highly anisotropic while preserving their oriented interaction volume exactly.

The Nanson material flux coordinates make this cancellation explicit by removing the common deformation from each vector before the determinant is formed.

## 3. Only relative generators matter

For role-dependent generators `A_1,A_2,A_3`, choose any common reference `A_0`.  Multilinearity gives

\[
\begin{aligned}
\dot{\mathcal Z}
={}&(\operatorname{tr}A_0)\mathcal Z\\
&+\det[(A_1-A_0)\omega_1,\omega_2,\overline{\omega_3}]\\
&+\det[\omega_1,(A_2-A_0)\omega_2,\overline{\omega_3}]\\
&+\det[\omega_1,\omega_2,(A_3-A_0)\overline{\omega_3}].
\end{aligned}
\]

For incompressible common `A_0`, the trace term vanishes.  The interaction changes only through **relative incidence/deformation**.

This is the 3D exterior-algebra analogue of the exact relative-polarization identity on the Fourier side.

## 4. Interpretation

The common structural rule is

\[
\boxed{
\text{common volume-preserving deformation}
\Rightarrow
\text{wedge/volume invariant},
}
\]

while

\[
\boxed{
\text{relative deformation or forcing}
\Rightarrow
\text{physical interaction change}.
}
\]

This explains why large common strain must not automatically be charged as a transfer deficit, why passive material frame motion creates no cubic work, and why the localized PDE law naturally exposes commutators/differences rather than absolute observer deformation.

In exterior-algebra language, the two programmes are seeing adjacent manifestations of the same determinant law: a `Lambda^2` invariant in transverse polarization space and a `Lambda^3` invariant in physical/material vorticity-flux space.

## 5. Research implication

The next coercive theorem should target **relative generators**, not absolute deformation norms.  For the localized material-flux law those relative generators are already named exactly by

\[
\partial_tQ+[u\cdot\nabla,Q]
\quad\text{and}\quad
Q\nabla u-\nabla u\,Q.
\]

This gives a principled route for comparing the Fourier relative-polarization obstruction with the Kelvin localization/connection obstruction without identifying their downstream currencies prematurely.
