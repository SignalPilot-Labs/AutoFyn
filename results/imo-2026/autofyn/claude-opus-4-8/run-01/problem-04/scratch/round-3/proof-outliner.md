## imo-2026-04 (Mulan's Triangle Game)

**Round-3 strategic note.** The answer is settled and both easy directions are certified:
Mulan wins iff θ=180/m (m∈ℤ, m≥2). Certified: `cevian-split-normal-form`,
`construction-180-over-m` (⊇), `device-classification-theta-gt-90` (θ>90). The ONLY open gap is
Direction III (⊆ survival for 0<θ<90, 180/θ∉ℤ). This round's key finding — independently
re-verified by me (0 counterexamples in 56000 exact-arithmetic trials, θ∈{50,72,40,100/3,220/7,48,65})
and by the newframing explorer (0/25000) — is that **the x=c−B "algebraic collapse" obstacle is
illusory**: the transcendence side-condition that stalled both live approaches for 2 rounds is
UNNECESSARY. The pure boolean invariant "F-free" (no angle equals any positive multiple of θ) is
already Shan-Yu-maintainable, via the approach's OWN Sub-lemma B, which never used transcendence.
This closes the whole problem. I field it as the primary advance plus two genuinely different
framings so the field does not collapse to one proof.

**Dissolved sub-issues (important for the reviewer).** The arithmetic explorer flagged two "open
sub-issues" (halving/denominator-escape, and arbitrary-x constant injection). For the pure
F-avoidance framing these DISSOLVE: Sub-lemma B is universally quantified over the split vertex AND
over x∈(0,A), so x=c/2 (halving), x=c−B (collapse), and every other x are all already covered by
the one finite case-check. Those sub-issues were artifacts of tracking a ℤ-module of *constants*
(approach 3's bookkeeping); they never arise if the invariant is just "no angle in the finite set F."

---

### F-avoidance-rank-induction : advance
(existing file `approaches/and-or-closure-rank-induction.md` — advance; the survival section is
re-planned to drop transcendence and use pure F-avoidance)

Target: Full characterization — Mulan can force victory iff θ=180/m (m∈ℤ, m≥2). ⊇ and θ>90 are
already complete in this file; this advance CLOSES Direction III, completing the whole proof.

Technique: AND–OR winning-set closure. Fixpoint/existential framing: prove the set of F-free
triangles is disjoint from every W_k by strong induction on the closure rank k, using the certified
cevian normal form and the approach's own Sub-lemma B (finite 4-case algebra) as the induction step.

Skeleton (only the ⊆, 0<θ<90, 180/θ∉ℤ part is new; everything else is already in the file):
  1. Define F := {mθ : m∈ℤ_{≥1}, mθ<180}. F is finite (|F| = ⌈180/θ⌉−1). Call a triangle F-free if
     none of its three angles lies in F. — definition.
  2. **Sub-lemma B (case-exclusion), sharpened to a standalone statement.** If T is F-free and
     180/θ∉ℤ, then for EVERY legal split (every vertex, every x∈(0,A)) at least one child is F-free.
     — by the four-combination algebra already in the file (see Key lemmas below). Note: quantifies
     over all x, so it subsumes halving and the x=c−B collapse.
  3. **F-free start exists.** Since F is finite, pick t∈(0,90) with t∉F and 180−2t∉F (only finitely
     many bad t); T₀=(t,t,180−2t) is a legal F-free triangle. — pigeonhole (continuum minus finite).
  4. **Rank induction.** Claim: every F-free triangle ∉ W_k, for all k≥0.
     Base k=0: W₀={T: θ∈T}; F-free ⟹ θ∉T (θ=1·θ∈F) ⟹ T∉W₀.
     Step: assume every F-free triangle ∉ W_k. Let T be F-free. By Sub-lemma B every split of T has
     an F-free child, which ∉ W_k by IH; hence no split has BOTH children in W_k, so T∉W_{k+1}.
     — strong induction on k.
  5. **Conclusion III.** F-free T₀ ∉ ⋃_k W_k = W(θ). By the certified normal-form characterization,
     W(θ)≠all triangles ⟹ Mulan cannot force a win; Shan-Yu survives forever from T₀. — direct.
  6. Combine with certified ⊇ (θ=180/m ⟹ W=all) and note θ>90 is the special case F={θ}: the full
     characterization θ=180/m is proved. Update current.md to solved.

Key lemmas (claim + mechanism):
  - **Sub-lemma B** — because the child angles are exactly child₁={x,B,180−x−B},
    child₂={A−x,C,x+B} (certified normal form). If both children held an F-angle p=aθ, q=bθ (a,b≥1),
    then since neighbours B,C∉F we must have p∈{x,180−x−B}, q∈{A−x,x+B}, giving four cases, each of
    which forces something excluded: (1) x=aθ,A−x=bθ ⟹ A=(a+b)θ∈F (vertex not F-free); (2)
    x=aθ,x+B=bθ ⟹ B=(b−a)θ, either B∈F or B≤0; (3) 180−x−B=aθ,A−x=bθ ⟹ C=(a−b)θ, same as (2);
    (4) 180−x−B=aθ,x+B=bθ ⟹ p+q=180 ⟹ (a+b)θ=180 ⟹ 180/θ=a+b∈ℤ (excluded). So at least one child
    is F-free. (This is Lemma D of the file, generalized from a=b=1 to arbitrary a,b; the algebra is
    identical, no bound on a,b needed. It is the certified θ>90 device lemma one step more general.)
  - **Finiteness of F ⟹ F-free start** — because a triangle is 1 real degree of freedom on the
    slice α=β; only finitely many values hit the finite bad set F.

Open gaps: NONE that are load-bearing. The builder must (a) restate Sub-lemma B as a standalone
universally-quantified lemma (it is currently phrased inside the S-invariant); (b) write the k-
induction explicitly; (c) write the F-free-start cardinality argument explicitly (no "trivially").
Everything reduces to already-verified algebra. Promote Sub-lemma B to `lemmas/`.

Cases to cover:
  - θ>90 (F={θ}): already certified; note it is the m=1-only special case of Sub-lemma B.
  - 0<θ<90, 180/θ∉ℤ: the new case, handled uniformly by steps 1–5 (θ rational or irrational alike —
    F is finite either way; NO transcendence, NO genericity, NO measure theory).
  - 180/θ∈ℤ, θ≤90 (incl. θ=90): Mulan wins, certified ⊇.

Watch out for:
  - Do NOT re-import the transcendence side-condition. The whole point is it is unnecessary; keep the
    invariant boolean (F-free) so Sub-lemma B's universal-in-x guarantee is all that's needed.
  - The win condition is angle EXACTLY =θ (not any multiple); W₀ uses θ, but the invariant must track
    all of F (multiples), because Mulan peels multiples down to θ — F-freeness (not just θ-freeness)
    is what is preserved and what blocks the peel. State this distinction.
  - Combo (2)/(3): must handle both b>a (gives B or C ∈F) and b≤a (gives ≤0) — don't drop the ≤0 leg.
  - Verify Sub-lemma B holds for ALL positive integers a,b, not just small — it does (pure linear
    algebra, no size bound); say so explicitly.

---

### explicit-ffree-strategy : new
(new file `approaches/explicit-ffree-strategy.md`)

Target: Full characterization θ=180/m — a complete rival attempt, differing from the advance in the
⊆ direction by giving an EXPLICIT constructive Shan-Yu strategy rather than an existential
fixpoint/rank argument.

Technique: Constructive invariant-maintenance (defender strategy) instead of AND–OR closure
induction. This is a genuinely different framing: no W_k, no closure rank — a directly exhibited
strategy with a maintained boolean invariant along the actual play sequence. (Analogous to the
crux-corpus template `aimo-0236`: defender maintains a witness that a forced move cannot violate in
both branches — here the witness is membership in the finite complement of F.)

Skeleton:
  1. ⊇ direction: import certified `construction-180-over-m` verbatim (θ=180/m ⟹ Mulan wins).
  2. Setup for ⊆ (all θ with 180/θ∉ℤ): F, F-free as above; Shan-Yu opens with an F-free triangle T₀
     (finiteness of F). — same start lemma.
  3. **Shan-Yu's explicit strategy Σ:** whenever Mulan splits the current (F-free) triangle, Shan-Yu
     keeps an F-free child; if both are F-free he keeps either (say child₁). — well-defined because
     Sub-lemma B guarantees ≥1 F-free child at every move.
  4. **Invariant maintenance:** by induction on the move number, the triangle after each Shan-Yu
     response is F-free (base T₀; step by Σ + Sub-lemma B). — direct induction on play length.
  5. **Survival:** the win condition is "some angle =θ"; θ∈F, so an F-free triangle never satisfies
     it. The play stays F-free forever ⟹ Mulan never wins from T₀. Since Shan-Yu chooses the start,
     Mulan does not force victory ⟹ θ∉winnable set. — direct.
  6. Combine with (1) and θ>90 (special case) to get θ=180/m.

Key lemmas (claim + mechanism):
  - **Sub-lemma B** — same finite 4-case exclusion as the advance (import once promoted to
    `lemmas/`). This is the shared certified engine; the two approaches differ in how they USE it
    (game-tree fixpoint vs. explicit strategy), so they are far apart in structure, not one idea
    twice.
  - **Strategy well-definedness** — because Sub-lemma B says a legal F-free child always exists, Σ
    never gets stuck; the maintained invariant is a boolean, so no numeric bookkeeping / no c/2 /
    no c−B special-casing is ever needed.

Open gaps: none load-bearing; same three write-up items as the advance (standalone Sub-lemma B,
explicit induction, explicit start).

Cases to cover: identical trichotomy (θ>90 / 0<θ<90 & 180/θ∉ℤ / 180/θ∈ℤ). The strategy Σ covers all
180/θ∉ℤ uniformly.

Watch out for: this is a rival, not a piece — it must include the ⊇ direction (imported) so it is a
complete end-to-end attempt. Emphasize the constructive-strategy advantage: no reasoning about
Mulan's intentions or a game-tree fixpoint, just "keep an F-free child," which some reviewers find
strictly more rigorous. Do NOT let it degenerate into a copy of the advance's induction — state the
strategy and invariant maintenance along the play, not the W_k closure.

---

### module-quotient-invariant : revise
(revise existing `approaches/transcendence-genericity-invariant.md`)

Target: Full characterization θ=180/m — a third rival framing, retaining a field/arithmetic flavor
distinct from the two combinatorial approaches, and providing a UNIFIED rational-vs-irrational-θ
treatment (robustness insurance if the reviewer wants the "why 180 is the modulus" made structural).

Technique: Replace the failed transcendence-degree self-restoration lemma with the arithmetic
explorer's ℤ-module quotient invariant. Frame combo-(4) of Sub-lemma B as a one-line group fact:
the two supplementary P-angles p+q=180 cannot both lie in F.

Skeleton:
  1. ⊇ direction: keep the file's already-complete Lemma A (peel) + Lemma B (seed).
  2. θ>90: keep the file's complete device induction.
  3. Direction III REVISED: define M:=ℤ+ℤθ and the quotient map π:M→M/⟨θ⟩ (≅ℤ if θ irrational,
     ≅ℤ/pℤ if θ=p/q in lowest terms). Fact: v∈M is a positive multiple of θ ⟺ π(v)=0; and
     **180/θ∉ℤ ⟺ π(180)≠0** (irrational: π(180)=1; rational: π(180)=180 mod p ≠0 since p∤180).
  4. **Supplement-nonvanishing lemma:** a cut's two P-angles p,q satisfy p+q=180, so
     π(p)+π(q)=π(180)≠0 ⟹ p,q cannot both be 0 in the quotient ⟹ cannot both be multiples of θ.
     This IS combo-(4), now structural. — group homomorphism + π(180)≠0.
  5. Reduce the OTHER three combos exactly as Sub-lemma B (they pin a multiple onto a *vertex* of T,
     excluded for an F-free T) — so the module framing still needs the finite vertex-exclusion; fold
     it in. Then run the SAME F-free maintenance as the advance. — case check.
  6. Combine to θ=180/m; explicitly note this route settles θ rational and irrational in one
     statement (the reviewer's uniformity concern).

Key lemmas (claim + mechanism):
  - **π(180)≠0 ⟺ 180/θ∉ℤ** — because in ℤ+ℤθ the θ-coordinate quotient sends 180 to its residue,
    which is nonzero exactly when 180 is not an integer multiple of θ (both rational and irrational
    cases unified).
  - **Supplement-nonvanishing** — because π is a homomorphism and p+q=180, so the two P-angles'
    images sum to π(180)≠0 and cannot both vanish.

Open gaps: (a) the three non-supplement combos still require the finite vertex-exclusion of Sub-lemma
B — the module invariant alone does not replace them, so this approach must still import that finite
check (the module framing streamlines only combo-4). (b) HONEST diversity caveat: because it
ultimately rests on the same case-exclusion, this is the least-independent of the three; its value is
the unified rational/irrational statement and the structural "why 180," not a separate line of
attack. Keep it as the lower-priority diversifier.

Cases to cover: θ irrational (M/⟨θ⟩≅ℤ) and θ rational=p/q (M/⟨θ⟩≅ℤ/pℤ) — the two must be written out
so 180/θ∉ℤ ⟺ π(180)≠0 is airtight in both.

Watch out for:
  - The module M=ℤ+ℤθ only contains CONSTANT (algebraic-in-θ) angle values; a generic start's angles
    are NOT in M, so π is not defined on them. Do NOT claim the invariant is "every angle has π≠0."
    The correct role of π is ONLY to prove the supplement-nonvanishing step (combo-4); the actual
    maintained invariant is still boolean F-freeness. Frame π as a cleaner proof of combo-4, NOT as a
    replacement invariant. (This is the arithmetic explorer's flagged pitfall — angles outside M.)
  - The denominator-escape / halving worry the arithmetic explorer raised is a NON-ISSUE once the
    maintained invariant is F-free (Sub-lemma B quantifies over all x); do not spend effort closing
    it as a separate module-closure lemma.

---

**Field summary for the outline-reviewer.** Primary: `and-or-closure-rank-induction` (advance) —
pure F-avoidance closes the whole problem, all machinery already present/certified, just needs a
clean write-up + promotion of Sub-lemma B. Rival framing 1: `explicit-ffree-strategy` (new) —
constructive defender strategy, genuinely different structure, same certified engine. Rival framing
2: `module-quotient-invariant` (revise transcendence approach) — arithmetic/group recasting,
unifies rational/irrational, lower-priority insurance. `explicit-shanyu-peel-potential` stays
dead (dyadic answer refuted; do not revive). Recommended build set: all three above, primary first.
