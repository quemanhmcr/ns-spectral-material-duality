# Spectral cutoff changes repartition the Cartan/material strain exactly; they do not create a new owner

Status: **EXACT NSE REPARTITION / EXACT MATERIAL-METRIC GAUGE IDENTITY**.

## 1. Scalar Fourier resolution preserves the physical tensor types

Let `R(D)` be a real scalar Fourier multiplier commuting with spatial derivatives, and split the actual state

\[
V=Ru,\qquad h=(I-R)u.
\]

Because `R` is scalar,

\[
\nabla V=R(\nabla u),\qquad \nabla h=(I-R)(\nabla u).
\]

Therefore

\[
\boxed{S_u=S_V+S_h,\qquad \Omega_u=\Omega_V+\Omega_h,}
\]
with

\[
S_V=RS_u,\quad S_h=(I-R)S_u,
\qquad
\Omega_V=R\Omega_u,\quad \Omega_h=(I-R)\Omega_u.
\]

The decomposition changes amplitudes and scale support, but it does not mix symmetric deformation with skew connection.

## 2. The whole resolved linearized Cartan split is affine in the transporter

The linearized operator is linear in its base field:

\[
\mathcal L_{V+h}=\mathcal L_V+\mathcal L_h.
\]

By Theorem CW this refines type-by-type:

\[
\boxed{
\mathcal K_u=\mathcal K_V+\mathcal K_h,
\qquad
\mathcal S_u=\mathcal S_V+\mathcal S_h.
}
\]

Now compare two analysis cutoffs `R_0,R_1`, with

\[
V_j=R_ju,\qquad h_j=(I-R_j)u,\qquad \delta V=(R_1-R_0)u.
\]

Then exactly

\[
\boxed{
\mathcal K_{V_1}-\mathcal K_{V_0}=\mathcal K_{\delta V},
\qquad
\mathcal S_{V_1}-\mathcal S_{V_0}=\mathcal S_{\delta V},
}
\]
while

\[
\boxed{
\mathcal K_{h_1}-\mathcal K_{h_0}=-\mathcal K_{\delta V},
\qquad
\mathcal S_{h_1}-\mathcal S_{h_0}=-\mathcal S_{\delta V}.
}
\]

Thus a cutoff change transfers connection and metric velocity between resolved and unresolved sectors with equal and opposite increments.  It does not mint a third interface tensor.

## 3. Full Kelvin metric velocity is invariant under the repartition

Let `H_u,M_u` denote the full material frame/metric, and let `H_V,M_V` and `H_h,M_h` denote the analysis flows generated separately by `V` and `h`.  Their raw metric histories are different, but after conjugation to the common Eulerian tensor space,

\[
H_u\dot M_uH_u^T=2S_u,
\]

\[
H_V\dot M_VH_V^T=2S_V,
\qquad
H_h\dot M_hH_h^T=2S_h.
\]

Hence instantaneously at the same physical point/time,

\[
\boxed{
H_u\dot M_uH_u^T
=H_V\dot M_VH_V^T+H_h\dot M_hH_h^T.
}
\]

This equality is between **Eulerian metric-velocity tensors** after their own frame conjugations.  It does not identify the three deformation histories or raw metrics.

Under `R_0 -> R_1`, the resolved Eulerian metric velocity gains `2S_{delta V}` and the unresolved one loses exactly the same tensor.  Full physical Kelvin metric velocity is unchanged.

## 4. Role matrices inherit the same gauge law

For fixed physical probes/roles `w_a`,

\[
\mathbf S^{(R)}_{ab}=\int w_a\cdot S_{Ru}w_b\,dx,
\]

so

\[
\boxed{
\mathbf S^{(R_1)}-\mathbf S^{(R_0)}
=\left[\int w_a\cdot S_{\delta V}w_b\,dx\right]_{ab}.
}
\]

The increment is symmetric.  The analogous `K` increment is skew.  Therefore Wang cutoff repartition preserves the Cartan owner types exactly.

## 5. Interpretation

This sharpens current Wang's exact statement that changing the resolved cutoff repartitions the same `-Q B(u,u)` interaction.  At the material level, what is being repartitioned is equally rigid:

\[
\boxed{
\text{resolved connection/metric work}
\leftrightarrow
\text{unresolved connection/metric work},
}
\]

with the full physical tensor fixed.

No cutoff choice is promoted to a physical material flow, and no cutoff-switch currency is created.
