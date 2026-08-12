# A low-strain high-frequency carrier cannot survive logarithmically many natural times without HH/relink/source input

Status: **RIGOROUS CONSEQUENCE OF THE EXACT SMOOTH `Q^2` ENERGY LAW**.  This theorem is a backward owner-forcing statement on the already-smooth pre-singular interval.  It does not assume or prove a forward lifespan.

## 1. Keep the exact carrier owners separate

Let `A(t,D)` be one real self-adjoint smooth carrier at physical scale `N`, transported by the common observer gauge already quotiented in the current Wang smooth-carrier theorem.  Put

\[
w=Au,
\qquad
E_A=\|w\|_2^2.
\]

Assume the carrier support has a fixed lower edge

\[
\boxed{|\xi|\ge c_-N}
\]

with `c_->0` throughout the typed interval.  The exact `Q^2` energy law after the low--low support moat and observer quotient is

\[
\boxed{
\frac d{dt}E_A
+2\nu\|\nabla w\|_2^2
=
W_{HH}+W_{K}+W_S+W_{src},
}
\]

where

- `W_HH` is actual smooth-carrier high--high energy work;
- `W_K` is physical conservative skew relink after common observer transport has been removed;
- `W_S` is symmetric resolved strain/deformation work;
- `W_src` denotes any separately typed source/interface remainder not already in those rows.

No term is merged before its owner is known.

## 2. On a no-input branch, only strain can multiply old carrier stock

Suppose on `[s,t]` the selected branch has **no positive** HH, relink or source input:

\[
W_{HH}^+=W_K^+=W_{src}^+=0.
\]

For the symmetric resolved operator,

\[
W_S
\le
2\|S_V\|_{op,\infty}E_A.
\]

The support lower edge gives

\[
\|\nabla w\|_2^2
\ge
c_-^2N^2E_A.
\]

Therefore the exact owner law implies only after this typing

\[
\boxed{
\frac d{dt}E_A
\le
\left(2\|S_V\|_{op,\infty}-2\nu c_-^2N^2\right)E_A.
}
\]

Write the actual strain action

\[
K_A[s,t]
=
\int_s^t\|S_V(r)\|_{op,\infty}\,dr.
\]

Gronwall gives

\[
\boxed{
E_A(t)
\le
\exp\!\left(
2K_A[s,t]-2\nu c_-^2N^2(t-s)
\right)E_A(s).
}
\]

This is not a synthetic damping estimate: the two exponential coordinates are exactly the physical viscous killing and symmetric strain work remaining after every other owner has been excluded.

## 3. A terminal critical carrier forces a named owner within a logarithmic natural window

Assume

\[
E_A(t)\ge\frac\eta N,
\qquad
E_A(s)\le E_*,
\]

with the ordinary global kinetic-energy cap `E_*`.

Fix a low-strain action threshold `K_0>0` and a desired old-stock fraction `0<delta<1`.  Define

\[
\boxed{
L_N(K_0,\delta)
=
\frac{
2K_0+
\log\!\left(\frac{E_*N}{\delta\eta}\right)
}{2\nu c_-^2N^2}.
}
\]

If the whole interval `[t-L_N,t]` were simultaneously

1. below the strain face `K_A<=K_0`, and
2. free of positive HH/relink/source input,

then Section 2 would give

\[
E_A(t)
\le
\delta\frac\eta N,
\]

contradicting the terminal critical floor.

Hence, whenever `t>=L_N`,

\[
\boxed{
\text{before }L_N\text{ elapses backward, either}
\quad
K_A>K_0
\quad\text{or}\quad
W_{HH}^++W_K^++W_{src}^+>0.
}
\]

More quantitatively, if all non-strain positive input is absent, the strain action must satisfy

\[
\boxed{
K_A[s,t]
\ge
\nu c_-^2N^2(t-s)
-
\frac12\log\!\left(\frac{E_*N}{\eta}\right).
}
\]

## 4. Current Wang high-strain threshold can be inserted literally

For the existing low-strain face take

\[
K_0=\frac1{30}.
\]

Then a sufficiently late/high critical carrier cannot remain a low-strain, no-input object across

\[
\boxed{
L_N
=O\!\left(\frac{\log N}{\nu N^2}\right).
}
\]

It must encounter one of the actual physical owners already present in the upstream architecture:

- high strain / critical resolved dissipation;
- positive HH generation;
- conservative physical relink/donor provenance;
- typed source/interface input.

The theorem does **not** count the high-strain face as a finite reset.  It only says the face or another input owner must physically appear.

## 5. Why conservative relink is not silently called generation

A positive skew `K` row may deliver energy to the selected carrier from another simultaneous role while preserving total energy across the role partition.  This is real carrier input but not generation.  Current Wang donor quotient traces it to same-event negative donor roles and gives it zero recursive depth.

Therefore Section 3 treats positive `W_K` as an owner exit from the no-input hypothesis, not as fresh kinetic energy.  Following its donor provenance is a separate ancestry operation.

## 6. Consequence for the high-companion seam

An old high-frequency companion cannot indefinitely support a critical selected carrier while remaining both

- low strain, and
- free of actual HH/relink/source input.

Viscosity erases such a carrier too quickly.  Thus the unresolved `U` seam contracts to **fresh owner recurrence**: repeated high strain, genuine HH generation, donor relink to another high stock, or typed source/material renewal.  The old-passive-companion scenario is removed without a packet mass floor.

No termination of the fresh-owner recurrence and no global-regularity conclusion is claimed.
