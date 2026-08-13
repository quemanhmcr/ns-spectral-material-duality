# Critical-lineage persistence and event-clock separation in exact Navier--Stokes

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + OPEN BRIDGE**.

Read-only truth before this batch:

- Kelvin `3397d3153d55ec460ac857a9a8d40a172c82779a` explicitly separates critical-point motion, Hessian degeneracy, branch-value crossing, and selector hysteresis; its exact heat-shear calibration has persistent critical sheets through a transverse value crossing.
- Wang `94cd83726123814ef7abc19ffa82c9c62a446698` keeps hard generation attached to actual physical service/work rather than selection/boundary bookkeeping.
- Repo-3 Theorem GY constructs exact periodic heat shears with any prescribed finite number of ranking crossings and zero nonlinear advection.

No upstream write was made.

---

## 1. Invertible enstrophy Hessian forces a unique local critical lineage

Let a smooth Navier--Stokes solution be given on a time interval and put

\[
e(x,t)=\frac12|\omega(x,t)|^2.
\]

Define

\[
F(x,t)=\nabla e(x,t).
\]

Suppose

\[
F(x_0,t_0)=0,
\qquad
H_e(x_0,t_0):=D_xF(x_0,t_0)=\nabla^2e(x_0,t_0)
\]

is invertible.  The ordinary implicit-function theorem then gives neighborhoods of `x_0,t_0` and a **unique** smooth local branch

\[
x_*(t_0)=x_0,
\qquad
\nabla e(x_*(t),t)=0.
\]

Differentiating this exact constraint recovers the previously derived speed law

\[
\boxed{
H_e\dot x_*+\partial_t\nabla e=0,}
\]

hence, after inserting the literal enstrophy PDE,

\[
\boxed{
\dot x_*-u
=-H_e^{-1}\nabla R,
\qquad
R=\omega\cdot S\omega-\nu|\nabla\omega|^2+\nu\Delta e.}
\]

Therefore an isolated nondegenerate critical object cannot be born, die, merge, or lose its unique local lineage **at a time where its Hessian remains invertible**.  Local lineage failure requires leaving the theorem domain: Hessian degeneracy, loss of the required smooth/support chart, or an external boundary of the chosen localization.

**Label: RIGOROUS CONSEQUENCE + EXACT NSE/PDE IDENTITY.**

---

## 2. Morse type is rigid until a Hessian eigenvalue reaches zero

Along a nondegenerate critical branch, `H_e(t)` is a continuous real symmetric matrix.  Its eigenvalues are continuous.  As long as

\[
\det H_e(t)\ne0,
\]

no eigenvalue can cross zero, so the inertia

\[
(n_+(H_e),n_-(H_e))
\]

is constant.

Hence a strict enstrophy maximum remains a strict maximum, a strict minimum remains a strict minimum, and a saddle keeps the same Morse index throughout any connected nondegenerate lineage interval.  A change of Morse type requires Hessian degeneracy.

This is a geometry theorem, not an energy estimate.

**Label: RIGOROUS CONSEQUENCE.**

---

## 3. Translation-symmetric critical sheets have the analogous normal-lineage law

The periodic heat-shear witnesses are independent of `x,z`, so their full three-dimensional Hessian has tangent zero modes.  The correct physical geometry is the normal coordinate `y`.

If

\[
\partial_y e(y_0,t_0)=0,
\qquad
\partial_{yy}e(y_0,t_0)\ne0,
\]

then the one-dimensional implicit-function theorem applied to `partial_y e` gives a unique local normal critical branch `y_*(t)`.  If

\[
\partial_{yy}e<0,
\]

through an interval, the corresponding translation-invariant sheet remains a strict **normal** enstrophy maximum throughout that interval.

Thus tangent symmetry degeneracy must not be confused with loss of the active normal critical geometry.

**Label: RIGOROUS CONSEQUENCE.**

---

## 4. The arbitrary-finite exact-NS crossing family can be made normally nondegenerate on one whole compact interval

Take any finite prescribed times

\[
0<t_1<\cdots<t_N
\]

and choose a compact interval

\[
K=[T_-,T_+]
\]

with all `t_i` in its interior.  In Theorem GY write

\[
E(t)=B e^{-4\nu t}>0,
\qquad
O(t)=\sum_j a_j e^{-\nu n_j^2t},
\qquad
O_2(t)=\sum_j n_j^2a_j e^{-\nu n_j^2t}.
\]

On compact `K` define

\[
m_E=\min_K E>0,
\qquad
M_0=\max_K|O|,
\qquad
M_2=\max_K|O_2|.
\]

Choose `epsilon>0` so small that

\[
\boxed{
\varepsilon M_0<m_E,
\qquad
\varepsilon M_2<4m_E.}
\]

For the exact shear vorticity amplitude,

\[
w_0=E+\varepsilon O,
\qquad
w_\pi=E-\varepsilon O,
\]

and

\[
\partial_{yy}w(0,t)=-4E-\varepsilon O_2,
\qquad
\partial_{yy}w(\pi,t)=-4E+\varepsilon O_2.
\]

Because `w_y=0` on both sheets,

\[
\partial_{yy}e=w\,\partial_{yy}w.
\]

The two smallness conditions imply, for every `t in K`,

\[
w_0>0,
\qquad
w_\pi>0,
\]

and

\[
\partial_{yy}w(0,t)<0,
\qquad
\partial_{yy}w(\pi,t)<0.
\]

Therefore

\[
\boxed{
\partial_{yy}e(0,t)<0,
\qquad
\partial_{yy}e(\pi,t)<0
\quad\text{for every }t\in K.}
\]

Both critical sheets are strict normal maxima on the **entire compact interval**.  There is no normal critical-geometry degeneracy anywhere in `K`.

The ranking gap remains

\[
\Delta e=2\varepsilon E O,
\]

so the prescribed `N` simple ranking crossings are unchanged by making `epsilon` small.

Finally, the velocity is still a heat shear:

\[
\boxed{
U_t=\nu U_{yy},
\qquad
(u\cdot\nabla)u=0.}
\]

Thus one exact smooth Navier--Stokes interval can contain arbitrarily many prescribed finite ranking crossings while both candidate geometries persist normally and no nonlinear hard interaction occurs.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 5. Three event clocks are provably independent in the direction needed for assembly hygiene

On the compact interval `K` above:

- ranking/readout clock: `N` transverse crossings occur;
- critical-geometry clock: zero normal-degeneracy events occur on the two tracked sheets;
- nonlinear-owner clock: `(u·grad)u=0` identically.

Hence for every finite `N`, exact smooth periodic NSE realizes

\[
\boxed{
N_{\rm rank}=N,
\qquad
N_{\rm normal\ geom}=0,
\qquad
\text{nonlinear advection}=0.}
\]

This proves a strong one-way independence: ranking activity can be arbitrarily rich while the other two event mechanisms remain absent on the tracked interval.

Therefore none of the following universal identifications is admissible:

\[
\text{ranking crossing}
=\text{critical-geometry birth/death},
\]

\[
\text{ranking crossing}
=\text{Wang hard nonlinear owner event}.
\]

A hysteretic Kelvin selector is a fourth rule clock and may switch at neither, either, or a delayed time depending on its still-open badness/resolve rule.

**Label: COUNTEREXAMPLE/NO-GO.**

---

## 6. State-map consequence: carry the geometry domain, not merely the winner

Any literal first-bad state that uses a critical candidate must preserve enough information to distinguish

1. the ranking value/gap;
2. the active branch label and selector history;
3. the critical-lineage domain (`H_e` for isolated points, or the appropriate normal Hessian/shape operator for critical sheets);
4. actual physical owner/work events.

A winner label or scalar badness score cannot reconstruct whether the underlying critical object is nondegenerate, what its Morse/normal type is, or whether a physical interaction occurred.  Conversely, nondegeneracy alone does not determine ranking.

The branch-persistence theorem therefore sharpens the state-map seam from “keep geometry somehow” to a necessary theorem domain: if an inverse-Hessian current law is used, its nondegeneracy/support chart must itself remain visible to the event logic.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 7. What remains open

- the actual Kelvin badness/resolve functional and whether its candidates are enstrophy critical objects at all;
- global continuation of a critical lineage beyond local IFT charts;
- critical-manifold bifurcation theory when symmetries break or normal rank changes;
- support/local packet exit and target-anchor reassignment;
- Wang central/joint-stop recurrence with genuine material/source owners;
- any assembly or termination theorem.

No local IFT statement is promoted to Navier--Stokes continuation.  No Zeno exclusion, restart, recurrence termination, or global-regularity theorem is claimed.
