# Enstrophy critical current is not a material carrier: exact NSE relative drift and curvature-volume law

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + OPEN BRIDGE**.

Read-only inputs for this batch:

- Wang latest audited head `ff8259ab5e0a57dfb342b9453f149be95aa3f5d8`.  Its smooth material-carrier relay distinguishes a continuing material carrier from observer re-anchoring: affine re-anchoring is gauge composition and hardening occurs only at a genuine physical interaction.
- Kelvin latest audited head `54d8a361a6a3697e919484f24869ff880867b03d`.  The exact PDE results used here were introduced at `37c635fc3f9ab61d62b86c61796b7170a00c5ce4` (local enstrophy growth), `c27d1f1dce0edecd0dba267af2befa6167168203` (nondegenerate critical-point speed), and `884956e61451649d33b207a60f960970b6900e65` (critical-Hessian evolution).  Their exact-head upstream Actions are green.

Nothing below identifies an enstrophy critical point with Kelvin's actual first-bad germ.  The statements are conditional physical laws that any such critical-point candidate must obey.

---

## 1. Start from the literal local enstrophy PDE

Let

\[
e=\frac12|\omega|^2,
\qquad
S=\frac12(\nabla u+\nabla u^T).
\]

For incompressible Navier--Stokes,

\[
\boxed{
(\partial_t+u\cdot\nabla)e
=R,
\qquad
R:=\omega\cdot S\omega
-\nu|\nabla\omega|_F^2
+\nu\Delta e .}
\]

The three local faces are physically different:

1. vortex stretching `omega.S.omega`;
2. viscous/Kelvin orientation-complete q.v. bulk `nu |grad omega|^2`;
3. spatial curvature diffusion `nu Delta e`.

Using the already exact Kelvin packet dictionary,

\[
\frac12\operatorname{tr}(\Gamma_H M_H)
=\nu|\nabla\omega|_F^2,
\]

so one may equivalently write

\[
\boxed{
R=\omega\cdot S\omega
-\frac12\operatorname{tr}(\Gamma_HM_H)
+\nu\Delta e .}
\]

This is not a norm estimate.  It is the pointwise PDE balance itself.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 2. A nondegenerate critical point has its own PDE-forced current

Let `x_*(t)` be a differentiable enstrophy critical branch,

\[
\nabla e(x_*(t),t)=0,
\]

and write

\[
H_e=\nabla^2e(x_*(t),t).
\]

Differentiate the critical constraint:

\[
0=\partial_t\nabla e+H_e\dot x_*.
\]

Taking one spatial gradient of the scalar PDE gives

\[
\partial_t\nabla e+\nabla(u\cdot\nabla e)=\nabla R.
\]

At a critical point `grad e=0`,

\[
\nabla(u\cdot\nabla e)=H_eu.
\]

Therefore

\[
\boxed{
H_e(\dot x_*-u)+\nabla R=0.}
\]

If the critical point is nondegenerate,

\[
\boxed{
\dot x_*-u=-H_e^{-1}\nabla R.}
\]

Thus the critical branch has a literal **relative current** with respect to the material flow.  Its three physical driving faces are the gradients of stretching, Kelvin q.v. bulk, and curvature diffusion:

\[
\boxed{
\dot x_*-u
=-H_e^{-1}\nabla(\omega\cdot S\omega)
+H_e^{-1}\nabla(\nu|\nabla\omega|_F^2)
-\nu H_e^{-1}\nabla\Delta e.}
\]

The critical tracker is material exactly when `grad R=0` on the nondegenerate branch.  Materiality is therefore a theorem condition, not a default interpretation.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 3. Exact ABC Navier--Stokes gives a strict nondegenerate critical maximum that is not material

Take the standard equal-parameter ABC Beltrami field with viscous amplitude

\[
a(t)=A e^{-\nu t},
\]

\[
u=a(t)
\begin{pmatrix}
\sin z+\cos y\\
\sin x+\cos z\\
\sin y+\cos x
\end{pmatrix},
\qquad
\omega=u.
\]

With pressure `p=-|u|^2/2`, this is an exact smooth periodic Navier--Stokes solution because

\[
(u\cdot\nabla)u=\nabla\frac{|u|^2}{2},
\qquad
\Delta u=-u,
\qquad
\partial_tu=-\nu u.
\]

At

\[
x_*=\left(\frac\pi4,\frac\pi4,\frac\pi4\right),
\]

the spatial ABC shape is fixed, hence

\[
\boxed{\dot x_*=0.}
\]

The velocity is nevertheless

\[
\boxed{u(x_*,t)=\sqrt2\,a(t)(1,1,1)^T\ne0.}
\]

Moreover

\[
\nabla e(x_*,t)=0,
\]

and

\[
\boxed{
H_e(x_*,t)
=-a(t)^2
\begin{pmatrix}
1&1/2&1/2\\
1/2&1&1/2\\
1/2&1/2&1
\end{pmatrix}.}
\]

This matrix is negative definite and

\[
\boxed{\det H_e=-\frac12a(t)^6\ne0,}
\]

so `x_*` is a strict nondegenerate enstrophy maximum.  The exact critical-current law reconstructs

\[
\dot x_*-u=-u.
\]

A material particle initially placed at this critical maximum therefore leaves the critical branch instantaneously.  The Eulerian critical tracker and the material carrier are distinct physical currents even inside a smooth exact periodic NSE solution.

**Label: EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO.**

---

## 4. The critical Hessian has a three-face moving law

Take two spatial derivatives of

\[
\partial_t e+u\cdot\nabla e=R.
\]

At a critical point the terms containing `grad e` vanish, giving

\[
\nabla^2(u\cdot\nabla e)
=(\nabla u)^TH_e+H_e\nabla u+(u\cdot\nabla)H_e.
\]

Along the critical branch,

\[
\boxed{
\frac{d_*H_e}{dt}
=\nabla^2R
-(\nabla u)^TH_e-H_e\nabla u
+((\dot x_*-u)\cdot\nabla)H_e.}
\]

The three faces are:

1. curvature of the physical growth landscape, `Hess R`;
2. the local fluid connection/congruence acting on the Hessian;
3. relative critical transport through Hessian inhomogeneity.

The last face is present precisely because the critical current need not be material.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 5. Incompressibility kills only the connection contribution to curvature volume

On a nondegenerate branch, Jacobi's identity gives

\[
\frac d{dt}\log|\det H_e|
=\operatorname{tr}\left(H_e^{-1}\frac{d_*H_e}{dt}\right).
\]

Let `A=grad u`.  The connection contribution is

\[
\begin{aligned}
\operatorname{tr}\left[H_e^{-1}(-A^TH_e-H_eA)\right]
&=-\operatorname{tr}(A^T)-\operatorname{tr}(A)\\
&=-2\nabla\cdot u.
\end{aligned}
\]

Hence incompressibility yields the exact cancellation

\[
\boxed{
\frac d{dt}\log|\det H_e|
=\operatorname{tr}(H_e^{-1}\nabla^2R)
+\operatorname{tr}\!\left[
H_e^{-1}((\dot x_*-u)\cdot\nabla)H_e
\right].}
\]

Substituting the exact critical speed gives a purely local critical-geometry form,

\[
\boxed{
\frac d{dt}\log|\det H_e|
=\operatorname{tr}(H_e^{-1}\nabla^2R)
-\operatorname{tr}\!\left[
H_e^{-1}\big((H_e^{-1}\nabla R)\cdot\nabla\big)H_e
\right].}
\]

This cancellation concerns the **determinant volume** of critical curvature only.  It does not freeze Hessian shape, eigenvalues, eigendirections, or the critical point itself.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 6. Cross-program typing: physical critical drift is not Wang re-anchoring gauge

Wang's current smooth-carrier theorem makes a sharp distinction:

- the same material carrier continues between actual physical interaction events;
- affine common-slice re-anchoring composes as a coordinate gauge and is not a material event.

The critical-current displacement above has a different type.  At an instant when a material trajectory `X_m` and a nondegenerate critical branch coincide,

\[
X_m(t_0)=x_*(t_0),
\qquad
\dot X_m(t_0)=u(x_*(t_0),t_0),
\]

so

\[
\boxed{
\frac d{dt}(x_*-X_m)\bigg|_{t_0}
=-H_e^{-1}\nabla R.}
\]

When this is nonzero, the two physical objects separate immediately.  No affine coordinate re-anchoring can turn that separation into a gauge event without changing which physical locus is being tracked.  Exact ABC activates the distinction with `xdot_*=0` and `u!=0`.

Therefore a literal Wang--Kelvin state construction that uses an enstrophy-critical candidate must either

1. retain material carrier current/shape and critical-locus current/geometry as separately typed observables; or
2. reconstruct the latter from the Eulerian field through `H_e`, `grad R`, and the required higher local jets.

It may not identify them by name or absorb their relative drift into observer gauge.

This is a state-typing theorem, not an actual first-bad instantiation and not a continuation theorem.

**Label: RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO.**

---

## 7. OPEN BRIDGE — what remains open

The PDE has now supplied an exact candidate-current law for one natural local observable.  It has **not** supplied the missing actual first-bad theorem.  Still open are:

- whether the real first-bad object is an enstrophy critical branch, another current/shape observable, or a library-level event;
- support-locality and nondegeneracy through the relevant time interval;
- event timing and ancestry when critical branches appear, merge, bifurcate, or lose Hessian invertibility;
- coupling to the persistent Kelvin library/full pair state and to Wang's genuine physical-owner recurrence;
- any assembly/termination theorem.

No recurrence, continuation, or global-regularity conclusion is claimed.
