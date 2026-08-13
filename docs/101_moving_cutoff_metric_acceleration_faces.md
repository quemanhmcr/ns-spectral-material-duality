# A moving spectral cutoff is gauge at metric-velocity level but has an unavoidable metric-acceleration time face

Status: **EXACT MOVING-MULTIPLIER / OBJECTIVE-STRAIN IDENTITY**.

## 1. Instantaneous metric velocity

Let `R=R(t,D)` be a real scalar Fourier multiplier and

\[
V=Ru.
\]

At each fixed time,

\[
\boxed{S_V=RS_u,\qquad \Omega_V=R\Omega_u.}
\]

Thus the instantaneous resolved metric velocity is simply the filtered full strain tensor.  No `dot R` term appears in metric **velocity** itself.

## 2. Time differentiation creates a literal selector face

Because the multiplier now moves,

\[
\boxed{
\partial_tS_V=\dot R\,S_u+R\,\partial_tS_u.
}
\]

The first term is an exact time-face of the moving resolution rule.  It is absent for a fixed cutoff and cannot be renamed physical full-strain production.

For a finite instantaneous reset `R^- -> R^+` at a continuous physical state,

\[
\boxed{
S_V^+-S_V^-=(R^+-R^-)S_u.
}
\]

The full tensor `S_u` does not jump merely because the analysis cutoff does.

## 3. Exact objective-strain mismatch

Define the corotational/objective strain derivative

\[
\mathring S_v
=\partial_tS_v+v\cdot\nabla S_v+S_v\Omega_v-\Omega_vS_v.
\]

Put `h=u-V`.  Direct substitution of `S_V=RS_u` and `Omega_V=R Omega_u` gives

\[
\boxed{
\mathring S_V-R\mathring S_u
=\dot R\,S_u
+[V\cdot\nabla,R]S_u
-R(h\cdot\nabla S_u)
+\mathcal R_{rot},
}
\]
where

\[
\boxed{
\mathcal R_{rot}
=(RS_u)(R\Omega_u)-(R\Omega_u)(RS_u)
-R(S_u\Omega_u-\Omega_uS_u).
}
\]

Every term has a distinct PDE meaning:

1. `dot R S_u`: moving-cut/time-face;
2. `[V.grad,R]S_u`: resolved transport/filter interface;
3. `-R(h.grad S_u)`: unresolved incidence into the resolved strain history;
4. `R_rot`: failure of filtering to commute with the nonlinear strain/rotation commutator.

There is no fifth residual hidden behind a norm.

## 4. Material metric acceleration reads exactly the same faces

For each material geometry,

\[
\mathring S
=\frac12H\ddot M H^T-\frac12(H\dot M H^T)^2.
\]

Therefore the boxed objective-strain identity is simultaneously an exact identity for the difference between resolved material metric acceleration and the filtered full material metric acceleration.

This links Wang's moving/renewed spectral transporter calculus to Kelvin material geometry without identifying their histories.

## 5. Fixed common-slice relay versus continuously moving selector

Current Wang correctly permits changing the cutoff at a common slice because the **full nonlinear NSE source** is cutoff-independent after all repartition terms are retained.  The present theorem distinguishes two operations:

- a one-slice repartition: an analysis gauge change with a finite representation jump;
- a cutoff carried through time: a moving representation with the explicit `dot R` time-face above.

Suppressing the second face would conflate observer motion with physical strain dynamics.

No estimate, event count, or continuation statement is used.
