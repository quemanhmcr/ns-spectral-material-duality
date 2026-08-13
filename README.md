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
- **common synthesis functor:** genuine linear refinement/event synthesis forces the full tensor-square pair state, including cross pairs; diagonal child/germ marginals erase relative coherent/common-driver coupling by introducing an artificial product gauge, so full ordered coupling is required unless independently reconstructible;
- **selector typing:** Kelvin's first-bad selector is a readout of a persistent physical library, not a universal transport map from the previously selected residual;
- **hybrid event typing:** a simultaneous physical event and selector uses the composed map `E_+ A` with the mandatory finite mixed face `DeltaE DeltaA`; continuous q.v. production, signed source-rate revaluation, optional jump q.v., and endpoint pair reset are distinct physical objects;
- **history no-go:** selector jump q.v. has positive closed-loop circulation while pair revaluation telescopes, so accumulated jump variation is path/history data rather than an endpoint-state potential.
- **passive packet quotient:** packet coordinates `(H,epsilon)` carry the exact passive gauge `(H,epsilon)~(HS,S^T epsilon)`; the physical residual `H^{-T}epsilon` and inverse-Gram energy are invariant, while raw coefficient size is not a physical first-bad score;
- **critical-current typing:** a nondegenerate enstrophy critical branch obeys `H_e(xdot_*-u)+grad R=0`; exact ABC has a fixed strict enstrophy maximum with nonzero fluid velocity, so critical-locus current and material-carrier current are distinct physical objects unless the PDE proves coincidence;
- **ranking/event typing:** exact periodic NSE can exchange the larger enstrophy candidate while both candidates decay and `(u.grad)u=0`; the crossing is invisible to the local velocity 2-jet but visible to the third jet/curvature, and ranking crossing, selector/readout reset, critical-geometry event, and Wang hard nonlinear interaction are not interchangeable clocks.
- **own-local affine event typing:** Kelvin packet/current events relative to packet-specific targets are `x_+=Ax_-+d`, with the exact coboundary `d=A Omega_- - Omega_+`; this target reanchoring can change residual/q.v. source even for `A=I` and is not Wang's passive carrier-chart gauge;
- **boundary-charge zero-depth typing:** Wang's selected-family Moyal charge `R_switch` can be positive on an identical coherent state with zero cell increments/work, while exact NSE can realize arbitrarily many finite ranking/selector crossings with zero nonlinear advection; neither boundary/readout count nor target/q.v. revaluation is a universal hard-generation-depth currency.
- **selector-path zero-depth law:** for the arbitrary-finite exact heat-shear crossing family, a right-continuous one-hot winner selector switches exactly `N` times and has exact optional label jump-q.v. `tr J_Y=2N`; for even `N` it returns to the same label while the accumulated path variation stays positive, and the selected scalar remains continuous;
- **critical-lineage clock separation:** invertible enstrophy Hessian (or nonzero active normal Hessian for a symmetry sheet) gives a unique local critical lineage and fixed Morse/normal type; exact periodic NSE realizes arbitrary finite ranking activity inside one compact interval with no tracked normal degeneracy and zero nonlinear advection, so **winner/readout != lineage domain != physical owner**;
- **exact Kelvin merger event now instantiated upstream:** current read-only Kelvin has an analytic two-mode heat-shear critical-sheet merger.  For one specified fixed-shape translated packet per sheet the physical library event is the central extraction `A=E_0`, with `d=0`, zero target-gradient coboundary, nonzero same-replica cross blocks, and zero selected physical packet jump at collision; scalar/position merger alone still does not canonically determine packet shape or ancestry.
- **enstrophy record owner clock:** the running record of the literal local enstrophy maximum has an exact PDE owner law: critical-selector drift drops out at `grad e=0`, and every positive record increment requires an active maximizer where vortex stretching beats `nu(|grad omega|^2-Delta e)`; ranking/selector/sweep/gauge/boundary activity cannot mint this monotone clock by itself.

The original metric dictionary remains in [`docs/01_common_deformation_dictionary.md`](docs/01_common_deformation_dictionary.md).  The current integrated bridge spine is in [`docs/122_core_pde_bridge_spine.md`](docs/122_core_pde_bridge_spine.md).

## Current frontier

The center of this repository is **strengthening the Wang and Kelvin programmes through literal PDE bridges**, not building an independent regularity proof around them.

The highest-priority seams are now:

1. build, or rule out, the literal cross-program state map with all required data attached: Eulerian/coherent field; material current/shape; packet/frame data modulo passive gauge; critical-locus current/geometry **and its lineage theorem domain** (`H_e` or the active normal Hessian/shape operator plus support chart) whenever a critical candidate is used; typed ranking/geometry/selector/event clocks and history; underlying physical owner/event/synthesis `A`; own-local target/anchor coboundary `d`; separately typed boundary sidecars; inherited stock/ancestry when used; and the persistent library with full relative pair/Gram coupling.  A winner label, selected channel, raw packet coordinate, diagonal pair list, endpoint-only history surrogate, or generic untyped `bad event` is not compositional;
2. use the now-closed affine-quotient law for all `p>=2` physical jets, then derive the programme-specific readout order actually demanded by the PDE: the exact enstrophy-ranking shear already proves that a local velocity 2-jet can be insufficient while the third jet controls the branch-rate difference; this is a readout requirement, not a reopening of the quotient seam;
3. carry the exact pressure and viscosity dictionaries through real moving/localized roles with every commutator, boundary face, q.v. cross block and clock face retained;
4. continue read-only audits of Wang's sidecar-bearing inherited-stock central/joint-stop integration and Kelvin's now-instantiated critical-sheet merger/own-local affine event/first-bad developments; the remaining bridge task is to connect real physical geometry/owner events to the programme badness/resolve and ancestry clocks without converting readout or boundary activity into fake recurrence depth.
5. test whether actual record-growth owner states obey an intrinsic depletion/reuse law: the new enstrophy running-record clock already forces stretching-dominant active maxima and annihilates pure selector/sweep/sidecar directions, so the remaining question is whether geometry, material ancestry and donor structure can prevent unlimited fresh effective stretching.

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
- tensor-square refinement/pair coherence, relative-coupling/diagonal-marginal no-gos, finite-shape state-map no-gos, and selector-event history/coboundary no-gos;
- hybrid selector/event product rules separating continuous q.v. source, signed source-rate revaluation, finite jump q.v., and endpoint pair reset;
- passive packet-gauge invariance versus raw-coordinate ranking;
- exact ABC enstrophy critical-current/material-current separation and incompressible critical-curvature-volume cancellation;
- exact periodic enstrophy ranking crossing, local velocity 2-jet no-go, and ranking/selector/Wang-hard-event type separation;
- own-local affine target-coboundary composition, exact cubic-shear target q.v. revaluation, and arbitrary-finite exact-NS ranking-crossing no-go.
- exact selector-label `tr J_Y=2N`, zero-depth owner-kernel witnesses, and same-endpoint positive path variation on smooth exact NSE;
- critical-lineage IFT/Morse rigidity, compact-interval ranking/geometry/nonlinear-owner clock separation, and ABC isolated-Hessian persistence calibration.

Every executable calibration is run in GitHub Actions and is treated only as an adversarial referee for manually derived claims.

## Attribution

Research direction and repository: **Manh Que (`quemanhmcr`)**.

Research assistance: **OpenAI ChatGPT (GPT-5.6 Sol)** for derivation support, adversarial testing design, and computational audit. All mathematical claims remain subject to independent verification.

## Exact boundary theorem

The first genuinely nonlinear result is an exact **no-go theorem**: fixed material metric/carrier geometry cannot determine the sign of helical child-energy work because the relative complex phase remains free. See [`docs/03_metric_phase_no_go.md`](docs/03_metric_phase_no_go.md).

A chronological status ledger is maintained in [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md), and the paper skeleton is in [`paper/OUTLINE.md`](paper/OUTLINE.md).

- **Relative-boundary owner law (HK–HR):** every moving NSE balance sees selector motion only through `V-u`; moving enstrophy splits exactly into stretching, bulk viscous loss, diffusive boundary flux and relative sweep, while moving circulation obeys a swept-ribbon Kelvin law.  The exact critical-sheet merger shows a `1/d` sweep-rate singularity with continuous current, zero nonlinear advection and zero enstrophy stretching.  Endpoint residual coalescence still does not erase Nanson transport ancestry.
