## Status
partial

## Approaches tried
- (round 2, new) smoothing-extremal: attack the upper bound from the MAX side, via an
  exchange/smoothing argument on the LB-partition space, proving that the dyadic profile
  G_n maximizes the value XY forces, F(A) ≤ F(G_n) = 2^n/D_n for all A at once — never
  building an explicit XY strategy. Outcome: the SHARED FOUNDATION (L0/L1/L2 reduction,
  the extremal reformulation, and existence of a maximizer) is proven rigorously here.
  The KEY GAP, Lemma G (the single consecutive-pair smoothing monovariant), was
  REFUTED by the mandated numeric pre-check: moving a consecutive-rank pair toward the
  2:1 ratio (sum fixed) DECREASES XY's forced value F in ~35% of tested cases, and for
  some non-dyadic A BOTH available consecutive-pair moves decrease it. A weaker
  "some 2-part mass-transfer strictly increases F at every non-dyadic A" holds numerically
  (no spurious local maxima found), but proving it rigorously re-imports the very object
  the framing was meant to avoid (XY's optimal-response structure / the directional
  derivative of a min-over-responses). Verdict: the smoothing route as specified is
  likely NON-VIABLE; recorded honestly, not forced.

## Current best
Rigorously established this round (reusable, promotable — see Promotable lemmas):

- **L0 (Claiming lemma).** For a fixed multiset of piece lengths in the alternating
  claim game (LB first), optimal play for both players is "take a largest remaining
  piece"; hence with pieces sorted descending p_(1) ≥ … ≥ p_(m), LB's total equals the
  sum of the odd-ranked pieces. (Full proof below.)
- **L1 (Reduction to the multiset-refinement game).** The whole problem is equivalent to:
  LB picks a multiset A of ≤ n+1 positive reals summing to 1 (his ≤ n marks); XY refines
  A by ≤ n cuts, each cut splitting one current part into two positive parts; LB's
  guaranteed total is the odd-rank sum of the resulting multiset. (Full proof below.)
- **L2 (Alternating-sum identity).** For final pieces summing to 1, the odd-rank sum
  equals (1+S)/2 where S = Σ_i (−1)^{i+1} p_(i). Hence the target c(n) = 2^n/D_n
  (D_n = 2^{n+1}−1) is equivalent to: for every LB partition A, XY can refine so that
  S ≤ 1/D_n; and LB can force S ≥ 1/D_n by playing G_n.
- **Extremal reformulation + existence of a maximizer.** Define
  S*(A) = min over XY's ≤ n cuts of S(final), and F(A) = (1+S*(A))/2 = min over XY of
  odd-rank sum. Then S* is continuous on the compact simplex of partitions of 1 into
  ≤ n+1 nonnegative parts, so max_A S*(A) is attained (Extreme Value Theorem). The upper
  bound c(n) ≤ 2^n/D_n is EXACTLY the statement max_A S*(A) = S*(G_n) = 1/D_n.

**Open gap (the crux, unclosed and — as prescribed — refuted):** the identity
max_A S*(A) = S*(G_n). The planned mechanism (Lemma G: a single consecutive-rank-pair,
sum-preserving perturbation toward ratio 2 does not decrease S*) is FALSE (numeric
refutation below). The only surviving version of the extremal claim ("at every
non-dyadic A some 2-part transfer strictly raises S*") is numerically true but its proof
requires understanding how XY's optimal response moves — i.e. it does not sidestep the
crux, it renames it. See "The gap, honestly" below.

## Approaches tried (detail) / The gap, honestly

### Why the smoothing framing was attractive
S*(A) = max-min value; its maximizer over the LB simplex is (numerically) the dyadic
G_n. An extremal/exchange proof would give the upper bound F(A) ≤ F(G_n) for ALL A at
once, with an explicit XY strategy needed only at (near-)dyadic profiles — avoiding the
per-partition match/bisect construction on which the other three approaches share a wall.

### Mandated numeric pre-check (this is what gates the approach)
I built a reliable estimator of S*(A) (min over all cut-allocations of the alternating
sum of the resulting multiset, inner splits optimized by multistart Nelder–Mead).
Validation: at G_2 = {1,2,4}/7 the estimator returns S* = 0.142857 = 1/7 exactly (to 6
digits), and on random A it returns values strictly below 1/7 — confirming the extremal
TARGET (dyadic maximizes S*).

**Lemma G, tested directly and REFUTED.** For sorted A = (a_1≥a_2≥a_3), sum 1, I moved a
consecutive pair (a_i, a_{i+1}) a fraction 0.4 toward the ratio-2 point (2s/3, s/3),
s = a_i+a_{i+1} fixed, and measured ΔS*. Result over 20 (A, pair) samples at n=2:
**7/20 moves toward dyadic strictly DECREASED S*** (magnitudes ~0.02, far above the
~1e-4 estimator noise). Concretely, for A = (0.390, 0.338, 0.272):
moving pair (1,2) toward 2:1 gave ΔS* = −0.0253; moving pair (2,3) toward 2:1 gave
ΔS* = −0.0275 — *both* consecutive-pair smoothing moves toward dyadic lower S*. So there
is NO consecutive-pair, sum-preserving, toward-ratio-2 step that keeps S* from
decreasing for this A. Lemma G is false as stated.

Two structural reasons it cannot be salvaged in that exact form:
1. A sum-preserving move on a consecutive pair fixes that pair's sum a_i+a_{i+1}. Dyadic
   G_2 has specific pair-sums (a_1+a_2 = 6/7, a_2+a_3 = 3/7); a generic A does not, and
   no sequence of sum-preserving consecutive-pair moves can change those pair-sums. So
   consecutive-pair ratio-2 moves cannot even CONNECT a generic A to G_n.
2. Even where connected, the move often decreases S* (point above).

**The weaker extremal claim, tested.** For non-dyadic A I scanned all six small 2-part
mass transfers (any pair, either direction) and recorded the best ΔS*. Over 8 random A at
n=2 every one admitted a strictly improving transfer (best ΔS* from +0.013 to +0.060);
no spurious local maximum appeared. So "G_n is the unique maximizer, and at every
non-dyadic A some improving 2-part transfer exists" is numerically supported.

### Why the weaker claim does NOT rescue the approach
The improving direction is not given by any simple rule — across the sample it was
(2→0), (0→2), (1→0), (1→2) with no pattern. To PROVE "some improving transfer exists at
every non-dyadic A" one must compute a directional derivative of S*(A). But S*(A) is a
min over XY's responses; its one-sided directional derivative at A in direction v is
min over XY's OPTIMAL responses at A of the derivative of that response's value — an
envelope-theorem object that requires knowing XY's optimal response set at A and how it
deforms (the max-min discontinuity the outline-reviewer flagged). That is precisely the
per-partition XY-strategy structure the smoothing framing was supposed to avoid. Hence
the framing does not sidestep the crux; it re-imports it as "identify the improving
direction," which is no easier than the direct upper bound.

**Honest verdict:** smoothing-extremal is likely non-viable as a crux-avoiding route.
The reusable value delivered here is the rigorous L0/L1/L2 foundation and the
maximizer-existence reformulation (all shared with the whole field). If a future round
wants to keep an extremal framing alive, it must supply the directional-derivative /
optimal-response analysis — which is the crux, not an escape from it.

---

# Rigorous proofs of the established results

Throughout, D_n = 2^{n+1} − 1, and G_n = { 2^0/D_n, 2^1/D_n, …, 2^n/D_n } (n+1 parts,
sum (2^{n+1}−1)/D_n = 1). The answer to be proven is c(n) = 2^n/D_n; this round secures
the reduction and reformulation, not the upper bound itself.

## Lemma L0 (Claiming lemma)

**Statement.** Fix a finite multiset M = {p_1, …, p_m} of nonnegative reals. Two players
alternately claim a not-yet-claimed element, the first player moving first, each seeking
to maximize the sum of the elements it claims. Then under optimal play the value obtained
by the first mover equals W(M) := the sum of the odd-ranked elements when M is sorted in
weakly decreasing order (i.e. p_(1) + p_(3) + p_(5) + …), and "claim a largest remaining
element" is an optimal move for the player to move.

**Sub-lemma (order-statistic monotonicity).** Let R be a finite multiset and let B be
obtained from R by replacing one element value v with a value v' ≥ v (all other elements
unchanged). Then for every j, the j-th largest element of B is ≥ the j-th largest element
of R.

*Proof of sub-lemma.* For any threshold t, let N_R(t) = #{elements of R that are ≥ t}.
Raising a single element from v to v' can only preserve or increase membership in
{≥ t} (it changes membership only for t in (v, v'], where it adds one), so
N_B(t) ≥ N_R(t) for all t. The j-th largest element of a multiset X equals
x_(j) = sup{ t : N_X(t) ≥ j } (with the convention sup ∅ = −∞). Since N_B(t) ≥ N_R(t)
for every t, the set {t : N_B(t) ≥ j} contains {t : N_R(t) ≥ j}, so its supremum is at
least as large: b_(j) ≥ r_(j). ∎(sub-lemma)

**Proof of L0.** Induct on m = |M|. For m = 0 both sides are 0; for m = 1 the first mover
claims p_1 and gets W = p_1. Assume the statement for all multisets of size < m, m ≥ 1.

Let T = Σ_i p_i and sort M as p_(1) ≥ … ≥ p_(m). Suppose the first mover claims a specific
element x, leaving the multiset M∖{x} of size m−1. The opponent now moves first on
M∖{x}, and by the induction hypothesis obtains exactly W(M∖{x}) under optimal play, while
the total of M∖{x} is T − x. The two players between them claim all of M∖{x}, so the
first mover's take from the remainder is (T − x) − W(M∖{x}). Hence the first mover's total
if it opens with x is
    g(x) = x + (T − x) − W(M∖{x}) = T − W(M∖{x}).
The first mover therefore chooses x to MINIMIZE W(M∖{x}).

Claim: W(M∖{x}) is minimized by taking x a largest element, and then equals
W(M∖{p_(1)}) = p_(2) + p_(4) + …. It suffices to show: for adjacent ranks i, i+1,
    W(M ∖ {p_(i)}) ≤ W(M ∖ {p_(i+1)}),   (∗)
i.e. removing the larger of two adjacent-ranked elements leaves the opponent with a
weakly smaller value; transitivity down the sorted order then makes removing p_(1) a
minimizer.

To prove (∗): the two multisets M∖{p_(i)} and M∖{p_(i+1)} have the SAME elements except
that the first contains p_(i+1) where the second contains p_(i), and p_(i) ≥ p_(i+1).
Thus M∖{p_(i+1)} is obtained from M∖{p_(i)} by raising one element from p_(i+1) to p_(i).
By the sub-lemma, every order statistic of M∖{p_(i+1)} is ≥ the corresponding order
statistic of M∖{p_(i)}. Since W is a sum of order statistics at fixed (odd) positions,
W(M∖{p_(i+1)}) ≥ W(M∖{p_(i)}), which is (∗).

Therefore the optimal opening take is a largest element, giving first-mover value
    g(p_(1)) = T − W(M∖{p_(1)}) = T − (p_(2)+p_(4)+…) = p_(1)+p_(3)+p_(5)+… = W(M).
This is exactly the claim; the induction is complete. In particular, both players playing
"take a largest remaining element" is a mutual best response, and the first mover
(Liu Bang) ends with the odd-ranked sum. ∎

## Lemma L1 (Reduction to the multiset-refinement game)

**Statement.** The original game has the same value as the following abstract game. LB
chooses a multiset A of ≤ n+1 positive reals summing to 1. XY then chooses a refinement:
starting from A, he performs a total of ≤ n "cuts", each cut replacing one current part
of length ℓ by two positive parts of lengths ℓ' and ℓ−ℓ' (0 < ℓ' < ℓ). Let B be the
resulting multiset. LB's guaranteed total equals the odd-rank sum of B. LB maximizes,
XY minimizes.

**Proof.** LB marks at most n distinct interior points of [0,1]; together with the
endpoints these cut the stick into k ≤ n+1 subintervals, i.e. a multiset A of k ≤ n+1
positive lengths summing to 1. Their positions along the stick are recorded but, as we
show, will not matter. XY then marks at most n further points, all distinct from each
other and from LB's marks and the endpoints. Each XY mark lies strictly inside exactly
one current subinterval and splits it into two positive pieces; since XY places at most n
such marks, the final collection of pieces B is obtained from A by at most n cuts in the
sense above. (XY may use fewer than n marks; distinctness guarantees each mark is a
genuine cut, and no mark coincides with an existing division point.)

The stick is then cut at all marked points, producing the pieces B (a multiset of
lengths), and the two players alternately claim pieces, LB first. By Lemma L0, the value
of this claiming phase depends only on the MULTISET B of piece lengths — it is the
odd-rank sum of B — and not on the positions of the pieces along the stick. Consequently
LB's payoff is a function of the multiset B alone, and B is exactly an ≤ n-cut refinement
of the multiset A. Thus the original game is equivalent to the abstract multiset game as
stated. ∎

## Lemma L2 (Alternating-sum identity and reformulation)

**Statement.** For a final multiset B with parts summing to 1, sorted p_(1) ≥ … ≥ p_(m),
the odd-rank sum satisfies
    O(B) := p_(1) + p_(3) + … = (1 + S(B))/2,  where  S(B) := Σ_{i=1}^m (−1)^{i+1} p_(i).
Consequently, with E(B) := p_(2) + p_(4) + … the even-rank sum,
c(n) ≤ 2^n/D_n ⟺ for every LB partition A there is an ≤ n-cut refinement with S ≤ 1/D_n.

**Proof.** O(B) + E(B) = Σ p_(i) = 1 and O(B) − E(B) = S(B). Adding, 2 O(B) = 1 + S(B),
so O(B) = (1+S(B))/2. For the equivalence: LB's guaranteed value with partition A and
optimal XY response is F(A) = min over ≤ n-cut refinements B of O(B) = (1 + S*(A))/2,
where S*(A) = min over ≤ n-cut refinements of S(B). The largest LB can guarantee is
max_A F(A) = (1 + max_A S*(A))/2. Since O ≤ 2^n/D_n ⟺ S = 2O − 1 ≤ 2·2^n/D_n − 1 =
(2^{n+1} − D_n)/D_n = 1/D_n (using D_n = 2^{n+1} − 1), the stated equivalence follows. ∎

## Extremal reformulation and existence of a maximizer

**Statement.** S*(A) = min over XY's ≤ n cuts of S(B) is continuous on the compact set
Δ = { x ∈ R^{n+1} : x_i ≥ 0, Σ x_i = 1 } (a partition into < n+1 positive parts is the
face where some x_i = 0). Hence max_{A∈Δ} S*(A) is attained, and the upper bound
c(n) ≤ 2^n/D_n is the assertion max_{A∈Δ} S*(A) = S*(G_n) = 1/D_n.

**Proof of continuity/attainment.** Fix an allocation of XY's cuts, i.e. a vector
c = (c_1,…,c_{n+1}) of nonnegative integers with Σ c_j ≤ n, meaning part x_j is split into
c_j + 1 positive sub-parts. For fixed c, XY's sub-parts are described by, for each j, a
point t^{(j)} in the closed simplex Σ^{c_j} = { f ∈ R^{c_j+1} : f_l ≥ 0, Σ f_l = 1 } (the
sub-part lengths are x_j · f^{(j)}_l). Let Φ_c(A, t) = S(B) be the alternating sum of the
resulting multiset; Φ_c is a continuous function of (A, t) (it is the alternating sum of
the sorted list of the numbers x_j f^{(j)}_l, and sorting a continuous vector is
continuous, as is the fixed-sign combination of order statistics). The parameter t ranges
over the fixed compact product of simplices K_c = Π_j Σ^{c_j}, independent of A. By
Berge's Maximum Theorem (applied to minimization: the value function of a continuous
objective minimized over a fixed compact set is continuous in the outer parameter), the
partial value g_c(A) := min_{t ∈ K_c} Φ_c(A, t) is continuous on Δ. There are finitely
many allocations c, and S*(A) = min_c g_c(A) (XY may take any allocation with ≤ n cuts,
including the zero allocation which yields S(A)). A finite minimum of continuous functions
is continuous, so S* is continuous on the compact set Δ. By the Extreme Value Theorem the
maximum max_{A∈Δ} S*(A) is attained. The equivalence to the upper bound is L2. ∎

*(What remains open — see "The gap, honestly": that the maximizer equals G_n. The
prescribed single-pair monovariant proof of this is refuted; a valid proof requires
XY's optimal-response structure, i.e. it is not a crux-avoiding argument.)*

## Promotable lemmas

- **L0 (Claiming lemma)** — statement above; full proof above (order-statistic
  monotonicity sub-lemma + induction on the number of pieces). Reusable by every
  approach; foundational. Numerically re-verified (greedy odd-index = game value on 2000
  random multisets, 0 mismatches).
- **L1 (Reduction to the multiset-refinement game)** — statement and full proof above.
  Foundational, shared by all approaches.
- **L2 (Alternating-sum identity, O = (1+S)/2, and the S ≤ 1/D_n reformulation)** —
  statement and full proof above. Shared by all approaches.
- **Existence-of-maximizer reformulation** (S* continuous on the simplex via Berge's
  Maximum Theorem; max attained; upper bound ⟺ max_A S*(A) = S*(G_n)) — proof above.
  Useful to any extremal-framing approach.

## Spec concerns
- The numeric pre-check REFUTES the specific Lemma G the outline prescribed for this
  approach. Per the task instruction ("if the pre-check fails, say so honestly and record
  smoothing-extremal as likely non-viable rather than forcing a proof"), this approach
  is recorded partial with the crux gap open and the prescribed mechanism disproven. For
  the orchestrator: smoothing-extremal should likely be routed RETHINK (its central
  monovariant is false and the surviving extremal claim re-imports the crux); its
  durable contribution is the certified L0/L1/L2 foundation. The other framings
  (induction-peel's value-function DP, potential/certificate's min-pairing witness)
  remain the live routes to the upper bound.
