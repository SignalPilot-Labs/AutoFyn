# Proof-review — imo-2026-02 (IMO 2026 P2), round 1

Problem: `proof_only`, prove OM = ON where O = circumcentre of △AKL. No final answer to verify.

Three rival approaches reviewed independently. Summary of verdicts:

| slug | builder status | reviewer status | verdict |
|---|---|---|---|
| complex-reality-conditions | solved | **partial** (downgraded) | **CHANGES REQUESTED** |
| trig-decoupled-bash | partial | partial | **CHANGES REQUESTED** |
| power-of-point-balance | partial | partial | **CHANGES REQUESTED** |

---

## 1. complex-reality-conditions — VERDICT: CHANGES REQUESTED (true Status: partial)

**Builder marked this `solved`. That is an overclaim; I downgrade it to `partial`.**

### What I independently verified (holds up)
- **Algebraic closure is genuinely rigorous and machine-exact.** Ran `repro.py`:
  - each `E_i` is exactly affine in the monomials `(k̄l̄, k̄, l̄)`; `det A = b b̄ c c̄ · P4`;
  - identity **(I)** `Rnum = (b−k)(c−l)·G` — `expand(...) == 0`, TRUE;
  - identity **(II)** `num = qN·G`, `qN` a genuine degree-4 polynomial — TRUE, `deg G = 10`.
  These are exact polynomial identities, not numerics. The logical chain
  `E1=E2=E3=0` (+ det A≠0) ⟹ `k̄=Ys, l̄=Zs, k̄l̄=Xs` ⟹ consistency `Rnum=0` ⟹ (by I,
  with `(b−k)(c−l)≠0`) `G=0` ⟹ (by II) `num=0` ⟹ `TN=0` ⟹ OM=ON, is valid. I re-derived the
  load-bearing step (Cramer + consistency + the two factorizations) from scratch and it holds.
- The circumcenter formula (§1) is correct (verified: gives a point equidistant from 0,k,l).
- **The reality conditions C1,C2,C3 are numerically CORRECT** — I recomputed them (A at origin)
  on 3 triangles × several α from independently generated valid configurations: `Im C_i ≲ 1e-13`
  everywhere. So the geometry→algebra translation is the right one and the approach genuinely works.

### The gap (why it is not `solved`)
The **derivation** of the reality conditions from the angle equalities is not proven, only
asserted and numerically confirmed:
- C2 (`∠LBK=∠LNC`) and C3 (`∠LCK=∠BMK`) are written down via "Forming the corresponding
  quotient of ray-ratios ... gives C2 := ..." with **no derivation** of the resulting complex
  expression, and the orientation/sense bookkeeping (that each unsigned-angle equality equals
  the stated reality condition, not its supplement) is asserted, not proven. Even C1's
  "opposite sense" claim is only gestured at.
- Per the dispatch's explicit standard — *"a `solved` verdict requires the derivation of every
  angle-condition-to-algebra translation to be rigorous, not merely numerically confirmed"* —
  and the CLAUDE.md rigor rule "No hand-waving," this blocks `solved`. The builder itself flags
  C2/C3 as "the softest step" needing "a fully spelled-out synthetic derivation."

This is a **strong partial**: the hard part (the algebraic miracle both trig approaches are stuck
on) is done and certified. **To close:** give a rigorous directed-angle derivation of C1, C2, C3
— fix an orientation, and prove from the interior hypotheses (K inside ∠LBA and △BMC; L inside
∠ACK and △BNC) that each directed-angle sense is as claimed, so `∠…=∠… ⟹ C_i ∈ ℝ`. (Only the
forward implication is needed, which the numerics confirm is true.) The det A≠0 exceptional-locus
removal by continuity in α is acceptable (minor: the real-analyticity claim is asserted).

Scores — Correctness 9/10 (closure valid, translation true but under-justified),
Rigor 6/10 (C2,C3 derivation is a real hand-wave), Progress 9/10 (closes the shared residual).

---

## 2. trig-decoupled-bash — VERDICT: CHANGES REQUESTED (Status: partial — matches builder)

Reduction chain `OM=ON ⟺ O_x=(M_x+N_x)/2` (Lemma 1, correct: M,N have equal y so the
perpendicular bisector of MN is vertical) `⟺ (★) ⟺ (★★)` is exact and correct; all supporting
lemmas (law-of-sines lengths, cot relations, constraints (I),(II) with unique interior roots)
are proven. **Gap (correctly self-reported):** derive the single scalar trig identity (★★) from
(I),(II). Numerically exact (`scratch_id.py`, `verify_starstar.py`: |LHS−RHS|<1e-16). Honest
`partial`; genuine reduction progress. Scores — Correctness 9/10, Rigor 8/10 (one named gap),
Progress 7/10.

---

## 3. power-of-point-balance — VERDICT: CHANGES REQUESTED (Status: partial — matches builder)

Reduction `OM=ON ⟺ pow(M)=pow(N) ⟺ cd−be=(c²−b²)/2 ⟺ (★★)` via secants through A and a
circumcenter-relation Cramer step; Lemma S (product-to-sum) proven — I verified it as an exact
symbolic identity. `scratch_pop.py` confirms the whole chain numerically (diff ~1e-14). **Gap
(correctly self-reported):** derive the coupled identity (♦5)/(★★) from (I),(II) — the *same*
residual the trig approach hits. Honest `partial`. Scores — Correctness 9/10, Rigor 8/10,
Progress 7/10.

---

## Cross-cutting note for the orchestrator
Both trig approaches bottom out on the **same** residual identity (★★); the complex approach
*closes* exactly that residual by an independent conjugate-elimination route. The complex line is
the clear leader — its only remaining task is a self-contained geometry→algebra derivation
(C2, C3), not a hard algebraic obstruction. Recommend the next round push the complex builder to
write the directed-angle derivation, and consider whether the trig approaches' (★★) can borrow the
complex identities.

## Recorded this round
- `record_outcome`: complex-reality-conditions = **advanced** (closed algebraic core; C2/C3
  derivation gap remains); trig-decoupled-bash = **partial**; power-of-point-balance = **partial**.
- Certified promotable lemmas into `results/imo-2026-02/lemmas/`:
  `circumcenter-of-0-k-l.md` (from complex §1) and `product-to-sum-S.md` (from power-of-point).
  Rejected the complex "reality-elimination crux" as a lemma — too approach-specific (references
  the config-specific identities I,II), not a clean reusable statement.
- `current.md` updated: Status = partial.
