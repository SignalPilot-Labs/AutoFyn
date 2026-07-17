# Outline review — imo-2026-04 (Mulan's Triangle Game), round 3

## Context
Answer θ=180/m settled; ⊇ construction and θ>90 impossibility certified. The one open gap is
Direction III: ⊆ survival for 0<θ<90, 180/θ∉ℤ. The outliner claims this gap is now closable by a
pure boolean **F-free** invariant (no angle equals any positive multiple of θ), maintained by
Shan-Yu via Sub-lemma B (a finite 4-case algebra), with the transcendence side-condition dropped as
unnecessary. I scrutinized this adversarially.

## Verification I performed
1. **Hand-checked the 4-combo algebra of Sub-lemma B.** With the certified normal form
   child1={x,B,180−x−B}, child2={A−x,C,x+B}, suppose both children hold an F-angle. Neighbours
   B,C∉F, so the F-angles sit in {x,180−x−B} and {A−x,x+B}. The four combos give:
   (1) A=(a+b)θ∈F; (2) B=(b−a)θ (∈F if b>a, ≤0 if b≤a); (3) C=(a−b)θ (symmetric); (4) p+q=180 ⟹
   180/θ=a+b∈ℤ. Every branch contradicts F-freeness or 180/θ∉ℤ. **Airtight for all positive
   integers a,b — no size bound needed.** The proof uses ONLY that T's vertices are not multiples
   of θ; transcendence is genuinely irrelevant. This is exactly the certified θ>90 device lemma
   (`device-classification-theta-gt-90.md`) generalized from θ to arbitrary multiples aθ,bθ.
2. **Exact-arithmetic stress test (my own, 1,113,134 trials, 0 counterexamples).** θ∈{50,72,40,
   100/3,220/7,48,65,200/3,37}; random F-free triangles; every legal x tested INCLUDING the
   adversarial collapse moves x=mθ−B and x=180−mθ−B for each neighbour B and m=1..5. No split ever
   produced two F-containing children. The x=c−B "algebraic collapse" that stalled two rounds is
   confirmed illusory for the F-free invariant.
3. **Confirmed Sub-lemma B is already in the file** (`and-or-closure-rank-induction.md` lines
   138–141) with a correct proof that references only "neighbours B,C∉F" and "a multiple on a
   vertex A,B,C excluded" — i.e. only F-freeness. The prior rounds carried a strictly stronger
   invariant S = "F-free AND has a transcendental angle"; the collapse only defeats the extra
   transcendence conjunct, never F-freeness itself. Dropping it is legitimate, not a shortcut.
4. **Non-winnability direction checks out.** W₀={θ∈T}; θ=1·θ∈F so F-free ⟹ T∉W₀. Induction step:
   F-free T has ≥1 F-free child at every split (Sub-lemma B) which is ∉W_k by IH, so no split has
   BOTH children in W_k ⟹ T∉W_{k+1}. Thus F-free ⟹ T∉⋃W_k=W(θ). A finite winning position lies in
   some W_k, so an F-free triangle is unwinnable. The AND–OR "both children" semantics is correct:
   Shan-Yu discards one child (the adversary AND), so Mulan needs both children winning.
5. **F-free start exists.** On the slice (t,t,180−2t), both t∈F and 180−2t∈F exclude only finitely
   many t (F finite), so a legal F-free start exists — for every θ with 180/θ∉ℤ, rational or
   irrational alike. No transcendence needed.

**Conclusion: the F-avoidance closure is sound and closes Direction III.** The problem is closable
this round.

## Verdicts

### and-or-closure-rank-induction — APPROVE (advance; build)
The strongest, most mature line: ⊇, θ>90, Lemma D, and Sub-lemma B are already in-file and
certified. The advance only needs to (a) restate Sub-lemma B as a standalone universally-quantified
lemma with S replaced by "F-free" (the existing proof already only uses F-freeness); (b) write the
k-induction explicitly; (c) write the F-free-start cardinality argument explicitly. Promote
Sub-lemma B to `lemmas/`.
- **Must-fix while building (CHANGES-level details, not blockers):** in combos (2)/(3) explicitly
  handle BOTH legs — b>a gives B (or C) ∈F, and b≤a gives B (or C) ≤0 impossible; do not drop the
  ≤0 leg. State combo (4) holds for all positive integers a,b (no size bound). State the win
  condition is angle EXACTLY =θ, but the invariant must track all of F (Mulan peels multiples down
  to θ), and note θ=1·θ∈F handles the base case.

### explicit-ffree-strategy — APPROVE (new; build)
Genuinely different structure from the fixpoint induction: an explicit Shan-Yu strategy ("always
keep an F-free child; Sub-lemma B guarantees one exists") with a boolean invariant maintained along
the actual play, no W_k closure. Same certified engine, different proof architecture — this is
legitimate diversity of write-up and gives robustness insurance if a reviewer objects to the
fixpoint framing. Must import the ⊇ direction so it is a complete end-to-end attempt (not a piece).
Same three write-up items as the advance.

### module-quotient-invariant (revise of transcendence-genericity-invariant) — APPROVE, NOT built this round
A valid lower-priority diversifier: recasts combo-(4) as the one-line group fact π(180)≠0 ⟺
180/θ∉ℤ and unifies rational/irrational θ. Honest caveat (the outliner states it): it still needs
the finite vertex-exclusion of Sub-lemma B for the other three combos, so it rests on the same
engine — the least independent of the three. Pitfall correctly flagged: M=ℤ+ℤθ does not contain a
generic start's angles, so π is only a cleaner proof of combo-(4), NOT a replacement invariant; the
maintained invariant stays boolean F-freeness. Kept live and ranked, but NOT in the build set:
building two independent write-ups (fixpoint + explicit strategy) of the same finish already gives
the needed robustness, and a third build on the same engine adds little.

### explicit-shanyu-peel-potential — stays DEAD
Dyadic answer (72,80,40 winnable) refuted in round 2. Do not revive.

## Field-diversity note for the orchestrator
All three live approaches now rest on the SAME engine (Sub-lemma B). Normally that is the
single-gap trap. Here it is acceptable **because the engine is verified airtight** (hand-checked +
1.1M exact trials + it is the certified θ>90 device lemma generalized) — the field has converged
onto a correct finish, not a shared open wall. The two builds use different proof architectures
(game-tree fixpoint vs. explicit defender strategy) as insurance: if the reviewer finds a subtle
objection to one framing, the other survives. If BOTH pass, the problem is solved. No need to seed a
farther framing this round; the gap is closing, not plateauing.

build set: and-or-closure-rank-induction, explicit-ffree-strategy
