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
