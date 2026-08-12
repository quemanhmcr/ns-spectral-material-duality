# Kelvin circulation realization of the complex interaction phase

Status: **Exact small-loop limit; CI calibrated on resonant helical plane waves.**

## 1. Keep the complex 3-form, not only its real part

For three material vorticity-flux roles

\[
\Phi_j=H^T\omega_j,
\]

define

\[
\boxed{
\mathcal Z_H
:=\frac{1}{\det H}
\overline{\Phi_3}\cdot(\Phi_1\times\Phi_2).
}
\]

The earlier signed flux observable is

\[
\mathcal C_H=\operatorname{Re}\mathcal Z_H.
\]

The full complex number contains the missing quadrature:

\[
\boxed{\vartheta_H=\arg\mathcal Z_H.}
\]

For a helical resonant edge, signed child-energy work is a real frequency/helicity factor times `Re Z_H`.  Therefore the phase sweep that defeated every metric-only closure is exactly rotation of this complex material interaction 3-form.

## 2. Gauge and observer invariance

`Z_H` is invariant under passive `GL(3)` packet reparameterization because numerator and denominator acquire the same determinant.

For a spatial translation by `a`, Fourier role fluxes gain phases `exp(i k_j.a)`.  On a resonance `k_1+k_2=k_3`, the phase of the cubic product is unchanged.  Hence `arg Z_H` is not a coordinate-origin phase.

A helical-basis phase convention also cannot change `Z_H` when the physical Fourier vectors `omega_j` are kept fixed.  Thus `vartheta_H` is a gauge-invariant interaction phase, not a Berry phase of an arbitrarily chosen basis.

## 3. Literal Kelvin-loop realization

Let the columns `h_a` of `H` be three independent oriented area vectors.  Around a point `x`, take three small material surfaces with area vectors

\[
h_{a,r}=r^2 h_a
\]

and closed boundary loops `Z_{a,r}`.  For role-filtered velocity `u_j`, define its three circulation coordinates

\[
\Gamma_{j,a}(r)=\oint_{Z_{a,r}}u_j\cdot d\ell.
\]

Stokes and smoothness give

\[
\Gamma_j(r)=r^2 H^T\omega_j(x)+o(r^2)
=r^2\Phi_j+o(r^2).
\]

Since

\[
\det(r^2H)=r^6\det H,
\]

we obtain the exact small-loop limit

\[
\boxed{
\lim_{r\to0}
\frac{
\overline{\Gamma_3(r)}\cdot
(\Gamma_1(r)\times\Gamma_2(r))
}{\det(r^2H)}
=\mathcal Z_H.
}
\]

Thus the complex interaction phase has a literal current/circulation realization.  It is third-order across **three role-filtered circulation vectors**; it is not contained in one-loop variance or any second-order covariance matrix.

For real-valued measurements the complex representation is simply two real quadratures of the resonant role pair.  No physical complex fluid is being postulated.

## 4. Exact phase evolution once role sources are known

Whenever `Z_H != 0`,

\[
\boxed{
D_t\log|\mathcal Z_H|
=\operatorname{Re}\frac{D_t\mathcal Z_H}{\mathcal Z_H},
\qquad
D_t\vartheta_H
=\operatorname{Im}\frac{D_t\mathcal Z_H}{\mathcal Z_H}.
}
\]

The localized material-flux PDE already decomposes each `D_t Phi_j` into moving/interface transport, strain-selection mismatch, and viscosity.  Substitution therefore gives an exact signed **phase-velocity ledger** with those same physical channels.

This is the candidate phase dictionary sought after the metric-phase no-go.

## 5. What is still open

The small-loop theorem identifies the correct material current observable, but it does not yet prove a useful coercive estimate for its phase velocity near a singular frontier.  In particular we still need to determine, for the literal role operators used in the two upstream programmes, whether low interface/strain/viscous phase velocity forces persistent favorable work or instead exposes a new holonomy/recurrence obstruction.
