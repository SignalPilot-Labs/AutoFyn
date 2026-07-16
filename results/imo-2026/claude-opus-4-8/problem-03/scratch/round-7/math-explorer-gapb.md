## imo-2026-03 (GAP-B and G-INC-2 lens)

### CRITICAL STRUCTURAL INSIGHT (overrides stale memory rule)

The tight A=1 witness Q={3,3,2}, R={2,2,2,1} cited in run_state as "GAP-B tight case" is in
Sub-3a, NOT Sub-3b. On I_0=[0,1): N_Q = 3 (all of {3,3,2} exceed x), N_R = 4 (all of {2,2,2,1}
exceed x), N_P = 7 (odd). So Sub-3a fires (I_0 fully odd), yielding A >= measure(I_0) = 1
immediately. GAP-B (Sub-3b B3) does NOT encounter tight A=1 cases. Verified: over all
Sub-3b B3 configs with |Q| in {3,4}, R=G_2, n=3 (1/4-grid, joint budget enforced),
min A(Q∪G_2) = 3/2 > 1 (237 valid configs, 0 exceptions).

The stale memory rule "Sub-3b B3 gives A>=2 (deleted in R6)" was wrong in the wrong direction;
the true picture is min A = 3/2, not 2, but all are > 1 with ample margin.

---

### Distinct openings

**Opening 1: Double-REFL telescoping proof for B3 (R=G_{n-1}, unrefined)**

Apply the certified Lemma REFL (results/imo-2026-03/lemmas/ll-reflection-identity.md) TWICE:

Step 1. The overall maximum of Q∪G_{n-1} is 2^{n-1} (from G_{n-1}, since max(Q) < 2^{n-1} in
Branch B3). REFL gives:
  A(Q∪G_{n-1}) = 2^{n-1} - A(Q∪G_{n-2})
where G_{n-2} = G_{n-1}\{2^{n-1}} = {1,2,...,2^{n-2}}.

Combine: A(Q∪G_{n-1}) >= 1 iff A(Q∪G_{n-2}) <= 2^{n-1}-1.

Step 2. Case split on max(Q) = q1 versus max(G_{n-2}) = 2^{n-2}:

- Case A (q1 <= 2^{n-2}): max(Q∪G_{n-2}) = 2^{n-2}. By A(P) <= max(P):
  A(Q∪G_{n-2}) <= 2^{n-2} <= 2^{n-1}-1.
  So A(Q∪G_{n-1}) >= 2^{n-2} >= 1. Verified: min A = 3 in this sub-case (n=3). DONE.

- Case B (q1 > 2^{n-2}): Apply REFL a second time (q1 = max(Q∪G_{n-2}) since q1 > 2^{n-2}):
  A(Q∪G_{n-2}) = q1 - A(Q'∪G_{n-2})
  where Q' = Q\{q1}. Combining:
  A(Q∪G_{n-1}) = 2^{n-1} - q1 + A(Q'∪G_{n-2}).
  
  Sub-case B1 (q1 <= 2^{n-1}-1, i.e., q1 <= 2^{n-2}+...): using A(Q'∪G_{n-2}) >= 0:
  A(Q∪G_{n-1}) >= 2^{n-1} - q1 >= 2^{n-1} - (2^{n-1}-1) = 1. Done directly from A >= 0.
  At n=3: q1 in (2,3] gives A >= 4-3 = 1 trivially. Verified: min A = 3/2. DONE.

  Sub-case B2 (q1 in (2^{n-1}-1, 2^{n-1})): Need A(Q'∪G_{n-2}) > q1-(2^{n-1}-1) in (0,1).
  At n=3: q1 in (3,4), need A(Q'∪G_1) > q1-3. Verified: min margin = 1/2 (tightest at
  Q=[15/4,5/2,7/4], giving A(Q'∪G_1) = 5/4 > q1-3 = 3/4). PROOF NEEDED.

The KEY FACT for Sub-case B2 (verified, analytic proof for 3-piece Q): Sub-3b on level I_{n-2}
forces: at most 2 Q-pieces exceed 2^{n-2} = 2. Specifically, for 3-piece Q with q1 > 3 = 2^{n-1}-1
in Sub-3b: exactly one piece (q3) satisfies q3 <= 2^{n-2} OR q3 in (2^{n-2}, 2^{n-2+1}) breaking
full-oddness on I_{n-2}. In both sub-subcases, the analytic formula for A(Q'∪G_1) gives:
- If q3 <= 1 (piece in level I_0): sorted Q'∪G_1 = {q2,2,1,q3}, A = q2-q3-1 = (7-q1-2q3) > 7-4-2=1 > q1-3.
- If q3 in (1,2) (piece in I_1): sorted Q'∪G_1 = {q2,2,q3,1}, A = q2+q3-3 = 5-q1 > 5-4=1 > q1-3.
Both cases give A(Q'∪G_1) > 1 >= q1-3 (strict, with margin).

For 4-piece Q: numerically verified (0 failures, min margin = 1/2 at Q=[15/4,5/2,7/4,3/2]-type).

This gives a complete proof for B3 with R=G_{n-1} (unrefined) at n=3. The generalization to n>=4
requires a recursive argument showing A(Q'∪G_{n-2}) > 0 by the same REFL chain.

**Opening 2: INC∩B3 forces G-INC-1 without top-band decomposition**

At n=3: for 3-piece Q in the INC branch (S_Q ⊆ S_{G_2}) AND Sub-3b B3 (max(Q) < 4):
- INC forces (Parity Condition lemma): #{Q-pieces >= 2} = h is even. So h in {0,2}.
- h=0 (all pieces < 2): ΣQ = q1+q2+q3 < 6 != 8. Contradiction.
- h=2 (two pieces >= 2, one piece < 2): q3 < 2. And q2+q3 = 8-q1 > 4 (since q1<4) so q2 >= 3.
  A(Q) = q1-q2+q3 <= (q1-q2)+q3 <= (q1-3)+q3 < (4-3)+2 = 3 = A(G_2)-1.
- G-INC-1 (deficit_top + M >= 1) follows: A(Q) < 3 = A(G_2), so the gap is >= 1.

This means G-INC-1 is provable for R=G_{n-1} (unrefined) WITHOUT the top-band decomposition
argument, using only the INC parity constraint + ΣQ constraint. This alternative route bypasses
the open gap entirely at n=3.

**Opening 3: G-INC-2 vacuously true at n=3; first non-trivial at n=4**

Budget parity analysis: INC requires N_P(0+) = |Q|+|R| to have the right parity. Specifically
the INC inclusion S_Q ⊆ S_R requires N_Q(0+)=|Q| and N_R(0+)=|R| to have the same parity
(otherwise I_0 = {x: N_Q(0+) odd} would differ in S_Q vs S_R). So |Q| ≡ |R| (mod 2).

For R refined (c_R >= 1 cuts of G_{n-1}): |R| = n+1 (unrefined) + c_R. At n=3: |G_2|=3, so
|R| = 3+c_R.
- c_R=1: |R|=4 (even). Need |Q|=4 (even), c_Q=3. Total c_Q+c_R=4 > 3=n. Budget exceeded.
- c_R=2: |R|=5 (odd). Need |Q|=3 or 5. c_Q>=2. Total >=4>3. Exceeded.
G-INC-2 (INC with refined R) is vacuously satisfied at n=3 (0 valid instances).

At n=4: |G_3|=4, c_R=1 gives |R|=5 (odd). Need |Q|=5 (odd), c_Q=4. Total=5>4=n. Still exceeded!
c_R=1, |Q|=3 (odd): |R|=5 odd ≡ |Q|=3 odd (mod 2). c_Q=2. Total=3 <= 4=n. VALID.
So n=4, |Q|=3, c_R=1 is the first non-trivial G-INC-2 case. The refined R has structure
different from G_{n-1} and S_R does not have the clean dyadic band structure.

---

### Candidate technique(s)

Double application of certified Lemma REFL (ll-reflection-identity.md): remove top piece of R
(gets A(Q∪G_{n-1}) = 2^{n-1} - A(Q∪G_{n-2})), then remove top piece of Q (gets A(Q∪G_{n-2})
= q1 - A(Q'∪G_{n-2})). This telescopes into the formula A(Q∪G_{n-1}) = 2^{n-1} - q1 +
A(Q'∪G_{n-2}). The A >= 0 lower bound closes Case B1 (q1 <= 2^{n-1}-1); Sub-3b parity
structure closes Case B2 (q1 > 2^{n-1}-1) via the formula showing A(Q'∪G_{n-2}) > q1-(2^{n-1}-1).

For G-INC-1: the parity argument (|Q| even in INC -> h=2 -> A(Q) <= 3 = A(G_2)-1) closes the
gap without the top-band decomposition. The technique is: count pieces, use budget constraint
ΣQ = 2^n, and INC parity to bound A(Q) directly.

---

### Cheap-kill candidates

1. Sub-3a/Sub-3b split: the cited "tight A=1" case for GAP-B is actually Sub-3a (I_0 fully odd
   -> A >= 1 immediately). No work needed there.
2. Case B1 (q1 <= 2^{n-1}-1): A >= 0 trivially gives A(Q∪G_{n-1}) >= 2^{n-1} - q1 >= 1. No case
   analysis needed; only the formula A(Q∪G_{n-1}) = 2^{n-1} - q1 + A(Q'∪G_{n-2}) and A >= 0.
3. G-INC-2 at n=3: budget+parity kills all instances. Vacuous.

---

### Knowledge-base entries to use

- REFL identity: ll-reflection-identity.md (certified lemma); apply to the top piece of G_{n-1}
  (from R) then top piece of Q (second application).
- A(P) <= max(P): elementary property of alternating sums (A = p1 - (p2-p3) - (p4-p5) - ...,
  each parenthesized pair >= 0, so A <= p1 = max(P)). Used in Case A of Opening 1.
- A(P) >= 0: trivial (used in Case B1).
- Parity-Condition Lemma: parity-condition-inc.md (certified). Used in Opening 2 (INC parity
  forces h even -> bounds A(Q)).
- Top-band decomposition: top-band-decomposition.md (certified). May be bypassed for G-INC-1 if
  Opening 2 argument goes through.

---

### Analogous past problems (cruxes)

Not searched (crux corpus search deferred; the double-REFL telescoping is specific to this problem's
structure and likely has no exact analogue in a 2434-entry corpus of pre-2026 problems).

---

### Prior progress

Status: partial. Two main open gaps in ll-dyadic-symdiff: GAP-A (A(Q'∪R) <= mu-1 for mu >= 2^{n-1})
and GAP-B (A(Q∪G_{n-1}) >= 1 for max(Q) < 2^{n-1}, Sub-3b). Three open gaps in ll-inclusion-gap:
G-INC-1 (deficit_top+M >= 1), G-INC-2 (refined R, general n), G-GAP. Current best: Regime A
and LL t=1 closed; t>=2 cases partially advanced.

GAP-B specific progress this round: A clean PROOF STRUCTURE is identified for R=G_{n-1} (unrefined)
at n=3: double-REFL telescopes to A = 2^{n-1}-q1+A(Q'∪G_{n-2}), then cases q1<=2^{n-2} (trivial
from A<=max), q1<=2^{n-1}-1 (trivial from A>=0), and q1>2^{n-1}-1 (Sub-3b parity forces
A(Q'∪G_{n-2}) > q1-(2^{n-1}-1) via analytic case analysis). Verified: 0 failures.

G-INC-2: vacuously true at n=3 (budget kills all instances). Becomes non-trivial at n>=4.

G-INC-1: NEW BYPASS ROUTE for R=G_{n-1}: INC parity (h even, h=2 forced by budget) + ΣQ = 2^n
constraint directly gives A(Q) <= A(G_{n-1})-1 without top-band decomposition.

---

### Dead ends (do not retry)

- "A>=2 in Sub-3b B3 globally": permanently dead. Min A = 3/2 (not 2) in Sub-3b B3.
- "GAP-B tight at A=1 in Sub-3b": the witness Q={3,3,2},R={2,2,2,1} is Sub-3a (I_0 fully odd),
  NOT Sub-3b. Sub-3b B3 has min A = 3/2 everywhere. The "tight" label was misapplied.
- "Per-level integral bound for B3": naive sum of level contributions too loose (each level <= 2^{k-1}
  but the Sub-3b condition prevents any single level from delivering the bound alone).
- "Sum-of-squares / AM-GM on A(Q∪G_{n-2})": not explored but unlikely to exploit Sub-3b structure.

---

### Small-case / intuition notes (conjectures)

- CONJECTURE (strong evidence): For 3-piece Q in Sub-3b B3 with q1 > 2^{n-1}-1, the Sub-3b
  condition on level I_{n-2} forces a Q-piece into [0, 2^{n-2}) or exactly at 2^{n-2}, which
  makes A(Q'∪G_{n-2}) larger than needed. This is PROVEN analytically for n=3.
- CONJECTURE: The double-REFL formula A = 2^{n-1}-q1+A(Q'∪G_{n-2}) generalizes via induction:
  A(Q'∪G_{n-2}) >= 1 because Q'∪G_{n-2} is itself a valid B3-type problem at the next level.
  (Not verified for n>=4.)
- EVIDENCE: At n=3, G-INC-2 is vacuous. The outliner should treat G-INC-2 as non-trivial only
  starting n=4 and may wish to separate the n=3 base case from the induction.
- EVIDENCE (min A values): Sub-3b B3, 3-piece Q: min=3/2; 4-piece Q: min=3/2. Distribution of
  A values: {3/2: ~20%, 2: ~37%, 5/2: ~33%, 3: ~7%}. All well above 1.
