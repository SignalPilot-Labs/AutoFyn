## imo-2026-03

Answer (CONFIRMED, do not re-derive): c(n) = 2^n/(2^{n+1}−1). Work unnormalized: pieces are integers,
G_n = {1,2,…,2^n}, D = 2^{n+1}−1, target val ≥ 2^n (lower) and ≤ 2^n (upper). With sorted final pieces
p_1≥…≥p_k, Lemma G (certified) gives LB = val = Σ_odd = (T+A)/2, A = p_1−p_2+p_3−… the alternating sum,
and A(P) = measure{x: N(x) odd} (Lemma M0, certified). So the whole problem is A ≥ 1 (lower) / A ≤ 1
(upper) at the geometric config / for all configs. Certified merge lemma: A(X∪Y) = A(X)+A(Y)−2B,
B = measure{x: N_X(x) odd AND N_Y(x) odd} ≥ 0.

Field this round: three revisions of the live population, each a WHOLE rival attempt, with genuinely
distinct upper-bound routes (explicit shadow strategy / potential-decrease strategy / no-strategy
extremal). All three share the lower-bound crux Lemma LL, but attack its open t≥2 tail by different
mechanisms. The t=1 tail of LL is now CLOSED (new, validated) and must be written into whichever
approaches carry the lower bound.

---

geometric-selfsimilar: revise
Target: c(n) = 2^n/(2^{n+1}−1), both bounds, whole claim.
Technique: geometric config + self-similar induction on n for the lower bound (LL); corrected explicit
  XY strategy (shadow + regime casework) for the upper bound, REPLACING the disproven "all cuts on A_1".
Skeleton:
  1. Reduction to val = Σ_odd = (T+A)/2 — Lemma G (certified, import).
  2. Measure form + merge lemma — Lemma M0, Lemma M (certified, import).
  3. Lower bound base n=1 and Case 1 (t=0, largest piece uncut) — already complete (import).
  4. Lower bound Case 2, Lemma LL, sub-case A(Q)=0 — merge lemma closes it (val(Q∪R) ≥ 2^{n−1}+Σ_even(Q)
     = 2^n). Already complete.
  5. **Lower bound Case 2, Lemma LL, sub-case A(Q)>0, t=1 (single cut of 2^n): NOW CLOSED.** Write the
     new proof (validated this round): Q={q, 2^n−q}, q≤2^{n−1}, so the Q-odd region is the single
     interval (q, 2^n−q) and A(Q)=2^n−2q. Since S_R ⊆ [0, max(R)] with max(R) ≤ 2^{n−1} (R refines
     G_{n−1}), B = measure{S_Q ∩ S_R} ≤ max(0, max(R)−q). Two cases: (i) max(R) ≤ q ⇒ B=0 ⇒
     A(Q∪R) ≥ A(Q)+A(R) ≥ A(R) ≥ 1 (as A(Q)=2^n−2q ≥ 0); (ii) max(R) > q ⇒ B ≤ max(R)−q ⇒
     A(Q∪R) ≥ (2^n−2q)+A(R)−2(max(R)−q) = 2^n−2max(R)+A(R) ≥ 2^n−2·2^{n−1}+A(R) = A(R) ≥ 1. ∎
  6. Lower bound Case 2, t≥2: OPEN (see gaps). Present the two settled sub-chunks: (a) disjoint-region
     B=0 chunk — when the Q-odd region lies entirely above max(R) (N_Q(x) even for all x ≤ max(R)),
     B=0 and A(Q∪R) ≥ A(Q)+A(R) ≥ 1; (b) Q-odd ⊇ R-odd chunk — when S_R ⊆ S_Q, B = A(R) and
     A(Q∪R) = A(Q)−A(R), which is ≥ 1 exactly when A(Q) ≥ A(R)+1 (this is the tight case
     Q={3,3,2}, R={2,2,2,1} for n=3). The residual middle is the gap.
  7. Upper bound, corrected. Sort LB pieces A_1≥…≥A_m (m ≤ n+1, Σ=1). Regime split on A_1:
     - **Regime A (1/2 ≤ A_1 ≤ c(n)): shadow strategy.** XY uses m−1 ≤ n cuts to carve A_1 into the
       m−1 pieces {A_2,…,A_m, r} with r = A_1−(A_2+…+A_m) = 2A_1−1 ≥ 0. Now every A_i (i≥2) is paired
       with an equal copy, the equal adjacent pairs cancel (even-run collapse, A-bound corollary), and
       the sorted odd-picks give val = A_1 ≤ c(n). ∎ this regime.
     - **Regime B (A_1 < 1/2, "flat"): val ≤ 1/2 < c(n).** No piece reaches 1/2; XY pairs pieces into
       near-equal halves so A → small, val → 1/2. Since c(n) > 1/2 always (2^{n+1} > 2^{n+1}−1), the
       bound 1/2 suffices. Needs a clean pairing/A-decrease argument (sub-gap, but only needs the loose
       1/2, not tightness).
     - **Regime C (A_1 > c(n), "dominant"): OPEN.** Non-A_1 pieces sum to 1−A_1 < 1−c(n) = (2^n−1)/D.
       Shadow overshoots (gives A_1 > c(n)); equal n-split only reaches A_1 ≤ (n+1)/D < c(n). Proposed
       mechanism: recursive reduction — XY's first cut splits A_1 into (1−A_1, 2A_1−1); the piece
       (1−A_1) equals A_2+…+A_m so it caps the sorted top, and the remaining n−1 cuts recurse on a
       scaled sub-instance (apply the (n−1) upper bound). Make the scaling/IH rigorous.
Key lemmas (claim + mechanism):
  - LL t=1 (CLOSED) — because the single-cut Q-odd region is one interval (q,2^n−q) whose overlap with
    the R-odd region is bounded by max(R)−q ≤ 2^{n−1}−q, exactly cancelling A(Q)=2^n−2q down to A(R)≥1.
  - Shadow strategy val = A_1 — because carving A_1 into copies of the other pieces plus residual r
    makes every non-A_1 piece an equal pair that cancels in the alternating sum, leaving LB exactly A_1.
  - A(R) ≥ 1 (the IH content) — because val(R) ≥ 2^{n−1} and T(R)=2^n−1 give A(R)=2val(R)−T(R) ≥ 1.
Open gaps:
  - LL t≥2, A(Q)>0, residual middle (step 6): neither B ≤ A(R) nor B ≤ A(Q)−A_Q^high alone reaches 1
    on ~12% of configs (validated numerically this round); needs a sharper joint Q–R bound. This is the
    load-bearing lower-bound gap.
  - Upper bound Regime B (clean 1/2 pairing bound) and Regime C (recursive reduction for A_1 > c(n)).
Cases to cover: LL: A(Q)=0 [done], A(Q)>0 t=1 [done], A(Q)>0 t≥2 [gap]. Upper: A_1∈[1/2,c(n)] [done],
  A_1<1/2 [sub-gap, loose], A_1>c(n) [gap].
Watch out for: NEVER re-state "XY concentrates all n cuts on A_1" — disproven by (0.4,0.4,0.2) at n=2
  (val 0.608 > 4/7). max(R) ≤ 2^{n−1} is the load-bearing fact in the t=1 proof — it holds because R
  refines G_{n−1} whose pieces are all ≤ 2^{n−1} and cuts only shrink. In Regime A, needs A_1 ≥ 1/2 for
  r ≥ 0; the A_1 < 1/2 case is Regime B, not Regime A.

---

alternating-sum-value: revise
Target: c(n) = 2^n/(2^{n+1}−1), both bounds, whole claim.
Technique: same reduction via A = measure{N odd} (the integral rep is this approach's distinctive tool);
  LL via a DIFFERENT mechanism (parity-of-piece-count + strengthened IH), upper bound via a DIFFERENT
  mechanism (potential-decrease greedy XY strategy). Kept genuinely rival to geometric-selfsimilar so a
  failure of one LL/upper mechanism does not sink both.
Skeleton:
  1. Reduction, integral rep, A-bounds, removal identity — all certified/proven (import).
  2. Lower bound Case 1 — complete (import).
  3. Lower bound Case 2, LL: import the t=1 closed proof (step 5 above). For t≥2 attack via the
     **parity-of-piece-count route** (distinct from geometric-selfsimilar's B-casework): total pieces
     k = (n+1) + (#cuts). When XY uses all n cuts and the smallest G_n piece 1 stays uncut, k = 2n+1 is
     odd and A(P) = Σ_{i=1}^{n}(p_{2i−1}−p_{2i}) + p_{2n+1} ≥ p_{2n+1} = min-piece. Sub-case min ≥ 1 ⇒
     A ≥ 1 immediately. Residual sub-cases (min < 1, i.e. XY cut some 2^j past its "1"-boundary; or
     k even, XY used < n cuts — but then some large piece survives uncut, pushing toward Case 1): close
     by strengthening the IH to control the low part of S_R.
  4. Upper bound via **potential-decrease strategy** (Opening 4, distinct from shadow): A = ∫𝟙[N odd].
     One cut of ℓ into (a, ℓ−a), s = smaller part, flips parity of N on [0,s)∪[ℓ−s,ℓ) (certified).
     XY greedy rule: each cut maximizes ΔA = (measure newly made even) − (measure newly made odd).
     Claim: n greedy cuts drive A ≤ 1 for every LB config, tight only at the geometric config (where the
     replica halving flips each piece into an equal pair). Verify the greedy sign against a few configs
     (bounded), then prove the per-cut decrease bound.
Key lemmas (claim + mechanism):
  - Parity identity: k=2n+1 (all cuts used, "1" uncut) ⇒ A = Σ n non-negative pairs + min-piece —
    because sorting makes each (p_{2i−1}−p_{2i}) ≥ 0 and the odd count leaves a trailing +min.
  - Potential decrease: one cut changes A by at most 2s (s = smaller subpiece) and XY can always pick a
    cut with ΔA making N even on the largest current odd-parity interval — because the parity-flip set
    [0,s)∪[ℓ−s,ℓ) can be aimed at an odd-parity region.
Open gaps:
  - LL t≥2 residual (min < 1 sub-case): needs strengthened IH bounding |S_R ∩ [0,y)| — same difficulty
    class as geometric-selfsimilar's gap, different handle.
  - Upper bound: proving greedy A-decrease reaches ≤ 1 in n cuts for ALL configs (the tight = geometric
    equality must come out exactly). This is the whole bet of the potential route.
Cases to cover: LL: t=1 [done], t≥2 k odd min≥1 [done via parity], t≥2 residual [gap]. Upper: greedy
  covers all configs [gap], geometric equality [tight check].
Watch out for: the parity identity gives only A ≥ min, which can be < 1 — do NOT overclaim it closes
  LL alone. The greedy potential must be shown to never get stuck above A=1 with cuts remaining; the
  {2/3,2/3,2/3} type 3-way even split (which drops A below 1) uses MORE cuts than budget — the ≤ n
  constraint is essential and must be used.

---

extremal-smoothing: revise (flesh out — primary upper-bound bet, BYPASSES per-config XY strategy)
Target: c(n) = 2^n/(2^{n+1}−1), both bounds, whole claim.
Technique: extremal/smoothing. Define V(A) = min over XY responses (≤ n cuts) of val. Prove the
  geometric config is the maximizer, so max_A V(A) = V(geom) = c(n) — the upper bound falls out with NO
  explicit XY strategy for arbitrary configs (this is the whole point, given "all cuts on A_1" is dead).
Skeleton:
  1. V(geom) = c(n). Lower part (V ≥ c(n)) = the geometric lower-bound induction = LL (import from
     whichever approach certifies it; the SAME shared lower-bound crux). Upper part (V ≤ c(n)) = ONE
     explicit replica response against the SINGLE geometric config (halve each 2^i into 2^{i−1},2^{i−1};
     equal pairs cancel; A = 1). Cheap — one config, one response. — GAP S0 = LL only.
  2. Smoothing lemma S1 (core bet): any LB config not in ratio-2 has an adjacent pair A_i/A_{i+1} ≠ 2;
     the LB mark between them can be shifted toward the ratio-2 profile with V weakly increasing.
     Mechanism: on the region where the sort order and XY's optimal-response type are fixed, val is
     LINEAR in the LB piece lengths, so V = min of linear functions is CONCAVE there; the geometric
     profile is a stationary point of this local concave V (first-order/KKT), and concavity upgrades
     stationary → local max; the exchange argument (moving mass toward ratio-2 reduces XY's pairwise
     cancellation, raising LB's odd-sum) rules out any competing local max above c(n).
  3. Compactness / USC: LB configs form a compact simplex; V is upper semicontinuous (min of continuous
     payoffs over XY's compact response set), so max_A V is attained (Weierstrass); by S1 it is at the
     geometric config.
  4. Conclude max_A V(A) = c(n): LB guarantees c(n) (from geom) and cannot exceed it (geom is the max).
Key lemmas (claim + mechanism):
  - Local concavity of V — because within a fixed sort-order + fixed XY-response-type cell, val is a
    linear function of the LB piece lengths, and a min of linear functions is concave.
  - Smoothing/exchange S1 — because making the LB spectrum "more geometric" (adjacent ratio → 2)
    strictly reduces XY's ability to pair-cancel LB's odd picks, so V does not decrease along the
    toward-geometric perturbation; geometric is the unique interior stationary point matching V = c(n).
Open gaps:
  - GAP S0 = LL (shared; import once certified).
  - GAP S1 = the smoothing monotonicity lemma. Load-bearing. Reduce to: (i) local concavity in each
    cell [tractable — linearity of val], (ii) stationarity of geom [first-order condition], (iii) no
    competing local max [exchange argument]. Verify the perturbation sign on 2–3 explicit non-geometric
    spectra (bounded computation) before committing.
Cases to cover (S1 perturbations): too-flat pair (A_{i+1} < 2A_i), too-steep pair (A_{i+1} > 2A_i),
  boundary configs (< n marks, equal pieces, single dominant piece).
Watch out for: min of PIECEWISE-linear (sort order changing) is not globally concave — concavity is only
  cell-local; the global step needs the exchange argument + USC, not naive calculus. Do NOT over-claim
  UNIQUE maximizer (a coarse grid found {1/14,3/14} also hitting 4/7 at n=2); the argument needs only
  that the MAX VALUE is c(n). State XY uses ≤ n cuts (not exactly n) in the V(geom) ≤ side.

---

Nomination for build set: all three (geometric-selfsimilar, alternating-sum-value, extremal-smoothing)
— each carries real new progress (LL t=1 closed everywhere; corrected upper bound in
geometric-selfsimilar; distinct potential upper bound in alternating-sum-value; the S1 bypass in
extremal-smoothing). The shared LL t≥2 gap is attacked by two distinct mechanisms so the field does not
collapse to one line. If LL t≥2 stays unchanged after this round, it becomes the flagged shared-gap
plateau for a dedicated bypass next round.
