# An old stopped parabolic-corridor population cannot carry the H1 blow-up rate

Status: **RIGOROUS MASS-FLOOR-FREE TERMINAL SECTOR EXCLUSION**.

Theorem AX used a scale-critical event floor to exclude terminal accumulation inside the corridor.  A stronger sector statement needs no per-event floor at all.

## 1. Standard H1 blow-up lower rate

The exact enstrophy work plus Sobolev/Gagliardo--Nirenberg gives

\[
Y'\le C_H\nu^{-3}Y^3,
\qquad
Y=\|\nabla u\|_2^2.
\]

If a maximal smooth solution has finite first singular time `T`, take a sequence `s_n upward T` with `Y(s_n)->infinity`.  Since

\[
\frac d{dt}Y^{-2}
=-2Y^{-3}Y'
\ge-2C_H\nu^{-3},
\]

letting `s_n -> T` gives

\[
\boxed{
Y(t)
\ge
c_H\nu^{3/2}(T-t)^{-1/2}
}
\]

with `c_H=(2C_H)^(-1/2)`.

This is the standard minimum `H^1` blow-up rate, derived only after the exact enstrophy owner is identified.

## 2. Old selected corridor mass decays too fast

Let `m_i` be a selected energy population initialized at time `s` and stopped at every corridor exit, with no incoming/reentry mass afterwards.  Suppose every alive state satisfies

\[
\alpha\le2\nu\kappa_i(T-t)\le\beta,
\qquad
\alpha>\frac12.
\]

Theorem AX gives

\[
M_m(t)
\le
M_m(s)
\left(\frac{T-t}{T-s}\right)^\alpha.
\]

Its enstrophy contribution is

\[
Y_m(t)=2\sum_i\kappa_im_i(t).
\]

The upper corridor face implies

\[
\boxed{
Y_m(t)
\le
\frac\beta{\nu(T-t)}M_m(t)
\le C_m(T-t)^{\alpha-1}.
}
\]

Compare with the necessary singular rate `Y(t)>=c_H nu^(3/2)(T-t)^(-1/2)`.  Then

\[
\boxed{
\frac{Y_m(t)}{Y(t)}
\le C(T-t)^{\alpha-1/2}
\longrightarrow0.
}
\]

Thus one old stopped matched-corridor population is asymptotically incapable of carrying the enstrophy required by a finite-time singularity.

**Classification: RIGOROUS TERMINAL SECTOR EXCLUSION.**

## 3. Consequence: terminal corridor activity requires fresh physical input

If matched-corridor enstrophy remains a non-negligible part of a candidate singular state near `T`, it cannot come only from one old selected population.  There must be arbitrarily late incoming mass through one of the exact faces in `docs/51_parabolic_corridor_reynolds_current.md`:

- nonlinear up-frequency reentry;
- one-time upper clock entry from the superparabolic sector;
- material/state relink supplying genuinely new selected ancestry.

The clock entry of one fixed mode is one-way and cannot recur by itself.  Therefore persistent terminal corridor activity reduces to actual nonlinear/relink input rather than survival of old corridor energy.

This result removes the uniform event-floor hypothesis from the statement “old corridor mass cannot itself be the singularity.”
