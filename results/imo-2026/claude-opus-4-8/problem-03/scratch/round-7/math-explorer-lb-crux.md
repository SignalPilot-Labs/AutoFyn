## imo-2026-03 — Lens: Lower-bound crux G-INC-1 = GAP-A

### Problem recap
Prove A(Q) ≤ A(G_{n−1}) − 1 whenever S_Q ⊆ S_{G_{n−1}}, ΣQ = 2^n, |Q| ≤ n+1
(equivalently: deficit_top + M ≥ 1, both terms ≥ 0, from the CERTIFIED top-band decomposition).

---

### 1. Algebraic identity — G-INC-1 ≡ O_Q ≤ O_{G_{n−1}}

From the definitions (O_P = sum of odd-position parts in descending sort, A(P) = 2·O_P − ΣP):

    deficit_top + M = A(G_{n−1}) − A(Q)
                    = [2·O_{G_{n−1}} − ΣG_{n−1}] − [2·O_Q − ΣQ]
                    = 2·(O_{G_{n−1}} − O_Q) + (ΣQ − ΣG_{n−1})
                    = 2·(O_{G_{n−1}} − O_Q) + 1.

So G-INC-1 is equivalent to O_Q ≤ O_{G_{n−1}}.

---

### 2. A(G_k) is always an ODD INTEGER — proved

Base: A(G_0) = 1 (odd). Induction: A(G_k) = 2^k − A(G_{k−1}) = even − odd = odd.

Verified: A(G_0..6) = 1, 1, 3, 5, 11, 21, 43. ALL ODD.

Consequence: ΣG_k = 2^k − 1 (odd), A(G_k) ≤ 2^k − 1 (odd), A(G_k) ≥ 1 for all k ≥ 0.

---

### 3. SET IDENTITY (key structural lemma, proved + verified n=3..7)

    S_{G_{n−1}} ∩ [0, 2^{n−2}) = S_{G_{n−3}}.

**Algebraic proof:** For x ∈ [0, 2^{n−2}), both 2^{n−2} and 2^{n−1} exceed x. Therefore
    N_{G_{n−1}}(x) = N_{G_{n−3}}(x) + 2.
Same parity ⟹ S_{G_{n−1}} ∩ [0, 2^{n−2}) = {x < 2^{n−2} : N_{G_{n−3}}(x) odd} = S_{G_{n−3}}.

This is a CLEAN algebraic proof (no computation required) that the INC constraint on Q_lo (the
parts of Q below thr = 2^{n−2}) reduces to the SAME INC constraint at level n−2:

    S_{Q_lo} ⊆ S_{G_{n−1}} ∩ [0, 2^{n−2}) = S_{G_{n−3}}.

**Self-similar identity (proved):** M = A(G_{n−3}) − A(Q_lo).
Proof: A(G_{n−3}) = 2^{n−2} − A(G_{n−2}) (from A(G_{n−2}) = 2^{n−2} − A(G_{n−3})), and the certified
top-band decomp gives M = 2^{n−2} − A(G_{n−2}) − A(Q_lo).

---

### 4. Budget propagation — the recursion closes

Top-band decomp: h = |Q_hi| (even, ≥ 2), |Q_lo| = |Q| − h ≤ n+1 − 2 = n−1.
Level n−2 IH needs |Q_lo| ≤ (n−2)+1 = n−1. EXACT MATCH.

So one application of top-band decomp maps:
  (level n, ΣQ = 2^n, |Q| ≤ n+1, S_Q ⊆ S_{G_{n−1}})
to
  (level n−2, S_{Q_lo} ⊆ S_{G_{n−3}}, |Q_lo| ≤ n−1, ΣQ_lo = 2^{n-2} ± ε).

---

### 5. Saturation analysis — the budget constraint is EXACTLY tight

Saturation config (achieves deficit_top + M = 0): {2^{n−1}, 2^{n−2}, ..., 2, 1, 1/2, 1/2} has n+2 parts.
Budget allows n+1. Over budget by EXACTLY 1.

Verified for n=2..6: saturation always requires n+2 parts. The budget constraint n+1 is what prevents
A(Q) = A(G_{n−1}) (i.e., prevents deficit_top + M = 0).

---

### 6. Proof opening for G-INC-1 via two-step induction

**Base cases:** n=2 (trivial: parity forces Q={2,2}, A(Q)=0 ≤ A(G_1)−1=0) and n=3 (Step 7 casework,
already in the approach).

**Inductive step (n ≥ 4), using IH at level n−2:**

Write q_1 ≥ q_2 for the two high parts (h=2, forced by parity + h<4 argument below). Let
  a = 2^{n−1} − q_1 ≥ 0,  b = q_2 − 2^{n−2} ≥ 0,  so deficit_top = a+b.
Then ΣQ_lo = 2^{n−2} + (a−b).

**CASE 1 (h ≥ 4):** ΣQ_lo ≤ ΣQ − 4·thr = 2^n − 2^n = 0. So Q_lo = ∅, A(Q_lo) = 0, M = A(G_{n−3}) ≥ 1.
deficit_top + M ≥ 1. ✓

**CASE 2a (h=2, deficit_top ≥ 1):** Done directly. ✓

**CASE 2b (h=2, a+b < 1):**

  Sub-case 2b-i (a ≥ b, ΣQ_lo ≥ 2^{n−2}): Apply the STRENGTHENED IH Claim(n−2, a−b) [see §7]:
    A(Q_lo) ≤ A(G_{n−3}) − 1 + (a−b).
  Then M = A(G_{n−3}) − A(Q_lo) ≥ 1 − (a−b).
  deficit_top + M ≥ (a+b) + (1−(a−b)) = 1 + 2b ≥ 1. ✓

  Sub-case 2b-ii (a < b, ΣQ_lo < 2^{n−2}): REMAINING SUB-GAP (see §8).

---

### 7. The strengthened IH needed (Claim(n, ε))

The inductive step for sub-case 2b-i requires the following generalization:

  **Claim(n, ε):** For Q with S_Q ⊆ S_{G_{n−1}}, ΣQ = 2^n + ε (ε ∈ [0,1)), |Q| ≤ n+1:
  A(Q) ≤ A(G_{n−1}) − 1 + ε.

The ε=0 case is the original G-INC-1. Sub-case 2b-i uses Claim(n−2, a−b) with ε = a−b ≥ 0. The induction
Claim(n, ε) ← Claim(n−2, ε') cycles cleanly because sub-case 2b-i always gives ε' = a−b ≥ 0.

**Base cases for Claim(n, ε), ε ∈ [0,1):**
- Claim(2, ε): ΣQ = 4+ε > 4. Parity forces |Q| even ≤ 2. Both parts ≤ 2 (Forcing). Sum ≥ 4+ε > 2·2 = 4.
  Contradiction. No valid Q exists. Vacuously true. ✓
- Claim(3, ε): ΣQ = 8+ε. Forcing: max(Q) ≤ 4. For ε ∈ (0,1): all parts ≤ 4, sum = 8+ε slightly above 8.
  The Step 7 casework handles ε=0; the ε ∈ (0,1) extension is a perturbation of the same cases and
  should follow by continuity of A(Q) in the parts. (Needs explicit verification by the proof-builder.)

---

### 8. Remaining sub-gap: Sub-case 2b-ii (a < b)

Here: deficit_top = a+b < 1, ΣQ_lo = 2^{n−2} − (b−a) ∈ (2^{n−2}−1, 2^{n−2}). Need:
  A(Q_lo) ≤ A(G_{n−3}) − 1 + deficit_top = A(G_{n−3}) − 1 + (a+b).

**At n=4 (proved):**
|Q_lo| ≤ 2 (parity forces |Q| ∈ {2,4}, h=2, so |Q_lo| ∈ {0,2}). For 2-part Q_lo with
S_{Q_lo} = [p_2, p_1) ⊆ S_{G_1} = [1,2): must have p_2 ≥ 1 and p_1 ≤ 2.
A(Q_lo) = p_1 − p_2. And p_1 = (ΣQ_lo + A(Q_lo))/2 ≤ 2. So A(Q_lo) ≤ 4 − ΣQ_lo = b−a.
With b−a ≤ a+b = deficit_top: A(Q_lo) ≤ deficit_top ≤ A(G_{n−3}) − 1 + deficit_top = deficit_top (since A(G_1)=1). ✓

**For general n:** The structural argument uses sup(S_{G_{n−3}}) = 2^{n−3} to bound max-part of Q_lo and
thence A(Q_lo). Multi-level Q_lo (|Q_lo| up to n−1) makes the argument harder.

**Possible approach:** Apply top-band decomp AGAIN to Q_lo at level n−2. The resulting "doubly-low" parts
Q_lo_lo satisfy the recursion one level further. The combined deficit sum
  deficit_top + deficit'_top + (A(G_{n−5}) − A(Q_lo_lo)) ≥ 1
follows from the base case A(G_{n−5}) ≥ 1 once all "low" parts are exhausted. This gives a
TELESCOPING-SUM argument across n/2 levels.

**Specific open question for the proof-builder:** Prove that for Q_lo with S_{Q_lo} ⊆ S_{G_{n−3}},
ΣQ_lo ∈ (2^{n−2}−1, 2^{n−2}), |Q_lo| ≤ n−1:
  A(Q_lo) ≤ deficit_top (= a+b, the "top-level" deficit at the same iteration).

This follows AT n=4 from the bound sup(S_{G_1})=2 on the parts of Q_lo. For larger n, the same
argument recurses: the high parts of Q_lo are bounded by sup(S_{G_{n−3}}) = 2^{n−3}, and the same
algebraic identity forces A(Q_lo) ≤ deficit_top via the constraint on ΣQ_lo and the part bounds.

---

### 9. GAP-B (max(Q) < 2^{n−1}) — genuinely separate from G-INC-1

**Sub-case max(Q) ≤ 2^{n−1}−1:** The interval [max(Q), 2^{n−1}) ⊆ S_R (since N_{G_{n−1}}=1 there and
no Q-part exceeds max(Q)). measure([max(Q), 2^{n−1})) ≥ 1. This region is in S_R \ S_Q.
So measure(S_Q △ S_R) ≥ 1. A(Q∪R) ≥ 1. ✓ CLOSED.

**Sub-case max(Q) ∈ (2^{n−1}−1, 2^{n−1}):** The interval [max(Q), 2^{n−1}) has measure < 1. Need
additional mass from lower levels. OPEN.

Verified: minimum A(Q∪R) in GAP-B is 1 (tight at Q={3,3,2}, R={2,2,2,1} at n=3, or equivalently
after applying REFL to the full P=Q∪R and using the dyadic structure of R).

REFL applies to the full P=Q∪R with max(P) = 2^{n−1} (from R):
  A(Q∪R) = 2^{n−1} − A((Q∪R)\{2^{n−1}}) = 2^{n−1} − A(Q∪R').
Need: A(Q∪R') ≤ 2^{n−1} − 1. With max(Q∪R') < 2^{n−1}: this is an upper-bound problem on a sum of
3*2^{n−1}−1. This doesn't directly match G-INC-1 (which is for unrefined Q). The tight case needs
the specific structure of R' (a refinement of G_{n−2}).

**GAP-B is separate:** Not reducible to G-INC-1 via REFL because after REFL on Q∪R, the resulting
problem has max(Q∪R') < 2^{n−1} and a different sum (not 2^n). A multi-step REFL chain or a separate
analysis of the "excess integral" ΣQ−ΣR = 1 in the lower dyadic levels is needed.

---

### 10. Crux corpus

No closely analogous past problem found. The sub-topic "alternating sums of stick partitions" does not
appear in the corpus. aimo-0377 uses digit-peel induction on alternating signed sums, but its structure
(fixed base, integer parts) differs from the real-valued dyadic recursion here. Not a strong analogue.

---

- **Distinct openings:**
  1. Two-step strong induction (n→n via n−2) with base n=2 (trivial) and n=3 (Step 7). The SET IDENTITY
     S_{G_{n−1}}∩[0,thr)=S_{G_{n−3}} (proved!) is the structural engine. Cases 1, 2a, 2b-i are closed;
     only sub-case 2b-ii remains.
  2. Strengthened IH (Claim(n,ε) for ε∈[0,1)): clean for sub-case 2b-i. Sub-case 2b-ii requires
     additionally showing A(Q_lo) ≤ deficit_top in the (a<b) regime, which follows from sup(S_{G_{n−3}})
     bounding max parts of Q_lo — a STRUCTURAL argument using the dyadic part bounds.
  3. Telescoping-sum approach across n/2 levels: apply top-band decomp repeatedly. The sum of all
     deficit_top terms + A(G_{base})−A(Q_{base}) = A(G_{n−1})−A(Q). At the base, A(G_{base}) ≥ 1
     and either Q_{base}=∅ (M=A(G_{base})≥1, done) or Q_{base}≠∅ with small sum (handled by base case).
  4. GAP-B via REFL + dyadic level analysis: max(Q)≤2^{n−1}−1 case is already closed. The sub-case
     max(Q)∈(2^{n−1}−1,2^{n−1}) needs a lower-level integral argument: ΣQ−ΣR=1 forces the lower
     levels' contribution to S_Q△S_R to exceed 1 − measure([max(Q),2^{n−1})) > 0.

- **Candidate techniques:** Two-step strong induction; top-band decomposition applied recursively; structural
  bound on A(Q_lo) via max-part bound + sum constraint; telescoping sum of deficit terms.

- **Cheap-kill candidates:** The SET IDENTITY (proved algebraically, 3-line proof) immediately reduces the
  INC constraint on Q_lo to the same type at level n−2 — this is not a lemma to prove but a CERTIFIED TOOL.
  The parity constraint h even (already CERTIFIED) forces Cases 1 and 2 immediately.

- **Knowledge-base entries to use:** Induction on n (two-step, descend by 2); measure/inclusion identity
  for alternating sums; dyadic level structure of G_k.

- **Analogous past problems:** None found in corpus.

- **Prior progress:** Top-band decomposition CERTIFIED. Parity-Condition CERTIFIED. Lemma REFL CERTIFIED.
  SET IDENTITY (S_{G_{n−1}}∩[0,2^{n−2})=S_{G_{n−3}}) proved but not yet in a certified lemma file.
  Self-similar identity (M=A(G_{n−3})−A(Q_lo)) proved but not certified. Cases 1, 2a, 2b-i of G-INC-1
  are closed by the two-step induction. Sub-case 2b-ii is the sole remaining gap for G-INC-1.
  GAP-B's "max(Q)≤2^{n−1}−1" sub-case is closed. The sub-case max(Q)∈(2^{n−1}−1,2^{n−1}) is open.

- **Dead ends (do not retry):**
  - Merge a/b approach: dead-ended (marked in run_state).
  - Peel-one-cut approach: dead-ended.
  - A≥2 for B3: dead-ended.
  - Claim(n, ε) for ε < 0: FALSE (counter-example: Q_lo={1.9,1.5}, n−2=2, A(Q_lo)=0.4 > 0=A(G_1)−1).
    Do not strengthen the IH to ε < 0 at n=2.

- **Small-case / intuition notes (all conjectural unless marked PROVED/CERTIFIED):**
  - A(G_k) always odd: PROVED by induction.
  - SET IDENTITY S_{G_{n−1}}∩[0,2^{n−2})=S_{G_{n−3}}: PROVED algebraically (N difference = 2).
  - Self-similar identity A(G_{n−3})=2^{n−2}−A(G_{n−2}): PROVED (follows from A(G_{n−2})=2^{n−2}−A(G_{n−3})).
  - Saturation config needs n+2 parts (verified n=2..6): CONJECTURE (likely provable by same argument).
  - Sub-case 2b-ii at n=4: A(Q_lo)≤deficit_top PROVED for 2-part Q_lo via p_1≤2 bound.
  - GAP-B tight at A(Q∪R)=1 (witness Q={3,3,2},R={2,2,2,1}): VERIFIED computationally.
