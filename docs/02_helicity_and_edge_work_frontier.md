# Helicity and actual edge-work frontier

Status: **first bridge succeeds for local helicity conversion; metric-only bridge fails for signed work**.

## Question

The common deformation dictionary reaches Fourier carrier geometry. Does it also determine the nonlinear helical transfer that carries actual child-energy work?

The correct answer begins with a split.

## 1. Local helicity conversion is encoded by metric velocity

Let `E=(e1,e2)` be an orthonormal frame of the transverse plane to a Kelvin carrier. In the objective frame, the real polarization generator is

\[
- E^T S E.
\]

But the common dictionary gives

\[
E^TSE=\frac12E^TH\dot M H^TE.
\]

Write the trace-free part as

\[
D=\begin{pmatrix}\delta&\beta\\\beta&-\delta\end{pmatrix}.
\]

In the circular/helical basis the off-diagonal conversion coefficients are `delta ± i beta` (with the overall sign set by the evolution convention). Therefore material metric velocity determines the instantaneous local helicity-mixing rate exactly.

## 2. Signed Fourier work needs more than metric geometry

For one Fourier child `q=k1+k2`, define vorticity modes

\[
\omega_j=i k_j\times u_j
\]

and compute the nonlinear child forcing directly from the NSE identity

\[
F_q=P_q(u_1\times\omega_2+u_2\times\omega_1).
\]

The physical child-energy work is

\[
T_q=2\operatorname{Re}(\overline{u_q}\cdot F_q).
\]

At fixed wavevectors, fixed material metric, fixed helicity signs and fixed modal magnitudes, changing only the relative complex phase of `u_q` changes `T_q` continuously through positive, zero and negative values.

Therefore

\[
\boxed{\text{metric/shape geometry does not determine signed physical edge work}.}
\]

This is an explicit non-equivalence, not a proof gap.

## 3. Minimal bridge state suggested by the experiment

To reach actual signed work, the common material deformation data must be augmented by at least:

- relative helical polarization;
- relative complex phase (or an equivalent gauge-invariant phase observable);
- modal amplitudes / physical capacity.

A plausible minimal dictionary is therefore

\[
(M,\ \text{connection/holonomy},\ \text{helical spinors},\ \text{relative phase},\ \text{amplitudes}).
\]

The metric determines carrier shape and local polarization conversion; it does not replace the signed nonlinear work law.

## 4. Next theorem target

Find a gauge-invariant material-side observable whose combination with the metric/connection reconstructs the phase factor in the direct Fourier–Leray edge identity, or prove that no local material observable of the proposed class can do so.

That is the first genuinely nonlinear frontier of this bridge programme.
