# Core PDE bridge spine: common physical laws before Wang/Kelvin programme-specific quotients

Status: **INTEGRATION MAP OF PROVED IDENTITIES / NO NEW REGULARITY CLAIM**.

This document records the present center of repo 3.

The purpose of this repository is **not** to replace the Wang or Kelvin programmes by a third proof programme.  Its central job is to strengthen both by identifying, from the literal Navier--Stokes PDE,

1. which physical objects are exactly common;
2. how those objects appear in different representations;
3. which programme-specific quotients lose different information;
4. which apparent correspondences are false.

Any regularity architecture that benefits from these bridges is a downstream consequence.

## 1. Layer zero: the actual local Navier--Stokes state

Before roles, packets, selectors, covariances or recurrence, the local first-order physical state is

\[
A=\nabla u=S+\Omega,
\qquad
S^T=S,
\quad
\Omega^T=-\Omega,
\quad
\operatorname{tr}S=0,
\]

with

\[
A-A^T=[\omega]_\times.
\]

The differentiated NSE is

\[
D_tA+A^2=-\nabla^2p+\nu\Delta A.
\]

Everything below is a representation, localization or higher-jet reading of this physical state.

## 2. First rigid law: deformation versus connection

The resolved linearized operator has the exact Cartan split

\[
\mathcal L_V
=\mathcal K_V+\mathcal S_V,
\]

\[
\boxed{
\mathcal K_V=\mathbb P(V\cdot\nabla+\Omega_V),
\qquad
\mathcal S_V=\mathbb P(S_V\,\cdot),
}
\]

with

\[
\mathcal K_V^*=-\mathcal K_V,
\qquad
\mathcal S_V^*=\mathcal S_V.
\]

Physical meaning:

- `K`: conservative transport/connection/relink sector;
- `S`: deformation/material metric-work sector.

For the resolved material metric,

\[
\boxed{H_V\dot M_VH_V^T=2S_V.}
\]

Thus Wang's symmetric resolved work is literally material metric velocity, while its skew sector is connection/transport modulo pressure gauge.

The same split exists for the unresolved field `h` and therefore for actual HH work.

## 3. Second rigid law: exterior degree determines the sign of deformation

For incompressible `A=S+Omega`, the Hodge representations are

\[
\boxed{
R_1(A)=S+\Omega,
\qquad
R_2(A)=-S+\Omega,
\qquad
R_3(A)=0.
}
\]

Hence:

| exterior degree | physical objects | generator |
|---|---|---|
| `Lambda^1` | material line, inviscid vorticity | `S+Omega` |
| `Lambda^2` | material area Hodge vector, local affine Fourier wavevector | `-S+Omega` |
| `Lambda^3` | oriented volume / common interaction top form | `0` |

This is why Wang wavefront geometry and Kelvin material-surface geometry obey the same local `-A^T` law, while common incompressible deformation is neutral on top volume.

## 4. Third rigid law: connection can be gauge-transported; strain cannot

For a state law

\[
\dot y=(K+S)y
\]

and orthogonal projector `P(t)`, define

\[
G_P=\dot P-[K,P].
\]

Then

\[
\boxed{
\frac d{dt}\frac12\langle y,Py\rangle
=\langle Py,Sy\rangle
+\frac12\langle y,G_Py\rangle.
}
\]

Therefore:

- fixed hard role: conservative `K` relink is visible;
- connection-comoving role: the same `K` becomes common observer transport;
- genuinely non-comoving role: `G_P` is an interface/selector face;
- finite reselection: finite jump, not smooth payment.

Under an orthogonal frame rotation,

\[
\widetilde S=O^TSO,
\qquad
\widetilde\Omega=O^T\Omega O-O^T\dot O.
\]

Thus connection is gauge-sensitive while physical strain spectrum and metric work survive every common orthogonal observer gauge.

This explains rather than erases the distinction between Wang fixed-event `K`, Wang moving-role connection, and Kelvin orientation-frame motion.

## 5. Fourth rigid law: pressure has a representation-dependent physical role

Pressure gradient is invisible to:

\[
\langle w,\nabla p\rangle
\]

for divergence-free `w`, to closed Kelvin circulation, and to curl.

But at gradient/metric-curvature order,

\[
\boxed{
D_tS+S^2+\Omega^2
=-\nabla^2p+\nu\Delta S.
}
\]

Pressure Hessian is therefore a genuine material-deformation face even though pressure gradient is gauge for first-order solenoidal work/circulation.

This is a model of the repository's typing rule: **an object may be gauge in one physical readout and active in another.**

## 6. Fifth rigid law: viscosity has one scalar Dirichlet amount but richer tensor information

At the instantaneous full physical state,

\[
\boxed{
2\nu\sum_{k,s}|k|^4E_{k,s}
=\nu\|\nabla\omega\|_2^2
=\frac12\int\operatorname{tr}\Gamma_K\,dx.
}
\]

Thus Wang spectral enstrophy killing and Kelvin orientation-complete q.v. trace are the same full-state Dirichlet dissipation.

But equal scalar killing does not determine the Kelvin q.v. tensor.  Relative polarization phase can change `Gamma_K` while leaving modal energies and its trace fixed.

The bridge is an exact scalar equality plus an exact tensor-information no-go.

## 7. Sixth rigid law: phase-space strain and fiber strain are different representations of the same `S`

For local affine transport,

\[
\dot k=-A^Tk,
\qquad
\frac d{dt}\log|k|
=-\hat k\cdot S\hat k.
\]

So conservative transport can move spectral content radially while preserving total transported `L^2`.

Separately, `S` acts on vector amplitudes as material metric work.

Therefore

\[
\boxed{
\text{radial spectral motion}
\not\equiv
\text{energy generation / symmetric fiber work},
}
\]

even though both read the same local strain tensor in different representations.

This distinction is essential for interpreting Wang radial crossing physically.

## 8. Wang objective polarization is the trace-free quotient of the same deformation

Current Wang's exact affine Kelvin mode gives, in an objective transverse frame,

\[
\dot c=-(B_\perp+\nu|k|^2I)c,
\qquad
B_\perp=E^TSE.
\]

Incompressibility forces

\[
\operatorname{tr}B_\perp
=\frac d{dt}\log|k|.
\]

Hence

\[
\boxed{
|k|\det U_\perp
\exp\left(2\nu\int|k|^2dt\right)
=\text{constant}.
}
\]

Factoring this scalar carrier/viscous dilation leaves

\[
\widetilde U\in SL(2,\mathbb R)=Sp(2,\mathbb R),
\]

generated by the trace-free transverse material metric velocity.

Noncommuting trace-free strains then have one exact commutator which appears as:

- real material polar holonomy;
- opposite circular/helical phase.

Thus Wang symplectic/helical geometry and repo-3 material holonomy are different basis readings of the same transverse metric-deformation algebra.

## 9. Full non-affine seam: one exact affine-quotient law

The quadratic Hessian bridge is now only the first derivative-level shadow of a stronger full-field statement.  In normalized material coordinates,

\[
v_W(z)=L^{-1}[u(X+Lz)-\dot X]
=c+A_Lz+\mathcal N_L(z),
\]

while Wang's Gaussian best-affine residual is

\[
R_W=v_W-\bar v-\bar A z.
\]

Therefore

\[
\boxed{
R_W-\mathcal N_L
=(c-\bar v)+(A_L-\bar A)z\in\mathrm{Aff}.}
\]

The two full residual fields are not identical, but they define exactly one physical non-affine class:

\[
\boxed{[R_W]_{/\mathrm{Aff}}=[\mathcal N_L]_{/\mathrm{Aff}}.}
\]

Every higher physical jet is then forced, not guessed:

\[
\boxed{
D^pR_W=D^p\mathcal N_L
=L^{-1}(\nabla^p u)L^{\otimes p},
\qquad p\ge2.}
\]

Thus the old “higher-jet seam” has collapsed at field level.  The common Hessian

\[
B=L^{-1}(\nabla^2u)L^{\otimes2}=\mathfrak J_2(L)
\]

is simply the `p=2` member of this one quotient law.  Programme-specific readouts can still discard information: Wang's third-Hermite transverse shape sees `Sym B`, while Kelvin's codeforming surface dynamics keeps the full `B`; the exact divergence-free kernel with `Sym B=0` but `B\ne0` remains a no-go against identifying those quotients.

Only **after** this exact typing may a norm be used.  Gaussian orthogonality gives

\[
\|\mathcal N_L\|_\rho^2
=\|R_W\|_\rho^2
+|\bar v-c|^2
+\operatorname{tr}[(\bar A-A_L)C_\rho(\bar A-A_L)^T],
\]

so `R_W` is the minimal `L^2(rho)` representative of the common affine class and the Kelvin excess is exactly affine-gauge mismatch.  This residual norm is **not** Wang's coherent deformation variance `K_C^2=E||grad W-Abar||_F^2`.

## 10. Current Wang/Kelvin dictionary

| physical object | Wang reading | Kelvin reading | relation |
|---|---|---|---|
| `S_V` | symmetric resolved/interface work | resolved part of residual/dyad deformation | **same tensor** |
| `Omega_V` / `K_V` | relink, transport, moving-role connection | orientation/current connection after correct state map | same Cartan sector, **not yet same state representation** |
| `S_h` | symmetric part of actual HH role work | unresolved residual/dyad deformation | **same tensor** |
| local `-A^T` | Fourier carrier/wavefront transport | material-area/current geometry | **same `Lambda^2` representation** |
| pressure gradient | Leray-quotiented work | closed-loop/curl-quotiented | same exact-gradient gauge |
| pressure Hessian | strain/metric-curvature source | full-state strain/material-metric curvature; finite-shape descent keeps additional shape residuals | physical at derivative order, not a scalar common charge |
| viscous enstrophy loss | spectral killing | `1/2 tr Gamma_K` after full-state integration | **same scalar Dirichlet form** |
| q.v. tensor | not determined by scalar killing | orientation-complete tensor | strictly richer directional information |
| trace-free transverse `D` | helical conversion / `SL(2)` polarization | material metric holonomy | same transverse metric-deformation tensor |
| full non-affine field | Gaussian best-affine residual `R_W` | anchor-Taylor residual `N_L` | **same class modulo `Aff`; distinct gauges** |
| higher jet `J_p`, `p>=2` | derivatives of Gaussian residual before programme-specific Hermite readout | derivatives of codeforming nonaffinity | **exactly the same physical jet** |
| normalized Hessian `B=J_2` | `Sym B` after third-Hermite transverse quotient | full codeforming `J_2(L)` | **same input, different quotient** |
| linear synthesis/refinement | coherent child sum with cross-pair energy | frame-aware current/event synthesis | **same tensor-square functor; cross pairs are physical** |
| first-bad selector | no direct Wang identity | readout `E_g` of a persistent germ library, not physical transport | state-map must retain hidden library/full pair state |
| full ordered pair/Gram coupling | coherent child pairs retain relative phase/coherence | same-replica cross-germ Gram retains relative common-driver orientation | **diagonal marginals lose physical relative coupling** |
| selector jump history | no direct instantaneous Wang identity | optional jump-q.v. accumulator of the càdlàg selected readout | **not an endpoint-state function** |
| packet/frame representation | no direct raw-coordinate Wang identity | `(H,epsilon)` with passive `(H,epsilon)~(HS,S^T epsilon)` | physical residual/inverse-Gram energy live on the quotient; raw coefficient norm does not |
| enstrophy critical current | continuing material carrier follows the material flow between genuine events | nondegenerate critical locus satisfies `xdot_*-u=-H_e^{-1} grad R` | **different currents in general**; exact ABC separates them |
| candidate ranking crossing | hard role requires actual nonlinear work/interaction | two persistent critical candidates can exchange rank by the three-face enstrophy-rate law | **not a hard interaction clock**; exact heat shear has crossing with zero nonlinearity |
| selected-family boundary charge | exact Moyal `R_switch` on inherited-stock sidecar; positive even on an identical state; zero generation depth by same-state anti-theorem | selector/readout boundary and optional jump-history charges are also not physical work | **same zero-depth guardrail, different currencies**; do not identify Moyal energy with selector q.v. |
| own-local target reanchoring | Wang common carrier-chart reanchoring is passive gauge | Kelvin own-local event is affine `x_+=Ax_-+d`, `d=A Omega_- - Omega_+`; target-gradient face can change q.v. source at `A=I` | **not the same gauge/type** despite exact coboundary composition |
| selector-label path variation | no direct Moyal equality; selected-family boundary currency is separately typed | right-continuous one-hot winner has `tr J_Y=2N` for `N` simple crossings; even `N` can return to the same label | **path/readout sidecar, zero hard-generation depth absent a physical owner** |
| critical-lineage theorem domain | material-carrier ancestry is a separate owner/history datum | isolated critical point needs invertible `H_e`; symmetry sheet uses active normal Hessian/support chart | **winner value does not determine lineage persistence or Morse/normal type** |
| exact critical-sheet merger | no automatic Wang hard event: advective nonlinearity is zero | latest Kelvin fixed-shape translated packet library has `A=E_0`, `d=0`, zero target-gradient face, full same-replica cross blocks, and zero selected physical jump at collision | **real geometry/library event after packet functor is supplied; scalar merger alone does not fix shape/ancestry** |

### Hybrid event/readout ledger: same quadratic algebra, different physical owners

Let `X` denote the persistent Kelvin library, `E_- -> E_+` a selector/readout change, and `A` a specified linear physical library event.  On a common target, the exact combined readout operator is

\[
\boxed{
D:=E_+A-E_-
=E_-\Delta A+\Delta E+\Delta E\,\Delta A.}
\]

The displayed linear ledger is the exact **common-target** slice.  For packet-specific own-local targets the current Kelvin interface is affine,

\[
\boxed{x_+=Ax_-+d,\qquad d=A\Omega_- - \Omega_+,}
\]

and a simultaneous selector has the full finite jump

\[
\boxed{J=(E_+A-E_-)X+E_+d.}
\]

The target offset is a coboundary under composition, but its pair/dyad and Brownian target-gradient cross faces remain mandatory own-local readout terms.  In particular `A=I` does not imply that own-local residual/q.v. data are unchanged.  This target operation is not Wang's passive same-carrier chart reanchoring.


The mixed finite face `DeltaE DeltaA` is mandatory.  It is an observer/physical-event interaction, not Brownian q.v.

For a full library pair state `P`, the selected endpoint pair revaluation is

\[
\boxed{
\Delta P_{\rm sel}
=DP E_-^T+E_-P D^T+DPD^T.}
\]

For one same-replica noise-response library `N`, put `B_-=E_-N`, `dB=DN`.  The **continuous Brownian source-rate revaluation** is

\[
\boxed{
\Delta\Gamma_{\rm cont}
=2\nu\left(dB B_-^T+B_-dB^T+dB dB^T\right).}
\]

By contrast, for a pathwise library state `X`, the finite selected jump is `J=DX` and the optional jump-q.v. atom is only

\[
\boxed{\Delta[Y]_{\rm jump}=JJ^T.}
\]

Finally, along a supplied selector path,

\[
\mathcal J[Y]=\sum_j\Delta_jY\,\Delta_jY^T
\]

is a **history functional**.  Pair revaluation telescopes on a closed loop, whereas `\mathcal J` can be strictly positive.  Hence the current endpoint pair, the current continuous source rate, the finite jump square, and the accumulated jump history are not interchangeable quadratic budgets.


## 11. What remains central

The next core questions are not “can this already prove regularity?”  They are:

1. **Literal state-map assembly.**  Any viable Wang→Kelvin lift must now preserve, as separately typed data whenever the target theorem uses them,
   \[
   \boxed{\text{Eulerian/coherent field}
   +\text{material current/shape}
   +\text{packet/frame physical state modulo passive gauge}
   +\text{critical-locus current/geometry and lineage theorem domain when used}
   +\text{typed ranking/geometry/selector/event clock-history}
   +\text{underlying physical owner/event/synthesis }A
   +\text{own-local target/anchor coboundary }d
   +\text{typed boundary sidecars and inherited stock/ancestry when used}
   +\text{persistent library with full relative pair/Gram coupling}.}
   \]
   The selector is a readout, not physical transport.  Full pair state means the ordered cross coupling modulo only the legitimate **common** latent gauge; diagonal marginals create an artificial product gauge and lose synthesis data.  Accumulated selector jump q.v. has nonzero closed-loop circulation, so if a theorem uses that path functional it must carry history/an equivalent accumulator or prove an independent physical timing theorem that reconstructs it from the endpoint.  The arbitrary-finite heat-shear family sharpens this to `tr J_Y=2N` for a one-hot winner selector while both tracked sheets remain strict normal maxima on one compact interval and nonlinear advection is zero.  **Winner/readout, lineage theorem domain, and physical owner are three different axes.**
2. **Programme-specific readouts after quotient closure.**  The full higher-jet field seam is closed by the affine-quotient law.  What remains is to derive only those Wang Hermite/packet and Kelvin surface/moment projections actually used by the two programmes, without pretending the quotients are identical.  Exact periodic NSE now gives a sharp order witness: two enstrophy critical sheets can have identical local velocity 2-jets but different third jets and therefore different curvature branch rates.  Thus quotient closure does not mean a `p=2` truncation; the PDE decides which higher readout is needed.
3. **Localized pressure/viscosity.**  Push the exact full-state pressure/Dirichlet dictionaries through actual smooth roles without losing commutator, boundary, q.v., common-noise cross blocks or clock faces.
4. **Wang native branch semantics.**  Wang now types sidecar-bearing inherited stock at the representation layer: intrinsic membership rereading is zero-charge provenance, and selected-family switching carries exact Moyal boundary energy `R_switch` whose same-state anti-theorem gives zero generation depth.  The open native seam is central/joint-stop integration of this sidecar while independently witnessed material/source service remains event-facing; `R_switch` itself may not be promoted to recurrence work.
5. **Kelvin first-bad library/timing instantiation.**  Current read-only Kelvin now goes beyond a generic affine interface: exact-head `d0c5863...` instantiates an analytic critical-sheet merger and, for one specified fixed-shape translated packet per sheet, a real dimension-dropping event `A=E_0` with `d=0`, zero target-gradient coboundary, nonzero same-replica cross blocks, and zero selected physical jump at collision.  The same audit proves scalar/position merger alone does not force full packet coalescence, and distinct branch histories remain distinct ancestry data.  Repo-3 separately proves local lineage/Morse rigidity and arbitrary finite ranking activity inside a nondegenerate compact interval.  The remaining literal seam is the actual badness/resolve rule, endogenous selector local finiteness/interface calculus, target/shape generation, support exit/bifurcation, and identification of physical branch ancestry with the programme ancestry state.

A necessary assembly guardrail is now exact: any hard-generation increment must vanish on the demonstrated pure-sidecar directions (pure selector reset on fixed library/target; same-state positive Wang Moyal boundary reread without independent service/source work; pure target q.v. reanchor with zero nonlinear advection).  Simultaneous genuine owners must still be preserved; the guardrail removes fake depth, not real multi-owner physics.

These tasks strengthen the two upstream programmes whether or not they eventually contribute to any global regularity argument.

## 12. Research discipline

The repository will continue to follow this order:

\[
\boxed{
\text{actual NSE phenomenon}
\to
\text{physical/PDE type}
\to
\text{exact representation law}
\to
\text{programme-specific quotient}
\to
\text{estimate only when needed}.
}
\]

A shorter proof architecture, if one emerges, is an **effect** of discovering these rigid physical laws.  It is not the object imposed on them from above.


## Relative-boundary transport layer (HK–HR)

The physical state/event spine now has one further forced separation.  For any moving balance surface/control object, the selector enters the exact PDE ledger through **relative** boundary velocity `V-u`, never through absolute selector speed.  Scalar inventories obey bulk-source + physical-flux + swept-boundary transfer; circulation obeys the corresponding swept-ribbon Kelvin law.  A pure boundary sweep is real transfer, not gauge, but exact heat shear proves that its magnitude or singular rate cannot be promoted to hard nonlinear/source generation.

The latest exact Kelvin merger also forces a transport-memory slot: endpoint anchor/current/residual coalescence can coexist with nontrivial Nanson frame holonomy.  Therefore the core typed state must preserve `transport ancestry/frame history (or equivalent holonomy)` separately from current residual readout.

Current owner-first order:

`intrinsic NSE source/sink/flux -> PDE-generated relative selector/boundary motion -> swept readout currency -> typed selector/target/Moyal sidecars`, with ancestry memory carried through the event.  Wang's current central routing independently enforces the same ordering principle for its own distinct currencies: physical stop first, sidecar second.  This is architecture hygiene, not yet a recurrence/termination theorem.


## Record-owner refinement after HS--HZ

The exact moving-boundary owner law now has a pointwise first-hit counterpart.  For the literal enstrophy field `e=|omega|^2/2`, the active spatial maximum satisfies

\[
D_+M=\max_{A(t)}[\omega\cdot S\omega-\nu(|\nabla\omega|^2-\Delta e)].
\]

Critical drift, ranking and selector motion determine which branch is read but contribute no direct value currency because `grad e=0` on the active set.  The running record `R(t)=max_{s<=t}M(s)` is therefore an intrinsic monotone owner clock whose positive increments require stretching to beat the full viscous/curvature defect.  This clock is deliberately distinct from selector q.v., moving-cut sweep, Moyal boundary charge, target reanchoring and inherited ancestry.  Any future first-bad assembly that uses enstrophy-record growth must route those side data after the local owner has been identified.

The remaining hard seam is no longer to invent a generation counter.  It is to prove or disprove an NSE law limiting *fresh effective stretching on record states* through geometry, material ancestry, donor exhaustion or owner reuse.


## Stretching-owner self-constraint after IA--IH

The record clock now feeds into a second exact PDE layer.  With `P=omega.S.omega`,

\[
D_tP=\omega^TS^2\omega-\omega^T(Hess p)\omega+V_P.
\]

The first term is nonnegative self-strain, while the pressure face is a signed directional curvature determined by the global incompressibility solve `-Delta p=|S|^2-|omega|^2/2`; viscosity has its own diffusion/gradient-conversion decomposition.  Exact affine strain--spin and periodic ABC calibrations realize opposite pressure signs.  Thus the common spine now has two nested owner gates: actual record growth requires stretching dominance, and persistence/renewal of stretching is itself constrained by strain square, pressure curvature and viscosity.
