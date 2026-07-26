## imo-2026-03 — lens: LIFT THE LOWER BOUND TO GENERAL n (L(4), L(5), inductive step)

### HEADLINE RESULTS (this round's computations)

1. **L(4) over reals is CERTIFIED (this round)** via the cell-complex vertex enumeration. Exact-rational, reproducible (`/tmp/round-5/n4_verify.py`):
   - Level-4 dyadic `(1,2,4,8,16)/31`, 4 Xiang marks → 9 sub-pieces, 5 sum-constraints, DoF = 9−5 = 4 (need 4-tuples, NOT triples — the n=3 proof used triples because DoF=3).
   - 70 distributions × C(45,4)=148995 4-tuples = **10,429,650 total 4-tuples**.
   - Float pass (138s): 839,787 feasible vertices; 6,008 candidates with A ≤ 1+eps collected.
   - **Exact Fraction verification (0.7s)**: all 6,008 candidates feasible, **12 distinct piece-multisets**, **min A = 1** (= α(4)·D(4) = 1/31 real), **0 EXACT VIOLATIONS**.
   - Equality multiset: the **pair-pile family** `(8,8,4,4,2,2,1,1,1)/31` (ks=(0,0,0,0,4), all 4 marks in the largest piece) — exactly the level-4 pair-pile, the conjectured equality case.
   - This is the **third lower-bound data point** (n=1,2,3,4 all certified over reals). The vertex-principle lemma (`lemma-vertex-principle-advantage.md`) applies for every fixed n; the enumeration is the per-n certificate.

2. **n=5 cell enumeration is INFEASIBLE by brute force.** Level-5 dyadic `(1,2,4,8,16,32)/63`, 5 marks → 11 sub-pieces, 6 sum-constraints, DoF=5 (need 5-tuples). Hyperplanes: E=C(11,2)=55, Z=11, total 66. 5-tuples per distribution = C(66,5) = 9,865,440. Distributions = C(10,5) = 252. **Total 5-tuples = 2.49 BILLION**. At the measured n=4 rate (75k 4-tuples/s, with 9×9 solves; 11×11 solves will be slower ≈40k/s) → ≈17 hours single-threaded, ≈75 min on 14 cores — exceeds the round budget. **n=5 cannot be closed by raw enumeration; the general-n lift MUST come from a structural/inductive argument, not enumeration.** n=4 is the last reachable enumeration data point.

### CRITICAL BUG FOUND IN A CERTIFIED LEMMA (outliner/builder must fix before relying on it)

3. **`lemmas/lemma-superincreasing-R.md` corollary "σ ≤ M/2 = a_1" is FALSE for k ≥ 2.** The corollary claims `m_1 ≥ M/2` ("largest of k+1 ≥ 2 pieces summing to M"). This is TRUE only when k+1 = 2 (k=1). For k ≥ 2 (the k≥2 sub-case the lever is supposed to address), m_1 is just the max of k+1 pieces, so `m_1 ≥ M/(k+1)`, NOT `m_1 ≥ M/2`. Verified at n=3 unrefined-R (k=3, M=8): **998,642 / 2,000,000 exact configs have σ = m_2+m_3+m_4 > 4 = a_1** (≈50%). The obstruction-magnitude bound `Σ_MM m_even ≤ σ ≤ a_1` is invalid for the sub-case it targets.

4. **`lemmas/lemma-L3-unrefined-R-subcase.md` proof is INVALID** (the result still holds numerically — 0 violations, 2M exact samples, min A = 1 — but the PROOF is unsound). The proof's setup treats `m_1` as the global rank-1 piece (merging only `{m_2,m_3,m_4}` with R, deriving `A = 7 − 2(s_3+s_5)`). This requires `m_1 ≥ a_1 = M/2 = 4`, which FAILS for 50% of configs (e.g. `m=(3,3,1,1)` has m_1=3 < 4; the true merged sort is `(4,3,3,2,1,1,1)` with A = 3, not the formula's `-1`). The proof's Case I ("t_2 > 2 ⇒ σ > 4, impossible") is also broken: σ > 4 IS possible (e.g. σ=5). **The certified L(3) result itself is rescued by the INDEPENDENT cell-complex-l3 vertex enumeration** (re-verified this round's methodology), which handles all configs uniformly. But the pairing-partner unrefined-R proof needs re-working with an m_1-split before it can support the general-n inductive lift.

### THE m_1-SPLIT (the structural insight the proof missed)

5. The unrefined-R sub-case has TWO structurally distinct branches, and the Hall conjecture applies to only one:
   - **Branch 1 (m_1 ≥ a_1 = M/2)**: m_1 is global rank 1. Merge `{m_2,…,m_{n+2}}` with R; s_1 = a_1. The pairing-partner Hall conjecture `s_3+s_5+…+s_{2n+1} ≤ a_2+…+a_{n+1}` lives here. Verified n=1..5 (slack ≥ 0, = 0 at staircase interleaving). Frequency: 75% (n=1), 50% (n=2), 31% (n=3), 19% (n=4), 11% (n=5) — the branch shrinks as n grows (since m_1 ≥ M/2 gets rarer with more sub-pieces).
   - **Branch 2 (m_1 < a_1)**: a_1 = R_largest is global rank 1 (Liu's, +a_1). All M-sub-pieces are < a_1, so they sit below a_1 in the merged sort. Numerically this branch is STRICTLY EASIER: min A exceeds α(n) by a growing margin (n=3: min A = 0.0667 = α; n=4: 0.0177 vs α=0.0159; n=5: 0.0147 vs α=0.0079). No analytic proof yet — but the margin suggests a simple argument exists (a_1 contributing at odd rank gives Liu a "free" a_1, and the rest is bounded by total_R − a_1).
   - The pairing-partner approach CONFLATED these two branches; the cell-complex approach handles both uniformly (hence its robustness). **Any inductive-lift proof MUST split on m_1 ≥ a_1 vs m_1 < a_1.**

### Distinct openings (for the outliner)

- **(O1) Cell-complex per-n certification + structural characterization of arrangement vertices.** L(4) certified this round (10.4M 4-tuples, 0 violations, pair-pile equality). The vertex-principle is general-n; the bottleneck is enumeration growth (n=5 infeasible). The lever: characterize the arrangement vertices STRUCTURALLY — every n=3,4 minimizer is the pair-pile family `(2^n,2^n,2^{n-1},2^{n-1},…,2,2,1,…,1)/D(n)` + degenerations with one zero piece. If one proves "every level-n arrangement vertex with A = α(n) is the pair-pile family, and all others have A > α(n)" by a rank-parity / dyadic-level argument on the merged sort, the general-n lift follows without enumeration. This is the cell-complex route's natural inductive target.
- **(O2) Fix the pairing-partner superincreasing-R lever with the m_1-split.** The Hall conjecture on rank indices is verified n=1..5 for Branch 1 (m_1 ≥ a_1). Prove it analytically: the superincreasing gap `a_j − Σ_{l>j} a_l = α(n+1)` IS genuine and certified; the issue is only the false corollary. A corrected proof splits on m_1 ≥ a_1 (Hall matching on the merge of `{m_2,…}` with R) vs m_1 < a_1 (a_1 at rank 1, simpler bound). The Hall matching is on RANK INDICES (per-position bound `s_{2j} ≤ a_{j+1}` FAILS — counterexample `b=(4/3,4/3,4/3)` at n=2; layer-cake too strong) — so a genuine Hall/marriage argument (distinct dyadic levels) is needed, not termwise dominance.
- **(O3) The m_1 < a_1 branch as a separate cheap lemma.** Numerically min A exceeds α(n) by a margin growing with n. Conjecture: when m_1 < a_1 = R_largest, `A ≥ a_1 − (total_R − a_1) = 2a_1 − total_R = M − total_R = α(n+1)` (the dyadic-dominance identity!), with equality iff the rest-pieces pair up perfectly. This would close Branch 2 in one line via the certified dyadic-dominance identity, reducing the inductive step to Branch 1 alone. **Probe this — it's the cleanest opening.**
- **(O4) Dyadic self-similar inductive lift via M⊎R (route 2, the dispatch's preferred route).** `D(n+1) = 2D(n)+1`, `M − total(R) = α(n+1)`. The reduction `L(n+1) ⟺ e_M ≤ o_R` (certified) localizes the obstruction. Self-compensation reduces to (Match). BUT the superincreasing-R "obstruction ≤ R_largest" corollary is FALSE (finding 3), so the inductive step cannot lean on it as stated. The M⊎R recursion `1/f(n+1) = 1 + 1/(2f(n))` is a verified algebraic identity but (per round-2 rule) a REPHRASING of L+U, not a bypass. The genuine inductive content is the e_M ≤ o_R inequality, which is exactly the open gap. crux `aimo-0261` (perimeter-min partition, local-exchange forces corner onto symmetry line → self-similar split for induction) is the closest template: a local-exchange argument forcing the extremal Xiang refinement onto the pair-pile symmetry locus, then recurse on the self-similar sub-structure. NOT a direct fit (aimo-0261 is a partition-min perimeter, not an alternating-sum bound), but the "local exchange forces self-similar extremal" pattern is the right shape.

### Candidate technique(s)
- **Cell-complex vertex enumeration** (CERTIFIED for n ≤ 4 this round; infeasible for n ≥ 5 by brute force — needs structural theorem).
- **Hall's marriage theorem on rank indices** (the (Match) residual; verified n=1..5 for Branch 1; needs the m_1-split fix; per-position dominance FAILS).
- **Dyadic self-similar induction** via M⊎R (crux aimo-0261 template: local-exchange forces extremal onto symmetry locus).
- **Piecewise-concavity / vertex-principle** (knowledge_base "Piecewise-concavity smoothing" — the minimizer of A is driven to a sparse axial/pair-pile config; A is piecewise-linear not concave, but the vertex-principle analog holds).

### Cheap-kill candidates
- **The m_1 < a_1 branch via the dyadic-dominance identity** (opening O3 above): conjecture `A ≥ 2a_1 − total_R = α(n+1)` when m_1 < a_1. If true, Branch 2 closes in one line, reducing the inductive step to Branch 1. **Highest-value cheap kill to probe next.**
- **Parity / pair-excess** (grid-only, certified `lemma-grid-parity.md`): does NOT lift to reals (sub-α fragments cancel at odd ranks). Already ruled out as a real proof.
- **CK odd-count cheap-kill** (certified): does NOT lift to reals (sub-α smallest piece possible). Already ruled out.

### Knowledge-base entries to use
- **Piecewise-concavity smoothing** (drive minimizer to sparse axial config — the pair-pile family is the analog sparse config here).
- **Invariants & monovariants** (the alternating advantage sum A; the M-vs-R split linearizes it).
- **Pigeonhole / extremal principle** (pair-excess parity, grid-only).
- **Hall's marriage theorem** (the (Match) residual — the canonical Hall matching framings).
- **Casework / exhaustion** (the n=3 unrefined-R 3-case casework pattern — but it must be REDONE with the m_1-split; the current proof is invalid).

### Analogous past problems (cruxes)
- **`aimo-0019`** (combinatorics, games-and-strategy / invariants) — crux: "bound a family of dyadic-length pieces of pairwise distinct sizes by twice the largest, via the geometric sum of distinct negative powers of two." This IS the superincreasing-R structure (each R-piece exceeds the sum of all smaller R-pieces by α(n+1)). The pairing-partner lever borrowed this correctly for the SUPERINCREASING IDENTITY (which is certified-valid); the BUG is only in the obstruction-magnitude corollary that mis-applied it. The crux's "amortized potential charged per frontier advance" is the right induction shape (NOT the falsified Ψ=1/A). Analogy: genuine (same dyadic-superincreasing structure).
- **`aimo-0261`** (combinatorics, extremal-principle / induction) — crux: "in a perimeter-minimizing partition, apply a merge-or-shift local exchange to the piece covering the extreme corner to force its opposite corner onto the symmetry line, producing a self-similar split for induction." The template for the M⊎R inductive lift: a local-exchange argument forcing the extremal Xiang refinement onto the pair-pile symmetry locus, then recurse. Analogy: structural (self-similar induction pattern), not a direct fit (perimeter-min vs alternating-sum-min) — adapt, don't cite.
- **`aimo-0225`** (combinatorics, games-and-strategy) — crux: "determine the game value by recursing on the 2-adic valuation of a difference that exactly halves at each step." The D(n)=2D(n-1)+1 Mersenne recursion is the analog (halving-step invariant). Analogy: thematic (2-adic induction), not directly load-bearing here.

### Prior progress
- **L(1), L(2), L(3) reals CERTIFIED** (rounds 1,2,4; cell-complex + pairing-partner). **L(4) reals CERTIFIED this round** (cell-complex, 10.4M 4-tuples, 0 violations, pair-pile equality `(8,8,4,4,2,2,1,1,1)/31`). Four lower-bound data points now (n=1..4). The vertex-principle is general-n; n=5 enumeration infeasible (2.49B 5-tuples).
- The pairing-partner superincreasing-R IDENTITY (a_j − Σ_{l>j} a_l = α(n+1)) is CERTIFIED-valid. The OBSTRUCTION BOUND corollary (σ ≤ a_1) is FALSE for k≥2 (finding 3). The L(3) unrefined-R PROOF is invalid (finding 4); the RESULT still holds (cell-complex independent).
- `c(1)=2/3, c(2)=4/7` solved end-to-end. `c(3)=8/15` lower-half certified; upper-half U(3) open (G2, owned by `two-regime-disjunctive`).

### Dead ends (do not retry)
- **Per-mark monovariant / ΔA −2T tail-flip** (round 1, certified dead). The cell-complex route sidesteps it by treating A as undecomposed.
- **Engine A two-tail cancellation** (round 3, falsified on n=3 brute force). `pairing-partner-transfer` retired.
- **Engine R-pile greedy pile-match** (round 3, falsified — 3 counterexample classes).
- **Unified Ψ=1/A amortized potential** (round 3, RETHINK — +1 boundary quantity FALSE for non-dyadic).
- **LP-dual / weight-function averaging / Schur-convexity** (round 3, killed — A neither Schur-convex nor concave; n=2 four-strategy is NOT a weighted-average identity).
- **Multi-aux L* generalization** (round 2, FALSE — counterexample W=(1/9,4/9,1/9)/D=9).
- **The superincreasing-R obstruction corollary σ ≤ M/2** (THIS ROUND, finding 3) — FALSE for k≥2. Do not cite `lemma-superincreasing-R.md`'s corollary as a bound on the obstruction magnitude. The IDENTITY `a_j − Σ_{l>j} a_l = α(n+1)` stands; the corollary does not.
- **The L(3) unrefined-R proof as written** (THIS ROUND, finding 4) — invalid (only covers m_1 ≥ a_1). The lemma's RESULT (A ≥ α(3)) stands by independent cell-complex certification; the pairing-partner PROOF must be redone with the m_1-split before reuse.

### Small-case / intuition notes (CONJECTURES, labeled)

- **CONJECTURE (L(n) for all n over reals)**: `A ≥ α(n) = 1/D(n)` for every real Xiang response to the level-n dyadic. Verified n=1..4 by CERTIFIED enumeration (n=4 this round, 0 exact violations); n=5 by Monte-Carlo only (200k random reals, 0 violations, min A = 32/63 region — NOT certified).
- **CONJECTURE (Hall matching on rank indices, Branch 1)**: for m_1 ≥ a_1, `s_3+s_5+…+s_{2n+1} ≤ a_2+…+a_{n+1}` with equality at the staircase interleaving. Verified n=1..5 (slack ≥ 0; = 0 at staircase for n=1..4; n=5 min slack 0.002 > 0 by random sampling — staircase is measure-zero, not hit). NO analytic proof.
- **CONJECTURE (Branch 2 cheap kill, opening O3)**: when m_1 < a_1 = R_largest, `A ≥ 2a_1 − total_R = α(n+1)` via the dyadic-dominance identity (a_1 at global rank 1 gives Liu +a_1; the rest pairs up with total ≤ total_R − a_1). Numerically consistent: Branch 2 min A exceeds α by a margin growing with n (n=3: 0.0667 vs 0.0667 ≈ equal? — actually n=3 Branch 2 min A = 0.0667 = α(3), so the bound may be TIGHT, not strict; needs careful check). **Probe this next round — if true, it closes Branch 2 in one line.**
- **Intuition**: the cell-complex route is the robust backbone (uniform across all k and all m_1 branches, certified n≤4). The pairing-partner route has a genuine structural insight (superincreasing-R identity) but its proof machinery has a hole (the m_1-split). The general-n lift most likely comes from a STRUCTURAL characterization of arrangement vertices (every minimizer is the pair-pile family + degenerations), not from raw enumeration (n=5 infeasible) and not from the broken superincreasing-R corollary.

### Recommendation to the outliner

**Prioritize the cell-complex route for the general-n lift.** Specifically:
1. **Re-dispatch `cell-complex-l3` builder** to (a) record the L(4) certification (this round's computation, scripts at `/tmp/round-5/n4_verify.py` and `/tmp/round-5/cell_vertex_n4b.py`), and (b) attempt the STRUCTURAL theorem: "every level-n arrangement vertex attaining A = α(n) is the pair-pile family `(2^n,2^n,2^{n-1},2^{n-1},…,2,2,1,…,1)/D(n)` or a one-zero degeneration; all other vertices have A > α(n)." If provable by a rank-parity / dyadic-level argument on the merged sort, this lifts L(n) to general n WITHOUT enumeration. The n=3,4 certified data (12 distinct min multisets at n=4, all pair-pile degenerations) is the evidence base.
2. **Re-dispatch `pairing-partner` builder** to FIX the m_1-split (Branch 1 Hall conjecture + Branch 2 cheap-kill O3). The certified superincreasing-R IDENTITY is still valid; only the corollary and the L(3) proof need rework. The Hall conjecture on rank indices (Branch 1) is verified n=1..5 — proving it analytically is the live handle.
3. **Probe opening O3 (Branch 2 cheap kill) first** — it's the highest-value cheap kill; if `A ≥ 2a_1 − total_R = α(n+1)` holds whenever m_1 < a_1, the inductive step reduces to Branch 1 only.
4. **Do NOT attempt n=5 cell enumeration** (2.49B 5-tuples, infeasible in-round). If n=5 certification is needed, it requires either 14-core parallelism with a smarter vertex-pruning algorithm, or the structural theorem above.
5. **G2 (upper bound U(3) reals) is the higher-value parallel target** (owned by `two-regime-disjunctive`) — closing it gives `c(3)=8/15` end-to-end, the second solved value. But that's a different lens; this report is the lower-bound lift.

Scripts: `/tmp/round-5/n4_verify.py` (n=4 exact certificate), `/tmp/round-5/cell_vertex_n4b.py` (n=4 float+exact), `/tmp/round-5/hall_check2.py` (Hall conjecture with m_1-split), `/tmp/round-5/bug_check2.py` (corollary bug verification).
