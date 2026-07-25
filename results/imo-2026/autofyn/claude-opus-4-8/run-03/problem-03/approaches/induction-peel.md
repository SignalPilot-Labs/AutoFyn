## Status
partial

## Approaches tried
- (round 6, this file) **UB branch-inequality line RETIRED (dead).** The official IMO-2026
  source's explicit n = 5 all-32-branches counterexample confirms the field's finding F1: a
  top-two-greedy MATCH/BISECT rule is the *wrong* upper-bound structure and is not salvageable as
  scoped. Open gap 2 (Section 4) is therefore recorded as **dead within this approach**; the
  upper bound now belongs to the segment-subset-pigeonhole approach and is not pursued here.
  **Shard-count induction axis (s_1 = H boundary invariance) FALSIFIED (falsify-first).** The
  lbclosure explorer's "slack is constant at the boundary s_1 = H, regardless of how the rest
  splits" is FALSE: with the cut budget respected (≤ n+1 Q-shards), at n = 3 the slack ranges over
  [0, 2] (e.g. rest = {3.9, 0.1} gives slack 1.8, not 0); it is non-constant even at a *fixed*
  rest-shard-count. So the "peel-and-recurse with a constant offset" reduction cannot work. What
  IS rigorous (matched-pair cancellation): at s_1 = H exactly, the Q-shard H and C's top element
  2^{n-1} = H are the two largest and equal, so by L4 they cancel at adjacent ranks and
  S(B_low) = S(Q_low' ⊔ P_{n-2}) with Q_low' = the remaining Q-shards (sum 2^{n-1}). But this
  fires ONLY on the measure-zero boundary s_1 = H, and even there the residual is a valid
  level-(n−1) config only when the remaining shards are ≤ H' = 2^{n-2} (otherwise a shard exceeds
  the smaller cap and there is no smaller copy — this is exactly why the constant invariance
  fails). It gives NO handle on the generic interior s_1 < H, which is the open (CB). Net: the
  shard-count axis is a dead end for closing (CB); the LB residual gaps 1''/1''' stand unchanged.
- (round 1) Set up the peel recursion; L0/L1 reduction and dyadic answer identified,
  upper bound left as the shared open gap.
- (round 2) Made the reduction (L0 claim lemma, L1 order-irrelevance, L2 identity) fully
  rigorous; proved base case n=1; proved lower-bound Case 1 (top piece uncut); introduced
  the integral/layer-cake formula (now certified L3) and reduced Case 2 and the upper bound
  to explicit sub-claims. Both crux gaps remained.
- (round 3, this file) **Lower bound:** replaced the asymmetric Q/C band-split by a cleaner,
  fully rigorous **truncation identity** S(B) = e + S(B_low) at the mid-scale H = 2^{n-1},
  using the new rigorous fact "at most one part of B exceeds H". This handles Case 1 and the
  regime e ≥ 1 completely, and reduces the whole lower bound to one crisp residual statement
  S(B_low) ≥ 1 − e (the "budget cap on W", now recast as a truncation-measure bound). The
  abstract |S(Q)−S(C)| bound and even the sharpened h + |S_low(Q)−S(C)| bound were **verified
  numerically to be too weak** (min over Case 2 drops to 0 for n ≥ 2 while S(B) stays = 1),
  confirming the residual genuinely needs the cut-budget, not just an interval inequality —
  this is the honest remaining lower-bound gap. **Upper bound:** fixed the part-count bug
  (Lemma B now holds for ALL A; base case via the certified min-odd-sum floor), and gave the
  exact S-effect of the MATCH and BISECT moves rigorously, reducing the upper bound to the
  two branch inequalities. The branch inequalities remain the shared field-wide crux (F1: no
  one-pass rule; the value function genuinely depends on the whole profile — verified, a
  single part gives U_k = 0 while dyadic gives 1/D_k, so no (a_1, sum) closed form exists).
- (round 4, this file) **Lower-bound residual advanced.** Proved and banked **L9** (self-pairing:
  S(Q_low)=0 ⟹ W=0 ⟹ S(B_low)=S(C)≥1). Recast the whole residual (A-res) into its cleanest,
  e-free form: with D := N_{Q_low} − N_C, S(B_low)=∫[D odd] and ∫D = 1−e (a sum identity), so
  (A-res) ⟺ the parity-vs-mean inequality **(PM) ∫[D odd] ≥ ∫D**. Made the extremal +1 accounting
  explicit (Q_low = C ⊔ {1} forces the unit via sum(Q_low)−sum(C)=1; (PM) tight there). Proved
  the sufficient pointwise lemma **R2**: D ≤ 1 a.e. ⟹ (PM), covering the entire extremal family
  and ≈87–94% of residual configs. **Refuted** the naive arbitrary-X profile invariant P*
  (numerically, slack → −1.4), pinning the missing content to Q's single-block part budget
  |Q_low|+|C| ≤ 2n+1 (NOT a cut-count cap on C, itself refuted). Remaining gap: compensate the
  interior {D ≥ 2} regions in (PM).

## Current best
Answer **c(n) = 2^n/D_n = 2^n/(2^{n+1}−1)**, D_n := 2^{n+1}−1. The full reduction to the
multiset-refinement game is certified (L0, L1, L2), as are the layer-cake identity (L3) and
min-pairing identity (L4). Base case n = 1 and lower-bound Case 1 are complete.

**New this round (rigorous):** the truncation identity
  S(B) = e + S(B_low),  e := (max part − 2^{n-1})^+,  B_low := B with its top part capped at 2^{n-1},
valid because at most one part of any ≤ n-cut refinement of P_n exceeds 2^{n-1}. This reduces
the entire lower bound to the single residual inequality **S(B_low) ≥ 1 − e**, proven whenever
e ≥ 1 and in Case 1 (e = 2^n − 2^{n-1} ≥ 1); the case e < 1 is the honest lower-bound gap.

**New this round (rigorous):** the residual (A-res) is recast into its cleanest e-free form.
With D(t) := N_{Q_low}(t) − N_C(t), the XOR/sum identities of L3 give S(B_low) = ∫[D odd] dt and
∫D dt = 1 − e, so **(A-res) ⟺ (PM): ∫[D odd] ≥ ∫D**. Banked **L9** (self-pairing ⟹ W=0 ⟹
S(B_low)=S(C)≥1) and proved **R2** (D ≤ 1 a.e. ⟹ (PM)), which covers the exact extremal family
Q_low = C ⊔ {1} and ~87–94% of residual configs. The naive arbitrary-X profile invariant P* is
numerically refuted, so the missing content must use Q's single-block part budget
|Q_low|+|C| ≤ 2n+1 (a cut-count cap on C is separately refuted).

Open gaps (updated round 6):
1. Lower bound, residual (round-4 sharpened → Open gap 1'): prove (PM) ∫[D odd] ≥ ∫D, i.e.
   compensate the interior {D ≥ 2} regions using the single-block part budget. Sub-cases D ≤ 1
   (R2) and S(Q_low)=0 (L9) are closed; the extremal is tight and understood. **Round 5:** the
   entire k_C = 0 regime (Case B) is reduced to one concrete finite shard inequality (CB) via
   exact closed forms (R3/R4); (CB) is numerically confirmed and left as sub-gap 1''. **Round 6:**
   the shard-count induction axis (s_1 = H boundary invariance + matched-pair recurse) is
   FALSIFIED (Section 3.5) — the invariance is not constant and the peel is confined to a
   measure-zero boundary; (CB) is still open.
2. Upper bound: **RETIRED / DEAD (round 6)** — the MATCH/BISECT branch-inequality line is refuted
   by the official n = 5 all-32-branches counterexample. The upper bound is now carried by the
   separate segment-subset-pigeonhole approach, not by this file.

**New this round (round 5, rigorous):** (a) **R3** measure = order statistic —
meas{N_X ≥ k} = x_(k), so meas{N_{Q_low} ≥ k} = s_k and Σ_k s_k = 2^n − e ≤ 2^n (the exact
measure form of the single-block part budget). (b) **R4** level-set form of (PM):
∫[D odd] − ∫D = 2(Σ_m meas{D ≤ −(2m−1)} − Σ_m meas{D ≥ 2m}), so (PM) ⟺ odd-deficit mass ≥
even-excess mass. (c) The pointwise A_{2m} ≤ B_{2m−1} is refuted in general (compensation is
cross-scale), but HOLDS throughout Case B (k_C = 0), which is reduced to the finite inequality (CB)
in the sorted shards subject to Σ s_k ≤ 2^n. Case B strictly enlarges the closed-modulo-gap slice.

---

# Approach: induction on n, peeling the top dyadic scale (self-similar recursion)

Throughout write **D_n = 2^{n+1} − 1** and the **dyadic partition**
G_n = { 2^0/D_n, 2^1/D_n, …, 2^n/D_n } (n+1 parts, sum 1).

**Claim (answer).** For every positive integer n the largest value Liu Bang (LB) can
guarantee is c(n) = 2^n / D_n = 2^n/(2^{n+1} − 1).

We prove both directions modulo two explicitly isolated crux gaps (the residual lower-bound
inequality and the upper-bound branch inequalities). Everything else is complete and rigorous.

---

## 1. Reduction to the multiset-refinement game (CERTIFIED — imported)

We import the four certified lemmas from `results/imo-2026-03/lemmas/`; they are not re-proved
here.

- **L0 (Claiming lemma).** In the alternating item-claiming game on a multiset (mover first,
  each maximizing own total), the mover's optimal total is the odd-ranked sum
  Σ_odd(P) := p_1 + p_3 + …, and taking a currently-largest item is optimal.
- **L1 (Order irrelevance / reduction).** The stick game is equivalent to the
  **multiset-refinement game**: LB chooses a multiset A of ≤ n+1 positive reals with sum 1
  (his ≤ n cut points), XY performs ≤ n split operations (each replaces one part x by two
  positive parts summing to x) producing B, and LB's guaranteed value is
  c(n) = max_A min_B Σ_odd(B).
- **L2 (Alternating-sum identity).** For a multiset B with sum 1, Σ_odd(B) = (1 + S(B))/2,
  where S(B) := Σ_i (−1)^{i+1} b_(i) is the alternating sum of B sorted descending. Hence
  c(n) = (1 + max_A min_B S(B))/2, and since 2·(2^n/D_n) − 1 = 1/D_n, the target
  c(n) = 2^n/D_n is equivalent to **max_A min_B S(B) = 1/D_n**.
- **L3 (Layer-cake identity).** For any finite multiset B, S(B) = meas{ t > 0 : N_B(t) odd },
  where N_B(t) := #{ parts of B > t }; also sum(B) = ∫_0^∞ N_B(t) dt. **Corollary (XOR):** if
  B = Q ⊔ C then N_B = N_Q + N_C, so S(B) = S(Q) + S(C) − 2·meas{ t : N_Q, N_C both odd }.
- **L4 (Min-pairing identity).** S(B) = min over pairings of (Σ_{pairs}|diff| + Σ_{singletons})
  = the consecutive pairing cost; equivalently, with sum(B) = s, S(B) = s − 2β where
  β := max over pairings Σ_{pairs} min = Σ_even(B) (the even-ranked sum).

Two elementary consequences used below (both immediate from L4 / sorting):
- **(P1) Nonnegativity.** S(B) ≥ 0 for every multiset B. *Proof.* Sorting descending,
  b_(1) ≥ b_(2), b_(3) ≥ b_(4), …, so Σ_odd ≥ Σ_even term-by-term, i.e. S = Σ_odd − Σ_even ≥ 0. ∎
- **(P2) Upper triviality.** S(B) ≤ sum(B), since S = sum − 2Σ_even and Σ_even ≥ 0.

Thus we must show: **(Lower)** dyadic A = G_n forces S(B) ≥ 1/D_n for every ≤ n-cut
refinement; **(Upper)** for every A, XY has a ≤ n-cut refinement with S(B) ≤ 1/D_n.

---

## 2. Base case n = 1 (COMPLETE)

Here D_1 = 3, target max_A min_B S(B) = 1/3. For three parts x ≥ y ≥ z with x+y+z = 1,
S = x − y + z = 1 − 2y; for two parts x ≥ y with x+y = 1, S = 1 − 2y.

**Lower (A = G_1 = {1/3, 2/3}).** XY has ≤ 1 cut.
 - No cut: B = {2/3,1/3}, S = 1 − 2·(1/3) = 1/3.
 - Cut the 2/3-part into (u, 2/3−u): the two parts average 1/3, so one is ≥ 1/3 and the other
   ≤ 1/3; the three-part median is exactly 1/3, S = 1/3.
 - Cut the 1/3-part into (v, 1/3−v): both < 1/3 < 2/3, median = max(v,1/3−v) ∈ [1/6,1/3),
   S = 1 − 2·max ∈ (1/3, 2/3].
In every case S ≥ 1/3. ✓

**Upper (any A).** WLOG A = {a, 1−a}, a ≥ 1/2 (A = {1} is a = 1). XY cuts a:
 - a ≥ 2/3: bisect, B = {a/2, a/2, 1−a}; 1−a ≤ 1/3 ≤ a/2, median a/2, S = 1 − a ≤ 1/3.
 - 1/2 ≤ a < 2/3: match, cut a into (1−a, 2a−1); B = {1−a,1−a,2a−1}; median 1−a,
   S = 2a − 1 < 1/3.
 - A = {1}: bisect to {1/2,1/2}, S = 0.
In every case S ≤ 1/3. ✓ Both bounds meet at 1/3, so c(1) = 2/3. ∎(n=1)

---

## 3. Lower bound (Lemma A)

By homogeneity of S (degree 1) it is equivalent to work with the integer multiset
**P_n = {2^0, 2^1, …, 2^n}**, sum D_n, and prove:

**Lemma A.** Every refinement B of P_n by at most n split operations has S(B) ≥ 1.

Dividing by D_n gives S ≥ 1/D_n for G_n, i.e. the lower bound. We use strong induction on n.
The **superincreasing key** is 2^n = 1 + (2^0 + … + 2^{n−1}): the top scale exceeds the sum
of all smaller parts by exactly 1.

*Base n = 0:* B = {1}, S = 1. ✓

### 3.1 The truncation identity at the mid-scale (new, rigorous)

Fix n ≥ 1 and set **H := 2^{n-1}**. Let B be any refinement of P_n by ≤ n cuts.

**Lemma A0 (at most one part above H).** At most one part of B exceeds H.
*Proof.* Every part of B is a sub-part (shard) of some original piece 2^j, 0 ≤ j ≤ n, and is
therefore ≤ 2^j. A shard of 2^j with j ≤ n−1 is ≤ 2^{n-1} = H, hence not > H. Shards of 2^n:
their values are positive and sum to 2^n; if two of them exceeded H = 2^{n-1}, their sum would
exceed 2^n, impossible. Also, if 2^n is uncut, it is the single part 2^n > H. In every case at
most one part of B exceeds H. ∎

Let p* denote the unique part of B exceeding H if it exists, and set
  **e := (max part of B − H)^+ = (p* − H)^+**  (so e = 0 when no part exceeds H).
Note 0 ≤ e ≤ 2^n − H = H, since p* ≤ 2^n. Define **B_low** to be B with p* (if it exists)
replaced by the value H; all parts of B_low are ≤ H.

**Lemma A1 (truncation identity).** S(B) = e + S(B_low).
*Proof.* Apply L3 and split the integral at H.
 - For t > H: by Lemma A0 the only part of B that can exceed t (> H) is p*, so
   N_B(t) = 1 if t < p*, else 0. Hence meas{t > H : N_B(t) odd} = meas{H < t < p*} = e.
 - For 0 < t < H: replacing p* (> H) by H does not change whether that part exceeds t (both
   p* > t and H > t hold), and no other part is altered, so N_B(t) = N_{B_low}(t). Thus
   meas{t < H : N_B odd} = meas{t < H : N_{B_low} odd}. Since every part of B_low is ≤ H,
   N_{B_low}(t) = 0 for t > H, so this equals meas{t > 0 : N_{B_low} odd} = S(B_low).
Adding the two bands (the single point t = H is null) gives S(B) = e + S(B_low). ∎

**Consequence (reduction of the whole lower bound).** Since S(B_low) ≥ 0 by (P1),
  S(B) = e + S(B_low) ≥ e,  so **e ≥ 1 ⟹ S(B) ≥ 1.**
It therefore remains only to prove, when **e < 1**, the residual inequality
  **S(B_low) ≥ 1 − e.**   (A-res)

### 3.2 Case 1 (top piece uncut) — COMPLETE

If XY never cuts 2^n, then p* = 2^n and e = 2^n − 2^{n-1} = 2^{n-1} ≥ 1 (as n ≥ 1). By the
Consequence above, S(B) ≥ e ≥ 1. ✓ (This reproves the round-2 Case 1 in one line.)

More generally, whenever the top shard is large — precisely when e ≥ 1, i.e. the surviving big
shard p* ≥ 2^{n-1} + 1 — the lower bound holds with no further work.

### 3.3 Case 2 residual (e < 1): reduction to a parity-vs-mean inequality (NEW, round 4)

**Setup.** The residual is (A-res): if e < 1 then S(B_low) ≥ 1 − e. First note e < 1 **forces
c ≥ 1** (at least one cut inside the top block 2^n): if c = 0 then Q = {2^n}, p* = 2^n and
e = 2^n − H = 2^{n-1} ≥ 1, contradicting e < 1. Hence, writing C for the shards of
R = {2^0,…,2^{n-1}} = P_{n-1} and k_C for the number of cuts XY spends inside R, we have
k_C ≤ n − c ≤ n − 1, so **C is a ≤(n−1)-cut refinement of P_{n-1}**. By the strong-induction
hypothesis Lemma A(n−1), **S(C) ≥ 1**. Every part of C is ≤ 2^{n-1} = H (a shard of 2^j,
j ≤ n−1, is ≤ 2^j ≤ H). By L6/A0 at most one part of B exceeds H, and since C ≤ H that part lies
in Q; let Q_low be Q with that part (if any) capped to H, so B_low = Q_low ⊔ C, all parts ≤ H.
By the L3 XOR corollary,
  S(B_low) = S(Q_low) + S(C) − 2W,  W := meas{t : N_{Q_low}(t) odd ∧ N_C(t) odd}.

**Mini-lemma L9 (self-pairing kills the overlap) — RIGOROUS, banked.**
*If S(Q_low) = 0 — equivalently N_{Q_low}(t) is even for a.e. t > 0, e.g. Q_low's sorted parts
pair into equal consecutive values (the pure-BISECT boundary, Q = {2^{n-1}, 2^{n-1}}) — then
W = 0 and S(B_low) = S(C) ≥ 1 ≥ 1 − e.*
*Proof.* By L3, S(Q_low) = meas{t : N_{Q_low}(t) odd}. The overlap integrand
{N_{Q_low} odd ∧ N_C odd} is supported inside {N_{Q_low} odd}, so
W ≤ meas{t : N_{Q_low}(t) odd} = S(Q_low) = 0, whence W = 0. Then
S(B_low) = S(Q_low) + S(C) − 2W = 0 + S(C) − 0 = S(C) ≥ 1 by the IH, and 1 ≥ 1 − e since
e ≥ 0. ∎
This disposes of the entire h = 0 / pure-bisect boundary slice with no new machinery. (Proposed
to the reviewer below as certified lemma **L9**.)

**The clean reformulation (parity dominates mean) — NEW.** Define the integer step function
  **D(t) := N_{Q_low}(t) − N_C(t).**
Since N_{B_low} = N_{Q_low} + N_C ≡ N_{Q_low} − N_C = D (mod 2), the odd-sets coincide, so by L3
  S(B_low) = meas{t : N_{B_low}(t) odd} = meas{t : D(t) odd} = ∫_0^∞ [D(t) odd] dt.
And by the L3 sum identity ∫_0^∞ N_X = sum(X),
  ∫_0^∞ D dt = sum(Q_low) − sum(C) = (2^n − e) − (2^n − 1) = **1 − e**
(sum(Q_low) = 2^n − e because capping the unique > H part from p* to H removes exactly
p* − H = e, and if no part exceeds H then e = 0; sum(C) = sum(R) = 2^n − 1 = D_{n-1}).
Therefore (A-res) is **exactly** the parity-dominates-mean inequality

  **(PM)   ∫_0^∞ [D(t) odd] dt  ≥  ∫_0^∞ D(t) dt   ( = 1 − e ).**

This is the residual in its cleanest, e-free form: the target constant 1 − e is *automatically*
the mean of D, so the whole e-dependence has been absorbed into a single sum identity, and what
remains is a pure statement "the measure where an integer function is odd is at least its
integral." The explorer's extremal witness Q_low = C ⊔ {1} (the "surviving +1" is forced by
sum(Q_low) − sum(C) = 1) gives D(t) = [t < 1] ∈ {0,1}, so ∫[D odd] = 1 = ∫D — **(PM) is tight**
there. This exhibits the extremal +1 accounting explicitly (addressing the outline-reviewer's
hold): the surviving unit is not asserted, it is the value of ∫D forced by the sum constraint.

**Sufficient pointwise lemma R2 (covers the extremal family) — RIGOROUS.**
*If D(t) ≤ 1 for a.e. t, then (PM) holds.*
*Proof.* For an integer d put f(d) := [d odd] − d. If d ≤ 0 then [d odd] ≥ 0 and −d ≥ 0, so
f(d) ≥ 0; if d = 1 then f(1) = 1 − 1 = 0. Hence f(d) ≥ 0 for every integer d ≤ 1. If D ≤ 1
a.e. then f(D(t)) ≥ 0 a.e., so ∫[D odd] − ∫D = ∫ f(D) ≥ 0. ∎
R2 covers every Q_low with N_{Q_low}(t) ≤ N_C(t) + 1 for all t — in particular the whole
**extremal family** Q_low = C ⊔ {one part u} (there N_{Q_low} = N_C + [t<u], so D = [t<u] ∈
{0,1}), hence the exact minimizer of S(B). A quick incremental numeric probe (n ≤ 4, 30 000
random residual configs each) confirms D(t) ≤ 1 holds on ≈ 87–94% of configurations, so R2 is a
large, sharp slice — but not all.

**The genuine residual: compensating the D ≥ 2 regions.** Near the bottom D is always ≤ 1:
|Q_low| ≤ c + 1 and |C| = n + k_C, so D(0+) = (c+1) − (n+k_C) ≤ (c+1) − (n) − k_C, and using
c ≤ n − k_C this is ≤ 1 − 2k_C ≤ 1. But in the interior D can reach 2 (e.g. n = 3,
Q = {2.5, 2.7, 2.8}, C = {4,2,1}: D = 2 on (2, 2.5)); on {D ≥ 2} we have f(D) < 0, and (PM) then
needs compensation from regions where D ≤ 0 (there f(D) > 0). Numerically the compensation is
always exactly enough (min over residual configs of S(B_low) − (1−e) = 0 at n ≤ 4). The honest
missing content is a *structural* reason the compensation never fails.

**The corrected profile invariant, and what is refuted.** The naive strengthened IH
  P*(m) := "for every ≤ m-cut refinement C of P_m and every multiset X with parts ≤ 2^m and
  sum(X) ≥ sum(C), one has meas{t : N_X + N_C odd} ≥ sum(X) − sum(C)"
is **FALSE for arbitrary X** — a fast incremental probe (m ≤ 3) drives its slack to −1.4. So a
profile statement that ignores the structure of Q cannot work: the invariant must encode that
**Q_low is a capped refinement of the *single* block 2^n by c cuts with c + k_C ≤ n**, whence the
combined part budget |Q_low| + |C| = (c+1) + (n+k_C) ≤ 2n + 1. This is the correct home for the
"cut budget", and — per the round-4 refutation — it lives on **Q's single-block structure**, NOT
on a cap of W by the number of cuts spent inside C (that mechanism is refuted: the true n = 3
extremal spends *zero* cuts on C yet has large W). We record the sharpened obligation:

> **Open gap 1' (round-4 sharpened).** Prove (PM): ∫[D odd] ≥ ∫D for D = N_{Q_low} − N_C, where
> Q_low is the capped ≤ c-cut refinement of the single block {2^n} and C a ≤ k_C-cut refinement
> of P_{n-1}, with c ≥ 1 and c + k_C ≤ n. Equivalently: the (negative) f-mass ∫_{D≥2}(D − [D odd])
> on the over-stacked regions is ≤ the (positive) f-mass ∫_{D≤0}([D odd] − D) on the deficit
> regions. The single-block part budget |Q_low| + |C| ≤ 2n + 1 must be used; the arbitrary-X
> profile invariant P* is refuted, and so is any "cuts-on-C cap W". Proven sub-cases: D ≤ 1 a.e.
> (R2, including the exact extremal family) and S(Q_low) = 0 (L9).

**Net advance this round.** The residual is now a single scalar-free inequality (PM) between the
odd-measure and the mean of one explicit integer function D, with (a) its tight extremal
(Q_low = C ⊔ {1}) and its extremal +1 accounting made explicit via the sum identity, (b) the
self-pairing boundary (L9) and the entire D ≤ 1 slice (R2) fully closed, and (c) the false
directions (arbitrary-X P*, cuts-on-C cap on W) fenced off with a proof/refutation. The one
remaining obligation is the compensation of the interior D ≥ 2 regions using the single-block
part budget.

Everything in Section 3 except Open gap 1' is complete: the reduction (Lemma A0/L6, A1), Case 1,
the entire regime e ≥ 1, the reformulation (PM), and the sub-cases L9 and R2.

### 3.4 Round-5 advance: the level-set form of (PM), the shard-sum bound, and Case B

Three rigorous new pieces this round, plus a reduction of the entire k_C = 0 regime to one
concrete finite inequality (numerically confirmed, honestly left as a sub-gap).

**Lemma R3 (measure = order statistic; single-block sum bound) — RIGOROUS, new.**
For any finite multiset X with parts sorted descending x_(1) ≥ x_(2) ≥ …,
  meas{ t > 0 : N_X(t) ≥ k } = x_(k)   (with x_(k) := 0 for k > |X|).
*Proof.* N_X(t) ≥ k ⟺ at least k parts exceed t ⟺ the k-th largest part exceeds t ⟺ t < x_(k).
So {N_X ≥ k} = (0, x_(k)), of measure x_(k). ∎ (Summing over k recovers ∫N_X = sum X, i.e. L3.)
Applied to Q_low, whose c+1 shards sort as s_1 ≥ … ≥ s_{c+1} (all ≤ H, capped), this gives
  meas{ N_{Q_low} ≥ k } = s_k,   and   Σ_{k} s_k = sum(Q_low) = 2^n − e ≤ 2^n.   (†)
This is the exact **measure-theoretic form of the single-block part budget**: because Q_low
refines the *single* block 2^n, its level sets have total mass ≤ 2^n and shrink like a sorted
sequence summing to ≤ 2^n. (This is the lever the refuted arbitrary-X invariant P* lacked.)

**Lemma R4 (level-set form of (PM)) — RIGOROUS, new.** Write, for m ≥ 1,
  A_m := meas{ D ≥ m },   B_m := meas{ D ≤ −m }.
Then, using the layer-cake decomposition of f(d) := 1[d odd] − d,
  1[d odd] = Σ_{m≥1}(1[d≥2m−1] − 1[d≥2m]) + Σ_{m≥1}(1[d≤−(2m−1)] − 1[d≤−2m])
(telescoping: for d = 2m−1 the positive block gives 1, for d = 2m it gives 0, symmetrically for
d < 0, and 0 at d = 0 — checked termwise), integrating and cancelling gives the identity
  ∫ 1[D odd] − ∫ D = 2( Σ_{m≥1} B_{2m−1} − Σ_{m≥1} A_{2m} ).
Hence **(PM) ⟺ Σ_{m≥1} B_{2m−1} ≥ Σ_{m≥1} A_{2m}**, i.e. the odd-deficit mass dominates the
even-excess mass. *Derivation of the identity.* With A_k, B_k as above,
∫1[D odd] = Σ_m(A_{2m−1}−A_{2m}) + Σ_m(B_{2m−1}−B_{2m}) and ∫D = Σ_k A_k − Σ_k B_k; subtracting,
the A-part is Σ_m(A_{2m−1}−A_{2m}) − Σ_m(A_{2m−1}+A_{2m}) = −2Σ_m A_{2m}, and the B-part is
Σ_m(B_{2m−1}−B_{2m}) + Σ_m(B_{2m−1}+B_{2m}) = 2Σ_m B_{2m−1}. ∎ (Verified on the reviewer's and
several sampled configs: e.g. Q_low={4,4}, C={2,16/9,4/3,1,8/9} gives ΣB_{odd}=20/9, ΣA_{ev}=18/9,
so LHS−RHS = 4/9 = ∫1[D odd]−∫D. ✓) This is an *equivalent* recasting (not by itself a closure),
but it turns (PM) into a pure comparison of super/sub-level-set measures of the single walk D,
which is the natural home for the two-source dichotomy.

**A caution the numerics force (do NOT retry).** The tempting *pointwise* strengthening
"A_{2m} ≤ B_{2m−1} for every m" is **FALSE in general**: for n = 3, Q_low = {4,4},
C = {2, 16/9, 4/3, 1, 8/9} (k_C = 2), one has A_2 = 2 > B_1 = 4/3 — the even-excess at level 2 (a
long D = 2 plateau just under the ceiling, of length H − max C) exceeds the level-1 deficit, and is
only rescued by the *deeper* deficit B_3 = 8/9 (Σ B_{odd} = 20/9 ≥ ΣA_{ev} = 2). So the true (PM)
is genuinely aggregate/non-local; the compensation reaches across scales. This kills any per-level
charging and confirms the dichotomy must be global.

**Case B (k_C = 0): reduction to one concrete shard inequality — RIGOROUS reduction; the
inequality itself numerically confirmed (sub-gap).** When XY spends *all* its cuts inside the top
block (k_C = 0), C = P_{n−1} = {2^0, …, 2^{n−1}} is the exact dyadic staircase, so N_C(t) = n − j
on the band I_j := (2^{j−1}, 2^j) (j = 1, …, n−1), N_C = n on I_0 := (0, 1), and N_C = 0 for
t > H. Using Lemma R3 (meas{N_{Q_low} ≥ k} = s_k), the excess/deficit level sets have **closed
forms** (convention s_k = +∞ for k ≤ 0, s_k = 0 for k ≥ c+2):
  A_{2m} = meas{D ≥ 2m} = Σ_{j=1}^{n−1} ( min(2^j, s_{n−j+2m}) − 2^{j−1} )^+ ,
  B_{2m−1} = meas{D ≤ −(2m−1)} = Σ_{j=0}^{n−1} ( 2^j − max(ℓ_j, s_{n−j−2m+2}) )^+ ,
with ℓ_0 = 0, ℓ_j = 2^{j−1}. *Derivation.* On band I_j, D(t) = N_{Q_low}(t) − (n−j); D ≥ 2m ⟺
N_{Q_low}(t) ≥ n−j+2m ⟺ t < s_{n−j+2m} (Lemma R3), intersecting the band gives the excess term;
D ≤ −(2m−1) ⟺ N_{Q_low}(t) ≤ n−j−2m+1 ⟺ t ≥ s_{n−j−2m+2}, giving the deficit term. Band I_0 and
the top region t > H contribute 0 excess for m ≥ 1 (they need s_{≥ n+2m} = 0, resp. s_{2m} ≤ H < t).
*(Both closed forms verified exactly against brute force: 0 mismatches over 90 000 random Case-B
configs at n = 4.)* By Lemma R4, Case B therefore reduces to the finite inequality
  **(CB)  Σ_{m≥1} A_{2m} ≤ Σ_{m≥1} B_{2m−1}**  in the sorted shards s_1 ≥ … ≥ s_{c+1} of 2^n,
subject only to Σ_k s_k = 2^n − e ≤ 2^n, s_k ≤ H = 2^{n−1}, and c ≤ n. Numerically, in Case B even
the *pointwise* A_{2m} ≤ B_{2m−1} holds (0 violations over 60 000 configs at n = 2, 3, 4) — so
Case B is far more benign than the general case, and the honest missing content is a proof of (CB)
from the shard-sum bound (†). This is a strictly larger closed-modulo-(CB) slice than R2/L9: it is
the entire "all cuts on the top block" regime, at *any* c ≤ n and any shard profile.

> **Open gap 1'' (round-5, Case B).** Prove (CB) — equivalently the pointwise Case-B claim
> A_{2m} ≤ B_{2m−1} — from Σ_k s_k ≤ 2^n and s_k ≤ H. Mechanism to pursue: an excess shard is
> "large for its rank" (s_k > 2^{n−k+2m−1}), and Σ s_k ≤ 2^n caps how many shards can be that large,
> forcing the remaining c+1−(few) shards to be small enough to manufacture the compensating
> odd-deficit mass B_{2m−1} lower down. The k_C ≥ 1 regime additionally has D(0+) ≤ 1 − 2k_C ≤ −1
> (a guaranteed deep bottom band) but there the pointwise claim FAILS and only the aggregate (CB-like)
> statement survives — so k_C ≥ 1 needs the full aggregate two-source charging (still open).

### 3.5 Round-6: shard-count induction axis — FALSIFIED (falsify-first, per gate)

The lbclosure explorer proposed a genuinely new reduction axis for (CB): an **induction on the
number of Q-shards** (orthogonal to the induction on n), keyed on a claimed *boundary invariance*
at s_1 = H (the top Q_low-shard equal to the cap), with a matched-pair peel of that H-shard
against C's own top element (also H = 2^{n-1} in Case B) as an L9-style zero-net-displacement
pair, then a recurse one level down. Per the gate's falsify-first directive we tested the two
load-bearing claims on small cases (exact `Fraction`, n ≤ 6) **before** investing. Both fail.

**Claim tested (invariance).** "At s_1 = H, the slack S(B_low) − (1 − e) is constant, independent
of how the remaining mass 2^n − H = H splits into further shards ≤ H." **FALSE.** Respecting the
cut budget (≤ n cuts on the top block, i.e. ≤ n+1 Q-shards):
 - n = 2: slack ≡ 0 (only one split possible: Q = {H, H}, trivially constant — the sole data point
   the explorer's n = 3, r = 2 examples resembled).
 - n = 3: slack ranges over **[0, 2]** across budget-legal splits (not constant). Concrete witness:
   rest = {3.9, 0.1} gives B_low = {4, 3.9, 2, 1, 0.1} ⊔ {4,2,1}, S(B_low) = 14/5, slack = 9/5,
   whereas rest = {2, 2} gives slack 0.
 - n = 4, 5, 6: slack ranges [0, 4], [0, 10], [0, 20] respectively.
The slack is non-constant **even at a fixed rest-shard-count r** (n = 3, r = 2: range [0, ~2]).
The explorer's "constant" observation was an artifact of three hand-picked r = 2 examples whose
rest-shards happened to interleave the dyadic bands {2, 1} evenly.

**Why the recursion cannot close (rigorous diagnosis).** The one *rigorous* fragment is the
matched-pair cancellation, and its failure mode is instructive:
 - At s_1 = H exactly, B_low's two largest parts are the Q-shard H and C's top element
   2^{n-1} = H; being equal and adjacent in rank they cancel by L4, so
   **S(B_low) = S(Q_low' ⊔ P_{n-2})**, where Q_low' = the remaining Q-shards (sum 2^{n-1}) and
   P_{n-2} = C ∖ {H} = {1, …, 2^{n-2}}. (Verified exactly: {4,2,2}↦S(resid)=1, {4,3,1}↦1,
   {4,3.9,0.1}↦14/5, matching S(B_low) in every case.)
 - The residual Q_low' ⊔ P_{n-2} is a *valid* level-(n−1) Case-B configuration — hence closable by
   the IH Lemma A(n−1) — **only when every remaining shard is ≤ H' = 2^{n-2}** (the smaller cap).
   But Q_low' shards are capped at H = 2^{n-1}, not H'; a shard in (H', H] (e.g. 3.9 at n = 3)
   exceeds the smaller cap, so the residual is NOT a smaller copy of the problem, and re-applying
   the truncation identity A1 at level n−1 gives e' = (shard − H')^+ that varies with the split.
   **This variable e' is exactly the non-constant slack** — the invariance fails for precisely the
   reason the recursion fails.
 - Worse, the entire mechanism fires only on the **measure-zero boundary s_1 = H**. For the generic
   interior s_1 < H (the bulk of Case B), the top two parts of B_low are H (from C) and s_1 < H —
   they do **not** cancel — so there is no matched pair to peel and no recursion at all.

**Verdict (per gate: record why, stop, do not force).** The shard-count induction axis via the
s_1 = H invariance is a **dead end** for closing (CB): the invariance is false, the matched-pair
peel is confined to a measure-zero boundary, and even there it only recurses when no residual
shard exceeds the smaller cap. It gives no leverage on the interior. Gaps 1'' (Case-B (CB)) and
1''' (k_C ≥ 1 aggregate charging) stand unchanged. No new violation of (CB) was found (min slack
= 0 throughout, so the LB claim itself remains safe — only this *route* to proving it is refuted).
Do NOT re-attempt: (i) any "constant boundary offset at s_1 = H", (ii) peel-and-recurse on
shard-count expecting a level-(n−1) smaller copy (the cap does not shrink), (iii) majorization /
Robin-Hood on the shard vector (separately refuted by lbclosure).

---

## 4. Upper bound (Lemma B)

Work with the value function on multisets A of any part count:
  U_k(A) := min over refinements of A using at most k split operations of S(B).
XY may stop early and may take the splits in any order, so U satisfies the exact recursion
  U_0(A) = S(A),   U_k(A) = min( S(A),  min_{one split A→A'} U_{k−1}(A') ).   (R)
The upper bound is the homogeneous statement:

**Lemma B.** For every multiset A (**any** number of positive parts),
  U_k(A) ≤ sum(A) / D_k.
Applied with k = n and sum(A) = 1 this gives min_B S(B) ≤ 1/D_n for every LB choice A, i.e.
max_A min_B S(B) ≤ 1/D_n. Together with Lemma A (which gives ≥ 1/D_n at A = G_n),
max_A min_B S(B) = 1/D_n, whence by L2 c(n) = 2^n/D_n.

**Part-count fix (this round).** The round-2 draft restricted A to ≤ k+1 parts; that
hypothesis is both unnecessary and self-inconsistent under (R) (a BISECT grows the part count).
It is dropped. The base case survives at **any** part count because of the certified min-odd
floor Σ_odd(A) ≥ sum(A)/2, equivalently S(A) ≥ 0 (our (P1)):
  *Base k = 0:* U_0(A) = S(A) ≤ sum(A) = sum(A)·2^0/D_0 (D_0 = 1) by (P2). ✓ (Valid for any
  number of parts; there is no part-count restriction anywhere below.)

**The two candidate moves and their exact S-effect (rigorous).** Sort A = {a_1 ≥ a_2 ≥ …} with
sum s and let ρ := s − a_1 be the sum of the parts other than a_1. Two splits of the top part:

 - **BISECT.** Replace a_1 by (a_1/2, a_1/2). Call the result A_B. Its top part is now
   max(a_1/2, a_2); a_1's rank-1 contribution to S is capped at a_1/2.
 - **MATCH** (available when a_2 exists, i.e. A has ≥ 2 parts). Replace a_1 by
   (a_2, a_1 − a_2), where a_2 ≤ a_1 so both are positive (if a_1 = a_2, the second part is 0
   and the "cut" is degenerate; handle ties by noting a matched pair of equal largest parts
   already cancels — see below). Call the result A_M. **Both** the original a_2 and the new twin
   a_2 survive (round-2 pitfall: the matched original is *not* deleted). In the sorted list of
   A_M the two equal values a_2 occupy adjacent ranks; being consecutive and equal they
   contribute +a_2 − a_2 = 0 to S. Concretely, by L4 (consecutive pairing) the two equal a_2's
   pair off at zero cost, so
     S(A_M) = |diff of that pair| + (cost of pairing the remaining parts)
            = 0 + S( A_M ∖ {a_2, a_2} )  when the two a_2's are the two largest,
   and in general S(A_M) equals the alternating sum of the multiset
   { a_2, a_1 − a_2 } ⊔ (A ∖ {a_1}) sorted descending. The carry a_1 − a_2 (< a_2) re-enters a
   strictly smaller subgame.

**Ties among the largest.** If a_1 = a_2 already (two equal largest parts in A), MATCH is not
needed: those two equal parts cancel at adjacent ranks (L4), so S(A) already equals the
alternating sum of A ∖ {a_1, a_2}, effectively reducing the profile at zero cut cost.

**The inductive step (reduced to the branch inequalities).** Assume Lemma B for k−1. Fix A with
sum s. Because cuts preserve the total, the plain IH gives, for either move's result A',
U_{k−1}(A') ≤ s/D_{k−1}. But
  s/D_{k−1} > s/D_k     (since D_{k−1}·2^k − D_k·2^{k−1} = 2^{k−1} > 0, i.e. 1/D_{k−1} > 1/D_k),
so the generic IH bound is **too large** — the chosen split must genuinely beat IH. This is
exactly explorer finding F1 (no one-pass syntactic rule works; a value function that depended
only on (a_1, s) is impossible — a single part {s} has U_k = 0 via one bisect, while the dyadic
profile of the same sum has U_k = s/D_k > 0, so the value function genuinely depends on the
whole profile). The governing parameter is r := a_1/ρ (top vs. rest), mirroring the
superincreasing condition:

> **Open gap 2 (upper-bound branch inequalities) — RETIRED / DEAD (round 6).** The official
> IMO-2026 source exhibits an explicit n = 5 counterexample checking all 32 branches of the
> top-two-greedy MATCH/BISECT tree: no such greedy rule attains the target. This confirms F1 and
> shows the top-two-greedy structure is the *wrong* upper-bound framing. **Do not re-attempt this
> line in this approach.** The upper bound is now carried by the segment-subset-pigeonhole
> approach (mirrored-cut construction + subset-sum pigeonhole), which does not use the value
> function U_k at all. The recursion (R), the part-count fix, the base case, and the exact
> MATCH/BISECT S-effect formulas below remain rigorous and reusable, but the two branch
> inequalities that would close the bound are refuted as scoped. The original (now-dead) statement
> was:
>
> **Open gap 2 (upper-bound branch inequalities).** For every A and k ≥ 1, the split
> c ∈ {MATCH, BISECT} minimizing U_{k−1}(c(A)) satisfies U_{k−1}(c(A)) ≤ s/D_k. Concretely: if
> r ≥ 1 (top dominates), BISECT caps a_1 at a_1/2 and closes the rest by IH; if r < 1, MATCH
> cancels the twin a_2 at adjacent rank and the carry a_1 − a_2 enters a strictly smaller
> subgame closed by IH. Equalizing the two branch bounds over LB's choice of A pins the
> geometric ratio 2 and the value 2^k/D_k, so the dyadic profile is LB's maximizer.

Open gap 2 is the shared field-wide crux. What is *rigorous* here: the recursion (R), the
part-count fix and base case (via the certified min-odd floor), and the exact S-effect of the
MATCH and BISECT moves (including the zero-cost cancellation of equal adjacent parts, from L4).
The two branch inequalities and the equalization that pins the maximizer to dyadic are the
remaining obligation. A brute-force search (thousands of random A, n = 1..4) confirms some
≤ n-cut refinement always reaches S ≤ 1/D_n, and separately confirms that **pure bisection of
the global max fails badly** (17–75% of trials exceed target), so MATCH is essential and the
min in (R) carries genuine multi-step lookahead.

---

## 5. Assembling and verifying the answer

Granting Open gaps 1 and 2, Section 3 gives max_A min_B S(B) ≥ 1/D_n (at A = G_n) and Section 4
gives ≤ 1/D_n (every A), hence max_A min_B S(B) = 1/D_n and by L2
  **c(n) = (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) = 2^{n+1}/(2 D_n) = 2^n/D_n = 2^n/(2^{n+1}−1).**

**Verification for small n.**
 - n = 1: 2/3, matching the complete base case of Section 2.
 - n = 2: 4/7. Refining G_2 = {1,2,4}/7 by 2^2 → 2+2 and 2^1 → 1+1 gives {2,2,1,1,1}/7 with
   Σ_odd = (2+1+1)/7 = 4/7 (S = 1/7), tight; the numeric min-search returns exactly this.
 - n = 3: 8/15 (S = 1/15), confirmed by numeric min-search.

---

## Open gaps (the honest remaining obligations)

1. **Lower-bound residual (Section 3.3), round-4 sharpened form (PM).** Prove
   ∫[D odd] ≥ ∫D for D = N_{Q_low} − N_C (Q_low a capped ≤c-cut refinement of the single block
   {2^n}, C a ≤k_C-cut refinement of P_{n-1}, c ≥ 1, c+k_C ≤ n). Equivalently compensate the
   interior {D ≥ 2} regions using the single-block part budget |Q_low|+|C| ≤ 2n+1. Reductions
   done and new this round: (A-res) ⟺ (PM) via the sum identity ∫D = 1−e; sub-cases D ≤ 1 (R2,
   incl. the exact extremal family Q_low = C ⊔ {1}) and S(Q_low)=0 (L9) are fully closed.
   Refuted, do NOT retry: the arbitrary-X profile invariant P* (slack → −1.4), the interval
   bounds |S(Q)−S(C)| and h + |S_low(Q)−S(C)|, any cut-count cap on C (the true extremal
   spends zero cuts on C with W large), and — new this round — the **pointwise** level claim
   A_{2m} ≤ B_{2m−1} in the general (k_C ≥ 1) case (n=3, Q_low={4,4}, C={2,16/9,4/3,1,8/9}:
   A_2 = 2 > B_1 = 4/3). **Progress this round (round 5):** R3 (meas{N_X ≥ k} = x_(k), giving
   Σ s_k ≤ 2^n), R4 (level-set form of (PM)), and the reduction of the whole k_C = 0 regime
   (Case B) to the concrete shard inequality (CB), numerically confirmed. Remaining sub-gaps:
   1'' (prove (CB) for Case B from Σ s_k ≤ 2^n) and the full aggregate two-source charging for
   k_C ≥ 1 (where only the aggregate, not the pointwise, survives).
2. **Upper-bound branch inequalities (Section 4) — RETIRED / DEAD (round 6).** Refuted by the
   official n = 5 all-32-branches counterexample: top-two-greedy MATCH/BISECT is the wrong UB
   structure. No longer an open obligation of *this* approach; the upper bound is owned by
   segment-subset-pigeonhole. The recursion (R), part-count fix, base case, and exact
   MATCH/BISECT S-effect formulas remain rigorous and reusable, but the branch inequalities that
   would close the bound are dead as scoped.

Everything else — L0–L4, base case n = 1, lower-bound Case 1, the truncation reduction, and
the exact MATCH/BISECT value formulas — is complete and rigorous.

## Promotable lemmas
- **A0 (at most one large shard).** For any refinement of the superincreasing set
  {2^0,…,2^n} by any number of cuts, at most one part exceeds 2^{n-1}. Proved in full
  (Section 3.1) — purely from "each shard ≤ its origin" and "two shards of 2^n both > 2^{n-1}
  would sum > 2^n". Reusable by any lower-bound approach.
- **A1 (truncation identity).** With H = 2^{n-1}, e = (max part − H)^+ and B_low = B with its
  top part capped at H, one has S(B) = e + S(B_low). Proved in full (Section 3.1) from L3 by
  splitting the layer-cake integral at H. Cleaner than the Q/C band split; isolates exactly the
  uncancellable high-band mass e. Reusable.
- **MATCH/BISECT exact effect (Section 4).** BISECT caps the top contribution at a_1/2; MATCH
  creates an equal twin of a_2 that cancels at adjacent rank (both copies survive), leaving
  carry a_1 − a_2 in a strictly smaller subgame. Rigorous consequence of L4. Reusable by the
  value-function/charging upper-bound approaches.
- **L9 (self-pairing kills the overlap) — NEW, propose to certify.** In the XOR split
  B_low = Q_low ⊔ C with S(B_low) = S(Q_low) + S(C) − 2W, if S(Q_low) = 0 (i.e. N_{Q_low}(t)
  even for a.e. t) then W = 0 and S(B_low) = S(C). Proof in full (Section 3.3): W ≤ meas{N_{Q_low}
  odd} = S(Q_low) = 0. Purely from L3; one line, reusable by every lower-bound approach to
  dispose of the pure-BISECT / self-pairing boundary.
- **R1 (parity-vs-mean reformulation) — NEW.** For B_low = Q_low ⊔ C with all parts ≤ H, set
  D := N_{Q_low} − N_C. Then S(B_low) = ∫[D odd] dt (since N_{B_low} ≡ D mod 2, via L3) and
  ∫D dt = sum(Q_low) − sum(C). Hence S(B_low) ≥ sum(Q_low) − sum(C) ⟺ ∫[D odd] ≥ ∫D. Proved in
  full (Section 3.3) from L3. Converts a residual "≥ constant" into an odd-measure-vs-integral
  comparison; reusable by any XOR-split lower-bound approach.
- **R2 (pointwise sufficient condition) — NEW.** With D as in R1, if D(t) ≤ 1 for a.e. t then
  ∫[D odd] ≥ ∫D. Proof in full (Section 3.3): f(d) := [d odd] − d ≥ 0 for every integer d ≤ 1.
  Covers the extremal family Q_low = C ⊔ {one part}. Reusable.
- **R3 (measure = order statistic; single-block sum bound) — NEW, propose to certify.** For any
  finite multiset X with parts sorted descending, meas{t > 0 : N_X(t) ≥ k} = x_(k) (the k-th largest
  part; 0 if k > |X|). Proof in full (Section 3.4): N_X(t) ≥ k ⟺ t < x_(k). Corollary for the
  single-block refinement Q_low: meas{N_{Q_low} ≥ k} = s_k and Σ_k s_k = sum(Q_low) = 2^n − e ≤ 2^n
  — the exact measure form of the single-block part budget. Reusable by every layer-cake approach.
- **R4 (level-set form of (PM)) — NEW, propose to certify.** With A_m := meas{D ≥ m},
  B_m := meas{D ≤ −m}, one has the identity ∫[D odd] − ∫D = 2(Σ_{m≥1} B_{2m−1} − Σ_{m≥1} A_{2m}).
  Proof in full (Section 3.4) via the layer-cake decomposition of f(d) = 1[d odd] − d. Hence
  (PM) ⟺ Σ_m B_{2m−1} ≥ Σ_m A_{2m} (odd-deficit mass ≥ even-excess mass). Reusable; recasts the
  residual as a pure super/sub-level-set comparison of the single walk D.
- **(Case-B closed forms) — NEW, rigorous reduction (the inequality (CB) itself is a sub-gap).**
  When C = P_{n−1} (k_C = 0), A_{2m} = Σ_{j=1}^{n−1}(min(2^j, s_{n−j+2m}) − 2^{j−1})^+ and
  B_{2m−1} = Σ_{j=0}^{n−1}(2^j − max(ℓ_j, s_{n−j−2m+2}))^+ (ℓ_0=0, ℓ_j=2^{j−1}), proved in Section
  3.4 from R3 and the dyadic staircase N_C. Reduces the whole k_C = 0 regime to (CB) Σ A_{2m} ≤ Σ B_{2m−1}.

## Build report (round 6)
- **Status: partial.** Answer c(n) = 2^n/(2^{n+1}−1) unchanged. This round was scoped by the gate
  to (i) RETIRE the refuted UB branch-inequality line and (ii) falsify-first the shard-count
  induction axis before investing.
- **Done round 6:** (1) UB branch-inequality line RETIRED as dead (official n = 5 all-32-branches
  counterexample); Open gap 2 recorded dead, UB delegated to segment-subset-pigeonhole. (2)
  Falsify-first on the s_1 = H boundary invariance: **FALSIFIED** — slack is non-constant even at
  fixed rest-shard-count (n = 3: range [0, 2]; witness rest = {3.9, 0.1}, slack 9/5). Rigorous
  diagnosis (Section 3.5): the matched-pair cancellation S(B_low) = S(Q_low' ⊔ P_{n-2}) at s_1 = H
  is real (L4) but (a) fires only on the measure-zero boundary s_1 = H, (b) recurses to a valid
  level-(n−1) copy only when every residual shard ≤ H' = 2^{n-2}; a shard in (H', H] breaks the
  cap and produces the variable e' that is precisely the non-constant slack. Shard-count induction
  axis is a dead end for (CB).
- **Prior-round LB results intact and unchanged:** R3 (meas{N_X ≥ k} = x_(k), Σ s_k ≤ 2^n), R4
  (level-set form of (PM)), Case-B closed-form band formulas, reduction of k_C = 0 to (CB).
- **Remaining GAPs (LB only; UB retired from this file):**
  1'' (LB, Case B): prove (CB) Σ_m A_{2m} ≤ Σ_m B_{2m−1} from Σ_k s_k ≤ 2^n, s_k ≤ H. Numerically
     confirmed (0 violations, n = 2,3,4). Route via Σ s_k ≤ 2^n (a large shard is "large for its
     rank"). **The shard-count induction axis is now excluded (Section 3.5).** Still open.
  1''' (LB, k_C ≥ 1): pointwise claim fails; needs the FULL aggregate two-source charging
     (Σ B_{2m−1} ≥ Σ A_{2m}) using D(0+) ≤ 1 − 2k_C ≤ −1 and the budget c + k_C ≤ n. Open.
  2 (UB): **RETIRED / DEAD** — official n = 5 all-32-branches counterexample. Delegated to
     segment-subset-pigeonhole.
- **Spec concerns:** The two LB approaches on this framing (induction-peel, alternating-sum,
  interlacing) all share the (CB)/(PM)/(Wβ) wall, and this round's falsify-first excludes the
  shard-count axis too — the layer-cake framing's routes to (CB) are now largely exhausted. The
  independent segment-subset-pigeonhole framing (tree-extraction LB1) is the more promising LB
  route and should be prioritized; this file remains the certified-lemma anchor and LB fallback.
- **Numerics:** all exact `Fraction`, n ≤ 6, finished < 30 s, incremental print; used only to
  CHECK/falsify the invariance claim — every written step in Section 3.5 stands on its own.
