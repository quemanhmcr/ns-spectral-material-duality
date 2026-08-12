# Literal localization owner calculus: covariant vorticity roles, hard-event work, and moving-current faces

Status: **PDE-first audit at exact-identity / rigorous-consequence level.**  This note uses the literal localization objects present at upstream HEADs

- `wang-ns-triad-diamond` @ `f56517caba641ccc109987c5eee4564b9fe66a55`,
- `ns-pde-first-kelvin-frontier` @ `517ced374ac2b48ebac9d7170bc5bb4151bd9437`,

and compares them only after re-deriving the relevant Navier--Stokes/current identities.  No recurrence termination or regularity claim is made.

The central rule is that an operator is not classified by its syntax (`Q`, projector, mask, cutoff) but by the physical space and clock on which it acts.

---

## 1. Exact NSE localization owner identity

Write the vorticity equation as

\[
\partial_t\omega+\mathcal K_u\omega=\nu\Delta\omega,
\qquad
\mathcal K_u:=u\cdot\nabla-\nabla u.
\]

Let the physical material area frame satisfy

\[
D_tH=-(\nabla u)^TH,
\qquad D_t=\partial_t+u\cdot\nabla,
\]

and let `Q(t)` be a sufficiently regular linear spatial role operator.  The localized material flux is

\[
\Phi_Q=H^TQ\omega.
\]

The previously separated interface and selection--strain terms combine exactly as

\[
\boxed{
\partial_tQ+[u\cdot\nabla,Q]+[Q,\nabla u]
=
\partial_tQ+[\mathcal K_u,Q].
}
\]

Therefore

\[
\boxed{
D_t\Phi_Q
=H^T\Big[
\underbrace{\big(\partial_tQ+[\mathcal K_u,Q]\big)\omega}_{\mathcal C_Q\omega}
+\nu Q\Delta\omega
\Big].
}
\]

This is only a regrouping of the exact Navier--Stokes identity; no term has been estimated or removed.

**Classification: EXACT NSE/PDE IDENTITY.**

The operator

\[
\boxed{\mathcal C_Q:=\partial_tQ+[\mathcal K_u,Q]}
\]

is the exact covariant localization defect for vorticity roles.  It is the object that changes a materialized localized role before viscosity is applied.

---

## 2. Quotient common motion before assigning an owner

Let `G(t)` be any common generator used to transport the analysis role and suppose

\[
\boxed{\partial_tQ+[G,Q]=0.}
\]

Then

\[
\boxed{
\mathcal C_Q=[\mathcal K_u-G,Q].
}
\]

Thus common observer/material motion does not enter the interaction-changing ledger.  Only the **relative generator** `K_u-G` survives.

This is the operator version of the exterior-power theorem in `docs/10_exterior_algebra_spine.md`: common trace-free deformation preserves the oriented wedge/volume, while relative incidence changes it.

**Classification: EXACT NSE/PDE IDENTITY.**

A large common strain norm is therefore not, by itself, a localization payment.

---

## 3. Literal Wang operators: hard event role and smooth PDE envelope are different types

The literal hard event role in `wang-ns-triad-diamond/docs/event_anchored_role_registration.md` is

\[
\boxed{P_{a\sigma}=1_{C_a}(D)H_\sigma(D).}
\]

It is an orthogonal Fourier/helical projector used at a physical transfer event.  The literal propagated PDE role is instead a real scalar smooth Fourier multiplier `Q(t,D)` satisfying

\[
\boxed{QP=P}
\]

on the event plateau, with lower radial envelope `11N/20`.  The upstream theorem explicitly says: **do not differentiate the hard event boundary**.

Accordingly:

- `P` owns exact event identity, signed HH work, helicity role, and orthogonal energy accounting;
- `Q` owns only the smooth between-slice PDE carrier;
- overlap of `Q` is not a second physical transfer measure.

**Classification: EXACT TYPE DISTINCTION.**

A useful no-go follows immediately.  Although `P(Q\omega)=P\omega` on the plateau, in general

\[
\mathcal Z(Q_1\omega,Q_2\omega,Q_3\omega)
\ne
\mathcal Z(P_1\omega,P_2\omega,P_3\omega),
\]

because the smooth envelopes contain additional overlap components.  The hard projection must still be applied to recover the actual event edge.

Therefore a phase/work trichotomy for the smooth carrier cubic cannot silently be renamed a theorem about persistent hard-cell physical work between events.

**Classification: COUNTEREXAMPLE/NO-GO (type/observable mismatch).**

---

## 4. Wang specialization of the exact covariant defect

The literal resolved field is

\[
V=S_{N/4}u,
\qquad h=u-V.
\]

Let the coherent averaged affine jet used to transport the smooth role be

\[
\bar V_{\rm aff}(x,t)=b(t)+\bar A(t)(x-X(t)),
\]

and define its vorticity transport/stretch generator

\[
G_{\rm aff}:=\bar V_{\rm aff}\cdot\nabla-\bar A.
\]

The upstream symbol law is

\[
\partial_tm-(\bar A^T\xi)\cdot\nabla_\xi m=0.
\]

For a scalar Fourier multiplier, constant matrix stretching commutes with `Q`, so this is exactly

\[
\partial_tQ+[G_{\rm aff},Q]=0.
\]

Write the non-affine resolved remainder

\[
r:=V-\bar V_{\rm aff}.
\]

Before recombining the source, the two pieces requested by the localized material-flux law are individually

\[
\boxed{
\partial_tQ+[u\cdot\nabla,Q]
=[r\cdot\nabla,Q]+[h\cdot\nabla,Q],
}
\]

because the common affine advection part is exactly cancelled by the symbol transport, and

\[
\boxed{
Q\nabla u-\nabla u\,Q
=[Q,\nabla r]+[Q,\nabla h],
}
\]

because `Q` is scalar on vector components and hence `[Q,\bar A]=0`.  Thus the first bracket is literal **transport/interface incidence**, while the second is literal **selection--stretching mismatch**.  They have the same resolved/high split but are not physically synonymous.

**Classification: EXACT NSE/PDE IDENTITY.**

Since

\[
\mathcal K_u-G_{\rm aff}
=(r\cdot\nabla-\nabla r)+(h\cdot\nabla-\nabla h)
=: \mathcal K_r+\mathcal K_h,
\]

the material-flux source becomes

\[
\boxed{
\mathcal C_Q
=[\mathcal K_r,Q]+[\mathcal K_h,Q].
}
\]

The two terms have different physical owners:

1. `[`\(\mathcal K_r,Q\)`]`: **resolved non-affine role-interface incidence**.  It vanishes for a genuinely affine resolved field and is the vorticity-side relative-generator descendant of the Wang non-affine moving-role interface.
2. `[`\(\mathcal K_h,Q\)`]`: **high-field nonlinear incidence relative to the spectral role**.  It is not part of the resolved non-affine service term.

**Classification: EXACT NSE/PDE IDENTITY.**

If the smooth envelope has additional motion not generated by the certified common affine flow, retain

\[
E_Q:=\partial_tQ+[G_{\rm aff},Q]
\]

and then

\[
\boxed{
\mathcal C_Q=E_Q+[\mathcal K_r,Q]+[\mathcal K_h,Q].
}
\]

`E_Q` is the literal extra time-face/observer-motion owner.  On the certified affine-transport slab `E_Q=0`; at event re-anchoring the architecture uses a new hard event rather than pretending that a discontinuous reselection is smooth `Qdot` work.

**Classification: EXACT NSE/PDE IDENTITY.**

---

## 5. Where the physical Wang HH source sits inside the material calculus

Let

\[
\Omega:=\nabla\times V,
\qquad
\zeta:=\nabla\times h,
\qquad
\omega=\Omega+\zeta.
\]

Because the strict low pass has Fourier support in `|xi|<=N/4` while the propagated outer envelope stays above `N/2`,

\[
\boxed{Q\Omega=0.}
\]

Therefore the high-field commutator acts on the low vorticity as

\[
\boxed{
[\mathcal K_h,Q]\Omega=-Q\mathcal K_h\Omega.
}
\]

This is a high--low cross source, not HH self-generation.

For the high vorticity,

\[
\boxed{
[\mathcal K_h,Q]\zeta
=\mathcal K_h(Q\zeta)-Q\mathcal K_h\zeta.
}
\]

For divergence-free `h`,

\[
\mathcal K_h\zeta
=h\cdot\nabla\zeta-(\zeta\cdot\nabla)h
=\nabla\times\mathbb P\nabla\cdot(h\otimes h).
\]

Since scalar Fourier `Q` commutes with curl and Leray pressure is curl-invisible,

\[
\boxed{
-Q\mathcal K_h\zeta
=
\nabla\times\big[-Q\mathbb P\nabla\cdot(h\otimes h)\big].
}
\]

This is exactly the vorticity curl of the Wang **complete HH generation source**.

The companion term `K_h(Q zeta)` is not a second HH charge.  It appears because the present theorem differentiates in the **full physical material frame**, whose left-hand transport already contains the high field.  Wang's resolved-transporter representation places the HH term explicitly on the right.  Moving this term between the derivative and source is a repartition of the same NSE dynamics, not new physics.

**Classification: EXACT NSE/PDE IDENTITY and RIGOROUS NO-DOUBLE-COUNTING CONSEQUENCE.**

---

## 6. Resolved-cutoff renewal is not a moving-role time face

The Wang upstream proves for any resolved `V`, with `h=u-V` and the same smooth role `Q`, that the entire cutoff-dependent nonlinear expression reduces identically to

\[
-Q\mathcal B(u,u).
\]

Thus replacing `S_{N/4}u` by `S_{N_p/4}u` at a common-slice scale renewal only repartitions the same nonlinear interaction between transporter, HH source, and interface commutator.

It must **not** be charged as `Qdot` or as a new moving-cut currency.

**Classification: COUNTEREXAMPLE/NO-GO (decomposition gauge is not localization motion).**

---

## 7. Smooth SGS is a work reader, not another microscopic role source

The literal Wang smooth-SGS objects live at a second level:

\[
U=G_N*u,
\qquad
R=G_N*(u\otimes u)-U\otimes U,
\]

with physical resolved energy transfer read from the SGS trilinear multiplier.  The upstream theorem separates this macroscopic ledger from the microscopic full-velocity role equation.

Therefore the following must remain distinct:

- hard `P`: actual event HH work atom;
- smooth role `Q`: between-event microscopic carrier;
- coarse-grain `G_N`: resolved SGS work reader;
- `RU`, pressure boundary work, and resolved viscous boundary flux: macroscopic SGS/window terms.

Adding `RU`, pressure work, or SGS boundary viscosity into the microscopic material-flux source `C_Q omega` would double count a different conservation law.

If one deliberately chooses `G_N` itself as a vorticity localization operator, it has its own exact `C_{G_N}` law, but that is a different observable and is not the literal hard HH event role used by the programme.

**Classification: COUNTEREXAMPLE/NO-GO (two-level bookkeeping).**

---

## 8. Literal Kelvin first-bad operator is current-side, not a primal Eulerian `Q`

The Kelvin upstream's intrinsic first-bad map is

\[
M_{\rm fb}:G\to G,
\qquad
P_{\rm fb}=K M_{\rm fb}:G\to C_1^{\rm phys},
\]

where the columns of `K` are closed physical Kelvin cycles.  For the orientation-complete restart packet the literal selector is

\[
\boxed{
M_{\rm fb}^{\rm mf}=M_{\rm fb}\otimes I_3,
\qquad
P_{\rm fb}^{\rm mf}=K_{\rm mf}M_{\rm fb}^{\rm mf}.
}
\]

This is precisely the smallest literal selector capable of carrying the three loop coordinates needed by the Kelvin realization of `Z_H`.

But it acts on **current/germ coefficient space**, not directly on Eulerian vorticity.  Replacing it by an arbitrary primal spatial projector `Q` would be a type error.

**Classification: EXACT TYPE DISTINCTION and OPEN BRIDGE for a primal realization.**

---

## 9. Exact dual current-owner calculus

The correct analogue of the primal commutator is obtained by duality, not analogy.

Let `P_t:Y->X` realize germ coefficients as physical currents.  Let `T_X` be the physical current transport generator and `A_Y` the germ-frame generator.  Define

\[
\boxed{
G_P:=\dot P+T_XP-PA_Y.
}
\]

Let `y` satisfy `dot y=-A_Y y`, and let a physical cochain `phi` satisfy

\[
\dot\phi=T_X^*\phi+S
\]

with physical source `S` (for viscous material flux this is the cochain-side viscous source).  Then direct differentiation gives

\[
\boxed{
\frac d{dt}\langle\phi,Py\rangle
=
\langle S,Py\rangle
+
\langle\phi,G_Py\rangle.
}
\]

This is the current-side exact localization law.

For the literal factorization `P=KM`,

\[
\boxed{
G_P=G_KM+KG_M,
}
\]

where

\[
G_K=\dot K+T_XK-KA_Y,
\qquad
G_M=\dot M+A_YM-MA_Y.
\]

Thus there are only two continuous current-side localization owners:

1. `G_K M`: material-current realization / connection / refinement defect;
2. `K G_M`: support transport in germ coordinates.

**Classification: EXACT CURRENT/PDE DUALITY IDENTITY.**

This is the rigorous way to compare the Kelvin current architecture with the primal localized material-flux PDE.  A literal adjoint/state-map theorem is still required before identifying `G_P^*` with any specific Eulerian `C_Q`.

The upstream also contains a finite-chain `weighted_cycle_projector` used to audit generic Hodge-projector motion.  Its own report explicitly states that **no literal programme-specific CK/Hodge operator has been identified**.  It is therefore excluded from the present bridge rather than promoted to a fake `Q`.

**Classification: COUNTEREXAMPLE/NO-GO against importing an audit-only toy operator.**

Finally, common material-frame connection must be charged only once.  The Nanson frame already removes common physical stretching from `H^T omega`; a covariantly transported current library removes the same common basis motion on the dual side.  Metric/Gram evolution may diagnose strain and packet geometry, but it cannot be added as an independent signed cubic production term.

**Classification: RIGOROUS NO-DOUBLE-COUNTING CONSEQUENCE.**

---

## 10. Literal hysteretic first-bad selector has no smooth `Mdot` between events

The implemented selector is

`hysteretic_first_bad_projection(bad_flags, previous_index, resolved)`.

On an unresolved branch it keeps the previous rank-one germ index, hence

\[
\boxed{\dot M_{\rm fb}=0}
\]

in selector coordinates.  Continuous support transport can still arise from

\[
A_gM-MA_g,
\]

but this is germ-frame connection/interface work, not a derivative of the undefined badness threshold.

Entry and resolve are finite jumps

\[
dM_{\rm fb}=\sum_k\Delta M_k\,\delta_{t_k}
\]

in event-measure notation.  The upstream repository still takes both `bad_flags` and `resolved` as external Boolean oracles; the Navier--Stokes score/threshold and resolve predicate remain undefined.

A finite selector reset therefore cannot be promoted to a positive smooth phase-payment density.  At such an event the localized phase theorem must stop and re-register the physical observable unless a separate theorem identifies the jump with actual physical work.

**Classification: EXACT IMPLEMENTATION IDENTITY plus OPEN BRIDGE for physical event semantics.**

---

## 11. Moving quantile/shell cuts: fixed mass cancels only the integrated face

For a genuine moving cut on a state space,

\[
Q_t=1_{\{g(y,t)<a(t)\}},
\]

transported by a probability-current velocity `j`, distributional differentiation gives

\[
\boxed{
(\partial_t+j\cdot\nabla)Q_t
=
\delta_{g=a}
\big(\dot a-\partial_tg-j\cdot\nabla g\big).
}
\]

The fixed-mass quantile law is

\[
\boxed{
\dot a
=
\frac{
\int_{g=a}\frac q{|\nabla g|}(\partial_tg+j\cdot\nabla g)\,dS
}{
\int_{g=a}\frac q{|\nabla g|}\,dS
}.
}
\]

Substitution yields

\[
\boxed{
\int_{g=a}
\frac q{|\nabla g|}
\big(\dot a-\partial_tg-j\cdot\nabla g\big)\,dS
=0.
}
\]

But the integrand need not vanish pointwise.  Therefore a fixed-mass moving quantile generally carries a **nonzero local conservative interface relay** even though its total mass flux is zero.

Only in special cases -- for example a one-dimensional single boundary, or a level surface whose material rate `partial_t g+j.grad g` is constant on the boundary -- does the entire local face vanish.

The affine reverse-Gaussian Mahalanobis shell audited upstream is such a calibration: the exact covariance ODE makes

\[
\partial_\tau g+j\cdot\nabla g=0
\]

pointwise for `g=x^T\Sigma^{-1}x`, so a fixed threshold is genuinely co-moving.

**Classification: RIGOROUS CONSEQUENCE of the exact Reynolds/coarea law.**

This rules out the false principle

> fixed mass => no moving-cut time face.

The correct statement is

> fixed mass => zero **integrated weighted** face; local relay may remain.

---

## 12. Physical time and ancestry/reverse-age time cannot be merged

The preceding quantile formula in the Kelvin upstream is currently derived on the normalized ancestry/reverse-age state with its probability current.  Under reverse-age clock reversal the current velocity changes sign.

The physical material-flux equation in Sections 1--2 uses actual Navier--Stokes physical time and the physical material derivative `D_t`.

The upstream explicitly leaves open the programme-specific state map

\[
\Pi:\text{ancestry state}\to\text{physical reverse-age Kelvin state}
\]

satisfying the exact drift/diffusion intertwining equations.

Therefore the ancestry moving-cut face and the physical Eulerian `Qdot+[K_u,Q]` face may be placed in the same **Reynolds/interface mechanism class**, but they may not yet be identified as the same physical source.

**Classification: OPEN BRIDGE and COUNTEREXAMPLE/NO-GO against clock conflation.**

---

## 13. Stochastic Kelvin q.v. is not cubic interaction phase

For the literal orientation-complete Kelvin packet, the shared-noise quadratic-variation matrix is

\[
\Gamma_{\rm mf}
=2\nu H^T(\nabla\omega)(\nabla\omega)^TH.
\]

This is an exact physical second-order stochastic object.  Its metric contraction recovers viscous vorticity-gradient dissipation.

It is **not** the oriented cubic interaction

\[
\mathcal Z_H
=\frac1{\det H}\overline{\Phi_3}\cdot(\Phi_1\times\Phi_2).
\]

Likewise, a stochastic pair carré-du-champ source is not automatically the deterministic material-flux viscous phase term `nu Q Delta omega`.

A state-map / stochastic-Kelvin theorem may relate their viscous provenance, but covariance or q.v. cannot replace the signed third-order edge observable.

**Classification: COUNTEREXAMPLE/NO-GO (second order is not signed cubic work).**

---

## 14. Common owner calculus

After the type corrections above, the two architectures share the following small set of mechanisms.

| Mechanism | Wang literal realization | Kelvin literal realization | May be identified now? |
|---|---|---|---|
| common covariant motion | dual-affine transport of smooth `Q` | covariant current/germ-frame transport | **yes as an exact quotient principle**, not as the same operator |
| moving/interface face | extra `E_Q=Qdot+[G_aff,Q]` or non-affine role crossing | `G_Q/G_H` Reynolds face for quantile/shell cuts | **same mechanism class**; physical equality needs clock/state map |
| relative selection/deformation | `[K_r,Q]` and high `[K_h,Q]` | `G_KM` / `KG_M` current connection-support defects | **same relative-generator principle**; operator equality open |
| true HH generation | hard-cell work from `-Q B(h,h)`; vorticity curl `-Q K_h zeta` | no literal direct analogue yet | **architecture-specific** |
| conservative relay/relink | skew part of the native `Q^2` carrier interface after common gauge quotient | fixed-mass local cut relay / germ support crossing | **same conservation pattern**, not same currency |
| symmetric strain work | native `Q^2` smooth-carrier strain contribution | material metric/current-frame deformation data | **do not identify with signed cubic work without a theorem** |
| viscosity | `nu Q Delta omega`; SGS boundary viscosity at a different level | stochastic Kelvin q.v./future-variance bank on its own clock | **common viscous provenance only; no direct equality yet** |
| finite reselection | hard event re-anchor | first-bad entry/resolve jump | **same event type only**, not a positive payment |
| decomposition gauge | resolved cutoff renewal | ancestry coordinate/reference reparameterization when exact | **zero physical source when the exact repartition identity holds** |

Two absolute prohibitions follow:

1. `Q^2` smooth velocity-carrier energy is not the same object as a tensor-square pair covariance lift.
2. A resolved-cutoff switch is not a moving-observable time face.

---

## 15. Typed owner-resolved local phase/work alternative

Let a fixed, physically typed localized role triple be valid on an open interval with no hard reselection, no clock/state-map change, and no geometry exit.  Suppose its exact complex interaction satisfies

\[
\dot{\mathcal Z}
=\sum_{o\in\mathcal O}\dot{\mathcal Z}_o,
\]

where every owner `o` is produced by an exact algebraic partition of the literal source ledger (for example Wang's resolved non-affine defect, high relative incidence, extra time face if present, and viscosity).

Define

\[
A_o=\int\left|\Re\frac{\dot{\mathcal Z}_o}{\mathcal Z}\right|dt,
\qquad
P_o=\int\left|\Im\frac{\dot{\mathcal Z}_o}{\mathcal Z}\right|dt.
\]

Then the calculus theorem of `docs/09_local_phase_work_trichotomy.md` immediately refines to named owners:

- if amplitude first falls to `rho |Z(0)|`,
  \[
  \boxed{\sum_{o\in\mathcal O}A_o\ge\log(1/\rho)};
  \]
- if favorable phase first leaves the corridor from `c_hi` to `c_lo`,
  \[
  \boxed{\sum_{o\in\mathcal O}P_o\ge
  \arccos(c_{\rm lo})-\arccos(c_{\rm hi})};
  \]
- otherwise favorable localized cubic interaction persists quantitatively while the real geometry coefficient remains positive.

Hence at least one named literal owner pays the corresponding action divided by `|O|`.

**Classification: RIGOROUS CONSEQUENCE.**

The qualification “fixed, physically typed role triple” is essential.  A hard event reselection, first-bad reset, or unresolved ancestry-to-physical clock change is a **typed exit**, not a free continuous action payment.  The theorem stops there and asks for re-registration.

For the Wang smooth envelope this is presently a theorem about the localized **carrier cubic**.  Turning persistence of that carrier cubic into persistence of actual hard-cell HH work between events remains an open event-registration/physical-energy bridge.

For the Kelvin programme the orientation-complete current selector is now literal enough to carry a circulation triple, but converting its ancestry/current-side owner defects into the physical-time Eulerian `Z_H` source still requires the missing state-map/adjoint realization.

**Classification: OPEN BRIDGE after the local owner calculus.**

---

## 16. What was actually advanced

The localization frontier is narrower than before.

1. The two material localization sources are now one exact covariant object `C_Q=Qdot+[K_u,Q]`.
2. Common affine/material motion is quotiented exactly before any owner is charged.
3. The literal Wang smooth role splits into resolved non-affine and high-field relative generators; the physical HH source is identified exactly as the `-Q K_h zeta` summand, with no double count against full material transport.
4. Hard event `P`, smooth carrier `Q`, resolved cutoff `V`, and SGS filter `G_N` are proved to be different operator types.
5. The literal Kelvin orientation-complete selector `M_fb tensor I_3` is the correct current-side carrier of the three-loop interaction observable, but it is dual/current-side rather than a primal Eulerian `Q`.
6. Fixed-mass quantiles cancel only integrated interface flux; local moving-cut relay generally remains.
7. Physical time and ancestry/reverse-age time remain separated until the missing state-map theorem is supplied.
8. The local phase/work trichotomy now admits a named owner decomposition on every fixed typed interval, while reselection/clock changes are explicit stops rather than hidden payments.

The next hard theorem is therefore not another abstract norm bound.  It is one of two concrete bridges:

- **Wang side:** prove an event-to-event hard-work registration theorem that converts smooth-carrier `Z_Q` control plus physical-energy reentry into control of the next literal hard HH work atom;
- **Kelvin side:** construct the programme-specific ancestry-to-physical Kelvin state map / adjoint realization so the current-side `G_P` and moving-cut faces can be inserted into the physical-time `Z_H` source without clock conflation.

Neither theorem is presently proved.

---

## 17. Action adversarial calibration

`experiments/exp11_literal_owner_calculus.py` is an **ACTION STRESS TEST**, not a proof.  It is designed to run only in GitHub Actions and checks:

- the finite-dimensional identity `Qdot+[K,Q]=[K-G,Q]` when `Qdot+[G,Q]=0`;
- the Wang relative-generator split into resolved remainder plus high generator;
- the exact low-support identity `[K_h,Q]Omega=-Q K_h Omega` when `Q Omega=0`;
- the HH repartition `[K_h,Q]zeta=K_h(Q zeta)-Q K_h zeta`;
- the fixed-mass quantile counterexample: total weighted face zero while local faces remain nonzero;
- the hard-event/smooth-envelope no-go: `Q_i P_i=P_i` does not imply equality of the cubic built from the full smooth envelopes and the hard projected cubic.

The theorem statements above do not depend on these numerical checks.
