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
- **first non-affine jet:** Wang's normalized velocity-Hessian tensor and Kelvin's codeforming quadratic jet are exactly the same tensor `B=L^{-1}(nabla^2u)L^(tensor 2)`, after which the two programmes take different quotients.

The original metric dictionary remains in [`docs/01_common_deformation_dictionary.md`](docs/01_common_deformation_dictionary.md).  The current integrated bridge spine is in [`docs/122_core_pde_bridge_spine.md`](docs/122_core_pde_bridge_spine.md).

## Current frontier

The center of this repository is **strengthening the Wang and Kelvin programmes through literal PDE bridges**, not building an independent regularity proof around them.

The highest-priority seams are now:

1. identify a literal state-map/selector bridge between Wang physical roles/coherent ancestry and Kelvin current/germ state without losing connection, interface, q.v. or finite-reset faces;
2. extend the exact common non-affine-jet dictionary beyond the quadratic Hessian layer where justified;
3. carry the exact pressure and viscosity dictionaries through real moving/localized roles with every commutator and boundary face retained;
4. continue read-only audits of Wang resolved-contact/HH routing and Kelvin current-shape/first-bad developments, adding equivalences **or no-go theorems** in this repository as the PDE dictates.

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
- common Wang/Kelvin non-affine Hessian-jet identities and representation-kernel counterexamples.

Every executable calibration is run in GitHub Actions and is treated only as an adversarial referee for manually derived claims.

## Attribution

Research direction and repository: **Manh Que (`quemanhmcr`)**.

Research assistance: **OpenAI ChatGPT (GPT-5.6 Sol)** for derivation support, adversarial testing design, and computational audit. All mathematical claims remain subject to independent verification.

## Exact boundary theorem

The first genuinely nonlinear result is an exact **no-go theorem**: fixed material metric/carrier geometry cannot determine the sign of helical child-energy work because the relative complex phase remains free. See [`docs/03_metric_phase_no_go.md`](docs/03_metric_phase_no_go.md).

A chronological status ledger is maintained in [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md), and the paper skeleton is in [`paper/OUTLINE.md`](paper/OUTLINE.md).
