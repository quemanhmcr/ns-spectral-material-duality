# Wang Gaussian non-affinity and Kelvin codeforming surface non-affinity start from the same normalized velocity-Hessian tensor

Status: **EXACT CROSS-UPSTREAM JET IDENTITY / PHYSICAL REPRESENTATION DICTIONARY**.

This note uses current Wang and current Kelvin results as read-only upstream inputs.  It does not replace either packet or material-current construction.

## 1. Wang's grain-normalized curvature tensor

For a physical Gaussian grain

\[
x=X+Lz,
\]

current Wang defines

\[
H_{ijk}=\partial_j\partial_k u_i(X)
\]

and

\[
\boxed{
B_{abc}
=(L^{-1})_{ai}H_{ijk}L_{jb}L_{kc}.
}
\]

The quadratic velocity remainder is

\[
R_2(X+Lz)
=\frac12L\,B[z,z].
\]

After the full center/carrier/covariance/chirp tangent quotient, Wang proves that only the full symmetric part enters the first genuine transverse packet-shape forcing:

\[
\boxed{
\frac{\|F_\perp\|_2^2}{\|\psi\|_2^2}
=\frac38\|\operatorname{Sym}B\|_F^2.
}
\]

## 2. Kelvin's codeforming quadratic jet is the identical tensor

Current Kelvin defines the codeforming homogeneous jet

\[
\mathfrak J_p(L)
=L^{-1}(\nabla^pu)L^{\otimes p}.
\]

At `p=2`, componentwise,

\[
(\mathfrak J_2)_{abc}
=(L^{-1})_{ai}(\partial_j\partial_ku_i)L_{jb}L_{kc}.
\]

Therefore

\[
\boxed{
\mathfrak J_2(L)=B
}
\]

**exactly, index by index.**

This is not a norm comparison and not a similarity of scaling.  The two upstream constructions use the same affine-covariant physical Hessian tensor.

## 3. Kelvin's codeforming nonaffinity field starts with the same `B`

The exact Kelvin codeforming residual field is

\[
\mathcal N_L(\xi)
=L^{-1}[u(X+L\xi)-u(X)-A_0L\xi].
\]

Taylor expansion at a smooth state gives

\[
\boxed{
\mathcal N_L(\xi)
=\frac12B[\xi,\xi]
+\frac1{3!}\mathfrak J_3(L)[\xi,\xi,\xi]
+\cdots.
}
\]

Thus for a purely quadratic nonaffine jet,

\[
\boxed{
\mathcal N_L(\xi)=\frac12B[\xi,\xi],
\qquad
D_\xi\mathcal N_L(\xi)=B[\,\cdot\,,\xi].
}
\]

The same `B` drives both relative-position transport and the oriented-area source in Kelvin's full moment tower.

## 4. The two programmes take different quotients of the same tensor

The equality `B=J_2(L)` does **not** mean the observables are equal.

Wang's Gaussian manifold treats:

- quadratic phase/chirp as tangent;
- linear center/carrier changes as tangent;
- only the third-Hermite part as genuine packet-shape exit.

Hence the first transverse packet defect sees only

\[
\operatorname{Sym}B.
\]

Kelvin's codeforming material surface is not quotienting by the same Gaussian tangent manifold.  Its residual velocity and moment tower use the full tensor

\[
B.
\]

Therefore the exact dictionary is

\[
\boxed{
\text{common physical nonaffine jet }B
\longrightarrow
\begin{cases}
\operatorname{Sym}B & \text{Wang third-Hermite packet exit},\\
B & \text{Kelvin codeforming shape transport}.
\end{cases}}
\]

The difference is representation/quotient semantics, not different PDE curvature.

## 5. Exact quadratic heat-shear calibration

Take the exact smooth Navier--Stokes heat shear already used by Kelvin,

\[
\boxed{u=(y^2+2\nu t,0,0).}
\]

Advection vanishes and

\[
\partial_tu-\nu\Delta u=0.
\]

At anchor `y=0`, with `L=I`, the affine gradient vanishes and the only nonzero Hessian component is

\[
B_{122}=2
\]

(using one-based physical indices).  Hence

\[
\mathcal N_I(\xi)=(\xi_2^2,0,0),
\]

while

\[
\operatorname{Sym}B\ne0.
\]

Thus the **same exact NSE nonaffinity event** simultaneously activates:

- Wang's genuine third-Hermite packet-shape channel;
- Kelvin's codeforming nonaffinity/moment-tower channel.

No temporal matching or norm inference is required.
