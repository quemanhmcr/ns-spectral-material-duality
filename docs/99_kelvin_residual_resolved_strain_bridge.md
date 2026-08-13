# Kelvin reconstructed residual and Wang resolved work probe the same strain tensor, with an explicit unresolved correction

Status: **EXACT CROSS-PROGRAMME CONSEQUENCE AT CURRENT HEADS / EXACT NS NO-GO AGAINST RESOLVED-FULL METRIC CONFLATION**.

This note compares current Kelvin `8eb6bb1597...` with the Wang resolved `K/S` geometry through the tensor they literally share.  It does not equate their scalar observables.

## 1. Start from the current Kelvin full-state law

Current Kelvin proves on the literal reverse-age current-shape state that the reconstructed physical residual `r` obeys

\[
dr=-A_ur\,d\sigma+\sqrt{2\nu}\,\widehat Q\,dW_B,
\]

with

\[
A_u=\nabla u,
\qquad
S_u=\operatorname{sym}A_u.
\]

Hence

\[
\boxed{
\frac d{d\sigma}\frac12|r|^2\Big|_{drift}
=-r\cdot S_ur+\nu\|\widehat Q\|_F^2.
}
\]

The strain term and q.v. term are different physical owners.

## 2. Insert the actual spectral decomposition `u=V+h`

For any real scalar resolved multiplier used by Wang/repo 3,

\[
u=V+h,
\qquad
S_u=S_V+S_h.
\]

Therefore the same Kelvin residual law has the exact owner refinement

\[
\boxed{
\frac d{d\sigma}\frac12|r|^2\Big|_{drift}
=-r\cdot S_Vr
-r\cdot S_hr
+\nu\|\widehat Q\|_F^2.
}
\]

The first deterministic term is the **same resolved strain tensor** whose divergence-free spatial bilinear form is Wang's `S` operator.  The second is the unresolved-strain correction.  The third is Kelvin anchor q.v. injection.

Thus Wang and Kelvin do not acquire a new common scalar currency.  They acquire a common **local symmetric tensor owner** `S_V`, probed by different physical observables.

## 3. Cross dyad reads the same bilinear form

Kelvin also has

\[
d\omega=-A_u\omega\,d\sigma+\sqrt{2\nu}\nabla\omega\,dW_B,
\]

and cross q.v.

\[
\Gamma_{\omega r}=2\nu(\nabla\omega)\widehat Q^T.
\]

Taking the drift of the scalar cross pairing gives

\[
\boxed{
\frac d{d\sigma}(\omega\cdot r)\Big|_{drift}
=-2\,\omega\cdot S_ur
+\operatorname{tr}\Gamma_{\omega r}.
}
\]

After `u=V+h`,

\[
\boxed{
\frac d{d\sigma}(\omega\cdot r)\Big|_{drift}
=-2\,\omega\cdot S_Vr
-2\,\omega\cdot S_hr
+\operatorname{tr}\Gamma_{\omega r}.
}
\]

The skew connection cancels exactly from this symmetric cross observable.  The signed cross q.v. does not.

This is the Kelvin analogue of Wang's off-diagonal symmetric role work: both are evaluations of

\[
\mathfrak s_V(a,b):=a\cdot S_Vb.
\]

## 4. Same tensor, different probes

For Wang event roles,

\[
\mathbf S_{ab}=\int\mathfrak s_V(w_a,w_b)\,dx.
\]

For Kelvin reconstructed geometry,

\[
-r\cdot S_Vr=-\mathfrak s_V(r,r),
\qquad
-2\omega\cdot S_Vr=-2\mathfrak s_V(\omega,r).
\]

These are not equal charges and need not have the same sign.  What is identical is the local tensor owner being interrogated.

This is the correct strengthening of both programmes: Wang receives a literal material/Kelvin tensor interpretation of its `S` branch, while Kelvin receives a literal spectral-role decomposition of one component of its deterministic strain drift.

## 5. Exact NS no-go: resolved metric velocity is not full material metric velocity

Consider the exact periodic Navier--Stokes shear family

\[
u(x,y,z,t)=(U(y,t),0,0),
\]

with

\[
U(y,t)=a e^{-\nu t}\sin y+b e^{-4\nu t}\sin2y.
\]

The convection vanishes identically and `U_t=nu U_yy`, so this is an exact smooth 3D periodic NSE solution with zero pressure gradient.

Let the resolved cutoff retain only the `|k|=1` mode.

### Full material active, resolved metric silent

Take `a=0`, `b\ne0`.  Then

\[
S_V=0,
\qquad
S_u=S_h\ne0
\]

at generic points.  Full Kelvin/material metric velocity is active while Wang resolved strain is zero.

### Resolved metric active, full material instantaneously silent

Fix `t=t_*`, take `a\ne0`, and choose

\[
b=-\frac a2 e^{3\nu t_*}.
\]

At `y=0`,

\[
\partial_yU
=a e^{-\nu t_*}+2b e^{-4\nu t_*}=0,
\]

so

\[
S_u(0,t_*)=0,
\]

while

\[
S_V(0,t_*)\ne0,
\qquad
S_h(0,t_*)=-S_V(0,t_*).
\]

Thus the resolved material metric can be active while the full physical material metric velocity cancels at the same point/time.

Therefore

\[
\boxed{
S_V\text{ alone neither determines nor is determined by }S_u.
}
\]

Only the exact typed identity `S_u=S_V+S_h` may be used.

## 6. Scope

This bridge does not claim a Kelvin first-bad selector, ancestry lift, future bank, event count, or regularity result.  It sharpens the two programmes at their shared local PDE tensor:

\[
\boxed{
\text{resolved spectral strain}
\longleftrightarrow
\text{resolved material metric velocity}
\longrightarrow
\text{one exact component of full Kelvin strain drift}.
}
\]

The unresolved correction, q.v., connection, localization/interface and clock faces remain separate physical phenomena.
