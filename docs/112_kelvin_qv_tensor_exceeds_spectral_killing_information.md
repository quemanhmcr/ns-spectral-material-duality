# Equal spectral viscous killing does not determine the Kelvin q.v. tensor

Status: **EXACT NSE COUNTEREXAMPLE / POLARIZATION-INFORMATION NO-GO**.

The trace dictionary of Theorem DZ is sharp: it cannot be upgraded to tensor equality from modal energy data alone.

## 1. One-wavevector transverse fields are exact Navier--Stokes

Fix a nonzero wavevector `k`.  Let

\[
\widehat u(k,0)=a_+h_+(k)+a_-h_-(k)
\]

and impose reality at `-k`.  The resulting velocity depends only on `k.x` and is everywhere transverse to `k`.  Hence

\[
(u\cdot\nabla)u=0.
\]

The exact NSE solution is simply

\[
\boxed{u(t)=e^{-\nu|k|^2t}u(0)}
\]

with constant pressure.

Thus arbitrary relative phase between `a_+` and `a_-` is realized by an exact smooth periodic NSE family.

## 2. Spectral killing sees only the two modal magnitudes

For fixed

\[
|a_+|,\qquad |a_-|,
\]

the kinetic and enstrophy viscous killing rates are fixed.  In particular changing

\[
a_-\mapsto e^{i\phi}a_-
\]

leaves

\[
\sum_s|k|^4E_{k,s}
\]

unchanged.

## 3. The orientation-complete Kelvin tensor sees relative polarization phase

At the same time,

\[
\widehat\omega(k)
=|k|\big(a_+h_+(k)-a_-h_-(k)\big).
\]

The spatially integrated q.v. tensor is

\[
\int\Gamma_Kdx
=2\nu|k|^2\Big(
\widehat\omega(k)\widehat\omega(k)^*
+\widehat\omega(-k)\widehat\omega(-k)^*
\Big),
\]

up to the fixed Fourier normalization.

The cross-helicity outer products depend on the relative phase of `a_+` and `a_-`.  Therefore two exact NSE states can have identical modal energies and identical scalar viscous killing while

\[
\boxed{
\int\Gamma_K^{(1)}dx
\ne
\int\Gamma_K^{(2)}dx.
}
\]

Their traces remain equal, exactly as Theorem DZ requires.

## 4. Physical consequence

Spectral killing is the scalar Dirichlet amount.  Kelvin q.v. additionally records how that viscous gradient activity is oriented in physical vector space.

Hence

\[
\boxed{
\text{spectral killing}
=\frac12\operatorname{tr}(\text{Kelvin q.v.})
\quad\text{but}\quad
\text{spectral killing does not determine Kelvin q.v. tensor}.
}
\]

This is why the two upstream programmes can share one viscous provenance without collapsing their state information.
