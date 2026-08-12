# The parabolic corridor has an exact moving-cut energy current

Status: **EXACT NSE / MOVING-CUT REYNOLDS IDENTITY**.

The matched heat corridor should not be treated as a static set of Fourier labels.  Its boundaries move because the remaining time `tau=T-t` changes.  The exact current law distinguishes physical nonlinear crossing from this observer/clock motion.

## 1. Hard parabolic corridor

Let

\[
a_i(t)=2\nu|k_i|^2(T-t)
\]

and define

\[
\chi_i(t)=\mathbf1_{\{\alpha\le a_i(t)\le\beta\}}.
\]

The corridor kinetic energy is

\[
M_C(t)=\sum_i\chi_i(t)E_i(t).
\]

Using the exact donor-kernel energy law,

\[
\boxed{
\dot M_C
=
\sum_{i,j}(\chi_j-\chi_i)K_{ij}
-
\sum_i d_i\chi_iE_i
+
\sum_i\dot\chi_iE_i,
\qquad d_i=2\nu|k_i|^2.
}
\]

For a hard cut the last term is a signed event measure.  Equivalently use smooth approximants and pass distributionally.

## 2. Physical typing of every face

The first term is actual nonlinear crossing:

- `chi_i=0, chi_j=1`: kinetic energy transported physically into the corridor;
- `chi_i=1, chi_j=0`: physical nonlinear exit;
- equal selector values: internal conservative transport, invisible to total corridor mass.

The second term is physical viscous killing while the energy is inside the corridor.

The third term is only motion of the heat-clock boundaries.  Since

\[
\dot a_i=-d_i<0,
\]

\[
\dot\chi_i
=\delta(a_i-\alpha)\dot a_i
-\delta(a_i-\beta)\dot a_i.
\]

Therefore:

- crossing `a=beta` by clock motion is **entry** from superparabolic to matched;
- crossing `a=alpha` by clock motion is **exit** from matched to subparabolic.

The clock never moves a fixed modal state in the opposite direction.

## 3. Clock motion cannot create a recurrent corridor cycle

For one fixed mode segment, `a(t)` is strictly decreasing.  It can cross the upper face at most once and the lower face at most once before a nonlinear jump changes the modal scale.

Hence repeated subparabolic-to-corridor reentry is necessarily a nonlinear/up-frequency transfer (or a separate relabel/relink event); it cannot be blamed on repeated motion of the same heat clock.

**Classification: RIGOROUS TOPOLOGICAL CONSEQUENCE OF THE EXACT MOVING-CUT LAW.**

## 4. Relation to earlier moving-role time faces

This is a concrete specialization of the general moving-cut lesson already present in the third repo: differentiating a role requires its `dot Q`/time-face.  Here the role is not arbitrary; it is the unique heat-conjugated parabolic coordinate from Theorem BD, so the time-face has a fixed physical direction.
