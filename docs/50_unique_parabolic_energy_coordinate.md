# The future-heat defect is the unique parabolic energy coordinate with unit physical killing

Status: **EXACT NSE / WEIGHTED-ENERGY GENERATOR IDENTITY**, **RIGOROUS UNIQUENESS**, and **COUNTEREXAMPLE/NO-GO** against a globally nondegenerate bounded scale currency.

The parabolic heat weight was not chosen because exponentials are convenient.  It is forced by the exact interaction between the terminal clock and viscous kinetic-energy killing.

## 1. General parabolic modal weight

Let

\[
d_i=2\nu|k_i|^2,
\qquad
\tau=T-t,
\qquad
a_i=d_i\tau.
\]

For any `C^1` scalar function `f:[0,infinity)->R`, define

\[
\mathscr F_f(t)=\sum_if(a_i(t))E_i(t).
\]

Between changes of the modal label,

\[
\dot a_i=-d_i.
\]

Using the exact energy transport-with-killing equation and the universal donor Dynkin identity,

\[
\boxed{
\dot{\mathscr F}_f
=
\sum_{i,j}[f(a_j)-f(a_i)]K_{ij}
-
\sum_i d_i\,[f(a_i)+f'(a_i)]E_i.
}
\]

This formula keeps three distinct physical actions:

- actual nonlinear energy transport through `Delta f`;
- terminal-clock motion through `f'`;
- viscous killing through `f`.

## 2. Unique zero-killing/survival coordinate

Suppose one asks that clock motion cancel viscous killing exactly for **every** modal spectrum.  Then necessarily

\[
f'+f=0.
\]

With the natural terminal normalization `f(0)=1`, the unique solution is

\[
\boxed{q(a)=e^{-a}.}
\]

Thus

\[
\mathscr H_T=\sum_iq(a_i)E_i
\]

is the unique normalized parabolic weighted energy whose derivative is pure nonlinear donor transport.

## 3. Unique unit-killing/heat-defect coordinate

Suppose instead one asks that the weighted balance retain exactly the **unweighted physical kinetic-energy killing**

\[
-\sum_i d_iE_i
\]

for every spectrum.  Then necessarily

\[
\boxed{f'+f=1.}
\]

With the natural terminal condition `f(0)=0`, the unique solution is

\[
\boxed{w(a)=1-e^{-a}.}
\]

Therefore

\[
\boxed{
\dot{\mathscr B}_T
=
\sum_{i,j}[w(a_j)-w(a_i)]K_{ij}
-
\sum_i d_iE_i
}
\]

is not one convenient member of a large family.  It is the unique normalized parabolic coordinate that converts terminal-clock motion plus viscosity into one exact physical killing ledger.

**Classification: RIGOROUS UNIQUENESS CONSEQUENCE OF THE EXACT NSE GENERATOR.**

## 4. Uniform multiplicative scale price must degenerate outside a compact parabolic corridor

For one fixed forward scale ratio `lambda>1`, the unique price is

\[
\Delta_\lambda w(a)
=w(\lambda^2a)-w(a)
=e^{-a}-e^{-\lambda^2a}.
\]

Hence

\[
\boxed{
\lim_{a\downarrow0}\Delta_\lambda w(a)=0,
\qquad
\lim_{a\uparrow\infty}\Delta_\lambda w(a)=0.
}
\]

So no fixed-ratio jump has a uniform positive price over all parabolic heights in the unique unit-killing coordinate.

More generally, any bounded continuous monotone scale coordinate has zero fixed-ratio price as `a->0`; if it has a finite limit at infinity, its fixed-ratio price also vanishes as `a->infinity`.

Thus a bounded energy currency cannot simultaneously:

1. be compatible with the finite kinetic-energy reservoir;
2. retain exact physical killing;
3. charge every multiplicative scale jump a uniform amount from `a=0` to `a=infinity`.

**Classification: COUNTEREXAMPLE/NO-GO against a universal one-scalar scale-progress budget.**

## 5. The compact corridor is therefore structural

The price function has one interior maximum.  Differentiating,

\[
-e^{-a}+\lambda^2e^{-\lambda^2a}=0
\]

gives

\[
\boxed{
a_*(\lambda)=\frac{2\log\lambda}{\lambda^2-1}.}
\]

This is the parabolic height where the unique kinetic-energy currency is most sensitive to a `lambda`-scale jump.  Away from the interior region, another physical mechanism must take over:

- `a<<1`: subparabolic/local-lifespan problem;
- `a~1`: matched future-heat progress currency;
- `a>>1`: superparabolic viscous/high-tail problem.

The three-region architecture is therefore not an arbitrary case split.  It is forced by the unique exact energy/clock/viscosity conjugation.

## 6. Relation to the remaining proof

Theorem BC says record enstrophy growth is upward squared-frequency transport.  The present theorem says the only exact bounded energy coordinate that pays that transport with the full kinetic killing rate necessarily saturates at both parabolic extremes.

Hence the remaining proof cannot be a search for a magical global scalar.  It must prove that actual first-bad transport is captured by the matched corridor or is routed to genuine sub/superparabolic owners.
