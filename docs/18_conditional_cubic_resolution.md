# Physical same-state cubic phase is not the cubic of independent ancestry replicas

Status: **Exact conditional third-order resolution identity and second-order no-go.**

The Kelvin covariance architecture is naturally two-replica because variance is second order.  The Navier--Stokes interaction phase carried by the material 3-form is third order.  This note keeps those facts distinct and asks what a reduced ancestry kernel actually does to the cubic observable.

No global estimate or continuation statement is used.

---

## 1. Full-state cubic and reduced conditional means

Let `kappa_y(dY)` be a conditional lift from one reduced ancestry state to full physical Kelvin states.  Let three complex vector observables on the **same** full state be

\[
\Phi_i(Y)\in\mathbb C^3,
\qquad i=0,1,2.
\]

Define the oriented trilinear form

\[
\mathcal T(z_0,z_1,z_2)
:=\overline{z_0}\cdot(z_1\times z_2).
\]

The physically same-hidden-state conditional cubic is

\[
\boxed{
\overline{\mathcal Z}(y)
:=R\,\mathcal T(\Phi_0,\Phi_1,\Phi_2).
}
\]

The conditional mean legs are

\[
m_i=R\Phi_i.
\]

Their cubic is

\[
\boxed{
\mathcal Z_{ind}(y):=\mathcal T(m_0,m_1,m_2).
}
\]

The subscript `ind` is literal: if `Y_0,Y_1,Y_2` are conditionally independent samples from `kappa_y`, multilinearity gives

\[
\boxed{
\mathbb E_y\mathcal T(\Phi_0(Y_0),\Phi_1(Y_1),\Phi_2(Y_2))
=\mathcal T(m_0,m_1,m_2).
}
\]

Thus independent replicas compute the cubic of conditional means, not the physical same-state cubic in general.

**Classification: EXACT CONDITIONAL-REPLICA IDENTITY.**

---

## 2. Exact cubic resolution decomposition

Write

\[
\xi_i(Y)=\Phi_i(Y)-m_i,
\qquad R\xi_i=0.
\]

Expanding the trilinear form and eliminating all one-centered-leg terms gives

\[
\boxed{
\begin{aligned}
\overline{\mathcal Z}
={}&\mathcal T(m_0,m_1,m_2)\\
&+R\mathcal T(\xi_0,\xi_1,m_2)\\
&+R\mathcal T(\xi_0,m_1,\xi_2)\\
&+R\mathcal T(m_0,\xi_1,\xi_2)\\
&+R\mathcal T(\xi_0,\xi_1,\xi_2).
\end{aligned}
}
\]

Define

\[
\boxed{
\Delta_3^{res}
:=\overline{\mathcal Z}-\mathcal Z_{ind}.
}
\]

Then `Delta_3^res` is exactly the sum of three pair-resolution contractions and one centered third-order oriented moment.

**Physical classification:** hidden-state relative orientation/phase content discarded when one replaces a full physical state by independent conditional replicas or by conditional mean legs.

**Classification: EXACT THIRD-ORDER RESOLUTION IDENTITY.**

---

## 3. A second-order bank cannot determine the missing signed cubic

The centered third-order term is genuinely independent of first and second moments.

Choose four hidden states with equal weights and signs

\[
(s_0,s_1,s_2)
\in
\{(+,+,+),(+,-,-),(-,+,-),(-,-,+)\}.
\]

For fixed nondegenerate complex vectors `z_i`, set

\[
\Phi_i=s_i z_i.
\]

Then

\[
R\Phi_i=0,
\qquad
R(s_is_j)=0\quad(i\ne j),
\]

while every state has

\[
s_0s_1s_2=+1.
\]

Hence all one-leg means vanish, all pair sign correlations vanish, and all one-leg quadratic moments are fixed, but

\[
\boxed{
\overline{\mathcal Z}=\mathcal T(z_0,z_1,z_2)\ne0,
\qquad
\mathcal Z_{ind}=0.
}
\]

Now replace the kernel by the four odd-parity sign states.  The first and second moments are unchanged, but

\[
\boxed{
\overline{\mathcal Z}=-\mathcal T(z_0,z_1,z_2).
}
\]

Thus two reduced-state ensembles can have identical first- and second-order data and opposite signed cubic work/phase.

\[
\boxed{
\text{means + covariance/q.v.}
\not\Rightarrow
\text{signed cubic phase}.
}
\]

**Classification: COUNTEREXAMPLE/NO-GO.**

This sharpens the earlier statement that covariance is second order.  The missing datum can be a pure conditional third-order parity/orientation correlation even when all pair correlations vanish.

---

## 4. Same-replica Cauchy cancellation survives inside each hidden state

Suppose one real incompressible Cauchy deformation `D(Y)` acts commonly on all three legs of each hidden full state.  Replica by replica,

\[
\mathcal T(D\Phi_0,D\Phi_1,D\Phi_2)
=\det D\,\mathcal T(\Phi_0,\Phi_1,\Phi_2)
=\mathcal T(\Phi_0,\Phi_1,\Phi_2).
\]

Averaging over `kappa_y` therefore gives

\[
R\mathcal T(D\Phi_0,D\Phi_1,D\Phi_2)
=\overline{\mathcal Z}.
\]

So conditional reduction does not turn common incompressible deformation into a phase source.  What may change under reduction is the hidden-state mixture, relative generator, selector correlation, or explicit forcing.

**Classification: EXACT CONSEQUENCE of common-replica `SL(3)` invariance.**

---

## 5. What replica coupling a physical phase theorem actually needs

There are three different objects:

1. **same full state:** `R T(Phi_0(Y),Phi_1(Y),Phi_2(Y))`;
2. **independent conditional replicas:** `T(RPhi_0,RPhi_1,RPhi_2)`;
3. **two-replica covariance bank:** second-order pair differences.

Only the first is automatically the conditional image of a physical cubic interaction defined on the full state.  The second and third can support useful diagnostics but do not equal the first without an additional theorem forcing `Delta_3^res=0` or explicitly carrying it.

Therefore the selected-support/replica bridge has a precise third-order requirement:

\[
\boxed{
\text{either preserve the same-hidden-state coupling,
 or carry }\Delta_3^{res}\text{ as a named physical resolution object.}
}
\]

**Classification: RIGOROUS STRUCTURAL CONSEQUENCE.**

---

## 6. Consequence for the programme frontier

A future Kelvin phase bridge cannot be closed by proving only a bound on `R_s=E[DD^T]`, centered covariance, or the same-ancestor two-replica bank.  Those are second-order geometries.

The literal third-order question is now:

> does the ancestry/full-state kernel become phase-sufficient on the selected set, or what exact law transports `Delta_3^res`?

The next note derives that transport law directly from the generator product rule.
