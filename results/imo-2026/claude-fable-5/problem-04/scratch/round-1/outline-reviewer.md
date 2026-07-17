# Outline review — imo-2026-04, round 1

## Answer-conjecture adjudication (the contradiction the field carried)

Two mutually exclusive answers were on the table: the outliner's **"Mulan wins iff 180/θ ∈ ℤ"** vs the explorers' **"Mulan wins iff θ ≤ 90°"**. I audited both hard, analytically and with exact-fraction computation (`/tmp/verify_review.py`, Fractions, no floats):

1. **Necessity invariant verified.** For a θℤ-free triple (P,Q,R), attacking R with t: C1 = (P, t, Q+R−t) hits θℤ iff t ≡ 0 or t ≡ Q+R (mod θ); C2 = (Q, R−t, P+t) iff t ≡ R or t ≡ −P. Both hit only if 0≡R, 0≡−P, Q≡0, or P+Q+R ≡ 180 ≡ 0 (mod θ) — all excluded when 180/θ ∉ ℤ. The algebra is correct and needs no rationality of θ (works in ℝ/θℤ). Computationally: at θ = 55, 80, 40, 79, over 2000 random exact-rational θℤ-free triples, all three attack vertices, and every t hitting each of the four residue classes (all in-range representatives, plus a generic t), **zero cases** where both children contain a θℤ element. In particular **θ = 80° is a Shan-Yu win**, killing "θ ≤ 90".
2. **Sufficiency strategy verified.** For n = 2,3,4,5,6,9 (θ = 180/n), the exact strategy (Lemma A split when an angle is kθ; else attack the largest angle with t₀ = (−P) mod θ ∈ (0,θ)) beat BOTH Shan-Yu replies from ~300 random exact-rational starts each, including obtuse and near-degenerate — zero failures, bounded depth. The n = 2 fallback (Lemma D: attack the vertex whose other two angles are < 90, r2 = 90−Q; needs r2 < R, which holds since R − r2 = 90 − P > 0) verified with zero failures on 500 acute samples.
3. **Cut-model completeness.** The statement's "point P on the perimeter, different from the three vertices, cut to the opposite vertex" is exactly the (attacked vertex, split parameter t ∈ (0,R)) model — P interior to a side determines a unique opposite vertex, the cevian splits that vertex's angle. No unmodeled Mulan move exists; escalation-below-90's Step 0(c) escape is closed. Terminal condition "some angle exactly θ" is class [0] — Step 0(b) closed. Step 0(a) closed by point 1.
4. The explorers' grid simulations claiming growth at θ = 55 are nearest-grid-point rounding artifacts, as the outliner diagnosed; the exact-fraction evidence and the analytic invariant agree against them.

**Verdict on the answer: the field builds toward "Mulan wins iff 180/θ ∈ ℤ, i.e. θ = 180°/n, n ≥ 2." The "θ ≤ 90" answer is refuted and must be recorded as a dead end in `current.md`.**

---

## residue-divisibility-characterization — APPROVE

Whole attempt, both directions, correct technique, sound skeleton. Every load-bearing lemma has a stated mechanism and I verified each (Lemma A induction, the fork, the four-case invariant, Lemma D). Remaining gaps (A, B, C) are genuinely write-up level. Builder notes:

- **GAP B (t₀ < R):** the clean line is: t₀ ∈ (0, θ) strictly (since P ∉ θℤ ⟹ −P ∉ θℤ ⟹ t₀ ≠ 0, and t₀ < θ by definition of smallest positive representative). For n ≥ 3, θ ≤ 60 ≤ R (largest angle) gives t₀ < θ ≤ R with the first inequality strict, so t₀ < R. For n = 2 do NOT patch the fork — just prove Lemma D as the entire θ = 90 sufficiency (it is one move and universal) and let Step 2's fork claim start at n ≥ 3. That removes the boundary case instead of enumerating it.
- **GAP C:** state the symmetry explicitly ("relabeling the untouched pair (P,Q) is a symmetry of the move; the attacked angle is arbitrary, call it R"), then the four-case intersection once. Also state that "≡" means difference ∈ θℤ ⊂ ℝ — one sentence disposes of irrational θ.
- **Lemma A:** include the observation that an angle x ∈ θℤ with 0 < x < 180 equals kθ for a unique integer 1 ≤ k ≤ n−1, and that the split r1 = θ is legal (0 < θ < kθ for k ≥ 2). Also state the timing convention once: the stop-check occurs at the start of a round, so a child containing θ is an immediate win.
- **Step 3a:** say explicitly that the excluded set per coordinate is the finitely many multiples of θ in (0,180) plus the values forced through P+Q+R = 180 — still finite, so a θℤ-free start exists.
- Also handle the trivial branch: if Shan-Yu's initial triangle already contains an angle in θℤ, Step 1/Lemma A finishes (the outline says this; keep it).

## circle-group-quotient — APPROVE

Same theorem, and I flag honestly: it shares its mathematical core (sum invariant, four-case intersection, fork, downward induction) with the leader, so it is a **framing rival, not a deep-strategy rival** — if the core algebra were wrong they would die together. That risk is now low because I verified the core independently above; the residual failure mode is write-up/boundary bookkeeping, and this approach's layered structure (algebra in G with no sizes, then two lifting lemmas with no residues) is specifically insurance against exactly that. Approved on that basis. Builder notes:

- Keep the layer discipline the file promises — it is the approach's only reason to exist. If residue talk leaks into the lifts or size talk into Step 2, this collapses into a worse copy of the rival.
- Lift 1: same n = 2 advice as above — route θ = 90 entirely through the direct one-move win rather than patching the representative bound.
- Step 1: state that the multiset projection is the right state because the move is symmetric in the two untouched angles, and that "winning terminal ⟹ contains [0]" is one line (θ ↦ [0]).

**Diversity note for the orchestrator:** the surviving field is two framings of ONE proof idea. That is acceptable this round because the idea is verified sound and near-complete; but if either builder stalls on something structural (not bookkeeping), next round's outliner should open a genuinely different framing rather than a third variation of the residue argument.

## escalation-below-90 — RETHINK (cut; do not register)

Its target answer "Mulan wins iff θ ≤ 90°" is refuted, and all three of its own gate conditions fail:

- (a) No hole in the invariant: the four-case algebra is correct (re-derived above) and exact-fraction adversarial testing at θ = 55, 80, 40, 79 found zero double-threat states reachable from θℤ-free triples. θ = 80 ≤ 90 with 180/80 ∉ ℤ is a concrete Shan-Yu win.
- (b) A terminal state contains θ, whose class is [0] — indisputable.
- (c) The (vertex, t) move model is complete per the statement (checked against the exact wording).

The approach's own Step 3 file already concedes the peeling dynamics preserve residues mod θ, i.e. it re-derives the rival's invariant against itself. Nothing salvageable as a rival answer; the reusable pieces (θ = 90 one-move win, θ > 90 invariant — the latter now subsumed by the characterization) already live in the approved approaches / lemma-cache candidates. **Record in `current.md` under Approaches tried: "θ ≤ 90 characterization — dead end, refuted by the mod-θ residue invariant (verified analytically and by exact-fraction search; θ = 80 is a Shan-Yu win)." The slug is not registered in the ranker; its file may be marked dead-end.** No replacement outline is needed — the falsification job it was opened for is done.

---

## Ranking

- residue-divisibility-characterization: 1516 — leader; direct write-up, closest to complete, all mechanisms verified.
- circle-group-quotient: 1484 — sound insurance framing, one layer of indirection behind.
- escalation-below-90: not registered (refuted at the gate).

## Build set

Both approved approaches build in parallel; their files are disjoint and their gaps (A/B/C vs Lift 1/Lift 2/Step 2 enumeration) are independent write-ups. Priority to the leader. Shared-cache lemma candidates L1 (θ = 90 one-move win) and L2 (kθ winning, ≤ k−1 moves) should be certified by whichever builder proves them first.

build set: residue-divisibility-characterization, circle-group-quotient
