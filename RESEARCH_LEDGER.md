# Research ledger

## Epistemic labels

- `EXACT`: derived directly from finite-dimensional algebra, continuum kinematics, or NSE identities under stated hypotheses.
- `RIGOROUS CONSEQUENCE`: theorem following from exact identities plus explicitly stated external hypotheses.
- `ACTION`: numerical/adversarial CI calibration only.
- `OPEN`: bridge not yet proved.
- `NO-GO`: exact obstruction to a tempting identification.

## 2026-08-12 — initial bridge

### EXACT — advected covector dictionary

Fourier Kelvin carriers and material area normals obey the same `F^{-T}` transport. Affine Fourier phase planes are material surfaces.

### EXACT — dual metric dictionary

`M=F^T F` controls material geometry while `M^{-1}` controls advected Fourier covector lengths.

### EXACT — strain from metric velocity

`H Mdot H^T = 2S` for `H=F^{-T}`.

### EXACT — objective strain from metric acceleration

`S_objective = (1/2) H Mddot H^T - (1/2)(H Mdot H^T)^2` with the corotational convention recorded in the dictionary note.

### EXACT — triad Hodge coordinates from inverse material metric

For an initially symmetric extremal triad, `u,v` are explicit logarithmic functions of `n_j^T M^{-1} n_j`.

### RIGOROUS CONSEQUENCE — local metric anisotropy costs spectral extremality

Combining the metric dictionary with the certified local single-edge and affine-strain inequalities gives the local condition-number lower bound recorded in `docs/01_common_deformation_dictionary.md`.

### EXACT — noncommuting strain produces common holonomy

The second-order commutator rotation in objective spectral polarization is the leading polar rotation of the same ordered material deformation.

### EXACT — metric velocity determines local helicity conversion

The transverse symmetric generator `E^T S E` equals one half the restriction of `H Mdot H^T`; in the circular basis its trace-free part gives the off-diagonal helicity-conversion coefficient.

### NO-GO — metric-only signed work closure

At fixed geometry, helicities and modal magnitudes, varying only child phase makes direct physical edge work attain positive, zero and negative values. See `docs/03_metric_phase_no_go.md`.

### ACTION — run 31576094866

GitHub Actions passed all three initial experiment modules on commit `2b5fdf5`.

Key calibrations:

- metric/direct parent-ratio residual `4.44e-16`;
- sampled local `Def/H` minimum `3.86999` (the certified theorem only requires `>=1/2` in its region);
- polar holonomy at `b=d=1, eps=.1`: `0.569140889°`, second-Magnus leading value `0.572957795°`;
- metric-velocity/helicity-conversion residual `8.88e-16`;
- fixed-metric phase sweep edge work: `[-0.7988680113,+0.7988680113]`, with sampled zero `4.89e-17`.

## Current frontier

### OPEN — phase dictionary

Find a gauge-invariant material/Kelvin-side observable that reconstructs the relative phase factor entering the direct Fourier–Leray helical edge law, or prove a no-go theorem for a natural class of local material observables.

### OPEN — nonlinear transport dictionary

Determine whether a material-current observable can distinguish positive forward spectral work from backscatter without importing a Fourier shell label by definition.

### OPEN — viscous scale bridge beyond monochromatic shells

Quantify the exact annular constants relating orientation-complete Kelvin q.v. density to scale-normalized Fourier-shell viscous payment without identifying smooth LP and hard projections.

## 2026-08-12 — Oriented flux and localized PDE bridge

- **EXACT:** For one helical edge, signed child-energy work equals a frequency/helicity coefficient times the GL(3)-invariant oriented material vorticity-flux 3-form `det(H)^(-1) Re(conj(Phi_q) . (Phi_1 x Phi_2))`.
- **NO-GO REFINED:** Metric/covariance alone cannot determine signed work because they are second-order; the missing information is genuinely third-order oriented flux information.
- **EXACT:** For `Phi_Q=H^T Q omega`, `D_t Phi_Q = H^T[(partial_t Q+[u.grad,Q])omega +(Q A-A Q)omega + nu Q Delta omega]`.
- **EXACT:** For `Q=I`, both localization commutators vanish and only the Kelvin/Nanson viscous flux remains.
- **EXACT:** The oriented cubic flux derivative splits linearly into interface/moving-cut, strain-selection, and viscosity terms; passive material-frame motion is not an additional source.
- **OPEN:** Instantiate this identity for the literal smooth/hard Fourier roles and literal Kelvin germ/quantile roles, then compare their physical source partitions without importing upstream closure claims.

- **EXACT / CALIBRATED:** A time-dependent role `Q(t)` carries the explicit time face `partial_t Q`.  Smooth moving-cut Action calibration shows that omitting it leaves exactly that residual; it cannot be hidden in `[u.grad,Q]`.

- **EXACT:** The full complex invariant `Z_H=det(H)^(-1) conj(Phi_3).(Phi_1 x Phi_2)` carries both signed-work quadrature and the gauge-invariant interaction phase `arg Z_H`.
- **EXACT SMALL-LOOP:** `Z_H` is the limit of the determinant-normalized oriented triple product of three role-filtered Kelvin circulation vectors on an orientation-complete small-loop packet.
- **EXACT:** Where `Z_H != 0`, phase velocity is `D_t arg Z_H = Im[(D_t Z_H)/Z_H]`; the localized PDE source decomposition therefore induces a phase-velocity decomposition without inventing a separate phase budget.
