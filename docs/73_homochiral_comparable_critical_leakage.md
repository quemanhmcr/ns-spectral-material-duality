# A comparable homochiral split pays high-scale progress by downward critical-mass leakage

Status: **EXACT EVENT GEOMETRY / RIGOROUS COMPARABLE-SPLIT CONSEQUENCE**.

## 1. Exact critical-mass shares

Consider a homochiral one-donor split and choose the common sign positive.  Order the signed frequencies

\[
0<a<b<c,
\]

with donor `b`, low recipient `a`, high recipient `c`.  Put

\[
r=a/b,
\qquad
\lambda=c/b>1.
\]

The martingale split fractions are fixed by energy plus helicity conservation:

\[
p_h=\frac{b-a}{c-a}=\frac{1-r}{\lambda-r},
\qquad
p_l=\frac{c-b}{c-a}=\frac{\lambda-1}{\lambda-r}.
\]

For donor work `Q`, the donor critical mass is `bQ`.  The high-recipient critical-mass fraction is

\[
\boxed{
\rho_h
=\frac{cp_h}{b}
=\frac{\lambda(1-r)}{\lambda-r}<1,
}
\]

and the low-recipient share is exactly

\[
\boxed{
1-\rho_h
=\frac{ap_l}{b}
=\frac{r(\lambda-1)}{\lambda-r}.
}
\]

Their sum is one because homochiral splitting creates no total absolute helical critical mass.

## 2. Fully comparable geometry gives a quantitative leakage law

Let `K=c` be the largest physical frequency and assume the fully comparable branch

\[
a,b,c\ge K/4.
\]

Then `r=a/b>=lambda/4`, while `lambda-r<=lambda`.  Therefore

\[
\boxed{
1-\rho_h
\ge\frac{\lambda-1}{4}
\ge\frac14\log\lambda.
}
\]

Equivalently,

\[
\boxed{
\rho_h\le\lambda^{-1/4}.
}
\]

So actual upward scale progress of a same-helicity branch cannot retain all of its donor critical mass.  The missing share is not destroyed: it is the simultaneous lower recipient mandated by helicity conservation.

## 3. Split variance directly prices the leakage

The enstrophy split variance of this event is

\[
\mathcal V_\triangle
=Q(b-a)(c-b).
\]

The low-recipient critical-mass leakage is

\[
\mathcal L_\triangle
=Qap_l
=Qa\frac{c-b}{c-a}.
\]

Hence

\[
\frac{\mathcal V_\triangle}{\mathcal L_\triangle}
=\frac{(b-a)(c-a)}{a}.
\]

On the comparable branch `a>=K/4`, while both differences are at most `K`, so

\[
\boxed{
\mathcal L_\triangle
\ge\frac{\mathcal V_\triangle}{4K}.
}
\]

Thus comparable homochiral enstrophy production has a compulsory downward critical-mass compensation at the same physical event.

**Classification: RIGOROUS CONSEQUENCE OF EXACT SPLIT GEOMETRY.**

## 4. Scope

This is not yet a global bound on total downward critical-mass traffic.  It removes one false escape only: a comparable homochiral split cannot both create enstrophy and send a high branch upward without paying simultaneous lower-recipient critical mass.  Any later replenishment of the high branch must come from another physical event.
