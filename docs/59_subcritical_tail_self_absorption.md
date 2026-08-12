# Subcritical ultraviolet self-interaction is viscosity-absorbable; growth must enter through an external incidence owner

Status: **EXACT HIGH-TAIL OWNER SPLIT / RIGOROUS LP CONSEQUENCE**.  The estimate is applied only after the nonlinear pieces have been physically typed.

## 1. Exact high-tail equation before any estimate

Fix one hard Fourier cutoff `Q` on a smooth NSE interval and write

\[
v=P_{\le Q}u,
\qquad
h=P_{>Q}u,
\qquad
u=v+h.
\]

Because the projection is fixed and commutes with `Delta`, the exact high-tail enstrophy balance is

\[
\boxed{
\frac12\frac d{dt}\|\nabla h\|_2^2
+
\nu\|\Delta h\|_2^2
=
\mathcal W_{ext,Q}
+
\mathcal W_{hhh},
}
\]

where

\[
\mathcal W_{hhh}
=
\left\langle
P_{>Q}\mathbb P(h\cdot\nabla h),\Delta h
\right\rangle
\]

is the **pure tail self-interaction**, and

\[
\boxed{
\mathcal W_{ext,Q}
=
\left\langle
P_{>Q}\mathbb P
\bigl(v\cdot\nabla v+v\cdot\nabla h+h\cdot\nabla v\bigr),
\Delta h
\right\rangle
}
\]

contains every term with at least one lower-frequency leg.

The three external pieces have different physical meanings:

- `v·grad v`: low--low boundary generation, confined by Fourier support to the finite boundary band above `Q`;
- `v·grad h`: low transport of the high field, conservative before localization and capable of radial/cutoff flux;
- `h·grad v`: resolved strain/deformation work on the high field.

After a smooth carrier is introduced, current Wang further quotients common observer transport and splits resolved incidence into conservative skew donor/relink and symmetric strain.  None of these terms is renamed pure HH self-generation here.

## 2. Restrict the record-shell LP estimate to the tail itself

Define the tail critical amplitude

\[
B_{1/2}(h)
=
\sup_{q: \lambda_q>Q}
\lambda_q^{1/2}\|P_qu\|_2.
\]

The same Bony/frequency-triad proof used in Theorem BA, now applied only to `h`, gives

\[
\boxed{
|\mathcal W_{hhh}|
\le
C_{tail} B_{1/2}(h)\,\|\Delta h\|_2^2.
}
\]

This is not a new norm owner.  It is the late estimate of one already-identified physical mechanism: self-interaction entirely inside the subcritical UV population.

## 3. Highest-critical-shell selection makes pure tail self-interaction dissipative

Let `q_*` be the highest active shell of Theorem BJ and choose its activation fraction so that

\[
A_*=
\theta\frac\nu{C_{LP}},
\qquad
0<\theta<
\theta_{abs}:=
\min\!\left(1,\frac{C_{LP}}{4C_{tail}}\right).
\]

By definition of the highest active shell,

\[
q>q_*
\quad\Longrightarrow\quad
\lambda_q^{1/2}\|P_qu\|_2<A_*.
\]

Therefore for the strict higher tail `h=P_{>q_*}u`,

\[
B_{1/2}(h)<A_*
\]

and hence

\[
\boxed{
|\mathcal W_{hhh}|
\le
\frac\nu4\|\Delta h\|_2^2.
}
\]

So the higher tail cannot autonomously balance its own viscous palinstrophy while it remains below the PDE-derived critical activation level.

## 4. Any high-tail record growth forces external incidence work

At any time for which

\[
\frac d{dt}\|\nabla h\|_2^2\ge0,
\]

the exact balance and the preceding absorption give

\[
\mathcal W_{ext,Q}+\mathcal W_{hhh}
\ge
\nu\|\Delta h\|_2^2.
\]

Consequently

\[
\boxed{
\mathcal W_{ext,Q}
\ge
\frac{3\nu}{4}\|\Delta h\|_2^2.
}
\]

This is the desired physical alternative: a critical-subthreshold higher tail cannot produce a record enstrophy increase by self-interaction alone.  The growth must enter through a lower-frequency incidence/boundary owner.

Exact signs and simultaneous owner ties are retained.  The theorem does not assert that all external work is strain; resolved transport, boundary generation and interface/relink remain separately typed.

## 5. Fixed highest-active scale cannot hide a singular tail

Suppose on an interval all active shells stay at or below one fixed dyadic scale `Q`.  The low part has the deterministic energy bound

\[
\|\nabla P_{\le Q}u(t)\|_2^2
\le
C Q^2 E_*.
\]

Therefore if total `H^1` enstrophy becomes arbitrarily large while no higher critical crossing occurs, the higher-tail enstrophy must itself become arbitrarily large.  It then has arbitrarily large first-hitting levels, and at those first-hitting times its derivative is nonnegative.  Section 4 forces the external incidence work lower on each such event.

Thus an unbounded subcritical UV tail cannot be an ownerless fourth mechanism.  It is necessarily being serviced by lower-frequency incidence/boundary physics.

## 6. Scope

The theorem does not prove that the external incidence owner is globally finite.  It only removes **autonomous subcritical-tail self-generation** from the recurrence graph.

The remaining external work must be routed using its literal physical structure:

- comparable/boundary generation -> actual HH/edge work;
- nonlocal upward transfer -> high-companion geometry;
- resolved low--high incidence -> conservative relink or symmetric strain after observer quotient;
- source/material changes -> their existing typed ledgers.

This is precisely the level at which the `S` seam should hand off to `U/R` and known strain/interface routes.

No global-regularity conclusion is claimed.
