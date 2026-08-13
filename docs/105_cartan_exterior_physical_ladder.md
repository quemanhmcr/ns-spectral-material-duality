# The incompressible Cartan generator has a rigid exterior-power sign ladder

Status: **EXACT EXTERIOR-REPRESENTATION SPECIALIZATION / EXACT NSE MATERIAL-FLUX CONSEQUENCE**.

This note specializes the already proved exterior representation formula to the actual Navier--Stokes velocity gradient `A=S+Omega` and reads each degree physically in Wang/Kelvin variables.

## 1. The three-dimensional ladder

For any linear generator `G` on `R^3`, repo 3 already proved

\[
R_1(G)=G,
\qquad
R_2(G)=(\operatorname{tr}G)I-G^T,
\qquad
R_3(G)=\operatorname{tr}G.
\]

For an incompressible velocity gradient

\[
A=S+\Omega,
\qquad
\operatorname{tr}A=\operatorname{tr}S=0,
\qquad
\Omega^T=-\Omega,
\]

this becomes

\[
\boxed{
R_1(A)=S+\Omega,
\qquad
R_2(A)=-S+\Omega,
\qquad
R_3(A)=0.
}
\]

Thus the two Cartan sectors behave differently across exterior degree:

- symmetric strain changes sign from degree one to degree two;
- skew connection keeps the same Hodge-vector sign;
- top volume sees neither one in incompressible flow.

## 2. Physical degree-one objects

Material line vectors satisfy

\[
D_t\ell=A\ell=(S+\Omega)\ell.
\]

The inviscid part of vorticity satisfies the same degree-one law,

\[
D_t\omega=A\omega.
\]

With viscosity,

\[
\boxed{D_t\omega=A\omega+\nu\Delta\omega.}
\]

These are `Lambda^1` objects in the Cartan ladder.

## 3. Physical degree-two objects

The Hodge vector of an incompressible material area element satisfies Nanson's law

\[
D_t n=-A^Tn=(-S+\Omega)n.
\]

A locally affine Fourier/coherent wavefront covector obeys the identical law

\[
\boxed{\dot k=-A^Tk=(-S+\Omega)k.}
\]

Therefore

\[
\boxed{
\text{material area Hodge vector}
\quad\text{and}\quad
\text{local affine Fourier wavevector}
}
\]

are not merely dual-looking objects: they are the same `Lambda^2` representation of the local incompressible deformation generator.

This statement is local/affine for spectral wavefront transport; it does not claim that a single global Fourier mode remains a Fourier mode under arbitrary non-affine flow.

## 4. Strain and connection cancel separately in the line/area pairing

Let `a` obey the degree-one law `dot a=Aa` and let `n` obey the degree-two Hodge law `dot n=-A^Tn`.  Then

\[
\frac d{dt}(a\cdot n)=0.
\]

More strongly, the cancellation occurs separately by Cartan type:

\[
(Sa)\cdot n+a\cdot(-Sn)=0,
\]

and

\[
(\Omega a)\cdot n+a\cdot(\Omega n)=0.
\]

Thus common deformation flux invariance does not require strain and connection to cancel each other.  Each sector is already representation-dual.

The same identity gives material phase invariance `d(k.ell)/dt=0` for a line and its advected wavefront covector.

## 5. Navier--Stokes material vorticity flux has only the viscous local source

Use the actual vorticity equation and the material area law:

\[
D_t\omega=A\omega+\nu\Delta\omega,
\qquad
D_t n=-A^Tn.
\]

Then

\[
\boxed{
D_t(\omega\cdot n)
=\nu(\Delta\omega)\cdot n.
}
\]

The stretching/strain and skew-connection contributions cancel exactly and separately.  This is the pointwise area-vector form underlying the viscous Kelvin circulation flux law.

No norm or covariance enters.

## 6. Top exterior neutrality

For three degree-one vectors `z_1,z_2,z_3` transported by the same `A`,

\[
\frac d{dt}\det(z_1,z_2,z_3)
=(\operatorname{tr}A)\det(z_1,z_2,z_3)=0.
\]

Because both `tr S=0` and `tr Omega=0`, common strain and common connection are each separately neutral on `Lambda^3`.

This is the deterministic Cartan explanation of the already proved common-deformation cancellation of the material interaction 3-form: differential owners, not common incompressible deformation, can change the cubic interaction.

## 7. Cross-programme dictionary

The physical ladder is therefore

\[
\boxed{
\begin{array}{ccl}
\Lambda^1 &:& \text{material line / inviscid vorticity},\quad S+\Omega,\\
\Lambda^2 &:& \text{material area / local Fourier wavevector},\quad -S+\Omega,\\
\Lambda^3 &:& \text{oriented interaction volume},\quad 0.
\end{array}}
\]

Wang's spectral deformation and Kelvin's material-current geometry are adjacent representations of one local Cartan generator.  The ladder supplies a dictionary, not a new currency or recurrence rule.
