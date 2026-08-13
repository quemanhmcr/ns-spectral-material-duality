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

The bridge has now moved beyond a metric-only dictionary.  At the local physical level write

\[
A=\nabla u=S+\Omega,
\qquad S^T=S,
\quad \Omega^T=-\Omega.
\]

A small set of exact Navier--Stokes laws now organizes both upstream descriptions:

- **Cartan split:** skew connection/transport `K` versus symmetric material deformation `S`;
- **exterior ladder:** `S+Omega` on material lines/vorticity, `-S+Omega` on material areas/local Fourier covectors, and zero common generator on top volume;
- **projector gauge:** fixed roles display conservative `K` relink, connection-comoving roles absorb it into observer motion, while strain cannot be gauged away by an orthogonal frame;
- **typed pressure:** `grad p` is gauge for divergence-free work/closed circulation, while `Hess p` is a real strain/material-metric curvature face;
- **typed viscosity:** spectral enstrophy killing is exactly the full-state Kelvin q.v. trace/Dirichlet form, while the q.v. tensor contains additional directional information;
- **full non-affine affine quotient:** Wang's Gaussian residual and Kelvin's anchor-Taylor residual differ exactly by an affine field, so all physical jets `p>=2` coincide; `B=L^{-1}(nabla^2u)L^(tensor 2)` is only the quadratic member, after which programme-specific quotients may differ;
- **common synthesis functor:** genuine linear refinement/event synthesis forces the full tensor-square pair state, including cross pairs; diagonal-only bookkeeping is exact only under additional orthogonality;
- **selector typing:** Kelvin's first-bad selector is a readout of a persistent physical library, not a universal transport map from the previously selected residual.

The original metric dictionary remains in [`docs/01_common_deformation_dictionary.md`](docs/01_common_deformation_dictionary.md).  The current integrated bridge spine is in [`docs/122_core_pde_bridge_spine.md`](docs/122_core_pde_bridge_spine.md).

## Current frontier

The center of this repository is **strengthening the Wang and Kelvin programmes through literal PDE bridges**, not building an independent regularity proof around them.

The highest-priority seams are now:

1. build, or rule out, the literal cross-program state map with all required state attached: Eulerian/coherent field, material current/shape, clock/history, linear physical synthesis, and the persistent full pair/library state; a selected channel alone is not compositional;
2. use the now-closed affine-quotient law for all `p>=2` physical jets, then derive only the programme-specific Hermite/moment readouts that are actually needed rather than reopening a fictitious higher-jet equivalence problem;
3. carry the exact pressure and viscosity dictionaries through real moving/localized roles with every commutator, boundary face, q.v. cross block and clock face retained;
4. continue read-only audits of Wang's resolved-contact plus pure-UV true-upward routing and Kelvin's frame-aware event/library/first-bad developments, adding exact equivalences **or no-go theorems** in this repository as the PDE dictates.

Interaction phase, recurrence, and possible regularity consequences remain important downstream applications, but they are not allowed to replace the repository's primary PDE-first bridge task.

See [`paper/MAIN_THEOREMS.md`](paper/MAIN_THEOREMS.md), [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md), and the core integration map above.

## Reproducibility

Experiments are run in **GitHub Actions**, not treated as hand calculations or theorem certificates.

Workflow: `.github/workflows/bridge-audit.yml`

The action currently stress-tests, among other things:

- material metric / Cartan `K/S` identities and role-gauge covariance;
- exterior line/area/top-form representations and exact material-flux cancellation;
- moving spectral-cut metric-acceleration faces;
- resolved/unresolved Wang HH work against Kelvin residual/dyad deformation;
- pressure-gradient gauge versus pressure-Hessian metric curvature;
- spectral viscous killing versus Kelvin q.v. trace, including tensor-information no-gos;
- affine wavefront radial transport versus fiber metric work;
- Wang objective `SL(2)` polarization, carrier/top-form balance, and material/helical holonomy;
- common Wang/Kelvin full non-affine affine-quotient identities, Gaussian/anchor gauge mismatch, and representation-kernel counterexamples;
- tensor-square refinement/pair coherence and finite-shape state-map no-gos.

Every executable calibration is run in GitHub Actions and is treated only as an adversarial referee for manually derived claims.

## Attribution

Research direction and repository: **Manh Que (`quemanhmcr`)**.

Research assistance: **OpenAI ChatGPT (GPT-5.6 Sol)** for derivation support, adversarial testing design, and computational audit. All mathematical claims remain subject to independent verification.

## Exact boundary theorem

The first genuinely nonlinear result is an exact **no-go theorem**: fixed material metric/carrier geometry cannot determine the sign of helical child-energy work because the relative complex phase remains free. See [`docs/03_metric_phase_no_go.md`](docs/03_metric_phase_no_go.md).

A chronological status ledger is maintained in [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md), and the paper skeleton is in [`paper/OUTLINE.md`](paper/OUTLINE.md).
