# Wang coherent refinement and Kelvin residual refinement share the same tensor-square law at quadratic level

Status: **EXACT LINEAR-SYNTHESIS / PAIR-FUNCTOR BRIDGE / NO STATE-SPACE IDENTIFICATION**.

Current Wang and current Kelvin use different physical states and different refinement semantics.  Nevertheless, whenever either construction is genuinely linear before quadratic readout, one algebraic law is unavoidable: **the second-order state is transported by the tensor-square functor**.

This is a common structural law, not a claim that the two refinement maps are the same map.

## 1. Universal deterministic pair lift

Let a parent physical vector/state be synthesized linearly from refined children,

\[
y=\sum_{\alpha=1}^m y_\alpha.
\]

Then the rank-one pair state is

\[
\boxed{
y\otimes y
=\sum_{\alpha,\beta}y_\alpha\otimes y_\beta.}
\]

Equivalently,

\[
\boxed{
y\otimes y
=\sum_\alpha y_\alpha\otimes y_\alpha
+\sum_{\alpha<\beta}
(y_\alpha\otimes y_\beta+y_\beta\otimes y_\alpha).}
\]

The off-diagonal pair terms are not optional.  They are the coherence/interference carried by the linear parent synthesis.

For a Hilbert energy,

\[
\boxed{
\|y\|^2
=\sum_\alpha\|y_\alpha\|^2
+2\sum_{\alpha<\beta}\Re\langle y_\alpha,y_\beta\rangle.}
\]

A diagonal-only child ledger is exact only when the refinement is orthogonal in the physical quadratic pairing.

## 2. Wang coherent refinement is exactly in this class

Current Wang's positive coherent localization operators satisfy, for a measurable refinement `E=disjoint union E_alpha`,

\[
\boxed{T_E=\sum_\alpha T_{E_\alpha}.}
\]

Hence for the physical field portion

\[
f_E=T_Ef,
\qquad
f_\alpha=T_{E_\alpha}f,
\]

one has

\[
\boxed{f_E=\sum_\alpha f_\alpha.}
\]

Therefore the exact quadratic refinement is

\[
\boxed{
f_E\otimes f_E
=\sum_{\alpha,\beta}f_\alpha\otimes f_\beta.}
\]

Wang correctly does **not** claim the coherent POVM pieces are orthogonal projections.  Thus cross-pair coherences generally survive.

This is why coherent refinement can be additive at first order while physical energy/covariance cannot be reconstructed by summing child diagonals alone.

## 3. Kelvin residual synthesis is the stochastic/ensemble version of the same functor

Current Kelvin has a full residual pair state `mathbb Q` and a physical linear synthesis map `A`.  The physical covariance is

\[
\boxed{Q_A=A\mathbb Q A^T.}
\]

This is exactly the pair pushforward

\[
\boxed{A\mapsto A\otimes A.}
\]

For a deterministic rank-one library `mathbb Q=c c^T`, this reduces to

\[
Q_A=(Ac)(Ac)^T,
\]

the same deterministic identity as §1.

For an ensemble/random pair state, expectation is linear and the same tensor-square pushforward remains exact.

## 4. Kelvin finite reset is the finite-difference form of the same pair functor

If

\[
A_+=A_-+\Delta A,
\]

then

\[
\boxed{
A_+\mathbb Q A_+^T-A_-\mathbb Q A_-^T
=\Delta A\mathbb Q A_-^T
+A_-\mathbb Q\Delta A^T
+\Delta A\mathbb Q\Delta A^T.}
\]

The left/right/quadratic reset faces are therefore not peculiar extra Kelvin bookkeeping.  They are the exact finite-difference expansion of the same tensor-square law that governs any quadratic readout of a linearly refined/synthesized state.

## 5. Smooth overlapping Wang roles give a physical nonzero cross term

Take a smooth scalar Fourier partition

\[
R_1(D)+R_2(D)=I,
\]

with both multipliers nonzero on the same active mode.  Put

\[
u_1=R_1u,
\qquad
u_2=R_2u.
\]

Then

\[
u=u_1+u_2
\]

exactly, but

\[
\boxed{
\|u\|_2^2
=\|u_1\|_2^2+\|u_2\|_2^2
+2\langle u_1,u_2\rangle.}
\]

For overlapping smooth roles the cross term is generically nonzero.  This is the Fourier analogue of the nonorthogonality already built into Wang's coherent positive-contraction refinement.

By contrast, truly orthogonal hard roles can kill the cross term.  The distinction is structural and must be retained.

## 6. State-map acceptance rule

Suppose a future bridge identifies a linear physical synthesis from some Wang-side state `c_W` to a Kelvin residual vector,

\[
r_K=Jc_W.
\]

Then at pair level the bridge is not free to choose a new rule.  It must satisfy

\[
\boxed{Q_K=JQ_WJ^T}
\]

for the actual full pair state `Q_W`, with any hidden/reduced-state resolution covariance kept separately as already proved elsewhere in repo 3.

Thus a candidate bridge must preserve:

1. first-order linear synthesis;
2. second-order tensor-square pushforward;
3. off-diagonal coherence/cross pairs;
4. finite reset expansion under synthesis changes.

Passing only first moments or diagonal child energies is not enough.

## 7. Scope

This theorem identifies a **common functorial law**, not a common state space.

It does not assert:

- Wang coherent cells are Kelvin germs;
- Wang `T_E` is Kelvin synthesis `A`;
- coherent-cell energy is a covariance probability;
- every Wang refinement is physical Kelvin refinement.

It says only that once a linear physical state map/refinement is declared, its quadratic consequences are rigid and the two programmes already obey the same tensor-square algebra in their own state spaces.
