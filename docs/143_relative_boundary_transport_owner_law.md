# Relative-boundary transport and owner-first event law

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + OPEN BRIDGE**.

Read-only upstream truth before this batch:

- Wang `24a725798948d7067afae1976afb9c712fb23b47` has routed typed material sidecars through the central/joint-stop layer without promoting selected-family Moyal boundary currency into a physical first stop.  The order is explicitly physical stop first, sidecar second; genuine `MATERIAL_RELINK` remains genuine when independently witnessed.
- Kelvin `4888b6e19293edc0950047fd2e52ad6b64fbe3ac` has proved on the exact critical-sheet merger calibration that the Eulerian critical path, the literal Kelvin/material ancestry path, and the Nanson-transported packet geometry are distinct.  The critical-sheet cusp is exactly a moving-cut circulation flux, and Nanson frame history remains different at the merger even when endpoint anchor/vorticity and residual fiber coalesce.
- Repo-3 Theorems GL--HJ already separate critical drift, ranking, selector history, target coboundary, geometry clock and hard nonlinear owner.

No upstream write is made in this batch.

---

## 1. General moving-balance identity: the selector enters only through relative boundary velocity

Let `D_t` be a smooth moving control volume with boundary velocity `V`, let `u` be incompressible, and suppose a scalar density `f` obeys the exact local balance

\[
(\partial_t+u\cdot\nabla)f=s+\nabla\cdot J.
\]

Because `div u=0`,

\[
\partial_t f+\nabla\cdot(uf)=s+\nabla\cdot J.
\]

Reynolds transport gives

\[
\boxed{
\frac{d}{dt}\int_{D_t}f
=
\int_{D_t}s
+\int_{\partial D_t}J\cdot n
+\int_{\partial D_t}f\,(V-u)\cdot n .}
\]

There are three intrinsically different faces:

1. bulk production/destruction `s`;
2. physical flux `J` through the current boundary;
3. **swept-boundary transfer** caused only by the boundary moving relative to the material.

The last face depends on `V-u`, not on `V` alone.  If the control volume is material (`V=u` on the boundary), it vanishes identically.  If `V-u` is purely tangential, it also vanishes identically.

Thus absolute selector speed is not an intrinsic owner currency.  Only transverse crossing relative to the material can alter the inventory through the moving-boundary face.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 2. Navier--Stokes enstrophy gives an exact four-face owner decomposition

For

\[
e=\frac12|\omega|^2,
\]

the exact local enstrophy equation is

\[
(\partial_t+u\cdot\nabla)e
=
\omega\cdot S\omega
-\nu|\nabla\omega|_F^2
+\nu\Delta e.
\]

Apply the moving-balance identity with

\[
s=\omega\cdot S\omega-\nu|\nabla\omega|_F^2,
\qquad
J=\nu\nabla e.
\]

Then every smooth moving control volume satisfies

\[
\boxed{
\frac{d}{dt}\int_{D_t}e
=
\underbrace{\int_{D_t}\omega\cdot S\omega}_{\text{stretching face}}
-
\underbrace{\nu\int_{D_t}|\nabla\omega|_F^2}_{\text{bulk viscous loss}}
+
\underbrace{\nu\int_{\partial D_t}\nabla e\cdot n}_{\text{diffusive boundary face}}
+
\underbrace{\int_{\partial D_t}e\,(V-u)\cdot n}_{\text{relative sweep face}}.}
\]

The relative sweep face is a real transfer of already existing enstrophy inventory across the observation boundary.  It is not a gauge and it must not be erased from an exact local budget.  But it is also not the same physical type as the stretching source or viscous destruction.

This distinction is the first literal owner typing forced directly by the PDE rather than by an abstract event ledger.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 3. Arbitrary moving loops satisfy a swept-ribbon Kelvin law

Let `C_t` be a smooth closed loop with point velocity `v`, and define its circulation

\[
\Gamma(t)=\oint_{C_t}u\cdot dx.
\]

Write the relative loop velocity

\[
w=v-u.
\]

Differentiating the moving line integral gives

\[
\frac{d\Gamma}{dt}
=
\oint_{C_t}
\left[
\partial_tu+(v\cdot\nabla)u+(\nabla v)^Tu
\right]\cdot dx.
\]

Insert Navier--Stokes and use

\[
(\nabla u)^Tu=\nabla\frac{|u|^2}{2},
\]

and

\[
(w\cdot\nabla)u+(\nabla w)^Tu
=\nabla(u\cdot w)-w\times\omega.
\]

All gradients integrate to zero around the closed loop.  Hence

\[
\boxed{
\frac{d\Gamma}{dt}
=
\nu\oint_{C_t}\Delta u\cdot dx
-
\oint_{C_t}(w\times\omega)\cdot dx.}
\]

Equivalently, by the scalar triple product,

\[
\boxed{
\frac{d\Gamma}{dt}
=
\nu\oint_{C_t}\Delta u\cdot dx
+
\oint_{C_t}\omega\cdot(w\times dx).}
\]

The second term is exactly the vorticity flux through the infinitesimal ribbon swept by the loop **relative to the fluid**.

If `w=0`, the ordinary material Kelvin law is recovered.  If `w` is tangent to the loop, then `(w\times\omega)\cdot dx=0`; pure reparameterization is invisible.  Only transverse relative motion contributes.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 4. Critical selectors plug into these laws through the already-forced relative critical drift

On a differentiable nondegenerate enstrophy critical branch, repo-3 Theorem GL gives

\[
\boxed{
\dot x_*-u=-H_e^{-1}\nabla R,
\qquad
R=\omega\cdot S\omega-\nu|\nabla\omega|^2+\nu\Delta e.}
\]

Therefore whenever a sheet-attached moving boundary is generated by such a critical selector, its new boundary currency enters through the **relative drift**

\[
V-u,
\]

not through the absolute critical speed.  In the active normal direction the sweep face is therefore controlled by the PDE-generated critical drift itself.

This gives a direct chain

\[
\boxed{
\text{local NSE balance}
\longrightarrow
\text{critical relative drift}
\longrightarrow
\text{moving-boundary transfer}.}
\]

Nothing in this chain creates a new source by changing readout coordinates.  It only says how a PDE-generated selector cuts across the physical inventory/current already present.

**Label: RIGOROUS CONSEQUENCE.**

---

## 5. Exact heat-shear merger: a singular selector rate produces a singular boundary-transfer rate but no fluid singularity and no jump atom

Use Kelvin's exact two-mode periodic heat shear

\[
u=(U(y,t),0,0),
\qquad
U=-e^{-\nu t}\sin y-\frac{e^3}{8}e^{-4\nu t}\sin2y,
\]

with

\[
q=-U_y
=e^{-\nu t}\cos y+\frac{e^3}{4}e^{-4\nu t}\cos2y.
\]

The nonlinear advection is identically zero and `U_t=nu U_yy`.

For the side critical sheets write

\[
a_\pm=\pi\pm d,
\qquad
\cos d=e^{3(\nu t-1)},
\qquad
T=\nu^{-1}.
\]

Then

\[
|\dot a_\pm|=3\nu\cot d,
\qquad
d|\dot a_\pm|\to3\nu.
\]

For the one-sided `xy` circulation cut

\[
K(a,t)=\ell\int_a^{a+s}q(y,t)\,dy,
\]

the swept-ribbon law becomes exactly

\[
\boxed{
\dot K
=
\ell\nu[q_y(a+s)-q_y(a)]
+
\ell\dot a[q(a+s)-q(a)].}
\]

At the merger,

\[
q(\pi+s,T)-q(\pi,T)
=\frac{e^{-1}}2(1-\cos s)^2,
\]

so

\[
\boxed{
 d|K'_{\rm sweep}|
\to
\frac{3\nu\ell e^{-1}}2(1-\cos s)^2.}
\]

The instantaneous boundary-transfer rate diverges like `1/d`, but the field is an analytic finite Fourier polynomial and the circulation itself is continuous because `(a(t),t)->(pi,T)` and `K(a,t)` is smooth in `(a,t)`.

Moreover the side cut is monotone and has finite geometric variation

\[
\int_{t_0}^{T}|\dot a_\pm|dt=d(t_0)<\pi.
\]

Thus a divergent selector/readout rate is not by itself a physical blow-up, a finite jump atom, or a hard-generation event.

The moving enstrophy slab obeys the analogous exact decomposition with zero stretching face in this shear:

\[
\frac{d}{dt}\int_{a(t)}^{a(t)+s}e\,dy
=
-\nu\int_a^{a+s}q_y^2\,dy
+\nu[e_y(a+s)-e_y(a)]
+\dot a[e(a+s)-e(a)].
\]

Again the singular term is the relative sweep face, not a nonlinear source.

**Label: EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO.**

---

## 6. Endpoint residual coalescence does not determine transport ancestry

Along a chosen sheet history, let the local line frame obey the literal Nanson deformation connection

\[
\dot L=(\nabla u)(a(t),t)L.
\]

For the heat shear,

\[
\nabla u=-qE_{xy},
\qquad
E_{xy}^2=0,
\]

so with common initial frame

\[
L_b(t)=(I+\gamma_b(t)E_{xy})L_{\rm init},
\qquad
\dot\gamma_b=-q_b.
\]

Kelvin's exact critical-sheet calculation gives, throughout the pre-merger interval,

\[
q_s-q_0
=-e^{-\nu t}\frac{(1-r)^2}{2r}<0,
\qquad
r=e^{3(\nu t-1)}.
\]

Hence equal central/side initial frames acquire a nonzero merger history gap

\[
\Delta\gamma_*=\gamma_0(T)-\gamma_s(T)\ne0.
\]

The endpoint comparison is

\[
\boxed{
J_{0\leftarrow s}=L_0L_s^{-1}
=I+\Delta\gamma_*E_{xy}\ne I,
\qquad
\det J_{0\leftarrow s}=1.}
\]

Yet for the same endpoint anchor and the same one-sided support width, the `xy` circulation, own-local target, coefficient residual, physical residual and codeforming residual can all coincide because the vorticity is purely `z`-directed while the history shear sits in the transverse support/frame components.

Therefore

\[
\boxed{
\text{endpoint current/residual fiber}
\not\Rightarrow
\text{transport ancestry state}.}
\]

Any state map that must preserve literal transported ancestry has to carry the frame/support history, the relative holonomy `J`, or some independently proved equivalent.  Endpoint residual coalescence alone is insufficient.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO.**

---

## 7. The new owner kernel: boundary transfer has physical meaning but zero hard-generation depth unless a source/work owner is independently present

The preceding identities force a sharper typing than “physical versus gauge”.

A moving-boundary sweep is physically meaningful: it transfers existing inventory/current because the observation boundary crosses material.  Therefore it must remain in the exact ledger.

But exact heat shear simultaneously has

\[
(u\cdot\nabla)u=0,
\qquad
\omega\cdot S\omega=0,
\]

while its critical moving-cut circulation/enstrophy sweep rate can be nonzero and even diverge like `1/d` near the smooth merger.

Hence no universal hard-generation rule may infer new nonlinear/source depth from the magnitude, positivity or singularity of a moving-boundary currency alone.

The necessary rule is

\[
\boxed{
\text{boundary/readout transfer}
\neq
\text{source/work generation};
}
\]

and a hard-generation depth increment must require an independently witnessed source/work owner on the relevant physical channel.

This extends Theorem HE: the zero-depth kernel is not restricted to passive gauges and finite selector/Moyal sidecars.  It also contains the **generation-depth component** of pure relative-boundary sweep events, while preserving their nonzero transfer ledger.

**Label: COUNTEREXAMPLE/NO-GO + RIGOROUS CONSEQUENCE.**

---

## 8. Owner-first triangularity now appears independently on both sides of the bridge

The exact PDE transport laws have the causal order

\[
\boxed{
\text{NS field/material state}
\longrightarrow
\text{relative boundary/selector motion}
\longrightarrow
\text{observed moving-cut currency}.}
\]

The selector can be endogenous because it is computed from the field, but its boundary currency is still a readout/transfer consequence of the already-given physical state and relative motion; it does not retroactively create the PDE source that generated the field.

Independently, current Wang central routing has the exact event order

\[
\boxed{
\text{independently witnessed physical stop}
\longrightarrow
\text{attach typed material/Moyal sidecar}.}
\]

These are not the same mathematical currency and are not identified.  What is common is the **triangular causal rule**:

> classify the intrinsic physical owner/source/transport first; then attach boundary/readout/selection currencies in their own slots; never promote a sidecar or sweep currency into hard generation without an independent physical theorem.

This is now supported by exact Navier--Stokes transport identities on the Kelvin side and by current exact central routing on the Wang side.

It is still an **OPEN BRIDGE** to prove that the actual programme first-bad/badness/resolve mechanism factors through this owner-first architecture and yields any recurrence/termination theorem.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 9. What this changes in the frontier

The event state should no longer be thought of as one undifferentiated jump charge.  At minimum it must distinguish

\[
\boxed{
\text{intrinsic source/sink}
+\text{physical flux}
+\text{relative-boundary sweep}
+\text{selector/target/boundary sidecars}
+\text{transport ancestry memory}.}
\]

The next literal seam is therefore narrower:

1. identify the actual first-bad observable/control object in the programme;
2. derive its exact moving-boundary/source/flux law from NSE;
3. bind its selector speed to the critical-current or other PDE-generated relative-motion law;
4. carry transport ancestry through collision by `L/H/J` or an equivalent physical state;
5. only then define hard-generation depth and attempt local finiteness/termination.

No Zeno exclusion, recurrence assembly, restart, continuation or global-regularity theorem is claimed here.


## 10. Action certification

The theorem batch is executable at repo-3 SHA `f3ca29119ceab9cb0a56b36e6df1ea5c0771803b`.  GitHub Actions run `31685600783` completed **success**.  The exact exp93 log reports:

- moving-loop Kelvin/Reynolds residual `2.696e-16`;
- heat-equation residual `1.201e-16`;
- moving-slab enstrophy four-face residual `7.720e-16`;
- nonzero moving-slab sweep signal `1.021614e+01`;
- tangential relative-motion kernel residual `5.572e-16`;
- critical-merger distance-weighted sweep coefficient `4.028288033e-02`;
- smallest-`d` coefficient residual `1.259e-04`;
- smallest-`d` circulation continuity error `3.633e-05`;
- Nanson merger history `Delta gamma=-5.167864107`;
- endpoint residual-fiber tie residual `0`;
- transport-frame history separation `5.529615`;
- holonomy separation from identity `5.167864`;
- holonomy determinant-one residual `1.110e-16`;
- nonlinear advection `0`;
- enstrophy stretching face `0`;
- final status: **PASS**.

**Label: ACTION STRESS TEST.**
