## imo-2026-03 (lens: non-crossing matching+deletion conjecture, upper-bound Case (ii), k=m+1)

### 1. Precise restatement of the conjecture (from `potential-weighting-upper-bound.md` §7.3)

Setup (§6 "one-shot tail"): given a sorted list `Y=(y_1≥…≥y_p)` (a residual after some
chain-prefix, or the original `A` itself at `c=0`) and a budget `b` (cuts remaining), a
**one-shot allocation** is a choice of:
- a set of disjoint **matched pairs** `(y_i,y_j)`, `i<j`, each replaced by the single value
  `y_i−y_j` (this is exactly the `M`-operation of the certified Lemma D/M, applied only to
  *original* elements, never to a value produced earlier in this phase — no cascading);
- a set of **deleted** singletons (the `D`-operation, Fact 5/Slack-Collapse style — simply
  removed);
- the rest **kept** untouched;
subject to `(#matched pairs)+(#deleted) ≤ b`. The **value** of a selection is `e` (alternating
signed sum, `+,−,+,…`, of the final multiset in sorted-descending order) of {kept elements} ∪
{match differences}. Define `OPT(Y,b) := min` of this value over **all** selections
(exponentially many — crossing or not).

**Non-crossing matching+deletion conjecture (numerically supported, NOT proved, per the file):**
`OPT(Y,b)` is always attained by some selection whose matched-pair set is **non-crossing** —
i.e., drawing an arc for each matched pair over the linear order `1,…,p`, no two arcs `(i,j)`,
`(i',j')` satisfy `i<i'<j<j'` (properly interleaved). Nesting (`i<i'<j'<j`) and disjointness
(`j<i'`) are both allowed; arcs may skip over deleted or kept points freely. Restricting the
search to non-crossing selections (a Catalan-sized, `O(4^p)`-ish space via the classical
non-crossing-partition recursion, vs. exponential-in-all-matchings for the unrestricted search)
would let Fact 3 (block extraction) turn Step 2 of §6 into a closed-form expression.

### 2. Fresh verification performed this round (exact integers/Fractions, independent code)

Wrote an independent exact (`fractions.Fraction`) brute-force harness
(`/tmp/round-6/ncmd_check.py`, `/tmp/round-6/ncmd_argmin.py`, `/tmp/round-6/ncmd_argmin2.py`):
`full_search(Y,budget)` enumerates **every** deletion-subset × every perfect matching of the
survivors (unrestricted, crossing allowed) and returns the true min; `noncrossing_search`
does the same but restricts matchings via the standard non-crossing recursion (peel the first
unmatched point, either leave/delete it, or pair it with some later point `k`, recursing
independently on the "inside" `(first,k)` interval and the "outside" tail — both must have even
size to admit a perfect matching, exactly the classical Catalan/Dyck-path recursion).

- **400 fresh random trials**, `p=3..6`, random integer values (1–200), random budget
  `b∈{1,…,p}`: **zero mismatches** between `full_search` and `noncrossing_search`. This
  independently reproduces (with a from-scratch implementation, not reused code) the file's
  own 560+-trial claim — the conjecture continues to hold on this fresh sample.
- **Re-verified the file's own hard counterexample** `Y=(43,33,20,16,11,8,2)` at every budget
  `b=0,…,6`: `full_search=noncrossing_search` exactly at each (`19,11,7,3,3,1,1` respectively) —
  matches the file's claim ("full=non-crossing=7 at b=2, matching across all budgets 0..6
  tested") exactly, independently re-derived.
- Did **not** push to `p=7,8` with full brute force (the file's own open item, §6's "re-run at
  m=7,8") — the unrestricted `full_search` is `O(2^p·p!!)`-ish and became slow beyond `p≈6-7`
  in this quick check; flagging this as still open/untested, not resolved by this round.

**Conclusion:** the conjecture is confirmed again, freshly, at bounded scale. This is
evidence, not proof — same status as before.

### 3. Diagnosis of *why* local pairwise uncrossing fails but the global non-crossing optimum
still wins (the counterexample `Y=(43,33,20,16,11,8,2)`, `b=2`)

Reconstructed the argmin exactly (`/tmp/round-6/ncmd_argmin.py`, `ncmd_argmin2.py`):

- **The file's local-exchange test** fixes the *support* — the 4 points `{43,16,11,2}`
  (indices `0,3,4,6`) — and the *rest* `{33,20,8}` as permanently **kept, untouched**, then
  compares only the **3 possible matchings on that fixed 4-point support**: crossing
  `(43,11),(16,2)`→`e=15`; nested `(43,2),(16,11)`→`e=25`; disjoint `(43,16),(11,2)`→`e=25`.
  Crossing wins *within this frozen support*.
- **The true global optimum at `b=2` is `7`**, strictly better than all three local options,
  and — critically — it is **not reached by re-pairing the same 4 points at all**. I found two
  distinct exactly-tied globally-optimal selections:
  - `kept={33,16,2}`, matched `(43,11)→32,(20,8)→12` → final `{33,32,16,12,2}`, `e=7`
    (this particular tied optimum, arcs `(0,4)` & `(2,5)`, is itself a **crossing** pair by the
    index-interleaving definition, `0<2<4<5` — i.e. not every optimal witness is non-crossing).
  - `kept={33,8,2}`, matched `(43,11)→32,(20,16)→4` → final `{33,32,8,4,2}`, `e=7` (arcs
    `(0,4)` & `(2,3)`, which **are** non-crossing/nested — this is the witness that actually
    satisfies the conjecture's "some non-crossing selection attains OPT" claim).
- **The structural point:** both global optima *change which points are matched vs. deleted vs.
  kept relative to the local test's frozen support* — the winning move replaces `20` (which the
  local test held fixed as part of "the rest") with a match partner, and drops `16` (which the
  local test used as a match input) to "kept" instead. **The real gain is not from re-crossing
  two already-chosen arcs while freezing everything else — it comes from re-choosing which
  elements participate in a match at all.** A proof strategy that only ever compares
  alternative *pairings of a fixed support* (the natural "local uncrossing exchange" move) can
  never see this — it needs to compare across different supports simultaneously, which is a
  strictly larger move.

**Implication for the outliner:** this rules out not just pairwise-uncrossing-with-fixed-rest,
but the whole *family* of exchange arguments that hold "the rest of the selection" fixed while
locally perturbing one match. Any working proof technique needs to be a genuinely global
comparison (e.g. compare two entire selections differing in support, not one arc swap), which
points toward an **inductive/DP construction of an explicit non-crossing optimum from scratch**
(build it top-down or bottom-up, case-splitting exhaustively on the fate of one extreme element
at a time — keep / delete / match-to-some-`j`, all `j` considered, not a fixed "obvious"
partner) rather than a "take any optimal selection and repair its crossings" argument.

### 4. Survey of alternative proof techniques (knowledge_base.md + crux corpus)

- **`knowledge_base.md`**: no entry titled "non-crossing matching," "rearrangement
  inequality," "exchange argument," or "assignment problem" as a dedicated technique. The
  closest generic entries: **Hall's marriage theorem / SDR** (bipartite matching existence —
  not directly useful here since we need an *optimality* result, not existence of *a*
  matching); the **"piecewise-concavity smoothing"** entry (Algebra & Polynomials) is a
  structurally similar *shape* of argument — reduce a minimization over a continuous/discrete
  parameter to checking breakpoints/extreme configurations via concavity — worth flagging as a
  candidate *shape* (not a ready-made tool): if `e` restricted to matchings-on-a-fixed-support,
  viewed as a function of "how much crossing" is introduced, were concave/monotone in some
  natural parameter, its minimum would sit at an extreme (non-crossing) configuration — but this
  is speculative and untested, and §3 above shows the naive fixed-support version of this idea
  is exactly what fails. The **Monotone-subsequence / Erdős–Szekeres / patience-sort** entry is
  a candidate combinatorial-structure tool if the eventual proof ends up needing to organize
  elements by rank interactions, but no direct fit was found.
- **Crux corpus search** (`domain=combinatorics`, subtopics `inequalities-SOS-and-convexity`,
  `extremal-principle`, `games-and-strategy`, `processes-and-algorithms`, plus free-text search
  across all domains for "non-crossing," "rearrangement inequality," "exchange argument,"
  "crossing pair," "adjacent swap," "uncrossing"): **200+ cruxes mention "matching" but almost
  all are Hall's-theorem/bipartite-matching-existence problems, unrelated to this optimality
  question.** The one genuinely on-topic hit is **`aimo-0459`** (algebra,
  `inequalities-SOS-and-convexity`): *"To bound a cyclic sum of two-variable terms, sort the
  variables and use the rearrangement inequality to re-pair them into the extreme
  (smallest-with-largest) pairing."* This is the classical sort-and-pair-extremes rearrangement
  idea — structurally the right *flavor* (global sort-based pairing beats an arbitrary one) but
  **not analogous enough to adapt directly**: rearrangement inequality applies to a *sum of
  products of a fixed pairing structure* varying only the assignment, with a fixed number of
  terms and no signed/alternating global-rank dependence; our objective's sign of each surviving
  element depends on its *rank among all survivors*, which changes non-locally when any element
  is deleted or replaced by a match-difference — this global-rank coupling is exactly what
  breaks simple rearrangement-style or local-exchange arguments (§3). No other crux (across
  `aimo-0003`, `aimo-0763`, `aimo-0872`, `aimo-0910`, `aimo-0999`'s crossing-chord entries, or
  `aimo-0597`'s crossing-to-non-crossing rewiring) solves an *optimization* over
  matchings/pairings with a globally-rank-dependent objective; they are either existence
  results (Hall) or purely local invariants (adjacent-swap monovariants) or geometric
  non-crossing facts unrelated to optimizing a signed alternating sum. **Verdict: no genuinely
  analogous crux found; do not force one of these as a template.**

### 5. Cheap-kill / structural candidates before a heavy global proof

- **None obvious as a full replacement**, but two structural facts worth checking cheaply before
  a heavy DP/induction write-up:
  1. **Parity/count check**: in every tied-optimal witness found so far (the two above, plus the
     file's own examples), the *number of matched pairs* used is exactly `min(b, ⌊p/2⌋)`-ish
     (budget fully spent on matches, not deletions) whenever a beneficial near-tie exists —
     worth checking systematically whether an optimal selection ever benefits from a deletion
     when `p` is large enough to also match (a cheap structural fact that could simplify the
     search space before attempting non-crossing DP).
  2. **Block-extraction compatibility (Fact 3)**: since matched/kept results must be
     re-sorted globally, and Fact 3 says `e(F)=e(X)+(-1)^{|X|}e(Y)` for a *dominant block* `X`
     (top-ranked elements) — check whether the *largest* original element `y_1` is **always**
     either kept-untouched or matched with something that leaves it (or its result) as the new
     top rank, never "buried" mid-stack by a match producing a larger competing value elsewhere.
     If `y_1`'s fate can be resolved first and cleanly peeled via Fact 3 (dominant-block style),
     it converts a global rank-coupled problem into a genuine top-down induction on `p` — this
     is the natural next move given the counterexample's own tied optima both keep or use `43`
     (the top element) as one match-input, never buried it.

### 6. Knowledge-base entries to use (for the outliner)

- **Lemma D/M** (`lemmas/dm-operation-reformulation.md`) — defines the `D`/`M` operations this
  whole sub-problem is phrased in terms of; already certified.
- **Facts 1–5** (`lemmas/insertion-and-cascade-facts.md`, `lemmas/dominant-extraction.md`) —
  Fact 3 (block extraction) is the most promising lever for a top-down induction (§5.2 above);
  Fact 4 (insertion bound) already shown too lossy alone elsewhere in the file, but may combine
  with a non-crossing DP as a per-step bound rather than the whole argument.
- **Slack Collapse** (`lemmas/slack-collapse.md`) — already reduces scope to `k=m+1`; not
  itself a tool for this sub-gap but the reason this is *the* remaining case.
- No entry in `knowledge_base.md` is a ready-made "non-crossing matching optimality" theorem;
  the closest generic shape is "piecewise-concavity smoothing" (Algebra & Polynomials section),
  flagged above as a speculative shape, not a citable tool for this exact setting.

### 7. Analogous past problems (crux corpus)

- **Best (partial) match: `aimo-0459`** (algebra, `inequalities-SOS-and-convexity`) — rearrangement-inequality sort-and-pair-extremes move. Same *flavor* (global sorted pairing beats
  arbitrary pairing) but not adaptable directly: no alternating/rank-dependent sign structure
  and no deletion option in that problem.
- **No strong match.** Searched combinatorics subtopics `games-and-strategy`,
  `processes-and-algorithms`, `extremal-principle`, `inequalities-SOS-and-convexity`, plus
  free-text "crossing"/"matching"/"rearrangement"/"exchange" across all 2434 cruxes; nothing
  else solves an optimal-matching-with-global-rank-coupled-objective problem. Honestly report:
  **this specific combinatorial-optimization structure (minimize a globally-rank-signed
  alternating sum over matchings+deletions) does not appear to have a close analog in the
  corpus** — the outliner should expect to build a bespoke argument, not adapt a crux.

### 8. Prior progress / dead ends (unchanged from the file, re-confirmed this round)

- **Prior progress:** Slack Collapse (certified) reduces the entire upper-bound induction to
  `k=m+1`. Within that, the chain-prefix + one-shot-tail family (§6) is numerically solid;
  Fact-3-based closed form is available *if* the non-crossing conjecture is proved.
- **Dead end, re-confirmed, do not retry:** local pairwise uncrossing-exchange with the rest of
  the selection held fixed (§7.3 of the file) — re-derived independently in §3 above; the
  precise failure mode is now sharper: it fails not merely because the wrong two arcs get
  compared, but because **the globally optimal fix changes which elements are chosen to
  participate in a match at all**, a move class the local-exchange technique structurally
  cannot express.
- **Dead end, re-confirmed:** literal "sorted-adjacency" (§7.2) — strictly weaker than
  non-crossing, already falsified with exact counterexamples; not re-tested here since it is a
  strict special case of non-crossing and non-crossing itself is not yet disproved.

### 9. Small-case / intuition notes (labeled conjecture, not proof)

- Every tied-optimal witness examined (this round's and the file's own) keeps or matches the
  **largest** element `y_1` in a way that leaves it (or its match-result) at or near the new top
  rank — suggestive that an induction peeling `y_1` first (three-way case split: kept / deleted
  / matched-to-some-`j`) could be the right shape for a global proof, rather than one that
  starts from an arbitrary interior crossing pair. This is a conjecture/heuristic from limited
  examples, not verified as a general pattern.
- The core obstruction to any clean DP: `e`'s alternating sign on a surviving element depends on
  its rank **among all final survivors**, which is a global, not local, quantity — this is
  exactly why interval-additive DP (the standard tool for non-crossing-matching optimization,
  e.g. matrix-chain-multiplication-style problems) does not obviously apply here without
  carrying extra state (something like a running signed partial sum, i.e. exactly the "richer
  non-scalar IH" the round-4/5 induction-loading postmortems already identified as missing).
  This suggests the non-crossing conjecture's eventual proof, if found, will look like a DP
  whose state is not just "the sub-interval" but "the sub-interval **plus a running rank/sign
  offset**" — a concrete, checkable hypothesis for the next round to test on the smallest known
  counterexamples before committing to a general write-up.
