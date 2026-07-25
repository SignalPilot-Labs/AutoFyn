# Round 17 proof-reviewer report — imo-2026-03

Reviewed the 3 built approach files (`self-similar-induction-on-n`,
`global-lp-vertex-sufficiency`, `lp-duality-split-polytope`), independently
re-derived every load-bearing step with fresh, from-scratch exact-`Fraction`
(and one `sympy` symbolic) scripts (not reusing any builder script), per
dispatch. Scripts left at `/tmp/round-17/scripts/`.

## 1. `self-similar-induction-on-n` — CHANGES REQUESTED (Status: `partial`)

**Headline claim under scrutiny**: "Sub-case (i) of GT(m) is fully closed
for every k≥1, every excess e≥1" (a corrected redo of round 16's retracted
false claim).

**What I independently re-verified as correct** (all via fresh scripts,
`/tmp/round-17/scripts/verify.py`, `verify_chain.py`, `verify_general.py`,
`verify_claims.py`):

1. **Fact (a)** ($O_j = 2^{j-1}+E_{j-1}$, the certified q=0 clause restated
   in the coupled-recursion notation) — matches the certified lemma file
   (`monotonicity-reduction-and-unified-threshold-pair-peeling.md`, line 114)
   verbatim once notation is unified. Verified 20,000 trials + 5,000
   explicit-tie trials (forcing $\max(D)=2^{j-1}$ exactly), zero violations.
2. **Fact (b)** ($E_j=O_{j-1}$, the new "Even-target Companion Peeling"
   identity) — this is exactly the general fact "for any finite multiset
   $S$ with unique max $x$: $\mathrm{EvenSum}(S)=\mathrm{OddSum}(S\setminus
   \{x\})$" specialized to $S=D\cup\Gamma_{j-1}$. Verified this **general**
   identity independently (20,000 trials, arbitrary multisets, unique max
   enforced): zero violations. **Genuinely correct, elementary, certified.**
3. **The composed ratio-4 closed form** (both parities of $e$) — verified
   directly against raw $\mathrm{OddSum}$ computation on the full multiset
   $D\cup\Gamma_{m-1}$ (not the decomposed formula), 20,000 trials,
   $k=1,\ldots,6$, $e=1,\ldots,8$: zero mismatches. This is a real, corrected
   fix of round 16's bug (round 16's claimed ratio-2/$e$-term telescoping is
   indeed false; the true form is ratio-4/$\lceil e/2\rceil$-term, matching
   the round-17 outline-reviewer's own mismatch table exactly, which I also
   reproduced independently).
4. **Claim A (even excess)** — re-derived the margin formula
   $\mathrm{LB}_{\mathrm{even}}-T_{\mathrm{even}}$ symbolically via `sympy`
   from scratch: matches the file's displayed formula exactly. Confirmed it
   is strictly increasing in $a_1$ and non-negative at the window's infimum
   for every $k\ge1$, every even $e\ge2$ — **and, because it is increasing,
   this genuinely extends to the FULL range** $a_1\in(2^{k-1},2^k]$, not
   just the window. Independently stress-tested 200,000+ trials spanning the
   full range for even $e$: **zero violations**. Claim A is correct and
   complete as literally usable to close the full range.
5. **The $(k,e)=(1,1)$ vacuity argument (Step 3)** — airtight. Independently
   confirmed: under $\mathrm{GT}(m)$'s own cardinality cap $|D|\le m+1=3$
   (so $|R|\le2$), with $\max(R)\le1$, the required $\mathrm{sum}(R)\in(2,3)$
   is unreachable ($\mathrm{sum}(R)\le2$ always) — a direct, elementary
   contradiction, confirmed by a targeted 50,000-trial search finding
   **zero feasible instances at all** at this $(k,e)$ under the cap.

**The gap I found (a new overclaim, distinct from round 16's, in the same
theorem)**: **Claim B (odd excess) is only ever proved for $a_1$ *inside*
the width-1 window** $(2^{k-1},2^{k-1}+1)$. Its own derivation computes the
margin's minimum only *over the window* (the margin
$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=2^k/6+2^m/6-a_1/2-1/2$ is
**decreasing** in $a_1$ — re-derived symbolically, confirmed matches the
file). Since it is decreasing, the theorem's own claimed *full* range
$a_1\in(2^{k-1},2^k]$ has its true worst case at the *far* end, $a_1=2^k$
(strictly further right than the window's own right endpoint whenever
$k\ge2$), which the file's proof never checks. I computed this true
worst-case margin symbolically: $2^k(2^e-2)/6-\tfrac12$. **For $e=1$ this is
$-\tfrac12<0$ for every $k$** — i.e. the cap-free version of the claimed
inequality is **provably false** there, confirmed by an explicit
hand-verified `Fraction` counterexample: $k=2,e=1,m=3$, $a_1=494/125\in
[2^{k-1}+1,2^k]=[3,4]$, a 4-element $R$ (max $\le2$, sum matching exactly):
true $\mathrm{OddSum}(D\cup\Gamma_{m-1})=122753/16235\approx7.56<8=2^m$.
This specific instance has $|D|=5>m+1=4$, so it is outside $\mathrm{GT}(m)$'s
own cardinality-capped scope — but critically, **no proof anywhere in this
round (or any prior round) establishes the capped version either**: Claims
A/B are explicitly derived cap-free (the cited Half-Sum Corollary is stated
"no cap needed"), and I found no argument in the file that reintroduces the
cap for this specific sub-region. (Targeted testing *with* the cardinality
cap enforced at exactly this $(k,e)=(2,1)$ found zero violations in 145,546
trials — so the capped claim is likely true — but it is *conjectural, not
proved*, by this round's own standard for what counts as established.) For
odd $e\ge3$ the analogous full-range worst case (also at $a_1=2^k$) happens
to stay non-negative both symbolically and in 140,245 stress trials — but
this too is not established by the file's given proof, which only ever
analyzes the window.

**Verdict on the theorem as literally stated ("full closure for every
$e\ge1$")**: **not established**. What IS established (independently
re-verified, safe to rely on): sub-case (i) is closed (a) for every even
excess $e\ge2$ across the *whole* range $a_1\in(2^{k-1},2^k]$; (b) for the
width-1 window itself at every excess $e\ge1$ (both parities — Claim B does
correctly close the window); (c) the vacuous $(k,e)=(1,1)$ case. **Not
established**: odd excess $e\ge1$ outside the window (concretely open at
every $k\ge2$, $e=1$, and not derived — even if numerically plausible — for
larger odd $e$ either). This is a genuinely narrower, but still real, gain
over round 15 (which had no even-excess-full-range result at all), so this
is real, certifiable progress — just not the "full closure" claimed.

**Certified**: `lemmas/even-target-companion-peeling-and-corrected-qzero-
chain.md` (the two general-purpose facts: Even-target Companion Peeling
identity; corrected $e$-fold $q{=}0$-chain closed form, both fully proved
and independently reverified). **Rejected as stated**: the "Sub-case (i)
Full Closure for $e\ge1$, corrected" bullet — the true, narrower scope is
recorded in `current.md` instead.

Ranker: recorded `partial` (not `dead-end` — genuine certified sub-results
survive; not `advanced` on the headline, since the headline itself does not
survive as stated).

## 2. `global-lp-vertex-sufficiency` — CHANGES REQUESTED (Status: `partial`)

New **Flat/Kink Parity Lemma**: for a within-piece bisection perturbed by
$t$ against a fixed background, $\mathrm{OddSum}$ is affine in $t$ on any
non-crossing interval with slope
$[\mathrm{rank}(x)\text{ odd}]-[\mathrm{rank}(y)\text{ odd}]\in\{-1,0,+1\}$.
Re-derived independently from the definition of $\mathrm{OddSum}$ (a sum
over a rank-fixed subset of coordinates on such an interval) and verified
with a fresh script: 19,806 valid (non-crossing) random trials out of
20,000 attempted, zero mismatches. This is a clean, correct, elementary,
general-purpose lemma that cleanly unifies the round's two previously
separate phenomena (Self-Bisection-Crossover = opposite-parity ranks at a
crossing → sharp kink; Flat-Edge = same-parity ranks → a genuine
positive-dimensional face of tied optima) into one mechanism. The exact toy
instance (3 flat runs, `Fraction` arithmetic) is correctly reported and I
did not find any issue with the reasoning connecting the lemma to the
observed hard-point data. Honestly scoped — explicitly not claimed to close
the Existence Theorem's $\Sigma$-shape residual, and the mandatory
cheap-kill is correctly flagged as tautological (verification-only) rather
than a constructive tool. No overclaim found. **Certified**
`lemmas/flat-kink-parity-lemma.md`.

## 3. `lp-duality-split-polytope` — CHANGES REQUESTED (Status: `partial`)

New **Even-Multiplicity Equality Criterion** ($\mathrm{OddSum}(M)=\tfrac12$
for a mass-1 multiset iff $|M|$ even and every value has even multiplicity)
and **Generalized Mass-Constraint Theorem** (construction-free extension of
the certified round-11 Mass-Constraint Theorem to *any* legal response
attaining the floor exactly). Independently verified: the Criterion via a
30,000-trial script (half forced-even-multiplicity, half unconstrained),
zero mismatches; the Theorem's underlying elementary counting argument
(each untouched value must reappear as a matching fragment inside some
active piece, bounding total untouched mass by total active mass) checked
directly via hand-built concrete constructions (both a positive instance
attaining the floor with untouched mass $\le\tfrac12$, and a negative
instance showing the predicted infeasibility when trying to force
untouched mass $>\tfrac12$). The $e_0$ application's exact closed form
($\tfrac mN-\delta\tfrac{m(N-m)}2$ for the bottom-$m$ mass) and its full
9-row requested table ($n=8,9,10$, $s=n-2,n-3,n-4$) were independently
reconstructed from the certified AP coordinates and matched digit-for-digit
against the file's reported fractions in all 9 rows (including the one
genuine rule-out, $n=8,s=4$: $2465/4599>1/2$). The honest asymptotic
argument (fixed $m$, bottom-$m$ mass $\to0$ as $N\to\infty$, so this
technique alone cannot reach $s\ge n-1$) is correct and not overclaimed.
**Certified**
`lemmas/even-multiplicity-criterion-and-generalized-mass-constraint.md`.

## Files touched this round

- `results/imo-2026-03/current.md` — added "Approaches tried (round 17)"
  section, updated "Current best" with round-17 corrections, and added a
  precise note to the "Open" gap-1 summary reflecting the corrected
  sub-case-(i) residual.
- `results/imo-2026-03/lemmas/even-target-companion-peeling-and-corrected-
  qzero-chain.md` — new, certified.
- `results/imo-2026-03/lemmas/flat-kink-parity-lemma.md` — new, certified.
- `results/imo-2026-03/lemmas/even-multiplicity-criterion-and-generalized-
  mass-constraint.md` — new, certified.
- Verification scripts: `/tmp/round-17/scripts/*.py` (verify.py,
  verify_chain.py, verify_claims.py, verify_general.py,
  verify_outside_window.py, find_ce.py, find_ce_capped.py,
  verify_parity.py, verify_evenmult.py, verify_gmct.py, verify_gmct2.py,
  verify_table.py, verify_e3.py, verify_even_outside.py).

## Ranker outcomes recorded

- `self-similar-induction-on-n`: `partial` — real certified sub-results
  (Even-target identity, corrected chain, even-excess full-range closure,
  vacuity proof) survive, but the round's own headline "full closure"
  claim does not; new, precisely-identified residual (odd excess outside
  the window) replaces the old, less-precise "$e=0$ only" residual.
- `global-lp-vertex-sufficiency`: `advanced` — new certified general
  lemma (Flat/Kink Parity), correctly scoped, no overclaim.
- `lp-duality-split-polytope`: `advanced` — two new certified
  general lemmas plus one genuine new exact impossibility result at
  $(n,s)=(8,4)$, correctly scoped, no overclaim.
