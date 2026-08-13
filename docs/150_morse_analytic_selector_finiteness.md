# Analytic-Morse selector finiteness and transverse-support separation

Status: **RIGOROUS CONSEQUENCE + EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO + ACTION STRESS TEST + OPEN BRIDGE**.

This batch attacks the remaining untyped `support-edge theorem-domain exit` from the running-record renewal trichotomy.  It separates two questions that must not be conflated:

1. can the scalar enstrophy support edge switch winners infinitely often while every critical branch remains nondegenerate?;
2. does scalar critical/chamber localization force the full physical Kelvin/Nanson packet support to localize?

The first answer is **no on every compact positive-time analytic Morse interval**.  The second answer is **no**, by current read-only Kelvin `1095c1353d42b67b9d0905e913ff494601770f1f`, Action `31710776956` success.

The only external analytic input used below is the standard positive-time analyticity of classical Navier--Stokes solutions.  For periodic/Gevrey formulations see Foias--Temam, *J. Funct. Anal.* 87 (1989), 359--369, DOI `10.1016/0022-1236(89)90015-3`; for classical time/space analyticity see Giga, *Comm. PDE* 8 (1983), 929--948, DOI `10.1080/03605308308820290`.  The new statements below are finite-dimensional consequences once this intrinsic parabolic regularity is available.

No continuation/global-regularity theorem is claimed.

---

## 1. Positive-time classical NS supplies an analytic enstrophy critical equation

Let `I=[t0,t1]` be a compact interval strictly inside a classical periodic Navier--Stokes lifespan, with `t0>0`.  Standard parabolic analyticity gives a real-analytic representative of `u`, hence of

\[
e=\frac12|\omega|^2
\]

and

\[
F(x,t)=\nabla e(x,t)
\]

on a space-time neighborhood of `T^3 x I`.

This is not a new regularity criterion.  It is an intrinsic smoothing property of the same classical NSE being studied.

**Label: RIGOROUS CONSEQUENCE from standard positive-time NSE analyticity.**

---

## 2. Uniformly Morse enstrophy gives a finite analytic critical-lineage covering

Assume every enstrophy critical point on `T^3 x I` is nondegenerate:

\[
F(x,t)=0\quad\Longrightarrow\quad \det H_e(x,t)\ne0.
\]

Let

\[
\mathcal C=\{(x,t)\in T^3\times I:\nabla e(x,t)=0\}.
\]

Because `T^3 x I` is compact, `C` is compact.  At every point of `C`,

\[
D_xF=H_e
\]

is invertible.  The analytic implicit-function theorem therefore makes `C` a one-dimensional analytic submanifold, and the projection

\[
\pi:\mathcal C\to I,
\qquad (x,t)\mapsto t,
\]

is a local analytic diffeomorphism.  Since `C` is compact, `pi` is proper.  A proper local diffeomorphism over the interval is a finite covering.  Because an interval is simply connected,

\[
\boxed{
\mathcal C=\bigsqcup_{j=1}^{N}\{(x_j(t),t):t\in I\}
}
\]

for finitely many analytic critical lineages `x_j(t)`.

Along each lineage the exact critical-current law remains

\[
\boxed{\dot x_j-u=-H_{e,j}^{-1}\nabla R.}
\]

Thus the finite covering is not an externally imposed branch catalogue: its curves are the literal PDE critical currents.

**Label: RIGOROUS CONSEQUENCE + EXACT NSE/PDE IDENTITY.**

---

## 3. Critical branch values are analytic and crossings are finite modulo persistent ties

Define

\[
m_j(t)=e(x_j(t),t).
\]

Every `m_j` is real analytic and, since `grad e=0` on the branch,

\[
\boxed{m_j'(t)=R(x_j(t),t).}
\]

For any pair `i,j`, the difference

\[
h_{ij}=m_i-m_j
\]

is analytic on a neighborhood of `I`.  Therefore exactly one of two things happens:

1. `h_ij` is identically zero on the connected analytic domain: the two branches are a **persistent tie class**;
2. its zero set in `I` is finite.

Quotient the finite branch set by persistent ties.  Between the finitely many remaining pairwise equality times, the strict ordering of all quotient classes is fixed.

Hence the global enstrophy maximum

\[
M(t)=\max_j m_j(t)
\]

can change its maximizing tie class only finitely many times on `I`.

Persistent equality is not repeated switching and must not be converted into selector q.v.

**Label: RIGOROUS CONSEQUENCE.**

---

## 4. The endogenous scalar support-edge selector is locally finite in the Morse regime

Choose any deterministic right-continuous representative of the maximizing persistent-tie class.  By Section 3 it has only finitely many jumps on `I`.

For a one-hot representative `Y(t)`, every genuine class change has

\[
|\Delta Y|^2=2.
\]

If `N_I` is the number of support-edge class changes,

\[
\boxed{\operatorname{tr}\mathcal J_Y(I)=2N_I<\infty.}
\]

Thus scalar selector Zeno accumulation is impossible on a compact positive-time interval while the entire enstrophy critical set remains Morse.

This closes the old **scalar endogenous-selector local-finiteness seam** on the analytic Morse theorem domain.  It does not bound `N_I` uniformly across solutions or intervals.

**Label: RIGOROUS CONSEQUENCE.**

---

## 5. Interior scalar Zeno forces critical-geometry degeneracy

Take any compact `I` strictly inside a classical positive-time lifespan.  Suppose the support-edge maximizing class changes infinitely often with an accumulation point in `I`.

The standard positive-time analyticity input is already available on such an interval.  Therefore Section 4 can fail only if the Morse hypothesis fails.  Consequently there exists

\[
(x_*,t_*)\in T^3\times I
\]

with

\[
\boxed{\nabla e(x_*,t_*)=0,\qquad \det H_e(x_*,t_*)=0.}
\]

So an **interior** scalar winner-Zeno accumulation cannot hide inside a completely nondegenerate critical geometry.

This statement deliberately does not exclude accumulation at a candidate endpoint `T` of the classical lifespan, where no uniform positive-time analytic neighborhood beyond `T` is being assumed.

**Label: RIGOROUS CONSEQUENCE.**

---

## 6. There is no universal numerical bound on finite ranking complexity

The exact heat-shear family already certified in GY/HI realizes any prescribed finite number `N` of simple ranking crossings while both tracked sheets remain strict normal maxima on one compact interval and

\[
(u\cdot\nabla)u=0
\]

identically.

Therefore analytic-Morse local finiteness gives only

\[
\boxed{N_I<\infty,}
\]

not a universal bound `N_I<=C` independent of the solution.

This is essential: the theorem removes Zeno accumulation without replacing the PDE by an artificial event-count budget.

**Label: COUNTEREXAMPLE/NO-GO + RIGOROUS CONSEQUENCE.**

---

## 7. Exact periodic global-max crossing calibrates one isolated support-edge switch

Current read-only Kelvin `5067f87` supplies the exact four-mode heat shear whose two genuine global enstrophy maxima at `t_*=1/nu` satisfy

\[
M=18,
\qquad
e_{yy}(0)=-240,
\qquad
e_{yy}(\pi)=-336,
\]

with rates

\[
R_0=-240\nu,
\qquad
R_\pi=-336\nu.
\]

The branch gap is analytic and has a simple zero at the crossing; the right support-edge defect selects `y=0`, the left defect selects `y=pi`.  The switch is isolated, both critical points are nondegenerate, and nonlinear generation is absent in the shear.

This is the literal single-switch calibration of Sections 2--4.

**Label: EXACT NSE/PDE IDENTITY + ACTION STRESS TEST calibration.**

---

## 8. Persistent ties are a quotient class, not infinite selector activity

The one-mode heat shear has enstrophy

\[
e(y,t)=M(t)\cos^2 y.
\]

The two strict normal maxima `y=0,pi` have identical branch values for all time.  Their branch-value difference is the analytic function identically equal to zero.

Counting arbitrary alternation between these physically tied labels would create unbounded selector q.v. by convention alone.  The analytic theorem instead quotients them as one persistent tie class unless an independently specified physical readout distinguishes them.

**Label: EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO.**

---

## 9. Scalar selector finiteness does not imply full physical support localization

Current read-only Kelvin head `1095c1353d42b67b9d0905e913ff494601770f1f`, Action `31710776956` success, gives an exact smooth periodic one-mode shear with intrinsic chamber half-width `alpha/n` tending to zero.  For the physical packet

\[
L=\operatorname{diag}(1,2\alpha/n,1),
\qquad B=LL^T,
\]

and intrinsic level normal `n=e_y`, the tangent projector is

\[
P=I-n\otimes n.
\]

Then

\[
\boxed{B_\parallel=PBP=\operatorname{diag}(1,0,1)}
\]

for every `alpha`, even though

- chamber thickness tends to zero;
- packet volume tends to zero;
- the physical Kelvin residual tends to zero;
- local orientation q.v. and codeforming noise vanish;
- the normal ancestry flux vanishes.

Therefore

\[
\boxed{
\text{scalar critical/chamber localization}
\not\Rightarrow
\text{full physical packet-support localization}.}
\]

**Label: RIGOROUS CROSS-PROGRAM CONSEQUENCE + COUNTEREXAMPLE/NO-GO.**

---

## 10. `support-edge domain exit` must be split into typed geometry channels

The running-record trichotomy in JJ--JS used the phrase `support-edge theorem-domain exit`.  Sections 2--9 refine it.

On a compact positive-time classical interval:

1. **ranking/selector accumulation** is not an independent escape channel inside the Morse regime; infinite interior churn forces a degenerate critical point;
2. **Morse/normal degeneracy** is a genuine scalar critical-geometry channel;
3. **tangential physical support noncollapse** is a separate Kelvin/Nanson packet-geometry channel and is not detected by scalar chamber collapse;
4. **transport ancestry/frame holonomy** remains separate again, as already forced by the exact merger.

Thus future recurrence/first-bad logic must use a typed geometry state rather than an unstructured `domain exit` flag.

The remaining endpoint problem is now sharper: near a hypothetical finite singular endpoint, control or classify

\[
\boxed{
\text{positive core renewal}
\;|\;
\text{positive geometry harvesting}
\;|\;
\text{Morse/normal degeneration}
\;|\;
\text{transverse support noncollapse/ancestry}.}
\]

No termination, restart, continuation, or global-regularity theorem is claimed.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

**JT–KC ACTION CERTIFICATE.** GitHub Actions `31712624893` on theorem SHA `6f348be1732dbd13d1f37e483286f6aed4cd880f` completed successfully. Exp100: four-mode common-max residual `0`, branch-rate `7.957e-17`, support-defect `1.973e-16`, analytic gap-rate residual `1.430e-11`; persistent one-mode tie gap `0`; four prescribed Morse crossings with interpolation `2.332e-16`, minimum simple-root signal `4.233e-02`, largest normal curvature `-2.781531`, sign-fail count `0`; Kelvin transverse-support residual `0`, chamber volume `3.478261e-02 -> 8.695652e-07`, physical residual `1.133534e+01 -> 7.141526e-09`, tangential-support signal `1`, q.v./codeforming `0/0`; PASS. No endpoint-Zeno, termination, continuation, or global-regularity claim.
