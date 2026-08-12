# Rate-critical comparable pair creation forces full-dimensional Fourier participation at fixed critical mass

Status: **RIGOROUS LATE-STAGE FOURIER CONSEQUENCE AFTER EXACT OWNER CLASSIFICATION**.

## 1. Start only with the final comparable heterochiral owner

Fix a dyadic physical scale block with maximum triad frequency below `2N`.  Let `c_k` be the helical `l^2` amplitude at wavevector `k`,

\[
c_k^2=|a_{k,+}|^2+|a_{k,-}|^2.
\]

For every fully comparable heterochiral triad, CI gives the crude universal pointwise capacity bound

\[
\mathcal P_\triangle
\le \sqrt2 K^2
\prod_{i=0}^2\bigl(|a_{i,+}|+|a_{i,-}|\bigr).
\]

Since `|a_+|+|a_-|<=sqrt(2)c_k` and `K<2N`, overcounting by ordered parent pairs gives the safe aggregate estimate

\[
\boxed{
\mathcal P_N^{cmp}
\le\frac{64}{27}N^2
\sum_{p,q}c_pc_qc_{-p-q}.
}
\]

Young/Cauchy on this already-typed physical owner gives

\[
\sum_{p,q}c_pc_qc_{-p-q}
\le
\|c*c\|_2\|c\|_2
\le
\|c\|_1\|c\|_2^2.
\]

Therefore

\[
\boxed{
\mathcal P_N^{cmp}
\le\frac{64}{27}N^2\|c\|_1\|c\|_2^2.
}
\]

## 2. Effective spectral participation

Put

\[
E_N^{part}=\|c\|_2^2,
\qquad
M_{eff}:=\frac{\|c\|_1^2}{\|c\|_2^2}.
\]

Then

\[
\mathcal P_N^{cmp}
\le\frac{64}{27}N^2\sqrt{M_{eff}}\,(E_N^{part})^{3/2}.
\]

If the comparable heterochiral branch owns the CB gate, its actual pair action satisfies

\[
\mathcal P_N^{cmp}
\ge\frac{\nu Z_N}{128N}
\ge\frac{\nu N^3E_N}{128}
\ge\frac{\nu N^3E_N^{part}}{128}.
\]

Consequently

\[
\boxed{
M_{eff}
\ge
\frac{729\,\nu^2N^2}{8192^2E_N^{part}}.
}
\]

Writing the participating critical mass as

\[
\mu_N^{part}=NE_N^{part},
\]

\[
\boxed{
M_{eff}
\ge
\frac{729\,\nu^2N^3}{8192^2\mu_N^{part}}.
}
\]

The constants are intentionally safe; the structural content is the full `N^3` scaling.

## 3. Fixed critical mass excludes sparse-triad rate criticality

At a PDE-derived first critical crossing with

\[
\mu_N^{part}\lesssim C\nu^2,
\]

rate-critical comparable pair creation requires

\[
\boxed{M_{eff}\gtrsim_C N^3.}
\]

But `M_eff` is at most the actual number of participating Fourier/helicity cells up to the finite helical factor.  Therefore any family with only `o(N^3)` effective modes is asymptotically incapable of carrying the rate-critical CB owner at fixed critical mass.

In particular, a finite-triad or fixed-width Hadamard ladder can be phase/topology compatible and still be dynamically far too weak at high scale.

## 4. Physical interpretation

The true critical obstruction, if it exists, must use essentially full-dimensional Fourier participation together with enough phase coherence to make the convolution large.  Equivalently, it is a physical-space concentration/coherent-packet problem, not a sparse shell-model problem.

This is the precise point where Wang's sharp Young/coherent packet machinery becomes relevant again -- **after** the global owner has been reduced to comparable heterochiral pair creation.

No near-extremality is claimed merely from the participation lower bound, and no regularity conclusion is made.
