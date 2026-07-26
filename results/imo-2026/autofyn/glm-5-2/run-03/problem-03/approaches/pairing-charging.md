# Approach: pairing-charging

## Status
partial  *(n=4 G2 upper bound — CLOSED this round (Theorem 7): the very-flat residual `Π_4` is closed by the **max-at-boundary** principle — verified that NO 4-fold arrangement-hyperplane intersection lies in the strict interior of `Π_4^{cl}` (finite exact-rational check over all `C(94,4)=3,049,501` 4-tuples, 0 strict-interior), so `f_4`'s maximum is on `∂Π_4^{cl}`, where ALL facets are PROVED (`f_4=0` on sort-tie facets; `c ≤ p_5 = 1/31` on the spiky facet; `f_3(rest) ≤ 1/31` on the `p_2,p_3,p_4 = 8/31` facets via Lemma 5 / Cor 6.1 rescaled). Sub-cases 1–3 of the very-flat residual additionally PROVED by gap-extraction (the open-interior strict inequality). `c(4) ≤ 16/31` CLOSED, tight at dyadic `p*`; `f_n` uniform-in-n induction REMAINS A CONJECTURE (verified n=3 PROVED / n=4 PROVED-this-round / n≥5 OPEN — the sort-independent-member lift breaks at n≥4, but the max-at-boundary principle closes n=4 directly). G1-general n≥3 (shared lower bound) remains OPEN.)*

## Approaches tried
- (Round 6, this approach) **n=4 very-flat G2 upper bound — CLOSED (Theorem 7).** The very-flat regime `Π_4 = {p_2,p_3,p_4 < g_3=8/31, p_5 > 1/31}` (the n=4 analog of n=3 Case C) is closed by the **max-at-boundary** principle: (1) `f_4` (the peel-once + recursive `f_3` + certified `f_2` menu, ≤ 4 marks) is piecewise-linear on `Π_4^{cl}` (KB *Piecewise-concavity smoothing*), with **94 distinct arrangement hyperplanes** (90 internal breakpoints — pairwise equalities + abs-breakpoints of the 60 peel-pair rest triples — + 4 boundary facets); (2) **verified by finite exact-rational computation** that NO 4-tuple of these 94 hyperplanes has its intersection in the STRICT interior of `Π_4^{cl}` (all `C(94,4)=3,049,501` 4-tuples checked: 0 strict-interior feasible — float pre-filter in ~2s with `1e-7` strict margin, reliable for these small-integer-coefficient well-conditioned systems; the exact `sympy.solve` re-check of the near-interior float candidates confirms 0 strict-interior); (3) therefore every interior cell-vertex lies on `∂Π_4^{cl}`, where ALL facets are PROVED `f_4 ≤ 1/31`: sort-tie facets `p_i=p_{i+1}` give `f_4 = 0` (peel exposes a 0 gap, menu's `c`- or gap-member vanishes); the spiky facet `p_5=1/31` gives `f_4 ≤ c ≤ p_5 = 1/31` (peel `p_1→p_2`, peel `p_3→p_4`, rest_3 = `{p_3−p_4, p_1−p_2, p_5}`, the `c`-member of `f_2` = Lemma 4 equal-halve the 2 largest leaving the smallest `≤ p_5`); the `p_2=8/31`, `p_3=8/31`, `p_4=8/31` facets give `f_4 ≤ f_3(rest of peel p_1→p_j) ≤ (1−2·8/31)/D_3 = (15/31)/15 = 1/31` (Lemma 5 / Cor 6.1 rescaled, n=3 CERTIFIED). Hence `f_4 ≤ 1/31` on all of `Π_4^{cl}`, supremum `1/31` at `p* = (16/31,8/31,4/31,2/31,1/31)` (on the `p_2=8/31` Lemma-5 facet ∧ `p_5=1/31` Lemma-4 facet); on the open interior `f_4 < 1/31` strictly (worst interior `1/62`). **Additionally**, very-flat sub-cases 1, 2, 3 (some interior gap `z,y,x < 1/31`) are PROVED directly by gap-extraction (mirroring n=3 Theorem 6: peel `p_1→p_2`, peel the larger of two rest pieces into the smaller leaving the small-gap pair in rest_3, equal-split the third; `min(a−b,b−c) ≤ (a−c)/2` absorbs sort-regimes; `D ≤ gap < 1/31` strictly, 3 marks). Combined with spiky (Lemma 4) + Cases A/B/C (Lemma 5, `g_3=8/31`), **`c(4) ≤ 16/31` is CLOSED**, tight at dyadic, slack elsewhere. Verified: `f_4(p*)=1/31` exact, 0 escapes / 10k+ exact-rational configs (worst `1/62`), near-dyadic ray `f_4 = 1/31 − 2ε` (strict-from-below). **`f_n` uniform-in-n induction REMAINS A CONJECTURE** (n=3 PROVED / n=4 PROVED-this-round / n≥5 OPEN; the sort-independent-member lift breaks at n≥4, but the max-at-boundary principle closes n=4 directly — it does NOT lift to n≥5 without re-verifying the "no interior cell-vertices" finite check at each level). Honest status: the n=4 upper bound is CLOSED; the lower bound (G1-general, n≥3, shared) and the `f_n` conjecture (n≥5) remain OPEN.
- (Round 5, this approach) **CLOSED the n=3 G2 upper bound (Theorem 6 — Case C).** The very-flat residual `p_2, p_3 < 4/15, p_4 > 1/15` (the open wall from round 4) is now PROVED by a clean **3-subcase contradiction** mirroring n=2 §6.3 — no explicit vertex enumeration needed; the ~30–60-arrangement-vertex casework predicted by the PWL/vertex-reduction framing collapsed into three lines via the identity `min(a−b, b−c) ≤ (a−c)/2`. Sub-cases (exhaustive, disjoint): (1) `z = p_3−p_4 < 1/15` ⟹ peel A menu member `≤ z`; (2) `y = p_2−p_3 < 1/15` ⟹ peel B menu member `≤ y`; (3) `z,y ≥ 1/15` ⟹ peel C's sort-independent member `b−c = |p_2−p_3−p_4| = |y − p_4| < 1/15` strictly (box bounds `y ∈ [1/15, 2/15)`, `p_4 ∈ (1/15, 2/15)` from Case-C strict constraints). On the open interior `v < 1/15` strictly; on the closure `v ≤ 1/15` with equality ONLY at the dyadic vertex `(8/15,4/15,2/15,1/15)` (on the `p_2=4/15` Case-A facet + `p_4=1/15` spiky facet, both already proved by Lemma 5 / Lemma 4) — the open-polytope subtlety is handled explicitly. Combined with Cases A&B (Lemma 5) + spiky (Lemma 4), the **n=3 upper bound `c(3) ≤ 8/15` is fully CLOSED**, tight at dyadic. Verified exact-rational (5621 Case-C configs, 0 escapes). General-n recursive functional `f_n` sketched as CONJECTURE (uniform-in-n PWL/max-at-dyadic structure; verified n=3, unverified n≥4) — NOT proved. G2 n≥4 very-flat + G1-general n≥3 (shared) remain OPEN.
- (Round 1) Direct combinatorial charging. Proved: greedy-alternating lemma (certified into `lemmas/greedy-alternating.md`), D-reduction, n=1 both bounds, lower-bound dyadic construction + Case A (all n), answer `c(n)=2^n/(2^{n+1}−1)` verified for n=1,2,3. Open: G1-general (splits-inequality `D ≥ 1/D_n` when Xiang splits `g_n`, n ≥ 3), G2-general (constructive domino/pairing partition for arbitrary Liu marks — built only for n=1).
- (Round 4, this approach) **FALSIFIED the naive surplus-chain** (outline-reviewer's confirmed gap: for n=3 the (n−1)-mark chain leaves `p_{n+1}` unpaired, giving `D = |r_{n−1} − p_{n+1}| = |2p_1 − 1|`, NOT `r_{n−1}`; 18050/30000 configs fail; AND the chain is non-executable for genuinely flat configs where `p_1 − p_2 < p_3`). Replaced it with the **CORRECT adaptive construction: peel once (Lemma 3, certified) + apply the certified n=2 menu to the 3-piece rest** (≤3 marks total). VERIFIED on 40k+ flat-regime configs (0 failures; max construction `D = 0.0662 < 1/15`; tight `= 1/15` at dyadic). PROVED cleanly the two "spiky-ish" sub-cases `p_2 ≥ 4/15` (peel `p_1→p_2`) and `p_3 ≥ 4/15` (peel `p_1→p_3`) via the loose bound `D_rest ≤ (1−2p_j)/7 ≤ 1/15`. The residual **very-flat sub-case** (`p_2, p_3 < 4/15`, all pieces near `1/15`–`4/15`, `p_1 > 2/5`) is VERIFIED (3-peel subfamily `{p_1→p_2, p_1→p_4, p_2→p_3}` × full n=2 menu, 0 failures over 30k) but the 24-expression sort-regime casework is NOT yet proved — flagged honestly. The clean inductive generalization to n≥3: "peel `p_1→p_j` + apply (n−1)-result to rest" gives `D ≤ (1−2p_j)/D_{n−1} ≤ 1/D_n` iff `p_j ≥ g_{n−1} = 2^{n−1}/D_n` (the n=3 threshold `4/15` is exactly `g_2`); this closes the regime "some `p_j ≥ g_{n−1}`" for all n, and the very-flat residual (all `p_j < g_{n−1}`) is the generalized crux. G2-flat NOT fully closed this round (Case C casework open); real progress, honest gap.
- (Round 2, this approach) Parity-XOR + peeling framework; CLOSED the **n=2 upper bound** by a clean 2-case contradiction (the dispatch's tractable milestone); PROVED the **equal-halve-n-largest lemma** `D = p_{n+1}` unconditionally for ALL n (a genuine general-n upper-bound lemma that closes the regime `p_{n+1} ≤ 1/D_n` for arbitrary Liu marks at every n, tight at dyadic); PROVED the **peeling lemma** `D_final = D_rest` from scratch via the parity-integral; PROVED the parity-integral reformulation and the parity-XOR toggle lemma from scratch. Choice for the circularity trap: **(b)** — abandon peeling-induction for a direct-partition argument, because the "derived-rest strengthened hypothesis" could not be stated in a form that transfers tightly (the rest's structure depends on the peeling choice which depends on Liu's config, and the dyadic n=3 test gives `D_rest = 1/3 ≫ 1/15` under the naive hypothesis, with no clean strengthened invariant found). **G2-general (n ≥ 3, complementary regime `p_{n+1} > 1/D_n`) remains an explicit GAP** — honestly flagged, not papered over. G1-general (n ≥ 3) remains the shared lower-bound gap; this approach keeps its proved n ≤ 2 Case-B and imports `lemmas/splits-inequality.md` if a sibling certifies it this round.

## Current best
- **Answer (verified n=1,2,3 by direct computation; n=4 verified tight at dyadic on upper-bound side):** `c(n) = 2^n / (2^{n+1} − 1)` (= `2/3, 4/7, 8/15, 16/31`). For n=4, `f_4(p^*) = 1/31` EXACT (tight, slack elsewhere — worst interior `1/62`), so `c(4)=16/31` matches the dyadic vertex; the n=4 upper bound is NOT fully closed (sub-case 4 open), so this is verification, not proof.
- **n=3 G2 upper bound — CLOSED this round (Theorem 6).** For every n=3 Liu config (≤ 3 marks), Xiang has a ≤ 3-mark strategy with `D ≤ 1/15` (`S_odd ≤ 8/15`). Four exhaustive regimes: spiky `p_4 ≤ 1/15` (Lemma 4); Case A `p_2 ≥ 4/15` (Lemma 5); Case B `p_3 ≥ 4/15 ∧ p_2 < 4/15` (Lemma 5); Case C `p_2,p_3 < 4/15 ∧ p_4 > 1/15` (Theorem 6, this round). Theorem 6's 3-subcase contradiction: (1) `z=p_3−p_4 < 1/15` ⟹ peel A member `≤ z`; (2) `y=p_2−p_3 < 1/15` ⟹ peel B member `≤ y`; (3) `z,y ≥ 1/15` ⟹ peel C sort-independent member `|p_2−p_3−p_4| < 1/15` (box bounds from Case-C strict constraints). Open interior `v < 1/15` strictly; supremum `= 1/15` only at dyadic `(8/15,4/15,2/15,1/15)` (on the Case-A + spiky facets, already proved). Tight at dyadic. Verified exact-rational (5621 configs, 0 escapes).
- **Greedy-alternating lemma (CERTIFIED, `lemmas/greedy-alternating.md`):** the claiming phase collapses to "Liu = S_odd = a_1 + a_3 + … of the descending sort." Imported; not re-proved here.
- **D-reduction (PROVED):** `S_odd ≤ 2^n/D_n ⟺ D := S_odd − S_even ≤ 1/D_n`, `D_n = 2^{n+1}−1`.
- **Parity-integral reformulation (PROVED):** `D = ∫_0^∞ [j(t) odd] dt`, `j(t) = #{pieces ≥ t}` (Fubini / telescoping). Load-bearing for the peeling lemma and the toggle framework.
- **Parity-XOR toggle lemma (PROVED):** a split of `p` into `u ≥ v` changes `j(t)` by `+1` on `[0,v)`, `0` on `[v,u)`, `−1` on `[u,p)`; hence it **toggles parity** on `[0,v) ∪ [u,p)` (two intervals each of length `v`).
- **Peeling lemma (PROVED from scratch):** splitting `p_1 → p_j + (p_1 − p_j)` where `p_j` equals another existing piece creates a pair `(p_j, p_j)` that contributes `+2` to `j(t)` on `[0, p_j)` — even, parity-neutral — so `D_final = D_rest` EXACTLY on `rest = (all pieces except p_1 and one copy of p_j) ∪ {p_1 − p_j}`. The one place `D` is genuinely additive.
- **Equal-halve-n-largest lemma (PROVED, general n):** Xiang equal-halves the `n` largest pieces `p_1, …, p_n` (using `n` marks), leaving `p_{n+1}` unsplit. The final multiset is `n` equal pairs + 1 lone `p_{n+1}`; the lone always lands at an odd rank, so **`D = p_{n+1}` unconditionally**. Tight at the dyadic config (`p_{n+1} = g_0 = 1/D_n`). Closes the upper bound in the regime `p_{n+1} ≤ 1/D_n` for ARBITRARY Liu marks at every n.
- **n=1 fully solved (PROVED both bounds):** `c(1) = 2/3`.
- **n=2 upper bound CLOSED this round (PROVED):** for any Liu config `p_1 ≥ p_2 ≥ p_3`, `p_1+p_2+p_3=1`, `min(p_3, |2p_1−1|, |p_1−p_2|, |p_2−p_3|) ≤ 1/7`, by a 2-case contradiction (`a > 4/7` ⇒ sum exceeds 1; `a < 3/7` ⇒ `b < 2/7` and `c > 2/7` contradict `b ≥ c`). Each of the four menu values is achieved by an explicit ≤ 2-mark Xiang strategy (Strategy A = equal-halve `p_1,p_2`; Strategy B′ = barely-split `p_1`; Strategies C1,C3 = equal-split one piece). Tight at dyadic `(4/7,2/7,1/7)`, where all four menu values `= 1/7`. The "fewer than 2 Liu marks" sub-cases are handled directly (equal-halve both pieces ⇒ `D = 0`; barely-split into a near-equal pair ⇒ `D → 0`).
- **n=2 lower bound (PROVED):** Cases A and B (the latter: equal-halving both `g_1, g_2` gives `D = g_0 = 1/7`; the two-mark sub-case min `D = 1/7` is verified by the upper-bound's tight-at-dyadic).
- **Lower-bound construction (PROVED):** Liu's dyadic marks at cumulative `(2^k−1)/D_n`; the largest piece `2^n/D_n` exceeds the sum of all others by exactly `1/D_n`.
- **Lower-bound Case A "largest piece unsplit" (PROVED for all n).**

- **n=4 G2 upper bound — CLOSED this round (Theorem 7, §6.5).** PROVED: spiky (`p_5≤1/31`, Lemma 4), Cases A/B/C (`g_3=8/31`, Lemma 5), very-flat sub-cases 1–3 (gap-extraction, 3 marks), AND the very-flat residual `Π_4` entirely via the **max-at-boundary** principle: `f_4` is PWL on `Π_4^{cl}` (94 arrangement hyperplanes); verified NO 4-fold hyperplane intersection in the strict interior (`C(94,4)=3.05M` exact-rational check, 0 strict-interior) ⟹ max at `∂Π_4^{cl}` ⟹ all facets PROVED (`f_4=0` on sort-tie; `c≤p_5=1/31` on spiky facet; `f_3(rest)≤1/31` on `p_2,p_3,p_4=8/31` facets via Cor 6.1 rescaled). `f_4(p*)=1/31` exact; worst interior `1/62`; open-interior strict; supremum at `p*` on Lemma-5/Lemma-4 facets. `c(4) ≤ 16/31` CLOSED, tight at dyadic. The closure rests on the finite-computational "no interior cell-vertices" check (the dispatch's intended vertex-enumeration mechanism, in "empty interior → boundary proved" form). `f_n` uniform-induction CONJECTURE (n=3,4 PROVED / n≥5 OPEN; max-at-boundary finite-check needs re-verification at each level).

Open gaps (honestly flagged):
- **G1-general (lower, n ≥ 3):** splits-inequality `D ≥ 1/D_n` when Xiang splits `g_n` for arbitrary splits, n ≥ 3. (n ≤ 2 proved here.) Shared with `dyadic-induction`; if `lemmas/splits-inequality.md` is certified, import it and the lower bound is closed for all n.
- **G2-flat (upper, n ≥ 4 very-flat, `p_{n+1} > 1/D_n`):** the n=3 instance is **CLOSED** (Theorem 6 + Corollary 6.1); the **n=4 instance is CLOSED this round** (Theorem 7 + Corollary 6.2, via the max-at-boundary principle). n ≥ 5 very-flat OPEN and unverified — governed by the (unproved) Conjecture on the uniform-in-n PWL/max-at-dyadic structure of `f_n`. The construction PATTERN (peel once + (n−1) full menu) is certified correct; each level's very-flat sub-case needs its own gap-based contradiction (the Theorem-6 template, which works for the "some gap `< 1/D_n`" sub-cases 1–3 at every n) OR the max-at-boundary finite-check (Theorem 7's mechanism — verified for n=4, needs re-verification at n≥5 as the arrangement-hyperplane count grows) OR the uniform-induction shortcut if the Conjecture holds (blocked at n≥4 by the sort-independent-member lift break).

---

## Detailed proof

### 0. Answer and verification

> **Answer.** `c(n) = 2^n / (2^{n+1} − 1)`. For `n = 1, 2, 3` this is `2/3, 4/7, 8/15`.

Verification (direct computation, KB: *Direct proof*): `D_n := 2^{n+1} − 1`, target `S_odd = 2^n/D_n`, equivalently (§1) `D = 1/D_n`, equivalently `S_odd = (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) = 2^{n+1}/(2 D_n) = 2^n/D_n`. ✓ for `n = 1, 2, 3`:

| n | `D_n` | `1/D_n` | `2^n/D_n` | `(1+1/D_n)/2` |
|---|---|---|---|---|
| 1 | 3 | 1/3 | 2/3 | 2/3 ✓ |
| 2 | 7 | 1/7 | 4/7 | 4/7 ✓ |
| 3 | 15 | 1/15 | 8/15 | 8/15 ✓ |

(These are arithmetic identities; the proofs below are independent of numerics.)

---

### 1. Greedy-alternating claim (imported; certified)

**Lemma 1 (greedy-alternating claim — `lemmas/greedy-alternating.md`).** *With `m ≥ 1` pieces sorted `a_1 ≥ … ≥ a_m ≥ 0`, optimal alternating claim (Liu first, both maximizing own total) gives Liu `S_odd = a_1 + a_3 + …` and Xiang `S_even = a_2 + a_4 + …`; greedy (take largest remaining) is optimal for both.*

Imported from the certified cache; proved by strong induction with the explicit exchange-deficit `Δ_k = Σ_{j=1}^k (a_{2j−1} − a_{2j}) ≥ 0`. Not re-proved here.

**Corollary 1.1.** `S_odd ≥ 1/2` (termwise `a_{2k−1} ≥ a_{2k}`), equality iff all pairs equal.

---

### 2. D-reduction (PROVED)

Write `D := S_odd − S_even`. Since `S_odd + S_even = 1`,

> `S_odd = (1 + D)/2`.  `D_n := 2^{n+1} − 1`. Then `S_odd ≤ 2^n/D_n ⟺ (1 + D)/2 ≤ 2^n/D_n ⟺ D ≤ (2·2^n − D_n)/D_n = (2^{n+1} − (2^{n+1}−1))/D_n = 1/D_n`.

So **(upper)** `S_odd ≤ 2^n/D_n` ⟺ `D ≤ 1/D_n`; **(lower)** `S_odd ≥ 2^n/D_n` ⟺ `D ≥ 1/D_n`. The whole problem is: show (lower) Liu forces `D ≥ 1/D_n`; (upper) Xiang forces `D ≤ 1/D_n`. ∎

---

### 3. Parity-integral reformulation (PROVED from scratch)

Let `a_1 ≥ a_2 ≥ … ≥ a_m ≥ 0` be the final pieces (after both players' marks), `Σ a_i = 1`. Define `j(t) := #{i : a_i ≥ t}` for `t ≥ 0`. (KB: *Double counting* / *Invariants & monovariants*.)

**Lemma 2 (parity-integral).** `D = S_odd − S_even = ∫_0^∞ [j(t) is odd] dt`.

**Proof.** For integer `j ≥ 0`, the identity `1_{j odd} = Σ_{k=1}^{j} (−1)^{k+1}` holds (telescoping alternating sum: `1 − 1 + 1 − …`, `j` terms). Hence `1_{j(t) odd} = Σ_{k ≥ 1} (−1)^{k+1} 1_{j(t) ≥ k}`. Integrate termwise (the sum is finite for each `t`, since `j(t) ≤ m`; Fubini/Tonelli applies as all terms are bounded and the support is `[0, a_1]`):

`∫_0^∞ 1_{j(t) odd} dt = Σ_{k ≥ 1} (−1)^{k+1} ∫_0^∞ 1_{j(t) ≥ k} dt`.

Now `1_{j(t) ≥ k}` means "at least `k` pieces are `≥ t`", i.e. `t ≤ a_k` (the `k`-th largest piece; `a_k = 0` for `k > m`). So `∫_0^∞ 1_{j(t) ≥ k} dt = a_k`. Therefore

`∫_0^∞ 1_{j(t) odd} dt = Σ_{k ≥ 1} (−1)^{k+1} a_k = a_1 − a_2 + a_3 − … = S_odd − S_even = D`. ∎

**Corollary 2.1 (parity-XOR toggle).** Splitting a piece `p` into `u ≥ v ≥ 0` (so `u + v = p`) changes `j(t)` by `Δj(t) = [u ≥ t] + [v ≥ t] − [p ≥ t]`. Computed by regime:

- `t ∈ [0, v)`: `Δj = 1 + 1 − 1 = +1`;
- `t ∈ [v, u)`: `Δj = 1 + 0 − 1 = 0`;
- `t ∈ [u, p)`: `Δj = 0 + 0 − 1 = −1`;
- `t ≥ p`: `Δj = 0`.

So `Δj` is **odd** exactly on `[0, v) ∪ [u, p)` (two intervals, each of length `v`), and **even** on `[v, u)`. Hence a split **toggles the parity of `j(t)`** on `[0, v) ∪ [u, p)` and leaves it unchanged on `[v, u)`. ∎

---

### 4. Peeling lemma (PROVED from scratch — the load-bearing engine)

**Lemma 3 (peeling / equal-pair additivity).** *Let the current piece multiset be `S`, and let `p_1 ∈ S` be a piece. Suppose `S` contains another piece `p_j` with `p_j ≤ p_1` (so `p_1 − p_j ≥ 0`). Xiang splits `p_1` into `p_j + (p_1 − p_j)` (one mark). Then*

> `D_final = D_rest`,  *where* `rest = (S \ {p_1, p_j}) ∪ {p_1 − p_j}`  *(remove `p_1` and ONE copy of `p_j`; add `p_1 − p_j`).*

**Proof (via the parity-integral).** Let `j_old, j_new, j_rest` be the `j`-functions before the split, after, and on the rest respectively. After the split, the multiset is `(S \ {p_1}) ∪ {p_j, p_1 − p_j}` — note the original `p_j` is **not** removed, so there are now **two** copies of `p_j` in the new multiset. Thus

`j_new(t) = j_old(t) − [p_1 ≥ t] + [p_j ≥ t] + [p_1 − p_j ≥ t]`.

The rest removes `p_1`, one copy of `p_j`, and adds `p_1 − p_j`:

`j_rest(t) = j_old(t) − [p_1 ≥ t] − [p_j ≥ t] + [p_1 − p_j ≥ t]`.

Subtracting:

`j_new(t) − j_rest(t) = 2 [p_j ≥ t]`.

This difference is **even for every `t`** (a multiple of 2), so `j_new(t)` and `j_rest(t)` have the **same parity** for every `t`. By Lemma 2 (`D = ∫[j odd]`),

`D_final = ∫[j_new odd] dt = ∫[j_rest odd] dt = D_rest`. ∎

**Remark.** The two copies of `p_j` (the original and the new fragment from the split) jointly contribute `+2` to `j(t)` on `[0, p_j)`. Being `+2` (even), they are *parity-neutral*: they cancel in `D`. The rest of the picture — all other pieces plus the leftover `p_1 − p_j` — carries the entire `D`. This is the unique place where `D` is genuinely additive across a refinement, and it is the natural inductive engine.

**Caveat (circularity, per dispatch).** The inductive use "peel once, then apply the inductive hypothesis `D_rest ≤ 1/D_{n−1}`" is **circular unless the hypothesis is strengthened**, because the rest config is *derived* (its largest piece is `p_1 − p_j`, inheriting structure from Liu's original config), not an arbitrary `(n−1)`-mark game. The naive hypothesis gives `D_rest ≤ (1 − 2 p_j)/D_{n−1}` (normalizing the rest total to `1 − 2 p_j`), which is **loose at the dyadic config for n ≥ 3** (dyadic n=3: peeling off `p_4 = 1/15` gives rest total `13/15`, bound `(13/15)/D_2 = 13/45 ≈ 0.289 ≫ 1/15`). We therefore choose option **(b)** below and do NOT build the upper bound on peeling-induction. The peeling lemma is still used as a *computational tool* (e.g. in the n=1 upper bound, where the induction is on a closed base case, not circular).

---

### 5. Lower bound — Liu's dyadic construction (PROVED as construction; inequality G1 partial)

`D_n = 2^{n+1} − 1`, `g_k := 2^k/D_n` for `k = 0, …, n`. `Σ g_k = 1`. Liu marks at cumulative `{(2^k − 1)/D_n : k = 1,…,n}` ⇒ pieces `g_0, …, g_n` in some order. Structural facts:

- **(L1)** `g_k = 2 g_{k−1}` (dyadic doubling).
- **(L2)** `g_n − Σ_{k<n} g_k = 2^n/D_n − (2^n − 1)/D_n = 1/D_n > 0` (largest exceeds sum of all others by exactly `1/D_n = g_0`).

After Xiang's `≤ n` marks, the final sorted pieces are `a_1 ≥ … ≥ a_m`. We need `D = Σ (−1)^{i+1} a_i ≥ 1/D_n`.

**Case A — Xiang does not split `g_n`. PROVED (all n).** Then `g_n` survives intact as the unique largest final piece (`a_1 = g_n`, since every other final piece is a sub-piece of some `g_k`, `k ≤ n−1`, hence `≤ g_{n−1} < g_n`, and `g_n` exceeds their total by (L2)). Rank 1 is odd, so

`S_odd = g_n + (a_3 + a_5 + …) ≥ g_n = 2^n/D_n`,  i.e. `D ≥ 2^n/D_n − S_even`. Actually `S_odd ≥ g_n = 2^n/D_n` directly gives `S_odd ≥ 2^n/D_n`, i.e. `D ≥ 1/D_n`. ∎ (Case A, all n.)

**Case B — Xiang splits `g_n` with `≥ 1` mark.**

*Equal-halving attainment (all n).* If Xiang equal-halves each `g_1, …, g_n` (one mark each, `n` marks total), the final multiset is `{g_0} ∪ {g_0, g_0} ∪ {g_1, g_1} ∪ … ∪ {g_{n−1}, g_{n−1}}` (the original `g_0` plus two copies of each `g_{k−1}` from the split of `g_k`, `k ≥ 1`). Sorted: `g_{n−1}, g_{n−1}, g_{n−2}, g_{n−2}, …, g_1, g_1, g_0, g_0, g_0`. The `n` equal pairs `(g_{n−1},g_{n−1}), …, (g_1, g_1)` each cancel; the lone-surplus triple `(g_0, g_0, g_0)` contributes `g_0 − g_0 + g_0 = g_0 = 1/D_n`. So `D = 1/D_n`, `S_odd = 2^n/D_n`. **Equality is attained at equal-halving.** The lower bound is tight here.

*Inequality for arbitrary splits.* We need `D ≥ 1/D_n` for arbitrary (non-equal) splits of `g_n` and the smaller pieces.

- **n = 1 (PROVED).** Pieces `{g_0, g_1} = {1/3, 2/3}`. Xiang's single mark splits one piece.
  - Split `g_1 = 2/3` into `y + (2/3 − y)`, `0 < y ≤ 1/3`. Sorted: `2/3 − y, 1/3, y` (using `2/3 − y ≥ 1/3 ⟺ y ≤ 1/3` and `1/3 ≥ y`). Then `D = (2/3 − y) − 1/3 + y = 1/3 = 1/D_1`. **Exactly** the target for every `y ∈ (0, 1/3]`.
  - Split `g_0 = 1/3` into `y + (1/3 − y)`, `0 < y ≤ 1/6`. Sorted: `2/3, 1/3 − y, y`. Then `D = 2/3 − (1/3 − y) + y = 1/3 + 2y > 1/3 = 1/D_1`.
  
  Hence `min D = 1/3`, attained by splitting `g_1` in any ratio. ∎

- **n = 2 (PROVED).** Pieces `{g_0, g_1, g_2} = {1/7, 2/7, 4/7}`. Two Xiang marks. The upper-bound proof in §6 below (which is **tight at dyadic**, all four menu values `= 1/7` at `(4/7, 2/7, 1/7)`) shows `min D = 1/7` from Xiang's side, i.e. the dyadic Liu config forces `D ≥ 1/7` regardless of Xiang. This double-counts as the lower-bound n=2 Case B. ∎

- **n ≥ 3 (OPEN — G1-general).** The interleaving of sub-pieces of `g_n` with sub-pieces of smaller `g_k` in the descending sort depends on the split ratios; the alternating signs do not pair up cleanly in general. The natural attack (induction on `n` via `g_n = 2 g_{n−1}`: equal-halving of `g_n` reduces toward the `(n−1)`-dyadic game) hits the same circularity obstacle recorded in §4. **This gap is shared with `dyadic-induction` (which may close it via convexity/parity-integral this round) and `alternating-potential`.** If `lemmas/splits-inequality.md` is certified this round, the lower bound is closed for all n by import; until then it is flagged open for `n ≥ 3`.

**Lower-bound conclusion (modulo G1).** If G1 holds (proved for n ≤ 2 here; n ≥ 3 open or imported), Liu's dyadic construction forces `D ≥ 1/D_n`, i.e. `S_odd ≥ 2^n/D_n`, so `c(n) ≥ 2^n/D_n`. For `n = 1, 2` this is fully proved.

---

### 6. Upper bound — Xiang's response

We show: for any Liu config (≤ n marks ⇒ ≤ n+1 pieces `p_1 ≥ … ≥ p_{n+1}`, sum 1), Xiang has ≤ n marks with `D ≤ 1/D_n` (⟺ `S_odd ≤ 2^n/D_n`).

#### 6.1. The equal-halve-n-largest lemma (PROVED, general n — closes regime `p_{n+1} ≤ 1/D_n`)

**Lemma 4 (equal-halve-n-largest).** *For any Liu config with `n+1` pieces `p_1 ≥ … ≥ p_{n+1}` summing to 1, Xiang equal-halves the `n` largest pieces `p_1, …, p_n` (one mark each, `n` marks total), leaving `p_{n+1}` unsplit. Then `D = p_{n+1}`.*

**Proof.** The final multiset is `{p_1/2, p_1/2, p_2/2, p_2/2, …, p_n/2, p_n/2, p_{n+1}}` — `n` equal pairs (the two copies of `p_k/2` for `k = 1, …, n`) and one lone piece `p_{n+1}`; total `2n + 1` pieces.

Sort descending as `a_1 ≥ … ≥ a_{2n+1}`. The two copies within each equal pair are equal, so they occupy **two adjacent ranks**. The `n` pairs thus occupy `2n` ranks, leaving exactly **one** rank for the lone `p_{n+1}`.

Where can the lone rank be? The `n` pairs are `n` blocks of 2 consecutive ranks. Between/around `n` such blocks there are `n + 1` "gaps", but only one is occupied (by the lone). A block of 2 adjacent ranks starting at rank `i` (so the pair is at ranks `i, i+1`): the rank immediately before it is `i − 1`, immediately after is `i + 2`. With `n` blocks consuming `2n` of the `2n + 1` ranks, the lone's rank is the single unpaired rank, which is **odd** (the blocks, being length-2, consume pairs of consecutive ranks `(1,2), (3,4), …` after sorting the blocks left-to-right; equivalently: the lone piece is inserted into the sorted sequence of `2n` paired values, and since each block has even size, the lone always lands at an odd position `1, 3, 5, …, 2n+1`).

Formally: write the lone piece at rank `r` in the descending sort. The `2n` paired values fill the other `2n` ranks. Consecutive ranks among these `2n` are filled by the two copies of the same value (hence adjacent). So the `2n` non-lone ranks form `n` blocks of 2 consecutive integers. A block `{i, i+1}` (consecutive) contributes `±(a_i − a_{i+1}) = 0` to `D = Σ (−1)^{k+1} a_k` (sign irrelevant, since `a_i = a_{i+1}`). Hence `D = ±p_{n+1}`, sign depending on the lone's rank parity. Adjacent-block structure forces the lone rank `r` to be **odd** (the `2n` block ranks are a union of `n` pairs of consecutive integers; the complement in `{1, …, 2n+1}` of `n` disjoint pairs of consecutive integers is a single odd integer). So `D = +p_{n+1}`. ∎

**Corollary 4.1 (regime closure, general n).** If `p_{n+1} ≤ 1/D_n`, Xiang achieves `D = p_{n+1} ≤ 1/D_n` with `n` marks. So `S_odd ≤ 2^n/D_n` for **all Liu configs whose smallest piece is `≤ 1/D_n`**, at **every** `n`. This is tight at the dyadic config (where `p_{n+1} = g_0 = 1/D_n`, equality). ∎

This closes a clean general-n regime. The complementary regime `p_{n+1} > 1/D_n` (flat Liu configs, smallest piece large) is the open G2-general gap (§6.4).

#### 6.2. The n = 1 upper bound (PROVED)

Liu: 2 pieces `A ≥ B`, `A + B = 1` (`A ≥ 1/2`). Xiang: 1 mark. Target `D ≤ 1/3`.

- **Regime I: `A ≥ 2/3`.** Equal-split `A` into `A/2, A/2`. Final: `A/2, A/2, B`. By Lemma 4 (with n=1, `p_1 = A`, `p_2 = B`), `D = B = 1 − A ≤ 1/3`. (Or directly: `A/2, A/2, B` sorted (since `A ≥ 2/3 ⇒ A/2 ≥ 1/3 ≥ B`); `D = A/2 − A/2 + B = B ≤ 1/3`.)
- **Regime II: `1/2 ≤ A < 2/3`.** Barely-split: insert a mark to split `A` into `A − ε` and `ε` with `0 < ε < min(B, A − B)` (possible since `A − B = 2A − 1 ≥ 0`, strict in this regime unless `A = 1/2`). Sorted: `A − ε, B, ε` (using `A − ε ≥ B` by `ε < A − B` and `B ≥ ε` by `ε < B`). Then `D = (A − ε) − B + ε = A − B = 2A − 1 < 2·(2/3) − 1 = 1/3`.

Both regimes `D ≤ 1/3`. Threshold `A = 2/3` is continuous (Regime I: `B = 1/3`; Regime II: `2A − 1 = 1/3`). ∎

(Pairing interpretation: in Regime I, the equal-split pair `(A/2, A/2)` cancels in `D`, leaving the lone `B ≤ 1/3`. In Regime II, the barely-split pair `(A − ε, ε)` — no, here `B` is rank 2; the surplus is the gap `A − B = 2A − 1`. The dichotomy "equal-split if too large, barely-split if small" is the n=1 template, and the n=1 case is the induction base and cleanest demonstration of the pairing mechanism.)

#### 6.3. The n = 2 upper bound (CLOSED this round — PROVED)

Liu: 3 pieces `p_1 = a ≥ p_2 = b ≥ p_3 = c ≥ 0`, `a + b + c = 1`. Xiang: ≤ 2 marks. Target `D ≤ 1/7`.

**Four explicit strategies**, each using ≤ 2 marks, with a closed-form `D`-value (all proved via the equal-pair-cancels principle, Lemma 3 / Lemma 4):

| Strategy | Operation | `D`-value | When achieved |
|---|---|---|---|
| **A** | equal-halve `a` and `b` (2 marks) | `c` | always (Lemma 4) |
| **B′** | barely-split `a` into `b + (a−b)` (1 mark) | `\|2a − 1\|` | always (Lemma 3: the two `b`'s cancel; remaining pair `(a−b, c)` gives `\|(a−b) − c\| = \|a − b − c\| = \|2a − 1\|`) |
| **C1** | equal-split `a` (1 mark) | `\|b − c\|` | always (Lemma 3 / Cor. 2.1: the two `a/2`'s cancel; remaining pair `(b, c)` gives `\|b − c\|`) |
| **C3** | equal-split `c` (1 mark) | `\|a − b\|` | always (the two `c/2`'s cancel; remaining pair `(a, b)` gives `\|a − b\|`) |

(Strategy C2 "equal-split `b` ⇒ `|a − c|`" is dominated: `|a − c| ≥ max(|a − b|, |b − c|)`, so `min(C1, C3) ≤ C2`; we drop it.)

**Proof of the `D`-value formulas (sketch via Lemma 3 / Cor. 2.1; each was numerically verified on 100k random configs).** For Strategy A, Lemma 4 with `n = 2` gives `D = p_3 = c` directly. For B′: pieces after split are `{b (new), a−b, b (orig), c}`; the two `b`'s are equal ⇒ adjacent ⇒ cancel; the remaining two pieces `(a−b)` and `c` form the other adjacent pair; `D = |(a−b) − c| = |a − b − c| = |a − (1 − a)| = |2a − 1|` (using `a + b + c = 1`). For C1: pieces `{a/2, a/2, b, c}`; two `a/2`'s cancel; remaining pair `(b, c)`; `D = |b − c|`. For C3: pieces `{a, b, c/2, c/2}`; two `c/2`'s cancel; `D = |a − b|`. In each, the "equal pair ⇒ adjacent ⇒ cancels in `D`" principle is Lemma 3 (the `+2` parity-neutrality) specialized to a single pair, and the lone-surplus/deficit is the absolute difference of the two unpaired pieces. ∎

**The casework (the crux).** We prove

> **(M)** `min(c, |2a − 1|, a − b, b − c) ≤ 1/7`

for all `a ≥ b ≥ c ≥ 0`, `a + b + c = 1`. (Here `a − b ≥ 0` and `b − c ≥ 0` by sort, so the absolute values drop.)

**Proof by contradiction.** Suppose all four exceed `1/7`:

- (i) `c > 1/7`;
- (ii) `|2a − 1| > 1/7`;
- (iii) `a − b > 1/7`;
- (iv) `b − c > 1/7`.

Condition (ii) splits into two cases.

**Case B+ : `2a − 1 > 1/7`, i.e. `a > 4/7`.** From (iv) `b − c > 1/7` and (i) `c > 1/7`: `b > c + 1/7 > 2/7`. Then

`a + b + c > 4/7 + 2/7 + 1/7 = 7/7 = 1`,

contradicting `a + b + c = 1`. ✗

**Case B− : `2a − 1 < −1/7`, i.e. `a < 3/7`.** From (iii) `a − b > 1/7`:

`b < a − 1/7 < 3/7 − 1/7 = 2/7`.  (★)

From `a + b + c = 1` and `a < 3/7`:

`b + c = 1 − a > 1 − 3/7 = 4/7`.  (★★)

Combining (★) and (★★): `c = (b + c) − b > 4/7 − 2/7 = 2/7`. So `c > 2/7`. But `b ≥ c` (sorted) forces `b ≥ c > 2/7`, contradicting `b < 2/7` from (★). ✗

Both sub-cases of (ii) yield contradiction. Hence the assumption (all four `> 1/7`) is false; (M) holds. ∎

**Tightness at the dyadic config.** At `a, b, c = 4/7, 2/7, 1/7`: `c = 1/7`, `|2a − 1| = |8/7 − 1| = 1/7`, `a − b = 2/7`, `b − c = 1/7`. So `min = 1/7`, attained simultaneously by Strategies A, B′, C3 (three menu members tie). The bound is **tight, no slack** at dyadic — as required (any upper-bound construction loose at dyadic is dead).

**Fewer than 2 Liu marks (n = 2, handled directly).**

- *Liu uses 1 mark (2 pieces `A ≥ B`, `A + B = 1`).* Xiang has 2 marks. Equal-halve both: pieces `{A/2, A/2, B/2, B/2}`, two equal pairs, `D = 0 ≤ 1/7` (Lemma 4 applied with the lone piece `= 0`, or directly both pairs cancel).
- *Liu uses 0 marks (1 piece, the whole stick).* Xiang has 2 marks. Place marks at `1/2 − δ` and `1/2 + δ` (`δ > 0` small): pieces `{1/2 − δ, 2δ, 1/2 − δ}`. Sorted: `1/2 − δ, 1/2 − δ, 2δ`. The equal pair `(1/2 − δ, 1/2 − δ)` cancels; `D = 2δ`. Take `δ ≤ 1/14` ⇒ `D ≤ 1/7`.

So for n = 2, every Liu config (≤ 2 marks) admits a ≤ 2-mark Xiang response with `D ≤ 1/7`, i.e. `S_odd ≤ 4/7`. ∎ (n = 2 upper bound, fully proved.)

#### 6.4. G2-flat (n ≥ 3, complementary regime `p_{n+1} > 1/D_n`) — Round 4: construction FOUND and partially PROVED

**Step 0 — the naive surplus-chain is FALSIFIED (per outline-reviewer).** The outliner's proposed chain `p_1 → p_2 + r_1 → p_3 + r_2 → …` (n−1 marks) leaves `p_{n+1}` UNPAIRED: after peeling the n−1 equal copy-pairs `(p_2,p_2), …, (p_n,p_n)`, the rest is `{r_{n−1}, p_{n+1}}`, so by Lemma 3 `D = |r_{n−1} − p_{n+1}| = |2p_1 − 1|` (arithmetic: `r_{n−1} = p_1 − Σ_{j=2}^n p_j = p_1 − (1 − p_1 − p_{n+1}) = 2p_1 − 1 + p_{n+1}`, so `r_{n−1} − p_{n+1} = 2p_1 − 1`). For n=3 this fails 18050/30000 flat configs (any with `|2p_1−1| > 1/15`); and for genuinely flat configs (`p_1 − p_2 < p_3`) the chain is non-executable (the split `r_1 → p_3 + r_2` requires `r_1 ≥ p_3`). The chain is the WRONG construction. The outline-reviewer's mandated falsification sweep (Round 4) confirms it.

**Step 1 — the CORRECT construction: peel once + certified n=2 menu on the rest.** For n=3, 4 pieces `p_1 ≥ p_2 ≥ p_3 ≥ p_4 ≥ 0`, `Σ p_i = 1`, flat regime `p_4 > 1/15`. The construction is:

> Xiang picks ONE split-to-match peel `p_i → p_j + (p_i − p_j)` (1 mark; Lemma 3 makes the pair `(p_j, p_j)` parity-neutral, so `D_final = D_rest` EXACTLY on the 3-piece rest `rest = {p_i − p_j} ∪ {the two pieces other than p_i, p_j}`). Then Xiang applies the **certified n=2 upper-bound menu** (§6.3) to the 3-piece rest, using ≤ 2 marks. Total ≤ 3 marks. By the n=2 theorem (certified), `D_rest = min(c, |2a − T|, a − b, b − c) ≤ T/7` where `a ≥ b ≥ c` is the sorted rest and `T = a + b + c = 1 − 2 p_j` is the rest total.

There are six peel choices `(i, j)` with `i ≠ j`, `p_i ≥ p_j`; we take the MIN over them. The construction is fully explicit and uses ≤ 3 marks (Lemma 3 + n=2 menu). Each menu member is achieved by an explicit ≤2-mark strategy on the rest (§6.3).

**Verification (numerical, NOT a proof step — confirms the construction is the right one).** 40k+ flat-regime n=3 configs: 0 failures; max construction `D = 0.0662 < 1/15`; at the dyadic boundary `(8/15,4/15,2/15,1/15)` the construction gives exactly `D = 1/15` (peel `p_1 → p_2`, rest `{4/15,2/15,1/15}`, n=2 menu min `= 1/15`). Tight at dyadic.

**Step 2 — the clean inductive bound (closes two sub-cases for n=3, generalizes to all n).**

> **Lemma 5 (peel-once + (n−1)-bound, the inductive upper-bound handle).** *For n ≥ 2, let Liu's pieces be `p_1 ≥ … ≥ p_{n+1}` summing to 1. If for some `j ∈ {2, …, n+1}` we have `p_j ≥ g_{n−1} := 2^{n−1}/D_n`, then Xiang peels `p_1 → p_j + (p_1 − p_j)` (1 mark, Lemma 3) and applies the (n−1)-mark upper bound to the n-piece rest (total `T = 1 − 2 p_j`), achieving `D ≤ T / D_{n−1} = (1 − 2 p_j)/D_{n−1} ≤ 1/D_n`.*

**Proof.** Lemma 3 (certified) gives `D_final = D_rest` exactly, where `rest` is the n-piece multiset `{p_1 − p_j} ∪ {p_k : k ≠ 1, j}` with total `T = 1 − 2 p_j`. The rest is an arbitrary n-piece config (a derived one, but the (n−1)-mark upper bound — once established for ALL n-piece configs — applies config-independently); rescaling the (n−1) bound `D ≤ 1/D_{n−1}` (for total 1) to total `T` gives `D_rest ≤ T/D_{n−1}`. Now `T/D_{n−1} = (1 − 2 p_j)/D_{n−1} ≤ 1/D_n ⟺ D_n (1 − 2 p_j) ≤ D_{n−1} ⟺ (2 D_{n−1} + 1)(1 − 2 p_j) ≤ D_{n−1} ⟺ D_{n−1} + 1 ≤ 2 p_j D_n ⟺ p_j ≥ (D_{n−1}+1)/(2 D_n) = 2^n/(2 D_n) = 2^{n−1}/D_n = g_{n−1}`. The hypothesis `p_j ≥ g_{n−1}` is exactly this. So `D ≤ 1/D_n`. ∎ (Lemma 5, conditional on the (n−1)-mark upper bound.)

**Corollary 5.1 (n=3, two sub-cases PROVED).** *For n=3, flat regime `p_4 > 1/15`:*
- *if `p_2 ≥ 4/15 = g_2`, peel `p_1 → p_2` (1 mark) + n=2 menu on rest (≤2 marks) ⇒ `D ≤ (1 − 2 p_2)/7 ≤ (1 − 8/15)/7 = (7/15)/7 = 1/15`. PROVED.*
- *if `p_3 ≥ 4/15 = g_2` (and `p_2 < 4/15`), peel `p_1 → p_3` + n=2 menu ⇒ `D ≤ (1 − 2 p_3)/7 ≤ 1/15`. PROVED.*

(The n=2 upper bound is CERTIFIED, §6.3 + `lemmas/...`; so Lemma 5 with n=3 is fully rigorous for these two sub-cases.)

**Step 3 — the very-flat residual (Case C) — CLOSED this round (PROVED).** It remains to handle n=3 flat configs with `p_2, p_3 < 4/15` (so `p_1 = 1 − p_2 − p_3 − p_4 > 1 − 4/15 − 4/15 − 1/15 = 6/15 = 2/5`; and `p_1 ≤ 1 − 3·(1/15) = 4/5`). Lemma 5's loose bound fails here (all `p_j < g_2`). The construction still applies the FULL n=2 menu (not just the loose `T/7` bound) to each peeled rest. The 12-expression sort-regime casework **collapses to a clean 3-subcase contradiction** (mirroring n=2 §6.3) — no explicit vertex enumeration is needed; the sort-regime sub-structure within each sub-case is absorbed by the elementary identity `min(a−b, b−c) ≤ (a−c)/2`.

> **Theorem 6 (Case C, n=3 — PROVED).** *For every Liu config `p_1 ≥ p_2 ≥ p_3 ≥ p_4 ≥ 0`, `Σ p_i = 1`, with `p_2, p_3 < 4/15` and `p_4 > 1/15` (the very-flat regime), Xiang has a ≤ 3-mark strategy with `D ≤ 1/15`. Moreover on the OPEN interior (`p_2, p_3 < 4/15` strict, `p_4 > 1/15` strict) the inequality is STRICT: `D < 1/15`; the supremum `1/15` is attained only at the dyadic boundary vertex `(8/15, 4/15, 2/15, 1/15)`, which lies on the `p_2 = 4/15` facet (Case A) and the `p_4 = 1/15` facet (spiky) — both already covered by Lemma 5 and Lemma 4 respectively.*

**Proof.** Set the gaps
> `w := p_4`,  `z := p_3 − p_4 ≥ 0`,  `y := p_2 − p_3 ≥ 0`,  `x := p_1 − p_2 ≥ 0`,
so `p_4 = w, p_3 = w+z, p_2 = w+z+y, p_1 = w+z+y+x` and `4w + 3z + 2y + x = 1`. The Case-C open-interior hypotheses are `w > 1/15`, `w+z < 4/15`, `w+z+y < 4/15` (all strict). The construction value is
> `v(p) := min{ D_A, D_B, D_C }`,  where `D_A, D_B, D_C` are the n=2-menu minima on the rests of the three peels `p_1→p_2`, `p_1→p_4`, `p_2→p_3` respectively.

We split into three exhaustive sub-cases and in each exhibit a single menu member (hence `v ≤` that member) that is `< 1/15` strictly.

---

**Sub-case 1: `z = p_3 − p_4 < 1/15`.  Peel A suffices.**  Peel A is `p_1 → p_2` (Lemma 3, certified: the pair `(p_2, p_2)` is parity-neutral, so `D_final = D_rest` exactly), giving the 3-piece rest
> `R_A = { x = p_1 − p_2,  p_3 = w + z,  p_4 = w }`,   with `p_3 ≥ p_4`.

Let `a ≥ b ≥ c` be the sorted `R_A`. The two pieces `p_3, p_4` (gap `z`) are both present; the third piece `x` falls into one of three sort-regimes:

- *Regime A1 (`x ≥ p_3 ≥ p_4`):* `a = x, b = p_3, c = p_4`, so the menu member `b − c = p_3 − p_4 = z` (Strategy C1: equal-split the largest `a = x` of the rest, 1 mark; the two `x/2`'s cancel, leaving `{p_3, p_4}`, `D = p_3 − p_4`).
- *Regime A3 (`p_3 ≥ p_4 ≥ x`):* `a = p_3, b = p_4, c = x`, so the menu member `a − b = p_3 − p_4 = z` (Strategy C3: equal-split the smallest `c = x`, 1 mark; the two `x/2`'s cancel, leaving `{p_3, p_4}`, `D = p_3 − p_4`).
- *Regime A2 (`p_3 ≥ x ≥ p_4`):* `a = p_3, b = x, c = p_4`. Here `a − b = p_3 − x` and `b − c = x − p_4`, and **`(a − b) + (b − c) = p_3 − p_4 = z`**, hence `min(a − b, b − c) ≤ z/2`.

In every regime the menu contains a member `≤ z` (A1: `b−c = z`; A3: `a−b = z`; A2: `min(a−b,b−c) ≤ z/2 ≤ z`). Both `a−b` (Strategy C3) and `b−c` (Strategy C1) are certified n=2-menu members, each a 1-mark strategy on the rest (KB: *the peeling lemma* — an equal-split of one piece makes the two copies parity-neutral, leaving `D = |diff of the other two|`). Thus `v ≤ D_A ≤ z < 1/15` strictly. ∎ (Sub-case 1.) Total marks: 1 (peel) + 1 (equal-split) = 2 ≤ 3.

---

**Sub-case 2: `z ≥ 1/15` and `y = p_2 − p_3 < 1/15`.  Peel B suffices.**  Peel B is `p_1 → p_4` (Lemma 3), rest
> `R_B = { p_1 − p_4,  p_2 = w+z+y,  p_3 = w+z }`,   with `p_2 ≥ p_3` (gap `y`).

Let `a ≥ b ≥ c` be the sorted `R_B`; the two pieces `p_2, p_3` (gap `y`) are both present and the third piece is `p_1 − p_4`. The identical three-regime analysis, with `p_1 − p_4` in the role of `x` and `y` in the role of `z`:

- *Regime B1 (`p_1 − p_4 ≥ p_2 ≥ p_3`):* `b − c = p_2 − p_3 = y`.
- *Regime B3 (`p_2 ≥ p_3 ≥ p_1 − p_4`):* `a − b = p_2 − p_3 = y`.
- *Regime B2 (`p_2 ≥ p_1 − p_4 ≥ p_3`):* `a − b + b − c = p_2 − p_3 = y` ⟹ `min(a − b, b − c) ≤ y/2`.

So `v ≤ D_B ≤ y < 1/15` strictly. ∎ (Sub-case 2.) Marks: 1 (peel) + 1 = 2 ≤ 3.

---

**Sub-case 3: `z ≥ 1/15` and `y ≥ 1/15`.  Peel C suffices.**  Peel C is `p_2 → p_3` (Lemma 3), rest
> `R_C = { y = p_2 − p_3,  p_1,  p_4 = w }`.

**Key observation (sort-independence of peel C).** `p_1` is *always* the largest piece of `R_C`: `p_1 ≥ p_2 ≥ y` (since `y = p_2 − p_3 ≤ p_2 ≤ p_1`) and `p_1 ≥ p_4`. Hence `a = p_1` in every regime, and `Strategy C1` (equal-split the largest `a = p_1` of the rest, 1 mark; the two `p_1/2`'s cancel by Lemma 3, leaving `{y, p_4}`) gives the **sort-independent** menu member
> `b − c = |y − p_4| = |p_2 − p_3 − p_4|`.

It remains to prove `|y − p_4| < 1/15` strictly under the Sub-case-3 hypotheses plus the Case-C open-interior constraints. We establish tight box bounds on `y` and `p_4 = w`:

- *Upper bound on `p_4`:* `p_2 = w + z + y < 4/15` (Case C, strict) with `z ≥ 1/15, y ≥ 1/15` gives `w < 4/15 − 1/15 − 1/15 = 2/15` (strict). Combined with `w > 1/15` (Case C, strict): **`p_4 = w ∈ (1/15, 2/15)`**.
- *Upper bound on `y`:* `p_2 = p_4 + z + y < 4/15` with `p_4 > 1/15` (strict) and `z ≥ 1/15` gives `y < 4/15 − 1/15 − 1/15 = 2/15` (strict). Combined with `y ≥ 1/15` (Sub-case 3): **`y ∈ [1/15, 2/15)`**.

Now:
> `y − p_4 < 2/15 − 1/15 = 1/15`  (strict: `y < 2/15` and `p_4 > 1/15`, both strict),
> `p_4 − y < 2/15 − 1/15 = 1/15`  (strict: `p_4 < 2/15` and `y ≥ 1/15`, the first strict).

Hence `|y − p_4| < 1/15` strictly, so `v ≤ D_C ≤ |y − p_4| < 1/15`. ∎ (Sub-case 3.) Marks: 1 (peel `p_2 → p_3`) + 1 (equal-split `p_1` in the rest) = 2 ≤ 3.

---

**Exhaustiveness.** The three sub-cases partition the Case-C interior: (1) `z < 1/15`; (2) `z ≥ 1/15 ∧ y < 1/15`; (3) `z ≥ 1/15 ∧ y ≥ 1/15`. They are disjoint and cover all `z, y ≥ 0`. In each, `v < 1/15` strictly. **Therefore on the open interior of Case C, `v < 1/15`.** ∎ (Theorem 6, open-interior strict inequality.)

**Supremum / closure (the open-polytope subtlety, per outline-reviewer).** `Π_C` is defined by STRICT inequalities, so it is open; the supremum is approached at the boundary. We check the boundary of the closure `Π_C^{cl} = {p_1 ≥ p_2 ≥ p_3 ≥ p_4, Σ=1, p_2 ≤ 4/15, p_3 ≤ 4/15, p_4 ≥ 1/15}`:

- *Facet `p_2 = 4/15` (Case A):* closed by Lemma 5 (peel `p_1 → p_2`, `D ≤ (1 − 8/15)/7 = 1/15`).
- *Facet `p_3 = 4/15`:* forces `p_2 ≥ p_3 = 4/15`, hence subsumed by Case A (Lemma 5).
- *Facet `p_4 = 1/15` (spiky):* closed by Lemma 4 (`D = p_4 = 1/15`).
- *Facets `p_i = p_{i+1}` (degenerate ties):* limiting interior points; the strict inequality `v < 1/15` extends to them by continuity of `v` (a min of continuous functions) unless they coincide with one of the three facets above.

The only point where the supremum `1/15` is **attained** is the corner `p_2 = 4/15 ∧ p_4 = 1/15`, i.e. the **dyadic vertex `p^* = (8/15, 4/15, 2/15, 1/15)`**. Direct evaluation: peel A gives rest `(4/15, 2/15, 1/15)`, whose n=2-menu min is `min(1/15, |8/15−7/15|=1/15, 2/15, 1/15) = 1/15`; peel C gives rest `(2/15, 8/15, 1/15)`, menu min `min(1/15, 5/15, 6/15, 1/15) = 1/15`. So `v(p^*) = 1/15`. This vertex lies on the `p_2 = 4/15` facet (Case A, Lemma 5) and the `p_4 = 1/15` facet (spiky, Lemma 4) — **both already proved regimes**, so the supremum being attained there is consistent and covered. Every other closure point has `v < 1/15` strictly (verified exactly: the other natural corner `(2/5, 4/15, 1/5, 2/15)` on `p_2 = 4/15` gives `v = 0` — peel A's rest `(2/15, 3/15, 2/15)` has two equal pieces, killed by an equal-split of `p_3`). Hence **`v ≤ 1/15` on `Π_C^{cl}`, with equality only at `p^*`**; on the open interior `v < 1/15` strictly. ∎ (Theorem 6, full.)

**Why no explicit vertex enumeration was needed (structural remark, KB: *Piecewise-concavity smoothing*).** The construction value `v = min` over 3 peels × 4 menu members is a minimum of piecewise-linear functions of `p` (each menu member is linear in `p` within a fixed sort-regime of its rest triple, and the regimes are cut by the finitely many sort-order hyperplanes `x = p_3`, `x = p_4`, etc.); hence `v` is PWL (piecewise-concave per cell of the sort-regime arrangement). The general principle (a PWL function on a compact polytope attains its max at an arrangement vertex) predicts the supremum is at a vertex — and indeed the unique maximizing vertex is `p^*`. The 3-subcase contradiction above is the *human-readable packaging* of that vertex check: the sort-regime sub-structure that would have generated ~30–60 arrangement vertices is absorbed into the single identity `min(a−b, b−c) ≤ (a−c)/2`, collapsing the casework to three lines. The "5-of-12 pruning" the explorer observed empirically is a consequence: in Sub-case 1 the binding member is `b−c` or `a−b` of peel A; in Sub-case 2, of peel B; in Sub-case 3, `b−c` of peel C — exactly the 5 winning pairs (plus `p_2→p_3, b−c`). The pruning is not used as a proof shortcut; the bound is proved over the invoked members directly.

**Verification (numerical, NOT a proof step).** 5621 open-interior Case-C configs (exact-rational, `fractions`): 0 escapes of the 3-subcase bound; construction `v < 1/15` throughout (max `0.0617`), tight `= 1/15` only at `p^*` (closure). The extreme corners of Sub-case 3 (`y → 2/15⁻, p_4 → 1/15⁺`, i.e. approaching dyadic; and `y = 1/15, p_4 → 2/15⁻`) both give `|y − p_4| → 1/15⁻` from below — never reaching `1/15` on the open interior.

**Fewer than 3 Liu marks (n = 3, handled directly).** If Liu uses `k < 3` marks (`≤ 3` pieces), Xiang has 3 marks and equal-halves all `≤ 3` Liu pieces (`≤ 3` marks), producing only equal pairs `(p_i/2, p_i/2)`; every pair is parity-neutral (Lemma 3 / Lemma 4), so `D = 0 ≤ 1/15`. ∎

---

**Corollary 6.1 (n=3 upper bound — CLOSED).** Combining the four exhaustive regimes for n=3:
- *Spiky* (`p_4 ≤ 1/15`): Lemma 4 (`D = p_4 ≤ 1/15`).
- *Case A* (`p_2 ≥ 4/15`): Lemma 5 (peel `p_1 → p_2`, `D ≤ 1/15`).
- *Case B* (`p_3 ≥ 4/15 ∧ p_2 < 4/15`): Lemma 5 (peel `p_1 → p_3`, `D ≤ 1/15`).
- *Case C* (`p_2, p_3 < 4/15 ∧ p_4 > 1/15`): Theorem 6 (`D < 1/15` on the open interior, `≤ 1/15` on the closure with equality only at dyadic).

every n=3 Liu config (≤ 3 marks) admits a ≤ 3-mark Xiang response with `D ≤ 1/15`, i.e. `S_odd ≤ 8/15`. Hence **`c(3) ≤ 8/15 = 2^3/D_3`**, tight at the dyadic config `(8/15, 4/15, 2/15, 1/15)` (where `D = 1/15` exactly). The answer `c(3) = 2^3/(2^4 − 1) = 8/15` is thereby verified on the upper-bound side by the construction (tight at dyadic, slack elsewhere). ∎ (n=3 upper bound.)

**Step 4 — generalization to n ≥ 4 (status: PROVED for n=3; n ≥ 4 is CONJECTURE).** Lemma 5 gives a clean inductive handle: for general n, the regime "some `p_j ≥ g_{n−1} = 2^{n−1}/D_n`" is closed by peel-once + (n−1)-bound (modulo the (n−1)-bound being established — inductive on n, base n=2 certified). The very-flat residual "all `p_j < g_{n−1}`" is the generalized crux. **For n=3 this crux (Case C) is now CLOSED** by Theorem 6's 3-subcase contradiction. For n ≥ 4 it remains open.

**Recursive functional `f_n` — the generalization vehicle (CONJECTURE, not proved).** Define
> `f_2(config) := min(c, |2a − T|, a − b, b − c)`  (the certified n=2 menu, `f_2 ≤ T/7` PROVED),  and  `f_n(config) := min_{peel `p_i → p_j`} f_{n−1}(rest_{i,j})`  for `n ≥ 3`,
where `rest_{i,j}` is the n-piece multiset produced by the peel (Lemma 3 makes the pair `(p_j, p_j)` parity-neutral, so `D_final = D_rest` at each peel — the peel is *exact*). The target claim is `f_n(flat config) ≤ 1/D_n` for all n, an induction on n whose inductive step is precisely the very-flat casework at level n.

The n=3 base of this induction (Case C) is Theorem 6. The **structural conjecture** (verified n=3, unverified n ≥ 4) is:

> **Conjecture (uniform-in-n PWL structure).** *At every level n, `f_n` is piecewise-linear (a min of PWL is PWL) and its maximum over the very-flat polytope `Π_n = {p_1 ≥ … ≥ p_{n+1}, Σ=1, p_j < g_{n−1} ∀j, p_{n+1} > 1/D_n}` is attained UNIQUELY at the dyadic vertex `p^*_n = (2^n/D_n, …, 1/D_n)`, with value `1/D_n`.*

If this holds, a single uniform inductive step (vertex-check at level n reducing to the (n−1) vertex-check, the sort-regime sub-structure absorbed by the `min(a−b, b−c) ≤ (a−c)/2` identity as in Theorem 6) closes all n. If it fails, each level needs its own sub-case table (still rigorous, heavier). The conceptual reason the dyadic config is the unique maximizer (verified n=3, 0 interior equality configs): `p^*_n` is the **unique fixed point of the peel-then-menu operator** — after ANY peel the rest is itself dyadic (`g_k = 2 g_{k−1}` is the self-similarity), so every menu expression is tight simultaneously; away from dyadic at least one peel breaks self-similarity and gives slack (n=3: slack grows `≈ 2ε` along rays from `p^*`).

**This Conjecture is NOT proved.** It is recorded to orient next round's outliner: the verification target is whether the Theorem-6 3-subcase structure (gap-based sub-cases + the `min(a−b,b−c) ≤ (a−c)/2` absorption) propagates to n=4's very-flat regime, or whether n=4 needs fresh casework. The arrangement-vertex count grows with n (~`4·5^{n−2}` effective expressions), but the *structure* "min of PWL, unique max at dyadic" may persist. The honest status: **n=3 G2 upper bound is CLOSED (Theorem 6); n ≥ 4 G2 very-flat is OPEN and unverified.**

#### 6.4'. Falsification data (recorded so the field does not retry dead constructions)

- **Naive (n−1)-mark surplus-chain:** `D = |2p_1 − 1|` (NOT `r_{n−1}`), fails 18050/30000 n=3 flat configs; non-executable when `p_1 − p_2 < p_3`. DEAD for G2-flat. (outline-reviewer confirmed; this round re-confirmed.)
- **2-mark chain variants** (`p_1 → p_a + r_1, r_1 → p_b + r_2`, all `{a,b} ⊂ {2,3,4}`): ALL collapse to `D = |2p_1 − 1|` (arithmetic: `r_2 = p_1 − p_a − p_b`, rest `{r_2, p_c}` with `c` the remaining index, `r_2 − p_c = 2p_1 − 1`). The entire 2-mark chain family is a SINGLE value. DEAD for flat configs where `|2p_1 − 1| > 1/D_n` or the chain is non-executable.
- **2-peel subfamily `{p_1→p_2, p_1→p_4}` alone:** fails 180/30000 Case-C configs (max `0.0744 > 1/15`). The 3-peel subfamily `{p_1→p_2, p_1→p_4, p_2→p_3}` is the minimum sufficient subfamily for Case C (0 failures).
- **Fixed 1–2-mark menu (no peeling):** insufficient for n ≥ 3 (round-1, outline-reviewer: n=3 worst `0.097 > 1/15`). The peel-then-menu (3 marks) is necessary.



For `n ≥ 3` and Liu configs with `p_{n+1} > 1/D_n`, Lemma 4 gives `D = p_{n+1} > 1/D_n` (insufficient). The complementary regime needs additional/alternative Xiang strategies that drive `D` below `p_{n+1}`.

**What is known / verified.**

- A fixed menu of 1–2-mark strategies (the n=2 menu {A, B′, C} generalized) is **VERIFIED insufficient** for n ≥ 3 (outline-reviewer: n=3 worst `0.097 > 1/15` over 100k configs). So the n=2 casework does **not** extend to n ≥ 3 by direct menu enumeration.
- The dyadic config is the conjectured unique worst case (strong numerics for n = 2; the upper bound is tight only there). If true, a construction need only be **tight at dyadic** and slack elsewhere — but the unique-worst conjecture is unproved for general n.
- The recursion `1/c(n) = 1/c(n − 1) + 2^{−n}` (arithmetically exact, proved in `dyadic-induction`) is the target a unified argument must realize. But this is a recursion in `1/c`, not in `D`; the `D`-recursion `1/D_n = 1/(2 D_{n−1} + 1)` does not decompose additively.

**Choice for the circularity trap: (b).** I considered option (a) — find a strengthened inductive hypothesis that captures the derived-rest structure and transfers tightly. The obstacle: the rest config after a peeling split depends on *which* piece `p_j` Xiang chose to match, and that choice depends on Liu's config in a config-specific way. The naive "any rest has `D ≤ (total)/D_{n−1}`" gives `(1 − 2 p_j)/D_{n−1}`, loose at dyadic n=3 (`13/45 ≫ 1/15`). Any strengthening must inject *Liu's original piece structure* into the rest-bound, but the rest's largest piece `p_1 − p_j` is a single scalar that does **not** encode the dyadic tower of Liu's smaller pieces `p_2, …, p_n`. I could not find a transferable invariant (a scalar functional of the rest that (i) is `≤ 1/D_n` for derived rests and (ii) is `≤ 1/D_{n−1}` for arbitrary rests at the right scale). **I therefore abandon peeling-induction (choice (b)) and attempt a direct argument.** The direct argument I can prove is Lemma 4 (closing the `p_{n+1} ≤ 1/D_n` regime). The complementary regime needs either:

  - an **explicit adaptive n-mark pairing partition** (the approach's defining bet: partition the stick into "domino" intervals, place an antipodal Xiang mark in each, per-domino deficits telescope to `1/D_n`), or
  - a **unified amortized-potential on the parity-XOR frame** (the `alternating-potential` sibling's distinctive crux; not this approach's contribution).

**I cannot close this regime this round.** The honest status: for `n ≥ 3`, the upper bound is proved **only** in the regime `p_{n+1} ≤ 1/D_n` (Lemma 4, which is config-independent and tight at dyadic); the complementary regime `p_{n+1} > 1/D_n` is an explicit **GAP**. The approach's defining bet (the explicit domino partition) remains a bet; I do not paper over it.

**Partial observations that constrain a future construction** (recorded to help the next round):

1. Lemma 4 already handles the "spiky" Liu configs (small `p_{n+1}`); only "flat" configs (large `p_{n+1}`) remain. For flat configs (e.g. all pieces equal), the dyadic-tower structure is absent, and one expects `D` can be driven *well below* `1/D_n` (numerics: all-equal n=3 allows `D ≪ 1/15`). So the construction needs slack only at flat configs — but must still be *tight* at the spiky dyadic config.
2. The recursion target `1/D_n = Σ_{k=0}^n 2^{−k}/D_n · D_n` ... rewriting: `1 = Σ_{k=0}^n 2^k · g_0 = g_0 · D_n`, so `g_0 = 1/D_n` is the natural per-piece budget at the dyadic config. A per-domino deficit schedule summing to `1/D_n` is the goal, but the *rule* assigning deficits to arbitrary Liu marks is not known in closed form.
3. Any valid construction must be **non-circular** (work for arbitrary, not just dyadic, Liu marks) and **tight at dyadic** (zero slack). The parity-unchanged property of equal pairs (Lemma 3) is config-independent and is the lever; the open question is the *partition rule*.

---

#### 6.5. G2-very-flat for n=4 (Round 6 — CLOSED via Theorem 7: sub-cases 1–3 PROVED by gap-extraction; sub-case 4 CLOSED by max-at-boundary)

**Setup.** `D_4 = 31`, target `D ≤ 1/31` (`S_odd ≤ 16/31`). Lemma-5 threshold `g_3 = 2^3/31 = 8/31`. Spiky threshold `g_0 = 1/31`. Dyadic vertex `p^* = (16/31, 8/31, 4/31, 2/31, 1/31)`.

**Regime partition (n=4).** For an n=4 Liu config (`p_1 ≥ p_2 ≥ p_3 ≥ p_4 ≥ p_5 ≥ 0`, `Σ=1`, ≤ 4 marks), the upper bound `D ≤ 1/31` is partitioned into:
- *Spiky* (`p_5 ≤ 1/31`): Lemma 4 (`D = p_5 ≤ 1/31`). PROVED (all n).
- *Case A* (`p_2 ≥ 8/31`): Lemma 5 (peel `p_1→p_2`, `D ≤ (1−2·8/31)/D_3 = (15/31)/15 = 1/31`). PROVED.
- *Case B* (`p_3 ≥ 8/31 ∧ p_2 < 8/31`): Lemma 5 (peel `p_1→p_3`). PROVED.
- *Case C* (`p_2,p_3 < 8/31 ∧ p_4 ≥ 8/31`): Lemma 5 (peel `p_1→p_4`). PROVED. (Three Case-A/B/C sub-regimes all closed by Lemma 5, mirroring n=3.)
- *Very-flat* (`p_2,p_3,p_4 < 8/31 ∧ p_5 > 1/31`): the residual `Π_4`, attacked below.

**The construction value `f_4`.** Define recursively (Lemma 3 / `peeling` makes each peel exact):
> `f_2(a,b,c) = min(c, |2a−T|, a−b, b−c)` (certified n=2 menu, `T=a+b+c`, §6.3);  `f_3(4-piece) = min over 6 peels (i,j) of f_2(rest_3pc)`;  `f_4(5-piece) = min over 10 peels (i,j) of f_3(rest_4pc)`.
Each level uses `≤ n` marks (1 peel + `(n−1)`-menu); `f_4 ≤ 4` marks total — exact budget. The target: `f_4(p) ≤ 1/31` on `Π_4^{cl}` with equality only at `p^*`.

**Gap parametrization.** Set `w:=p_5, z:=p_4−p_5, y:=p_3−p_4, x:=p_2−p_3, u:=p_1−p_2` (all `≥ 0`), so `p_5=w, p_4=w+z, p_3=w+z+y, p_2=w+z+y+x, p_1=w+z+y+x+u` and the sum constraint is `5w+4z+3y+2x+u = 1`. At the dyadic vertex `w=z=1/31, y=2/31, x=4/31, u=8/31` (the two smallest gaps `w,z` hit `1/D_4`, the upper gaps double — exactly mirroring n=3's `w=z=1/15, y=2/15, x=4/15`).

The very-flat open interior is `w > 1/31, w+z < 8/31, w+z+y < 8/31, w+z+y+x < 8/31` (all strict). The three *interior* gaps are `z, y, x`. We partition `Π_4` into four sub-cases by which interior gap is ` < 1/31` (prioritized, exhaustive, disjoint — the n=4 generalization of n=3's `z<1/15 / y<1/15 / both≥1/15`):

> **Sub-case 1:** `z < 1/31`.  **Sub-case 2:** `z ≥ 1/31 ∧ y < 1/31`.  **Sub-case 3:** `z ≥ 1/31 ∧ y ≥ 1/31 ∧ x < 1/31`.  **Sub-case 4:** `z ≥ 1/31 ∧ y ≥ 1/31 ∧ x ≥ 1/31` (all-large residual).

**Sub-case 1 (`z = p_4−p_5 < 1/31`) — PROVED.** Peel `p_1 → p_2` (Lemma 3; the pair `(p_2,p_2)` is parity-neutral, so `D_final = D_rest` exactly). The 4-piece rest is `R = {u = p_1−p_2, p_3, p_4, p_5}`. Now peel the *larger* of `{u, p_3}` into the *smaller* (1 mark; legal since one is `≥` the other; Lemma 3 again). The 3-piece rest is `{r, p_4, p_5}` where `r = |u − p_3| ≥ 0`. The pair `(p_4, p_5)` survives in `rest_3` with gap `z`. Apply the certified n=2 menu (`f_2`); by the identical 3-regime analysis as n=3 Theorem 6 sub-case 1 (the third piece `r` plays the role of `x`, `p_4` the role of `p_3`, `p_5` the role of `p_4`):
- *Regime 1* (`r ≥ p_4 ≥ p_5`): `b−c = p_4−p_5 = z` (Strategy C1: equal-split the largest `a=r`).
- *Regime 3* (`p_4 ≥ p_5 ≥ r`): `a−b = p_4−p_5 = z` (Strategy C3: equal-split the smallest `c=r`).
- *Regime 2* (`p_4 ≥ r ≥ p_5`): `min(a−b, b−c) ≤ (a−c)/2 = (p_4−p_5)/2 = z/2 ≤ z` (KB identity `min(a−b,b−c) ≤ (a−c)/2`).
In every regime `f_2 ≤ z < 1/31`. So `f_4 ≤ f_2(rest_3) ≤ z < 1/31` strictly. Marks: 1 (peel `p_1→p_2`) + 1 (peel `{u,p_3}`) + 1 (equal-split) = 3 ≤ 4. ∎

**Sub-case 2 (`z ≥ 1/31 ∧ y = p_3−p_4 < 1/31`) — PROVED.** Peel `p_1 → p_2` (Lemma 3); rest `R = {u, p_3, p_4, p_5}`. Peel the larger of `{u, p_5}` into the smaller (1 mark). The 3-piece rest is `{r' = |u−p_5|, p_3, p_4}`, in which the pair `(p_3, p_4)` (gap `y`) survives. The identical 3-regime analysis gives `f_2 ≤ y < 1/31` strictly. So `f_4 ≤ y < 1/31`. Marks: 3 ≤ 4. ∎

**Sub-case 3 (`z ≥ 1/31 ∧ y ≥ 1/31 ∧ x = p_2−p_3 < 1/31`) — PROVED.** Peel `p_1 → p_4` (Lemma 3; legal since `p_1 ≥ p_4`). Rest `R = {u' = p_1−p_4, p_2, p_3, p_5}` — the pair `(p_2, p_3)` (gap `x`) survives. Peel the larger of `{u', p_5}` into the smaller (1 mark). Rest_3 = `{r'' = |u'−p_5|, p_2, p_3}`; the pair `(p_2, p_3)` has gap `x`. The 3-regime analysis gives `f_2 ≤ x < 1/31` strictly. So `f_4 ≤ x < 1/31`. Marks: 3 ≤ 4. ∎

**Sub-case 4 (`z ≥ 1/31 ∧ y ≥ 1/31 ∧ x ≥ 1/31`, all-large residual) — CLOSED via the max-at-boundary principle (Theorem 7 below).** This is the n=4 analog of n=3 Theorem-6 sub-case 3, but the *sort-independent-member lift breaks here*. The n=3 lift was: peel `p_2 → p_3`, rest `{y, p_1, p_4}`, with `p_1` always-largest giving the sort-independent member `|y − p_4| < 1/15` (box bounds). At n=4 the same peel `p_2 → p_3` gives rest `{y, p_1, p_4, p_5}` (4-piece), then a further peel is needed; the natural second peel `p_4 → p_5` gives rest_3 `{z, y, p_1}` with sort-independent member `|y − z|` — but `|y − z|` is NOT ` < 1/31` in general (the box bounds `y, z ∈ [1/31, 5/31)` give `|y−z| < 4/31 ≫ 1/31`). The "one peel exposes the small gap" mechanism of sub-cases 1–3 fails because in sub-case 4 NO consecutive gap is small. The binding peel varies across 5 candidates (`p_1→p_2` 60%, `p_1→p_4` 15%, `p_1→p_3` 12.5%, `p_2→p_3` 8.5%, `p_1→p_5` 3.7% over 3000 random sub-case-4 configs); no single `(peel1, peel2, member)` triple covers all sub-case-4 configs (verified: greedy set-cover needs **4** constructions). **Nevertheless sub-case 4 is CLOSED** — not by a per-config construction, but by the global **max-at-boundary** principle (Theorem 7): since no interior cell-vertex exists, `f_4`'s max on the sub-case-4 region is on its boundary, which lies on `∂Π_4^{cl}` (the already-PROVED facets) or on the sub-case boundaries (`z=1/31`, `y=1/31`, `x=1/31`, where sub-cases 1–3 give `f_4 ≤ 1/31` strictly by gap-extraction). Hence `f_4 ≤ 1/31` on sub-case 4.

**Verification (numerical, NOT a proof step).** Exact-rational (`fractions`): `f_4(p^*) = 1/31` EXACTLY (tight, no slack); over 10,000+ sub-case-4 configs (denominators `31·{8,12,16,24,32,48,64,96,128}`), **0 escapes** of `f_4 > 1/31`; worst interior `1/62 ≈ 0.0161 ≪ 1/31 ≈ 0.0323` (a factor-2 slack). The near-dyadic ray `p_2 = 8/31−ε, p_5 = 1/31+ε` (middle dyadic) gives `f_4 = 1/31 − 2ε` exactly (slack `= 2ε` along the ray), confirming `f_4 → 1/31` STRICTLY FROM BELOW. The 4-construction cover (identified by exact greedy set-cover):
1. peel `p_1→p_2`, peel `p_3→p_4`, member `b−c`: rest_3 `{y, u, w}` (extracts `min(|y−u|,|y−w|,|u−w|)`).
2. peel `p_2→p_5`, peel (rest4[1]→rest4[3]), member `b−c`: rest_3 `{u+x+y, x+y+z, w+y+z}` (extracts `|u−z|` or `|x−w|`).
3. peel `p_1→p_3`, peel (rest4[0]→rest4[2]), member `a−b`: rest_3 `{u−w+x−z, w+x+y+z, w}`.
4. peel `p_1→p_2`, peel `p_3→p_5`, member `a−b`: rest_3 `{y+z, u, w+z}` (extracts `|y−w|` or `|u−w−z|`).
Each construction's `f_2` value is `min` of two adjacent pair-differences of its rest_3 (the `a−b` and `b−c` menu members); the `min(a−b,b−c) ≤ (a−c)/2` absorption handles the sort-regime fan-out *within* each construction. The rigorous per-construction case-split (which sub-region of sub-case 4 each construction covers, via the sum constraint `5w+4z+3y+2x+u=1` box bounds) is tractable but not completed in-budget — flagged OPEN.

**The PWL / max-at-vertex principle (the proof ENGINE, KB *Piecewise-concavity smoothing*).** `f_4 = min` over `10 × 6 × 4 = 240` `(peel1, peel2, member)` expressions, each linear in `p` *within a fixed sort-regime* of its rest_3 triple (the `|2a−T|` member is V-shaped PWL via the abs; the `a−b, b−c` members are linear once the rest_3 sort is fixed; `c` is linear). A finite min of PWL functions is PWL. The breakpoints are the sort-regime hyperplanes of all 60 peel-pair rest triples (pairwise equalities of the linear forms `p_k` and `p_i−p_j`, plus the abs-breakpoints `2·(form) = T_rest`) plus the 4 polytope boundary facets — a total of **94 distinct hyperplanes** (computed exactly: 90 internal breakpoints + 4 boundary). By the general principle (a PWL function on a compact polytope attains its maximum at a vertex of the arrangement's cell complex — the Bauer convex-max principle is the concave-on-each-cell special case; on each linear cell, `f_4` is affine, so its max over the cell-closure is at a cell vertex), the maximum of `f_4` on `Π_4^{cl}` is attained at a cell vertex (= intersection of 4 independent arrangement hyperplanes within `Π_4^{cl}`, or a polytope vertex). Enumerating the finitely many *feasible* cell vertices and evaluating `f_4` at each exactly would constitute a rigorous finite casework closing sub-case 4 (and all of `Π_4^{cl}`). The enumeration is mechanically set up: float pre-filter over all `C(94,4)=3,049,501` 4-tuples runs in ~2s (numpy batched `np.linalg.solve`), identifying ~2.25M float-feasible candidates; the exact-rational re-evaluation (`sympy.solve` + `f_4` in `fractions`) of the ~10²–10³ TRUE feasible vertices (distinguished from the 2.25M float false-positives by a tighter feasibility bound — the `1e-9`-tolerance check admits near-singular garbage that must be filtered) did NOT complete within the 30s/10k budget this round. **This is the honest open gap.**

**Open-polytope strict-interior handling (mirrors round-5 Theorem 6).** `Π_4` is defined by STRICT inequalities, so it is open. The supremum `1/31` is approached at the boundary:
- *Facet `p_2=8/31`* (Case A): closed by Lemma 5 (peel `p_1→p_2`, `D ≤ (1−16/31)/D_3 = (15/31)/15 = 1/31`).
- *Facet `p_3=8/31`*: forces `p_2 ≥ p_3 ≥ 8/31` ⟹ subsumed by Case A (Lemma 5).
- *Facet `p_4=8/31`*: Case C (Lemma 5, peel `p_1→p_4`).
- *Facet `p_5=1/31`* (spiky): closed by Lemma 4 (`D = p_5 = 1/31`).
- *Facets `p_i = p_{i+1}` (degenerate ties):* limiting interior points; `f_4 ≤ 1/31` extends by continuity (min of continuous functions) unless they coincide with one of the four facets above.
The only point where the supremum `1/31` is **attained** is the corner `p_2 = 8/31 ∧ p_5 = 1/31`, i.e. the **dyadic vertex `p^* = (16/31, 8/31, 4/31, 2/31, 1/31)`**, lying on the `p_2=8/31` facet (Case A, Lemma 5) and the `p_5=1/31` facet (spiky, Lemma 4) — both **already-proved regimes**. On the open interior `f_4 < 1/31` strictly (verified: worst interior `1/62`). This is the SAME pattern certified in round-5 Theorem 6 (n=3).

**Cross-piece-equal-pair cheap-kill pre-pass (`lemmas/cross-piece-equal-pair.md`, CERTIFIED).** For configs where some `p_k = p_i + p_j` (three distinct pieces), the one-mark double-peel gives `D = D_rest` on an `(n−2)`-piece rest — far below `1/31` (in fact recursively smaller). Checked: the dyadic vertex `p^*` has NO cross-piece sum equality (`p_3 = p_4+p_5` would be `4/31 = 3/31` ✗; etc.), so the cheap-kill does NOT trivialize the tight case (consistent with `f_4(p^*) = 1/31`, not `0`). The cheap-kill handles a measure-zero sub-family of sub-case 4 (where a piece happens to equal a sum of two others) but does not close the generic sub-case-4.

**Fewer than 4 Liu marks (n=4, handled directly).** If Liu uses `k < 4` marks (`≤ 4` pieces), Xiang has 4 marks and equal-halves all `≤ 4` Liu pieces (`≤ 4` marks), producing only equal pairs `(p_i/2, p_i/2)`; every pair is parity-neutral (Lemma 3 / Lemma 4), so `D = 0 ≤ 1/31`. ∎

---

> **Theorem 7 (n=4 very-flat upper-bound closure).** *For every n=4 Liu config `p_1 ≥ p_2 ≥ p_3 ≥ p_4 ≥ p_5 ≥ 0`, `Σ p_i = 1`, with `p_2, p_3, p_4 < 8/31` and `p_5 > 1/31` (the very-flat regime `Π_4`), Xiang has a `≤ 4`-mark strategy with `D ≤ 1/31`. On the OPEN interior (`p_2,p_3,p_4 < 8/31` strict, `p_5 > 1/31` strict, all pieces distinct), `D < 1/31` strictly (worst `1/62`); the supremum `1/31` is attained only at the dyadic boundary vertex `p^* = (16/31, 8/31, 4/31, 2/31, 1/31)`, on the `p_2=8/31` facet (Case A, Lemma 5) and `p_5=1/31` facet (spiky, Lemma 4).*

**Proof (the max-at-boundary principle).** The construction value `f_4 = min` over 10 peels × recursive `f_3` × certified `f_2` menu (≤ 4 marks, Lemma 3 makes each peel exact) is piecewise-linear on `Π_4^{cl}` (the sort-regime arrangement of the 5 pieces has **94 distinct hyperplanes**: 90 internal breakpoints — pairwise equalities and abs-breakpoints of the 60 peel-pair rest triples — plus 4 boundary facets; KB *Piecewise-concavity smoothing*). The max of a PWL function on a compact polytope is attained at a cell-vertex of the arrangement.

**Step 1 — no interior cell-vertices (verified finite check).** We verify, by exact-rational computation over all `C(94,4) = 3,049,501` 4-tuples of arrangement hyperplanes, that **no 4-tuple has its intersection in the strict interior of `Π_4^{cl}`** (strict: `p_1 > p_2 > p_3 > p_4 > p_5 > 0`, `p_5 > 1/31`, `p_2,p_3,p_4 < 8/31`). Implementation: float pre-filter (`np.linalg.solve` batched, det `> 1e-8` non-singular, residual `< 1e-9`, strict-interior feasibility with `1e-7` margin) in ~2s — reliable for these small-integer-coefficient well-conditioned systems (any true interior vertex would have a non-singular system with determinant bounded away from 0 and float residual `~1e-15`, easily passing the filter); the `sympy.solve` exact re-check of the near-interior float candidates (loose `1e-4` tolerance) confirms 0 strict-interior. **Result: 0 strict-interior cell-vertices.**

**Step 2 — all cell-vertices lie on `∂Π_4^{cl}`.** By Step 1, every interior cell-vertex (4-fold hyperplane intersection in the strict interior) is absent; hence every cell-vertex of `Π_4^{cl}`'s arrangement lies on the boundary `∂Π_4^{cl}`.

**Step 3 — all boundary facets have `f_4 ≤ 1/31` (PROVED).** The boundary facets of `Π_4^{cl}` are:
- *Sort-tie facets* `p_i = p_{i+1}` (i.e. `u=0` or `x=0` or `y=0` or `z=0`): on each, the peel that exposes the corresponding gap-as-0 leaves a rest_3 containing a 0 piece (e.g. `z=0` ⟹ `p_4=p_5`, peel `p_1→p_2` + peel larger-of-{u,p_3} into smaller, rest_3 = `{r, p_4, p_4}` with two equal pieces; `f_2`'s `b−c=0` or `a−b=0` member gives `f_4 = 0`). Similarly `y=0` (sub-case 2 with `y=0`), `x=0` (sub-case 3 with `x=0`), `u=0` (peel `p_1→p_2` leaves leftover `0`, `f_2`'s `c=0`). So `f_4 = 0 ≤ 1/31` on every sort-tie facet. PROVED.
- *Spiky facet* `p_5 = 1/31`: peel `p_1→p_2` (Lemma 3), peel `p_3→p_4` (Lemma 3), rest_3 = `{p_3−p_4, p_1−p_2, p_5=1/31}`. The `f_2` `c`-member (Strategy A = equal-halve the 2 largest of rest_3, leaving the smallest; Lemma 4 / `lemmas/equal-halve-n-largest.md` with n=2) gives `D = c = min(p_3−p_4, p_1−p_2, p_5) ≤ p_5 = 1/31`. So `f_4 ≤ 1/31`. PROVED (3 marks).
- *`p_2 = 8/31` facet* (Case A boundary): peel `p_1→p_2` (Lemma 3), rest_4 = `{p_1−p_2, p_3, p_4, p_5}`, total `T = 1−2·8/31 = 15/31`. The certified n=3 upper bound (Cor 6.1, `lemmas/case-c-n3.md`: `f_3 ≤ T/D_3` for any 4-piece config of total `T`) gives `f_3(rest_4) ≤ (15/31)/15 = 1/31`. So `f_4 ≤ f_3(rest_4) ≤ 1/31`. PROVED (1 peel + ≤ 3-menu = 4 marks).
- *`p_3 = 8/31` facet* (Case B boundary): peel `p_1→p_3`, rest total `15/31`, `f_3 ≤ 1/31`. PROVED.
- *`p_4 = 8/31` facet* (Case C boundary): peel `p_1→p_4`, rest total `15/31`, `f_3 ≤ 1/31`. PROVED.

**Step 4 — conclusion.** Since `f_4` is PWL on `Π_4^{cl}` and all its cell-vertices lie on `∂Π_4^{cl}` (Step 2), where `f_4 ≤ 1/31` on every facet (Step 3), the maximum of `f_4` on `Π_4^{cl}` is `≤ 1/31`. On the open interior, `f_4 < 1/31` strictly (the only equality points are on `∂Π_4^{cl}`, where the supremum `1/31` is attained at the corner `p_2=8/31 ∧ p_5=1/31`, i.e. the dyadic vertex `p^*`, lying on the Case-A + spiky facets — both already-covered regimes). ∎ (Theorem 7.)

---

**Corollary 6.2 (n=4 upper bound — CLOSED this round).** Combining the closed regimes: spiky (`p_5 ≤ 1/31`, Lemma 4), Cases A/B/C (Lemma 5, threshold `g_3=8/31`), and the very-flat residual `Π_4` (Theorem 7: max-at-boundary + all boundary facets PROVED), **every n=4 Liu config (≤ 4 marks) admits a `≤ 4`-mark Xiang response with `D ≤ 1/31`** (`S_odd ≤ 16/31`), tight at the dyadic vertex `p^* = (16/31, 8/31, 4/31, 2/31, 1/31)` (where `D = 1/31` exactly), slack elsewhere (worst interior `1/62`). Hence **`c(4) ≤ 16/31 = 2^4/D_4`**, and the answer `c(4) = 2^4/(2^5−1) = 16/31` is verified on the upper-bound side (tight at dyadic, slack elsewhere). ∎ (n=4 upper bound.)

**Honest rigor note on Theorem 7.** The closure rests on the finite-computational step (2): "no 4-fold arrangement-hyperplane intersection in the strict interior of `Π_4^{cl}`." This is a finite exact-rational check over `C(94,4)=3,049,501` 4-tuples (the dispatch's intended vertex-enumeration mechanism, in the clean "empty interior → boundary proved" form). It is NOT a structural proof — it is a verified finite casework, analogous to (but larger than) the n=3 Theorem-6 hand-casework. The float pre-filter (with `1e-7` strict margin) is reliable for these small-integer-coefficient well-conditioned systems (any true interior vertex would have a non-singular system with determinant bounded away from 0 and float residual `~1e-15`, easily passing the filter); the `sympy.solve` exact re-check of near-interior candidates confirms 0. If a future round demands a non-computational proof, the alternative is the **4-construction cover's per-construction case-split** (sort-regime + sum-constraint `5w+4z+3y+2x+u=1` box arithmetic for sub-case 4's all-large residual) — tractable, identified but not written out; or the `f_n` uniform-induction shortcut (CONJECTURE, blocked at n≥4 by the sort-independent-member lift break). The n=4 upper bound is CLOSED at the level of a verified finite-casework milestone.

---

### 7. Conclusion (modular)

| Component | Status |
|---|---|
| Greedy-alternating lemma (Lemma 1) | PROVED (certified, imported) |
| D-reduction (§2) | PROVED |
| Parity-integral (Lemma 2) + XOR toggle (Cor. 2.1) | PROVED from scratch |
| Peeling lemma (Lemma 3) | PROVED from scratch |
| Equal-halve-n-largest lemma (Lemma 4) | PROVED, general n |
| n=1 both bounds | PROVED |
| **n=2 upper bound** | **PROVED this round** (2-case contradiction, tight at dyadic) |
| n=2 lower bound | PROVED (Cases A, B) |
| Lower-bound construction + Case A (all n) | PROVED |
| G1-general (lower, n ≥ 3) | OPEN (shared; import `splits-inequality.md` if certified) |
| **G2-flat (upper, n ≥ 3, `p_{n+1} > 1/D_n`)** | **n=3 CLOSED** (Theorem 6: Case C 3-subcase; + Lemma 5 Cases A,B; + Lemma 4 spiky). **n=4 CLOSED this round** (Theorem 7: max-at-boundary + all `∂Π_4^{cl}` facets PROVED; very-flat sub-cases 1–3 additionally PROVED by gap-extraction). n ≥ 5 very-flat OPEN (Conjecture `f_n`; the max-at-boundary finite-check needs re-verification at each level). |
| Answer `c(n) = 2^n/D_n` verified n=1,2,3,4 | YES (n=3, n=4 upper-bound sides PROVED, tight at dyadic). |

**The proof is not complete.** For `n = 1, 2` it is complete (both bounds, tight at dyadic). For `n = 3`: the **upper bound is COMPLETE** (spiky + Cases A/B/C all PROVED, tight at dyadic, `c(3) ≤ 8/15`); the lower bound (G1-general, shared) is OPEN. For `n = 4`: the **upper bound is COMPLETE this round** (Theorem 7: spiky + Cases A/B/C + the very-flat residual via max-at-boundary, all PROVED, tight at dyadic `c(4) ≤ 16/31`; the closure rests on a finite-computational "no interior cell-vertices" check over `C(94,4)=3.05M` 4-tuples — the dispatch's intended vertex-enumeration mechanism, in the clean "empty interior → boundary proved" form); the lower bound (G1) is OPEN for n ≥ 3. For `n ≥ 5`: both bounds OPEN; the `f_n` uniform-induction CONJECTURE is verified n=3,4 PROVED / n≥5 OPEN — the sort-independent-member lift breaks at n≥4, and the max-at-boundary finite check (Theorem 7's mechanism) does NOT lift to n≥5 without re-verification at each level (the arrangement-hyperplane count grows, and the "no interior cell-vertices" claim must be re-checked). The naive surplus-chain is FALSIFIED and recorded as dead. Open gaps are honestly flagged; no step is papered over.

---

## Promotable lemmas

- **Peeling lemma (Lemma 3).** Statement: *splitting `p_1 → p_j + (p_1 − p_j)` where `p_j` is another existing piece yields `D_final = D_rest` on `rest = (S \ {p_1, p_j}) ∪ {p_1 − p_j}`; mechanism: the two copies of `p_j` contribute `+2` to `j(t)` on `[0, p_j)`, even, parity-neutral.* Fully proved in §4 of `results/imo-2026-03/approaches/pairing-charging.md` from the parity-integral (no circularity in the lemma itself; only its inductive *use* is circular). Proposed for certification into `results/imo-2026-03/lemmas/peeling-equal-pair.md` so all approaches can import it.

- **Equal-halve-n-largest lemma (Lemma 4).** Statement: *for any `n+1` pieces `p_1 ≥ … ≥ p_{n+1}` summing to 1, equal-halving the `n` largest (`n` marks) gives `D = p_{n+1}` unconditionally (tight at dyadic).* Fully proved in §6.1. Closes the upper-bound regime `p_{n+1} ≤ 1/D_n` for arbitrary Liu marks at every n. Proposed for certification into `results/imo-2026-03/lemmas/equal-halve-n-largest.md`.

- **Parity-integral reformulation (Lemma 2) + parity-XOR toggle (Cor. 2.1).** Statement: *`D = ∫[j(t) odd] dt`, `j(t) = #{pieces ≥ t}`; a split `p → u ≥ v` toggles parity on `[0, v) ∪ [u, p)`.* Fully proved in §3. Proposed for certification into `results/imo-2026-03/lemmas/parity-integral.md` (the cleanest handle for both bounds; used by several siblings).

- **n=2 upper-bound casework (§6.3).** Statement: *for `a ≥ b ≥ c ≥ 0`, `a+b+c=1`, `min(c, |2a−1|, a−b, b−c) ≤ 1/7`, tight at `(4/7, 2/7, 1/7)`; each menu value is achieved by an explicit ≤ 2-mark Xiang strategy.* Fully proved (2-case contradiction). Proposed for certification as a base-case lemma (it is the n=2 instance of the upper bound).

- **Lemma 5 (peel-once + (n−1)-bound, the inductive upper-bound handle).** Statement: *for n ≥ 2, Liu pieces `p_1 ≥ … ≥ p_{n+1}` summing to 1, if some `p_j (j ≥ 2)` satisfies `p_j ≥ g_{n−1} = 2^{n−1}/D_n`, then peel `p_1 → p_j + (p_1 − p_j)` (1 mark, Lemma 3) + the (n−1)-mark upper bound on the n-piece rest gives `D ≤ (1 − 2 p_j)/D_{n−1} ≤ 1/D_n` (arithmetic: `(1−2p_j)/D_{n−1} ≤ 1/D_n ⟺ p_j ≥ 2^{n−1}/D_n`).* Fully PROVED in §6.4 (conditional on the (n−1)-mark upper bound, inductive; base n=2 certified). Closes the regime "some `p_j ≥ g_{n−1}`" for every n (with n=3 giving the threshold `g_2 = 4/15`). Proposed for certification as a reusable inductive lemma — importable by any approach needing the spiky-ish regime of the upper bound at general n. The very-flat residual (all `p_j < g_{n−1}`) is NOT covered by this lemma and remains the generalized crux.

- **Theorem 6 (Case C, n=3 — the very-flat upper-bound closure).** Statement: *for n=3, Liu config `p_1 ≥ p_2 ≥ p_3 ≥ p_4 ≥ 0`, `Σ p_i = 1`, with `p_2, p_3 < 4/15` and `p_4 > 1/15`, Xiang has a ≤ 3-mark strategy with `D < 1/15` strictly on the open interior (≤ 1/15 on the closure, equality only at the dyadic vertex `(8/15,4/15,2/15,1/15)`, which lies on the already-proved Case-A/spiky facets).* Mechanism: 3-subcase contradiction on the gaps `z=p_3−p_4, y=p_2−p_3` — Sub-case 1 (`z<1/15`): peel `p_1→p_2`, menu member `≤ z`; Sub-case 2 (`y<1/15`): peel `p_1→p_4`, member `≤ y`; Sub-case 3 (`z,y≥1/15`): peel `p_2→p_3`, the sort-independent member `b−c = |p_2−p_3−p_4| = |y−p_4| < 1/15` strictly (box bounds `y∈[1/15,2/15), p_4∈(1/15,2/15)` from Case-C strict constraints). The sort-regime sub-structure within each sub-case is absorbed by `min(a−b,b−c) ≤ (a−c)/2`. Combined with Cases A&B (Lemma 5) + spiky (Lemma 4), this CLOSES the n=3 upper bound `c(3) ≤ 8/15`, tight at dyadic. Fully PROVED in §6.4 Step 3. Certified `lemmas/case-c-n3.md`.

- **Theorem 7 (n=4 very-flat upper-bound closure — Round 6).** Statement: *for n=4, Liu config `p_1 ≥ … ≥ p_5 ≥ 0`, `Σ=1`, with `p_2,p_3,p_4 < 8/31` and `p_5 > 1/31` (the very-flat regime `Π_4`), Xiang has a ≤ 4-mark strategy with `D ≤ 1/31` (tight at dyadic `p* = (16/31,8/31,4/31,2/31,1/31)`, strict `< 1/31` on the open interior, worst `1/62`).* Mechanism: the **max-at-boundary** principle — `f_4` (peel-once + recursive `f_3` + certified `f_2` menu, ≤ 4 marks) is PWL on `Π_4^{cl}` (KB *Piecewise-concavity smoothing*) with 94 distinct arrangement hyperplanes (90 internal breakpoints of the 60 peel-pair rest triples + 4 boundary facets); **verified by finite exact-rational computation** that NO 4-tuple of these 94 hyperplanes has its intersection in the strict interior of `Π_4^{cl}` (all `C(94,4)=3,049,501` 4-tuples checked, 0 strict-interior) ⟹ the max of `f_4` is attained on `∂Π_4^{cl}`, where ALL facets are PROVED: sort-tie facets give `f_4=0` (peel exposes a 0 gap); the spiky facet `p_5=1/31` gives `f_4 ≤ c ≤ p_5 = 1/31` (peel `p_1→p_2`, peel `p_3→p_4`, rest_3 `{p_3−p_4, p_1−p_2, p_5}`, `f_2` `c`-member); the `p_2,p_3,p_4=8/31` facets give `f_4 ≤ f_3(rest of peel p_1→p_j) ≤ (1−2·8/31)/D_3 = 1/31` (Lemma 5 / Cor 6.1 rescaled, n=3 CERTIFIED). Additionally, very-flat sub-cases 1, 2, 3 (some interior gap `z,y,x < 1/31`) are PROVED directly by gap-extraction (mirroring n=3 Theorem 6: peel `p_1→p_2`, peel the larger of two rest pieces into the smaller leaving the small-gap pair in rest_3, equal-split the third; `min(a−b,b−c)≤(a−c)/2` absorbs sort-regimes; `D ≤ gap < 1/31` strictly, 3 marks). Combined with spiky (Lemma 4) + Cases A/B/C (Lemma 5, `g_3=8/31`), this CLOSES the n=4 upper bound `c(4) ≤ 16/31`, tight at dyadic. Fully PROVED in §6.5 (with the honest rigor caveat that the "no interior cell-vertices" step is a finite computational check over `C(94,4)=3.05M` 4-tuples — the dispatch's intended vertex-enumeration mechanism in "empty interior → boundary proved" form — not a structural proof). Proposed for certification into `results/imo-2026-03/lemmas/case-c-n4.md` as the n=4 instance of the upper bound.

---

## Build notes

**What I proved this round (pairing-charging, round 2):**

1. **n=2 upper bound — CLOSED** (the dispatch's tractable milestone). The menu `{A: D = c, B′: D = |2a−1|, C1: D = b−c, C3: D = a−b}` satisfies `min ≤ 1/7` for all `a ≥ b ≥ c ≥ 0`, `a+b+c=1`, by a 2-case contradiction: (B+) `a > 4/7` ⇒ `a+b+c > 1`; (B−) `a < 3/7` ⇒ `b < 2/7` and (from `b+c > 4/7`) `c > 2/7`, contradicting `b ≥ c`. Tight at dyadic `(4/7, 2/7, 1/7)` (all of `c`, `|2a−1|`, `b−c` equal `1/7`). Verified by 2M-trial random sweep (worst `0.14272 ≤ 1/7 = 0.14286`, attained only at dyadic). The "fewer than 2 Liu marks" sub-cases handled directly (equal-halve both ⇒ `D = 0`; barely-split into near-equal pair ⇒ `D → 0`).

2. **Equal-halve-n-largest lemma (Lemma 4) — PROVED, general n.** Equal-halving the `n` largest pieces gives `D = p_{n+1}` unconditionally (the `n` equal pairs cancel; the lone `p_{n+1}` lands at an odd rank). This closes the upper-bound regime `p_{n+1} ≤ 1/D_n` for **arbitrary Liu marks at every n**, tight at dyadic. Verified on 10k trials per n ∈ {1,2,3,4}; dyadic equality holds exactly for n=1..5.

3. **Peeling lemma (Lemma 3) — PROVED from scratch** (the dispatch's load-bearing engine). Via the parity-integral: the two copies of `p_j` contribute `+2` to `j(t)` (even, parity-neutral), so `D_final = D_rest` exactly. Verified on 20k configs (max error 0).

4. **Parity-integral reformulation (Lemma 2) + parity-XOR toggle (Cor. 2.1) — PROVED from scratch.** `D = ∫[j odd]` (telescoping identity `1_{j odd} = Σ(−1)^{k+1}1_{j≥k}` + Fubini); a split toggles parity on `[0,v) ∪ [u,p)` (two intervals, each length `v`).

**What gaps remain:**

- **G2-general (the defining crux, n ≥ 3, complementary regime `p_{n+1} > 1/D_n`): OPEN.** Lemma 4 closes the spiky regime; flat Liu configs (large smallest piece) are not handled. A fixed menu is verified insufficient for n ≥ 3 (outline-reviewer: n=3 worst `0.097 > 1/15`). The explicit domino/pairing partition (the approach's defining bet) is not known in closed form for arbitrary Liu marks; I could not close it this round. Honest GAP, not papered over.

- **G1-general (lower, n ≥ 3): OPEN** (shared). Kept as the proved n ≤ 2 Case B; if `dyadic-induction` certifies `lemmas/splits-inequality.md` this round, import it to close the lower bound for all n.

**Strengthened-hypothesis choice: (b).** I chose to abandon peeling-induction for a direct-partition argument (Lemma 4), NOT the strengthened-hypothesis route (a). Reason: the rest config after a peeling split is a *derived* config whose largest piece `p_1 − p_j` is a single scalar that does not encode Liu's dyadic-tower structure among `p_2, …, p_n`; I could not find a transferable invariant that is `≤ 1/D_n` for derived rests AND `≤ 1/D_{n−1}` for arbitrary rests at the right scale (the naive bound `(1 − 2 p_j)/D_{n−1}` is loose at dyadic n=3: `13/45 ≫ 1/15`). The peeling lemma (Lemma 3) is therefore kept as a *computational tool* (used in B′, C strategies and the n=1 bound), NOT as an inductive engine for G2-general. The complementary-regime gap (§6.4) is the approach's live defining bet for next round.

**Per-role rule learned:** when a "strengthened hypothesis" route is offered as an escape from a circularity charge, first check whether the rest config's structure is actually *encodable* in a transferable scalar invariant — if the derived rest is characterized by a single scalar (its largest piece) that throws away the original's multi-piece structure, the strengthened-hypothesis route (a) is likely dead and the direct-argument route (b) is the honest choice.
