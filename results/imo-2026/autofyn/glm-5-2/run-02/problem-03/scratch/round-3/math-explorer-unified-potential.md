# imo-2026-03 — unified-potential / LP-duality / weight-function route

Lens: a SINGLE framing proving BOTH bounds at once, bypassing the separate Lemma-L + Lemma-U induction that has stalled for 2 rounds. Verified against current.md, all 3 live approaches, and all 6 certified lemmas.

---

## 1. The terrain — is a unified framing viable?

**Reframing the value as a saddle.** Let `A = Σ(−1)^{i+1} p_i` (advantage coord); `Liu = (1+A)/2`. The conjectured `c(n) = f(n) = 2^n/(2^{n+1}−1)` is exactly the statement that the *advantage minimax value*

> `c(n) = f(n)  ⇔  max_{Liu P} min_{Xiang Q}  A(P,Q)  =  1/D(n)`,  with `D(n)=2^{n+1}−1`.

Lemma L (dyadic Liu ≥ 1/D) is the **maximin half**; Lemma U (Xiang caps ≤ 1/D) is the **minimax half**. They are the two halves of a saddle-point claim with saddle (dyadic Liu, pair-pile Xiang). A "unified" approach is one that proves the saddle-point identity directly, WITHOUT splitting into L + U.

**The structural invariant (confirmed numerically).** The saddle is TIGHT only at the dyadic; for every non-dyadic Liu config Xiang forces strictly less (n=2 grid D=252: non-dyadic configs give cap ≈ 1/2, well below f(2)=4/7). Equality iff dyadic. Confirmed by full enumeration for n=2 (denom 168, 13530 responses) and n=3 (denom 120, 253460 responses): the dyadic saddle is exactly `f(n)`, and at n=3 (grid 30) there are 114 distinct minimizing responses — the minimizers span all k=1,2,3 (the k≥2 sub-case gap), so any per-k induction is fighting a robust minimizer set.

**Verdict on the four candidate engines:**

| engine | viability | reason |
|---|---|---|
| **Mersenne contraction** `B(n+1)=2B(n)+1` (per-round potential) | **most promising** | algebraically solid; the `+1` is the structural boundary correction; the only open step is to *charge* the `+1` to a specific structural element |
| LP-dual / weight-function on piece sizes | **weak** | the n=2 four-strategy bound does NOT follow from any averaging/weighted-sum identity (avg of the 4 functionals at dyadic = 5/28 > 1/7); the contradiction uses `a+b+c=1` cross-terms, not a clean linear dual |
| Majorization (Schur-convex oddsum) | **failed** | pair-pile does NOT majorize every Xiang refinement of the dyadic (only 776/1378 on grid 56 at n=2); oddsum is not Schur-convex/concave on the full sorted vector |
| Binary-tree / Kraft | **plausible, under-developed** | dyadic pieces `2^i/D(n)` ↔ binary-tree leaves; pair-pile "equal pairs of powers of 2" ↔ balanced tree; Mersenne `2^{n+1}−1` = # non-empty subsets of an (n+1)-set is a strong hint; needs concrete construction |

The headline: **the only engine with a real chance of subsuming both gaps is the Mersenne contraction** `B := 1/A → 2B+1` per round, and the open step is *exactly* the `+1` interleaving correction — which is what `induct-one-mark` (round 2) flagged as "best regarded as a unifying conjecture, not a bypass." The unified route's job is to find a CHARGING ARGUMENT that produces the `+1` from a structural element (not from per-mark casework).

**Numerical confirmation of the Mersenne closed form as a geometric series** (conjecture, not proof): `f(n) = (1/2)·Σ_{k≥0} 2^{−k(n+1)} = (1/2)/(1−2^{−(n+1)})`. Verified for n=1..5 by exact rational arithmetic. This is the "1/2 fair-share + geometric Liu-edge" decomposition — a strong hint that the `+1` per round is a `2^{−(n+1)}`-scaled structural boundary.

---

## 2. Closest crux moves retrieved

Three genuinely analogous cruxes (read in full; re-prove, don't cite):

- **`aimo-0019`** (combinatorics, invariants-and-monovariants) — *dyadic covering game*. Crux: "Maintain a linear potential bounding cumulative resource by a constant times progress, proved by **amortized induction that charges each frontier advance against the pieces it absorbs**." B keeps `ink ≤ 3·x_r` by charging each advance `x_{r+1}=x_r+α` to `2/2^m` (scattered) + `1/2^m` (filled) ≤ `3·α`. **Why analogous**: same structure — a dyadic-length game where one player (B/Xiang) controls a boundary and the bound is a *linear potential* (constant × progress) maintained by amortized charging. **Adaptation**: define `Ψ = B = 1/A` as the maintained potential; each Xiang mark is a "frontier advance" producing a `+1` correction that must be charged against the dyadic level boundary (Liu's largest piece `M` vs the rest `R`). The `M − total(R) = 1/D(n+1)` identity (already certified in `pairing-partner`) is the charging target — it IS the `+1` in `B(n+1) = 2 B(n) + 1`, since `1/D(n+1) = 1/(2 D(n) + 1)` and `B(n+1) = D(n+1) = 2 D(n) + 1`.

- **`aimo-0146`** (combinatorics, double-counting) — *university dinner min-degree functional*. Crux: "Charge each edge's min-degree label to its smaller-degree endpoint in a fixed degree ordering, so the functional becomes a **weighted sum of the sorted degrees with the weight on rank i capped by i−1**." **Why analogous**: oddsum is also a weighted sum of the sorted piece vector (`w_i = (−1)^{i+1}`), and the parity-rank cap is the structural constraint. **Adaptation**: prove that the alternating-sign rank weights `w_i = (−1)^{i+1}` satisfy `Σ w_i p_i ≥ 1/D(n)` whenever `p` is a refinement of the dyadic, by charging each "excess" `p_{2k−1} − p_{2k}` to its dyadic level. The rank-cap `a_i ≤ i−1` here becomes "the number of Liu pieces at dyadic level ≥ k."

- **`aimo-0196`** (combinatorics, extremal-principle + invariants-and-monovariants) — *coin-box deficit arc game*. Crux: "When a resource is only slightly below the uniform average, **measure the deficit from that average as an additive potential**; a global deficit ≥ d spread over a bounded cyclic/linear domain forces a local arc with deficit ≥ 3." Plus: "hand the opponent a designated forced move that both drains the potential and pins one boundary cell." **Why analogous**: the `+1` in `B(n+1)=2B(n)+1` is a deficit-from-average term; the "designated forced move" is Liu's dyadic move forcing Xiang's response. **Adaptation**: track `Ψ − 2·Ψ_parent − 1` as the per-round deficit; show it cannot be negative under the dyadic Liu move (Liu's guarantee) and cannot be positive under any Xiang response (Xiang's cap), forcing equality `= 0` at the saddle.

No crux on classical LP-duality or majorization matched this problem's structure — those that mention "minimax" / "duality" (aimo-0811, aimo-0198) are about trapping values in intervals or averaging a greedy minimizer's two options (`min ≤ (A+B)/2`), not about a saddle-point of a refinement game. The LP-dual engine is NOT supported by the corpus for this problem type.

---

## 3. Concrete candidate engines (2–3) for a new `unified-duality` approach

Each is genuinely FAR from per-mark induction and from n=2-casework — their whole point is to subsume both.

### Engine A — the Mersenne contraction via a per-round charging potential (RECOMMENDED)

**Setup.** Define `Ψ(state) = 1 / A(state) = 1 / (2·oddsum − 1)` as the maintained potential (a real ≥ 1, with `Ψ(dyadic+pair-pile) = D(n) = 2^{n+1}−1`). Liu MINIMIZES `Ψ` (max A); Xiang MAXIMIZES `Ψ` (min A). Base `Ψ(0 marks) = 1` (Liu takes the whole stick; A=1, B=1). Target: prove `Ψ(after n rounds) = D(n)`, equivalently `Ψ → 2 Ψ + 1` per round.

**The unified claim to prove (this is the load-bearing step):**
> For ANY intermediate configuration with potential `Ψ`, one round (Liu adds a mark, Xiang adds a mark) sends the value to `2 Ψ + 1`.

This is exactly the `induct-one-mark` round-2 conjecture, but re-cast as a CHARGING claim (not a per-mark monovariant). The crux from `aimo-0019` is the template: maintain a linear potential via amortized induction, charging each move against the structural boundary it absorbs.

**Hard step identified.** The `+1` per round must be charged to a SPECIFIC structural element. The certified identity `M − total(R) = 1/D(n+1)` (from `pairing-partner`, the `M ⊎ R` self-similar decomposition) is the natural charging target: it says the "level boundary" between Liu's largest piece `M` and the rest `R` carries exactly `1/D(n+1) = α(n+1)` of advantage. The `+1` in `B → 2B+1` corresponds to this single boundary unit. **The open step is to show that NO Xiang response can avoid producing this `+1` boundary term** (Liu's lower bound) AND **that Xiang can ALWAYS produce exactly this `+1`** (Xiang's upper bound, the pair-pile). Both are statements about the SAME boundary quantity, so a single charging argument closes both.

**Distance from prior dead ends.** The per-mark monovariant (ΔA closed form with the `−2T` tail-flip) is RETIRED because it tried to charge PER MARK. The unified route charges PER ROUND, against the level boundary — exactly the `aimo-0019` amortized-frontier pattern. The multi-aux `L*` FALSE counterexample `W=(1/9,4/9,1/9)` over D=9 is sidestepped because we never split `M` into sub-pieces for per-mark analysis; we work on the global potential `Ψ`.

**Honest risk.** The `+1` boundary correction may not be a single quantity — the `M ⊎ R` identity gives `1/D(n+1)` for the *dyadic* decomposition, but for an ARBITRARY Liu partition there's no canonical `M, R` split, so the charging target is unclear. This is the make-or-break step.

### Engine B — the binary-tree / Mersenne-subset charging scheme (speculative)

**Setup.** Map the dyadic Liu config `(2^n, 2^{n−1}, ..., 1)/D(n)` to a binary tree: leaf `i` (for i=1..n+1) at depth `n+1−i` carrying weight `2^{n+1−i}/D(n)`. Pair-pile Xiang response = "balance" the tree: split each right-spine node into a balanced pair, producing the equal-pair structure `(2^{n−1},2^{n−1},...,4,4)` with the `(3,2,1,1)` tail. The Mersenne `D(n) = 2^{n+1}−1` = # non-empty subsets of an (n+1)-set is a strong hint that the charging is over subsets (each subset ↔ a strategy).

**Hard step identified.** The oddsum is NOT a standard tree invariant (depth-weighted leaf sum); it's a SORTED-RANK sum, and the sort is by weight not by tree-position. To make this work one would need a "parity-majorization" lemma: *if a binary tree refines the dyadic-spine tree, then its sorted-leaf oddsum ≥ 1/D(n), with equality iff the pair-pile.* This is plausible but not standard; no crux in the corpus supports it directly.

**Distance from prior dead ends.** Completely different framing — no per-mark analysis, no k-casework, no M⊎R decomposition. The risk is that oddsum's sort-by-weight doesn't align with the tree structure cleanly.

### Engine C — the minimax-saddle direct proof via a topological/continuous relaxation (speculative)

**Setup.** Liu's strategy set = the (n+1)-simplex (compact convex); Xiang's strategy set = the compact set of mark placements; payoff `A(P,Q)` is continuous. Prove `max_P min_Q A = min_Q max_P A = 1/D(n)` by exhibiting a saddle at (dyadic Liu, pair-pile Xiang) and proving the saddle inequalities directly — i.e. the pair-pile is the Xiang MINIMAX strategy (not just a best response to dyadic), and the dyadic is the Liu MAXIMIN strategy (not just a best response to pair-pile).

**Hard step identified.** Pure-strategy minimax swaps are generally FALSE; proving the swap here needs quasi-concavity (in Liu) / quasi-convexity (in Xiang) of `A`, which is piecewise-linear and may fail at sort-boundaries. The corpus has NO crux supporting this pattern for refinement games. **High risk of being a false lead.**

---

## 4. Honest dead ends (what would make the unified framing fail)

1. **The `+1` per round is NOT a single boundary quantity.** If, for arbitrary Liu partitions, the per-round `+1` term decomposes into multiple interacting boundary contributions (not just `M − total(R)`), then Engine A's charging target evaporates. The ΔA closed form's `−2T` tail-flip term (certified `lemma-delta-a-local-cut.md`) is evidence FOR this risk: the tail parity is scrambled by non-local cuts, so a single boundary charge won't capture it.

2. **LP-dual / weight-function certificate does not exist (likely).** My numerical test on n=2 showed the four-strategy minimum does NOT come from a weighted-average identity (avg = 5/28 > 1/7 = target). The bound genuinely uses `a+b+c=1` cross-terms. So a clean LP-dual certificate is unlikely for general n — do NOT pursue the LP-dual engine.

3. **Majorization fails (confirmed).** Pair-pile does not majorize every refinement (776/1378 at n=2 grid 56); oddsum is not Schur-convex/concave. Do NOT pursue the majorization engine.

4. **Pure-strategy minimax swap may be false.** Engine C is the riskiest; without a corpus crux supporting it for refinement games, it could be a research-level detour. Deprioritize.

5. **The binary-tree framing's "parity-majorization" lemma may not exist.** No corpus support; the sort-by-weight misaligns with tree structure.

---

## 5. Summary table for the outliner

- **Distinct openings surfaced**:
  1. (A) Mersenne contraction `Ψ → 2Ψ+1` per round, with `+1` charged to the `M−total(R)=α(n+1)` level boundary — crux template `aimo-0019` (amortized frontier charging).
  2. (B) Binary-tree / Mersenne-subset charging — `D(n) = # non-empty subsets of (n+1)-set` hint; needs a parity-majorization lemma.
  3. (C) Direct minimax-saddle proof at (dyadic, pair-pile) — risky, no corpus support.
- **Candidate technique(s)**: amortized charging potential (aimo-0019 pattern) + rank-cap double-counting (aimo-0146 pattern); the `M⊎R` dyadic-dominance identity as the charging target.
- **Cheap-kill candidates**: NONE obvious — the problem has resisted per-mark monovariants, multi-aux `L*`, per-Xiang-mark induction, and majorization. The only "cheap" structural fact is the `M − total(R) = 1/D(n+1)` identity (already certified); the question is whether it can carry the whole `+1` term.
- **Knowledge-base entries to use**: *Invariants & monovariants* (the alternating sum A is the controlled invariant; `Ψ = 1/A` is the amortized potential); *Induction* (Pólya "Generalize: a stronger statement is sometimes easier" — load both bounds into one induction via the saddle-point); *Constructive/incremental* (the pair-pile is the constructive extremal); *Extremal principle* (the dyadic is the unique cap-attainer).
- **Analogous past problems (cruxes)**: `aimo-0019` (dyadic covering game, amortized linear potential — BEST match); `aimo-0146` (rank-cap weighted-sum via endpoint charging); `aimo-0196` (deficit-from-average additive potential).
- **Prior progress**: conjectured `c(n) = 2^n/D(n)` verified exact n=1..5; c(1)=2/3, c(2)=4/7 rigorously end-to-end; Lemma G, pair-pile, mirror, ΔA, L*, L(n+1) k=0/k=1, U(1), U(2) all certified; the `M⊎R` self-similar decomposition + dyadic-dominance identity `M − total(R) = 1/D(n+1)` is the load-bearing structural fact for the unified route.
- **Dead ends (do not retry)**: per-mark monovariant (ΔA `−2T` tail-flip, certified fatal); multi-aux `L*` (FALSE, counterexample `W=(1/9,4/9,1/9)`); (2^n−1)-way casework generalization of U(2) (no clean lift); per-Xiang-mark induction (round-level not per-mark); Hall-matching (fails dominance for non-dyadic); `A≤0` pairing for regime-N (FALSE, non-dyadic caps above 1/2); LP-dual/weight-function averaging (n=2 average = 5/28 > 1/7, too weak); majorization (pair-pile does not majorize all refinements).
- **Small-case / intuition notes (CONJECTURE, not proof)**:
  - `c(n) = (1/2) Σ_{k≥0} 2^{−k(n+1)}` — the "1/2 fair share + geometric Liu edge" decomposition (verified n=1..5 exact rational).
  - At dyadic, ALL n+1 "alternating differences" + the smallest piece + the dominance excess `|2p_1−1|` equal `1/D(n)`. The four functionals of U(2) are `p_3, p_2−p_3, p_1−p_2, |2p_1−1|`.
  - For non-dyadic n=2 configs, the cap is typically ≈ 1/2 (sliver limit), well below f(2)=4/7. The "1/2 floor" is significant — it's the asymptotic fair share.
  - At n=3 (grid 30), the minimizer set (114 responses) spans k=1,2,3 — the lower-bound minimizers are NOT concentrated at k=1, so per-k casework is fundamentally fighting a robust minimizer set. This is evidence the unified route MUST avoid per-k decomposition.
