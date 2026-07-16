# Proof-reviewer — imo-2026-03, Round 5

Three slugs reviewed independently. Answer c(n)=2^n/(2^{n+1}−1) is pre-confirmed; only the NEW steps judged.

---

## 1. geometric-selfsimilar — VERDICT: CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10 · Rigor/completeness 8/10 (gaps honestly flagged) · Progress 9/10.

**Load-bearing new step re-derived from scratch: the partial-shadow prefix (PS-VAL), val ≤ 1 − A_1 for all A_1 < 1/2.**
I re-derived the whole chain independently:
- k = largest index with A_2+…+A_k ≤ A_1; k≥2, k<m (needs A_1<1/2 ⇒ tail 1−A_1>A_1), so A_{k+1} exists; s := A_1−(A_2+…+A_k) with 0≤s<A_{k+1}. ✓
- F = {A_2..A_k doubled} ∪ R', R'={s,A_{k+1},…,A_m}; doubled values parity-invisible ⇒ A(F)=A(R'). ✓
- Σ R' = 1 − 2A_1 + 2s (checked). R' has ≥2 elements ≥ s (namely s and A_{k+1}), so Σ_even(R') ≥ p_2 ≥ s ⇒ A(R') = ΣR' − 2Σ_even ≤ 1 − 2A_1 ⇒ val = (1+A(R'))/2 ≤ 1 − A_1. ✓
- Cut budget k−1 ≤ m−1 ≤ n. ✓
**Independent numeric check:** val ≤ 1−A_1 over 17,961 random flat configs (exact Fractions, m≤9): **0 violations.** The m>3 counterexample the builder cites ({12,9,2,2}/25) checks out: k=3, val=13/25=1−A_1 ≤ c(3)=8/15. The naive "one cut at A_2" is correctly identified as an m=3 artifact.

Sub-regime **B1** (A_1 ≥ 1−c(n)) ⇒ 1−A_1 ≤ c(n): closed for **all n**. Rigorous.
**Regime B at n=2 fully closed** (B1 + B2a + B2b): I verified the ε-cancellation identity val = A_1 + A_3/2 in B2a (odd region [0,ε)∪[A_2,A_1−ε), measure A_1−A_2, independent of ε) and the bound (3A_1+1)/4 < 4/7 for A_1<3/7; B2b val=1/2; the split A_1>A_2 / A_1=A_2 is exhaustive. Rigorous.

**Remaining gaps (honestly flagged, not overclaimed):** LL t≥2 with A(Q)>0 (lower bound); Regime B2 general n≥3; Regime C. No overclaim — the file marks each open. Recorded Status `partial` is correct.

**Certified this round:** `lemmas/partial-shadow-B1.md` (val ≤ 1 − A_1).

---

## 2. ll-dyadic-symdiff — VERDICT: CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10 · Rigor/completeness 8/10 · Progress 7/10.

Attacks LL t≥2 via a three-way split on measure(S_Q △ S_R) (= A(Q∪R) by Lemma M). I checked:
- **Case split exhaustive & disjoint:** Case 1 = max(Q) ≥ 2^{n−1}+1; complement split by "(odd count) ∧ (all pieces ≥ 1)" into Case 2 / Case 3. No hole; the band max(Q)∈(2^{n−1},2^{n−1}+1) correctly falls into Case 2/3, not Case 1. ✓
- **Case 1** (high-interval disjointness): on [2^{n−1}, max(Q)), N_Q=1, N_R=0 ⇒ interval ⊆ S_Q△S_R, measure ≥ max(Q)−2^{n−1} ≥ 1. Re-derived independently. Rigorous. ✓
- **Case 2** via certified Lemma P (odd count, all ≥ 1 ⇒ A ≥ 1). Correct application. ✓
- **Case 3 / Sub-3a** (some full dyadic level odd ⇒ measure ≥ level ≥ 1): trivially correct; sufficient condition (∗) checked. Rigorous but conditional. ✓
- **No recorded dead-end smuggled** (does not use merge a/b or peel-one-cut). ✓
- Verified the Sub-3b example Q={4,3,1}, R={1,2,4}: S_Q△S_R = [2,3), measure 1, no fully-odd level — matches the builder's claim.

**Open gap (honestly flagged):** Sub-3b (no fully-odd dyadic level; 85/187 n=3 residual configs) — the residual LL t≥2 crux. Not overclaimed. Recorded Status `partial` is correct.

**Certified this round:** `lemmas/ll-case1-high-interval.md` (canonical, shared with ll-inclusion-gap GAP-Case-1) and `lemmas/dyadic-level-parity.md` (Sub-3a, conditional).

---

## 3. ll-inclusion-gap — VERDICT: CHANGES REQUESTED (Status: partial) — with a FLAGGED OVERCLAIM

**Scores:** Correctness 6/10 (one claimed-rigorous lemma is false) · Rigor/completeness 5/10 · Progress 5/10.

Rigorous, correct new pieces (re-derived and confirmed):
- **Forcing Lemma** (S_Q⊆S_R ⇒ max(Q)≤2^{n−1}): correct. ✓
- **INC reduction** (S_Q⊆S_R ⇒ A(Q∪R)=A(R)−A(Q)): immediate from Lemma M. ✓
- **INC sub-case max(Q)≤2^{n−2}** (top band deficit ≥ 2^{n−2} ≥ 1): correct, does not use the Structural Lemma. ✓
- **GAP-branch Case-1** (b=max(Q)−2^{n−1}≥1): same as Case-1 high-interval. ✓

**FLAW — the builder's headline new lemma is false as stated:**
The **Structural Lemma part (a)** — "no part of Q lies in the interior of a forbidden dyadic band" — is **FALSE.** Its proof asserts "N_Q even throughout a band forces it constant there," which is wrong: an **even-multiplicity** part in the interior keeps N_Q even while N_Q is non-constant. **Explicit counterexample (n=3):** Q = {3/2, 3/2, 2, 3} partitions 8, is an inclusion config (S_Q = [2,3) ⊆ S_{G_2} = [0,1)∪[2,4)), and has two parts (3/2, 3/2) strictly inside the forbidden band (1,2). Found a second: Q={3/2,3/2,5/2,5/2}.

**Consequence — Step 6 (the claimed "complete, all sub-cases" n=3 base case) is INCOMPLETE.** Step 6 asserts "every part is ≤1 or ≥2" and does casework on that; Q={3/2,3/2,2,3} (a legal t=3 config with R=G_2, in the INC branch) is **not covered** by any Step-6 sub-case. So the "rigorous, complete" label is an **overclaim**.

Mitigating: the lemma's *headline conclusion* A(Q) ≤ A(G_{n−1}) is numerically true (0 violations, n=3 grid), because S_Q still lives only in allowed bands; it just needs an even-multiplicity-aware reproof. The inclusion *mechanism* is sound (not fatally broken), so this is CHANGES REQUESTED, not RETHINK.

**What the builder must fix:** (i) drop/replace claim (a) — parts may sit in forbidden-band interiors with even multiplicity; (ii) re-prove Step 6 covering even-multiplicity interior parts; (iii) the general gaps G-INC-1, G-INC-2, G-GAP remain the LL t≥2 crux.

**NOT certified:** the Structural Lemma (part (a) false). **Certified from this slug:** `lemmas/forcing-inc-reduction.md` (Forcing Lemma + INC reduction only) and the shared `lemmas/ll-case1-high-interval.md`.

---

## Goal Progress (for Eval History)

- **geometric-selfsimilar** (advanced, elo 1606.5): NOW RIGOROUS — upper-bound Regime B1 (partial-shadow, val ≤ 1−A_1) for **all n**; Regime B fully closed at n=2. STILL OPEN — LL t≥2 (A(Q)>0), Regime B2 general n, Regime C. Leader; largest real advance this round.
- **ll-dyadic-symdiff** (advanced, elo 1514.9): NOW RIGOROUS — LL t≥2 Cases 1, 2, and Sub-3a; exhaustive/disjoint split. STILL OPEN — Sub-3b (no fully-odd dyadic level, 85/187 n=3 residual). Clean reformulation of the shared crux.
- **ll-inclusion-gap** (partial, elo 1517.2): NOW RIGOROUS — Forcing Lemma, INC reduction, small-max sub-case, GAP Case-1. FLAWED/OVERCLAIMED — Structural Lemma (a) false, n=3 base case incomplete. STILL OPEN — G-INC-1/2, G-GAP (same LL t≥2 crux).

**Certified lemmas (round 5):** partial-shadow-B1, ll-case1-high-interval, forcing-inc-reduction, dyadic-level-parity. **Rejected:** ll-inclusion-gap "Structural Lemma" (part (a) demonstrably false).

**Overall problem Status: partial** — LL t≥2 (lower bound) and Regime C + Regime B2 general-n (upper bound) remain load-bearing open. No APPROVE.

**Shared-gap watch:** LL t≥2 (A(Q)>0) is now attacked by three distinct mechanisms; each closes a slice (high max(Q), odd-count, one-full-odd-level, inclusion small-max) but all bottom out on the same residual — spread mismatch mass / the "+1 deficit" with no single band forcing it. This is the round-4 plateau, still unbroken.
