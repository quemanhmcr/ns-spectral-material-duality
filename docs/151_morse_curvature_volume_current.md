# Morse curvature-volume current and quantitative degeneration currency

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + COUNTEREXAMPLE/NO-GO + ACTION STRESS TEST + OPEN BRIDGE**.

JT--KC closes interior scalar selector Zeno on the positive-time analytic Morse domain: if winner changes accumulate at an interior classical time, critical geometry must degenerate.  This batch asks the next PDE-first question:

> Can `Morse degeneration` itself be replaced by an exact physical current rather than left as a Boolean geometry-failure flag?

Yes.  The already certified critical-Hessian equation yields a scalar curvature-volume ledger whose incompressible connection cancels exactly.  Literal degeneration forces infinite negative log-volume variation.  The exact Kelvin merger then shows that this geometry currency can diverge while the Navier--Stokes field remains analytic, so it must not be renamed fluid blow-up.

No continuation/global-regularity theorem is claimed.

---

## 1. Strict critical maxima carry an exact curvature-volume current

Let `x_*(t)` be a differentiable strict nondegenerate enstrophy maximum and put

\[
H=\nabla^2e(x_*(t),t),
\qquad
G=-H>0,
\qquad
w_*=\dot x_*-u=G^{-1}\nabla R.
\]

The certified critical-Hessian equation is

\[
\frac{d_*H}{dt}=\nabla^2R-(\nabla u)^TH-H\nabla u+(w_*\cdot\nabla)H.
\]

Therefore

\[
\boxed{
\frac{d_*G}{dt}
=-\nabla^2R-(\nabla u)^TG-G\nabla u+(w_*\cdot\nabla)G.}
\]

Taking the logarithmic determinant gives

\[
\boxed{
\frac d{dt}\log\det G
=
-\operatorname{tr}(G^{-1}\nabla^2R)
+\operatorname{tr}\!\left[G^{-1}(w_*\cdot\nabla)G\right].}
\]

The two `grad u` terms contribute `-2 div u=0`.  Common incompressible deformation can change the curvature shape but not this critical curvature volume directly.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 2. The curvature-volume current has owner and geometry-harvesting faces

Define

\[
\boxed{
\mathcal C_{\rm owner}
=-\operatorname{tr}(G^{-1}\nabla^2R),
\qquad
\mathcal C_{\rm sweep}
=\operatorname{tr}[G^{-1}(w_*\cdot\nabla)G].}
\]

Then

\[
\boxed{
\frac d{dt}\log\det G
=\mathcal C_{\rm owner}+\mathcal C_{\rm sweep}.}
\]

`C_owner` changes the local curvature through the Hessian of the exact enstrophy owner field `R`.  `C_sweep` changes which curvature environment the nonmaterial critical lineage samples.  The common velocity-gradient connection has already cancelled and is not a third volume source.

This parallels the JJ--JS stretching-renewal split but is a different physical currency.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 3. Running-record normalization gives a similarity-invariant Morse-volume grammar

Under Navier--Stokes similarity,

- `e` has weight `4`;
- `G=-Hess e` has weight `6`;
- `det G` has weight `18`;
- the running enstrophy record `mathscr M` has weight `4`.

Hence

\[
\boxed{
\mathfrak K
=\frac{\det G}{\mathscr M^{9/2}}}
\]

is similarity invariant.

Use the running-record intrinsic time

\[
d\vartheta=\sqrt{\mathscr M}\,dt,
\qquad
\rho_{\rm rec}=\frac{\dot{\mathscr M}}{\mathscr M^{3/2}}\ge0.
\]

Then

\[
\boxed{
\frac d{d\vartheta}\log\mathfrak K
=
\mathfrak C_{\rm owner}
+\mathfrak C_{\rm sweep}
+\mathfrak C_{\rm norm},}
\]

where

\[
\boxed{
\mathfrak C_{\rm owner}
=-\frac{1}{\sqrt{\mathscr M}}\operatorname{tr}(G^{-1}\nabla^2R),}
\]

\[
\boxed{
\mathfrak C_{\rm sweep}
=\frac{1}{\sqrt{\mathscr M}}
\operatorname{tr}[G^{-1}(w_*\cdot\nabla)G],}
\]

and

\[
\boxed{
\mathfrak C_{\rm norm}=-\frac92\rho_{\rm rec}\le0.}
\]

Thus record normalization can only compress normalized Morse volume; it cannot be a positive geometry-renewal source.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 4. Literal Morse degeneration requires infinite negative log-volume variation

Suppose a strict critical lineage remains nondegenerate on `[t0,t_*)` and

\[
\det G(t)\downarrow0
\quad\text{along a sequence as }t\uparrow t_*.
\]

Then

\[
\log\det G(t)\to-\infty.
\]

For the exact current

\[
c(t)=\mathcal C_{\rm owner}+\mathcal C_{\rm sweep}
=\frac d{dt}\log\det G,
\]

its negative variation satisfies

\[
\int_{t_0}^{t}[-c(s)]_+\,ds
\ge
\log\det G(t_0)-\log\det G(t).
\]

Therefore

\[
\boxed{
\int_{t_0}^{t_*}
[-(\mathcal C_{\rm owner}+\mathcal C_{\rm sweep})]_+\,dt
=\infty.}
\]

A genuine Hessian-degeneration event cannot occur with finite total negative curvature-volume currency.

This is a necessary geometry condition, not a bound proving degeneration impossible.

**Label: RIGOROUS CONSEQUENCE.**

---

## 5. Interior scalar winner-Zeno now routes into a quantitative geometry currency

JT--KC proves that, on a compact interval strictly inside a positive-time classical lifespan, an interior accumulation of scalar support-edge winner changes forces an enstrophy critical point with degenerate Hessian.

If that degeneration is approached along a strict-max critical lineage, Section 4 gives the stronger route

\[
\boxed{
\text{interior scalar winner-Zeno}
\Rightarrow
\text{Morse degeneration}
\Rightarrow
\text{infinite negative curvature-volume variation}.}
\]

The first implication is analytic/Morse; the second is an exact determinant-current consequence.  No selector q.v. is converted into geometry currency: the selector only identifies the forced geometry channel.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 6. Exact two-mode Kelvin merger has quadratic normal-curvature collapse

Use the exact periodic two-mode heat shear from the Kelvin merger.  Let

\[
r=\cos d=e^{3(\nu t-1)},
\qquad
\alpha=e^{-\nu t}=e^{-1}r^{-1/3}.
\]

On either side critical sheet `y=pi+-d`, the vorticity and its second derivative give the strict normal enstrophy curvature

\[
\boxed{
G_n(d)=-e_{yy}
=\frac{\alpha^2(2r^2+1)(1-r^2)}{4r^2}>0.}
\]

As the sheets merge, `d->0`, `r->1`, and

\[
\boxed{
\frac{G_n(d)}{d^2}
\longrightarrow
\frac{3}{4e^2}.}
\]

Thus the normal Morse curvature collapses quadratically even though the underlying velocity field remains a finite Fourier polynomial.

**Label: EXACT NSE/PDE IDENTITY + ACTION STRESS TEST calibration.**

---

## 7. The merger curvature-volume rate diverges with an exact coefficient

Since

\[
\dot d=-3\nu\cot d,
\qquad
\dot r=3\nu r,
\]

exact differentiation of the previous formula yields

\[
\boxed{
\frac d{dt}\log G_n
=-8\nu
+\frac{12\nu r^2}{2r^2+1}
-\frac{6\nu r^2}{1-r^2}.}
\]

Consequently

\[
\boxed{
d^2\frac d{dt}\log G_n\longrightarrow-6\nu.}
\]

Equivalently, because

\[
d^2\sim6\nu(t_*-t),
\]

one has

\[
\frac d{dt}\log G_n\sim-\frac1{t_*-t}.
\]

The integrated negative log-curvature variation therefore diverges at the merger exactly as Section 4 requires.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + ACTION STRESS TEST.**

---

## 8. Divergent geometry currency is not fluid blow-up

At the exact merger:

- the Navier--Stokes field is analytic and finite Fourier;
- nonlinear advection in the shear is zero;
- the branch coordinate speed diverges like `1/d`;
- the normal curvature tends to zero like `d^2`;
- the log-curvature depletion rate diverges like `-1/(t_*-t)`.

Hence

\[
\boxed{
\text{divergent curvature-volume depletion}
\not\Rightarrow
\text{fluid singularity}.}
\]

It certifies a real geometry theorem-domain exit, not a blow-up of the NSE state.

**Label: COUNTEREXAMPLE/NO-GO.**

---

## 9. Exact ABC flow calibrates finite curvature-volume erosion without degeneration

At the fixed strict ABC enstrophy maximum,

\[
G(t)=a(t)^2G_0,
\qquad
a(t)=A e^{-\nu t},
\qquad
\det G=\frac12a^6.
\]

Therefore

\[
\boxed{
\frac d{dt}\log\det G=-6\nu}
\]

for every finite time, while `det G>0` remains nondegenerate.

So negative curvature-volume current by itself is not a geometry event.  Literal degeneration requires the **infinite accumulated negative variation** of Section 4, not merely a negative instantaneous rate.

**Label: EXACT NSE/PDE IDENTITY + ACTION STRESS TEST calibration.**

---

## 10. Scalar Morse volume and Kelvin transverse support remain different geometry owners

`det G` measures local scalar critical curvature volume.  Current Kelvin `1095c13` proves independently that a shrinking intrinsic chamber can retain `O(1)` tangential packet support `B_parallel=P L L^T P` even when current/noise readouts collapse.

Therefore

\[
\boxed{
\text{Morse curvature-volume control}
\not\Rightarrow
\text{physical transverse packet-support control}.}
\]

The two geometry currencies must remain separate in any first-bad/recurrence state.

**Label: RIGOROUS CROSS-PROGRAM CONSEQUENCE.**

---

## 11. The geometry exit channel is now a current, not a Boolean flag

The endpoint grammar can now type the scalar geometry route as follows:

\[
\boxed{
\text{Morse/normal geometry exit}
\leadsto
\text{negative curvature-volume current}
\leadsto
\text{infinite accumulated depletion at literal degeneration}.}
\]

This sits beside, but is not identified with,

- positive running-record core renewal;
- positive specific-stretching geometry harvesting;
- Kelvin tangential packet-support noncollapse;
- transport ancestry/frame holonomy.

The remaining hard problem is to prove a capacity/nonaccumulation law across these typed channels near a candidate terminal endpoint.  No termination, restart, continuation, or global-regularity theorem is claimed.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

**KD–KN ACTION CERTIFICATE.** Action 31714985899 on theorem SHA d9af664d5c15974b2b1def115fcaad59c48fd92a: connection 9.770e-15; similarity 1.597e-15; ABC determinant 1.839e-16; merger derivative identity 1.627e-16; G_n/d^2 residual 2.812e-12; d-squared log-rate residual 9.409e-17; negative log-volume drop 2.150569e+01; negative log-rate signal 1.860000e+10; nonlinear advection 0; PASS.
