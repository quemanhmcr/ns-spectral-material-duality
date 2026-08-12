# Common stochastic Cauchy deformation is phase-neutral; only relative replicas can deform the cubic interaction

Status: **Exact incompressible exterior-algebra identity, specialized to the literal stochastic Cauchy deformation.**

The Kelvin upstream now identifies the stochastic Cauchy deformation Gram with the packet material metric on each replica:

\[
\partial_\sigma D=D(\nabla u)^T,
\qquad
\det D=1.
\]

The metric may become highly anisotropic.  The question here is different: can that same common deformation rotate the complex cubic interaction phase?

---

## 1. One common replica preserves the full complex triple product

Let `z_0,z_1,z_2 in C^3` and let one real deformation matrix `D in SL(3,R)` act on all three legs.  Because `D` is real,

\[
\overline{Dz_0}=D\overline{z_0}.
\]

The scalar triple product transforms by the determinant:

\[
\overline{Dz_0}\cdot(Dz_1\times Dz_2)
=
(\det D)
\overline{z_0}\cdot(z_1\times z_2).
\]

For incompressible Cauchy deformation, `det D=1`, hence

\[
\boxed{
\overline{Dz_0}\cdot(Dz_1\times Dz_2)
=
\overline{z_0}\cdot(z_1\times z_2).
}
\]

Both amplitude and phase are unchanged.

**Classification: EXACT NSE/CAUCHY / LAMBDA^3 IDENTITY.**

This remains true even when `DD^T` has severe stretching.  Metric anisotropy and cubic phase rotation are therefore different physical effects.

---

## 2. Generator form: common trace-free deformation cancels exactly

For a real matrix `G`,

\[
(Ga)\cdot(b\times c)
+a\cdot((Gb)\times c)
+a\cdot(b\times(Gc))
=(\operatorname{tr}G)a\cdot(b\times c).
\]

Thus if three complex legs obey the same real generator,

\[
\dot z_i=Gz_i,
\]

then

\[
\boxed{
\dot{\mathcal Z}=(\operatorname{tr}G)\mathcal Z.
}
\]

For incompressible common deformation, `tr G=0`, so `Zdot=0`.

For the Cauchy matrix equation `Ddot=D A^T`, each transported vector `z=Dw` obeys

\[
\dot z=G_Dz,
\qquad
G_D=DA^TD^{-1},
\]

and

\[
\operatorname{tr}G_D=\operatorname{tr}A=\nabla\cdot u=0.
\]

**Classification: EXACT RELATIVE-GENERATOR FORM OF THE CAUCHY CANCELLATION.**

---

## 3. Different replicas expose the true deformation owner

Let the three legs obey

\[
\dot z_i=G_i z_i+f_i,
\]

with real `G_i`.  Choose any real reference generator `G` and write

\[
R_i=G_i-G.
\]

For

\[
\mathcal Z=\overline{z_0}\cdot(z_1\times z_2),
\]

the exact derivative is

\[
\boxed{
\begin{aligned}
\dot{\mathcal Z}
={}&(\operatorname{tr}G)\mathcal Z\\
&+\overline{R_0z_0}\cdot(z_1\times z_2)
+\overline{z_0}\cdot((R_1z_1)\times z_2)
+\overline{z_0}\cdot(z_1\times(R_2z_2))\\
&+\overline{f_0}\cdot(z_1\times z_2)
+\overline{z_0}\cdot(f_1\times z_2)
+\overline{z_0}\cdot(z_1\times f_2).
\end{aligned}
}
\]

For an incompressible reference `tr G=0`, only **relative generators and forcing** change the cubic interaction.

**Classification: EXACT OWNER DECOMPOSITION.**

In the stochastic Cauchy setting, different replicas sample `grad u` along different random anchor paths.  The deformation matrices have no direct Brownian differential; randomness enters the cubic deformation owner through these different sampled velocity gradients and through the terminal/forcing legs.

---

## 4. What can and cannot rotate phase in the Kelvin bridge

On one active germ, two exact cancellations now coexist:

- the first-bad orientation lift `M_fb tensor I_3` is orientation-blind and creates no continuous internal orientation phase;
- one common incompressible Cauchy deformation is an `SL(3)` action and creates no cubic phase rotation.

Therefore continuous phase rotation cannot be charged to either mechanism by itself.

It must enter through one of the genuinely relative/nonconservative owners:

- different physical/current realizations of the three legs;
- different stochastic replicas or different sampled velocity gradients;
- moving quantile/shell or state-map/clock interface mismatch;
- viscosity or other PDE forcing;
- a finite reset/reselection event, which is a typed jump rather than a smooth phase density.

**Classification: RIGOROUS CONSEQUENCE.**

---

## 5. Covariance and q.v. remain non-equivalent to cubic phase

The common-replica identity is pathwise and third-order/oriented.  The Kelvin covariance and q.v. ledgers are second-order.  Averaging `DD^T` or forming centered covariance cannot reconstruct the phase of the complex triple product.

Moreover, a common replica can have large finite-variation metric stretching while the cubic phase remains exactly fixed.  Thus

\[
\boxed{
\text{Cauchy metric growth or q.v. growth}
\not\Rightarrow
\text{interaction-phase rotation}.
}
\]

**Classification: COUNTEREXAMPLE/NO-GO.**

---

## 6. Remaining literal Kelvin bridge

The theorem is deliberately conditional on the three legs sharing a specified replica/common deformation.  The upstream programme has not yet identified its deterministic/hysteretic selected first-bad packet with one stochastic replica or a replica coupling.

Hence the remaining open question is now sharper:

> construct the selected-support/replica coupling and state-map/clock intertwining, then measure only the resulting **relative-replica** generator and interface residuals.

No recurrence, restart termination, or regularity claim is made.
