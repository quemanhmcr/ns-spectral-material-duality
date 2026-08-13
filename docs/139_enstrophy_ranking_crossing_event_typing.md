# Enstrophy ranking crossing is a readout event, not a hard interaction: exact NS curvature crossing and local-jet no-go

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + OPEN BRIDGE**.

Read-only inputs:

- Wang `ff8259ab5e0a57dfb342b9453f149be95aa3f5d8`: hard roles are created by actual nonlinear interaction/work; a generic common-slice or observer re-anchoring is not a hard physical event.
- Kelvin current head `881bf32adbdcb09376e64c4f466ca93a106660b8`, including `b3c87f7` (`Separate enstrophy branch ranking crossings from degeneracy`), with current-head Action `31678459542` green.  The upstream exact shear crossing is used here read-only and then connected to repo-3 selector/library and Wang event typing.

The result does not identify enstrophy value with the actual Kelvin first-bad badness functional.  It says what must be true **if** a branch-ranking observable of this kind is used.

---

## 1. The two-branch ranking gap keeps the literal three-face Navier--Stokes ledger

For two differentiable enstrophy critical objects, write

\[
e_i(t)=e(x_i(t),t),
\qquad
\Delta e=e_1-e_2.
\]

At a critical point or critical sheet,

\[
\dot e_i
=\mathcal S_i-\mathcal K_i+\mathcal C_i,
\]

with

\[
\mathcal S_i=\omega\cdot S\omega,
\qquad
\mathcal K_i=\nu|\nabla\omega|^2,
\qquad
\mathcal C_i=\nu\Delta e.
\]

Hence

\[
\boxed{
\dot{\Delta e}
=(\mathcal S_1-\mathcal S_2)
-(\mathcal K_1-\mathcal K_2)
+(\mathcal C_1-\mathcal C_2).}
\]

A transverse value crossing satisfies

\[
\Delta e(t_*)=0,
\qquad
\dot{\Delta e}(t_*)\neq0.
\]

This is a competition law between physical mechanisms, not a threshold estimate.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 2. Exact periodic Navier--Stokes has a smooth transverse ranking crossing driven only by curvature

Consider the periodic shear

\[
u=(U(y,t),0,0),
\]

\[
\boxed{
U(y,t)=
-e^{-\nu t}\sin y
-\frac32e^3e^{-4\nu t}\sin 2y
+\frac13e^8e^{-9\nu t}\sin 3y.}
\]

Because the field is independent of `x`,

\[
(u\cdot\nabla)u=0,
\]

and each Fourier mode obeys the heat equation.  Thus constant pressure gives an exact smooth periodic Navier--Stokes solution.

The vorticity is

\[
\omega=(0,0,w),
\]

\[
 w=e^{-\nu t}\cos y
+3e^3e^{-4\nu t}\cos2y
-e^8e^{-9\nu t}\cos3y,
\qquad
e=\frac12w^2.
\]

The sheets `y=0` and `y=pi` are critical for all time.  At

\[
\boxed{t_*=\nu^{-1}}
\]

their values tie:

\[
\boxed{e_0(t_*)=e_\pi(t_*)=\frac92e^{-2}.}
\]

Their active transverse curvatures are nevertheless strictly negative and different:

\[
\boxed{e_{yy}(0,t_*)=-12e^{-2},
\qquad
e_{yy}(\pi,t_*)=-60e^{-2}.}
\]

Because the shear is translation-invariant in `x,z`, these are critical **sheets** and the full three-dimensional Hessian has flat directions.  The theorem here is a transverse critical-sheet calibration, not a full isolated-Hessian crossing example.

At both sheets,

\[
\omega\cdot S\omega=0,
\qquad
\nabla\omega=0.
\]

Therefore both rates are purely curvature diffusion:

\[
\dot e_0=-12\nu e^{-2}<0,
\qquad
\dot e_\pi=-60\nu e^{-2}<0,
\]

while

\[
\boxed{\dot{\Delta e}(t_*)=48\nu e^{-2}>0.}
\]

So the winner changes even though **both candidates are decreasing** and neither stretching nor local Kelvin q.v. bulk drives the crossing.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 3. Exact NSE local 2-jet no-go: equal `u`, `grad u`, and `Hess u` do not determine the branch rate

At the crossing time, differentiate the exact shear profile.  At both `y=0` and `y=pi`,

\[
U=0,
\qquad
U_y=-3e^{-1},
\qquad
U_{yy}=0.
\]

Thus the complete local velocity jets through order two agree at the two sheets:

\[
\boxed{j^2u(0,t_*)=j^2u(\pi,t_*).}
\]

Equivalently, the local velocity, velocity gradient, vorticity, first vorticity derivative and second velocity derivative are all tied.

But the third derivative differs:

\[
\boxed{U_{yyy}(0,t_*)=4e^{-1},
\qquad
U_{yyy}(\pi,t_*)=20e^{-1}.}
\]

Since

\[
e=\frac12U_y^2,
\]

and `U_yy=0` at the two sheets,

\[
e_{yy}=U_yU_{yyy}.
\]

Hence the equal 2-jets produce different curvature rates and opposite future ranking slopes solely because the third jet differs.

Therefore no universal branch-rate or post-crossing-winner map can factor through the local velocity 2-jet alone, even on exact smooth periodic Navier--Stokes data.  One must retain the needed higher physical jet (here order three), an equivalent curvature/growth observable, or the full Eulerian field from which it is reconstructed.

This does **not** reopen the repo-3 affine-quotient seam: all `p>=2` physical jets still belong to the same common affine quotient.  It identifies which programme-specific readout order the actual ranking law needs.

**Label: COUNTEREXAMPLE/NO-GO + EXACT NSE/PDE IDENTITY.**

---

## 4. A ranking crossing is not a Wang hard nonlinear interaction

The same exact shear has

\[
\boxed{(u\cdot\nabla)u=0}
\]

globally.  There is no nonlinear HH transfer to create a Wang hard interaction role at the ranking-crossing time.  Nevertheless the two enstrophy critical sheets exchange which one has the larger value, transversely and with a nonzero physical gap rate.

Wang's smooth material-carrier theorem explicitly reserves hard-role creation for actual nonlinear interaction/work.  Therefore

\[
\boxed{
\text{enstrophy ranking crossing}
\not\equiv
\text{Wang hard interaction event}.}
\]

The crossing is also not a physical jump of the Navier--Stokes field: the field remains smooth and solves the heat-reduced NSE exactly.

**Label: COUNTEREXAMPLE/NO-GO.**

---

## 5. The selected scalar can remain continuous while the active branch index and derivative switch

For the non-hysteretic envelope

\[
M(t)=\max\{e_0(t),e_\pi(t)\},
\]

the tie gives

\[
M(t_*^-)=M(t_*^+)=\frac92e^{-2}.
\]

But the one-sided derivatives are

\[
M'_-(t_*)=-60\nu e^{-2},
\qquad
M'_+(t_*)=-12\nu e^{-2},
\]

so

\[
\boxed{M'_+(t_*)-M'_-(t_*)=48\nu e^{-2}.}
\]

Thus the selected scalar state has no jump while its active branch label changes and the derivative kinks.  If a vector packet/residual readout is attached to the branch, that readout may jump even though the scalar ranking value is continuous; repo-3's selector/library theorem already shows that equal scalar/selected blocks do not determine the hidden branch state.

A readout jump must therefore not be retyped as a physical field jump or as positive production.

**Label: RIGOROUS CONSEQUENCE.**

---

## 6. OPEN BRIDGE — hysteresis and event clocks remain separate physical/rule data

Kelvin's actual first-bad selector is hysteretic.  A raw branch-value crossing does not by itself determine the switch time: the previous active index may be retained until a separately specified resolve/badness condition fires.

The physical event taxonomy now contains at least five distinct clocks/faces:

1. branch-ranking crossing (`Delta e=0`);
2. critical-geometry degeneracy/birth/death (loss of the appropriate Hessian/implicit-function condition or support boundary);
3. Kelvin physical packet/library event;
4. Kelvin selector/readout event, possibly hysteretic;
5. Wang hard nonlinear interaction/work event.

The exact shear above proves that items 1 and 5 can separate completely.  Upstream critical geometry proves that ranking crossing and branch degeneracy are not algebraically identical.  Repo-3's selector algebra proves that a selector switch is not universal physical transport.

Therefore a literal cross-program state/event map must preserve the event type and its clock/history unless a separate Navier--Stokes theorem identifies two of them.  A generic `bad event` quotient is not physically admissible.

**Label: OPEN BRIDGE + COUNTEREXAMPLE/NO-GO.**

No recurrence, continuation, termination, or global-regularity theorem is claimed.
