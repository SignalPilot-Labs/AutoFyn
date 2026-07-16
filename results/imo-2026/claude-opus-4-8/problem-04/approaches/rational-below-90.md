# Approach: rational-below-90 (RIVAL ANSWER — tests 72° head-on)

## Status
unsolved

## Approaches tried
- CUT by outline-reviewer (round 1). The rival answer θ ∈ ℚ·180 ∩ (0,90] is REFUTED at θ=72°.
  The closure lemma of `safe-set-invariant` proves that from any safe triangle (no angle a
  multiple of θ) Mulan can NEVER force both children non-safe unless 180=(n+m)θ, i.e.
  180/θ ∈ ℤ. Since 180/72 = 2.5 ∉ ℤ, Shan-Yu survives forever from (36,36,108) — grid-confirmed
  (no both-non-safe cut exists) and algebraically proven. Hence Part C (rational≤90 ⟹ win)
  is FALSE, and the correct criterion is θ=180/N. Parts A (θ>90 loses) and B (irrational loses)
  are already subsumed by the safe-set closure lemma (both θ>90 and irrational satisfy θ≠180/N),
  so nothing correct is lost by cutting. Not registered in the population.

## Current best
Nothing proved. This is the **rival** approach carrying the analogy-lens answer
**θ ∈ ℚ·180° ∩ (0°, 90°]** (θ a rational multiple of 180° and θ ≤ 90°). Its purpose in the
population is to force the ranking to test the θ = 72° question head-on: 72° is rational and
≤ 90°, so this approach MUST win at 72°. The outliner's analysis (and computation) indicates
this winning claim FAILS at 72°; if so this approach dead-ends at G1 and is ranked below the
180/N approaches. Kept live so the field resolves the disagreement empirically, not by fiat.

---

### Claimed answer (RIVAL)
Mulan wins iff θ = (p/q)·180° with gcd(p,q)=1 and θ ≤ 90° (i.e. p ≤ q/2).
This DISAGREES with the 180/N answer exactly on rationals like 72°, 40°, 100/... .

### Technique (spine)
- **Impossibility θ > 90°:** clean — a win needs a 2θ vertex to bisect, but 2θ > 180°.
- **Impossibility irrational θ:** Shan-Yu keeps a rational-angle invariant; θ irrational can
  never appear in the child Shan-Yu keeps.
- **Sufficiency (rational θ ≤ 90°):** force 2θ via the multiple chain kθ (mod 180), then bisect.

---

### Skeleton

**Part A — θ > 90° loses.** Both children can have θ from one cut only if some vertex is 2θ
or θ = 90°; for θ > 90°, 2θ > 180° is not an angle, so at most one child has θ. Shan-Yu keeps
the θ-free child (always exists). Invariant "no angle θ" preserved. — contradiction (KB).

**Part B — irrational θ loses.** Shan-Yu starts (60,60,60); maintains "all angles rational
multiples of 180°." Any cut with rational parameter keeps both children rational; a cut with
irrational parameter can inject θ into only one child, and the sibling stays rational (θ-free).
Shan-Yu keeps the rational child. — rationality invariant (KB: invariants).

**Part C — rational θ ≤ 90° wins.** For θ = (p/q)·180°, the multiples kθ mod 180 cycle with
period q. Claim Mulan forces the surviving triangle to carry 2θ, then bisects (both children θ).

---

### Key lemmas (claim + mechanism)
- θ > 90° impossibility: 2θ > 180° blocks the only double-θ cut — solid.
- irrational impossibility: rational invariant closed under Shan-Yu's safe-child choice — solid.
- **rational-≤90 sufficiency: the disputed lemma** — "for every rational θ ≤ 90°, Mulan forces
  a 2θ vertex in finitely many steps," supposedly via the periodic chain kθ mod 180.

### Open gaps (builder fills — and where this approach likely breaks)
- **G1 (THE decisive gap):** Prove or REFUTE "rational θ ≤ 90° ⟹ Mulan forces 2θ" for
  θ = 72°. Concretely: from a safe triangle, can Mulan ever make the survivor carry 144°?
  Outliner's algebra: a cut giving {72° in one child, 144° in the other} forces one of
  A=216 (impossible), B=72 (excluded), C=−72 (impossible), or A+B+C=216≠180 — ALL impossible.
  And a both-multiples cut needs 180=(n+m)·72, impossible. So no 2θ can be forced from a safe
  triangle ⇒ this lemma is FALSE at 72°, and Shan-Yu's start (36,36,108) survives. If the
  builder confirms this, Part C fails and the correct criterion is 180/N, not "rational ≤ 90".
- **G2:** Even granting some rational θ ≤ 90° with 180/θ ∉ ℤ, exhibit an ACTUAL winning
  strategy or concede. The burden is on Part C.

### Cases to cover
θ > 90° (loses), irrational (loses), rational ≤ 90° split into 180/θ ∈ ℤ (wins — agreed) vs.
180/θ ∉ ℤ e.g. 72°, 40° (the contested cases; outliner predicts these LOSE, refuting Part C).

### Watch out for
- This approach's Parts A and B are correct and reusable (θ>90 and irrational both lose under
  BOTH answers). The disagreement is ONLY the rational-≤90-but-not-180/N band. If the builder
  refutes G1 at 72°, harvest Parts A/B as lemmas and retire the θ-rational-≤90 claim; the
  surviving correct answer is θ = 180/N.
