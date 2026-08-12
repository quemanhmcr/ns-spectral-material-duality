# Actual nonlinear energy routing is a transport-with-killing system

Status: **EXACT NSE / ENERGY-TRANSPORT IDENTITY** on a finite Fourier--Galerkin system, plus an exact sub-Markov representation once the physical donor kernel is fixed.

This note uses the current Wang donor/recipient theorem only for what it literally supplies: a nonnegative same-time transport table whose donor marginal is canonical negative nonlinear work and whose recipient marginal is canonical positive nonlinear work.  No Wang recursion, Young gate, packet, or ancestry architecture is imported.

## 1. Start from the exact modal energy law

Let `i` index resolved divergence-free Fourier modes (or helical roots after summing the internal polarization labels as desired), and write

\[
E_i(t)=\frac12|\widehat u_i(t)|^2\ge0.
\]

For unforced incompressible Navier--Stokes,

\[
\boxed{
\dot E_i=W_i^+-W_i^- - d_iE_i,
\qquad d_i=2\nu |k_i|^2,
}
\]

where `W_i^+=[W_i]_+`, `W_i^-=[-W_i]_+` are the Hahn positive/negative pieces of the actual nonlinear child-energy work.  Closed nonlinear energy conservation gives

\[
\sum_iW_i^+=\sum_iW_i^-.
\]

Current Wang upstream `8d21df4` supplies a same-time nonnegative donor/recipient transport law.  In finite notation let

\[
K_{ij}(t)\ge0
\]

be its aggregate physical energy-transfer table, with

\[
\boxed{
\sum_jK_{ij}=W_i^- ,
\qquad
\sum_iK_{ij}=W_j^+ .
}
\]

Hence the modal Navier--Stokes balance is exactly

\[
\boxed{
\dot E_i
=\sum_jK_{ji}-\sum_jK_{ij}-d_iE_i.
}
\]

**Physical typing.**  `K` is same-time conservative nonlinear transfer.  `d_iE_i` is physical viscous loss.  There is no third source.

## 2. Zero modal energy cannot emit nonlinear work

If `E_i=0`, then `u_i=0`, hence the modal nonlinear work pairing is zero and therefore `W_i^-=0`.  Since the row of `K` is nonnegative and has row sum zero,

\[
K_{ij}=0\qquad\text{for every }j.
\]

Thus the rates

\[
\boxed{
r_{ij}(t)=
\begin{cases}
K_{ij}(t)/E_i(t),&E_i(t)>0,\\
0,&E_i(t)=0
\end{cases}
}
\]

are well typed; no division-by-zero source is hidden.

Substitution gives

\[
\boxed{
\dot E_i
=\sum_j r_{ji}E_j
-E_i\sum_jr_{ij}
-d_iE_i.
}
\]

This is the forward equation of a time-inhomogeneous jump process with jump rates `r_ij` and killing rate `d_i`.

**Classification: EXACT TRANSPORT-WITH-KILLING REPRESENTATION.**

This does **not** assert that kinetic energy consists of microscopic particles.  It says that once the actual donor kernel is fixed, the deterministic energy balance has a canonical Markovian disintegration requiring no FIFO/LIFO pairing of earlier deposits and later withdrawals.

## 3. Exact between-time energy ancestry

Let `Pi_{s,t}` be the sub-Markov propagator of the jump-plus-killing generator.  Then the modal energy vector satisfies

\[
\boxed{E(t)=E(s)\Pi_{s,t}.}
\]

Consequently total kinetic energy has the exact survival representation

\[
\boxed{
\sum_iE_i(t)
=
\sum_iE_i(s)\,\mathbb P_{s,i}(\zeta>t),
}
\]

where `zeta` is the viscous killing time in this representation.

Nonlinearity redistributes surviving energy among modes; viscosity alone removes total mass.  This is the between-time counterpart of the same-time donor theorem, but it is a representation theorem on the third-repo bridge, not a modification of Wang upstream.

## 4. Universal Dynkin energy identity

For any differentiable real modal observable `f_i(t)`, multiply the exact modal balance by `f_i` and sum.  The donor/recipient table gives

\[
\boxed{
\frac d{dt}\sum_i f_iE_i
=
\sum_i(\partial_tf_i)E_i
+
\sum_{i,j}(f_j-f_i)K_{ij}
-
\sum_i d_if_iE_i.
}
\]

Every term is physically typed:

- `partial_t f`: observer/clock motion of the chosen modal observable;
- `(f_j-f_i)K_ij`: actual nonlinear transport across its level sets;
- `d_i f_iE_i`: viscous killing measured by that observable.

This identity is exact before any estimate and will be the base for the future-heat currency.

## 5. Scope

The theorem is finite-dimensional as stated, matching the exact Fourier--Galerkin donor registration used in current Wang audits.  A continuum/countable extension requires the usual measurability and integrability needed to define the donor kernel and the jump generator.

No first-bad event, parabolic scale identification, recurrence termination, or 3D regularity conclusion is claimed here.
