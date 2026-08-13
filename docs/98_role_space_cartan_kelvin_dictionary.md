# Wang role-space `K/S` is a skew 2-form plus a material metric-velocity form

Status: **EXACT ROLE-GAUGE CONSEQUENCE / EXACT TRANSPOSE-DUALITY / NO-GO AGAINST CONNECTION CONFLATION**.

## 1. Complete event roles see two tensors, not many owners

Let `{P_a}` be any finite complete orthogonal role partition of a divergence-free high field and write `w_a=P_a h`.  Define

\[
\mathbf K_{ab}=\langle w_a,\mathcal K_Vw_b\rangle,
\qquad
\mathbf S_{ab}=\langle w_a,\mathcal S_Vw_b\rangle.
\]

Then exactly

\[
\boxed{
\mathbf K^T=-\mathbf K,
\qquad
\mathbf S^T=\mathbf S.
}
\]

Thus the role decomposition reads the resolved PDE through only two algebraic objects:

- a skew role-space 2-form `K`, which is conservative redistribution;
- a symmetric role-space form `S`, which is deformation/metric work.

For coefficients `c_a` and `h_c=\sum_ac_aw_a`,

\[
\boxed{
\langle h_c,\mathcal L_Vh_c\rangle
=c^T\mathbf S c,
\qquad
c^T\mathbf Kc=0.
}
\]

## 2. Role changes are coordinates, not physical resets

Let `O` be an orthogonal change of basis inside the same physical role subspace and put

\[
w'_a=\sum_bw_bO_{ba}.
\]

Then

\[
\boxed{
\mathbf K'=O^T\mathbf KO,
\qquad
\mathbf S'=O^T\mathbf SO.
}
\]

Hence diagonal/off-diagonal strain work and individual skew relay edges can move under role coordinates, while the underlying 2-form/symmetric form do not change.

In particular,

\[
\operatorname{tr}\mathbf S'=\operatorname{tr}\mathbf S,
\qquad
\mathbf K'_{aa}=0.
\]

This supplies a geometric explanation for Wang's theorem that a role-interface branch is not a new source: it is an off-diagonal coordinate reading of the same physical `K/S` tensors.

## 3. Material metric representation of the entire symmetric role matrix

Using the resolved material frame of Theorem CW,

\[
\boxed{
\mathbf S_{ab}
=\frac12\int
(H_V^Tw_a)^T\dot M_V(H_V^Tw_b)\,dx.
}
\]

So the **whole** Wang strain matrix, including interface cross terms, is exactly the matrix of one material metric-velocity bilinear form in the chosen event-role coordinates.

The interface/diagonal distinction is representation.  The material strain tensor is physical.

## 4. Vector and Kelvin connections are transpose-dual

For the same local gradient

\[
A=S+\Omega,
\]

the vector generator uses `A`, whereas the dual covector/area generator uses `A^T` (with the appropriate forward/reverse time sign).  Therefore

\[
\boxed{
A-A^T=2\Omega=[\omega]_\times,
\qquad
\operatorname{sym}A=\operatorname{sym}A^T=S,
\qquad
\operatorname{skew}A^T=-\Omega.
}
\]

The symmetric deformation owner survives the vector/covector duality unchanged; the connection sector flips orientation.

Therefore

\[
\boxed{
\text{Wang }S\leftrightarrow\text{Kelvin metric strain exactly},
\qquad
\text{Wang }K\not\equiv\text{Kelvin connection without dualization}.
}
\]

This prevents a silent identification of conservative role relink with a Kelvin circulation/current connection.

## 5. Why quadratic metric observables forget the skew connection

For any vectors `a,b`,

\[
a\cdot\Omega a=0,
\]

and

\[
(\Omega a)\cdot b+a\cdot(\Omega b)=0.
\]

Thus norms and symmetric cross dyads see only `S`; orientation, phase and circulation can still see `Omega`.  This is why metric work is the exact common bridge while connection information must remain a separate side of both programmes.
