# Why every hypothesis in the parabolic killing theorem is physical and non-removable

Status: **COUNTEREXAMPLE/NO-GO ledger** for the conditional termination theorem in `docs/42_parabolic_killing_depth_criterion.md`.

The purpose is to prevent a promising termination mechanism from being promoted too early.  Each hypothesis blocks a distinct escape.

## 1. No lower parabolic face: infinite forward depth can have finite killing hazard

Fix `lambda>1`, let

\[
N_n=N_0\lambda^n,
\qquad
\tau_n=C\lambda^{-4n}.
\]

Then

\[
a_n=2\nu N_n^2\tau_n
=2\nu C N_0^2\lambda^{-2n}\to0.
\]

On the interval between successive event times, the viscous hazard is of order

\[
2\nu N_n^2(\tau_n-\tau_{n+1})
\asymp \lambda^{-2n},
\]

which is summable.  Thus an infinite geometric forward scale sequence can fit into finite total killing hazard if the event slides below the parabolic lower face.

**Classification: COUNTEREXAMPLE/NO-GO at the exact scale-clock kinematic level.**

This is why `a>=alpha>0` cannot be replaced by the vague statement “high frequency.”

## 2. Reverse jumps can refund the heat coordinate without paying viscosity

At fixed physical time a forward jump `N -> lambda N` raises `a`, while a reverse jump `lambda N -> N` lowers it instantaneously.  Alternating the two can create arbitrarily many forward counts without requiring the continuous clock to lower `a`.

Therefore internal continuation must be one-sided in the parabolic coordinate.  Reverse/nonforward work must be an absorbing exit or be charged to a separate physical owner.  Current Wang's positive nonforward work and coarse self-loops are exact physical reminders of this distinction.

## 3. No upper scale-ratio bound: the critical energy floor can collapse too quickly

The survival theorem gives a depth-`n` upper of the form

\[
M_n\lesssim e^{-cn}.
\]

A scale-critical floor gives only `E_n>=eta/N_n`.  If `N_n` is allowed to grow super-exponentially, for example

\[
N_n=e^{2cn}N_0,
\]

then the required event mass decays like `e^{-2cn}`, faster than the survival upper.  No contradiction follows.

Thus the upper progress ratio `N_{j+1}/N_j<=Lambda` is logically independent of the lower forward ratio.

## 4. No scale-critical mass floor: a zero-mass exceptional branch remains possible

Finite expected energy-lineage depth and exponential surviving mass do not exclude a deterministic sequence of event labels whose carried energy tends to zero faster than the survival tail.  A physical event lower such as

\[
N_jE_j\ge\eta
\]

or another equally coercive same-lineage lower is required to turn mass depletion into event termination.

This is exactly where a genuine first-bad definition must enter; it cannot be supplied by the transport representation itself.

## 5. Re-entry/cloning restarts the finite budget

The stopped-lineage theorem assumes that once energy exits the typed continuation corridor it does not later reappear as the **same** selected lineage for free.  If an external source, fresh-service branch, or observer relabeling can inject new selected mass at every depth, each injection starts a new survival budget and the finite-depth conclusion fails.

Hence state-map descent, single-charge ancestry, and literal re-entry ownership are structural hypotheses, not bookkeeping details.

## 6. Parabolic matching is the exact acceptance test for the next first-bad theorem

The conditional proof mechanism therefore needs all of the following from the actual NSE event semantics:

1. a true physical first-bad/continuation state;
2. a same-lineage positive energy lower;
3. parabolic lower and upper faces for `2nu(T-t)N^2`;
4. bounded forward scale ratios on continuing events;
5. reverse/nonforward transitions typed as exits;
6. no free re-entry or cloning after exit.

If NSE supplies these, `docs/42_parabolic_killing_depth_criterion.md` gives finite depth.  If one item fails, that failure identifies the exact physical owner/escape that must be studied next.

**Classification: OPEN BRIDGE / SHARP ACCEPTANCE LEDGER.**
