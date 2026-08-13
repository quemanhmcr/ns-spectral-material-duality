# Enstrophy record owner clock and first-hit stretching funnel

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + OPEN BRIDGE**.

Read-only truth before this batch:

- Wang `24a725798948d7067afae1976afb9c712fb23b47` classifies independently witnessed physical first stops before attaching typed material/Moyal sidecars; sidecar positivity cannot mint recursive depth.
- Kelvin `4888b6e19293edc0950047fd2e52ad6b64fbe3ac` separates Eulerian critical paths, literal material/Kelvin ancestry, and transported packet geometry; the critical moving-cut cusp is transfer, not generation.
- Repo-3 Theorems HK--HR show that moving-boundary complexity is driven by the relative velocity `V-u`, and that relative sweep remains a physical transfer currency with zero hard-generation depth unless an independent source/work owner is present.

The present question is stricter: can an actual *growth record* of a literal Navier--Stokes field quantity identify its owner without asking a selector or boundary ledger to decide?

For local enstrophy the answer is yes.

No upstream write is made in this batch. No recurrence, restart, continuation, termination, or global-regularity conclusion is asserted.

---

## 1. The active enstrophy maximum has an exact PDE rate

Let `u` be a smooth incompressible Navier--Stokes solution on the periodic three-torus over a compact time interval, let

\[
\omega=\nabla\times u,
\qquad
e=\frac12|\omega|^2,
\]

and write the exact local enstrophy balance

\[
(\partial_t+u\cdot\nabla)e
=\omega\cdot S\omega-\nu|\nabla\omega|^2+\nu\Delta e.
\]

Define the spatial maximum and active maximizing set

\[
M(t)=\max_x e(x,t),
\qquad
\mathcal A(t)=\{x:e(x,t)=M(t)\}.
\]

Compactness and smoothness make `M` locally Lipschitz.  Danskin's theorem gives its exact right derivative

\[
D_+M(t)=\max_{x\in\mathcal A(t)}\partial_t e(x,t).
\]

Every active maximizer satisfies

\[
\nabla e=0,
\qquad
\Delta e\le0.
\]

Therefore the advective readout vanishes pointwise on the active set and

\[
\boxed{
D_+M(t)=
\max_{x\in\mathcal A(t)}
\left[
\omega\cdot S\omega
-\nu|\nabla\omega|^2
+\nu\Delta e
\right].}
\]

This is not a norm estimate.  It is the exact local NSE law evaluated on the physical active set selected by the field itself.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 2. Critical-selector drift is exactly annihilated from the value rate

Suppose a differentiable critical branch `x_*(t)` is active, so

\[
\nabla e(x_*(t),t)=0.
\]

Then regardless of whether that branch is material,

\[
\frac d{dt}e(x_*(t),t)
=\partial_t e+\dot x_*\cdot\nabla e
=\partial_t e.
\]

Using the exact critical-current law from Theorem GL,

\[
\dot x_*-u=-H_e^{-1}\nabla R,
\]

changes the branch location and its geometry, but it contributes **zero direct value currency** at the critical readout because the multiplier is `grad e=0`.

Thus the first-order causal order is triangular:

\[
\boxed{
\text{critical geometry/drift}
\quad\hbox{selects where to read, but}\quad
\text{local PDE owner determines how the critical value changes}.}
\]

A ranking switch can change which active branch realizes `M`, and can create a derivative kink, but it does not create an additional selector-speed term in `D_+M`.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 3. Positive record growth forces a genuine stretching owner

At every active maximizer define the nonnegative viscous defect

\[
\mathcal D_\nu
:=\nu\bigl(|\nabla\omega|^2-\Delta e\bigr).
\]

Because `Delta e<=0` on the active set,

\[
\boxed{
\mathcal D_\nu\ge\nu|\nabla\omega|^2\ge0.}
\]

The active maximum rate becomes

\[
D_+M(t)=
\max_{x\in\mathcal A(t)}
\left[
\omega\cdot S\omega-\mathcal D_\nu
\right].
\]

Hence

\[
\boxed{
D_+M(t)>0
\Longrightarrow
\exists x_*\in\mathcal A(t):
\quad
\omega\cdot S\omega>
\mathcal D_\nu
\ge\nu|\nabla\omega|^2.}
\]

So a growing enstrophy record cannot be owned by:

- critical drift;
- ranking/selector motion;
- relative-boundary sweep;
- passive packet gauge;
- target reanchoring;
- inherited stock or Moyal boundary currency.

Those mechanisms can affect where or how the state is observed, transported, or remembered.  They cannot make the active local enstrophy maximum increase unless the intrinsic stretching face beats the full viscous/curvature defect at some active maximizer.

This is the first literal first-hit owner gate in repo-3.

**Label: RIGOROUS CONSEQUENCE.**

---

## 4. The owner has an intrinsic strain-alignment form

At an active maximizer with `omega!=0`, put

\[
\hat\omega=\frac\omega{|\omega|},
\qquad
s_\omega=\hat\omega^T S\hat\omega.
\]

Then

\[
\omega\cdot S\omega=|\omega|^2s_\omega=2M s_\omega
\]

on the active set, and the local rate is

\[
\boxed{
D_+M
=\max_{\mathcal A}
\left[2M s_\omega-\mathcal D_\nu\right].}
\]

Whenever the record grows, some active maximizer must satisfy

\[
\boxed{
s_\omega>
\frac{\mathcal D_\nu}{2M}\ge0.}
\]

If `lambda_1>=lambda_2>=lambda_3` are the strain eigenvalues and `c_i` are the direction cosines of `hat omega`, incompressibility gives

\[
\lambda_1+\lambda_2+\lambda_3=0,
\qquad
s_\omega=\sum_i\lambda_i c_i^2.
\]

Thus positive record growth requires a sufficiently strong extensional strain component *in the actual vorticity direction*.  A large strain tensor by itself is not the owner; the alignment-weighted stretching must beat the viscous defect.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 5. The running enstrophy record gives a canonical monotone owner clock

Define the running physical record

\[
\mathcal R(t)=\max_{0\le s\le t}M(s).
\]

Since `M` is absolutely continuous on every smooth compact interval, `R` is absolutely continuous and, for almost every time,

\[
\boxed{
\mathcal R'(t)
=\mathbf 1_{\{M(t)=\mathcal R(t)\}}
[M'(t)]_+.}
\]

At almost every differentiability time of `M`, the active-max law gives

\[
\boxed{
\mathcal R'(t)
=\mathbf 1_{\{M=\mathcal R\}}
\left[
\max_{x\in\mathcal A(t)}
\bigl(\omega\cdot S\omega-\mathcal D_\nu\bigr)
\right]_+.}
\]

This is a canonical monotone clock extracted from the PDE field itself.

It has exactly the kernel demanded by the previous no-go theorems:

- a ranking loop below the old record contributes zero;
- a selector label loop contributes zero;
- pure moving-cut/sweep activity contributes zero unless it changes the actual local field maximum through an independently present source owner;
- endpoint reanchoring or passive gauge contributes zero;
- inherited stock without fresh stretching contributes zero.

In contrast to selector jump q.v., `R` cannot acquire positive closed-loop circulation while returning to the same record level.

This does **not** yet prove that `R` is the final programme generation depth.  It proves that it is an intrinsic PDE owner clock with the necessary zero-sidecar kernel.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 6. First-hit funnel without a transversality assumption

Fix a level `L>M(0)` and define the first record hit

\[
\tau_L=\inf\{t>0:M(t)\ge L\}.
\]

Assume `tau_L` is finite while the solution remains smooth through that time.  Continuity gives

\[
M(\tau_L)=L,
\qquad
M(t)<L\quad(t<\tau_L).
\]

For every `delta>0` small enough,

\[
\mathcal R(\tau_L)-\mathcal R(\tau_L-\delta)>0.
\]

Absolute continuity of the running record therefore supplies a time

\[
t_\delta\in(\tau_L-\delta,\tau_L)
\]

at which `R'(t_delta)>0`.  At almost every such record-growth time the exact owner gate applies.  Choosing `delta_n downarrow0` gives a sequence

\[
t_n\uparrow\tau_L,
\qquad
x_n\in\mathcal A(t_n),
\]

with

\[
\boxed{
\omega\cdot S\omega(x_n,t_n)
>
\nu\bigl(|\nabla\omega|^2-\Delta e\bigr)(x_n,t_n)
\ge
\nu|\nabla\omega|^2(x_n,t_n).}
\]

So even a tangential or nondifferentiable first hit cannot be approached using selector/boundary activity alone.  Arbitrarily close from below, actual record growth is witnessed by genuine stretching-dominant PDE states.

**Label: RIGOROUS CONSEQUENCE.**

---

## 7. Exact periodic heat shear: selector/curvature activity with no record generation

Take the exact periodic Navier--Stokes shear

\[
u=(A e^{-\nu k^2t}\sin ky,0,0).
\]

Its nonlinear transport and vortex stretching vanish identically.  The vorticity is

\[
\omega=(0,0,-Ak e^{-\nu k^2t}\cos ky),
\]

so

\[
M(t)=\frac12A^2k^2e^{-2\nu k^2t}.
\]

At every active maximum `y=0 mod pi/k`,

\[
|\nabla\omega|^2=0,
\qquad
\Delta e=-A^2k^4e^{-2\nu k^2t},
\]

and therefore

\[
\boxed{
M'(t)=-2\nu k^2M(t)<0.}
\]

The entire decay is the curvature part of the viscous defect.  No record generation occurs.

The earlier three-mode exact periodic shear can simultaneously exhibit a transverse ranking switch with both candidate rates negative.  Hence even a genuine selector change at a critical tie need not create any positive record-owner currency.

**Label: EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO.**

---

## 8. Exact affine strain--spin NSE: pure stretching activates the record owner

For a complementary exact Euclidean calibration, fix `a>0`, let

\[
\Omega(t)=\Omega_0e^{2at},
\]

and define

\[
\boxed{
u(x,t)=(-ax-\Omega y,\;\Omega x-ay,\;2az).}
\]

The velocity gradient is

\[
A(t)=
\begin{pmatrix}
-a&-\Omega&0\\
\Omega&-a&0\\
0&0&2a
\end{pmatrix}.
\]

Because `Omega'=2a Omega`, the skew part of `A'+A^2` cancels exactly.  Hence

\[
A'+A^2
=\operatorname{diag}(a^2-\Omega^2,
                         a^2-\Omega^2,
                         4a^2)
\]

is symmetric and the field solves incompressible NSE with `Delta u=0` and quadratic pressure

\[
p=-\frac12\left[(a^2-\Omega^2)(x^2+y^2)+4a^2z^2\right].
\]

Its vorticity and strain are

\[
\omega=(0,0,2\Omega),
\qquad
S=\operatorname{diag}(-a,-a,2a).
\]

Thus spatial enstrophy is uniform,

\[
M=e=2\Omega^2,
\]

with zero viscous defect and

\[
\boxed{
M'=4aM
=\omega\cdot S\omega>0.}
\]

For every target level `L>M(0)`, the exact first-hit time is

\[
\boxed{
\tau_L=\frac1{4a}\log\frac{L}{M(0)}.}
\]

This calibration shows that the owner gate is not merely a no-growth statement: exact smooth NSE can activate it by pure extensional vortex stretching.

The flow is an exact smooth Euclidean affine calibration, not a finite-energy periodic regularity model.

**Label: EXACT NSE/PDE IDENTITY + ACTION STRESS TEST calibration.**

---

## 9. Log-record generation measure and the remaining regularity seam

Whenever `R(0)>0`, define

\[
\mathcal G(t)=\log\frac{\mathcal R(t)}{\mathcal R(0)}.
\]

Then for almost every record-growth time,

\[
\boxed{
\mathcal G'(t)
=
\mathbf 1_{\{M=\mathcal R\}}
\frac{
\left[
\max_{\mathcal A}
(\omega\cdot S\omega-\mathcal D_\nu)
\right]_+
}{\mathcal R(t)}.}
\]

Equivalently, at an active nonzero maximizer,

\[
\frac{\omega\cdot S\omega-\mathcal D_\nu}{M}
=2s_\omega-\frac{\mathcal D_\nu}{M}.
\]

Therefore if the physical enstrophy record were to become unbounded at a finite time while the preceding smooth identities remain valid, necessarily

\[
\boxed{
\mathcal G(t)\to+\infty,}
\]

so the time-integrated positive effective stretching on record states must diverge.

This is only a **necessary owner condition**.  It is not a bound, not a Zeno exclusion, not a continuation theorem, and not a proof that finite-time blow-up cannot occur.

The next genuine seam is now narrower: determine whether the exact NSE geometry/transport/ancestry laws force enough cancellation, depletion, donor exhaustion, or owner reuse on these record-growth states to prevent unlimited fresh effective stretching.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 10. Structural consequence for the programme

The current event architecture can now be sharpened from

\[
\text{physical owner first, sidecar second}
\]

to

\[
\boxed{
\text{field-generated active set}
\to
\text{intrinsic local owner rate}
\to
\text{monotone record clock}
\to
\text{geometry/selector/ancestry side data}.}
\]

The record clock is not allowed to count:

- ranking crossings;
- selector jumps;
- moving-cut sweep magnitude;
- target coboundaries;
- passive gauge changes;
- Moyal boundary charge;
- inherited stock;
- ancestry relabeling;

unless those events coincide with an independently witnessed positive local owner rate that raises the actual enstrophy record.

This is a PDE-derived owner projection, not a human-imposed recurrence rule.
