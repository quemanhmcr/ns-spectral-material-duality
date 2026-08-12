# Reduced ancestry carries a hard physical selector iff its resolution kernel is selector-pure

Status: **Exact conditional-kernel identity and exact pair-disagreement criterion.**

This note updates the deterministic state-map branch of the Kelvin bridge after reading the literal upstream full/reduced-state audit at `ns-pde-first-kelvin-frontier` HEAD `2745fa2c979bbcc1c850dd57743e60881a3b565e`.  The general reduced-to-full bridge is not a map `Pi`; it is a conditional Markov kernel

\[
\kappa_t(y,dY),
\]

from a reduced ancestry state `y` to a full physical Kelvin current-shape state `Y`.

No upstream file is changed here.  No restart, recurrence, or regularity claim is made.

---

## 1. The exact lift operator

For every full physical observable `F(Y)`, define

\[
\boxed{
(R_tF)(y)=\int F(Y)\,\kappa_t(y,dY).
}
\]

If `L_y` and `L_Y` are the reduced and full backward-observable generators, the exact intertwining defect is the operator

\[
\boxed{
\mathcal D_R
:=\partial_tR_t+L_yR_t-R_tL_Y.
}
\]

Thus for every physical observable

\[
\boxed{
(\partial_t+L_y)(R_tF)
=R_t(\partial_t+L_Y)F+\mathcal D_RF.
}
\]

When `D_R=0`, reduced transport is exactly the conditional image of full physical transport.  When it is nonzero, it is a named state-resolution / generator-intertwining owner; it must not be hidden inside viscosity, interface work, or a generic norm defect.

**Classification: EXACT KERNEL/PDE IDENTITY.**

The deterministic theorem `Pi:Y_red -> Y_full` is the Dirac special case `kappa_y=delta_{Pi(y)}`.  For first-order transport it reduces to the previously derived `grad F(Pi) . R_Pi`.  For a genuine diffusion, the kernel formulation is safer because deterministic Itô pushforward also has a diffusion-tensor residual and Hessian drift correction.

---

## 2. A physical hard selector becomes a conditional occupancy

Let `A_t` be a physical selected set in the full Kelvin state and let

\[
\chi_A(Y)\in\{0,1\}
\]

be its hard indicator.  The reduced ancestry state sees only

\[
\boxed{
\alpha(y):=(R\chi_A)(y)=\kappa_y(A)\in[0,1].
}
\]

Unless the kernel resolves the interface, the reduced object is not a hard selector.  It is the conditional probability that the hidden full physical state lies in the selected set.

The exact conditional selector variance is

\[
\boxed{
V_A(y)
:=R(\chi_A^2)-(R\chi_A)^2
=\alpha(y)(1-\alpha(y)).
}
\]

Since `chi_A^2=chi_A`, no approximation enters.

**Physical classification:** unresolved physical-side membership inside one reduced ancestry label.

**Classification: EXACT CONDITIONAL-RESOLUTION IDENTITY.**

---

## 3. Hard selector descent iff the kernel is selector-pure

A hard reduced selector `chi_red(y)` satisfying

\[
\chi_A(Y)=\chi_{red}(y)
\quad\text{for }\kappa_y\text{-almost every }Y
\]

exists exactly when

\[
\boxed{V_A(y)=0.}
\]

Indeed `V_A=alpha(1-alpha)=0` iff `alpha` is `0` or `1`, which is equivalent to `chi_A` being constant `kappa_y`-almost surely.

Equivalently, the support of `kappa_y` lies entirely inside `A` or entirely inside its complement.

\[
\boxed{
\text{hard selector descent}
\Longleftrightarrow
\text{kernel selector purity}.
}
\]

This is the conditional-kernel generalization of the earlier deterministic fiber criterion.

**Classification: EXACT NECESSARY-AND-SUFFICIENT DESCENT CRITERION.**

---

## 4. The existing same-ancestor pair process detects selector impurity exactly

Draw two independent full states from the same reduced ancestor,

\[
Y_1,Y_2\sim\kappa_y
\quad\text{independently conditional on }y.
\]

Then

\[
\boxed{
\frac12\mathbb E_y
[\chi_A(Y_1)-\chi_A(Y_2)]^2
=\alpha(1-\alpha)
=V_A(y).
}
\]

Thus the Kelvin programme's existing same-ancestor two-replica variance object already contains an exact **selector-resolution diagnostic**.  No new probability law is needed.

The interpretation is rigid:

- zero pair disagreement: the reduced ancestor resolves which physical side is selected;
- positive pair disagreement: the same reduced ancestor hides physical states on both sides of the cut.

This pair disagreement is a state-resolution face.  It may exist even when the full physical diffusion has no local viscous q.v. at the reduction face, exactly as in the upstream resolution-covariance audit.

**Classification: EXACT PAIR IDENTITY / PHYSICAL TYPING.**

---

## 5. Selection and phase can correlate inside an unresolved fiber

Let `Z(Y)` be any full-state complex interaction observable, in particular a physical oriented material cubic when that observable has been literally constructed on `Y`.  The selected reduced interaction is

\[
Z_A^{same}(y)=R(\chi_A Z).
\]

It differs from multiplying average occupancy by average interaction:

\[
\boxed{
R(\chi_A Z)
=\alpha\,RZ
+\operatorname{Cov}_{\kappa_y}(\chi_A,Z),
}
\]

where the second term is the exact complex conditional selection/interaction correlation.

If `V_A=0`, then `chi_A` is constant on the kernel support and this correlation vanishes exactly.  If `V_A>0`, replacing `R(chi_A Z)` by `alpha RZ` silently discards physical hidden-state selection information.

**Classification: EXACT CONDITIONAL IDENTITY / COUNTEREXAMPLE-NO-GO against multiplying a soft occupancy by an unconditioned phase statistic.**

---

## 6. Relation to deterministic state-map/clock theorem

The earlier theorem with

\[
R_\Pi=\partial_t\Pi+D\Pi\,b_y-b_Y\circ\Pi
\]

is retained as the first-order Dirac-kernel branch.  It is not the general Kelvin bridge.

For a deterministic Itô map with diffusion tensors `a_y,a_Y`, composition gives two exact residuals:

\[
\boxed{
A_\Pi
=D\Pi\,a_yD\Pi^T-a_Y\circ\Pi,
}
\]

and

\[
\boxed{
B_\Pi
=\partial_t\Pi+D\Pi b_y+\frac12a_y:D^2\Pi-b_Y\circ\Pi.
}
\]

The observable defect is

\[
\boxed{
\mathcal D_R F
=B_\Pi\cdot\nabla F
+\frac12A_\Pi:\nabla^2F.
}
\]

Only after diffusion compatibility `A_Pi=0` does a hard-interface mismatch reduce to the normal drift face discussed previously.  This is important for the literal Kelvin future-bank state map, whose physical shape q.v. is degenerate.

**Classification: EXACT ITÔ COMPOSITION IDENTITY.**

---

## 7. New bridge status

The selected-support/Cauchy-replica problem is now more precise.

One does not need to ask vaguely whether a deterministic first-bad packet "is a stochastic replica."  The programme must instead specify whether its ancestry state is full or reduced.  In the reduced branch it must provide `kappa(y,dY)` and then answer two exact questions:

1. **selector purity:** is `V_A=0` for the physical selected set?
2. **generator compatibility:** is `D_R=0` on the observables used by the selected interaction?

Only after those pass may a reduced ancestry selector be called a hard physical selector.

**Classification: OPEN LITERAL KERNEL CONSTRUCTION; exact acceptance tests supplied here.**
