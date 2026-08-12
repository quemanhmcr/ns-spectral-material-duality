# Record-derived highest critical shell as a PDE-facing first-bad candidate

Status: **RIGOROUS RECORD-EVENT CONSTRUCTION** plus **OPEN BRIDGE** for promotion to the programme's literal first-bad selector.

The current Kelvin first-bad implementation still receives Boolean `bad_flags` from outside the PDE.  The enstrophy record theorem suggests a more intrinsic candidate: let the exact NSE growth gate itself create the active shell event.

## 1. PDE-derived critical amplitude level

Theorem BA gives, at every nontrivial enstrophy record-growth time,

\[
B_{1/2}(u)
:=\sup_q\lambda_q^{1/2}\|P_qu\|_2
\ge\frac\nu{C_{LP}}.
\]

Fix any strict fraction

\[
0<\theta<1
\]

and put

\[
\boxed{
A_*:=\theta\frac\nu{C_{LP}}.
}
\]

At every record-growth time the active set

\[
\mathcal A(t)
=\left\{q:\lambda_q^{1/2}\|P_qu(t)\|_2\ge A_*\right\}
\]

is nonempty.

Because `u(t)` is smooth for every `t<T`, its high-frequency dyadic energies decay faster than any power; hence `A(t)` is bounded above in shell index.  Therefore the highest active shell

\[
\boxed{
q_*(t)=\max\mathcal A(t)
}
\]

exists at every record-growth time.

Its physical shell energy obeys the fixed active-event floor

\[
\boxed{
\lambda_{q_*}\|P_{q_*}u(t)\|_2^2
\ge A_*^2.
}
\]

Every strictly higher shell is subcritical in the same scale-invariant amplitude:

\[
\boxed{
q>q_*(t)
\Longrightarrow
\lambda_q^{1/2}\|P_qu(t)\|_2<A_*.
}
\]

This is not an arbitrary raw-amplitude threshold: its scale and units are forced by the exact enstrophy-work/viscosity gate.

## 2. First higher critical crossing

Starting from one record event `(t_0,q_0)`, define the next **higher critical crossing time** as the first `t>t_0` for which some `q>q_0` satisfies

\[
\lambda_q^{1/2}\|P_qu(t)\|_2=A_*.
\]

Before that crossing, every shell above `q_0` remains strictly subcritical in the PDE-derived critical amplitude.

If no such crossing occurs before the next enstrophy record, the new record must either be supported at/below the old critical scale or be generated through a low-frequency strain/catalyst mechanism acting on a subcritical tail.  Those are physically different alternatives rather than an untyped “bad flag.”

## 3. Optional hysteresis for a hard selector

To avoid grazing observer switches, choose

\[
0<\theta_-<\theta_+<1
\]

and corresponding levels `A_-<A_+`.  Activate a shell only when it reaches `A_+`; retain it until it falls below `A_-` or a higher shell activates.

This produces a mathematically well-defined hysteretic spectral selector, but it is not yet declared the Kelvin programme's physical first-bad selector.  To make that identification one must still prove:

- state-map/kernel purity of the event under any reduced ancestry representation;
- physical meaning of the resolve rule;
- compatibility with material/current shape and actual exit/reentry owners.

## 4. Why this candidate is useful even before promotion

It gives a sharp PDE-facing acceptance test for the subparabolic seam:

- if `q_*` lies in the matched heat corridor, killed-lineage/corridor theorems apply;
- if `q_*` is subparabolic, the higher tail is **uniformly critical-subthreshold** until the next crossing, so any record growth must be traced to low-scale strain/catalyst or to the crossing event itself;
- if a higher shell appears by a nonlocal jump, Theorem BI forces a comparable high-frequency companion at that physical event.

Thus the remaining first-bad problem can be formulated without a free Boolean oracle.

**Classification: OPEN BRIDGE for full first-bad/regularity use.**
