# Orthogonal observer gauge can move connection but cannot remove physical strain

Status: **EXACT FRAME-GAUGE IDENTITY / COUNTEREXAMPLE-NO-GO AGAINST GAUGING AWAY METRIC DEFORMATION**.

## 1. Transform the local generator by a rotating orthonormal frame

Let

\[
A=S+\Omega,
\qquad S^T=S,
\quad \Omega^T=-\Omega.
\]

Let `O(t)` be orthogonal and define frame coordinates `x=O(t)\tilde x`.  The transformed generator is

\[
\widetilde A
=O^TAO-C,
\qquad
C:=O^T\dot O,
\qquad C^T=-C.
\]

Taking symmetric/skew parts gives

\[
\boxed{
\widetilde S=O^TSO,
\qquad
\widetilde\Omega=O^T\Omega O-C.
}
\]

The observer angular velocity `C` enters only the skew connection.

## 2. Strain invariants survive every orthogonal gauge

Because `S` changes only by orthogonal conjugation,

\[
\boxed{
\operatorname{spec}\widetilde S=\operatorname{spec}S,
\qquad
\operatorname{tr}(\widetilde S^m)=\operatorname{tr}(S^m),
\qquad
\|\widetilde S\|_F=\|S\|_F.
}
\]

For transformed probes `\tilde a=O^Ta`, `\tilde b=O^Tb`,

\[
\boxed{
\tilde a\cdot\widetilde S\tilde b
=a\cdot Sb.
}
\]

Thus the material metric-work bilinear form is observer-rotation invariant.

## 3. No-go: common rotation cannot gauge away nonzero strain

If an orthogonal observer could make

\[
\widetilde S=0,
\]

then `O^TSO=0`, hence

\[
\boxed{S=0.}
\]

Therefore a nonzero Wang symmetric resolved owner cannot be converted into pure `K` relink by a common orthogonal role/frame motion.  Conversely a pure skew connection can be changed or removed locally by choosing the frame angular velocity `C` appropriately.

This is the exact geometric reason the `K/S` split is not cosmetic.

## 4. Material metric interpretation

The resolved material identity

\[
H\dot MH^T=2S
\]

is consistent with the frame law above: an orthogonal change of spatial frame conjugates the Eulerian metric velocity but does not change its spectrum or bilinear physical work.

A non-orthogonal `GL(3)` reparameterization can move deformation into the coordinate metric, but then the metric itself changes.  That is material deformation bookkeeping, not a free observer rotation.

## 5. Consequence for Wang/Kelvin

- Wang fixed-event or moving-role `K` belongs to the connection/observer sector and may be redistributed by connection gauge.
- Wang `S` is metric deformation and survives orthogonal gauge.
- Kelvin orientation frame rotations similarly alter connection coordinates while leaving physical strain work invariant.

No norm estimate or regularity statement is involved.
