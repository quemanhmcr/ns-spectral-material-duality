# Full Cauchy payoff separates common deformation from terminal and mixed resolution

Status: **Exact conditional Cauchy / cubic-resolution factorization.**

The previous exterior-volume theorem fixed the terminal interaction vectors and
isolated the defect created by averaging a common stochastic deformation before
forming the cubic.  Actual Cauchy payoffs are richer:

\[
Y_i=D\,w_i,
\]

where `D` and the terminal/role vector `w_i` live on the same hidden stochastic
state and can be correlated.  This note keeps that correlation instead of replacing
it by a norm or an independence assumption.

---

## 1. Common Cauchy deformation cancels pathwise even for random terminal vectors

Let `D` be real with

\[
\det D=1
\]

pathwise and let `w_i` be arbitrary complex random vectors on the same probability
space.  Then

\[
\boxed{
\mathcal T(Dw_0,Dw_1,Dw_2)
=\mathcal T(w_0,w_1,w_2)
}
\]

pathwise.  Therefore

\[
\boxed{
\mathcal Z_{\rm same}
:=\mathbb E\mathcal T(Y_0,Y_1,Y_2)
=\mathbb E\mathcal T(w_0,w_1,w_2).
}
\]

**Classification: EXACT STOCHASTIC CAUCHY / MATERIAL 3-FORM IDENTITY.**

Thus stochastic variation of a **common** incompressible Cauchy deformation is not
present in the same-replica cubic at all.  Its metric anisotropy and deformation
covariance remain physically real, but the top exterior interaction quotients them
exactly.

---

## 2. Current mean legs contain a separate deformation--terminal correlation

Define

\[
\bar D=\mathbb ED,
\qquad
\bar w_i=\mathbb Ew_i,
\]

and fluctuations

\[
\delta D=D-\bar D,
\qquad
\eta_i=w_i-\bar w_i.
\]

The current mean Cauchy leg is

\[
m_i:=\mathbb E[D w_i].
\]

Expanding gives exactly

\[
\boxed{
m_i=\bar D\,\bar w_i+r_i,
\qquad
r_i:=\mathbb E[(\delta D)\eta_i].
}
\]

The vector `r_i` is a literal mixed deformation--terminal correlation.  It is not
contained in `Sigma_D` alone and is not a centered covariance of the final Cauchy
payoff alone.

**Classification: EXACT MIXED-RESOLUTION IDENTITY.**

---

## 3. Exact three-owner factorization of the same-state / independent-mean cubic gap

Set

\[
B_i:=\bar D\,\bar w_i,
\qquad
\mathcal Z_{\bar w}:=\mathcal T(\bar w_0,\bar w_1,\bar w_2),
\]

and define the terminal hidden-state cubic resolution

\[
\boxed{
\Delta_w
:=\mathbb E\mathcal T(w_0,w_1,w_2)-\mathcal Z_{\bar w}.
}
\]

The independent-mean cubic is

\[
\mathcal Z_{\rm ind}=\mathcal T(m_0,m_1,m_2).
\]

By trilinearity,

\[
\mathcal Z_{\rm ind}
=\det(\bar D)\mathcal Z_{\bar w}
+\mathcal C_{D-w},
\]

where the exact mixed correlation polynomial is

\[
\boxed{
\begin{aligned}
\mathcal C_{D-w}={}&
\mathcal T(r_0,B_1,B_2)
+\mathcal T(B_0,r_1,B_2)
+\mathcal T(B_0,B_1,r_2)\\
&+\mathcal T(r_0,r_1,B_2)
+\mathcal T(r_0,B_1,r_2)
+\mathcal T(B_0,r_1,r_2)
+\mathcal T(r_0,r_1,r_2).
\end{aligned}
}
\]

Consequently

\[
\boxed{
\mathcal Z_{\rm same}-\mathcal Z_{\rm ind}
=(1-\det\bar D)\mathcal Z_{\bar w}
+\Delta_w
-\mathcal C_{D-w}.
}
\]

**Classification: EXACT CONDITIONAL CUBIC FACTORIZATION.**

No estimate appears.  The apparent complexity has reduced to three typed owners:

1. `1-det bar D`: common-deformation exterior-volume resolution;
2. `Delta_w`: terminal/role same-state cubic resolution;
3. `C_{D-w}`: deformation--terminal correlation resolution.

---

## 4. Only the first owner is forced to be radial

The first term

\[
(1-\det\bar D)\mathcal Z_{\bar w}
\]

is a real scalar multiple of the terminal mean cubic.  While `det bar D>0`, it is
an amplitude-resolution term and not a continuous phase source.

The other two terms are genuinely complex.  They need not be collinear with
`Z_barw`, so either can rotate the interaction phase.

Therefore, after common Cauchy deformation is quotiented, the first stochastic
mechanisms capable of rotating phase are not `Sigma_D` or the packet metric by
themselves.  They are

\[
\boxed{
\text{terminal/role cubic resolution}
\quad\text{and}\quad
\text{deformation--terminal correlation}.
}
\]

**Classification: RIGOROUS CONSEQUENCE / OWNER IDENTIFICATION.**

---

## 5. Exact sufficient interaction data at one conditional state

For this common-Cauchy sector, both same-state and independent-mean cubics are
reconstructed exactly from

\[
\boxed{
(\bar D,\ \bar w_0,\bar w_1,\bar w_2,\ r_0,r_1,r_2,\ \Delta_w).
}
\]

The full deformation covariance `Sigma_D` remains essential for the evolution and
metric-spread problem, but it is not by itself the missing algebraic statistic for
signed cubic interaction.  The mixed correlations `r_i` and the third-order
terminal resolution `Delta_w` are different data types.

This is an interaction-sufficiency statement for the displayed Cauchy algebra, not
a claim that these quantities close dynamically without their own PDE/source laws.

**Classification: EXACT ALGEBRAIC SUFFICIENCY; dynamic closure remains OPEN BRIDGE.**

---

## 6. Relation to localized Navier--Stokes roles

For role-filtered Navier--Stokes legs, `w_i` can contain hard/smooth localization,
helical marks, terminal event data, or source/Duhamel contributions.  Those roles
need not share a homogeneous Cauchy evolution.  The exact factorization says what
must happen before any estimate:

- quotient the common real `SL(3)` deformation;
- retain terminal/role hidden-state cubic resolution;
- retain mixed deformation--terminal correlations;
- then add explicit localization, viscosity, nonlinear forcing, clock/interface,
  and reset owners from the earlier PDE ledger.

No term may be silently renamed covariance or phase loss.
