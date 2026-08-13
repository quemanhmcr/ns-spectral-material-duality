# Research ledger

## Epistemic labels

- `EXACT`: derived directly from finite-dimensional algebra, continuum kinematics, or NSE identities under stated hypotheses.
- `RIGOROUS CONSEQUENCE`: theorem following from exact identities plus explicitly stated external hypotheses.
- `ACTION`: numerical/adversarial CI calibration only.
- `OPEN`: bridge not yet proved.
- `NO-GO`: exact obstruction to a tempting identification.

## 2026-08-12 — initial bridge

### EXACT — advected covector dictionary

Fourier Kelvin carriers and material area normals obey the same `F^{-T}` transport. Affine Fourier phase planes are material surfaces.

### EXACT — dual metric dictionary

`M=F^T F` controls material geometry while `M^{-1}` controls advected Fourier covector lengths.

### EXACT — strain from metric velocity

`H Mdot H^T = 2S` for `H=F^{-T}`.

### EXACT — objective strain from metric acceleration

`S_objective = (1/2) H Mddot H^T - (1/2)(H Mdot H^T)^2` with the corotational convention recorded in the dictionary note.

### EXACT — triad Hodge coordinates from inverse material metric

For an initially symmetric extremal triad, `u,v` are explicit logarithmic functions of `n_j^T M^{-1} n_j`.

### RIGOROUS CONSEQUENCE — local metric anisotropy costs spectral extremality

Combining the metric dictionary with the certified local single-edge and affine-strain inequalities gives the local condition-number lower bound recorded in `docs/01_common_deformation_dictionary.md`.

### EXACT — noncommuting strain produces common holonomy

The second-order commutator rotation in objective spectral polarization is the leading polar rotation of the same ordered material deformation.

### EXACT — metric velocity determines local helicity conversion

The transverse symmetric generator `E^T S E` equals one half the restriction of `H Mdot H^T`; in the circular basis its trace-free part gives the off-diagonal helicity-conversion coefficient.

### NO-GO — metric-only signed work closure

At fixed geometry, helicities and modal magnitudes, varying only child phase makes direct physical edge work attain positive, zero and negative values. See `docs/03_metric_phase_no_go.md`.

### ACTION — run 31576094866

GitHub Actions passed all three initial experiment modules on commit `2b5fdf5`.

Key calibrations:

- metric/direct parent-ratio residual `4.44e-16`;
- sampled local `Def/H` minimum `3.86999` (the certified theorem only requires `>=1/2` in its region);
- polar holonomy at `b=d=1, eps=.1`: `0.569140889°`, second-Magnus leading value `0.572957795°`;
- metric-velocity/helicity-conversion residual `8.88e-16`;
- fixed-metric phase sweep edge work: `[-0.7988680113,+0.7988680113]`, with sampled zero `4.89e-17`.

## Current frontier

### OPEN — phase dictionary

Find a gauge-invariant material/Kelvin-side observable that reconstructs the relative phase factor entering the direct Fourier–Leray helical edge law, or prove a no-go theorem for a natural class of local material observables.

### OPEN — nonlinear transport dictionary

Determine whether a material-current observable can distinguish positive forward spectral work from backscatter without importing a Fourier shell label by definition.

### OPEN — viscous scale bridge beyond monochromatic shells

Quantify the exact annular constants relating orientation-complete Kelvin q.v. density to scale-normalized Fourier-shell viscous payment without identifying smooth LP and hard projections.

## 2026-08-12 — Oriented flux and localized PDE bridge

- **EXACT:** For one helical edge, signed child-energy work equals a frequency/helicity coefficient times the GL(3)-invariant oriented material vorticity-flux 3-form `det(H)^(-1) Re(conj(Phi_q) . (Phi_1 x Phi_2))`.
- **NO-GO REFINED:** Metric/covariance alone cannot determine signed work because they are second-order; the missing information is genuinely third-order oriented flux information.
- **EXACT:** For `Phi_Q=H^T Q omega`, `D_t Phi_Q = H^T[(partial_t Q+[u.grad,Q])omega +(Q A-A Q)omega + nu Q Delta omega]`.
- **EXACT:** For `Q=I`, both localization commutators vanish and only the Kelvin/Nanson viscous flux remains.
- **EXACT:** The oriented cubic flux derivative splits linearly into interface/moving-cut, strain-selection, and viscosity terms; passive material-frame motion is not an additional source.
- **OPEN:** Instantiate this identity for the literal smooth/hard Fourier roles and literal Kelvin germ/quantile roles, then compare their physical source partitions without importing upstream closure claims.

- **EXACT / CALIBRATED:** A time-dependent role `Q(t)` carries the explicit time face `partial_t Q`.  Smooth moving-cut Action calibration shows that omitting it leaves exactly that residual; it cannot be hidden in `[u.grad,Q]`.

- **EXACT:** The full complex invariant `Z_H=det(H)^(-1) conj(Phi_3).(Phi_1 x Phi_2)` carries both signed-work quadrature and the gauge-invariant interaction phase `arg Z_H`.
- **EXACT SMALL-LOOP:** `Z_H` is the limit of the determinant-normalized oriented triple product of three role-filtered Kelvin circulation vectors on an orientation-complete small-loop packet.
- **EXACT:** Where `Z_H != 0`, phase velocity is `D_t arg Z_H = Im[(D_t Z_H)/Z_H]`; the localized PDE source decomposition therefore induces a phase-velocity decomposition without inventing a separate phase budget.

- **EXACT:** For a monochromatic resonant helical edge, viscosity acts on the complex interaction 3-form by real scalar damping `-nu(|k1|^2+|k2|^2+|q|^2) Z`; hence its interaction-phase velocity is exactly zero.
- **EXACT / CALIBRATED:** On a smooth periodic NSE state, instantaneous interaction-phase velocity splits into the literal vorticity transport and stretching convolutions plus viscosity; Action confirms the channel sum and zero monochromatic viscous phase rotation to floating precision.
- **OPEN:** Derive a coercive alternative for localized packets: persistent favorable `Re Z`, or quantified phase rotation sourced by literal interface/selection terms, or amplitude loss routed to existing physical reservoirs.

- **RIGOROUS CONSEQUENCE:** Inside a good real edge-coefficient corridor, favorable signed work has an exact trichotomy: persistent positive work, cubic-amplitude loss paying at least `log(1/rho)` total channel amplitude action, or phase loss paying at least `acos(c_lo)-acos(c_hi)` total channel phase action.
- **GUARDRAIL:** These logarithmic amplitude/phase actions are local diagnostic/action quantities, not globally bounded reset resources.  They must be converted to literal scale-sensitive physical source currencies before any recurrence claim.

- **EXACT STRUCTURAL BRIDGE:** The Fourier parent symplectic wedge is a `Lambda^2` determinant invariant under common `SL(2)` deformation; the complex material interaction is a `Lambda^3` determinant invariant under common incompressible deformation.  In both cases only relative generators/forcing change the interaction object.

## 2026-08-12 — Literal upstream localization audit and covariant owner calculus

Audited current upstream HEADs through MCP Linux Cloud only:

- `wang-ns-triad-diamond` `f56517caba641ccc109987c5eee4564b9fe66a55`;
- `ns-pde-first-kelvin-frontier` `517ced374ac2b48ebac9d7170bc5bb4151bd9437`.

### New exact identity

**EXACT NSE/PDE IDENTITY.**  With `K_u=u.grad-grad u`,

`C_Q = Qdot + [u.grad,Q] + [Q,grad u] = Qdot + [K_u,Q]`.

If `Qdot+[G,Q]=0`, then `C_Q=[K_u-G,Q]`.  This is the exact relative-generator owner calculus behind the exterior-algebra common-deformation cancellation.

### Wang literal specialization

**EXACT NSE/PDE IDENTITY.**  The literal hard event role is `P_{a sigma}=1_{C_a}(D)H_sigma(D)`; the propagated role is a distinct scalar smooth `Q(t,D)` with `QP=P`.  With `V=S_(N/4)u`, `h=u-V`, and the common affine generator used to transport `Q`,

`C_Q=[K_{V-V_aff},Q]+[K_h,Q]`.

For `zeta=curl h`, the exact physical HH vorticity source is

`-Q K_h zeta = curl[-Q P div(h tensor h)]`.

The companion `K_h(Q zeta)` is the transport/stretch repartition created by using the full material derivative and must not be charged as a second HH source.

**COUNTEREXAMPLE/NO-GO.**  Hard event `P`, smooth PDE carrier `Q`, resolved cutoff `V`, and smooth SGS filter `G_N` are not interchangeable.  A resolved-cutoff renewal is a decomposition gauge, not a `Qdot` time face.  SGS `RU`/pressure/window viscosity belong to the macroscopic resolved-energy ledger and must not be inserted again into the microscopic material-flux source.

**OPEN BRIDGE.**  `P(Q omega)=P omega` registers the hard event component, but the cubic built from full smooth envelopes generally contains overlap pollution.  A smooth-carrier phase theorem therefore does not yet imply persistence of literal hard-cell HH work between events.

### Kelvin literal specialization

**EXACT TYPE IDENTITY.**  The restart-layer literal first-bad selector is `M_fb^mf=M_fb tensor I_3`, realized as a closed-current map `P_fb^mf=K_mf M_fb^mf`.  This is the correct orientation-complete selector for a three-loop circulation triple, but it is current/germ-side rather than a primal Eulerian vorticity projector.

**EXACT CURRENT/PDE DUALITY IDENTITY.**  For `P=KM`,

`G_P=Pdot+T_X P-P A_g = G_K M + K G_M`.

This is the exact dual analogue of the primal localization commutator.  The literal hysteretic selector has `Mdot=0` between unresolved events; entry/resolve are finite jumps, not a smooth positive payment.

**RIGOROUS CONSEQUENCE.**  For a moving quantile `Q_t=1_{g<a(t)}`, fixed mass sets only the integrated weighted Reynolds face to zero.  The local density `(a_dot-g_t-j.grad g) delta_{g=a}` need not vanish.  One-dimensional and exact affine Mahalanobis shells are special co-moving cases.

**OPEN BRIDGE / NO-GO.**  The quantile/shell law currently lives on ancestry/reverse-age state and probability current.  It may not be equated with physical-time `Qdot+[K_u,Q]` until the programme-specific ancestry-to-physical Kelvin state map is constructed.  Stochastic Kelvin q.v./future covariance is second-order and cannot replace the signed cubic interaction phase/work observable.

### Localized owner alternative

**RIGOROUS CONSEQUENCE.**  On a fixed typed interval, any exact decomposition `Zdot=sum_o Zdot_o` into literal physical owners refines the existing trichotomy: amplitude loss pays total named log-amplitude action at least `log(1/rho)`; phase loss pays total named phase action at least `acos(c_lo)-acos(c_hi)`; otherwise favorable localized cubic interaction persists while geometry remains good.  Reselection, reset, geometry exit, or unresolved clock/state-map change is a typed stop requiring re-registration, not a free continuous payment.

Detailed derivation: `docs/11_literal_localization_owner_calculus.md`.

### Wang eventwise phase versus smooth-carrier energy handoff — follow-up audit

**EXACT OPERATOR IDENTITY / COUNTEREXAMPLE-NO-GO.**  For the literal commuting hard/smooth roles, `Q_i P_i=P_i Q_i=P_i`.  Writing `R_i=Q_i-P_i`, the smooth oriented cubic equals the hard cubic plus the seven nonempty `P/R` overlap terms.  `QP=P` therefore registers `P(Qv)=Pv` exactly but does not register the scalar cubic before hard projection.  No phase/cancellation conclusion about a hard edge follows from `Z_Q` alone.

**RIGOROUS CONSEQUENCE.**  The Wang smooth-material-carrier theorem supplies a different, genuinely physical handoff: for signed actual HH work density `r` and `0<=q<=1`, `[int q^2 r]_+ <= int q^2[r]_+ <= int[r]_+`.  Positive smooth-carrier HH energy therefore forces actual positive physical HH work, after which hard Fourier/helical roles and edge phase are read anew at the nonlinear event.  The literal architecture is `smooth carrier -> Q^2 energy gate -> actual positive HH work -> hard event edge/phase`, not persistent hard-edge phase between events.

**OPEN BRIDGE.**  A smooth-triple `Z_Q` trichotomy does not become Wang's causal event-phase theorem until the seven overlap terms are controlled or the next hard event is re-read.  The vorticity phase owner `C_Q` and the native `Q^2` kinetic-energy interface share the same relative resolved generator but are non-equivalent observables/currencies.

### Kelvin orientation covariance and state-map descent — follow-up audit

**EXACT OPERATOR IDENTITY.**  The literal orientation-complete restart selector `M_fb^mf=M_fb tensor I_3` commutes with every orientation reparameterization `I_G tensor L`, `L in GL(3)`.  On an unresolved branch `Mdot_fb=0`; first-bad selection therefore creates no continuous orientation connection or internal phase rotation.  Material-frame connection belongs to the current realization/Nanson geometry, while support commutator and finite reset remain separately typed.

**RIGOROUS CONSEQUENCE.**  This tensor-product selector is compatible with the GL(3)-invariant small-loop circulation triple: it selects a whole three-loop germ packet without privileging an orientation.  It does not by itself turn an ancestry germ label into a primal Eulerian localization.

**EXACT STATE-MAP DESCENT CRITERION.**  For an ancestry scalar cut `chi_Y` and state map `Pi:Y->X`, a target physical selector `chi_X` with `chi_Y=chi_X o Pi` exists iff `chi_Y` is constant on every fiber of `Pi`.  A hard chamber must therefore be a union of state-map fibers.  A quantile/shell cut separating two hidden ancestry states that realize the same physical Kelvin state is non-descending observer localization, not a physical NS source.

**OPEN BRIDGE.**  The Kelvin programme must establish selector descent first, then reverse-age/physical generator intertwining, before ancestry moving-cut faces can be identified with physical-time localized `Z_H` owners.

## 2026-08-12 — Current-upstream re-audit after concurrent HEAD advances

The upstream repositories advanced while the literal-localization audit was in progress.  Re-audited the new heads through MCP Linux Cloud:

- `wang-ns-triad-diamond` `a55ea1faa192427c22ba4e8141beb8c29bb3f263`;
- `ns-pde-first-kelvin-frontier` `2745fa2c979bbcc1c850dd57743e60881a3b565e`.

The previously audited hard/smooth role, first-bad selector, quantile/shell and clock operator files were not changed by these upstream commits.  Two new upstream theorems create additional direct PDE bridges.

### Cyclic closed-triad phase

**EXACT NSE/PDE / MATERIAL 3-FORM IDENTITY.**  For `k0+k1+k2=0`, reality and cyclicity give one common material interaction

`Z_0=Z_1=Z_2=Z_triangle`.

With `x_i=s_i/|k_i|`, the three root works are `T_i=kappa_i Re Z_triangle` with cyclic `kappa_i=2 x_i(x_j-x_l)` and `sum_i kappa_i=0`.  Thus triad energy conservation is a real-coefficient telescope multiplying one common phase.

**EXACT REPRESENTATION CONVERSION.**  Relative to the current Wang cyclic theorem `T_i=lambda_i R_triangle`, `kappa_i=-(2 s0 s1 s2/(|k0||k1||k2|)) lambda_i`, hence the common Wang cubic factor is the velocity/helical representative of the same material cubic work factor (modulo the common helical sign convention).

**COUNTEREXAMPLE/NO-GO.**  Negative donor/backscatter work is not equivalent to phase dephasing.  The same `Z_triangle` can give positive and negative root works simultaneously because the real root coefficients have different signs.

**RIGOROUS CONSEQUENCE.**  The current Wang donor/recipient kernel is same-time energy-owner redistribution of one common cubic event.  Cyclic re-rooting creates no phase source and cannot be treated as recurrence termination.

Detailed derivation: `docs/12_cyclic_triad_common_phase.md`.

### Stochastic Cauchy/material metric

**EXACT NSE/PDE IDENTITY.**  On one backward stochastic replica, `D_sigma=D(grad u)^T`, `F_C=D^T`, `H_C=rho^2 F_C^-T`, and `M_C=(H_C^T H_C)^-1` give

`D D^T = rho^4 M_C`,

`(D D^T)_sigma = 2 D S D^T`,

and `H_C (M_C)_sigma H_C^T = 2S`.

Thus the fixed-past stochastic Cauchy deformation Gram and the orientation-complete Kelvin packet metric are literally the same right Cauchy--Green geometry on the same replica.

**RIGOROUS CONSEQUENCE.**  `R_s=E[D D^T]=rho^4 E[M_C]`, and the total Cauchy second moment obeys `Q_s <= W_s R_s`.  The geometric factor in this envelope is not an invented norm.

**COUNTEREXAMPLE/NO-GO.**  Cauchy/material metric work is finite-variation strain and is distinct from centered stochastic covariance and martingale q.v.; the upstream affine-vortex calibration has nontrivial stretching with zero centered covariance.

**OPEN BRIDGE.**  Same-replica identity does not align a deterministic/hysteretic first-bad packet with the stochastic replica ensemble.  State-map descent, replica/selector alignment and clock/generator intertwining remain required before charging this bank to a selected physical `Z_H` role.

Detailed derivation: `docs/13_stochastic_cauchy_material_metric.md`.

## 2026-08-12 — Event-plateau readout, state-map clock residual, and common-replica phase cancellation

### Wang: full carrier retains event phase, scalar summaries do not

**EXACT OPERATOR / MATERIAL 3-FORM IDENTITY.**  For the literal event role/envelope pair `P_i Q_i=Q_i P_i=P_i`,

`P_i(Q_i omega_i)=P_i omega_i`,

hence the hard cubic read from the full smooth carrier is exactly the physical hard cubic:

`Z_P(Q_0 omega_0,Q_1 omega_1,Q_2 omega_2)=Z_P(omega_0,omega_1,omega_2)`.

The event readout is independent of the smooth envelope outside the hard plateau.

**COUNTEREXAMPLE/NO-GO.**  This full-field sufficiency does not imply `Z_Q=Z_P`; the smooth scalar cubic still contains seven overlap terms.  Nor can the quadratic carrier energy inherit cubic phase: modal phase rotation preserves all quadratic energies while rotating `arg Z_P`.

**RIGOROUS TYPING CONSEQUENCE.**  The literal Wang architecture does not need persistent hard phase between events.  Energy is propagated by the smooth `Q^2` carrier and actual physical HH work; hard phase is read from the actual field at the physical event.  A later role `P+` need not satisfy `P+ Q-=P+`, so no event-to-event phase theorem is claimed.

Detailed derivation: `docs/14_event_plateau_phase_readout.md`.

### Kelvin: clock/state-map incompatibility has an exact face

**EXACT PDE/STATE-MAP IDENTITY.**  After selector descent through `Pi_t:Y->X`, define

`R_Pi = partial_t Pi + DPi b_Y - b_X o Pi`.

Then

`L_Y(chi_X o Pi) - (L_X chi_X)oPi = grad chi_X(Pi).R_Pi`.

For a hard cut `chi_X=1_{g<a}`, the residual is the distributional interface face

`-delta_(g(Pi)=a) grad g(Pi).R_Pi`.

Only the normal component of `R_Pi` crosses the interface; tangential mismatch is reparameterization.

**COUNTEREXAMPLE/NO-GO.**  `Mdot_fb=0` in the ancestry/germ clock does not imply a physically frozen selector unless the descended interface has zero normal state-map/clock residual.

**RIGOROUS TYPING CONSEQUENCE.**  Fiber descent, generator/clock intertwining, and fixed-mass integrated-face cancellation are logically distinct and must occur in that order.

Detailed derivation: `docs/15_state_map_clock_residual.md`.

### Kelvin: common Cauchy deformation is cubic-phase neutral

**EXACT NSE/CAUCHY / EXTERIOR-ALGEBRA IDENTITY.**  On one incompressible stochastic Cauchy replica, `det D=1`, so for any three complex legs

`conj(D z0).(D z1 x D z2)=conj(z0).(z1 x z2)`.

Equivalently a common generator contributes only `tr(G) Z`, hence zero for incompressible common deformation.

**EXACT OWNER DECOMPOSITION.**  With leg generators `G_i` and any common reference `G`, only the relative generators `G_i-G` plus explicit forcing terms change the cubic interaction.

**RIGOROUS CONSEQUENCE.**  Same-replica metric stretching can be large while cubic phase stays exactly fixed.  Continuous Kelvin-side phase rotation therefore belongs to relative replica/current realization, moving cut/state-map clock mismatch, viscosity/forcing, or a typed jump—not to common Cauchy deformation itself and not to the orientation-blind first-bad selector.

**OPEN BRIDGE.**  The literal selected first-bad packet is still not identified with a stochastic replica/coupling.  The remaining task is to construct that coupling and the programme-specific state map, then evaluate the relative-generator and normal-interface residuals rather than a generic covariance surrogate.

Detailed derivation: `docs/16_common_replica_phase_cancellation.md`.

### ACTION STRESS TEST — run 31582930093

GitHub Actions passed `experiments/exp13_event_clock_replica.py` on theorem commit `a43519b0239dd4ab014656fc4e947bfd0ecd221a`.

Adversarial calibrations:

- hard-event plateau readout residual: `0.000e+00`;
- maximum smooth-summary overlap gap: `3.000e+01`;
- quadratic-energy / phase-rotation residual: `7.105e-15`;
- state-map chain-rule residual: `2.842e-14`;
- tangential hard-face contraction residual: `2.665e-15`;
- minimum sampled normal hard-face signal: `3.335e-02`;
- common-replica `SL(3)` cubic residual: `6.439e-14`;
- relative-generator decomposition residual: `1.589e-14`;
- maximum sampled relative-replica cubic-rate magnitude: `7.597e+01`.

**Classification: ACTION STRESS TEST only, not proof.**  The large smooth-summary gap and relative-replica rate are intentional adversaries: they confirm that the exact cancellations disappear when the theorem's hard-readout/common-replica hypotheses are removed.

## 2026-08-12 — Conditional-kernel selector and cubic-resolution closure

Re-audited `ns-pde-first-kelvin-frontier` at `2745fa2c979bbcc1c850dd57743e60881a3b565e` through MCP Linux Cloud only.  No upstream file, branch, issue, or pull request was modified.

### Reduced ancestry is generally a kernel, not a deterministic state map

**EXACT KERNEL/PDE IDENTITY.**  For the literal conditional lift `R F(y)=int F(Y) kappa_y(dY)`, the complete generator-intertwining owner is

`D_R = partial_t R + L_y R - R L_Y`.

The earlier deterministic `Pi` theorem is the Dirac-kernel branch.  For a deterministic Itô map, both drift and pushed diffusion must match; only after diffusion compatibility does a hard-interface mismatch reduce to the normal drift residual.

### Selector purity has an exact pair witness

For a physical hard selected set `A`, let `alpha=kappa_y(A)`.  Then

`alpha(1-alpha) = (1/2) E[(chi_A(Y1)-chi_A(Y2))^2 | y]`.

**EXACT NECESSARY AND SUFFICIENT CRITERION.**  A hard reduced selector exists iff this quantity is zero, equivalently iff the conditional kernel lies entirely on one physical side of the cut.  Positive value is unresolved physical-side membership, not viscous q.v.

### Same-state cubic versus independent replicas

**EXACT THIRD-ORDER RESOLUTION IDENTITY.**  The conditional physical cubic `R T(Phi0,Phi1,Phi2)` equals the cubic of conditional means plus three pair-resolution contractions and one centered third-order oriented moment.  Three independent conditional replicas give only the cubic of means.

**COUNTEREXAMPLE/NO-GO.**  Uniform even- and odd-parity four-hidden-state kernels can have identical first and second moments while their same-state signed cubic interactions are opposite.  Therefore no covariance/q.v.-only bridge can reconstruct signed phase.

### Trilinear stochastic transfer

**EXACT GENERATOR IDENTITY.**  The diffusion product defect

`Gamma_L^(3)=L T - sum_i T(...,L Phi_i,...)`

is exactly the sum of pair derivative contractions with the third leg retained.  Under exact kernel intertwining, the homogeneous cubic resolution object obeys

`H_y Delta_3^res = Gamma_y^(3)[m] - R Gamma_Y^(3)[Phi]`.

With physical leg sources there is one separately typed source-resolution defect.  This is the third-order analogue of the upstream covariance carre-du-champ transfer law.

**PHYSICAL TYPING.**  Common incompressible Cauchy finite-variation deformation remains phase-neutral.  Stochastic state diffusion can transfer cubic content only through the oriented trilinear `Gamma^(3)` owner.  Independent variance replicas must not be substituted for same-state interaction legs by analogy.

Detailed derivations: `docs/17_kernel_selector_resolution.md`, `docs/18_conditional_cubic_resolution.md`, `docs/19_trilinear_resolution_transfer.md`.

### New frontier

The Kelvin bridge is now reduced to literal semantics rather than an estimate problem: construct the actual full/reduced ancestry state and conditional kernel; determine whether the first-bad selected set is kernel-pure; identify the literal full-state interaction-leg/payoff observables; then evaluate the exact third-order resolution and trilinear diffusion/source owners.  No recurrence, restart-capacity, or regularity claim is made.

### Interaction-sufficiency hierarchy

**COUNTEREXAMPLE/NO-GO.**  Kernel selector purity can hold exactly while cubic resolution remains nonzero: a non-Dirac parity kernel may lie wholly inside one selected physical set.  Thus hard support descent does not imply phase descent.  Identical second-order data likewise do not imply phase descent.

**EXACT NECESSARY-AND-SUFFICIENT NO-GO.**  On a standard-Borel full physical state space, if a conditional kernel preserves the oriented cubic by factorization for every bounded interaction-leg triple, then the kernel is Dirac.  Universal cubic sufficiency therefore means no nontrivial hidden-state reduction.  A useful reduced programme must instead prove sufficiency for its restricted physical event algebra or carry `Delta_3^res` explicitly.

Detailed derivation: `docs/20_interaction_sufficiency_hierarchy.md`.

### ACTION STRESS TEST — run 31583870491

GitHub Actions passed `experiments/exp14_kernel_cubic_resolution.py` on theorem commit `e4edb1ca9719f080cede88368c9f4b8c75d89a20`.

Adversarial calibration output:

- selector pair-disagreement residual `3.331e-16`;
- minimum sampled genuinely mixed selector variance `3.873e-04`;
- conditional cubic-resolution residual `5.927e-15`;
- maximum same-state/independent cubic gap `1.214e+01`;
- even/odd parity first-second-moment residual `0.000e+00`;
- parity cubic sign-flip residual `0.000e+00`, with signed-cubic separation `1.173e+01`;
- trilinear carré-du-champ residual `1.214e-13`, with sampled transfer magnitude `4.625e+02`;
- finite-state cubic-resolution transfer residual `7.944e-15`, with sampled transfer magnitude `6.415e+01`.

These are numerical/action stress tests only, never proof.

## 2026-08-12 — Cauchy exterior-volume resolution after Kelvin vectorized covariance advance

Re-audited Kelvin upstream `c1773ffa8fa5cc4bfa8fb5aa461dd4b43dbed1c1` read-only.  Its new literal object is the full deformation covariance `Sigma_D=Cov(vec D)` with exact reverse-age connected source `Gamma_D^vec=2 nu sum_mu vec(partial_mu Dbar) vec(partial_mu Dbar)^T`; `C_D^Gram` is only the column partial trace entering the mean packet metric.

**EXACT NSE/STOCHASTIC 3-FORM IDENTITY.**  For fixed terminal vectors and one common real stochastic Cauchy deformation `D in SL(3)`, the same-replica cubic is exactly `Z_same=Z_0`, while the cubic of three independent replica means is `Z_ind=det(Dbar) Z_0`.  The resolution defect is `(1-det Dbar) Z_0`.  While `det Dbar>0` this defect is radial amplitude resolution, not continuous phase rotation; a sign flip must pass through zero amplitude.

**EXACT PDE IDENTITY.**  With `H_h Dbar=A^T Dbar` and incompressibility, `J_D=det Dbar` obeys `H_h J_D=-(1/2) Hess(det)(Dbar):Gamma_D^vec`, equivalently the sum of three oriented pair-column derivative determinants.  The source is indefinite although `Gamma_D^vec` is PSD.

**RIGOROUS SHORT-HORIZON CONSEQUENCE.**  `delta_D=1-det Dbar=-(nu h^3/3) sum_mu tr((partial_mu grad u)^2)+O(h^4)`.  This differs structurally from the PSD row-Gram onset `(2nu/3) h^3 sum (partial_mu grad u)^T(partial_mu grad u)`.

**EXACT NSE CALIBRATION.**  The smooth periodic 2D eigenstreamfunction `psi=e^{-5nu t}[cos(x+2y)+a cos(2x+y)]`, embedded in 3D, gives at `x=y=pi/6` the coefficient `sum tr((partial_mu A)^2)=-72 a e^{-10nu t}`, hence `delta_D=24 nu a e^{-10nu t} h^3+O(h^4)`.

**COUNTEREXAMPLE/NO-GO.**  Kelvin's exact one-mode NS shear has `Sigma_D>0` and `C_D^Gram>0` but `Dbar=I+cbar E21`, so `det Dbar=1` exactly and the fixed-terminal same/independent cubic interactions agree.  Deformation covariance or metric mismatch therefore does not imply cubic amplitude loss, still less phase rotation.

Detailed derivations: `docs/21_cauchy_exterior_volume_resolution.md`, `docs/22_mean_deformation_determinant_pde.md`, `docs/23_deformation_covariance_phase_no_go.md`.

## 2026-08-12 — Full Cauchy payoff: phase survives only in terminal and mixed resolution after common deformation quotient

**EXACT STOCHASTIC CAUCHY IDENTITY.**  For arbitrary random complex terminal/role vectors `w_i` on the same replica and real pathwise incompressible Cauchy deformation `D`, `T(Dw_0,Dw_1,Dw_2)=T(w_0,w_1,w_2)` pathwise.  Thus common Cauchy deformation disappears exactly from the same-replica cubic even when terminal vectors and deformation are correlated.

**EXACT MIXED-RESOLUTION IDENTITY.**  With `Dbar=E D`, `wbar_i=E w_i`, the mean current leg is `m_i=Dbar wbar_i+r_i`, where `r_i=E[(D-Dbar)(w_i-wbar_i)]` is a mixed deformation--terminal correlation vector.

**EXACT THREE-OWNER FACTORIZATION.**  Writing `Delta_w=E T(w_0,w_1,w_2)-T(wbar_0,wbar_1,wbar_2)` and `C_Dw` for the seven trilinear terms containing at least one `r_i`, `Z_same-Z_ind=(1-det Dbar)Z_wbar+Delta_w-C_Dw`.  The first term is radial while `det Dbar>0`; the latter two are genuinely complex and are the first hidden-state Cauchy sectors capable of continuous phase rotation after common deformation is quotiented.

**EXACT WEIGHTED SELECTION IDENTITY.**  For any legitimate scalar physical event weight `chi`, even if it depends on deformation, `E[chi T(Dw_0,Dw_1,Dw_2)]=E[chi T(w_0,w_1,w_2)]`.  A selected first-bad law therefore does not turn common `SL(3)` deformation into a phase owner.  Selection changes phase only through reweighting terminal/role resolution, mixed correlations, or explicit localized PDE sources.

**OPEN BRIDGE.**  The literal first-bad badness/resolve event set remains undefined upstream.  Once supplied, the remaining phase bridge is selected interaction-law sufficiency plus mixed/third-order source dynamics, not equality of deterministic and stochastic packet metrics.

Detailed derivations: `docs/24_full_cauchy_payoff_factorization.md`, `docs/25_selection_commutes_with_cauchy_volume.md`.

## 2026-08-12 — Full-vorticity transpose gauge and mixed Cauchy phase owners

**EXACT NSE IDENTITY.**  With the upstream Jacobian convention `A=grad u`, `A-A^T=[omega]_x`, hence `(A-A^T)omega=omega cross omega=0`.  Full physical vorticity therefore satisfies both `L_nu omega=A omega` and `L_nu omega=A^T omega`.  The apparent Cauchy transpose seam closes on the actual full field.

**EXACT LOCALIZED CONNECTION IDENTITY.**  A role `Q omega` is not generally self-aligned.  The exact `A`-connection and `A^T`-connection source ledgers differ by `[omega]_x Q omega`.  This is a common real trace-free skew connection.  When all three cubic legs are transformed consistently its `Lambda^3` contribution cancels exactly.  Changing transpose convention without moving this compensating role source creates an artificial polarization/phase residual.

**EXACT MIXED CONNECTED LAW.**  For a homogeneous fixed-past terminal vector mean `wbar_i` under the same reverse anchor semigroup, with `H_h Dbar=A^T Dbar`, `H_h wbar_i=0`, `H_h m_i=A^T m_i`, the mixed vector `r_i=m_i-Dbar wbar_i` obeys `H_h r_i=A^T r_i+2nu sum_mu (partial_mu Dbar)(partial_mu wbar_i)`.  Its source is a complex mixed deformation--terminal carré-du-champ, not a PSD covariance tensor.

**RIGOROUS SHORT-HORIZON HIERARCHY.**  For smooth fixed-past terminal fields, terminal-anchor cubic resolution starts at `O(nu h)`, mixed deformation--terminal correlation at `O(nu h^2)`, and pure deformation exterior-volume resolution at `O(nu h^3)` when the corresponding leading coefficients are nonzero.  This is a causal-order statement, not a long-time norm comparison or lower bound.

Detailed derivations: `docs/26_vorticity_transpose_connection_gauge.md`, `docs/27_mixed_cauchy_terminal_correlation_pde.md`, `docs/28_cauchy_resolution_onset_hierarchy.md`.

## 2026-08-12 — First-bad Boolean realizability and finite interaction reset face

**EXACT BOOLEAN REALIZABILITY.**  If a reduced ancestry state `y` lifts through `kappa_y` to full physical states and a full-state bad set has occupancy `beta_i=kappa_y(B_i)`, then the current deterministic `bad_flags[i]` can represent that physical event iff `beta_i in {0,1}`.  Equivalently its same-ancestor pair disagreement `beta_i(1-beta_i)` vanishes.  The independent `resolved` oracle obeys the same criterion for its own physical event set.  Mixed occupancy cannot be silently substituted into the hard hysteretic API.

**NECESSARY ADMISSIBILITY.**  Full bad/resolve events must also be invariant under exact representation gauges: ancestry reference gauge, passive packet `GL(3)` orientation changes, and the `A`/`A^T` connection gauge with compensating role-source re-registration.  Otherwise the same physical NS state would produce different event flags.

**EXACT FINITE EVENT IDENTITY.**  For event weights `chi^- -> chi^+` and complex same-state cubic `Z(Y)`, the unnormalized jump is `Z^+-Z^-=E[(chi^+-chi^-)Z]`.  For positive selected masses, the normalized jump is `[E Delta chi (Z-Zhat^-)]/alpha^+`.  This is a finite complex reweighting face, not a continuous positive source.  Common `SL(3)` Cauchy deformation cancels pathwise through the jump.

**OPEN BRIDGE.**  Kelvin still supplies no literal physical badness or resolve set.  These theorems constrain any future definition but do not invent one.

Detailed derivations: `docs/29_first_bad_boolean_kernel_realizability.md`, `docs/30_finite_selector_cubic_jump.md`.

## 2026-08-12 — Hybrid continuous/event phase-work ledger

**EXACT HYBRID LOGARITHM IDENTITY.**  For a nonzero piecewise absolutely continuous interaction `Z` with finitely many typed event jumps, total log-amplitude change is the sum of continuous `Re(Zdot/Z)` integrals plus finite event `log(|Z^+|/|Z^-|)` jumps.  A lifted phase obeys the analogous identity with `Im(Zdot/Z)` plus finite event angles; the branch-free phase path length is the continuous owner variation plus principal event geodesic jumps.

**RIGOROUS HYBRID NO-FREE-ESCAPE.**  Amplitude loss to `rho|Z_0|` forces continuous owner amplitude action plus discrete event amplitude action at least `log(1/rho)`.  Loss of favorable alignment from `c_hi` to `c_lo` forces continuous owner phase action plus finite event angular jumps at least `acos(c_lo)-acos(c_hi)`.  Otherwise, while the signed-work geometry coefficient remains `>=kappa_*>0` and no typed structural exit occurs, favorable work remains quantitatively positive.

**EVENT TYPING.**  Selector entry/resolve/reselection contributes through its exact finite reweighting jump and must not be smeared into neighboring continuous phase action.  This closes the local bookkeeping seam across finitely many already-legitimate events but supplies no uniform event-count bound, reset bank, recurrence termination, or regularity theorem.

Detailed derivation: `docs/31_hybrid_phase_work_ledger.md`.

## 2026-08-12 — Local peak growth gate is directional metric work versus Kelvin q.v.

**EXACT NSE/MATERIAL IDENTITY.**  With `e=|omega|^2/2`, material area frame `H`, metric `M`, and `Phi=H^T omega`, the objective identity `H Mdot H^T=2S` converts the exact enstrophy law to `D_t e=(1/2) Phi^T Mdot Phi + nu Delta e - nu|grad omega|^2`.  Using the orientation-complete Kelvin microframe, `nu|grad omega|^2=(1/2) sum_j gamma_dens(n_j)`.  Thus the physical ledger is directional material-metric strain work minus Kelvin bulk q.v. plus signed curvature flux.

**RIGOROUS LOCAL-MAX GATE.**  At a spatial local maximum of enstrophy, positive material growth requires `(1/2)Phi^T Mdot Phi > nu|grad omega|^2`.  The producer is a directional anisotropy work, not a norm or isotropic volume change; incompressibility keeps the material metric determinant fixed at a fixed reference scale.

**EXACT AFFINE NS CALIBRATION / SCOPED NO-GO.**  In the exact affine vortex flow `A=[[-a,-r,0],[r,-a,0],[0,0,2a]]`, `r=r0 e^(2at)`, vorticity is spatially uniform, `grad omega=Delta e=0`, and `G=omega.S.omega=8 a r0^2 e^(4at)`.  Every point is a non-strict spatial local enstrophy maximum and the solution is smooth at every finite time.  Hence any finite threshold on this local growth margin alone cannot be a universal continuation-failure flag on a solution class containing these affine flows.  This no-go does not address narrower periodic/finite-energy classes or strict/nondegenerate maximum hypotheses.

**TYPE SEPARATION.**  The local peak gate is quadratic directional metric/q.v. physics; signed interscale work remains cubic oriented-flux physics.  A future first-bad definition may use both, but cannot identify them.

Detailed derivation: `docs/32_local_peak_metric_qv_gate.md`.

## 2026-08-12 — Exact two-flow no-go: local peak growth versus Cauchy deformation covariance

**EXACT AFFINE BRANCH.**  Spatially uniform affine vortex stretching has `D_t e=8 a r0^2 e^(4at)>0` at every non-strict local enstrophy maximum, while spatially uniform `A` makes the conditional Cauchy deformation deterministic and hence `Sigma_D=C_D^Gram=0`.  Positive peak growth does not require stochastic deformation covariance.

**EXACT PERIODIC SHEAR BRANCH.**  For `u=(e^(-nu k^2t) cos ky,0,0)`, at the strict active-direction enstrophy maximum `y=pi/(2k)`, stretching and instantaneous Kelvin vorticity-gradient q.v. vanish and `D_t e=-nu k^4 e^(-2nu k^2t)<0`.  Nevertheless the exact finite-horizon Cauchy variance is `k^2 e^(-2alpha t)[(cosh(2alpha h)-1)/(2alpha^2)-h^2]>0` for every `h>0`.  The row-Gram covariance lies in `e2`, orthogonal to the `e3` vorticity direction.

**COUNTEREXAMPLE/NO-GO.**  `Sigma_D>0` is neither necessary nor sufficient for positive local peak enstrophy growth.  Current directional stretching and finite-horizon Brownian-anchor deformation dispersion are distinct NS mechanisms and clocks.

Detailed derivation: `docs/33_growth_covariance_two_flow_no_go.md`.

## 2026-08-12 — Cauchy gradient geometry: strain variation, vorticity variation, and Kelvin-q.v. complement

**EXACT SHORT-HORIZON DECOMPOSITION.**  With `A=S+Omega`, `Omega=(1/2)[omega]_x`, `P_mu=partial_mu S`, `Q_mu=(1/2)[partial_mu omega]_x`, each Cauchy row-Gram source splits as `(partial_mu A)^T(partial_mu A)=P_mu^2-Q_mu^2+(P_mu Q_mu-Q_mu P_mu)`.  The first two pieces are PSD strain-gradient and rotation-gradient dispersion; the third is symmetric trace-free orientation coupling.

**EXACT KELVIN-QV COMPLEMENT.**  The rotation-gradient contribution is `C_Omega=(h^3/12)[tr(Gamma_K)I-Gamma_K]+O(h^4)` with `Gamma_K=2nu(grad omega)(grad omega)^T`.  Thus finite-horizon rotation-induced deformation dispersion occupies the transverse complement of the instantaneous Kelvin vorticity-gradient q.v. tensor.

**RIGOROUS SIGNED EXTERIOR-VOLUME CONSEQUENCE.**  `1-det Dbar=(nu h^3/6)|grad omega|^2-(nu h^3/3)|grad S|_F^2+O(h^4) = (h^3/12)tr Gamma_K-(nu h^3/3)|grad S|_F^2+O(h^4)`.  The determinant source is physically a vorticity-gradient versus strain-gradient competition, explaining why it has no fixed sign.

**EXACT SHEAR CALIBRATION.**  In one-mode shear, `|grad omega|^2=2|grad S|_F^2`, so exterior-volume onset cancels; the trace-free strain/rotation cross sector is nevertheless essential to rotate the full row-Gram covariance into the single `e2` direction.  This locally explains `det Dbar=1` and the upstream exact covariance orientation.

Detailed derivation: `docs/34_cauchy_gradient_geometry_decomposition.md`.

## 2026-08-12 — Vectorized Cauchy inverse dictionary

**EXACT DUAL PARTIAL TRACES.**  The full `9x9` deformation covariance has two natural contractions: `C_row=E[DD^T]-Dbar Dbar^T` and `C_col=E[D^T D]-Dbar^T Dbar`.  At `O(nu h^3)`, they are respectively sums of `(partial A)^T(partial A)` and `(partial A)(partial A)^T`.

**RIGOROUS MATRIX INVERSE.**  `(C_row+C_col)/2` contains PSD strain-gradient plus Hodge-lifted rotation-gradient dispersion, while `(C_row-C_col)/2` isolates the symmetric trace-free strain/rotation commutator.  Subtracting `(h^3/12)[tr Gamma_K I-Gamma_K]` from the even part recovers `(2nu h^3/3) sum_mu (partial_mu S)^2+O(h^4)`.

**RIGOROUS SCALAR INVERSE.**  With `T_h=tr C_row` and `delta_h=1-det Dbar`, `tr Gamma_K = lim_(h->0) [3T_h+6delta_h]/h^3` and `nu|grad S|_F^2 = lim_(h->0)[3T_h-6delta_h]/(4h^3)`.  Positive deformation covariance trace and signed exterior-volume defect are complementary enough to separate instantaneous vorticity-gradient q.v. trace from strain-gradient magnitude.

**EXACT SHEAR CALIBRATION.**  One-mode shear has row Gram along `e2`, column Gram along `e1`, and their half-difference is exactly the orientation-coupling tensor.  Keeping only one partial trace loses this dual geometry.

Detailed derivation: `docs/35_vectorized_cauchy_inverse_dictionary.md`.

## 2026-08-12 — Kelvin q.v. exterior-power ladder

**EXACT EXTERIOR REPRESENTATION.**  For any `G:R^3->R^3`, the induced actions are `R_1(G)=G`, `*G^[2]*^-1=(tr G)I-G^T`, and `R_3(G)=tr G`.  Applying this to the symmetric Kelvin q.v. tensor `Gamma_K` gives one rigid degree-1/2/3 hierarchy.

**RIGOROUS CAUCHY CONSEQUENCE.**  The rotation-gradient Cauchy covariance is `C_Omega=(h^3/12) R_2(Gamma_K)+O(h^4)`, while the vorticity-gradient contribution to `1-det Dbar` is `(h^3/12) R_3(Gamma_K)+O(h^4)`.  The common coefficient is forced by the reverse-age Cauchy onset.  Rank-one q.v. along `n` lifts to an exact transverse-plane tensor `lambda(I-nn^T)` at degree two.

**TYPE SEPARATION.**  The exterior ladder resolves the rotation/vorticity-gradient branch only; strain-gradient and strain/rotation coupling remain separately typed physical sectors.  Reducing `Gamma_K` immediately to its trace preserves the top-volume contribution but destroys two-plane orientation information.

Detailed derivation: `docs/36_kelvin_qv_exterior_power_ladder.md`.

## 2026-08-12 — Current Kelvin `ceca144`: reduced-state covariance resolution blocks naive Cauchy inverse

Re-audited Kelvin upstream `ceca144d51b8585986145f89323fbffa6f075d6e` read-only.  It now explicitly specializes the existing connected vector-covariance/pair theorem to `Sigma_D` and proves the reduced/full law `Sigma_D^red=R Sigma_D+Cov_R(zbar)`: intrinsic same-clock deformation covariance and hidden-state resolution covariance are distinct additive sectors.  The actual ancestry lift kernel remains open-literal.

**EXACT REDUCED GRAM/EXTERIOR LEDGER.**  Both row and column Cauchy Gram covariances inherit separate resolution faces.  Mean top exterior power has the independent face `delta_Lambda3^res=R det(Dbar)-det(RDbar)`, so `delta_red=R delta_full+delta_Lambda3^res`.  Therefore the AL/AM inverse combinations at reduced state equal averaged physical gradient currencies plus explicit resolution contamination.

**RIGOROUS ORDER NO-GO.**  If hidden full states have different current traceless gradients, `Cov_R(Dbar)=O(h^2)` generically, one order earlier than intrinsic Brownian-anchor Cauchy covariance `O(nu h^3)`.  Applying the `h^-3` inverse formulas without removing resolution can therefore diverge.

**EXACT AFFINE NSE COUNTEREXAMPLES.**  An equal hidden mixture of exact affine `+/-` pure strains has zero physical `grad S` and `grad omega` in every full state but produces `T_red=2sinh^2(ah)`, `delta_red=-sinh^2(ah)`, causing the naive reduced strain inverse to behave as `3a^2/h`.  An equal hidden mixture of exact `+/-` rigid rotations likewise has zero physical gradient currencies but produces `T_red=2sin^2(ah)`, `delta_red=sin^2(ah)`, causing the naive reduced Kelvin-q.v. inverse to behave as `12a^2/h`.

**ADMISSIBILITY.**  Reduced-state inversion is physical only when the lift is Dirac on the relevant deformation state, the resolution faces are subtracted, they are proved `o(h^3)`, or the theorem explicitly returns physical average plus resolution owner.

Detailed derivation: `docs/37_reduced_cauchy_inverse_resolution_no_go.md`.

## 2026-08-12 — Current Wang `8d21df4`: cyclic hard-cell single charge is phase-diagonal provenance

Re-audited Wang upstream `8d21df4d1971f96c90fd0406136f4fa1882d3ad9` read-only. Its certified hard-cell theorem pushes the already-physical closed-triad donor/recipient measure through deterministic hard cells, preserving canonical donor `dW^-` and good/bad recipient `dW^+` exactly once. Coarse self-loops remain real same-time work with zero recursive depth and no scale progress.

**EXACT PHASE-FIBER CONSEQUENCE.** Theorem M gives one common complex `Z_triangle` for all three cyclic roots. Hence every donor/recipient atom of the physical closed-triad kernel carries the same phase mark. Adjoining that mark to Wang's hard pushforward gives an identity phase kernel: routing changes energy owner/provenance, not interaction phase. Coarse hard-cell self-loops are label aliasing, not phase loops or recurrence.

**COUNTEREXAMPLE/NO-GO.** The unmarked hard donor table cannot reconstruct phase. `Z_+=R exp(i theta)` and `Z_-=R exp(-i theta)` have identical `Re Z`, hence identical root works and donor tables, but opposite phases. The single-charge theorem is an energy-routing theorem, not a hidden phase law.

**SIGN REVERSAL.** Negating the real field sends `Z_triangle -> -Z_triangle`, reverses root works and swaps donor/recipient roles, while routing remains phase-diagonal within the new physical event. This matches Wang's current evolved-NS sign-reversal audit without creating a phase source.

Detailed derivation: `docs/38_wang_single_charge_phase_fiber.md`.

## 2026-08-12 — Action calibration record for Theorems V–AQ

All executable checks below are **ACTION STRESS TESTS, not proofs**.  Proof status remains the exact PDE/operator/exterior/conditional identities recorded in the corresponding docs.

Successful GitHub Actions runs during this research pass:

- `31585189414` — Cauchy exterior-volume / covariance-phase separation;
- `31585507364` — full Cauchy payoff and selected-event factorization;
- `31586511972` — transpose-gauge / mixed-correlation / onset hierarchy after algebraic referee repair;
- `31586860618` — first-bad Boolean-kernel and finite cubic reset;
- `31587099671` — hybrid continuous/event phase-work ledger;
- `31587576636` — local peak material-metric/Kelvin-q.v. gate after normalized referee repair;
- `31587989654` — exact NS growth/deformation-covariance two-flow no-go;
- `31588548071` — strain/rotation-gradient Cauchy geometry and Kelvin-q.v. Hodge complement;
- `31588774303` — vectorized Cauchy dual-partial-trace inverse dictionary;
- `31588989587` — Kelvin q.v. exterior-power ladder;
- `31589566191` — reduced-state Cauchy inverse-resolution no-go, with all previous lanes passing;
- `31589912336` — Wang cyclic single-charge phase fiber, with all previous lanes passing.

Transparent failed-referee lineage:

- `31586337634` failed because an `eps=1e-5` second-difference referee amplified floating roundoff in a cubic polynomial.  The theorem and tolerance were not weakened; the referee was replaced by the exact symmetric algebraic extraction at `eps=1`, yielding residual `5.124e-14` in successful run `31586511972`.
- `31587469046` failed because subtracting two equal affine-growth values of size about `1e10` produced an absolute floating residual around `1e-6`.  The theorem and threshold were not weakened; the referee was replaced by the dimensionless invariant ratio, yielding residual `2.220e-16` in successful run `31587576636`.

Latest stress signals include: false reduced strain inverse `1.051e+04`, false reduced Kelvin-q.v. inverse `1.137e+04` under pure hidden affine-state mixing; Wang hard-cell phase-fiber residual `0`, `504` sampled coarse self-loops, and phase separation `2.593` radians hidden by an identical unmarked donor table.

## 2026-08-12 — Actual energy donor transport yields a killed lineage and a parabolic termination mechanism

**EXACT NSE / TRANSPORT IDENTITY.**  Using current Wang `8d21df4` only for its literal same-time donor/recipient marginals, modal energy obeys `E_i'=sum_j K_ji-sum_j K_ij-2nu|k_i|^2E_i`.  Since a zero-energy mode has zero nonlinear work, `r_ij=K_ij/E_i` is well typed with zero convention on empty modes.  Conditional on the actual solution and donor kernel this is an exact sub-Markov energy lineage: nonlinearity moves energy, viscosity alone kills it.  No FIFO/LIFO pairing is introduced.

**EXACT FUTURE-HEAT GAUGE.**  `q_i^T=exp[-2nu|k_i|^2(T-t)]` cancels the viscous killing face exactly, so `H_T=sum q_iE_i=(1/2)||exp(nu(T-t)Delta)u||_2^2` changes only by donor transport `sum(q_j-q_i)K_ij`.  The complementary heat-defect `w=1-q` obeys `B_T'=sum(w_j-w_i)K_ij-sum2nu|k_i|^2E_i`.  This is a PDE-generated bounded coordinate, not an external norm penalty.

**RIGOROUS STOPPED-LINEAGE BUDGET.**  Stop a selected lineage at reverse/nonforward/reentry edges.  If all internal edges satisfy `Delta w>=0`, then exact mass conservation gives `int F_progress <= sum q_i(s)m_i(s) <= M(s)`.  If `Delta w>=c_*>0`, the normalized energy lineage has expected continuation depth at most `1/c_*`.  This removes global backscatter cancellation only because reverse transfer is an absorbing physical exit, not because it was discarded.

**RIGOROUS PARABOLIC KILLING LAW.**  For `a=2nu(T-t)N^2`, continuous motion has `a_dot=-2nuN^2`, exactly the killing hazard.  A forward jump `N^+/N^- >= lambda` from `a^->=alpha` raises `a` by at least `c_jump=(lambda^2-1)alpha`.  If the same lineage remains below `a<=beta`, depth `n` forces hazard `>=n c_jump-beta`, hence surviving energy mass `<=M_0 exp(beta-n c_jump)`.

**CONDITIONAL FINITE-DEPTH THEOREM.**  If the same physical continuation additionally has `N_jE_j>=eta` and `lambda<=N_{j+1}/N_j<=Lambda`, then depth is finite whenever `c_jump>log Lambda`, with explicit bound `[log(M_0N_0/eta)+beta]/[c_jump-log Lambda]`.  Wang signed-good ratios make the numerical condition non-vacuous (`alpha>~0.3274`), but the third repo does not import the Wang recursion and does not claim the literal first-bad event satisfies it.

**COUNTEREXAMPLE/NO-GO.**  Removing the lower parabolic face allows infinite geometric depth with finite hazard; reverse jumps refund the heat coordinate without viscous waiting; removing the upper scale ratio lets the critical floor collapse too fast; removing the mass floor leaves zero-mass exceptional paths; free re-entry restarts the budget.  These are now explicit acceptance conditions for the next first-bad theorem.

Detailed derivations: `docs/39_energy_transport_killing.md`, `docs/40_future_heat_parabolic_currency.md`, `docs/41_stopped_lineage_parabolic_budget.md`, `docs/42_parabolic_killing_depth_criterion.md`, `docs/43_parabolic_termination_hypothesis_audit.md`.

## 2026-08-12 — Terminal parabolic corridor decay and the literal first-bad reduction target

**RIGOROUS TERMINAL NON-ACCUMULATION.**  A stopped selected energy population confined to `alpha<=2nu(T-t)N^2<=beta` satisfies `M(t)<=M(s)[(T-t)/(T-s)]^alpha` by physical viscous killing alone.  A same-population scale-critical event `NE>=eta` in the same corridor needs at least `eta sqrt(2nu/beta)(T-t)^(1/2)` energy.  Hence `alpha>1/2` excludes accumulation of such events at the candidate terminal time.  No event counting or forward-jump ratio is used inside the corridor.

**EXACT CAPTURE KINEMATICS.**  If continuing scale jumps have `N^+/N^-<=Lambda` and `beta>Lambda^2 alpha`, a jump from `a<alpha` cannot land above `beta`, while continuous clock motion only decreases `a`.  Every subparabolic-to-superparabolic transition must therefore visit the corridor.  Unbounded nonlocal UV jumps are a distinct physical exit, not a violation of the coordinate.

**RIGOROUS CONDITIONAL FIRST-BAD REDUCTION / OPEN BRIDGE.**  If a future full-PDE theorem says that, absent named exits, a bad state at scale `N` extends the full smooth solution for `c_*/(nu N^2)`, then first-singular-time semantics force `2nu N^2(T-t)>=2c_*`.  This would derive the parabolic lower face from NSE lifespan itself.  Current Wang natural service is carrier-local and current Kelvin `dc26c0c` is selected-current/pair typing only; neither supplies this missing full-solution theorem.

**CURRENT KELVIN `dc26c0c` READ-ONLY AUDIT.**  The new upstream theorem gives `T(P,D)=P tensor D^T`, proves Cauchy deformation cannot manufacture a boundary seam for a closed selected cycle, and splits replica-dependent selected pair content into selector, deformation, and mandatory cross sectors.  It also proves by exact heat-shear NS that local `D` does not close finite current shape.  This supports the no-cloning/type discipline but is not identified with the modal energy lineage of AR--AV.

Detailed derivations: `docs/44_terminal_parabolic_corridor_decay.md`, `docs/45_parabolic_corridor_capture.md`, `docs/46_first_bad_parabolic_reduction.md`.

## 2026-08-12 — Active enstrophy record floor and the donor/catalyst split

**EXACT NSE ENSTROPHY OWNER.**  `Y=||grad u||_2^2` obeys `(1/2)Y'+nu||Delta u||_2^2=W_ens`, with pressure absent by Leray/gauge orthogonality.  Only after this physical work is identified, a dyadic Bony decomposition gives `|W_ens|<=C_LP [sup_N sqrt(N)||P_Nu||_2] ||Delta u||_2^2`.

**RIGOROUS ACTIVE-EVENT FLOOR.**  At every nontrivial enstrophy record-growth time `Y'>=0`, some actual shell satisfies `N||P_Nu||_2^2>=nu^2/C_LP^2`.  A candidate first singular time has arbitrarily late such record events because bounded `H^1` gives a standard positive restart interval.  This floor applies to the active record shell only and therefore does not contradict the Wang amplitude-homogeneity no-go against fixed mass on every ancestry root.

**DONOR/CATALYST TYPE SPLIT.**  The energy donor side is governed by AR--AX killed-lineage physics.  A distinct low-frequency structural parent may catalyze high-scale generation without losing the same energy.  For one materially reused reservoir, Kelvin covector transport gives `M_(j+1)/M_j<=exp(Sigma_j)`, while Galilean-neutral increment service per unit physical energy scales as `M^3/N^2`.  Against child progress `N_(j+1)/N_j>=lambda`, low strain `Sigma_j<=sigma` gives catalyst service ratio `<=exp(3sigma)/lambda^2`.  If this is `<1`, one old reservoir cannot service infinitely many uniformly efficient generations.

**OPEN SCALE-ROLE BRIDGE.**  The active critical shell forced at an enstrophy record is not yet proved to sit in the terminal parabolic corridor.  If it is too low, it must be treated as a catalyst/strain reservoir rather than mislabeled as the donor child.  The remaining literal theorem must route each record event to parabolic donor continuation or to strain/interface/relink/high-tail/service exits.

Detailed derivations: `docs/47_record_enstrophy_critical_shell.md`, `docs/48_material_reservoir_service_half_life.md`.

## 2026-08-12 — Enstrophy is the first spectral moment of the same actual energy donor transport

**EXACT NSE / DONOR-MOMENT IDENTITY.**  Because `(1/2)||grad u||_2^2=sum |k_i|^2 E_i`, AR with `f_i=|k_i|^2` gives `(1/2)Y'+nu Z=sum_ij(|k_j|^2-|k_i|^2)K_ij`.  The global vorticity/enstrophy producer is therefore not a separate mysterious cubic currency: it is the first squared-frequency moment of the already-physical single-charge energy transport table.

**RIGOROUS RECORD-GROWTH CONSEQUENCE.**  Splitting the moment into up/down frequency parts, every `Y'>=0` time has `F_kappa^+>=nu Z+F_kappa^-`.  Thus record growth requires actual upward energy transport sufficient to beat viscosity and any simultaneous backscatter/down-frequency transport.

**EXACT PARABOLIC READING.**  With `a=2nu(T-t)|k|^2`, the nonlinear parabolic drift is `F_a=2nu(T-t)[Y'/2+nu Z]`.  For a forward edge with both endpoints below `beta`, `Delta w>=exp(-beta)Delta a`; hence record-producing work inside a bounded heat corridor spends the stopped future-heat currency directly.  Remaining record growth is forced into subparabolic, superparabolic/nonlocal, or typed exit sectors.

Detailed derivation: `docs/49_enstrophy_energy_transport_moment.md`.

## 2026-08-12 — Uniqueness of the future-heat energy currency

**EXACT GENERAL PARABOLIC WEIGHT LAW.**  For `F_f=sum f(a_i)E_i`, `a_i=2nu(T-t)|k_i|^2`, one has `F_f'=sum Delta f K-sum d_i[f+f']E_i`.  Clock motion and viscous killing are therefore coupled by the one-dimensional operator `f -> f+f'`.

**RIGOROUS UNIQUENESS.**  Zero weighted killing with terminal normalization `f(0)=1` forces `f=e^-a`.  Exact unweighted physical killing with `f(0)=0` forces `f=1-e^-a`.  Future-heat survival/defect are not arbitrary exponential test functions; they are the unique normalized coordinates with these physical jobs.

**COUNTEREXAMPLE/NO-GO.**  For every fixed multiplicative scale ratio `lambda>1`, `Delta w=e^-a-e^(-lambda^2 a)` vanishes as `a->0` and `a->infinity`.  Thus the exact bounded kinetic-energy currency cannot assign a uniform price to scale jumps globally.  Its sensitivity peaks at `a_*=2log lambda/(lambda^2-1)`.  The parabolic corridor and typed sub/superparabolic exits are forced by the generator itself.

Detailed derivation: `docs/50_unique_parabolic_energy_coordinate.md`.

## 2026-08-12 — Corridor Reynolds current, mass-floor-free blow-up exclusion, and hysteretic reentry cost

**EXACT MOVING-CUT CURRENT.**  The hard parabolic corridor energy obeys `M_C'=sum(chi_j-chi_i)K_ij-sum d_i chi_i E_i+sum dot(chi_i)E_i`.  Nonlinear crossing, viscous killing and heat-clock motion are distinct.  Since `a_dot=-d<0`, the upper clock face enters the corridor and the lower clock face exits it; clock motion cannot generate a recurrent sub->corridor loop.

**RIGOROUS MASS-FLOOR-FREE SECTOR EXCLUSION.**  A first singular solution has `H1` lower blow-up rate `Y>=c_H nu^(3/2)tau^-1/2`.  An old selected corridor population with lower face `alpha>1/2`, no incoming mass, and upper face `beta` has mass `O(tau^alpha)` and enstrophy `O(tau^(alpha-1))`, hence contributes a vanishing fraction `O(tau^(alpha-1/2))` of the required singular enstrophy.  Persistent matched-corridor activity therefore needs arbitrarily late physical input, not mere survival of old energy.

**RIGOROUS HYSTERETIC CYCLE CONSEQUENCE.**  If actual bad/resolve semantics uses `alpha_-<alpha_+`, one clean reentry-return cycle with no negative parabolic jump costs at least `alpha_+-alpha_-` of viscous killing hazard.  Repeated cycles have exponential survival loss.  A reverse jump avoiding that hazard is itself a physical down-frequency owner.  Current Kelvin's hysteresis makes this a natural acceptance test, but its physical bad/resolve gap is not yet supplied.

Detailed derivations: `docs/51_parabolic_corridor_reynolds_current.md`, `docs/52_corridor_cannot_carry_h1_blowup.md`, `docs/53_hysteretic_parabolic_reentry_killing.md`.

## 2026-08-12 — Radial mode-set layer cake after Wang `ae85f4d`

**READ-ONLY UPSTREAM COMPATIBILITY.**  Wang `ae85f4d` certifies helical mode-set energy continuity: persistent stock is physical helical modal energy, same-time donor flow has exact graph divergence on arbitrary measurable mode sets, and radial mode boundaries are explicitly named as the next scale-bearing specialization.  This independently validates the physical stock/current ontology of AR while preserving the anti-theorem that gross internal nonlinear traffic is not a finite energy budget.

**EXACT RADIAL LAYER CAKE.**  For `A_R={|k|^2<=R}`, actual outward/inward donor currents `Phi_up/Phi_down` satisfy `F_kappa^+=int Phi_up dR`, `F_kappa^-=int Phi_down dR`.  Therefore enstrophy production is the net unweighted radial kinetic-energy current.  Future-heat progress is the same net radial current weighted by `2nu tau exp(-2nu tau R)`.  The matched/sub/superparabolic split is literally a decomposition of this physical radial control-volume current.

Detailed derivation: `docs/54_radial_mode_flux_layer_cake.md`.

## 2026-08-12 — Nonlocal companion geometry and a record-derived critical-shell selector

**EXACT CLOSED-TRIAD GEOMETRY.**  A donor-to-recipient jump with `|k_r|>=Lambda|k_d|` forces the third triad root to satisfy `|k_c|>=(1-1/Lambda)|k_r|`.  A subparabolic-to-superparabolic skip therefore has a contemporaneous comparable high-frequency companion.  UV skipping is not low-frequency energy teleportation; it reduces to donor transfer plus high-frequency companion ancestry.

**RIGOROUS RECORD-EVENT CONSTRUCTION.**  At every enstrophy record choose a strict fraction of BA's PDE-forced critical amplitude and take the highest dyadic shell above that level.  Smoothness makes this highest shell finite; all higher shells are critical-subthreshold.  The first later higher-shell crossing of the same PDE-derived level is a well-defined spectral event.  Optional two-level hysteresis avoids grazing but is not yet identified with the Kelvin bad/resolve semantics.

**OPEN BRIDGE.**  The remaining subparabolic problem can now be asked on a concrete state: before the next higher critical crossing, the entire higher tail is uniformly subthreshold, so continued record growth must be produced by low-scale strain/catalyst interaction or by a typed source/relink/high-tail event.  A full PDE theorem turning that alternative into continuation/termination remains open.

Detailed derivations: `docs/55_nonlocal_jump_companion_geometry.md`, `docs/56_record_critical_shell_event_semantics.md`.

## 2026-08-12 — Minimal unresolved owner graph

After AR--BJ and read-only audits of Wang `ae85f4d` / Kelvin `7dc3a87`, the global recurrence frontier is compressed to three genuine seams rather than a long owner list.

**S: subparabolic critical-shell renewal.**  BJ supplies a highest PDE-critical record shell and subthreshold higher tail, but a full-PDE own-scale lifespan / first-stop theorem is still missing.

**U: high-companion renewal.**  BI proves every nonlocal UV energy jump needs a comparable high-frequency triad companion.  Old low-strain companions have finite service, high-strain tracking fires its own owner, so indefinite UV skipping requires repeated new/relinked/fragmented companion ancestry or genuine high-tail/source renewal.

**R: material/reselection reentry.**  Kelvin `7dc3a87` closes full current-shape joint covariance/cross terms but keeps finite shape as its own state.  A physical hysteresis gap would let BG price repeated reentry; gapless or kernel-impure relabelled reentry remains open.

Phase, common deformation, covariance, hard-cell/checkpoint rereading, old matched energy populations, eventually-pure high strain, and eventually-pure signed-good HH no longer need independent infinite-cycle nodes in the proposed global proof skeleton.  Breadth/entropy is retained as a mechanism for renewing U/R ancestry, not as an additional energy source.

Detailed reduction: `docs/57_minimal_unresolved_owner_graph.md`.

## 2026-08-12 — AR--BJ proof-mechanism Action lineage

All executable checks below were run only by GitHub Actions after commit/push.  They are **ACTION STRESS TESTS**, not proofs; the analytic identities and consequences are recorded separately in the theorem spine/docs.

- AR--AW, commit `501fcd14b395456c4ae720be0e884175b8753c6c`: run `31600977353` SUCCESS.  Donor-kernel master/Dynkin/future-heat residuals were at `0`--`2.3e-13`; stopped-lineage/hazard/depth checks passed; the collapsing-lower-face adversary retained finite hazard after 80 forward jumps and reverse-jump refund closed to `2.22e-16`.
- AX--AZ, commit `d7ebcf491f62a2eadea5806985388fd2ccc08493`: run `31602163531` SUCCESS.  Corridor decay, capture, and conditional lower-face violations were zero; unbounded jumps skipped the corridor as intended and `alpha<1/2` preserved the cheap-survival no-go.
- BA--BB, commit `4992db2c9a9f7089b8dbd86924a35bfc014d33ab`: run `31603373405` SUCCESS.  Actual spectral amplitude homogeneity passed at `1.326e-13`; catalyst service ratio at `7.772e-16`; Wang-compatible ratio `(21/20)^3(5/8)^2=0.452197266`.
- BC, commit `99b8484e4c2753a4c18312b7c453191f040d7802`: run `31603864970` SUCCESS.  Enstrophy/donor-energy transport-moment and heat-corridor identities passed.
- BD was committed locally as `35bd6bd1f7d12cd06a06522093188416dc6071e6`; its first `git push` hit a Linux-Cloud network/cgroup timeout before remote mutation.  No theorem or Action failed.  The exact commit was then included unchanged in the next successful push together with BE--BG.
- BD + BE--BG, remote head `ee31b8cf2c67912e420ff8e5a512ba92548d3e9c`: run `31604972072` SUCCESS.  Unique heat-coordinate generator residual `2.842e-14`; both endpoint price no-gos visible; corridor current `1.421e-14`; clock monotonicity, hysteretic gap, and survival identities exact to displayed precision; reverse shortcut explicitly registered as a `0.7` owner signal.
- BH--BJ + minimal S/U/R owner graph, commit `edc71e1ea66a28946d19caad2ffb3820810dbfec`: run `31606469143` SUCCESS.  Radial outward/inward/enstrophy layer-cake residuals `4.547e-13`, heat-weighted radial residual `3.553e-15`; nonlocal companion, parabolic-skip companion fraction, and highest-critical-shell selector violations all `0`.

Read-only upstream compatibility was re-audited at Wang `ae85f4df372cd2942a0181c1a8f105cd4118edec` (certified helical mode-set energy continuity) and Kelvin `7dc3a871cfa5f8e9c362a38a383978b13988940e` (full current-shape Kelvin covariance / deformation--circulation cross covariance).  Neither upstream was modified.

## 2026-08-12 — Radial high-tail memory erasure removes S as an independent owner

**EXACT MODE-SET CONSEQUENCE.** For the radial high set `A_R`, current Wang mode-set continuity gives `E_R' + D_R + Phi_down = Phi_up` with `D_R>=2nu R^2 E_R`. Hence `E_R(t)<=exp(-2nu R^2L)E_R(t-L)+int exp(-2nu R^2(t-s))Phi_up ds`.

**RIGOROUS FRESH-FUNDING CONSEQUENCE.** If a hard shell at scale `N` has `N E_N(t)>=eta` and lies above `rho N`, choosing `L_N=[log(2E_*N/eta)]/(2nu rho^2N^2)` forces at least `eta/(2N)` of exponentially weighted actual upward radial work during `[t-L_N,t]`. Thus a late critical shell cannot be ancient UV stock; `L_N=O((log N)/(nu N^2))->0`.

**RIGOROUS TAIL-ABSORPTION CONSEQUENCE.** For the strict higher tail above the highest PDE-active shell, the pure tail self-interaction obeys the same `B_(1/2) Z` estimate as the full enstrophy work. Choosing the activation fraction below the resulting absorption constant makes pure UV self-work at most one quarter of viscous palinstrophy. Any high-tail record growth then forces at least `3nu/4` palinstrophy worth of lower-frequency incidence/boundary work.

**OWNER REDUCTION.** A higher critical crossing is therefore an actual freshly funded radial-work event; if no higher crossing occurs while enstrophy grows without bound, the subcritical tail must be externally serviced. Subparabolicity itself is no longer an independent recurrence owner. The minimal unresolved graph contracts from `S/U/R` to `U/R`, with global measurable assembly still open.

Detailed derivations: `docs/58_radial_high_tail_memory_erosion.md`, `docs/59_subcritical_tail_self_absorption.md`, `docs/60_subparabolic_seam_elimination.md`.

## 2026-08-12 — Exact radial record-flux gate

**EXACT RADIAL LAYER CAKE.** With `F(R)=Phi_up(R)-Phi_down(R)` and tail gradient stock `G(R)=sum_(|k|>R)|k|^2 E_k`, the nonlinear enstrophy work and palinstrophy obey `W_ens=int 2R F(R)dR` and `Z=int 2R G(R)dR`.

**RIGOROUS RECORD CONSEQUENCE.** At every enstrophy record-growth time, `W_ens>=nu Z`, so some physical radial boundary satisfies `F(R)>=nu G(R)=D_R/2`, where `D_R=2nu G(R)` is the actual viscous killing of the full high set outside that radius. Gross cyclic traffic cannot fake the event because the gate uses net outward current.

**SELECTOR TYPING.** This supplies an exact radial-current first-bad coordinate complementary to the BJ highest-critical-shell energy coordinate. It uses no LP/Bony estimate and creates no new scalar currency.

Detailed derivation: `docs/61_radial_record_flux_gate.md`.

## 2026-08-12 — Low-strain carrier memory erasure contracts U

**EXACT OWNER INPUT.** After the smooth `Q^2` energy law, low--low moat and common observer quotient, a selected high carrier has only HH work, physical skew relink, symmetric strain, typed source/interface input and viscosity.

**RIGOROUS NO-INPUT CONSEQUENCE.** On an interval with no positive HH/relink/source input, `E_A' <= [2||S_V||_op - 2nu c_-^2N^2]E_A`, hence `E_A(t)<=exp(2K_A-2nu c_-^2N^2L)E_A(s)`. A terminal critical floor `E_A(t)>=eta/N` therefore forces either the strain action above any chosen physical face `K_0` or a positive HH/relink/source owner within `L_N=[2K_0+log(E_*N/(delta eta))]/(2nu c_-^2N^2)=O((log N)/(nu N^2))`.

**OWNER REDUCTION.** Passive old high-companion service is not an independent recurrence mechanism. After resolved incidence is split, the remaining UV seam is fresh generic HH/relink/source renewal alternating with strain. The graph is sharpened from `U/R` to `G/R`, where `G` denotes fresh typed high-frequency owner recurrence, not a new scalar currency.

Detailed derivations: `docs/62_low_strain_carrier_memory_erasure.md`, `docs/63_high_companion_owner_reduction.md`.

## 2026-08-12 — Radial record-gate owner trichotomy

**EXACT POSITIVE-FLOW PARTITION.** At a BN gate, `Phi_up>=nu G`. Partition the actual upward recipient law first by whether **either quadratic interaction parent** lies below `R/4`. This prevents a near-boundary energy donor with a low companion from being mistyped as local HH.

**RIGOROUS CONSEQUENCE.** Every record gate has either (i) hard low--high work whose exact skew-redistribution or symmetric-strain row carries at least `nu G/4`; (ii) genuinely comparable outward work at least `nu G/4`, with all three mode scales in `[R/4,5R)` and total ratio `<20`; or (iii) UV-skip work at least `nu G/4`, in which every closed triad has a companion above `3R`.

Detailed derivation: `docs/64_record_gate_owner_trichotomy.md`.

## 2026-08-12 — Signed-helical martingale branching is the exact nonlinear enstrophy owner

**EXACT TRIAD IDENTITY.** Besides `sum T_i=0`, every closed helical triad obeys `sum x_i T_i=0` with `x_i=s_i|k_i|`. A one-donor/two-recipient event therefore has donor signed frequency equal to the recipient barycenter and contributes `+Q Var(x)` to nonlinear enstrophy work; a two-donor/one-recipient event has recipient equal to the donor barycenter and contributes `-Q Var(x)`.

**GLOBAL CONSEQUENCE.** `Y'/2 + nu Z = V_split - V_merge`, with both variance terms nonnegative. At every enstrophy record, `V_split>=nu Z+V_merge`. Only one-donor branching splits can create nonlinear enstrophy; two-donor merges oppose it.

**CANONICAL ENTROPY.** A binary split with fraction `p` carries actual donor-kernel entropy `Q h_2(p)` and `h_2(p)>=2p(1-p)`. On a BQ-comparable triad `|x_i|<5R`, this gives `Q h_2(p)>=V_split/(50R^2)`.

**NO-GO.** Cyclic charge share times scale has no universal contraction. The homochiral strict triangle `(1,16,16.5)` has two donors and one recipient; the low donor routes 100% of its charge to the recipient sixteen times higher. The full event is a merge and therefore enstrophy-destructive, showing why rooted scale-share bookkeeping is the wrong object.

Detailed derivations: `docs/65_signed_helical_frequency_branch_variance.md`, `docs/66_cyclic_share_scale_no_go.md`.

## 2026-08-12 — Global owner quotient and convex-order branching hierarchy

**GLOBAL OWNER QUOTIENT.** BR shows the unforced full-state enstrophy ledger has one positive nonlinear owner: one-donor signed-frequency split variance. Two-donor merge variance and viscosity are sinks. Phase, strain, radial geometry, material service and interface decompositions remain important rate/provenance refinements of the same triad law, not additional global enstrophy sources. Reduced/material state fidelity is therefore an auxiliary-admissibility seam, not a physical global source term.

**EXACT CONVEX-ORDER HIERARCHY.** For every convex `phi(s|k|)`, one-donor splits contribute a nonnegative Jensen gap and two-donor merges the opposite gap. Affine `phi=1,x` recover energy/helicity invariance; `phi=x^2` is the exact enstrophy variance law.

**PARABOLIC INFLECTION.** The unique future-heat defect `w_tau(x)=1-exp(-2nu tau x^2)` has `w_tau''=4nu tau exp(-a)(1-2a)`, so its exact signed-frequency branching curvature changes sign at `a=1/2`. For a split entirely in `a<=alpha<1/2`, the defect Jensen gap is at least `2nu tau exp(-alpha)(1-2alpha)` times the BR variance work. The same half-face independently appears in the old-corridor H1 exclusion theorem; this is structural alignment, not a global reset theorem.

Detailed derivations: `docs/67_global_enstrophy_owner_quotient.md`, `docs/68_convex_order_helical_moment_hierarchy.md`, `docs/69_parabolic_currency_branching_inflection.md`.

## 2026-08-12 — Vandermonde compression and rate-critical split scale

**EXACT TRIAD COMPRESSION.** For every observable `phi`, `sum phi(x_i)T_i = -R_triangle (x0-x1)(x1-x2)(x2-x0) phi[x0,x1,x2]`. Enstrophy (`phi=x^2`) is the bare signed-frequency Vandermonde times the common cubic. Affine energy/helicity have zero second divided difference. If `|x_i|<=K`, the exact geometry capacity is `|Vandermonde|<=2K^3`, with equality at `(-K,0,K)`.

**RATE-CRITICAL SCALE.** Partition one-donor split variance by actual triad maximum frequency `K_triangle` and palinstrophy by the same dyadic scale. At every enstrophy record some shell obeys `V_split,q>=nu Z_q`. Triangle geometry then has only two classes: two-high/one-low (`min<K/4`, other two `>3K/4`) or all-comparable (`all >=K/4`). One class carries at least `nu Z_q/2`.

**ACTUAL WORK LOWER.** Since split variance `Q Var(x)<=K_triangle^2 Q<4N_q^2Q` on the block, the owner class has donor-work rate `Q_owner>=nu Z_q/(8N_q^2)>= (nu/8)N_q^2E_q`. This is a branch-specific physical work-vs-viscous-rate gate, not a new threshold norm.

Detailed derivations: `docs/70_vandermonde_divided_difference_triad_law.md`, `docs/71_record_split_rate_scale_gate.md`.

## 2026-08-13 — BY–CB: helical critical-mass compensation law

**EXACT NSE/PDE IDENTITY.**  The absolute signed-frequency first moment `C=sum |s|k|| E = sum |k|E` has nonlinear source only when a closed-triad split/merge crosses helicity sign.  Heterochiral one-donor splitting creates equal positive/negative critical-helicity charges; reversing the event annihilates the same pair.  Homochiral events do not create this stock.

**RIGOROUS CONSEQUENCE.**  On fully comparable homochiral splits, high-scale progress leaks critical mass to the lower recipient and the leakage satisfies `L>=V/(4K)`.  On fully comparable heterochiral splits, high-branch critical-mass gain equals the opposite-helicity sibling charge and `V/(16K)<=P<=4V/K`.

**OWNER REDUCTION.**  Combining with BX, a rate-critical comparable split must pay either downward critical-mass leakage `>=nu Z_q/(32N)` or opposite-helicity pair creation `>=nu Z_q/(128N)`.  Exhaustion of these compensation channels remains open; no regularity conclusion is claimed.

## 2026-08-13 — CC–CE: finite pair action continues the PDE

**RIGOROUS CONTINUATION CRITERION.**  If the total actual opposite-helicity pair-creation action is finite on `[0,T)`, the exact critical-mass ledger bounds both `sup C` and `int B`; modal Cauchy gives `int Y^2<infinity`, and only then a standard enstrophy Gronwall step bounds `H^1`.  Hence a finite first singular time requires `int P_create=infinity`.

**EXACT RADIAL IDENTITY.**  Net pair creation minus annihilation is half the unweighted radial first moment of the same physical donor/recipient energy current.  This places the final owner directly in Wang's certified radial-control-volume geometry.

**EXACT SEPARATED GEOMETRY.**  For heterochiral normal form `-b<a<c`, `P=b(c-a)|R|` and triangle geometry gives `c-a<b`; the opposite-recipient physical capacity yields `P<=4b^2|a0 a1 a2|`.  Low-opposite and low-donor separated branches are therefore physically distinct.

## 2026-08-13 — CF–CH: quotient the last owner to positive net critical radial action

**RIGOROUS CONTINUATION CRITERION.**  The sharp state-level requirement is finite positive variation of the signed degree-one radial current `J1`, not finite gross pair creation.  Create/annihilate cycling cancels before the criterion.  A first singular time requires `int [J1]_+ = infinity`.

**EXACT NSE/HELICITY IDENTITY.**  The positive- and negative-helicity critical stocks obey twin equations with the same nonlinear source `N=Pcreate-Pann`; signed helicity is the source-free difference mode.  The final nonlinear obstruction is therefore paired two-sector injection.

**COUNTEREXAMPLE/NO-GO.**  The integrated final action is scale-critical whereas the kinetic-energy budget scales subcritically.  A universal energy-budget bound is dimensionally impossible; the remaining proof must exploit heterochiral/radial/split-merge structure.

## 2026-08-13 — CI–CJ: exact separated Waleffe depletion and local-core no-go

**EXACT NSE/WALEFFE CONSEQUENCE.**  Heterochiral pair action has a closed area/coupling envelope.  Low-donor/high-pair events gain one low/high ratio; low opposite-helicity recipients gain two low-scale factors.  These exhaust separated heterochiral geometry.

**COUNTEREXAMPLE/NO-GO.**  The fully comparable triangle `(3/4,3/4,1)` has dimensionless pair-capacity coefficient `sqrt(10)/24`, so the local heterochiral core has no scale-decaying Waleffe factor.  The remaining closure is genuinely critical rather than a missed geometric depletion.

## 2026-08-13 — CK: exact Hadamard heterochiral diamond adversary

**COUNTERMODEL/NO-GO.**  The lattice recurrence `p+q, p-q` gives an exact nested comparable diamond with scale ratio `sqrt(2)` and alternating `+/-` helicity tracks.  Static one-donor fractions amplify high-branch critical mass by `4-2sqrt(2)>1` even while kinetic energy fraction falls.  Thus topology, conservation and parabolic-time summability alone cannot close the final action.

**ACTION TARGET.**  The companion full Fourier--Galerkin NSE referee asks whether actual shared-mode birth phases generate both first and second Hadamard generations.  A positive signal is adversarial evidence only, not a cascade proof.

### CI/CJ referee correction provenance

Initial Action `31650446519` correctly rejected the hand-written explicit comparable constant while all structural Waleffe/depletion residuals were green.  The Heron area for `(3/4,3/4,1)K` is `K^2 sqrt(5)/8`, giving the stronger exact coefficient `sqrt(10)/24 = 0.131761569...`; no theorem hypothesis or tolerance was weakened.

## 2026-08-13 — CL–CM: rate-critical pair creation requires full-dimensional Fourier participation

**RIGOROUS LATE-STAGE CONSEQUENCE.**  After exact owner reduction, a safe convolution bound shows `P_cmp<=16 N^2 ||c||_1 ||c||_2^2`.  Combining with CB forces `M_eff>=nu^2 N^3/(2048^2 mu_part)`.  At fixed critical mass this has full `N^3` spectral-volume scaling.

**COUNTEREXAMPLE/NO-GO.**  Finite-mode/Hadamard ladders may be useful phase/topology adversaries but cannot carry the ultraviolet rate gate with fixed critical mass.  A genuine singular mechanism must broaden to dense coherent Fourier participation or enter a separately typed large-critical-mass branch.

## 2026-08-13 — CN: failed Hadamard ladder reveals exact full-vector polarization obstruction

**FAILURE LINEAGE / EXACT PDE CORRECTION.**  Actions `31651033582` and `31651133703` strongly birthed the first Hadamard siblings but kept the proposed second axial modes at `~1e-20`; the failed assertion was not weakened.  Direct NSE algebra shows why: orthogonal equal-scale `+/-` parents generate both first siblings parallel to the common normal, hence with equal `+/-` helical magnitudes and zero sibling mutual interaction.

**EXACT NSE/PDE IDENTITY.**  The whole seed lies in a 2D3C class.  The horizontal flow is a single Laplacian eigenspace and evolves only by heat decay; the vertical component is passive.  Static rooted-helicity channels therefore cannot be recursively composed without the full vector polarization state.

## 2026-08-13 — CO–CP: full-vector heterochiral birth polarization law

**EXACT NSE/WALEFFE IDENTITY.**  Opposite-helicity parents do not generate an independently choosable child helicity.  The two child-fiber source magnitudes are in ratio `(1+delta)/(1-delta)`, `delta=(a-b)/c`, giving exact Stokes polarization `2delta/(1+delta^2)`.  Every strict triad births both helicities.

**RIGOROUS CONSEQUENCE.**  Near-pure fresh birth forces `|delta|->1`, hence triangle-area/Waleffe depletion.  This supplies a full-vector renewal constraint missing from rooted energy/helicity channel graphs; inherited old polarization remains a separate state case.

### CL/CM referee normalization provenance

Action `31651734164` passed the corrected Hadamard polarization lanes but exp49 stopped on an absolute subtraction residual `9.313e-10` between two algebraically identical rate-gate expressions evaluated at large random magnitudes.  Young and participation violations were exactly zero.  The referee now records the native relative equality residual; no theorem constant or hypothesis was changed.

## 2026-08-13 — CQ: current Wang true-upward theorem quotients the final pair owner to first-shell comparable supply or resolved contact

Re-audited Wang `76e6ee97efe2f014e67e2e2209b3f6228af7b0a5` read-only.  Its certified hard-tail theorem uses actual radial `Phi_up`, proves pure-UV upward atoms only enter `M=2N` with comparable parents, and forces every deeper direct upward atom to have resolved-scale parent contact.

**EXACT REPO-3 CONSEQUENCE.**  A heterochiral pair-creation split always contains a donor-to-high-recipient true-upward atom.  On Wang's first-shell pure-UV branch the pair charge `dP=b dT_o^+` is within fixed `N` factors of the actual opposite-helicity positive child-work law, and CB becomes an actual-work rate lower.  Deep supply is not silently renamed strain; positive resolved-contact binding remains open exactly as upstream states.

## 2026-08-13 — CR: fixed-critical rate gate forces efficient mixed-polarization edges

**RIGOROUS CONDITIONAL CONSEQUENCE.**  Under the natural `O(N^3)` Fourier support-volume bound and a fixed participating critical mass `mu<=M0 nu^2`, the comparable pair rate lower is a fixed fraction of a literal helical capacity measure.  At least half actual pair action lies on edges with uniform positive work/capacity efficiency.

**FULL-VECTOR CONSEQUENCE.**  Those efficient edges are uniformly away from triangle degeneracy, so CO forces a fixed nonzero minority-helicity fraction in their fresh child source.  This supplies local efficiency/polarization hypotheses for a future weighted reuse/holonomy assembly without asserting that old child state is fresh-source dominated.

## 2026-08-13 — CS: repo-3 plateau transporter closes deep pair positive binding

**EXACT FOURIER SUPPORT / NSE REPARTITION.**  Anchor a dyadic scale to the actual pair-action donor and choose a new smooth transporter equal to one on `B_(M/8)` and supported in `B_(M/4)`.  For `M>=8N` the donor is exactly resolved and low--low output cannot reach the high child, so the pair source is literally resolved mixed `V/h` work; positive work then splits into conservative skew redistribution or symmetric strain.

**RIGOROUS ALTERNATIVE.**  If the deep condition fails, `c/a<16`.  This closes the contact-to-owner seam for deep repo-3 pair events without asserting that Wang's own transporter has a plateau and without modifying upstream.

## 2026-08-13 — CT: exact universal pair-capacity constant sharpens dense-core efficiency

**RIGOROUS TRIAD GEOMETRY.**  Every heterochiral pair-creation coefficient satisfies `eta_pair<=4sqrt(2)/27`.  This is proved analytically by separate `K=c` and `K=b` triangle envelopes, not inferred from Action search.

**RIGOROUS DOWNSTREAM STRENGTHENING.**  The aggregate comparable capacity improves from the intentionally crude constant `16` to `64/27`; CL participation and CR mean-efficiency constants were updated accordingly.  No physical hypothesis was changed.

## 2026-08-13 — CU: heat memory erosion upgraded from fresh energy to fresh amplitude

**EXACT MILD NSE / RIGOROUS CONSEQUENCE.**  On a high-pass set, heat semigroup erases the old vector itself.  A terminal critical shell therefore forces a recent nonlinear Duhamel contribution of at least `3/4` of the critical amplitude after a logarithmic natural-scale window.  This supplies the missing amplitude-side input for future polarization attachment; inter-atom/time cancellation remains a separately typed phase phenomenon.

### CO/CP referee ratio-coordinate provenance

Action `31652859240` reached exp51 after all preceding corrected lanes passed.  The Stokes-polarization and minority-fraction identities were at `~1e-15`, while the direct quotient `|F+|/|F-|` produced a `2.054e-05` numerical residual near the strict-triangle boundary where the denominator tends to zero.  The referee now checks the equivalent cross-multiplied identity `F+(1-delta)=F-(1+delta)` in a native normalized residual.  No CO/CP hypothesis or theorem constant changed.

## 2026-08-13 — CV: exact spin-2 azimuthal cancellation blocks a false polarization shortcut

**COUNTEREXAMPLE/NO-GO.**  Rotational covariance around a fixed child axis, combined with a compensating common parent-product phase, leaves the `+` child source unchanged while multiplying the `-` source by `exp(2i phi)`.  Two individually efficient mixed-polarization atoms separated by `pi/2` therefore add in positive `+` work and cancel their minority source exactly.

**OPEN BRIDGE SHARPENING.**  Edgewise CO/CR mixedness cannot be attached to child state without controlling the spin-2 angular order parameter of the actual source law (or routing its cancellation through an existing phase/geometry owner).  This no-go does not affect the global CF pair-action continuation criterion because each event's opposite-helicity recipient work remains real modal state injection.

### CT downstream exp49 constant-sync provenance

Action `31653241490` passed CO/CP, CQ, CR, CS, CT and CU lanes, then exp49 exposed one stale implementation constant: the required `M_eff` had been strengthened using CT's `64/27` capacity, while `upper_at_required` still used the old crude `16`.  The resulting `0.7419` equality residual compared two different formulas rather than testing the theorem.  The referee is synchronized to `64/27`; no theorem hypothesis or constant changed.

## 2026-08-13 — Frontier compression after CV

The current global obstruction is no longer a generic owner graph.  CF requires infinite positive net degree-one radial action at a finite singular time.  Deep/nonlocal pair creation routes to resolved mixed strain or a bounded-ratio core (CQ/CS); sparse ladders are excluded at the record rate (CL/CM); the fixed-critical local core is dense, has a positive efficient actual-work sublaw, and has edgewise nondegenerate mixed fresh polarization (CR/CO/CT); CU forces recent nonlinear amplitude.  CV shows that spin-2 azimuthal organization can nevertheless cancel minority source at the aggregate child state.

**OPEN BRIDGE.**  The remaining theorem is a full-vector source/temporal-ancestry attachment: either the efficient first-shell source survives into a nonaccumulating state consequence, or its spin-2/time cancellation must be routed into a quantitative phase/geometry/reuse action on the same physical work law.  No regularity conclusion is claimed.

## 2026-08-13 — BY–CV final Action certification and failure lineage closure

Final integrated bridge Action `31653630227` completed successfully on exact code/theorem ancestry through CV.  The run passed the corrected Galerkin Hadamard polarization obstruction, orthogonal full-vector polarization, CO/CP fresh-birth polarization, CQ true-upward binding, CR efficient mixed sublaw, CS plateau resolved binding, CT universal capacity, CU fresh-amplitude funding, CV spin-2 cancellation, and the strengthened CL/CM participation referee.

Key final residuals/signals:
- CO child-helicity cross-multiplied ratio residual `3.248e-15`; Stokes residual `1.780e-15`;
- CQ first-radial-moment residual `1.819e-12`, RN/gate violations zero;
- CR average-efficiency and half-action violations zero, nondegeneracy residual `1.665e-16`;
- CS support violations zero, K/S positive-cover residual `4.441e-16`;
- CT universal/envelope violations zero, sampled `eta_pair=0.198041634 < 4sqrt(2)/27=0.209513120`;
- CU old-amplitude residual `1.219e-16`, fresh-amplitude violation `4.441e-16`;
- CV spin-2 rotation residuals `~1e-32`, two-atom cancellation residual `1.059e-16`, positive-work violation zero;
- strengthened CL/CM rate-gate residual `2.243e-16` with sparse participation deficit signal `1.429e3`.

Failure lineage retained rather than erased:
- `31650446519`: referee exposed the incorrect hand-written Heron constant; corrected to the stronger `sqrt(10)/24` with no theorem weakening;
- `31651033582` / `31651133703`: actual Galerkin NSE rejected the static second-generation Hadamard ladder; this produced the exact CN 2D3C/full-polarization theorem instead of a relaxed threshold;
- `31651734164`: exp49 absolute cancellation normalization mismatch; changed to native relative equality residual;
- `31652859240`: direct `F+/F-` ratio became ill-conditioned near the strict-triangle boundary; replaced by equivalent cross-multiplied CO identity;
- `31653241490`: CT-strengthened `M_eff` formula was paired with a stale old capacity constant `16` in exp49; synchronized to `64/27` without changing theorem constants.

**CURRENT OPEN BRIDGE.**  The proof frontier is now the full-vector temporal source/ancestry attachment recorded in `docs/96_final_dense_heterochiral_source_attachment_frontier.md`: infinite positive net degree-one radial action must be exhausted on a recently funded dense first-shell heterochiral work law after resolved/deep routing, while CV shows that spin-2 azimuthal organization can cancel edgewise minority source.  No global-regularity theorem is claimed.

## 2026-08-13 — CW–DB: resolved Wang strain is literal material metric work; Kelvin sees the same tensor with an unresolved correction

**EXACT NSE OPERATOR IDENTITY / EXACT MATERIAL GEOMETRY.**  Re-audited Wang `main` `76e6ee97...` and the read-only resolved-contact theorem branch `9d615568...`; no upstream write occurred.  For the actual resolved linearized operator, `L_V=P(V·grad+grad V)`, the adjoint split is explicitly `K_V=P(V·grad+Omega_V)` and `S_V=P(S_V .)`.  The symmetric bilinear form is exactly `int f.S_V g`, and the resolved material metric satisfies `H_V Mdot_V H_V^T=2S_V`.  Therefore Wang `S` work is literally resolved material metric-velocity work.

**RIGOROUS ROLE-GAUGE CONSEQUENCE.**  On any complete hard-role partition the K matrix is a skew 2-form and the S matrix is a symmetric metric-velocity form; orthogonal role changes act by congruence.  Off-diagonal interface strain is a coordinate reading of the same material tensor, not a new source.

**EXACT KELVIN BRIDGE / OWNER TYPING.**  Re-audited Kelvin `8eb6bb1597...` read-only.  Its reconstructed residual drift uses full `S_u`.  Inserting the actual spectral split `u=V+h` gives exactly `-r.S_V r-r.S_h r+qv`; the `omega.r` cross drift likewise splits through the same bilinear tensor plus signed cross q.v.  Wang and Kelvin therefore share the local symmetric tensor owner, not a scalar bank.

**COUNTEREXAMPLE/NO-GO.**  Vector and Kelvin/covector skew connections are transpose-dual and must not be silently identified.  Exact periodic NSE shears also show `S_V` neither determines nor is determined by full `S_u`; the unresolved strain correction is mandatory.

## 2026-08-13 — DC–DF: cutoff repartition is metric gauge; moving resolution has a typed acceleration face

**EXACT REPARTITION.**  For scalar Fourier resolution `u=V+h`, symmetric strain and skew connection split linearly, and so do the Cartan operators.  Changing cutoff transfers equal and opposite `K/S` tensors between resolved and unresolved sectors; full physical Kelvin metric velocity stays `2S_u`.

**EXACT MOVING-CUT IDENTITY.**  If the multiplier depends on time, instantaneous metric velocity remains `S_V=R S_u`, but differentiation creates `dot R S_u`.  The full resolved objective-strain mismatch has exactly four typed faces: moving-cut time face, transport/filter commutator, unresolved incidence, and nonlinear rotation-filter mismatch.  No norm remainder or cutoff-switch currency is introduced.

## 2026-08-13 — DG–DI: Wang HH has an unresolved Cartan/material reading shared with Kelvin

**EXACT NSE BILINEAR IDENTITY.**  Since `L_h h=2B(h,h)`, signed HH work into any complete event role is exactly half the row sum of unresolved `K_h+S_h`.  Global HH energy conservation becomes simultaneous cancellation of the skew 2-form and the complete-field symmetric self-work.

**EXACT MATERIAL/KELVIN BRIDGE.**  The unresolved symmetric role matrix is the metric-velocity form generated by `h`.  Current Kelvin's unresolved residual-strain correction evaluates the same `S_h` tensor on a different physical probe.  The canonical positive HH cause is not replaced: rolewise `K_h` remains essential, and Kelvin q.v./current-shape state remain distinct.

## 2026-08-13 — DJ–DL: Kelvin dyads expose the same resolved/unresolved Cartan spine

**EXACT KELVIN/ITÔ IDENTITY.**  The reconstructed residual dyad law splits as `-{S,R}+[R,Omega]+Gamma`.  Pure connection acts by orthogonal conjugation and is isospectral; strain changes dyad shape/trace; q.v. is a separate positive source.

**CROSS-PROGRAMME DICTIONARY.**  With `u=V+h`, the Kelvin dyad has exactly resolved/unresolved strain, resolved/unresolved connection, and q.v. faces.  These are the physical-dyad representations corresponding to Wang/repo-3 `S_V,S_h,K_V,K_h`, not identical scalar currencies or state coordinates.

## 2026-08-13 — DM–DP: physical Cartan exterior ladder unifies Wang wavefronts and Kelvin surfaces

**EXACT EXTERIOR/PDE DICTIONARY.**  Specializing the existing exterior representation theorem to incompressible `A=S+Omega` gives `(S+Omega,-S+Omega,0)` on Hodge degrees 1,2,3.  Material area vectors and local affine Fourier wavevectors are the same degree-two representation; vorticity/material lines are degree one.

**EXACT NSE FLUX CONSEQUENCE.**  In the material vorticity-flux pairing, strain and connection cancel separately, leaving only `nu Delta omega` as the local viscous source.  Common strain and common connection are separately neutral on the top interaction form.  This strengthens the structural Wang/Kelvin dictionary without adding a scalar budget.

## 2026-08-13 — DQ–DS: fixed Wang K relink and moving-role connection are projector gauges; Kelvin orientation selector has zero plateau defect

**EXACT PROJECTOR/CARTAN IDENTITY.**  Selected energy for `dot y=(K+S)y` obeys `E_dot=<Py,Sy>+1/2<y,(Pdot-[K,P])y>`.  A fixed hard role displays conservative K flux; a role transported by the same connection absorbs that K flux into observer motion.  This supplies the algebraic bridge Wang deliberately left between fixed-event K and moving-carrier connection without identifying their observables.

**EXACT SELECTOR TYPING.**  Smooth orthogonal projector motion is purely off-diagonal; finite reselection is a finite jump.  Kelvin's orientation-complete `M_fb tensor I_3` commutes with a pure common orientation connection, so on hysteretic intervals with `Mdot_fb=0` it has zero continuous orientation Cartan defect.  Any nonzero continuous first-bad selector face requires an actual germ-mixing/current-state connection and state-map theorem.

## 2026-08-13 — DT–DU: orthogonal observer motion cannot erase the metric-deformation sector

**EXACT FRAME GAUGE / NO-GO.**  Under a rotating orthonormal frame, `S` transforms by orthogonal conjugation while `Omega` acquires the observer angular velocity.  Strain eigenvalues and metric-work pairings are invariant.  Therefore the connection `K` sector can be gauge-transported, but a nonzero `S` owner cannot be converted into conservative relink by common orthogonal observer motion.  This locks the physical distinction used in DQ–DS.

## 2026-08-13 — DV–DY: HH TV is transfer capacity only; pressure is gauge at first order and physical at metric-curvature order

**COUNTEREXAMPLE/NO-GO.**  Read-only audited Wang `resolved-contact-native-binding-tv`: its signed-edge total variation is correctly used as a capacity envelope for canonical HH transfer.  Exact periodic NSE shear has zero `B(h,h)` and hence zero HH work/TV while unresolved `S_h,Omega_h` are active.  TV must not be retyped as Cartan activity.

**EXACT PRESSURE TYPING.**  Leray/divergence-free work, closed Kelvin circulation and curl annihilate `grad p`, but differentiating NSE exposes `-Hess p` in the symmetric strain equation and material metric acceleration.  Exact affine strain and rigid rotation show this Hessian face is physically active.  Pressure is therefore representation/degree typed, not universally a zero owner.

## 2026-08-13 — DZ–EB: Wang spectral viscous killing equals Kelvin q.v. trace, but not its tensor information

**EXACT VISCOUS DICTIONARY.**  At the instantaneous full physical state, Parseval identifies Wang's spectral enstrophy killing with the vorticity Dirichlet form and exactly one half of the orientation-complete Kelvin q.v. trace.  This closes the old "common provenance only" seam at trace/integrated level.

**COUNTEREXAMPLE/NO-GO.**  Exact monochromatic transverse NSE solutions with the same helical modal energies but different relative helicity phase have the same scalar killing and q.v. trace while the Kelvin q.v. tensor changes.  Directional q.v., future covariance and reduced resolution information remain strictly richer/different.

## 2026-08-13 — EC–EE: Wang radial scale motion and Kelvin area motion are conservative phase-space deformation, distinct from fiber strain work

**EXACT LOCAL-AFFINE GEOMETRY.**  A transported wavefront and a material area Hodge vector obey the same `-A^T` law.  Their log-radius rate is `-khat.S.khat`; connection rotates without radial change.  Material lines have the opposite strain sign.

**PHYSICAL TYPING / NO-GO.**  The skew-adjoint transport inside Wang `K_V` can move spectral content across radius while conserving total `L^2`; the self-adjoint `S_V` operator is separate fiber/material metric work.  The same strain tensor appears in both representations, but radial scale progress must not be retyped as energy generation.

## 2026-08-13 — EF–EI: deterministic vorticity curvature and Kelvin q.v. share the exterior-square representation but not the physical input

**EXACT NSE SOURCE ANATOMY.**  `-Omega^2=(1/4)R2(omega omega^T)`, so the strain PDE splits exactly into strain self-action, transverse vorticity geometry, pressure Hessian and viscous diffusion.  Material metric acceleration adds the symmetric trace-free `[S,Omega]` orientation-coupling face.

**CROSS-KELVIN REPRESENTATION / NO-GO.**  Kelvin q.v. enters stochastic geometry through the same `R2` functor applied to `Gamma_K`, but exact affine rotation and periodic shear show deterministic vorticity-amplitude curvature and gradient-q.v. curvature are independent in both directions.  The bridge is representation-theoretic, not a covariance/currency identification.

## 2026-08-13 — EJ–EM: Wang objective `SL(2)` polarization is forced by carrier/top-form incompressibility

**READ-ONLY WANG INPUT / EXACT BRIDGE.**  Current Wang already has the exact affine Kelvin-mode carrier and transverse amplitude equations.  Repo 3 does not duplicate that theorem; it derives the missing material/exterior dictionary.  The transverse strain trace equals the carrier log-radius rate, and `|k| det U_perp exp(2nu int |k|^2)` is exactly constant.

**MATERIAL/SYMPLECTIC CONSEQUENCE.**  Factoring the forced carrier-radius and viscous scalars leaves a determinant-one transverse map generated by the trace-free transverse restriction of material metric velocity.  This gives a geometric origin for Wang's objective `SL(2)`/symplectic polarization calculus.  Exact affine strain is a no-go against applying `SL(2)` directly to the raw transverse amplitude map while carrier radius changes.

## 2026-08-13 — EN–EO: Wang helical geometric phase is the circular-basis reading of material strain holonomy

**EXACT CROSS-PROGRAMME COMMUTATOR.**  The trace-free transverse generator already used by Wang is the trace-free material metric velocity from repo 3.  Its noncommutator is a real `SO(2)` polar-rotation generator; in the circular/helical basis the same matrix is opposite imaginary phase on the two helicities.  The anisotropy-area coefficient is common-frame invariant.

**EXACT NSE CALIBRATION / SCOPE.**  A time-dependent symmetric trace-free affine NSE family realizes nonzero commutator curvature with a fixed transverse carrier.  Its second Magnus term is explicit.  This identifies local holonomy algebra only; higher time-ordering and transfer/recurrence remain separate.

## 2026-08-13 — EP–ES: Wang Gaussian exit and Kelvin finite-shape nonaffinity share the exact same normalized Hessian jet

**READ-ONLY UPSTREAM BRIDGE / EXACT IDENTITY.**  Wang's grain-normalized velocity-curvature tensor `B` and Kelvin's codeforming quadratic jet `J_2(L)` are identical index by index.  Kelvin's leading nonaffinity field is `(1/2)B[xi,xi]`; Wang's first transverse Gaussian shape exit sees only `Sym B` after its tangent-manifold quotient.

**EXACT NS CALIBRATION / NO-GO.**  The quadratic heat shear activates both channels from one physical Hessian jet.  A smooth periodic divergence-free jet has `Sym B=0` but `B!=0`, proving that Wang third-Hermite transverse forcing cannot replace Kelvin total codeforming nonaffinity.  The common object is the full Hessian jet before representation-specific quotienting.

## 2026-08-13 — Core integration: repo 3 re-centered explicitly on strengthening Wang/Kelvin through literal PDE bridges

**PROGRAMME INTEGRATION / NO NEW THEOREM.**  After CW–ES certification, the repository README and core map now state the research center explicitly: actual NSE phenomenon -> physical/PDE type -> exact representation law -> programme-specific quotient -> estimate only when needed.  The current small-law spine is Cartan `K/S`, exterior degree, projector gauge, typed pressure, typed viscosity, phase-space versus fiber strain, objective transverse `SL(2)`/holonomy, and the common non-affine Hessian jet `B=J_2(L)`.  Regularity/proof architecture is recorded only as a possible downstream consequence, not the organizing target of repo 3.

## 2026-08-13 — ET–EX: current Kelvin principal first-bad lineage meets repo-3 projector calculus exactly, with a sharper connection taxonomy

**READ-ONLY KELVIN UPDATE / EXACT BRIDGE.**  Re-audited Kelvin `c6e0d55...`.  Its principal material-metric projectors are exactly connection-comoving in the repo-3 sense: `Pdot=[C_M,P]`, so their Cartan projector defect vanishes.  Kelvin eigenframe mixing is precisely the projector-connection traffic term and sums to off-diagonal metric work.  The literal diagonal first-bad germ selector commutes with the per-germ principal projectors/connections, so it adds no spectral commutator source on hysteretic intervals.

**CONNECTION NO-GO.**  The metric eigenframe connection `C_M` is not the fluid vorticity/Cartan connection `Omega_u`: exact affine pure strain has `Omega_u=0` while a non-aligned finite line metric has `C_M!=0`.  Skew type alone is insufficient for physical identification.

**RESET SCOPE SHARPENING.**  Repo-3's finite projector jump is exact only for a frozen physical state/library.  Current Kelvin physical residual refinement changes the synthesis map itself and therefore requires the full `A tensor A` pair reset (left/right/quadratic faces) plus any metric revaluation.  Positive quadratic reset squares are not standalone costs.

## 2026-08-13 — EY–FA: finite Kelvin current state cannot descend from Wang Eulerian data without physical shape, and `B=J_2` is not enough

**EXACT PERIODIC NSE STATE-MAP NO-GO.**  One-mode shear gives a closed finite-surface residual `4a e^{-nu t}(b-sin b)`.  Same instantaneous Eulerian field, same surface area/orientation, different aspect ratios produce different Kelvin residuals.  Therefore a full Wang-to-Kelvin finite-current state map must carry actual material current/shape state in addition to Eulerian/coherent data and the correct causal clock/history.

**HIGHER-JET NECESSITY.**  At the symmetry anchor the shared quadratic jet `B=J_2(L)` vanishes exactly while the finite Kelvin residual remains nonzero and begins at cubic surface-size order.  The current Kelvin higher-jet/moment tower is therefore physically necessary; repo 3 will not extrapolate Wang higher-Hermite formulas beyond certified upstream theorems merely by pattern matching.

## 2026-08-13 — FB–FD: Wang coherent refinement and Kelvin residual synthesis share one tensor-square pair functor

**READ-ONLY WANG/KELVIN INPUT / EXACT COMMON ALGEBRA.**  Wang coherent localization refines additively at the linear field level, while Kelvin residual state is synthesized linearly before covariance readout.  In both cases the quadratic state is forced by the tensor-square functor, so all cross-pair coherences are physical unless the refinement is genuinely orthogonal.

**STATE-MAP ACCEPTANCE RULE.**  Kelvin's left/right/quadratic reset faces are exactly the finite-difference expansion of this universal pair law.  A future Wang-to-Kelvin linear state lift must therefore descend the full pair state by `J Q J^T` and preserve cross coherence; diagonal child energies or first moments are insufficient.  No common state-space identification is claimed.

## 2026-08-13 — FE–FG: Wang and Kelvin full non-affine fields are the same physical defect modulo affine gauge

**READ-ONLY UPSTREAM DEFINITIONS / EXACT QUOTIENT BRIDGE.**  Wang's normalized velocity and Kelvin's codeforming field satisfy `v_W=c+A_L z+N_L`.  Therefore Wang's Gaussian least-squares remainder and Kelvin's anchor-Taylor remainder differ only by an affine function.  They define the same class modulo affine motions, and every derivative order `p>=2` is exactly the same Kelvin codeforming jet `J_p(L)`.

**EXACT NSE GAUGE NO-GO.**  Periodic one-mode shear shows the full residual fields are not equal: Wang's Gaussian affine slope differs from Kelvin's anchor derivative, while their higher jets coincide.  Higher-jet bridge work should therefore begin from this common affine-quotient field and only then apply programme-specific Hermite/moment projections; no p-by-p equivalence is to be guessed by pattern.

## 2026-08-13 — FH–FI: after exact affine typing, Wang's Gaussian residual is the minimal quotient representative and Kelvin's excess is explicit gauge mismatch

**NORM ONLY AFTER STRUCTURE.**  FE–FG first identify the common physical non-affine class modulo affine motions.  Only then Gaussian orthogonality gives an exact Pythagorean law: Wang's Gaussian residual is the minimal `L^2(rho)` representative over that affine class, while Kelvin's anchor residual norm adds a computable local-vs-Gaussian affine-gauge mismatch.  This residual norm is not Wang's coherent deformation variance `K_C^2=E||grad W-Abar||_F^2`; the latter is a distinct gradient-level observable.  The affine-gauge excess is not retyped as new physical non-affinity.

**EXACT NSE CALIBRATION.**  Periodic one-mode shear realizes a strictly positive gauge excess with identical higher jets.  This provides a safe way to compare Gaussian/Kelvin residual magnitudes without using a norm to invent the underlying bridge.


## 2026-08-13 — post-FH/FI consolidation and latest read-only upstream audit

**RIGOROUS CONSEQUENCE / FRONTIER CORRECTION.**  The old higher-jet seam has collapsed to one exact affine-quotient field law: `[R_W]_/Aff=[N_L]_/Aff` and `D^pR_W=D^pN_L=J_p(L)` for every `p>=2`.  The remaining cross-program state seam is therefore not a missing tower of jet identities.  It is the literal assembly `Eulerian/coherent field + material current/shape + clock/history + linear physical synthesis + persistent full pair/library state`, followed only then by selector/programme-specific readout.

**READ-ONLY WANG AUDIT.**  Upstream `main` advanced from `026b49337083433fbcf9764ab145ca5f7066f4a2` to `3c3ee1ee74c464bdf1c4501aa52b2c853f1fea6c`.  The new pure-UV theorem routes actual true-upward support to the unique first recipient shell `M=2N`; both interaction parents lie strictly outside the `M/4` resolved cutoff so `h=u` on them and no resolved-contact K/S repartition is created.  This is a support/natural-window closure, not a recurrence theorem.  Existing upstream Actions at the latest head are green; no upstream write was made.

**READ-ONLY KELVIN AUDIT.**  Upstream `main` advanced from `c6e0d55d11dfa59762fd983a5ade4a77e3504ed1` to `119b6e3769a45c04a4b0620c837c32f86b7e86c3`.  Frame-aware event synthesis, spectral projector traffic and event gauge normal form are now exact for specified physical events.  More importantly for repo 3, a genuine first-bad selector switch is only a readout `E_g -> E_h` of a persistent candidate library and does not define universal old-selected-to-new-selected transport.  For one stochastic-flow replica, the full residual library q.v. is the common-noise Gram `Gamma_lib=2nu Qcal Qcal^T`, including signed cross-germ blocks, and specified linear events push it by the same congruence `A Gamma_lib A^T`.  The latest Kelvin Action is green; no upstream write was made.


## 2026-08-13 — FJ–FM: selector readout no-go and persistent library pair/Gram functor

**READ-ONLY UPSTREAM DEFINITIONS.**  Kelvin `119b6e3769a45c04a4b0620c837c32f86b7e86c3` separates hysteretic first-bad selector readout from specified physical library events and derives one same-replica residual-library Gram q.v.  Wang `3c3ee1ee74c464bdf1c4501aa52b2c853f1fea6c` retains additive coherent refinement.  No upstream write was made.

**COUNTEREXAMPLE/NO-GO.**  For distinct germs `g!=h`, there is no universal `T` with `E_h=T E_g`; the old selected residual literally does not contain the hidden `h` coordinate.  The same nonclosure persists at pair level: honest PSD full pair states can have the same old selected diagonal block and different new selected block.  A universal cross-program lift that keeps only the active selected residual/diagonal pair block therefore cannot compose through arbitrary genuine selector switches unless an independent Navier--Stokes admissible-state factorization is proved.

**EXACT TENSOR-SQUARE / q.v. FUNCTOR.**  A specified linear event pushes deterministic pair state as `P -> A P A^T` and a one-replica Kelvin q.v. source as `Gamma -> A Gamma A^T`.  The common algebra is the tensor-square functor; the physical owners are different.  Deterministic pair coherence is state, stochastic q.v. is a continuous source.  One common spatial Brownian driver forces all signed cross-germ q.v. blocks and `rank Gamma_lib<=3`.

**EXACT NSE NO-GO.**  Periodic one-mode shear gives two Kelvin packet anchor-noise coefficients `q_2=-q_1!=0`; common-replica synthesis cancels exactly, whereas a counterfactual independent/diagonal per-germ noise model remains strictly positive.  Dropping cross-germ q.v. therefore changes the physical model rather than simplifying the same one.

**OPEN BRIDGE.**  The remaining first-bad state-map question is now literal candidate-library instantiation: actual Navier--Stokes germs, current shapes/frames, replica/clock semantics, physical event maps, support locality and cross-clock ancestry.  Selector logic itself cannot manufacture those dynamics.


## 2026-08-13 — FN–FQ: diagonal marginals enlarge gauge and erase relative synthesis coupling

**EXACT REPRESENTATION IDENTITY.**  For a block Gram `G_ij=B_iB_j^*`, every diagonal is invariant under independent right isometries `B_i -> B_i U_i`, while cross blocks retain the relative alignment `U_i U_j^*`.  One common `U` leaves the full Gram invariant.  Diagonal marginalization therefore has a larger invariance than the physical full-pair construction and loses relative coupling before any estimate is taken.

**WANG SPECIALIZATION.**  Coherent child diagonal pairs are blind to independent child phases, while ordered cross pairs and the synthesized quadratic state retain relative phase.  This is not a declaration that independent phases are a gauge of the full NSE field; it is a no-go for diagonal child data as a complete coherent synthesis state.

**KELVIN SPECIALIZATION.**  In one stochastic-flow replica, one common `O(3)` rotation is Brownian-driver basis gauge.  Independent germwise right rotations leave diagonal q.v. blocks fixed but alter cross-germ Gram blocks and physical synthesis, hence change the coupling/model rather than coordinates.  The earlier exact one-mode NSE shear realizes the negative relative sign with equal diagonal q.v. and exact sum cancellation.

**OPEN BRIDGE / NO-GO.**  A universal Wang--Kelvin quadratic state map cannot be built from diagonal child/germ marginals alone.  Full ordered pair/Gram coupling must be carried, or an independent physical theorem must reconstruct it from other NSE state data.  The Wang relative phase and Kelvin relative driver orientation remain distinctly typed physical information despite the common block-Gram representation law.


## 2026-08-13 — FR–FU: hybrid selected path separates continuous q.v., jump variation and pair reset

**LATEST READ-ONLY KELVIN INPUT.**  Kelvin advanced to `b8caf4862eb11e5661a69d0600b9050e7d1ca929`; upstream Action `31664212015` is green.  Its hybrid selected-residual law is exact conditional on a supplied same-replica library and selector path.  Wang latest is `efb286e6710d9c20cb25a6303d2cb16b3a9e344a` (integration-baseline refresh only).  No upstream write was made.

**EXACT PHYSICAL TYPE SEPARATION.**  On frozen selector intervals, selected continuous q.v. is the selected block of the common-replica Brownian Gram.  A selector-only event is a finite readout jump: its square enters optional càdlàg q.v. but not the continuous bracket.  Endpoint pair revaluation additionally has signed left/right faces, so jump square is not the pair reset itself.

**EXACT NSE NO-GO.**  The half-period one-mode shear gives `chi_1=-chi_0`.  A single selector sign flip has strictly positive jump q.v. but zero selected endpoint dyad change because signed linear faces cancel the quadratic face exactly.  A closed `0->1->0` excursion accumulates positive jump q.v. while returning to the identical selected state.  Selector jump-square is therefore path variation, not a monotone covariance/energy/continuation bank.

**EVENT/SELECTOR COMPOSITION.**  When a physical library map `A` and selector change occur together, the literal post-selected map is `E_+ A`.  Any split into event and selector pieces introduces cross terms in the jump square; adding separate positive costs is invalid absent physical orthogonality.  This sharpens the state-map rule: transport, readout, q.v. and reset are distinct faces even when they occur at one clock time.


## 2026-08-13 — FV–FY: selector jump q.v. has nonzero loop circulation, so history is literal state data

**LATEST READ-ONLY KELVIN INPUT.**  Kelvin advanced to `ad8cd25c8fa0d8aa73bc2f37ec86d8a763820063`.  Commit `ecc31f0` makes the simultaneous packet-selector product rule exact, including the mandatory mixed face `DeltaE DeltaA`; `ad8cd25` separately types signed continuous Brownian source-rate revaluation versus finite state jump optional q.v.  No upstream write was made.  Wang remains `efb286e6710d9c20cb25a6303d2cb16b3a9e344a`.

**EXACT COBOUNDARY / HISTORY NO-GO.**  Endpoint selected pair revaluation telescopes on every path.  Accumulated selector jump q.v. does not: a two-point closed loop has `2(b-a)(b-a)^T>0`.  Therefore jump q.v. is not an endpoint-state potential.  Two supplied hybrid histories can have identical current persistent library, selector and selected residual yet different accumulated selector jump q.v.; current continuous source rate does not recover the missing history.

**EXACT NSE CALIBRATION.**  The half-period one-mode shear gives opposite exact Kelvin residual readouts.  On that frozen exact-NSE payload, the stationary selector history and `0->1->0` end at the same selected state/pair while the loop carries jump-q.v. `8chi_0^2P_z`, trace `128e^{-2nu k^2t}k^4/pi^4`.  This activates the state-map obstruction but does not claim actual first-bad event timing realizes the loop.

**OPEN BRIDGE.**  The `clock/history` seam is now literal: any cross-program state map requiring accumulated selector path variation must carry selector-event history/an equivalent accumulator, unless a separate Navier--Stokes event-timing theorem reconstructs it from endpoint data.  Continuous q.v. production, source-rate revaluation, optional jump q.v. and endpoint pair reset remain four separately typed faces.


## 2026-08-13 — core-spine consolidation after FV–FY and Kelvin `ad8cd25`

**RIGOROUS CONSEQUENCE / FRONTIER CORRECTION.**  The surviving state-map seam is now recorded as `Eulerian/coherent field + material current/shape + selector-event clock/history + linear physical event/synthesis + persistent library with full relative pair/Gram coupling`.  “Full pair” is not merely a list of diagonal child/germ energies: diagonal marginalization enlarges the latent gauge to an artificial blockwise product gauge and deletes relative synthesis coupling.  “History” is not merely a clock label: selector jump optional q.v. has positive closed-loop circulation and is not an endpoint-state coboundary.

**EXACT HYBRID LEDGER.**  For a simultaneous physical library map and selector change, `D=E_+A-E_-=E_-DeltaA+DeltaE+DeltaE DeltaA`; the mixed face is mandatory.  Endpoint pair revaluation, signed continuous-source rate revaluation, finite optional jump q.v. and accumulated selector jump history are separately typed even though all use quadratic pair algebra.  None is promoted to a monotone energy/covariance/continuation bank.

**LATEST READ-ONLY REMOTE TRUTH.**  Wang remains `efb286e6710d9c20cb25a6303d2cb16b3a9e344a`.  Kelvin is `ad8cd25c8fa0d8aa73bc2f37ec86d8a763820063`; Action `31665051054` is green and its combined-event/source-rate tests pass on Python 3.11/3.12.  No upstream write was made.


## 2026-08-13 — FZ–GC: arbitrary adaptive physical events require a fifth mixed map/payload face

**LATEST READ-ONLY KELVIN INPUT.**  Kelvin advanced to `eba4aa953117785194281aff82e3ea5720d20950`; Action `31665366133` is green.  Upstream proves the exact equal-weight two-replica mean-correlation and quadratic four-face laws, with PSD event-map dispersion and signed event-state correlation faces.  Actual adaptive first-bad joint-law instantiation remains Open-literal.  Wang remains `efb286e6710d9c20cb25a6303d2cb16b3a9e344a`; its fixed physical hard event roles remain pathwise exact.  No upstream write was made.

**EXACT GENERALIZATION.**  For a general adaptive physical map/payload law, `E[CQC^T]` has five exact central faces.  The additional term `E[deltaC deltaQ deltaC^T]` is a cubic mixed correlation.  Kelvin's four-face formula is recovered because equal-weight two-replica centering has exact odd parity, not because the fifth face is universally absent.

**COUNTEREXAMPLE/NO-GO.**  Two three-replica scalar ensembles with strictly positive payloads have the same mean face, same event dispersion and zero left/right correlations, but cubic faces `+2/3` and `-2/3`, producing outputs `17/3` and `13/3`.  Thus the cubic face cannot be absorbed into the four upstream faces.  At quadratic order, general adaptive physical synthesis raises the required joint correlation order by one.

**CROSS-PROGRAM CONSEQUENCE.**  Kelvin actual first-bad expectation laws must carry the joint law of realized `C=E_+A` and physical payload once that adaptive law is instantiated.  Wang's present fixed-event hard-role identities are untouched, but any future averaging across state-selected physical event roles likewise cannot replace joint role-map/coherent-pair data by separated marginal means without proving an exact closure domain.


## 2026-08-13 — GD–GG: inherited carrier stock versus selector path variation and simultaneous-owner preservation

**LATEST READ-ONLY WANG INPUT.**  Wang is `c2641bbecb8c12d8a75f0acca83556bbbefd5a9c`.  Exact-head Actions are green, including the independent 100k same-carrier inheritance audit and actual-NS probes.  Upstream types `E_M` as inherited same-carrier stock with generation depth zero, keeps `T_j=E_j W_j+N_j+V_j` and material sidecars as simultaneous owners, and rejects a stock-only quotient when classified residual work is non-negligible.  No upstream write was made.

**LATEST READ-ONLY KELVIN INPUT.**  Kelvin is `9bc8fb01454084861f85e3c7e99683d2dad029e1`; Action `31665852564` is green.  Its first-bad admissibility ledger now explicitly requires passive packet/event gauge invariance, physical support locality, persistent-library memory, full coherence and adaptive event-map/state joint law.  Actual first-bad score, timing, packet library and uniform locality theorem remain Open-literal.

**COUNTEREXAMPLE/NO-GO.**  Wang inherited stock/ancestry and Kelvin selector jump q.v. are different memory types.  The former is a persistent-carrier stock classification; the latter is positive path variation with nonzero closed-loop circulation.  Stationary and closed selector histories can have identical endpoint physical state/stock data and different jump-q.v. accumulators, so no universal stock-to-path bridge exists.

**SIMULTANEOUS-OWNER PRINCIPLE.**  A quotient is only an identity on the physical component it retains.  Wang's stock relay does not delete residual/material owners.  Kelvin's selector/event decomposition does not delete the mixed `DeltaE DeltaA` face or the distinct pair/source/q.v. owners.  Repo-3 must preserve every concurrent owner after typing rather than infer its absence from a quotient on another component.

**OPEN BRIDGE.**  The state-map seam now has at least two noninterchangeable memory coordinates: carrier ancestry/current inherited stock and selector-event path history.  Any future assembly must say which one each quantity belongs to and cannot use a generic positive “bank” as a substitute.


## 2026-08-13 — GH–GK: passive packet gauge, inverse-Gram physical residual, and gauge-safe ranking

**LATEST READ-ONLY KELVIN INPUT.**  Kelvin `9bc8fb01454084861f85e3c7e99683d2dad029e1` makes passive packet/event gauge invariance a necessary first-bad admissibility condition.  Its audited counterexample shows raw packet-coordinate ranking can flip under passive gauge while the physical residual is unchanged.  Support locality, persistent-library memory, full coherence and adaptive joint-law memory remain separately necessary; actual badness/timing remains Open-literal.  No upstream write was made.

**EXACT REPRESENTATION IDENTITY.**  `r=H^{-T}epsilon` is invariant under `(H,epsilon)->(HS,S^T epsilon)`.  The induced packet metric `G_H=H^TH` transforms by congruence and `epsilon^T G_H^{-1}epsilon=|r|^2` is exactly invariant.  Raw `|epsilon|^2` is representation-dependent and can be scaled without changing physical state.

**COUNTEREXAMPLE/NO-GO.**  Raw coefficient ranking can be reversed by a passive basis choice while physical residual ordering stays fixed.  Exact one-mode NSE gives an even sharper calibration: opposite half-period residuals have equal physical energy, yet a passive gauge on one candidate produces a raw coefficient energy ratio `9` with no physical change.

**CROSS-PROGRAM CONSEQUENCE.**  Wang hard roles and Kelvin first-bad selectors are not identified.  The common physicality rule is that event-role/selector logic must factor through the relevant physical equivalence class.  Raw packet coordinates are not bridge state unless the frame and passive-gauge quotient are carried explicitly.


## 2026-08-13 — GL–GO: NSE enstrophy critical current, material-current no-go, and curvature-volume law

**LATEST READ-ONLY INPUTS.**  Wang was refreshed read-only to `ff8259ab5e0a57dfb342b9453f149be95aa3f5d8`; its smooth material-carrier theorem keeps a genuine material carrier continuous between actual interactions and types common affine re-anchoring as gauge composition.  Kelvin was refreshed read-only to `54d8a361a6a3697e919484f24869ff880867b03d`; the exact PDE layers used here are local enstrophy growth `37c635f`, nondegenerate critical speed `c27d1f1`, and critical-Hessian evolution `884956e`, all with green exact-head upstream Actions.  No upstream write was made.

**EXACT NSE/PDE IDENTITY.**  With `e=|omega|^2/2` and `R=omega.S.omega-nu|grad omega|^2+nu Delta e`, a differentiable nondegenerate critical branch obeys `H_e(xdot_*-u)+grad R=0`.  Through the exact Kelvin packet metric dictionary, the viscous face is the orientation-complete q.v. bulk, so the relative current is driven by gradients of stretching, Kelvin q.v. bulk, and curvature diffusion rather than by an observer score.

**COUNTEREXAMPLE/NO-GO.**  Exact periodic ABC has a fixed strict nondegenerate enstrophy maximum at `(pi/4,pi/4,pi/4)` while the local fluid velocity is nonzero.  Hence enstrophy-critical current and material carrier current are not universally the same physical object.  Wang common-slice affine re-anchoring is gauge; this critical/material relative drift is physical.

**EXACT CURVATURE-VOLUME CONSEQUENCE.**  The critical Hessian evolves by growth-landscape curvature + local fluid congruence + relative critical transport.  The congruence contributes exactly `-2 div u` to `d log|det H_e|/dt`, hence zero for incompressible flow, while Hessian shape can still evolve.  The remaining determinant-volume faces are `H_e^{-1} Hess R` and relative transport through `grad H_e`.

**OPEN BRIDGE.**  This does not instantiate the actual first-bad germ.  If future first-bad logic uses a critical-locus candidate, its support/nondegeneracy, branch births/mergers, event clock, persistent library coupling, and relation to Wang genuine-owner recurrence must still be proved.  No recurrence/continuation/global-regularity claim.


## 2026-08-13 — GP–GU: exact NS ranking crossing, 2-jet no-go, and event-clock separation

**LATEST READ-ONLY INPUT.**  Kelvin advanced to `881bf32adbdcb09376e64c4f466ca93a106660b8`, merging `b3c87f7` on enstrophy branch competition; current-head Action `31678459542` is green.  Wang remains read-only at `ff8259ab5e0a57dfb342b9453f149be95aa3f5d8`.  No upstream write was made.

**EXACT NSE/PDE IDENTITY.**  Two critical branch values compete by the exact difference of stretching, Kelvin q.v.-bulk loss, and curvature diffusion.  The exact periodic three-mode shear has a transverse `y=0` versus `y=pi` crossing at `t=1/nu` where both candidates decay and the crossing is driven only by different curvature rates.

**COUNTEREXAMPLE/NO-GO — LOCAL CLOSURE.**  At that exact crossing the two locations have identical local velocity 2-jets (`U`, `U_y`, `U_yy`) and identical local vorticity/first derivative, but different `U_yyy`, hence different enstrophy curvature and branch rates.  A local `p<=2` first-bad ranking state is therefore insufficient even on exact smooth NSE.  This does not reopen the common affine quotient; it identifies a required programme-specific higher-jet readout.

**COUNTEREXAMPLE/NO-GO — EVENT TYPE.**  The crossing shear has `(u.grad)u=0` globally.  A smooth ranking crossing can therefore occur with no Wang hard nonlinear interaction/work event.  The selected scalar max is continuous at the tie while its branch index and derivative switch, so readout reset and physical state jump are also distinct.

**OPEN BRIDGE.**  Raw crossing, branch degeneracy/support exit, physical packet event, hysteretic selector event, and Wang hard interaction have separate clocks/owners.  The actual first-bad badness/resolve functional must say which one triggers selection and how history is used.  No recurrence/continuation/global-regularity claim.


## 2026-08-13 — docs consolidation through GH–GU [skip-ci target]

The integrated bridge spine is synchronized through the Action-certified passive packet quotient (GH–GK), enstrophy critical-current/material-current separation and critical-curvature-volume law (GL–GO), and exact branch-ranking/event-typing no-gos (GP–GU).  The literal state target now keeps packet/frame data only modulo passive gauge; distinguishes material current from any critical-locus current/geometry used by first-bad logic; records the actual programme-specific jet order demanded by the PDE (the exact crossing shear needs the third velocity jet although the common affine quotient is already closed for every `p>=2`); and keeps ranking crossing, critical-geometry events, selector/readout events, physical packet events, and Wang hard nonlinear-work events as separate clocks/types unless an independent NSE theorem identifies them.  This is documentation consolidation only and adds no recurrence/continuation/global-regularity claim.


## 2026-08-13 — GV–HA: own-local affine target coboundary and arbitrary finite ranking-crossing no-go

**LATEST READ-ONLY INPUTS.**  Wang remains `ff8259ab5e0a57dfb342b9453f149be95aa3f5d8`.  Kelvin advanced to `3397d3153d55ec460ac857a9a8d40a172c82779a`; its own-local Kelvin event interface is affine and exact-head Action `31679953296` is green.  No upstream write was made.

**EXACT REPRESENTATION LAW.**  Own-local residual events are `x_+=Ax_-+d`, `d=A Omega_- - Omega_+`; the offset is a compositional coboundary.  Simultaneous selector readout is `DeltaY=(E_+A-E_-)X+E_+d`, so affine target cross faces survive in pair/q.v. bookkeeping.

**COUNTEREXAMPLE/NO-GO — REANCHORING TYPE.**  Wang common carrier reanchoring is passive chart gauge.  Kelvin target reanchoring can change residual/q.v. source even with `A=I`.  Exact cubic heat shear gives `Q_a=0` at the packet's own target and `Q_0=-12ab ell` after target reanchor, while nonlinear advection remains zero.  Same composition law does not imply same physical quotient.

**EXACT NSE/PDE IDENTITY — MANY CROSSINGS.**  For arbitrary finite prescribed times, an odd-mode exponential Chebyshev interpolation supplies `O(t_i)=0`, `O'(t_i)!=0`.  Adding one even heat mode gives an exact periodic shear with `Delta e=2 epsilon E O` between `y=0,pi`, zero nonlinear advection, and—after small odd-sector scaling—strict negative transverse enstrophy curvature on both sheets at every crossing.

**COUNTEREXAMPLE/NO-GO — GENERATION COUNT.**  Ranking/selector crossing count can therefore be made arbitrarily large at finite prescribed times while hard nonlinear interaction remains absent.  A pure selector reset on fixed library/target may change readout with no physical library event.  Selector/ranking count and target q.v. revaluation are not universal Wang hard-generation-depth currencies and may not create extra recurrence vertices by observer fiat.

**OPEN BRIDGE.**  This does not prove selector Zeno/local finiteness, does not identify the actual first-bad score, and does not close Wang sidecar-bearing mixed genuine-owner recurrence or any assembly/termination theorem.  No recurrence/continuation/global-regularity claim.


## 2026-08-13 — docs consolidation through GV–HA and Wang material-sidecar theorem [skip-ci target]

The bridge spine now uses Kelvin's latest own-local **affine** event interface `(A,d)` rather than treating every residual event as purely linear.  The target coboundary composes exactly but is not Wang passive carrier-chart gauge; its target-gradient face may revalue q.v. even with `A=I`.  Repo-3's arbitrary-finite heat-shear construction proves that ranking/readout crossings can be prescribed in any finite number while nonlinear advection vanishes identically, so event count cannot be promoted to hard-generation depth.  Read-only Wang at `94cd83726123814ef7abc19ffa82c9c62a446698` independently closes the sidecar representation layer: material-membership rereading is zero-charge provenance and selected-family Moyal `R_switch` may be positive on an identical coherent state yet has zero generation depth.  Moyal boundary energy, Kelvin selector jump variation, and Kelvin target q.v. revaluation remain different currencies with the same guardrail: none may create a physical recurrence owner without independently witnessed NSE service/work.  Wang central/joint-stop sidecar integration, Kelvin actual badness/resolve/target generation and local-finiteness calculus, and any cross-program assembly/termination theorem remain open.  No recurrence/continuation/global-regularity claim.


## 2026-08-13 — HB–HE: selector path q.v. growth and zero-depth owner-kernel condition

**READ-ONLY TRUTH.** Wang `94cd83726123814ef7abc19ffa82c9c62a446698` now proves that selected-family Moyal `R_switch` may be positive on an identical coherent state while all cell increments/work vanish, so that boundary charge itself has zero generation depth. Kelvin remains `3397d3153d55ec460ac857a9a8d40a172c82779a` with affine own-local event typing and persistent-library selector semantics. No upstream write was made.

**RIGOROUS CONSEQUENCE FROM EXACT NSE.** The arbitrary-finite heat-shear crossing theorem has exactly `N` simple ranking roots. A one-hot winner selector therefore toggles exactly `N` times and carries exact optional label jump-q.v. trace `2N`. For even `N` the selector returns to its initial label while the path variation remains positive. The selected scalar maximum is continuous at every switch.

**COUNTEREXAMPLE/NO-GO.** Since `N` is arbitrary finite and `(u.grad)u=0` identically for the exact shear family, selector count/jump q.v./label variation can be arbitrarily large while no nonlinear hard interaction occurs. Wang independently supplies a positive same-state Moyal boundary charge with zero generation depth. The currencies are not identified; the shared guardrail is that positive selection/boundary activity does not manufacture physical nonlinear generation.

**OPEN BRIDGE / OWNER KERNEL.** Any hard-generation increment rule must annihilate the demonstrated pure selector, same-state Moyal-boundary, and zero-nonlinearity target-reanchor directions unless independently witnessed physical service/work is simultaneously present. This is a necessary kernel condition, not a completed owner quotient or recurrence assembly theorem. No Zeno/continuation/termination/global-regularity claim.


## 2026-08-13 — HF–HJ: critical-lineage persistence and exact event-clock separation

**RIGOROUS LOCAL GEOMETRY.**  If `grad e=0` and the enstrophy Hessian is invertible, the implicit-function theorem gives a unique local critical lineage and the exact previously derived NSE critical-current speed.  Hessian inertia is constant on every connected nondegenerate lineage interval.  For translation-symmetric shears the correct condition is normal nondegeneracy `e_yy!=0`, not the full Hessian which contains symmetry tangent zero modes.

**EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO.**  Strengthening the arbitrary-finite crossing construction, fix one compact interval around all prescribed times and choose the odd-sector amplitude so `epsilon max|O|<min E` and `epsilon max|O_2|<4 min E`.  Then both fixed critical sheets are strict normal enstrophy maxima on the whole interval, all `N` transverse ranking crossings remain, and `(u.grad)u=0` identically.  Thus ranking clock can have arbitrary finite activity while the tracked normal-geometry clock has zero degeneracy events and the nonlinear-owner clock is absent.

**OPEN BRIDGE.**  Actual Kelvin hysteresis is a fourth rule clock.  A first-bad state using critical candidates must retain its Hessian/normal-lineage theorem domain, support chart, ranking/selector state, and physical owner events separately.  Local IFT persistence is not a Navier--Stokes continuation theorem; global branch bifurcation/support exit, Wang owner assembly, Zeno/local finiteness and termination remain open.  No global-regularity claim.


## 2026-08-13 — docs consolidation through HF–HJ and Kelvin exact critical-sheet merger [skip-ci target]

**ACTION-CERTIFIED CORE.**  Repo-3 theorem SHA `2203b7f73ba3673b39fb2ee27aaa001c27389763`, Action `31682239600`, closes local critical-lineage IFT/Morse rigidity and the compact exact-NS clock-separation theorem.  The arbitrary-finite heat-shear family now supplies two exact readout laws simultaneously: a right-continuous one-hot winner carries `tr J_Y=2N`, while for sufficiently small odd-sector amplitude both tracked sheets remain strict normal maxima on the entire compact crossing interval and nonlinear advection vanishes identically.  Thus winner/readout, lineage theorem domain, and physical owner are separately typed axes.  The hard-generation assembly must annihilate demonstrated pure selector/target/Moyal-sidecar directions unless independently witnessed physical owners are present; this is a necessary kernel condition, not a completed owner quotient.

**LATEST READ-ONLY KELVIN.**  Kelvin advanced to `d0c5863dae226600e1344626aa27f3ecc18df72d`; exact-head Action `31682402804` succeeded.  Its exact analytic two-mode heat shear instantiates a critical-sheet merger.  For one specified translation-covariant fixed-shape packet per critical sheet, full instantaneous packet state coalesces, the branch-resolved physical library event is central extraction `A=E_0`, the own-local affine and target-gradient coboundaries vanish (`d=0`, `N_target=0`) for exact collision/criticality reasons, nonzero same-replica cross-label q.v. blocks are required for the collision quotient, and a branch-label selector can jump with zero selected physical packet jump.  The side packet branch rate has a singular critical-coordinate face although the NS field remains analytic.  The same upstream theorem proves the no-go that scalar/critical coalescence alone does not force full packet-state coalescence for different admissible shapes, and instantaneous state equality does not identify branch ancestry.  Actual first-bad badness/resolve and general endogenous selector local finiteness remain Open-literal.

**LATEST READ-ONLY WANG.**  Wang remains `94cd83726123814ef7abc19ffa82c9c62a446698`; selected-family Moyal `R_switch` is a typed zero-generation-depth boundary currency on same-state rereading, while genuine material/source recurrence still requires independent physical service/source evidence.  Central/joint-stop integration and mixed genuine-owner ancestry remain open.

No upstream write was made.  No Zeno exclusion, recurrence assembly, continuation, restart, termination, or global-regularity theorem is claimed.

## 2026-08-13 — HK–HR: relative-boundary transport law, swept-ribbon Kelvin currency, and transport-ancestry obstruction

- Derived the exact moving-balance identity `d int_D f = int_D s + int_boundary J.n + int_boundary f(V-u).n`; selector/boundary motion enters only through velocity relative to the material.
- Specialized it to the exact Navier--Stokes enstrophy four-face law: stretching, bulk viscous loss, diffusive boundary flux, and relative sweep.
- Derived the arbitrary-moving-loop Kelvin law `dot Gamma = nu*oint Delta u.dx - oint((v-u)xomega).dx`, equivalently vorticity flux through the swept ribbon.
- Bound the new sweep face to the existing critical-current law `dot x_*-u=-H_e^{-1}grad R`; absolute selector speed is not the intrinsic currency.
- On Kelvin's exact two-mode heat-shear merger, identified the `1/d` critical packet cusp as a singular but continuous relative-boundary transfer with zero nonlinear advection and zero enstrophy stretching.
- Imported read-only Kelvin head `4888b6e19293edc0950047fd2e52ad6b64fbe3ac`: Nanson transport retains a nontrivial merger history holonomy even when endpoint current/residual fiber coalesces.
- Imported read-only Wang head `24a725798948d7067afae1976afb9c712fb23b47`: central/joint routing now enforces physical-stop first, typed material/Moyal sidecar second, while preserving genuine independently witnessed material service.
- New necessary assembly rule: moving-boundary transfer remains a real transfer ledger but carries zero hard-generation depth unless an independent source/work owner is present.
- Action stress test `experiments/exp93_relative_boundary_transport_owner_law.py` certified on run `31685600783` at theorem SHA `f3ca29119ceab9cb0a56b36e6df1ea5c0771803b`: moving-loop residual `2.696e-16`, moving-slab four-face residual `7.720e-16`, tangential-kernel residual `5.572e-16`, endpoint residual-fiber tie `0`, nonzero frame-history separation `5.529615`, holonomy determinant residual `1.110e-16`; PASS.
- No upstream writes. No Zeno, recurrence, restart, continuation, termination, or global-regularity claim.

## 2026-08-13 — HS–HZ: enstrophy record owner clock and first-hit stretching funnel

**READ-ONLY INPUTS.** Wang remains `24a725798948d7067afae1976afb9c712fb23b47`; Kelvin remains `4888b6e19293edc0950047fd2e52ad6b64fbe3ac`.  No upstream write was made.

**EXACT NSE/PDE IDENTITY.** For `M(t)=max_x |omega|^2/2`, the right derivative is the maximum over the active maximizing set of the literal local enstrophy rate.  Since `grad e=0` and `Delta e<=0` there, critical-selector motion is annihilated from the value rate and positive record growth requires `omega.S.omega > nu(|grad omega|^2-Delta e) >= nu|grad omega|^2` at an active maximizer.

**RIGOROUS CONSEQUENCE.** The running record `R(t)=max_{s<=t}M(s)` is a canonical monotone owner clock.  It increments only on actual record states with positive stretching-dominant local owner rate; ranking/selector loops, subrecord sweep, gauge/target changes, Moyal boundaries and inherited stock do not increment it by themselves.  Any smooth finite first hit of a higher level has a sequence of stretching-owned record states approaching the hit from below, without a transversality assumption.

**EXACT CALIBRATIONS.** Periodic one-mode heat shear has zero stretching and strictly decaying record through curvature diffusion.  Exact Euclidean affine strain-spin NSE has zero viscous defect and strictly growing enstrophy record owned purely by extensional vortex stretching, with an explicit first-hit time.

**OPEN BRIDGE.** `log R` gives a necessary accumulated effective-stretching measure for any hypothetical unbounded record, but no bound on that measure is proved.  The next seam is whether NSE geometry/transport/ancestry forces depletion, cancellation, donor exhaustion or owner reuse on record-growth states.  No recurrence/restart/continuation/termination/global-regularity claim.

### HS–HZ Action certification

Theorem SHA `455dd2d70b3a39858789a17044af5a14cf2fa0c2` is certified by bridge Action `31686689214` (**completed/success**).  Exact exp94 outputs: heat-shear PDE residual `1.235e-16`; active-record owner residual `1.004e-16`; largest heat-shear record rate `-5.318182e-03`; affine NSE matrix residual `7.081e-17`; pure-stretching owner residual `0`; affine minimum positive owner margin `1.207224`; first-hit and first-hit-stretching residuals `0`; exact ranking tie residual `0` with both candidates decaying (largest rate `-6.008887e-01`) while the ranking gap crosses; seven selector switches below the old record produce exactly zero record increment.  PASS.

## 2026-08-13 — IA–IH: stretching-owner self-constraint and pressure-curvature regulation

**EXACT NSE/PDE IDENTITY.**  Differentiated NSE gives the exact strain equation `D_tS=-S^2-Omega^2-Hess p+nu Delta S`, vorticity equation `D_t omega=S omega+nu Delta omega`, and pressure Poisson law `-Delta p=|S|^2-|omega|^2/2`.  Therefore `P=omega.S.omega` obeys `D_tP=omega.S^2.omega-omega.Hess(p).omega+V_P` with an explicit viscous composite face.

**INTRINSIC GLOBAL CONSTRAINT.**  On the torus `Hess p=R_iR_j(|S|^2-|omega|^2/2)`: a pointwise stretching owner is constrained by the whole incompressible field.  The scalar pressure trace does not by itself supply the directional contraction used by the owner law.

**EXACT SIGN CALIBRATIONS TO BE ACTION-CERTIFIED.**  Constant-strain affine NSE has positive pressure curvature equal to the positive strain-square face.  Viscous periodic ABC at `(pi/2,0,0)` has `P=0`, `Q_S=1`, pressure face `-5`, hence material owner derivative `-4`; pressure can overpower self-strain.  These examples type pressure as a signed regulator, not a universal sink/source.

**OPEN BRIDGE.**  Record generation and stretching-owner persistence are now separate nested gates.  The next question is whether pressure/strain geometry plus material/donor ancestry constrains repeated fresh owner renewal.  No recurrence/termination/continuation/global-regularity claim.

### IA–IH Action certification

Theorem SHA `e76af8ef68dac706713e3897a4bbeef7e28e8357` is certified by bridge Action `31687505801` (**completed/success**).  Exp95 gives affine owner-law residual `0`, exact equality of self-strain and positive pressure-curvature faces (`0` residual), ABC full owner-law residual `1.831e-16`, inviscid-core residual `1.244e-16`, viscous-face residual `0`, pressure-Poisson trace residual `2.187e-16`.  At the exact ABC suppression point, `P≈2.45e-16`, `Q_S=1`, `C_p=-5`, and material owner derivative `-4`; pressure trace is `2` while the vorticity-direction contraction is `5`.  At the ABC origin, `P=Q_S=3`, pressure face `0`, advective owner derivative `3`.  PASS.

## 2026-08-13 — II–IQ: endogenous enstrophy moving readout and local-to-global owner layer cake

**NEW READ-ONLY KELVIN INPUT.**  Kelvin advanced during the previous Action to `2227e1a9d3fbe48de591cfee2d4d09fe09b4f1bf` (Action `31686276216`, success).  It composes physical Kelvin ancestry through a conditional lift into a supplied Eulerian moving localization, with exact intrinsic/resolution/localization covariance layers and signed Reynolds boundary revaluation; it explicitly leaves the programme-specific first-bad localization Open-literal.  No upstream write was made.

**EXACT NSE LEVEL-SET LAW.**  For a regular enstrophy superlevel boundary `e=lambda(t)`, the outward relative speed is `(V-u).n=(R-dot lambda)/|grad e|`.  Consequently superlevel volume changes by the boundary integral of that owner mismatch, and the selected enstrophy has stretching, bulk viscosity, diffusive boundary flux, and signed moving-threshold revaluation as distinct faces.

**LOCAL-TO-GLOBAL BRIDGE.**  Fixed-level coarea gives `int_0^infty int_(e=lambda) R/|grad e| = int R = d/dt int e`.  Combining with certified BR--BT yields the exact all-level identity `level-set owner flux = V_split - V_merge - nu Z`.  This is an integrated bridge only; no individual spectral atom is assigned to one level set.

**KELVIN COMPOSITION.**  For an ancestry density satisfying `partial_t rho+div J_rho=0` on a compatible observation clock, the signed selected-mass gain is `(rho V-J_rho).n = rho(R-dot lambda)/|grad e| + (rho u-J_rho).n`.  The first face is NSE level-set sweep; the second is intrinsic ancestry/Fokker--Planck current mismatch and must not be discarded.  In deterministic material transport, and in Kelvin's exact uniform two-mode shear normal marginal, the second face vanishes and the calibrated flux reduces to `rho(R-dot lambda)/|grad e|`.  No extra selector covariance source is introduced.

**OPEN BRIDGE.**  The actual first-bad level rule, critical-level topology changes, and a levelwise spectral/donor localization remain unproved.  No recurrence/restart/continuation/termination/global-regularity claim.

### II–IQ Action certification

The executable batch at corrected referee SHA `cbdea2b9bcaac0784657df75cf332dbf66684bf1` is certified by bridge Action `31688661368` (**completed/success**).  Exp96 gives fixed-level boundary-speed owner residual `1.059e-16`, chamber-volume flux residual `1.391e-16`, minimum regular level-gradient signal `7.068981`, co-decaying fractional-level residual `1.055e-16`, global layer-rate versus viscous owner residual `1.264e-16`, and regularized direct coarea quadrature residual `0`.  PASS.  The coarea stress uses the exact regularizing change `lambda=M sin^2(theta)` rather than sampling the integrable endpoint singularity directly.

## 2026-08-13 — IR–IZ: enstrophy value-space continuity and support-edge selection

**EXACT NSE/PDE IDENTITY.**  Push physical volume through `e=|omega|^2/2`.  The resulting measure `mu_t=e_#dx` and signed owner current `j=e_#(R dx)` satisfy `partial_t mu+partial_a j=0` exactly; incompressible advection disappears from every test function of the value.  At regular levels this is `partial_t g+partial_a J=0` with the II--IQ level-set flux `J`.

**VALUE CURRENT FACES.**  `J=J_P-nu B_omega+nu partial_a K_e`, where `J_P` is stretching, `B_omega` is vorticity-gradient loss, and `K_e=int_(e=a)|grad e|` is the curvature geometry.  Every `C^2` observable `Phi(e)` obeys the corresponding exact weighted owner identity; increasing convex `Phi` has two nonpositive viscous faces.

**SUPPORT EDGE.**  A unique nondegenerate maximum is the characteristic endpoint of the same current: `J/g -> R_* = M'`.  At a tie, however, bulk near-edge current takes a curvature-volume weighted average of branch owners while Danskin record motion takes their maximum.  The exact three-mode shear gives `c_bulk=-12 sqrt(5) nu e^-2`, `D_+M=-12nu e^-2`, and left winner rate `-60nu e^-2`.

**OPEN BRIDGE.**  The value-space law compresses interior level complexity but does not remove lineage at a tied support edge.  Repeated support-edge owner renewal under pressure/strain/viscosity and material/donor ancestry remains open.  No recurrence/termination/continuation/global-regularity claim.

### IR–IZ Action certification and referee correction

Initial Action `31689422082` failed only because the continuity referee compared the absolute cancellation `g_t+J_a` to zero; it reported `3.638e-12` while every other value-current and tied-edge signal already passed, including the exact-shear edge asymptotic residual `8.859e-10`.  No theorem formula was changed.  The referee was corrected to the scale-aware comparison `rel(g_t,-J_a)` in SHA `e5fd950d9841a757556fa59e89879460fa5020e0`.

Corrected bridge Action `31689876267` is **completed/success**.  Exp97 outputs: value-space continuity residual `2.038e-16`; value-current decomposition `2.966e-15`; conditional owner velocity `8.561e-17`; survival/current `1.081e-15`; convex power-moment hierarchy `3.350e-16`; tied-edge closed-form residual `6.022e-17`; bulk edge velocity `-1.343627885`; record right/left velocities `-0.6008886576 / -3.004443288`; bulk-record separation `0.7427392`; exact-shear near-edge asymptotic residual `8.859e-10`.  PASS.

## 2026-08-13 — post-IR/IZ read-only upstream convergence

**KELVIN.**  Upstream advanced to `5067f87b5a921d3f260433ec4f3ee1ce0df81f2c` (Action `31688392611`, success) with an intrinsic max-normalized enstrophy localization grammar.  Its filtration `g=e/M`, `Omega_theta={g>=theta}` is similarity-invariant and needs no absolute magnitude threshold.  On a regular boundary its exact compatibility defect is `C_theta=R-theta Mdot`, with `(V-u).n=C_theta/|grad e|`.  This is exactly the `lambda(t)=theta M(t)` specialization of repo-3 II--IQ.  Kelvin further preserves two ancestry-boundary faces, `rho(u-c).n + rho C_theta/|grad e|`, matching repo-3's warning not to erase intrinsic ancestry/Fokker--Planck current.  The upstream still leaves identification with actual first-bad localization, badness/resolve, packet support, two-clock closure, restart and continuation open.

**WANG.**  Upstream advanced to `7b9182854d956b2514d994ac35f4f75adef3815e`; exact theorem/fix `d6ee03d5b9b7a82d11a2259c5dc0b8ae2ac945ab` is certified by dedicated/audit/integration Actions.  Raw `material_relink` / `new_coherent_ancestry` labels are now fail-closed pre-owner locators: a material address does not create service or recursion.  Certified smooth `K_phys` relink is antisymmetric same-event subset flux, not source; OO/ON/NN material readings only repartition an already-existing positive service law.  A genuine physical supplier must be independently certified before owner admission.

**CONVERGENCE.**  The independent programmes now reinforce one common order without identifying their currencies: physical PDE owner/current first; intrinsic geometry/localization/material address second; signed boundary/ancestry/readout revaluation after that.  No upstream write was made.

## 2026-08-13 — JA–JI: support-edge compatibility and intrinsic owner-renewal Riccati grammar

**LATEST READ-ONLY INPUTS.**  Kelvin `5067f87b5a921d3f260433ec4f3ee1ce0df81f2c` supplies the max-normalized enstrophy filtration and compatibility defect; Wang `63178b0e7f9fabdfd8c344dab938a3d639639df5` fail-closes raw material-address labels unless native physical service is certified.  No upstream write was made.

**EXACT SUPPORT-EDGE LAW.**  At the active max set, `R=partial_t e`; therefore the active-set extension of the `theta->1` compatibility numerator relative to `D^+M` is nonpositive and vanishes exactly on right-winning active branches (with the left analogue relative to `D^-M`).  Kelvin's exact four-mode periodic global-max crossing gives right defects `(0,-96nu)` and left defects `(96nu,0)` with zero stretching/nonlinear advection.

**EXACT INTRINSIC OWNER CLOCK.**  With `d tau=sqrt(M)dt`, `sigma=P/(2M^(3/2))`, `delta=nu(|grad omega|^2-Delta e)/M^(3/2)`, the record obeys `d_tau log M=2sigma-delta`.  On a unique nondegenerate maximizing lineage, specific stretching `alpha=xi.S.xi` yields the scale-free Riccati identity `d_tau sigma=-sigma^2+N_renew`, where `N_renew` is the exact transverse-strain + signed pressure-curvature + viscous + critical-relative-transport excess after support-growth dilution.

**RIGOROUS CONSEQUENCE.**  If `N_renew<=0` eventually while the unique nondegenerate record branch persists, `sigma<=sigma0/(1+sigma0 Delta tau)` and `M<=M0(1+sigma0 Delta tau)^2`; `dt/dtau=M^-1/2` then forces infinite physical time to reach infinite `M`.  Hence any hypothetical finite-time unbounded record must have positive renewal excess arbitrarily late or repeatedly exit the support-edge theorem domain.  This is a conditional finite-time exclusion/reduction, not global regularity.

**EXACT CALIBRATION.**  Constant-strain affine strain-spin has `N_renew=0` and exactly saturates the Riccati/quadratic intrinsic-time bound while growing only at infinite physical time.  Accelerating affine strain-spin `a=1/[2(T-t)]`, `Omega=b/(T-t)` has `N_renew=sigma^2>0` and finite-time amplitude blow-up; it is nonperiodic/infinite-energy and used only as an exact Euclidean calibration.

**OPEN BRIDGE.**  The next seam is no longer generic event counting.  It is to decompose/bound positive renewal excess by native finite-capacity owners or prove that repeated support-edge theorem-domain exits cannot remain admissible under full Kelvin/Nanson ancestry and Wang native-service causality.  No restart/continuation/global-regularity claim.

**JA–JI ACTION CERTIFICATE.**  GitHub Actions `31707632509` on theorem SHA `51033a4f1d7a0918fe8cf157182b6e179e5d2d90` completed successfully.  Exp98: global-max and support-defect residuals `0`; constant-affine Riccati `1.202e-17`, zero-renewal `5.512e-17`, exact quadratic-bound saturation `1.722e-16`; accelerating-affine NSE symmetry `1.479e-16`, positive-renewal `1.860e-16`, Riccati `5.551e-16`, `M(T-t)^2` `1.472e-16`; PASS.  No continuation/global-regularity claim.

## 2026-08-13 — JJ–JS: running-record renewal gauge

**EXACT PDE STRUCTURE.** The monotone enstrophy running record gives a Riccati efficiency law whose renewal term splits into local core, geometry harvesting, and record normalization. The normalization face is never positive.

**RIGOROUS CONSEQUENCE.** Eventual nonpositive total renewal on one persistent nondegenerate maximizing branch forces a quadratic record bound in intrinsic time and rules out finite-physical-time record divergence on that branch, including through subrecord excursions.

**OPEN BRIDGE.** A hypothetical finite-endpoint unbounded record must use positive local core renewal, positive geometry harvesting, or support-edge theorem-domain exit arbitrarily late. No termination or global-regularity claim.
