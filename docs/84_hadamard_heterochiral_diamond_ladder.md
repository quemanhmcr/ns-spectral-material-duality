# An exact Hadamard Fourier diamond is an adversary to topology-only termination

Status: **EXACT WAVENUMBER/HELICITY GEOMETRY + COUNTERMODEL TO EVENTWISE/TOPOLOGY-ONLY CLOSURE**.  This is not asserted to be an invariant Navier--Stokes subsystem and is not a blow-up solution.

## 1. Exact nested Fourier geometry

Take two nonzero orthogonal wavevectors with equal length,

\[
p_j\cdot q_j=0,
\qquad
|p_j|=|q_j|=N_j.
\]

Define

\[
\boxed{
p_{j+1}=p_j+q_j,
\qquad
q_{j+1}=p_j-q_j.}
\]

Then

\[
\boxed{
|p_{j+1}|=|q_{j+1}|=\sqrt2N_j,
\qquad
p_{j+1}\cdot q_{j+1}=0.}
\]

Moreover

\[
\boxed{p_{j+2}=2p_j,\qquad q_{j+2}=2q_j.}
\]

Starting from integer orthogonal lattice vectors therefore gives an infinite exact Fourier-lattice ladder.  No approximate shell geometry is used.

## 2. Helicity assignment

Assign helicity `+` to `p_j` and `-` to `q_j`.  Reality supplies the partner `-q_j` with the same helical sign in the repository convention.

Two physical closed triads are available:

\[
p_j+q_j=p_{j+1},
\qquad
p_j+(-q_j)=q_{j+1}.
\]

Choose the first high child in the `+` sector and the second in the `-` sector.  Their signed-frequency triples are, up to ordering,

\[
(-N_j,+N_j,+\sqrt2N_j)
\]

and its sign reverse.  Thus each is a fully comparable heterochiral split geometry of the exact type isolated by CA/CI.

## 3. Static split fractions are critical-mass amplifying

For the normal form `-N<N<sqrt(2)N`, the one-donor split fractions are

\[
p_h=\frac{2}{1+\sqrt2}=2(\sqrt2-1),
\]

\[
p_o=\frac{\sqrt2-1}{1+\sqrt2}
=(\sqrt2-1)^2=3-2\sqrt2.
\]

The high branch loses kinetic energy fraction because `p_h<1`, but its transferred critical mass is amplified by

\[
\boxed{
\sqrt2\,p_h
=4-2\sqrt2
\approx1.171572875>1.}
\]

The opposite-helicity sibling carries exactly the excess critical fraction

\[
\boxed{p_o=3-2\sqrt2.}
\]

This is the CA pair-creation identity in a self-similar lattice geometry.

## 4. Parabolic time is Zeno-compatible at the level of scale laws

Since `N_(j+1)=sqrt(2)N_j`, natural windows satisfy

\[
\sum_jN_j^{-2}
=N_0^{-2}\sum_j2^{-j}<\infty.
\]

Thus wavevector closure, energy/helicity split fractions, and parabolic scaling alone do not prohibit a finite-time infinite-depth ladder.

The kinetic energy carried by a fixed critical charge scales like `1/N_j` and is geometrically summable, while the critical charge itself need not decay.  This is exactly why the ordinary energy budget cannot close CF.

## 5. What the static geometry does not prove

The two split signs/rates cannot be prescribed independently in real Navier--Stokes.  Shared modal amplitudes, Waleffe phases, viscosity, all other convolution channels, and the birth phase of newly generated modes evolve together.

Therefore the decisive next question is dynamical:

> Does the actual Fourier--Galerkin NSE generate both first-generation helical children and then the next Hadamard generation with compatible phases, or do the coupled amplitudes force cancellation/merge before the ladder can renew?

The companion Action referee tests exactly this question on the full retained Galerkin nonlinear term.  A positive numerical signal is only an adversarial witness, never a proof of a cascade.
