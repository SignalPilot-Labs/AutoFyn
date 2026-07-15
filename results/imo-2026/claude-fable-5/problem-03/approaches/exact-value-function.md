# Approach: exact-value-function

## Status
partial

## Approaches tried
- (round 1, outline) Skeleton opened. Numerics at n = 2 (grid best-response search) support the conjectured best-response formula on all tested configurations; the formula reproduces the known closed form V(a, b) = min((1 + a)/2, b) at n = 1.
- (round 1, build) Repaired the two mechanisms the outline-reviewer flagged: (i) E1 vertex classification now proven in full as Lemma V, covering all three facet families (cross-piece ties, same-piece ties = equipartitions, zero/boundary facets = coalesced marks / fewer effective marks); (ii) the false "vertex sizes in ½ℤ" claim of E3 is withdrawn and replaced by the correct statement "vertex values are the unique solution of a full-rank nonnegative-integer linear system" — integrality is NOT automatic (equipartitions give denominators ≥ 3), so E3 splits into a PROVEN integer-vertex parity lemma (Lemma P) and an open fractional-vertex gap (E3′). Lemmas C, D, F proven in full. Upper bound: replies H and F(j,r) constructed with exact mark ledgers, Chain Lemma proven, cases (a),(b) closed; deficient case (c) remains open (Gap E2). Multistart numerical minimization at n = 1, 2, 3 confirms min defect over ALL replies to the geometric configuration equals exactly 1/D (so the fractional-vertex gap E3′ is true, just unproven). — outcome: real progress, two hard gaps remain (E2, E3′).

## Current best
Answer (to be proven): **c(n) = 2^n/(2^{n+1} − 1)**; write D = 2^{n+1} − 1, and work in units of 1/D where convenient.

Fully proven this round (all proofs below):
- **Lemma C** (claiming value = Odd of the piece multiset),
- **Lemma D** (defect layer-cake identity + corollaries D1–D4: nonnegativity, strip-pairs invariance, pairs-plus-leftover formula, zero-append invariance),
- **Lemma F** (LB with < n effective marks is held to exactly 1/2),
- **Lemma V** (attainment of XY's best response and the full vertex classification: an optimal reply exists whose distinct positive sizes v_1 > … > v_s are the unique solution of A v = q for a nonnegative integer matrix A of rank s),
- **Lemma P** (integer-vertex parity: any reply to the geometric configuration all of whose sub-piece sizes are integers in units 1/D has defect ≥ 1/D),
- **Chain Lemma** and upper-bound cases (a), (b); the reduction V(q) = (1 + mindefect(q))/2.

Open gaps: **E2** (upper bound, deficient case: some d_j < 0 — needs cascade replies) and **E3′** (lower bound: fractional vertices, i.e. vertex replies with non-integer values). Partial structure on E3′ is proven (Fact 1: every LB piece contains 0 or ≥ 2 non-integer sub-pieces; mod-p refinement sketched as candidate repair).

---

## The build (proofs in full; gaps marked)

### 0. Setup and conventions

Liu Bang (LB) marks at most n points of the stick [0,1], then Xiang Yu (XY), seeing them, marks at most n further points, all marked points distinct; the stick is cut at all marked points; the players alternately claim pieces, LB first, each maximizing his own total length. We must compute the largest total c(n) that LB can guarantee.

A *configuration* is the multiset of piece lengths after LB's marks; a *reply* is XY's legal set of marks; the *final multiset* P is the multiset of piece lengths after all cuts. A mark at an endpoint of the stick, or the degenerate limit of coalescing marks, creates a zero-length piece; by Corollary D4 below zero pieces change nothing, so we may freely allow sub-piece lengths equal to 0 in parametrizations and delete them at the end.

For a finite multiset P of nonnegative reals with decreasing enumeration p_1 ≥ p_2 ≥ … ≥ p_m define

- Odd(P) = p_1 + p_3 + p_5 + … , Even(P) = p_2 + p_4 + … ,
- defect(P) = Odd(P) − Even(P), so Odd(P) = (Σ(P) + defect(P))/2 where Σ(P) is the total.

### 1. Lemma C (claiming value)

**Lemma C.** In the alternating claiming game on a finite multiset S of nonnegative reals (players alternately remove one element each, the mover keeps it, both maximize their own total, perfect information), the first mover's optimal value is f(S) = Odd(S).

*Proof.* Strong induction on m = |S|. If m = 0, both sides are 0. Let m ≥ 1 and sort S as p_1 ≥ … ≥ p_m. If the first mover takes the element at sorted position i (for equal values the resulting multiset is the same, so the position determines everything), the opponent becomes first mover on S_i := S \ {p_i} and by induction obtains Odd(S_i); the original mover therefore ends with

  p_i + (Σ(S_i) − Odd(S_i)) = Σ(S) − Odd(S_i).

Hence f(S) = Σ(S) − min_{1≤i≤m} Odd(S_i), and we must show the minimum is attained at i = 1 with value Even(S).

The sorted enumeration of S_i is p_1, …, p_{i−1}, p_{i+1}, …, p_m, so

  Odd(S_i) = Σ_{j<i, j odd} p_j + Σ_{j>i, j even} p_j.

For i = 1 this is Σ_{j even} p_j = Even(S). For general i:

- i even: Odd(S_i) − Even(S) = Σ_{j<i, j odd} p_j − Σ_{j≤i, j even} p_j = (p_1 − p_2) + (p_3 − p_4) + … + (p_{i−1} − p_i) ≥ 0.
- i odd (i ≥ 3): Odd(S_i) − Even(S) = Σ_{j<i, j odd} p_j − Σ_{j<i, j even} p_j = (p_1 − p_2) + … + (p_{i−2} − p_{i−1}) ≥ 0.

Each bracket is ≥ 0 because the list is sorted. So min_i Odd(S_i) = Even(S) and f(S) = Σ(S) − Even(S) = Odd(S). ∎

(Technique: exchange/greedy induction; cf. knowledge_base.md entries on exchange arguments in take-away games. This settles the claiming phase completely: LB's payoff against a final multiset P is exactly Odd(P), and since the game is constant-sum with total Σ(P) = 1, XY's goal in the marking phase is exactly to minimize Odd(P).)

### 2. Lemma D (defect identity) and corollaries

**Lemma D.** For a finite multiset P of nonnegative reals, let N(x) = #{p ∈ P : p > x}. Then

  defect(P) = λ({x ≥ 0 : N(x) is odd}) (λ = Lebesgue measure).

*Proof.* With the decreasing enumeration p_1 ≥ … ≥ p_m, write p_i = ∫_0^∞ 1[x < p_i] dx. Then

  defect(P) = Σ_i (−1)^{i+1} p_i = ∫_0^∞ Σ_i (−1)^{i+1} 1[p_i > x] dx

(the sum is finite, so the interchange is just linearity of the integral over a finite sum of integrable functions). For fixed x, {i : p_i > x} = {1, 2, …, N(x)} by sortedness, so the integrand is Σ_{i=1}^{N(x)} (−1)^{i+1} = 1 if N(x) is odd and 0 if even. ∎

**Corollary D1 (nonnegativity).** defect(P) ≥ 0; equivalently Odd(P) ≥ Σ(P)/2. (The measure of a set is ≥ 0.)

**Corollary D2 (strip pairs).** If P′ is obtained from P by deleting two elements of equal value s, then defect(P′) = defect(P). (N′(x) = N(x) − 2·1[x < s], so parity is unchanged pointwise.)

**Corollary D3 (pairs + leftover).** If P is a disjoint union of pairs of equal elements together with at most one extra element ρ, then defect(P) = ρ (respectively 0 if there is no extra element), so Odd(P) = (Σ(P) + ρ)/2. (Strip all the pairs by D2; the remaining multiset is {ρ} or ∅, whose defect is ρ or 0.)

**Corollary D4 (zero-append).** defect(P ∪ {0}) = defect(P) and Odd(P ∪ {0}) = Odd(P). (A zero element never satisfies p > x for x ≥ 0, so N is unchanged; totals are unchanged; use Odd = (Σ + defect)/2.)

### 3. Lemma F (fewer marks) and the reduction

**Lemma F.** If after LB's move the stick has pieces q_1, …, q_{m+1} coming from m ≤ n − 1 effective (interior, distinct) marks, then XY can force LB's payoff to be exactly 1/2.

*Proof.* XY marks the midpoint of each of the m + 1 pieces: these m + 1 ≤ n points are interior to distinct pieces, hence distinct from each other and from LB's marks — a legal reply. The final multiset is the disjoint union of the pairs {q_i/2, q_i/2}, so by Corollary D3 and Lemma C LB's payoff is Odd = Σ/2 = 1/2. Conversely, LB's payoff is always ≥ 1/2 by Corollary D1 and Lemma C. ∎

Since 2^n/D = 2^n/(2^{n+1} − 1) > 1/2, a configuration with fewer than n effective marks already satisfies the upper bound V ≤ 2^n/D, and cannot be LB-optimal once the lower bound is established. **From now on LB's configuration is q = (q_1, …, q_{n+1}), q_i > 0, Σ q_i = 1** (n interior distinct marks), and we study

  V(q) := inf over legal XY replies of Odd(final multiset) = (1 + mindef(q))/2,

where mindef(q) := inf over legal replies of defect(P). The target claim becomes:

- **Upper bound:** mindef(q) ≤ 1/D for every q. (Then c(n) ≤ max(1/2, (1 + 1/D)/2) = (D+1)/(2D) = 2^n/D.)
- **Lower bound:** mindef(g) ≥ 1/D for the geometric configuration g = (1, 2, 4, …, 2^n)/D, obtained from LB's marks at (2^k − 1)/D, k = 1, …, n (these are interior and distinct; the k-th gap has length ((2^{k+1}−1) − (2^k −1))/D = 2^k/D). (Then c(n) ≥ (1 + 1/D)/2 = 2^n/D.)

### 4. Lemma V (attainment and vertex classification) — Gap E1 closed

**Parametrization.** Fix q as above. For a *cut assignment* m = (m_1, …, m_{n+1}) of nonnegative integers with Σ m_i = n, let

  𝒯_m = { t = (t_{i,j})_{1≤i≤n+1, 1≤j≤m_i+1} : t_{i,j} ≥ 0, Σ_j t_{i,j} = q_i for every i },

a product of simplices, hence a compact convex polytope. Write P(t) for the multiset of ALL entries t_{i,j} (zeros included).

**Claim V0 (the parametrization is exact).** mindef(q) = min over assignments m of min over t ∈ 𝒯_m of defect(P(t)), and the inner minima are attained.

*Proof.* (≥) A legal reply with k ≤ n marks puts m_i marks into the interior of piece i (marks at LB's marks or at stick endpoints are illegal or create zero pieces; a mark AT an endpoint of the stick is a point of the stick and creates a zero piece — either way, replace it by nothing and use D4: the defect is unchanged and the reply remains legal with fewer marks). The marks inside piece i cut it into m_i + 1 positive sub-lengths. Pad with n − k zero sub-pieces (say, appended to piece 1's list, formally increasing m_1 by n − k with the extra t_{1,j} = 0) to get a point t ∈ 𝒯_m for an assignment with Σ m_i = n; by D4, defect(P(t)) equals the defect of the true final multiset. So every legal reply's defect is realized in the right-hand side.

(≤) Conversely, given t ∈ 𝒯_m, delete the zero entries; inside piece i place marks at the partial sums of its positive entries — these are interior points of piece i, distinct from each other and from all LB marks, and the number used is at most Σ m_i = n. This is a legal reply whose final multiset is P(t) minus zeros, with the same defect by D4.

Attainment: 𝒯_m is compact and t ↦ defect(P(t)) is continuous, because the sorting map ℝ^N → ℝ^N (N = Σ_i (m_i+1) = 2n+1 fixed) is continuous (each order statistic is 1-Lipschitz in the sup norm: |p_{(k)}(a) − p_{(k)}(b)| ≤ max_{i}|a_i − b_i|, a standard fact), and defect is a fixed linear functional of the sorted vector. There are finitely many assignments m. ∎

**Lemma V (vertex classification).** There exist an assignment m and a minimizer t* ∈ 𝒯_m of defect(P(·)) with the following structure. Let v_1 > v_2 > … > v_s > 0 be the distinct positive values among the entries of t*, let n_c ≥ 1 be the multiplicity of v_c in P(t*), and let A = (a_{i,c}) be the (n+1) × s nonnegative integer matrix with a_{i,c} = #{ j : t*_{i,j} = v_c }. Then

  A v = q, and rank(A) = s,

i.e. v = (v_1, …, v_s) is the UNIQUE solution of the linear system A x = q.

*Proof.* By Claim V0 pick an assignment m and any minimizer t¹ ∈ 𝒯_m. Choose a linear order σ on the index set {(i,j)} such that t¹_{σ(1)} ≥ t¹_{σ(2)} ≥ … ≥ t¹_{σ(N)} (ties broken arbitrarily), and consider the *pattern polytope*

  Q_σ = { t ∈ 𝒯_m : t_{σ(1)} ≥ t_{σ(2)} ≥ … ≥ t_{σ(N)} } ∋ t¹,

a compact convex polytope. On Q_σ the coordinates listed in σ-order ARE the decreasing enumeration of P(t), so on Q_σ

  defect(P(t)) = ℓ_σ(t) := Σ_{l odd} t_{σ(l)} − Σ_{l even} t_{σ(l)}

is a LINEAR functional. A linear functional on a nonempty compact convex polytope attains its minimum at an extreme point (Minkowski/Krein–Milman for polytopes; knowledge_base.md, linear programming fundamentals); let t* be an extreme point of Q_σ with ℓ_σ(t*) = min_{Q_σ} ℓ_σ ≤ ℓ_σ(t¹) = mindef(q). Since t* ∈ 𝒯_m corresponds to a legal reply (Claim V0), defect(P(t*)) = ℓ_σ(t*) = mindef(q): t* is a minimizer.

Now the rank claim. A v = q is just the row sums: Σ_c a_{i,c} v_c + (zero entries) = Σ_j t*_{i,j} = q_i. Suppose rank(A) < s, so there is u ∈ ℝ^s, u ≠ 0, with A u = 0. Define the perturbation direction t̂ by t̂_{i,j} = u_c if t*_{i,j} = v_c (c = 1..s) and t̂_{i,j} = 0 if t*_{i,j} = 0. Then t̂ ≠ 0 (each value v_c occurs at least once). For small ε > 0, t* ± ε t̂ ∈ Q_σ:

- Simplex equations: Σ_j (t* ± εt̂)_{i,j} = q_i ± ε (Au)_i = q_i. ✓
- Nonnegativity: zero coordinates are unmoved; coordinates with value v_c stay positive for ε small. ✓
- Order constraints t_{σ(l)} ≥ t_{σ(l+1)}: coordinates with the same value receive the SAME perturbation ±ε u_c, so tight order constraints (equal neighbours in σ) remain equalities; strict inequalities between distinct values (or between v_s and 0) persist for ε small. ✓

Thus t* = ½(t* + εt̂) + ½(t* − εt̂) is a proper convex combination of two distinct points of Q_σ, contradicting extremality. Hence rank(A) = s. ∎

**Remark (the corrected classification — replaces the outline's false "½ℤ" claim).** The tight constraints at t* fall into exactly three families: cross-piece ties (a value shared by sub-pieces of different pieces — "matching"), same-piece ties (a_{i,c} ≥ 2 — "equipartition-type", producing values like q_i/3, q_i/5, …), and zero facets (t_{i,j} = 0 — coalesced marks, i.e. XY effectively using fewer than n marks; these are erased by D4 and reduce N). Consequently the vertex values are NOT in general half-integer combinations of the q_i: by Cramer's rule applied to any invertible s × s submatrix B of A (which exists since rank A = s and the system is consistent with unique solution), v = B^{−1} q_B, so v_c ∈ (1/det B) · ℤ-span{q_i} — arbitrary denominators dividing det B can occur. The lower-bound argument must therefore treat non-integer vertices separately (Gap E3′ below); integrality is available only in the integer case, which is Lemma P.

### 5. Lower bound at the geometric configuration

From here take q = g, i.e. in units of 1/D the pieces are the integers g = (2^0, 2^1, …, 2^n), with total Σ = 2^{n+1} − 1 = D, an odd integer. We must show mindef(g) ≥ 1 (units of 1/D). By Lemma V it suffices to show defect(P(t*)) ≥ 1 for every vertex reply t* as classified above.

**Lemma P (integer vertices).** Let t* be any reply to g (vertex or not) all of whose sub-piece sizes are nonnegative integers in units of 1/D. Then defect(P(t*)) ≥ 1.

*Proof.* Delete zeros (D4). Strip equal pairs repeatedly (D2): the surviving multiset consists of the values w with odd multiplicity in P(t*), each surviving exactly once; list them as w_1 > w_2 > … > w_r ≥ 1 (integers). Then

  defect(P(t*)) = w_1 − w_2 + w_3 − … ± w_r,

an integer. Modulo 2, this alternating sum is ≡ w_1 + w_2 + … + w_r ≡ Σ_c n_c v_c = Σ(P) = D ≡ 1 (mod 2), because every value with even multiplicity contributes an even amount n_c v_c to the total while every value with odd multiplicity contributes n_c v_c ≡ v_c (mod 2). By Corollary D1 the defect is ≥ 0; an odd nonnegative integer is ≥ 1. ∎

**Fact 1 (structure of non-integer replies).** In any reply to g, every LB piece contains either zero or at least two sub-pieces of non-integer size. *Proof.* The sub-piece sizes of piece i sum to the integer g_i; if exactly one of them were non-integer, the sum would be non-integer. ∎

*Consequence:* every piece containing non-integer sub-pieces carries at least one XY mark, and non-integer values propagate in groups whose fractional parts sum to an integer within each piece.

**Gap E3′ (open).** It remains to prove: every VERTEX reply t* to g with at least one non-integer value v_c has defect ≥ 1. (Equivalently, combined with Lemma P and Lemma V: mindef(g) ≥ 1/D.)

Status of E3′: numerically true — a multistart Nelder–Mead minimization of the defect over ALL replies (every cut assignment, hundreds of random starts) at n = 1, 2, 3 returns exactly 1/D each time, so no fractional reply beats the integer optimum; at n = 1 it is proven by hand (cutting piece 2: the vertex options are the match (1,1) and the halving (1,1), both defect 1; cutting piece 1 leaves 2 as strict maximum and defect ≥ 2 − 1 = 1; no cut gives defect 1). Candidate repair, recorded for the next round: for a prime p dividing some denominator of v, let μ = min_c ν_p(v_c) < 0 and W = {c : ν_p(v_c) = μ}. Reducing the row equations A v = g modulo p^{−μ}-scaled units shows Σ_{c∈W} a_{i,c} · (p^{−μ} v_c mod p) ≡ 0 (mod p) for every piece i, so each piece meets W either not at all, or in ≥ 2 components, or in a single component with a_{i,c} ≡ 0 (mod p) (an equipartition into a multiple of p parts, costing ≥ p − 1 marks in that piece). Both alternatives are mark-expensive; the hope is a counting contradiction against the budget Σ m_i ≤ n using the mass-domination g_{n+1-th piece} = 2^n = (Σ of all other pieces) + 1. This is the round-2 target.

**Verification of tightness (XY side).** XY can achieve defect = 1 against g: cut the top piece 2^n into parts 2^{n−1}, 2^{n−2}, …, 2, 1, 1 (n cuts; the parts sum to 2^n). The final multiset is the pairs {2^k, 2^k}, k = 0, …, n−1, plus one extra 1; by D3 the defect is exactly 1 unit, so V(g) ≤ (1 + 1/D)/2 = 2^n/D. Hence once E3′ closes, V(g) = 2^n/D exactly and the geometric marking attains the answer.

### 6. Upper bound: mindef(q) ≤ 1/D for every q — cases (a), (b) closed, (c) open

Sort q_1 ≥ q_2 ≥ … ≥ q_{n+1} > 0, Σ = 1. Two explicit reply families:

**Reply H (halve all but the smallest).** Mark the midpoints of q_1, …, q_n (n marks, interior, distinct). Final multiset: pairs {q_i/2, q_i/2}, i ≤ n, plus q_{n+1}. By D3: defect = q_{n+1}.

**Reply F(j, r) (match a block, halve the rest), for 1 ≤ j < r ≤ n+1 with ρ_{j,r} := q_j − Σ_{i=j+1}^r q_i ≥ 0.** Cut piece q_j into consecutive parts of sizes q_{j+1}, q_{j+2}, …, q_r, ρ_{j,r} (r − j cuts if ρ_{j,r} > 0, r − j − 1 if ρ_{j,r} = 0); halve every other piece q_i, i < j or i > r (that is (j − 1) + (n + 1 − r) marks). Mark ledger: (r − j) + (j − 1) + (n + 1 − r) = n. ✓ Final multiset: pairs {q_i, q_i} for j < i ≤ r (original + copy), pairs {q_i/2, q_i/2} for the halved pieces, plus the single leftover ρ_{j,r}. By D3: defect = ρ_{j,r}.

**Chain Lemma.** Let d_j := q_j − Σ_{i=j+1}^{n+1} q_i = ρ_{j,n+1} for j = 1, …, n. It is impossible that simultaneously q_{n+1} > 1/D and d_j > 1/D for all j.

*Proof.* Suppose all these hold. We show by downward induction that q_j > 2^{n+1−j}/D for j = n+1, n, …, 1. Base: q_{n+1} > 1/D = 2^0/D. Step: if q_i > 2^{n+1−i}/D for all i > j, then

  q_j = d_j + Σ_{i>j} q_i > 1/D + (2^{n−j} + … + 2 + 1)/D = 1/D + (2^{n+1−j} − 1)/D = 2^{n+1−j}/D.

Summing, 1 = Σ_{j=1}^{n+1} q_j > (2^n + 2^{n−1} + … + 1)/D = (2^{n+1} − 1)/D = 1, a strict contradiction. ∎

**Case split for the upper bound.**
- (a) q_{n+1} ≤ 1/D: Reply H gives mindef(q) ≤ q_{n+1} ≤ 1/D. Done.
- (b) q_{n+1} > 1/D and some d_j ∈ [0, 1/D]: Reply F(j, n+1) is feasible (ρ_{j,n+1} = d_j ≥ 0) and gives mindef(q) ≤ d_j ≤ 1/D. Done.
- (c) q_{n+1} > 1/D and every d_j ∉ [0, 1/D]: by the Chain Lemma not all d_j exceed 1/D, so some d_j < 0 (the *deficient case*). **Gap E2 (open).**

Status of E2: the outline-reviewer's and outliner's computations (recorded in round 1) show the H + F family ALONE does not suffice in case (c): for n = 2, q = (0.49, 0.345, 0.165) has q_3 = 0.165 > 1/7, d_2 = 0.18 > 1/7, d_1 = −0.02 < 0, and no H/F reply reaches ≤ 1/7; but the *cascade* reply — cut q_1 into (0.345, 0.145) and q_3 into (0.145, 0.02), 2 = n marks, final multiset {0.345, 0.345, 0.145, 0.145, 0.02} — has defect 0.02 < 1/7 by D3. So case (c) needs cascade replies: chains that cut q_a into (q_b, δ_1), then some q_c into (δ_1, δ_2), etc., halving everything else, with an exact mark ledger. Closing (c) — a cascade-selection rule with a proof that some cascade's terminal remainder is ≤ 1/D whenever (c) holds, with total marks ≤ n in every branch — is the other round-2 target. (2000 random n = 2 configurations were checked in round 1: cascades always close case (c) there.)

### 7. Conclusion (conditional) and verification

Modulo Gaps E2 and E3′:

- Upper bound: for every LB play (≤ n marks), either Lemma F (fewer than n effective marks, value exactly 1/2 < 2^n/D) or cases (a)–(c) give mindef(q) ≤ 1/D, hence V(q) = (1 + mindef(q))/2 ≤ (1 + 1/D)/2 = (2^{n+1})/(2D) = 2^n/D.
- Lower bound: LB marks (2^k − 1)/D, k = 1..n; by Lemma V + Lemma P + E3′, mindef(g) ≥ 1/D; with the tightness reply of §5, V(g) = 2^n/D exactly.

Hence c(n) = 2^n/(2^{n+1} − 1).

Verification of the formula at small n: n = 1: 2/(4−1) = 2/3, matching the complete hand analysis (LB marks 1/3; pieces (1/3, 2/3); every XY reply leaves defect ≥ 1/3, and cutting 2/3 at its midpoint attains 1/3 — §5's argument at n = 1 is gap-free since E3′ is proven by hand there). n = 2: 4/7, matching the exact Fraction-arithmetic exhaustive computation of round 1 (LB marks {1/7, 3/7}). Numerical optimization confirms mindef(g) = 1/D exactly at n = 1, 2, 3.

## Open gaps
- **E2 (hard, upper bound):** deficient case (c) — construct and verify a cascade reply with terminal remainder ≤ 1/D and marks ≤ n. (Shared difficulty with pairing-defect-strategy-family's G3.)
- **E3′ (hard, lower bound):** vertex replies to g with non-integer values have defect ≥ 1 unit. Proven: integer vertices (Lemma P), n = 1 by hand; Fact 1 and the mod-p structure are partial progress. This is the distinctive discrete mechanism of this approach; the mod-p mark-cost counting is the candidate repair.
- E1 is CLOSED (Lemma V). The former "½ℤ integrality" claim is withdrawn as false (equipartition vertices have denominators ≥ 3); the corrected statement is the Remark after Lemma V.

## Cases covered
- LB with < n effective marks or endpoint/degenerate marks: Lemma F + D4.
- XY with < n marks, endpoint marks, coalesced marks: zero facets of 𝒯_m + D4 (subsumed in Lemma V).
- Ties everywhere: all statements are about multisets; strip-pairs and the sorted-pattern polytopes handle ties by construction (σ breaks ties arbitrarily, and Q_σ is closed).

## Watch out for (unchanged warnings, updated)
- defect(P(t)) IS continuous in t for a fixed number of sub-pieces (order statistics are 1-Lipschitz); the discontinuity worry of round 1 was unfounded once zeros are handled by D4 — but Odd is only piecewise linear, so minimization must still go through the closed pattern polytopes Q_σ.
- Do NOT use "vertex values are half-integers": false. Use the rank-s system A v = q (Lemma V) and treat denominators via Cramer.
- Zero slack at the geometric configuration: every inequality used near g must be exact.

## Promotable lemmas
All proved in full in this file (section references above); statements are configuration-generic and reusable by both sibling approaches:
- **Lemma C (claiming value)** — §1: first claimer's optimal value on multiset S is Odd(S). Proved by exchange induction.
- **Lemma D + D1–D4 (defect identity and calculus)** — §2: defect = λ{x : N(x) odd}; nonnegativity; strip-pairs invariance; pairs-plus-leftover formula; zero-append invariance.
- **Lemma F (fewer marks ⇒ exactly 1/2)** — §3.
- **Lemma V (best-response attainment + vertex classification)** — §4: XY's optimum is attained at a reply whose distinct positive values solve a full-rank nonnegative-integer system A v = q uniquely. (Useful to any approach wanting a finite/discrete description of XY's best replies.)
- **Chain Lemma** — §6: q_{n+1} > 1/D and all d_j > 1/D is impossible. (Also used by pairing-defect-strategy-family.)
- **Lemma P (integer-vertex parity at the geometric configuration)** — §5: any reply to g with all sizes in ℤ units has defect ≥ 1 unit.
