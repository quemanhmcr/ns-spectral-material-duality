# Interaction-phase velocity from the instantaneous Navier--Stokes vorticity RHS

Status: **Exact modal identity; Action calibrated on a smooth real periodic NSE state.**

Let

\[
\mathcal Z
=\overline{\omega_q}\cdot(\omega_1\times\omega_2),
\qquad k_1+k_2=q,
\]

for three oriented helical Fourier roles.  This is the `H=I` representative of the GL(3)-invariant material interaction 3-form.

The exact vorticity PDE is

\[
\partial_t\omega
=-u\cdot\nabla\omega
+(\nabla u)\omega
+\nu\Delta\omega.
\]

Projecting the literal instantaneous RHS onto the three helical roles and applying the product rule gives

\[
\dot{\mathcal Z}
=\dot{\mathcal Z}_{\rm transport}
+\dot{\mathcal Z}_{\rm stretch}
+\dot{\mathcal Z}_{\rm visc}.
\]

Where `Z != 0`,

\[
\boxed{
\dot\vartheta
=\operatorname{Im}\frac{\dot{\mathcal Z}}{\mathcal Z}
=\dot\vartheta_{\rm transport}
+\dot\vartheta_{\rm stretch}
+\dot\vartheta_{\rm visc}.
}
\]

## Monochromatic viscosity cannot rotate the interaction phase

For one exact Fourier mode,

\[
\nu\Delta\omega_k=-\nu|k|^2\omega_k.
\]

Therefore

\[
\boxed{
\dot{\mathcal Z}_{\rm visc}
=-\nu(|k_1|^2+|k_2|^2+|q|^2)\mathcal Z.
}
\]

The coefficient is real, so

\[
\boxed{\dot\vartheta_{\rm visc}=0.}
\]

Viscosity reduces the magnitude of a monochromatic interaction but does not rotate its gauge-invariant interaction phase.  Any instantaneous phase rotation of such an edge is nonlinear: it comes from advective convolution and vortex-stretching convolution (or, after localization/materialization, from their named interface/selection descendants).

For broad packets the viscous operator need not be scalar on the role, so a packet-level phase contribution must be derived rather than assumed zero.

## Why this matters

The signed edge work is proportional to `Re Z = |Z| cos vartheta`.  The PDE therefore separates two physically different ways an interaction can lose favorable work:

1. **amplitude erosion/amplification:** change `|Z|`;
2. **phase dephasing:** rotate `vartheta`.

The metric controls geometry; the oriented circulation triple supplies `Z`; the exact NSE RHS tells us which physical channels change its magnitude and which rotate its phase.  No abstract phase penalty is required at this stage.
