## Statement

Normalize $T=p_1+p_2+p_3+p_4$, $u:=T/15$. For every
$(p_1,p_2,p_3,p_4)$ with $p_1\ge p_2\ge p_3\ge p_4>0$,
$$p_1\ge T/2 \qquad\text{and}\qquad T/15<p_2<4T/15$$
(i.e. the exact residual region left open by rounds 24–26's
`case-b2-n3-covering-closure`, once that lemma's $p_1<T/2$ restriction is
correctly restored), at least one of the four "Gap-Filler" chambers
$$\{\mathrm{Bisect}\{1,4\},\ \mathrm{Bisect}\{1,2\},\
\mathrm{Bisect}\{1,2,3\},\ \mathrm{Bisect1{+}Pin2to3}\}$$
is feasible (each always is — see below) **and successful**
($\Phi_\tau(p)\le\tfrac8{15}T$). Consequently $\Phi_{\min}(p)\le\tfrac8{15}T$
throughout this region.

**The four chambers** (writing $x:=p_2-p_3,\ y:=p_3-p_4,\ z:=p_4$):

- $\mathrm{Bisect}\{1,4\}$: bisect $p_1$ and $p_4$; leave $p_2,p_3$.
  $\Phi=(T+x)/2$, succeeds iff $x\le u$.
- $\mathrm{Bisect}\{1,2\}$: bisect $p_1$ and $p_2$; leave $p_3,p_4$.
  $\Phi=(T+y)/2$, succeeds iff $y\le u$.
- $\mathrm{Bisect}\{1,2,3\}$: bisect $p_1,p_2,p_3$; leave $p_4$.
  $\Phi=(T+z)/2$, succeeds iff $z\le u$.
- $\mathrm{Bisect1{+}Pin2to3}$: bisect $p_1$; cut $p_2$ into $(p_3,\,x)$
  (one fragment exactly equal to $p_3$); leave $p_3,p_4$.
  $\Phi=(T+|x-z|)/2$, succeeds iff $|x-z|\le u$.

Each chamber's closed form is derived via the `pair-insensitivity-corollary`
of `odd-run-reduction-lemma` (see that lemma file, or
`results/imo-2026-03/approaches/lp-duality-certificate.md` §R27.2 for the
full derivation of each). All four use at most $3$ marks and are legal by
`budget-monotonicity` (using fewer than the full budget is always legal).

## Proof (covering theorem)

In $(x,y,z)$-coordinates ($x,y,z\ge0$; $p_1\ge T/2\Leftrightarrow
x+2y+3z\le T/2$; $T/15<p_2<4T/15\Leftrightarrow u<x+y+z<4u$), suppose
toward contradiction all four chambers fail: $x>u,\ y>u,\ z>u,\ |x-z|>u$.
Split on the sign of $x-z$.

**Case (i), $x-z>u$.** The nonnegative combination
$$1\cdot(4u-x-y-z)+1\cdot(y-u)+1\cdot(x-z-u)+2\cdot(z-u)$$
of the strict inequalities $4u-x-y-z>0$ (from $p_2<4u$), $y-u>0$,
$x-z-u>0$ (Case (i) hypothesis), $z-u>0$ is a sum of $4$ strictly positive
terms with nonnegative (here all positive) coefficients, hence strictly
positive; but expanding termwise it equals $0$ identically. Contradiction
($0>0$).

**Case (ii), $z-x>u$.** The nonnegative combination
$$1\cdot(T/2-x-2y-3z)+4\cdot(x-u)+2\cdot(y-u)+3\cdot(z-x-u)$$
of the non-strict $T/2-x-2y-3z\ge0$ (from $p_1\ge T/2$) and the strict
$x-u>0$, $y-u>0$, $z-x-u>0$ (Case (ii) hypothesis) is, by the same
argument, strictly positive; expanding termwise (with $T/2=7.5u$) it
equals $-1.5u$ identically. So $0<-1.5u$, i.e. $u<0$, contradicting $u=T/15>0$.

Both cases are contradictory, so at least one of $x\le u,\ y\le u,\
z\le u,\ |x-z|\le u$ holds throughout the region, i.e. at least one
chamber succeeds. $\blacksquare$

## Verification

- Each chamber's closed form: 2000 exact-`Fraction` random trials
  (`/tmp/round-27/verify_formulas.py`), zero mismatches against direct
  sort-and-alternate-sum.
- The covering theorem itself: 300,000-trial exact-`Fraction` random
  search over the region (`/tmp/round-27/final_check.py`), zero
  violations of $\min(x,y,z,|x-z|)\le u$; a separate LP tightness check
  (`/tmp/round-27/find_witness2.py`) confirms Case (i)'s bound is attained
  with equality exactly (sup margin $=0$) and Case (ii)'s bound is strict
  (infeasible even at margin $0$), consistent with the algebraic proof
  above (both are corroboration, not substitutes for the algebraic proof).
- Motivating witness: $p=(0.6,0.15,0.15,0.10)$ (round-27 outline-
  reviewer's counterexample to the abandoned "forced-feasibility" lemma)
  is closed trivially by Chamber A ($x=p_2-p_3=0\le u$).
- Worst-case (tightest) witness found: $p=(1/2,1/4,1/6,1/12)$, where
  Chambers A, B, C individually fail ($x=y=z=1/12>u=1/15$) but Chamber E
  succeeds exactly at equality ($x=z=1/12\Rightarrow|x-z|=0\le u$,
  $\Phi_E=T/2=0.5\le8/15$).

## Discussion / provenance

Built in `results/imo-2026-03/approaches/lp-duality-certificate.md`,
round 27, §R27.0–R27.3, in response to the round-27 outline-reviewer's
finding that the outline's proposed "forced-feasibility lemma" was false
and that a genuinely new chamber family (in the spirit of the reviewer's
observed "bisect $p_1$ + refine $p_4$" optimal pattern) was needed to
close the residual $p_1\ge T/2$, $T/15<p_2<4T/15$ gap. Combined with the
already-certified case (a)/(b1)/(b2)-restricted-to-$p_1<T/2$ regimes
(`unconditional-p2-threshold-closure`, the Corollary to Theorem B $+$
`n2-upper-bound-lp-argument`, `case-b2-n3-covering-closure`), this
completes the general-marking $n=3$ upper bound $c(3)\le8/15$ (see the
approach file's §R27.5 for the full assembly).

## Certification note

CERTIFIED round 27. Proof-reviewer independently re-derived both Farkas
certificates (Case (i): expansion is identically $0$; Case (ii): expansion
is identically $-1.5u$) by hand and confirmed each termwise. Independently
re-verified all four chamber closed forms and the covering property with a
fresh script (`/tmp/verify_gapfiller.py`, 28,699 exact-`Fraction` random
trials landing in the exact region $p_1\ge T/2,\ T/15<p_2<4T/15$): zero
formula mismatches, zero coverage violations. Also independently confirmed
this family resolves the specific witness that broke round 26's rejected
"bonus" domain-widening attempt ($p=(3/5,9/40,29/200,3/100)$: $z\le u$
holds there, so Chamber C succeeds, $\Phi_C=103/200<8/15$). **Scope
warning (unchanged):** this lemma closes only the specific residual region
stated — it does not by itself establish the full $n=3$ upper bound (that
requires the additional, separately-certified case (a)/(b1)/(b2)-restricted
pieces cited above and assembled in the approach file). The reviewer
additionally re-checked, by hand, that case (a)'s citation (R26.1) genuinely
imposes no restriction on $p_1$ (it peels $p_2$ via Theorem B and discharges
the reduced 3-element instance unconditionally via `n2-upper-bound-lp-
argument`), and that the four regimes (b1)/(a)/middle-$p_1<T/2$/middle-
$p_1\ge T/2$ are exhaustive and non-overlapping — no gap found in the
final assembly.
