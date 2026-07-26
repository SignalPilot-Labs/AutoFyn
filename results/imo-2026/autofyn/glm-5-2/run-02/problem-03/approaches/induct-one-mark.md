## Status
partial

## Approaches tried
- (round 3, RETIRED) The value-recursion route is conceded DEAD (round 2: builder conceded `1/V(n+1)=1+1/(2V(n))` is a rephrasing of Lemma L + Lemma U, NOT an independent bypass; the `+1` interleaving correction has no identified potential accounting). The algebraic Mersenne identity is verified but consequent, not a proof. This approach is RETIRED — do NOT re-dispatch. Its correct sub-results (k=0 trivial sub-case; k=1 reduction to `L*(n)`) are shared with and subsumed by `pairing-partner`. The genuinely-new Mersenne-route attempt (charging argument via crux `aimo-0019`, picking up exactly the gap this approach left) is fielded as a SEPARATE new approach `unified-mersenne-charging` this round — it is NOT a revision of this slug.
- (round 1) Strong induction on n via a one-mark reduction factoring `1/f(n+1)=1+1/(2f(n))`, templated on the verified n=1 two-mode (bisect/sliver) base case. — Outcome: Lemma G (greedy→odd-rank sum) PROVED in full; Lemma S (small-n) verified; Lemma L (Liu lower bound on the dyadic config) PROVED for n=1,2 by exhaustive casework, general-n claim stated with the mechanism (ΔA closed form + dyadic compensation) but NOT closed (interleaving obstruction — explicit gap); Lemma U (Xiang upper bound) base n=1 PROVED (two-mode), general inductive step NOT closed — the recursion is a VALUE recursion, not a per-partition monovariant, so the one-mark reduction lemma does not factor cleanly (consistent with the outline-reviewer's verdict that the per-mark linear advance is false). Status: partial, the upper bound for general n is the open gap.

- (round 2) RETIRED the certified-false per-mark monovariant (NEVER re-attempt: verified fatal — a single Xiang mark does NOT drive `A → A/(A+2)`; on `A=1/3`, bisect gives `A'=1/3` not `1/7`). Upgraded to the **round-level value recursion** in advantage coordinates: `1/V(n+1) = 1 + 1/(2 V(n))` (Mersenne form `B(n+1)=2 B(n)+1`, `B(n):=1/A(n)=D(n)=2^{n+1}−1`, `B(1)=3`). Algebraically verified (R)/(M) for n=1..5 (substitution into the closed form). Proved the **trivial k=0 sub-case of Lemma L(n+1)** rigorously (Opening B: if 0 Xiang marks land in the largest dyadic piece `M`, then `oddsum ≥ M = f(n+1)`, no induction). Proved the **k=1 sub-case as a clean reduction** to the sibling `pairing-partner` approach's single-aux strengthened IH `L*(n)` (conditional on `L*`'s certification this round). Cross-checked the dyadic saddle by full grid enumeration: n=2 (denom 168) and n=3 (denom 120) both give xiang-min exactly `f(n)`. Honestly flagged the value-level `+1` interleaving correction as UN-CLOSED: the value recursion is a REPHRASING of (Lemma L + Lemma U) into one statement, NOT a bypass (no potential accounting for the `+1` term is identified). Lemma L general-n (k≥2 sub-case) and Lemma U general-n remain OPEN, delegated to the sibling approaches (`pairing-partner`'s `L*` route; `two-regime-disjunctive`'s corrected two-regime route). Status: partial, unchanged at the top level — the round-level recursion does not fire as an independent proof.

## Current best
The conjectured answer `c(n) = 2^n/(2^{n+1}−1) =: f(n)` (verified exact by rational arithmetic for n=1..5; asymptote 1/2 from above). Rigorous progress established (cumulative across rounds):
- **Lemma G (greedy-picking reduction)** — fully proved (import from `lemmas/lemma-g-greedy-picking.md`): Liu's payoff = odd-rank sum `S_odd` of the descending-sorted final pieces.
- **Parity identity** `Liu = (1 + A)/2`, `A = Σ (−1)^{i+1} p_i` — corollary of Lemma G. In advantage coordinates `A = 2·Liu − 1`, so `Liu = (1+A)/2`; `Liu ≥ f(n) ⇔ A ≥ 1/D(n)`.
- **Pair-pile construction** (all n) — Xiang caps the dyadic config at exactly `f(n)` (import from `lemmas/lemma-pair-pile-dyadic-cap.md`). The **mirror certificate** (this round, verified n=1..5: reviewer finding 1) is a cleaner alternative dyadic-cap certificate, pending certification by the `pairing-partner` builder.
- **ΔA local-cut closed form** `ΔA = 2·((−1)^r b − T)` — import from `lemmas/lemma-delta-a-local-cut.md`; explains the parity-flip-on-tail obstruction (the `−2T` term) that kills the per-mark route.
- **n=1 complete** (both bounds): `c(1) = 2/3`. L(1), L(2), U(1) proved.
- **NEW (round 2): the Mersenne value-recursion identity (R)/(M)** — the closed form `f(n)` satisfies `1/f(n+1) = 1 + 1/(2 f(n))` and `B(n+1) = 2 B(n) + 1` (`B(n)=D(n)`). Algebraically verified for n=1..5. This is the right UNIFYING FRAME: IF Lemma L(n) and Lemma U(n) hold for all n, then `V(n) = f(n)` for all n, and (R)/(M) is the consequent algebraic identity. The recursion is a *consequence* of the conjectured closed form, not independently a proof of it.
- **NEW (round 2): Lemma L(n+1) k=0 sub-case PROVED** (trivial, no induction): if 0 Xiang marks land in `M`, `S_odd ≥ M = f(n+1)`.
- **NEW (round 2): Lemma L(n+1) k=1 sub-case** reduced cleanly to `L*(n)` (sibling's strengthened dual IH, pending certification).
- **NEW (round 2): dyadic saddle cross-checked** by full grid enumeration for n=2 (denom 168, 13530 Xiang responses) and n=3 (denom 120, 253460 Xiang responses): in both, xiang-min on the dyadic Liu config = `f(n)` exactly. Corroborates Lemma L (lower) and pair-pile/mirror (upper) simultaneously for n=2,3.

**Open gaps (honest, both halves of general n):**
1. **Lemma L general-n** — the k≥2 sub-case (per-round peeling D1, or a WLOG-k=1 argument D2) is OPEN; the k=0 and k=1 sub-cases are closed (the latter conditionally on `L*(n)`). Delegated to `pairing-partner`'s `L*` simultaneous-induction route.
2. **Lemma U general-n** — Xiang caps EVERY Liu config at ≤ `f(n)`; the per-mark route is a certified dead end; the two-regime disjunctive invariant (regime D dyadic-dominant via mirror/pair-pile; regime N non-dyadic via a sliver/shave mechanism, NOT the false `A ≤ 0` pairing) is the live route. Delegated to `two-regime-disjunctive`.
3. **The round-level value-recursion proof** (closing the `+1` interleaving correction at the value level) is UN-CLOSED and, per the honest assessment below, is best regarded as a UNIFYING CONJECTURE packaging (L+U) rather than an independent bypass.

---

## Proof (partial — what is rigorously established)

**Notation.** The stick is `[0,1]`. Liu first places `n` marks (distinct points of `(0,1)`), partitioning the stick into `n+1` *Liu-intervals*; Xiang then places `n` marks (distinct from Liu's and from each other), refining the partition into at most `2n+1` *pieces*; the pieces are sorted descending `p_1 ≥ p_2 ≥ … ≥ p_M` and the two players alternately claim an unclaimed piece, Liu first. Let

`D(n) := 2^{n+1}−1`  (Mersenne),   `f(n) := 2^n / D(n)`,   `A := p_1 − p_2 + p_3 − … = Σ_i (−1)^{i+1} p_i`  (alternating advantage sum),

so that by Lemma G's parity identity `Liu = (1 + A)/2`. In particular `Liu ≥ f(n) ⇔ A ≥ 2 f(n) − 1 = (2·2^n − D(n))/D(n) = (2^{n+1} − (2^{n+1}−1))/D(n) = 1/D(n)`. Thus the target `c(n) = f(n)` is, in advantage coordinates, the statement

> **(T)**  `c(n) = f(n)`  ⇔  the minimax value of `A` over `(Liu config, Xiang ≤ n marks)` is exactly `1/D(n)`.

---

### Lemma G (greedy picking → odd-rank sum) — IMPORTED

*After all marks are placed, let the pieces sorted descending be `p_1 ≥ p_2 ≥ … ≥ p_M`. Under optimal play by both players in the alternating-pick phase, Liu's payoff equals the odd-rank sum `S_odd = p_1 + p_3 + p_5 + …`, and Xiang's payoff equals the even-rank sum `p_2 + p_4 + …`.*

Imported verbatim from `lemmas/lemma-g-greedy-picking.md` (strong induction on `M` loading both move-orders into one induction; Pólya "a stronger statement is easier"). Henceforth `c(n) = max_{Liu's ≤n marks} min_{Xiang's ≤n marks} S_odd`. ∎ (Lemma G, certified round 1.)

---

### Lemma S (small-n verification) — IMPORTED

By exhaustive grid computation (exact rational arithmetic; grid a multiple of `D(n)` so the conjectured extremum lies on the grid):
- `c(1) = 2/3`, attained at Liu mark `1/3`; Xiang mark bisects `2/3`.
- `c(2) = 4/7`, attained at the dyadic Liu config `(1,2,4)/7`; exhaustive grid over all 2-mark Xiang responses gives min `S_odd = 4/7`.
- `c(3)=8/15, c(4)=16/31, c(5)=32/63` (verified by the explorers, exact rational).

This is a computational certificate (for the grid), not a proof for all `n`. The lemmas below supply the proof structure. ∎ (Lemma S, round 1.)

**Round-2 cross-check (computational, corroborates L+U at the dyadic saddle).** Full grid enumeration of Xiang's best response on the dyadic Liu config: for n=2, denom 168, all 13530 two-mark Xiang responses give min `S_odd = 4/7 = f(2)`; for n=3, denom 120, all 253460 three-mark Xiang responses give min `S_odd = 8/15 = f(3)`. These corroborate Lemma L (lower bound `S_odd ≥ f(n)`) AND the pair-pile/mirror cap (upper bound `S_odd ≤ f(n)`) simultaneously for n=2,3, confirming the dyadic saddle is tight at `f(n)`.

---

### Lemma L (Liu lower bound on the dyadic config) — n=1,2 PROVED; general n PARTIAL

**Config.** For the `(n)`-game Liu places his `n` marks at the cumulative sums of `(1, 2, 4, …, 2^{n−1})/D(n)`, i.e. at `1/D, 3/D, 7/D, …, (2^n−1)/D`. This partitions `[0,1]` into pieces `d_k := 2^k/D(n)` for `k = 0, …, n`. Note `d_n = 2^n/D(n) > 1/2` and

> `d_n − (d_0 + d_1 + … + d_{n−1}) = 2^n/D − (2^n−1)/D = 1/D = d_0`,  the **dyadic-dominance identity**.

The dyadic config is recursively self-similar: the `(n+1)`-dyadic config decomposes as `{M} ⊎ R` where `M := d_{n+1} = 2^{n+1}/D(n+1)` is the largest piece and `R := (d_0, …, d_n)` is, after rescaling by `D(n+1)/D(n)`, exactly the `(n)`-dyadic config (since `(2^0,…,2^n)/D(n+1) = (D(n)/D(n+1)) · (2^0,…,2^n)/D(n)`). The dyadic-dominance identity becomes `M − total(R) = 1/D(n+1)`.

**Claim L(n).** For the dyadic config, for *every* Xiang response (≤ `n` marks), `S_odd ≥ 2^n/D(n) = f(n)` (equivalently `A ≥ 1/D(n)`).

**Proof of L(1).** Liu pieces `{1/3, 2/3}`. Xiang's single mark splits one piece.
- *Split `2/3`* into `x, 2/3−x` (`x ≤ 1/3` WLOG). For `x < 1/3`: sorted `(2/3−x, 1/3, x)`, so `S_odd = (2/3−x) + x = 2/3`. For `x = 1/3`: three equal thirds, `S_odd = 2/3`.
- *Split `1/3`* into `x, 1/3−x` (`x ≤ 1/6` WLOG). The piece `2/3` is untouched, rank 1 (Liu's); `S_odd ≥ 2/3`.
Both cases give `S_odd ≥ 2/3 = f(1)`. ∎ (L(1))

**Proof of L(2).** Liu pieces `{1/7, 2/7, 4/7}`. Xiang's two marks each split one piece (if both hit the same piece, it is split into three). Casework on which pieces are touched (full sub-cases recorded in round 1; reproduced in the round-1 file). Every case gives `S_odd ≥ 4/7 = f(2)`. ∎ (L(2))

(The exhaustive grid check over all two-mark Xiang responses on the dyadic n=2 config — grid denom 168 — returns min `S_odd = 4/7` exactly, matching the casework.)

---

#### Round-2 progress on Lemma L general-n

The self-similar `M ⊎ R` decomposition is the engine. Fix `n+1 ≥ 2`; decompose the `(n+1)`-dyadic as `{M} ⊎ R`, `M = 2^{n+1}/D(n+1)`, `R = (D(n)/D(n+1)) ·` (n-dyadic). Let `k` be the number of Xiang marks landing *inside* `M` (`0 ≤ k ≤ n+1`); the remaining `n+1−k` marks refine `R` into `R'`.

**Sub-case k=0 (PROVED, trivial, no induction).** `M` is untouched and is a single piece. Since `M = 2^{n+1}/D(n+1) = (2^{n+1})/(2^{n+1}−1) > 1/2`, and `total(R) = 1 − M < 1/2 < M`, every piece of `R'` has size `≤ total(R) < M`; hence `M` is the global rank-1 piece (Liu's). The remaining pieces `R'` occupy global ranks `2, 3, …`, so

`S_odd = M +` (pieces of `R'` at global ranks `3, 5, 7, …`).

The global ranks `3, 5, 7, …` are the *even* ranks within `R'` (rank 2 = `R'`-position 1 = odd, rank 3 = `R'`-position 2 = even, …), so `S_odd = M + evensum(R')`. Every piece being nonneg, `evensum(R') ≥ 0`, hence

`S_odd ≥ M = 2^{n+1}/D(n+1) = f(n+1)`. ∎ (L(n+1), k=0)

This disposes of the entire "0 marks in `M`" branch with no induction and no interleaving obstruction — the obstruction only arises when `M` is split.

**Sub-case k=1 (reduced to `L*(n)`, conditional on sibling certification).** `M` is split into `m_1 ≥ m_2` with `m_1 + m_2 = M`; the remaining `n` marks refine `R` into `R'`. Since `m_1 ≥ M/2 = 2^n/D(n+1) =` (unrefined `R`'s largest piece) `d_n^{(R)}`, and refining `R` only shrinks its pieces, `m_1 ≥` every piece of `R'`; hence `m_1` is the global rank-1 piece (Liu's). The remaining multiset `{m_2} ∪ R'` occupies global ranks `2, 3, …`; as above,

`S_odd = m_1 + evensum({m_2} ∪ R')`.

We want `S_odd ≥ M = m_1 + m_2`, i.e. `evensum({m_2} ∪ R') ≥ m_2`. Now `m_2 ≤ M/2 = 2^n/D(n+1) = d_n^{(R)} =` the largest piece of the (unrefined) `(n)`-dyadic `R`. This is **exactly** the hypothesis of the strengthened dual IH

> **L\*(n)** (sibling `pairing-partner`, pending certification): for the `(n)`-dyadic config `R` (total `D(n)/D(n+1)`, largest piece `d_n^{(R)}`) refined by ≤ `n` marks into `R'`, and a single auxiliary piece `w` with `0 ≤ w ≤ d_n^{(R)}`, the merged multiset `{w} ∪ R'` satisfies `evensum({w} ∪ R') ≥ w`.

with `w = m_2`. Applying `L*(n)`: `evensum({m_2} ∪ R') ≥ m_2`, hence `S_odd ≥ m_1 + m_2 = M = f(n+1)`. ∎ (L(n+1), k=1, *conditional on `L*(n)`*)

`L*(n)` is verified for n=1..5 (Monte-Carlo, reviewer finding 4: gap ≥ 0 in every case, equality at the self-similar extremal) and is the load-bearing strengthened IH being proved this round by the sibling `pairing-partner` approach via simultaneous induction (the Lemma G "load both sides into one induction" pattern). I do not re-prove it here; I record the dependency.

**Sub-case k ≥ 2 (OPEN GAP).** Multiple marks land in `M`. The naive "multi-aux" generalization of `L*` — `evensum({w_1,…,w_j} ∪ R') ≥ Σ w_j` — is **FALSE** (counterexample, explorer-lowerbound: `W = (1/9, 4/9, 1/9)` over `D=9`, `R' = {2,1}/3` unrefined, `evensum = 5/9 < 6/9 = ΣW`); do NOT propose it. The live reduction is the **per-round peeling** (D1): peel a *pair* of Xiang marks at a time — one from `M`, one from `R` — so that each peel-pair reduces to a single-aux `L*` instance, matching the per-round (not per-mark) structure of the value recursion (R). This sub-step is OPEN and delegated to `pairing-partner`. The fallback (D2: "there exists a k=1 response at least as good for Xiang as any k≥2 response") is unverified.

---

### Lemma U (Xiang upper bound) — n=1 PROVED; general n GAP (delegated)

**Claim U(n).** For *every* Liu config (any `n+1` intervals summing to `1`), Xiang has a strategy with `≤ n` marks forcing `S_odd ≤ 2^n/D(n) = f(n)`.

**Proof of U(1).** Liu has two intervals `a, 1−a`, WLOG `a ≤ 1/2`. Target `f(1) = 2/3`. Two-mode case split on `a` (threshold `a = 1/3`):
- **Mode (i) — bisect, when `a ≤ 1/3`.** Xiang places his one mark at the midpoint of the larger interval `1−a`, splitting it into `(1−a)/2, (1−a)/2`. Since `a ≤ 1/3 ⇔ (1−a)/2 ≥ a`, the sorted order is `(1−a)/2, (1−a)/2, a`, so `S_odd = (1−a)/2 + a = (1+a)/2 ≤ (1 + 1/3)/2 = 2/3`. ✓
- **Mode (ii) — sliver, when `a ≥ 1/3`.** Xiang places his mark at distance `ε` (`0 < ε < 1 − 2a`, positive since `a ≤ 1/2`) from the boundary of the larger interval, splitting it into `1−a−ε` and `ε`. For small `ε`: `1−a−ε ≥ a ≥ ε`, so sorted `1−a−ε, a, ε`, giving `S_odd = (1−a−ε) + ε = 1−a ≤ 1 − 1/3 = 2/3`. ✓
The two modes cover `a ≤ 1/3` and `a ≥ 1/3` (threshold covered by both, continuity). ∎ (U(1))

**General-n (OPEN GAP, delegated).** The per-mark monovariant route is a **certified dead end** (round 1, verified fatal): the recursion (R) is per-ROUND (one mark to each player), not per-Xiang-mark; a single Xiang mark does NOT drive `A → A/(A+2)` (counterexamples: on `A=1/3`, bisect gives `A'=1/3` not `1/7`; on `A=1/2`, bisect gives `A'=1/4` not `1/5`). The `−2T` parity-flip-on-tail term (ΔA closed form) is the obstruction. This round RETIRES that route permanently.

The live route is the sibling `two-regime-disjunctive` approach: a disjunctive two-regime invariant with the regime boundary at **dyadic vs non-dyadic** (NOT dominant vs non-dominant — reviewer F2). Regime D (the rest `R` is a scaled `(n)`-dyadic) is capped at `f(n)` by the mirror/pair-pile certificate; regime N (non-dyadic) is capped strictly below `f(n)` (reviewer finding 3: cap ≈ 0.5 `<< f(n)`) by a sliver/shave mechanism generalizing U(1)'s sliver mode — NOT by the false `A ≤ 0` pairing (reviewer finding 2: non-dyadic configs give cap ≈ 0.503–0.525 > 1/2; the cap is `< f(n)` but the mechanism is a sliver, not a pairing). I delegate the full construction of regime N to that sibling and do not re-attempt it here.

---

### The round-level value recursion — UNIFYING CONJECTURE (not an independent proof)

**The Mersenne identity (algebraic, verified).** Define `V(n) := c(n)` (the minimax value) and `A(n) := 2 V(n) − 1` (advantage coordinate), `B(n) := 1/A(n)`. The conjectured closed form gives `A(n) = 1/D(n)`, `B(n) = D(n) = 2^{n+1}−1`, `B(1) = 3`. Then the **Mersenne value recursion** is

> **(M)**  `B(n+1) = 2 B(n) + 1`, equivalently `1/A(n+1) = 2/A(n) + 1`, equivalently `A(n+1) = A(n)/(A(n) + 2)`, equivalently **(R)** `1/V(n+1) = 1 + 1/(2 V(n))`, equivalently `V(n+1) = 2 V(n)/(2 V(n) + 1)`.

**Algebraic verification.** Substituting `B(n) = D(n) = 2^{n+1}−1`: `2 B(n) + 1 = 2(2^{n+1}−1) + 1 = 2^{n+2} − 1 = D(n+1) = B(n+1)`. ✓ Substituting `V(n) = f(n) = 2^n/D(n)`: `1 + 1/(2 V(n)) = 1 + D(n)/(2·2^n) = 1 + (2^{n+1}−1)/2^{n+1} = (2^{n+1} + 2^{n+1} − 1)/2^{n+1} = (2^{n+2}−1)/2^{n+1} = D(n+1)/2^{n+1} = 1/f(n+1) = 1/V(n+1)`. ✓ Verified by exact rational arithmetic for n=1..5 (`1/V(n+1) = 1 + 1/(2V(n))` matches at every step: n=1 → 7/4, n=2 → 15/8, n=3 → 31/16, n=4 → 63/32, n=5 → 127/64).

**IMPORTANT — the wrong recursion, NEVER used.** The dispatch's `V(n+1) = (1 + V(n))/2` is **mathematically inconsistent** with the verified closed form: it predicts `V(2) = (1 + 2/3)/2 = 5/6`, but `V(2) = 4/7` (verified by full enumeration). Setting `(1+V)/2 = 2V/(2V+1)` gives `2V^2 − V + 1 = 0`, discriminant `−7 < 0`: the two forms are *not* equivalent. The correct form is (R)/(M) above.

**Base case.** `V(1) = 2/3` is certified (L(1) + U(1)); `A(1) = 1/3`, `B(1) = 3`. ✓

**The value-level induction step — UN-CLOSED (honest gap).** To prove (M) as an *independent* value-level induction `n → n+1`, one would decompose the `(n+1)`-game as one round (Liu adds a mark, Xiang adds a mark) on top of an `n`-game and show the `+1` term in `1/A(n+1) = 2/A(n) + 1` is exactly the interleaving-boundary correction at `M`'s second-largest piece `= M/2` (the boundary case of the self-similar decomposition). **No potential accounting for this `+1` term is identified.** The obstruction is the same as Lemma L's interleaving (round 1, certified): the `(n+1)`-dyadic config = `[piece M] ∪ [scaled n-dyadic]`, but the global descending sort *interleaves* pieces from `M`'s sub-pieces and the small sub-config (the dyadic second-largest `= M/2` exactly is the boundary case), so additivity `V(n+1) = M + (1−M)·V(n)` does NOT hold cleanly — the `+1` term is precisely the non-additive correction.

**Honest assessment.** The value-recursion route is, on the current evidence, a **REPHRASING of (Lemma L + Lemma U) into one algebraic statement**, not a bypass: if both `L(n)` and `U(n)` hold for all `n`, then `V(n) = f(n)` for all `n` trivially, and (M) is the consequent identity. A slick *independent* value-level proof would need a potential that absorbs the global-sort interleaving correction into exactly `+1` in `1/A`-space; none is in hand. I flag (R)/(M) as the **unifying conjecture** — the right target, algebraically solid and numerically corroborated — and rely on the separate (L+U) closures from the sibling approaches for the actual proof.

---

### What a complete proof still requires
1. **Lemma L general-n, k≥2 sub-case** — close via per-round peeling (D1) or a WLOG-k=1 lemma (D2). Delegated to `pairing-partner`'s simultaneous-induction route (with `L*(n)` as the strengthened dual IH).
2. **Lemma U general-n** — the two-regime disjunctive invariant with the regime boundary at dyadic vs non-dyadic and the regime-N mechanism a sliver/shave (NOT `A ≤ 0`). Delegated to `two-regime-disjunctive`.
3. **(Optional) An independent value-level proof of (M)** — the `+1` interleaving correction. Un-closed; treated as a unifying conjecture, not a bypass.

Both Lemma L general-n and Lemma U general-n are honest open gaps, attacked by sibling approaches this round. The small-n verifications (Lemma S), the greedy reduction (Lemma G), the n=1 base cases for both bounds (L(1), U(1)), the k=0 sub-case of L(n+1), the k=1 reduction to `L*(n)`, the ΔA closed form, and the algebraic Mersenne identity (R)/(M) are all rigorous and load-bearing.

## Promotable lemmas
- **Lemma L(n+1), k=0 sub-case** (trivial dyadic-untouched case): if the `(n+1)`-dyadic's largest piece `M` receives 0 Xiang marks, then `S_odd ≥ M = f(n+1)`, with no induction. *Where proved*: this file, "Lemma L general-n / Sub-case k=0." Fully proved; reusable by any approach closing Lemma L (it disposes of the entire "0 marks in `M`" branch for free, sidestepping the interleaving obstruction). Small enough that it may not warrant a separate lemma file; recorded here for the reviewer to certify if useful.
- **Mersenne value-recursion identity (algebraic)** — `f(n) = 2^n/D(n)` satisfies `1/V(n+1) = 1 + 1/(2 V(n))` and `B(n+1) = 2 B(n)+1`. *Where proved*: this file, "The round-level value recursion." This is an *algebraic identity consequent on the closed form*, not a game-theoretic lemma; recorded as the unifying frame, NOT as a certified game lemma (it does not close a game-theoretic step).
- No NEW game-theoretic lemma certified this round: the substantive reusable lemmas on this route (`L*(n)`, the mirror certificate) belong to the sibling `pairing-partner` builder's lane and are pending certification there.
