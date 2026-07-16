# Proof review — round 1, imo-2026-05

Problem: determine all f : ℝ_{>0} → ℝ_{>0} with √((x² + f(y)²)/2) ≥ (f(x) + y)/2 ≥ √(x·f(y)) for all x, y > 0. Task `compute_and_prove`, answer_type `characterization`. All three built approaches claim the answer **f(x) = x + c, c ≥ 0 constant** and Status `solved`. I reviewed each adversarially and independently: re-derived every load-bearing step by hand, re-checked every algebraic identity in sympy, and stress-tested the kill inequalities numerically (20k+ random samples each). I also confirmed the derived constraints have real content (e.g. both the chain inequality (*) and the FE reject the non-solution f(y) = 2y, and a two-valued h ≡ {1, 2} numerically violates (†) at (x, y) = (0.5, 1)).

Common answer check (all approaches): Part 1 verification is a correct sum-of-squares computation — both margins equal (x − y − c)²/4, confirmed in sympy; c < 0 correctly excluded by codomain (f(−c/2) = c/2 < 0). The stated family is correct and verified by substitution, as `answer_type: characterization` requires.

---

## 1. chain-lipschitz-squeeze — verdict: **APPROVE** (Status: solved)

**Scores.** Correctness 10/10 · Completeness/rigor 10/10 · Progress 10/10 (from empty to full proof).

**Load-bearing step re-derived.** The chain inequality (*): LEFT at (f(y₂), y₂) gives f(f(y₂)) ≤ 2f(y₂) − y₂ (the QM collapses to f(y₂), positive root justified); RIGHT at (f(y₂), y₁) gives f(f(y₂)) ≥ 2√(f(y₁)f(y₂)) − y₁; chaining eliminates f∘f. Reproduced exactly.

**Checks performed.**
- Increment bounds: from (*) with (y₁, y₂) = (z+t, z): 2pq ≤ 2q² + t ⇒ p − q ≤ t/(2q) ⇒ (A) f(z+t) − f(z) ≤ t + t²/(4f(z)). With (z, z+t): 2pq ≤ 2p² − t ⇒ p − q ≥ t/(2p) > 0 (strict monotonicity, correctly derived — not assumed) ⇒ (B) f(z+t) − f(z) ≥ t − t²/(4pq) > t − t²/(4f(z)) using pq > q². All directions verified by hand and numerically over 5000 random (p, q, t) triples consistent with the constraints.
- Squaring steps: positivity of both sides stated at every squaring/division (the "squaring principle"); no sign traps found.
- Telescoping (Step 2.3): finite sums only, uniform constant m = f(y) justified at every partition point by the monotonicity proved in 2.2(B) (order of derivation sound); |f(y+T) − f(y) − T| ≤ T²/(4mn) for every n, and the n-quantifier is discharged by an explicit Archimedean argument — no hidden limit or continuity. Edge k = 0 (equality f(z₀) = m) is fine since (AB) needs only f(z) ≥ m.
- Conclusion: g = f − id constant; c ≥ 0 from codomain with −c/2 > 0 stated. No hidden regularity anywhere; the proof uses only (*), derived monotonicity, and Archimedes.

**Gaps found: none.** Recorded outcome: `verified-milestone`.

## 2. orbit-forbidden-zone — verdict: **APPROVE** (Status: solved)

**Scores.** Correctness 10/10 · Completeness/rigor 10/10 · Progress 10/10.

**Load-bearing step re-derived.** The (L) reduction: LEFT squared ⇔ (x − f(y))² ≥ 2c(x + f(y)) + c² with c = h(x) − h(y), via 2x² + 2f(y)² − (x + f(y))² = (x − f(y))² (sympy-confirmed). Both kill arguments re-derived from scratch.

**Checks performed.**
- FE f∘f = 2f − id (Step 2.1) and the orbit induction fⁿ(y) = y + n·h(y), h(fⁿ(y)) = h(y) (Step 2.2): full double-payload induction, base + step + positivity of iterates. Correct.
- h ≥ 0 (Step 2.3): Archimedean orbit escape. Correct — the orbit argument does NOT assume h > 0 anywhere; h(y) < 0 is refuted, h = 0 orbits are constant and harmless.
- Step 2.5 (two positive values a < b die): the within-one-step-hit sub-claim handles both n ≥ 1 and the n = 0 boundary (forcing f(y₀) = x, still (x − f(yₙ))² = 0 < a²); the threshold m > max{(y₀ + a − x₀)/b, (a²/(4(b−a)) − x₀)/b} delivers both x > y₀ + a and x > a²/(4(b−a)); then a² > 2(b−a)(x + f(yₙ)) + (b−a)² > 4(b−a)x uses f(yₙ) ≥ x — contradiction. Every inequality direction checked.
- Step 2.6 ({0, a} dies): forbidden interval roots (y₀ + a) ± √(4ay₀ + 2a²) — discriminant re-computed (sympy: 4ay₀ + 2a²); interval length 2w > a since (2w)² = 16ay₀ + 8a² > a². The AP-hits-interval case split (u > α / u ≤ α) is exhaustive including α ≤ 0 (vacuous case noted); minimal-m landing in (α, α + a] ⊂ (α, β) correct. Supremum squeeze: F nonempty and bounded above (by u₁ − a) before sup is taken — no empty-set supremum; (T, ∞) ⊆ P justified from the partition; ε = a/4 gives a/4 > 3a/4, immediate contradiction. All existence claims explicit.
- Step 2.7 case exhaustion (range {0}, {a} only): correct.

**Gaps found: none.** Recorded outcome: `verified-milestone`.

## 3. right-spreading-fixed-points — verdict: **APPROVE** (Status: solved)

**Scores.** Correctness 10/10 · Completeness/rigor 10/10 · Progress 10/10.

**Load-bearing step re-derived.** The exact expansion (EXP): (2yₙ + s + a)² − 4(yₙ + s)(yₙ + b) = 4yₙ(a − b) + (s + a)² − 4sb (sympy-confirmed), and its negativity for 0 ≤ s < a, yₙ > a²/(b − a): verified over 20 000 random samples — no counterexample. The builder's own flag is right that the crude bound would only kill b > 2a; the exact expansion kills all b > a.

**Checks performed.**
- Steps 2.1–2.3 (FE, orbits, h ≥ 0) proved in-file in full; identical in substance to the certified lemmas. Correct.
- Step 2.5' chase: n-threshold max(0, ⌈(x₀ − y₀)/b⌉, ⌊(a²/(b−a) − y₀)/b⌋ + 1) satisfies (T1) non-strict and (T2) strict (the ⌊·⌋+1 handles strictness); m = ⌈(yₙ − x₀)/a⌉ ≥ 0 well defined by (T1) and yields s ∈ [0, a) via the ceiling bounds. f(x) = x + a and f(yₙ) = yₙ + b justified by orbit invariance. Correct.
- Step 2.6' spreading: (ZONE) (y − y₀)² ≥ 4ay₀ for y ∈ P (sympy-confirmed); the J(y₀) ∩ ℝ_{>0} ⊆ F conclusion correctly deferred until after 2.5' (two-valuedness needed — order preserved). Sub-claim [y₀, S) ⊆ F proved from the sup property; S = ∞ vs S < ∞ dichotomy handled (A nonempty before sup — no empty-set supremum); window W = (S − r₀, S) points satisfy y > y₀ (via S ≥ y₀ + 2r₀), making √(ay) > r₀ strict; the union [y₀, S) ∪ [y, y + 2√(ay)) covers [y₀, S + r₀) including the endpoint S (S > y and S < y + 2√(ay)) — the builder's flagged probe point holds. S + r₀ ∈ A contradicts S = sup A. Orbit escape (iii) with explicit Archimedean m. Correct.
- Step 2.7' case exhaustion airtight.

**Gaps found: none.** Recorded outcome: `verified-milestone`.

---

## Lemma certifications

- `lemmas/fe-double-iterate.md` — **certified.** Statement exactly matches proof; positive-root steps justified.
- `lemmas/orbit-invariance.md` — **certified.** Full induction; hypothesis is only the FE (no stronger than proved — in fact appropriately general).
- `lemmas/h-nonnegative.md` — **certified.** Archimedean escape correct.
- Additionally admitted (flagged promotable by builders, held to the same bar): `lemmas/chain-inequality.md`, `lemmas/increment-bounds.md` (from chain-lipschitz-squeeze), `lemmas/onepos-right.md` (from right-spreading-fixed-points). All `sorry`-free with statements no stronger than what is proved.

## Goal Progress

- **Status: `results/imo-2026-05/current.md` = solved.** Headline: three independent complete proofs APPROVED in round 1; canonical Full proof (chain-lipschitz-squeeze) written into `current.md`. The run's goal is met.
- **Ranking snapshot** (post-`record_outcome`; Elo predates outcomes, `stale=true` on all three): chain-lipschitz-squeeze 1531 (verified-milestone), right-spreading-fixed-points 1486 (verified-milestone), orbit-forbidden-zone 1483 (verified-milestone). All live, none dead-ended, zero open gaps.
- Answer of record: **f(x) = x + c for all x > 0, c ≥ 0 a constant** — family verified by substitution (margin (x − y − c)²/4 on both sides), uniqueness proven three independent ways, c < 0 excluded by codomain.
- No re-dispatch needed; all three verdicts terminal (APPROVE).
