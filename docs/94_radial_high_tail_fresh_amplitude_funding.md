# A late critical shell is large in recent nonlinear Duhamel amplitude, not only in fresh energy flux

Status: **EXACT MILD NSE IDENTITY / RIGOROUS HEAT-MEMORY CONSEQUENCE**.

## 1. High-pass mild equation

Let `P_R` be the hard high-pass Fourier projection `|k|>=R` and write

\[
u_R=P_Ru.
\]

On every smooth interval `[t-L,t]`, the Leray Navier--Stokes equation gives exactly

\[
\boxed{
u_R(t)
=e^{\nu L\Delta}u_R(t-L)
+G_R[t-L,t],}
\]

where

\[
G_R[t-L,t]
=-\int_{t-L}^t
 e^{\nu(t-s)\Delta}
P_R\mathbb P\nabla\cdot(u\otimes u)(s)\,ds.
\]

`G_R` is the actual recent nonlinear Duhamel amplitude.  It is not normalized as a causal probability and is not assumed positive.

## 2. Heat erases the old vector in amplitude

Because every retained frequency has `|k|>=R`,

\[
\boxed{
\|e^{\nu L\Delta}u_R(t-L)\|_2
\le e^{-\nu R^2L}\|u(t-L)\|_2
\le e^{-\nu R^2L}\sqrt{E_*}.}
\]

Suppose a terminal hard shell `C_N subset {|k|>=R}` satisfies

\[
N\|P_{C_N}u(t)\|_2^2\ge\eta.
\]

Then

\[
\|u_R(t)\|_2\ge\sqrt{\eta/N}.
\]

Choose

\[
\boxed{
L_N^{amp}
=\frac1{\nu R^2}
\log\!\left(4\sqrt{\frac{E_*N}{\eta}}\right),}
\]

when the logarithm is positive.  The old term is at most

\[
\frac14\sqrt{\eta/N}.
\]

The exact mild identity and the reverse triangle inequality therefore force

\[
\boxed{
\|G_R[t-L_N^{amp},t]\|_2
\ge\frac34\sqrt{\eta/N}.}
\]

## 3. Physical meaning

BK showed that at least half the terminal critical energy must be recently funded by actual upward radial work.  The present theorem is the amplitude-side companion:

> the current high-pass vector itself cannot be mostly ancient heat-surviving amplitude; a definite `L^2` part is a recent nonlinear Duhamel response.

No individual earlier deposit is paired to a later withdrawal.

## 4. Why this matters for polarization

CO controls the full two-helicity polarization of each **fresh heterochiral source atom**.  CU now shows that late critical high-pass state has a large recent source-generated vector component.  One final interface remains before CO can be applied directly to the state:

- disintegrate `G_R` by the already-typed physical source owners;
- on the comparable heterochiral branch, decide whether the mixed-polarization source atoms survive in the Duhamel sum or undergo substantial temporal/inter-atom cancellation.

Such cancellation is a phase/polarization phenomenon and must remain typed separately; it is not silently estimated away.

No regularity conclusion is claimed.
