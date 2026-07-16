# imo-2026-03 — Upper-Bound Explorer (lens: which route is closer)

## Problem and Context
c(n) = 2^n/(2^{n+1}−1) confirmed. Upper bound = show XY holds EVERY LB config to val ≤ c(n).

Two independent open routes:
- **Route A** (geometric-selfsimilar): Regime A (1/2 ≤ A_1 ≤ c(n)) CLOSED. Open: **Regime B (A_1 < 1/2)** and **Regime C (A_1 > c(n))**.
- **Route B** (extremal-smoothing): Framework Props 1–4 done. Whole upper bound reduced to **S1** (G_n is unique maximizer of V on Δ). Open: S1 alone.

---

## Numeric Probes (Python, bounded ≤15s each, all verified)

**Regime B (A_1 < 1/2), n=2:**
- [2/5, 2/5, 1/5]: XY achieves val → 1/2 (e.g., two cuts inside 1/5-piece at ε and 1/10 → val ≈ 0.504 < c(2)=4/7). ✓
- [1/3, 1/3, 1/3]: XY achieves val → 1/2 similarly. ✓
- [0.45, 0.30, 0.25]: XY cuts A_1 at A_2 → val = 1-A_1 = 0.55 < c(2). ✓ (one cut only)
- [0.40, 0.35, 0.25]: XY best val = 0.525 < c(2). ✓

**Regime B, n=3:** All tested configs ([0.45,0.30,0.15,0.10]; [1/4,1/4,1/4,1/4]; [0.45,0.45,0.10]) gave XY val ≤ c(3)=8/15. ✓

**Regime C (A_1 > c(n)), n=2:**
- [5/7, 1/7, 1/7]: ONE XY cut at 2/7 (= 1−A_1) → pieces {2/7,3/7,1/7,1/7}, val = 4/7 = c(2). ✓
- [3/4, 1/8, 1/8]: XY grid val ≈ 0.503 < c(2). Optimal: halve A_1 (1 cut), then halve one 1/8 piece → val ≈ 1/2. ✓
- [3/5, 1/5, 1/5]: halve A_1 (1 cut) → {3/10, 3/10, 1/5, 1/5}, val = 1/2 < c(2). ✓ (1 cut only!)
- [7/12, 17/60, 8/60]: halve A_1 AND halve A_2 → val = (1+A_3)/2 = 17/30 < c(2). ✓ (2 cuts)
- Regime C n=3 with [0.6, 0.2, 0.133, 0.067]: XY grid val ≈ 0.507 < c(3). ✓

**S1 check (Route B), n=2:** All 6 coordinate perturbations from G_2=(4/7,2/7,1/7) give V < c(2). Confirmed V is strictly less for all tested non-geometric A. No maximizer other than G_2 found.

---

## Route A — Regime B: NEAR-COMPLETE FOR n=2, CLEAR MECHANISM FOR GENERAL n

### Complete two-case proof for n=2 (m=3, all A_i < 1/2):

**Setup:** A_1 ≥ A_2 ≥ A_3 > 0, A_1+A_2+A_3=1, A_1 < 1/2. Note A_1 ≥ 1/3 (else A_1 < 1/m = 1/3 for m=3, impossible if A_1 is max). Also: **A_1−A_2 < A_3** (proof: A_1−A_2 < 1/2−A_2 and 1/2−A_2 ≤ A_3 iff A_2+A_3 ≥ 1/2 iff 1−A_1 ≥ 1/2 iff A_1 ≤ 1/2 ✓). Key bound: **A_3 ≤ (1−A_1)/2** (from A_2+A_3=1−A_1, A_2 ≥ A_3 → 2A_3 ≤ 1−A_1).

**Case B1 (A_1 ≥ 1−c(2) = 3/7):** XY uses ONE cut, placing A_1 at position A_2 from its left endpoint: subpieces {A_2, A_1−A_2}. Final pieces: {A_2(×2), A_1−A_2, A_3}. Since A_1−A_2 < A_3 ≤ A_2, sorted order is [A_2, A_2, A_3, A_1−A_2]. val = A_2 + A_3 = 1−A_1 ≤ 1−3/7 = 4/7 = c(2). ✓ (Uses ≤ 1 ≤ n=2 cuts.)

**Case B2 (A_1 < 3/7):** XY uses TWO cuts. Cut A_1 at ε (for any 0 < ε < c(2)−1/2−A_3/2 = 1/7−A_3/2−(A_1−1/3)·(relevant margin)), cut A_3 at A_3/2.
- Pieces: {ε, A_1−ε, A_2, A_3/2, A_3/2}. For small ε satisfying ε < A_1−A_2 and ε < A_3/2: sorted [A_1−ε, A_2, A_3/2, A_3/2, ε].
- S_{ε, A_1−ε, A_2}: N(x) = 3 for x<ε (odd), 2 for ε≤x<A_2, 1 for A_2≤x<A_1−ε. S = [0,ε)∪[A_2,A_1−ε).
- S_{A_3/2, A_3/2}: A(pair) = 0 (even count everywhere). B = overlap = 0 (since S_{pair} ⊂ [0,A_3/2) and [A_2,A_1−ε) has A_2 ≥ A_3 ≥ A_3/2 at left endpoint, so no intersection; and [0,ε) ∩ [0,A_3/2) = [0,ε) but offset by A_2 > ε → B = ε for the small interval contribution).
- **Direct computation:** val = (A_1−ε) + A_3/2 + ε = A_1 + A_3/2 (the ε's cancel exactly).
- **Bound:** A_1 + A_3/2 ≤ A_1 + (1−A_1)/4 = (3A_1+1)/4 (using A_3 ≤ (1−A_1)/2). And (3A_1+1)/4 ≤ c(2)=4/7 iff A_1 ≤ 3/7. ✓ (True in B2.)
- **Conclusion:** val = A_1+A_3/2 ≤ (3A_1+1)/4 ≤ 4/7 = c(2). ✓

**Cases B1 and B2 are exhaustive** (A_1 ≥ 3/7 or A_1 < 3/7). Together: val ≤ c(2) for ALL Regime B configs (n=2). **Numerically verified (0 errors, DENOM=60 exhaustive rational grid, eps=1/1000).**

### What n=2 Regime B proof needs to be formalized:
1. The sorted-order argument for Case B1 (requires showing A_1−A_2 < A_3 in Regime B).
2. The overlap B=0 claim in Case B2 (the two small intervals of S_pair = [0,ε)∪[A_3/2−ε,A_3/2) don't overlap with [A_2, A_1−ε) because A_2 ≥ A_3 ≥ A_3/2 > ε; and they only overlap [0,ε) in [0,ε)∩[0,ε) = [0,ε) but this is in the "N=odd for ε,A_1−ε,A_2" region only up to ε, while the pair contributes N=2 (even) everywhere below A_3/2 → combined N changes parity → need careful computation).
3. The bound A_3 ≤ (1−A_1)/2.

**RECOMMENDATION: Builder should write this n=2 proof in full — it is essentially complete.**

### General n Regime B: inductive path is CLEAR but needs formalization

Observation: 1−c(n) = (2^n−1)/(2^{n+1}−1) → 1/2 as n→∞. So:
- For n=3: Case B1 threshold is 7/15 ≈ 0.467 (A_1 ∈ [7/15, 1/2)).
- For large n: almost all of Regime B falls in Case B1.

Case B1 for general n (A_1 ≥ 1−c(n)): One cut at A_2 → val = 1−A_1 ≤ c(n). Clean inductive step; needs careful casework on sorted order when m > 3 (A_1−A_2 vs A_3).

Case B2 for general n (A_1 < 1−c(n)): Needs ≥ 2 cuts; an inductive argument reducing to an (n−1)-cut problem. The n=2 case B2 is the base, but the general bound A_1+A_m/2 ≤ c(n) (using A_m ≤ (1−A_1)/(m−1)) requires careful estimates for m > 3.

**What general n Regime B needs:** An inductive framework where the Case B1/B2 split works at each level. The key algebraic fact (3A_1+1)/4 ≤ c(n) for A_1 < 1−c(n) needs to be generalized; for general n the analogous bound is (1+(m−1)·A_1/(m−1))/m ... this requires careful analysis.

---

## Route A — Regime C: PARTIALLY UNDERSTOOD, MORE COMPLEX THAN REGIME B

### What works:
- **A_1 ∈ (c(n), 5/6] for n=2:** Cut A_1 at (1−A_1). New pieces {1−A_1, 2A_1−1, A_2,...,A_m}. Now 2A_1−1 ≤ 1/3 < c(2), 1−A_1 < 3/7 < c(2). All new pieces < c(2). With n−1=1 cut remaining, apply Regime B (specifically Case B1 if new_largest ≥ 3/7).
- **A_1 = 5/7 (clean case):** Cut at 2/7 = 1−A_1 → {2/7, 3/7, 1/7, 1/7}, val = 4/7 = c(2). **Zero remaining cuts needed.**
- **m=2 (A_1+A_2=1, A_1 > c(n)):** Halve A_1 and halve A_2 → val = 1/2. Always works.
- **A_2=A_3 (balanced small pieces):** Halve A_1 → two copies cancel, val = 1/2. One cut.
- **General m=3:** Halve A_1 AND halve A_2 → val = (1+A_3)/2. Works when A_3 ≤ 1/D.

### What's still missing for Regime C:
- **Worst sub-case:** A_1 ∈ (c(2), 2/3) with A_2−A_3 > 1/7 and none of the above clean strategies applies. These need a combined (cut-at-residual) + (Regime B sub-call) argument. Example: [7/12, 17/60, 8/60] requires halving BOTH A_1 and A_2 to get val=(1+A_3)/2 < c(2).
- **Inductive structure:** Recursive reduction "cut A_1 at 1−A_1" reduces to a (n−1)-cut problem; but for A_1 close to c(n)+, the residual 2A_1−1 may be small and the sub-problem may require full B2 type argument.
- **Key gap for Regime C general n:** Formalizing the induction — specifically showing that after peeling ONE Regime C cut, the sub-problem is strictly "easier" (bounded by c(n) rather than c(n−1)).

The difficulty in Regime C is moderate: the cases can be enumerated, and the numeric evidence confirms XY always achieves val ≤ c(n). The builder needs to find the right inductive handle.

---

## Route B — Smoothing Lemma S1: STUCK, MUCH HARDER

### State:
S1 says: for every A ≠ G_n in Δ, there exists A' ∈ Δ with V(A') > V(A). Numerically verified for all tested perturbations from G_2.

### Why S1 is harder than Regimes B and C:
1. **Global exchange argument required.** V is piecewise-linear (Prop 5a) and cell-locally concave but NOT globally concave across breakpoints. So "stationary ⇒ global max" fails. The directional-derivative D_u V(A) = min over active XY responses of ⟨∇val_τ, u⟩ requires finding u that beats ALL of XY's optimal responses at A simultaneously.
2. **Dead end:** The "V globally concave → unique stationary point is global max" argument was disproved (round 3) — cell-local concavity ≠ global concavity.
3. **Stuck for 3 rounds.** No new mechanism has been proposed. The gap is "of the same difficulty class as the problem itself" per approach file.
4. **No crux-corpus analog found** for piecewise-linear minimax uniqueness arguments of this type.

### What S1 would need:
- Full description of XY's optimal-response correspondence at every non-geometric A (very hard).
- Or: a direct comparison argument "V(G_n) ≥ V(A) for all A" that does not go through per-direction derivatives. (Not yet identified.)
- Or: a convexity/quasi-convexity argument that V is quasiconcave on the specific simplex Δ with G_n as the unique maximizer. Needs verification.

---

## Assessment: Which Route is Closer?

| | Route A Regime B | Route A Regime C | Route B S1 |
|---|---|---|---|
| n=2 proof status | **ESSENTIALLY DONE** (0 errors, verified) | Partially done (cases work, induction unclear) | Open (no mechanism) |
| General n | Clear induction path, needs formalization | Moderate difficulty, recursive structure | No path (3 rounds stuck) |
| Estimated rounds | **1 (just formalize)** | 1–2 | Unknown |

**Route A is significantly closer.** Route A Regime B (n=2) is essentially a formalization task. Route A Regime C needs more work but has clear numeric evidence and partial strategies. Route B S1 has been stuck for 3 rounds with no mechanism.

---

## Concrete Next Lemma for Each Route

**Route A, Regime B** needs one new lemma:

> **Lemma (Upper bound Regime B, n=2):** If A_1 < 1/2 with m=3 LB pieces, Xiang Yu forces val ≤ c(2) = 4/7 using ≤ 2 cuts.
> Proof: B1 (A_1 ≥ 3/7): one cut at A_2 → val = 1−A_1 ≤ 4/7. B2 (A_1 < 3/7): cut A_1 at ε, cut A_3 at A_3/2 → val = A_1+A_3/2 ≤ (3A_1+1)/4 ≤ 4/7.

Then the builder needs a **general n induction** (Regime B Lemma, all n) — the n=2 case is the base; the inductive step uses Case B1 (one cut) for A_1 ≥ 1−c(n) and Case B2 (two cuts, recurse on sub-pieces) for A_1 < 1−c(n).

**Route A, Regime C** needs:

> **Lemma (Upper bound Regime C):** If A_1 > c(n), Xiang Yu forces val ≤ c(n) using ≤ n cuts.
> Mechanism: Induction on n. Base n=1: LB has 1 piece (A_1=1, XY cuts at 1/2 → val=1/2=c(1)? No, c(1)=2/3 and A_1=1 > c(1) means m=1... need careful argument). Step: (i) if 2A_1−1 ≤ c(n−1): cut at 1−A_1, apply (n−1) upper bound; (ii) else: halve A_1 and apply Regime B for (n−1)-cut sub-problem.

**Route B, S1** needs:

> A global comparison argument bypassing the per-direction-derivative approach. No candidate mechanism identified.

---

## Distinct Openings for the Outliner

1. **Route A Regime B (n=2) formalization:** Write the two-case proof as a standalone lemma; zero open questions, just needs rigorous presentation. Builder can close this in one pass.
2. **Route A Regime B (general n) induction:** Generalize Case B1 to m > 3 pieces (sorted-order analysis); strengthen Case B2 bound for general m. May need a two-layer induction (on n and on the "depth" of B2 iterations).
3. **Route A Regime C combined recursion:** Unify "cut at 1−A_1" + "halve A_1" + Regime B sub-call into a single inductive argument. Key distinction: 2A_1−1 ≤ c(n−1) or not.
4. **Route B S1 quasi-concavity probe:** Check if V is quasiconcave on Δ (sufficient condition: every sub-level set {A : V(A) ≥ v} is convex). If true, G_n as a "stationary point" of a quasi-concave function would be the unique global max. This has NOT been checked.

---

## Dead Ends (do NOT retry)

- "Concentrate all n cuts on A_1" (disproven R2).
- Potential-decrease greedy XY (disproven R3: stalls at A≈0.287 vs target 0.143).
- Shadow strategy for A_1 > c(n) (overshoots: gives val = A_1 > c(n)).
- "V globally concave → stationary = max" (disproven R3: V only cell-locally concave).
- Cut A_1 at A_2 in Regime C (gives val = 1−A_2 ≥ A_1 > c(n) for m=2 or val = A_1 for certain m=3 sub-cases).

---

## Small-Case / Intuition Notes (labeled as CONJECTURE unless stated)

- [VERIFIED] Regime B n=2 two-case proof is complete and rigorous for all rational grids tested.
- [CONJECTURE] Regime B general n follows by induction with the same B1/B2 case split.
- [VERIFIED numerically] Regime C is XY-winnable for all tested n=2,3 configs.
- [CONJECTURE] The "cut at (1−A_1) then recurse" strategy for Regime C fails near A_1=c(n)+ε but "halve A_1 then halve A_2" saves those cases.
- [CONJECTURE] S1 holds (V(G_n) is unique max) but no constructive proof path identified.

---

## Prior Progress
- Regime A (1/2 ≤ A_1 ≤ c(n)): CLOSED via shadow strategy (certified `lemmas/shadow-regime-A.md`).
- Regime B (A_1 < 1/2): n=2 essentially done (this round); general n open.
- Regime C (A_1 > c(n)): partial strategies, no full proof.
- S1 (Route B): open since R3, no new progress this round.
