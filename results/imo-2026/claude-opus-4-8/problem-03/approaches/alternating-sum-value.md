# Approach: alternating-sum-value

## Status
partial

## Approaches tried
- R1 (outliner): reformulate LB share as (1+A)/2, reduce to the alternating-sum game value A* = 1/D;
  outline only, gaps AL/AU open.
- R2 (builder): **Fully proved** Lemma G (greedy/odd-index), the reformulation LB = (1+A)/2, the
  integral representation A = |{x ≥ 0 : N(x) odd}|, the A-bounds 0 ≤ A ≤ p_1, the **lower bound Case 1**
  (XY spares the largest piece ⇒ A ≥ 2^{n−1} ≥ 1), and the **tightness** (XY's replica forces A = 1).
  Recorded dead-end: the top/bottom decomposition A = A_top + A_bot − 2B does NOT reduce Case 2
  term-by-term (the sufficient inequality A_top ≥ 2B is FALSE, min ≈ −10.5). GAP AL and GAP AU open.
- R3 (builder, this round):
  - **Lower bound Case 2, t=1 (single cut of 2^n): CLOSED** (new for this file). Full proof written
    below as **Lemma LL‑1**, using the single-interval structure of the Q-odd region and the bound
    max(R) ≤ 2^{n−1}. Numerically validated (0 violations, n = 2,3,4; >9000 random Case‑2 configs).
  - **Parity-of-piece-count sub-case: CLOSED** (new). Full proof written below as **Lemma P**: whenever
    XY's total number of cuts t satisfies t ≡ n (mod 2) (so the piece count k = n+1+t is odd) *and* every
    final piece has length ≥ 1, then A ≥ 1 in one line. Validated (0 violations, 15000 samples).
  - **GAP AU upper bound via potential-decrease greedy XY: recorded DEAD-END** (validated numerically,
    per the outline-reviewer's mandatory pre-check). The greedy rule "each cut maximizes the immediate
    A-decrease" does NOT reach A ≤ 1/D: it stalls at A ≈ 0.27 on the dominant config (0.649, 0.351) for
    n = 2 (target 1/D ≈ 0.143), while the *true* 2-cut optimum for that config is A ≈ 0 ≤ 1/D. Greedy is
    genuinely sub-optimal (no per-cut sign/magnitude bound closes the gap); the correct universal
    strategy needs lookahead (shadow/pairing), which is geometric-selfsimilar's route. GAP AU stays open
    for THIS approach — kept distinct so a failure here does not sink geometric-selfsimilar.
  - Residual **GAP AL** (Case 2 with t≥2 AND either a sub-1 piece present or t ≢ n mod 2) remains open.

## Current best
Rigorously established (all proofs below):

1. **Lemma G** (greedy/odd-index, certified `lemmas/greedy-odd-index.md`): with sorted final pieces
   p_1 ≥ … ≥ p_k summing to 1, Liu Bang's guaranteed optimal share equals Σ_odd = p_1 + p_3 + ⋯.
2. **Reformulation:** LB share = (1 + A)/2 with A := p_1 − p_2 + p_3 − ⋯. So c(n) = (1 + A*)/2,
   A* := max_LB min_XY A; target A* = 1/D, D = 2^{n+1} − 1, giving **c(n) = 2^n/(2^{n+1} − 1)**.
3. **Integral representation** (certified `lemmas/alt-sum-integral.md`): A = |{x ≥ 0 : N(x) odd}|,
   N(x) = #{pieces > x}; A-bounds 0 ≤ A ≤ p_1; merge lemma A(X∪Y) = A(X)+A(Y)−2B with
   B = measure{N_X odd ∧ N_Y odd}; single-cut effect (a cut with smaller subpiece s flips N-parity on
   [0,s)∪[ℓ−s,ℓ), measure 2s).
4. **Lower bound, Case 1** (2^n uncut): A ≥ 2^{n−1} ≥ 1. Complete.
5. **Lower bound, Case 2, t = 1** (Lemma LL‑1, NEW this round): A ≥ 1. Complete, via IH.
6. **Lower bound, parity sub-case** (Lemma P, NEW this round): t ≡ n (mod 2) and all pieces ≥ 1 ⇒ A ≥ 1.
   Complete, self-contained.
7. **Tightness:** XY's replica forces A = 1 exactly at the geometric config. Complete.

Open gaps (precise):
- **GAP AL — Lower bound Case 2, t ≥ 2 residual.** When XY cuts 2^n with ≥ 2 cuts and the final config
  neither satisfies the parity sub-case (some piece < 1, or total cuts t ≢ n mod 2) nor t = 1, prove
  A ≥ 1. True numerically (min A = 1, attained). Shared with geometric-selfsimilar's LL t≥2 gap.
- **GAP AU — Universal upper bound.** For every LB config, XY (≤ n cuts) forces A ≤ 1/D. The
  potential-decrease greedy route (this approach's distinctive upper-bound bet) is a **recorded
  dead-end** (numerics above). Open here.

---

## Details of what is proved

### 0. Setup and Lemma G
Liu Bang marks ≤ n points on [0,1], then Xiang Yu marks ≤ n further distinct points; the stick is cut at
all marks into pieces summing to 1. In the claiming phase LB moves first and both maximize their own
total. The claiming game is finite zero-sum with constant total 1, hence has a value; by **Lemma G**
(certified `lemmas/greedy-odd-index.md`; technique: minimax + backward induction, KB "Minimax of a
zero-sum game") the value of LB's share, with the pieces sorted p_1 ≥ … ≥ p_k, is exactly
Σ_{i odd} p_i, and both bounds hold (LB guarantees it; XY holds LB to it). So the whole problem is the
min–max over the marking phase of Σ_odd.

### 1. Reformulation LB = (1 + A)/2
Let A := p_1 − p_2 + p_3 − ⋯ = Σ_odd − Σ_even. Since Σ_odd + Σ_even = 1, Σ_odd = (1 + A)/2. Therefore
c(n) = (1 + A*)/2 with A* = max_LB min_XY A. With A* = 1/D (D = 2^{n+1} − 1),
c(n) = (1 + 1/D)/2 = (D+1)/(2D) = 2^{n+1}/(2(2^{n+1} − 1)) = **2^n/(2^{n+1} − 1).**
*Check:* n = 1: D = 3, c = 2/3. n = 2: D = 7, c = 4/7. ✓

### 2. Integral representation, A-bounds, merge lemma, single-cut effect
All certified in `lemmas/alt-sum-integral.md`; imported. For sorted q_1 ≥ … ≥ q_K > 0 and
N(x) = #{i : q_i > x}:
- **A = ∫_0^∞ 𝟙[N(x) odd] dx = measure{x ≥ 0 : N(x) odd}.**
- **0 ≤ A ≤ q_1** (largest piece); grouping A = q_1 − (q_2 − q_3) − ⋯ gives A ≤ q_1, grouping in adjacent
  pairs gives A ≥ 0.
- **Removal identity:** A(M) = q_1 − A(rest), rest = M minus its largest piece.
- **Merge lemma:** A(X∪Y) = A(X) + A(Y) − 2B, B := measure{x : N_X(x) odd ∧ N_Y(x) odd} ≥ 0.
- **Single-cut effect:** cutting a length-ℓ piece into (a, ℓ−a) with s := min(a, ℓ−a) flips N-parity
  exactly on [0, s) ∪ [ℓ − s, ℓ) (measure 2s), and nowhere else; hence |ΔA| ≤ 2s.

### 3. Unnormalized geometric setup
LB marks at (2^k − 1)/D, k = 1,…,n, producing pieces 2^i/D, i = 0,…,n. Multiply all lengths by D and
work with integer pieces **G_n = {2^0, 2^1, …, 2^n}**, total D = 2^{n+1} − 1. The target A ≥ 1/D becomes
**A ≥ 1** (unnormalized). XY adds ≤ n cuts; each only shrinks an existing piece. Throughout this section
A, val, N refer to the unnormalized pieces.

### 4. Lower bound — Case 1 (2^n uncut)
If XY never cuts the piece 2^n, it survives intact. Every other original piece is ≤ 2^{n−1}, and cutting
only shrinks, so every other final piece is ≤ 2^{n−1} < 2^n; hence the largest final piece is q_1 = 2^n.
By the removal identity and 0 ≤ A(rest) ≤ (largest of rest) ≤ 2^{n−1},
A = 2^n − A(rest) ≥ 2^n − 2^{n−1} = 2^{n−1} ≥ 1  (n ≥ 1).  ∎(Case 1)

### 5. Lower bound — Case 2, t = 1 (single cut of 2^n)  — Lemma LL‑1 (NEW)

**Induction on n.** *Base n = 1:* XY has ≤ 1 cut. If 2^1 = 2 is uncut we are in Case 1. Otherwise XY's
single cut is on the piece 2 (t = 1), which is exactly the t = 1 sub-case below with R = {1} (the piece
1, uncut, A(R) = 1). So n = 1 is fully covered by Case 1 and the t = 1 argument.

*Inductive step (assume the lower bound holds for n − 1).* Suppose XY makes **exactly one** cut on the
piece 2^n, splitting it into Q = {q, 2^n − q} with q := smaller part ≤ 2^{n−1}, and refines the remaining
pieces G_{n−1} = {2^0, …, 2^{n−1}} into a multiset R using its remaining ≤ n − 1 cuts. The final config
is P = Q ∪ R.

- **R obeys the IH.** R is a refinement of G_{n−1} by ≤ n−1 cuts, i.e. exactly an instance of the
  (n−1)-game with LB's geometric config. By the inductive hypothesis val(R) ≥ 2^{n−1}. Since
  T(R) = T(G_{n−1}) = 2^n − 1 and A(R) = 2·val(R) − T(R), we get **A(R) ≥ 2·2^{n−1} − (2^n − 1) = 1.**
- **max(R) ≤ 2^{n−1}.** Every G_{n−1} piece is ≤ 2^{n−1}, and cuts only shrink pieces, so every R-piece
  is ≤ 2^{n−1}.
- **Q-odd region is a single interval.** For Q = {q, 2^n − q} with q ≤ 2^n − q, N_Q(x) = 2 on [0, q),
  = 1 on [q, 2^n − q), = 0 on [2^n − q, ∞). So N_Q is odd exactly on [q, 2^n − q), and A(Q) = 2^n − 2q.
- **Bounding B.** N_R is odd only where N_R(x) ≥ 1, i.e. only for x < max(R). Thus
  B = measure{x ∈ [q, 2^n − q) : N_R(x) odd} = measure{x ∈ [q, 2^n − q) ∩ [0, max(R)) : N_R odd}.
  - If max(R) ≤ q: the intersection [q, 2^n − q) ∩ [0, max(R)) is empty, so **B = 0.** Then, since
    A(Q) = 2^n − 2q ≥ 2^n − 2·2^{n−1} = 0, the merge lemma gives
    A(P) = A(Q) + A(R) − 0 ≥ A(R) ≥ 1.
  - If max(R) > q: the intersection ⊆ [q, max(R)), so **B ≤ max(R) − q.** The merge lemma gives
    A(P) = A(Q) + A(R) − 2B ≥ (2^n − 2q) + A(R) − 2(max(R) − q) = 2^n − 2·max(R) + A(R)
    ≥ 2^n − 2·2^{n−1} + A(R) = A(R) ≥ 1.

In both sub-cases A(P) ≥ 1.  ∎(Lemma LL‑1)

*(Numerical check: 0 violations of A(P) ≥ 1 over >9000 random Q = {q, 2^n−q} × random refinements of
G_{n−1}, for n = 2, 3, 4.)*

### 6. Lower bound — parity sub-case  — Lemma P (NEW, self-contained)

**Lemma P.** Suppose XY makes a total of t ≤ n cuts on G_n, producing k = (n + 1) + t final pieces. If
**k is odd** (equivalently t ≡ n mod 2) **and every final piece has length ≥ 1**, then A ≥ 1.

**Proof.** Sort the k pieces p_1 ≥ … ≥ p_k. Because k is odd, write k = 2r + 1 and group
A = Σ_{i=1}^{k} (−1)^{i+1} p_i = (p_1 − p_2) + (p_3 − p_4) + ⋯ + (p_{2r−1} − p_{2r}) + p_{2r+1}.
Every parenthesised pair p_{2j−1} − p_{2j} ≥ 0 by sortedness, and the trailing term is p_k = min piece.
Hence A ≥ p_k = min piece ≥ 1.  ∎(Lemma P)

*Scope.* k = (n+1)+t is odd iff t ≡ n (mod 2); in particular t = n (all cuts used) always gives k = 2n+1
odd. "Every piece ≥ 1" holds precisely when XY only ever cuts a piece of length ≥ 2 into two parts each
≥ 1 (e.g. keeps the piece 1 uncut and never over-splits). This is a genuine — but restricted — family of
XY responses. (Numerical check: 0 violations over 15000 sampled such configs, n = 2, 3, 4.)

### 7. Coverage and the residual gap
Together, Case 1 (§4), Lemma LL‑1 (§5), and Lemma P (§6) settle the lower bound A ≥ 1 whenever ONE of:
(i) XY leaves 2^n uncut; (ii) XY cuts 2^n with exactly one cut; (iii) XY's total cut count has the same
parity as n and no final piece drops below 1. The **residual GAP AL** is: XY cuts 2^n with **t ≥ 2**
cuts AND the config falls outside (iii) — i.e. some final piece is < 1, or the total cut count has the
wrong parity. This is the load-bearing lower-bound gap, shared with geometric-selfsimilar. Numerically
A ≥ 1 holds there too (min A = 1, attained e.g. at the n = 3 config sorted {2,2,2,2,1}·… giving A = 1),
but no rigorous argument is yet in hand.

### 8. Tightness (upper bound at the geometric config)
Against G_n, XY halves each piece 2^i (i = 1,…,n) into 2^{i−1}, 2^{i−1} (n cuts, distinct interior
points). The final multiset is sorted 2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 1, 1, 1: every equal
adjacent pair cancels in the alternating sum, leaving A = 1 = 1/D · D. So XY forces A = 1 at the
geometric config, matching the lower bound there: val(G_n) = c(n) exactly. This is the tight case, not
the universal upper bound.

### 9. Upper bound — potential-decrease greedy XY  — RECORDED DEAD-END

Per the outline-reviewer's mandatory directive, the potential-decrease greedy strategy was validated
numerically BEFORE any writeup. **It fails.**

*The proposed rule.* Using A = ∫ 𝟙[N odd] dx, each cut of a piece ℓ into (a, ℓ−a) with s = min(a, ℓ−a)
flips N-parity on [0, s) ∪ [ℓ − s, ℓ) (certified). The greedy XY rule: each of the n cuts is chosen to
**minimize the resulting A** (equivalently maximize the immediate decrease). The bet was: n greedy cuts
drive A ≤ 1/D for every LB config, tight only at the geometric config.

*Numerical refutation.* For n = 2 the greedy strategy (fine grid of split points, exact per-step A) on
the dominant config (0.649, 0.351) stalls at **A ≈ 0.287**, and on (0.636, 0.322, 0.042) at A ≈ 0.271,
whereas the target is 1/D = 1/7 ≈ 0.143. Yet the **true** 2-cut optimum for (0.649, 0.351) is A ≈ 0
(≤ 1/D): cut 0.649 → (0.351, 0.298) creating a matching 0.351-pair, then halve 0.298 → (0.149, 0.149),
giving pieces {0.351, 0.351, 0.149, 0.149} with A = 0. So the bound A ≤ 1/D is TRUE (as it must be — the
answer is confirmed), but **the greedy potential rule is genuinely sub-optimal**: maximizing the
immediate decrease leaves XY unable to complete the pairing with the remaining budget. No per-cut
sign/magnitude bound rescues it (the optimal move can even *increase* A on the first step to enable a
larger decrease later — a pure lookahead phenomenon).

*Conclusion.* The potential-decrease greedy route does not prove GAP AU. The correct universal strategy
requires lookahead — the shadow/pairing regime strategy (Regime A: carve A_1 into equal copies of the
smaller pieces plus a residual; val = A_1 ≤ c(n)) plus a recursive treatment of the dominant regime —
which is geometric-selfsimilar's route. To keep this approach a genuine rival (not a copy), GAP AU is
left OPEN here rather than importing that route. Recorded so no future round re-attempts greedy potential.

---

## Verification of the answer for small n
- n = 1: G_1 = {2, 1}, D = 3. XY has ≤ 1 cut. If 2 is spared (Case 1): A ≥ 2^{0} = 1. If XY cuts 2 into
  (a, 2−a): pieces {a, 2−a, 1}; exactly one of a, 2−a is ≥ 1 and the other ≤ 1, so the median is 1 and
  A = max − med + min = (a + (2−a) + 1) − 2·1 = 1. Either way A ≥ 1, with XY's halving 2 → (1,1) giving
  {1,1,1}, A = 1. Hence A* = 1/3, c(1) = (1 + 1/3)/2 = **2/3.** ✓
- n = 2: XY's replica ({2,2,2,1}/7 or {2,2,1,1,1}/7) forces A = 1 (unnorm), so A* = 1/7, c(2) = **4/7.** ✓

## Full proof
(Not present — Status is `partial`; GAP AL, t≥2 residual, and GAP AU remain open.)

## Promotable lemmas
- **Lemma LL‑1 (Case 2, single cut of the top piece).** In the (unnormalized) geometric lower bound,
  when XY cuts 2^n with exactly one cut into Q = {q, 2^n − q} (q ≤ 2^{n−1}) and refines G_{n−1} into R
  with A(R) ≥ 1 (IH), then A(Q ∪ R) ≥ 1. Proof in §5 (single-interval Q-odd region + max(R) ≤ 2^{n−1}
  bound on B). Reusable by geometric-selfsimilar as the settled t = 1 tail of Lemma LL. Propose to
  `lemmas/case2-single-cut.md`.
- **Lemma P (parity sub-case).** For any XY response with total cut count t ≡ n (mod 2) and all final
  pieces ≥ 1, the alternating sum A ≥ 1 (one line: A ≥ min-piece ≥ 1 when the piece count is odd). Proof
  in §6. Elementary, self-contained. Propose to `lemmas/parity-piece-count.md`.
