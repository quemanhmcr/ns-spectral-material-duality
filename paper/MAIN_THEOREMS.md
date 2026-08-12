# Main theorem spine — working draft

These statements are the current self-contained mathematical spine of the bridge paper.  They are intentionally separated from any 3D Navier--Stokes regularity claim.

## Theorem A — Dual deformation geometry

For a smooth incompressible flow map with deformation gradient `F`, material area covectors and Kelvin/Fourier wavefront covectors are transported by `F^{-T}`.  The material metric

\[
M=F^TF
\]

and spectral covector metric `M^{-1}` are dual.  In particular

\[
|k|^2=k_0^TM^{-1}k_0.
\]

## Theorem B — Metric velocity is objective strain

For an invertible material area frame `H=F^{-T}`,

\[
H(D_tM)H^T=2S,
\qquad S=\operatorname{sym}\nabla u.
\]

Consequently the trace-free restriction of the material metric velocity to a triad plane is exactly the nonconformal strain driving Fourier/helical polarization and triad deformation.

## Theorem C — Near-extremal triad coordinates are inverse-metric observables

For the symmetric reference triad with directions `n_a,n_b,n_c`, define

\[
q_j=n_j^TM^{-1}n_j.
\]

Then the spectral Hodge coordinates are

\[
u=\frac12\log\frac{q_b}{q_a},
\qquad
v=\frac14\log\frac{q_c^2}{q_aq_b}.
\]

Thus material anisotropy, including its orientation relative to the triad, quantitatively determines near-extremal spectral shape loss.

## Theorem D — Noncommuting strain holonomy is polar material rotation

Successive noncommuting symmetric deformations generate a second-order rotation governed by their commutator.  In the planar two-strain calibration this is simultaneously the second Magnus/geometric-phase generator of the helical description and the polar-rotation part of the material deformation.

## Theorem E — Signed helical edge work is an oriented material-flux 3-form

For a resonant helical edge `k_1+k_2=q`, let

\[
\Phi_j=H^T\omega_j.
\]

Then

\[
\boxed{
T_e=
2\frac{s_q}{|q|}
\left(\frac{s_1}{|k_1|}-\frac{s_2}{|k_2|}\right)
\operatorname{Re}\mathcal Z_H,
}
\]

where

\[
\boxed{
\mathcal Z_H
=\frac{1}{\det H}
\overline{\Phi_q}\cdot(\Phi_1\times\Phi_2).
}
\]

`Z_H` is invariant under passive `GL(3)` packet reparameterization and resonant spatial translation.  Its argument is the gauge-invariant interaction phase.  Metric/covariance alone cannot determine this phase because they are second-order while `Z_H` is genuinely third-order.

## Theorem F — Localized material-flux source law

For any sufficiently regular time-dependent linear role operator `Q(t)`,

\[
\boxed{
D_t(H^TQ\omega)
=H^T\Big[
(\partial_tQ+[u\cdot\nabla,Q])\omega
+(Q\nabla u-\nabla u\,Q)\omega
+\nu Q\Delta\omega
\Big].
}
\]

The three terms are respectively moving/interface transport, strain--selection mismatch, and viscosity.  For `Q=I` the two localization terms vanish and the full Kelvin/Nanson viscous flux law is recovered.

## Theorem G — Moving localization has an unavoidable time face

If `Q=Q(t)`, the term `partial_t Q` is a literal source face.  It cannot in general be replaced by the static commutator `[u.grad,Q]`.  It vanishes only under an explicitly proved covariant/co-moving law.

## Theorem H — Kelvin-loop realization of interaction phase

For an orientation-complete packet of small material loops with area frame `r^2H`, let `Gamma_j(r)` be the three role-filtered circulation coordinates.  Then

\[
\boxed{
\lim_{r\to0}
\frac{\overline{\Gamma_q(r)}\cdot(\Gamma_1(r)\times\Gamma_2(r))}
{\det(r^2H)}
=\mathcal Z_H.
}
\]

Hence the signed nonlinear interaction and its `U(1)` phase have a literal Kelvin-current small-loop realization.

## Theorem I — Monochromatic viscosity does not rotate interaction phase

For one resonant Fourier edge,

\[
\dot{\mathcal Z}_{\nu}
=-\nu(|k_1|^2+|k_2|^2+|q|^2)\mathcal Z.
\]

Therefore

\[
\boxed{\dot\vartheta_{\nu}=0,
\qquad \vartheta=\arg\mathcal Z.}
\]

Viscosity damps interaction amplitude but does not rotate monochromatic interaction phase.  Instantaneous phase rotation is nonlinear; for localized packets a viscous phase term must be derived from the non-monochromatic role rather than assumed absent.

# Current open theorem

The next genuinely new closure target is a **localized phase/work alternative** derived from Theorems E--I:

> On a physically selected localized resonant packet, either favorable `Re Z_H` persists for a controlled interval, or loss of favorable work is quantitatively charged to an explicit phase-velocity source (moving/interface transport or strain-selection mismatch), or the interaction amplitude is lost through a separately typed physical channel.

No theorem currently proves that this alternative terminates a Navier--Stokes recurrence or yields regularity.
