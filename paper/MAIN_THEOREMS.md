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

## Theorem CC — Finite opposite-helicity pair-creation action implies continuation

Let `C=sum |k|E`, `B=sum |k|^3E`, and `P_create` be the exact BY pair-creation rate.  If `P_T=int_0^T P_create dt<infinity`, then `C_*:=C(0)+2P_T` satisfies

\[
\sup_{t<T}C(t)\le C_*,
\qquad
2\nu\int_0^T Bdt\le C_*.
\]

The moment inequality `Y^2<=CB` gives

\[
\boxed{\int_0^T Y^2dt\le C_*^2/(2\nu)<\infty.}
\]

A late-stage enstrophy estimate yields `Y'<=C nu^-3 Y^3=(C nu^-3Y^2)Y`, so Gronwall bounds `Y` and the `H^1` solution restarts through `T`.  Therefore every finite first singular time necessarily has

\[
\boxed{\int_0^T P_{create}(t)dt=\infty.}
\]

## Theorem CD — Pair creation is the first radial moment of the physical energy current

For net radial kinetic-energy current `F(R)=Phi_up(R)-Phi_down(R)`, the truncated linear layer cake is exact.  Under finite first radial moment,

\[
\boxed{\int_0^\infty F(R)dR
=\int(|k_r|-|k_d|)d\mathcal M
=2(P_{create}-P_{ann}).}
\]

Thus the critical-mass pair ledger is the degree-one radial reading of the same physical donor current whose degree-two reading is enstrophy production.  Homochiral first radial moments cancel; heterochiral sign crossing is exactly the uncancelled critical radial moment.

## Theorem CE — Pair creation is quadratically suppressed by a low opposite-helicity recipient

For a heterochiral split in normal form `-b<a<c`,

\[
\boxed{P_\triangle=b(c-a)|R_\triangle|.}
\]

Strict triangle geometry gives `c-a<b`, hence `P_triangle<b^2|R_triangle|`.  Since `P_triangle=b T_o^+` for the opposite-helicity recipient and current Wang edge capacity gives `T_o^+<=4b|a_0a_1a_2|`,

\[
\boxed{P_\triangle\le4b^2|a_0a_1a_2|.}
\]

Therefore a separated event with a low opposite-helicity recipient carries a genuine two-power low-scale suppression.  The low-donor/high-pair geometry remains a separate branch.

## Theorem CF — Finite positive net critical radial action implies continuation

Let `J_1(t)=int_0^infinity[Phi_up(R,t)-Phi_down(R,t)]dR=2(P_create-P_ann)`.  The exact critical-stock ledger is `C'+2nu B=J_1`.  If

\[
A_1(T)=\int_0^T[J_1(t)]_+dt<\infty,
\]

then `sup C<=C(0)+A_1`, `2nu int B<=C(0)+A_1`, and `Y^2<=CB` gives `int Y^2<infinity`.  The late-stage enstrophy Gronwall argument continues the `H^1` solution.  Therefore every finite first singular time requires

\[
\boxed{\int_0^T[J_1(t)]_+dt=\infty.}
\]

This is sharper than CC because create/annihilate cycling cancels before the criterion is read.

## Theorem CG — Positive and negative helical critical stocks have the same nonlinear source

For `C_+=sum |k|E_(k,+)`, `C_-=sum |k|E_(k,-)` and `B_\pm=sum |k|^3E_(k,\pm)`, with `N=P_create-P_ann=J_1/2`, exact absolute-critical-mass and signed-helicity ledgers give

\[
\boxed{C_+'+2nu B_+=N,\qquad C_-'+2nu B_-=N.}
\]

Thus nonlinear pair production injects equal critical charge into both helicity sectors; homochiral traffic vanishes from each critical-sector source.  Signed helicity is the difference mode and has no nonlinear source.

## Theorem CH — Ordinary kinetic-energy dissipation cannot universally bound the final critical action

Under `R^3` Navier--Stokes scaling, `int[J_1]_+dt` is invariant while kinetic energy and integrated kinetic-energy dissipation scale like `lambda^-1`.  Therefore no scale-independent universal bound of the final critical action by the ordinary energy budget can hold over the scaling class.  Any closure must use critical heterochiral/radial/split-merge structure rather than a renamed energy norm.

## Theorem CI — Exact Waleffe geometry depletes every separated heterochiral pair-creation event

For the heterochiral normal form `-b<a<c`, Wang's exact coupling magnitude and common phase factor give

\[
\boxed{P_\triangle
\le\sqrt2\,\Delta(a,b,c)\frac{(c-a)(a+c-b)}{ac}|a_0a_1a_2|.}
\]

If the donor `a` is the low leg and `K=max(b,c)`, triangle geometry yields

\[
\boxed{P_\triangle\le\sqrt2\,aK|a_0a_1a_2|.}
\]

If the opposite-helicity recipient `b` is the low leg,

\[
\boxed{P_\triangle<\sqrt2\,b^2|a_0a_1a_2|.}
\]

Since `c>a`, these exhaust genuinely separated heterochiral pair creation.  Only the fully comparable branch lacks a small scale ratio.

## Theorem CJ — Fully comparable heterochiral pair creation has no hidden Waleffe small factor

The dilation-invariant pair-capacity coefficient is nonzero at fixed comparable geometry.  For `a=b=3K/4`, `c=K`,

\[
\boxed{\eta_{pair}=\sqrt{10}/24\approx0.131761569.}
\]

Hence no universal scale-decaying Waleffe factor suppresses the comparable heterochiral core.  Closure of the final critical action must use recurrence/cancellation/killing or another critical structure, not a missing single-triad geometric epsilon.

## Theorem CK — Exact Hadamard diamond geometry defeats topology-only termination

For orthogonal equal-length lattice modes `p_j,q_j`,

\[
\boxed{p_{j+1}=p_j+q_j,\qquad q_{j+1}=p_j-q_j}
\]

preserves orthogonality and multiplies both radii by `sqrt(2)`; after two steps both vectors double.  Assigning helicities `+` to `p_j` and `-` to `q_j`, reality supplies two fully comparable heterochiral triads producing the next `+/-` pair.  The static split has high energy fraction `2/(1+sqrt2)` and high critical-mass amplification

\[
\boxed{4-2\sqrt2>1.}
\]

while natural times `sum N_j^-2` are finite.  Therefore wavevector closure, helicity conservation, eventwise split fractions and parabolic time alone do not terminate a local heterochiral diamond.  Actual coupled NSE amplitude/phase dynamics remains essential.

## Theorem CL — Rate-critical comparable pair creation forces full-dimensional Fourier participation at fixed critical mass

For the already-typed comparable heterochiral owner,

\[
P_N^{cmp}\le(64/27)N^2\|c\|_1\|c\|_2^2.
\]

With `E_part=||c||_2^2` and `M_eff=||c||_1^2/||c||_2^2`, the CB lower gate gives

\[
\boxed{M_{eff}\ge\frac{729\,\nu^2N^2}{8192^2E_{part}}
=\frac{729\,\nu^2N^3}{8192^2\mu_{part}}.}
\]

Thus at fixed participating critical mass `mu_part=O(nu^2)`, a rate-critical ultraviolet event requires `M_eff` of order `N^3`.  Sparse finite-triad ladders cannot carry the record-rate owner asymptotically.

## Theorem CM — Sparse heterochiral ladders are topology adversaries, not rate-critical blow-up mechanisms

Any fixed-width ladder has bounded `M_eff`, while CL requires `M_eff~N^3` at fixed critical mass.  Therefore even a phase-compatible multigeneration Hadamard birth signal cannot by itself sustain the CB/CF critical rate at ultraviolet scales.  The remaining obstruction is dense coherent heterochiral pair production (or growth of critical mass beyond the fixed-crossing regime), not a sparse shell-model cascade.

## Theorem CN — Orthogonal equal-scale heterochiral Hadamard seeds collapse to an exact 2D3C polarization class

For `p perpendicular q`, `|p|=|q|=N`, helicities `p:+`, `q:-`, and normal `n=p_hat cross q_hat`, the exact Leray-projected sources at `p+q` and `p-q` are both parallel to `n`.  Hence each first child is linearly polarized and has equal-magnitude `+/-` helical projections.  The two generated siblings have zero mutual quadratic interaction because their velocities are normal to both planar wavevectors.

Moreover the full real seed is 2D3C: its horizontal streamfunction is monochromatic with `-Delta psi=N^2 psi`, so horizontal nonlinearity is pure pressure and `v(t)=exp(-nu N^2t)v(0)`; the normal component is a passive scalar.  Thus the static single-helicity Hadamard ladder does not compose into a 3D feedback cascade in actual NSE.

## Theorem CO — Fresh heterochiral child polarization is fixed exactly by parent scale imbalance

For opposite-helicity parents of radii `a,b` feeding child radius `c`, the two child-helicity source magnitudes satisfy

\[
\boxed{|F_\pm|=\frac{(a+b)\Delta}{\sqrt2abc}(c\pm(a-b))|AB|.}
\]

With `delta=(a-b)/c`,

\[
\boxed{\Pi_F=\frac{2\delta}{1+\delta^2},\qquad
r_{min}=\frac{(1-|\delta|)^2}{2(1+\delta^2)}.}
\]

Every nondegenerate fresh heterochiral child therefore contains both helicities; equal parent radii give exact linear polarization.  Pure-helicity birth occurs only at the degenerate triangle boundary where the Waleffe source vanishes.

## Theorem CP — Near-pure fresh helicity pays geometric coupling depletion

If the minority fresh-source energy fraction satisfies `r_min<=epsilon`, then `1-|delta|<=2 sqrt(epsilon)`.  Heron's formula forces the interaction area, and hence total fresh-source amplitude, to lose an `epsilon^(1/4)` geometric factor.  Thus fresh heterochiral renewal cannot be both arbitrarily helicity-pure and order-one nondegenerate in Waleffe coupling.

## Theorem CQ — Heterochiral pair creation contains true-upward supply and pure UV pair action is first-shell only

In normal form `-b<a<c`, pair creation contains the genuine radial atom `a->c`.  Applying current Wang `76e6ee9` read-only to that atom yields: deep direct upward supply has resolved-scale parent contact; pure-UV supply is confined to the first shell `M=2N` with comparable parents.  On that first-shell branch,

\[
\boxed{\frac N2dT_o^+<dP\le3N dT_o^+,}
\]

so the normalized pair-action and opposite-helicity positive child-work laws have RN density in `[1/6,6]`.  The CB rate gate implies

\[
\boxed{T_{o,q}^+\ge\nu Z_q/(384N^2)\ge(\nu/384)N^2E_q.}
\]

Thus the only pure-UV final core is first-shell, comparable, heterochiral, true-upward, and already carried by actual positive child-energy work.

## Theorem CR — Fixed-critical rate production forces a positive action sublaw of uniformly efficient mixed-polarization edges

Assume one comparable block satisfies `||c||_1<=sqrt(V_0N^3)||c||_2` and participating critical mass `mu=NE<=M_0nu^2`.  With the physical helical capacity `dA_e=4sqrt(2)N^2|a_0a_1a_2|`, the CB rate gate implies

\[
\boxed{P/A\ge\rho_0:=27/(8192\sqrt{V_0M_0}).}
\]

Therefore edges with `dP/dA>=rho_0/2` carry at least half of actual pair action.  Every such edge has `eta_pair>=(2sqrt2/27)rho_0`, hence `1-delta^2>=rho_0^2/2916`; by CO its fresh-source minority-helicity fraction obeys

\[
\boxed{r_{min}\ge\rho_0^4/136048896.}
\]

Thus a fixed-mass rate-critical core contains a positive actual-action sublaw that is simultaneously work-efficient, geometrically nondegenerate, and fresh-polarization mixed.  Temporal ancestry/fresh-source dominance remains separate.

## Theorem CS — Donor-anchored plateau transport binds every genuinely deep pair edge to actual resolved mixed work

For donor dyadic scale `N/2<a<=N` and high recipient shell `M/2<c<=M`, choose a repo-3 smooth multiplier equal to one on `B_(M/8)` and supported in `B_(M/4)`.  If `M>=8N`, the donor is exactly resolved (`h_a=0`) and `B(V,V)` cannot reach the child shell `>M/2`; the edge source is therefore exactly in `B(V,h)+B(h,V)`.  Its positive energy work routes through the adjoint split `K_V+S_V` into same-time conservative skew redistribution or resolved strain/deformation.

If `M<8N`, then

\[
\boxed{c/a<16.}
\]

Thus there is no arbitrarily nonlocal untyped pair-creation branch: deep events bind to actual resolved mixed work, while the remainder has bounded donor/recipient scale ratio.

## Theorem CT — Universal heterochiral pair-capacity coefficient is at most `4sqrt(2)/27`

For every strict heterochiral pair-creation triangle,

\[
\boxed{\eta_{pair}\le4\sqrt2/27.}
\]

The proof splits `K=max(b,c)`: when `K=c`, area `<=ab/2` and the triangle interval reduce the maximum to the one-variable boundary value at `a/c=1/3`; when `K=b`, area `<=ac/2` gives the stronger `sqrt2/8` bound.  Consequently

\[
\boxed{P_N^{cmp}\le(64/27)N^2\|c\|_1\|c\|_2^2,}
\]

strengthening CL/CR.  In CR the fixed-critical mean-efficiency constant becomes `rho_0=27/(8192 sqrt(V_0M_0))`.

## Theorem CU — A late critical high-frequency shell has a definite recent nonlinear Duhamel amplitude

For `u_R=P_(|k|>=R)u`, the exact mild equation gives `u_R(t)=exp(nu L Delta)u_R(t-L)+G_R`.  If a terminal shell satisfies `N||P_Cu(t)||_2^2>=eta`, choose

\[
L_N^{amp}=\frac1{\nu R^2}\log\left(4\sqrt{E_*N/\eta}\right).
\]

Then the old heat-surviving vector has norm at most `(1/4)sqrt(eta/N)` and

\[
\boxed{\|G_R\|_2\ge(3/4)\sqrt{\eta/N}.}
\]

Thus late critical state is not only fresh in radial energy flux (BK) but has a definite recent nonlinear source-generated amplitude.  Applying CO to that state still requires a type-correct source-owner/cancellation disintegration.

## Theorem CV — Edgewise mixed heterochiral birth does not descend to mixed child state without spin-2 coherence control

Fix a child axis and rotate one strict heterochiral parent pair around it by `phi`.  After multiplying the parent-product phase by `exp(i phi)` so the `+` child source is aligned, rotational covariance gives

\[
\boxed{f_+(\phi)=f_+(0),\qquad f_-(\phi)=e^{2i\phi}f_-(0).}
\]

Thus two equally efficient positive-work atoms at `phi=0,pi/2` have `f_+^tot=2f_+(0)` but `f_-^tot=0`, despite CO giving nonzero minority birth on each atom.  For a rotated orbit the aggregate minority is controlled by the second angular harmonic `Q_2=E[e^{2i phi}]`.  Therefore CR/CO require an additional spin-2 source-coherence/cancellation theorem before yielding mixed child state.  CF's global pair-action criterion is unaffected.

## Theorem CW — The resolved linearized NSE has an explicit connection/metric Cartan split

For every smooth divergence-free resolved transporter `V`,
\[
\mathcal L_V=\mathbb P(V\cdot\nabla+\nabla V)
=\mathcal K_V+\mathcal S_V,
\]
with
\[
\boxed{\mathcal K_V=\mathbb P(V\cdot\nabla+\Omega_V),\qquad
\mathcal S_V=\mathbb P(S_V\,\cdot),}
\]
`K_V^*=-K_V` and `S_V^*=S_V`.  Thus the symmetric Wang owner is the literal resolved strain tensor; the skew owner is resolved transport/rotation modulo Leray gauge.

## Theorem CX — Wang symmetric resolved work is exactly resolved material-metric velocity

For the resolved flow deformation `F_V`, `H_V=F_V^{-T}`, `M_V=F_V^TF_V`,
\[
H_V\dot M_VH_V^T=2S_V.
\]
Hence for divergence-free probes
\[
\boxed{\langle f,\mathcal S_Vg\rangle
=\frac12\int(H_V^Tf)^T\dot M_V(H_V^Tg)\,dx.}
\]
This is an equality of physical geometry, not an analogy or estimate.

## Theorem CY — Complete event roles see a skew 2-form and one symmetric metric-velocity form

For any complete orthogonal role family `w_a`, the matrices
\[
K_{ab}=\langle w_a,\mathcal K_Vw_b\rangle,
\qquad S_{ab}=\langle w_a,\mathcal S_Vw_b\rangle
\]
obey `K^T=-K`, `S^T=S`.  Under any orthogonal role-coordinate change `O`,
\[
\boxed{K\mapsto O^TKO,\qquad S\mapsto O^TSO.}
\]
The entire symmetric role matrix is the coordinate matrix of the material metric-velocity bilinear form.  Interface versus diagonal strain is representation; the strain tensor is physical.

## Theorem CZ — Wang and Kelvin share the symmetric tensor but not an identical skew connection

For `A=S+Omega`, vector and transpose-dual material/covector generators have the same symmetric part and opposite skew parts:
\[
\boxed{A-A^T=[\omega]_\times,\qquad \operatorname{sym}A=\operatorname{sym}A^T=S.}
\]
Therefore Wang `S` identifies exactly with Kelvin metric strain, while Wang `K` may not be silently identified with a Kelvin connection without the correct transpose/clock/localization map.

## Theorem DA — Kelvin reconstructed residual drift splits exactly into resolved strain, unresolved strain, and q.v.

Using current Kelvin's exact law and any typed split `u=V+h`,
\[
\boxed{
\frac d{d\sigma}\frac12|r|^2\Big|_{drift}
=-r\cdot S_Vr-r\cdot S_hr+\nu\|\widehat Q\|_F^2.}
\]
The scalar cross dyad satisfies
\[
\boxed{
\frac d{d\sigma}(\omega\cdot r)\Big|_{drift}
=-2\omega\cdot S_Vr-2\omega\cdot S_hr+\operatorname{tr}\Gamma_{\omega r}.}
\]
Thus Kelvin and Wang probe the same local symmetric bilinear form `a.S_V b`, but they do not share a scalar currency.

## Theorem DB — Resolved material metric velocity and full physical Kelvin metric velocity are non-equivalent

Exact periodic Navier--Stokes shears provide both directions of the no-go.  A high-only shear can have `S_V=0` while `S_u!=0`; a low+high exact shear can be tuned at one point/time so `S_u=0` while `S_V!=0` and `S_h=-S_V`.  Hence only
\[
\boxed{S_u=S_V+S_h}
\]
is a valid full/resolved bridge.

## Theorem DC — Spectral cutoff repartition preserves Cartan owner types exactly

For every real scalar Fourier split `u=V+h`,
\[
\boxed{S_u=S_V+S_h,\qquad \Omega_u=\Omega_V+\Omega_h,}
\]
and the linearized operators satisfy
\[
\boxed{\mathcal K_u=\mathcal K_V+\mathcal K_h,\qquad
\mathcal S_u=\mathcal S_V+\mathcal S_h.}
\]
Changing cutoff from `R_0` to `R_1` transfers equal and opposite skew/symmetric tensors between resolved and unresolved sectors.  It creates no third interface owner.

## Theorem DD — Full Kelvin metric velocity is invariant under resolved/unresolved repartition

After conjugating each analysis metric velocity to Eulerian tensor space,
\[
\boxed{
H_u\dot M_uH_u^T
=H_V\dot M_VH_V^T+H_h\dot M_hH_h^T
=2S_u.}
\]
Raw metric histories are not identified; the equality is the instantaneous physical strain tensor identity.

## Theorem DE — Moving resolution has an unavoidable metric-velocity time face after differentiation

For `V=R(t,D)u`,
\[
S_V=RS_u,
\qquad
\boxed{\partial_tS_V=\dot R\,S_u+R\partial_tS_u.}
\]
A finite reset has `Delta S_V=(R^+-R^-)S_u` while full `S_u` remains unchanged at a continuous physical state.

## Theorem DF — Resolved objective strain differs from filtered full objective strain by four typed faces

With `h=u-V`,
\[
\boxed{
\mathring S_V-R\mathring S_u
=\dot R S_u+[V\cdot\nabla,R]S_u-R(h\cdot\nabla S_u)+\mathcal R_{rot},}
\]
where
\[
\mathcal R_{rot}=(RS_u)(R\Omega_u)-(R\Omega_u)(RS_u)-R(S_u\Omega_u-\Omega_uS_u).
\]
These are respectively moving-cut, filter-interface, unresolved-incidence and rotation-filter faces.  The same identity is the material metric-acceleration mismatch through the exact metric-acceleration formula.

## Theorem DG — Actual HH child work is a Cartan row sum

For a divergence-free unresolved field `h` and complete orthogonal roles `h=sum_b w_b`,
\[
\mathcal L_hh=2\mathcal B(h,h),
\]
so with unresolved Cartan matrices
\[
K^{(h)}_{ab}=\langle w_a,\mathcal K_hw_b\rangle,
\qquad
S^{(h)}_{ab}=\langle w_a,\mathcal S_hw_b\rangle,
\]
the signed HH child work satisfies
\[
\boxed{T_a^{HH}=\frac12\sum_b(K^{(h)}_{ab}+S^{(h)}_{ab}).}
\]

## Theorem DH — The symmetric HH role matrix is unresolved material metric velocity

For the analysis deformation generated by `h`,
\[
\boxed{
S^{(h)}_{ab}
=\frac12\int(H_h^Tw_a)^T\dot M_h(H_h^Tw_b)\,dx.}
\]
Moreover `1^T K^(h) 1=0` and `1^T S^(h) 1=0`, reproducing global nonlinear energy conservation without forcing either matrix to vanish rolewise.

## Theorem DI — Kelvin unresolved strain and Wang HH share `S_h` but not a scalar charge

Current Kelvin's unresolved deterministic correction `-r.S_h r` evaluates the same local tensor that forms Wang's symmetric HH role matrix, while actual HH child work additionally contains the unresolved skew/relink row.  Therefore canonical positive HH transfer, unresolved symmetric metric work, and Kelvin residual strain are non-equivalent scalar observables of overlapping PDE structure.

## Theorem DJ — Kelvin residual dyads have an exact commutator/anticommutator Cartan split

For `R_r=rr^T` and `A_u=S_u+Omega_u`, current Kelvin's exact dyad law becomes
\[
\boxed{\dot R_r|_{drift}=-\{S_u,R_r\}+[R_r,\Omega_u]+\Gamma_r.}
\]
The three terms are deformation, connection and q.v. respectively.

## Theorem DK — Pure Kelvin connection is isospectral on dyad space

If `S=Gamma=0`, then `dot R=[R,Omega]` and
\[
R(\sigma)=Q(\sigma)R(0)Q(\sigma)^T,
\qquad \dot Q=-\Omega Q.
\]
Hence every spectral invariant `tr(R^m)` is preserved by the pure connection sector, while strain changes `tr R` through `-2 tr(SR)`.

## Theorem DL — Full Kelvin dyad dynamics have five resolved/unresolved physical faces

For `u=V+h`,
\[
\boxed{
\dot R_r|_{drift}
=-\{S_V,R_r\}-\{S_h,R_r\}
+[R_r,\Omega_V]+[R_r,\Omega_h]+\Gamma_r.}
\]
This is the dyad-space counterpart of Wang/repo-3 resolved/unresolved `K/S` Cartan geometry, with Kelvin q.v. retained as a distinct stochastic source.

## Theorem DM — Incompressible Cartan deformation has a rigid exterior sign ladder

For `A=S+Omega`, `tr A=0`, the induced three-dimensional Hodge representations are
\[
\boxed{R_1(A)=S+\Omega,\qquad R_2(A)=-S+\Omega,\qquad R_3(A)=0.}
\]
Strain flips sign from line to area representation, skew connection keeps the same Hodge-vector sign, and top volume is neutral.

## Theorem DN — Material area normals and local affine Fourier wavevectors are the same degree-two representation

Material line/inviscid vorticity obey `dot a=Aa`, while material area Hodge vectors and locally affine Fourier covectors obey
\[
\boxed{\dot n=\dot k=-A^T(n\text{ or }k)=(-S+\Omega)(n\text{ or }k).}
\]
Thus Wang spectral wavefront geometry and Kelvin material-surface geometry are literally the same local `Lambda^2` action.

## Theorem DO — Material vorticity flux cancels strain and connection separately

For Navier--Stokes,
\[
D_t\omega=A\omega+\nu\Delta\omega,
\qquad D_tn=-A^Tn,
\]
so
\[
\boxed{D_t(\omega\cdot n)=\nu(\Delta\omega)\cdot n.}
\]
The strain and skew-connection contributions each cancel separately by degree-one/degree-two duality.

## Theorem DP — Common Cartan deformation is separately neutral on the interaction top form

For three common degree-one legs, the top wedge derivative is `tr A` times the wedge.  Incompressibility gives zero; moreover `tr S=tr Omega=0`, so common strain and common connection are separately neutral on `Lambda^3`.

## Theorem DQ — Selected energy has an exact Cartan projector-connection defect law

If `dot y=(K+S)y`, `K^*=-K`, `S^*=S`, and `P(t)` is an orthogonal projector, define
\[
G_P=\dot P-[K,P].
\]
Then
\[
\boxed{
\frac d{dt}\frac12\langle y,Py\rangle
=\langle Py,Sy\rangle+rac12\langle y,G_Py\rangle.}
\]
For a fixed role `G_P=-[K,P]`, reproducing visible conservative K relink; for a connection-comoving role `dot P=[K,P]`, `G_P=0` and only symmetric deformation remains.

## Theorem DR — Smooth orthogonal selector velocity is purely off-diagonal and finite reselection is a finite face

Differentiating `P^2=P` gives `P dotP P=0` and `(I-P)dotP(I-P)=0`.  Thus smooth role motion has no diagonal selector production.  At a finite jump `P^- -> P^+` with continuous state,
\[
\boxed{\Delta E_P=\frac12\langle y,(P^+-P^-)y\rangle,}
\]
which is a finite event face, not a smooth positive payment.

## Theorem DS — Kelvin orientation-complete first-bad selector has zero pure-orientation Cartan defect on hysteretic intervals

For `P_fb=M_fb tensor I_3` and a pure common orientation connection `K_ori=I tensor Omega`,
\[
[K_{ori},P_{fb}]=0.
\]
Since current Kelvin has `dot M_fb=0` between entry/resolve events,
\[
\boxed{G_{fb}^{ori}=0.}
\]
A continuous selector face can arise only from an identified germ-mixing current connection or other state-map dynamics; finite first-bad/resolve changes remain discrete jumps.

## Theorem DT — Orthogonal observer gauge changes connection but only conjugates physical strain

For a rotating orthogonal frame `O(t)` with `C=O^T O_dot`, the transformed generator
\[
\widetilde A=O^TAO-C
\]
has
\[
\boxed{\widetilde S=O^TSO,\qquad \widetilde\Omega=O^T\Omega O-C.}
\]
Hence strain spectrum, Frobenius magnitude and material metric-work bilinear form are invariant under common orthogonal observer motion.

## Theorem DU — Nonzero strain cannot be gauged into conservative relink by an orthogonal role/frame motion

If an orthogonal gauge has `S_tilde=0`, then necessarily `S=0`.  Thus Wang symmetric resolved work and Kelvin material strain are physical deformation sectors; only the skew connection can be absorbed into a common rotation gauge.  A non-orthogonal reparameterization moves deformation into the metric rather than eliminating it.

## Theorem DV — HH edge total variation is a realized-transfer capacity, not a Cartan activity observable

Exact periodic NSE shear `h=(a e^{-nu t} sin y,0,0)` has `B(h,h)=0`, hence zero signed HH edge work and zero HH total variation, while `S_h` and `Omega_h` are nonzero at generic points.  Therefore canonical HH TV cannot be retyped as unresolved strain/connection magnitude.

## Theorem DW — Pressure gradient is annihilated by divergence-free work, closed circulation, and curl

For divergence-free `w`, `<w,grad p>=0`; for closed loops `int_C grad p.dl=0`; and `curl grad p=0`.  Thus Wang Leray work and Kelvin closed circulation both legitimately quotient the pressure gradient at first-order transfer/circulation level.

## Theorem DX — Pressure Hessian is an exact physical source in strain/material metric acceleration

The gradient NSE is
\[
D_tA+A^2=-\nabla^2p+\nu\Delta A.
\]
With `A=S+Omega`,
\[
\boxed{D_tS+S^2+\Omega^2=-\nabla^2p+\nu\Delta S,}
\qquad
\boxed{D_t\Omega+S\Omega+\Omega S=\nu\Delta\Omega.}
\]
Moreover
\[
\Delta p=-|S|_F^2+|\Omega|_F^2=-|S|_F^2+\frac12|\omega|^2,
\]
and the material metric acceleration contains `-Hess p` explicitly.  Pressure is therefore gauge for first-order closed/divergence-free work but not absent from deformation curvature.

## Theorem DY — Exact affine strain and rigid rotation calibrate the pressure-Hessian face

For affine pure strain `A=S=diag(a,-a,0)`, quadratic pressure has `Hess p=-S^2`; for rigid rotation `A=Omega`, centrifugal pressure has `Hess p=-Omega^2`.  Both are exact smooth affine NSE solutions with `Delta u=0`, showing pressure Hessian can actively balance either deformation or rotation curvature while pressure still performs no solenoidal kinetic-energy work.

## Theorem DZ — Spectral enstrophy killing and full-state Kelvin q.v. trace are the same Dirichlet form

With helical energy `E_(k,s)=|a_(k,s)|^2/2` and `Gamma_K=2nu(grad omega)(grad omega)^T`,
\[
\boxed{
2\nu\sum_{k,s}|k|^4E_{k,s}
=\nu\|\nabla\omega\|_2^2
=\frac12\int\operatorname{tr}\Gamma_K\,dx.}
\]
Likewise `2nu sum |k|^2 E=nu||grad u||_2^2`.  This closes the full-state trace-level viscosity dictionary between Wang spectral killing and Kelvin instantaneous q.v.

## Theorem EA — Periodic global enstrophy reads Kelvin q.v. as exactly the viscous loss

On a periodic domain,
\[
\boxed{
\frac d{dt}\frac12\|\omega\|_2^2
=\int\omega\cdot S\omega\,dx
-\frac12\int\operatorname{tr}\Gamma_K\,dx.}
\]
The omitted local Laplacian term is spatial curvature flux whose integral vanishes.  No future/reduced covariance is identified with this instantaneous trace.

## Theorem EB — Scalar spectral killing does not determine the Kelvin q.v. tensor

Exact one-wavevector transverse NSE solutions with fixed `|a_+|,|a_-|` but different relative helical phase have identical modal energies and scalar viscous killing, while their integrated orientation-complete `Gamma_K` tensors differ.  Only the trace is fixed by the spectral killing.

## Theorem EC — Local affine wavefront radius is driven by directional strain inside conservative transport

For `V=Ax`, `A=S+Omega`, a transported local phase covector obeys
\[
\dot k=-A^Tk=(-S+\Omega)k,
\]
so
\[
\boxed{\frac d{dt}\log|k|=-\hat k\cdot S\hat k,}
\qquad
\boxed{\dot{\hat k}=\Omega\hat k-(I-\hat k\hat k^T)S\hat k.}
\]
The same laws hold for a material area Hodge vector; material-line magnitude has the opposite strain sign.

## Theorem ED — Radial spectral motion can be conservative transport rather than energy production

Incompressible scalar transport preserves total `L^2`, yet its local affine wavevector can change radius by Theorem EC.  The transport term inside the skew-adjoint resolved `K_V` therefore can relocate spectral content across radius without creating total energy.

## Theorem EE — Phase-space strain and fiber metric strain are distinct representations of the same tensor

`V.grad` carries `S_V` through the wavevector characteristic `kdot=-A_V^T k`, while the self-adjoint operator `S_V^{op}` carries the same tensor as vector-amplitude/material metric work.  Hence radial scale progress and symmetric strain work are non-equivalent physical observables even though both depend on `S_V`.

## Theorem EF — Deterministic rotation curvature is the exterior-square lift of the vorticity dyad

With `Omega=(1/2)[omega]_x`,
\[
\boxed{-\Omega^2=\frac14R_2(\omega\omega^T)
=\frac14(|\omega|^2I-\omega\omega^T).}
\]
The tensor is PSD transverse to vorticity and has trace `|omega|^2/2` after the factor `1/4`.

## Theorem EG — Exact strain dynamics have four typed local source faces

The symmetric gradient equation can be written
\[
\boxed{
D_tS=-S^2+\frac14R_2(\omega\omega^T)-\nabla^2p+\nu\Delta S.}
\]
These are strain self-interaction, deterministic transverse-vorticity geometry, pressure curvature, and viscous strain diffusion.  Taking trace recovers the pressure Poisson equation exactly.

## Theorem EH — Material metric acceleration has a five-face deterministic anatomy

Using `1/2 H Mddot H^T = ringS + 2S^2`,
\[
\boxed{
\frac12H\ddot MH^T
=S^2+\frac14R_2(\omega\omega^T)-\nabla^2p+\nu\Delta S+[S,\Omega].}
\]
The commutator `[S,Omega]` is symmetric trace-free orientation coupling.

## Theorem EI — Deterministic vorticity curvature and Kelvin q.v. curvature share `R_2` but are non-equivalent

Affine rigid rotation has `R_2(omega omega^T)!=0` and `Gamma_K=0`; an exact periodic shear at a vorticity-zero symmetry point has `R_2(omega omega^T)=0` but `Gamma_K!=0`.  The common `R_2` is a representation law, not a physical equivalence of amplitude and gradient-q.v. inputs.

## Theorem EJ — Wang transverse strain trace equals Kelvin-carrier radial dilation

For the exact affine Kelvin mode in Wang's objective transverse frame `E`, with `B_perp=E^T S E`,
\[
\boxed{\operatorname{tr}B_\perp=\frac d{dt}\log|k|.}
\]
Thus scalar transverse deformation and carrier-radius deformation are one incompressibility constraint, not independent parameters.

## Theorem EK — Kelvin-mode carrier radius and transverse polarization area obey an exact top-form balance

If `U_perp` is the transverse amplitude fundamental map,
\[
\boxed{
\frac d{dt}\log(|k|\det U_\perp)=-2\nu|k|^2,}
\]
so
\[
\boxed{
|k(t)|\det U_\perp(t)e^{2\nu\int_0^t|k|^2ds}=|k(0)|.}
\]
Inviscidly `|k| det U_perp` is constant.  This is a Kelvin-mode phase/polarization top-form law, structurally parallel to incompressible `Lambda^3` neutrality but not identified with literal material volume.

## Theorem EL — Wang's objective polarization `SL(2)` map is the forced trace-free material-metric quotient

Writing `B_perp=sigma I+D`, `tr D=0`,
\[
U_\perp=\left(\frac{|k_0|}{|k|}\right)^{1/2}e^{-\nu\int|k|^2}\widetilde U
\]
gives
\[
\boxed{\dot{\widetilde U}=-D\widetilde U,\qquad \det\widetilde U=1.}
\]
Moreover `D=tf[(1/2)E^T H Mdot H^T E]`; it is the trace-free transverse material metric velocity.  In two real dimensions the map is symplectic.

## Theorem EM — Raw transverse polarization is generally not `SL(2)` when carrier radius changes

Exact affine pure strain gives `|k|=e^{-at}` and inviscid raw `U_perp=diag(e^{at},1)`, so `det U_perp=e^{at}!=1` while `|k|det U_perp=1`.  Only the physically normalized trace-free map is determinant one.

## Theorem EN — Wang helical phase commutator is the circular-basis image of material strain holonomy

For trace-free transverse material metric velocities
\[
D_j=\begin{pmatrix}\delta_j&\beta_j\\\beta_j&-\delta_j\end{pmatrix},
\]
\[
\boxed{[D_1,D_2]=2(\delta_1\beta_2-\beta_1\delta_2)J.}
\]
In the circular/helical basis `C`, `C^*JC=diag(i,-i)`.  Thus the same noncommutativity is a real polar-holonomy generator and an opposite-helicity phase generator.  The coefficient is invariant under a common `SO(2)` transverse frame rotation.

## Theorem EO — An exact affine NSE family realizes nonzero material/helical commutator curvature

For
\[
S(t)=\begin{pmatrix}d&\gamma t&0\\\gamma t&-d&0\\0&0&0\end{pmatrix},
\qquad u=S(t)x,
\qquad \nabla^2p=-\dot S-S^2,
\]
the flow is an exact affine NSE solution, `k=e_3` is fixed, and the transverse strain obeys
\[
[D(t_1),D(t_2)]=2d\gamma(t_2-t_1)J.
\]
The exact second Magnus face is
\[
\boxed{\Omega_2(T)=-(d\gamma T^3/6)J,}
\]
which becomes opposite diagonal helical phases.  No claim is made that higher Magnus terms vanish or that this local holonomy is a global transfer cost.

## Theorem EP — Wang grain curvature and Kelvin codeforming quadratic jet are exactly the same tensor

Current Wang defines
\[
B_{abc}=(L^{-1})_{ai}(\partial_j\partial_ku_i)L_{jb}L_{kc},
\]
while current Kelvin defines `J_2(L)=L^{-1}(nabla^2u)L^(tensor 2)`.  Therefore
\[
\boxed{B=\mathfrak J_2(L)}
\]
index by index.  The quadratic Kelvin codeforming field begins as `N_L(xi)=(1/2)B[xi,xi]`.

## Theorem EQ — Wang and Kelvin take different physical quotients of the common nonaffine Hessian jet

Wang's first genuine Gaussian packet-shape exit satisfies
\[
\boxed{\|F_\perp\|_2^2/\|\psi\|_2^2=(3/8)\|\operatorname{Sym}B\|_F^2,}
\]
where affine/tangent packet parameters have been quotiented.  Kelvin's codeforming position/area and moment-tower laws use the full `B`.  Hence the common cause is `B`, while the observables are non-equivalent projections.

## Theorem ER — Exact quadratic heat shear activates both nonaffine representations from one physical jet

For exact NSE `u=(y^2+2nu t,0,0)` at the centered anchor with `L=I`, `B_122=2`; both `Sym B` and the Kelvin quadratic nonaffinity field are nonzero.  One exact NSE velocity-curvature event therefore feeds both programmes without temporal matching.

## Theorem ES — `Sym B=0` does not imply Kelvin codeforming affinity

The smooth periodic divergence-free state `u=(0,sin x sin z,-sin x sin y)` has, at the origin, nonzero Hessian tensor `B` with `Sym B=0`.  Wang's first third-Hermite transverse-shape forcing vanishes at that jet while Kelvin's quadratic codeforming field is nonzero.  The bridge must carry full `B` before programme-specific quotienting.

## Theorem ET — Kelvin principal metric projectors are exactly connection-comoving

For a simple-spectrum physical line metric `M=V Lambda V^T`, define `C_M=Vdot V^T`.  Then each principal projector `P_i=v_i v_i^T` obeys
\[
\boxed{\dot P_i=[C_M,P_i],\qquad G_{P_i}^{M}=0.}
\]
In principal coordinates `Omega_M=V^T Vdot`, current Kelvin's spectral-gap law is `Omega_M,ij=B_ij/(lambda_j-lambda_i)`, `B=V^T Mdot V`.

## Theorem EU — Kelvin principal-channel mixing is the repo-3 projector connection term and equals off-diagonal metric work

For residual second moment `Q`,
\[
\boxed{\operatorname{tr}(\dot P_iQ)=[\widetilde Q,\Omega_M]_{ii}.}
\]
Weighted summation gives
\[
\boxed{\sum_i\lambda_i[\widetilde Q,\Omega_M]_{ii}=2\sum_{i<j}B_{ij}\widetilde Q_{ij}.}
\]
Thus eigenframe mixing is moving-projector traffic and exactly the off-diagonal metric-work face, not a new source.

## Theorem EV — Literal first-bad selection preserves principal-projector connection transport on hysteretic intervals

For Kelvin's `M_fb tensor I_3` and block-diagonal per-germ principal projectors/connections, the selector commutes with both.  Hence selected principal projectors obey the same connection-comoving law and have zero selector-spectral Cartan defect on `Mdot_fb=0` intervals.

## Theorem EW — Metric-eigenframe connection and fluid Cartan/vorticity connection are non-equivalent

An exact affine pure-strain NSE solution has physical `Omega_u=0`, but a non-aligned finite material line frame can have a rotating simple-spectrum metric eigenframe `C_M!=0`.  Therefore a skew metric-spectral gauge connection may not be identified with the skew part of `grad u` merely because both are antisymmetric.

## Theorem EX — Repo-3 pure projector resets do not cover Kelvin physical residual synthesis/refinement

If only a projector changes on a frozen state, the repo-3 finite projector jump applies.  If Kelvin's physical residual synthesis `A` changes, then
\[
\boxed{\Delta Q=\Delta A\mathbb Q A_-^T+A_-\mathbb Q\Delta A^T+\Delta A\mathbb Q\Delta A^T,}
\]
and weighted events additionally carry geometry revaluation.  The tensor-square pair reset is mandatory; it cannot be replaced by one positive projector-distance payment.

## Theorem EY — An instantaneous Eulerian/Wang field does not determine a Kelvin finite-current residual without material shape state

For exact periodic NSE `u=(e^{-nu t} sin y,0,0)`, a centered rectangle of half-widths `(a,b)` has finite-to-local Kelvin flux residual
\[
\boxed{\varepsilon_\Sigma=4ae^{-\nu t}(b-\sin b).}
\]
Two rectangles with the same area and orientation but different aspect ratio have different residuals in the identical Eulerian field.  Hence a universal field-only Wang-to-Kelvin finite-current state map is impossible; actual material shape/current data are mandatory.

## Theorem EZ — The common Hessian jet `B=J_2(L)` is insufficient for finite Kelvin shape

At the same one-mode shear anchor `y=0`, `nabla^2u=0`, hence `B=J_2(L)=0` for every L and Wang's Hessian-driven third-Hermite transverse forcing vanishes.  Nevertheless the finite Kelvin residual above is nonzero, with
\[
\varepsilon_\Sigma=(2/3)ae^{-\nu t}b^3-(1/30)ae^{-\nu t}b^5+O(b^7).
\]
Thus higher jets/moments or the full codeforming field are physically necessary for finite-shape descent.

## Theorem FA — A valid Wang-to-Kelvin state bridge must augment Eulerian/coherent data by material current/shape and correct clock/history

The exact no-go implies the full finite-current state can only have a bridge of the typed form
\[
\boxed{
\text{Kelvin current state}
=\Phi(\text{Eulerian/Wang physical state},\text{material shape/current state},\text{causal clock/history}),}
\]
not a universal function of Eulerian role data alone.  The theorem does not prescribe a unique such lift.

## Theorem FB — Every linear physical refinement/synthesis has an exact tensor-square pair lift

If `y=sum_alpha y_alpha`, then
\[
\boxed{y\otimes y=\sum_{\alpha,\beta}y_\alpha\otimes y_\beta,}
\]
so quadratic energy contains all diagonal children plus all cross coherences.  A diagonal-only refinement is exact only under physical orthogonality.

## Theorem FC — Wang coherent refinement and Kelvin residual synthesis obey the same pair functor in different state spaces

Current Wang has additive coherent localization `T_E=sum_alpha T_(E_alpha)`, hence `f_E=sum_alpha f_alpha` and the pair state contains all `alpha,beta` cross terms.  Current Kelvin has `Q_A=A mathbb Q A^T`, the ensemble/covariance form of the same `A tensor A` pushforward.  This is a common functorial law, not an identification of Wang cells with Kelvin germs.

## Theorem FD — Kelvin left/right/quadratic reset faces are the finite-difference expansion of the universal pair functor

For `A_+=A_-+Delta A`,
\[
\boxed{\Delta Q=\Delta A\mathbb Q A_-^T+A_-\mathbb Q\Delta A^T+\Delta A\mathbb Q\Delta A^T.}
\]
Thus any future linear Wang-to-Kelvin state lift must preserve the full pair pushforward and cross coherence; first moments or diagonal child energies alone cannot define the quadratic state bridge.

## Theorem FE — Wang and Kelvin full non-affine velocity fields differ exactly by an affine gauge

With Wang normalized velocity `v_W=L^{-1}[u(X+Lz)-Xdot]`, put `c=L^{-1}[u(X)-Xdot]` and `A_L=L^{-1}(grad u(X))L`.  Kelvin's codeforming field satisfies `v_W=c+A_L z+N_L`.  Therefore Wang's Gaussian remainder `R_W=v_W-vbar-Abar z` obeys
\[
\boxed{R_W-N_L=(c-vbar)+(A_L-Abar)z\in\mathrm{Aff}.}
\]
Hence `[R_W]_/Aff=[N_L]_/Aff` exactly.

## Theorem FF — All higher physical jets of the two full non-affine fields coincide

For every smooth state and every `p>=2`,
\[
\boxed{D^pR_W(0)=D^pN_L(0)=L^{-1}(\nabla^p u(X))L^{\otimes p}=\mathfrak J_p(L).}
\]
This identifies the common higher physical input without asserting a separate Wang packet-normal/Hermite formula at every order.

## Theorem FG — Wang Gaussian affine gauge and Kelvin anchor affine gauge are non-identical in exact periodic NSE

For exact shear `u=(e^{-nu t} sin y,0,0)` at `X=0,L=I`, Kelvin has `N=e^{-nu t}(sin y-y)e_1`, while Wang's centered Gaussian affine fit gives `R_W=e^{-nu t}(sin y-kappa_rho y)e_1` with `0<kappa_rho<1`.  Their difference is nonzero affine, while all derivatives of order at least two agree.

## Theorem FH — Wang Gaussian residual is the minimal Gaussian-norm representative of the common affine-equivalence class

With `N_L=R_W+(vbar-c)+(Abar-A_L)z` and centered Gaussian covariance `C_rho`, Wang affine orthogonality gives
\[
\boxed{
\|N_L\|_\rho^2
=\|R_W\|_\rho^2
+|vbar-c|^2
+\operatorname{tr}[(Abar-A_L)C_\rho(Abar-A_L)^T].}
\]
Hence `||R_W||_rho^2=inf_(a,B)||v_W-a-Bz||_rho^2`: the Gaussian residual is the quotient-norm representative after the exact common affine class has been identified.  This is not Wang's coherent deformation variance `K_C^2=E||grad W-Abar||_F^2`; that is a distinct gradient-level observable related only by Wang's OU spectral-gap estimates.

## Theorem FI — Kelvin anchor residual norm contains an explicit affine-gauge mismatch beyond the common nonaffinity

The nonnegative difference `||N_L||_rho^2-||R_W||_rho^2` is exactly the mismatch between Kelvin's local anchor affine gauge and Wang's Gaussian best affine gauge; it is not additional physical non-affinity.  Exact periodic shear with `rho=pi^-1/2 exp(-y^2)` gives excess `(1/2)e^{-2nu t}(1-e^{-1/4})^2`.


## Theorem FJ — A genuine Kelvin selector switch is not universal transport of the old selected residual

For a persistent finite residual library `X` with germ extraction maps `E_g`, a switch `g!=h` cannot satisfy `E_h=T E_g` on the whole library for any matrix `T`, because `ker E_g` contains nonzero vectors supported in germ `h` while `ker E_h` does not.  More generally, after a specified physical library event `A_full`, a reduced selected transition exists exactly when `E_h A_full=T E_g`, equivalently `ker E_g subset ker(E_h A_full)`.  Thus selector readout and physical transport are different operations; a restricted reduction requires an independently proved admissible-state relation.

## Theorem FK — The active selected pair block is not a universal compositional state across genuine switches

For full library pair state `P=E[XX^T]`, the selected block is `P_g=E_g P E_g^T` and a switch obeys
\[
\boxed{P_h-P_g=\Delta E\,P E_g^T+E_gP\,\Delta E^T+\Delta E\,P\,\Delta E^T.}
\]
There exist deterministic PSD pair states `P_i=X_iX_i^T`, `X_1=(a,b_1)`, `X_2=(a,b_2)`, with identical old selected block `aa^T` and different new blocks `b_i b_i^T`.  Hence, absent an extra admissible factorization theorem, hidden library coordinates and cross pairs are mandatory for universal selector composition.

## Theorem FL — Deterministic pair coherence and same-replica Kelvin q.v. obey one tensor-square event functor but remain distinct physical faces

Every linear physical event `X_+=AX` pushes a state pair/second moment by `P_+=APA^T`.  For a one-replica Kelvin residual library with stacked common-noise response `Sigma`, `Gamma_lib=2nu Sigma Sigma^T`; the same event gives `Sigma_+=A Sigma` and
\[
\boxed{\Gamma_+=A\Gamma_{lib}A^T.}
\]
Thus Wang coherent refinement, Kelvin residual pair synthesis, and Kelvin same-replica q.v. all carry the same `A tensor A` congruence law.  This does not identify the objects: `P` is pair/coherence state, while `Gamma_lib` is the continuous martingale q.v. source.  One common three-dimensional Brownian driver also forces `rank Gamma_lib<=3`.

## Theorem FM — Diagonal independent per-germ q.v. is not the same physical Kelvin replica

For exact NSE shear `u=e^{-nu k^2t}cos(ky)e_1`, Kelvin asymmetric packets with `rho=pi/(2k)`, anchors `Y_1=pi/(2k)`, `Y_2=3pi/(2k)` have exact anchor-noise coefficients `q_1=-4e^{-nu k^2t}k^3/pi^2`, `q_2=-q_1`.  Hence in one common stochastic-flow replica `Gamma_12=-Gamma_11`, and synthesis `A=[I I]` gives `A Gamma_lib A^T=0`.  Replacing the common driver by independent per-germ noises deletes the cross block and gives `A Gamma_ind A^T=4nu Sigma_1 Sigma_1^T>0`.  Therefore diagonal-only q.v. changes the physical stochastic model rather than approximating the same replica.


## Theorem FN — Diagonal block-Gram marginals enlarge latent-frame invariance and erase relative coupling

For blocks `B_i` with full quadratic state `G_ij=B_iB_j^*`, independent latent isometries `B_i -> B_i U_i` leave every diagonal `G_ii` invariant but change cross blocks to `B_i U_i U_j^* B_j^*`.  A common latent change `U_i=U` leaves the full Gram invariant.  Therefore diagonal projection has a strictly larger generic invariance than the full quadratic state and cannot determine the relative coupling required by `A G A^*` synthesis.

## Theorem FO — Wang coherent child diagonals do not determine relative phase coherence or the synthesized quadratic state

For complex coherent children `f_alpha`, `C_{alpha beta}=f_alpha f_beta^*` and `f=sum_alpha f_alpha`.  Independent phase changes leave all `C_{alpha alpha}` fixed but send `C_{alpha beta}` to `e^{i(theta_alpha-theta_beta)}C_{alpha beta}`.  Hence diagonal child pairs do not determine `ff^*=sum_{alpha,beta}C_{alpha beta}`.  This is an information-loss statement about a reduced pair state, not a claim that independent phase rotation is a gauge of the full NSE field.

## Theorem FP — Kelvin diagonal same-replica q.v. blocks do not determine relative common-driver orientation

For one stochastic-flow replica, `Gamma_gh=2nu Sigma_g Sigma_h^T`.  A common Brownian coordinate change `Sigma_g -> Sigma_g O` with one `O in O(3)` leaves the full Gram invariant and is genuine driver gauge.  Independent right rotations `Sigma_g -> Sigma_g O_g` preserve every diagonal `Gamma_gg` but generally change `Gamma_gh` and synthesized q.v.; they are not a mere coordinate change of one shared Brownian driver.  Thus diagonal germ q.v. enlarges the apparent gauge and discards physical inter-germ coupling.

## Theorem FQ — No universal diagonal-marginal quadratic state map can preserve Wang/Kelvin linear synthesis

The Wang and Kelvin relative couplings are different physical objects, but both are erased by diagonal marginalization and both enter their exact tensor-square synthesis laws.  Therefore a universal cross-program quadratic bridge based only on diagonal child/germ marginals is impossible: it must carry the relevant full ordered pair/Gram state or supply an independent Navier--Stokes theorem reconstructing the missing relative coupling.  Exact one-mode NSE realizes the Kelvin negative-coupling branch with equal diagonal q.v. blocks and complete sum-synthesis cancellation.


## Theorem FR — Frozen-selector Brownian q.v. and finite selector jump variation are different path mechanisms

For a persistent same-replica library `dChi=sqrt(2nu) Q dW`, `Gamma_lib=2nu Q Q^T`, a frozen selector gives `dY=sqrt(2nu) E_g Q dW` and continuous q.v. rate `d[Y]^c/dsigma=E_g Gamma_lib E_g^T`.  At a selector-only event with continuous library, `Delta Y=(E_+-E_-)Chi`; this creates no atom in `[Y]^c`, although total optional q.v. contains `Delta Y Delta Y^T`.  Continuous viscous production and finite readout path variation are therefore distinct physical types.

## Theorem FS — Selector optional jump q.v. is only the quadratic face of endpoint pair revaluation

For `Y_+=Y_-+Delta Y`,
\[
\boxed{Y_+Y_+^T-Y_-Y_-^T=\Delta Y\,Y_-^T+Y_-\Delta Y^T+\Delta Y\Delta Y^T.}
\]
The optional jump-q.v. atom is only `Delta Y Delta Y^T`; the two linear faces are signed.  Hence positive jump q.v. cannot replace the full pair reset ledger or be identified with deterministic pair/coherence production.

## Theorem FT — Exact NSE selector sign flip has positive jump q.v. but zero pair revaluation, and a closed excursion has positive path q.v. with zero net state

For exact shear `u=e^{-nu k^2t}cos(ky)e_1` and Kelvin half-period asymmetric packets of side `rho=pi/(2k)`, `chi_0=4e^{-nu k^2t}k^2/pi^2` and `chi_1=-chi_0`.  A selector switch `chi_0 e_z -> -chi_0 e_z` has jump square `4chi_0^2 P_z>0` but endpoint dyad jump exactly zero because the signed linear faces cancel it.  The closed excursion `0->1->0` returns to the identical selected state while accumulating jump-q.v. trace `8chi_0^2=128e^{-2nu k^2t}k^4/pi^4>0`.  Thus selector jump q.v. is path variation, not a monotone physical state/covariance bank.

## Theorem FU — Simultaneous physical event plus selector is the composed map, not a sum of independent positive reset costs

If the library event is `Chi_+=A Chi_-` and the selector changes `E_- -> E_+`, then `Y_+=E_+A Chi_-` and the literal jump is `J=(E_+A-E_-)Chi_-`.  Different exact intermediate decompositions of `J` exist, but `JJ^T` contains their cross faces.  Therefore a simultaneous event cannot generically be charged as “selector jump square plus physical-event jump square” unless an independent orthogonality theorem removes the cross terms.  Physical event transport and selector readout must remain separately typed before the composed pair functor is formed.


## Theorem FV — Selected pair revaluation is an endpoint coboundary, while selector jump q.v. has nonzero closed-loop circulation

For any supplied selected path `Y_0,...,Y_m`, the pair increments telescope exactly: `sum_j (Y_jY_j^T-Y_{j-1}Y_{j-1}^T)=Y_mY_m^T-Y_0Y_0^T`.  In contrast the selector jump optional-q.v. accumulator `J=sum_j DeltaY_j DeltaY_j^T` satisfies `J[a->b->a]=2(b-a)(b-a)^T!=0` for `a!=b`.  Therefore no universal endpoint-state potential `F(Y)` can satisfy `F(Y_+)-F(Y_-)=DeltaY DeltaY^T` for every selector jump; the trace version is impossible as well.

## Theorem FW — Current library/readout state does not determine accumulated selector jump q.v.

For a frozen persistent library with distinct readouts `a=E_0X`, `b=E_1X`, the stationary selector history and the closed excursion `0->1->0` have the same endpoint `(X,E_0,Y=a)` but accumulated jump q.v. `0` and `2(b-a)(b-a)^T`, respectively.  Thus no universal instantaneous map of the current library, selector and selected residual reconstructs accumulated selector jump q.v. on the supplied hybrid path space.  Adding only the current continuous Brownian source rate does not repair the loss.  Any restriction that removes this obstruction must come from an independently proved physical event-timing/admissible-history theorem.

## Theorem FX — Exact NSE activates the selector-history state-map obstruction

For exact shear `u=e^{-nu k^2t}cos(ky)e_1`, the half-period Kelvin residual readouts are `a=chi_0e_z`, `b=-chi_0e_z`, `chi_0=4e^{-nu k^2t}k^2/pi^2`.  On this frozen exact-NSE payload, the stationary selector path and `0->1->0` have the same endpoint selected state/pair/current source rate, but the loop accumulates jump-q.v. `8chi_0^2P_z` with trace `128e^{-2nu k^2t}k^4/pi^4>0`.  This calibrates the history obstruction without asserting that the actual first-bad timing realizes that excursion.

## Theorem FY — A literal cross-program state map must carry selector-event history or prove it reconstructible

Even after the instantaneous Eulerian/coherent field, material current/shape, persistent candidate library, active selector, full pair/Gram coupling and current continuous q.v. source are supplied, accumulated selector jump q.v. is not universally determined by endpoint data.  A Wang--Kelvin lift that needs this path functional must therefore carry selector-event history/an equivalent accumulator, or prove an independent Navier--Stokes theorem making the relevant history a function of endpoint state on its theorem domain.  No recurrence or continuation consequence follows from the path accumulator itself.


## Theorem FZ — General adaptive physical-event first moment requires the joint map-state correlation

For a realized physical linear map `C` and input state `x`, assuming the displayed products are integrable, with centered variables `deltaC=C-E C`, `deltax=x-E x`, one has exactly `E[Cx]=(E C)(E x)+E[deltaC deltax]`.  Thus mean-map times mean-state is an identity only on a domain where the physical map-state correlation vanishes.

## Theorem GA — General adaptive quadratic synthesis obeys an exact five-face law

For symmetric quadratic payload `Q`, assuming the displayed quadratic/mixed expectations are finite, put `Cbar=E C`, `Qbar=E Q`, `deltaC=C-Cbar`, `deltaQ=Q-Qbar`.  Then
\[
\boxed{E[CQC^T]=Cbar Qbar Cbar^T+E[deltaC Qbar deltaC^T]+Cbar E[deltaQ deltaC^T]+E[deltaC deltaQ]Cbar^T+E[deltaC deltaQ deltaC^T].}
\]
The first correction is PSD when `Qbar>=0`; the remaining mixed faces are signed.  The last cubic mixed face is forced because the adaptive physical map occurs on both sides of the quadratic payload.

## Theorem GB — Kelvin's equal-weight two-replica four-face law is the centrally symmetric specialization, not a general closure

For two equal-weight replicas, `deltaC` and `deltaQ` change sign together between replicas, so `E[deltaC deltaQ deltaC^T]=0` by odd parity and Theorem GA reduces exactly to Kelvin `eba4aa9`'s four-face identity.  With three or more nonsymmetric adaptive replicas the cubic face need not vanish.

## Theorem GC — The cubic adaptive event-payload face is irreducible even for positive payloads

For three equal-weight scalar replicas `C=(0,1,2)`, the two strictly positive payload ensembles `Q^+=(4,1,4)` and `Q^-=(2,5,2)` have the same `Cbar=1`, `Qbar=3`, mean face `3`, event-dispersion face `2`, and zero left/right event-payload correlations.  Their cubic faces are `+2/3` and `-2/3`, giving exact outputs `17/3` and `13/3`.  Therefore deleting the cubic face cannot be a universal adaptive-ensemble closure.  Kelvin adaptive first-bad averaging and any future averaging across Wang state-selected physical event roles must retain the relevant joint event-map/payload law unless an exact closure domain is proved.


## Theorem GD — Wang inherited carrier stock and Kelvin selector jump q.v. are inequivalent memory types

Wang's current same-carrier relay identifies the inherited component with the carrier energy stock `E_M(u)` and assigns that inherited component generation depth zero; the inheritance statement is about a persistent physical carrier/stock amount, not fresh positive-work generation.  Kelvin selector jump optional q.v. is instead the path functional `J[Y]=sum_j DeltaY_j DeltaY_j^T`, which has nonzero PSD circulation `J[a->b->a]=2(b-a)(b-a)^T` on a closed readout loop.  Therefore no universal endpoint/ancestry stock rule can reconstruct selector jump variation on a path class containing both stationary and closed-excursion histories with the same endpoints.

## Theorem GE — Exact NSE activates the stock-versus-path-memory no-go

For exact shear `u=e^{-nu k^2t}cos(ky)e_1`, half-period Kelvin residual readouts satisfy `chi_1=-chi_0`, `chi_0=4e^{-nu k^2t}k^2/pi^2`.  On the same frozen exact-NSE payload, the stationary selector history and the closed `0->1->0` excursion have identical endpoint state/pair and therefore identical endpoint state-stock observables, while the excursion accumulates jump-q.v. `8chi_0^2P_z` with trace `128e^{-2nu k^2t}k^4/pi^4>0`.  This calibrates the state-map no-go without claiming actual first-bad timing or a Wang relay event for that shear.

## Theorem GF — An exact quotient of one physical owner cannot erase simultaneous owners

For a typed product event state `Z=(S,R_1,...,R_q)`, the component projection `q_S(Z)=S` may support an exact identity `S_+=S_-`, but this implies equality only after projection; it cannot imply `Z_+=Z_-` unless the remaining owners are separately controlled.  Wang's inherited-stock relay therefore does not delete its simultaneous classified residual/material owners; current upstream explicitly fail-closes a stock-only quotient when classified residual work is non-negligible.  Kelvin's simultaneous physical-event/selector law gives the complementary exact example `D=E_+A-E_-=E_-DeltaA+DeltaE+DeltaE DeltaA`, where the mixed face is lost by either single-owner projection.

## Theorem GG — A literal Wang--Kelvin state map must keep carrier ancestry stock and selector-event path history separately when both are used

Same-carrier inheritance memory records physical carrier identity plus current inherited energy stock.  Selector-event memory records a traversed readout/event path or equivalent jump-q.v. accumulator.  Closed-loop non-telescoping proves that the latter is not determined by the former.  Thus a cross-program theorem using both mechanisms must retain both memory types and every simultaneous work/material/event/q.v. owner, or prove an independent Navier--Stokes reconstruction theorem; nonnegativity alone provides no identification.


## Theorem GH — Kelvin packet coefficients carry a passive `GL(3)` gauge, while the physical residual and inverse-Gram energy are invariant

For `H in GL(3)`, coefficient `epsilon`, and physical residual `r=H^{-T}epsilon`, a passive packet-basis change `(H,epsilon)->(HS,S^T epsilon)` leaves `r` exactly invariant.  With `G_H=H^TH`, the scalar `epsilon^T G_H^{-1} epsilon=|r|^2` is likewise invariant under `G_H->S^T G_H S`.  The raw coefficient norm `|epsilon|^2` is not invariant and can be scaled arbitrarily by a passive `S=lambda I` without changing the physical residual.

## Theorem GI — Raw packet-coefficient ranking is not a physically admissible universal first-bad ordering

Two candidates can keep exactly the same physical residuals and inverse-Gram energies while a passive basis change reverses their raw `|epsilon|^2` ordering.  Therefore any physical first-bad score must descend to the passive-gauge quotient; raw coordinate size alone cannot define the ordering.  Gauge invariance is necessary but not sufficient: Kelvin's current support-locality, persistent-library, full-coherence and adaptive-joint-law conditions remain separately necessary.

## Theorem GJ — Exact NSE activates a gauge-spurious ranking asymmetry

For exact shear `u=e^{-nu k^2t}cos(ky)e_1`, the half-period Kelvin residual pair is `r_0=chi e_z`, `r_1=-chi e_z`, `chi=4e^{-nu k^2t}k^2/pi^2`, so their physical residual energies are exactly tied.  Representing candidate `0` by the passive gauge `(H_0,epsilon_0)=(3I,3r_0)` and candidate `1` by `(I,r_1)` preserves both physical residuals and inverse-Gram energies, but gives raw coefficient energies in ratio `9`.  Thus raw packet ranking creates a fake first-bad asymmetry on exact smooth NSE data.

## Theorem GK — Cross-program role/selector maps must act on physical equivalence classes, not representation gauges

Kelvin first-bad logic must factor through the quotient `(H,epsilon)~(HS,S^T epsilon)`, equivalently through the physical residual or other gauge-invariant physical data.  Wang hard event roles remain distinct physical event-owner observables, not Kelvin selectors; the common bridge is only that role/selector decisions must be functions of physical state rather than arbitrary coordinate representatives.  A literal Wang--Kelvin state map therefore cannot treat raw packet coefficients as physical state without retaining the frame and quotienting the passive gauge.


## Theorem GL — Navier--Stokes forces an exact relative current for every differentiable nondegenerate enstrophy critical branch

Let `e=|omega|^2/2` and `R=omega.S.omega-nu|grad omega|_F^2+nu Delta e`.  If `grad e(x_*(t),t)=0` and `H_e=Hess e` is invertible, differentiating the critical constraint and the exact local enstrophy PDE gives
\[
\boxed{H_e(\dot x_*-u)+\nabla R=0,\qquad \dot x_*-u=-H_e^{-1}\nabla R.}
\]
Using the orientation-complete Kelvin packet identity `nu|grad omega|^2=(1/2)tr(Gamma_H M_H)`, the three physical drivers of the relative current are the gradients of vortex stretching, Kelvin q.v. bulk, and curvature diffusion.  A nondegenerate enstrophy critical branch is material exactly when `grad R=0` along it.

## Theorem GM — A nondegenerate enstrophy critical current is not universally a material carrier

For the exact viscously decaying periodic ABC Beltrami solution, `x_*=(pi/4,pi/4,pi/4)` is a fixed strict nondegenerate enstrophy maximum with `xdot_*=0`, while `u(x_*,t)=sqrt(2) A e^{-nu t}(1,1,1) != 0` and `det Hess e=-(1/2)A^6 e^{-6nu t}`.  Thus a material particle initially at the maximum immediately leaves the critical branch.  Therefore a Kelvin critical-locus candidate current cannot be universally identified with Wang's continuing material carrier current.

## Theorem GN — Incompressibility cancels the local velocity-gradient contribution to enstrophy-critical curvature volume, not to curvature shape

Along any differentiable enstrophy critical branch,
\[
\frac{d_*H_e}{dt}=\nabla^2R-(\nabla u)^TH_e-H_e\nabla u+((\dot x_*-u)\cdot\nabla)H_e.
\]
For nondegenerate `H_e`, the connection contribution to `d log|det H_e|/dt` is exactly `-2 div u`.  Hence incompressible Navier--Stokes obeys
\[
\boxed{\frac d{dt}\log|\det H_e|=\operatorname{tr}(H_e^{-1}\nabla^2R)+\operatorname{tr}[H_e^{-1}((\dot x_*-u)\cdot\nabla)H_e].}
\]
After substituting Theorem GL, the second face is the physical relative-transport correction driven by `-H_e^{-1}grad R`.  Zero connection contribution to determinant volume does not imply frozen Hessian shape or eigenstructure.

## Theorem GO — Physical critical-locus drift cannot be quotiented as material affine re-anchoring gauge

Wang's smooth material-carrier relay treats common affine re-anchoring of the same carrier as coordinate gauge, while a nondegenerate enstrophy critical locus satisfies a physical relative-current law.  If a material trajectory and critical branch coincide at `t_0`, then
\[
\boxed{\frac d{dt}(x_*-X_m)|_{t_0}=-H_e^{-1}\nabla R.}
\]
When nonzero this separates two physical loci and cannot be removed by re-anchoring without changing the tracked object.  Therefore any literal cross-program construction using an enstrophy-critical candidate must keep the material carrier and critical-locus current/geometry separately, or reconstruct the latter from the Eulerian field and required local jets.  This is not an identification of the actual Kelvin first-bad selector.


## Theorem GP — Enstrophy branch-ranking competition has an exact three-face Navier--Stokes gap law

For two differentiable enstrophy critical objects, `Delta e=e_1-e_2` obeys
\[
\boxed{\dot{\Delta e}=(S_1-S_2)-(K_1-K_2)+(C_1-C_2),}
\]
where `S_i=omega.S.omega`, `K_i=nu|grad omega|^2` is the Kelvin q.v. bulk, and `C_i=nu Delta e` is curvature diffusion.  A transverse crossing is `Delta e=0`, `dot Delta e!=0`; it is a physical rate competition, not a norm threshold.

## Theorem GQ — Exact periodic NSE has a transverse winner crossing with both candidates decaying and with zero nonlinear interaction

For the exact periodic shear in `docs/139_enstrophy_ranking_crossing_event_typing.md`, the critical sheets `y=0,pi` tie at `t_*=1/nu` with value `(9/2)e^{-2}` and active transverse curvatures `-12e^{-2}`, `-60e^{-2}`.  Stretching and local Kelvin q.v. bulk vanish at both sheets, so both branch rates are negative curvature-only rates while `dot Delta e=48 nu e^{-2}>0`; the winner switches because one smooth branch decays faster.  Globally `(u.grad)u=0`.

## Theorem GR — The local velocity 2-jet does not determine enstrophy critical-branch rate even on exact smooth NSE

At the exact crossing of Theorem GQ, the two sheets have identical `u`, `grad u`, and `Hess u`: `U=0`, `U_y=-3e^{-1}`, `U_yy=0`.  But `U_yyy` equals `4e^{-1}` and `20e^{-1}` respectively, producing different `e_yy=U_y U_yyy` and different branch rates.  Therefore no universal branch-rate or post-crossing-winner map can factor through the local velocity 2-jet alone.  The needed third jet/equivalent curvature observable is still part of the already closed common affine quotient; this identifies programme-specific readout order rather than reopening the quotient seam.

## Theorem GS — An enstrophy ranking crossing is not universally a Wang hard interaction event

The exact crossing shear has zero advective nonlinearity everywhere, hence no nonlinear HH work that could create a Wang hard interaction role, while its enstrophy candidate ranking switches transversely.  Since Wang hard roles are created at actual nonlinear work events, branch-ranking crossing and Wang hard interaction are distinct event types absent an independent identifying theorem.

## Theorem GT — A selected ranking scalar can be continuous while its active branch label and derivative switch

For `M(t)=max(e_0,e_pi)` in Theorem GQ, `M` is continuous at the tie but its derivative jumps from `-60 nu e^{-2}` to `-12 nu e^{-2}`.  Thus a selector/readout index can change without a physical scalar-state jump.  Any vector packet jump attached to the new branch is a readout reset and must not be retyped as field production or physical transport.

## Theorem GU — Raw ranking-crossing time does not close hysteretic first-bad event timing

A physical first-bad construction must keep distinct: branch-ranking crossing, critical-geometry degeneracy/support exit, Kelvin physical packet/library event, hysteretic selector/readout event, and Wang hard nonlinear interaction.  Kelvin's hysteretic switch may lag or ignore a raw value crossing according to a separate badness/resolve predicate, while the exact shear proves ranking crossing can occur with no Wang nonlinear event.  Therefore a generic `bad event` quotient or endpoint scalar clock is not compositional; selector history/rule state remains necessary unless NSE supplies an independent timing theorem.


## Theorem GV — Own-local Kelvin current events require an affine target coboundary

If an unreanchored readout `z=x+Omega` obeys the supplied linear event `z_+=A z_-`, then the own-local residual obeys `x_+=A x_-+d` with `d=A Omega_- - Omega_+`.  Consecutive offsets compose by `A_2d_1+d_2=(A_2A_1)Omega_0-Omega_2`.  With a simultaneous selector change, `DeltaY=(E_+A-E_-)X+E_+d`; hence the target offset and its signed second-moment/q.v. cross faces are mandatory and are not contained in the linear tensor-square functor alone.

## Theorem GW — Wang passive carrier reanchoring and Kelvin own-local target reanchoring are inequivalent physical operations

Wang common-slice affine reanchoring is a chart/observer gauge of the same continuing material carrier.  Kelvin own-local target reanchoring can have `A=I` but nonzero `d=Omega_- - Omega_+` and target-gradient Brownian response `G_- - G_+`.  Since it can change the physical residual/q.v. source, it cannot be quotiented as the same passive carrier-coordinate gauge merely because its offset composes as a coboundary.

## Theorem GX — Exact cubic heat-shear NSE activates the target-reanchoring no-go with zero nonlinear advection

For `u=(y^3+6nu t y,0,0)`, `(u.grad)u=0` and the heat equation is exact.  A rectangular Kelvin loop centered at `y=a` has residual-noise coefficient `Q_p=12 b ell (p-a)` against target `p`.  Thus the own target `p=a` gives `Q_a=0`, whereas the same current/frame reanchored to `p=0` gives `Q_0=-12ab ell !=0` with `A=I`.  Target-induced q.v.-source revaluation is therefore neither Wang passive carrier gauge nor a hard nonlinear-work event.

## Theorem GY — Exact periodic NSE heat shears realize arbitrarily many prescribed transverse critical-sheet ranking crossings with zero nonlinear interaction

Given any `N` ordered positive times, choose `N+1` distinct odd Fourier modes and a nonzero coefficient vector annihilating the `N` exponential interpolation rows.  The resulting odd exponential polynomial `O(t)` has exactly those prescribed roots and each is simple by the Chebyshev-system zero theorem.  Adding an even mode `E=B e^{-4nu t}` yields an exact periodic shear with enstrophy gap `Delta e=2 epsilon E O` between the fixed critical sheets `y=0,pi`.  Hence all prescribed roots are transverse ranking crossings while `(u.grad)u=0` identically.  Scaling the odd sector small keeps both sheets strict transverse enstrophy maxima at every crossing.

## Theorem GZ — Ranking/selector event count cannot be a universal Wang hard-generation-depth currency

Theorem GY gives, for every finite `N`, an exact smooth periodic NSE flow with at least `N` prescribed ranking crossings and identically zero nonlinear advection.  Therefore ranking-crossing count, selector-switch count, selector jump variation, or target-induced q.v.-source revaluation cannot universally equal or increment Wang hard nonlinear-work generation depth.  This is a no-go for observer/rule-generated recursion, not a statement that viscous evolution or every other physical owner vanishes.

## Theorem HA — Cross-program event assembly must keep physical owner, target coboundary, selector, and event clock separately typed

For a pure selector reset on a fixed physical library and fixed target, `A=I` and `d=0`, so the underlying physical library has no event while `DeltaY=(E_+-E_-)X` can be nonzero.  The selector therefore cannot add an extra physical-owner vertex by itself.  When a true event and/or target change is simultaneous, the affine readout faces remain mandatory, but they do not license duplicating the underlying NSE owner into extra recurrence generations.  Endogenous selector local finiteness, actual badness/resolve timing, and Wang mixed genuine-owner recurrence remain open.


## Theorem HB — Arbitrary-finite exact-NS ranking crossings produce exactly linear selector-label jump q.v.

In Theorem GY the enstrophy gap is `Delta e=2 epsilon E O` with `E>0`, and the exponential Chebyshev theorem makes the `N` prescribed roots of `O` the only roots and all simple.  Hence the non-hysteretic winner label alternates exactly `N` times.  Encoding the active branch by `q_0=(1,0)`, `q_1=(0,1)` gives `|DeltaY|^2=2` at every switch and therefore
\[
\boxed{\operatorname{tr}\mathcal J_Y=2N.}
\]
For even `N`, the selector endpoint returns to its initial label while this jump variation remains positive, realizing the selector-history non-coboundary on exact smooth NSE.

## Theorem HC — Selector label q.v. can be arbitrarily large while the selected scalar and the Navier--Stokes field remain continuous

For `M=max(e_0,e_pi)`, every ranking tie has zero scalar jump while its one-sided derivative changes by the nonzero transverse gap rate.  Given any finite `L`, Theorem GY with `N>L/2` gives `tr J_Y=2N>L` although the exact periodic shear is smooth and satisfies `(u.grad)u=0` identically.  Thus selector path variation is not a jump of the field or selected scalar and cannot by itself certify hard nonlinear generation.

## Theorem HD — Wang Moyal boundary charge and Kelvin selector jump variation are distinct currencies with the same zero-depth guardrail

Current Wang's same-state selected-family anti-theorem permits exact `R_switch>0` while all coherent cell increments, positive/negative increment work and total state change vanish; the boundary charge itself has zero generation depth.  Repo-3 exact heat shears permit arbitrarily large finite selector-label jump q.v. with zero nonlinear advection.  No equality between these currencies is asserted.  Together they refute the universal implication `positive selection/boundary sidecar => physical nonlinear generation`.

## Theorem HE — Any hard-generation assembly must annihilate the demonstrated pure-sidecar event directions

A recurrence event record must keep underlying physical owner/event `A`, own-local target coboundary `d`, selector change `DeltaE`, and boundary sidecars separately.  Exact counterexamples force any physically faithful hard-generation increment rule to assign zero increment to: a pure selector reset on fixed library/target; a same-state Wang selected-family boundary reread absent independent service/source work; and a pure target q.v.-reanchor witness with zero nonlinear advection.  If a genuine physical event is simultaneous, these faces remain mandatory bookkeeping but may not clone the physical owner into extra generations.  Full factorization through a completed owner quotient is still open.


## Theorem HF — Invertible enstrophy Hessian forces a unique local critical lineage

For a smooth Navier--Stokes solution, let `F=grad e`.  If `F(x_0,t_0)=0` and `H_e=D_xF` is invertible, the implicit-function theorem gives a unique local critical branch `x_*(t)` through `(x_0,t_0)`.  Its differentiated constraint is `H_e xdot_* + partial_t grad e=0`, hence the exact PDE speed law `xdot_*-u=-H_e^{-1}grad R`.  A local isolated critical-lineage birth/death/merge cannot occur at an interior point where this theorem domain remains valid.

## Theorem HG — Critical Morse type is invariant on a connected nondegenerate lineage interval

Along a nondegenerate critical branch, the real-symmetric Hessian eigenvalues vary continuously and none can cross zero while `det H_e!=0`.  Therefore the Hessian inertia, and hence strict maximum/minimum/saddle type, is constant until a degeneracy or theorem-domain exit occurs.

## Theorem HH — Normal nondegeneracy is the correct lineage condition for translation-symmetric critical sheets

For a shear enstrophy `e(y,t)`, if `e_y(y_0,t_0)=0` and `e_yy(y_0,t_0)!=0`, the scalar implicit-function theorem gives a unique local normal critical lineage even though tangent `x,z` Hessian directions vanish by symmetry.  Negative `e_yy` preserves strict normal-max type until normal degeneracy.

## Theorem HI — Exact periodic NSE admits arbitrarily many ranking crossings on one interval with zero normal-geometry events and zero nonlinear advection

In Theorem GY choose a compact interval `K` containing all prescribed crossing times.  With `m_E=min_K E>0`, `M_0=max_K|O|`, `M_2=max_K|O_2|`, choose `epsilon M_0<m_E` and `epsilon M_2<4m_E`.  Then for every `t in K`, the fixed sheets `y=0,pi` have positive vorticity amplitudes and strictly negative normal enstrophy curvatures.  Thus both are persistent strict normal maxima on all of `K`, while the gap `Delta e=2 epsilon E O` retains all `N` prescribed transverse crossings and `(u.grad)u=0` identically.

## Theorem HJ — Ranking, critical-geometry, and hard nonlinear-owner clocks cannot be universally identified

Theorem HI realizes `N_rank=N` with zero tracked normal-degeneracy events on the entire interval and zero nonlinear advection, for arbitrary finite `N`.  Hence ranking/readout crossings cannot universally stand for critical-branch birth/death or Wang hard nonlinear owner events.  Any critical-candidate first-bad state must keep ranking/selector data, the Hessian or appropriate normal-lineage theorem domain, and physical owner/work events separately.  Hysteretic selector timing remains an additional open rule clock.

## Theorem HK — Every moving scalar balance splits into bulk source, physical flux, and relative-boundary sweep

If `div u=0`, `(partial_t+u·grad)f=s+div J`, and `D_t` has boundary velocity `V`, then
\[
\boxed{\frac d{dt}\int_{D_t}f=\int_{D_t}s+\int_{\partial D_t}J\cdot n+\int_{\partial D_t}f(V-u)\cdot n.}
\]
The sweep face depends only on the boundary velocity relative to the material.  Material motion `V=u` and pure tangential relative motion both lie in its kernel.

## Theorem HL — Moving Navier--Stokes enstrophy has an exact four-face owner law

For `e=|omega|^2/2`, every smooth moving control volume satisfies
\[
\boxed{\frac d{dt}\int_{D_t}e=\int_{D_t}\omega\cdot S\omega-\nu\int_{D_t}|\nabla\omega|^2+\nu\int_{\partial D_t}\nabla e\cdot n+\int_{\partial D_t}e(V-u)\cdot n.}
\]
Stretching, bulk viscous loss, diffusive boundary transport and relative-boundary sweep are therefore distinct exact PDE faces.

## Theorem HM — Arbitrary moving loops obey an exact swept-ribbon Kelvin law

For a smooth closed loop `C_t` with point velocity `v` and `w=v-u`, circulation obeys
\[
\boxed{\dot\Gamma=\nu\oint_{C_t}\Delta u\cdot dx-\oint_{C_t}(w\times\omega)\cdot dx=\nu\oint_{C_t}\Delta u\cdot dx+\oint_{C_t}\omega\cdot(w\times dx).}
\]
The second term is vorticity flux through the ribbon swept by the loop relative to the fluid.  Tangential reparameterization contributes zero.

## Theorem HN — Critical-selector boundary currency is driven by relative critical drift, not absolute selector speed

On a nondegenerate enstrophy critical branch, `dot x_*-u=-H_e^{-1}grad R`.  Whenever a control boundary/readout is attached to that branch, the moving-boundary faces in Theorems HK--HM use this relative drift in the active normal direction.  Thus the exact causal chain is local NSE balance -> critical relative drift -> swept-boundary transfer.

## Theorem HO — Exact smooth NSE has a singular critical moving-cut rate with continuous current and zero nonlinear/stretching generation

In the two-mode periodic heat shear, side critical sheets satisfy `d|dot a|->3nu` at their analytic merger.  The one-sided circulation sweep obeys
\[
 d|K'_{sweep}|\to\frac{3\nu\ell e^{-1}}2(1-\cos s)^2,
\]
while circulation remains continuous, `(u·grad)u=0`, and `omega·S omega=0`.  Hence a divergent selector/readout transfer rate is not universally a blow-up, jump atom, or hard-generation event.

## Theorem HP — Endpoint current/residual coalescence does not determine literal transport ancestry

For the same exact merger, common pre-merger Nanson initialization yields `J_{0<-s}=I+Delta gamma_* E_xy != I`, `det J=1`, at the common endpoint, even though anchor, vorticity, circulation, own-local coefficient residual, physical residual and codeforming residual can coincide.  Any ancestry-preserving state map must therefore carry frame/support history, this relative holonomy, or an independently proved equivalent.

## Theorem HQ — Relative-boundary sweep has zero hard-generation depth unless an independent source/work owner is present

A sweep term is genuine transfer and must remain in the exact ledger, but the exact heat-shear witness has nonzero and even singular sweep currency with zero nonlinear advection and zero enstrophy stretching.  Therefore no universal hard-generation rule may increment generation depth from sweep magnitude, sign or singularity alone.

## Theorem HR — Cross-program event assembly has an owner-first triangular order

Exact NSE moving-boundary laws first determine intrinsic source/sink/flux and then the relative-boundary/readout currency.  Independently, current Wang central routing first classifies physical first stops and only then attaches typed material/Moyal sidecars.  These currencies are not identified, but both force the same assembly hygiene: physical owner classification precedes sidecar/readout attachment, and no sidecar or sweep is promoted to hard generation without an independent physical theorem.  First-bad closure and termination remain open.

## Theorem HS — The spatial enstrophy maximum obeys an exact active-owner law

For smooth periodic NSE, `e=|omega|^2/2`, `M(t)=max_x e(x,t)` and active set `A(t)={e=M}`, Danskin's theorem and the local enstrophy PDE give
\[
\boxed{D_+M(t)=\max_{x\in A(t)}[\omega\cdot S\omega-\nu|\nabla\omega|^2+\nu\Delta e].}
\]
At every active maximizer, `grad e=0` and `Delta e<=0`; the advective/readout term is absent exactly.

## Theorem HT — Critical-selector drift changes the maximizing location but contributes zero direct critical-value currency

Along any differentiable active critical branch, `d e(x_*(t),t)/dt=partial_t e` because `grad e=0`, even when `xdot_*-u=-H_e^{-1}grad R` is nonzero or singular.  Thus critical geometry/drift determines where the readout lives, while the local NSE owner determines its value rate.  Ranking switches may change the active branch and derivative, but do not add a selector-speed term.

## Theorem HU — Positive enstrophy-record growth forces stretching to beat the full viscous defect

At an active maximizer define `D_nu=nu(|grad omega|^2-Delta e)>=nu|grad omega|^2>=0`.  Then
\[
D_+M=\max_A[\omega\cdot S\omega-D_\nu].
\]
Hence `D_+M>0` implies an active maximizer with `omega.S.omega>D_nu`.  If `omega!=0`, equivalently `hat omega^T S hat omega>D_nu/(2M)>=0`.  Positive record growth therefore has an intrinsic extensional-vortex-stretching owner and cannot be minted by selector, sweep, gauge, target or boundary sidecar activity alone.

## Theorem HV — The running enstrophy record is a canonical monotone PDE owner clock

Let `R(t)=max_{0<=s<=t}M(s)`.  On every smooth compact interval `R` is absolutely continuous and almost everywhere
\[
\boxed{R'=1_{\{M=R\}}[M']_+=1_{\{M=R\}}\left[\max_A(\omega\cdot S\omega-D_\nu)\right]_+.}
\]
Thus ranking loops, selector jumps, subrecord sweep activity, passive gauge, target coboundaries and inherited/boundary sidecars lie in the record clock's kernel unless an independently present local owner raises the actual physical enstrophy record.

## Theorem HW — Every smooth finite first hit of a higher enstrophy level has a stretching-owned approach sequence

For `L>M(0)` and `tau_L=inf{t:M(t)>=L}<infty`, smoothness gives `M(tau_L)=L` and `M<L` before `tau_L`.  On every interval ending at `tau_L` the running record increases; absolute continuity therefore provides record-growth times `t_n up tau_L` and active maximizers `x_n` with
\[
\boxed{\omega\cdot S\omega(x_n,t_n)>\nu(|\nabla\omega|^2-\Delta e)(x_n,t_n)>=\nu|\nabla\omega|^2(x_n,t_n).}
\]
No transversality of the hit is required.

## Theorem HX — Exact periodic heat shear has curvature-driven record decay and no generation owner

For `u=(A e^{-nu k^2t} sin(ky),0,0)`, stretching and nonlinear advection vanish, while `M=A^2k^2e^{-2nu k^2t}/2` and `M'=-2nu k^2M<0`.  At the active maxima `|grad omega|=0` and the entire viscous defect is `-nu Delta e`.  The existing exact three-mode shear can simultaneously switch the winning critical candidate while both candidate rates are negative, so a selector switch does not imply positive record-owner currency.

## Theorem HY — Exact affine strain--spin NSE activates the record owner by pure stretching

For `a>0`, `Omega=Omega_0 e^{2at}` and
\[
u=(-ax-\Omega y,\Omega x-ay,2az),
\]
`div u=0`, `Delta u=0`, and `A'+A^2=diag(a^2-Omega^2,a^2-Omega^2,4a^2)` is symmetric, hence a quadratic pressure gives an exact smooth Euclidean NSE solution.  Here `omega=(0,0,2Omega)`, `S=diag(-a,-a,2a)`, `M=2Omega^2`, the viscous defect is zero, and
\[
\boxed{M'=4aM=\omega\cdot S\omega>0.}
\]
The exact first hit of `L>M(0)` is `tau_L=(4a)^{-1}log(L/M(0))`.

## Theorem HZ — Finite-time unbounded enstrophy record would require infinite accumulated effective record stretching

For `R(0)>0`, define `G(t)=log(R(t)/R(0))`.  Almost everywhere on smooth record-growth times,
\[
\boxed{G'=1_{\{M=R\}}\frac{[\max_A(\omega\cdot S\omega-D_\nu)]_+}{R}.}
\]
Consequently `R(t)->infty` at finite time would force `G(t)->infty`, i.e. divergent accumulated positive effective stretching on actual record states.  This is only a necessary owner condition; it is not a continuation, termination or global-regularity theorem.

## Theorem IA — Gradient NSE gives an exact strain/vorticity/pressure owner system

With `A=grad u=S+Omega` and `D_t=partial_t+u.grad`, incompressible NSE gives
\[
D_tA=-A^2-Hess p+nu Delta A,
\quad
D_tS=-S^2-Omega^2-Hess p+nu Delta S,
\quad
D_t omega=S omega+nu Delta omega,
\]
and `-Delta p=tr(A^2)=|S|^2-|omega|^2/2`.

## Theorem IB — The stretching owner obeys a three-face exact material law

For `P=omega.S.omega`,
\[
\boxed{D_tP=\omega^TS^2\omega-\omega^T(Hess p)\omega+nu[2(Delta omega)^TS\omega+\omega^T(Delta S)\omega].}
\]
The self-strain face is `|S omega|^2>=0`; pressure curvature and the viscous stretching face are separately typed.

## Theorem IC — Pressure regulation of stretching is an intrinsic nonlocal incompressibility constraint

On the torus, with `q=|S|^2-|omega|^2/2` and mean-zero pressure, `partial_i partial_j p=R_iR_j q`.  Hence the stretching pressure face is `-omega_i omega_j R_iR_j q`.  The local owner rate is therefore constrained by the whole quadratic field through the elliptic pressure solve; the local scalar trace `Delta p` alone does not determine the directional curvature used by `P`.

## Theorem ID — Viscous stretching-owner evolution is diffusion plus signed gradient conversion

The composite viscous face satisfies
\[
\boxed{V_P=nu Delta P-2nu\sum_k(partial_k omega)^TS(partial_k omega)-4nu\sum_k(partial_k omega)^T(partial_kS)omega.}
\]
Thus viscosity is sign-definite in the enstrophy Dirichlet ledger but not a single scalar negative charge in the evolution ledger of the stretching owner itself.

## Theorem IE — Record generation and owner persistence are distinct causal layers

HS--HZ forces every positive enstrophy-record increment through `P>D_nu`.  IB then forces persistence/change of that same `P` through `Q_S+C_p+V_P`.  Positive current stretching therefore does not close its own recurrence law; pressure curvature and viscous conversion remain mandatory physical faces.

## Theorem IF — Exact affine strain--spin NSE realizes pressure reinforcement of self-strain

For constant `a>0`, `Omega=Omega_0e^{2at}`, `u=(-ax-Omega y,Omega x-ay,2az)`, one has `P=8aOmega^2`, `Q_S=16a^2Omega^2`, `C_p=16a^2Omega^2`, `V_P=0`, and
\[
\boxed{D_tP=32a^2Omega^2.}
\]
Pressure curvature is positive and exactly equals the self-strain face in this smooth exact Euclidean calibration.

## Theorem IG — Exact periodic ABC NSE realizes pressure suppression stronger than self-strain

For the viscously decaying unit ABC Beltrami solution and the point `(pi/2,0,0)`, at unit amplitude `P=0`, `Q_S=1`, `C_p=-5`, while `V_P=-3nu P=0`.  Hence
\[
\boxed{D_tP=-4.}
\]
After viscous scaling the value is `-4e^{-4nu t}`.  Exact NSE therefore realizes both signs of the pressure-curvature owner face; pressure is neither a universal sink nor a universal source.

## Theorem IH — Fresh record generation now has a two-level endogenous PDE gate

The first gate is `record growth = stretching P - active viscous/curvature defect`; the second is `D_tP=self-strain square + global pressure curvature + viscous conversion`.  Thus any future recurrence/termination argument must control renewal of stretching through these intrinsic NSE faces rather than count selector, ranking, sweep or sidecar events.  No such renewal bound is yet proved.

## Theorem II — Regular enstrophy superlevel boundaries have an exact owner-driven relative speed

For `Omega_lambda(t)={e>lambda(t)}` and outward normal `n=-grad e/|grad e|`, every regular boundary point obeys
\[
\boxed{(V-u)\cdot n=\frac{R-\dot\lambda}{|\nabla e|},\qquad R=(partial_t+u.grad)e.}
\]
Thus a fixed-level boundary is driven by `R/|grad e|`; the moving readout is generated by the same local NSE owner field rather than by an independent selector mechanism.

## Theorem IJ — Enstrophy superlevel volume is an exact owner-flux observable

Incompressibility and Reynolds transport give
\[
\boxed{\frac d{dt}|\Omega_\lambda|=\int_{\partial\Omega_\lambda}\frac{R-\dot\lambda}{|\nabla e|}\,dS.}
\]
For fixed regular `lambda`, `partial_t V(lambda,t)=int_(e=lambda) R/|grad e| dS`.

## Theorem IK — Moving superlevel enstrophy has an intrinsic four-face ledger

On `e=lambda` with outward normal,
\[
\boxed{\frac d{dt}\int_{\Omega_\lambda}e=\int_{\Omega_\lambda}omega.S.omega-nu\int_{\Omega_\lambda}|grad omega|^2-nu\int_{\partial\Omega_\lambda}|grad e|+lambda\int_{\partial\Omega_\lambda}\frac{R-\dot\lambda}{|grad e|}.}
\]
The final face is signed readout transfer, not fresh stretching generation.

## Theorem IL — Coarea layer-cakes local level-set owner flux into the global enstrophy law

For almost every regular fixed level and smooth periodic NSE,
\[
\boxed{\int_0^\infty\int_{e=\lambda}\frac{R}{|\nabla e|}\,dS\,d\lambda=\int R\,dx=\frac d{dt}\int e\,dx.}
\]
Thus global enstrophy evolution is exactly the all-level integral of local physical level-crossing owner flux.

## Theorem IM — The all-level local owner flux equals the certified global spectral split/merge ledger

Combining IL with BR--BT gives
\[
\boxed{\int_0^\infty\int_{e=\lambda}\frac{R}{|\nabla e|}\,dS\,d\lambda=\mathcal V_{split}-\mathcal V_{merge}-nu Z.}
\]
This closes an exact local-levelset-to-global-spectral bridge, but does not assign individual split/merge atoms to individual level surfaces.

## Theorem IN — Value-threshold motion is a signed readout currency, not a new PDE source

The moving level rule enters the relative flux only through `-dot lambda/|grad e|`; it changes the selected population but not the underlying owner field `R`.  A first-bad construction must therefore derive its threshold/localization rule from a physical obstruction rather than count threshold motion as generation.

## Theorem IO — Exact periodic heat shear realizes fixed-level owner-driven chamber collapse

For `e=M(t)cos^2(ky)`, fixed `0<L<M`, `r=sqrt(L/M)` and `cos^2(ka)=L/M`,
\[
\boxed{\dot a=-nu k\frac r{\sqrt{1-r^2}}=\frac{R}{|e_y|}.}
\]
The shear has zero material normal velocity, so the chamber collapse is exactly the relative level-set owner flux.

## Theorem IP — A co-decaying fractional enstrophy level can be stationary while the field evolves

For `lambda=theta M(t)`, the heat-shear level location is constant and `R-dot lambda=0` on the boundary.  Thus zero moving-readout speed does not imply zero PDE evolution, just as nonzero moving-readout speed does not imply fresh generation.

## Theorem IQ — Kelvin moving-readout composition preserves both level-set sweep and intrinsic ancestry current

If an ancestry density on a compatible observation clock satisfies `partial_t rho+div J_rho=0`, then the signed selected-mass gain density through a moving enstrophy boundary is
\[
\boxed{lambda_partial=(rho V-J_rho).n=rho(R-dot lambda)/|grad e|+(rho u-J_rho).n.}
\]
Thus the NSE level-set sweep and the intrinsic ancestry/Fokker--Planck current are distinct mandatory faces before Kelvin's signed moving mean/covariance revaluation is applied.  For deterministic material transport `J_rho=rho u`, and in Kelvin's exact uniform two-mode shear normal marginal where both intrinsic normal current and `u_n` vanish, this reduces to `rho(R-dot lambda)/|grad e|`.  No fourth selector covariance source appears.  General physical-time/reverse-age clock identification, the actual first-bad level rule, and critical-level topology remain open.

## Theorem IR — Physical volume pushed through local enstrophy obeys an exact one-dimensional continuity law

Let `mu_t=e(.,t)_# dx` and define the signed owner-current measure `j_t` by `int psi(a) dj=int psi(e)R dx`, where `R=D_t e`.  Incompressibility removes the spatial advection face from every test function of `e`, giving
\[
\boxed{\partial_t\mu+\partial_a j=0}
\]
in distributions on enstrophy-value space.  This formulation remains valid at critical values without dividing by `|grad e|`.

## Theorem IS — Regular level-set transport is the density form of the value-space continuity law

At a regular value, `g(a)=int_(e=a)|grad e|^{-1}dS` and `J(a)=int_(e=a)R|grad e|^{-1}dS` satisfy `partial_t g+partial_a J=0`.  Where `g>0`, the conditional owner velocity is `c_e=J/g=E_dx[R|e=a]`, and the superlevel survival function obeys `partial_t V=J`.

## Theorem IT — The value current splits exactly into stretching, vorticity-gradient loss, and curvature redistribution

With `J_P=int_(e=a)(omega.S.omega)/|grad e|`, `B_omega=int_(e=a)|grad omega|^2/|grad e|`, and `K_e=int_(e=a)|grad e|`, periodic integration by parts gives `int_(e=a) Delta e/|grad e|=partial_a K_e` distributionally.  Therefore
\[
\boxed{J=J_P-nu B_omega+nu partial_a K_e.}
\]
Curvature diffusion is a value-space flux derivative, not a new event source.

## Theorem IU — Every convex local-enstrophy moment has an exact stretching-versus-two-viscous-faces law

For `Phi in C^2`,
\[
\boxed{\frac d{dt}\int Phi(e)=\int Phi'(e)omega.S.omega-nu\int Phi'(e)|grad omega|^2-nu\int Phi''(e)|grad e|^2.}
\]
For increasing convex `Phi` both viscous faces are nonpositive.  In particular, for integer `m>=1`, the exact `e^m` hierarchy has the additional negative `m(m-1)nu int e^(m-2)|grad e|^2` face beyond the weighted vorticity-gradient loss.

## Theorem IV — A unique isolated nondegenerate maximum is the characteristic support edge of the value current

If `K=-Hess e(x_*)>0` at the unique maximum `M`, then in three dimensions with `delta=M-a`, `V(a)~(4pi/3)(2delta)^(3/2)/sqrt(det K)` and `g(a)~2^(5/2)pi delta^(1/2)/sqrt(det K)`.  Continuity of `R` gives `J/g -> R(x_*)` as `a up M`; at a differentiability time this is exactly the HS--HZ record speed `M'`.

## Theorem IW — At a tied support edge the bulk conditional current is curvature-volume averaged but the record speed is extremal

For finitely many isolated nondegenerate maxima `x_i` at common value `M`,
\[
\boxed{\lim_{a\uparrow M}J/g=\frac{\sum_i R_i/\sqrt{det K_i}}{\sum_i1/\sqrt{det K_i}},\qquad D_+M=\max_iR_i.}
\]
Thus a generic tie prevents replacement of support-edge lineage selection by the bulk value-space conditional average.

## Theorem IX — Exact three-mode NSE realizes the bulk-edge versus record-edge split

At the GP--GU crossing, the normal maxima have `kappa_0=12e^-2`, `kappa_pi=60e^-2`, `R_0=-12nu e^-2`, `R_pi=-60nu e^-2`.  The normal value-population edge velocity is
\[
\boxed{c_{bulk,edge}=-12\sqrt5\,nu e^{-2},}
\]
while `D_+M=-12nu e^-2` and the left winner rate is `-60nu e^-2`.  Ranking/lineage information is therefore genuinely required at the support edge but does not create a new generation owner.

## Theorem IY — Exact one-mode heat shear is a linear dilation in enstrophy-value space

Per unit tangent area, `g=2/[a(M-a)]^(1/2)`, `J=-2nu k^2 a g`, and `c_e=-2nu k^2a`, hence `partial_tg+partial_a(-2nu k^2a g)=0`.  Its viscous current faces satisfy `B_omega=4k^2 sqrt((M-a)/a)`, `K_e=8k^2 sqrt(a(M-a))`, and `-nu B_omega+nu partial_aK_e=J` exactly.

## Theorem IZ — Enstrophy complexity now has an interior-current / support-edge grammar

The same local owner `R` generates the value-space current, regular superlevel motion, global moment/spectral ledgers, and record-edge motion.  Population/integral readings use the same current; a tied support edge adds the distinct extremal branch-selection law.  The remaining recurrence problem is repeated renewal of support-edge stretching owners under the IA--IH pressure/strain/viscous self-constraint and material/donor ancestry, not raw event counting.
