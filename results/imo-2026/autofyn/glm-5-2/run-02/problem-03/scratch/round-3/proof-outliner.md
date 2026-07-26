## imo-2026-03

Target (whole claim, every slug): `c(n) = 2^n / (2^{n+1} − 1) =: f(n)`, with `D(n) = 2^{n+1} − 1`, `α(n) = 1/D(n)`. By Lemma G (certified), `Liu = oddsum`, `Liu = (1+A)/2`, `A = Σ(−1)^{i+1} p_i`. So `c(n)=f(n) ⇔` minimax value of `A` is exactly `α(n)`. Verified exact for n=1..5; c(1)=2/3, c(2)=4/7 rigorous end-to-end. Open for n≥3: G1 (Lemma L general-n k≥2, lower bound) and G2 (Lemma U regime-N, upper bound).

Certified lemmas imported by all slugs (do NOT re-prove): **Lemma G** (`lemmas/lemma-g-greedy-picking.md`), **pair-pile dyadic cap** (`lemmas/lemma-pair-pile-dyadic-cap.md`), **mirror certificate** (`lemmas/lemma-mirror-dyadic-cap.md`), **ΔA local-cut** `ΔA = 2((−1)^r b − T)` (`lemmas/lemma-delta-a-local-cut.md`), **Lemma L\*** single-aux (`lemmas/lemma-L-star-single-aux.md`), **U(2) four-strategy** (`lemmas/lemma-u2-four-strategy.md`). PROVED sub-cases reusable: L(n+1) k=0 (trivial), L(n+1) k=1 (reduces to L\*).

Pre-flight checks I ran (sympy/Fraction) before outlining:
- **CK** (odd piece-count ⟹ `A ≥ smallest piece`): 0/20000 violations. One-line proof: `A = Σ_pairs(p_{2i−1}−p_{2i}) + p_{last}`, each pair-excess ≥0 by sorted order, leftover = smallest.
- **Geometric series** `f(n) = (1/2)Σ_{k≥0} 2^{−k(n+1)}`: symbolically `(1/2)/(1−2^{−(n+1)}) = 2^n/D(n) = f(n)`. ✓ (the "1/2 fair-share + geometric Liu-edge" decomposition).
- **Greedy pile-match** (two-largest, `a_1≥2a_2`): on dominant (.6,.2,.1,.1) caps at 1/2 < 8/15 in 2 marks, canceling pairs land at consecutive sorted ranks (equal pieces cluster). On the DYADIC (8,4,2,1)/15 it OVERSHOOTS to 3/5 > 8/15 — so Engine R-pile is a **regime-N tool only**; the certified pair-pile remains the regime-D equality case. On balanced (1/2,3/10,3/20,1/20) it is inadmissible from the start (`a_1<2a_2`) — confirms the balanced-fallback need.

---

### pairing-partner: advance
Target: c(n)=f(n) end-to-end (lower bound via weight-function for the k≥2 sub-case + imported k≤1 sub-cases + pair-pile upper bound at the dyadic; regime-N upper bound carried as a tracked gap delegated to two-regime-disjunctive).
Technique: global weight-function / charging inequality (Engine C from the variational explorer, crux `aimo-0019` amortized-charging + `aimo-0146` rank-cap weighted-sum) — bypasses the per-k interleaving obstruction by proving `A ≥ 1/D(n)` directly on every Xiang refinement of the dyadic, with no k-classification, no WLOG-k≤1 exchange.
Skeleton:
  1. Lemma G (imported) ⟹ Liu = oddsum = (1+A)/2; target `A ≥ α(n)`.
  2. Liu plays the dyadic `(1,2,…,2^n)/D(n)`. Lemma L(n): `A ≥ α(n)` for every Xiang refinement by ≤ n marks.
  3. M⊎R self-similar decomposition (imported): largest piece `M = 2^{n+1}/D(n+1)`, rest `R` a scaled level-n dyadic, identity `M − total(R) = α(n+1)`.
  4. k=0 sub-case (PROVED, imported): `A ≥ M − total(R) = α(n+1)`.
  5. k=1 sub-case (PROVED, imported): reduces to L\*(n).
  6. **k≥2 sub-case (THE GAP, new via Engine C)**: construct a weight function `w` (hybrid: size + local-rank/parity-aware) such that
     - **(W1)** `A ≥ Σ_{pieces} w(piece)` for every sorted multiset (a matching/alternating inequality — independent of which dyadic piece a size came from),
     - **(W2)** `Σ_{pieces} w(piece) ≥ α(n)` for every refinement of the level-n dyadic by ≤ n marks (conservation / amortized-charging on the multiset of sizes).
     Combining: `A ≥ α(n)`. No exchange, no k-count.
  7. Upper bound at the dyadic: pair-pile caps at exactly f(n) (imported, regime D).
  8. Regime-N upper bound (non-dyadic configs cap < f(n)): tracked gap, delegated to two-regime-disjunctive.
  9. Synthesis: c(n) = f(n) (once gap in step 6 closes and the regime-N gap closes in the sibling).
Key lemmas (claim + one-line mechanism):
  - **CK (odd-count cheap-kill, one-line)** — `A = Σ_pairs(p_{2i−1}−p_{2i}) + p_{last} ≥ p_{last}` because every pair-excess ≥0 by the sorted order and the leftover is the smallest piece. Sub-case of (W1) for odd-count configs. Verified 0 violations.
  - **(W1) matching inequality** `A ≥ Σw` — because `w` is chosen so that `Σw` is bounded above by the alternating sum on ANY sorted multiset (the alternating-sign rank weights `w_i=(−1)^{i+1}` already give `Σw_i p_i = A`; the engine seeks a coarser `w` depending on piece size, not rank, losing equality but gaining the conservation (W2)).
  - **(W2) conservation** `Σw ≥ α(n)` — by amortized charging of each dyadic-level piece `2^j/D(n)` against the geometric sum `Σ2^{−k}`: when Xiang splits a level-j piece, the children's `w`-total is at least the parent's `w` minus a controlled sliver, telescoping to `α(n)` (crux `aimo-0019` frontier-charging pattern).
Open gaps: step 6 — find `w`. The odd-count sub-case reduces (via CK) to conjecture **(S)** "the smallest piece ≥ α(n) at the minimizer" (splitting a piece ≤ α(n) never helps Xiang); the even-count case (pair-pile-type extremals) needs a separate `w`-argument. The pair-pile extremal is EVEN-count, so CK does not cover all minimizers — `w` must handle even-count too.
Cases to cover: odd-count minimizers (CK + (S)); even-count minimizers (pair-pile-type — `w` must give Σw = α(n) at the pair-pile with equality).
Watch out for:
  - The explorer's obstruction: a PURE-size `w` cannot detect the parity-of-multiplicity that distinguishes the pair-pile's canceling equal pairs from a non-canceling pair of the same sizes — `w` may need local-rank info (hybrid). If no hybrid `w` exists, this route dies.
  - Conjecture (S) shares the same ΔA `−2T` hard step as the per-mark route (Engine A) — they are not independent; if (S) is unprovable, the odd-count sub-case of Engine C also stalls. The EVEN-count sub-case is the genuinely-new territory Engine C must own.
  - Do NOT retry multi-aux L\* (FALSE, W=(1/9,4/9,1/9)/9) or "WLOG k=1" (literal monotonicity FALSE, n=3 brute: k=2,3 extremals more numerous than k=1).

---

### two-regime-disjunctive: advance
Target: c(n)=f(n) end-to-end (upper bound via regime-D pair-pile + regime-N greedy recursive pile-match; lower bound carried as a tracked gap delegated to pairing-partner).
Technique: greedy recursive pile-matching of the two largest pieces (Engine R-pile, crux `aimo-0369` recursive one-move-then-recurse) — generalizes the n=1 sliver mode and n=2 Strategy A; agnostic (caps for all P, equality characterization falls out at the dyadic via the pair-pile, NOT via the greedy which overshoots there — verified).
Skeleton:
  1. Lemma G (imported).
  2. Upper bound: for every Liu config `P` of n+1 pieces, Xiang with ≤ n marks forces `oddsum ≤ f(n)`.
  3. Regime D (P is the scaled dyadic): pair-pile caps at exactly f(n) (imported). Equality case.
  4. **Regime N (P non-dyadic) — THE GAP, new via Engine R-pile**: recursively, while marks remain and ≥2 pieces exist:
     - identify the two current largest pieces `a_1 ≥ a_2`;
     - if `a_1 ≥ 2 a_2` (admissibility: residual `a_1−a_2 ≥ a_2`), place one mark cutting `a_2` out of `a_1`, creating the canceling pair `(a_2, a_2)`; the residual `a_1−a_2` and the pair both rejoin the partition; recurse (one fewer mark);
     - if `a_1 < 2 a_2` (balanced), fire a bisect/sliver fallback (generalize U(1) sliver mode + U(2) Strategies B/C/E): bisect `a_1` into `(a_1/2, a_1/2)` (canceling pair) and use remaining marks on the next-largest pieces.
     - the greedy creates canceling equal pairs that occupy consecutive sorted ranks (equal pieces cluster), contributing 0 to A; the residual singleton tail determines the cap.
  5. Termination: ≤ n marks consumed; final `A < α(n)` strictly for non-dyadic P (equality only at the dyadic, handled by regime D).
  6. Lower bound (Lemma L general-n): tracked gap, delegated to pairing-partner.
  7. Synthesis: c(n) = f(n).
Key lemmas (claim + one-line mechanism):
  - **Consecutive-rank invariant (the load-bearing claim)** — after each greedy pile-match, the created equal pair `(a_2,a_2)` lands at consecutive sorted ranks, because equal pieces cluster in the sorted order and the residual `a_1−a_2 ≥ a_2` (admissibility) keeps the residual above the pair, so the pair is a block below the residual. Hence the pair contributes `−p_{2i}+p_{2i+1}=0` to A (cancels). [Verified on (.6,.2,.1,.1): pairs at ranks 2,3 and 4,5, A=0 after 2 marks.]
  - **Greedy caps below f(n) when it runs to completion** — because each canceling pair reduces A by exactly `a_2`'s contribution and the residual tail `≤ 1/2` (the largest remaining piece after k pile-matches is `≤ 1/2` once the config is non-dyadic), giving `A ≤` tail-excess ` < α(n)` for non-dyadic P. [Verified: (.6,.2,.1,.1) → A=0, oddsum=1/2 < 8/15.]
  - **Balanced fallback** — when `a_1 < 2a_2` (no dominant piece), bisect `a_1` into `(a_1/2,a_1/2)` (one mark, canceling pair) and recurse on `(a_1/2, a_2, a_3, …)`; the n=1 base is `a_1<2/3` (bisect mode), n=2 bases are Strategies B/C/E; the threshold generalizes `α(n)=1/D(n)`.
Open gaps: (a) PROVE the consecutive-rank invariant inductively across multiple pile-matches (the interleaving of residual pieces with created pairs across steps — same wall that killed Hall, but the greedy controls the sort at each step, unlike a global Hall matching); (b) the balanced-case fallback when `a_1<2a_2` for n≥3 (the n=2 four-strategy template does not lift to a (2^n−1)-way contradiction — the recursion must replace flat casework); (c) prove the residual tail `≤ 1/2` bound for non-dyadic P after the greedy terminates.
Cases to cover: dominant non-dyadic (`a_1 ≥ 2a_2` — greedy runs); balanced non-dyadic (`a_1 < 2a_2` — fallback); near-dyadic (greedy may overshoot like it does on the exact dyadic — must detect dyadic-ness and fall through to regime D / pair-pile).
Watch out for:
  - The greedy OVERSHOOTS on the exact dyadic (verified: (8,4,2,1)/15 → 3/5 > 8/15); it is a regime-N tool only. The dyadic MUST be detected and routed to the pair-pile. The dyadic-detection condition is the regime boundary (dyadic-vs-non-dyadic, already the certified boundary).
  - The consecutive-rank invariant is the SAME interleaving wall that killed Hall (round 1) — the greedy must control it LOCALLY at each step (always the two current largest), not globally. If this fails, fall back to Engine R-dyadic-comparison (agnostic majorization) — but majorization was KILLED (pair-pile does not majorize all refinements; oddsum not Schur-convex/concave), so the fallback is weak. Engine R-pile is the live engine.
  - Do NOT retry the false `A≤0` pairing (non-dyadic n=2 caps above 1/2); the (2^n−1)-way flat casework; per-Xiang-mark induction.

---

### unified-mersenne-charging: new
Target: c(n)=f(n) end-to-end via a SINGLE amortized-potential argument that subsumes both Lemma L (lower) and Lemma U (upper) — picking up the exact gap `induct-one-mark` left ("no potential accounting for the +1") but with a new mechanism (charging, not identity verification).
Technique: amortized per-round charging potential `Ψ := 1/A` (crux `aimo-0019` dyadic-frontier amortized charging + `aimo-0196` deficit-from-average additive potential). The per-round Mersenne contraction `Ψ → 2Ψ+1` (base `Ψ(0)=1`, target `Ψ(n)=D(n)`) is a verified algebraic identity; the new content is a CHARGING ARGUMENT producing the `+1` from the structural level-boundary `M − total(R) = α(n+1)` (certified dyadic-dominance identity).
Skeleton:
  1. Lemma G (imported). Define `Ψ = 1/A = 1/(2·oddsum − 1)` (a real `≥ 1`; `Ψ(dyadic+pair-pile) = D(n)`). Liu MINIMIZES `Ψ` (max A); Xiang MAXIMIZES `Ψ` (min A). Base `Ψ(0 marks) = 1` (whole stick to Liu, `A=1`).
  2. **The unified claim (load-bearing)**: one round (Liu adds a mark, Xiang adds a mark) sends `Ψ → 2Ψ+1`. After n rounds, `Ψ = D(n)`, `A = α(n)`, `oddsum = f(n)`.
  3. The charging: the `+1` per round is charged to the level-boundary quantity `M − total(R) = α(n+1)` — the certified dyadic-dominance identity. At each round, the largest piece `M` of the current config and the rest `R` satisfy `M − total(R) = α(current level)`; this `α` IS the `+1` in `Ψ → 2Ψ+1` because `α(n+1) = 1/D(n+1) = 1/(2D(n)+1)` and `Ψ_parent = D(n)`, so `2Ψ_parent + 1 = 2D(n)+1 = D(n+1) = Ψ_child`.
  4. Lower bound (Liu's guarantee): Liu's dyadic move CREATES the `M,R` structure with the boundary `M−total(R)=α(n+1)`; prove NO Xiang response can avoid producing this `+1` boundary term ⟹ `Ψ ≥ 2Ψ+1` (Liu minimizes Ψ, so the value is at least `D(n)`). This is Lemma L rephrased in Ψ-space — the charging argument replaces the per-k casework.
  5. Upper bound (Xiang's cap): Xiang's pair-pile response FORCES exactly the boundary `M−total(R)=α(n+1)` ⟹ `Ψ ≤ 2Ψ+1` (Xiang maximizes Ψ, so the value is at most `D(n)`). This is Lemma U rephrased — the pair-pile is the extremal charging response.
  6. Both bounds charge the SAME boundary quantity ⟹ saddle at `Ψ = D(n)`, `oddsum = f(n)`. Equality iff dyadic (Liu) + pair-pile (Xiang).
  7. Synthesis: c(n) = f(n), with both bounds closed by one charging argument.
Key lemmas (claim + one-line mechanism):
  - **The `+1` boundary charge** — `M − total(R) = α(n+1) = 1/(2D(n)+1)` is exactly the additive `+1` in `Ψ → 2Ψ+1` because `Ψ_parent = D(n)` and `2D(n)+1 = D(n+1) = Ψ_child`; the per-round potential increments by exactly the level-boundary excess (certified identity). This is the crux `aimo-0019` pattern: maintain a linear potential via amortized charging of each frontier advance against the dyadic level it absorbs.
  - **Charge invariance under both players' moves** (the make-or-break claim) — the boundary quantity `M−total(R)` is invariant under who controls the split: Liu's move creates it (lower bound) and Xiang's response forces it (upper bound), both charging the same `+1`. If this invariance holds, one argument closes both bounds.
Open gaps: the make-or-break step is proving the `+1` is a SINGLE boundary quantity for ARBITRARY Liu partitions (not just the dyadic, where `M,R` are canonical). The explorer's honest dead-end #1: for arbitrary partitions there is no canonical `M,R` split, and the ΔA `−2T` tail-flip term (certified) is evidence that the per-round correction may decompose into multiple interacting boundary contributions, not a single charge. The charging argument must either (a) define a canonical `M,R` split for every partition (e.g. `M` = largest piece always, `R` = the rest), or (b) show the multi-boundary contributions telescope to a single `+1` in Ψ-space.
Cases to cover: dyadic Liu config (canonical M,R — cleanest, both bounds close here first); non-dyadic Liu config (canonical M = largest piece, R = rest — the +1 must still telescope); balanced configs (no dominant M — the charging target is least clear here).
Watch out for:
  - This is NOT `induct-one-mark` reheated. `induct-one-mark` VERIFIED the algebraic identity and conceded "no potential accounting for the +1 is identified." This approach's NEW content is exactly that accounting (the charging argument via `aimo-0019`). If the charging argument fails (the `+1` is not a single boundary quantity), this approach dies the SAME death as `induct-one-mark` — honest assessment, it is a bet that `aimo-0019`'s amortized-frontier pattern realizes what `induct-one-mark` could not.
  - The `+1` may not be a single quantity (the ΔA `−2T` scrambling suggests it isn't for arbitrary partitions). If so, this approach is dead — recorded honestly.
  - LP-dual / weight-function averaging is KILLED (n=2 average = 5/28 > 1/7); majorization is KILLED (pair-pile doesn't majorize; oddsum not Schur-convex). This approach is NEITHER — it is an amortized CHARGING argument, not an LP dual or a majorization.

---

### pairing-partner-transfer: copy-of pairing-partner
Target: c(n)=f(n) end-to-end (lower bound via the extremal+non-improving-transfer engine for the k≥2 sub-case; upper bound via pair-pile + sibling regime-N — identical twin of pairing-partner but with a DIFFERENT engine for the same gap G1).
Technique: extremal minimizer + non-improving 2-piece transfer (Engine A from the variational explorer, crux `aimo-0119` non-improving-transfer on the extremal minimizer) — a genuinely different mechanism from pairing-partner's weight-function (Engine C): it uses a SWAP/transfer on the `A`-minimizing Xiang refinement rather than a global inequality.
Skeleton: steps 1–5 and 7–9 identical to pairing-partner (same imports, same M⊎R decomposition, same k=0/k=1 sub-cases, same pair-pile upper bound, same regime-N delegation). The ONLY difference is step 6:
  6'. **k≥2 sub-case (THE GAP, new via Engine A)**: let `C* = argmin A` over Xiang refinements of the level-n dyadic, tie-broken by (a) fewest marks in `M`, (b) lexicographically smallest sorted piece vector. If `C*` has `k≥2` marks in `M` (the k≥2 sub-case), pick the two smallest `M`-sub-pieces `m_k ≥ m_{k+1}`; MERGE them (remove the mark between) and RE-PLACE that mark to bisect the largest unsplit `R`-piece. Call the result `C'`. Claim: `A(C') ≤ A(C*)` (non-increasing). Iterate to `k=1`, where the proved sub-case gives `A ≥ α(n)`.
Key lemma (claim + one-line mechanism):
  - **Two-tail cancellation (the load-bearing claim)** — the ΔA for this 2-piece simultaneous move (merge in `M` + bisect in `R`) involves two tail terms `T_M, T_R`; the conjecture is `T_M + T_R ≤ 0` (the parity-flip-on-tail terms cancel because the two operations are at the SAME sorted-rank boundary — the merge raises a piece's rank while the bisect lowers one, and the tail re-indexings are opposite). Combined with the tie-break (b), `A(C') ≤ A(C*)`, so `C'` is also a minimizer with one fewer mark in `M`; iterate to k=1.
Open gaps: prove `A(C') ≤ A(C*)` — the two-tail cancellation. This is the SINGLE load-bearing unproved step.
Cases to cover: the transfer is always "merge the two smallest M-sub-pieces + bisect the largest unsplit R-piece" — one canonical transfer; the tie-break (b) handles equality (non-strict).
Watch out for:
  - Engine A is HIGH risk, HIGHEST reward (the explorer's honest assessment). If the two tails do NOT cancel, Engine A hits the SAME `−2T` wall as the per-mark route (certified dead) and dies the same death. The dispatch flagged literal monotonicity in k as FALSE (n=3: k=2,3 extremals more numerous than k=1); Engine A only needs the WEAK form `A(C') ≤ A(C*)` (non-increasing, not strict), and the tie-break handles equality — but even the weak form is unverified.
  - This is a COPY of pairing-partner (two viable engines for the same gap G1 k≥2): Engine C (global weight-function, MED risk) on the original, Engine A (extremal transfer, HIGH risk) on this twin. They are genuinely different mechanisms (global inequality vs swap-on-extremal). If Engine C closes G1, the twin is redundant; if Engine C fails, the twin is the fallback. Worth running both in parallel.

---

### induct-one-mark: RETIRE (do NOT re-dispatch)
The value-recursion route (Mersenne identity `1/V(n+1)=1+1/(2V(n))`) is conceded DEAD (round 2: builder conceded it is a rephrasing of Lemma L + Lemma U, NOT an independent bypass; the `+1` interleaving correction has no identified potential accounting). The algebraic identity is verified but consequent, not a proof. Retirement recorded in `approaches/induct-one-mark.md` under Approaches tried. Its correct sub-results (k=0 trivial sub-case; k=1 reduction to L\*) are shared with and subsumed by `pairing-partner`. The genuinely-new Mersenne-route attempt (charging argument via crux `aimo-0019`) is fielded as the SEPARATE new slug `unified-mersenne-charging` above — it is NOT a revision of this slug.

---

## Field summary

4 active approaches on the table (2 advances, 1 new, 1 copy) + 1 retirement:

- **pairing-partner** (advance, Engine C weight-function) — G1 k≥2 via global weight-function, MED risk.
- **two-regime-disjunctive** (advance, Engine R-pile) — G2 regime-N via greedy recursive pile-match, MED risk (consecutive-rank invariant is the hard step).
- **unified-mersenne-charging** (new, Engine A-of-unified = amortized Ψ=1/A charging) — both bounds at once via the M−total(R)=α(n+1) boundary charge, MED-HIGH risk (the `+1` may not be a single boundary quantity).
- **pairing-partner-transfer** (copy of pairing-partner, Engine A extremal+two-tail-cancellation) — G1 k≥2 via a different mechanism, HIGH risk, highest reward.
- **induct-one-mark** — RETIRED.

Diversity check (framings kept FAR apart):
- pairing-partner: per-k induction on the dyadic + global weight-function (lower bound).
- two-regime-disjunctive: greedy recursive strategy construction (upper bound).
- unified-mersenne-charging: amortized per-round potential / charging (both bounds, no induction, no casework).
- pairing-partner-transfer: extremal minimizer + non-improving swap (lower bound, different mechanism than the weight-function twin).

Rejected 4th-framing candidates (considered, judged too close to KILLED routes to spend a builder):
- Binary-tree/Kraft: oddsum is a sorted-RANK sum, not a tree-leaf-depth sum (sort-by-weight misaligns with tree structure); no corpus support.
- LP-dual/minimax-saddle direct: LP-dual KILLED (n=2 four-strategy average = 5/28 > 1/7; the bound uses `a+b+c=1` cross-terms, not a linear dual); pure-strategy minimax swap has no corpus support for refinement games.
- Majorization (Engine R-dyadic-comparison): KILLED (pair-pile does not majorize all refinements, 776/1378 at n=2 grid 56; oddsum neither Schur-convex nor Schur-concave).
- Subset-probability (f(n) = P(random non-empty subset of [n+1] contains element 1)): the subset recursion `D(n)=2D(n−1)+1` IS the Mersenne recursion, so this collapses into unified-mersenne-charging — not genuinely different.

build set: pairing-partner, two-regime-disjunctive, unified-mersenne-charging, pairing-partner-transfer
