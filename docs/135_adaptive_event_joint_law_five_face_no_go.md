# Adaptive physical event laws require a fifth mixed correlation face beyond the symmetric two-replica formula

Status: **EXACT REPRESENTATION IDENTITY / RIGOROUS CONSEQUENCE / COUNTEREXAMPLE-NO-GO**.

This note starts from already-typed physical event maps rather than inventing a
statistical surrogate first.

- Kelvin pathwise selected events use the literal realized map
  `C=E_+A` on the persistent physical library.
- Wang hard roles are physical event observables; at a fixed event their exact
  pathwise role/synthesis laws remain the starting point.
- `Q` below is an already-physical quadratic payload: a state pair/dyad, coherent
  pair state, or same-replica q.v. Gram, according to the application.

Only after those objects exist do we ask what happens if the realized physical event
map itself varies across an ensemble because the event/selector is adaptive.

The latest Kelvin upstream is used read-only at
`eba4aa953117785194281aff82e3ea5720d20950`.  Its exact equal-weight two-replica
four-face law is the symmetric special case derived below.

---

## 1. First moment: adaptive event map and state cannot be decorrelated by notation

Let `(C,x)` be a random/adaptive realized physical event map and input state, with
the displayed first-moment products integrable.  Write

\[
\bar C=\mathbb E C,
\qquad
\bar x=\mathbb E x,
\qquad
\delta C=C-\bar C,
\qquad
\delta x=x-\bar x.
\]

Then exact expansion gives

\[
\boxed{
\mathbb E[Cx]
=\bar C\,\bar x
+\mathbb E[\delta C\,\delta x].}
\]

Thus `mean event map x mean state` is exact only on a closure domain where the
map--state correlation face vanishes.

**Label: EXACT ADAPTIVE EVENT IDENTITY.**

---

## 2. General quadratic payload: exact five-face law

Let `Q=Q^T` be a symmetric quadratic payload and assume the displayed quadratic/mixed
products have finite expectation.  Put

\[
\bar Q=\mathbb E Q,
\qquad
\delta Q=Q-\bar Q.
\]

Expand

\[
CQC^T
=(\bar C+\delta C)(\bar Q+\delta Q)(\bar C+\delta C)^T
\]

and use only

\[
\mathbb E\delta C=0,
\qquad
\mathbb E\delta Q=0.
\]

The exact identity is

\[
\boxed{
\begin{aligned}
\mathbb E[CQC^T]
={}&\bar C\bar Q\bar C^T \\
&+\mathbb E[\delta C\,\bar Q\,\delta C^T] \\
&+\bar C\,\mathbb E[\delta Q\,\delta C^T] \\
&+\mathbb E[\delta C\,\delta Q]\,\bar C^T \\
&+\mathbb E[\delta C\,\delta Q\,\delta C^T].
\end{aligned}}
\]

The five faces are:

1. **mean-map / mean-payload**;
2. **event-map dispersion**;
3. **left event--payload correlation**;
4. **right event--payload correlation**;
5. **cubic mixed event--payload correlation**.

If `\bar Q\succeq0`, face 2 is PSD.  Faces 3--5 are signed in general.

The fifth face is not a higher-order correction inserted by an estimate.  It is an
exact term created because the adaptive map appears on **both** sides of a quadratic
payload.

**Label: EXACT REPRESENTATION IDENTITY.**

---

## 3. Why Kelvin's current two-replica law has only four faces

For two equal-weight replicas, write

\[
C_{1,2}=\bar C\pm\frac12\Delta C,
\qquad
Q_{1,2}=\bar Q\pm\frac12\Delta Q.
\]

Then the centered pairs are exactly antisymmetric between replicas.  Therefore

\[
\mathbb E[\delta C\,\delta Q\,\delta C^T]=0
\]

by odd parity, while

\[
\begin{aligned}
\mathbb E[\delta C\bar Q\delta C^T]
&=\frac14\Delta C\bar Q\Delta C^T,\\
\bar C\mathbb E[\delta Q\delta C^T]
&=\frac14\bar C\Delta Q\Delta C^T,\\
\mathbb E[\delta C\delta Q]\bar C^T
&=\frac14\Delta C\Delta Q\bar C^T.
\end{aligned}
\]

Hence the latest Kelvin four-face identity is recovered exactly.

So the absence of the cubic face there is a **two-replica central-symmetry fact**,
not a general adaptive-event closure theorem.

**Label: EXACT UPSTREAM SPECIALIZATION / RIGOROUS CONSEQUENCE.**

---

## 4. The cubic face is irreducible: two PSD three-replica witnesses

Work in one scalar input/output dimension with three equal-weight replicas and

\[
C=(0,1,2).
\]

Then

\[
\bar C=1,
\qquad
\delta C=(-1,0,1).
\]

Consider two strictly positive payload ensembles.

### Ensemble `+`

\[
Q^+=(4,1,4),
\qquad
\bar Q=3,
\qquad
\delta Q^+=(1,-2,1).
\]

### Ensemble `-`

\[
Q^-=(2,5,2),
\qquad
\bar Q=3,
\qquad
\delta Q^-=(-1,2,-1).
\]

For **both** ensembles:

\[
\boxed{
\bar C\bar Q\bar C^T=3,}
\]

\[
\boxed{
\mathbb E[\delta C\bar Q\delta C^T]=2,}
\]

and

\[
\boxed{
\mathbb E[\delta C\delta Q]=0,}
\]

so both signed left/right correlation faces vanish.

But the cubic faces are opposite:

\[
\boxed{
\mathbb E[\delta C\delta Q^+\delta C^T]=+\frac23,}
\]

\[
\boxed{
\mathbb E[\delta C\delta Q^-\delta C^T]=-\frac23.}
\]

Therefore

\[
\boxed{
\mathbb E[CQ^+C^T]=\frac{17}{3},
\qquad
\mathbb E[CQ^-C^T]=\frac{13}{3}.}
\]

The mean face, event-dispersion face and left/right correlation faces are identical in
both cases.  The output differs **only** through the fifth face.

Thus a four-face formula obtained by deleting the cubic mixed term cannot be a
universal adaptive-ensemble identity beyond the centrally symmetric two-replica
domain.

**Label: COUNTEREXAMPLE/NO-GO with PSD payloads.**

---

## 5. Exact closure domains

The five-face law immediately identifies several honest special domains.

### Fixed realized event map

If `C` is deterministic, `delta C=0` and

\[
\mathbb E[CQC^T]=C\bar Q C^T.
\]

This is the pathwise/specified-event regime already used throughout the deterministic
event calculus.

### Event map independent of payload

If `C` and `Q` are independent, all three mixed event--payload faces vanish, but the
event-dispersion face remains:

\[
\mathbb E[CQC^T]
=\bar C\bar Q\bar C^T
+\mathbb E[\delta C\bar Q\delta C^T].
\]

So independence still does **not** justify mean-map factorization unless the event map
itself is non-random in the relevant directions.

### Centrally symmetric two-replica law

The cubic face vanishes by parity, recovering Kelvin's exact four-face theorem.

These are theorem domains, not approximations.

**Label: RIGOROUS CONSEQUENCE.**

---

## 6. Adaptive event hierarchy: quadratic synthesis raises the required joint moment order

At first order, an adaptive event needs the joint second moment

\[
\mathbb E[\delta C\delta x].
\]

At quadratic order, because `C` appears twice, a general adaptive event needs the
third mixed central moment

\[
\boxed{
\mathbb E[\delta C\delta Q\delta C^T].}
\]

Therefore an adaptive selector/event mechanism generically does not close on the
marginal means of event map and payload, nor on the symmetric two-replica four-face
ledger alone.

This is a representation-level hierarchy generated by the exact physical synthesis
map.  It is not a norm hierarchy imposed from outside.

**Label: RIGOROUS CONSEQUENCE / NO-CLOSURE PRINCIPLE.**

---

## 7. Cross-program consequence

### Kelvin

For an actual adaptive first-bad mechanism, the realized physical map is

\[
C=E_+A.
\]

If its law depends on the same persistent library payload being observed, a general
expectation-level theorem must carry enough of the **joint law of `(C,Q)`** to recover
the five faces above.  The actual badness functional/event law remains Open-literal
upstream, so no probability law is invented here.

### Wang

At a fixed physical event, Wang's hard role is an exact event observable and its
pathwise role/synthesis identities remain untouched.  But any future averaging across
**state-selected physical event roles** cannot replace the joint role-map/payload law
by a mean role map and a mean coherent pair payload unless it proves one of the exact
closure domains above.

Thus the common bridge is not that Wang and Kelvin use the same selector.  They do
not.  The common law is:

\[
\boxed{
\text{adaptive physical linear map}
+\text{quadratic physical payload}
\Longrightarrow
\text{joint map/payload correlations are state}.}
\]

**Label: EXACT REPRESENTATION DICTIONARY / OPEN BRIDGE.**

No recurrence, continuation, termination or global-regularity theorem is claimed.
