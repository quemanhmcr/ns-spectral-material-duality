# Edgewise mixed heterochiral birth does not descend to mixed child state: an exact spin-2 azimuthal cancellation

Status: **EXACT ROTATIONAL-COVARIANCE COUNTEREXAMPLE/NO-GO**.  This theorem prevents an invalid final shortcut from CR/CO to a mixed-polarization state conclusion.

## 1. One fixed child, a rotated parent orbit

Fix a nonzero child wavevector `k` and a strict heterochiral parent pair

\[
p_0+q_0=k
\]

with parent helicities `+,-`.  Rotate both parents and their physical helical velocity vectors by `R_phi`, a Euclidean rotation through angle `phi` about the `k` axis:

\[
p_\phi=R_\phi p_0,
\qquad
q_\phi=R_\phi q_0.
\]

The child wavevector is unchanged.  Let `F_0` be the exact Leray-projected child source vector of the base parent pair.  Navier--Stokes rotational covariance gives

\[
F_\phi^{raw}=R_\phi F_0
\]

when the parent amplitude product is unchanged.

Now multiply the parent amplitude product at angle `phi` by the common complex phase `e^{i phi}`.  Bilinearity gives

\[
\boxed{F_\phi=e^{i\phi}R_\phi F_0.}
\]

This phase choice does not change any parent/child energy, triangle geometry, Waleffe magnitude, or capacity.

## 2. Child helical fibers carry spin one

Choose a fixed helical basis `h_+(k),h_-(k)` at the child.  Under rotation about `k`,

\[
R_\phi h_s(k)=e^{-is\phi}h_s(k).
\]

Write

\[
f_s(\phi)=\langle h_s(k),F_\phi\rangle.
\]

Then

\[
\boxed{
f_+(\phi)=f_+(0),
\qquad
f_-(\phi)=e^{2i\phi}f_-(0).}
\]

The common phase compensation has frozen the `+` source while the relative `-` component becomes a **spin-2 azimuthal phase**.

For a nondegenerate heterochiral pair, CO guarantees both `f_+(0)` and `f_-(0)` are nonzero.

## 3. Exact two-atom cancellation

Take two physically distinct parent pairs at

\[
\phi_1=0,
\qquad
\phi_2=\frac\pi2.
\]

Their source coefficients satisfy

\[
f_+(\phi_1)=f_+(\phi_2)=f_+(0),
\]

but

\[
f_-(\phi_2)=-f_-(\phi_1).
\]

Hence

\[
\boxed{
f_+^{tot}=2f_+(0),
\qquad
f_-^{tot}=0.}
\]

Choose the existing `+` child amplitude phase so that

\[
\Re(\overline{a_+}f_+(0))>0.
\]

Then **both atoms individually deliver positive `+` child work**, have identical work/capacity efficiency, identical CO minority fraction, and identical pair geometry; nevertheless their fresh minority-helicity source cancels exactly in the aggregate child equation.

## 4. General orbit: the missing observable is a second angular harmonic

For a positive measure of such rotated copies whose common phase has been chosen to align the `+` source, the aggregate is

\[
f_+^{tot}=f_+(0)\int d\mu(\phi),
\]

\[
f_-^{tot}=f_-(0)\int e^{2i\phi}d\mu(\phi).
\]

Therefore the normalized aggregate minority survival is controlled by

\[
\boxed{
Q_2(\mu)
=\frac{\int e^{2i\phi}d\mu(\phi)}{\int d\mu(\phi)}.}
\]

`|Q_2|` is the spin-2 azimuthal coherence of the parent-plane law around the child axis.

- `|Q_2|=1`: the edgewise minority source survives coherently;
- `Q_2=0`: it cancels completely although all `+` work atoms remain aligned.

## 5. Consequence for the proof architecture

CR + CO do **not** imply a mixed-polarization child state without an additional theorem controlling source geometry across atoms/times.  The exact remaining alternative is:

\[
\boxed{
\text{minority source survives}
\quad\text{or}\quad
\text{spin-2 azimuthal cancellation is active}.}
\]

This cancellation is a physical geometric/phase organization of many genuine NSE source atoms; it must not be relabeled as numerical cancellation or thrown away by absolute values.

The global CF critical-action criterion itself is unaffected, because the opposite-helicity recipient energy work of each pair event is a real separate modal state injection.  The no-go applies specifically to the attempted **fresh-source polarization attachment** route.

**Classification: EXACT NSE SYMMETRY / COUNTEREXAMPLE-NO-GO.**
