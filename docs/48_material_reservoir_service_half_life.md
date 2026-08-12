# A low-strain material reservoir cannot catalyze an indefinitely advancing scale at fixed efficiency

Status: **EXACT KELVIN COVECTOR KINEMATICS** plus a **RIGOROUS GALILEAN-INCREMENT SERVICE CONSEQUENCE**.  This is the catalyst-side complement to the donor-energy killed-lineage mechanism.

A quadratic NSE interaction has two structural parents, while the cyclic energy donor theorem shows that energy-donor ontology is different.  The second parent can act as a reservoir/catalyst without losing the same amount of modal energy.  Energy killing alone therefore cannot control indefinite reuse of that parent.

## 1. Same material reservoir has an exact covector fingerprint

Along an affine/material background,

\[
\dot L=AL,
\qquad
\dot k=-A^Tk,
\qquad
S=\frac12(A+A^T).
\]

Hence

\[
\boxed{L^Tk=\text{constant}}
\]

and

\[
\boxed{
\frac d{dt}\log|k|
=-\widehat k^TS\widehat k
\le\|S\|_{op}.
}
\]

If one material reservoir is reused over one generation with strain action

\[
\Sigma_j=\int_{I_j}\|S\|_{op}dt,
\]

its characteristic frequency can grow by at most

\[
\boxed{
M_{j+1}/M_j\le e^{\Sigma_j}.
}
\]

If this material fingerprint fails, the event is spectral/material relinking rather than free reuse.

## 2. Galilean cancellation makes low-frequency service decay with scale separation

Let the child/service scale be `N` and a low reservoir band be `M<=N`.  For a physical displacement `|r|~N^-1`, the exact increment identity and Bernstein give

\[
\|\delta_ru_M\|_2
\le |r|\|\nabla u_M\|_2
\lesssim\frac MN\|u_M\|_2.
\]

Thus its squared scale-critical increment service has the form

\[
\boxed{
\mathsf C(M,N)
\lesssim
\left(\frac MN\right)^2
\mu_M,
\qquad
\mu_M=M\|u_M\|_2^2,
}
\]

or equivalently, per unit physical reservoir energy,

\[
\boxed{
\mathsf C(M,N)
\lesssim
\frac{M^3}{N^2}E_M.
}
\]

The factor `(M/N)^2` is the physical statement that uniform large-scale sweeping does not create a small-scale velocity increment.

## 3. Scale progress outruns a low-strain old reservoir

Suppose the continuing child scale satisfies

\[
N_{j+1}/N_j\ge\lambda>1
\]

and the same material reservoir remains on low-strain episodes

\[
\Sigma_j\le\sigma.
\]

Even under the adversarial energy bound `E_{M_j}<=E_global`, its maximum service capacity obeys

\[
\frac{\mathsf C_{j+1}^{max}}{\mathsf C_j^{max}}
\le
\boxed{
\rho_{cat}:=\frac{e^{3\sigma}}{\lambda^2}.
}
\]

If

\[
\boxed{e^{3\sigma}<\lambda^2,}
\]

then

\[
\mathsf C_j^{max}\le \rho_{cat}^j\mathsf C_0^{max},
\qquad
\sum_j\mathsf C_j^{max}<\infty.
\]

Therefore one fixed material reservoir cannot provide a uniform positive service threshold to infinitely many advancing generations while remaining low-strain.

## 4. Infinite efficient catalyst reuse has only named exits

If a continuing event requires `C_j>=c_*>0` and scale continues to advance, an infinite reuse chain must eventually violate at least one premise:

1. **high strain:** `Sigma_j` becomes large enough for the material covector to track the cascade scale;
2. **relink/new ancestry:** the Kelvin fingerprint no longer identifies the same reservoir;
3. **fragmentation/spatial replication:** many distinct samples replace one material reservoir and require their own packing/source law;
4. **service failure:** the reservoir no longer supplies the required physical increment.

These are physical alternatives, not names invented to close a proof.

## 5. Relation to the new donor-energy mechanism

The killed-lineage theorem controls the energy-donor side of actual transfer.  This theorem controls a different loophole: repeated use of a non-donating or weakly donating low-frequency structural parent.

The two mechanisms should not be merged into one scalar currency:

\[
\boxed{
\text{donor energy}\to\text{viscous killing},
\qquad
\text{old catalyst service}\to\text{strain/relink/service half-life}.
}
\]

A full proof still has to derive the actual event/service threshold and route high-strain/relink/fragmentation exits globally.
