# Radial mode-set flux gives exact layer-cake formulas for enstrophy and future-heat transport

Status: **EXACT NSE / RADIAL CONTROL-VOLUME IDENTITY**.

Current Wang `ae85f4d` closes native helical mode-set energy continuity.  Specializing the mode boundary to radial sets reveals an exact layer-cake form of the third-repo donor-moment and future-heat laws.

## 1. Radial physical mode control volumes

Let

\[
\kappa_i=|k_i|^2,
\qquad
A_R=\{i:\kappa_i\le R\}.
\]

For the actual nonnegative donor flow `K_ij`, define the outward and inward radial energy currents

\[
\boxed{
\Phi_\uparrow(R)
=\sum_{\kappa_i\le R<\kappa_j}K_{ij},
}
\]

\[
\boxed{
\Phi_\downarrow(R)
=\sum_{\kappa_j\le R<\kappa_i}K_{ij}.
}
\]

Then Wang's mode-set continuity specialized to `A_R` is

\[
\boxed{
\frac d{dt}E_{\le R}
+D_{\le R}
+\Phi_\uparrow(R)
=\Phi_\downarrow(R),
}
\]

where `D_{<=R}=2nu sum_{kappa_i<=R} kappa_i E_i` is the instantaneous viscous loss inside the radial control volume.

Thus outward/inward radial flux is not inferred from a shell norm.  It is actual donor/recipient energy crossing a physical Fourier-mode boundary.

## 2. Enstrophy work is the unweighted layer cake of radial energy flux

For one forward edge,

\[
(\kappa_j-\kappa_i)_+
=\int_0^\infty
\mathbf1_{\{\kappa_i\le R<\kappa_j\}}\,dR.
\]

Therefore Tonelli gives

\[
\boxed{
F_\kappa^+
=\int_0^\infty\Phi_\uparrow(R)\,dR,
}
\]

and similarly

\[
\boxed{
F_\kappa^-
=\int_0^\infty\Phi_\downarrow(R)\,dR.
}
\]

Consequently Theorem BC becomes

\[
\boxed{
\frac12Y'+\nu Z
=\int_0^\infty
[\Phi_\uparrow(R)-\Phi_\downarrow(R)]\,dR.
}
\]

At an enstrophy record-growth time,

\[
\boxed{
\int_0^\infty\Phi_\uparrow(R)dR
\ge
\nu Z+\int_0^\infty\Phi_\downarrow(R)dR.
}
\]

This is the radial control-volume form of “enstrophy grows because kinetic energy is actually transported upward in squared frequency.”

## 3. Future-heat progress is the exponentially weighted same radial flux

Fix `T`, `tau=T-t`, and put

\[
c=2\nu\tau,
\qquad
w(\kappa)=1-e^{-c\kappa}.
\]

For every edge,

\[
w(\kappa_j)-w(\kappa_i)
=\int_{\kappa_i}^{\kappa_j}
c e^{-cR}\,dR.
\]

Summing over the donor table and using the radial currents gives

\[
\boxed{
\sum_{i,j}[w_j-w_i]K_{ij}
=\int_0^\infty
2\nu\tau e^{-2\nu\tau R}
[\Phi_\uparrow(R)-\Phi_\downarrow(R)]\,dR.
}
\]

Likewise its positive one-sided continuation price is

\[
\boxed{
F_w^+
=\int_0^\infty
2\nu\tau e^{-2\nu\tau R}
\Phi_\uparrow(R)\,dR.
}
\]

Thus the unique future-heat currency is not a second transport mechanism.  It is the **same actual radial energy current** viewed through the physical heat-survival weight.

## 4. The three parabolic regions are radial control-volume regions

Use the dimensionless radial coordinate

\[
a=2\nu\tau R.
\]

Then

- subparabolic: `a<alpha`;
- matched: `alpha<=a<=beta`;
- superparabolic: `a>beta`.

The heat kernel weight in the layer cake is exactly `e^-a`.  Hence:

- near `a=0`, heat price is small because the radius is below the diffusive scale;
- on `a~1`, the same physical flux is seen with order-one sensitivity;
- at `a>>1`, heat survival has already saturated and a high-tail/dissipation owner must take over.

This is the radial current form of Theorem BD's uniqueness/no-global-price result.

## 5. Exact radial crossing measure

Define the positive measure on radius-time

\[
\boxed{d\mathfrak F_\uparrow(t,R)=\Phi_\uparrow(t,R)\,dt\,dR.}
\]

It has units of enstrophy work.  Its two natural marginals are:

- unweighted radial moment: actual positive enstrophy-producing work;
- heat-weighted radial moment: actual matched parabolic progress currency.

No new causal probability law is created.  If normalized for diagnostics, that normalization must not be confused with the physical energy donor rates.

## 6. Proof consequence

A candidate singularity cannot hide “enstrophy creation” in a nonlocal algebraic term: the exact owner is radial energy boundary current.  The remaining proof question is now geometric/dynamical:

> can the required outward radial current recur to `T` while repeatedly avoiding matched heat killing, high-tail dissipation, catalyst erosion, strain/relink, and the already typed phase/interface/reset exits?

This is the minimal owner-cycle problem developed next.
