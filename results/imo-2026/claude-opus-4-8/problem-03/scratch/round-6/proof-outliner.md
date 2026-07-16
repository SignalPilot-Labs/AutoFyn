## imo-2026-03

Answer CONFIRMED: c(n) = 2^n/(2^{n+1}−1). Two fronts open: LOWER (Lemma LL t≥2 Sub-3b) and UPPER
(Regime B2 general n + Regime C). Field below: two rival LL routes to the same Sub-3b residual (distinct
primary invariants, healthy breadth), one upper-bound advance, plus the arithmetic-INC revise that
bypasses the false Structural Lemma. Certified imports free to all: greedy-odd-index, alt-sum-integral,
ll-t1-single-cut, shadow-regime-A, partial-shadow-B1, extremal-framework, ll-case1-high-interval,
dyadic-level-parity, forcing-inc-reduction, parity-piece-count.

---

ll-inclusion-gap: revise
Target: The full problem — c(n) = 2^n/(2^{n+1}−1), both bounds; this slug owns the LOWER bound via
  Lemma LL (t≥2, A(Q)>0), importing the certified upper-bound regime lemmas.
Technique: Inclusion split of the symmetric-difference target. Reduce LL to measure(S_Q△S_R)≥1
  (certified Lemma M), split on S_Q⊆S_R (INC) vs S_Q⊄S_R (GAP). REPLACE the FALSE Structural Lemma with
  a pure ARITHMETIC bound on A(Q); close GAP by dyadic alignment cost.
Skeleton:
  1. Reduce to measure(S_Q△S_R)≥1 — certified Lemma M / alt-sum-integral.
  2. Forcing Lemma: S_Q⊆S_R ⟹ max(Q)≤2^{n−1}; INC reduction A(Q∪R)=A(R)−A(Q) — certified
     forcing-inc-reduction.
  3. INC branch (S_Q⊆S_R): prove A(Q)≤A(G_{n−1})−1, hence A(Q∪R)=A(R)−A(Q)≥A(G_{n−1})−A(Q)≥1
     (using A(R)≥A(G_{n−1}) for R=G_{n−1}, and strengthened IH A(R)≥A(Q)+1 for refined R).
  4. GAP branch (S_Q⊄S_R): a Q-piece crossing a dyadic boundary of G_{n−1} produces a "bulge" in
     S_Q\S_R and a compensating "gap" in S_R\S_Q; their measures sum to ≥1 by the integral constraint
     ∫(N_Q−N_R)=1 restricted to the symdiff, using G_{n−1}'s alternating level structure.
Key lemmas (claim + mechanism):
  - INC arithmetic bound A(Q)≤A(G_{n−1})−1 (replaces false Structural Lemma) — because with ΣQ=2^n,
    the alternating sum gives (for the k parts) the smallest INC-allowed pieces bounded ABOVE by the
    forbidden-band exclusion (no Q-piece in an odd-N_G forbidden interior, so bottom pieces ≤1), while
    the Forcing Lemma bounds the TOP pieces (≤2^{n−1}); ΣQ=2^n=ΣG_{n−1}+1 ties them so the "+1 excess"
    forces q_min ≥ A(Q)/(#odd-indexed parts) yet q_min ≤ 1, giving A(Q)≤A(G_{n−1})−1. Verified n=3:
    3-part exact (q3≥A/2, q3≤1 ⟹ A≤2=A(G_2)−1); 4-part 0 violations of A(Q)≤2 on the 1/4-grid.
  - GAP alignment cost ≥1 — because on each dyadic level I_k of G_{n−1}, N_G is constant-parity; a
    Q-piece at value v∈I_k shifts the odd-region boundary, and ∫_{symdiff}(N_Q−N_R) collects exactly the
    +1 excess with |N_Q−N_R|=1 on the tight cases, so the two complementary pieces sum to ≥1. Tight
    n=3 witnesses Q={3/2,5/2,4}, Q={1/2,3/2,2,4} each give two ½-measure pieces summing to 1.
Open gaps: (G-INC-1) general-n/general-part-count arithmetic bound A(Q)≤A(G_{n−1})−1 [the substance —
  generalize the n=3 arithmetic]; (G-INC-2) refined-R strengthened IH A(R)≥A(Q)+1; (G-GAP) alignment
  cost ≥1 general n.
Cases to cover: INC vs GAP (exhaustive, disjoint). Within INC: R=G_{n−1} vs refined R. Within arithmetic:
  bottom pieces ≤1 vs even-multiplicity interior pieces (the case the false Structural Lemma missed).
Watch out for: do NOT reinstate the Structural Lemma (FALSE, counterexample Q={3/2,3/2,2,3}); the INC
  bound must be proved by arithmetic on piece values, not by "no piece in forbidden band". Even-
  multiplicity interior pieces are INC-legal and must be handled. The refined-R case (G-INC-2) genuinely
  needs A(R)≥A(Q)+1 as a strengthened IH, not just A(R)≥A(G_{n−1}).

---

ll-dyadic-symdiff: advance
Target: The full problem — both bounds; this slug owns the LOWER bound via LL by a max(Q)-split route.
Technique: Direct measure(S_Q△S_R)≥1 by casework on max(Q) vs 2^{n−1}, using the NEW verified identity
  and the certified dyadic-level parity lemma. Distinct primary invariant from ll-inclusion-gap (which
  splits on inclusion) — a genuine rival route to the same Sub-3b residual.
Skeleton:
  1. Cases 1, 2, Sub-3a — CLOSED, certified (ll-case1-high-interval, dyadic-level-parity, Lemma P).
  2. Sub-3b split A: max(Q) < 2^{n−1}. Show A(Q∪R) ≥ 2 (strict slack) — a shifted-level / Sub-3a-adjacent
     argument fires with a full-measure level contribution.
  3. Sub-3b split B: max(Q) = 2^{n−1} (the ONLY tight boundary). Apply the identity
     A(Q∪R) = 2^{n−1} − A(Q'∪R), Q' = Q∖{2^{n−1}} partitioning 2^{n−1}; reduce to A(Q'∪R) ≤ 2^{n−1}−1.
  4. Close step 3 by INC/GAP sub-split on Q'∪R (import ll-inclusion-gap's arithmetic INC bound and GAP
     alignment for the boundary), or directly since Q'∪R has one fewer top piece.
Key lemmas (claim + mechanism):
  - IDENTITY A(Q∪R) = 2^{n−1} − A(Q'∪R) when max(Q)=2^{n−1} — because on [0,2^{n−1}) the piece 2^{n−1}
    always exceeds x, so N_Q(x)=1+N_{Q'}(x), flipping parity: S_Q∩[0,2^{n−1}) = [0,2^{n−1})∖S_{Q'};
    hence measure(S_Q△S_R) = 2^{n−1} − measure(S_{Q'}△S_R). VERIFIED n=3, all 4 test partitions
    (this outliner re-ran: {4,3,1}, {4,5/2,3/2}, {4,7/2,1/2}, {4,2,2} all MATCH).
  - Slack bound for max(Q)<2^{n−1}: A(Q∪R)≥2 — because the tight value 1 is ONLY attained at
    max(Q)=2^{n−1} (verified n=3: max(Q)<4 ⟹ A≥2), so a strict-slack argument (a full dyadic level or
    a doubled partial-overlap contribution) is available where Sub-3a nearly fires.
Open gaps: step 2 (max(Q)<2^{n−1} ⟹ A≥2 general n — needs the shifted-level mechanism made rigorous);
  step 3→4 (A(Q'∪R)≤2^{n−1}−1: guard against circularity — Q'∪R is NOT a valid G_{n−1}-refinement, so
  close via the INC/GAP arithmetic on Q'∪R, not via a naive induction).
Cases to cover: max(Q)<2^{n−1} (slack) vs max(Q)=2^{n−1} (tight). Within tight: INC vs GAP.
Watch out for: the identity is "circular but structurally useful" — Q'∪R has sum 3·2^{n−1}−1, NOT a
  valid refinement, so do NOT attempt a clean induction on it; use it only to reduce the tight boundary
  to a bounded-A statement closed by the arithmetic/alignment mechanisms. Per-level bound
  (mismatch_k≥|∫_k|) and the ∫_symdiff identity are BOTH FALSE — do not retable.

---

geometric-selfsimilar: advance
Target: The full problem — c(n) = 2^n/(2^{n+1}−1), both bounds; this slug owns the UPPER bound via
  explicit XY strategy, importing LL for the lower bound.
Technique: Multilevel partial-shadow recursion on the residual (recurse on (n,m)) for Regime B2; a
  dominant-piece chopping strategy for Regime C. Spine: partial-shadow-B1 (certified) applied iteratively.
Skeleton:
  1. Regimes A (1/2≤A_1≤c(n)) and B1 (1−c(n)≤A_1<1/2) — CLOSED, certified (shadow-regime-A,
     partial-shadow-B1).
  2. Regime B2 (A_1<1−c(n)): apply partial-shadow level-1 (k_1−1 cuts) → residual R'_1 with largest
     piece A_{k_1+1}, Σ(R'_1)=1−2(A_2+…+A_{k_1}). If B1 fires on R'_1, one more cut closes; else recurse.
  3. Termination: each level drops m by ≥1 and n by ≥1; terminal m=1 (halve once, A=0) or n=1 (trivial).
  4. Regime C (A_1>c(n)>1/2): 2-stage — chop A_1 to pair off A_2,…,A_m, then reduce the residual;
     the shadow alone gives val=A_1>c(n) so C needs the residual reduction (genuinely open).
Key lemmas (claim + mechanism):
  - B2 recursion terminates in ≤n cuts with A(final)≤1/D — because each partial-shadow level carves the
    largest piece into copies of the next pieces (parity-invisible pairs) leaving a residual whose
    largest-piece ratio stays in B/B1; the effective residual after r depth-2 levels is
    {d_1,…,d_r,A_{2r+1},…} with d_i=A_{2i−1}−A_{2i}, and the B2 condition A_1<(2^n−1)/D bounds the final
    single piece ≤1/D. Verified n=3: all denom-15 4-piece B2 configs achieve minimax val≤8/15 (10 tight).
  - Regime C dominant-chop — because A_1>c(n)>1/2 leaves 1−A_1<1−c(n) of mass in small pieces; XY spends
    cuts inside A_1 to pair EACH small piece and then binary-splits the leftover; the tight C witness
    {9/15,3/15,2/15,1/15} needs the exact cut set {1/15,3/15,6/15} inside A_1 — the strategy must be
    pinned to hit ≤1/D.
Open gaps: B2 general-n termination + the "final residual piece ≤1/D" algebraic bound (the KEY FORMULA);
  Regime C general n (the residual-reduction after pairing — shadow alone fails, needs a genuinely new
  chopping/halving analysis). B fully closed at n=2 already.
Cases to cover: B2 (recurse) vs C (dominant-chop). Within B2: B1 fires on residual vs recurse again;
  terminal m=1 vs n=1. Regime boundary A_1=1−c(n), A_1=c(n).
Watch out for: single-level PS+B1 for k=2 is a recorded dead-end (A_full=2A_1+2A_4−1 exceeds 1/D on ~22%
  of B2 configs) — must be the MULTILEVEL recursion. Binary-halving A_1 for C is a dead-end
  (A_full=A({A_2,…}) unbounded by 1/D). Shadow strategy for C gives val=A_1>c(n) — FAILS, do not table.
  c(n)>1/2 for all n, so C ⟹ A_1>1/2 (use this).

---

Field summary: 4 approaches. Lower-bound front gets TWO distinct rival routes to Sub-3b
(ll-inclusion-gap: inclusion split + arithmetic INC + GAP alignment; ll-dyadic-symdiff: max(Q) split +
identity + slack) so a single wrong sub-target cannot sink both. Upper-bound front advances
geometric-selfsimilar (B2 recursion + C). alternating-sum-value and extremal-smoothing stay live but are
not nominated this round (last-placed; their gaps are strict subsets of the above). Recommended build set:
ll-inclusion-gap (revise — highest-value, closest to closing the lower bound via arithmetic INC),
ll-dyadic-symdiff (advance — rival route/insurance), geometric-selfsimilar (advance — upper-bound front).
