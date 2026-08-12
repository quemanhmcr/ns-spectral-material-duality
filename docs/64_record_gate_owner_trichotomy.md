# Every radial record gate resolves into local crossing, resolved incidence, or a genuine UV-skip companion

Status: **EXACT POSITIVE-FLOW PARTITION / RIGOROUS OWNER PIGEONHOLE**. This theorem starts from the BN net radial record gate and refines only the actual upward donor measure. No norm estimate is used.

## 1. Start from a BN record gate

At a record-gate radius `R`,

\[
F(R)=\Phi_\uparrow(R)-\Phi_\downarrow(R)\ge\nu G(R),
\]

where `G(R)=sum_(|k|>R,s)|k|^2E_(k,s)`. Since `Phi_down>=0`,

\[
\boxed{\Phi_\uparrow(R)\ge\nu G(R).}
\]

Thus the record event carries a definite positive actual upward energy-flow law. We refine that same law by physical frequency geometry; no second Hahn decomposition is taken.

## 2. First split: far-low donor versus near-boundary donor

Every upward atom has donor radius `<R` and recipient radius `>R`. Split it into

\[
\Phi_{far}=\Phi_\uparrow\{|k_d|<R/4\},
\qquad
\Phi_{near}=\Phi_\uparrow\{R/4\le|k_d|<R\}.
\]

Exactly `Phi_up=Phi_far+Phi_near`. Hence at least one satisfies

\[
\boxed{\Phi_{far}\ge\frac{\nu G(R)}2\quad\text{or}\quad\Phi_{near}\ge\frac{\nu G(R)}2.}
\]

## 3. Far-low donor is a literal hard low--high incidence

Take one far atom with donor `d`, recipient `r`, and third closed-triad mode `c`. Since `|d|<R/4` and `|r|>R`,

\[
\boxed{|c|\ge |r|-|d|>3R/4.}
\]

So the recipient source is literally low--high: one interaction leg is below `R/4` and the other is already high.  To type this event, do **not** identify the hard low leg with Wang's smooth strict transporter.  Instead use the physical hard split at this same event,

\[
V_R=P_{|k|<R/4}u,
\qquad
h_R=u-V_R.
\]

The exact mixed NSE operator on the high field is

\[
L_{V_R}f=\mathcal B(V_R,f)+\mathcal B(f,V_R).
\]

On divergence-free `L^2`, `B(V_R,.)` is skew-adjoint.  In the second term the Leray projector disappears in the energy pairing and the matrix `grad V_R` splits as

\[
\nabla V_R=S_R+\Omega_R,
\qquad S_R^T=S_R,
\qquad\Omega_R^T=-\Omega_R.
\]

On the divergence-free subspace define

\[
\mathsf S_R f=\mathbb P(S_Rf),
\qquad
\mathsf K_Rf=\mathbb P(V_R\cdot\nabla f+\Omega_Rf).
\]

Then, **exactly**,

\[
\boxed{L_{V_R}=\mathsf K_R+\mathsf S_R,\qquad \mathsf K_R^*=-\mathsf K_R,\quad \mathsf S_R^*=\mathsf S_R.}
\]

In an energy pairing with a divergence-free role, Leray drops out and the symmetric row is literally the physical strain contraction with `S_R`.  For any complete hard high-role partition, the `mathsf K_R` row is conservative same-event role redistribution while the `mathsf S_R` row is strain/deformation work.  This is the hard-event analogue of Wang's smooth resolved-interface owner split; no equality of the two transporter fields is assumed.

If the far branch owns the first split, its **canonical positive edge work** is at least `nu G(R)/2`.  Decompose each far low--high edge before any modal summation.  On every signed edge atom,

\[
R_{LH,e}=R_{K,e}+R_{S,e},
\qquad
[R_{LH,e}]_+\le [R_{K,e}]_+ + [R_{S,e}]_+.
\]

Integrating this inequality over the same far edge sublaw preserves gross positive work without losing it to later modal cancellation.

Therefore one of the two literal rows carries at least

\[
\boxed{\nu G(R)/4.}
\]

There is no independent nonlocal-companion currency on this branch.

## 4. Near-boundary donor: local crossing or true UV skip

If the near branch owns the first split, divide it by recipient radius:

\[
\Phi_{loc}=\Phi_{near}\{|k_r|\le4R\},
\qquad
\Phi_{skip}=\Phi_{near}\{|k_r|>4R\}.
\]

Then

\[
\boxed{\Phi_{loc}\ge\frac{\nu G(R)}4\quad\text{or}\quad\Phi_{skip}\ge\frac{\nu G(R)}4.}
\]

For every local atom,

\[
R/4\le|k_d|<R<|k_r|\le4R,
\]

so

\[
\boxed{|k_r|/|k_d|\le16.}
\]

For every skip atom, `|k_d|<R` and `|k_r|>4R`, hence

\[
\boxed{|k_c|\ge |k_r|-|k_d|>3R.}
\]

Thus a true UV skip requires a high companion at the same physical event.

## 5. Exact three-way record owner alternative

Every BN record gate has at least one of

\[
\boxed{
\begin{array}{ll}
\textbf{Resolved:}&\text{skew donor/relink or strain work }\ge \nu G(R)/4,\\[1mm]
\textbf{Local:}&\Phi_{loc}\ge \nu G(R)/4\text{ with donor/recipient ratio }\le16,\\[1mm]
\textbf{UV skip:}&\Phi_{skip}\ge \nu G(R)/4\text{ and a companion }|k_c|>3R.
\end{array}}
\]

Exact ties remain joint. This partitions actual positive upward energy flow, not capacity mass or a new causal probability.

## 6. Scope

The resolved branch is already typed upstream. The local branch has bounded radial geometry. Only the UV-skip branch retains the true high-companion question, now with a quantitative work lower and exact companion floor.

The theorem does not terminate the local or UV-skip branches and makes no regularity claim.
