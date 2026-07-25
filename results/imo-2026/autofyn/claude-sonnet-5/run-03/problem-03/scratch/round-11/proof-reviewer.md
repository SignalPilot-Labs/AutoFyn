# Round 11 proof-reviewer report — imo-2026-03

Overall: all four built approaches (`global-lp-vertex-sufficiency`,
`self-similar-induction-on-n`, `greedy-reduction-geometric`,
`lp-duality-split-polytope`) made genuine, correctly-scoped progress this
round. No overclaims found; every self-reported `partial` Status is
accurate. Every new load-bearing claim was independently re-derived and/or
re-computed by the reviewer (own from-scratch scripts, exact `Fraction`
arithmetic, not the builders' own scripts) and confirmed correct. Four new
lemma files certified into `results/imo-2026-03/lemmas/`. `current.md`
updated with a new "Approaches tried (round 11)" section and a short
"Round 11 additions" note under "Current best." No promotable lemma was
rejected this round (all four proposals passed the adversarial check
described below).

---

## 1. `global-lp-vertex-sufficiency` — Verdict: CHANGES REQUESTED

**Status: `partial` (correct, matches self-report).**

Round 11 delivers three items, all independently checked:

1. **Textual fix** to Section 1's degrees-of-freedom description (trivial,
   confirmed).
2. **Rank-Pinning Lemma**, closing a real gap in Lemma 4.1(b): round 10's
   $L$ correctly pinned the *ordering between* branches $\sigma,\tau$ via
   $f_\sigma-f_\tau\in L$, but never justified that each $f_\sigma$ is
   itself a single affine formula on a cell (it depends on which
   coordinate of $y_\sigma(p)$ occupies which sorted rank, which nothing
   in round 10's $L$ pinned). The fix enlarges $L$ with all pairwise
   differences among each $\sigma$'s own multiset $y_\sigma(p)$. I
   independently re-derived the argument from scratch (constant sign of
   finitely many pairwise differences on a connected open cell fixes the
   coordinates' full relative order, hence a fixed rank assignment,
   hence a fixed affine formula for the sum of the odd-rank coordinates) —
   correct, elementary order theory. I checked the claim that this does
   not disturb Lemma 4.1(a), Lemma 4.2, or the already-closed
   $Q_{\mathrm{region}}$: all three depend only on finiteness/affineness
   of $L$'s members and on region-only functionals, both preserved/
   unaffected by the enlargement — confirmed correct.
3. **General Multi-Piece Subset-Tie construction + Mass-Constraint
   Theorem**, the round's main new target (bounded-split-piece-count
   sufficiency), delivering a genuine, fully rigorous **negative** result
   rather than the requested positive construction. I independently
   re-derived: (a) the value formula
   $\mathrm{OddSum}(M)=(1-\Pi)+\mathrm{OddSum}(\{r_1,\dots,r_s\})$ from the
   $B\sqcup L$ decomposition and the certified Singleton-Interleaving
   Lemma — correct; (b) the Mass-Constraint inequality $\Pi\ge1/2$, a
   one-line summation of the legality constraints — correct; (c) the exact
   coordinate bound $p_1(e_0)=(2+n(n+1)\gamma(n))/(2(n+1))<3/(2(n+1))$,
   re-derived independently from the (already-certified, round 10)
   closed-form coordinates of $e_0$ and matched exactly to the file's
   claim; (d) the resulting bound $s>(n+1)/3$ — correct algebra. The
   negative result's scope is stated honestly: it rules out only the
   "tie split fragment to a whole untouched piece" family for any fixed
   $s_0$, not fragment-vs-fragment tying or non-tie mechanisms, both
   flagged as the genuinely open next leads.

**No gap found in any of this round's new content.** The pre-existing gap
(the $\Sigma$-shape part of $Q$, i.e. the Existence Theorem itself) remains
open, honestly reported as such — no overclaim.

**Certified:**
`lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md` (Rank-Pinning
Lemma + General Multi-Piece Subset-Tie construction + Mass-Constraint
Theorem, both self-contained and correctly scoped).

---

## 2. `self-similar-induction-on-n` — Verdict: CHANGES REQUESTED

**Status: `partial` (correct, matches self-report).**

Round 11 proves two new general-purpose lemmas from scratch (explicitly
*not* assumed transferred from the sibling `global-lp-vertex-sufficiency`,
since the polytope is genuinely different — free real coordinates here vs.
fragments constrained to sum to a fixed $p_i$ there, so no "free-block"
elimination step is needed):

- **Affine-Rank Lemma**: within a fixed strict order type $\tau$ on free
  coordinates $x$ merged with frozen values $c_l$, $\mathrm{OddSum}$ is a
  fixed affine ($0/1$-linear) function of $x$. I independently re-derived
  this — a strict total order determines fixed ranks, hence a fixed set of
  odd-rank $x$-indices and a fixed constant from the odd-rank $c_l$'s —
  correct, and genuinely simpler than the sibling's version, as claimed.
- **Vertex-Attainment Lemma**: extrema of an affine functional on a
  compact convex polytope occur at a vertex — standard, correctly proved
  in full via the finite segment-extension argument, independently
  verified.

These combine into the **Middle-Regime Vertex Reduction Theorem** (a
structural reduction, not itself a closure) plus a **Feasibility Fact**
(the middle regime is nonempty only if $S$'s own top piece $2^{m-1}$ is
cut) — I re-derived the Feasibility Fact's pigeonhole argument
independently, correct.

Applied to the minimal middle-regime instance $(j,c)=(2,1)$, I hand-verified
all three exact-arithmetic claims, digit for digit:
- $m=3$: $\{4,2,2\}\cup\{4,0,2,1\}$ sorted $4,4,2,2,2,1,0$,
  OddSum $=4+2+2+0=8=2^3$. Matches.
- $m=4$: $\{6,6,4\}\cup\{4,4,4,2,1\}$ sorted $6,6,4,4,4,4,2,1$,
  OddSum $=6+4+4+2=16=2^4$. Matches.
- $m=5$: $\{12,12,8\}\cup\{8,8,8,4,2,1\}$ sorted $12,12,8,8,8,8,4,2,1$,
  OddSum $=12+8+8+4+1=33>32=2^5$. Matches (strict slack, as claimed).

**Honestly scoped, no overclaim.** The file is explicit that the vertex
candidates used were located by numerical search, not a completed
exhaustive enumeration (which would also need ties against individual
elements of $\Gamma_{m-2}$); general $m$, the middle regime in general,
`Case-B(m,k)`, and gap (b)(ii) remain fully open. The file also honestly
reports a genuine self-caught bug (an initial $\Gamma_{m-3}$ vs. correct
$\Gamma_{m-2}$ indexing slip, caught via a failing numerical sanity check
before any claim was made) — good process discipline.

**Certified:**
`lemmas/affine-rank-and-vertex-attainment-middle-regime.md` (Affine-Rank
Lemma, Vertex-Attainment Lemma, Feasibility Fact, plus the three
hand-verified small-instance closures recorded as reviewer-checked
examples, not as a general theorem).

---

## 3. `greedy-reduction-geometric` — Verdict: CHANGES REQUESTED

**Status: `partial` (correct, matches self-report).**

This round's headline finding is a *self-correction*: the round's
dispatched "Case B quick win" premise (last round's explorer's claim of
"$\approx0.34$ substantial slack, no near-ties") is refuted by the
builder's own mandatory stress test, and replaced with a genuine positive
finding.

**Stress-test counterexample, independently reproduced from scratch** (own
exact-`Fraction` Python script, not the builder's):
$P=(327889/81977,\,203653/81977,\,97214/81977,\,27060/81977)$ at $m=4$:
$\mathrm{sum}(P)=8$ exactly, $\max(P)=327889/81977<4$ (genuine Case B
instance), and $\mathrm{OddSum}(P\cup\{4,2,1\})-8=19/81977$ — matched the
file's claimed margin exactly, confirming the round's original "quick win"
premise does not hold.

**Lemma N (WLOG $b_2=2^{m-1}$).** A clean monotonicity argument (none of
$P$, $S'''$, or the cut budget depend on $b_2$; the hypothesis
$\max(P)<b_2$ implies $\max(P)<2^{m-1}$ when $b_2\le2^{m-1}$). I
independently re-checked every step; no gap, including the previously
implicit fact $|P|\ge2$ (correctly proved: a single piece would force
$\max(P)=2^{m-1}\ge b_2$, contradicting the hypothesis).

**Theorem N (Case B $\equiv$ TOP-ONLY$(m-1)$ complementary regime, on the
$S'''$-unsplit-full-budget slice).** I independently re-checked every
symbol substitution: $\{2^{m-2}\}\cup S'''=\{2^{m-2}\}\cup\Gamma_{m-3}
=\Gamma_{m-2}=\Gamma_{m'-1}$ (definitional), the piece-cap arithmetic
$|P|\le m=m'+1$ (from the cut-budget hypothesis with $S'''$ unsplit), and
the hypothesis match $\max(P)<2^{m-2}=2^{m'-1}$ — all correct, term-for-
term. This is a genuine equivalence, not an analogy, and its corollaries
(Theorem 6 closes a genuine, if vacuous-until-$m=9$, sub-slice with zero
new work; the remaining sub-slice coincides exactly with
`self-similar-induction-on-n`'s Branch-I.A-restricted window) are both
correctly derived, cross-checking cleanly against that sibling file's own
open-gap description.

**Scope honestly stated**: Theorem N covers only the $S'''$-unsplit slice
of Case B, not the general case (allowing $S'''$ itself to be split); Case
A is untouched beyond a recorded (not claimed-proved) scope diagnosis.
Level-Absorption remains open. No overclaim found.

**Certified:**
`lemmas/wlog-b2-and-case-b-topOnly-equivalence.md` (Lemma N + Theorem N).

---

## 4. `lp-duality-split-polytope` — Verdict: CHANGES REQUESTED

**Status: `partial` (correct, matches self-report).**

Two independently-checked findings:

**Finding 1 (negative, exact).** The dispatched generalization (transplant
round 10's Multi-Piece Sufficiency construction to LB's geometric
partition) fails. I independently re-implemented the construction from
its literal description (top-pair $\varepsilon$-trick, equal-halves middle
landmarks, bottom landmark unsplit) and re-computed the shortfall table in
exact `Fraction` arithmetic for $n=2,\dots,8$: my results
($1.4\times10^{-7}$ at $n=2$ up to $\approx0.1233$ at $n=8$, monotonically
growing) matched the file's table to the reported precision at every
tested $n$. The structural diagnosis given (LB's exponential landmark
gaps vs. the AP family's constant-gap structure the mechanism actually
needs) is a reasonable qualitative explanation, correctly flagged as
explanatory, not a separate formal theorem.

**Finding 2 (new positive result): Top-Duplication Witness Theorem.** I
independently re-implemented the construction from scratch (split only the
top landmark into $2^{n-1},\dots,2^1,1,1$, leave every other landmark
unsplit) and computed $\mathrm{OddSum}$ by direct sort-and-sum in exact
`Fraction` arithmetic for $n=0,\dots,14$: exact fraction equality with
$c(n)=2^n/(2^{n+1}-1)$ in all 15 instances (verified as identical fractions,
not floating-point approximations — e.g. $n=9$ gives $512/1023$ on both
sides exactly). The proof's mechanism (isolated tied pairs contributing $0$
to AltSum via the certified Even-Block-Neutrality machinery, plus a
bottom-three-block of value $1$ landing at odd-even-odd ranks since $2n$ is
even) is correct and matches the exact computation. This proves
$V(p_{\mathrm{LB}})\le c(n)$ unconditionally for every $n$ — a genuine,
correctly and honestly scoped single-point contribution to the upper-bound
direction (it does not touch the reverse inequality nor extend beyond
$p=\mathrm{LB}$, both stated explicitly in the file).

**Certified:** `lemmas/top-duplication-witness-theorem.md`.

---

## Certification summary

All four proposed lemma sets passed the full adversarial check (independent
re-derivation of the load-bearing step, independent from-scratch numeric
reproduction of every exact-arithmetic claim, and a check that no builder
self-certified — confirmed: none of the four files contain pre-written
"Reviewer assessment / Certified" text, all four properly proposed
"Promotable lemmas" for the reviewer). Newly certified this round:

- `results/imo-2026-03/lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md`
- `results/imo-2026-03/lemmas/affine-rank-and-vertex-attainment-middle-regime.md`
- `results/imo-2026-03/lemmas/wlog-b2-and-case-b-topOnly-equivalence.md`
- `results/imo-2026-03/lemmas/top-duplication-witness-theorem.md`

`results/imo-2026-03/current.md` updated: new "Approaches tried (round 11)"
section (all four `CHANGES REQUESTED`) and a short "Round 11 additions"
note under "Current best." Overall Status remains `partial` — no approach
claimed `solved` this round, and none should: the Existence Theorem
(upper-bound direction) and Level-Absorption / the general middle regime
(lower-bound direction) both remain genuinely open, though narrower in
well-documented, cross-checked ways.

## Ranker outcomes recorded

All four recorded as `advanced` (real, gap-closing or genuinely new
positive/negative progress, not just narrowing):
`global-lp-vertex-sufficiency`, `self-similar-induction-on-n`,
`greedy-reduction-geometric`, `lp-duality-split-polytope`.
