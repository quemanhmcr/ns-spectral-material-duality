# Exact no-go: material metric alone cannot determine signed helical edge work

Status: **exact finite-triad identity / non-equivalence theorem**.

## Setup

Fix a nondegenerate Fourier triad

\[
q=k_1+k_2,
\]

fix parent divergence-free modes `u1,u2`, fix a unit child helical vector `h_q`, and define

\[
\omega_j=i k_j\times u_j,
\]

\[
F_q=P_q(u_1\times\omega_2+u_2\times\omega_1).
\]

All carrier geometry, material metric data, helicity signs, parent amplitudes and child amplitude magnitude are held fixed. Only the child complex phase varies:

\[
u_q(\phi)=e^{i\phi}h_q.
\]

The physical child-energy work is

\[
T(\phi)=2\operatorname{Re}(\overline{u_q(\phi)}\cdot F_q).
\]

## Theorem

Let

\[
C:=\overline{h_q}\cdot F_q.
\]

Then

\[
\boxed{T(\phi)=2\operatorname{Re}(e^{-i\phi}C).}
\]

If `C != 0`, write `C=|C|e^{i\theta}`. Therefore

\[
\boxed{T(\phi)=2|C|\cos(\theta-\phi).}
\]

Consequently

\[
\max_\phi T=2|C|,
\qquad
\min_\phi T=-2|C|,
\]

and there are phases with `T=0`.

Hence no observable depending only on the fixed material metric/carrier geometry, helicity signs and modal magnitudes can determine the sign of physical edge work.

## Interpretation

The material metric can determine deformed carrier geometry and, through its velocity, the local symmetric polarization generator. It cannot replace the gauge-invariant relative phase entering actual nonlinear work.

Thus a correct cross-representation state must retain a phase/polarization sidecar or an equivalent invariant carrying the same information.

This theorem is compatible with, and conceptually explains, the distinction between geometric interaction capacity and signed causal work.

## Action calibration

The action experiment `exp03_helicity_edge_work.py` selects one deformed near-optimal triad with fixed material metric, fixed helicity signs and fixed unit modal magnitudes. Its phase sweep checks a nonzero `C` and realizes the full sign change numerically. The numerical run is only a calibration of the exact identity above.
