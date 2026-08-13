# Canonical HH edge total variation is a transfer capacity, not a Cartan activity norm

Status: **EXACT NSE NO-GO / CROSS-WANG TV TYPING**.

Current Wang's read-only `resolved-contact-native-binding-tv` branch correctly passes the donor-restricted canonical HH positive law through the total variation of the same signed helicity-edge measure and then through a Young capacity.  This note records what that TV can and cannot mean physically.

## 1. What TV controls

For the actual signed HH edge/work measure `dW_HH`, its total variation satisfies

\[
0\le dW_{HH}^+\le d|W_{HH}|.
\]

Thus total variation is a legitimate positive **capacity envelope for realized nonlinear transfer**.  It can dominate a canonical positive HH submeasure without re-Hahn splitting the cause.

## 2. What TV does not control

The unresolved Cartan tensors are

\[
S_h=\operatorname{sym}\nabla h,
\qquad
\Omega_h=\operatorname{skew}\nabla h.
\]

Theorem DG gives actual HH work only after these tensors are contracted with the unresolved state/roles:

\[
T_a^{HH}=\frac12\sum_b(K^{(h)}_{ab}+S^{(h)}_{ab}).
\]

Therefore cancellation or kinematic annihilation can make `dW_HH` vanish while `S_h` and `Omega_h` remain nonzero.

## 3. Exact periodic Navier--Stokes shear no-go

Take

\[
h(x,y,z,t)=(a e^{-\nu t}\sin y,0,0).
\]

This is an exact smooth periodic 3D Navier--Stokes solution with constant pressure because

\[
(h\cdot\nabla)h=0,
\qquad
\partial_th=\nu\Delta h.
\]

Hence

\[
\boxed{\mathcal B(h,h)=0}
\]

and every realized HH child work, signed edge measure and its total variation vanish:

\[
\boxed{dW_{HH}=d|W_{HH}|=0.}
\]

But at generic `y`,

\[
\nabla h
=\begin{pmatrix}
0&a e^{-\nu t}\cos y&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\]

so

\[
\boxed{S_h\ne0,\qquad \Omega_h\ne0.}
\]

Thus no universal implication of the form

\[
d|W_{HH}|=0\Longrightarrow S_h=0
\quad\text{or}\quad
\Omega_h=0
\]

is valid.

## 4. Consequence for the Wang/Kelvin bridge

Wang's HH TV is exactly what its theorem says: a measure/capacity control on **realized canonical transfer**.  Kelvin's unresolved residual-strain term may be active even when that HH transfer is zero, because Kelvin probes the local tensor `S_h`, not the transfer contraction `B(h,h)`.

Therefore

\[
\boxed{
\text{HH edge TV}
\not\equiv
\text{unresolved material deformation activity}.
}
\]

No norm lower bound should be inferred in either direction without additional physical hypotheses.
