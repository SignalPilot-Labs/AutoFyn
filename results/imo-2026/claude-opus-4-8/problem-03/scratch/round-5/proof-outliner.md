## imo-2026-03

Field this round: **direct-constructive** (ADVANCE — the converging leader; precise skeletons
for BOTH open gaps) + **dyadic-carry-upper** (NEW far framing for the Case-B upper wall, as
diversity insurance against single-framing collapse, carries a numeric kill-switch).

Answer (fixed, certified small-n): **c(n) = 2^n/(2^{n+1}−1)**, D = 2^{n+1}−1. Units: scale by D,
so intacts I = {2^0,…,2^{n−1}}, target lower bound A ≥ 1, target upper bound A ≤ 1 (A = 2O − D
= μ{N odd}·D in D-units; A = O − E on the sorted list). Certified imports: G1, R, H, X,
CaseB-Reductions (Spare-R_n + Red 1 + Red 2), Lemma S, fragment-count bound, interleaving value.

---

### direct-constructive : advance

**Target:** the whole problem — c(n) = 2^n/D with both bounds. Advance closes the two named gaps:
(★) lower bound at a=0 clustered vertices, and U1 Case-B hard regime (IH(q≥4) + B2).

**Technique (spine):** explicit optimal strategies both sides; Phase-1 reduction to the odd-sum
marking game (G1), then (LOWER) a **monovariant descent** on the (n+1)-fragment simplex Δ, and
(UPPER) **strong induction IH(q)** via an adaptive pair-cancelling reduction.

#### GAP (★) LOWER — close via the Descent Lemma (PRIMARY; numerically airtight)

Skeleton:
  1. Recall (certified §4.2.6): confined lower bound ⟺ A ≥ 1 at every vertex of Δ = {g_i ≥ 0,
     Σ_{i=1}^{n+1} g_i = 2^n}, min attained at a vertex; interleaving cell (A ≡ 1) and all a=1
     vertices (top-fragment cascade) already closed. Only a=0 (top piece = intact 2^{n−1},
     all fragments < 2^{n−1}) remains.
  2. **Descent Lemma (the new core).** At any a=0 config with A > 1, there exist a fragment g_j
     at an ODD rank with g_j > 0 (donor) and a fragment g_i at an EVEN rank (receiver).
     Transferring mass ε from g_j to g_i (staying in Δ, infinitesimal ⟹ within one cell) changes
     A by (sign_i − sign_j)·ε = (−1 − (+1))·ε = **−2ε < 0**: A strictly decreases.
  3. Hence A has NO local minimum with A > 1 in the strict a=0 interior. A is continuous,
     piecewise-affine on the compact a=0 region; its minimum is therefore attained on the
     boundary of that region — either a fragment = 0 (fewer fragments: reduce to G-L1(n−1) /
     lower fragment count, closed by the same induction) or a fragment = 2^{n−1} (the a=0/a=1
     boundary, where the cascade + continuity give A = 1). Either way min A = 1. ∎ (★)

Key lemma (claim + mechanism):
  - **Existence of the (odd-donor, even-receiver) fragment pair** — because in a=0 the intact
    2^{n−1} occupies rank 1 (ODD, since every fragment < 2^{n−1}); with n intacts and n+1
    fragments over n+1 odd / n even ranks, an intact at an odd rank forces (pigeonhole:
    ≤ n odd ranks left for n+1 fragments) **≥ 1 fragment at an even rank** (receiver exists);
    and n+1 fragments vs only n even ranks forces **≥ 1 fragment at an odd rank** (donor exists).
    The transfer sign is −2ε by Lemma S / the alternating-sum sign rule (increasing an even-rank
    value lowers A, decreasing an odd-rank value lowers A). Numerically verified: 0 failures over
    ~180k strict-interior a=0 configs each at n=3,4,5 — every A>1 config has such a pair.
  - **Termination at the boundary** — because each descent step strictly lowers the affine A and Δ
    is compact, the infimum is on ∂(a=0 region), reached by continuity; boundary faces are lower
    fragment-count instances (induct) or the a=1 face (cascade, A=1).

Watch out for:
  - **Donor must have POSITIVE mass at a vertex.** At a genuine vertex some g_j = 0. If every
    odd-ranked fragment is a zero, that config lies on a fragment-count boundary face
    (effectively ≤ n fragments) — handle by the fewer-fragment induction, NOT by claiming a
    positive-mass donor. State this branch explicitly; do not hand-wave it.
  - Keep ε within the current cell (no rank crossing) so A is genuinely affine along the move;
    the descent is a sequence of within-cell moves, each strictly decreasing, not one long move.
  - Do NOT invoke Lemma S as a *global* min (it is local only) — the win is the *existence of a
    decreasing direction at every* interior point, which upgrades local→global via compactness.

Fallback for (★) if the vertex/positive-mass branch resists (secondary mechanism, different tool):
  - **Dyadic-charging bound E* ≥ 2^{n−1}** (explorer Opening C). After removing the rank-1 intact
    2^{n−1}, prove the even-indexed sum of the remaining 2n pieces (I_{n−1} ∪ F) is ≥ 2^{n−1},
    i.e. A ≥ 1. Mechanism: partition the 2n pieces by dyadic level (2^{m−1}, 2^m]; the certified
    fragment-count bound N_F(2^{n−j}) ≤ 2^j − 1 caps how many fragments can push intacts up a
    rank per level; charge each even slot to an intact plus (from ΣF = 2^n with all g_i < 2^{n−1})
    at least one fragment ≥ 1 landing at an even rank. Verified for n=2 in the explorer report.
    This uses the count bound directly (the descent does not) — an independent route to the SAME
    (★), lowering risk. Build descent first; keep this ready if the vertex branch stalls.

#### GAP U1 UPPER — Case-B hard regime, IH(q) via corrected adaptive reduction

Skeleton (B1-large; B2 below):
  1. Setup (certified): hard regime is p = n+1, all a_i > 1/D, all consecutive gaps > 1/D.
     B1-large (a_1 > c(n)): XY halves a_1 (pair cancels, 0 to A), reducing to
     **IH(q):** q = p−1 pieces b_1 ≥ … ≥ b_q, all > 1/D, S = Σ b_i < (2^q − 1)/D, target A ≤ 1/D
     with q−1 cuts. IH(1),IH(2),IH(3) certified. Goal: IH(q≥4).
  2. **Corrected Case-A reduction (the fix).** Halving b_1 cancels the pair and reduces A to the
     alternating sum of {b_2,…,b_q}; this is a valid IH(q−1) instance **iff S − b_1 < (2^{q−1}−1)/D**
     (the RELATIVE threshold), NOT the explorer's absolute b_1 > 2^{q−2}/D (which is FALSE:
     881/200k q=4 configs violate it, remaining sum exceeds 2^{q−1}−1). Equivalent alternative
     move: cut b_1 at b_2 (pair {b_2,b_2} cancels), reducing to IH(q−1) on {b_1−b_2, b_3,…,b_q}
     with sum S − 2b_2; valid iff b_1−b_2 > 1/D (holds, gaps > 1/D) and S − 2b_2 < (2^{q−1}−1)/D.
  3. **Adaptive rule.** A valid one-step reduction exists iff S − max(b_1, 2b_2) < (2^{q−1}−1)/D.
     Pick whichever move (halve b_1 or cut b_1 at b_2) minimizes the residual sum; induct to
     IH(q−1). This closes ~95% of the hard-regime feasible region.
  4. **Flat residual (the honest open sub-core).** ~4.5% of feasible IH(q) configs (numerically,
     q=4,5,6) have BOTH b_1 and 2b_2 small relative to S (near-flat, clustered near S/q): no
     single pair-cancelling move keeps the sum-bound. These need a **two-cut move** dropping q by 2
     while restoring the sum invariant (the doubly-hard IH(3) leaf is the q=3 instance of this).
     Mechanism to write: cut b_1 at b_2 and cut the residual (b_1−b_2) at b_3 (as in the certified
     IH(3) doubly-hard leaf), leaving |b_1−b_2−b_3| plus {b_4,…,b_q}; bound the sum by S − 2b_2 −
     2b_3 and show it satisfies IH(q−2), with the leaf singleton < 1/D from the sum bound.

Key lemmas:
  - **Halve-b_1 = IH(q−1) reduction** — because {b_1/2, b_1/2} occupy consecutive ranks (generic
    distinctness) and cancel in the alternating sum (Lemma H pair-cancellation), leaving A equal to
    the alternating sum of the untouched {b_2,…,b_q}; parities of those pieces are preserved
    (removing a consecutive equal pair shifts all others by an even amount).
  - **Reduction feasibility** — because S − max(b_1, 2b_2) < (2^{q−1}−1)/D is exactly the condition
    the halved/cut residual sum fits the IH(q−1) budget; this is the corrected engine.

Watch out for:
  - Do NOT use the explorer's b_1 > 2^{q−2}/D threshold — refuted above. Use the relative bound.
  - Do NOT use the plain Euclidean cascade (Opening 5) as the strategy — FALSE (fails 33k/300k at
    q=4; residual is NOT ≤ 1/D from the sum bound alone). The strategy must be adaptive.
  - The flat residual is real; do not claim IH(q) fully closed if only the Case-A reduction is
    written. Mark it partial with the two-cut sub-gap explicit.

Skeleton (B2, a_1 ≤ 1/2 — the hardest, still open):
  1. All n+1 pieces in (1/D, 1/2], S = 1 = D/D (tight — cannot reduce to IH(n+1), which needs
     S < (D−1)/D). Lemma I unavailable (no dominant piece).
  2. Candidate mechanism (from certified Lemma X toggle-measure): XY makes one asymmetric cut on
     some piece producing a fragment of length ≤ 1/D, THEN halves a chosen subset so the surviving
     odd toggle layer has measure ≤ 1/D. The subset choice + ≤ n budget is the open content.
     Numerics: A ≤ 1/D achievable for n ≤ 5 (0 fails), but no explicit strategy.

Open gaps: (★) a=0 vertices — builder proves via Descent Lemma (primary) or dyadic-charging
(fallback); U1 — IH(q≥4) Case-A reduction (writable now) + flat two-cut residual + B2 (hardest).

Cases to cover: LOWER — a=0 interior (descent), a=0/a=1 boundary (cascade+continuity, done),
fragment=0 face (fewer-fragment induction). UPPER — IH(q) reduction case, IH(q) flat residual,
B1-clean (Lemma I, done), Case A (Lemma H, done), B2.

---

### dyadic-carry-upper : new

**Target:** the whole problem's UPPER bound — for EVERY LB marking (all pieces > 1/D, hard
regime), XY can hold O ≤ c(n), completing c(n) ≤ 2^n/D. (Lower bound imported from
direct-constructive; this is a genuinely different route to the Case-B wall, NOT a rename of the
pair-creation induction.)

**Technique (spine):** work directly with the certified **Lemma X toggle representation**
A = μ(⊕_i [0, m_i] ∪ [ℓ_i − m_i, ℓ_i]) and prove XY can drive the XOR toggle-measure ≤ 1/D by a
**binary-carry / dyadic-alignment** argument on piece lengths — different object (XOR of intervals
+ binary carries) and different mechanism (carry telescoping) than sorted-rank pair-cancellation.
This ALLOWS fragment cascades (a piece may be cut, then its residual cut again) — mandatory per
the round-4 finding that the menu class is too weak. Far from the whole graveyard (game-separation,
concavity-of-g, amortized-greedy, potential-duality, caseB-matching/menu).

**Skeleton:**
  1. Import Lemma X: A equals the Lebesgue measure of the symmetric difference (XOR) of the
     toggle-intervals induced by XY's cuts on LB's pieces. Target: choose cuts making μ(XOR) ≤ 1/D.
  2. Write each hard-regime piece length in D-units as a real in a binary expansion. XY's cut of a
     piece at a chosen point toggles an interval; two cuts producing equal fragments cancel (XOR).
  3. **Carry lemma (crux, to prove):** XY can cut so the toggle-intervals pair up dyadically —
     each carry from level 2^{−k} is absorbed by a matching cut at the next level — leaving a
     single residual interval of measure ≤ 1/D. This mirrors the aimo-0117 "play the next unused
     power of two" and aimo-0019 dyadic geometric-sum crux (Σ distinct negative powers of 2 ≤
     2·max), adapted: the residual after telescoping distinct dyadic toggles is ≤ the smallest,
     which the sum-bound S < D/D caps at 1/D.
  4. Assemble: μ(XOR) ≤ 1/D ⟹ A ≤ 1/D ⟹ O = 1/2 + A/2 ≤ c(n) for every hard-regime LB config.

**Key lemma (claim + mechanism):**
  - **Dyadic carry telescoping** — because XY can choose each cut to place a toggle boundary at a
    dyadic point, so successive toggle-intervals form a chain of distinct dyadic lengths whose XOR
    telescopes (each level's overlap cancels the previous carry), leaving a residual bounded by the
    finest level ≤ 1/D; the sum constraint Σℓ_i = 1 forces the finest surviving level ≤ 1/D.

**KILL-SWITCH (run BEFORE building):** For hard-regime configs (n=3,4; p=n+1; all pieces & gaps
> 1/D; sample ≥ 10^4), compute the MINIMUM XOR toggle-measure achievable over cuts placed only at
dyadic-aligned points (the carry strategy's allowed move set) and check it is ≤ 1/D on EVERY
sampled config. If a positive-measure set of configs forces dyadic-aligned μ(XOR) > 1/D, the
binary-carry mechanism is too weak (cuts must be at computed non-dyadic values) and this framing
dies at the gate — exactly as caseB-matching's menu died in round 4. (Optimize over the ACTUAL
allowed move set, per the round-4 rule: do not measure general cuts.)

**Open gaps:** the entire carry lemma (step 3) — unproved, gated by the kill-switch. If the
kill-switch fails, RETHINK/park; if it passes, the carry telescoping is the build target.

**Cases to cover:** B1-large and B2 both fall under one XOR-measure statement here (no a_1 > 1/2
split needed — the toggle representation is cut-agnostic). Verify the carry chain covers the flat
(B2) configs that stall the pair-creation induction — that is the whole point of the reframe.

**Watch out for:** vacuity/rename risk — if "μ(XOR) ≤ 1/D via dyadic cuts" is provably equivalent
to the pair-creation IH with no new leverage (same wall on flat configs), it is a rename; the
kill-switch is designed to expose this. Only worth a build slot if it passes the gate.
