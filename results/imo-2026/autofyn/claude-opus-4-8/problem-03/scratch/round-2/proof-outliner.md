## imo-2026-03

Answer to prove (all three approaches): **c(n) = 2^n / (2^{n+1} − 1) = 1/(2 − 2^{-n})**,
D := 2^{n+1} − 1. Verified numerically n=1..4 by both explorers. Recursion
c(n) = 2c(n−1)/(2c(n−1)+1), i.e. 1/c(n) = 2 − 2^{-n}.

Shared reduction (all approaches, one shared lemma **G1**): once cuts are fixed, the
alternating claim-to-maximize game is won by greedy-largest for BOTH players, so LB's
total = sum of odd-ranked pieces. Certify G1 once, import everywhere.

Field of three FAR-APART framings:

---

direct-constructive: new
Target: the full claim — state answer, prove LB guarantees ≥ c(n), prove XY forces ≤ c(n).
Technique: explicit strategies both sides + exchange argument; dominance invariant (LB)
  and interleaving-plus-halving response (XY). Constructive/extremal spine.
Skeleton:
  1. Claiming phase = odd-ranked pieces — greedy optimality (exchange argument). [G1]
  2. LB marks (2^k−1)/D → pieces P_j=2^j/D; dominance identity P_j = Σ_{i<j}P_i + 1/D.
  3. LB lower bound: any ≤ n XY cuts keep odd-sum ≥ 2^n/D. Easy sub-case (XY spares P_n
     ⇒ q_1=P_n ⇒ done); hard sub-case (XY cuts P_n ⇒ interleaving-optimality gives
     odd-sum = P_n). [G2]
  4. XY upper bound vs ANY LB marking: interleave a_1 (when a_1>Σ smaller) to force
     odd-sum=a_1, plus halving the top piece with spare marks; minimax value = 2^n/D. [G3]
  5. Assemble the two bounds and verify n=1,2.
Key lemmas: greedy=odd-ranked (exchange); dominance identity P_j−Σ_{i<j}P_i=1/D>0 is the
  saddle-point fact; interleaving lemma (owner of B>ΣS forces claimer to get exactly B).
Open gaps: G1 (greedy optimality), G2 (LB invariant under XY cuts of P_n — the charging/
  interleaving-optimality bound), G3 (all-strategies XY upper bound — hardest, global).
Cases to cover: G2 {cuts in P_n / spread / <n marks}; G3 {a_1>1/2 vs a_1≤1/2}; base n=1,2.
Watch out for: easy sub-case masking the real content; a_1=Σsmaller boundary; ε→0 limits
  (sup not attained, value is the infimum 2^n/D); distinctness of marks.

induction-recursion: new
Target: the full claim, by induction on n.
Technique: induction on n driven by c(n)=2c(n−1)/(2c(n−1)+1) (r(n)=1+r(n−1)/2); decompose
  the game at the big-piece boundary into a renormalized (n−1)-subgame.
Skeleton:
  1. Recursion ⇒ closed form r(n)=2−2^{-n} ⇒ c(n)=2^n/D; base c(0)=1. [airtight]
  2. Reduction move: isolate one geometric level; opponent cuts dominant remainder once;
     one-step minimax is the Möbius map v↦2v/(2v+1). [H2 game-separation lemma]
  3. LB lower bound by induction (isolate P_0=1/D, play scaled (n−1)-strategy on remainder).
  4. XY upper bound by induction (first mark neutralizes LB's largest piece → (n−1)-game).
  5. Sandwich at recursion value; evaluate.
Key lemmas: recursion identity (Möbius iterate = 2−2^{-n}); GAME-SEPARATION lemma H2 — the
  sorted-order claiming game splits across the boundary because geometric spacing prevents
  value-changing cross-boundary interleaving (the true crux; naive induction fails here);
  threshold-indifference pins the fixed point.
Open gaps: H2/H3a/H3b — legitimize "reduce to (n−1) subgame" despite the globally coupled
  claiming phase; shared G1.
Cases to cover: base n=0,1 explicit; inductive step {XY attacks isolated piece / remainder
  / splits marks across boundary — last must be shown suboptimal}.
Watch out for: single-gap trap (if H2 false, both inductions die); verify H2 on n=2 by hand
  before trusting; sub-strategy scaling (remainder length ≠ 1); do not assert separability.

potential-duality: new
Target: the full claim, certifying the game value with one potential Φ.
Technique: LP-duality / monovariant — find Φ(pieces, remaining marks) that upper-bounds
  under XY play and lower-bounds under LB play, meeting at c(n) (complementary slackness =
  the threshold-indifference). Object is an invariant, not a strategy.
Skeleton:
  1. Reduce to odd-ranked (shared G1).
  2. Define Φ: weighted truncated top-sum on the dyadic ladder 1,2,…,2^n over D; Φ(start)=c(n).
     [P2 — exact closed form is the whole game]
  3. XY monovariant: Φ nonincreasing under XY's optimal cut, held ≤ 2^n/D. [P3a]
  4. LB monovariant: Φ ≥ 2^n/D, no XY cut drops it below. [P3b]
  5. Bounds coincide ⇒ c(n)=2^n/D; cross-check Φ on exact n=1,2,3 positions.
Key lemmas: value-certifying potential exists (finite zero-sum) — content is its closed
  form; dyadic-redistribution identity v↦2v/(2v+1) as a monovariant step; complementary
  slackness = threshold-indifference.
Open gaps: P2 (explicit Φ — high risk of vacuity), P3a/P3b (monovariant inequalities), G1.
Cases to cover: FALSIFY Φ on n=1,2,3 first; cuts of non-top pieces.
Watch out for: "value function exists by backward induction" is true but worthless without
  the closed form — this approach earns its keep only if P2 is explicit and passes n≤3.
  Keep weights vs lengths distinct; Φ must reduce to true odd-sum at terminals.

---

Recommendation to the reviewer: register all three as the initial population (first round,
empty workspace — maximal breadth wanted). They are genuinely far apart: constructive
strategy-exhibition, induction-on-n via the recursion, and a duality/potential certificate.
G1 (greedy=odd-ranked) is common infrastructure — worth certifying early as a shared lemma.
Highest-value near-term build targets: direct-constructive (G2 lower-bound invariant is the
most self-contained real result) and induction-recursion (test H2 on n=2 to decide if the
recursion is a genuine spine or a coincidence). potential-duality is the riskiest; gate it on
the n≤3 falsification check for Φ before heavy investment.

build set: direct-constructive, induction-recursion, potential-duality
