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

The original metric-phase question has now split cleanly.  Metric geometry determines carrier/triad deformation and helicity conversion, but signed nonlinear work is carried by the **complex oriented material-flux 3-form**

\[
\mathcal Z_H=\det(H)^{-1}\,\overline{\Phi_q}\cdot(\Phi_1\times\Phi_2).
\]

Its real part gives signed helical edge work up to the exact frequency/helicity coefficient; its argument is the gauge-invariant interaction phase.  `Z_H` has a literal small-Kelvin-loop circulation realization.

The localized PDE law is also exact: after common Nanson transport is removed, a role evolves only through moving/interface transport, strain--selection mismatch, and viscosity.  A moving cut carries an explicit `Qdot` time face.

The current open problem is therefore no longer “where is phase?” but:

> Can the exact phase-velocity/source ledger force a useful localized alternative: persistent favorable work, quantified physical dephasing, or separately paid amplitude loss?

See [`paper/MAIN_THEOREMS.md`](paper/MAIN_THEOREMS.md) and docs 04--08.

## Reproducibility

Experiments are run in **GitHub Actions**, not treated as hand calculations or theorem certificates.

Workflow: `.github/workflows/bridge-audit.yml`

The action currently runs:

- metric ↔ triad-Hodge dictionary checks;
- two-strain holonomy checks;
- metric-velocity ↔ helicity-conversion and metric-only no-go checks;
- direct Fourier--Leray work ↔ oriented material-flux 3-form checks under random `GL(3)` frames;
- localized instantaneous NSE vorticity-role source classification;
- moving-cut `Qdot` time-face calibration;
- small-Kelvin-loop circulation convergence to the complex interaction 3-form;
- instantaneous physical interaction-phase velocity and zero monochromatic viscous phase rotation.

## Attribution

Research direction and repository: **Manh Que (`quemanhmcr`)**.

Research assistance: **OpenAI ChatGPT (GPT-5.6 Sol)** for derivation support, adversarial testing design, and computational audit. All mathematical claims remain subject to independent verification.

## Exact boundary theorem

The first genuinely nonlinear result is an exact **no-go theorem**: fixed material metric/carrier geometry cannot determine the sign of helical child-energy work because the relative complex phase remains free. See [`docs/03_metric_phase_no_go.md`](docs/03_metric_phase_no_go.md).

A chronological status ledger is maintained in [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md), and the paper skeleton is in [`paper/OUTLINE.md`](paper/OUTLINE.md).
