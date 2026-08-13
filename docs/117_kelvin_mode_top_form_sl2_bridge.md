# Wang's objective `SL(2)` polarization is the trace-free quotient of an exact Kelvin-mode top-form balance

Status: **EXACT LINEARIZED NSE / CROSS-WANG MATERIAL-CARTAN BRIDGE**.

Current Wang already proves the exact transverse Kelvin-mode equation.  This note does not re-prove that theorem as a new upstream result.  It identifies the geometric origin of its scalar/trace-free split and connects it to repo-3 exterior/material structure.

## 1. Start from Wang's exact affine Kelvin mode

Let the incompressible affine base flow be

\[
U(x,t)=A(t)x,
\qquad \operatorname{tr}A=0,
\qquad A=S+\Omega.
\]

For a transverse linearized Navier--Stokes Kelvin mode, current Wang has

\[
\dot k=-A^Tk
\]

and, in the objective orthonormal transverse frame `E(t)` spanning `k(t)^perp`,

\[
\boxed{
\dot c
=-\left(B_\perp+\nu|k|^2I_2\right)c,
\qquad
B_\perp:=E^TSE.
}
\]

The pressure correction is parallel to `k` and therefore disappears from the transverse amplitude equation/work after projection.

## 2. The transverse trace is exactly the carrier radial rate

Since

\[
EE^T=I-\hat k\hat k^T
\]

and `tr S=0`,

\[
\operatorname{tr}B_\perp
=\operatorname{tr}[(I-\hat k\hat k^T)S]
=-\hat k\cdot S\hat k.
\]

The Kelvin carrier law gives

\[
\frac d{dt}\log|k|
=-\hat k\cdot S\hat k.
\]

Therefore

\[
\boxed{
\operatorname{tr}B_\perp
=\frac d{dt}\log|k|.
}
\]

The scalar transverse strain is not an independent amplitude parameter.  It is exactly the radial dilation rate of the carrier covector.

## 3. Exact Kelvin-mode top-form balance

Let `U_perp(t)` be the fundamental matrix of the transverse amplitude equation,

\[
\dot U_\perp
=-\left(B_\perp+\nu|k|^2I_2\right)U_\perp,
\qquad U_\perp(0)=I_2.
\]

Jacobi's determinant identity gives

\[
\frac d{dt}\log\det U_\perp
=-\operatorname{tr}B_\perp-2\nu|k|^2.
\]

Using the carrier-radius identity,

\[
\boxed{
\frac d{dt}\log\left(|k|\det U_\perp\right)
=-2\nu|k|^2.
}
\]

Hence

\[
\boxed{
|k(t)|\det U_\perp(t)
\exp\!\left(2\nu\int_0^t|k(s)|^2ds\right)
=|k(0)|.
}
\]

Inviscidly,

\[
\boxed{|k|\det U_\perp=\text{constant}.}
\]

This is the Kelvin-mode phase/polarization version of incompressible top-form neutrality: carrier covector dilation and transverse polarization-area dilation compensate exactly.  It is not identified with the literal material volume `det F`; the objects are different, while the exterior mechanism is the same.

## 4. The trace-free polarization map is forced to be `SL(2)`

Decompose

\[
B_\perp=\sigma I_2+D,
\qquad
\sigma=\frac12\operatorname{tr}B_\perp,
\qquad
\operatorname{tr}D=0.
\]

Since

\[
\sigma=\frac12\frac d{dt}\log|k|,
\]

define

\[
\boxed{
U_\perp(t)
=\left(\frac{|k(0)|}{|k(t)|}\right)^{1/2}
\exp\!\left(-\nu\int_0^t|k(s)|^2ds\right)
\widetilde U(t).
}
\]

Then exactly

\[
\boxed{
\dot{\widetilde U}=-D\widetilde U,
\qquad
\det\widetilde U=1.
}
\]

Thus the determinant-one polarization dynamics used by Wang is what remains **after** the physically forced scalar carrier/viscous factors are removed.

In two real dimensions, `SL(2,R)=Sp(2,R)`, so

\[
\boxed{\widetilde U^T J\widetilde U=J.}
\]

This explains the exact common-parent symplectic wedge neutrality in Wang from the same incompressible Cartan/exterior spine.

## 5. Material metric interpretation of the trace-free generator

Repo 3 gives

\[
H\dot MH^T=2S.
\]

Therefore

\[
B_\perp
=\frac12E^TH\dot MH^TE.
\]

Its trace-free part

\[
\boxed{
D
=\operatorname{tf}\left(\frac12E^TH\dot MH^TE\right)
}
\]

is literally the non-conformal transverse part of material metric velocity.  Wang's helicity conversion matrix is therefore a circular-basis reading of trace-free material metric deformation.

## 6. Scope

This theorem strengthens the dictionary:

- carrier radius: scalar transverse metric dilation;
- raw transverse amplitude determinant: compensating area factor plus viscosity;
- `SL(2)` polarization: trace-free material deformation;
- helical conversion: circular-basis representation of that trace-free deformation.

No recurrence cost or regularity conclusion is inferred from determinant-one structure alone.
