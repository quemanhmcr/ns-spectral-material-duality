# A reduced first-bad Boolean exists only when the physical event is kernel-pure

Status: **Exact conditional-kernel realizability criterion.**

The literal Kelvin first-bad selector consumes two discrete data types:

- `bad_flags: Sequence[bool]`;
- `resolved: bool`.

The upstream correctly leaves the physical Navier--Stokes definitions of those
Booleans open.  Independently, the ancestry-state audit shows that a reduced
ancestry label may lift to a distribution of full physical Kelvin states through a
conditional kernel

\[
\kappa_t(y,dY).
\]

This note asks a prior question: even after a full-state physical bad/resolve event
is defined, when can it be represented by the current **deterministic Boolean API**
on the reduced state?

---

## 1. Full-state bad event and reduced occupancy

Let `B_i(t)` be a genuine physical full-state bad set for germ `i`, with indicator

\[
\chi_i(Y)=1_{B_i(t)}(Y).
\]

At reduced ancestry state `y`, define

\[
\boxed{
\beta_i(y)=\int\chi_i(Y)\,\kappa_t(y,dY).
}
\]

`beta_i` is the conditional probability that the unresolved full state is physically
bad for germ `i`.

A deterministic reduced Boolean `b_i(y)` represents the full physical event exactly
iff

\[
\chi_i(Y)=b_i(y)
\quad\kappa_t(y,\cdot)\text{-a.s.}
\]

This occurs iff

\[
\boxed{
\beta_i(y)\in\{0,1\}.
}
\]

**Classification: EXACT SET-THEORETIC / CONDITIONAL-PROBABILITY IDENTITY.**

---

## 2. Same-ancestor pair disagreement is the exact obstruction

For two conditionally independent full states `Y_1,Y_2` drawn from the same reduced
ancestor,

\[
\boxed{
\beta_i(1-\beta_i)
=\frac12
\mathbb E\big[(\chi_i(Y_1)-\chi_i(Y_2))^2\mid y\big].
}
\]

Therefore

\[
\boxed{
\text{reduced hard bad flag exists}
\Longleftrightarrow
\text{same-ancestor full states always agree on badness}.
}
\]

This is the first-bad specialization of the kernel selector-purity theorem.

If

\[
0<\beta_i<1,
\]

then every deterministic Boolean assigned at `y` misclassifies a set of positive
`kappa_y` measure.  No estimate can repair this; the state resolution is simply
insufficient for the hard API.

**Classification: RIGOROUS CONSEQUENCE / NO-GO.**

---

## 3. The resolve oracle has an independent identical criterion

Let `R_i(t)` be the future physical full-state event that releases the hysteresis
freeze, with indicator `rho_i(Y)` and reduced occupancy

\[
\varrho_i(y)=\int\rho_i(Y)\,\kappa_t(y,dY).
\]

Then a deterministic reduced `resolved` Boolean exists exactly when

\[
\boxed{
\varrho_i(y)\in\{0,1\},
}
\]

or equivalently when the same-ancestor pair disagreement for the resolve event
vanishes.

Badness purity does not imply resolve purity.  These are two different event sets
and two different physical definitions, exactly as the upstream hysteresis audit
requires.

**Classification: EXACT BOOLEAN-REALIZABILITY CRITERION.**

---

## 4. Replacing a mixed Boolean by its occupancy changes the architecture

When `0<beta_i<1`, the number `beta_i` is a perfectly legitimate conditional
observable.  But it is not the current hard first-bad flag.  Substituting it for a
Boolean would replace

\[
M_{\rm fb}\in\{\text{rank-one hard projector or zero}\}
\]

by a soft/probabilistic selector with different jump, pair, and hysteresis
semantics.

Therefore

\[
\boxed{
\text{conditional occupancy}
\neq
\text{hard first-bad Boolean}
}
\]

unless occupancy is `0` or `1`.

**Classification: TYPE NO-GO.**

No soft replacement is proposed here.

---

## 5. Physical bad/resolve sets must also be gauge invariant

Kernel purity is necessary but not sufficient.  A physical full-state event must be
constant under exact representation changes that leave the Navier--Stokes state
unchanged.  The current audits already expose such changes:

- the ancestry reference gauge that leaves `q,j,L,b_+,b_-` invariant;
- passive `GL(3)` orientation reparameterization of a complete Kelvin packet;
- the `A` versus `A^T` vorticity connection gauge when the compensating localized
  source is moved consistently.

If a proposed `B_i` or `R_i` changes under one of these while the physical state is
unchanged, it is an observer/representation event rather than a Navier--Stokes
event.

**Classification: RIGOROUS NECESSARY ADMISSIBILITY CONDITION.**

---

## 6. What remains open

The theorem does **not** define the missing physical sets `B_i` or `R_i`.  The
amplitude-scaled ABC exclusions in the Kelvin upstream still rule out many naive
standalone continuation-failure thresholds.

The literal order is now forced:

1. define full-state physical bad and resolve events from actual PDE obstruction;
2. prove their gauge invariance;
3. prove kernel purity if the first-bad API remains hard/deterministic on reduced
   ancestry state;
4. only then feed the resulting Booleans into the hysteretic selector.

No restart, recurrence, or regularity conclusion is claimed.
