# Proof-reviewer report — Round 3 — imo-2026-06 (IMO 2026 P6)

Two candidates, both self-marked `solved`. I reviewed each independently, re-derived
the load-bearing step (the SCPL minimal-counterexample descent) from scratch, and
computationally verified the crux claims. **Both are correct and complete.**

---

## Approach 1: `small-prime-core` — APPROVE (Status: solved)

**Scores:** Correctness 10/10 · Completeness/rigor 10/10 · Progress: closes the crux (SCPL) and the whole problem.

**Structure.** Q={p≤a_1} fixed up front → Clique (L1) → Bounded gaps (L2) →
Reduction A=V_∞∩[a_1,∞) (L3) → Valid-below-are-terms (L4) → Companion (L5, threshold
z=a_1) → SCPL (L6, the crux) → membership characterization mod M (L7–9) → exact
periodicity, T=|R|, L=M (Step 6).

**Crux re-derived independently (L6, SCPL descent).** Strong induction on the larger
index j; within it, minimal-counterexample on the smaller index i. I confirmed the
induction is well-founded and non-circular:
- Step 2 needs S(i) (pairs (i',i), i'<i, share a small prime). Since i<j, S(i) is
  among the assumed S(j') for j'<j — legitimate use of the IH.
- Step 4 needs (a_s,a_j) to share a small prime for s<i. This is (6.1), the
  *minimality of i* (i is the smallest index whose pair with j has no small prime),
  NOT the IH. Correctly justified.
- The companion x lands as an earlier term a_s (s≤i-1) via valid-below-are-terms +
  greedy minimality; r'|a_s=x ⟹ r'∈P(x)=σ(a_i) ⟹ r' small prime | gcd(a_i,a_j),
  contradiction. Airtight.
- Base i=1 excluded correctly (P(a_1)=σ(a_1)); S(1),S(2) handled.

**Companion (L5) checked.** Threshold z=a_1 (not rad(a_1)/p_max) is genuinely
load-bearing — verified the a_1=48 counterexample (term 56=2^3·7). Both t=0 and t≥1
cases give a_1≤x<a. Uses a≥pq and a≥m_0·q correctly.

**Endgame checked.** L8/L9 characterization A={m≥a_1 : m mod M ∈ R} is exactly
periodic from a_1; window argument gives exactly T=|R| terms per M consecutive
integers; a_{n+T}=a_n+M for ALL n≥1 (the problem's actual requirement — no transient,
no "eventually"). R≠∅ since a_1∈A. Note L=M=∏(all primes ≤a_1) is a valid (non-minimal)
period — fine, the problem only asks existence.

No skipped cases, no hand-waving, no external theorem uncited. Answer_type is none.

## Approach 2: `wqo-domination` — APPROVE (Status: solved)

**Scores:** Correctness 10/10 · Completeness/rigor 10/10 · Progress: independent full solution, genuinely different endgame.

**Same L1–L6 spine (independently written), different endgame.** Instead of mod-M
collapse, it uses the inclusion-minimal constraint family
E_∞ = min-members of {P(a_i)}. Checked:
- (3a) every P(a_i) contains a member of E_∞ — minimality below a fixed finite set,
  no WQO needed (the file explicitly avoids the false WQO-on-P_fin claim). Correct.
- (3b) V_∞ = {m>1 : P(m)∩F≠∅ ∀F∈E_∞}. Both inclusions verified.
- (3c) E_∞⊆2^Q: if F∈E_∞ had a large prime q, then x_N=∏_{p∈σ(a_k)}p^N ∈ V_∞ for all
  N (via SCPL: every term shares a small prime of σ(a_k)), and for large N,
  x_N∈A with P(x_N)=σ(a_k)⊊F, contradicting minimality. I re-derived this — correct.
- Step 4–5: L=∏(⋃E_∞), V_∞ exactly L-periodic; window count gives a_{n+T}=a_n+L
  from n=1. Correct, and L here is the natural (smaller) period.

The SCPL descent is phrased with Π(j) starting at j≥2 and the base observation
settling i=1; equivalent to Approach 1's induction and equally sound.

---

## Independent computational verification (both approaches)
Generated the greedy sequence for a_1 ∈ {2,3,15,26,30,32,48,49,77,105,210}:
- **SCPL** (any two terms share a prime ≤a_1): TRUE in all cases (200 terms each).
- **Companion lemma** (every term with a large prime has x, P(x)=σ(a), a_1≤x<a):
  TRUE in all cases, including the a_1=48 non-squarefree case.
- **Periodicity from n=1** (a_{n+T}=a_n+L holds for ALL n≥1, no transient): TRUE;
  minimal (T,L) matches the theory, e.g. a_1=15→(8,30) [=wqo's E_∞={{2,3},{2,5},{3,5}}],
  a_1=49→(1,7), a_1=48→(1,2), a_1=77→(18,154), a_1=105→(58,210).

## Failure modes hunted and cleared
- Circularity in the double induction — cleared (Step 2 uses IH via i<j; Step 4 uses
  minimality of i, not IH).
- Companion threshold error (rad/p_max) — both use z=a_1; the trap is explicitly
  documented with the 48/56 example.
- Global vs eventual periodicity — both prove ALL n≥1 (exactly-periodic set from a_1,
  no transient). This is the problem's real requirement and is met.
- σ(a)=∅ edge, a_1 prime/prime-power edge, i=1 base — all handled.

## Lemma certification
All six promotable lemma files (clique, reduction, valid-below-are-terms, companion,
scpl, periodic-enumeration) hold to the full bar: statements correct, proofs complete
(no `sorry`/gaps), and no stronger than what is proved in the approaches. **CERTIFIED**
(status line updated in each file).

## Recorded
- record_outcome: `small-prime-core` → verified-milestone; `wqo-domination` → verified-milestone.
- current.md: Status=solved, Full proof written (self-contained small-prime-core proof,
  with note on the wqo-domination second route).

## Verdict
- `small-prime-core`: **APPROVE** — solved.
- `wqo-domination`: **APPROVE** — solved.

The run's goal (proof-reviewer APPROVE) is met, with two independent complete proofs.
