# Diagonal marginals erase relative coupling: Wang coherent phase versus Kelvin common-driver orientation

Status: **EXACT REPRESENTATION IDENTITY / RIGOROUS CONSEQUENCE / COUNTEREXAMPLE-NO-GO**, downstream of the physically typed linear synthesis and same-replica q.v. laws.

The result below does **not** identify a Wang coherent phase with a Kelvin Brownian
orientation.  Those are different physical objects.  The common statement is only
the representation law governing quadratic block data after the physical objects
have already been typed.

Current upstream snapshots are used read-only:

- Wang `3c3ee1ee74c464bdf1c4501aa52b2c853f1fea6c`;
- Kelvin `119b6e3769a45c04a4b0620c837c32f86b7e86c3`.

---

## 1. The block-Gram law

Let `B_i` be linear maps from one latent inner-product space `H` into physical
fibers `V_i`.  Over `R` use transpose; over `C` use Hermitian adjoint.  The full
quadratic block state is

\[
\boxed{G_{ij}=B_iB_j^*.}
\]

Its diagonal marginals are

\[
D_i=G_{ii}=B_iB_i^*.
\]

Now choose latent isometries `U_i` and replace

\[
B_i\mapsto B_iU_i.
\]

Every diagonal block is exactly unchanged:

\[
\boxed{B_iU_i(B_iU_i)^*=B_iB_i^*.}
\]

But the cross block becomes

\[
\boxed{
G_{ij}\mapsto
B_iU_iU_j^*B_j^*.}
\]

Hence diagonal marginals cannot determine the relative latent alignment
`U_iU_j^*`.

By contrast, a **common** latent change `U_i=U` for every block gives

\[
B_iUU^*B_j^*=B_iB_j^*
\]

for every ordered pair.  Thus the full Gram is invariant under a common latent
basis change, whereas the diagonal projection is invariant under the much larger
product family of independent blockwise basis changes.

This is the precise information loss:

\[
\boxed{
\text{diagonalization enlarges the invariance}
\Longrightarrow
\text{relative coupling is quotiented out}.}
\]

No norm or estimate is involved.

**Label: EXACT REPRESENTATION IDENTITY / COUNTEREXAMPLE-NO-GO.**

---

## 2. Why the lost datum matters for physical synthesis

Stack the blocks and let a specified linear physical synthesis/event be `A`.  The
full quadratic state is pushed by

\[
G\mapsto AGA^*.
\]

Because `AGA^*` contains all ordered cross blocks, two full Gram states with the
same diagonal marginals can produce different synthesized outputs.

For two equal block fibers and sum synthesis

\[
A=[I\ I],
\]

one reads

\[
\boxed{
AGA^*=G_{11}+G_{12}+G_{21}+G_{22}.}
\]

The diagonal data alone supplies only the first and last terms.  Relative coupling
is therefore state data for synthesis, not decorative bookkeeping.

**Label: RIGOROUS CONSEQUENCE.**

---

## 3. Wang specialization: relative coherent phase is invisible to diagonal child pairs

Take complex coherent child fields/fibers `f_\alpha`.  Their ordered pair state is

\[
C_{\alpha\beta}=f_\alpha f_\beta^*.
\]

The additive coherent synthesis is

\[
f=\sum_\alpha f_\alpha,
\qquad
ff^*=\sum_{\alpha,\beta}C_{\alpha\beta}.
\]

Under independent child phase changes

\[
f_\alpha\mapsto e^{i\theta_\alpha}f_\alpha,
\]

each diagonal child pair is unchanged:

\[
C_{\alpha\alpha}\mapsto C_{\alpha\alpha},
\]

while

\[
\boxed{
C_{\alpha\beta}\mapsto
 e^{i(\theta_\alpha-\theta_\beta)}C_{\alpha\beta}.}
\]

A common phase `\theta_\alpha=\theta` leaves the entire quadratic pair state
unchanged.  Relative phases do not.

For the quadratic coherent state this means

\[
\boxed{
\{C_{\alpha\alpha}\}_\alpha
\not\Rightarrow
\{C_{\alpha\beta}\}_{\alpha,\beta}
\not\Rightarrow
ff^*.}
\]

This does not say that an arbitrary independent phase rotation is a gauge of the
full Navier--Stokes field.  It says the opposite: **diagonal child data cannot see
whether such relative phase information changed**, while coherent synthesis can.
The missing datum belongs to pair/coherence state.

A two-child algebraic witness is immediate.  Let `f_1=f_2=v\ne0`.  The child
diagonals are `vv^*` in both of the following cases, but

\[
(v+v)(v+v)^*=4vv^*,
\]

whereas after the relative phase flip `f_2\mapsto-f_2`,

\[
(v-v)(v-v)^*=0.
\]

**Label: EXACT WANG COHERENT-PAIR CONSEQUENCE / DIAGONAL-STATE NO-GO.**

---

## 4. Kelvin specialization: only a common `O(3)` rotation is Brownian-driver gauge

For one Kelvin stochastic-flow replica, all residual packets use the same spatial
Brownian vector `W\in\mathbb R^3`:

\[
d\chi_g=\sqrt{2\nu}\,\Sigma_g\,dW.
\]

The same-replica q.v. blocks are

\[
\boxed{
\Gamma_{gh}=2\nu\Sigma_g\Sigma_h^T.}
\]

A common orthogonal change of Brownian coordinates

\[
dW'=O^T dW,
\qquad
\Sigma_g'=\Sigma_gO
\quad\text{for every }g,
\qquad O\in O(3),
\]

is a genuine driver-basis gauge.  Every full Gram block is invariant:

\[
\Sigma_gOO^T\Sigma_h^T
=\Sigma_g\Sigma_h^T.
\]

Now allow an **independent** right rotation `O_g` for each germ.  Every diagonal
q.v. block remains unchanged,

\[
\Sigma_gO_gO_g^T\Sigma_g^T
=\Sigma_g\Sigma_g^T,
\]

but

\[
\boxed{
\Gamma_{gh}\mapsto
2\nu\Sigma_gO_gO_h^T\Sigma_h^T.}
\]

Unless the relative rotations collapse to one common driver transformation on the
relevant subspaces, this is not a coordinate change of the single shared `W`.  It
changes the inter-germ coupling seen by physical synthesis.

Therefore

\[
\boxed{
\{\Gamma_{gg}\}_g
\text{ forgets relative common-driver orientation}.}
\]

The independent per-germ invariance of the diagonal blocks is larger than the
actual common-driver gauge of one physical replica.

**Label: EXACT KELVIN q.v. GAUGE TYPING / COUNTEREXAMPLE-NO-GO.**

---

## 5. A two-germ Kelvin witness with identical diagonal q.v. and opposite synthesis

Let `S\ne0` and compare two common-driver libraries

\[
(\Sigma_1,\Sigma_2)=(S,S)
\]

and

\[
(\widetilde\Sigma_1,\widetilde\Sigma_2)=(S,-S).
\]

Both have exactly the same diagonal q.v. blocks

\[
2\nu SS^T,
\qquad
2\nu SS^T.
\]

Their cross blocks have opposite sign.  Under sum synthesis `A=[I\ I]`,

\[
\boxed{
A\Gamma_+A^T=8\nu SS^T,
\qquad
A\Gamma_-A^T=0.}
\]

Thus even inside the class of one-common-driver Gram factorizations, diagonal q.v.
blocks do not determine the synthesized q.v.

This is stronger than saying that an independent-noise model is different: the
nonuniqueness already exists at the level of **relative coupling inside a common
latent driver space**.

**Label: EXACT GRAM COUNTEREXAMPLE/NO-GO.**

---

## 6. Exact Navier--Stokes activates the negative Kelvin coupling

The previous repo-3 theorem gives an actual smooth NSE realization, not merely the
algebraic `(S,-S)` witness.  For

\[
u(y,t)=e^{-\nu k^2t}\cos(ky)e_x,
\]

with the two asymmetric Kelvin packets

\[
\rho=\frac{\pi}{2k},
\qquad
Y_1=\frac{\pi}{2k},
\qquad
Y_2=\frac{3\pi}{2k},
\]

the exact anchor-noise responses satisfy

\[
\Sigma_2=-\Sigma_1\ne0
\]

on the active residual/Brownian entry.  Hence the two diagonal q.v. blocks are
equal while the cross block is exactly negative and the sum synthesis cancels.

So the relative-coupling state erased by diagonal marginals is activated by exact
Navier--Stokes/Kelvin dynamics; it is not a bookkeeping pathology invented by the
abstract Gram lemma.

**Label: EXACT NSE CALIBRATION / RIGOROUS ACTIVATION.**

---

## 7. Common representation dictionary, distinct physical meanings

The two programmes now share a sharper quadratic dictionary:

| structure | Wang coherent children | Kelvin same-replica residual library |
|---|---|---|
| physical block | complex child field/fiber `f_alpha` | noise-response map `Sigma_g` |
| full pair block | `f_alpha f_beta^*` | `2nu Sigma_g Sigma_h^T` |
| diagonal marginal forgets | relative child phase/coherence | relative common-driver orientation |
| common latent gauge | common phase for the quadratic pair representation | common Brownian `O(3)` basis change |
| independent block change | generally alters coherent synthesis | generally alters same-replica coupling/model |
| synthesis law | full ordered child-pair sum | full Gram congruence `A Gamma A^T` |

The relative phase and relative Brownian orientation are **not the same physical
variable**.  What is common is the exact representation principle:

\[
\boxed{
\text{linear synthesis}
+\text{quadratic observable}
\Longrightarrow
\text{full relative block coupling is state}.}
\]

**Label: EXACT REPRESENTATION DICTIONARY.**

---

## 8. State-map no-go

A cross-program bridge that retains only diagonal child/germ quadratic marginals
cannot be universally compatible with the already-audited linear synthesis laws.
There exist full pair/Gram states with the same diagonals and different synthesized
outputs.

Therefore any literal Wang--Kelvin quadratic state bridge must either

1. carry the relevant full ordered pair/Gram coupling; or
2. prove an independent physical theorem that reconstructs the missing relative
   coupling from other Navier--Stokes state data on the intended domain.

No diagonal energy/q.v. list can manufacture that theorem by itself.

**Label: COUNTEREXAMPLE/NO-GO / OPEN BRIDGE.**

No recurrence, continuation, termination or global-regularity claim is made.
