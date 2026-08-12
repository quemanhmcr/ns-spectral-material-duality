# Enstrophy records force a radial boundary where net outward current beats half the tail viscous killing

Status: **EXACT NSE / RADIAL LAYER-CAKE CONSEQUENCE**.  No Littlewood--Paley estimate, packet selection, Young inequality, or material label is used.

## 1. Two exact layer-cake readings of the same physical state

Let

\[
F(R,t)=\Phi_\uparrow(R,t)-\Phi_\downarrow(R,t)
\]

be the **net** nonlinear kinetic-energy current across the radial Fourier boundary `|k|=R`, positive outward.  Theorems BC/BH give the exact nonlinear enstrophy moment

\[
\boxed{
\mathcal W_{ens}(t)
=
\int_0^\infty 2R\,F(R,t)\,dR.
}
\]

Now define the physical high-tail gradient stock

\[
G(R,t)
=
\sum_{|k|>R,s}|k|^2E_{k,s}(t).
\]

A second layer-cake identity is immediate:

\[
\boxed{
Z(t)=\|\Delta u(t)\|_2^2
=
\int_0^\infty 2R\,G(R,t)\,dR.
}
\]

Indeed each modal term `|k|^4E_k` equals

\[
|k|^2E_k\int_0^{|k|}2R\,dR.
\]

Thus enstrophy production and viscous palinstrophy are integrals over the **same radial control surfaces**, with respectively net nonlinear current and tail gradient stock as their densities.

## 2. Record growth forces a physical radial gate

At an enstrophy record-growth time,

\[
\frac12Y'(t)\ge0,
\]

and the exact NSE identity gives

\[
\mathcal W_{ens}(t)\ge\nu Z(t).
\]

Using Section 1,

\[
\int_0^\infty
2R\,[F(R,t)-\nu G(R,t)]\,dR
\ge0.
\]

Therefore there must exist at least one radius with nonzero tail stock for which

\[
\boxed{
F(R,t)
\ge
\nu G(R,t).
}
\]

But the actual viscous killing of the radial high set is

\[
D_R(t)=2\nu G(R,t).
\]

Hence the same condition is

\[
\boxed{
F(R,t)\ge\frac12D_R(t).
}
\]

**Physical meaning:** at every enstrophy record there is a spectral control surface across which the **net outward nonlinear energy current is at least one half of the instantaneous viscous killing of the entire high tail outside that surface**.

This is a pointwise-in-time PDE event, not an integrated norm threshold.

## 3. Why gross circulation cannot fake the gate

The gate uses

\[
F=\Phi_\uparrow-\Phi_\downarrow,
\]

not gross `Phi_up` alone.  Same-time cyclic traffic which crosses a radius in both directions cancels according to its actual effect on radial energy transport.  Consequently a large conservative gross-transfer loop cannot satisfy the gate merely by circulating mass; it must leave a positive net outward current at the chosen control surface.

This is exactly the radial information relevant to enstrophy growth.

## 4. Relation to the exact high-set stock law

For the same radial set,

\[
\frac d{dt}E_R
+2\nu G(R,t)
=F(R,t).
\]

At a record-gate radius,

\[
F\ge\nu G,
\]

so

\[
\frac d{dt}E_R
\ge-\nu G.
\]

The theorem does **not** assert that high-tail kinetic energy itself is increasing: actual killing may still exceed the net inflow.  The gate says instead that nonlinear outward transport is already paying at least half of that killing.  This distinction is essential and is why the theorem is not a disguised shell-growth criterion.

## 5. A PDE-facing radial first-bad candidate

At every record time the admissible set

\[
\mathcal R_{bad}(t)
=
\{R>0:G(R,t)>0,\ F(R,t)\ge\nu G(R,t)\}
\]

is nonempty.  On the periodic Fourier lattice, `F` and `G` are piecewise constant between modal radii, so the event may be registered on the deterministic radial mode-set filtration without inventing a free Boolean oracle.

This candidate has a different job from the highest-critical-shell selector BJ:

- **BJ:** supplies a scale-critical shell-energy floor, using one late LP estimate after the enstrophy-work owner is known;
- **BN:** supplies an exact net-current-versus-tail-killing event, with no LP estimate at all.

A future first-bad architecture may use both as typed coordinates rather than forcing one selector to encode both amplitude and transport.

## 6. Coupling to the subcritical-tail theorem

If a record-gate radius lies above the highest PDE-active shell, then the tail beyond that radius is critical-subthreshold.  Theorem BL says its pure self-interaction is viscosity-absorbable.  Therefore the outward current required by the radial gate must be supplied through external incidence/boundary physics.

If the gate radius lies at or below the active scale, the gate directly identifies the radial current that must be followed by the modal donor/recipient law.

Either way, the radial gate contains no new abstract currency: it is a physical control surface on the existing energy current.

No global-regularity or recurrence-termination conclusion is claimed.
