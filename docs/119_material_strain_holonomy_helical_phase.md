# Wang helical geometric-phase commutator is the circular-basis image of material strain holonomy

Status: **EXACT TRANSVERSE COMMUTATOR DICTIONARY / EXACT AFFINE NSE CALIBRATION**.

Current Wang already identifies noncommuting objective transverse strain as a local helical geometric-phase mechanism.  Repo 3 already identifies noncommuting material strain with polar holonomy.  This note proves that, on the common transverse state, these are the same commutator in two bases.

## 1. Trace-free transverse material metric velocity

From Theorem EL, after carrier-radius and viscous scalar factors are removed, Wang's objective transverse polarization satisfies

\[
\dot{\widetilde U}=-D(t)\widetilde U,
\]

where

\[
D(t)=\operatorname{tf}(E^TSE)
=\begin{pmatrix}
\delta(t)&\beta(t)\\
\beta(t)&-\delta(t)
\end{pmatrix}.
\]

The same matrix is the trace-free transverse restriction of material metric velocity:

\[
D=\operatorname{tf}\left(\frac12E^TH\dot MH^TE\right).
\]

## 2. Exact commutator is a real polar-rotation generator

For two times/states,

\[
D_j=\begin{pmatrix}\delta_j&\beta_j\\\beta_j&-\delta_j\end{pmatrix},
\]

direct multiplication gives

\[
\boxed{
[D_1,D_2]
=2(\delta_1\beta_2-\beta_1\delta_2)
J,
\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
}
\]

Thus the noncommutativity of two symmetric metric-deformation states is a skew generator.  Its coefficient is the oriented area of the two anisotropy vectors

\[
(\delta_1,\beta_1),\qquad(\delta_2,\beta_2).
\]

This is exactly the local material strain-holonomy generator already present in repo 3.

## 3. Circular/helical basis turns the same rotation into opposite phases

Let

\[
e_+=\frac1{\sqrt2}\binom{1}{i},
\qquad
e_-=\frac1{\sqrt2}\binom{1}{-i},
\]

and let `C=(e_+,e_-)`.  Then

\[
\boxed{C^*JC=\operatorname{diag}(i,-i).}
\]

Consequently

\[
\boxed{
C^*[D_1,D_2]C
=2i(\delta_1\beta_2-\beta_1\delta_2)
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
}
\]

The real polar rotation of material geometry is therefore the same object that Wang reads as opposite phase rotation of the two circular/helical polarizations.

There are not two phase mechanisms here.

## 4. Common transverse frame rotation leaves the coefficient invariant

Under a common `SO(2)` change of transverse frame,

\[
D_j\mapsto R^TD_jR.
\]

Then

\[
[D_1,D_2]\mapsto R^T[D_1,D_2]R.
\]

Because `R^TJR=J` for `R in SO(2)`, the scalar

\[
\boxed{\chi=\delta_1\beta_2-\beta_1\delta_2}
\]

is invariant under common objective transverse rotation.

Thus the local holonomy/helical-phase coefficient is not a frame-spin artifact.

## 5. Exact affine Navier--Stokes realization

Take

\[
u(x,t)=S(t)x,
\]

with

\[
S(t)=\begin{pmatrix}
d&\gamma t&0\\
\gamma t&-d&0\\
0&0&0
\end{pmatrix}.
\]

This field is divergence free, symmetric-gradient, and harmonic in space.  Set the quadratic pressure Hessian

\[
\boxed{\nabla^2p=-\dot S-S^2.}
\]

Since `Sdot+S^2` is symmetric,

\[
\partial_tu+(u\cdot\nabla)u+\nabla p=0,
\qquad \Delta u=0.
\]

Therefore this is an exact smooth affine Navier--Stokes solution.

The carrier `k=e_3` obeys

\[
\dot k=-S^Tk=0,
\]

so its transverse plane is fixed and

\[
D(t)=\begin{pmatrix}d&\gamma t\\\gamma t&-d\end{pmatrix}.
\]

For `t_1,t_2`,

\[
[D(t_1),D(t_2)]
=2d\gamma(t_2-t_1)J.
\]

This gives an exact NSE realization of nonzero material/helical commutator curvature without invoking a numerical shell model.

## 6. Exact second-Magnus face, not a full-holonomy truncation

For

\[
\dot{\widetilde U}=-D(t)\widetilde U,
\]

the second Magnus term is exactly

\[
\Omega_2(T)
=\frac12\int_0^Tdt_1\int_0^{t_1}dt_2\,[D(t_1),D(t_2)].
\]

For the affine family above,

\[
\boxed{
\Omega_2(T)=-\frac{d\gamma T^3}{6}J.
}
\]

In the circular basis this is

\[
\boxed{
C^*\Omega_2C
=\operatorname{diag}\left(-i\frac{d\gamma T^3}{6},
+i\frac{d\gamma T^3}{6}\right).
}
\]

This statement identifies the exact second-Magnus commutator face.  It does **not** assert that higher Magnus terms vanish or that this local phase is a global transfer/recurrence cost.

## 7. Bridge meaning

The common object is

\[
\boxed{
\text{noncommuting trace-free material metric velocity}
\longleftrightarrow
\text{real polar holonomy generator}
\longleftrightarrow
\text{opposite helical phase generator}.
}
\]

Wang's helical phase and repo-3/Kelvin material holonomy are thus two coordinate readings of one local geometric fact.
