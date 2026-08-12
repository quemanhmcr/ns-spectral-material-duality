# Moving spectral cut: the time face is an exact physical term

Status: **Exact operator identity plus NSE Action calibration.**

The localized material-flux law contains

\[
(\partial_tQ+[u\cdot\nabla,Q])\omega.
\]

The two pieces have different meanings.  `[u.grad,Q]` is the mismatch between physical transport and the chosen spatial/spectral observer.  `partial_t Q` is the literal motion of the observer boundary itself.

To prevent these from being conflated, the CI calibration uses the smooth Fourier multiplier

\[
Q_t(k)=\exp\left[-\left(\frac{|k|}{N(t)}\right)^4\right],
\qquad
\frac{\dot N}{N}=\alpha.
\]

At the observation time,

\[
\boxed{
\dot Q_t(k)
=4\alpha\left(\frac{|k|}{N}\right)^4 Q_t(k).
}
\]

On a random smooth periodic divergence-free state, the experiment computes the instantaneous **full Navier--Stokes vorticity RHS**, then compares

\[
D_t(H^TQ_t\omega)
\]

with the classified source ledger.

With `Qdot` retained, the identity closes to floating-point precision.  If `Qdot` is deliberately omitted, the entire residual is exactly the missing time face.

This is not a numerical theorem about one cutoff.  It is a calibration of the exact product rule.  Its conceptual consequence is representation-independent:

\[
\boxed{
\text{moving localization} \Rightarrow \text{explicit time face}.
}
\]

Any quantile, shell, germ or packet boundary whose definition changes with physical time must either carry this term or prove that its chosen covariant motion makes it vanish.  A static spatial commutator alone is not exhaustive.
