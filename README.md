# NS Spectral–Material Duality

An independent PDE-first research programme on exact bridges between two complementary descriptions of three-dimensional incompressible Navier–Stokes:

1. **spectral/helical/Fourier-triad geometry**, and
2. **material/Kelvin/vorticity-flux geometry**.

The project does **not** assume that the two descriptions are equivalent. Its job is to derive from Navier–Stokes which objects are exactly the same, which are only quantitatively comparable, and which must never be identified.

## Independent upstream programmes

This repository openly records the two independent research programmes that motivated the comparison:

- [`quemanhmcr/wang-ns-triad-diamond`](https://github.com/quemanhmcr/wang-ns-triad-diamond) — Eulerian/Fourier/helical physical-work and recurrence programme.
- [`quemanhmcr/ns-pde-first-kelvin-frontier`](https://github.com/quemanhmcr/ns-pde-first-kelvin-frontier) — PDE-first material/Kelvin/current and restart programme.

Their authorship and collaborator credit remains with the upstream projects. This bridge repository is independent and does not imply that either upstream programme endorses statements made here.

## Research rule

Every bridge is classified as one of:

- **Exact NSE/kinematic identity**
- **Rigorous consequence**
- **Numerical/action stress test**
- **Conjectural bridge**
- **Explicit non-equivalence / counterexample**

Numerical tests are never proof. No 3D Navier–Stokes regularity claim is made.

## Current common spine

Let `F` be the incompressible deformation gradient and let

\[
M=F^T F.
\]

The material description naturally sees `M`, while advected Fourier covectors see

\[
k=F^{-T}k_0,
\qquad
|k|^2=k_0^T M^{-1}k_0.
\]

Thus the initial candidate common spine is the pair

\[
(M,M^{-1})
\]

together with its objective strain rate and connection/holonomy.

The first exact dictionary is documented in [`docs/01_common_deformation_dictionary.md`](docs/01_common_deformation_dictionary.md).

## Current frontier

The next question is deliberately adversarial:

> Does material metric/holonomy determine actual signed helical edge work, or only geometry/capacity?

The first action experiment answers part of this question: material metric velocity determines local helicity conversion, but **metric geometry alone cannot determine signed physical edge work**; a relative complex phase/polarization sidecar remains necessary.

See [`docs/02_helicity_and_edge_work_frontier.md`](docs/02_helicity_and_edge_work_frontier.md).

## Reproducibility

Experiments are run in **GitHub Actions**, not treated as hand calculations or theorem certificates.

Workflow: `.github/workflows/bridge-audit.yml`

The action currently runs:

- metric ↔ triad-Hodge dictionary checks;
- two-strain holonomy checks;
- metric-velocity ↔ helicity-conversion checks;
- fixed-metric phase sweep for direct Fourier–Leray edge work.

## Attribution

Research direction and repository: **Manh Que (`quemanhmcr`)**.

Research assistance: **OpenAI ChatGPT (GPT-5.6 Sol)** for derivation support, adversarial testing design, and computational audit. All mathematical claims remain subject to independent verification.
