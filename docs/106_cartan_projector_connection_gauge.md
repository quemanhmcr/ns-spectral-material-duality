# Fixed event-role relink and moving-role connection are the same Cartan flux in different projector gauges

Status: **EXACT PROJECTOR/CARTAN IDENTITY / CROSS-WANG ROLE-GAUGE BRIDGE**.

This theorem closes the algebraic distinction deliberately retained by current Wang between fixed-event skew `K` redistribution and a role transported by a smooth connection.  It does not identify the two representations; it gives the exact gauge transformation between them.

## 1. Abstract physical state law

Let a real Hilbert-space state satisfy

\[
\dot y=(K+S)y,
\qquad K^*=-K,
\qquad S^*=S.
\]

Let `P(t)` be an orthogonal projector,

\[
P^2=P,
\qquad P^*=P,
\]

and define selected energy

\[
E_P=\frac12\langle y,Py\rangle
=\frac12\|Py\|^2.
\]

Differentiation gives

\[
\dot E_P
=\langle Py,(K+S)y\rangle
+\frac12\langle y,\dot Py\rangle.
\]

## 2. The exact connection-covariant projector defect

Because `K` is skew,

\[
\frac12\langle y,[K,P]y\rangle
=-\langle Py,Ky\rangle.
\]

Define the **projector connection defect**

\[
\boxed{G_P:=\dot P-[K,P].}
\]

Then

\[
\boxed{
\dot E_P
=\langle Py,Sy\rangle
+\frac12\langle y,G_Py\rangle.
}
\]

This is an identity before any estimate or positive-part decomposition.

The two terms are physically distinct:

1. `P-S` term: actual symmetric deformation/metric work seen by the role;
2. `G_P` term: mismatch between role motion and the physical skew connection.

## 3. Fixed hard event role

For a fixed hard role on one physical event,

\[
\dot P=0,
\qquad
G_P=-[K,P].
\]

Hence

\[
\frac12\langle y,G_Py\rangle
=\langle Py,Ky\rangle.
\]

This is exactly the same-event conservative `K` relink read by Wang's fixed event-role decomposition.

Thus fixed-event `K` work is not a new source.  It is what the connection sector looks like in a **fixed projector gauge**.

## 4. Connection-transported role

Suppose instead that the role is transported by the same physical skew connection,

\[
\boxed{\dot P=[K,P].}
\]

Then

\[
G_P=0
\]

and

\[
\boxed{
\dot E_P=\langle Py,Sy\rangle.
}
\]

All `K` transfer has been absorbed into common role motion.  The physical deformation work remains.

This is the exact algebraic bridge between

\[
\boxed{
\text{Wang fixed-event conservative relink}
\quad\leftrightarrow\quad
\text{smooth connection-comoving role gauge}.
}
\]

They are not equal observables; they are two gauges of the same skew Cartan sector.

## 5. General moving role

For arbitrary smooth role motion,

\[
\dot P=[K,P]+G_P.
\]

The extra `G_P` face is the genuine moving-selector/interface mismatch after common connection transport has been quotiented.

For an orthogonal projector, differentiating `P^2=P` gives

\[
P\dot PP=0,
\qquad
(I-P)\dot P(I-P)=0,
\]

so smooth projector velocity is purely off-diagonal between selected and unselected subspaces.  The same is true of `[K,P]` and hence of `G_P`.

No diagonal "selector production" exists for a smooth orthogonal role.

## 6. Finite reselection is a finite face, not `Pdot`

At a physical re-registration time let the state be continuous but the analysis role jump

\[
P^-\to P^+.
\]

Then exactly

\[
\boxed{
E_{P^+}-E_{P^-}
=\frac12\langle y,(P^+-P^-)y\rangle.
}
\]

This jump may have either sign and is not an infinitesimal positive payment.  It belongs in the discrete/event part of the hybrid ledger.

## 7. Relation to Wang

Current Wang fixed-event `K` donor/relink calculus and its separately constructed smooth moving-carrier connection therefore fit one exact projector law:

- fixed projector -> visible conservative `K` flux;
- connection-comoving projector -> `K` is gauge-transported away;
- non-comoving smooth role -> explicit `G_P` interface face;
- hard reselection -> finite jump.

No cutoff, event role, or observer motion is promoted to a new physical source.
