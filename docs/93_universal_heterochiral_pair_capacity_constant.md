# Universal heterochiral pair-capacity coefficient is at most `4 sqrt(2) / 27`

Status: **RIGOROUS EXACT-GEOMETRY UPPER BOUND**.

## 1. Dimensionless coefficient

For heterochiral pair creation in normal form

\[
-b<a<c,
\qquad a,b,c>0,
\]

define

\[
K=\max\{b,c\}
\]

and the phase-saturated dimensionless pair-capacity coefficient

\[
\eta(a,b,c)
=
\frac{\sqrt2\,\Delta(a,b,c)(c-a)(a+c-b)}{acK^2}.
\]

CI gives

\[
P_\triangle
\le
\eta(a,b,c)K^2|a_0a_1a_2|.
\]

We prove

\[
\boxed{
\eta(a,b,c)\le\frac{4\sqrt2}{27}.}
\]

## 2. Case `K=c`

Scale `c=1` and write

\[
t=a/c\in(0,1),
\qquad
r=b/c\le1.
\]

Strict triangle geometry gives

\[
1-t<r<1+t.
\]

Using the elementary area bound

\[
\Delta\le\frac12ab
\]

gives

\[
\eta
\le
\frac{\sqrt2}{2}
r(1-t)(1+t-r).
\]

For fixed `t`, the quadratic `r(1+t-r)` has vertex at `(1+t)/2`.

### `t>=1/3`

The vertex lies in the allowed interval, hence

\[
\eta
\le
\frac{\sqrt2}{8}(1-t)(1+t)^2.
\]

The function `(1-t)(1+t)^2` decreases for `t>=1/3`, with value `32/27` at `t=1/3`.  Therefore

\[
\eta\le\frac{4\sqrt2}{27}.
\]

### `t<1/3`

The vertex lies below the lower triangle face `r=1-t`, so the maximum over the allowed interval is attained at that lower endpoint in the closure.  Hence

\[
\eta
\le
\sqrt2\,t(1-t)^2.
\]

This increases on `(0,1/3)` and again approaches `4sqrt(2)/27` at `t=1/3`.

## 3. Case `K=b`

Scale `b=1` and write

\[
t=a/b,
\qquad
r=c/b,
\]

so

\[
0<t<r\le1,
\qquad
t+r>1.
\]

Use

\[
\Delta\le\frac12ac.
\]

Then

\[
\eta
\le
\frac{\sqrt2}{2}(r-t)(t+r-1).
\]

Let

\[
x=r-t>0,
\qquad
y=t+r-1>0.
\]

Since

\[
x+y=2r-1\le1,
\]

AM--GM gives `xy<=1/4`, hence

\[
\eta\le\frac{\sqrt2}{8}
<\frac{4\sqrt2}{27}.
\]

The two cases exhaust `K=max(b,c)`.

**Classification: RIGOROUS CONSEQUENCE OF EXACT TRIAD GEOMETRY.**

## 4. Aggregate capacity improvement

For a dyadic comparable block with `K<2N`, one helical edge satisfies

\[
P_e
\le
\frac{16\sqrt2}{27}N^2|a_0a_1a_2|.
\]

Summing all helical choices at a fixed wavevector triple and using

\[
\prod_j(|a_{j,+}|+|a_{j,-}|)
\le2\sqrt2\,c_0c_1c_2
\]

gives

\[
\boxed{
P_N^{cmp}
\le
\frac{64}{27}N^2
\sum_{p,q}c_pc_qc_{-p-q}
\le
\frac{64}{27}N^2\|c\|_1\|c\|_2^2.}
\]

This strengthens CL/CR without changing their physical typing.
