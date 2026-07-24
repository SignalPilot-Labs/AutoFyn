# Round 27 proof-reviewer report — imo-2026-03

Overall problem Status: remains `partial` (general n, both directions, not solved).
One genuine sub-milestone certified this round: the general-marking n=3
upper bound c(3)<=8/15 is now fully, rigorously solved (lp-duality-certificate).

## 1. rank-pigeonhole-budget — Verdict: APPROVE (own scope: Claim (A), unaffected)

Status recorded in file: `solved` (correctly scoped to Claim (A) only — the
achievability + full lower bound for the sub-case "Xiang Yu spends his whole
budget fragmenting p1, tail untouched"). This scope was fully closed in
round 8 and is untouched by this round's work; APPROVE stands (no change).

**This round's new content (§7.14, §7.15) — reviewed adversarially, both
verified correct, no overclaim:**

- **§7.14 (σ2-Untouched Closure Theorem, general m).** Claim: for every
  m>=2 and every legal top-cut shape of a ratio-2 tail σ with σ1 receiving
  >=1 cut and σ2 left completely untouched (no restriction on σ3..σm's
  cuts), A(S) <= σ1 - σm. I independently re-derived both case branches by
  hand (odd/even total multiplicity at σ2 in the "no fragment exceeds σ2"
  case; the two-peel argument via `sharp-dominant-removal-identity` in the
  "one fragment exceeds σ2" case), confirmed the identity
  R(σ)+σm=2σ1 algebraically, and independently wrote a fresh verification
  script (`/tmp/verify_714.py`, 20,000 random trials, m=2..7, arbitrary cut
  counts on σ1 and σ3..σm): zero violations. This is a genuine, fully
  general, budget-free theorem — no case split on cut count anywhere,
  correctly generalizing 4 of the 5 m=4 shapes closed by hand in round 26.
  **No gap found.**

- **§7.15 (Necessity Theorem).** Claim: for m>=5, closing the complementary
  (σ2-touched) residual of MaxCeil(m)'s top-cut branch *in full generality*
  necessarily entails a restricted instance of (star_{m-2}), the project's
  own uncertified central obstruction — proved via a continuity/limiting
  argument on S_ε = {σ1-ε,ε}∪Z∪τ as ε→0+. I re-checked: (i) the continuity
  lemma is a standard, valid fact (limit of finitely many continuous
  order-statistic functions, extended correctly through the ε=0 boundary
  case since the "0" fragment is provably the unique bottom rank near
  ε=0); (ii) A(S_0) = σ1 - A(Z∪τ) via `sharp-dominant-removal-identity`
  is correct; (iii) the final identification of A(Z∪τ)>=σm with a
  restricted case of MinFloor(m-1)≡(star_{m-2}) (via §7.11's already-
  certified Index-Chain Identity) is algebraically sound. **Crucially, this
  is a correctly and honestly scoped *necessity* (not impossibility)
  finding**: it does not claim (7.9.1)/MaxCeil(m) is false or unprovable
  for m>=5 — only that no proof avoiding (star_k), k>=3 can exist. This
  does not foreclose future work; it correctly redirects it. **No
  overclaim found** — this was the specific risk flagged by the dispatch,
  and the file passes: it never claims impossibility, only entanglement.

**Lemma certifications:** `sigma2-untouched-closure-theorem.md` and
`pair-insensitivity-corollary.md`-independent — wait, that one belongs to
lp-duality-certificate (see below). `sigma2-untouched-closure-theorem.md`
CERTIFIED (edited in place with verification note). The Necessity
Theorem's Continuity Lemma was not proposed as a standalone lemma by the
builder (folded into the approach file) — left as is, no separate
certification needed.

**record_outcome:** advanced.

## 2. greedy-halving-adversary — Verdict: CHANGES REQUESTED

Status recorded in file: `partial` (correct — matches the true state).

**Theorem 41 (Even-Multiplicity Non-Maximal-Tie Closure) — verified,
genuine, unconditional, no gap.** Closes the complementary half of round
26's Theorem 40: for every legal T'' with a value t* of EVEN multiplicity
mu>=2, A({t*}∪{p4}∪T'') >= f(n)+t* > f(n), unconditionally, for every
n>=5. I independently re-derived the entire 5-step chain by hand (Rank-
Split Formula; odd-run collapse of the even-multiplicity block via
`odd-run-reduction-lemma`; the `insert-element-identity` substitution;
substitution of the ladder mass identity Total(T'')=p4-f(n); the two
trivial per-piece bounds A<=Total and A>=0 applied *separately* to H and L
rather than to T'' as one lump) and cross-checked every algebraic
substitution against the certified `insert-element-identity`'s literal
statement. I then wrote an independent verification script
(`/tmp/verify_thm41.py`, 20,000 trials constructing genuine ladder tails
with engineered even-multiplicity ties via equal-splitting a random tail
piece, n=5..12): zero violations. Theorem 41 itself is correct and exactly
as strong as claimed. **Certified** `even-multiplicity-non-maximal-tie-closure.md`.

**Real gap found: the file's own "Corollary" overclaimed.** The Corollary
(and three other places in the file — the top "Approaches tried" summary,
the "Round 27 update" note in Current best, and the "Round 27 status" Open
gaps entry) combined Theorem 41 with Theorem 40 AND Theorem 37 to claim
"Theorem 37's whole T'-untouched branch...is now closed unconditionally,
for every n>=5." This is FALSE for n>=7: Theorem 37 itself (the symmetric
vertex b=p4, round 23) is explicitly stated in its own header as "closes
unconditionally for n<=6, conditionally on (star_{n-4}) in general" — i.e.
conditional for n>=7, and this round's work (Theorems 40/41) never removes
that conditionality; it only closes the *other* candidate vertices (b
ties to a non-maximal T'' element, odd or even multiplicity). Combining a
newly-and-genuinely-unconditional result with an older conditionally-
scoped sibling, and then dropping the sibling's own caveat in the combined
claim, is exactly the overclaim pattern flagged in rounds 24-26 (memory
rules 30-32) recurring in a new location. **I corrected this in place, in
all three locations in the approach file** (top summary, the Corollary
section itself, and the Open-gaps "Round 27 status" entry): the corrected
claim is that the non-maximal-tie residual (odd+even multiplicity) is
fully closed unconditionally for every n>=5 (genuine, new), but the
"T'-untouched" branch AS A WHOLE (including Theorem 37's own vertex)
remains unconditionally closed only for n<=6, conditional on (star_{n-4})
for n>=7 — exactly Theorem 37's pre-existing scope, unchanged.

This is a real gap that must be flagged (not a fatal error in Theorem 41
itself, which stands), so the approach's Status stays `partial` and the
verdict is CHANGES REQUESTED — the recommended next step (already noted in
the file, unaffected) is to attack h(m) (the separate "T'-cuts-p4" branch)
for general m>=3.

**record_outcome:** advanced (Theorem 41 is real, verified progress; the
overclaim was caught and corrected in-round, not left standing).

## 3. lp-duality-certificate — Verdict: APPROVE (own scope: n=3 upper bound)

Status recorded in file: `solved (scope: the general-marking n=3 upper
bound c(3)<=8/15 only)` — correctly and explicitly NOT claiming the whole
problem. This scoping is honest and accurate.

Given this exact claim was overclaimed twice before (round 25's
mislabeled "case (a)", round 26's false "drop p1<T/2" bonus, both caught
by prior reviewers), I applied maximum scrutiny:

- **Re-derived the four Gap-Filler chamber formulas from scratch.**
  Chamber A (bisect p1, p4): A = p2-p3 = x. Chamber B (bisect p1, p2):
  A = p3-p4 = y. Chamber C (bisect p1,p2,p3): A = p4 = z. Chamber E
  (bisect p1; cut p2 into (p3, x)): A = |x-z|. Each follows cleanly from
  the new `pair-insensitivity-corollary` (A(M∪{v,v})=A(M), a two-line
  parity consequence of the already-certified `odd-run-reduction-lemma` —
  re-derived by hand, correct, elementary). Independently re-verified all
  four formulas against direct sort-and-alternate-sum computation
  (`/tmp/verify_gapfiller.py`, 28,699 random trials landing exactly in the
  target region p1>=T/2, T/15<p2<4T/15): zero mismatches.

- **Re-derived both Farkas certificates algebraically by hand** (not just
  re-read): Case (i) (x-z>u): the combination
  (4u-x-y-z)+(y-u)+(x-z-u)+2(z-u) expands to exactly 0, contradicting that
  it is a sum of 4 strictly-positive terms — confirmed by hand, matches.
  Case (ii) (z-x>u): the combination
  (T/2-x-2y-3z)+4(x-u)+2(y-u)+3(z-x-u) expands to exactly -1.5u,
  contradicting that it is a sum with at least one strictly-positive term
  and all-nonnegative-coefficients — confirmed by hand, matches. Both
  certificates are valid.

- **Confirmed the specific historical counterexample witness
  p=(3/5,9/40,29/200,3/100)** (the exact point that broke round 26's
  rejected "bonus" domain-widening attempt) is now correctly resolved:
  z=3/100 <= u=1/15, so Chamber C succeeds, Phi_C=103/200=0.515<=8/15.

- **Re-checked the four-regime assembly is exhaustive and non-overlapping**
  with no gap at any boundary: (b1) p2<=T/15; (a) p2>=4T/15 (re-checked
  the citation — peels p2 via Theorem B, discharges the reduced 3-element
  instance via `n2-upper-bound-lp-argument` unconditionally, genuinely no
  restriction on p1, confirmed by hand); middle strip split by p1<T/2 vs.
  p1>=T/2 (ordinary dichotomy, no gap). Ran an additional coarse global
  numeric optimizer sanity check (`/tmp/global_check.py`) across the full
  domain (not just region R): no ratio found exceeding 8/15 in 150 random
  markings x up to 4 cuts, worst observed ratio 0.5265 < 0.5333.

**No gap found anywhere in this round's proof.** This is a genuine,
non-numeric, reviewer-certified closure of a real sub-target (the n=3
upper-bound direction only — NOT the n=3 lower bound/achievability
direction, and NOT n>=4, both correctly and explicitly out of scope in the
file's own text). **Certified** `pair-insensitivity-corollary.md` and
`gap-filler-four-chamber-covering.md`.

**record_outcome:** verified-milestone.

## Lemma certifications this round (all verified independently, all CERTIFIED)

- `results/imo-2026-03/lemmas/sigma2-untouched-closure-theorem.md`
- `results/imo-2026-03/lemmas/even-multiplicity-non-maximal-tie-closure.md`
- `results/imo-2026-03/lemmas/pair-insensitivity-corollary.md`
- `results/imo-2026-03/lemmas/gap-filler-four-chamber-covering.md`

## current.md

Updated: Status remains `partial` (whole problem, general n, both
directions, not solved). Added a full round-27 summary paragraph
documenting the n=3 upper-bound milestone (lp-duality-certificate), the
verified Theorem 41 + corrected overclaim (greedy-halving-adversary), and
the verified §7.14/§7.15 (rank-pigeonhole-budget), plus a Next-round
recommendation (push h(m) for general m>=3; attempt (star_3) directly per
§7.15's precise identification; pivot lp-duality-certificate to n=4 or the
n=3 lower-bound direction now that the n=3 upper bound is closed).

## Files touched by this review

- `/home/agentuser/repo/results/imo-2026-03/current.md` (Status kept
  `partial`; round-27 summary appended)
- `/home/agentuser/repo/results/imo-2026-03/approaches/greedy-halving-adversary.md`
  (3 overclaim corrections in place: top summary bullet, the Corollary
  section, the "Round 27 status" Open-gaps entry, and the "Current best"
  Round-27-update note)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/sigma2-untouched-closure-theorem.md`
  (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/even-multiplicity-non-maximal-tie-closure.md`
  (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/pair-insensitivity-corollary.md`
  (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/gap-filler-four-chamber-covering.md`
  (certified)
- `results/imo-2026-03/approaches/.ranking.json` updated via `record_outcome`
  for all 3 slugs (tool-owned, not hand-edited)

## Verdicts summary

- **rank-pigeonhole-budget: APPROVE** (own scope, Claim (A), unaffected;
  this round's §7.14/§7.15 addendum is correct, no overclaim, genuine
  progress on the still-open general-n front)
- **greedy-halving-adversary: CHANGES REQUESTED** (Theorem 41 genuine and
  certified; real overclaim found in the combining Corollary, corrected
  in-round by this reviewer; Status `partial` is accurate)
- **lp-duality-certificate: APPROVE** (own scope, n=3 upper bound, fully
  and rigorously solved, no gap found after maximum adversarial scrutiny)
