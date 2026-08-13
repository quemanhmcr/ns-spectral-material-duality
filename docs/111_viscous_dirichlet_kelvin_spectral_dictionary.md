# Spectral viscous killing and the orientation-complete Kelvin q.v. trace are the same Dirichlet form

Status: **EXACT PARSEVAL/NSE VISCOUS IDENTITY / CROSS-PROGRAMME DICTIONARY**.

This closes the full-state trace-level viscosity seam left open in the earlier localization dictionary.  It does not identify the full Kelvin q.v. tensor, a future covariance bank, or a reduced-state covariance with one scalar spectral killing rate.

## 1. Helical spectral normalization

Write the divergence-free velocity as

\[
\widehat u(k)=\sum_{s=\pm1}a_{k,s}h_s(k),
\qquad
E_{k,s}=\frac12|a_{k,s}|^2.
\]

The vorticity coefficient is

\[
\widehat\omega(k)
=\sum_s s|k|a_{k,s}h_s(k).
\]

Because the helical fibers are orthonormal,

\[
\frac12\|\omega\|_2^2
=\sum_{k,s}|k|^2E_{k,s}.
\]

## 2. Wang spectral enstrophy killing is the vorticity Dirichlet form

Parseval gives

\[
\boxed{
\nu\|\nabla\omega\|_2^2
=2\nu\sum_{k,s}|k|^4E_{k,s}.
}
\]

This is exactly the viscous killing term in the spectral enstrophy moment ledger.

At kinetic-energy level, similarly,

\[
\boxed{
\nu\|\nabla u\|_2^2
=2\nu\sum_{k,s}|k|^2E_{k,s}.
}
\]

No shell estimate is involved.

## 3. Kelvin q.v. trace is the same full-state Dirichlet form

Current Kelvin's orientation-complete instantaneous vorticity q.v. tensor is

\[
\Gamma_K=2\nu(\nabla\omega)(\nabla\omega)^T.
\]

Therefore pointwise

\[
\boxed{
\frac12\operatorname{tr}\Gamma_K
=\nu|\nabla\omega|^2.
}
\]

Integrating and using Parseval,

\[
\boxed{
\frac12\int\operatorname{tr}\Gamma_K\,dx
=\nu\|\nabla\omega\|_2^2
=2\nu\sum_{k,s}|k|^4E_{k,s}.
}
\]

Thus **Wang spectral viscous enstrophy killing and the trace of Kelvin instantaneous full-state q.v. are literally the same physical dissipation**, expressed in Fourier and stochastic/material coordinates.

## 4. Global enstrophy ledger

On a periodic domain,

\[
D_t\frac{|\omega|^2}{2}
=\omega\cdot S\omega
+\nu\Delta\frac{|\omega|^2}{2}
-\frac12\operatorname{tr}\Gamma_K.
\]

After spatial integration the curvature flux vanishes:

\[
\boxed{
\frac d{dt}\frac12\|\omega\|_2^2
=\int\omega\cdot S\omega\,dx
-\frac12\int\operatorname{tr}\Gamma_K\,dx.
}
\]

Equivalently the last term is the spectral killing `2nu sum |k|^4 E_(k,s)`.

## 5. What is and is not identified

The equality is exact for:

- the **instantaneous full physical state**;
- the orientation-complete q.v. **trace**;
- the full spectral enstrophy killing summed over modes.

It does not identify:

- directional entries/eigenvectors of `Gamma_K` with scalar killing;
- future covariance with instantaneous q.v.;
- reduced ancestry covariance with full-state q.v.;
- a localized q.v. tensor with a shell killing unless the localization operation is carried explicitly.

These distinctions are physical information, not technical caveats.
