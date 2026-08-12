# Radial high-tail memory erosion: every late critical shell needs fresh upward energy funding

Status: **EXACT MODE-SET NSE CONSEQUENCE / RIGOROUS FRESH-FUNDING THEOREM**.  This theorem uses the persistent object that the current Wang mode-set theorem identifies literally: Fourier--helical modal kinetic energy.  No packet persistence, FIFO/LIFO pairing, or synthetic reset is introduced.

## 1. Start from the physical radial control volume

For a radius `R>0`, let

\[
A_R=\{(k,s): |k|\ge R\}
\]

be the high Fourier--helical mode set and write

\[
E_R(t)=\sum_{(k,s)\in A_R}E_{k,s}(t).
\]

Let

\[
\Phi_\uparrow(R,t)=\mathcal F_t(A_R^c\times A_R),
\qquad
\Phi_\downarrow(R,t)=\mathcal F_t(A_R\times A_R^c)
\]

be the actual same-time nonlinear energy current crossing the radial boundary upward and downward.  Current Wang `ae85f4d` gives the exact mode-set continuity law

\[
\boxed{
\frac d{dt}E_R
+
2\nu\sum_{(k,s)\in A_R}|k|^2E_{k,s}
+
\Phi_\downarrow(R,t)
=
\Phi_\uparrow(R,t).
}
\]

This is a physical stock/flux/killing equation.  Internal high--high donor traffic cancels from the set boundary exactly; it is not discarded from the PDE.

## 2. Viscosity gives an exact one-sided memory inequality

Every mode in `A_R` has `|k|^2\ge R^2`.  Hence

\[
2\nu\sum_{A_R}|k|^2E_{k,s}
\ge
2\nu R^2E_R.
\]

Since `Phi_down>=0`, the exact continuity equation implies

\[
\boxed{
\frac d{dt}E_R+2\nu R^2E_R\le \Phi_\uparrow(R,t).
}
\]

Multiplying by the integrating factor gives, for every `L>0` with `t-L>=0`,

\[
\boxed{
E_R(t)
\le
e^{-2\nu R^2L}E_R(t-L)
+
\int_{t-L}^{t}
e^{-2\nu R^2(t-s)}\Phi_\uparrow(R,s)\,ds.
}
\]

This is not an estimate on gross nonlinear transfer.  It is the causal statement that old energy already inside the radial high set is exponentially erased unless actual nonlinear energy crosses the radial boundary into that set.

**Classification: RIGOROUS CONSEQUENCE OF EXACT NSE MODE-SET CONTINUITY.**

## 3. A critical shell forces fresh upward radial work

Let `C_N` be a hard shell whose lower frequency edge is at least `rho N`, with fixed `rho>0`, so that

\[
C_N\subset A_{\rho N}.
\]

Suppose at time `t`

\[
\boxed{N E_{C_N}(t)\ge\eta>0.}
\]

Then with `R=rho N`,

\[
E_R(t)\ge\frac\eta N.
\]

Let

\[
E_*=\sup_{0\le s<T}\|u(s)\|_2^2,
\]

which is bounded by the ordinary unforced NSE energy law.  Define

\[
\boxed{
L_N=
\frac{1}{2\nu\rho^2N^2}
\log\!\left(\frac{2E_*N}{\eta}\right)
}
\]

whenever the logarithm is positive.  Then

\[
e^{-2\nu(\rho N)^2L_N}E_R(t-L_N)
\le
\frac\eta{2N}.
\]

Therefore, whenever `t>=L_N`, the terminal critical shell forces

\[
\boxed{
\int_{t-L_N}^{t}
e^{-2\nu\rho^2N^2(t-s)}
\Phi_\uparrow(\rho N,s)\,ds
\ge
\frac\eta{2N}.
}
\]

At least half of the terminal critical energy is thus **freshly funded across the actual radial boundary**, after old high-tail stock has been discounted by its physical viscous survival.

No temporal pairing of individual deposits is needed.  The theorem uses only the radial control-volume current and the exact viscous killing inside it.

## 4. The funding window is asymptotically shorter than a logarithmic number of natural times

As `N->infinity`,

\[
\boxed{L_N=O\!\left(\frac{\log N}{\nu N^2}\right)\to0.}
\]

Hence if a candidate singular path contains critical shells `N_j->infinity` at times `t_j->T`, their required upward funding occurs on windows whose left endpoints also approach `T`.

This is stronger than saying that some total outward spectral work exists near a record time: it localizes an actual positive radial energy current to the physical scale supporting the critical shell.

## 5. Why this does not resurrect a finite gross-work budget

The theorem does **not** claim

\[
\int\Phi_\uparrow<\infty
\]

uniformly over all radii or all repeated passages.  Current Wang correctly gives an anti-theorem against bounding total gross internal transfer by kinetic-energy stock.

The statement is instead local and causal:

> a late high-frequency critical shell cannot be merely ancient high-frequency stock; viscosity forces a definite fraction of its present energy to have crossed in recently through a radial mode boundary.

What happens to that incoming physical work is a separate owner question: comparable generation, nonlocal high-companion transfer, resolved interface/strain, source, relink, or material renewal.

## 6. Relation to the subparabolic seam

This theorem removes the need to prove a full forward lifespan merely to show that a subparabolic critical shell is physically active.  A shell with the PDE-derived record floor from Theorem BA/BJ already forces recent upward radial work on the window above.

Thus the remaining `S` question is no longer

> can a critical shell silently sit below the heat scale until singularity?

It becomes

> which actual owner supplies the fresh radial current that viscosity requires?

The companion tail-self-absorption theorem answers the autonomous-tail part of that question.

No global-regularity conclusion is claimed.
