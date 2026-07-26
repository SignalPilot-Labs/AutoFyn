# outline-reviewer — IMO 2026 P4 (Mulan's triangle game)

Answer target (verified by 3 explorer routes + retrieval): **Mulan wins ⟺ θ = 180°/n, integer n ≥ 2.** Each approach must prove BOTH directions and state the characterization. Field: 5 approaches. Population is empty (round 1), so each approved approach is newly registered.

I verified the two load-bearing mechanisms numerically: (a) four-coset closure for θ = 40° (non-winning) gives 0 cuts forcing both children into L_θ from the equilateral safe state — necessity confirmed; (b) the max-angle lattice-point-in-open-interval entry cut finds a valid k for every random state across n ∈ {2,3,4,5,7,11,60} — sufficiency Phase 1 confirmed for all n.

---

## 1. lattice-coset-descent — APPROVE (CHANGES REQUESTED)

Verdict: the strategy is sound and the cleanest of the field; both directions close with all sub-lemmas identified. Four-coset necessity (algebraic) is rigorous and verified; the max-angle entry + k-descent sufficiency is verified across all n. Register and build.

Fixable gaps the builder must close:
- **Step 5 lattice-point lemma — the n = 2 (θ = 90°) justification is wrong as stated.** The outline claims "n = 2 ⟹ A ≥ 90 with equality already θ-present." This is FALSE for the equilateral state (60,60,60), which has A = 60 < 90 and no angle equal to 90°. The "open interval of length > θ" sufficient condition therefore FAILS for n = 2 equilateral (interval length A = 60 < θ = 90). The CLAIM is still true — 90° ∈ (c′, A + c′) holds because c′ ≤ 60 < 90 (always, since c′ is the minimum angle) and A + c′ = 180° − b′ > 90° (always, since b′ < 90° as b′ is not the max and c′ > 0). The builder must replace the "A ≥ 90" argument with this direct c′ < 90 < 180 − b′ justification; the general n ≥ 3 argument (length A ≥ 60 ≥ θ, with equality only when θ present) is fine.
- **Step 6 descent positivity.** The carried angles evolve as (b, c) → (b + θ, c) during k-descent. The outline asserts boundedness (b + (k−1)θ < 180) but only flags positivity as "a one-line check." The builder must write that check explicitly: the cut x = θ at the kθ-vertex is valid because 0 < θ < kθ for k ≥ 2, and the resulting child C2 = ((k−1)θ, c, b + θ) has all angles positive because (k−1)θ > 0, c > 0, and b + θ > 0 trivially; the sum ((k−1)θ + c + b + θ) = (kθ + b + c) = 180° checks out.
- **Four-coset exhaustiveness (Step 3).** Builder must write cleanly that "both children in L_θ" ⟹ x ∈ (union_1) ∩ (union_2), and the four pairwise intersections are exhaustive (the intersection of two 2-element unions is exactly four pairwise intersections). Do not leave this as a set identity the reader must trust.

Cases: n = 2 (special lattice argument above), n ≥ 3 (general), A = θ already-won (trivial), initial θ-present (0 moves). All present.

No dead-end repetition. No circularity (necessity uses four-coset; sufficiency uses lattice-point — independent).

---

## 2. altitude-halving — APPROVE

Verdict: this is the canonical Evan Chen route (matches the retrieved official solution); both directions sound. Halving lemma + altitude round-up for sufficiency, safe/unsafe external-angle dichotomy for necessity. Register and build. Highest correctness confidence (matches three independent retrieved sources).

Fixable gaps:
- **Step 3 k-existence boundary.** The integer k with 45° < kθ ≤ 90° exists for n ≥ 3 (θ ≤ 60°); builder must verify 1 ≤ k ≤ n/2 and the boundary kθ = 90° exactly (still works: ∠ADB = 180 − kθ = (n − k)θ, ∠ADC = kθ = 90° = θ when k = n/2, immediate win). The strict 45° < kθ bound holds because θ ≤ 60° and the multiples kθ march in steps ≤ 60° through (45°, 90°].
- **Step 6 sum/difference lemma.** The two external-angle identities (∠CDA = ∠B + ∠BAD; ∠DAC = ∠A − ∠BAD) involve a SUM in one and a DIFFERENCE in the other. The "safe ± unsafe = safe" lemma must be stated with the sign correct in each identity; the load-bearing input is "180° is safe when θ ≠ 180°/n." Builder must write the contradiction cleanly: if a safe angle equaled (unsafe ± unsafe), it would be a difference of two θ-multiples, hence itself a θ-multiple — contradiction.
- **Step 7 "both children unsafe" case.** The dichotomy forces ≥ 1 safe child; builder must write the contradiction showing both unsafe is impossible (it would force, via the identities, the safe parent angles to be θ-multiples).
- **Altitude foot on segment.** For an obtuse triangle, the altitude from the obtuse vertex still lands on the opposite side (not its extension) — builder should state this (true because the foot lies between the other two vertices when the altitude is from the obtuse vertex).

Cases: n = 2 (90°-trick), n ≥ 3 (altitude round-up), ∠B = 45° boundary, initial θ-present. All present.

---

## 3. safe-unsafe-pairing — APPROVE

Verdict: necessity shared with approach 2 (intentional — same canonical lemma, two phrasings); sufficiency via the deedy round-up / deficit-pairing construction is a genuinely different entry mechanism from the altitude route. Register and build.

I sanity-checked the deficit mechanism on θ = 60° and θ = 180°/7: d-sum = θ, pairing d(u) < v holds, and u + d(u) = next multiple of θ above u, with 180° − (u + d(u)) also a multiple (using 180° = nθ). Both supplementary angles at the cut foot land on θ-multiples. Sound.

Fixable gaps (the load-bearing ones):
- **Step 5 pairing lemma — the clean proof is available; write it.** Negation of "∃ distinct u, v with d(u) < v" is "∀ distinct u, v: d(u) ≥ v." Summing the cyclic triple d(a) ≥ b, d(b) ≥ c, d(c) ≥ a gives d(a) + d(b) + d(c) ≥ a + b + c = 180° = nθ. But d-sum ∈ {θ, 2θ} ≤ 2θ < nθ for n ≥ 3. Contradiction. So the pairing holds for n ≥ 3. Builder must write this cleanly and handle n = 2 separately (θ = 90°: use the 90°-trick directly, since d(x) = 90° − x for x < 90° and the pairing degenerates).
- **Step 4 ruling out d-sum = 3θ.** Builder must show d-sum = 3θ is impossible: it would require all three m_x = n, i.e. all x = 180° − d(x) > 180° − θ, impossible for three positive angles summing to 180° (would need each > 180° − θ ≥ 90°, three angles all > 90° can't sum to 180°).
- **Step 6 angle-chase.** Builder must verify which child contains which multiple: cutting at vertex v with x = d(u) (u a carried angle, u ≠ v), the child containing u has its angle-at-D = u + d(u) = m_u · θ; the other child's angle-at-D = 180° − m_u θ = (n − m_u)θ. Both multiples. State this precisely.
- **d(x) ∈ (0, θ] endpoint.** d(x) = θ means x is itself a multiple (already won); the pairing assumes strict d(x) < θ. Handle the already-won case before invoking pairing.

Cases: n = 2 (degenerate, 90°-trick), n ≥ 3 (pairing), all three angles already multiples (0 moves), exactly one angle a multiple (halving directly). All present.

---

## 4. attractor-potential — CHANGES REQUESTED (register; do NOT build this round)

Verdict: the attractor/potential framing is a legitimate, non-circular re-organization of the proof (least-fixed-point attractor W; potential Φ = min{k : angle = kθ}, well-founded descent on Φ). It targets the full claim end to end. It is NOT one proof split into pieces — it is a wrapper. But it is structurally DEPENDENT: every load-bearing step (the four-coset trap for necessity; the entry cut for sufficiency's Φ = ∞ case; the halving descent for Φ = k ≥ 2) is imported from approaches 1/2/3. Its only independent content is the proof-organizing principle.

Not circular: the entry cut (altitude / pairing / lattice max-angle) is a constructive geometric fact that does not depend on the attractor definition; the induction on Φ is well-founded (Φ ∈ {1, 2, …, n−1, ∞}, strictly decreasing). So the framing is valid.

Gaps the builder must close before this can be built:
- **Commit to ONE entry construction** (lattice max-angle, altitude round-up, or deficit-pairing) and either prove it inline OR import a reviewer-certified shared lemma. Do not leave the entry as a black box — the reviewer will flag a gap.
- **State the monotone-operator framework** for the least fixed point W (standard, but write one paragraph).
- **Pick the entry cut BEFORE building.** The outline's "pick one" leaves the approach under-specified; until an entry cut is chosen, this approach has no independent mathematical content to verify.

Diversity note: the field should not collapse to one framing. Approach 4's diversity is in proof ORGANIZATION (game-theoretic fixed-point), not in new mechanics — it shares the same wall (entry into L_θ) as 1/2/3. If that wall is wrong, 4 dies with them. This is acceptable as a hedge (a clean termination framing) but the orchestrator should be aware: if 1/2/3 succeed, 4 is unnecessary; if they stall on termination, 4's potential Φ may help structure it. Register at cold-start, rank below 1/2/3, defer to round 2 (or until a shared "entry cut" lemma is certified).

---

## 5. residue-transfer-reframe — RETHINK (NOT registered)

Verdict: the standalone mod-θ residue framing is fatally flawed on BOTH directions. Do not register; do not build. The outline itself concedes this (route (iii) collapses into approach 1).

Fatal flaws:
- **Sufficiency has a hard gcd obstruction with no known mechanism (Step 5).** For θ = 180°/n with θ ∤ 90° (e.g. θ = 60°, n = 3 — the simplest winning case), the only candidate residue-breaker (the 90°-trick) plants residue 90° mod θ. The Euclidean-algorithm reduction of (90° mod θ) terminates at gcd(90°, θ), which equals θ iff θ | 90°. For θ = 60°: 90 mod 60 = 30, gcd(90, 60) = 30 ≠ 60. So the residue reduction lands at 30°, NOT at residue 0. There is NO known residue-breaking move that produces residue 0 mod θ for general n. The outline offers three rescues: (i) a different residue-breaker (none exists or is proposed); (ii) a "kθ-trick" for k coprime to n — but finding kθ is the GOAL of the proof, so this is circular; (iii) concede and import the entry step from approach 1, which makes this approach a DUPLICATE of approach 1 (same invariant "angle ∈ θℤ," not residue), not a rival.
- **Necessity is also unprovable by the residue invariant alone (Step 6).** The mod-θ residue multiset is preserved by the transfer move (x = a − θ), but Mulan has NON-transfer cuts (any x ≠ a − θ) that change residues freely. So the residue invariant does not bound Mulan's reachable states — it cannot prove Shan-Yu defends. The outline itself flags this as "a second gap." The builder would have to import the four-coset / external-angle necessity argument — again collapsing into approaches 1/2/3.

The lesson to feed back (per the dispatch context and the additive explorer's explicit note): **the mod-θ residue is the wrong invariant; the correct invariant is "angle ∈ θℤ" (membership), not "angle mod θ."** This is already captured in approach 1. Recording the residue route as a dead-end here is the intended outcome.

---

## Diversity assessment

Approaches 1, 2, 3 share the necessity spine (four-coset / external-angle — two phrasings of the same lemma, both verified) but diversify in SUFFICIENCY: lattice max-angle cut (algebraic) vs. altitude round-up (geometric, official) vs. deficit-pairing (combinatorial). Three genuinely different entry constructions. This is acceptable diversity — the shared necessity gap is low-risk (well-established, matches the official solution) and the harder direction (sufficiency) is fully diversified. Approach 4 diversifies proof-organization only (dependent on 1/2/3's mechanics); approach 5 probes the wrong invariant and dies.

If 1/2/3 stall next round, the plateau is NOT the shared necessity gap (it's solid) — it would be the entry cut, which is already three-ways diversified. The next-round outliner should push for a genuinely different FRAMING of the whole game (e.g. a potential/monovariant directly on the angle tuple, or a topological/dynamical-systems view of the cut operator), not a fourth entry construction.

## Ranking (round 1, all cold-start 1500)

Comparisons (anchored to evidence: complete + verified > complete > dependent; matching official solution = strong correctness signal; cleaner sub-lemma identification > harder load-bearing lemma):

- {lattice-coset-descent, altitude-halving} draw — both complete, sound, verified; 1 is cleanest with most complete sub-lemma identification, 2 matches the official solution (highest correctness confidence). Equal.
- lattice-coset-descent > safe-unsafe-pairing — 1's entry (lattice point) is a one-liner; 3's pairing lemma is load-bearing and harder to get right.
- lattice-coset-descent > attractor-potential — independent vs. dependent wrapper.
- altitude-halving > safe-unsafe-pairing — canonical/official vs. heavier bookkeeping.
- altitude-halving > attractor-potential — independent vs. dependent.
- safe-unsafe-pairing > attractor-potential — independent sufficiency mechanism vs. imported.

Result: lattice-coset-descent ≈ altitude-halving > safe-unsafe-pairing > attractor-potential. (residue-transfer-reframe not registered.)

## Build set

Build three in parallel (one builder per slug), confirming the outliner's recommendation:

build set: lattice-coset-descent, altitude-halving, safe-unsafe-pairing
