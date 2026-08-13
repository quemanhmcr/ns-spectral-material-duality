# Kelvin reconstructed dyads inherit the same Cartan split, with q.v. as a separate source

Status: **EXACT ITÔ/CARTAN IDENTITY / CROSS-PROGRAMME OWNER DICTIONARY**.

## 1. Start from the current Kelvin residual dyad law

Current Kelvin gives

\[
\frac d{d\sigma}[rr^T]_{drift}
=-A_u rr^T-rr^TA_u^T+\Gamma_r.
\]

Write

\[
A_u=S_u+\Omega_u,
\qquad R_r=rr^T.
\]

Then exactly

\[
\boxed{
\dot R_r\big|_{drift}
=-\{S_u,R_r\}+[R_r,\Omega_u]+\Gamma_r,
}
\]
where

\[
\{S,R\}=SR+RS,
\qquad
[R,\Omega]=R\Omega-\Omega R.
\]

The three terms have distinct geometry:

1. `-{S,R}`: symmetric deformation/metric action;
2. `[R,Omega]`: connection rotation;
3. `Gamma_r`: positive martingale q.v. injection.

## 2. Pure connection is isospectral

If `S=0` and `Gamma=0`,

\[
\dot R=[R,\Omega].
\]

Let `Q` solve

\[
\dot Q=-\Omega Q,
\qquad Q^TQ=I.
\]

Then

\[
\boxed{R(\sigma)=Q(\sigma)R(0)Q(\sigma)^T.}
\]

Therefore all eigenvalues and spectral invariants of `R` are preserved by the pure connection sector.  Infinitesimally,

\[
\operatorname{tr}[R,\Omega]=0,
\]

and for every positive integer `m`,

\[
\boxed{\frac d{d\sigma}\operatorname{tr}(R^m)=0}
\]
under pure connection.

This is the physical-dyad analogue of Wang's same-event skew relink: connection rearranges orientation without creating quadratic size.

## 3. Strain changes dyad shape and trace

For the symmetric sector,

\[
\dot R=-\{S,R\},
\]
so

\[
\boxed{
\frac12\frac d{d\sigma}\operatorname{tr}R
=-\operatorname{tr}(SR).
}
\]

For `R=rr^T`, this is exactly

\[
-r\cdot Sr.
\]

Thus the same strain tensor that Wang reads through role work is what changes Kelvin dyad magnitude/shape.

## 4. Resolved/unresolved split gives five literal faces

Insert

\[
u=V+h,
\qquad
S_u=S_V+S_h,
\qquad
\Omega_u=\Omega_V+\Omega_h.
\]

Then

\[
\boxed{
\dot R_r\big|_{drift}
=-\{S_V,R_r\}
-\{S_h,R_r\}
+[R_r,\Omega_V]
+[R_r,\Omega_h]
+\Gamma_r.
}
\]

So the full Kelvin residual dyad has exactly five typed local faces:

1. resolved material deformation `S_V`;
2. unresolved material deformation `S_h`;
3. resolved connection `Omega_V`;
4. unresolved connection `Omega_h`;
5. stochastic q.v. `Gamma_r`.

There is no generic sixth "high-frequency complexity" remainder.

## 5. Relation to Wang

Current Wang/repo-3 Cartan calculus gives the corresponding operator tensors

\[
\mathcal K_V,\mathcal S_V,
\qquad
\mathcal K_h,\mathcal S_h.
\]

The physical-space Kelvin commutators and the role-space Wang skew matrices are **different representations** of connection structure; the anticommutator strain action and the role-space symmetric matrices are different probes of the same `S_V,S_h` tensors.

Therefore the correct bridge is

\[
\boxed{
(K_V,S_V,K_h,S_h)
\quad\longleftrightarrow\quad
([R,\Omega_V],\{S_V,R\},[R,\Omega_h],\{S_h,R\})
}
\]

plus Kelvin's independent q.v. face.

No identification of role labels with current-shape coordinates is made.
