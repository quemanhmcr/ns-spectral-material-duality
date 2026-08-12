# A stopped forward energy lineage has a finite one-sided parabolic budget

Status: **EXACT STOPPED TRANSPORT IDENTITY** and **RIGOROUS FINITE EXPECTED-DEPTH CONSEQUENCE**.

The global future-heat scalar sees signed forward/backward transport.  A causal proof, however, follows one selected physical continuation law.  Once the actual donor kernel has supplied the jump rates, this can be done without inventing packet persistence.

## 1. Selected subpopulation and absorbing exits

Let `r_ij=K_ij/E_i` be the exact rates from `docs/39_energy_transport_killing.md`.  At time `s`, choose a nonnegative selected energy subpopulation

\[
0\le m_i(s)\le E_i(s).
\]

Let `C_t` be the set of typed **continuation edges**.  A selected lineage

- follows the same physical rate `r_ij` while `(i,j) in C_t`;
- is absorbed at the first transfer edge outside `C_t`;
- is killed at the physical viscous rate `d_i`.

The alive selected mass obeys

\[
\boxed{
\dot m_i
=\sum_jm_jr_{ji}\mathbf1_{(j,i)\in C_t}
-m_i\sum_jr_{ij}
-d_im_i.
}
\]

There is no incoming mass after an exit.  Re-entry, if physically present, is a distinct owner and invalidates this stopped-lineage theorem until explicitly re-registered.

Let

\[
M=\sum_im_i,
\qquad
D_m=\sum_id_im_i,
\]

and let

\[
X=\sum_{(i,j)\notin C_t}m_ir_{ij}
\]

be the absorbing exit rate.  Then

\[
\boxed{\dot M=-D_m-X.}
\]

Thus

\[
M(t)+\int_s^tD_m\,dr+\int_s^tX\,dr=M(s).
\]

Every unit of selected energy is still alive, viscously killed, or exited exactly once.

## 2. Exact stopped heat-defect balance

Use the future-heat defect

\[
w_i=1-e^{-d_i(T-t)}.
\]

Define

\[
B_m(t)=\sum_iw_i(t)m_i(t).
\]

A direct product rule gives

\[
\boxed{
\dot B_m
=F_{\rm prog}-D_m-X_w,
}
\]

where

\[
F_{\rm prog}
=\sum_{(i,j)\in C_t}(w_j-w_i)m_ir_{ij},
\]

and

\[
X_w
=\sum_{(i,j)\notin C_t}w_i m_ir_{ij}.
\]

The clock term and the viscous `w`-weighted killing combine to the **full** physical kill rate `D_m`; no estimate is involved.

## 3. One-sided continuation budget

Assume every continuation edge is parabolically forward:

\[
w_j-w_i\ge0
\qquad\text{on }C_t.
\]

Integrating the exact identity,

\[
\int_s^tF_{\rm prog}
=B_m(t)-B_m(s)
+\int_s^tD_m
+\int_s^tX_w.
\]

Since `0<=w<=1`,

\[
B_m(t)\le M(t),
\qquad
X_w\le X.
\]

Using exact mass conservation gives the sharp bound

\[
\boxed{
\int_s^tF_{\rm prog}\,dr
\le
M(s)-B_m(s)
=\sum_iq_i^T(s)m_i(s)
\le M(s).
}
\]

This is the finite currency that the unrestricted global scalar did not provide.  Reverse/nonforward transfer cannot cancel it because such a transfer is an absorbing exit from this typed lineage rather than an internal negative contribution.

## 4. Uniform parabolic price gives finite expected continuation depth

Suppose in addition every internal continuation edge satisfies

\[
w_j-w_i\ge c_*>0.
\]

Then

\[
\boxed{
\int_s^t
\sum_{(i,j)\in C_r}m_i r_{ij}\,dr
\le
\frac{\sum_iq_i^T(s)m_i(s)}{c_*}.
}
\]

After normalizing the initial selected mass to a probability law, the left side is the expected number of continuation jumps before exit/killing.  Therefore

\[
\boxed{
\mathbb E N_{\rm cont}
\le\frac{\mathbb E q^T(X_s,s)}{c_*}
\le\frac1{c_*}.
}
\]

Finite expectation implies that an energy-weighted stopped lineage has infinitely many such continuation jumps with probability zero.

**Classification: RIGOROUS ENERGY-WEIGHTED DEPTH CONSEQUENCE.**

This still does not exclude a zero-energy-measure exceptional infinite branch.  The next theorem adds a scale-critical event mass floor and bounded scale ratios to convert the survival estimate into a deterministic finite-depth obstruction.

## 5. Scope

The result needs an actual donor kernel, actual selected lineage semantics, parabolic-forward internal edges, and absorbing treatment of all reverse/nonforward/reentry events.  Dropping any of these changes the theorem rather than weakening a constant.
