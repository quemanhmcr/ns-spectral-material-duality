# Opposite-helicity pair creation is the first radial moment of the same physical energy current

Status: **EXACT RADIAL LAYER-CAKE / HELICAL OWNER IDENTIFICATION**.

## 1. Use the certified donor/recipient energy current

For a physical donor atom `d -> r` with energy-work mass `m`, write

\[
\rho_d=|k_d|,
\qquad
\rho_r=|k_r|.
\]

Let

\[
F(R)=\Phi_\uparrow(R)-\Phi_\downarrow(R)
\]

be the net radial energy current across the Fourier sphere of radius `R`.

For a truncated interval `0<R_0<R_1`, define the clipped linear radial potential

\[
\psi_{R_0,R_1}(\rho)
=
\min\{(\rho-R_0)_+,R_1-R_0\}.
\]

One atom satisfies

\[
\int_{R_0}^{R_1}
\bigl[
1_{\rho_d\le R<\rho_r}
-
1_{\rho_r\le R<\rho_d}
\bigr]dR
=
\psi(\rho_r)-\psi(\rho_d).
\]

Hence the already-existing physical energy current obeys

\[
\boxed{
\int_{R_0}^{R_1}F(R)\,dR
=
\int[\psi(|k_r|)-\psi(|k_d|)]\,d\mathcal M(d,r).
}
\]

No new Hahn decomposition is taken.

## 2. Infinite-range first moment

Whenever the physical first radial moment is finite, monotone/truncation passage gives

\[
\boxed{
\int_0^\infty F(R)\,dR
=
\int (|k_r|-|k_d|)\,d\mathcal M(d,r).
}
\]

The right side is exactly the nonlinear derivative of

\[
\mathcal C=\sum |k|E.
\]

Therefore Theorem BY yields

\[
\boxed{
\int_0^\infty F(R)\,dR
=2(\mathcal P_{create}-\mathcal P_{ann}).
}
\]

This is the degree-one radial companion of the enstrophy layer cake

\[
\int_0^\infty 2R F(R)dR
=\mathcal V_{split}-\mathcal V_{merge}.
\]

## 3. Physical interpretation

A homochiral split may send energy both inward and outward, but helicity conservation is also conservation of `|k|`-weighted energy on one sign half-line.  Its first radial moments cancel exactly.

A heterochiral split breaks that radial cancellation because signed helicity uses opposite signs while physical radius uses absolute values.  The uncancelled first radial moment is exactly twice the opposite-helicity pair charge.

Thus pair creation is not an abstract extra statistic.  It is the net outward **critical radial moment** of the same kinetic-energy current already certified by Wang's radial crossing theorem.

**Classification: EXACT NSE/PDE IDENTITY.**
