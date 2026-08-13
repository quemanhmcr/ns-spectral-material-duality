# Kelvin first-bad selector inherits a sharp Cartan acceptance test without becoming an Eulerian role

Status: **EXACT TYPING CONSEQUENCE / OPEN STATE-MAP BRIDGE / NO-GO AGAINST SILENT SELECTOR CONNECTION**.

The projector theorem of Theorem DQ is representation-independent, but applying it to Kelvin requires the correct current/germ state and connection.  This note records exactly what can and cannot be concluded from current upstream semantics.

## 1. The literal Kelvin selector remains current-side

Current Kelvin's orientation-complete first-bad selector has the form

\[
M_{fb}\otimes I_3
\]

on germ/current coefficient space.  It is not an Eulerian Fourier projector and is not identified with Wang's `P` or smooth `Q`.

Therefore no equation of the form

\[
\dot M_{fb}=[K_{Euler},M_{fb}]
\]

may be asserted without a state/connection map.

## 2. Pure orientation connection commutes with the orientation-complete selector

On the tensor-product current space, a pure common orientation connection has the form

\[
K_{ori}=I_{germ}\otimes\Omega,
\qquad \Omega^T=-\Omega.
\]

Then

\[
\boxed{
[K_{ori},M_{fb}\otimes I_3]=0.
}
\]

On an unresolved hysteretic interval current Kelvin has

\[
\dot M_{fb}=0.
\]

Hence the Cartan defect with respect to the pure orientation sector is exactly zero:

\[
\boxed{
G_{fb}^{ori}
=\dot M_{fb}-[K_{ori},M_{fb}\otimes I_3]=0.
}
\]

This re-derives geometrically why there is no fictitious continuous "first-bad orientation motion" owner between selector events.

## 3. Germ-mixing connection is a separate question

A more general current-space skew connection can contain germ mixing,

\[
K_{cur}=K_{germ}+I_{germ}\otimes\Omega.
\]

Then

\[
G_{fb}^{cur}
=-[K_{germ},M_{fb}]\otimes I_3
\]

on a hysteretic interval with `dot M_fb=0`.

Therefore a nonzero continuous selector/interface face is possible **only if the actual physical current connection mixes selected and unselected germ sectors**.

Current Kelvin must identify that connection on the literal physical state before such a term can be charged.

## 4. Finite first-bad/resolve transitions remain finite events

When `M_fb` changes at an entry/resolve event, Theorem DQ does not smear the transition into a smooth density.  The selected quadratic state has the exact finite jump

\[
\Delta E
=\frac12\langle y,[(M_{fb}^+-M_{fb}^-)\otimes I_3]y\rangle.
\]

The existing repo-3 cubic selector theorem supplies the analogous exact finite jump for the interaction observable.

Thus Kelvin selector semantics remain:

- no continuous orientation face on a hysteretic plateau;
- possible current/germ interface face only after a literal connection is identified;
- finite entry/resolve reset at selector jumps.

## 5. Acceptance test for a future Wang/Kelvin selector identification

Any proposed state-map bridge must prove, not assume:

1. the target current-space skew generator `K_cur`;
2. descent/pullback of the physical selector through the state map;
3. the equality of the selector defect
   \[
   G=\dot P-[K,P]
   \]
   under that map;
4. preservation of finite jump semantics.

Only then may Wang moving-role interface and Kelvin first-bad selector faces be called the same physical source.
