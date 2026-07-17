## imo-2026-03

Answer: c(n) = 2^n/(2^{n+1}−1), D = 2^{n+1}−1. Reduction settled (G1, R1/R2 certified). The
field-wide wall has shrunk this round: the upper bound U1 now splits cleanly into Case A
(CLOSED via new Lemma H) and Case B (all LB pieces > 1/D — the remaining hard core). The
three approaches below hit Case B (and the lower bound) from three genuinely different
framings so the field does not collapse to one wall.

---

direct-constructive: revise (leader; L1/L2 re-planned, U1 Case A closed, Case B flagged)
Target: c(n) = 2^n/(2^{n+1}−1) end to end — LB guarantees ≥ c(n) AND XY holds LB ≤ c(n).
Technique: explicit optimal strategies for both players (constructive), on the odd-sum
marking game (G1). Distinct route: exhibit the strategies and prove each bound directly.
Skeleton:
  1. Reduce to odd-sum marking game — Lemma G1 (certified).
  2. O = 1/2 + ½·μ{N odd}; targets μ{N odd} ≷ 1/D — Lemma R2 (certified).
  3. LB geometric marks P_j = 2^j/D + dominance identity P_j − Σ_{i<j}P_i = 1/D (certified).
  4. Lower bound: §4.1 easy case (XY spares R_n ⟹ O ≥ 2^n/D) DONE; §4.2 confined case via
     L1 + L2.
  5. Upper bound: Case A (Lemma H) DONE; Case B (GAP U1).
Key lemmas (claim + mechanism):
  - L1 (confined Fragments Lemma, O ≥ 2^n) — because interleaving is the GLOBAL MIN:
    O = ΣF = 2^n exactly on the interleaving region, and every boundary crossing raises O by
    ΔO = I_k − f_j > 0; cut-count k ≤ n forces the min to be exactly 2^n. DROP the circular
    integral ∫⌊(N_F−N_I)/2⌋dt (it equals 2^n − O identically — a rename, not a reduction).
  - L2 (confine XY cuts to R_n) — because moving a cut from R_j (j<n) into R_n weakly
    lowers O for XY: a cut in R_j makes two ≤ P_j/2 pieces that only push intacts to odd
    ranks (helps LB), whereas the same cut in R_n fragments the dominant piece (helps XY).
  - Lemma H (halve n largest ⟹ O = 1/2 + a_{n+1}/2) — because each halved pair contributes
    0 to the alternating sum and the spared smallest piece lands at an odd rank; so O ≤ c(n)
    ⟺ a_{n+1} ≤ 1/D. This CLOSES Case A.
Open gaps: L1 (builder writes the boundary-crossing / induction-on-k proof; hard sub-step =
splitting a middle odd-ranked fragment — use dyadic gaps), L2 (exchange argument), U1 =
CASE B ONLY (all pieces > 1/D; sub-case B2 with a_1 ≤ 1/2 is the genuine difficulty).
Cases to cover: L1 base k=0 (done §4.1); U1 Case A (done, Lemma H); Case B sub-cases B0
(n=1 vacuous), B1 (a_1 > 1/2, Lemma I), B2 (a_1 ≤ 1/2, open).
Watch out for: the circular integral (do not revive it); the k ≤ n cut-count bound is
load-bearing in L1 (k=n+1 breaks it); the ε→0 supremum limit in Lemma I.

---

extremal-config: new (config-space saddle / concavity — attacks Case B without a strategy)
Target: c(n) = 2^n/(2^{n+1}−1) end to end, via one extremal analysis giving BOTH bounds.
Technique: extremal principle + concavity. Study g(a) = min_XY O(a,XY) over the LB
piece-vector simplex; c(n) = max_a g(a). Show the max is the geometric config a*, value
c(n). Genuinely different: no per-config XY strategy — the upper bound (incl. Case B) is
"no LB config beats g(a*)".
Skeleton:
  1. c(n) = max_a g(a) — Lemma G1 (certified).
  2. g(a*) = c(n): XY all-cuts-in-P_n forces O = P_n = c(n) (Lemma I); lower side from
     L1/L2 or step 4.
  3. Lemma E1: g is CONCAVE on the simplex (O linear in a per fixed cut-pattern; g = min of
     these). RUN NUMERICAL CONCAVITY CHECK FIRST (kill-switch).
  4. Lemma E2: the interior stationary point of concave g is a* — the dominance identity
     P_j − Σ_{i<j}P_i = 1/D IS the KKT/equal-marginal condition (dual certificate).
  5. max_a g(a) = g(a*) = c(n); both bounds follow.
Key lemmas (claim + mechanism):
  - E1 (concavity of g) — because for each fixed cut-pattern O is piecewise-linear in a, and
    g is a min over patterns; load-bearing, test numerically before proving.
  - E2 (stationary point = geometric) — because equal marginal gain 1/D across dyadic-ladder
    rungs holds exactly at a* (dominance identity = complementary slackness / threshold
    indifference).
Open gaps: E1 (HIGH RISK — concavity; if only cellwise, fall back to a smoothing exchange
moving length toward a*), E2 (KKT computation), E3 lower side (import L1/L2).
Cases to cover: numerical concavity check n=2,3,4 (kill-switch); simplex boundary (some
a_i = 0, fewer pieces); max is interior not on boundary.
Watch out for: VACUITY — if concavity is not an independent structural fact, "max at a*"
= U1 renamed (same wall); the whole worth is E1 proved independently. g is NOT Schur-concave
(vertex {1,0,…} gives 1/2) — the max is a genuine interior saddle.

---

amortized-parity: new (sequential-cut monovariant with amortized budget — third framing)
Target: c(n) = 2^n/(2^{n+1}−1) end to end; distinct spine is the UPPER bound.
Technique: monovariant + amortized potential (aimo-0019 "linear potential bounds cumulative
resource"). Target Ψ := μ{N odd} ≤ 1/D (via certified R2). XY places n cuts sequentially by
a greedy rule; an amortized argument shows n cuts drive Ψ ≤ 1/D — uniform over Case A/B, no
case split.
Skeleton:
  1. Ψ = μ{N odd}, goal Ψ ≤ 1/D — Lemma R2 (certified).
  2. Per-cut change formula ΔΨ ∈ [−2L_min, +L_min] (Lemma A1).
  3. Greedy rule: cut across the largest current odd-N region (both sub-intervals flip
     odd→even).
  4. Amortized bound (Lemma A2): each cut removes at least its fair share of the excess
     (Ψ − 1/D); N(0) ≤ n+1 and dyadic gaps floor the per-cut removal ⟹ n cuts suffice.
  5. Möbius-map cross-check (A3): v ↦ 2v/(2v+1), n iterates reach 2^n/D — confirms budget.
Key lemmas (claim + mechanism):
  - A1 (per-cut formula) — a cut flips N by 1 on its two sub-intervals; Ψ counts odd-parity
    measure. Routine from R1/R2.
  - A2 (greedy amortized sufficiency) — LOAD-BEARING; because ≤ n+1 initial pieces bound
    N(0) and dyadic gaps prevent odd regions smaller than the per-mark decrement (amortized,
    NOT per-cut — the explorer showed no uniform per-cut bound exists).
Open gaps: A2 (HIGH RISK; the Case-B wall attacked via amortized accounting). Lower bound
imported from direct-constructive (L1/L2).
Cases to cover: greedy numerical sufficiency test n=2,3,4 (falsification, do first);
dominant vs non-dominant a_1 handled uniformly; already-satisfying config (XY passes).
Watch out for: SAME-WALL risk — if A2 degrades to per-config checking it renames U1; keep
it a genuine linear-potential argument. Handle the ε→0 open-cut supremum.

---

### Notes for the outline-reviewer

- The wall genuinely moved this round: Lemma H closes Case A of the upper bound
  unconditionally, so U1 has shrunk to Case B (all LB pieces > 1/D). L1 dropped the circular
  integral for the boundary-crossing route; L2 has a concrete exchange argument.
- Anti-collapse: three DIFFERENT framings now hit Case B — constructive strategy
  (direct-constructive), config-space concavity/saddle (extremal-config), amortized
  monovariant (amortized-parity). Both new approaches carry an explicit NUMERICAL
  KILL-SWITCH (concavity of g; greedy sufficiency) so a builder can abandon fast if the
  distinct mechanism is false, rather than burning a round on a rename.
- Do NOT revive induction-recursion (n→n−1 separation refuted). potential-duality stays
  parked (its Φ collapses to L1/U1 by another name — the fresh-framing explorer confirmed).
- Recommended build set emphasis: advance direct-constructive (close L1, L2, and Lemma H /
  Case A which are ready to write), and build ONE of the new upper-bound framings after its
  kill-switch check — extremal-config is the more distinct (both bounds from one argument);
  amortized-parity is the backup framing on the wall.

build set: direct-constructive, extremal-config, amortized-parity
