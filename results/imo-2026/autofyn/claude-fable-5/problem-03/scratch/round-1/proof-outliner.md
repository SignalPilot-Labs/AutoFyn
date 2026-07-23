## imo-2026-03

Answer targeted by all approaches: c(n) = 2^n/(2^{n+1}-1). Notation: D = 2^{n+1}-1, unit u = 1/D; LB's geometric pieces = {1, 2, 4, ..., 2^n} in units; picking-phase value = oddsum (sum of odd-ranked sorted pieces) = (σ + A)/2 where A = alternating sorted sum. Both bounds are equivalent to statements about A: lower bound ⟺ "A ≥ 1 unit vs geometric", upper bound ⟺ "XY forces A ≤ 1 unit vs any LB".

Shared Lemma 0 (certify once in lemmas/): optimal alternating picking from a fixed multiset gives the first picker exactly the odd-ranked sorted sum — exchange argument. Every approach needs it; the first builder to prove it should file it as a shared lemma. Same for the Pairs Lemma (equal pairs + leftover r ⟹ LB ≤ (σ+r)/2).

geometric-cascade-induction: new
Target: c(n) = 2^n/(2^{n+1}-1) — lower bound (geometric strategy survives any ≤ n cuts) and upper bound (XY pairing recursion vs any LB placement).
Technique: induction on n / cut budget, exploiting self-similarity of {1,2,...,2^n}.
Skeleton:
  1. Lemma 0 (oddsum value) — exchange argument.
  2. Lower: if XY leaves 2^n uncut, LB's first pick alone is 2^n u ≥ c(n) — greedy.
  3. Lower: if XY spends j ≥ 1 cuts on 2^n, apply Merge Lemma (|fragments| even: oddsum(P∪Q) ≥ σ(P)/2 + oddsum(Q)) + induction L(n-1) on the rest — telescopes to exactly 2^n u.
  4. Lower: odd fragment count handled via surplus of under-budget sub-game L(m,c) (computed: L(3,c) = 10,9,8,8 for c=0..3 — one unit of surplus per unspent cut, saturating).
  5. Upper: Pairs Lemma; XY induction U(k,m): k ≤ m+1 pieces, m cuts ⟹ pairs + leftover r ≤ σ/(2^{m+1}-1); branches: halve (closes iff p_1 ≥ 2^mσ/D_m), match (closes iff p_2 ≥ 2^{m-1}σ/D_m), spare-cut trick (k ≤ m ⟹ r = 0).
Key lemmas (claim + mechanism):
  - Merge Lemma — pairing the fragments of one piece in sorted order feeds exactly half their mass into LB's odd ranks (verified on 6+ hand cases, equality at cascade).
  - U(k,m) leftover bound — subtractive descent; geometric is the slowest-shrinking chain (equality case).
Open gaps: GAP 1 Merge Lemma proof; GAP 2 odd-fragment/surplus bookkeeping (test data recorded in file); GAP 3 monotonicity (easy); GAP 4 upper-bound hard case (p_1, p_2 both below thresholds — stress test recorded showing free-pair rescue; needs strengthened invariant).
Cases to cover: top piece cut/uncut; j odd/even; upper branches A/B/C + spare cut; LB with < n marks.
Watch out for: slivers (no minimum piece size); tie-breaking in sorted order; exact halving is legal.

parity-alternating-sum: new
Target: c(n) = 2^n/(2^{n+1}-1) — lower bound by parity, upper bound by response averaging.
Technique: alternating-sum reformulation; integer-lattice rounding + parity (lower); convex combination of explicit XY responses dominating on the simplex (upper).
Skeleton:
  1. LB-value = (1+A)/2; both bounds ⟺ A vs 1 unit — algebra + Lemma 0.
  2. Lower, parity: if all pieces are integers in units u, A ≡ σ = D ≡ 1 (mod 2) and A ≥ 0, so A ≥ 1 — parity of alternating vs plain sum.
  3. Lower, Rounding Lemma: some optimal XY response uses only integer cut points and never cuts the unit piece — oddsum is piecewise linear in each cut coordinate, so optima sit at tie breakpoints; tie systems have interval (totally unimodular) constraint matrices with integer RHS ⟹ integral vertices.
  4. Upper: explicit family R_j (cascade-j then telescoping pairing); LBvalue(R_j)(p) piecewise linear; find weights w_j with Σ w_j LBvalue(R_j) ≤ c(n) on the whole simplex, tight only at geometric (XY-optima multiplicity at the saddle point, verified numerically by explorers).
Key lemmas (claim + mechanism):
  - Parity forces A ≥ 1 — because the total D = 2^{n+1}-1 is odd and integer alternating sums preserve parity of the total. This "explains" why every optimal XY response lands exactly on c(n).
  - Rounding — piecewise linearity + total unimodularity of tie constraints.
Open gaps: GAP A Rounding Lemma (including "never cut the unit piece"); GAP A' rounding must use the budget ≤ n (parity is FALSE for > n cuts — e.g. halving the unit piece); GAP B existence of averaging weights (do n = 1, 2 by hand first).
Cases to cover: sliver limits; cuts in unit piece; k < n+1; simplex vertex check for (*).
Watch out for: never quote parity without the cut budget; infima vs attained minima.

pairing-exchange-normal-form: new
Target: c(n) = 2^n/(2^{n+1}-1) — lower bound by normalizing XY to tie normal form + enumeration; upper bound by XY's greedy pairing algorithm.
Technique: exchange/smoothing arguments; superincreasing (distinct-subset-sum) rigidity of powers of 2; subtractive-Euclid descent for the leftover.
Skeleton:
  1. Lemma 0 + Pairs Lemma — shared.
  2. Lower: Normalization — every optimal cut is at a tie or deletable (piecewise linearity, slide to breakpoint).
  3. Lower: enumerate tie patterns over {1,...,2^n}: distinct subset sums of powers of 2 force cascade-type patterns; all normal forms give oddsum ≥ 2^n, minimum attained by cascade halving.
  4. Upper: greedy pairing (free pair / halve if L ≥ 2S / match cut L→(S, L-S)); ≤ n cuts always suffice to reach pairs + leftover r; LB ≤ (1+r)/2.
  5. Upper: Leftover Lemma r ≤ 1/D (equality exactly at geometric); spare cut ⟹ r = 0.
Key lemmas (claim + mechanism):
  - Tie-pattern rigidity — fragments can only copy existing sizes; powers of 2 have distinct subset sums, pinning the patterns.
  - Leftover Lemma — geometric chain 2^n → 2^{n-1} → ... → 1 is the extremal (slowest) subtractive descent; free pairs yield spare cuts yield r = 0.
Open gaps: GAP I normalization; GAP II exhaustive tie-pattern enumeration (do n ≤ 4 by exact computation first); GAP III leftover invariant — same difficulty as GAP 4 of geometric-cascade-induction; whoever cracks it first certifies it as a shared lemma.
Cases to cover: deletable slivers; unit-piece cuts; free-pair/spare-cut branches; k < n+1.
Watch out for: lower bound must cover ALL XY responses (normal form must be WLOG, not assumed); enumeration must be provably exhaustive.

Notes for the reviewer:
- All three are new (round 1, empty population). Files written to results/imo-2026-03/approaches/.
- Deliberate risk spread: the two upper-bound mechanisms differ (pairing recursion vs response averaging) and the three lower-bound mechanisms differ (merge-induction vs parity/rounding vs tie enumeration). Residual overlap: GAP III ≈ GAP 4 (the leftover invariant) is shared between slugs 1 and 3 — parity-alternating-sum is the hedge, since its upper bound avoids that invariant entirely.
- The parity mechanism (slug 2, lower) is in my judgment the most likely single move to crack the problem cleanly; the pairing algorithm (slug 3, upper) is the most concrete. A plausible eventual proof = slug 2 lower + slug 3 upper; keep both alive.
- Cheap kills rejected: pointwise rank bounds (q_{2i-1} ≤ 2^{n-i}u) are FALSE — counterexample n=3: 8→(3,3,2), 4→(2,2) gives q_1 = 3 < 4 yet oddsum = 8; only aggregate arguments can work. Equal-piece LB placements are dead (recorded by explorers).

build set suggestion: all three (each has independent first gaps a builder can attack: Lemma 0 + Pairs Lemma certification, small-n exact enumerations, and the n = 1, 2 hand cases of the averaging inequality).
