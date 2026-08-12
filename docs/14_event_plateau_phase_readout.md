# Wang hard-event phase is an exact readout of the full smooth carrier on the event plateau

Status: **Exact operator/material-cubic identity plus a quadratic-to-cubic no-go.**

This note uses the literal Wang distinction between the hard physical event role

\[
P_{a\sigma}=1_{C_a}(D)H_\sigma(D)
\]

and the scalar smooth PDE envelope `Q(t,D)` chosen at that event with

\[
QP=PQ=P.
\]

No upstream theorem is modified here.  The point is to identify exactly what information is and is not transported by the smooth carrier.

---

## 1. The full smooth carrier contains the hard event component exactly

For one event role `P` and its smooth envelope `Q`,

\[
\boxed{P(Q\omega)=P\omega.}
\]

This is not an estimate and it does not use small overlap.  It is the literal plateau identity `PQ=P`.

For three event legs `P_i,Q_i`, define

\[
\Phi_i^P=H^TP_i\omega_i,
\qquad
\Phi_i^{P\leftarrow Q}=H^TP_iQ_i\omega_i.
\]

Then leg by leg

\[
\boxed{\Phi_i^{P\leftarrow Q}=\Phi_i^P.}
\]

Hence the hard material interaction read from the full smooth carrier is exactly the hard interaction read from the physical field:

\[
\boxed{
\mathcal Z_P(Q_0\omega_0,Q_1\omega_1,Q_2\omega_2)
=
\mathcal Z_P(\omega_0,\omega_1,\omega_2),
}
\]

where

\[
\mathcal Z_P
=
\frac1{\det H}
\overline{H^TP_0\omega_0}\cdot
\bigl(H^TP_1\omega_1\times H^TP_2\omega_2\bigr).
\]

Therefore both `Re Z_P` and `arg Z_P` are exactly recoverable at the event from the **full carrier field** followed by the hard event readout.

**Classification: EXACT OPERATOR / MATERIAL 3-FORM IDENTITY.**

This is the cubic counterpart of Wang's exact coefficient registration
`<Pu,phi>=<Qu,Pphi>`.

---

## 2. Event readout is independent of how the envelope is filled outside the plateau

Let `Q_i` and `Q_i~` be two smooth envelopes satisfying

\[
P_iQ_i=P_i\widetilde Q_i=P_i.
\]

Then

\[
P_iQ_i\omega_i=P_i\widetilde Q_i\omega_i=P_i\omega_i,
\]

so

\[
\boxed{
\mathcal Z_P(Q_0\omega_0,Q_1\omega_1,Q_2\omega_2)
=
\mathcal Z_P(\widetilde Q_0\omega_0,\widetilde Q_1\omega_1,\widetilde Q_2\omega_2).
}
\]

The overlap region is therefore a PDE-carrier choice, not an additional physical phase owner **at the registered event**.

**Classification: EXACT ENVELOPE-GAUGE INVARIANCE OF EVENT READOUT.**

---

## 3. Why the smooth scalar cubic can still be wrong

Write

\[
Q_i=P_i+R_i.
\]

The unprojected smooth cubic contains the hard term plus the seven nonempty `P/R` overlap terms.  Thus generally

\[
\mathcal Z_Q\neq \mathcal Z_P.
\]

There is no contradiction with the theorem above.  The two statements concern different observables:

- `Q omega` is a full field and retains `P omega` exactly on the event plateau;
- `Z_Q` is one cubic scalar compression of that field and mixes hard and overlap components before the hard role is re-applied.

So the overlap obstruction is an **information-compression obstruction**, not loss of the hard component from the carrier field.

**Classification: EXACT MULTILINEAR DECOMPOSITION / COUNTEREXAMPLE-NO-GO.**

---

## 4. Quadratic carrier energy cannot inherit cubic interaction phase

The native smooth Wang carrier currency is quadratic, `\langle u,Q^2u\rangle`.  A quadratic observable cannot determine the `U(1)` phase of a nonzero cubic interaction.

Indeed, fix three hard event vectors with nonzero cubic interaction and rotate one Fourier coefficient by a phase while rotating its reality partner by the conjugate phase.  Every modal quadratic energy is unchanged, while

\[
\mathcal Z_P\mapsto e^{\pm i\theta}\mathcal Z_P.
\]

Thus one may preserve all hard/smooth quadratic energies while changing `arg Z_P` arbitrarily.

\[
\boxed{
\text{quadratic carrier-energy inheritance}
\not\Rightarrow
\text{cubic phase inheritance}.
}
\]

**Classification: COUNTEREXAMPLE/NO-GO.**

This is physically important: the Wang `Q^2` Hahn gate is an energy-causality theorem, not a hidden phase-transport theorem.

---

## 5. Literal causal architecture after the distinction

The exact picture is now:

\[
\text{hard physical event}
\to
\text{smooth full-field carrier}
\to
\text{physical energy gate / actual HH work}
\to
\text{new hard event readout}.
\]

At an event whose hard role lies on the plateau of its registered envelope, hard phase is read exactly by `P(Q omega)=P omega`.  Between events, no persistent hard projector or scalar hard phase is required.

At a later event with a new hard role `P^+`, the old envelope `Q^-` need not satisfy `P^+Q^-=P^+`.  Therefore this theorem does **not** assert event-to-event phase persistence.  The later phase is read from the actual field at the later nonlinear event, exactly as the upstream architecture prescribes.

**Classification: RIGOROUS CONSEQUENCE / TYPING CLARIFICATION.**

The remaining Wang bridge is no longer “control seven overlap terms so that `Z_Q` becomes `Z_P`.”  Such control is needed only if one insists on a smooth scalar phase carried between events.  The literal eventwise architecture does not require that identification.
