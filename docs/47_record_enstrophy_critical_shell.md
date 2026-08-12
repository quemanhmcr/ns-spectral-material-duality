# Enstrophy record growth forces an actual scale-critical velocity shell

Status: **EXACT NSE ENSTROPHY IDENTITY**, followed by a **RIGOROUS LP CONSEQUENCE**.  This is deliberately a late estimate applied only after the physical nonlinear enstrophy-work owner has been identified.

The old uniform-root-mass hypothesis is too strong for trilinear ancestry.  A first-singularity argument needs much less: a physical floor on the **active bad event**.  Navier--Stokes itself supplies such events at enstrophy record times.

## 1. Exact global enstrophy work

For a smooth divergence-free solution set

\[
Y(t)=\|\nabla u(t)\|_2^2,
\qquad
Z(t)=\|\Delta u(t)\|_2^2.
\]

Pair NSE with `-Delta u`.  Leray projection and pressure are exact gauge sectors in this pairing, giving

\[
\boxed{
\frac12Y'(t)+\nu Z(t)
=\mathcal W_{ens}(t),
}
\]

where

\[
\mathcal W_{ens}
=\langle \mathbb P(u\cdot\nabla u),\Delta u\rangle.
\]

This is the actual nonlinear work feeding velocity enstrophy against viscous palinstrophy.

## 2. Localize the work only after identifying it

Let `P_q` be a standard dyadic Littlewood--Paley decomposition, with frequency `lambda_q~2^q`, and define the scale-critical shell amplitude

\[
\boxed{
B_{1/2}(u)
:=\sup_q\lambda_q^{1/2}\|P_qu\|_2.
}
\]

A direct Bony/frequency-triad decomposition of the **same** enstrophy work yields

\[
\boxed{
|\mathcal W_{ens}|
\le C_{LP}\,B_{1/2}(u)\,Z.
}
\]

The mechanism of the estimate is physical and scale exact:

### Low--high transport
For `p<<q`, Bernstein gives

\[
\sum_{p<q-C}\|u_p\|_\infty
\lesssim
B_{1/2}\sum_{p<q-C}\lambda_p
\lesssim B_{1/2}\lambda_q.
\]

Multiplication by one derivative on the high factor and two on the enstrophy test produces `lambda_q^4||u_q||_2^2`, exactly the palinstrophy scale.

### High--low strain
If the derivative falls on the low factor,

\[
\sum_{p<q-C}\|\nabla u_p\|_\infty
\lesssim
B_{1/2}\sum_{p<q-C}\lambda_p^2
\lesssim B_{1/2}\lambda_q^2,
\]

and the remaining high/test factors again produce the same palinstrophy weight.

### Comparable high--high, including low output
For two comparable high inputs and output `ell<=q+O(1)`, place the output test in `L^infty`:

\[
\|\Delta u_\ell\|_\infty
\lesssim \lambda_\ell^{7/2}\|u_\ell\|_2
\le B_{1/2}\lambda_\ell^3.
\]

The geometric sum `sum_{ell<=q}lambda_ell^3` is `O(lambda_q^3)`; the differentiated high input contributes the fourth power.  Finite overlap and Cauchy on comparable shells close the sum by `B_{1/2}Z`.

No shell is declared dominant before this decomposition.

## 3. Enstrophy record growth forces a uniform active-shell floor

At any time with

\[
Y'(t)\ge0,
\]

the exact identity gives

\[
\mathcal W_{ens}\ge\nu Z.
\]

For a nontrivial finite-energy state `Z>0`, so the LP inequality implies

\[
\boxed{
B_{1/2}(u(t))\ge\frac\nu{C_{LP}}.
}
\]

Hence at least one actual shell obeys

\[
\boxed{
\lambda_q\|P_qu(t)\|_2^2
\ge
\eta_{ens},
\qquad
\eta_{ens}=\frac{\nu^2}{C_{LP}^2}.
}
\]

This is a scale-critical velocity-energy floor supplied by the PDE at an active enstrophy-growth event.

**Classification: RIGOROUS CONSEQUENCE OF THE EXACT NSE WORK IDENTITY.**

## 4. A first singular time has arbitrarily late record-growth events

The standard `H^1` restart estimate follows from

\[
|\mathcal W_{ens}|
\lesssim
\|u\|_6\|\nabla u\|_3\|\Delta u\|_2
\lesssim
Y^{3/4}Z^{3/4}
\]

and Young:

\[
Y'\le C\nu^{-3}Y^3.
\]

Thus a maximal smooth solution whose `H^1` norm stays bounded has a uniform positive restart interval and cannot terminate.  Therefore at a first singular time `T`, `Y` is unbounded as `t upward T`.

Choose increasing levels `R_n -> infinity` and let `t_n` be their first hitting times.  Then

\[
t_n\uparrow T,
\qquad
Y'(t_n)\ge0,
\]

so every `t_n` carries at least one shell satisfying the fixed active-event floor above.

This gives a literal source of critical events approaching any candidate singular time without requiring a threshold on every ancestry root.

## 5. Compatibility with the amplitude-homogeneity no-go

Current Wang amplitude-entropy work correctly rejects the hypothesis

\[
N_rE_r\ge\eta
\]

for **every distinct structural root** merely from Young near-extremality.  The theorem here makes no such claim.  It says only:

> whenever the full NSE enstrophy is at a record-growth event, at least one velocity shell has a fixed scale-critical mass.

Structural parent amplitudes may still be arbitrarily imbalanced.  The active-shell floor and the multiplicative parent-product theorem are different statements.

## 6. What remains open

The record theorem does not locate the forced shell relative to the terminal heat scale `[(nu(T-t))^-1/2]`.  A low shell can catalyze high-frequency enstrophy through strain.  Therefore the next physical alternative is:

- shell lies on the active forward/parabolic energy route -> apply killed-lineage theory;
- shell acts as an old low-frequency catalyst -> test whether material/Kelvin strain can keep it coupled to the growing child scale;
- otherwise a strain/interface/relink/high-tail owner has fired.

That scale-role localization is the next bridge; no regularity conclusion is made here.
