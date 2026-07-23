# Approach: geometric-cascade-induction

## Status
unsolved

## Target
c(n) = 2^n/(2^{n+1}-1). Both directions: (i) LB's geometric strategy guarantees ≥ 2^n/(2^{n+1}-1); (ii) against any LB placement, XY can hold LB to ≤ 2^n/(2^{n+1}-1).

## Technique
Induction on n (equivalently on the cut budget), exploiting the self-similar structure of the geometric configuration. Work in units of u = 1/D, D = 2^{n+1}-1, so LB's pieces are the integers 2^0, 2^1, ..., 2^n and the target is "LB gets ≥ 2^n units."

## Proof skeleton

### Lemma 0 (picking-phase value)
When the pieces are fixed, optimal alternating play gives the first picker exactly the sum of the odd-indexed pieces in sorted (decreasing) order: with q_1 ≥ q_2 ≥ ... ≥ q_m, first picker gets q_1 + q_3 + q_5 + ....
Mechanism: exchange/induction argument — picking the largest piece is optimal for both players since pieces have no interaction (folklore; prove by induction on m: if first picker takes q_j with j > 1, swapping to q_1 never loses). Certify this once as a shared lemma (`lemmas/`), all approaches use it.

Consequence: LB's guarantee for a final multiset M is oddsum(M) := sum of odd-ranked elements. Also oddsum(M) = (σ(M) + A(M))/2 where A = q_1 - q_2 + q_3 - ... is the alternating sorted sum.

### Part 1: Lower bound (LB plays geometric, gets ≥ 2^n u)

LB's marks at positions (2^{j+1}-1)/D, j = 0..n-1, giving pieces {1, 2, 4, ..., 2^n} (units).

Statement L(n): for the multiset G_n = {2^0,...,2^n} and ANY ≤ n cuts by XY (a cut replaces a piece p by x, p-x with 0 < x < p), oddsum ≥ 2^n.

Induction on n. Base n=0: no cuts, oddsum = 1 = 2^0. Base n=1 directly: pieces (2,1); one cut of 2 into (x,2-x) leaves 1 as median (since x + (2-x) = 2 > 1 forces one part ≥ 1 ≥ other), so oddsum = x + (2-x)... more precisely LB gets max part + third pick = 2 units exactly or more; a cut of 1 gives LB 2 + (part) > 2. Done (this is the known c(1) = 2/3 proof).

Step for n ≥ 2:
1. If XY leaves the top piece 2^n uncut, it is the unique largest final piece (all other pieces or fragments are ≤ 2^{n-1} < 2^n), so LB's first pick alone is 2^n. Done. — by Lemma 0.
2. So assume XY spends j ≥ 1 cuts on the piece 2^n, splitting it into fragments P = {b_1 ≥ ... ≥ b_{j+1}}, Σb_i = 2^n, and ≤ n - j cuts on the rest, turning G_{n-1} into Q.
3. **Merge Lemma (GAP 1, even case):** if |P| is even, oddsum(P ∪ Q) ≥ σ(P)/2 + oddsum(Q).
   Then oddsum ≥ 2^{n-1} + L(n-1) [Q is G_{n-1} with ≤ n-j ≤ n-1 cuts] = 2^{n-1} + 2^{n-1} = 2^n. Done for j odd.
   Evidence for the even Merge Lemma (all verified by hand): P=(2,2),Q=(2,1): 4 = 2+2 (eq); P=(1,1),Q=(10): 11 = 1+10 (eq); P=(4,4),Q=(5,1): 9 = 4+5 (eq); P=(6,2),Q=(5,3): 9 = 4+5 (eq); several strict cases hold. Suspected proof: pair the elements of P in sorted order (b_1,b_2),(b_3,b_4),...; each pair contributes ≥ (b_{2i-1}+b_{2i})/2·... via a rank-tracking argument: inserting an equalized pair into any sorted list changes oddsum by exactly the pair value's half-sum... needs care; this is the load-bearing gap.
4. **Odd |P| case (GAP 2):** when j is even (so |P| = j+1 odd, j ≥ 2), the naive move (peel off the smallest fragment b, apply monotonicity oddsum(M ∪ {b}) ≥ oddsum(M), then the even Merge Lemma) loses b/2 and is NOT sufficient: e.g. n=3, P=(3,3,2), Q_worst=(2,2,2,1) has oddsum(P∪Q) = 8 exactly, while the naive bound gives 8 - b/2 = 7. The compensating slack must come from Q having only ≤ n-j ≤ n-2 cuts. Recorded minima for G_m with c cuts (units): G_3: c=0→10, c=1→9, c=2→8, c=3→8. So L(m,c) := min oddsum of G_m under ≤ c cuts satisfies L(3,1) = 9 = 2^3+1, i.e. one unit of surplus per unspent cut at first, saturating at 2^m. Candidate strengthened induction: L(m,c) ≥ 2^m + max(0, δ(m,c)) with δ capturing the surplus; find the right δ and redo step 3-4 with it. This closes the odd case IF the surplus ≥ b/2 - (loss in merge). Builder: first compute L(m,c) exactly for m ≤ 4, all c, by exact search over tie-breakpoint cut positions, then guess-and-prove δ.
5. **Monotonicity Lemma (GAP 3, easy):** oddsum(M ∪ {x}) ≥ oddsum(M) for any x > 0 — adding a piece never hurts the first picker. Mechanism: inserting x at rank r shifts subsequent parities; compare pick-by-pick (LB can imitate its old strategy). Needed as glue in step 4.

### Part 2: Upper bound (XY response to arbitrary LB placement)

Statement U(k,m): for any k pieces p_1 ≥ ... ≥ p_k with sum σ, k ≤ m+1, XY with m cuts can reach a final multiset consisting of **equal pairs plus at most one leftover r** with r ≤ σ/(2^{m+1}-1).

**Pairs Lemma (easy, prove first):** if M = {a_1,a_1, a_2,a_2, ..., a_t,a_t} ∪ {r}, then oddsum(M) ≤ (σ(M)+r)/2. Mechanism: in the sorted list, each equal pair contributes exactly one element to the odd ranks regardless of where r falls (ties broken arbitrarily, both orders give the same oddsum), so LB gets Σa_i + (r or 0).

Given U(n+1, n) applied to LB's ≤ n+1 pieces: LB ≤ (1 + r)/2 ≤ (1 + 1/D)/2 = 2^n/D. Done.

Proof of U by induction on m:
- Base m=0: k=1, no cuts, r = σ ≤ σ/(2^1-1). ✓ (equality — this is why the bound is what it is.)
- Spare-cut trick: if k ≤ m, XY can finish pairing with ≤ k-1 cuts and use one spare cut to split the final leftover exactly in half (making it a pair), so r = 0 and LB ≤ σ/2. This handles LB using fewer than n marks, and any branch that generates a free pair (two equal pieces pair without a cut).
- Case A (top piece large): p_1 ≥ 2^m σ/(2^{m+1}-1). XY halves p_1 (one cut, creates a pair p_1/2,p_1/2), recurses on the remaining k-1 ≤ m pieces with m-1 cuts, sum σ-p_1 ≤ σ(2^m-1)/(2^{m+1}-1): induction gives r ≤ (σ-p_1)/(2^m-1) ≤ σ/(2^{m+1}-1). ✓ (Verified arithmetic.)
- Case B (p_2 large): p_2 ≥ 2^{m-1}σ/(2^{m+1}-1). XY cuts p_1 into (p_2, p_1-p_2), pairing p_2; the leftover p_1-p_2 rejoins the pool: k-1 pieces, m-1 cuts, sum σ-2p_2: induction gives r ≤ (σ-2p_2)/(2^m-1) ≤ σ/(2^{m+1}-1). ✓ (Verified arithmetic: reduces to p_2 ≥ 2^{m-1}σ/(2^{m+1}-1).)
- **Case C (GAP 4 — the hard case): p_1 < 2^m σ/(2^{m+1}-1) AND p_2 < 2^{m-1}σ/(2^{m+1}-1).** Neither branch's arithmetic closes. Concrete stress test: pieces (0.45, 0.15, 0.1, 0.1, 0.1, 0.1), m=5: greedy pairing chains leftovers 0.30, 0.20, 0.10, then the pool (0.1,0.1,0.1) yields a FREE pair, freeing a spare cut, so actually r = 0 — the greedy process succeeds even though the inductive bound σ/(2^m-1) fails at intermediate steps. So the fix is a **stronger induction hypothesis** that tracks more than σ (e.g. "r ≤ σ/(2^{m+1}-1) OR a free pair/spare cut arises downstream", or a potential like r ≤ max(0, 2p_1 - σ) combined with the σ-bound). Builder: run the greedy pairing process symbolically/numerically over many random and adversarial configs to find the true invariant, then prove it.

## Key lemmas (claim + mechanism)
- Lemma 0 (oddsum value) — exchange argument on picks; shared across approaches.
- Pairs Lemma — equal pairs contribute exactly one element each to odd ranks.
- Merge Lemma (even |P|) — pairing fragments in sorted order preserves half their mass into LB's odd ranks. GAP.
- Surplus function L(m,c) for under-budget XY — one unit of surplus per unspent cut near c = m. GAP.
- U(k,m) hard case — needs strengthened invariant; free-pair bonus is the rescue mechanism. GAP.

## Open gaps
GAP 1 (Merge Lemma even case), GAP 2 (odd fragment count / surplus bookkeeping), GAP 3 (monotonicity — easy), GAP 4 (upper-bound hard case invariant).

## Cases to cover
Lower: XY cuts / doesn't cut top piece; j odd vs j even. Upper: cases A/B/C plus spare-cut and free-pair branches; LB using < n marks; LB making equal pieces.

## Watch out for
- Zero-length pieces are impossible (marks distinct) but XY can shave arbitrarily small slivers — no bound may assume a minimum piece size.
- Ties in the sorted order: check that oddsum is well-defined under ties (it is — any tie-breaking gives the same value; state this).
- "XY halves a piece exactly" is legal (only marks must be distinct points).
- The upper bound must hold for EVERY LB placement including k < n+1 pieces.
