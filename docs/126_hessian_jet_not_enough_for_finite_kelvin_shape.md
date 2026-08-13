# The common Hessian jet `B=J_2(L)` does not determine the finite Kelvin residual

Status: **EXACT PERIODIC NSE NO-GO / HIGHER-JET-MOMENT NECESSITY**.

Theorem EP identifies Wang and Kelvin's common quadratic non-affine jet exactly.  The present theorem shows why that success must not be extrapolated into a finite-shape closure.

## 1. The common quadratic jet vanishes at the symmetry anchor

For the exact periodic shear

\[
u=(e^{-\nu t}\sin y,0,0),
\]

at `y=0`,

\[
\partial_y^2u_x=-e^{-\nu t}\sin y=0.
\]

All other velocity Hessian components also vanish.  Therefore for every grain frame `L`,

\[
\boxed{
B=L^{-1}(\nabla^2u)L^{\otimes2}=0.
}
\]

Hence Wang's first Hessian-driven third-Hermite transverse packet-shape forcing is zero at this anchor:

\[
\boxed{\operatorname{Sym}B=0.}
\]

Kelvin's local quadratic codeforming jet also vanishes.

## 2. The finite Kelvin surface residual remains nonzero

For the centered rectangle from Theorem EY,

\[
\boxed{
\varepsilon_\Sigma
=4ae^{-\nu t}(b-\sin b).
}
\]

Its small-shape expansion is

\[
\boxed{
\varepsilon_\Sigma
=\frac{2}{3}ae^{-\nu t}b^3
-\frac1{30}ae^{-\nu t}b^5
+O(b^7).
}
\]

The leading nonzero term comes from the next odd spatial derivative of the velocity/vorticity structure, not from the Hessian jet `B`.

Thus

\[
\boxed{
B=0
\not\Longrightarrow
\varepsilon_\Sigma=0.
}
\]

## 3. Why Kelvin's moment tower is physically necessary

Current Kelvin's `J_p(L)` hierarchy and surface-moment tower are therefore not technical over-resolution.  Even an exact one-mode Navier--Stokes solution can be invisible to the local quadratic jet at a symmetry point while a finite material surface sees a real residual.

A finite-shape bridge must either:

1. carry the full codeforming residual field `N_L(xi)`; or
2. carry enough higher jets/moments to reconstruct the finite surface observable with a justified remainder.

It may not stop at `J_2(L)` merely because Wang and Kelvin share that tensor exactly.

## 4. Scope for future higher-jet work

This theorem does **not** assert a general Wang `p>=3` packet-normal formula by pattern extrapolation.  Current Wang higher-Hermite/pressure/viscous channels must be audited theorem by theorem before any identification with Kelvin `J_p(L)` is claimed.

The result only proves the necessity of additional physical information beyond the common Hessian layer.
