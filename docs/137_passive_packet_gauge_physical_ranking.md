# Passive packet gauge versus physical residual: first-bad ranking must descend to the physical quotient

Status: **EXACT REPRESENTATION IDENTITY + EXACT NSE CALIBRATION + COUNTEREXAMPLE/NO-GO**.

The starting point is the current Kelvin necessary first-bad admissibility ledger,
used read-only at `9bc8fb01454084861f85e3c7e99683d2dad029e1`.
It distinguishes a packet-frame representation from the physical residual carried by
that representation.  This note connects that distinction to the repo-3
metric/observer spine without turning a coordinate norm into a physical score.

Wang remains read-only at `c2641bbecb8c12d8a75f0acca83556bbbefd5a9c`.
Its hard event roles are physical event-owner observables; no claim is made that Wang
and Kelvin use the same selector.

---

## 1. Kelvin packet coefficients are representation data

Let `H in GL(3)` be an invertible packet frame and let `epsilon in R^3` be the
corresponding coefficient vector.  The physical residual is

\[
\boxed{r=H^{-T}\epsilon.}
\]

A passive change of packet coordinates is a right basis change

\[
\boxed{
H\mapsto H'=HS,
\qquad
\epsilon\mapsto\epsilon'=S^T\epsilon,
\qquad S\in GL(3).}
\]

Then

\[
\begin{aligned}
r'
&=(HS)^{-T}S^T\epsilon\\
&=H^{-T}\epsilon\\
&=r.
\end{aligned}
\]

Thus

\[
\boxed{r' = r.}
\]

The transformation changes packet coordinates and the frame matrix, but it does not
change the physical residual.

**Label: EXACT REPRESENTATION / PASSIVE-GAUGE IDENTITY.**

---

## 2. The inverse-Gram energy is physical; the raw coefficient norm is not

Define the packet Gram metric

\[
G_H=H^TH.
\]

Since `r=H^{-T}epsilon`,

\[
\boxed{
|r|^2
=\epsilon^T(H^TH)^{-1}\epsilon.}
\]

Under the passive basis change,

\[
G_H\mapsto G_{H'}=S^TG_HS,
\]

and therefore

\[
\boxed{
(\epsilon')^TG_{H'}^{-1}\epsilon'
=\epsilon^TG_H^{-1}\epsilon
=|r|^2.}
\]

By contrast,

\[
|\epsilon'|^2
=\epsilon^TSS^T\epsilon,
\]

which is not invariant for general `S`.
For `S=lambda I`, it scales by `lambda^2` while the physical residual remains exactly
fixed.

Hence

\[
\boxed{
\text{raw coefficient size}
\ne
\text{physical residual size}.}
\]

**Label: EXACT METRIC IDENTITY / COUNTEREXAMPLE TARGET.**

---

## 3. Raw-coefficient first-bad ranking can be reversed by a passive gauge

Consider two physical candidates with

\[
H_1=H_2=I,
\qquad
\epsilon_1=e_1,
\qquad
\epsilon_2=2e_1.
\]

Initially

\[
|r_1|^2=1<4=|r_2|^2
\]

and the raw coefficient norms happen to agree with that physical ordering.

Now make only a passive coordinate change in candidate `1`:

\[
S_1=3I,
\qquad
S_2=I.
\]

The physical residuals and physical energies are unchanged, but

\[
|\epsilon'_1|^2=9>4=|\epsilon'_2|^2.
\]

The raw ranking has reversed while the physical ordering has not changed at all.

Therefore any first-bad score/order based only on raw `|epsilon_g|`, or on another
quantity that does not descend through the passive packet gauge, is not a physical
selector.

**Label: COUNTEREXAMPLE/NO-GO.**

---

## 4. Exact NSE calibration: passive gauge can split a physically tied packet pair

Use again the exact periodic shear

\[
u(y,t)=E\cos(ky)e_x,
\qquad
E=e^{-\nu k^2t},
\]

with asymmetric packet side

\[
\rho=\frac{\pi}{2k}.
\]

At the half-period anchors the exact codeforming residuals are

\[
\boxed{
r_0=\chi e_z,
\qquad
r_1=-\chi e_z,
\qquad
\chi=\frac{4Ek^2}{\pi^2}.}
\]

They have exactly equal physical residual energy:

\[
|r_0|^2=|r_1|^2=\chi^2.
\]

Represent them initially with

\[
H_0=H_1=I,
\qquad
\epsilon_0=r_0,
\qquad
\epsilon_1=r_1.
\]

The raw norms are tied as well.  Now apply only a passive packet gauge to candidate
`0`:

\[
H'_0=3I,
\qquad
\epsilon'_0=3r_0,
\]

while candidate `1` is left unchanged.  Then

\[
(H'_0)^{-T}\epsilon'_0=r_0,
\qquad
H_1^{-T}\epsilon_1=r_1,
\]

and both inverse-Gram physical energies remain `chi^2`, but

\[
|\epsilon'_0|^2=9\chi^2,
\qquad
|\epsilon_1|^2=\chi^2.
\]

Thus exact smooth NSE supplies a physically tied pair for which raw packet-coordinate
ranking creates a completely artificial asymmetry.

This calibrates gauge admissibility only.  It does not assert that the actual Kelvin
first-bad score chooses either packet at those anchors.

**Label: EXACT NSE CALIBRATION / COUNTEREXAMPLE-NO-GO.**

---

## 5. Metric interpretation: the score is a pullback norm, not an artificial normalization

The identity

\[
|r|^2=\epsilon^TG_H^{-1}\epsilon
\]

has the same representation logic already visible elsewhere in repo 3:
physical vectors/tensors may be expressed in a moving material or packet frame, and
the coordinate coefficients must be contracted with the induced metric to recover a
physical scalar.

The passive transformation

\[
H\mapsto HS,
\qquad
G_H\mapsto S^TG_HS
\]

is a basis change of the representation.  It is not fluid strain, not physical
packet deformation, not Kelvin q.v., and not a source term.

So the invariant packet score belongs to the **metric/representation** face of the
PDE geometry.  Its invariance is not a norm estimate; it is an exact equivalence of
representations of the same physical residual.

**Label: EXACT REPRESENTATION DICTIONARY.**

---

## 6. First-bad selectors and event roles must factor through physical equivalence classes

Let `R` denote a raw representation state and let `[R]` be its passive-gauge
physical equivalence class.  A physically meaningful candidate score `B` must satisfy

\[
\boxed{
R\sim R'
\Longrightarrow
B(R)=B(R').}
\]

Equivalently, the score must factor as

\[
B=\widehat B\circ\pi,
\]

where `pi:R->[R]` is the quotient to physical state.

Kelvin's current necessary admissibility theorem now enforces precisely this kind of
requirement before an actual first-bad rule is accepted.  Its additional conditions
on support locality, persistent-library memory, full coherence and adaptive joint law
remain separately necessary; gauge invariance alone is not sufficient.

On the Wang side, current hard roles are already registered as physical event-owner
observables rather than arbitrary packet-coordinate labels.  The common
cross-program rule is therefore only:

\[
\boxed{
\text{role/selector logic must act on physical state, not representation gauge}.}
\]

This does **not** identify Wang hard roles with Kelvin first-bad selectors.

**Label: RIGOROUS CONSEQUENCE / CROSS-PROGRAM DICTIONARY.**

---

## 7. State-map consequence

A literal Wang--Kelvin state map cannot use raw packet coefficients as physical state
unless it also carries the packet frame and quotients by the passive gauge.  The
minimal physical datum at this face is the invariant residual itself, or an equivalent
frame-plus-coefficient class:

\[
\boxed{
r
\longleftrightarrow
[H,\epsilon]_{(H,\epsilon)\sim(HS,S^T\epsilon)}.}
\]

If a candidate badness rule uses a quadratic residual size, the exact physical scalar
is

\[
\boxed{
|r|^2
=\epsilon^T(H^TH)^{-1}\epsilon,}
\]

not `|epsilon|^2`.

The remaining actual first-bad score, timing, support-locality theorem and library
assembly remain Open-literal upstream.

**Label: RIGOROUS CONSEQUENCE / OPEN BRIDGE.**

No recurrence, continuation, termination or global-regularity theorem is claimed.
