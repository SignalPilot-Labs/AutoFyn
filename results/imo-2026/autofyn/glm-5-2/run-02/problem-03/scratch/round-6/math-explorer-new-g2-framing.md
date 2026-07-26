# imo-2026-03 — G2 upper-bound, GENUINELY-DIFFERENT framings (lens: new-g2-framing)

Target: `cap(P) := min_{Xiang marks x} A(P,x) ≤ α(n) = 1/D(n)` for ALL Liu configs `P` at ALL `n` (the non-strict `U(n)`). Dead routes to avoid: (i) the 2-adic strict-decrease `Φ>0 ⟹ cap<α` (FALSIFIED by the ridge `R_e=(8,4,2+e,1−e)/15`); (ii) the two-regime 17-family/sliver casework (stuck on `U(3)` `d<1/2` extreme sub-cases, no general-`n` mechanism).

## Distinct openings (each far from both dead routes)

### Opening 1 — "Constant value on an equality locus" (the reconnaissance headline)
The strongest structural finding from probing: `V(P) := min_x A(P,x)` is conjectured **constant `= α(n)`** on a structured *equality locus* `E_n`, and **strictly `< α(n)`** elsewhere. Evidence (all n=3, conjectural):
- `V(dyadic) = α` (CERTIFIED, cell-complex L(3) + pair-pile).
- `V(R_e) = α` for the **non-dyadic ridge** `R_e=(8,4,2+e,1−e)/15`, all `e∈(0,1)` (pair-pile attains `A=α`, no strategy beats it — dyadic-halving approach §5). So `E_3` is **positive-dimensional**, NOT just the dyadic point.
- `V(balanced) < α` (S1 sliver, CERTIFIED); `V(extreme-dom L>4/5) < α` (S3, CERTIFIED); far-from-dyadic `V < α` numerically (two-regime).

The dyadic is NOT an isolated max of `V` — it is one point of a locus. **`U(n)` reframes as: characterize `E_n` and prove `V(P) ≤ α` universally with equality iff `P ∈ E_n`.** This is genuinely different from the 17-family (per-config strategy casework) and from Φ (strict-decrease, dead). The equality locus `E_n` is the UPPER-BOUND dual of cell-complex's lower-bound equality-vertex set (12 distinct min multisets at n=4). Shared-wall risk: if `E_n` is characterized via the same pair-excess binary form, it overlaps cell-complex D2/D3. **Divergence from cell-complex**: cell-complex characterizes equality VERTICES of `A` for fixed `P=dyadic`; this opening characterizes equality CONFIGS `P` for the value `V(P)`. Different object.

**Concrete next step for outliner**: state `E_n` as the set of `P` for which the pair-pile/mirror strategy attains `A = α(n)` exactly (i.e. `P` admits a pair-pile-type refinement). Prove (a) `E_n` contains the dyadic + the ridge family (verified); (b) for `P ∉ E_n`, the pair-pile overshoots and a sliver-shave gives `V < α` (the 17-family mechanism, but now UNIFIED under "the pair-pile is the canonical witness; everything else is strict"). This collapses the regime-D/regime-N split into "equality locus vs strict-decrease locus" — a single-gap statement, but the gap (sliver-forcing off `E_n`) is the SAME as two-regime's wall. Flag: single-gap-trap if the sliver-forcing is shared.

### Opening 2 — Self-reproducing invariant (aimo-0262 Cinderella/Stepmother template)
**Crux `aimo-0262` is the closest structural analogue** in the corpus: adversary (Stepmother = Liu) distributes water over `n+1` buckets; defender (Cinderella = Xiang) empties a **neighboring pair** each round; she maintains a **self-reproducing invariant** ("two adjacent buckets empty, flanking pair ≤ 1, last ≤ 1") that re-establishes after every adversary move, capping every bucket at 1 < 2 forever. The bound comes from a disjoint-pair averaging argument (`y_0+y_2` and `y_1+y_3` sum to ≤ 2, so one ≤ 1).

**Translation to our game**: Xiang's pair-pile IS a self-reproducing invariant — "after my marks, the pair-excess binary structure holds: every pair-excess ∈ {0,1}, leftover ∈ {0,1}, total `A = α(n)`." The ridge finding shows this invariant **reproduces under level-1-exact perturbations** (the pair-pile absorbs deeper-level perturbation, residual excesses `(1−e)+e = 1` sum to `α`). **The genuinely-different question**: does the pair-pile invariant reproduce under ARBITRARY Liu perturbation, with the residual cap staying ≤ α? If YES, `U(n)` follows from a single invariant, no casework. If NO (and the two-regime wall suggests NO for far-from-dyadic), the invariant must be ENRICHED — a self-reproducing family of invariants indexed by which halving-level is broken (the Φ organization, but NON-strict).

**This is far from both dead routes**: not strict-decrease (Φ dead), not 17-family casework (one invariant, not many strategies). **Next step**: formalize the pair-pile as a self-reproducing invariant on the pair-excess vector `(e_1,...,e_n, ℓ)`; identify the reproduction rule (how Liu's perturbation maps to an `e_i`-shift); prove the invariant caps `Σ e_i + ℓ ≤ α(n)` for all perturbations. The ridge shows the cap is TIGHT (not strict) on `E_n`. The hard case is far-from-dyadic (balanced/extreme-dominant) where the invariant must be enriched — flag: this is where the wall with two-regime could re-emerge.

### Opening 3 — D3-dual structural theorem (cell-complex dualized to U)
Cell-complex's D3 conjecture (open): "every FRACTIONAL arrangement vertex of the dyadic config has `A > α(n)·D(n)`" (verified n=3,4). The **DUAL for U(n)**: "for every non-dyadic `P`, the arrangement vertices of `P` have `A ≤ α(n)` (with equality characterizing a pair-pile-type vertex)." Same parity technique (D2: at integer-valued vertices, `A` is odd non-neg ≥ 1), applied to `P`'s vertex structure instead of the dyadic's.

**Far from dead routes**: not Φ (uses vertex-principle, not halving-defect); not 17-family (structural theorem, not strategy casework). **Single-gap-trap risk HIGH**: it shares the cell-complex D3 technique. If D3's "fractional vertices exceed α" mechanism is the same as the dual's "fractional vertices of non-dyadic P are ≤ α", they could fail together. **Divergence**: D3 lower-bounds (proves `V(dyadic) = α`); the dual upper-bounds (proves `V(P) ≤ α` for `P ≠ dyadic`). The parity argument runs in OPPOSITE directions (lower bound: `A ≥ 1` at integer vertices; upper bound: `A ≤ α` at the pair-pile vertex for non-dyadic `P`). Worth a probe but flag the shared-wall risk.

### Opening 4 — Minimax / LP-dual on the continuous mark-simplex (RISKY)
The round-3 rule KILLED LP-dual/weight-function averaging for the DISCRETE n=2 four-strategy average. The dispatch asks whether a DUAL framing on the CONTINUOUS mark-simplex escapes. Assessment: **RISKY, likely dead.**
- The cell-complex vertex-principle IS a continuous-simplex reduction (for L): `min_x A(P,x) = min` over arrangement vertices. This works because `A` is piecewise-linear in `x` for fixed `P`.
- For U, we want `max_P min_x A(P,x)`. `min_x A(P,x)` (min over `x` of a jointly-piecewise-linear function) is NOT obviously concave in `P` (min of piecewise-linear, not linear). The maximizer (dyadic) is INTERIOR to the Liu simplex, so `V` is NOT concave (a concave function peaks at an extreme point). So the clean minimax-duality route does not fire.
- The sequential (Stackelberg) structure (Xiang sees `P` then moves) breaks von Neumann minimax, which needs simultaneous mixed play.
- **Do not retry** this as the primary framing; it risks re-dying the round-3 death. A continuous-LP dual is only revivable if a SPECIFIC dual-feasible weight function on the mark-simplex is exhibited — none is visible, and the round-3 rule explicitly forbids weight-function averaging.

### Opening 5 — Single self-similar mirror strategy (PROBED, DEAD)
I probed whether the **mirror** (Xiang marks at `1−l_j`, the reflection of Liu's marks) — a SINGLE self-similar strategy, far from casework — gives `A ≤ α(n)` universally. **Result: DEAD.**
- On the dyadic: `A = α(3)` (tight, ✓).
- On the ridge `R_e`: `A = α(3)` (tight, ✓ — consistent with `R_e ∈ E_n`).
- On balanced `(1/4)×4`: `A = 0 < α` ✓.
- On extreme-dominant `(.9, 1/30, 1/30, 1/30)`: `A = 0.8 ≫ α = 0.0667` ✗ VIOLATION.
- On moderate-dominant `(.6,.25,.1,.05)`: `A = 0.2 ≫ α` ✗ VIOLATION.
- 24410/30000 random n=3 configs VIOLATE (`A` up to 0.978).
- n=2: 22063/30000 violations.

The mirror is tight EXACTLY on the equality locus `E_n` (dyadic + ridge + symmetric configs) and overshoots elsewhere. It is a WITNESS for `E_n`, NOT a universal cap. **Do not retry the mirror as a single-strategy U(n) proof.** (The mirror CERTIFICATE on the dyadic stands — it witnesses the lower bound's tightness, not U(n).)

## Candidate technique(s)
- **Self-reproducing invariant** (aimo-0262 template) — the pair-pile as an invariant on the pair-excess vector that reproduces under Liu perturbation. The most promising genuinely-different mechanism.
- **Equality-locus characterization** — structural theorem dual to cell-complex D2 (lower-bound equality vertices) but for the UPPER bound (equality configs `P`).
- **Vertex-principle dual** (cell-complex, applied to U) — RISKY, shared technique with D3.

## Cheap-kill candidates
- **Parity at integer-valued vertices** (D2, CERTIFIED): at integer-valued arrangement vertices of the dyadic, `A` is odd non-neg ≥ 1. The DUAL cheap-kill for U: at integer-valued arrangement vertices of a NON-dyadic `P`, is `A` odd and ≤ α? No — parity gives a LOWER bound (`A ≥ 1`), not upper. So parity cheap-kills the LOWER bound, not the upper. No cheap-kill for U via parity alone.
- **Pair-excess averaging** (aimo-0262 disjoint-pair): the disjoint diagonal pairs `y_0+y_2` and `y_1+y_3` sum to ≤ 2, so one ≤ 1. Analog for our `2n+1` pieces: split the pair-excesses into two disjoint sub-collections whose sums are bounded by `α(n)`; one is ≤ `α/2`? Not obviously — the pair-excess identity `A = Σ e_i + ℓ` has `n+1` terms, and the dyadic gives `Σ e_i + ℓ = 1` (integer scale). No clean disjoint-pair averaging visible for the upper bound. **None obvious.**

## Knowledge-base entries to use
- **Invariants & monovariants** (the pair-excess vector as a self-reproducing invariant; the Φ halving-defect — already certified, use the non-strict version).
- **Hall's marriage theorem / SDR** (the residual Match `Σ_MM m_even ≤ Σ_RR r_odd` from pairing-partner — relevant if the self-reproducing-invariant route reduces to a matching).
- **Induction (structural)** — the self-similar `M ⊎ R` recursion (NOT the killed bisect-recurse; the pair-pile's self-similar structure).
- **Casework / exhaustion** — ONLY as the last resort for the far-from-dyadic strict-decrease (shared wall with two-regime).
- **Constructive / incremental** — explicit Xiang mark placements (the pair-pile + its enrichments).
- **Meta-Strategy**: "Prune before you compute" — the self-reproducing invariant is the prune; the 17-family is the heavy route.

## Analogous past problems (cruxes)
- **`aimo-0262`** (Cinderella/Stepmother, self-reproducing invariant) — **BEST match.** Crux: defender maintains a self-reproducing invariant (adjacent-pair-empty + flanking ≤ 1) that re-establishes after every adversary move, capping every bucket at 1 < 2. Analog: Xiang's pair-pile maintains the pair-excess binary invariant; the ridge shows it reproduces under level-1-exact perturbations. The disjoint-pair averaging (`y_0+y_2 + y_1+y_3 ≤ 2 ⟹ one ≤ 1`) is the template for a possible disjoint-pair cheap-kill on `Σ e_i + ℓ`.
- **`aimo-0225`** (n-gon, v_2(n−3) recursion) — strategy-stealing + 2-adic-valuation recursion on a halving-difference. Already flagged (round 5). Relevant to the Φ organization (non-strict) and the self-similar recursion, BUT the strict-decrease is dead; use only the strategy-stealing / self-reproducing-symmetric-position half.
- **`aimo-0019`** (paint game, dyadic + linear potential `3x_r`) — maintain a linear potential bounding cumulative resource by amortization. Template for a potential `Ψ(P,x) ≥ A` with Xiang keeping `Ψ ≤ α`. The killed `Ψ=1/A` (round 3) is dead, but a DIFFERENT potential (e.g. on the pair-excess vector) might fire. Lower priority.
- **`aimo-0117`** (Jesse/Tjeerd, dyadic geometric sequence) — "the single largest power outweighs the entire rest" = the superincreasing-R identity (CERTIFIED `a_j − Σ_{l>j} a_l = α(n+1)`). Confirms the pair-pile's self-similar structure. Already harvested.

## Prior progress
- `c(1)=2/3, c(2)=4/7` solved end-to-end (both bounds).
- `L(3), L(4)` over reals CERTIFIED (cell-complex, vertex-principle + exhaustive enumeration). n=1..4 lower bounds all certified.
- `U(3)`: `d≥1/2` regime CLOSED (5-cap, CERTIFIED `lemma-u3-5cap-dominant.md`); `d<1/2` gap `G` CLOSED (3-mark sliver, CERTIFIED `lemma-u3-sliver-gap.md`); `d<1/2` non-gap `w,z≥−2α` CLOSED. **MATERIAL GAP**: `d<1/2` non-gap extreme sub-cases (`w<−2α` or `z<−2α`) — computationally 0 violations, analytic 17-family case-by-case NOT written.
- Pair-pile + mirror certified (regime-D equality, all n). Φ=0 uniqueness + local-kink + ridge falsification certified.

## Dead ends (do not retry)
- **Φ strict-decrease** (`Φ>0 ⟹ cap<α`) — FALSIFIED by ridge `R_e` (round 5, `lemma-ridge-falsification.md`).
- **Mirror as single-strategy U(n)** — PROBED THIS ROUND, overshoots on extreme-dominant (A=0.8) and moderate-dominant (A=0.2); 24410/30000 random violations. Tight only on `E_n`.
- **LP-dual / weight-function averaging on discrete strategies** — KILLED round 3 (n=2 four-strategy minimum is NOT a weighted-average identity). Do not retry on discrete strategies; continuous-simplex dual (Opening 4) is RISKY, only revivable with a specific dual-feasible weight function (none visible).
- **Engine R-pile greedy** (round 3), **Engine A two-tail cancellation** (round 3), **bisect-recurse** (round 3), **unified-mersenne-charging** (round 3), **σ≤M/2 corollary** (round 5, FALSE k≥2) — all dead, do not retry.
- **Equality-case-classification as standalone** (round 4 RETHINK) — union of two shared walls. The Opening 1 equality-LOCUS framing here is the REFINEMENT that diverges (targets `P`-equality, not vertex-equality).

## Small-case / intuition notes (CONJECTURAL, labeled)
- The mirror probe CONFIRMS the equality-locus conjecture: the mirror is tight (`A=α`) exactly on `E_n` (dyadic + ridge + symmetric), and `A > α` OFF `E_n`. This means `E_n` is precisely the set of `P` where the pair-pile/mirror witnesses `V(P)=α`; off `E_n`, Xiang needs a different strategy (the 17-family/sliver) to get `V < α`. CONJECTURAL: `E_n` is characterized by "Liu's config admits a pair-pile-type refinement" — a structural condition on `P`'s dyadic-ratio structure (level-`j` exact for a prefix of levels, with compensating perturbations below).
- The ridge `R_e` is the cleanest witness: level-1 exact (`p_1=2p_2`), deeper levels perturbed but compensating (`(1−e)+e=1`). CONJECTURAL general form of `E_n`: `P` such that for some `j`, levels `1..j` are exact and levels `j+1..n` perturb with pair-excesses summing to `α(n)`. This is the "self-reproducing invariant" of Opening 2.
- The mirror's overshoot on extreme-dominant (A=0.8) CONFIRMS that far-from-dyadic configs need the sliver (not the mirror/pair-pile) — consistent with two-regime's S3 (extreme-dominant `L>4/5` forced `< α` by cutting `L` into 4 equal). So Opening 2's invariant MUST be enriched (not just the pair-pile) to handle far-from-dyadic — the wall with two-regime re-emerges there. Flag for outliner: the self-reproducing-invariant route is genuinely different NEAR the dyadic but shares the far-from-dyadic wall with two-regime. To avoid the single-gap-trap, the invariant must be a FAMILY (one per structural class), not a single pair-pile — but then it converges to the 17-family. The genuine escape is to prove the FAR-FROM-DYADIC case by a DIFFERENT mechanism (e.g. the D3-dual parity, or a potential `Ψ`), leaving the pair-pile invariant for the near-dyadic equality locus.

## Recommendation for the outliner
Field **Opening 2 (self-reproducing invariant, aimo-0262 template)** as the primary genuinely-different G2 framing for general `n`: the pair-pile as a self-reproducing invariant on the pair-excess vector, with the equality locus `E_n` as the set where it reproduces exactly (tight cap `α`), and an enriched invariant family for the strict-decrease off `E_n`. **Opening 1 (equality-locus characterization)** is the structural-theorem companion. **Opening 3 (D3-dual)** is a high-risk-high-reward alternative (shared-wall risk with cell-complex D3 — only field if D3 and its dual can be proved by genuinely different techniques). **Do NOT field** Opening 4 (LP-dual, round-3 death) or Opening 5 (mirror single-strategy, probed dead this round). For the `c(3)` end-to-end near-term, the highest-value target remains closing `U(3)`'s `d<1/2` extreme sub-cases (the 17-family case-by-case) — but that is two-regime's job, not this lens; this lens targets the GENERAL-`n` mechanism that the 17-family lacks.
