## imo-2026-03

potential-weighting-upper-bound: advance
Target: Determine c(n) = 2^n/(2^{n+1}-1) as the answer to "largest c Liu Bang can guarantee," proving
both the upper bound (Xiang Yu can prevent Liu Bang from doing better) and the lower bound (the dyadic
construction achieves it), for ALL positive integers n. (Lower bound direction is already fully,
unconditionally proved since round 8 — `g(D_m,m)>=e_m*S(D_m)` for every m. This approach carries the
entire remaining upper-bound direction, reduced since round 12 to Claim A via the Non-Matching-Witness
Criterion, further reduced since round 13-16 to 3 named gaps: 1a, 1b, 1c.)
Technique: Reduction chain (peeling DP + KEEP/DELETE/MATCH trichotomy on sorted order statistics) +
strong induction on list size / recursion depth, using certified lemmas (Rank-Extraction, Shrink-List
Monotonicity, Lemma P duplicate-pair invariance, Three-Bound Domination, Insertion-Difference Identity,
Delete-Suffices-Insertion-Domination) as building blocks. Route unchanged this round — this round is a
reconciliation of three explorer findings into one clearer picture, not a new mechanism.

Skeleton (updated, §27 of the approach file):
  1. Reduce the theorem to Claim A / SAR at scope |B|<=1 — DONE (round 8-12, certified).
  2. Prove Non-Matching-Witness existence on the non-dominated prefix, split into Gaps 1a/1b/1c —
     ongoing since round 13.
  3. NEW this round (§27.1): Gap 1b's general inductive step is algebraically IDENTICAL (via the
     certified KEEP-branch closed form at h=0) to the DELETE-vs-KEEP half of Gap 1a's own
     Deletion-Suffices-for-k*/Per-Partner-Domination conjecture at general q — proving the latter
     gives the former's KEEP half for free at every recursion depth. The DELETE-vs-MATCH half remains
     open and is now understood to be shared, load-bearing content across Gap 1a's general-q closure,
     Gap 1b's induction, AND (structurally, not proved identical) Two-Touch's own Match-Branch
     Domination sub-piece — three faces of one mechanism, not three independent problems.
  4. NEW this round (§27.2): a "Three-Touch" (touch<=3) closed-form candidate now exists for Two-Touch's
     missing sigma=-1 mirror (KEEP branch b_0<=w_1 sub-case) — 0/3480 + 0/1239 violations, unproved,
     recommended proof route: same induction-on-|W| pattern already used for the 3 proved sigma=+1
     sub-pieces.
  5. NEW this round (§27.3): Gap 1c's nonempty-xi* case refines into a genuine 3-way split: (a) sparsest
     Lemma-P-irreducible witness (the true hard core, ~99.7% of cases, unproved), (b) sparsest witness
     Lemma-P-collapses to a duplicate pair (reduces FOR FREE to the same conditional mechanism as (c)),
     (c) xi*=empty literally (already closed, round 16, conditional on Deletion-Suffices q<=3). A
     sharper aimo-0960 crux mapping (two-technique split: rewrite-identity for (b), value-bound for (a))
     now applies precisely.

Key lemmas (claim + mechanism):
  - Gap 1b/Gap 1a equivalence (§27.1) — because the certified peeling trichotomy's KEEP-branch closed
    form at h=0 (KEEP = w1 - OPT_{-1}(C,rest)) turns "Sum Bound holds" into "KEEP >= DELETE" by a direct
    3-line algebraic substitution, which is literally half of Deletion-Suffices-for-k*'s claim
    (DELETE beats both KEEP and MATCH).
  - Three-Touch candidate (§27.2(d)) — because the sigma=-1 (maximizing) mirror can exploit Lemma P's
    duplicate-pair cancellation ADVERSARIALLY (manufacture a MATCH-created duplicate of the background
    value c to force cancellation, isolating untouched top elements), a mechanism with no sigma=+1
    analogue, which is why touch<=3 (not <=2) is needed on this side.
  - Gap 1c case (b) reduction (§27.3) — because when the sparsest optimal witness is a duplicate pair
    {c,c}, Lemma P forces RHS = e(B_1 u {d}) exactly, collapsing the target to the already-certified
    delete-suffices-insertion-domination.md conclusion (same conditional as case (c)).

Open gaps (ranked, per §27.5):
  1. [HIGHEST LEVERAGE] Deletion-Suffices-for-k*/Per-Partner-Domination at general q, DELETE-vs-MATCH
     half specifically (closes part of Gap 1a AND Gap 1b's inductive step's KEEP half is then free).
  2. [TRACTABLE, independent of #1] Prove Three-Touch (Gap 1a's KEEP b_0<=w_1 sub-piece).
  3. [NARROWED, independent of #1] Gap 1c case (a) — sparsest Lemma-P-irreducible nonempty xi*.
  4. [CHEAP] Formalize Gap 1c case (b) as an explicit corollary — a few lines.
  5. [LOWER PRIORITY] Match-Branch Domination (Two-Touch's MATCH sub-piece) — no candidate mechanism
     yet, per-partner-indexed strengthening flagged as next angle.

Cases to cover: the 3-way Gap 1c split (a)/(b)/(c) above is now the exhaustive case list for the
nonempty/empty-xi* question — no case omitted (c) is closed, (b) reduces for free, (a) is the residual.

Watch out for: (i) do NOT claim Gap 1b's general induction is closed/free — only its DELETE-vs-KEEP
half reduces to Gap 1a's still-open conjecture; (ii) do NOT use an arbitrary/first-found optimal witness
for Gap 1c's construction — confirmed to fail (5 counterexamples with largest-cardinality tie-break),
must use the sparsest witness; (iii) do NOT resurrect the general |C|=2 Two-Touch formula in any form,
including as a one-directional lower bound (now confirmed false both ways: 23.8% as equality, 35.8% as
a one-directional bound); (iv) do NOT drop the top-level trigger A_1 in any induction attempt at any
recursion depth (37.0% failure confirmed at a second depth, q=4, this round); (v) items 2 and 3 above
are logically independent of item 1 — a builder can progress on either without waiting.

No 5th slug opened. dyadic-cascade-induction and concavity-minimax-duality remain benched (no new
leverage found or claimed this round; not re-examined this round per the standing rule that re-checking
is due only after 2+ rounds without progress on the live slug, which is not the case here).
