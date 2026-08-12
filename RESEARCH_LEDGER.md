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
