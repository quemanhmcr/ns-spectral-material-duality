# Future-heat conjugation turns viscosity into an exact parabolic transport currency

Status: **EXACT NSE / HEAT-CONJUGATION IDENTITY**, **RIGOROUS PARABOLIC PRICE CONSEQUENCE**.

The previous note exposes the actual nonlinear energy transport table `K_ij` and physical viscous killing rates `d_i=2 nu |k_i|^2`.  This note asks for a scalar coordinate supplied by the PDE itself, not by an external norm.

Fix a candidate terminal time `T` and write

\[
\tau=T-t>0.
\]

## 1. Future heat gauge in physical space

Define

\[
\boxed{v_T(t)=e^{\nu(T-t)\Delta}u(t).}
\]

Because

\[
\partial_t e^{\nu(T-t)\Delta}=-\nu\Delta e^{\nu(T-t)\Delta},
\]

while Navier--Stokes has `+nu Delta u`, the linear viscous term cancels exactly:

\[
\boxed{
\partial_t v_T
=-e^{\nu(T-t)\Delta}\mathbb P\nabla\cdot(u\otimes u).
}
\]

Thus the future-heat-gauged kinetic energy

\[
\boxed{
\mathscr H_T(t)=\frac12\|e^{\nu(T-t)\Delta}u(t)\|_2^2
}
\]

changes only through nonlinear physical transfer.  This is not an estimate and does not use knowledge of `u(T)`.

## 2. Modal survival coordinate

For mode `i` let

\[
\boxed{
q_i^T(t)=e^{-d_i(T-t)}
=e^{-2\nu|k_i|^2\tau}.
}
\]

It obeys

\[
\partial_tq_i^T=d_iq_i^T.
\]

Since `E_i=|u_i|^2/2`,

\[
\mathscr H_T=\sum_iq_i^TE_i.
\]

The universal Dynkin identity from `docs/39_energy_transport_killing.md` gives exact cancellation of clock motion and viscous killing:

\[
\boxed{
\dot{\mathscr H}_T
=\sum_{i,j}(q_j^T-q_i^T)K_{ij}.
}
\]

Equivalently, current Wang's same-time donor measure transports the heat-survival mark without creating or destroying it except through its change between donor and recipient labels.

## 3. Heat-defect coordinate retains the physical dissipation ledger

Define

\[
\boxed{
w_i^T=1-q_i^T,
\qquad
\mathscr B_T=\sum_iw_i^TE_i.
}
\]

Then

\[
\partial_tw_i^T=-d_iq_i^T,
\qquad
w_i^T+q_i^T=1,
\]

and therefore

\[
\boxed{
\dot{\mathscr B}_T
=
\sum_{i,j}(w_j^T-w_i^T)K_{ij}
-
\sum_i d_iE_i.
}
\]

The three terms are literal:

1. bounded parabolic modal content `B_T`;
2. signed nonlinear transport across parabolic heat levels;
3. actual kinetic-energy dissipation.

No exchange rate has been inserted between unrelated currencies; all three arise from one exact NSE identity.

## 4. A forward scale jump has a uniform price only in the parabolic corridor

Put

\[
a_i(t)=d_i\tau=2\nu|k_i|^2(T-t).
\]

Suppose a donor state satisfies

\[
\alpha\le a_i\le\beta,
\qquad 0<\alpha<\beta<\infty,
\]

and an actual recipient obeys the physical forward scale relation

\[
|k_j|\ge\lambda |k_i|,
\qquad \lambda>1.
\]

Then `a_j>=lambda^2 a_i`, and

\[
\boxed{
\Delta w_{ij}
:=w_j^T-w_i^T
=e^{-a_i}-e^{-a_j}
\ge c_{\alpha,\beta,\lambda}>0,
}
\]

where

\[
\boxed{
c_{\alpha,\beta,\lambda}
=\min_{a\in[\alpha,\beta]}
\left(e^{-a}-e^{-\lambda^2a}\right).
}
\]

This is the exact reason the unresolved Kelvin seam

\[
2\nu(T-t)N^2\asymp1
\]

matters: if `a->0` or `a->infinity`, the price of a fixed frequency-ratio jump degenerates to zero.  Parabolic scale matching is not decorative synchronization; it is what turns actual scale progress into a nondegenerate bounded PDE currency.

## 5. Physical no-go: positive work is not automatically parabolic progress

Current Wang upstream explicitly retains positive nonforward work and coarse hard-cell self-loops.  Such work is real physical energy redistribution but supplies no directional scale progress.  In the present currency a self-loop has

\[
\Delta w=0
\]

exactly.

Therefore

\[
\boxed{
\text{positive nonlinear work}
\not\Rightarrow
\text{positive parabolic transport price}.
}
\]

A proof must obtain the scale direction from the literal physical event, or route the nonforward/self-loop piece to its own exit/owner.  It cannot infer progress merely from positivity of work.

## 6. Scope

`H_T` and `B_T` are globally bounded by kinetic energy, but their unrestricted donor transport is signed.  Backscatter can cancel forward transport in the global scalar.  The next theorem removes that cancellation only after selecting one actual energy lineage and stopping it at reverse/nonforward/reentry exits.

No recurrence theorem is claimed in this note.
