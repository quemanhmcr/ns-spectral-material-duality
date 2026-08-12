# Every radial record gate resolves into hard low--high incidence, comparable local crossing, or a genuine UV skip

Status: **EXACT POSITIVE-FLOW PARTITION / RIGOROUS OWNER PIGEONHOLE**.  The partition is made on the two literal interaction parents of each actual upward recipient edge, not merely on its energy-donor label.  No norm estimate is used.

## 1. Start from a BN record gate

At a record-gate radius `R`,

\[
F(R)=\Phi_\uparrow(R)-\Phi_\downarrow(R)\ge\nu G(R),
\]

so, because `Phi_down>=0`,

\[
\boxed{\Phi_\uparrow(R)\ge\nu G(R).}
\]

Every atom of this canonical positive upward flow contains

- an energy donor mode `d` with `|k_d|<R`;
- a positive recipient mode `r` with `|k_r|>R`;
- the third closed-triad mode `c`, which is the recipient's other quadratic interaction parent.

The two interaction parents of the recipient are therefore exactly `d` and `c`.

## 2. First physical split: does the quadratic source contain a genuinely low leg?

Define

\[
\Phi_{res}
=
\Phi_\uparrow
\{\min(|k_d|,|k_c|)<R/4\},
\]

and let `Phi_hi=Phi_up-Phi_res`.  Thus every atom of `Phi_hi` satisfies

\[
|k_d|\ge R/4,
\qquad
|k_c|\ge R/4.
\]

Exactly,

\[
\boxed{
\Phi_{res}\ge\frac{\nu G(R)}2
\quad\text{or}\quad
\Phi_{hi}\ge\frac{\nu G(R)}2.}
\]

This split is made by the actual quadratic source geometry.  It cannot misclassify a near-boundary energy donor whose *other* interaction parent is low.

## 3. The resolved branch has an exact hard-event skew/strain split

On `Phi_res`, choose the literal hard low field

\[
V_R=P_{|k|<R/4}u,
\qquad
h_R=u-V_R.
\]

Every retained recipient edge belongs to the mixed operator

\[
L_{V_R}f=\mathcal B(V_R,f)+\mathcal B(f,V_R).
\]

Write

\[
\nabla V_R=S_R+\Omega_R,
\qquad S_R^T=S_R,
\qquad\Omega_R^T=-\Omega_R.
\]

On the divergence-free subspace define

\[
\mathsf S_Rf=\mathbb P(S_Rf),
\qquad
\mathsf K_Rf=\mathbb P(V_R\cdot\nabla f+\Omega_Rf).
\]

Then

\[
\boxed{
L_{V_R}=\mathsf K_R+\mathsf S_R,
\qquad
\mathsf K_R^*=-\mathsf K_R,
\quad
\mathsf S_R^*=\mathsf S_R.}
\]

In divergence-free energy pairing, `mathsf S_R` is the physical resolved-strain contraction and `mathsf K_R` is conservative same-event redistribution.  This is a hard-event identity; no equality with Wang's smooth strict transporter is assumed.

Decompose each canonical positive resolved edge before modal summation.  Edgewise,

\[
R_{LH,e}=R_{K,e}+R_{S,e},
\qquad
[R_{LH,e}]_+\le[R_{K,e}]_+ + [R_{S,e}]_+.
\]

Hence if `Phi_res>=nu G/2`, one of the two gross positive rows carries at least

\[
\boxed{\nu G(R)/4.}
\]

## 4. If there is no low interaction leg, split only by the recipient jump

Suppose instead `Phi_hi>=nu G/2`.  Split

\[
\Phi_{loc}
=
\Phi_{hi}\{|k_r|\le4R\},
\qquad
\Phi_{skip}
=
\Phi_{hi}\{|k_r|>4R\}.
\]

Then

\[
\boxed{
\Phi_{loc}\ge\frac{\nu G(R)}4
\quad\text{or}\quad
\Phi_{skip}\ge\frac{\nu G(R)}4.}
\]

### Comparable local branch

Every local atom has

\[
R/4\le |k_d|<R,
\qquad
R/4\le |k_c|,
\qquad
R<|k_r|\le4R.
\]

Triad closure gives

\[
|k_c|\le|k_d|+|k_r|<5R.
\]

Thus **all three physical mode scales** lie in the fixed window

\[
\boxed{R/4\le |k_d|,|k_c|,|k_r|<5R,}
\]

so the largest/smallest frequency ratio is strictly below `20`.

### True UV-skip branch

For every skip atom,

\[
|k_d|<R,
\qquad
|k_r|>4R,
\]

hence

\[
\boxed{|k_c|\ge|k_r|-|k_d|>3R.}
\]

So a true skip requires a high companion at the same physical event.

## 5. Exact record-gate alternative

Every BN gate has at least one quantitative owner:

\[
\boxed{
\begin{array}{ll}
\textbf{Resolved:}&
\text{hard low--high skew redistribution or strain work }\ge\nu G(R)/4,\\[1mm]
\textbf{Comparable local:}&
\Phi_{loc}\ge\nu G(R)/4,
\quad R/4\le |k_d|,|k_c|,|k_r|<5R,\\[1mm]
\textbf{UV skip:}&
\Phi_{skip}\ge\nu G(R)/4,
\quad |k_c|>3R.
\end{array}}
\]

Exact ties remain joint.  The measure being partitioned is the actual canonical positive upward energy flow; no capacity probability or second Hahn law is introduced.

## 6. Scope

The resolved branch is already physically typed by an exact hard-event operator identity.  The comparable branch is now genuinely comparable in **both** interaction parents, not merely in energy donor/recipient labels.  Only the UV-skip branch retains a genuine separated high-companion question.

The theorem does not terminate the comparable or UV-skip branches and makes no regularity claim.
