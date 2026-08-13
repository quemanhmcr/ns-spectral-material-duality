# The resolved Cartan tensor acts twice: conservative phase-space transport and fiber metric work

Status: **EXACT LOCAL-AFFINE TRANSPORT IDENTITY / CROSS-WANG-KELVIN TYPING**.

The same local velocity gradient enters both wavefront kinematics and vector-amplitude deformation, but these are different physical actions.  This note keeps them separate.

## 1. Local affine wavefront transport

Let the resolved transporter be locally affine,

\[
V(x,t)=A(t)x,
\qquad \operatorname{tr}A=0,
\qquad A=S+\Omega.
\]

Let a phase `theta=k(t).x` be materially transported by `V`:

\[
(\partial_t+V\cdot\nabla)\theta=0.
\]

Then

\[
\boxed{\dot k=-A^Tk=(-S+\Omega)k.}
\]

This is the same `Lambda^2` law as a material area Hodge vector.

## 2. Radial spectral motion is strain-directional

Taking the squared magnitude,

\[
\frac12\frac d{dt}|k|^2
=k\cdot(-S+\Omega)k
=-k\cdot Sk,
\]

because `k.Omega k=0`.  Therefore

\[
\boxed{
\frac d{dt}\log|k|
=-\hat k\cdot S\hat k.
}
\]

The angular law is

\[
\boxed{
\dot{\hat k}
=\Omega\hat k-(I-\hat k\hat k^T)S\hat k.
}
\]

Thus:

- skew connection rotates the wavefront without changing radius;
- strain can change both radius and direction.

## 3. The same law holds for Kelvin material area

For a material area Hodge vector `n`,

\[
\dot n=-A^Tn.
\]

Hence

\[
\boxed{
\frac d{dt}\log|n|
=-\hat n\cdot S\hat n,
}
\]

with the same angular law.  Wang local spectral wavefront scale and Kelvin material-area scale are therefore the same deformation readout at exterior degree two.

A material line `ell` instead obeys

\[
\dot\ell=A\ell,
\qquad
\boxed{
\frac d{dt}\log|\ell|
=+\hat\ell\cdot S\hat\ell.}
\]

This is the line/area sign reversal of Theorem DM at the level of physical magnitudes.

## 4. Why radial motion does not mean energy production

For a scalar transported by incompressible `V`,

\[
\partial_tf+V\cdot\nabla f=0,
\]

one has

\[
\boxed{
\frac d{dt}\frac12\|f\|_2^2=0.
}
\]

Nevertheless its local affine wavevector can satisfy `d|k|/dt != 0` by the formula above.

Therefore a skew-adjoint transport operator can move spectral content across radius while conserving total energy.  Spectral scale relocation is not by itself an energy source.

## 5. Relation to the resolved `K/S` operator split

The resolved skew-adjoint operator is

\[
\mathcal K_V=\mathbb P(V\cdot\nabla+\Omega_V),
\]

while the self-adjoint fiber operator is

\[
\mathcal S_V=\mathbb P(S_V\,\cdot).
\]

The transport part `V.grad` inside `K_V` carries the phase-space characteristic `kdot=-A_V^T k`, which includes `S_V` in wavevector space.  Meanwhile `S_V` also acts directly on vector amplitudes through `S_V^{op}`.

Thus the same physical tensor `S_V` has two different representations:

1. **phase-space strain:** conservative relocation/deformation of wavefronts through the transport characteristic;
2. **fiber strain:** symmetric metric work on vector amplitudes.

They must not be merged into one scalar owner.

## 6. Cross-programme consequence

Wang radial crossing/current may contain conservative scale relocation produced by the transport characteristic even when no net energy is created.  Kelvin material surfaces see exactly the same local area/wavefront kinematics.  Wang symmetric `S` work, by contrast, is fiber/material metric work.

Hence

\[
\boxed{
\text{radial scale progress}
\not\equiv
\text{symmetric strain work},
}
\]

even though both are governed locally by the same tensor `S`.
