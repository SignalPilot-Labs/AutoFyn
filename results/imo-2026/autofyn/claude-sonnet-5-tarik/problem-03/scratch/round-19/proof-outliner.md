## imo-2026-03

### Summary of this round's reconciliation

Three explorers scouted in parallel this round. I read all three reports, independently re-verified
their two most consequential claims with my own fresh code (not reusing any explorer's harness) before
committing anything to the population:

1. **`math-explorer-general-q.md`** (Generalized Touch-Bound closed form, `|C|=k` general): plausible,
   internally consistent (the `2^k`/`2^{m+1}-1`-style threshold identification is sound reasoning), no
   independent re-derivation attempted by me (would require re-running the explorer's own harness at
   scale, out of scope this round) — folded into `potential-weighting-upper-bound.md` as new §31,
   explicitly marked conjectural/corroborated-only.
2. **`math-explorer-27-2-d.md`** (candidate complete proof of §27.2(d)'s KEEP `b0<=w1` target at
   `|W|=3`): I independently re-checked the *reduction logic* (min-of-5-terms `>=Y` iff every term
   `>=Y` — elementary, confirmed) but did NOT re-derive the 5 case-split sub-proofs by hand myself
   (that is exactly the builder/reviewer's job per the file contract) — folded into
   `potential-weighting-upper-bound.md` as new §32, explicitly flagged as "strong candidate proof, not
   yet independently re-derived by anyone besides the reporting explorer."
3. **`math-explorer-plateau-break.md`** (pigeonhole/subset-sum route, a genuinely different,
   non-recursive framing for the WHOLE upper bound): **I independently verified this myself with fresh
   Python/`Fraction` code before deciding whether to open a slug** (per the dispatch's explicit
   instruction to judge soundness, not just trust the explorer). Result: **Step 1 (pigeonhole) is
   solid and essentially proved** (0/500 fresh re-verification); **Step 2 (Signed-Sum Realizability
   Lemma) has a genuinely FALSE specific proof mechanism** — I found a concrete counterexample
   (`X=(36,48,4)`) to the explorer's claimed "at most one non-tied same-sign element" sub-argument,
   confirmed by running the explorer's algorithm exactly as described (fails `2351/3000` fresh trials).
   **However, the Lemma's underlying CONCLUSION (existence of some realizing merge order) still appears
   true** — I ran a full brute-force search over *every* possible merge order (not the flawed specific
   algorithm) and found 0/300 violations, including on the counterexample instance itself (a different
   merge order, `M(48,36)=12` then `M(12,4)=8`, does realize the true optimum `8`). **Net judgment: this
   route is structurally sound and worth a build slot, but its central open gap (Step 2) is genuinely
   open — not close to done — and must be reported honestly as such, not as a near-complete proof.**
   This satisfies CLAUDE.md's diversity requirement (a genuinely different framing, non-recursive,
   attacks the whole theorem in one shot) and the plateau-break mandate (the shared background-tracking
   machinery has been stuck on the same DELETE-vs-MATCH wall for 6 consecutive rounds, 14-18) — opened
   as new slug `pigeonhole-subset-sum-upper-bound`.

No approach was retired or RETHINK'd this round. `dyadic-cascade-induction` and `concavity-minimax-duality`
remain benched (re-confirmed no new leverage this round — neither explorer touched the lower-bound
direction, which is already fully unconditional since round 8, nor found anything for the benched
approaches' own machinery). `elementary-exchange-smoothing` remains retired.

### Ranker note
`mcp__approach-ranker__sample_approaches(imo-2026-03, k=5)` currently reports `total_approaches: 4` —
the newly-written `pigeonhole-subset-sum-upper-bound.md` file is not yet visible to the ranker (no
register tool is available to this role; only `sample_approaches` is exposed to proof-outliner per this
session's tool list). The outline-reviewer or downstream tooling should pick up the new file from disk
when it next scans `results/imo-2026-03/approaches/`.

---

pigeonhole-subset-sum-upper-bound: new
Target: the whole theorem's upper-bound direction — for every `m`, Xiang Yu can force
`e(final) <= e_m*S(A)` for Liu Bang's opening `A` (`|A|=m+1` after Slack Collapse), for every `m`/`n`
simultaneously (no case split by `m`, no Case (i)/(ii)).
Technique: Pigeonhole/extremal principle (`knowledge_base.md` Combinatorics, "Pigeonhole / extremal
principle" entry) on the `2^k` subset sums of `A`, combined with a constructive realization into a
legal D/M-operation sequence via the already-certified Lemma D/M (`lemmas/dm-operation-reformulation.md`,
imported, not re-derived) — genuinely different from `potential-weighting-upper-bound`'s recursive
background-tracking machinery (no induction on `q`/background size at all).
Skeleton:
  1. Import Slack Collapse (`lemmas/slack-collapse.md`) to restrict to the tight case `k=m+1` — by
     citation.
  2. Pigeonhole step (PROVED, outliner-reverified 0/500 fresh): partition `[0,S]` into `2^k-1` bins,
     `2^k` subset sums force a same-bin collision `U!=V`, giving a signed-sum witness `T=U△V` with
     `|sum_T eps_i a_i| <= S/(2^{m+1}-1) = e_m*S`, no casework.
  3. Signed-Sum Realizability Lemma (OPEN — see Key lemmas below) — turns the abstract sign-pattern
     witness into an actual sequence of M-operations on `T`.
  4. Combine via Lemma D/M: D-delete `A\T` (legal, no restriction), then M-merge `T` per Step 3 — total
     `m` operations, achieved value `<= e_m*S(A)`.
  5. Import the already-unconditional lower bound (`lemmas/all-cycles-resolution.md` +
     `lemmas/superincreasing-no-early-zero.md`) — by citation — to close the whole theorem.
  6. State and verify the final answer `c(n)=2^n/(2^{n+1}-1)` explicitly, citing the dyadic construction
     already established in `dyadic-cascade-induction`.
Key lemmas (claim + mechanism):
  - Pigeonhole margin bound — PROVED: `2^k` points, `2^k-1` bins, elementary counting, no mechanism
    needed beyond the definition of pigeonhole.
  - Signed-Sum Realizability Lemma (OPEN, the sole gap on this route's critical path): for any
    nonnegative multiset `X`, `min_eps |sum eps(x)x|` is achieved by SOME sequence of `|X|-1`
    M-operations — because (conjectured mechanism, not yet correctly proved) the sign-optimal pattern's
    binary merge-tree can always be built by choosing, at each step, SOME (not a fixed-rule) pair of
    opposite-signed elements whose merge preserves the reduced instance's own optimum equal to the
    original. The explorer's specific candidate mechanism ("merge same-sign-tied pairs to 0, else merge
    an opposite-sign pair, contradiction if a same-sign pair is untied") is FALSIFIED (see Watch out
    for) — a correct mechanism/invariant for "which pair is safe next" is still needed.
Open gaps:
  1. (Highest priority) Prove the Signed-Sum Realizability Lemma with a correct mechanism — candidate
     directions: sorted-descending processing with a provenance-consistent running accumulator, or a
     strong induction characterizing precisely which opposite-signed pair is always safe to merge next
     (existence, not "any pair works," is all that's needed — the outliner's full-search re-verification
     shows existence holds, 0/300, even on the instance where the explorer's specific rule fails). A
     fresh crux-corpus query (domain=combinatorics, subtopics ~ "signed sums"/"partition problem"/
     "differencing method") has not yet been run for this specific lemma.
  2. Formalize the pigeonhole bin-boundary tie-handling as an exhaustive case split (mechanical).
  3. Verify/replace the "zero-pad to size m+1" ad hoc argument by simply citing Slack Collapse directly
     (already imported in skeleton step 1) rather than re-deriving padding separately.
  4. Once gap 1 closes, spell out the `|T|=1` degenerate sub-case explicitly (all-D, zero M-operations).
Cases to cover: none beyond the single tight case `k=m+1` (Slack Collapse disposes of `k<m+1` for free)
— this route's structural appeal is that it needs no further case split by `m` or by background size.
Watch out for:
  - The explorer's specific "at most one non-tied same-sign element under the optimal sign pattern"
    sub-claim is FALSE — concrete counterexample `X=(36,48,4)`: true optimum `8` at
    `eps*=(+,-,+)` (`36-48+4=-8`), where `36` and `4` share sign `+1` and are NOT tied, and flipping the
    smaller (`4`) makes the magnitude strictly worse (`8` -> `16`), contradicting the claimed
    "flip-improves" mechanism. Running the explorer's algorithm exactly as described fails `2351/3000`
    fresh trials. Do NOT resurrect this specific mechanism without fixing the underlying invariant — a
    correct proof needs a genuinely different argument for choosing which pair to merge next (the
    counterexample instance IS realizable via a different order: `M(48,36)=12` then `M(12,4)=8` — so the
    Lemma's conclusion is not refuted, only this specific proof of it).
  - Do not conflate this route's "some merge order exists" claim with the round-4 dead end ("no fixed
    lookahead depth suffices") — the round-4 dead end is about a single FIXED rule always working; this
    route only needs EXISTENCE of some order, a strictly weaker and different claim not covered by that
    dead end.
  - Do not port constructions between this slug and `potential-weighting-upper-bound.md` — keep the two
    frameworks strictly separate per the single-approach-single-slug rule.
  - If Step 2 (Realizability) is eventually proved false in general, Step 1 (pigeonhole) remains a
    correct, reusable fact regardless — do not let a failure of Step 2 be read as invalidating Step 1.

potential-weighting-upper-bound: advance
Target: same as always — Per-Partner Domination / Two-Touch / Three-Touch closure at general `q`,
closing the whole upper-bound direction via the recursive background-tracking machinery (§17-§32).
Technique: strong induction on background/list size with DELETE/KEEP/MATCH trichotomy (Generalized
Multi-Background Peeling Lemma), unchanged from prior rounds.
Skeleton: unchanged from round 18's §29-§30, extended this round with two new sections:
  - New §31 (Generalized Touch-Bound Lemma, conjectural, `|C|=2` general-`q` closed-form candidate) —
    see Key lemmas below.
  - New §32 (candidate complete proof of §27.2(d)'s KEEP `b0<=w1` target at `|W|=3`) — see Key lemmas
    below.
Key lemmas (claim + mechanism):
  - Generalized Touch-Bound Lemma (§31, CONJECTURAL, corroborated only): `OPT_{+1}(C,W)` with `|C|=k`
    equals the min over selections touching `<=2k` raw elements of `W` (`sigma=-1` mirror: `<=2k+1`) —
    because (conjectured, untested proof route) any wider-touch selection is dominated by a `<=2k`-touch
    alternative via a redundancy-elimination argument generalizing the certified Three-Bound Domination
    Lemma's own `k=1` instance. At `k=2` (needed for `A_{3,l}` itself), if proved, replaces the entire
    open-ended induction-on-`q` with ONE finite, `q`-independent case analysis (`O(q^4)` candidates).
    NOT proved — no attempt at the induction-on-`|C|` proof has been made yet (open gap).
  - §32's target `w1-ThreeTouch(b0,rest) >= TwoTouch(b0,W)` at `|rest|=2`: STRONG CANDIDATE PROOF via a
    5-term reduction (min-of-terms identity, elementary and re-checked) plus a new Two-Variable
    Reflection Bound sub-lemma (`w1-|b0-w| >= |b0-(w1-w)|` for `0<=b0,w<=w1`, 3-case elementary proof) —
    because each of ThreeTouch's 5 candidate terms is individually dominated by an explicit TwoTouch
    candidate witness, mirroring the population's established per-term-domination methodology. NOT yet
    independently re-derived by the outliner or reviewer — needs a builder to formalize + a reviewer to
    check each of the 5 sub-cases from scratch before certification.
Open gaps: §31's Generalized Touch-Bound Lemma proof (induction on `|C|`, not attempted); §31's finite
`touch<=4` case analysis (not attempted); §32's 5 per-term sub-proofs (candidate, needs independent
re-derivation); §32's Two-Variable Reflection Bound (candidate, needs independent re-derivation); Gap 1c
case (a)'s `delta_c` bound (unchanged, still fully open); Three-Touch's own MATCH branch (§30.2,
unchanged, still fully open, 3 routes refuted).
Cases to cover: §32's 5 per-term cases are explicit (delete-all, keep-`w2`, keep-`w3`, match, keep-all)
— each needs independent verification, none may be skipped.
Watch out for: do NOT write §32's consequence ("Two-Touch fully proved at |W|<=3") into `current.md` or
any headline claim until the reviewer independently confirms §32.1-§32.4 by hand — this is the EXACT
overclaim pattern round 18's reviewer already caught once on this precise target; a corroboration count
is not a substitute for an actual independently-checked proof. Do NOT conflate §31's new `touch<=4`
threshold with the already-dead `touch<=2` formula at `|C|=2` (18-24% failure, different threshold,
different claim).

dyadic-cascade-induction: advance (benched, reconfirmed)
Target: unchanged — the lower bound against arbitrary openings (already fully unconditional against the
dyadic construction since round 8; the file's own remaining scope is synthesis/writeup once the upper
bound closes).
Technique: unchanged (D/M-completeness + cascade induction).
Skeleton: unchanged from round 8-18 (no new content this round — neither math-explorer this round
touched the lower-bound direction).
Key lemmas: none new this round.
Open gaps: none newly opened; the milestone lower-bound result stands, unconditional. Kept benched (no
concrete open task) per the standing rule since round 9 — re-activate only for a genuinely new angle or
final synthesis once the upper bound closes.
Cases to cover: none (benched).
Watch out for: do not re-attempt the all-cycles closure (done, round 8 milestone) — nothing this round
changes that.

concavity-minimax-duality: advance (benched, reconfirmed)
Target: unchanged — Distinct-Bucket Lemma / Local Claim (would only re-derive the already-unconditional
lower bound if closed, no new leverage on the theorem's actually-open items).
Technique: unchanged (token-labeled D_m-specific bucket argument).
Skeleton: unchanged, no new content this round.
Key lemmas: none new this round.
Open gaps: the Local Claim (unchanged, still open, still lower-priority than every item in
`potential-weighting-upper-bound` or the new pigeonhole route, since even a full closure gives no new
leverage on the currently-open upper-bound gap).
Cases to cover: none (benched).
Watch out for: do not un-bench without a genuinely new A-generic (non-superincreasing-specific) idea —
unchanged standing rule since round 9-11, reconfirmed again this round (neither explorer touched this
approach's machinery).

build set: pigeonhole-subset-sum-upper-bound, potential-weighting-upper-bound
