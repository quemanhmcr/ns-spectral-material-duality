# A Wang Eulerian/spectral state does not determine a Kelvin finite-current residual without physical shape data

Status: **EXACT NSE STATE-MAP NO-GO / SHAPE-STATE ACCEPTANCE RULE**.

Repo 3 has now identified many common local tensors between Wang and Kelvin.  That does **not** imply that the Kelvin finite-current state is a deterministic function of the Eulerian field or of one local jet.  The actual material/current shape is independent physical state data.

## 1. Exact periodic Navier--Stokes shear

Take

\[
\boxed{u(x,y,z,t)=(e^{-\nu t}\sin y,0,0).}
\]

This is an exact smooth periodic 3D Navier--Stokes solution:

\[
(u\cdot\nabla)u=0,
\qquad
\partial_tu=\nu\Delta u,
\]

with constant pressure.

Its vorticity is

\[
\omega=(0,0,-e^{-\nu t}\cos y).
\]

Fix the physical anchor at the origin.

## 2. Two finite material surfaces see different residuals in the same Eulerian field

Let `Sigma_(a,b)` be the centered rectangle

\[
-a\le x\le a,
\qquad
-b\le y\le b,
\qquad z=0,
\]

with upward orientation.

The exact Stokes/Kelvin flux through the finite surface is

\[
K_\Sigma
=\iint_{\Sigma_{a,b}}\omega_z\,dxdy
=-4a e^{-\nu t}\sin b.
\]

The local affine readout at the anchor is the center vorticity times the area:

\[
K_{loc}
=\omega_z(0,t)\,|\Sigma_{a,b}|
=-4ab e^{-\nu t}.
\]

Hence the finite-to-local Kelvin descent residual is

\[
\boxed{
\varepsilon_\Sigma(a,b,t)
=K_\Sigma-K_{loc}
=4a e^{-\nu t}(b-\sin b).
}
\]

For `b!=0` this is generically nonzero and depends on the physical surface shape.

## 3. Same Eulerian state, same orientation and same area, different Kelvin residual

Fix an area `A_0>0` and choose

\[
4ab=A_0.
\]

Then

\[
\varepsilon_\Sigma
=A_0e^{-\nu t}\left(1-\frac{\sin b}{b}\right).
\]

Two different aspect ratios `b_1!=b_2` with the same area and orientation therefore give different residuals while the complete instantaneous Eulerian Navier--Stokes field is identical.

Thus no field-only map

\[
\boxed{
r_{Kelvin}=\Phi(u(t))}
\]

can represent the full finite-current residual universally.

The missing variable is not an estimate.  It is physical **finite current/surface shape state**.

## 4. Consequence for a Wang-to-Kelvin state map

Wang's hard roles, smooth Fourier carriers, coherent cells and canonical transfer laws are constructed from the Eulerian field plus analysis/coherent labels.  They do not, by themselves, specify an arbitrary Kelvin finite material surface/current.

Therefore a literal bridge must have the form

\[
\boxed{
\text{Kelvin current state}
=\Phi(\text{Eulerian/Wang physical state},
\text{material shape/current data},
\text{correct clock/history}).
}
\]

A state map that omits the second argument can at best recover a local/pointwise quotient, not the full finite-current residual used by current Kelvin.

This is why the current Kelvin first-bad descent problem remains a genuine state-lift problem after local tensor dictionaries have been closed.
