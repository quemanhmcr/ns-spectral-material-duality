# Core PDE bridge spine: common physical laws before Wang/Kelvin programme-specific quotients

Status: **INTEGRATION MAP OF PROVED IDENTITIES / NO NEW REGULARITY CLAIM**.

This document records the present center of repo 3.

The purpose of this repository is **not** to replace the Wang or Kelvin programmes by a third proof programme.  Its central job is to strengthen both by identifying, from the literal Navier--Stokes PDE,

1. which physical objects are exactly common;
2. how those objects appear in different representations;
3. which programme-specific quotients lose different information;
4. which apparent correspondences are false.

Any regularity architecture that benefits from these bridges is a downstream consequence.

## 1. Layer zero: the actual local Navier--Stokes state

Before roles, packets, selectors, covariances or recurrence, the local first-order physical state is

\[
A=\nabla u=S+\Omega,
\qquad
S^T=S,
\quad
\Omega^T=-\Omega,
\quad
\operatorname{tr}S=0,
\]

with

\[
A-A^T=[\omega]_\times.
\]

The differentiated NSE is

\[
D_tA+A^2=-\nabla^2p+\nu\Delta A.
\]

Everything below is a representation, localization or higher-jet reading of this physical state.

## 2. First rigid law: deformation versus connection

The resolved linearized operator has the exact Cartan split

\[
\mathcal L_V
=\mathcal K_V+\mathcal S_V,
\]

\[
\boxed{
\mathcal K_V=\mathbb P(V\cdot\nabla+\Omega_V),
\qquad
\mathcal S_V=\mathbb P(S_V\,\cdot),
}
\]

with

\[
\mathcal K_V^*=-\mathcal K_V,
\qquad
\mathcal S_V^*=\mathcal S_V.
\]

Physical meaning:

- `K`: conservative transport/connection/relink sector;
- `S`: deformation/material metric-work sector.

For the resolved material metric,

\[
\boxed{H_V\dot M_VH_V^T=2S_V.}
\]

Thus Wang's symmetric resolved work is literally material metric velocity, while its skew sector is connection/transport modulo pressure gauge.

The same split exists for the unresolved field `h` and therefore for actual HH work.

## 3. Second rigid law: exterior degree determines the sign of deformation

For incompressible `A=S+Omega`, the Hodge representations are

\[
\boxed{
R_1(A)=S+\Omega,
\qquad
R_2(A)=-S+\Omega,
\qquad
R_3(A)=0.
}
\]

Hence:

| exterior degree | physical objects | generator |
|---|---|---|
| `Lambda^1` | material line, inviscid vorticity | `S+Omega` |
| `Lambda^2` | material area Hodge vector, local affine Fourier wavevector | `-S+Omega` |
| `Lambda^3` | oriented volume / common interaction top form | `0` |

This is why Wang wavefront geometry and Kelvin material-surface geometry obey the same local `-A^T` law, while common incompressible deformation is neutral on top volume.

## 4. Third rigid law: connection can be gauge-transported; strain cannot

For a state law

\[
\dot y=(K+S)y
\]

and orthogonal projector `P(t)`, define

\[
G_P=\dot P-[K,P].
\]

Then

\[
\boxed{
\frac d{dt}\frac12\langle y,Py\rangle
=\langle Py,Sy\rangle
+\frac12\langle y,G_Py\rangle.
}
\]

Therefore:

- fixed hard role: conservative `K` relink is visible;
- connection-comoving role: the same `K` becomes common observer transport;
- genuinely non-comoving role: `G_P` is an interface/selector face;
- finite reselection: finite jump, not smooth payment.

Under an orthogonal frame rotation,

\[
\widetilde S=O^TSO,
\qquad
\widetilde\Omega=O^T\Omega O-O^T\dot O.
\]

Thus connection is gauge-sensitive while physical strain spectrum and metric work survive every common orthogonal observer gauge.

This explains rather than erases the distinction between Wang fixed-event `K`, Wang moving-role connection, and Kelvin orientation-frame motion.

## 5. Fourth rigid law: pressure has a representation-dependent physical role

Pressure gradient is invisible to:

\[
\langle w,\nabla p\rangle
\]

for divergence-free `w`, to closed Kelvin circulation, and to curl.

But at gradient/metric-curvature order,

\[
\boxed{
D_tS+S^2+\Omega^2
=-\nabla^2p+\nu\Delta S.
}
\]

Pressure Hessian is therefore a genuine material-deformation face even though pressure gradient is gauge for first-order solenoidal work/circulation.

This is a model of the repository's typing rule: **an object may be gauge in one physical readout and active in another.**

## 6. Fifth rigid law: viscosity has one scalar Dirichlet amount but richer tensor information

At the instantaneous full physical state,

\[
\boxed{
2\nu\sum_{k,s}|k|^4E_{k,s}
=\nu\|\nabla\omega\|_2^2
=\frac12\int\operatorname{tr}\Gamma_K\,dx.
}
\]

Thus Wang spectral enstrophy killing and Kelvin orientation-complete q.v. trace are the same full-state Dirichlet dissipation.

But equal scalar killing does not determine the Kelvin q.v. tensor.  Relative polarization phase can change `Gamma_K` while leaving modal energies and its trace fixed.

The bridge is an exact scalar equality plus an exact tensor-information no-go.

## 7. Sixth rigid law: phase-space strain and fiber strain are different representations of the same `S`

For local affine transport,

\[
\dot k=-A^Tk,
\qquad
\frac d{dt}\log|k|
=-\hat k\cdot S\hat k.
\]

So conservative transport can move spectral content radially while preserving total transported `L^2`.

Separately, `S` acts on vector amplitudes as material metric work.

Therefore

\[
\boxed{
\text{radial spectral motion}
\not\equiv
\text{energy generation / symmetric fiber work},
}
\]

even though both read the same local strain tensor in different representations.

This distinction is essential for interpreting Wang radial crossing physically.

## 8. Wang objective polarization is the trace-free quotient of the same deformation

Current Wang's exact affine Kelvin mode gives, in an objective transverse frame,

\[
\dot c=-(B_\perp+\nu|k|^2I)c,
\qquad
B_\perp=E^TSE.
\]

Incompressibility forces

\[
\operatorname{tr}B_\perp
=\frac d{dt}\log|k|.
\]

Hence

\[
\boxed{
|k|\det U_\perp
\exp\left(2\nu\int|k|^2dt\right)
=\text{constant}.
}
\]

Factoring this scalar carrier/viscous dilation leaves

\[
\widetilde U\in SL(2,\mathbb R)=Sp(2,\mathbb R),
\]

generated by the trace-free transverse material metric velocity.

Noncommuting trace-free strains then have one exact commutator which appears as:

- real material polar holonomy;
- opposite circular/helical phase.

Thus Wang symplectic/helical geometry and repo-3 material holonomy are different basis readings of the same transverse metric-deformation algebra.

## 9. First non-affine layer: both programmes use the same normalized Hessian jet

After the affine layer, current Wang and current Kelvin meet again at exactly one tensor:

\[
\boxed{
B
=L^{-1}(\nabla^2u)L^{\otimes2}
=\mathfrak J_2(L).
}
\]

Wang then projects this common physical curvature through its Gaussian tangent quotient:

\[
B\mapsto\operatorname{Sym}B
\mapsto\text{third-Hermite packet-shape forcing}.
\]

Kelvin keeps the full tensor in its codeforming residual field and surface-moment tower:

\[
B\mapsto\frac12B[\xi,\xi]
\mapsto\text{position/area/moment transport}.
\]

A divergence-free kernel example has

\[
\operatorname{Sym}B=0,
\qquad B\ne0,
\]

so these programme-specific quotients are provably non-equivalent even though the physical cause is exactly common.

## 10. Current Wang/Kelvin dictionary

| physical object | Wang reading | Kelvin reading | relation |
|---|---|---|---|
| `S_V` | symmetric resolved/interface work | resolved part of residual/dyad deformation | **same tensor** |
| `Omega_V` / `K_V` | relink, transport, moving-role connection | orientation/current connection after correct state map | same Cartan sector, **not yet same state representation** |
| `S_h` | symmetric part of actual HH role work | unresolved residual/dyad deformation | **same tensor** |
| local `-A^T` | Fourier carrier/wavefront transport | material-area/current geometry | **same `Lambda^2` representation** |
| pressure gradient | Leray-quotiented work | closed-loop/curl-quotiented | same exact-gradient gauge |
| pressure Hessian | strain/metric-curvature source | full-state strain/material-metric curvature; finite-shape descent keeps additional shape residuals | physical at derivative order, not a scalar common charge |
| viscous enstrophy loss | spectral killing | `1/2 tr Gamma_K` after full-state integration | **same scalar Dirichlet form** |
| q.v. tensor | not determined by scalar killing | orientation-complete tensor | strictly richer directional information |
| trace-free transverse `D` | helical conversion / `SL(2)` polarization | material metric holonomy | same transverse metric-deformation tensor |
| normalized Hessian `B` | `Sym B` after Gaussian tangent quotient | full codeforming `J_2(L)` | **same input, different quotient** |
| first-bad selector | no direct Wang identity | current/germ projector with finite events | state-map bridge remains open |

## 11. What remains central

The next core questions are not “can this already prove regularity?”  They are:

1. **State-map/selector bridge.**  Identify the literal map, if one exists, from Wang physical roles/coherent ancestry to Kelvin current/germ state while preserving the Cartan defect `G_P`, connection orientation, and finite jump semantics.
2. **Higher non-affine jets.**  Determine whether Wang higher packet-normal directions and Kelvin `J_p(L)` moment tower share the same higher physical jets before programme-specific quotienting.
3. **Localized pressure/viscosity.**  Push the exact full-state pressure/Dirichlet dictionaries through actual smooth roles without losing commutator, boundary, q.v. or clock faces.
4. **Resolved-contact branch semantics.**  Continue to audit Wang's native PDE contact binding and place each resulting K/S/HH branch into the material/current dictionary without modifying upstream.
5. **Kelvin first-bad physical semantics.**  Use current Kelvin's full current-shape/residual laws to determine which selector/state quantities can descend literally and which remain open.

These tasks strengthen the two upstream programmes whether or not they eventually contribute to any global regularity argument.

## 12. Research discipline

The repository will continue to follow this order:

\[
\boxed{
\text{actual NSE phenomenon}
\to
\text{physical/PDE type}
\to
\text{exact representation law}
\to
\text{programme-specific quotient}
\to
\text{estimate only when needed}.
}
\]

A shorter proof architecture, if one emerges, is an **effect** of discovering these rigid physical laws.  It is not the object imposed on them from above.
