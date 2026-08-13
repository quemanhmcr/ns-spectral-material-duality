# Enstrophy level-set owner flux and endogenous Kelvin moving readout

Status: **EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE + ACTION STRESS TEST + OPEN BRIDGE**.

This batch composes three already-certified facts:

1. HS--HZ: actual enstrophy-record growth has the intrinsic local owner `R=omega.S.omega-nu|grad omega|^2+nu Delta e` evaluated on the field-generated active set;
2. HK--HR: any moving boundary enters physical balances only through its velocity relative to the material;
3. current read-only Kelvin `2227e1a9d3fbe48de591cfee2d4d09fe09b4f1bf`, Action `31686276216` success: a Kelvin ancestry population observed through a supplied Eulerian moving localization obeys signed Reynolds mean/covariance revaluation, with no extra selector covariance producer.

The remaining question is whether Navier--Stokes itself can supply such a moving localization rather than importing a threshold oracle.  Regular enstrophy level sets do exactly that once a level rule `lambda(t)` is specified.

No upstream write is made.

---

## 1. Exact relative velocity of an enstrophy level boundary

Let

\[
e=\frac12|\omega|^2,
\qquad
R=(\partial_t+u\cdot\nabla)e
=\omega\cdot S\omega-\nu|\nabla\omega|^2+\nu\Delta e.
\]

For a differentiable level rule `lambda(t)`, define the superlevel region

\[
\Omega_\lambda(t)=\{x:e(x,t)>\lambda(t)\}.
\]

At a regular boundary point `grad e!=0`, let `n` be the **outward** normal of the high-enstrophy region.  Then

\[
n=-\frac{\nabla e}{|\nabla e|}.
\]

If the boundary point moves with velocity `V`, differentiating the exact level constraint `e=lambda` gives

\[
\partial_t e+V\cdot\nabla e=\dot\lambda.
\]

Subtracting the material velocity and using the local enstrophy PDE yields

\[
\boxed{
(V-u)\cdot n
=\frac{R-\dot\lambda}{|\nabla e|}.}
\]

Thus the moving readout speed is not a new mechanism.  It is the local physical enstrophy owner rate minus the chosen motion of the value threshold, divided by the actual level-set gradient.

For a fixed physical level, `dot lambda=0` and

\[
\boxed{(V-u)\cdot n=R/|\nabla e|.}
\]

**Label: EXACT NSE/PDE IDENTITY.**

---

## 2. Superlevel volume is an exact owner-flux observable

Incompressibility gives

\[
\int_{\partial\Omega_\lambda}u\cdot n\,dS=0.
\]

Reynolds transport therefore implies

\[
\boxed{
\frac d{dt}|\Omega_\lambda(t)|
=\int_{\partial\Omega_\lambda(t)}
\frac{R-\dot\lambda}{|\nabla e|}\,dS.}
\]

For fixed regular `lambda`,

\[
\boxed{
\partial_t V(\lambda,t)
=\int_{e=\lambda}\frac{R}{|\nabla e|}\,dS,
\qquad
V(\lambda,t)=|\{e>\lambda\}|.}
\]

Positive or negative motion of a superlevel population is therefore a literal flux of the same local owner field that controls the enstrophy value.  The geometry and the owner are coupled by the denominator `|grad e|`; neither is an independently assigned event clock.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 3. Moving superlevel enstrophy has an exact owner/readout ledger

Apply the HK--HL moving-domain law to the superlevel region.  Since `e=lambda` on the boundary and

\[
\nabla e\cdot n=-|\nabla e|,
\]

one obtains

\[
\boxed{
\begin{aligned}
\frac d{dt}\int_{\Omega_\lambda}e
={}&\int_{\Omega_\lambda}\omega\cdot S\omega
-\nu\int_{\Omega_\lambda}|\nabla\omega|^2\\
&-\nu\int_{\partial\Omega_\lambda}|\nabla e|\,dS
+\lambda\int_{\partial\Omega_\lambda}
\frac{R-\dot\lambda}{|\nabla e|}\,dS.
\end{aligned}}
\]

The four faces are now intrinsic:

- local stretching owner inside the selected physical region;
- bulk viscous loss;
- diffusive flux down the enstrophy gradient;
- signed value-threshold/moving-readout revaluation.

The last face is physical transfer across the moving level boundary, not fresh stretching generation.

**Label: EXACT NSE/PDE IDENTITY.**

---

## 4. Coarea turns all local level-set owner fluxes into the global enstrophy law

Because `e>=0`, layer cake gives

\[
\boxed{
\int e(x,t)\,dx
=\int_0^\infty V(\lambda,t)\,d\lambda.}
\]

For almost every regular level, Section 2 gives the fixed-level derivative.  Coarea then yields

\[
\boxed{
\int_0^\infty
\int_{e=\lambda}
\frac{R}{|\nabla e|}\,dS\,d\lambda
=\int R\,dx.}
\]

On the periodic domain the curvature flux integrates to zero, so

\[
\boxed{
\frac d{dt}\int e\,dx
=\int\omega\cdot S\omega\,dx
-\nu\int|\nabla\omega|^2\,dx.}
\]

Therefore the global enstrophy ledger is literally the layer-cake integral of the local level-set crossing owner flux.

This is an exact local-to-global bridge, not an estimate.

**Label: EXACT NSE/PDE IDENTITY + RIGOROUS CONSEQUENCE.**

---

## 5. Exact bridge to the global spectral split/merge owner

Repo-3 Theorems BR--BT already give, in their certified helical donor notation,

\[
\frac12Y'+\nu Z
=\mathcal V_{\rm split}-\mathcal V_{\rm merge},
\]

where `Y/2` is the global enstrophy, `Z` is the global viscous enstrophy Dirichlet quantity, one-donor split variance is the only positive nonlinear global owner, and merge variance is the nonlinear sink.

Combining that exact global theorem with the coarea identity gives

\[
\boxed{
\int_0^\infty
\int_{e=\lambda}
\frac{R}{|\nabla e|}\,dS\,d\lambda
=
\mathcal V_{\rm split}
-\mathcal V_{\rm merge}
-\nu Z.}
\]

This is the first direct repo-3 bridge from the **physical local level-set owner flux** to the **global spectral donor split/merge ledger**.

It does **not** assign an individual spectral split or merge to a particular level surface.  Such a levelwise localization would require a new theorem.  What is closed here is the exact all-level integral.

**Label: RIGOROUS CONSEQUENCE from two exact certified identities.**

---

## 6. Moving value thresholds are signed readout revaluation, not a new source

The level rule enters only through

\[
-\dot\lambda\int_{e=\lambda}\frac{1}{|\nabla e|}\,dS.
\]

Changing `lambda(t)` changes which physical ancestry/space population is selected.  It does not change the underlying local owner field `R`.

Thus

\[
\boxed{
\text{PDE owner }R
\quad\neq\quad
\text{value-threshold motion }\dot\lambda.}
\]

The latter is a signed finite-variation readout currency, directly analogous in type -- but not numerically identified -- with Kelvin's new moving-population boundary revaluation.

A future first-bad construction must derive its level rule from an actual obstruction/observable.  Merely choosing a convenient moving percentile or threshold would still be an external readout choice.

**Label: RIGOROUS CONSEQUENCE + OPEN BRIDGE.**

---

## 7. Exact periodic heat shear: fixed-level chamber speed is the owner flux

Take

\[
u=(A e^{-\nu k^2t}\sin ky,0,0),
\]

so

\[
e(y,t)=M(t)\cos^2(ky),
\qquad
M(t)=\frac12A^2k^2e^{-2\nu k^2t}.
\]

Fix `0<L<M(t)` and consider the chamber around `y=0` with boundary `y=+-a(t)`,

\[
\cos^2(ka)=\frac{L}{M(t)}.
\]

Put

\[
r=\sqrt{L/M}.
\]

Then

\[
\boxed{
\dot a=-\nu k\frac{r}{\sqrt{1-r^2}}.}
\]

At the boundary,

\[
R=-2\nu k^2L,
\qquad
|e_y|=2Mk r\sqrt{1-r^2},
\]

so exactly

\[
\boxed{
\dot a=\frac{R}{|e_y|}.}
\]

The material normal velocity is zero in this shear, hence the shrinking chamber is literally the owner-driven relative level-set motion.

**Label: EXACT NSE/PDE IDENTITY + ACTION STRESS TEST calibration.**

---

## 8. A co-decaying fractional level can have zero boundary motion

Now choose

\[
\lambda(t)=\theta M(t),
\qquad 0<\theta<1.
\]

Then the level equation is

\[
\cos^2(ka)=\theta,
\]

so the chamber boundary is stationary.

On that boundary,

\[
R=-2\nu k^2\lambda,
\qquad
\dot\lambda=-2\nu k^2\lambda.
\]

Therefore

\[
\boxed{
R-\dot\lambda=0,
\qquad
(V-u)\cdot n=0.}
\]

The field is still decaying physically.  What vanishes is only the motion of this co-decaying readout boundary.

This is an exact no-go against interpreting absence of selector/boundary motion as absence of PDE evolution, or interpreting boundary motion itself as generation.

**Label: EXACT NSE/PDE IDENTITY + COUNTEREXAMPLE/NO-GO.**

---

## 9. Kelvin ancestry moving readout now has a PDE-generated candidate localization

Current Kelvin `2227e1a` proves that, once an Eulerian localization is supplied on a reduced physical ancestry coordinate, the selected mean/covariance evolves by a **signed total ancestry-mass boundary flux**; it does not create a fourth selector covariance source.

To compose this correctly with an NSE level set, do not erase the intrinsic ancestry current.  Suppose an ancestry density on the same observation clock satisfies

\[
\partial_t\rho+\nabla\cdot J_\rho=0.
\]

For a moving selected region with outward normal `n`, Reynolds transport gives the signed selected-mass gain density

\[
\boxed{
\lambda_{\partial}
=(\rho V-J_\rho)\cdot n.}
\]

Using the exact enstrophy level-set law,

\[
V\cdot n
=u\cdot n+\frac{R-\dot\lambda}{|\nabla e|},
\]

so

\[
\boxed{
\lambda_{\partial}
=
\rho\,\frac{R-\dot\lambda}{|\nabla e|}
+
(\rho u-J_\rho)\cdot n.}
\]

This is the correct two-face composition:

- `rho (R-dot lambda)/|grad e|` is the **Eulerian level-set sweep** generated by the NSE observable;
- `(rho u-J_rho).n` is the **intrinsic ancestry-current mismatch** relative to deterministic material transport.

For a deterministic material population `J_rho=rho u`, the second face vanishes.  In Kelvin's exact two-mode heat-shear calibration the relevant `y` marginal is uniform and stationary, with zero `y` drift and zero diffusive probability current; the fluid also has zero `y` velocity.  Hence on that calibrated normal coordinate the total signed boundary flux reduces exactly to

\[
\boxed{
\lambda_{\partial}
=\rho\,\frac{R-\dot\lambda}{|\nabla e|}.}
\]

That calibrated flux can be inserted directly into Kelvin's exact moving selected-mean/covariance revaluation formulas.  In general, however, the intrinsic Fokker--Planck/current face must be retained.

Thus the safe composition is

\[
\boxed{
\text{local NSE owner}
\to
\text{enstrophy level-set sweep}
\oplus
\text{intrinsic ancestry current}
\to
\text{total ancestry boundary flux}
\to
\text{Kelvin signed moving-readout revaluation}.}
\]

No independent selector covariance producer appears, and no ancestry-current face is silently discarded.

The remaining clock caveat is essential: Kelvin's literal stochastic construction is naturally written in its ancestry/reverse-age clock.  A general identification with the physical-time level-set clock still requires an explicit clock/lift theorem.  The exact stationary shear calibration avoids that ambiguity on the audited normal marginal, but does not solve the general two-clock seam.

What also remains open is which level rule/localization is the actual programme first-bad obstruction.  The record theorem supplies an intrinsic scalar owner clock; the present theorem supplies a PDE-generated family of localization geometries once a level rule is fixed; a future theorem must select the physically forced member and handle critical levels/topology changes.

**Label: RIGOROUS CROSS-PROGRAM CONSEQUENCE + OPEN BRIDGE.**
