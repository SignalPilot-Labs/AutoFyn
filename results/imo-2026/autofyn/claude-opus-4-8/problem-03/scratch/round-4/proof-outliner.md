# Proof-outliner field — round 4 — imo-2026-03

Answer c(n) = 2^n/D, D = 2^{n+1}−1. Certified/imported free: G1 (greedy = odd-ranked), R
(O = 1/2 + ½·μ{N odd}; target O ≤ c(n) ⟺ A := μ{N odd} = 2O−1 ≤ 1/D), H (halve p−1 largest ⟹
O = 1/2 + a_p/2, closes upper-bound Case A), fragment-count bound, interleaving value = 2^n,
Lemma S, top-fragment cascade (G-L1 case a=1). Live population: direct-constructive (elo 1558,
CHANGES REQUESTED) is the ONLY live approach; induction-recursion (dead), potential-duality
(parked/vacuous). Remaining gaps: **U1 = Case B** upper bound (3rd round on this wall), **L1**
lower bound case a=0, **L2** confine-to-R_n.

Design note (gate-validated this round): I re-ran the Case-B strategy search. **The upper-bound
Case B is a FINITE strategy problem** — over the finite menu of *matchings* of the LB pieces (cut
larger at smaller) + selective halving, the best strategy forces A ≤ 1/D with 0 failures for
n=2,3,4 (worst excess −0.14, −0.11, −0.09). Cutting each original piece at most once suffices; no
continuous cut fractions, no fragment-of-fragment cuts. This *corrects* the round-4 explorer's
"B2 needs a continuous argument" reading (that came from restricting to consecutive matchings).
It also gives a genuinely new, non-graveyard Case-B framing (below).

---

## imo-2026-03

### direct-constructive: advance
Target: the full problem — c(n) = 2^n/(2^{n+1}−1), both bounds, all n.
Technique: explicit optimal strategies both sides; alternating-sum boundary-crossing (lower
bound), pair-creation IH(n) (Case-B upper bound). This round: close the LOWER bound outright
(cleanest wins) and push Case B.
Skeleton (only the open gaps — everything else is proved/certified in the file):

  1. **L1, case a=0 (Route A — alternating-sum identity).** In D-units target O ≥ 2^n ⟺
     A = O − E ≥ 1. Prove the identity
        **A = 1 + 2·Σ_{inverted (I_k, f_j) pairs} (I_k − f_j),  each term ≥ 0 ⟹ A ≥ 1**,
     where an "inverted pair" is an intact I_k and fragment f_j that sit in the interleaving order
     f_j > I_k but in the target config satisfy f_j ≤ I_k. — by Lemma S applied crossing-by-crossing
     from the interleaving reference config F* (each crossing away from the interleaving adds
     +2(I_k − f_j) > 0; the sum is path-independent, hence an identity). The cut-count k ≤ n enters
     because the interleaving needs n+1 fragments to fill the n+1 odd slots; with k < n fragments some
     intact sits at an odd rank, only raising A. Tight at f_1 = 2^{n−1} (A = 1). — GAP L1
  2. **L2 (confine-to-R_n — unreachable-interleaving).** For any XY placement with ≥1 cut outside
     R_n: moving that stray cut into R_n weakly lowers O (the two small pieces from an R_j cut,
     j<n, only push intacts from even to odd ranks). Formalize the strict version: with ≤ n−1 cuts
     in R_n only ≤ n fragments of R_n exist, so the n+1-slot interleaving is unreachable ⟹ some
     intact P_m (m<n) sits at an odd rank contributing a fixed >0 amount ⟹ O > 2^n; combined with
     §4.1 (spares R_n ⟹ O ≥ 2^n) and step 1 (all cuts in R_n ⟹ O ≥ 2^n), every placement gives
     O ≥ 2^n. — by fragment-count bound (certified) + Lemma S. — GAP L2
  3. **U1 = Case B (pair-creation IH(n)).** B1-large (a_1 > c(n)): halve a_1 (pair cancels), reduce
     to n sub-singletons with sub-sum < (2^n−1)/D; apply IH(n): n pieces > 1/D, sum < (2^n−1)/D ⟹
     XY forces A ≤ 1/D with n−1 cuts. Base IH(2) (1 cut: a_2−a_3 < 1/D from a_2+a_3 < 3/D) and
     IH(3) (three-way split, doubly-hard leaf |a_2−a_3−a_4| < 1/D from the sum bound) proved by the
     explorer. B2 (a_1 ≤ 1/2): same IH menu. — GAP U1 (general-n IH induction is the open core).
Key lemmas:
  - Route-A identity A = 1 + 2Σ_inversions(I_k−f_j) — because each interleaving boundary-crossing
    contributes +2(I_k−f_j) by Lemma S and the total is path-independent (a genuine identity, not
    an inequality chain), so A ≥ 1 term-by-term.
  - Unreachable-interleaving — because filling all n+1 odd slots with fragments needs n+1 fragments
    = n cuts in R_n; a cut spent outside R_n leaves an intact stranded at an odd rank (fragment-
    count bound), forcing A > 1.
  - IH(n) pair-creation — because "cut larger at smaller" pairs cancel in A and the sum bound
    (2^n−1)/D forces the residual singleton |Σ±b_i| < 1/D at the doubly-hard leaf.
Open gaps: L1 (Route-A identity for all n), L2 (strict unreachable-interleaving), U1 (IH(n) general
induction step — B1-large and B2).
Cases to cover: L1 case a=0 (a=1 done via cascade); L2 stray-cut placements; U1 sub-cases
B1-large + B2; base cases n=1,2 done.
Watch out for: do NOT revive the ∫⌊(N_F−N_I)/2⌋ integral for L1 (it equals 2^n−O, circular — proved
round 3). Do NOT use the per-rank bound r_{2j} ≤ 2^{n−j} (FALSE). Route A must use k ≤ n. IH(n)
must actually induct — the n=3 leaf bound must be shown to generalize (the real risk).

### caseB-matching: new
Target: the full problem — c(n) = 2^n/(2^{n+1}−1), both bounds, all n. (File written at
approaches/caseB-matching.md.)
Technique: **finite matching-exchange** for the Case-B upper bound (genuinely different from
direct-constructive's IH(n) induction and far from the graveyard). Reuses G1, R, H and
direct-constructive's lower bound; substitutes the Case-B step with a finite optimization.
Skeleton:
  1. Reduce to A ≤ 1/D — G1 + R (certified).
  2. Lower bound — imported from direct-constructive (shares L1/L2, closed there).
  3. Upper bound Case A — Lemma H (certified).
  4. **Upper bound Case B — Lemma M.** XY's menu = a matching M of the p pieces (each pair: cut
     larger at smaller → an exact cancelling copy + residual gap) + a halve/keep choice on
     unmatched singletons; |M|+|H| ≤ n. **Some matching strategy achieves A ≤ 1/D.** — GAP
  5. Assemble.
Key lemmas:
  - **Lemma M** (best matching ⟹ A ≤ 1/D) — because "cut larger at smaller" creates cancelling
    copies, and a matching-exchange (swap two pairs, or match↔halve) strictly lowers A whenever
    A > 1/D; termination below 1/D uses Σa_i = 1 and all a_i > 1/D to cap the surviving odd-parity
    interval. Evaluate A exactly via the **parity/XOR** tool: each cut of ℓ into (m,ℓ−m) XORs
    [N(t) odd] on (0,m)∪(ℓ−m,ℓ), so A = XOR-measure of the toggle sets (the naive "altsum of gaps"
    is FALSE — verified this round — because equal copies interleave).
Open gaps: Lemma M (matching-exchange proof for general n); budget lemma (|M|+|H| ≤ n, routine).
Cases to cover: p even / p odd (leftover halve-or-keep); Case A vs Case B; n=1 base (Case B
vacuous).
Watch out for: keep it induction-free (that is what makes it distinct from direct-constructive).
Do NOT use the false "altsum of residual gaps." **KILL-SWITCH ALREADY PASSED AT THE GATE**:
exhaustive matching+halving search gives A ≤ 1/D with 0 failures over 800 random Case-B configs at
each of n=2,3,4 (worst excess −0.14/−0.11/−0.09); full continuous ≤ n-cut optimization agrees, so
original-piece cuts suffice. The wall this NEW framing must break is Lemma M's exchange proof, not
feasibility.

### lower-routeB: copy-of direct-constructive
Target: the full problem (identical twin of direct-constructive), diverging only on the L1 route.
Technique: L1 via **Route B (sub-problem induction)** instead of Route A — two documented viable
routes to the same gap justify a copy so both run in parallel.
Skeleton: identical to direct-constructive except step 1:
  1'. **L1 case a=0 (Route B).** Delete the top intact 2^{n−1} (rank 1, odd in case a=0);
     parities flip, so E(I_n∪F) ≤ ΣI_n reduces to O_sub ≤ 2^n − 1 on the sub-problem I_{n−1} ∪ F
     (ΣF up to 2^n, each f ≤ 2^{n−1}). Prove O_sub ≤ 2^n − 1 by recursing: apply the a=1 cascade to
     the sub-problem's top fragment (if a fragment ∈ (2^{n−2}, 2^{n−1}) exists, cascade again),
     terminating when all fragments ≤ 1 (E_sub = 0). — GAP (needs the generalized sub-statement,
     since O_sub ≤ 2^n − 1 is NOT G-L1(n−1)). Verified n=4: max O_sub = 15 = 2^n − 1, tight at
     F = {8,4,2,1,1}.
Key lemmas: shifted-interleaving sub-bound O(I_{n−1}∪F) ≤ 2^n − 1 — because the tight config is
F = {2^{n−1},…} and the a=1 cascade peels one fragment per level until fragments vanish.
Open gaps: the generalized sub-statement for Route B (the reason Route A is primary — B "loops"
without it). L2, U1 shared.
Cases to cover: case a=0 recursion depth. Watch out for: this route is LOWER priority than
Route A (which is a clean identity) — recommend building it only if Route A stalls; the reviewer
may cut it to save a builder. Kept on the table for route-diversity on L1.

---

## Proposed field for the outline-reviewer

- **direct-constructive** — advance. Priority order this round: (1) L1 case a=0 via Route-A
  identity, (2) L2 via unreachable-interleaving — these close the lower bound outright and are the
  cleanest wins; (3) U1 Case B via IH(n).
- **caseB-matching** — new. The required ≥1 genuinely-new Case-B framing (finite matching-exchange,
  not in the graveyard: differs from game-separation induction, concavity-of-g, amortized-greedy,
  potential-duality). Numerical kill-switch already PASSED at the gate. Adds the second live
  approach, diversifying the narrow field.
- **lower-routeB** — copy-of direct-constructive. Optional route-B parallel on L1; low priority,
  cut if builder budget is tight.

Recommended build set (reviewer decides): direct-constructive (lower-bound close + Case B) and
caseB-matching (Lemma M). Include lower-routeB only if a third builder is free.
