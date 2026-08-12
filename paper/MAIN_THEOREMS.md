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
