# Proof outline — imo-2026-04 (Mulan's Triangle Game), round 2

**Answer (all three approaches target this exact claim):** Mulan can force victory **iff θ = 90°/n
for some positive integer n**, i.e. iff 90/θ ∈ ℤ⁺. (Corrects round-1's {90/2^k}, which is a strict
subset — do NOT build on it. Confirmed constructively + numerically by the survival explorer.)

*(Housekeeping: `problems.jsonl` tags this `medium`/rating 7, not one of the 39 `hard`. All three
explorers flagged this; the run has committed. Noted, proceeding.)*

---

## Shared, SETTLED machinery (identical in every approach — write once, import into each)

**Normal form.** State = angle triple (A,B,C), A+B+C=180. A move: Mulan picks a vertex (angle A)
and x∈(0,A); the two children are
`child1 = {x, B, 180−x−B}` and `child2 = {A−x, C, x+B}`; Shan-Yu keeps one. (The two P-angles
`180−x−B` and `x+B` are supplementary — straight-line fact. Verified by all three explorers.)

**S1 — ⊇ construction (θ=90°/n forceable in ≤ n moves; SETTLED, verified).**
- *90°-fork (base):* from ANY triangle pick a vertex whose other two angles are both acute (exists:
  ≤1 angle is ≥90°), cut at x=90°−B. Both children get 90° at the foot (supplementary P-angles,
  90° self-supplementary). Guarantees 90° regardless of Shan-Yu.
- *θ-peel:* if the current triangle has a vertex = mθ (m≥2 integer), split it at x=θ: child1={θ,…}
  contains θ (Shan-Yu must avoid it), forcing child2 = {(m−1)θ, C, θ+B}, which contains (m−1)θ
  **for any B,C**. Iterate m→m−1→…→1.
- *Chain:* θ=90/n ⟹ 90 = nθ; fork to 90 (1 move), peel n−1 times → θ. Deterministic vs all
  Shan-Yu play, all starting triangles. (Explorer: full game-tree verified n=1..7,10, 4 triangles.)
  Adapts crux `aimo-0445` (create a fork so one response can't block both lines).

**S2 — θ>90° impossibility (SETTLED, clean induction).**
Define W₀ = {triangles containing θ}; W_{k+1} = W_k ∪ {T : ∃ split with BOTH children ∈ W_k};
W(θ)=∪W_k. Mulan wins from T ⟺ T∈W(θ) (AND-OR reachability: she picks split, he picks child).
*Complete 1-move device classification:* both children ∈ W₀ (both directly contain θ) is possible
**iff** θ=90° (state-independent) **or** the split vertex A=2θ (state-dependent). [θ enters child1
via x=θ or 180−x−B=θ, child2 via A−x=θ or x+B=θ; the 4 combinations reduce to exactly these two,
the others force a zero/negative angle — 4-case check by hand.] For θ>90°: 90°-device excluded,
2θ>180° impossible, so W₁=W₀; induction ⟹ W_k=W₀ ∀k. Shan-Yu picks any start avoiding θ ⟹ never
reachable. **Closes θ>90° with no gap.** (Also kills indirect "route through 120°" precursors,
since any angle >90° is itself unreachable.)

**S3 — the closure set C(θ) (arithmetic backbone of the ⊆ direction; VERIFIED this round).**
Let C(θ) = smallest set of positive reals with 90∈C, closed under (i) v↦v/2 and (ii) v↦v−θ *only
when v is a positive integer multiple of θ*. Then **θ∈C(θ) ⟺ θ=90/n** (proved: any element is
`90/2^a − mθ`; equals θ ⟺ θ=90/(2^a(m+1))=90/integer; reachability by peeling 90=nθ down. BFS-
verified for n=1..24 and for many non-90/n values → unreachable). C(θ) is exactly the set of
"Shan-Yu-immune constant values" Mulan can manufacture. **This is the target of the survival lemma.**

**THE ONE REAL GAP (θ<90°, θ∉{90/n}): the Guaranteed-Constant Lemma.**
> *From a generic starting triangle, every angle-value Mulan can guarantee to force into the
> survivor (independent of Shan-Yu) that is algebraic over ℚ(θ) lies in C(θ).*
Since θ is algebraic over ℚ(θ), this gives θ guaranteeable ⟹ θ∈C(θ) ⟹ θ=90/n, closing ⊆.
**Crucial simplification (use everywhere):** Shan-Yu needs only ONE surviving start, so he may pick
a maximally generic triangle; "Mulan wins for θ" ⟺ W(θ)=all triangles. The three approaches below
are **rival proofs of this one lemma** via genuinely different engines (invariant / global closure
/ descent) so they fail in different modes.

---

## imo-2026-04

### transcendence-genericity-invariant: new
Target: full characterization θ∈{90/n}. Spine of the hard half = a self-restoring
algebraic-independence invariant (move-by-move Shan-Yu strategy). Adapts crux `aimo-0236`
(two-phase self-restoring invariant, defender stays one step ahead).
Technique: field-theoretic invariant over ℚ(θ) + explicit dodge.
Skeleton:
  1. Answer, normal form, S1, S2 — import (SETTLED).
  2. Shan-Yu picks A₀,B₀ algebraically independent over ℚ(θ) (C₀=180−A₀−B₀). — legal start.
  3. Define the invariant **I(T): every angle of T is either (a) algebraic over ℚ(θ) and ∈ C(θ),
     or (b) transcendental over ℚ(θ); and no angle equals θ.** Initially holds (all three angles
     transcendental). — by construction.
  4. *Single-move dodge:* at most one child contains θ (S2 device classification, θ≠90, no vertex
     =2θ under I), so a θ-free child always exists. — by S2.
  5. *Self-restoration:* show Shan-Yu can always pick a θ-free child still satisfying I(T). — GAP.
  6. I ⟹ no angle ever equals θ ⟹ Shan-Yu survives ⟹ θ∉{90/n} not forceable. Combine with S1,S2
     for the full iff. — direct.
Key lemmas (claim + mechanism):
  - *Constants ⊆ C(θ).* A value forced independent of the generic seed A₀,B₀ is algebraic over
     ℚ(θ); the only Shan-Yu-immune ways to create an algebraic-over-ℚ(θ) angle are the 90°-fork
     (→90), bisection (v↦v/2), and θ-peel (v↦v−θ from v∈θℤ) — exactly the generators of C(θ).
     Because any other split leaves the new angle transcendental (case b) or reducible by Shan-Yu's
     child choice. — this IS the Guaranteed-Constant Lemma.
  - *WARNING / known trap (found this round):* the naive invariant "tr.deg_{ℚ(θ)}=2 always" is
     FALSE — Mulan's move x = c−B (constant c) collapses BOTH children to tr.deg 1 (child1={c−B,B,
     180−c}, child2={180−C−c,C,c}); with c=θ or c=180−θ one child even gets θ. So the invariant must
     track the *algebraic part* landing in C(θ) (clause a), not raw transcendence degree. This is
     the crux subtlety; do not revert to plain tr.deg.
Open gaps: step 5 (self-restoration of clause (a) — that any algebraic-over-ℚ(θ) angle a child can
be forced to carry stays inside C(θ), given Mulan's x is arbitrary). This is the whole difficulty.
Cases to cover: which vertex Mulan splits (generic vs C(θ)-vertex vs mixed); x transcendental
(adds a case-b angle, harmless) vs x algebraic over ℚ(θ,angles) (the dangerous collapse case).
Watch out for: Mulan choosing x algebraic to manufacture a new C(θ)∪{θ}-related constant in one
child while the other stays generic — must show the θ-free child still satisfies clause (a)/(b);
the c−B collapse move above is the stress test the builder MUST handle.

### and-or-closure-rank-induction: new
Target: full characterization. Spine = global structural induction on the AND-OR winning-set rank,
lifting the 2-device classification from "both children contain θ" (W₀) to "both children ∈ W_{k}".
Technique: well-founded induction on game rank / fixpoint of W.
Skeleton:
  1. Answer, normal form, S1, S2, C(θ) — import.
  2. Strengthen S2's device lemma to all levels: **prove by induction on k that any T∈W_k which
     does not already contain θ has a vertex whose value ∈ C(θ).** — GAP (the lift).
  3. Base k=0: vacuous (T∈W₀ contains θ). Step: T∈W_{k+1}\W_k ⟹ ∃ split, both children ∈ W_k;
     apply the induction hypothesis to both children (each contains θ or a C(θ)-vertex) and the
     device classification to back out a C(θ)-vertex (or θ) in T. — GAP (the algebra of the step).
  4. Consequence: a generic triangle (no vertex in C(θ)∪{θ}, e.g. A₀,B₀ transcendental) ∉ W(θ).
     Hence θ forceable-from-all ⟺ C(θ) meets every triangle ⟺ θ∈C(θ) ⟺ θ=90/n (S3). — direct.
Key lemmas (claim + mechanism):
  - *Rank-lifted device lemma:* if both children of a split are in W_k and each (per IH) carries θ
     or a C(θ)-value, then the parent carries a C(θ)-value, because a value guaranteed in both
     children traces back through {x, A−x, x+B, 180−x−B} to either a shared bisection point (v↦v/2,
     stays in C(θ) by closure) or a θ-poisoned peel (v↦v−θ from a C(θ)∩θℤ vertex) — the SAME two
     generators as S2, now with C(θ)-values in place of θ. — mechanism = S2 classification re-run
     with target ranging over C(θ)∪{θ}.
Open gaps: step 2/3 — the lift of the 2-device classification to "both children carry a (possibly
different) C(θ)-value". The child values may differ, so one must show the parent-level shared/peeled
value still lands in C(θ) (uses closure under /2 and −θ). This is the load-bearing algebra.
Cases to cover: children carry the same C(θ)-value (bisection ancestor) vs different values (must
reconcile via the split formulas) vs one child carries θ directly (peel).
Watch out for: the two children carrying two *different* C(θ)-values that don't obviously combine —
must verify the split map forces their preimage into C(θ); if a pair escaped C(θ) the whole answer
would be wrong, so this is where a counterexample (if any) would surface. Cross-check against S1's
peel to confirm consistency.

### explicit-shanyu-peel-potential: new
Target: full characterization. Spine = an EXPLICIT Shan-Yu child-choice rule + a discrete potential
that provably never reaches a θ-forcing configuration — a constructive defense, not an existence
invariant. Adapts crux `aimo-0262` (defender maintains a self-reproducing safe family).
Technique: explicit strategy + monovariant/potential (knowledge_base "Invariants & monovariants").
Skeleton:
  1. Answer, normal form, S1, S2, C(θ) — import.
  2. Shan-Yu start: concrete generic triangle (A₀,B₀ transcendental over ℚ(θ)). Define potential
     **Φ(T) = min over angles α of T of d(α)**, where d(α)=0 if α=θ (lost), d(α)=k if α∈C(θ) and
     α is k peel/halve steps from being θ (finite only when θ∈C(θ)), and d(α)=∞ if α is not linked
     to θ inside C(θ). Generic start has Φ=∞. — by construction.
  3. **Explicit rule:** when Mulan splits, Shan-Yu keeps the child maximizing Φ (ties: keep the one
     with a transcendental angle). — explicit.
  4. *Preservation:* Φ(kept child) = ∞ for all time when θ∉C(θ). — GAP.
  5. Φ=∞ forever ⟹ no angle ever equals θ (d=0 needs a finite chain to θ, impossible) ⟹ survival.
Key lemmas (claim + mechanism):
  - *Φ non-collapse:* a single split cannot create an angle with finite d unless a parent angle
     already had finite d, because a new angle is x (Mulan-chosen, but any finite-d value it takes
     must lie in C(θ) and be reachable — impossible from an all-∞ parent when θ∉C(θ)), or a
     supplement/peel of an existing angle (which only moves within C(θ), preserving ∞). — mechanism:
     the split map sends {∞-angles} to {∞-angles} because the C(θ) generators (/2, −θ) never reach θ
     when θ∉C(θ) (S3), and transcendental angles stay transcendental (d=∞).
Open gaps: step 4 — proving Mulan's arbitrary-x move cannot inject a finite-d angle into BOTH
children (so Shan-Yu's max-Φ child stays ∞). Equivalent to the Guaranteed-Constant Lemma but stated
as an explicit potential preservation. Must define d rigorously (well-defined, ∞ for generic).
Cases to cover: Mulan splits a transcendental vertex vs (hypothetically) a finite-d vertex (shouldn't
exist under invariant) vs x chosen algebraic to fabricate a threat.
Watch out for: making d well-defined and genuinely ∞ on the generic start (needs θ∉C(θ) ⟹ no finite
chain); and the same c−B collapse move — show it leaves ≥1 child with Φ=∞ (the child NOT handed θ,
which retains a transcendental angle).

---

## Notes for the reviewer / build set

- **Shared crux, honest:** all three approaches reduce the open half to the **Guaranteed-Constant
  Lemma** (Constants ⊆ C(θ)). This is intrinsic to the problem — the constructive and θ>90° halves
  are done, so the whole difficulty is this one lemma. Diversity is in the *proof engine*: a
  self-restoring field invariant (A), a global rank induction on W (B), an explicit potential/strategy
  (C) — different enough that a failure in one (e.g. the tr.deg collapse that already killed the
  naive form of A) need not sink the others.
- **Do NOT** import a 2-adic/dyadic invariant (round-1's {90/2^k} was wrong; the right condition is
  ordinary integrality 90/θ∈ℤ⁺, captured by C(θ)). **Do NOT** use plain tr.deg-2 as the invariant
  (collapses under x=c−B — shown above).
- **Recommended build set:** `and-or-closure-rank-induction`, `transcendence-genericity-invariant`,
  `explicit-shanyu-peel-potential`. B is the cleanest single framing (unifies both directions under
  the closure) and should be the primary; A and C give independent attacks on the shared lemma.
  All three can already write S1+S2 in full (real, reviewer-ready progress) and mark only the
  Guaranteed-Constant Lemma as the open gap.

build set: and-or-closure-rank-induction, transcendence-genericity-invariant, explicit-shanyu-peel-potential
