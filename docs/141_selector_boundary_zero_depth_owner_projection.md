# Selector path variation can grow without nonlinear generation: exact-NS label q.v. and zero-depth owner kernel

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + OPEN BRIDGE**.

Read-only inputs before this batch:

- Wang `94cd83726123814ef7abc19ffa82c9c62a446698`, whose material-sidecar theorem records the exact Moyal selected-family boundary charge and proves by a same-state anti-theorem that this boundary charge itself has zero generation depth.  Genuine material/source recursion still requires independent physical service/source evidence.
- Kelvin `3397d3153d55ec460ac857a9a8d40a172c82779a`, whose current own-local event interface is affine and whose selector remains a readout of a persistent physical library.  Exact-head Action `31679953296` is green.
- Repo-3 Theorem GY, which gives an exact periodic heat-shear construction with any prescribed finite number of transverse enstrophy ranking crossings while nonlinear advection vanishes identically.

The theorem below compares **typing**, not numerical currencies: Wang Moyal boundary energy and Kelvin selector jump q.v. are not identified.

---

## 1. The arbitrary-finite crossing construction forces exactly `N` selector-label switches

Use the exact periodic heat shear from Theorem GY.  For any prescribed

\[
0<t_1<\cdots<t_N,
\]

its two persistent critical-sheet enstrophy values satisfy

\[
\Delta e(t)=e_0(t)-e_\pi(t)=2\varepsilon E(t)O(t),
\qquad E(t)>0,
\]

where `O` is a nonzero exponential polynomial with exactly the `N` prescribed simple zeros.  The exponential Chebyshev zero theorem gives two facts at once:

1. there are no additional zeros;
2. every prescribed zero is simple and therefore changes sign.

Define the non-hysteretic winner label away from ties by the larger branch value and, at each `t_i`, assign the **right-continuous** post-crossing value.  Thus `g` is càdlàg and has no artificial extra jump caused by a tie convention.  Encode it by the one-hot readout

\[
Y(t)=q_{g(t)},
\qquad
q_0=(1,0)^T,
\quad
q_1=(0,1)^T.
\]

Because the sign alternates at each simple crossing, `Y` switches exactly `N` times.  Every selector jump is

\[
\Delta Y=\pm(q_1-q_0),
\]

so

\[
\boxed{\|\Delta Y\|^2=2.}
\]

Therefore the optional selector-label jump quadratic variation on any interval containing all crossings is exactly

\[
\boxed{
\operatorname{tr}\mathcal J_Y
:=\sum_{i=1}^N\|\Delta_iY\|^2
=2N.}
\]

For even `N`, the selector returns to its initial label while

\[
Y(t_{\rm final})=Y(t_{\rm initial}),
\qquad
\operatorname{tr}\mathcal J_Y=2N>0,
\]

which is the finite exact-NS realization of the earlier selector-history non-coboundary law.

**Label: RIGOROUS CONSEQUENCE.**

---

## 2. The selected physical scalar remains continuous through every label jump

Let

\[
M(t)=\max\{e_0(t),e_\pi(t)\}.
\]

At every crossing `t_i`,

\[
e_0(t_i)=e_\pi(t_i),
\]

so

\[
\boxed{M(t_i^-)=M(t_i^+)=M(t_i).}
\]

The one-sided derivatives generally differ by the transverse gap rate,

\[
M'_+(t_i)-M'_-(t_i)=\pm\dot{\Delta e}(t_i),
\qquad
\dot{\Delta e}(t_i)\ne0.
\]

Thus the full Navier--Stokes field is smooth, the two candidate values are smooth, and the selected scalar is continuous, while the **readout label** is càdlàg and carries positive jump q.v.  The jump variation belongs to the selector path, not to a jump of the Eulerian field or of the selected scalar value.

**Label: RIGOROUS CONSEQUENCE.**

---

## 3. Selector path variation can be arbitrarily large while the nonlinear interaction term is identically zero

The same family obeys

\[
\boxed{(u\cdot\nabla)u\equiv0}
\]

for every `N`, because `u=(U(y,t),0,0)` is independent of `x` and each Fourier mode solves the heat equation.

Given any finite `L>0`, choose an integer

\[
N>\frac L2.
\]

Then the exact smooth periodic Navier--Stokes shear satisfies

\[
\operatorname{tr}\mathcal J_Y=2N>L
\]

while nonlinear advection remains zero everywhere and at all times.

Hence no universal physical law may infer a positive **hard nonlinear-generation increment** merely from large selector jump q.v., large selector-switch count, or large selector-label total variation.  Those can all grow by readout competition alone.

This does not say viscosity is absent—the heat evolution is viscous and physical.  It says only that selector path variation is not nonlinear work and cannot manufacture a Wang hard interaction owner that the PDE does not contain.

**Label: COUNTEREXAMPLE/NO-GO.**

---

## 4. Wang supplies an independent same-state boundary-charge anti-theorem

Current Wang proves a complementary statement at the material-sidecar layer.  For two selected families `S_old,S_new` on the **same coherent state**, the exact Moyal boundary currency is

\[
R_{\rm switch}
=\sum_{C\in S_{\rm old}\triangle S_{\rm new}}E_C.
\]

It may satisfy

\[
R_{\rm switch}>0
\]

while every cell energy increment is exactly zero, hence

\[
P_+=P_-=0
\]

and total coherent state energy is unchanged.  Wang therefore classifies the boundary charge itself as zero generation depth; separate physical service/source evidence is required for genuine recursion.

This is **not** an equality

\[
R_{\rm switch}=\operatorname{tr}\mathcal J_Y.
\]

They have different units, constructions, and owners.  The common statement is only the negative one:

\[
\boxed{
\text{positive selection/boundary sidecar}
\centernot\Longrightarrow
\text{physical nonlinear generation}.}
\]

**Label: RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO.**

---

## 5. Necessary owner-projection rule for any recurrence assembly

Let an assembled event record retain separately

\[
\mathfrak E=(A,d,\Delta E,\text{boundary sidecars},\text{physical owners}),
\]

where

- `A` is the underlying physical/library event map;
- `d` is the own-local target coboundary;
- `Delta E` is selector/readout change;
- boundary sidecars include quantities such as Wang `R_switch` or Kelvin optional selector path variation;
- physical owners are independently witnessed NSE work/service/material events.

The exact witnesses above force the following **necessary condition** on any hard-generation increment rule `G`:

1. a pure selector reset with fixed physical library/target cannot contribute hard-generation depth merely because `Delta E !=0`;
2. a same-state Wang selected-family reread cannot contribute hard-generation depth merely because `R_switch>0`;
3. an own-local target reanchor cannot contribute hard nonlinear depth merely because its q.v. source changes—exact cubic heat shear has such a change with zero nonlinear advection.

Equivalently, `G` must annihilate these demonstrated pure-sidecar directions unless a separately typed physical owner is simultaneously present.  If a genuine physical event is simultaneous, the selector/target/Moyal faces remain mandatory for readout and ancestry bookkeeping, but they cannot clone that one physical owner into extra generations.

This is not yet a theorem that **every** admissible recurrence functional factors through one finished quotient: the complete owner algebra and central/joint-stop assembly remain open.  It is a rigorous necessary kernel condition enforced by exact counterexamples.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 6. What remains open

- Kelvin's actual hysteretic badness/resolve functional may not switch at every raw ranking crossing; its endogenous local-finiteness/Tanaka interface is still open.
- Wang's sidecar representation layer is typed, but central/joint-stop integration of zero-depth Moyal boundary currency versus genuine material/source service is still open.
- Simultaneous physical owners must be preserved rather than erased by this zero-depth guardrail.
- No theorem here bounds, terminates, or even instantiates the actual first-bad recurrence tree.

No Zeno exclusion, recurrence assembly, continuation, restart, termination, or global-regularity theorem is claimed.
