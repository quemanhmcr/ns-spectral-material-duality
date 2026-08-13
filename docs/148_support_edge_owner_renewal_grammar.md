# Support-edge compatibility and the intrinsic stretching-renewal Riccati grammar

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + ACTION STRESS TEST + OPEN BRIDGE**.

This batch attacks the next literal seam after the enstrophy record, level-set and value-space laws.  The question is no longer merely which physical face owns fresh record growth.  It is:

> if a genuine stretching-owned support edge keeps creating fresh enstrophy records, what exact Navier--Stokes mechanism renews the scale-free stretching efficiency that makes this possible?

The answer below is local and conditional on the natural theorem domain of a unique nondegenerate maximizing lineage.  It is not a continuation or global-regularity theorem.  Its role is to reduce finite-time record blow-up on such a lineage to a positive, explicitly typed **renewal excess** or to exit from the lineage theorem domain.

Current read-only upstream inputs are Kelvin `5067f87b5a921d3f260433ec4f3ee1ce0df81f2c` (intrinsic max-normalized enstrophy localization) and Wang `63178b0e7f9fabdfd8c344dab938a3d639639df5` (native material-service causal quotient).  No upstream write is made.

---

## 1. The max-normalized support edge selects its own compatible branch

Let

\[
e=\frac12|\omega|^2,
\qquad
M(t)=\max_x e(x,t),
\qquad
\mathcal A(t)=\{x:e(x,t)=M(t)\}.
\]

At every active maximum, `grad e=0`, so the material and Eulerian enstrophy rates agree:

\[
R(x,t)=D_te(x,t)=\partial_t e(x,t),
\qquad x\in\mathcal A(t).
\]

Compact max-envelope calculus gives

\[
D^+M(t)=\max_{x\in\mathcal A(t)}R(x,t),
\qquad
D^-M(t)=\min_{x\in\mathcal A(t)}R(x,t).
\]

The **numerator** of Kelvin's intrinsic normalized compatibility defect has a canonical active-set extension to `theta=1`; no boundary-speed division by `|grad e|` is made there.  Define

\[
\mathcal C_i^+=R_i-D^+M,
\qquad
\mathcal C_i^-=R_i-D^-M,
\qquad R_i=R(x_i,t),\ x_i\in\mathcal A(t).
\]

Then

\[
\boxed{\mathcal C_i^+\le0,\qquad \mathcal C_i^-\ge0.}
\]

with

\[
\boxed{\mathcal C_i^+=0\iff R_i=D^+M,}
\qquad
\boxed{\mathcal C_i^-=0\iff R_i=D^-M.}
\]

Thus the scalar support edge needs no external branch oracle.  The right-moving compatible branches are exactly the zero right-defect active branches; the left-moving compatible branches are exactly the zero left-defect branches.  Losing active branches remain real lineages, but they have nonzero signed compatibility defect relative to the support edge.

**Label: RIGOROUS CONSEQUENCE of exact NSE + max-envelope calculus.**

---

## 2. Exact periodic global-max crossing calibrates the compatibility selector

Use Kelvin's exact four-mode periodic heat-shear vorticity

\[
q=e^{1-\nu t}\cos y
+4e^{4-4\nu t}\cos2y
-e^{9-9\nu t}\cos3y
+2e^{16-16\nu t}\cos4y.
\]

At `t_*=1/nu`, the exact global maxima are `y=0,pi`, both with

\[
M=18,
\]

and exact rates

\[
R_0=-240\nu,
\qquad
R_\pi=-336\nu.
\]

Hence

\[
D^+M=-240\nu,
\qquad
D^-M=-336\nu,
\]

and the support-edge defects are

\[
\boxed{(\mathcal C_0^+,\mathcal C_\pi^+)=(0,-96\nu),}
\]

\[
\boxed{(\mathcal C_0^-,\mathcal C_\pi^-)=(96\nu,0).}
\]

Both branch rates are pure curvature rates in an exact heat shear: vortex stretching and nonlinear advection vanish.  Thus the compatibility selector is an intrinsic edge/readout law; it does not manufacture a nonlinear generation owner.

**Label: EXACT NSE/PDE CALIBRATION + COUNTEREXAMPLE/NO-GO.**

---

## 3. The support-edge record admits a similarity-invariant intrinsic clock

Assume `M(t)>0` and differentiability at the active support edge.  Define intrinsic time

\[
\boxed{d\tau=\sqrt M\,dt.}
\]

Under the Navier--Stokes similarity action, `sqrt(M)` has weight `2` and `dt` has weight `-2`; hence `d tau` is similarity invariant.

At an active maximum write

\[
P=\omega\cdot S\omega,
\qquad
\mathcal D_\nu=\nu\bigl(|\nabla\omega|^2-\Delta e\bigr)\ge0.
\]

Define the scale-free stretching efficiency, viscous defect, and support-edge speed

\[
\boxed{
\sigma=\frac{P}{2M^{3/2}},
\qquad
\delta=\frac{\mathcal D_\nu}{M^{3/2}},
\qquad
\varrho=\frac{M'}{M^{3/2}}.
}
\]

Because `P=2M alpha` with `alpha=xi^T S xi`, `sigma=alpha/sqrt(M)`.  The exact record law becomes

\[
\boxed{\varrho=2\sigma-\delta,\qquad \delta\ge0.}
\]

Equivalently,

\[
\boxed{\frac{d}{d\tau}\log M=2\sigma-\delta.}
\]

Every multiplicative growth of the support edge therefore spends scale-free stretching efficiency against a nonnegative scale-free viscous defect.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 4. Specific vortex stretching obeys an exact short material law

Where `omega!=0`, let

\[
\xi=\frac{\omega}{|\omega|},
\qquad
\alpha=\xi^T S\xi.
\]

The vorticity and strain equations imply

\[
D_t\xi
=(I-\xi\xi^T)
\left(S\xi+\nu\frac{\Delta\omega}{|\omega|}\right),
\]

and, using `Omega xi=0`,

\[
\boxed{
\begin{aligned}
D_t\alpha={}&|S\xi|^2-2\alpha^2-\xi^T(\nabla^2p)\xi\\
&+\nu\,\xi^T(\Delta S)\xi
+\frac{2\nu}{|\omega|}\Delta\omega\cdot(S\xi-\alpha\xi).
\end{aligned}}
\]

On a nondegenerate enstrophy critical lineage,

\[
w_*=\dot x_*-u=-H_e^{-1}\nabla R,
\]

so the literal branch derivative is

\[
\boxed{\frac{d_*\alpha}{dt}=D_t\alpha+w_*\cdot\nabla\alpha.}
\]

Thus renewal of specific stretching has only the following exact faces: strain geometry, pressure curvature, viscosity, and relative critical transport.  No selector or material-address label supplies an additional source.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 5. The normalized stretching efficiency satisfies an exact Riccati renewal law

Now restrict to a unique nondegenerate active maximizing branch, so `M=e(x_*(t),t)` and all branch quantities are unambiguous.  Let

\[
\Pi_\perp=I-\xi\xi^T.
\]

Define the scale-free renewal excess

\[
\boxed{
\begin{aligned}
\mathfrak N={}&
\frac{|\Pi_\perp S\xi|^2}{M}
-\frac{\xi^T(\nabla^2p)\xi}{M}\\
&+\frac{\nu\,\xi^T(\Delta S)\xi}{M}
+\frac{2\nu}{M|\omega|}\Delta\omega\cdot(S\xi-\alpha\xi)\\
&+\frac{w_*\cdot\nabla\alpha}{M}
-\frac12\sigma\varrho.
\end{aligned}}
\]

Every term is similarity invariant.  Differentiating `sigma=alpha/sqrt(M)` in intrinsic time and using

\[
|S\xi|^2=\alpha^2+|\Pi_\perp S\xi|^2
\]

gives the exact identity

\[
\boxed{
\frac{d\sigma}{d\tau}=-\sigma^2+\mathfrak N.
}
\]

This is the support-edge **Riccati renewal grammar**.  The negative quadratic term is intrinsic self-dilution.  `mathfrak N` is precisely the excess supplied by transverse strain conversion, signed pressure curvature, viscosity, critical-relative transport, after paying the normalization cost of the growing support edge.

No sign is assumed for `mathfrak N`.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 6. Nonpositive renewal excess excludes finite-time support-edge blow-up on a persistent branch

Assume that from some intrinsic time `tau_0` onward:

1. the active maximizer remains one differentiable nondegenerate branch;
2. `M>0`;
3. `mathfrak N<=0`.

Then

\[
\frac{d\sigma}{d\tau}\le-\sigma^2.
\]

If `sigma_0=sigma(tau_0)<=0`, then `varrho<=2sigma<=0` and no future support-edge growth can diverge.  If `sigma_0>0`, scalar comparison gives

\[
\boxed{
\sigma(\tau)
\le
\frac{\sigma_0}{1+\sigma_0(\tau-\tau_0)}.
}
\]

Since `delta>=0`,

\[
\varrho=2\sigma-\delta\le2\sigma,
\]

hence

\[
\boxed{
M(\tau)
\le
M_0\,[1+\sigma_0(\tau-\tau_0)]^2.
}
\]

Finally `dt/dtau=M^{-1/2}`, so

\[
t-t_0
\ge
\frac{1}{\sqrt{M_0}}
\int_{\tau_0}^{\tau}
\frac{ds}{1+\sigma_0(s-\tau_0)}.
\]

The right side diverges logarithmically as `tau->infinity`.  Therefore

\[
\boxed{
\mathfrak N\le0\ \text{eventually on one persistent nondegenerate record branch}
\Longrightarrow
M\ \text{cannot diverge at finite physical time on that branch}.}
\]

This is a conditional finite-time exclusion theorem, not a global regularity result.

**Label: RIGOROUS CONSEQUENCE.**

---

## 7. Finite-time unbounded record has an endogenous renewal/geometry alternative

Suppose a smooth periodic solution exists on `[0,T)` and

\[
M(t)\to\infty
\qquad(t\uparrow T<\infty).
\]

Then it is impossible that, from some late time onward, the support edge is one persistent differentiable nondegenerate maximizing branch with `mathfrak N<=0`.

Consequently every such hypothetical finite-time unbounded record must exit through at least one of the following intrinsic channels arbitrarily late:

\[
\boxed{
\text{positive renewal excess }\mathfrak N>0
\quad\text{or}\quad
\text{support-edge theorem-domain exit}.}
\]

The second channel includes ties/branch exchange, Hessian degeneracy, support-chart loss, or another failure of the unique nondegenerate lineage hypothesis.  It is not automatically a physical generation event; it is a geometry/lineage alternative that must be resolved by its own exact PDE law.

This reduces the finite-time record problem but does not prove either channel impossible.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 8. Exact affine NSE calibrates both sides of the renewal threshold

The affine strain--spin family

\[
u=(-ax-\Omega y,\ \Omega x-ay,\ 2az)
\]

is an exact Euclidean Navier--Stokes solution whenever

\[
\Omega'=2a\Omega,
\]

because `Delta u=0` and `A'+A^2` is symmetric, hence absorbed by quadratic pressure.

### 8.1 Constant strain: zero renewal excess and only infinite-time growth

For constant `a>0`,

\[
\Omega=\Omega_0e^{2at},
\qquad
M=2\Omega^2,
\]

and

\[
\sigma=\frac{\sqrt2 a}{\Omega},
\qquad
\varrho=2\sigma,
\qquad
\boxed{\mathfrak N=0}.
\]

The Riccati law is exactly

\[
\frac{d\sigma}{d\tau}=-\sigma^2.
\]

Moreover the quadratic intrinsic-time bound in Section 6 is saturated exactly.  `M` grows exponentially in physical time but reaches infinity only as `t->infinity`.

### 8.2 Accelerating strain: positive renewal exactly balances Riccati dilution

Let `s=T-t`, choose `b>0`, and set

\[
a=\frac1{2s},
\qquad
\Omega=\frac b s.
\]

Then `Omega'=2a Omega` exactly and

\[
M=\frac{2b^2}{s^2},
\qquad
\sigma=\frac1{\sqrt2 b},
\qquad
\varrho=2\sigma.
\]

The renewal excess is

\[
\boxed{
\mathfrak N=\frac{a'}{\Omega^2}
=\frac1{2b^2}
=\sigma^2>0,
}
\]

so

\[
\frac{d\sigma}{d\tau}=0=-\sigma^2+\mathfrak N.
\]

Thus this exact affine field reaches `M=infinity` at finite `T` precisely while positive renewal balances the intrinsic Riccati loss.

This accelerating affine solution is **not periodic and not finite energy**; it is only an exact local/Euclidean NSE calibration of the renewal law and is not a counterexample to periodic or finite-energy regularity.

**Label: EXACT NSE/PDE IDENTITY + ACTION STRESS TEST calibration.**

---

## 9. Cross-program owner admission becomes sharper, not broader

Current Kelvin supplies the max-normalized filtration and its exact compatibility defect.  Section 1 shows that the `theta->1` compatibility numerator, evaluated on the active set, already contains the scalar support-edge branch selection law.  Current Wang independently fail-closes raw material-address labels: a material exit/relink name does not become a recursive physical owner without native PDE evidence.

The assembled causal order is therefore

\[
\boxed{
\text{support-edge compatibility}
\to
\text{record-generation margin}
\to
\text{stretching-renewal excess}
\to
\text{typed ancestry/service provenance}.}
\]

These arrows are **not identities of currency**.  Compatibility selects which active lineage moves the edge; the generation margin decides whether the edge grows; `mathfrak N` decides whether scale-free stretching efficiency is being renewed; ancestry/service data decide how an already physical cause is transported or admitted downstream.

The next open theorem is now sharply phrased: can positive `mathfrak N` itself be reduced to a finite-capacity/reused set of native PDE owners, or can support-edge theorem-domain exits accumulate indefinitely while the full Kelvin/Wang physical state stays admissible?

**Label: RIGOROUS CROSS-PROGRAM CONSEQUENCE + OPEN BRIDGE.**

---

## 10. Action certification

The theorem batch was audited on GitHub Actions run `31707632509`, executable SHA `51033a4f1d7a0918fe8cf157182b6e179e5d2d90`, with conclusion **success**.

Selected exp98 metrics:

- four-mode global-max residual: `0`;
- right/left support-edge defect residuals: `0 / 0`;
- constant-affine NSE symmetry / specific-stretching residuals: `0 / 0`;
- constant-affine Riccati residual: `1.202e-17`;
- constant-affine zero-renewal residual: `5.512e-17`;
- exact no-renewal bound saturation residual: `1.722e-16`;
- accelerating-affine NSE symmetry residual: `1.479e-16`;
- accelerating-affine specific-stretching residual: `8.739e-17`;
- accelerating-affine positive-renewal residual: `1.860e-16`;
- accelerating-affine Riccati residual: `5.551e-16`;
- `M(T-t)^2` residual: `1.472e-16`;
- accelerating renewal signal: `9.918667e-01`;
- PASS.

The accelerating affine calibration remains explicitly nonperiodic/infinite-energy and is not a regularity counterexample.

**Label: ACTION STRESS TEST.**
