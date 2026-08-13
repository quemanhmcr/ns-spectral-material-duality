# Enstrophy value-space current, convex moment hierarchy, and support-edge selection

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + ACTION STRESS TEST + OPEN BRIDGE**.

The previous batch resolved regular enstrophy level sets one surface at a time.  This batch compresses the entire family without imposing a selector: push physical volume forward by the actual local enstrophy value.

Let

\[
e(x,t)=\frac12|\omega(x,t)|^2,
\qquad
R(x,t)=D_te
=\omega\cdot S\omega-\nu|\nabla\omega|^2+\nu\Delta e.
\]

No upstream write is made.  Current read-only Kelvin remains `2227e1a9d3fbe48de591cfee2d4d09fe09b4f1bf`; Wang remains `24a725798948d7067afae1976afb9c712fb23b47`.

---

## 1. The full enstrophy population obeys a one-dimensional exact continuity law

On the periodic domain define the pushforward volume measure

\[
\mu_t=e(\cdot,t)_\#dx,
\]

so for every test function `phi`,

\[
\int\phi(a)\,d\mu_t(a)=\int\phi(e(x,t))\,dx.
\]

Define the signed owner-current measure `j_t` by

\[
\int\psi(a)\,dj_t(a)=\int\psi(e(x,t))R(x,t)\,dx.
\]

Because

\[
\partial_t e=R-u\cdot\nabla e
\]

and incompressibility kills the spatial integral of `u.grad phi(e)`, one obtains for every smooth compactly supported `phi`

\[
\frac d{dt}\int\phi\,d\mu_t
=\int\phi'(a)\,dj_t(a).
\]

Equivalently, in distributions on enstrophy-value space,

\[
\boxed{
\partial_t\mu+\partial_a j=0.}
\]

This statement is valid at critical values as a measure identity.  No division by `|grad e|` and no regular-level assumption is needed.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 2. Regular levels recover the level-set owner flux exactly

At a regular value `a`, coarea gives densities

\[
\boxed{
g(a,t)=\int_{e=a}\frac{1}{|\nabla e|}\,dS,}
\]

and

\[
\boxed{
J(a,t)=\int_{e=a}\frac{R}{|\nabla e|}\,dS.}
\]

Thus the measure law becomes

\[
\boxed{
\partial_tg+\partial_aJ=0.}
\]

If `g>0`, define the conditional owner velocity

\[
\boxed{
c_e(a,t)=\frac{J}{g}
=\mathbb E_{dx}[R\mid e=a].}
\]

Then

\[
\boxed{
\partial_tg+\partial_a(g c_e)=0.}
\]

The superlevel survival function from II--IQ is

\[
V(a,t)=\mu_t((a,\infty)),
\]

and its exact fixed-level law is simply

\[
\boxed{
\partial_tV(a,t)=J(a,t).}
\]

So the apparently large family of moving surfaces is the geometric realization of one one-dimensional owner current.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 3. The value current has stretching, vorticity-gradient loss, and curvature-redistribution faces

At regular values define

\[
J_P(a)=\int_{e=a}\frac{\omega\cdot S\omega}{|\nabla e|}\,dS,
\]

\[
B_\omega(a)=\int_{e=a}\frac{|\nabla\omega|^2}{|\nabla e|}\,dS,
\]

and

\[
K_e(a)=\int_{e=a}|\nabla e|\,dS.
\]

Periodic integration by parts in delta/coarea form gives the exact curvature identity

\[
\boxed{
\int_{e=a}\frac{\Delta e}{|\nabla e|}\,dS
=\partial_aK_e(a)}
\]

in the distributional value-space sense.  Therefore

\[
\boxed{
J=J_P-\nu B_\omega+\nu\partial_aK_e.}
\]

The value-space continuity law is consequently

\[
\boxed{
\partial_tg
+\partial_a\left(
J_P-\nu B_\omega+\nu\partial_aK_e
\right)=0.}
\]

This is a conservative value-space law.  Curvature diffusion is not an extra event source; it is a derivative of a geometric value-space flux.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 4. Every smooth enstrophy-value observable obeys one exact weighted owner identity

Let `Phi` be `C^2` on the range of `e`.  The weak value-space law, or direct spatial integration by parts, gives

\[
\boxed{
\begin{aligned}
\frac d{dt}\int\Phi(e)\,dx
={}&\int\Phi'(e)\,\omega\cdot S\omega\,dx
-\nu\int\Phi'(e)|\nabla\omega|^2\,dx\\
&-\nu\int\Phi''(e)|\nabla e|^2\,dx.
\end{aligned}}
\]

For increasing convex `Phi`, both viscous faces are nonpositive.  Hence positive growth of any such physical observable requires the weighted stretching face to beat both losses.

For integer `m>=1`,

\[
\boxed{
\begin{aligned}
\frac d{dt}\int e^m dx
={}&m\int e^{m-1}\omega\cdot S\omega\,dx
-m\nu\int e^{m-1}|\nabla\omega|^2\,dx\\
&-m(m-1)\nu\int e^{m-2}|\nabla e|^2\,dx.
\end{aligned}}
\]

At `m=1` the last face vanishes and one recovers the global enstrophy ledger.  For large `m`, the state observable concentrates near high-enstrophy regions, but no derivative-limit or regularity conclusion is asserted here.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 5. A unique nondegenerate maximum is the characteristic support edge of the same current

Suppose at time `t` there is a unique isolated strict nondegenerate maximum `x_*` with

\[
M=e(x_*,t),
\qquad
K=-\nabla^2e(x_*,t)>0.
\]

Put `delta=M-a`.  Morse expansion gives

\[
e(x_*+y,t)=M-\frac12y^TKy+O(|y|^3).
\]

In three dimensions, as `a\uparrow M`,

\[
\boxed{
V(a,t)
\sim
\frac{4\pi}{3}
\frac{(2\delta)^{3/2}}{\sqrt{\det K}},}
\]

and hence

\[
\boxed{
g(a,t)
\sim
\frac{2^{5/2}\pi}{\sqrt{\det K}}\,\delta^{1/2}.}
\]

Since `R` is continuous,

\[
J(a,t)\sim R(x_*,t)g(a,t),
\]

so

\[
\boxed{
\lim_{a\uparrow M}\frac{J(a,t)}{g(a,t)}
=R(x_*,t).}
\]

At a differentiability time of the unique maximizing branch, HS--HZ gives the same number as `M'(t)`.  Thus the interior value-space characteristic reaches the unique nondegenerate record edge with exactly the record-owner speed.

This explains how the regular-level law and the critical maximum law join without dividing by zero at the maximum itself.

**Label: RIGOROUS CONSEQUENCE.**

---

## 6. At a tie, bulk edge current averages owners while the record edge selects the fastest owner

Now suppose finitely many isolated nondegenerate maxima `x_i` share the same value `M`, with

\[
K_i=-\nabla^2e(x_i,t)>0,
\qquad
R_i=R(x_i,t).
\]

The same Morse asymptotics add over components:

\[
g(a,t)
\sim C_3\delta^{1/2}
\sum_i\frac1{\sqrt{\det K_i}},
\]

\[
J(a,t)
\sim C_3\delta^{1/2}
\sum_i\frac{R_i}{\sqrt{\det K_i}}.
\]

Therefore

\[
\boxed{
\lim_{a\uparrow M}\frac{J}{g}
=
\frac{\sum_iR_i/\sqrt{\det K_i}}
{\sum_i1/\sqrt{\det K_i}}.}
\]

But Danskin's exact support-edge law is

\[
\boxed{D_+M=\max_iR_i.}
\]

These are generally different.

So even the intrinsic value-space pushforward cannot erase branch identity at a tied support edge:

\[
\boxed{
\text{bulk edge population velocity}
\neq
\text{record-edge winner velocity}
\quad\text{at a generic tie}.}
\]

The distinction is not a bookkeeping artifact.  The bulk current averages all near-edge populations with curvature-volume weights; the support edge follows whichever active branch advances fastest.

**Label: RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO to bulk-average replacement of record selection.**

---

## 7. The exact three-mode shear realizes the tied-edge split with closed-form constants

At the exact transverse ranking crossing from GP--GU, `t_*=1/nu`, the two translation-symmetric normal maxima at `y=0,pi` have

\[
M=\frac92e^{-2},
\]

normal curvatures

\[
\kappa_0=12e^{-2},
\qquad
\kappa_\pi=60e^{-2},
\]

and branch owner rates

\[
R_0=-12\nu e^{-2},
\qquad
R_\pi=-60\nu e^{-2}.
\]

For the one-dimensional normal pushforward, the near-edge density weights are proportional to `1/sqrt(kappa_i)`.  Hence the bulk conditional edge velocity is

\[
\boxed{
c_{\rm bulk,edge}
=
\frac{R_0/\sqrt{\kappa_0}+R_\pi/\sqrt{\kappa_\pi}}
{1/\sqrt{\kappa_0}+1/\sqrt{\kappa_\pi}}
=-12\sqrt5\,\nu e^{-2}.}
\]

By contrast,

\[
\boxed{D_+M=R_0=-12\nu e^{-2},}
\]

while the left winner has rate `R_pi=-60 nu e^-2`.

Thus one exact smooth NSE tie simultaneously has:

- one bulk near-edge population current;
- two distinct branch owner rates;
- a record edge that switches to the branch with the larger rate (the more slowly decaying branch at this tie);
- zero nonlinear advection in the velocity equation.

This cleanly locates ranking/lineage information: it is needed at the support edge, but it still does not create a new generation owner.

**Label: EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO + ACTION STRESS TEST calibration.**

---

## 8. Exact heat shear is a pure dilation in enstrophy-value space

For the one-mode exact periodic heat shear, per unit `x-z` tangent area,

\[
e=M(t)\cos^2(ky),
\qquad
M'= -2\nu k^2M.
\]

On `0<a<M`, the exact pushforward density is

\[
\boxed{
g(a,t)=\frac{2}{\sqrt{a(M-a)}}.}
\]

Since the local owner is

\[
R=-2\nu k^2e,
\]

the value current is

\[
\boxed{
J(a,t)=-2\nu k^2a\,g(a,t)
=-4\nu k^2\sqrt{\frac{a}{M-a}}.}
\]

Therefore

\[
\boxed{c_e(a,t)=-2\nu k^2a,}
\]

and the entire enstrophy population obeys the simple dilation law

\[
\boxed{
\partial_tg+\partial_a(-2\nu k^2a\,g)=0.}
\]

The viscous current decomposition is also exact:

\[
B_\omega=4k^2\sqrt{\frac{M-a}{a}},
\qquad
K_e=8k^2\sqrt{a(M-a)},
\]

with

\[
\boxed{-\nu B_\omega+\nu\partial_aK_e=J.}
\]

A spatially oscillatory field has therefore collapsed to a one-dimensional linear contraction of its enstrophy-value population.

**Label: EXACT NSE/PDE IDENTITY + ACTION STRESS TEST calibration.**

---

## 9. Structural consequence: interior current plus support-edge selection

The enstrophy side of the programme now has a compact endogenous hierarchy:

\[
\boxed{
\text{local NSE owner }R
\to
\text{value-space current }j
\to
\begin{cases}
\text{interior population transport},\\
\text{superlevel moving geometry},\\
\text{global moment / spectral owner ledgers},\\
\text{support-edge record selection}.
\end{cases}}
\]

The first three are population/integral readings of the same current.  The final support edge has an additional extremal selection law when multiple lineages tie.

This is a substantial reduction of apparent event complexity, but not a regularity theorem.  The next hard seam is now precise: understand whether repeated support-edge owner renewal can occur indefinitely once the owner itself is constrained by IA--IH pressure/strain/viscous dynamics and by material/donor ancestry.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**
