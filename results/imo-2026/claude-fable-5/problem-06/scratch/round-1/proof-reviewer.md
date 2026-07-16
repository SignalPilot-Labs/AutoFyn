# Proof review — round 1 — imo-2026-06

Three built approaches reviewed independently. Headline: **the problem is SOLVED** — `crt-window-small-prime-lockin` delivers a complete, rigorous proof, verified step by step and computationally.

---

## 1. crt-window-small-prime-lockin — **VERDICT: APPROVE** (Status: solved)

**Scores.** Correctness 10/10 · Completeness/rigor 10/10 · Progress 10/10 (full solution from a standing start).

**What I checked (adversarial pass).**
- **Load-bearing step re-derived from scratch: Step 6 (essential prime bound, ρ < a_1·g).** I reconstructed the descent independently: for Y ∈ M ∋ ρ with X = Y∖{ρ} ∉ H*, any realization m ≥ a_1 with P(m) = X is a non-term > a_1; the Exclusion Principle gives a term t < m coprime to m; intersecting-family forces P(t) ∩ Y = {ρ}; minimizing inside P(t) gives U ∈ M with ρ ∈ U and rad(U) ≤ t < m. Case c = rad(X) ≥ a_1 yields rad(X') < c/ρ (strict multiplicative descent on a positive integer); case c < a_1 realizes X by m = s^j·c < s·a_1 ≤ g·a_1 ≤ ρ (s ∈ X ∩ A, minimal j), while QW forces ρ < m — contradiction. Cases are exhaustive and disjoint; descent terminates by well-ordering; singleton members are excluded by the |Z| ≥ 2 note (Z ∩ A ≠ ∅, ρ ∉ A). My derivation reproduces the claim exactly.
- **Every other step checked line by line.** Step 2 (terms = sorted valid set): the max-index/greedy-minimality sandwich a_{n+1} ≤ m ≤ a_{n+1} is airtight. Step 3 (H* = types, realization p_1^j·p_2⋯p_r): correct, including the r = 1 case. Lemma EP (Step 4): correct static recasting, no counterfactual reasoning. Lemma QW (Step 5): the degenerate m = a_1 input is explicitly excluded (P(a_1) ∈ H* vs P(m) ∉ H*); the size chain rad(U) ≤ rad(P(t)) ≤ t < m is the genuine number-theoretic input. Steps 7–8: Claim 7.1 and both directions of Claim 8.1 correct; the order-isomorphism argument gives periodicity for ALL n ≥ 1 (not merely eventually), which is exactly what the problem demands; T ≥ 1 and L ≥ 2 verified.
- **Hidden-gap hunt.** No "clearly/obviously" load-bearing shortcuts found; well-definedness of the greedy step, finiteness of terms below any bound, and min V = a_1 are all justified. No circularity (EP uses only greedy minimality; QW uses EP; Step 6 uses QW; Step 8 uses only Step 6's output). No crux-move citations.
- **Computational verification (my own code).** (i) Exact periodicity from n = 1 for seeds 6, 15, 20, 21, 35, 45, 77, 105: all pass with squarefree L. (ii) Edge seed a_1 = 385: T = 5088, L = 43890 = 2·3·5·7·11·19, holds from n = 1 across 16185 terms — Remark 2's numbers confirmed exactly. (iii) Exclusion Principle: 0 failures on all 17341 non-terms in (385, 20000]. (iv) {2,11,19} hits all 5394 prefix types while all three 2-subsets fail, and A = {2,7} is the unique small pair — confirming the strict lock-in p ≤ g is false and the weakened bound is the right theorem.
- **Consistency with the no-go result (approach 3).** No conflict: the winning proof's essential input is the size bound rad(t) ≤ t < m, which has no clutter-level analog — precisely the kind of number-theoretic input the ladder counterexample proves is necessary.

**Builder's recorded Status `solved` is correct.** Full proof written into `results/imo-2026-06/current.md` (reviewer-owned). Outcome recorded: `verified-milestone`.

---

## 2. valid-set-sunflower-core — **VERDICT: CHANGES REQUESTED** (Status: partial — builder's status is accurate)

**Scores.** Correctness 9/10 (everything claimed proved is proved) · Completeness 7/10 (GAP 1 open) · Progress 8/10 (foundation + Theorem K are real, certified assets).

**Checked.** The three lemma files (foundation, dodging/witness, finite-core⟹periodicity) are fully correct — certified (see below). The infinite sunflower lemma (Erdős–Rado, infinite version) proof by induction on s is correct, including the two-case split and the discard-one-empty-petal edge case. 5b (bounded-size kill) is correct. 5c (β-extraction) is correct — the fresh witness G_m is properly chosen disjoint from σ ∪ B_m. Theorem K (König transversal tree): Facts 1–3 correct; levels nonempty by pigeonhole; parent map well-defined; the König argument (finitely many roots, descendant counting through finitely many children) is sound; properties (i)–(vii) all justified, including the bounded-size ⟹ eventually-constant ⟹ T ∈ H* contradiction for (ii).

**Remaining gap (exact).** GAP 1: ruling out the König branch (equivalently "M is finite") is not closed within this route. It is now closed *globally* by the rival's Step 6 descent — this approach could import `lemmas/essential-prime-bound.md` to complete itself, but with the problem solved this is optional. The approach stays live as a correct partial with certified reusable output. Outcome recorded: `advanced`.

---

## 3. self-blocking-clutter-induction — **VERDICT: RETHINK** (Status: unsolved as an approach to the problem; builder's own assessment "dead end as scoped" is accurate and honest)

**Scores.** Correctness 10/10 (the counterexample is correct) · Completeness n/a (the approach's target theorem is false) · Progress: high *meta*-value, zero direct progress on the problem's claim.

**The counterexample was verified carefully, as dispatched.** The ladder clutter M = {{1,2}} ∪ {{1}∪P} ∪ {{2}∪C} (P simple s–t paths, C minimal finite s–t cuts of the one-way infinite ladder):
- Lemma 1 (D_k = {r_0,…,r_k, a_k} are infinitely many distinct minimal finite cuts): checked by hand — the one-edge-deletion paths are correct and the upward-closure argument correctly upgrades to full minimality.
- Lemma 2 (i)–(v): all correct; the path-determined-by-edge-set argument in (v) is valid.
- **Lemma 3 (crux: any finite transversal of the minimal cuts contains a path)** re-derived by hand — the finite s-component S, δ(S) finite (degree ≤ 3), δ(S) ∩ T = ∅, δ(S) a cut containing a minimal cut missed by T — and independently re-verified with fresh code: 585 cut-transversals on truncations, 0 failures (and every enumerated minimal cut contains r_0, as forced by the member {1}∪{r_0}).
- Lemmas 4–6: intersecting/antichain casework complete; the four-case self-covering proof exhaustive; Lemma 6 (b(N) = N + witness lemma from (S1)+(S2)) correct.

**Consequence — accepted.** The pure theorem "identically self-blocking clutter of finite sets ⟹ finite" is FALSE; GAP B is unclosable; the induction-on-τ plan can never work. This redirects the field exactly as claimed, and it *explains* why the winning proof needed the size bound. Certified as `lemmas/no-go-infinite-self-blocking-clutter.md` (hypothesis filter for any future combinatorial attempt). The slug itself must be re-planned or retired by the outliner — with the problem solved, retirement is the natural end. Outcome recorded: `dead-end` (with the no-go noted as its certified legacy).

---

## Lemma certifications

- `lemmas/terms-equal-valid-set.md` — **CERTIFIED** (L1.1–L1.5 all correct; L1.5 also computationally verified).
- `lemmas/dodging-and-witness.md` — **CERTIFIED** (L2.1–L2.4 correct; singleton case of L2.3 handled).
- `lemmas/finite-core-implies-periodicity.md` — **CERTIFIED** (gives the claim for ALL n ≥ 1; verified on 9 seeds).
- `lemmas/essential-prime-bound.md` — **NEW, CERTIFIED** (EP + QW + the descent, from the winning approach; sharpness remark included).
- `lemmas/no-go-infinite-self-blocking-clutter.md` — **NEW, CERTIFIED** (ladder counterexample; independently re-verified).
- The infinite sunflower lemma and Theorem K remain proved in full inside `approaches/valid-set-sunflower-core.md`; no separate file needed now that the problem is solved.

## Goal Progress

- **Status: `results/imo-2026-06/current.md` = SOLVED** (round 1). Full proof recorded there.
- Ranking snapshot (post-outcomes; Elo predates outcomes, stale flags set):
  - crt-window-small-prime-lockin — Elo 1500.7, last_outcome **verified-milestone** (APPROVE, solved).
  - valid-set-sunflower-core — Elo 1531.3, last_outcome **advanced** (partial; GAP 1 closed only globally).
  - self-blocking-clutter-induction — Elo 1468.0, last_outcome **dead-end** (no-go theorem certified).
  - finite-state-window-pullback — not built this round, not reviewed.
- The run's goal is met. No further building is required; any remaining rounds are cleanup only.
