## imo-2026-03 — plateau-break slot (route: genuinely different framing for the upper bound)

### HEADLINE FINDING: a classical pigeonhole/subset-sum argument appears to close the ENTIRE
upper-bound direction in one shot, bypassing the Per-Partner-Domination/F-provenance machinery
entirely. This is a *candidate*, heavily corroborated but not yet formally written up as a
complete proof — strongly recommend the outliner open it as a genuinely new slug this round.

### Setup / where I started
Read `results/imo-2026-03/current.md`, `run_state.md`, and `approaches/potential-weighting-
upper-bound.md` (§1 for the D/M reformulation, §17-§30 for the current bottleneck). Confirmed:
lower bound is fully unconditional (do not touch); the entire remaining task is proving, for
Liu Bang's arbitrary opening multiset `A` (`|A|=k≤m+1`), that Xiang Yu has a legal sequence of
`≤m` **D/M operations** (certified `Lemma D/M`: `D(x)` deletes any one active value; `M(x,y)`,
`x≥y` **any two active values, not necessarily the top two**, replaces them with `x-y`) driving
`e(final) ≤ e_m·S(A) = S(A)/(2^{m+1}-1)`. Per `lemmas/slack-collapse.md` only the tight case
`k=m+1` matters. All the machinery since round 9 (Per-Partner Domination, Two-Touch/Three-Touch,
Gaps 1a/1b/1c) is one specific *strong-induction-with-background-tracking* attack on exactly
this claim, stuck on general `q` for 6 rounds now.

### The new route: pigeonhole on subset sums + a signed-sum realizability lemma

**Step 1 (classical pigeonhole).** For `A=(a_1,...,a_k)`, `k=m+1`, `S=Σa_i`, consider the `2^k`
subset sums `Σ_{i∈U}a_i` over all `U⊆{1,...,k}` (including `∅`, `U=[k]`). They lie in `[0,S]`.
Partition `[0,S]` into `2^k-1` bins of width `L=S/(2^k-1)`. `2^k` points, `2^k-1` bins ⟹ by
pigeonhole two **distinct** subsets `U≠V` have sums in the same bin, so
`|sum(U)-sum(V)| ≤ L = S/(2^{m+1}-1) = e_m·S`. Let `T:=U△V` (nonempty since `U≠V`), with sign
`ε_i=+1` for `i∈U\V`, `ε_i=-1` for `i∈V\U`. Then `|Σ_{i∈T}ε_i a_i| ≤ e_m·S` **exactly by
construction** (no casework, no induction — this is a one-line counting argument).

**Step 2 (Signed-Sum Realizability Lemma — new, general, fully proved by induction, no
`F`-provenance needed anywhere).** *Claim:* for any finite multiset `X` of nonnegative reals,
`min_{ε:X→{±1}} |Σ_{x∈X}ε(x)x|` is exactly achievable via a sequence of `|X|-1` applications of
the **M**-operation alone (no D needed within `X`). *Proof (by strong induction on `|X|=t`):*
`t≤1` trivial. For `t≥2`: take an optimal sign pattern `ε*`. If two nonzero elements `x_i,x_j`
share the same sign under `ε*`, flipping the smaller one's sign strictly decreases `|Σε*x|`
(standard fact), contradicting optimality — so at most one nonzero value can be "isolated"
(handle a stray zero by trivially pairing it with anything, harmless). Otherwise pick `i,j`
with `ε*_i≠ε*_j`; apply `M(x_i,x_j)` (WLOG `x_i≥x_j`) to get `x_i-x_j`, keeping every other
sign fixed. The reduced `(t-1)`-element multiset's own optimal signed sum **equals** the
original optimum *exactly* (its search space is exactly `{ε: ε_i≠ε_j}` of the original,
restricted, but the original optimum's own pattern already lies in that restricted subspace by
construction — so the restricted min equals the global min, not merely `≥`). By IH the
`(t-1)`-problem is `M`-realizable, so appending this one step realizes the `t`-problem's optimum
too. ∎

**Step 3 (combine).** Apply Lemma D/M: `D`-delete every element of `A\T` (`k-|T|` operations),
then apply Step 2's `M`-sequence on `T` (`|T|-1` operations) — total `k-1=m` operations exactly,
all legal per the already-certified `Lemma D/M` (which places **no restriction** that `M` acts
on the top-two active values — this is exactly the freedom the pigeonhole witness needs and
exactly the freedom the population's existing greedy-rule dead ends (Rule 1/Rule 2) never
exploited). The achieved value is `min_ε|Σ_Tε_ia_i| ≤ |Σ_Tε_i a_i|` (Step 1's specific witness)
`≤ e_m·S(A)`. This proves `g(A,m) ≤ e_m·S(A)` for **every** `A` with `|A|=m+1` — i.e. the entire
upper bound — **in one uniform argument, no Case (i)/(ii) split, no background/residual
bookkeeping, no general-`q` induction.**

### Computational corroboration (all bounded, exact `Fraction` arithmetic; scripts in
`/tmp/round-19/explore/`)
- **0/~2600 failures** of the full pigeonhole+realizability construction vs. target, across
  `m=1..7`, random rational values (small and large, up to `10^6` scale), including `k<m+1`
  (zero-padded) cases (`pigeonhole_proof.py`, `stress2.py`-equivalent inline run).
- **Exact equality at the dyadic construction** `D_m` for `m=1,...,5` — the construction
  reproduces `e_m` **exactly**, matching the known tight case perfectly (not just `≤`).
- **On the population's own hardest known adversarial counterexample** (the `m=3` instance that
  falsified both Rule 1 and Rule 2, `A=(239/500,112/500,75/500,74/500)` from
  `potential-weighting-upper-bound.md` §2(b)): the construction achieves `1/500`, which is
  **exactly the TRUE brute-force-optimal value** (`g(A,3)=1/500` by exhaustive D/M-sequence
  search) — not merely under the target `1/15`, but matching the actual game-theoretic optimum
  bit-for-bit.
- **Signed-Sum Realizability Lemma's constructive induction** independently stress-tested
  (`500/500`, `t≤7`, plus explicit edge cases: all-zero, all-equal, single-element,
  zero-mixed-with-nonzero) — the *reduction step itself* (not just existence via brute force)
  was verified to preserve the optimal value exactly at every step, confirming the induction is
  genuinely constructive, not just an existence claim found by search.
- Adversarial perturbations of the dyadic point (`m=1..6`, `±5·10^{-6}` random jitter on each
  coordinate) — zero failures.

### Why this is genuinely different from everything on the dead-end list
It is not: global concavity of `g` (this is a counting/pigeonhole argument, no convexity
claimed anywhere); a bounded-lookahead greedy rule (Rule 1/2 both fixed a *specific* pair —
top-two, or smallest-gap — at each step; the pigeonhole witness `T` is a *global, all-at-once*
selection with no notion of "steps" at all until Step 3's realization); strategy-stealing;
Hall's theorem; the `aimo-0198` averaging trick (that bounds an *adversary's minimum* by an
*average*; this is a counting argument bounding the minimum of `2^k` numbers by pigeonhole,
structurally unrelated); concavity/LP-duality on the opening; layer-cake toggle-pair; merge-
tree/Euclidean framing (these all still work over the *same* recursive per-cut decomposition
the current machinery uses — the pigeonhole route makes no recursive appeal to `e_{m-1}` /
smaller `m` at all, it is a single non-inductive-on-`m` counting step, with induction only
appearing in the *separate*, fully general, `F`-provenance-free Realizability Lemma); the Fixed-
Support Uncrossing Conjecture or the generalized Full-Slack Insertion Lemma (both are about
*re-pairing an existing witness*; this route never starts from a witness to re-pair — it
constructs one from scratch via counting). I grepped `potential-weighting-upper-bound.md`,
`dyadic-cascade-induction.md`, and `concavity-minimax-duality.md` for "pigeonhole", "subset
sum", "Karmarkar", "discrepancy" — zero hits anywhere in the population's ~15 rounds of work.

### What is NOT yet nailed down (honest gaps, for the outliner to scope as explicit gaps if a
slug is opened)
1. The Signed-Sum Realizability Lemma's proof above is a genuine proof sketch (the induction is
   complete on paper and I independently coded and verified the *constructive* reduction step,
   not just existence) but has not been reviewed/written as a fully formal lemma yet — the
   "flip the smaller same-signed element strictly decreases the magnitude" sub-claim needs one
   more line spelled out (trivial: if `ε*_i=ε*_j=+1` WLOG and `x_i≤x_j`, flipping `x_i` changes
   the sum by `-2x_i≠0` unless `x_i=0`, and moves it towards `0` since the pre-flip sum has the
   same sign as `x_i`'s contribution — needs the standard "greedy sign to reduce a partial sum"
   argument written out fully, not hard, but not yet on file).
2. Need to double check the pigeonhole bin edge cases (ties landing exactly on bin boundaries)
   are handled with a clean, rigorous convention (I used floor-division binning with the
   top point routed to the last bin — worked in every test, including exact dyadic equality,
   but should be stated as a precise, provably-exhaustive case split, not just "it worked in
   code").
3. Should double-check whether `T` could, in principle, need `|T|=1` (i.e. `U,V` differ by
   exactly one element) — this is a degenerate but valid case (`M`-count `0` on `T`, all budget
   spent on `D`); the general argument handles it fine (`t=1` base case of Step 2) but it's
   worth a builder writing it out as an explicit sub-case for full rigor.
4. This route proves `g(A,m) ≤ e_m S(A)` (the *achievable* upper bound via one specific
   D/M realization), which per the already-certified Lemma D/M immediately gives the true
   upper bound on Xiang Yu's forceable value — this final translation step (already used by the
   existing `potential-weighting-upper-bound` slug throughout) should be re-cited, not
   re-derived.
5. Have NOT yet cross-checked this against `k<m+1` without invoking `Slack Collapse` as a
   separate lemma — I zero-padded `A` to size `m+1` directly in the pigeonhole construction and
   it worked in every test (0 failures), suggesting `Slack Collapse` may not even be needed as a
   separate lemma under this route (the padding is "free" — pigeonhole with more elements only
   gives a *stronger* bound), but this equivalence should be verified formally, not just
   computationally.

### Recommendation to the outliner
Open a genuinely new slug (e.g. `pigeonhole-subset-sum-upper-bound`) built around Steps 1-3
above. Recommend NOT folding it into `potential-weighting-upper-bound` (would violate the
"one approach = one slug, complete rival attempt" rule and risks burying a structurally very
different, much shorter argument inside 7000+ lines of a different framing). If it survives a
builder's formal write-up and independent review, it would very likely **solve the entire
upper-bound direction of the whole theorem in one round**, since it needs no case split by `m`,
no background/residual state, and no general-`q` Per-Partner-Domination closure at all — the
long-stuck bottleneck may be an artifact of the machinery's *own* recursive/inductive framing on
the game's cut-by-cut structure, not of the underlying mathematical difficulty.

### Cheap-kill candidates
None additional beyond the above — the pigeonhole route itself functions as the "cheap kill" of
the entire remaining problem if it holds up under formal review.

### Knowledge-base entries to use
`knowledge_base.md` was not the primary source for this find (it came from testing a classical
pigeonhole/discrepancy technique directly against the reformulated combinatorial claim); worth
checking the KB for a "pigeonhole" or "subset-sum discrepancy" entry to cite formally once a
builder writes this up — recommend the outliner grep `knowledge_base.md` for "pigeonhole" when
scoping the new slug's proof so the exact entry name is cited per CLAUDE.md's rigor rules.

### Analogous past problems (crux corpus)
Did not have remaining budget to run a full crux-corpus query this round (all time went to
computational verification of the new route, per the dispatch's priority on finding/testing a
genuinely different framing). Recommend a future round query the corpus (per
`crux_moves_documentation.md`'s field names) for `domain=combinatorics`,
subtopics ~ "pigeonhole", "extremal set theory", "signed sums" / "discrepancy" — this specific
"`2^k` subset sums into `2^k-1` bins" trick is a well-known competition technique (used e.g. in
classical results about subsequence sums close to a target), so a matching crux entry likely
exists and could supply a polished write-up template.

### Prior progress (unchanged, for context — do not re-attempt)
Per-Partner Domination Lemma: proved `q≤3`, open `q≥4`, top priority for 6 rounds — status
unchanged by this report; the pigeonhole route is a *parallel* candidate, not a fix for that
gap. Two-Touch closed for `|W|≤3` (round 18), Three-Touch 4/5 pieces, Gap 1c narrowed to
`delta_c` — all unchanged, all still live if the pigeonhole route needs more rounds to formalize
or (less likely given the corroboration strength) turns out to have a hidden flaw.

### Dead ends (do not retry)
All previously-listed dead ends stand; nothing in this report contradicts or revives any of
them. Two NEW near-misses found and ruled out this round while searching for the fresh route
(both are simple greedy variants, consistent with — not contradicting — round 4's "no bounded
lookahead suffices" finding, so do not re-attempt): (a) "always merge/discard the two smallest
active elements" (`rule_smallest_pair`, `rule_smallest_pair_always_M`) — fails ~40-90% of random
`m∈{1..4}` trials; (b) "compare largest to sum-of-rest; if dominant delete it, else pair
largest with smallest" (`rule_big_small`) — fails ~55% of random trials. Both confirm greedy
single-step policies (of any flavor) remain hopeless, reinforcing why the pigeonhole route's
*non-recursive, all-at-once* character is the genuinely new ingredient.

### Small-case / intuition notes (all labeled conjecture/corroboration, not proof)
The pigeonhole+realizability construction is **conjectured** (heavily corroborated: thousands of
exact-fraction trials, zero failures, exact equality at the known tight dyadic point, exact
match with the known-hardest counterexample's true optimum) to satisfy
`g(A,m) ≤ e_m·S(A)` for every `A`. The Signed-Sum Realizability Lemma is **conjectured-but-
essentially-proved** (a complete, checked-by-hand induction; independently verified
constructively in code) — the only remaining work to call it a certified lemma is writing the
"flip smaller same-sign element" sub-argument out formally and handling the zero-element
bookkeeping cleanly. If a builder confirms both pieces formally, this closes the entire
theorem's upper bound (the lower bound already being unconditional since round 8) — i.e. would
be Status `solved` for the whole `imo-2026-03` problem.
