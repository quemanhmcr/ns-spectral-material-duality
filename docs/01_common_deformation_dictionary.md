# Common deformation dictionary

Status: **exact kinematic identities plus local quantitative consequences**.

## 1. Fourier wavefronts are material surfaces in an affine flow

For `x_dot=A x` and `k_dot=-A^T k`,

\[
\frac{d}{dt}(k\cdot x)=0.
\]

Hence Kelvin/Fourier phase planes are material surfaces, and Fourier wavevectors and material area normals are the same type of advected covector.

## 2. Dual metrics

With deformation gradient `F`,

\[
M=F^TF,
\qquad
k=F^{-T}k_0,
\]

so

\[
|k|^2=k_0^TM^{-1}k_0.
\]

Material geometry sees `M`; spectral geometry sees `M^{-1}`.

## 3. Strain from metric velocity

For `H=F^{-T}` and incompressible velocity gradient `A=S+W`,

\[
\dot H=-A^TH,
\qquad
M=(H^TH)^{-1},
\]

and

\[
\boxed{H\dot M H^T=2S.}
\]

Thus the symmetric deformation generator in a Fourier transverse plane is the restriction of the material metric velocity.

## 4. Objective strain variation from metric acceleration

Write `Q=H\dot M H^T=2S`. Then

\[
\boxed{
\mathring S
:=D_tS+SW-WS
=\frac12H\ddot M H^T-\frac12Q^2.
}
\]

This is a kinematic identity. Substitution of the NSE velocity-gradient equation converts it into a PDE identity for material-metric curvature.

## 5. Triad Hodge coordinates directly from `M^{-1}`

Start from a symmetric optimal parent pair with unit directions `n_a,n_b`, child direction `n_c`, parent/child ratio `r_*`, and deform all covectors by `F^{-T}`. Define

\[
q_j=n_j^TM^{-1}n_j.
\]

After normalizing the deformed child magnitude to one,

\[
x=r_*\sqrt{q_a/q_c},
\qquad
y=r_*\sqrt{q_b/q_c}.
\]

Therefore the signed Hodge coordinates are

\[
\boxed{u=\frac12\log(q_b/q_a)},
\]

\[
\boxed{v=\frac14\log\frac{q_c^2}{q_aq_b}}.
\]

Thus the near-extremal spectral shape defect is an observable of the inverse material metric.

## 6. Local consequence

On the certified local single-edge region of the upstream spectral programme,

\[
1-\frac{J}{J_*}\ge \frac12\left(\frac{u^2}{2}+2v^2\right).
\]

For constant planar trace-free strain with eigenvalues `±d`, the upstream affine result gives, for `dT<=1/25`,

\[
\frac{u^2}{2}+2v^2\ge\frac35(dT)^2.
\]

Since the material metric condition number is

\[
\kappa(M)=e^{4dT},
\]

one obtains the local bridge

\[
\boxed{
1-\frac{J}{J_*}
\ge
\frac{3}{160}(\log\kappa(M))^2.
}
\]

This is local and orientation-sensitive; condition number alone does not encode the full triad response.

## 7. Holonomy

Two noncommuting symmetric strains generate a second-order rotation. For

\[
D_1=\begin{pmatrix}d&0\\0&-d\end{pmatrix},
\quad
D_2=\begin{pmatrix}0&b\\b&0\end{pmatrix},
\]

and `F=exp(eps D_2)exp(eps D_1)`, the polar rotation obeys

\[
\tan\theta=\tanh(b\varepsilon)\tanh(d\varepsilon)
=bd\varepsilon^2+O(\varepsilon^4).
\]

The leading rotation is the same commutator/Magnus holonomy seen by objective helical polarization. The symmetric metric does not itself contain this rotation; connection data must be retained separately.
## 8. Current Cartan/non-affine extension

The original metric dictionary above remains exact, but the bridge has since been sharpened substantially.  The current integrated PDE spine is recorded in [`docs/122_core_pde_bridge_spine.md`](122_core_pde_bridge_spine.md): the resolved/unresolved Cartan `K/S` split, exterior line/area/top-form ladder, projector connection gauge, typed pressure and viscosity, Wang objective `SL(2)` polarization/material holonomy, and the exact common non-affine Hessian jet `B=\mathfrak J_2(L)`.

That extension deliberately keeps programme-specific quotients distinct; it should be read as a strengthening of this dictionary, not as an assertion that Wang and Kelvin observables are globally equivalent.
