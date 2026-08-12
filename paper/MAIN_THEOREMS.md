# Main theorem spine — working draft

These statements are the current self-contained mathematical spine of the bridge paper.  They are intentionally separated from any 3D Navier--Stokes regularity claim.

## Theorem A — Dual deformation geometry

For a smooth incompressible flow map with deformation gradient `F`, material area covectors and Kelvin/Fourier wavefront covectors are transported by `F^{-T}`.  The material metric

\[
M=F^TF
\]

and spectral covector metric `M^{-1}` are dual.  In particular

\[
|k|^2=k_0^TM^{-1}k_0.
\]

## Theorem B — Metric velocity is objective strain

For an invertible material area frame `H=F^{-T}`,

\[
H(D_tM)H^T=2S,
\qquad S=\operatorname{sym}\nabla u.
\]

Consequently the trace-free restriction of the material metric velocity to a triad plane is exactly the nonconformal strain driving Fourier/helical polarization and triad deformation.

## Theorem C — Near-extremal triad coordinates are inverse-metric observables

For the symmetric reference triad with directions `n_a,n_b,n_c`, define

\[
q_j=n_j^TM^{-1}n_j.
\]

Then the spectral Hodge coordinates are

\[
u=\frac12\log\frac{q_b}{q_a},
\qquad
v=\frac14\log\frac{q_c^2}{q_aq_b}.
\]

Thus material anisotropy, including its orientation relative to the triad, quantitatively determines near-extremal spectral shape loss.

## Theorem D — Noncommuting strain holonomy is polar material rotation

Successive noncommuting symmetric deformations generate a second-order rotation governed by their commutator.  In the planar two-strain calibration this is simultaneously the second Magnus/geometric-phase generator of the helical description and the polar-rotation part of the material deformation.

## Theorem E — Signed helical edge work is an oriented material-flux 3-form

For a resonant helical edge `k_1+k_2=q`, let

\[
\Phi_j=H^T\omega_j.
\]

Then

\[
\boxed{
T_e=
2\frac{s_q}{|q|}
\left(\frac{s_1}{|k_1|}-\frac{s_2}{|k_2|}\right)
\operatorname{Re}\mathcal Z_H,
}
\]

where

\[
\boxed{
\mathcal Z_H
=\frac{1}{\det H}
\overline{\Phi_q}\cdot(\Phi_1\times\Phi_2).
}
\]

`Z_H` is invariant under passive `GL(3)` packet reparameterization and resonant spatial translation.  Its argument is the gauge-invariant interaction phase.  Metric/covariance alone cannot determine this phase because they are second-order while `Z_H` is genuinely third-order.

## Theorem F — Localized material-flux source law

For any sufficiently regular time-dependent linear role operator `Q(t)`,

\[
\boxed{
D_t(H^TQ\omega)
=H^T\Big[
(\partial_tQ+[u\cdot\nabla,Q])\omega
+(Q\nabla u-\nabla u\,Q)\omega
+\nu Q\Delta\omega
\Big].
}
\]

The three terms are respectively moving/interface transport, strain--selection mismatch, and viscosity.  For `Q=I` the two localization terms vanish and the full Kelvin/Nanson viscous flux law is recovered.

## Theorem G — Moving localization has an unavoidable time face

If `Q=Q(t)`, the term `partial_t Q` is a literal source face.  It cannot in general be replaced by the static commutator `[u.grad,Q]`.  It vanishes only under an explicitly proved covariant/co-moving law.

## Theorem H — Kelvin-loop realization of interaction phase

For an orientation-complete packet of small material loops with area frame `r^2H`, let `Gamma_j(r)` be the three role-filtered circulation coordinates.  Then

\[
\boxed{
\lim_{r\to0}
\frac{\overline{\Gamma_q(r)}\cdot(\Gamma_1(r)\times\Gamma_2(r))}
{\det(r^2H)}
=\mathcal Z_H.
}
\]

Hence the signed nonlinear interaction and its `U(1)` phase have a literal Kelvin-current small-loop realization.

## Theorem I — Monochromatic viscosity does not rotate interaction phase

For one resonant Fourier edge,

\[
\dot{\mathcal Z}_{\nu}
=-\nu(|k_1|^2+|k_2|^2+|q|^2)\mathcal Z.
\]

Therefore

\[
\boxed{\dot\vartheta_{\nu}=0,
\qquad \vartheta=\arg\mathcal Z.}
\]

Viscosity damps interaction amplitude but does not rotate monochromatic interaction phase.  Instantaneous phase rotation is nonlinear; for localized packets a viscous phase term must be derived from the non-monochromatic role rather than assumed absent.

## Theorem J — Local phase/work no-free-escape trichotomy

Assume a selected interaction remains in a geometry corridor `kappa(t)>=kappa_*>0`, starts with normalized alignment `c(0)>=c_hi`, and let `0<c_lo<c_hi<1`, `0<rho<1`.  Then before geometry exits, either `|Z|` falls below `rho|Z(0)|`, or `Re Z/|Z|` falls below `c_lo`, or the actual signed work obeys

\[
W(t)\ge kappa_* c_{lo} rho |Z(0)|>0.
\]

At the first amplitude-loss time the sum of physical channel amplitude actions is at least `log(1/rho)`.  At the first phase-loss time the sum of channel phase actions is at least

\[
\arccos(c_{lo})-\arccos(c_{hi}).
\]

Thus loss of favorable physical work cannot occur for free while geometry remains good.  This is a local calculus theorem, not a global recurrence or regularity result.

## Theorem K — Exterior-power common-deformation cancellation

The Fourier parent wedge and the material interaction 3-form obey the same determinant law.  A common trace-free `2x2` generator preserves the polarization `Lambda^2` wedge, and a common trace-free real `3x3` generator preserves the complex vorticity `Lambda^3` interaction volume.  With role-dependent generators, only their differences from an arbitrary common reference (plus the reference trace) enter the derivative.  Thus common incompressible deformation is geometric transport; differential deformation/forcing is the interaction-changing content.

# Current open theorem

The next genuinely new closure target is a **localized phase/work alternative** derived from Theorems E--I:

> On a physically selected localized resonant packet, either favorable `Re Z_H` persists for a controlled interval, or loss of favorable work is quantitatively charged to an explicit phase-velocity source (moving/interface transport or strain-selection mismatch), or the interaction amplitude is lost through a separately typed physical channel.

No theorem currently proves that this alternative terminates a Navier--Stokes recurrence or yields regularity.

## Theorem L — Covariant localization owner calculus and typed local alternative

Let

\[
\mathcal K_u=u\cdot\nabla-\nabla u.
\]

For every sufficiently regular spatial role operator `Q(t)`, the exact localized material-flux law can be written

\[
\boxed{
D_t(H^TQ\omega)
=H^T\left[(\partial_tQ+[\mathcal K_u,Q])\omega+\nu Q\Delta\omega\right].
}
\]

If `Q` is transported by a common generator `G`, so `partial_t Q+[G,Q]=0`, then only the relative generator survives:

\[
\boxed{\partial_tQ+[\mathcal K_u,Q]=[\mathcal K_u-G,Q].}
\]

For the literal Wang smooth role, with `V=S_(N/4)u`, `h=u-V` and common affine generator `G_aff`, this gives exactly

\[
\partial_tQ+[\mathcal K_u,Q]
=[\mathcal K_{V-\bar V_{aff}},Q]+[\mathcal K_h,Q],
\]

and the vorticity curl of the physical HH source is the explicit summand

\[
-Q\mathcal K_h(\nabla\times h)
=\nabla\times[-Q\mathbb P\nabla\cdot(h\otimes h)].
\]

For the literal orientation-complete Kelvin restart selector `M_fb^mf=M_fb tensor I_3`, first-bad support commutes with every orientation `GL(3)` reparameterization and is therefore phase-neutral inside a frozen active germ.  For a general current-side selector `P=KM`, the dual covariant defect is

\[
G_P=\dot P+T_XP-PA_Y=G_KM+KG_M,
\]

so realization/connection and support transport are the only continuous current-side localization owners.  Moreover, an ancestry scalar cut descends through a state map `Pi:Y->X` to a physical selector iff it is constant on every fiber of `Pi`.  A moving fixed-mass quantile cancels only its integrated weighted Reynolds face; the local face need not vanish pointwise.

On any interval where the role type, physical clock/state map and geometry corridor remain fixed, the local phase/work trichotomy refines to these named exact owners: loss of cubic amplitude or phase forces the corresponding sum of owner actions to pay the same logarithmic/angular threshold; otherwise favorable localized cubic interaction persists.  Hard reselection, first-bad reset, or an unresolved clock/state-map transition is a typed exit requiring re-registration, not a positive continuous payment.

For the literal Wang hard/smooth registration, writing `R_i=Q_i-P_i` expands the smooth cubic into the hard cubic plus seven overlap terms.  Thus `QP=P` exactly registers hard **field components**, not the scalar cubic before re-projection.  The upstream `Q^2` Hahn-energy law does give a different exact handoff: positive smooth-carrier HH generation is dominated by actual positive physical HH work, after which hard edge geometry/phase is read eventwise.

This theorem therefore does not identify smooth Wang carrier cubic work with hard event HH work between events, and it does not identify ancestry-time Kelvin cuts with physical-time Eulerian localization before the missing state-map theorem.

## Theorem M — One closed triad has one cyclic material interaction phase

For a real Navier--Stokes field on a closed helical triad

\[
k_0+k_1+k_2=0,
\]

let `Phi_i=H^T omega_(k_i)` in one real material area frame.  Rooting the same triad at child `-k_i` gives

\[
\mathcal Z_i
=\frac1{\det H}\overline{\Phi_{-k_i}}\cdot(\Phi_j\times\Phi_\ell).
\]

Reality and cyclic invariance of the scalar triple product imply

\[
\boxed{\mathcal Z_0=\mathcal Z_1=\mathcal Z_2=: \mathcal Z_\triangle.}
\]

Writing `x_i=s_i/|k_i|`, the three actual child-energy works are

\[
T_0=2x_0(x_1-x_2)\operatorname{Re}\mathcal Z_\triangle,
\]

with the two cyclic analogues.  Their real coefficients sum exactly to zero, hence

\[
\boxed{T_0+T_1+T_2=0.}
\]

Thus cyclic re-rooting changes only the real helicity/frequency owner coefficient; it does not rotate interaction phase.  Negative donor work is therefore not equivalent to phase loss.  The current Wang cyclic donor/recipient kernel is same-time redistribution of one common cubic interaction among three energy roots, not a new phase source.

## Theorem N — Stochastic Cauchy deformation is the packet material metric replica by replica

On one backward stochastic Kelvin replica in reverse age `sigma`, let

\[
\partial_\sigma D=D(\nabla u)^T,
\qquad F_C=D^T,
\qquad H_C=\rho^2F_C^{-T},
\qquad M_C=(H_C^TH_C)^{-1}.
\]

Then exactly

\[
\boxed{DD^T=F_C^TF_C=\rho^4M_C.}
\]

Moreover, with `S=sym grad u`,

\[
\partial_\sigma(DD^T)=2DSD^T,
\qquad
\boxed{H_C(\partial_\sigma M_C)H_C^T=2S.}
\]

Thus the stochastic Cauchy deformation Gram tensor is literally the same Nanson/material packet metric on that replica, and its finite-variation work is objective strain rather than martingale quadratic variation or centered covariance.  Incompressibility fixes `det D` but not metric anisotropy.

For the fixed-past Cauchy bank,

\[
R_s=\mathbb E[DD^T]=\rho^4\mathbb E[M_C],
\]

and the total second moment satisfies `Q_s <= W_s R_s` in Loewner order.  This same-replica identity does not identify the deterministic first-bad selected packet with the replica ensemble; selector/replica alignment and state-map descent remain separate open bridges.

## Theorem O — Hard event phase is an exact plateau readout of the full Wang carrier

For each literal Wang hard event role `P_i` and its smooth scalar envelope `Q_i` satisfying

\[
P_iQ_i=Q_iP_i=P_i,
\]

one has leg by leg `P_i(Q_i omega_i)=P_i omega_i`.  Therefore the hard material cubic obeys

\[
\boxed{
\mathcal Z_P(Q_0\omega_0,Q_1\omega_1,Q_2\omega_2)
=
\mathcal Z_P(\omega_0,\omega_1,\omega_2).
}
\]

Thus the full smooth carrier retains the hard event interaction amplitude and phase exactly on the event plateau, independently of how the envelope is filled outside that plateau.  This does not imply `Z_Q=Z_P`: the unprojected smooth cubic contains seven overlap terms.  Nor can the native quadratic carrier energy determine cubic phase, since a Fourier phase rotation preserves every quadratic energy while rotating `arg Z_P`.

Hence Wang's literal architecture needs no persistent hard phase between events: energy is carried quadratically, while hard geometry/phase is re-read from the actual field at each physical event.  A later hard role need not lie on the previous envelope plateau, so no event-to-event phase-persistence theorem is asserted.

## Theorem P — State-map/clock mismatch is an exact normal interface owner

Let `Pi_t:Y->X` be a time-dependent ancestry-to-physical state map, let

\[
L_Y=\partial_t+b_Y\cdot\nabla_y,
\qquad
L_X=\partial_t+b_X\cdot\nabla_x,
\]

and define

\[
R_\Pi=\partial_t\Pi+D\Pi\,b_Y-b_X\circ\Pi.
\]

For every physical scalar observable `chi_X`, with `chi_Y=chi_X o Pi`,

\[
\boxed{
L_Y\chi_Y-(L_X\chi_X)\circ\Pi
=\nabla\chi_X(\Pi)\cdot R_\Pi.
}
\]

For a hard moving cut `chi_X=1_{g<a}`, the mismatch is distributionally

\[
\boxed{
-\delta_{g(\Pi)=a}\,\nabla g(\Pi)\cdot R_\Pi.
}
\]

Thus only the interface-normal component of the clock/state-map residual is physical crossing; tangential mismatch is reparameterization.  A frozen first-bad ancestry selector therefore need not be a frozen physical selector unless this normal residual vanishes.  Selector descent, clock intertwining, and fixed-mass cancellation are three distinct steps.

## Theorem Q — Common incompressible Cauchy deformation cannot rotate cubic phase

For one real stochastic Cauchy deformation `D` acting on all three complex legs,

\[
\det D=1
\]

and

\[
\boxed{
\overline{Dz_0}\cdot(Dz_1\times Dz_2)
=
\overline{z_0}\cdot(z_1\times z_2).
}
\]

Equivalently, a common real generator contributes only `(tr G)Z`; for incompressible common deformation this vanishes.  If the three legs have generators `G_i`, then after subtracting any common reference `G`, the cubic derivative contains only the relative generators `G_i-G` and explicit forcing terms.

Therefore severe same-replica Cauchy metric stretching can coexist with exactly fixed cubic phase.  Continuous phase rotation in the Kelvin bridge must come from relative replica/current realization, moving-cut or state-map/clock mismatch, viscosity/forcing, or a separately typed jump.  Martingale q.v. and centered covariance remain second-order and are not substitutes for this oriented cubic owner.

## Theorem R — Kernel selector purity is exactly same-ancestor pair agreement

Let `kappa_y(dY)` be a conditional lift from a reduced Kelvin ancestry state to full physical current-shape states, and let `chi_A` be a hard physical selector.  Define

\[
\alpha(y)=\int\chi_A(Y)\,\kappa_y(dY).
\]

Then

\[
\boxed{
\alpha(1-\alpha)
=
\frac12\iint[\chi_A(Y_1)-\chi_A(Y_2)]^2
\,\kappa_y(dY_1)\kappa_y(dY_2).
}
\]

A hard reduced selector exists iff this quantity vanishes, equivalently iff `chi_A` is constant `kappa_y`-almost surely.  Thus the existing same-ancestor pair process exactly detects whether a reduced ancestry label resolves the physical side of a selected interface.  If the kernel intertwining defect `D_R=partial_t R+L_yR-RL_Y` is nonzero, it is a separate state-resolution/generator owner.  The earlier deterministic state-map theorem is only the Dirac-kernel branch; for an Itô map one must also match the pushed diffusion tensor before the remaining hard-interface defect reduces to a normal drift face.

## Theorem S — Physical same-state cubic differs from independent-replica cubic by an exact third-order resolution object

For three complex full-state interaction legs `Phi_i(Y)` and the oriented trilinear form

\[
\mathcal T(z_0,z_1,z_2)=\overline z_0\cdot(z_1\times z_2),
\]

let `m_i=R Phi_i`.  Then

\[
\overline{\mathcal Z}=R\mathcal T(\Phi_0,\Phi_1,\Phi_2)
\]

is the same-hidden-state physical conditional cubic, while three conditionally independent replicas give exactly

\[
\mathcal Z_{ind}=\mathcal T(m_0,m_1,m_2).
\]

Writing `xi_i=Phi_i-m_i`,

\[
\boxed{
\begin{aligned}
\overline{\mathcal Z}-\mathcal Z_{ind}
={}&R\mathcal T(\xi_0,\xi_1,m_2)
+R\mathcal T(\xi_0,m_1,\xi_2)\\
&+R\mathcal T(m_0,\xi_1,\xi_2)
+R\mathcal T(\xi_0,\xi_1,\xi_2).
\end{aligned}
}
\]

The final centered third-order term is genuinely invisible to all first- and second-order data.  Even- versus odd-parity four-state kernels can have identical means and second moments but opposite signed cubic interaction.  Hence covariance/q.v. and independent variance replicas cannot determine physical signed phase without a same-state coupling theorem or an explicit third-order resolution object.

## Theorem T — Trilinear carré-du-champ is the exact stochastic cubic-resolution transfer law

For a diffusion generator `L`, define

\[
\Gamma_L^{(3)}[f_0,f_1,f_2]
=L\mathcal T(f_0,f_1,f_2)
-\sum_i\mathcal T(f_0,\ldots,Lf_i,\ldots,f_2).
\]

If `L=b.grad+(1/2)a^{alpha beta}partial_{alpha beta}`, this defect consists exactly of the three pair derivative contractions weighted by the remaining third leg.  If `H_y R=R H_Y`, `H=partial_tau-L`, and the full legs are homogeneous, then the cubic resolution object from Theorem S obeys

\[
\boxed{
H_y\Delta_3^{res}
=\Gamma_{L_y}^{(3)}[m_0,m_1,m_2]
-R\Gamma_{L_Y}^{(3)}[\Phi_0,\Phi_1,\Phi_2].
}
\]

With physical leg sources there is one additional exact source-resolution trilinear defect.  Thus stochastic q.v. can transfer cubic interaction only through an oriented pair-cross term carrying the third leg; it is not itself a replacement for cubic phase.  Common incompressible Cauchy finite-variation deformation remains phase-neutral, while kernel/interface defects, relative generators, trilinear diffusion transfer, explicit source correlations, and finite typed resets remain distinct owners.

## Theorem U — Universal cubic interaction sufficiency forces the conditional kernel to be Dirac

Let `kappa_y` be a conditional probability kernel on a standard-Borel full physical Kelvin state space.  If for every bounded measurable complex-vector triple

\[
R\mathcal T(\Phi_0,\Phi_1,\Phi_2)
=\mathcal T(R\Phi_0,R\Phi_1,R\Phi_2),
\qquad
\mathcal T(z_0,z_1,z_2)=\overline z_0\cdot(z_1\times z_2),
\]

then `kappa_y` is a Dirac mass.  Indeed fixed basis vectors reduce the hypothesis to `R(conj(f)gh)=conj(Rf)(Rg)(Rh)` for all bounded scalar observables; setting `h=1` and `g=f` forces zero conditional variance for every indicator, hence a `0-1` probability measure and therefore a point mass on a standard-Borel space.  The converse is immediate.

Consequently hard support purity and even complete second-order information are strictly weaker than cubic phase sufficiency.  A nontrivial reduced Kelvin state must either be sufficient only for a restricted physical interaction algebra or explicitly carry the third-order resolution object `Delta_3^res`; covariance alone cannot provide universal signed-phase closure.

## Theorem V — Common stochastic Cauchy averaging creates only an exterior-volume amplitude defect

Let `D` be a real random Cauchy deformation with `det D=1` pathwise and let `Dbar=E D`.  For fixed complex terminal vectors and `T(z0,z1,z2)=conj(z0).(z1 cross z2)`, a same-replica interaction satisfies

\[
\boxed{E\,T(Dz_0,Dz_1,Dz_2)=T(z_0,z_1,z_2).}
\]

Three conditionally independent replica means instead give

\[
\boxed{T(Dbar z_0,Dbar z_1,Dbar z_2)=\det(Dbar)T(z_0,z_1,z_2).}
\]

Hence the exact resolution defect is `(1-det Dbar) Z_0`.  Since `det Dbar` is real, while it remains positive this is purely radial amplitude resolution and carries zero continuous interaction-phase velocity.  Any sign flip must pass through zero independent-replica cubic amplitude first.

## Theorem W — The mean-Cauchy determinant is driven by a signed trilinear contraction of the deformation carré-du-champ

For the current Kelvin reverse-age connected law

\[
\mathcal H_h\bar D=A^T\bar D,
\qquad
\Gamma_D^{vec}=2\nu\sum_\mu vec(\partial_\mu\bar D)vec(\partial_\mu\bar D)^T,
\]

incompressibility gives, with `J_D=det Dbar`,

\[
\boxed{
\mathcal H_hJ_D
=-\frac12\nabla^2_{vec D}\det(\bar D):\Gamma_D^{vec}.
}
\]

Equivalently this is `-2nu` times the sum of the three pair-column derivative determinants.  Therefore `delta_D=1-J_D` obeys the same law with opposite sign.  At a smooth current point,

\[
\boxed{
\delta_D(h)
=-\frac{\nu h^3}{3}\sum_\mu\operatorname{tr}((\partial_\mu\nabla u)^2)+O(h^4).
}
\]

The source is signed even though `Gamma_D^vec` is PSD.  For the exact periodic NS eigenstreamfunction `psi=e^{-5nu t}[cos(x+2y)+a cos(2x+y)]`, at `x=y=pi/6` one has `sum tr((partial_mu A)^2)=-72 a e^{-10nu t}`, hence `delta_D=24 nu a e^{-10nu t}h^3+O(h^4)`.

## Theorem X — Deformation covariance and interaction phase are non-equivalent owners

The exact periodic one-mode NS shear in the Kelvin Cauchy audit has

\[
D_h=I+c_hE_{21},
\qquad
\Sigma_D>0
\]

at the symmetry anchor for every positive horizon, while

\[
\boxed{\det\bar D=1.}
\]

Thus `C_D^Gram>0` and the mean stochastic packet metric differs from the deterministic/mean-deformation metric, but every fixed-terminal same-replica and independent-mean cubic agrees exactly.  Nonzero deformation covariance or metric mismatch therefore does not imply cubic amplitude loss or phase rotation.  Common real deformation dispersion must be quotiented before relative terminal/role, interface, forcing, or third-order resolution mechanisms are charged as phase owners.

## Theorem Y — Full Cauchy cubic resolution has exactly three hidden-state owners

Let `Y_i=D w_i` with one common real random `D in SL(3)` and arbitrary correlated complex terminal vectors `w_i`.  Then pathwise

\[
\boxed{T(Dw_0,Dw_1,Dw_2)=T(w_0,w_1,w_2).}
\]

With `Dbar=E D`, `wbar_i=E w_i`, define

\[
r_i=E[(D-Dbar)(w_i-wbar_i)],
\qquad
m_i=E Y_i=Dbar\,wbar_i+r_i.
\]

If `Delta_w=E T(w_0,w_1,w_2)-T(wbar_0,wbar_1,wbar_2)` and `C_Dw` is the exact seven-term trilinear expansion containing at least one `r_i`, then

\[
\boxed{
Z_{same}-Z_{ind}
=(1-\det Dbar)T(wbar_0,wbar_1,wbar_2)
+\Delta_w-C_{Dw}.
}
\]

Thus after common deformation is quotiented, hidden-state continuous phase rotation can enter through terminal/role cubic resolution or deformation--terminal correlation.  The pure exterior-volume defect is radial while `det Dbar>0`.

## Theorem Z — Same-state physical selection commutes with common Cauchy top-volume cancellation

For any real scalar physical event/localization weight `chi` on the same hidden state,

\[
\boxed{
E[\chi\,T(Dw_0,Dw_1,Dw_2)]
=E[\chi\,T(w_0,w_1,w_2)].
}
\]

The same holds under the normalized selected law whenever `E chi>0`.  Therefore a legitimate first-bad or event selector can reweight terminal/role resolution and mixed correlations, but cannot by itself turn common incompressible Cauchy deformation or packet-metric dispersion into a same-replica phase source.  Selected metric alignment and selected cubic-phase alignment are distinct bridge requirements.

## Theorem AA — The Cauchy transpose is a full-vorticity connection gauge, not a cubic phase source

For `A=grad u` and physical vorticity `omega=curl u`,

\[
\boxed{A-A^T=[\omega]_\times,
\qquad
(A-A^T)\omega=0.}
\]

Hence full vorticity satisfies `L_nu omega=A omega=A^T omega`.  For a localized role `Q omega`, the exact source ledgers using `A` and `A^T` differ by `[omega]_x Q omega`.  This is a common real trace-free skew connection, and for three oriented cubic legs its contributions telescope exactly to zero by the `Lambda^3` trace law.  A transpose switch becomes an apparent phase source only if the compensating localization commutator is omitted.

## Theorem AB — Mixed deformation--terminal correlation has a literal connected diffusion source

For a homogeneous fixed-past terminal vector observable under the reverse-anchor Cauchy semigroup, let

\[
\mathcal H_h\bar D=A^T\bar D,
\qquad
\mathcal H_h\bar w_i=0,
\qquad
\mathcal H_hm_i=A^Tm_i,
\]

and `r_i=m_i-Dbar wbar_i`.  Then exactly

\[
\boxed{
\mathcal H_hr_i
=A^Tr_i
+2\nu\sum_\mu
(\partial_\mu\bar D)(\partial_\mu\bar w_i).
}
\]

Consequently

\[
\boxed{
r_i(h)
=\nu h^2\sum_\mu
(\partial_\mu\nabla u)^T\partial_\mu w_i
+O(h^3).
}
\]

The source is complex and phase-capable; it is neither `Sigma_D` nor an interface/forcing source.  Physical localized roles add those explicit sources separately.

## Theorem AC — Fixed-past Cauchy hidden-state resolution has an h, h^2, h^3 causal onset hierarchy

For smooth deterministic terminal vector fields under the reverse anchor semigroup, the terminal cubic resolution `Delta_w=P_h T(w_0,w_1,w_2)-T(P_hw_0,P_hw_1,P_hw_2)` obeys the exact trilinear carré-du-champ law

\[
\mathcal H_h\Delta_w
=2\nu\sum_\mu
\big[T(\partial_\mu\bar w_0,\partial_\mu\bar w_1,\bar w_2)
+T(\partial_\mu\bar w_0,\bar w_1,\partial_\mu\bar w_2)
+T(\bar w_0,\partial_\mu\bar w_1,\partial_\mu\bar w_2)\big].
\]

Thus, when the respective leading coefficients do not vanish,

\[
\boxed{
\Delta_w=O(\nu h),
\qquad
r_i=O(\nu h^2),
\qquad
1-\det\bar D=O(\nu h^3).
}
\]

The first two sectors can rotate phase; the pure common-deformation exterior-volume sector is radial while `det Dbar>0`.  The hierarchy is local causal ordering, not a recurrence or regularity estimate.

## Theorem AD — A hard first-bad Boolean on reduced ancestry state exists iff the full physical event is kernel-pure

Let `kappa_y` lift a reduced ancestry state to full physical Kelvin states and let `B_i` be a full-state physical bad set with occupancy `beta_i=kappa_y(B_i)`.  Then a deterministic reduced Boolean `bad_flags[i]` represents the physical event exactly iff

\[
\boxed{\beta_i\in\{0,1\}.}
\]

Equivalently,

\[
\boxed{
\beta_i(1-\beta_i)
=\frac12E[(1_{B_i}(Y_1)-1_{B_i}(Y_2))^2\mid y]
=0.
}
\]

The physical resolve event has an independent identical criterion.  If an occupancy lies strictly between zero and one, replacing it by a Boolean necessarily misclassifies positive conditional mass; replacing the hard selector by the occupancy would be a different architecture.  Any full bad/resolve set must additionally be invariant under exact representation gauges before it can be called a physical Navier--Stokes event.

## Theorem AE — First-bad entry/resolve carries an exact finite complex interaction face

Let `chi^-` and `chi^+` be the legitimate scalar event weights immediately before and after a selector event and let `Z(Y)` be the same-state complex interaction.  Then

\[
\boxed{Z^+-Z^-=E[(\chi^+-\chi^-)Z].}
\]

If `alpha^\pm=E chi^\pm>0` and `Zhat^\pm=Z^\pm/alpha^\pm`, then

\[
\boxed{
Zhat^+-Zhat^-
=\frac{E[(\chi^+-\chi^-)(Z-Zhat^-)]}{\alpha^+}.
}
\]

Thus reset phase/amplitude changes are finite selection-reweighting data, not smooth phase-action density.  For a common Cauchy payoff `Z=T(Dw_0,Dw_1,Dw_2)` with `D in SL(3)`, the same jump equals the terminal jump with `D` removed pathwise.  No positive reset reservoir or termination conclusion follows from the identity.

## Theorem AF — Continuous PDE owners and finite selector events obey one hybrid no-free-escape law

Let `Z` be nonzero and absolutely continuous between finitely many typed event times, with exact continuous split `Zdot=sum_o Zdot_o` and nonzero one-sided event values `Z_j^\pm`.  Then

\[
\boxed{
\log\frac{|Z(T^-)|}{|Z(0^+)|}
=
\sum_o\sum_j\int
\operatorname{Re}\frac{\dot Z_o}{Z}\,dt
+
\sum_j\log\frac{|Z_j^+|}{|Z_j^-|}.
}
\]

A lifted phase satisfies the analogous exact identity with `Im(Zdot_o/Z)` and finite event angles.  Consequently, if `|Z|` falls to `rho|Z(0)|`, the sum of continuous owner amplitude actions plus absolute finite event log-amplitude jumps is at least `log(1/rho)`.  If `Re Z/|Z|` falls from at least `c_hi` to at most `c_lo`, the continuous owner phase path length plus finite event geodesic jumps is at least

\[
\boxed{\arccos(c_{lo})-\arccos(c_{hi}).}
\]

Otherwise, while a chosen physical work coefficient stays `kappa>=kappa_*>0`, the favorable work remains at least `kappa_* c_lo rho |Z(0)|`.  Geometry exit, a zero of `Z`, loss of physical selector/state-map semantics, or an unregistered post-event role remains a typed structural exit.  The theorem closes local bookkeeping across finitely many events but proves no global bound on event count, reset action, recurrence, or regularity.

## Theorem AG — Positive local peak enstrophy growth is directional material-metric work beating Kelvin q.v.

Let `e=|omega|^2/2`, `Phi=H^T omega`, and let the material metric satisfy `H Mdot H^T=2S`.  Then the exact Navier--Stokes enstrophy equation is

\[
\boxed{
D_t e
=\frac12\Phi^T\dot M\Phi
+\nu\Delta e
-\nu|\nabla\omega|^2
=\frac12\Phi^T\dot M\Phi
-\frac12\sum_j\gamma_{dens}(n_j)
+\nu\Delta e.
}
\]

Therefore at a spatial local maximum of enstrophy,

\[
D_t e>0
\Longrightarrow
\boxed{
\frac12\Phi^T\dot M\Phi
>\nu|\nabla\omega|^2
=\frac12\sum_j\gamma_{dens}(n_j).
}
\]

At fixed reference scale incompressibility keeps the material metric determinant constant, so the positive producer is anisotropic directional deformation rather than volume expansion.

## Theorem AH — A finite threshold on the local growth margin is not by itself a continuation-failure oracle in the smooth affine NS class

For the exact affine Navier--Stokes vortex-stretch solution

\[
A(t)=\begin{pmatrix}-a&-r(t)&0\\r(t)&-a&0\\0&0&2a\end{pmatrix},
\qquad r(t)=r_0e^{2at},
\]

with `a>0`, vorticity is spatially uniform, every point is a non-strict spatial local enstrophy maximum, and

\[
\boxed{
\mathfrak G
=\omega\cdot S\omega-\nu|\nabla\omega|^2
=8ar_0^2e^{4at}
=D_t e.
}
\]

For every finite threshold `Theta`, parameters can be chosen so `G>Theta` while the affine solution remains smooth at every finite time.  Thus such a threshold alone cannot be a universal continuation-failure event on any admissible class containing these affine flows.  The calibration does not exclude narrower periodic/finite-energy classes or strict/nondegenerate local-maximum hypotheses, and it does not define the missing first-bad event.

## Theorem AI — Local peak growth and finite-horizon Cauchy deformation covariance are non-equivalent NS mechanisms

Two exact smooth Navier--Stokes solutions separate the mechanisms in both directions.  In the affine vortex-stretch flow, `A` is spatially uniform, so conditional Cauchy deformation is deterministic and

\[
\boxed{\Sigma_D=C_D^{Gram}=0,}
\]

while

\[
\boxed{D_t e=8ar_0^2e^{4at}>0}
\]

at every non-strict spatial local enstrophy maximum.  Conversely, for the exact periodic one-mode shear at `y=pi/(2k)`,

\[
\boxed{D_t e=-\nu k^4e^{-2\nu k^2t}<0,}
\qquad
\omega\cdot S\omega=|\nabla\omega|^2=0,
\]

but for every backward horizon `h>0`, with `alpha=nu k^2`,

\[
\boxed{
\operatorname{Var}(c_h)
=k^2e^{-2\alpha t}
\left[\frac{\cosh(2\alpha h)-1}{2\alpha^2}-h^2\right]>0.
}
\]

Thus stochastic deformation covariance is neither necessary nor sufficient for positive local peak growth.  It measures finite-horizon Brownian-anchor sampling of spatially varying velocity gradient, whereas the local growth gate measures current vorticity-direction metric work against instantaneous Kelvin q.v. and curvature flux.

## Theorem AJ — Cauchy deformation covariance resolves into strain-gradient, Kelvin-q.v.-complement, and orientation-coupling sectors

Write `A=S+Omega`, `Omega=(1/2)[omega]_x`, and for each spatial direction let `P_mu=partial_mu S`, `Q_mu=(1/2)[partial_mu omega]_x`.  Then

\[
\boxed{
(\partial_\mu A)^T(\partial_\mu A)
=P_\mu^2-Q_\mu^2+(P_\mu Q_\mu-Q_\mu P_\mu).
}
\]

Consequently the `O(nu h^3)` Cauchy row-Gram covariance splits into PSD strain-gradient and rotation-gradient sectors plus a symmetric trace-free orientation-coupling sector.  If `Gamma_K=2nu(grad omega)(grad omega)^T` is the instantaneous Kelvin q.v. tensor, the rotation-gradient part is exactly

\[
\boxed{
C_\Omega(h)
=\frac{h^3}{12}\big[(\operatorname{tr}\Gamma_K)I-\Gamma_K\big]+O(h^4).
}
\]

Thus the vorticity-gradient contribution to finite-horizon deformation dispersion is the transverse tensor complement of the Kelvin q.v. directions, not the q.v. tensor itself.  More invariantly, under the three-dimensional Hodge identification `Lambda^2 R^3 ~= R^3`,

\[
\boxed{
C_\Omega(h)
=\frac{h^3}{12}\,*\,\Gamma_K^{[2]}\,*^{-1}+O(h^4),
}
\]

because the induced two-vector generator satisfies `* G^[2] *^-1=(tr G)I-G^T`.  The bridge is therefore an exact exterior-square representation law.

## Theorem AK — Mean Cauchy exterior-volume onset is vorticity-gradient minus strain-gradient work

At every smooth point,

\[
\boxed{
1-\det\bar D
=
\frac{\nu h^3}{6}|\nabla\omega|^2
-
\frac{\nu h^3}{3}|\nabla S|_F^2
+O(h^4)
=
\frac{h^3}{12}\operatorname{tr}\Gamma_K
-
\frac{\nu h^3}{3}|\nabla S|_F^2
+O(h^4).
}
\]

The signed determinant source is therefore a literal competition between spatial variation of local rotation and spatial variation of strain.  For the exact one-mode shear, `|grad omega|^2=2|grad S|_F^2`, so this onset vanishes; the stronger exact shear law has `det Dbar=1` for all horizons.  The symmetric trace-free strain/rotation cross sector, although absent from the determinant trace, is essential to the actual row-Gram covariance orientation.

## Theorem AL — The full vectorized Cauchy covariance has dual Gram projections that separate orientation coupling

For `Sigma_D=Cov(vec D)`, define the exact partial traces

\[
C_{row}=E[DD^T]-\bar D\bar D^T,
\qquad
C_{col}=E[D^TD]-\bar D^T\bar D.
\]

If `P_mu=partial_mu S` and `Q_mu=(1/2)[partial_mu omega]_x`, then

\[
\boxed{
\frac{C_{row}+C_{col}}2
=\frac{2\nu h^3}{3}\sum_\mu(P_\mu^2-Q_\mu^2)+O(h^4),
}
\]

while

\[
\boxed{
\frac{C_{row}-C_{col}}2
=\frac{2\nu h^3}{3}\sum_\mu(P_\mu Q_\mu-Q_\mu P_\mu)+O(h^4).
}
\]

Thus the even partial-trace sector contains PSD strain plus Hodge-lifted rotation dispersion, and the odd sector isolates the symmetric trace-free orientation coupling.  Subtracting `(h^3/12)[tr Gamma_K I-Gamma_K]` from the even sector recovers the leading strain-gradient square tensor.

## Theorem AM — Finite-horizon Cauchy trace plus mean exterior volume invert to instantaneous Kelvin q.v. and strain-gradient magnitudes

Let

\[
T_h=\operatorname{tr}C_{row},
\qquad
\delta_h=1-\det\bar D.
\]

Then at every smooth point,

\[
\boxed{
\operatorname{tr}\Gamma_K
=\lim_{h\downarrow0}\frac{3T_h+6\delta_h}{h^3},
}
\]

and

\[
\boxed{
\nu|\nabla S|_F^2
=\lim_{h\downarrow0}\frac{3T_h-6\delta_h}{4h^3}.
}
\]

Equivalently, `|grad omega|^2=lim[3T_h+6delta_h]/(2nu h^3)`.  Thus the positive trace of stochastic deformation spread and the signed top-exterior defect form a two-channel infinitesimal inverse dictionary: neither alone separates strain-gradient from vorticity-gradient physics, but together they do.

## Theorem AN — Kelvin q.v. propagates into stochastic Cauchy geometry through the exterior-power representation ladder

For a linear map `G` on `R^3`, let `G^[p]` denote its induced Lie-algebra action on `Lambda^p R^3`.  Under the Hodge identification of `Lambda^2 R^3` with `R^3`,

\[
R_1(G)=G,
\qquad
R_2(G)=*G^{[2]}*^{-1}=(\operatorname{tr}G)I-G^T,
\qquad
R_3(G)=\operatorname{tr}G.
\]

For the symmetric instantaneous Kelvin q.v. tensor `Gamma_K=2nu(grad omega)(grad omega)^T`, the Cauchy rotation-gradient sector satisfies

\[
\boxed{
C_\Omega(h)=\frac{h^3}{12}R_2(\Gamma_K)+O(h^4),
}
\]

while the vorticity-gradient contribution to the mean exterior-volume defect is

\[
\boxed{
\delta_\omega(h)=\frac{h^3}{12}R_3(\Gamma_K)+O(h^4).
}
\]

Thus the same physical q.v. tensor appears at exterior degrees one, two and three through its induced representations.  If `Gamma_K=lambda nn^T` is rank one, `R_2(Gamma_K)=lambda(I-nn^T)`: the two-plane Cauchy rotation dispersion is exactly the Hodge complement of the q.v. direction.  Strain-gradient and strain/rotation-coupling sectors remain separate owners.

## Theorem AO — Reduced Cauchy inverse formulas require explicit hidden-state covariance and top-exterior resolution faces

For a reduced/full lift kernel `R(y,dY)`, current Kelvin upstream `ceca144` gives the exact vector law `Sigma_D^red=R Sigma_D+Cov_R(vec Dbar)`.  Consequently both exact Gram projections split as

\[
C_{row}^{red}=R C_{row}+C_{row}^{res},
\qquad
C_{col}^{red}=R C_{col}+C_{col}^{res},
\]

and the mean top-exterior defect splits as

\[
\boxed{
\delta^{red}=R\delta+\delta_{\Lambda^3}^{res},
\qquad
\delta_{\Lambda^3}^{res}=R[\det\bar D]-\det(R\bar D).
}
\]

Hence, with `T_h^red=tr C_row^red`,

\[
\frac{3T_h^{red}\pm6\delta_h^{red}}{h^3}
=R\frac{3T_h\pm6\delta_h}{h^3}
+\frac{3T_h^{res}\pm6\delta_{\Lambda^3,h}^{res}}{h^3}.
\]

If hidden full states have different current traceless velocity gradients, the resolution covariance is generically `O(h^2)`, one order earlier than intrinsic same-clock Cauchy covariance.  Thus the full-state inverse formulas cannot be applied to reduced ancestry data without typing/removing the resolution face.

## Theorem AP — Pure hidden affine-state mixing can manufacture divergent false Kelvin-q.v. or strain-gradient inverse signals

Let a reduced state equally mix two exact smooth affine Navier--Stokes full states.  For the pair of pure strains `A_+=S`, `A_-=-S`, `S=diag(a,-a,0)`, every full state has `grad S=grad omega=Sigma_D=0`, but

\[
T_h^{red}=2\sinh^2(ah),
\qquad
\delta_h^{red}=-\sinh^2(ah),
\]

so the naive reduced strain inverse is `3sinh^2(ah)/h^3 ~ 3a^2/h`.  For the pair of opposite rigid rotations `A_+=Omega`, `A_-=-Omega`, every full state again has zero physical gradient currencies, but

\[
T_h^{red}=2\sin^2(ah),
\qquad
\delta_h^{red}=\sin^2(ah),
\]

so the naive reduced Kelvin-q.v. trace inverse is `12sin^2(ah)/h^3 ~ 12a^2/h`.  These are pure resolution artefacts, not physical diffusion or strain-gradient production.

## Theorem AQ — Wang cyclic single-charge routing is diagonal on the common interaction-phase fiber

Current Wang upstream `8d21df4` pushes the physical closed-triad donor/recipient measure through deterministic hard cells while preserving canonical negative donor and positive recipient work exactly once. For each underlying closed triad, Theorem M gives one common complex interaction `Z_triangle` for all three energy roots. Therefore, after adjoining the phase mark `theta_triangle=arg Z_triangle`, every donor/recipient atom satisfies

\[
\boxed{\theta_{donor}=\theta_{recipient}.}
\]

The phase-marked hard table is the pushforward of the same physical measure with `theta_triangle` carried unchanged; forgetting the mark recovers Wang's current table. Thus cyclic donor routing and coarse hard-cell self-loops change energy ownership/provenance but create no phase rotation, phase recurrence, event time, or scale progress.

The unmarked table does not determine phase: `R exp(i theta)` and `R exp(-i theta)` have the same real quadrature and therefore identical signed root works and identical donor tables but opposite phases. Thus the certified single-charge law is an energy-routing theorem, not a phase-reconstruction theorem.

## Theorem AR — Actual nonlinear energy routing is a transport-with-killing equation

Let `E_i=|u_i|^2/2` be modal kinetic energies, let `K_ij>=0` be the current physical donor/recipient transport table with row marginal `W_i^-` and column marginal `W_j^+`, and put `d_i=2nu|k_i|^2`.  Then the exact Navier--Stokes modal balance is

\[
\boxed{
\dot E_i=\sum_jK_{ji}-\sum_jK_{ij}-d_iE_i.
}
\]

If `E_i=0`, the nonlinear work pairing vanishes, so the entire nonnegative donor row `K_i*` vanishes.  Hence `r_ij=K_ij/E_i` for `E_i>0` and `0` otherwise is well defined and

\[
\boxed{
\dot E_i=\sum_jr_{ji}E_j-E_i\sum_jr_{ij}-d_iE_i.
}
\]

Thus, once the actual donor kernel is fixed, nonlinear NSE energy transfer has an exact time-inhomogeneous Markov disintegration and viscosity is the only killing term.  For every differentiable modal observable `f_i(t)`,

\[
\boxed{
\frac d{dt}\sum_if_iE_i
=\sum_i\dot f_iE_i
+\sum_{i,j}(f_j-f_i)K_{ij}
-\sum_id_if_iE_i.
}
\]

This is a representation theorem, not a claim that energy consists of microscopic particles and not a FIFO/LIFO inventory rule.

## Theorem AS — Future-heat conjugation produces an exact bounded parabolic transport coordinate

For a candidate terminal time `T`, let

\[
q_i^T(t)=e^{-2\nu|k_i|^2(T-t)},
\qquad
w_i^T=1-q_i^T.
\]

Then

\[
\mathscr H_T(t)=\sum_iq_i^TE_i
=\frac12\|e^{\nu(T-t)\Delta}u(t)\|_2^2
\]

obeys

\[
\boxed{
\dot{\mathscr H}_T
=\sum_{i,j}(q_j^T-q_i^T)K_{ij},
}
\]

because the heat-clock face cancels physical viscosity exactly.  Equivalently,

\[
\boxed{
\dot{\mathscr B}_T
=\sum_{i,j}(w_j^T-w_i^T)K_{ij}
-\sum_i2\nu|k_i|^2E_i,
\qquad
\mathscr B_T=\sum_iw_i^TE_i.
}
\]

If `a_i=2nu(T-t)|k_i|^2` lies in `[alpha,beta]` and an actual recipient satisfies `|k_j|>=lambda|k_i|`, `lambda>1`, then

\[
\boxed{
w_j^T-w_i^T
\ge
\min_{a\in[\alpha,\beta]}(e^{-a}-e^{-\lambda^2a})>0.
}
\]

Thus parabolic scale matching is exactly what turns physical forward scale progress into a nondegenerate bounded PDE currency.

## Theorem AT — A stopped parabolically forward energy lineage has a finite one-sided budget

Follow a selected energy subpopulation `m_i` with the exact rates `r_ij`, but absorb it at the first edge outside a typed continuation set `C_t`; viscosity kills it at rate `d_i`.  With `M=sum_i m_i`, physical killing `D_m=sum_i d_i m_i`, and exit rate `X`,

\[
\boxed{\dot M=-D_m-X.}
\]

For `B_m=sum_iw_i^Tm_i`,

\[
\boxed{
\dot B_m
=F_{prog}-D_m-X_w,
}
\]

where `F_prog=sum_C (w_j-w_i)m_i r_ij` and `X_w` is the `w`-weighted absorbing exit.  If every internal continuation edge has `w_j-w_i>=0`, exact mass conservation yields

\[
\boxed{
\int_s^tF_{prog}\,dr
\le
\sum_iq_i^T(s)m_i(s)
\le M(s).
}
\]

If moreover every continuation edge costs at least `c_*>0`, the expected number of continuation jumps of the normalized killed lineage is at most `1/c_*`.  Reverse/nonforward/reentry transitions are not allowed to cancel this scalar internally; they are typed absorbing exits.

## Theorem AU — Repeated forward scale jumps in a bounded parabolic corridor force linear viscous killing hazard

Along an alive lineage set

\[
a(t)=2\nu|k(t)|^2(T-t).
\]

Between jumps, `dot a=-2nu|k|^2`, exactly the viscous killing hazard density.  At a forward jump with `|k^+|>=lambda|k^-|` and `a^->=alpha>0`,

\[
\Delta a\ge(\lambda^2-1)\alpha=:c_{jump}.
\]

If the lineage remains below `a<=beta` and undergoes `n` such jumps, then

\[
\boxed{
\int2\nu|k(t)|^2dt
\ge nc_{jump}-\beta,
}
\]

so its viscous survival factor is at most

\[
\boxed{e^{\beta-nc_{jump}}.}
\]

Therefore total selected energy mass capable of reaching depth `n` through the same forward parabolic corridor is at most `M_0e^{\beta-nc_{jump}}`.

## Theorem AV — A scale-critical parabolic energy lineage has finite depth

Assume, for the same physical stopped lineage,

\[
\alpha\le2\nu(T-t)N_j^2\le\beta,
\qquad
1<\lambda\le\frac{N_{j+1}}{N_j}\le\Lambda,
\]

and every continuing event carries a same-lineage scale-critical energy floor

\[
N_jE_j\ge\eta>0.
\]

Then `N_n<=Lambda^nN_0`, so a depth-`n` event requires `E_n>=eta/(N_0Lambda^n)`, whereas Theorem AU gives `E_n<=M_0e^{beta-nc_jump}`.  If

\[
\boxed{c_{jump}=(\lambda^2-1)\alpha>\log\Lambda,}
\]

then depth is finite and obeys

\[
\boxed{
 n
\le
\frac{\log(M_0N_0/\eta)+\beta}
{c_{jump}-\log\Lambda}.
}
\]

For Wang's currently certified signed-good scale ratios `8/5 < N_child/N_parent < 5/3`, the denominator is positive whenever `alpha>(25/39)log(5/3)≈0.3274`.  This is a compatibility calculation only; the third repo has not proved that the actual first-bad state satisfies the required parabolic corridor or same-lineage energy floor.

## Theorem AW — The parabolic termination hypotheses are logically non-removable

The finite-depth mechanism fails in distinct ways if its physical hypotheses are dropped.  If the lower parabolic face is removed, `N_n=N_0lambda^n` and `T-t_n=C lambda^{-4n}` give infinite forward depth with summable killing hazard.  Reverse jumps can refund the heat coordinate instantaneously and avoid viscous payment.  Without an upper scale-ratio bound, `N_n` may grow faster than the exponential survival loss, so the scale-critical floor need not contradict it.  Without a same-lineage critical mass floor, a zero-mass exceptional branch remains possible.  Free re-entry/cloning restarts the finite survival budget.

Hence the next literal first-bad theorem has a sharp acceptance test: NSE must supply parabolic lower/upper faces, bounded one-sided scale progress, a same-lineage physical energy floor, and explicit ownership of reverse/reentry exits.  Until then AV is a conditional termination mechanism, not a recurrence or regularity theorem.

## Theorem AX — A stopped parabolic corridor cannot carry scale-critical energy to the terminal time when the lower face exceeds one half

Let `m_i` be a selected energy population with no incoming mass after typed exit, and suppose every alive state satisfies

\[
\alpha\le2\nu|k_i|^2(T-t)\le\beta.
\]

The exact killed-mass law gives

\[
\dot M\le-\frac{\alpha}{T-t}M,
\qquad
\boxed{
M(t)\le M(s)\left(\frac{T-t}{T-s}\right)^\alpha.}
\]

If every continuing event in the same selected population requires `NE_event>=eta`, the upper parabolic face implies

\[
E_{event}\ge\eta\sqrt{\frac{2\nu}{\beta}}(T-t)^{1/2}.
\]

Hence if `alpha>1/2`, such events cannot accumulate at `T`.  The exponent `1/2` is sharp for this comparison: at `alpha<1/2` the survival upper decays more slowly than the scale-critical event floor, so another physical currency would be required.

## Theorem AY — A bounded physical scale ratio makes the parabolic corridor a capture region

For `a=2nu N^2(T-t)`, continuous motion between events only decreases `a`, while a same-time scale jump gives `a^+=(N^+/N^-)^2a^-`.  If every continuing jump satisfies `N^+/N^-<=Lambda` and

\[
\beta>\Lambda^2\alpha,
\]

then any jump starting below `alpha` lands below `beta`.  Consequently every transition from `a<alpha` to `a>beta` must visit `[alpha,beta]`.  Without an upper physical scale-ratio theorem, one nonlocal ultraviolet jump can skip the corridor and must be typed as its own owner rather than treated as parabolic progress.

## Theorem AZ — A full-PDE own-scale continuation theorem would derive the first-bad parabolic lower face rather than assume it

Let `T` be a first candidate singular time.  Suppose a future literal NSE first-bad theorem proves that, absent already named exits, a bad/continuing event at scale `N` and time `t` extends the **full smooth NSE solution** for at least

\[
L_N=\frac{c_*}{\nu N^2}.
\]

Then first-singular-time semantics force `L_N<=T-t`; otherwise the solution would extend through `T`.  Therefore every genuine continuing first-bad state satisfies

\[
\boxed{2\nu N^2(T-t)\ge2c_*.}
\]

Thus the lower parabolic face would be a consequence of actual PDE lifespan, not an observer threshold.  Current Wang own-scale service is only carrier/shell-local, and current Kelvin `dc26c0c` only refines selected-current/deformation pair typing; neither is silently promoted to this full-solution continuation theorem.  Combined with AX/AY and AR--AV, this gives a short conditional termination skeleton, but literal first-bad semantics, the same-selected-energy floor, and repeated typed exit/re-entry assembly remain open.

## Theorem BA — Enstrophy record growth forces a uniform scale-critical shell on the active NSE state

Let `Y=||grad u||_2^2` and `Z=||Delta u||_2^2`.  The exact NSE enstrophy balance is

\[
\frac12Y'+\nu Z=\mathcal W_{ens},
\qquad
\mathcal W_{ens}=\langle \mathbb P(u\cdot\nabla u),\Delta u\rangle.
\]

For a standard dyadic LP decomposition define `B_(1/2)=sup_q lambda_q^(1/2)||P_q u||_2`.  Decomposing this already-identified physical work into low--high, high--low and comparable high--high interactions gives

\[
\boxed{|
\mathcal W_{ens}|
\le C_{LP}B_{1/2}Z.}
\]

Hence every nontrivial time with `Y'>=0` satisfies

\[
\boxed{
B_{1/2}\ge\nu/C_{LP},
}
\]

so at least one actual shell has

\[
\boxed{
\lambda_q\|P_qu\|_2^2
\ge\nu^2/C_{LP}^2.}
\]

A finite first singular time forces `Y` unbounded by the standard `H^1` restart estimate `Y'<=C nu^-3 Y^3`; first hitting times of increasing enstrophy records therefore provide such active critical shells arbitrarily close to the candidate singular time.  This is an active-event floor only, not a uniform floor on every structural ancestry root.

## Theorem BB — A materially reused low-strain catalyst has a geometric service half-life against an advancing scale

For one material reservoir, Kelvin kinematics gives `L^T k=const` and

\[
\frac d{dt}\log|k|=-\hat k^TS\hat k\le\|S\|_{op}.
\]

Thus over one generation with strain action `Sigma_j`, its scale satisfies `M_(j+1)/M_j<=exp(Sigma_j)`.  A low-band physical increment sampled at child scale `N` obeys

\[
\|\delta_ru_M\|_2\lesssim(M/N)\|u_M\|_2,
\qquad |r|\sim N^{-1},
\]

so its maximum squared scale-critical service per unit physical reservoir energy scales as `M^3/N^2`.  If child scales advance by `N_(j+1)/N_j>=lambda>1`, the same reservoir under `Sigma_j<=sigma` obeys

\[
\boxed{
\mathsf C_{j+1}^{max}/\mathsf C_j^{max}
\le e^{3\sigma}/\lambda^2.}
\]

When `e^(3sigma)<lambda^2`, one old low-strain reservoir has finite total future service capacity.  Infinite efficient catalyst reuse must therefore exit through high strain, material/spectral relink, fragmentation/replication, or service failure.  This is the catalyst-side complement to donor-energy viscous killing; the two currencies are not identified.

## Theorem BC — Global enstrophy production is exactly the first squared-frequency moment of the physical energy donor kernel

With `E_i=|u_i|^2/2`, `kappa_i=|k_i|^2`, and the exact donor table `K_ij`,

\[
\frac12\|\nabla u\|_2^2=\sum_i\kappa_iE_i.
\]

Therefore Theorem AR with the observable `f_i=kappa_i` gives

\[
\boxed{
\frac12\frac d{dt}\|\nabla u\|_2^2
+\nu\|\Delta u\|_2^2
=\sum_{i,j}(\kappa_j-\kappa_i)K_{ij}.}
\]

Writing the positive/negative squared-frequency transport moments as `F_kappa^+` and `F_kappa^-`, every enstrophy record-growth time satisfies

\[
\boxed{F_\kappa^+\ge\nu\|\Delta u\|_2^2+F_\kappa^-\ge\nu\|\Delta u\|_2^2.}
\]

Thus global enstrophy growth is literally kinetic energy transported upward in squared frequency strongly enough to beat both viscosity and simultaneous downward transfer.  For the terminal coordinate `a_i=2nu(T-t)kappa_i`, the same moment is `F_a=2nu(T-t)[Y'/2+nu Z]`.  On a bounded corridor `a_i<a_j<=beta`, future-heat progress satisfies `Delta w>=e^-beta Delta a`, so the corridor part of actual enstrophy-producing transport consumes the exact one-sided heat currency of AT.  Any unpaid record-growth transport must lie in subparabolic, superparabolic/nonlocal, or already typed exit sectors.

## Theorem BD — Future-heat survival and heat defect are the unique normalized parabolic energy coordinates with zero and unit physical killing

For `a_i=2nu|k_i|^2(T-t)` and any `C^1` scalar weight `f`,

\[
\boxed{
\frac d{dt}\sum_if(a_i)E_i
=
\sum_{i,j}[f(a_j)-f(a_i)]K_{ij}
-
\sum_i2\nu|k_i|^2[f(a_i)+f'(a_i)]E_i.}
\]

Requiring clock motion to cancel viscosity for every modal spectrum gives `f'+f=0`; with `f(0)=1`, uniquely `q=e^-a`.  Requiring clock plus viscosity to retain exactly the unweighted kinetic-energy killing gives `f'+f=1`; with `f(0)=0`, uniquely `w=1-e^-a`.

Thus the future-heat pair is forced by the NSE generator.  For a fixed scale ratio `lambda>1`, its unit-killing scale price is `Delta_lambda w=e^-a-e^(-lambda^2 a)`, which tends to zero both as `a->0` and `a->infinity` and is maximal at `a_*=2 log(lambda)/(lambda^2-1)`.  Therefore no exact bounded unit-killing energy currency can price multiplicative scale progress uniformly across all parabolic heights.  The matched corridor plus sub/superparabolic owner split is structurally forced rather than an arbitrary proof case split.

## Theorem BE — The parabolic corridor obeys an exact moving-cut energy Reynolds law

For `a_i=2nu|k_i|^2(T-t)` and the hard corridor selector `chi_i=1_{alpha<=a_i<=beta}`,

\[
\boxed{
\frac d{dt}\sum_i\chi_iE_i
=
\sum_{i,j}(\chi_j-\chi_i)K_{ij}
-
\sum_i2\nu|k_i|^2\chi_iE_i
+
\sum_i\dot\chi_iE_i.}
\]

The three faces are respectively actual nonlinear crossing, physical viscous killing, and the moving heat-clock face.  Since `dot a_i=-2nu|k_i|^2<0`, clock motion crosses `beta` only from superparabolic into the corridor and crosses `alpha` only from corridor into subparabolic.  Repeated subparabolic-to-corridor reentry therefore cannot be manufactured by the same clock; it requires nonlinear up-frequency transfer or a distinct relink/reselection owner.

## Theorem BF — One old stopped matched-corridor population is asymptotically incapable of carrying H1 blow-up

A finite first singular time satisfies the standard lower rate `Y(t)>=c_H nu^(3/2)(T-t)^(-1/2)`, obtained from `Y'<=C_H nu^-3Y^3`.  For a selected population initialized at `s`, stopped at every corridor exit and receiving no later incoming mass, Theorem AX gives `M_m(t)<=C(T-t)^alpha`.  If its alive states satisfy `a<=beta`, then its enstrophy contribution obeys

\[
Y_m(t)\le\frac\beta{\nu(T-t)}M_m(t)\le C(T-t)^{\alpha-1}.
\]

Hence for `alpha>1/2`, `Y_m/Y ->0` as `t->T`.  Thus a singularity cannot be carried by one old stopped corridor population; persistent corridor enstrophy requires arbitrarily late nonlinear/clock/relink input.  The one-way clock topology of BE means recurrent fresh corridor input ultimately reduces to actual nonlinear/relink ownership.

## Theorem BG — A physical hysteresis gap makes repeated parabolic reentry pay viscous killing hazard

Suppose a selected lineage exits below `a<=alpha_-` and can be re-admitted only at `a>=alpha_+`, with `alpha_+>alpha_-`.  Over one completed reentry cycle the exact path law is

\[
a_{end}-a_{start}=-\int2\nu|k|^2dt+\sum_j\Delta a_j.
\]

If all internal continuation jumps have `Delta a_j>=0`, then before the lineage returns to the lower face it must pay

\[
\boxed{
\int2\nu|k|^2dt\ge\alpha_+-\alpha_-.}
\]

After `n` clean hysteretic cycles its energy survival is at most `exp[-n(alpha_+-alpha_-)]`.  A negative-`Delta a` jump can shortcut this cost only by firing an actual reverse/down-frequency owner.  The theorem is conditional on a literal physical bad/resolve semantics supplying a nonzero hysteresis gap; current Kelvin's selector is hysteretic but its bad/resolve predicates remain open-literal.

## Theorem BH — Enstrophy and future-heat progress are two layer-cake readings of the same radial energy current

For radial mode sets `A_R={i:|k_i|^2<=R}`, define actual outward/inward donor currents

\[
\Phi_\uparrow(R)=\sum_{\kappa_i\le R<\kappa_j}K_{ij},
\qquad
\Phi_\downarrow(R)=\sum_{\kappa_j\le R<\kappa_i}K_{ij}.
\]

Current Wang mode-set continuity gives the exact radial stock law.  Layer cake then yields

\[
\boxed{
F_\kappa^+=\int_0^\infty\Phi_\uparrow(R)dR,
\qquad
F_\kappa^-=\int_0^\infty\Phi_\downarrow(R)dR,}
\]

hence

\[
\boxed{
\frac12Y'+\nu Z
=\int_0^\infty[\Phi_\uparrow-\Phi_\downarrow]dR.}
\]

For the unique future-heat defect `w=1-exp[-2nu(T-t)R]`, the same donor transport obeys

\[
\boxed{
\sum_{ij}(w_j-w_i)K_{ij}
=
\int_0^\infty2\nu(T-t)e^{-2\nu(T-t)R}
[\Phi_\uparrow(R)-\Phi_\downarrow(R)]dR.}
\]

Thus global enstrophy production and parabolic progress are not separate currencies: they are unweighted and heat-weighted readings of one actual radial kinetic-energy current.  This upgrades AR/BC from finite modal-table algebra to the native helical mode-set control-volume structure now certified upstream, without importing Wang recurrence architecture.

## Theorem BI — A nonlocal upward donor-energy jump requires a comparable high-frequency companion in the same physical triad

For a closed triad `k_d+k_c+k_r=0`, if an actual energy recipient obeys `|k_r|>=Lambda|k_d|` relative to one donor, then

\[
\boxed{|k_c|\ge(1-Lambda^{-1})|k_r|.}
\]

In particular, a same-time jump from `a_d<alpha` to `a_r>beta` has a third physical root satisfying

\[
\boxed{|k_c|>(1-\sqrt{alpha/beta})|k_r|.}
\]

Thus a corridor-skipping ultraviolet energy jump cannot create an isolated high scale from purely low-frequency content.  It requires contemporaneous comparable high-frequency ancestry: either an old/materially reused companion subject to catalyst/strain geometry, or a fresh/relinked/fragmented companion which is itself a typed owner.  The theorem supplies geometry, not an amplitude lower bound.

## Theorem BJ — Every enstrophy record has a highest PDE-critical shell, giving a non-oracular first-bad candidate

At a record-growth time BA gives `B_(1/2)>=nu/C_LP`.  Fix `0<theta<1` and set `A_*=theta nu/C_LP`.  Smoothness before the candidate singular time implies the set

\[
\{q:\lambda_q^{1/2}\|P_qu\|_2\ge A_*\}
\]

is nonempty and bounded above, hence has a highest shell `q_*`.  It obeys the fixed active-event floor `lambda_(q_*)||P_(q_*)u||_2^2>=A_*^2`, while every higher shell is critical-subthreshold.  The first later time a higher shell reaches `A_*` is therefore a PDE-derived higher-critical crossing event.  This constructs a rigorous spectral record-event selector without a free Boolean oracle, but promotion to the Kelvin first-bad selector still requires kernel purity, a physical resolve rule and material/current-state compatibility.

## Theorem BK — Radial high-tail stock has exponential viscous memory loss and critical shells require fresh upward funding

For the radial helical mode set `A_R={|k|>=R}`, current Wang mode-set continuity gives

\[
E_R'+D_R+\Phi_\downarrow(R)=\Phi_\uparrow(R),
\qquad
D_R\ge2\nu R^2E_R.
\]

Hence for every `L>0`,

\[
\boxed{
E_R(t)
\le e^{-2\nu R^2L}E_R(t-L)
+
\int_{t-L}^{t}e^{-2\nu R^2(t-s)}\Phi_\uparrow(R,s)\,ds.}
\]

If a hard shell `C_N subset A_(rho N)` obeys `N E_C_N(t)>=eta`, set

\[
L_N=
\frac{\log(2E_*N/\eta)}{2\nu\rho^2N^2}.
\]

Whenever `t>=L_N`,

\[
\boxed{
\int_{t-L_N}^{t}
e^{-2\nu\rho^2N^2(t-s)}\Phi_\uparrow(\rho N,s)\,ds
\ge\frac\eta{2N}.}
\]

Thus a late high-frequency critical shell is necessarily funded by recent actual upward radial energy current; old high-tail stock alone is exponentially erased. `L_N=O((log N)/(nu N^2))->0`.

## Theorem BL — A critical-subthreshold UV tail cannot self-generate record enstrophy against viscosity

For a fixed hard cutoff write `u=v+h`, `v=P_<=Q u`, `h=P_>Q u`. The exact high-tail enstrophy balance is

\[
\frac12\frac d{dt}\|\nabla h\|_2^2
+\nu\|\Delta h\|_2^2
=\mathcal W_{ext,Q}+\mathcal W_{hhh},
\]

where `W_hhh` is the pure tail self-interaction and `W_ext,Q` contains exactly the terms with at least one lower-frequency leg. The restricted Bony estimate gives

\[
|\mathcal W_{hhh}|
\le C_{tail}B_{1/2}(h)\|\Delta h\|_2^2.
\]

Choose the highest-active-shell fraction so that `C_tail A_*<=nu/4`. Since all strictly higher shells satisfy `B_(1/2)(h)<A_*`,

\[
|\mathcal W_{hhh}|\le\frac\nu4\|\Delta h\|_2^2.
\]

Therefore at every high-tail record-growth time,

\[
\boxed{
\mathcal W_{ext,Q}
\ge\frac{3\nu}{4}\|\Delta h\|_2^2.}
\]

Pure subcritical UV self-interaction is viscosity-absorbable; record growth must enter through lower-frequency incidence/boundary physics.

## Theorem BM — Subparabolic renewal is not an independent recurrence owner

At a first higher PDE-critical crossing, Theorem BK forces a definite recent upward radial-work lower on an `O((log N)/(nu N^2))` window. If no higher crossing occurs while the highest active scale stays bounded and total enstrophy grows without bound, the low part has bounded `H^1` content and the higher tail must have record-growth times; Theorem BL then forces a resolved external-incidence/boundary owner.

Thus every subparabolic critical renewal is physically rerouted into actual radial/edge work, resolved strain/interface/relink, source/material change, or nonlocal high-companion ancestry. Subparabolicity itself supplies no fourth recurrence mechanism. At the owner-reduction level the unresolved graph contracts from `S/U/R` to `U/R`; exhaustion of `U/R` and measurable global assembly remain open.

## Theorem BN — Every enstrophy record contains a radial boundary where net outward current beats half the high-tail viscous killing

Let `F(R)=Phi_up(R)-Phi_down(R)` be net outward nonlinear energy current and `G(R)=sum_(|k|>R)|k|^2E_k` the high-tail gradient stock. Exact radial layer cake gives

\[
\mathcal W_{ens}=\int_0^\infty2R F(R)\,dR,
\qquad
Z=\int_0^\infty2R G(R)\,dR.
\]

At every time with `Y'>=0`, the NSE enstrophy identity gives `W_ens>=nu Z`. Therefore at least one radius with nonzero tail stock satisfies

\[
\boxed{F(R)\ge\nu G(R)=\frac12D_R,}
\]

where `D_R=2nu G(R)` is the actual instantaneous viscous killing of the radial high set. The gate uses net rather than gross radial flow, so conservative up/down circulation cannot manufacture it. This is an exact PDE-facing record-current event; it is complementary to the highest-critical-shell amplitude selector and makes no regularity claim.

## Theorem BO — Low-strain old carrier memory is erased unless a positive HH/relink/source owner appears

For a smooth selected carrier `w=Au` supported on `|xi|>=c_-N`, the exact `Q^2` energy law after low--low exclusion and observer quotient has typed rows `W_HH`, physical skew relink `W_K`, symmetric strain `W_S`, source/interface `W_src`, and viscosity. On a branch with no positive HH/relink/source input,

\[
\frac d{dt}E_A
\le
[2\|S_V\|_{op,\infty}-2\nu c_-^2N^2]E_A,
\]

so

\[
\boxed{E_A(t)\le e^{2K_A[s,t]-2\nu c_-^2N^2(t-s)}E_A(s).}
\]

If `E_A(t)>=eta/N`, `E_A(s)<=E_*`, and one fixes a physical strain face `K_0` and `0<delta<1`, then a full interval of length

\[
\boxed{L_N=
\frac{2K_0+\log(E_*N/(\delta\eta))}
{2\nu c_-^2N^2}}
\]

cannot be simultaneously below `K_0` and free of positive HH/relink/source input. Thus a late critical carrier forces a named owner within `O((log N)/(nu N^2))`; no forward lifespan assumption is used.

## Theorem BP — The old high-companion seam reduces to fresh typed owner recurrence

Combining BK and BO with the current resolved-interface quotient, passive old high stock and low-strain companion service are not independent UV recurrence mechanisms. Resolved low--high incidence either traces same-event conservative donor/relink or fires symmetric strain; otherwise a late critical carrier requires genuine positive HH or typed source/material input. The unresolved graph therefore sharpens from `U/R` to `G/R`, where `G` is generic fresh HH/relink/source recurrence after passive memory has been removed. Pure high-strain and pure signed-good generated-HH tails remain separately finite; mixed/generic fresh-owner exhaustion and state descent remain open.

## Theorem BQ — Every radial record gate has a quantitative resolved/comparable/UV-skip owner

At a BN gate `Phi_up>=nu G`. Partition actual upward recipient edges by whether either of the two quadratic interaction parents lies below `R/4`. If that resolved branch carries at least half, use the physical hard split `V_R=P_(|k|<R/4)u`; its exact mixed operator is `L_(V_R)=mathsf K_R+mathsf S_R`, with skew-adjoint conservative redistribution and self-adjoint physical strain, so one gross positive row carries at least `nu G/4`. Otherwise both interaction parents are at least `R/4`. Splitting by recipient radius `4R` yields either comparable local work at least `nu G/4`, with all three mode scales in `[R/4,5R)` and ratio `<20`, or UV-skip work at least `nu G/4`; every skip atom has a closed-triad companion above `3R`.

## Theorem BR — Closed-triad energy transport is a signed-helical-frequency martingale split/merge and enstrophy is its variance ledger

For `x_i=s_i|k_i|`, the cyclic root works obey both `sum_i T_i=0` and `sum_i x_iT_i=0`. If one root is the unique donor with mass `Q` and two roots are recipients with probabilities `p_1,p_2`, then `x_d=p_1x_1+p_2x_2` and the triad nonlinear enstrophy work is `+Q p_1p_2(x_1-x_2)^2`. If two roots are donors with normalized weights `q_1,q_2` and one root is the recipient, then `x_r=q_1x_1+q_2x_2` and the enstrophy work is `-Qq_1q_2(x_1-x_2)^2`. Consequently

\[
\boxed{\frac12Y'+\nu Z=\mathcal V_{split}-\mathcal V_{merge},}
\]

with both variance ledgers nonnegative; every enstrophy record satisfies `V_split>=nu Z+V_merge`. For a binary split, canonical donor-kernel entropy obeys `Qh_2(p)>=2Qp(1-p)`; on a comparable triad with `|x_i|<5R`, `Qh_2(p)>=V_split/(50R^2)`.

## Theorem BS — Rooted recipient share times scale has no universal contraction

For any `L>1` and `0<delta<1`, take a strict homochiral triangle with magnitudes `(1,L,L+delta)` and the phase orientation `R_triangle>0`. The cyclic works have sign pattern `(-,+,-)`, so the middle-frequency root is the unique recipient and the low donor sends 100% of its canonical donor charge to it. Thus `p_(0->1)=1` while `|k_1|/|k_0|=L`, disproving every universal contraction `p lambda^alpha<1`, `alpha>0`. The explicit `(1,16,16.5)` family lies inside the BQ comparable `<20` window. Its full triad is a two-donor merge and hence enstrophy-destructive by BR; the no-go shows that the complete split/merge variance event, not a rooted edge scalar, is the correct object.

## Theorem BT — The full-state global enstrophy source graph has one positive nonlinear owner

For unforced NSE, BR is defined directly on the physical closed-triad/modal state and gives `Y'/2+nu Z=V_split-V_merge`. Thus one-donor signed-frequency split variance is the only positive global nonlinear enstrophy owner; two-donor merge variance and viscosity are sinks. Phase, strain, radial, interface and material decompositions refine the rate/provenance of this same law. Reduced/material state resolution remains an admissibility condition for auxiliary localized theorems but cannot add a new term to the full-state global ledger. The main physical recurrence problem is therefore split-variance rate/non-explosion versus merge destruction and viscous killing.

## Theorem BU — Convex spectral moments form an exact split/merge convex-order hierarchy

For every convex `phi` for which the relevant moment/work integrals are finite (or after justified truncation), a one-donor split contributes `Q[E_p phi(x_r)-phi(x_d)]>=0` while a two-donor merge contributes `Q[phi(x_r)-E_q phi(x_d)]<=0`, because energy and helicity conservation make the singleton signed frequency the barycenter of the two-point side. Globally, `M_phi'=J_split^phi-J_merge^phi-2nu sum |k|^2 phi(s|k|)E`. Affine `phi=1,x` have zero Jensen gap; `phi=x^2` is BR. If `phi''>=m` on the event interval, the split gap is at least `(m/2)Q Var(x)`.

## Theorem BV — The unique parabolic defect has its branching inflection exactly at `a=1/2`

For `tau=T-t` and `w_tau(x)=1-exp(-2nu tau x^2)`, `w_tau''(x)=4nu tau exp(-a)(1-2a)` with `a=2nu tau x^2`. Hence `w_tau` is convex for `a<1/2`, has zero curvature at `1/2`, and is locally concave beyond the half-face. If a one-donor split stays entirely in `a<=alpha<1/2`, its defect Jensen gap obeys

\[
Q[E_pw_\tau(x_r)-w_\tau(x_d)]
\ge
2\nu\tau e^{-\alpha}(1-2\alpha)\,\mathcal V_2.
\]

A merge has the opposite sign. The same half-face appears independently in the old-corridor `H^1` exclusion threshold; the alignment is exact but does not by itself terminate split/merge recurrence.

## Theorem BW — Every helical triad moment is one signed-frequency Vandermonde times one divided difference

For any scalar observable `phi` on the three signed frequencies,

\[
\boxed{\sum_i\phi(x_i)T_i
=-R_\triangle(x_0-x_1)(x_1-x_2)(x_2-x_0)\phi[x_0,x_1,x_2].}
\]

Thus enstrophy is the bare Vandermonde (`phi=x^2`, divided difference 1), energy/helicity vanish because affine divided differences vanish, and every convex moment has the same triad sign as enstrophy. If `|x_i|<=K`, `|(x0-x1)(x1-x2)(x2-x0)|<=2K^3`, with equality at `(-K,0,K)` up to permutation. Coincident signed frequencies are exactly enstrophy-neutral.

## Theorem BX — Every enstrophy record contains a rate-critical one-donor split scale

Assign split triads by `K_triangle=max_i|k_i|` to dyadic blocks `[N_q,2N_q)` and let `V_q` be split-variance work there; let `Z_q` be modal palinstrophy on the same shell. Since at a record `sum V_q>=nu sum Z_q`, some shell satisfies `V_q>=nu Z_q`. Every triangle at that scale is either two-high/one-low (`min<K/4`, the other two radii strictly above `3K/4`) or fully comparable (`all radii >=K/4`); one class carries at least `nu Z_q/2`. Because `Q Var(x)<=K^2Q<4N_q^2Q`, the owning class has actual donor-work rate

\[
\boxed{Q_q^{owner}\ge\frac{\nu Z_q}{8N_q^2}\ge\frac\nu8N_q^2E_q.}
\]

This localizes the unresolved rate problem to separated or comparable **one-donor split** work; two-donor merges never enter the positive gate.

## Theorem BY — Absolute helical critical mass has an exact opposite-helicity pair creation/annihilation ledger

For `x=s|k|` and modal energy `E`, the critical stock `C=sum |x|E` obeys

\[
\boxed{C'+2\nu\sum |x|^3E=2(P_{create}-P_{ann}).}
\]

Homochiral split/merge events contribute zero because `|x|` is affine on one sign half-line.  A heterochiral one-donor split creates pair charge `P_triangle=Q min(p_-|x_-|,p_+x_+)` and increases `C` by exactly `2P_triangle`; the reversed two-donor merge annihilates the same charge.  Thus opposite-helicity pair creation is the only nonlinear source of total absolute helical critical mass.

## Theorem BZ — Comparable homochiral scale progress leaks critical mass downward

For a same-sign split `0<a<b<c`, donor `b`, and `lambda=c/b`, the high-recipient critical-mass fraction is `rho=lambda(1-r)/(lambda-r)`, `r=a/b`.  On the fully comparable branch `a,b,c>=c/4`,

\[
\boxed{1-\rho\ge\tfrac14\log\lambda,\qquad \rho\le\lambda^{-1/4}.}
\]

Moreover if `V_triangle` is split variance and `L_triangle` is the low-recipient critical-mass leakage,

\[
\boxed{L_\triangle\ge V_\triangle/(4K).}
\]

A comparable homochiral split therefore cannot produce enstrophy and move a branch upward without simultaneous downward critical-mass compensation.

## Theorem CA — Comparable heterochiral high-branch gain equals opposite-helicity pair creation

In the normal form `-b<a<c`, donor `a`, define `P_triangle=Q b(c-a)/(b+c)`.  Then

\[
\boxed{Qp_hc=Qa+P_\triangle,\qquad Qp_ob=P_\triangle.}
\]

Thus every high same-helicity critical-mass gain is matched one-for-one by an opposite-helicity sibling.  For a fully comparable triad with maximum physical scale `K`,

\[
\boxed{V_\triangle/(16K)\le P_\triangle\le4V_\triangle/K.}
\]

## Theorem CB — Rate-critical comparable split work must pay a critical-mass compensation action

At a BX rate-critical shell, if the comparable split class owns at least half of `V_q`, then either homochiral comparable splits supply downward critical-mass leakage

\[
\boxed{L_q\ge \nu Z_q/(32N),}
\]

or heterochiral comparable splits supply opposite-helicity pair creation

\[
\boxed{P_q^{create}\ge \nu Z_q/(128N).}
\]

Both are on the native critical-mass viscous scale `nu N^3E_q`.  The comparable recurrence problem therefore reduces to downward critical-mass recycling versus opposite-helicity pair creation/annihilation; there is no untyped comparable self-reproduction owner.
