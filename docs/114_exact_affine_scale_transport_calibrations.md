# Exact affine Navier--Stokes calibrations separate radial phase transport from metric work

Status: **EXACT NS CALIBRATION / NO-GO AGAINST SCALE-MOTION-AS-SOURCE**.

## 1. Pure strain base flow

Take

\[
A=S=\operatorname{diag}(a,-a,0),
\qquad u(x)=Ax,
\]

with the quadratic pressure from Theorem DY.  This is an exact smooth affine Navier--Stokes solution.

A transported wavefront covector obeys

\[
\dot k=-Sk,
\]

so

\[
k(t)=(e^{-at}k_1(0),e^{at}k_2(0),k_3(0)).
\]

For `k(0)=e_1`,

\[
\boxed{|k(t)|=e^{-at}|k(0)|.}
\]

There is genuine radial spectral/phase-scale motion under a conservative transport characteristic.

## 2. Rigid rotation base flow

Take the exact affine rigid rotation

\[
A=\Omega=\begin{pmatrix}0&-r&0\\r&0&0\\0&0&0\end{pmatrix}.
\]

Then

\[
\dot k=\Omega k
\]

and

\[
\boxed{|k(t)|=|k(0)|.}
\]

The connection rotates wavefront orientation without radial scale motion.

## 3. Material area follows the identical two calibrations

A material area Hodge vector `n` obeys the same `-A^T` law, so pure strain changes its magnitude by the same directional rate and rigid rotation preserves it.

This is a literal Wang/Kelvin geometric identity, not a shell-model analogy.

## 4. No-go

Because scalar incompressible transport conserves total `L^2` while pure strain can change `|k|`, no theorem may infer positive physical energy work solely from an observed radial wavefront drift.

Actual radial **energy current** requires the transported energy measure; actual symmetric **metric work** requires contraction with the fiber strain operator.  Those are distinct typed observables.
