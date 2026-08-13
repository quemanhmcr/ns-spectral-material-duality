# Inherited carrier stock is not selector path variation: two memory types and a simultaneous-owner no-go

Status: **RIGOROUS CROSS-PROGRAM CONSEQUENCE + EXACT NSE CALIBRATION + COUNTEREXAMPLE/NO-GO**.

The comparison begins from the physical owners, not from the fact that several
quantities happen to be nonnegative.

Latest upstream snapshots are used read-only:

- Wang `c2641bbecb8c12d8a75f0acca83556bbbefd5a9c`;
- Kelvin `9bc8fb01454084861f85e3c7e99683d2dad029e1`.

No upstream write is made.

---

## 1. Wang: inherited energy is a same-carrier stock amount, not fresh generation

On Wang's current same-carrier relay branch the physical carrier is the same shell
map at successive registered stages.  The stock amount is the carrier energy

\[
\mathcal E_M(u)=\int_{\mathbb T^3}|P_Mu|^2\,dx.
\]

When the earlier output and later input are literally the same physical carrier
state, the inherited amount is the same:

\[
\boxed{\mathcal E_{\rm late}=\mathcal E_{\rm prev}.}
\]

The corresponding inheritance quotient is therefore one on that **stock component**.
The upstream theorem explicitly gives this inherited component generation depth zero:
it is not reclassified as a fresh positive-work injection merely because it is
present at the later stage.

But the same stage can carry other physical owners.  In Wang's ledger the classified
residual owner

\[
\mathcal T_j
=\mathcal E_j\mathcal W_j+\mathcal N_j+\mathcal V_j
\]

is kept separate, as are material sidecars.  Current upstream deliberately rejects a
stock-only quotient when the classified residual work is not negligible.

Thus

\[
\boxed{
\text{inherited stock identity}
\not\Rightarrow
\text{all simultaneous physical owners vanish}.}
\]

**Label: RIGOROUS CONSEQUENCE of current Wang theorem typing.**

---

## 2. Kelvin: selector jump q.v. is path variation, not endpoint stock

For a supplied selected càdlàg residual path

\[
Y_0,Y_1,\ldots,Y_m,
\]

the finite selector-jump contribution to optional q.v. is

\[
\boxed{
\mathcal J[Y]
=\sum_{j=1}^m
\Delta_jY\,\Delta_jY^T.}
\]

This is a path functional.  On the closed two-point loop

\[
a\to b\to a,
\qquad a\ne b,
\]

one has

\[
\boxed{
\mathcal J[a\to b\to a]
=2(b-a)(b-a)^T\succeq0,\qquad b
e a,}
\]

while the endpoint selected state and endpoint dyad return exactly.

Hence selector jump q.v. is not an inherited stock amount and is not a state
coboundary.

**Label: EXACT KELVIN PATH IDENTITY / COUNTEREXAMPLE-NO-GO.**

---

## 3. No endpoint/ancestry stock rule can reconstruct selector jump variation

Let `Z` denote any current physical state description and let `S(Z)` be any stock
amount determined by that endpoint state.  More generally, allow a same-carrier
inheritance rule to depend on the two endpoint states `(Z_-,Z_+)` and their carrier
identity/ancestry label.

Compare two histories with identical start and end physical state and the same carrier
identity:

1. a stationary readout path;
2. a closed selector excursion through another readout and back.

Every endpoint stock rule sees the same data in the two histories.  Therefore it must
assign the same stock amount/stock increment to both.  But the selector jump-q.v.
accumulators are respectively

\[
0
\quad\text{and}\quad
2(b-a)(b-a)^T\succeq0` and nonzero.
\]

Consequently there is no universal map

\[
\boxed{
\Phi(\text{endpoint stock/ancestry data})
=\mathcal J[Y]}
\]

on a path class containing both histories.  The same no-go holds after taking trace.

This distinguishes two genuine memory types:

- **carrier ancestry/stock memory:** which physical carrier persists and how much
  current energy stock it carries;
- **selector-event path memory:** which readout/event route was traversed and how much
  optional jump variation accumulated.

They may coexist, but one does not encode the other.

**Label: COUNTEREXAMPLE/NO-GO / STATE-MAP CONSEQUENCE.**

---

## 4. Exact Navier--Stokes activates the distinction

Use the exact periodic shear

\[
u(y,t)=E\cos(ky)e_x,
\qquad
E=e^{-\nu k^2t},
\]

and the Kelvin asymmetric packet side

\[
\rho=\frac{\pi}{2k}.
\]

The half-period codeforming residual readouts satisfy exactly

\[
\boxed{
\chi_0=\frac{4Ek^2}{\pi^2},
\qquad
\chi_1=-\chi_0.}
\]

At one fixed physical NSE state/time, take

\[
a=\chi_0e_z,
\qquad
b=-\chi_0e_z.
\]

The stationary selector path and `0->1->0` closed selector excursion use the same
frozen exact-NSE payload and have identical start/end selected state.  Thus every
endpoint state stock observable agrees between them.  Nevertheless the excursion has

\[
\boxed{
\mathcal J_{\rm loop}
=8\chi_0^2P_z,
\qquad
\operatorname{tr}\mathcal J_{\rm loop}
=\frac{128E^2k^4}{\pi^4}>0,}
\]

whereas the stationary history has zero selector jump q.v.

So the stock-vs-path distinction is activated by exact smooth NSE data, not only by
an abstract loop.

Scope remains strict: this does **not** assert that Kelvin's actual first-bad rule
realizes that excursion at physical badness times, and it does not assert that the
shear lies on Wang's audited relay event lineage.  It calibrates the cross-program
state-map no-go only.

**Label: EXACT NSE CALIBRATION / COUNTEREXAMPLE-NO-GO.**

---

## 5. Componentwise quotient theorem: a correct quotient of one owner does not erase simultaneous owners

Let a physically typed event state be a product

\[
\mathfrak Z=(S,R_1,\ldots,R_q),
\]

where `S` is the component on which an exact quotient/relay identity is proved and
`R_i` are other physical owners at the same event.  The projection

\[
q_S(\mathfrak Z)=S
\]

may be exact for the `S`-claim.  But

\[
S_+=S_-
\]

implies equality only after projection.  It does not imply

\[
\mathfrak Z_+=\mathfrak Z_-
\]

unless every remaining owner is separately shown to agree.

Equivalently, the kernel of `q_S` contains all changes of the other owners.  A quotient
cannot prove that information in its own kernel is zero.

This elementary statement becomes physically nontrivial only because the owners have
already been typed before quotienting.

**Label: EXACT REPRESENTATION/QUOTIENT IDENTITY.**

---

## 6. Wang specialization: stock relay preserves simultaneous residual/material owners

For Wang's inherited relay, take

\[
S=\mathcal E_M
\]

and retain, separately, the current stage residual owner

\[
R_{\rm dyn}=\mathcal T_j
=\mathcal E_j\mathcal W_j+\mathcal N_j+\mathcal V_j
\]

plus the material sidecars.

The inherited-stock identity can therefore coexist with

\[
R_{\rm dyn}\ne0.
\]

Current Wang upstream makes this operational rather than rhetorical: its theorem
returns the stock quotient only on the inheritance domain and explicitly rejects a
stock-only use when classified residual work exceeds its admissibility criterion.
The exact-head Actions also preserve the material sidecars across the relay.

Hence the correct repo-3 dictionary entry is

\[
\boxed{
\text{same-carrier inheritance}
=\text{stock typing},
\quad
\text{not deletion of concurrent dynamics}.}
\]

**Label: RIGOROUS CONSEQUENCE / SIMULTANEOUS-OWNER PRESERVATION.**

---

## 7. Kelvin specialization: selector and physical event owners do not superpose naively

For Kelvin's persistent library, a simultaneous physical event `A` and selector
change `E_- -> E_+` have the literal combined selected operator

\[
\boxed{
D=E_+A-E_-
=E_-\Delta A+\Delta E+\Delta E\,\Delta A.}
\]

A quotient that looks only at the selector face `Delta E` or only at the physical
event face `E_- Delta A` misses the mixed simultaneous owner

\[
\boxed{\Delta E\,\Delta A.}
\]

At quadratic level, endpoint pair reset, continuous-source rate revaluation and
optional jump q.v. likewise remain distinct typed owners.

Thus Kelvin gives the same structural warning as Wang in a different physical
language:

\[
\boxed{
\text{a correct component identity}
\not\Rightarrow
\text{the other simultaneous faces disappear}.}
\]

**Label: EXACT KELVIN EVENT IDENTITY / RIGOROUS CONSEQUENCE.**

---

## 8. Cross-program dictionary and state-map consequence

The two programmes now separate four notions that a scalar “bank” picture would
wrongly merge:

| notion | Wang | Kelvin |
|---|---|---|
| current stock | same-carrier shell energy `E_M` | current selected/library pair or source state, according to owner |
| fresh generation/source | classified work/nonlinear/viscous stage owners | continuous Brownian q.v. source or physical event dynamics |
| owner registration / readout variation | hard physical event registration identifies the owner but does not by itself retype inherited stock as fresh generation | selector readout jump contributes optional path q.v. |
| history/ancestry | same-carrier inheritance relation | selector-event path/accumulator |

The exact common rule is not “all positive quantities are energy”.  It is

\[
\boxed{
\text{type the owner}
\;\longrightarrow\;
\text{apply only the quotient valid for that owner}
\;\longrightarrow\;
\text{retain every simultaneous face}.}
\]

Therefore a literal Wang--Kelvin state map that uses both inherited stock and selector
jump variation must carry both memory types separately (or prove an independent
physical theorem reconstructing one from the other).  Nonnegativity alone supplies no
bridge.

**Label: RIGOROUS CONSEQUENCE / OPEN BRIDGE.**

No recurrence, continuation, termination or global-regularity theorem is claimed.
