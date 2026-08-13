# Selector jump q.v. is history, not an endpoint state: exact coboundary no-go

Status: **EXACT PATH IDENTITY / COUNTEREXAMPLE-NO-GO / EXACT NSE CALIBRATION**.

This note starts only after the physical types have already been separated:

- the persistent Kelvin library is physical state;
- the selector is a readout;
- continuous same-replica Brownian q.v. is a viscous stochastic source;
- a continuous-source rate change is a signed source **revaluation**;
- a finite selector jump contributes a square to optional càdlàg q.v.;
- endpoint pair/dyad revaluation has signed left/right/quadratic faces.

The question here is narrower: can the **accumulated selector jump-square** be
reconstructed from the current endpoint state alone?  The answer is no, before any
estimate is made.

The latest Kelvin input is used read-only at
`ad8cd25c8fa0d8aa73bc2f37ec86d8a763820063`.  Its actual first-bad timing,
physical packet maps and clock instantiation remain Open-literal.

---

## 1. Pair revaluation is an endpoint coboundary

Let a supplied selector path read a fixed-dimensional selected residual sequence

\[
Y_0,Y_1,\ldots,Y_m.
\]

At event `j`, write

\[
\Delta_jY=Y_j-Y_{j-1}.
\]

The endpoint pair increment is

\[
Y_jY_j^T-Y_{j-1}Y_{j-1}^T.
\]

Summing over all events telescopes exactly:

\[
\boxed{
\sum_{j=1}^m
\left(Y_jY_j^T-Y_{j-1}Y_{j-1}^T\right)
=Y_mY_m^T-Y_0Y_0^T.}
\]

Thus deterministic selected pair revaluation is a genuine endpoint coboundary.
On every closed selector loop `Y_m=Y_0`, its total revaluation is zero.

**Label: EXACT PAIR/RESET IDENTITY.**

---

## 2. Selector jump optional q.v. has positive loop circulation

The finite-jump contribution to optional quadratic variation is instead

\[
\boxed{
\mathcal J[Y]
:=\sum_{j=1}^m
\Delta_jY\,\Delta_jY^T.}
\]

Every summand is positive semidefinite.  For the two-point closed loop

\[
a\longrightarrow b\longrightarrow a,
\qquad a\ne b,
\]

one has

\[
\boxed{
\mathcal J[a\to b\to a]
=2(b-a)(b-a)^T\ne0.}
\]

Therefore the jump-q.v. path functional does **not** telescope on closed loops.
It is a positive path-length/variation object, not an endpoint revaluation.

**Label: EXACT SEMIMARTINGALE PATH IDENTITY.**

---

## 3. No endpoint-state potential can generate selector jump q.v.

Suppose there were a universal matrix-valued state function `F` such that every
admissible selector jump obeyed

\[
F(Y_+)-F(Y_-)
=(Y_+-Y_-)(Y_+-Y_-)^T.
\]

Apply this first to `a->b` and then to `b->a`.  The left sides add to zero, while
the right sides add to

\[
2(b-a)(b-a)^T.
\]

For `a\ne b` this is nonzero.  Contradiction.

Hence

\[
\boxed{
\text{selector jump q.v. is not an endpoint-state coboundary}.}
\]

The same contradiction holds after taking trace, so no scalar endpoint potential can
recover the accumulated jump-q.v. trace either.

**Label: COUNTEREXAMPLE/NO-GO.**

---

## 4. Current persistent library + current selector do not determine accumulated jump q.v.

Freeze a physical candidate library `X` with two distinct readouts

\[
a=E_0X,
\qquad
b=E_1X,
\qquad a\ne b.
\]

Compare two supplied hybrid selector histories on the same frozen library:

1. the stationary history, which remains at selector `0`;
2. the closed excursion `0->1->0`.

At the endpoint, both have exactly the same

\[
\boxed{
(X,\ E_0,\ Y=a).}
\]

Their accumulated selector jump q.v. differs:

\[
\mathcal J_{\rm stationary}=0,
\qquad
\mathcal J_{0\to1\to0}=2(b-a)(b-a)^T>0.
\]

Consequently there is no universal instantaneous map

\[
\Psi(X,E_g,Y)
=\text{accumulated selector jump q.v.}
\]

on the supplied hybrid path space.

If the theorem domain carries a physical clock value as an additional current
coordinate, the same obstruction persists whenever two admissible histories can end
at the same clock/state.  Avoiding it requires an independently proved event-timing
or admissible-history theorem; the selector algebra does not supply one.

**Label: COUNTEREXAMPLE/NO-GO / HISTORY-STATE NECESSITY.**

---

## 5. Continuous source-rate revaluation does not repair the history loss

The latest Kelvin layer also distinguishes the pre/post continuous Brownian source
rates

\[
\Gamma_-^{\rm cont},
\qquad
\Gamma_+^{\rm cont}
\]

and their signed finite difference.  That object is an endpoint revaluation of which
continuous source is active; it is not the accumulated selector jump square.

On a selector-only closed excursion of a frozen physical library/noise response, the
initial and final continuous source rate can be identical while `mathcal J[Y]` is
positive.  Therefore adding the **current** continuous source rate to the endpoint
state still does not reconstruct the past selector jump variation.

This is not a claim that the rate revaluation itself is path-independent under
arbitrary physical events.  It is only the exact statement that the current rate and
the accumulated jump-q.v. history are different data.

**Label: RIGOROUS CONSEQUENCE / PHYSICAL TYPE SEPARATION.**

---

## 6. Exact Navier--Stokes calibration activates the loop obstruction

Use the exact periodic shear

\[
u(y,t)=E\cos(ky)e_x,
\qquad
E=e^{-\nu k^2t},
\]

and the Kelvin asymmetric packet side

\[
\rho=\frac{\pi}{2k}.
\]

For the half-period anchors `0` and `pi/k`, the exact codeforming residuals are

\[
\boxed{
\chi_0=\frac{4Ek^2}{\pi^2},
\qquad
\chi_1=-\chi_0.}
\]

Take the frozen exact-NSE residual library readouts

\[
a=\chi_0e_z,
\qquad
b=-\chi_0e_z.
\]

Then the closed selector excursion `0->1->0` has

\[
\boxed{
\mathcal J_{\rm loop}
=8\chi_0^2P_z
=\frac{128E^2k^4}{\pi^4}P_z>0,}
\]

while its endpoint selected residual and endpoint dyad are exactly the same as at the
start.

A stationary selector history on the **same frozen exact-NSE payload** has zero
selector jump q.v. and the same endpoint library/readout/state.  Thus exact smooth NSE
activates the state-indistinguishability obstruction.

Scope is important: this calibration supplies exact NSE library values.  It does
**not** assert that the actual first-bad badness/resolve logic realizes the closed
selector excursion at those times.  Actual event timing remains Open-literal upstream.

**Label: EXACT NSE CALIBRATION / COUNTEREXAMPLE-NO-GO.**

---

## 7. Cross-program state-map consequence

The repo-3 state-map seam can now be sharpened.  Even after carrying

- the instantaneous Eulerian/coherent field;
- the material current/shape;
- the persistent physical candidate library;
- the active selector and selected residual;
- the full current pair/Gram coupling;
- the current continuous q.v. source rate;

one still cannot universally reconstruct an **accumulated selector jump-q.v.
functional** from those current endpoint data alone.

One must either carry selector-event history (or an equivalent path accumulator) or
prove an independent Navier--Stokes theorem that makes the relevant history a
function of the endpoint state on the intended theorem domain.

Thus the surviving seam is not merely “clock” as a label.  It contains a literal
history variable forced by a closed-loop obstruction.

**Label: RIGOROUS CONSEQUENCE / OPEN BRIDGE.**

No recurrence, continuation, termination or global-regularity theorem is claimed.
