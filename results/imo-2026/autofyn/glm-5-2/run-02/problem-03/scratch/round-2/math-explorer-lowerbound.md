## imo-2026-03 (LOWER-BOUND route — Lemma L general-n)

**Target.** Prove Lemma L general-n: when Liu plays the **dyadic config** (pieces `(1, 2, 4, …, 2^n)/D(n)`, `D(n)=2^{n+1}−1`), for EVERY Xiang response (≤ n marks), Liu's odd-rank sum `≥ f(n) = 2^n/D(n)`. Combined with the certified **pair-pile construction** (Xiang caps the dyadic config at exactly `f(n)`), this pins the dyadic config's value to exactly `f(n)`, giving `c(n) ≥ f(n)`.

Equivalently (via the certified parity identity `Liu = (1+A)/2`, `A = Σ(−1)^{i+1}p_i`), Lemma L is `A ≥ 1/D(n)` for every refinement.

---

### Distinct openings (the lower-bound route)

**Opening A — the `M ⊎ R` self-similar decomposition (CLEANEST; the engine).** The level-n dyadic config splits as `{M} ⊎ R` where
- `M = 2^n/D(n)` (the single largest piece, `> 1/2`),
- `R = (2^{n−1}, …, 2, 1)/D(n) = (D(n−1)/D(n)) · (level-(n−1) dyadic config)`, i.e. **R is a scaled copy of the level-(n−1) dyadic config**, scaled to total `R = D(n−1)/D(n)`.

The key identity: `M − R = (2^n − D(n−1))/D(n) = 1/D(n)`. So Lemma L `A ≥ 1/D(n)` is **exactly** `global_A ≥ M − R`. This is the form that factors the recursion.

**Opening B — the trivial half (0 marks in M).** When Xiang places 0 marks in the largest piece `M`, `M` is a single piece at global rank 1 (Liu's). Then `global_A = M − A_rest` where `A_rest` is the standard alternating sum of the rest `{M's nothing} ∪ R' = R'` (R refined by all n marks). Since `A_rest ≤ total(R') = R` (trivially, as `A = oddsum − evensum ≤ oddsum ≤ total`), we get `global_A ≥ M − R = 1/D(n)`. **Lemma L is immediate in this case, NO induction needed.** This disposes of the entire "0 marks in M" branch — the interleaving obstruction does NOT arise when M is untouched.

**Opening C — the hard half (k ≥ 1 marks in M); single-aux strengthened IH (VERIFIED).** When Xiang places exactly **one** mark in `M` (k=1), splitting `M → (m_1, m_2)`, `m_1 ≥ m_2`, `m_1 + m_2 = M`:
- `m_1 ≥ M/2 ≥` every R-piece (since R's largest unrefined piece `= 2^{n−1}/D(n) = M/2`, and refining only shrinks R-pieces), so `m_1` is global rank 1 (Liu's).
- `global_oddsum = m_1 + evensum(rest)`, where `rest = {m_2} ∪ R'` (R' = R refined by the remaining `n−1` marks).
- Want `global_oddsum ≥ M = m_1 + m_2`, i.e. **`evensum({m_2} ∪ R') ≥ m_2`**.
- This is EXACTLY the level-(n−1) strengthened IH (see below) with auxiliary `w = m_2 ≤ M/2 = R's largest piece`. ✓

So `L*(n−1) ⟹ L(n)` for the **k=1 sub-case**. The recursion is clean: peel one Xiang mark from M, the smaller half `m_2` becomes the auxiliary, and the residual is a level-(n−1) problem.

**Opening D — the k ≥ 2 half (multiple marks in M) — OPEN, needs a separate reduction.** Brute force (dyadic-grid enumeration, n=3) shows extremal Xiang responses exist for **every** k from 1 to n (n=3: 7 extremals at k=1, 21 at k=2, 12 at k=3). So the worst case is NOT always k=1; the k ≥ 2 branch must be handled. The natural "multi-aux" generalization of L* — `evensum({w_1,…,w_j} ∪ R') ≥ Σ w_j` for `Σ w_j ≤ R_largest`, each `w_i ≤ R_largest` — is **FALSE** (counterexample at level-1: `W = (1/9, 4/9, 1/9)` over D=9, R' unrefined `= {2,1}/3`, `evensum = 5/9 < 6/9 = ΣW`). So the k ≥ 2 case cannot just iterate the single-aux IH. Two candidate reductions for the outliner to investigate:
  - **(D1) Per-ROUND peeling.** The value recursion `1/f(n+1) = 1 + 1/(2f(n))` is per-ROUND (one mark to EACH player), not per-mark. So peel a *pair* of Xiang marks at a time: one from M (splitting it) AND one from R (further refining R). The single-aux IH L*(n−1) might then absorb the pair, since the R-side mark stays inside R'.
  - **(D2) "Splitting M further helps Liu" — WORST-CASE IS k=1.** Conjecture: for fixed R-configuration, increasing k (further splitting M) does NOT decrease the global oddsum below the k=1 minimum. (Plausible but NOT verified — outliner must prove or refute.) If true, WLOG the extremal Xiang response has k=1, and the single-aux IH suffices. The brute-force extremal distribution (k=2 most common at n=3) suggests this conjecture is FALSE as stated, but a weaker version ("there EXISTS a k=1 response at least as good for Xiang as any k≥2 response") may hold.

---

### Candidate strengthened induction hypothesis (CONCRETE, VERIFIED level 1..5)

**`L*(L)`:** For the level-`L` dyadic config `R` (pieces `(1, 2, …, 2^L)/D(L)`, total 1, largest piece `R_largest = 2^L/D(L)`), refined by ≤ `L` Xiang marks into `R'`, and a SINGLE auxiliary piece `w` with `0 ≤ w ≤ R_largest`, the merged multiset `{w} ∪ R'` satisfies

> **`evensum({w} ∪ R') ≥ w`**   (equivalently `oddsum({w} ∪ R') ≤ total(R') = 1`).

**Why it survives interleaving.** `w ≤ R_largest` means `w` can be placed anywhere in the merged sorted order — but the level-`L` lower bound (Lemma L applied to R') gives `oddsum(R') ≥ R_largest ≥ w`, and the case analysis `w at even rank` (trivial) vs `w at odd rank` (use `oddsum(R') ≥ w` to compensate) closes both sub-cases. **L*(L) is the Xiang-side dual of Lemma L(L)** — loading both into one induction is exactly the Lemma G pattern (both move-orders / both sides in one induction).

**Tightness.** Equality `evensum({w} ∪ R') = w` is attained at `w = R_largest` and `R'` = the pair-pile of level L (the self-similar extremal). Verified for L=1..5 (exact rational + Monte-Carlo for L=4,5: min gap = 0).

**Induction shape (the skeleton for the outliner):**
- Prove **L(n)** and **L*(n)** simultaneously by induction on n.
- Base n=1: L(1) and L*(1) by hand (already done in round 1; L*(1) is a 3-piece casework).
- Step n → n+1:
  - L(n+1), k=0 sub-case: trivial via Opening B.
  - L(n+1), k=1 sub-case: peel one mark from M_{n+1}, reduce to L*(n). ✓ (Opening C)
  - L(n+1), k≥2 sub-case: **OPEN** — needs D1 or D2 above. The outliner should pick D1 (per-round peeling, most consistent with the per-round value recursion) and fall back to D2 if D1 does not close.
  - L*(n+1): prove the Xiang-side dual using L(n+1) and the same M⊎R decomposition with roles swapped.

---

### Brute-force corroboration (CONJECTURE, labeled as such)

- **Lemma L exact for n=1,2,3,4** (full enumeration on a grid that is a multiple of D(n)): min oddsum `= f(n)` EXACTLY in every case. n=5: dyadic-grid enumeration (Xiang marks at multiples of `1/D(5)=1/63`) finds min oddsum `= 32/63 = f(5)`, with **3046 extremal responses** on that grid; Monte-Carlo over 200k random responses also returns min `= f(5)`. (Conjecture confirmed for n=1..5; NOT a proof for general n.)
- **Extremal structure (n=3, dyadic grid):** the pair-pile response `(4, 11)` over D=15 (bisect M=8 → (4,4); split piece 4 → (1,3)) is extremal, but so are 39 other responses spanning k=1 (7), k=2 (21), k=3 (12) marks-in-M. So the extremal Xiang response is **NOT unique** and NOT always the pair-pile — the minimum oddsum `= f(n)` is a robust floor.
- **Self-similar extremal pattern (n=5):** the pair-pile response is `(4, 11, 23, 47)` over D=63 — i.e. bisect M=32 → (16,16); bisect piece 16 → (8,8); bisect piece 8 → (4,4); split piece 4 → (1,3). This is exactly the level-4 pair-pile (scaled) plus M bisected. **The extremum is self-similar.**
- **Easy-case triviality confirmed:** when 0 marks land in M, the oddsum is well above f(n) (e.g. n=3, k=0: oddsum = 8/15 + (R's oddsum which is ≥ ...) ≫ 8/15). The tight cases all have ≥ 1 mark in M.

---

### Cheap-kill candidates

- **The trivial k=0 case** (Opening B) — disposes of the entire "0 marks in M" branch with one line: `global_A ≥ M − R = 1/D(n)`. No induction. The outliner should write this case first; it's free.
- **The dyadic dominance `M − R = 1/D(n)` identity** — the load-bearing identity that makes the whole induction tick. Verify it explicitly in the approach file.

---

### Knowledge-base entries to use

- **Invariants & monovariants** — the alternating advantage sum `A = Σ(−1)^{i+1}p_i` (the game's natural monovariant; already certified as Lemma G's parity identity).
- **Induction (strong; load two statements into one induction)** — Pólya "a stronger statement is sometimes easier to prove by induction": load `L(n)` (Liu-side) and `L*(n)` (Xiang-side dual) together, exactly as Lemma G loads both move-orders.
- **Constructive / incremental** — the pair-pile construction (already certified) is the matching UPPER bound at the dyadic config; Lemma L is the matching LOWER bound; together they pin the dyadic saddle.

---

### Analogous past problems (cruxes)

- **`aimo-0117`** (games-and-strategy) — *"Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others."* The crux move: Jesse writes only powers of two, so `2^j > 2^{j−1} + … + 2^{−i}`, and the largest outweighs the rest regardless of the split. **Directly analogous** to the dyadic dominance `M = 2^n/D(n) > R = (2^n − 1)/D(n)` (the excess is exactly `1/D(n)`), which is the load-bearing identity of Opening A. (Note: `induct-one-mark` already cites this — the analogy holds; adapt, don't cite.)
- **`aimo-0019`** (games-and-strategy / invariants-and-monovariants) — *"In a covering game, respond to each opponent move by painting the cell immediately beyond the current filled frontier… so that no cell-size is ever painted twice ahead of the frontier"* and *"Bound a family of dyadic-length pieces of pairwise distinct sizes by twice the largest."* Analogous in that the game is played on dyadic-length pieces and the strategy is a look-ahead that controls which sizes get claimed. The "bound dyadic pieces by twice the largest" is the same flavor as `M − R = 1/D`.
- **`aimo-0964`** (induction-and-construction) — *"Read the whole evolution as a space-time matrix… prove a claim about a distinguished final row rather than tracking one step at a time"* and *"a corner sub-block of the space-time diagram is a scaled copy"* — the self-similar sub-block induction is the same shape as the level-(n−1)-scaled-R reduction. Worth adapting the "look at the whole matrix, not one step" framing for the global-sort interleaving obstruction.

(None of these is a direct citation — every borrowed step must be re-proved from scratch.)

---

### Prior progress (round 1, certified + verified)

- **Lemma G (greedy picking → odd-rank sum)** — fully certified in `lemmas/lemma-g-greedy-picking.md`. IMPORT IT; do not re-prove.
- **Pair-pile construction** — certified in `lemmas/lemma-pile-dyadic-cap.md`; gives the matching UPPER bound `f(n)` at the dyadic config for all n. Lemma L is the missing LOWER bound.
- **ΔA local-cut closed form** `ΔA = 2·((−1)^r b − T)` — certified in `lemmas/lemma-delta-a-local-cut.md`; explains the parity-flip-on-tail obstruction. The `M ⊎ R` decomposition here AVOIDS the local-cut tail-flip by working globally (M at rank 1, R as a block), which is why it survives where the per-mark monovariant failed.
- **L(1), L(2)** proved by casework (in `induct-one-mark`); L(2) brute-force corroborated.

---

### Dead ends (do NOT retry)

- **Naive level-induction on the dyadic self-similarity via local cuts / per-mark monovariants.** The certified ΔA closed form shows a single Xiang mark flips the parity of the entire tail (`−2T` term), so a per-mark reduction does NOT factor the per-round value recursion `1/f(n+1) = 1 + 1/(2f(n))`. (Round 1, `induct-one-mark`, verified-fatal.) The `M ⊎ R` decomposition here sidesteps this by NEVER doing a local cut — it works on the global M-vs-R split.
- **"Largest piece M dominates → bare dominant-piece claim pins top odd rank."** FALSE (round 1 counterexample: `M=0.6` split into `(0.3,0.3)`, `R=0.4` split into `(0.2,0.2)`, oddsum `= 0.5 < 0.6 = M`). The dyadic structure (`R`'s largest `= M/2`) is what avoids this; do NOT argue from bare dominance.
- **Multi-auxiliary strengthened IH** `evensum({w_1,…,w_j} ∪ R') ≥ Σ w_j`. FALSE (counterexample above). Do NOT propose this as the strengthened hypothesis; use the SINGLE-aux L* and handle k ≥ 2 via D1/D2.
- **Splitting the proof of Lemma L across slugs.** Each slug targets the whole c(n) claim end-to-end.

---

### Small-case / intuition notes (CONJECTURE)

- Lemma L (oddsum ≥ f(n) on the dyadic config) is **confirmed exact for n=1..5**; the floor is robust (thousands of extremal responses at n=5, all hitting exactly f(n), none below).
- The extremal is self-similar: the level-n pair-pile is the level-(n−1) pair-pile (scaled) plus M bisected.
- The strengthened IH L* is **confirmed for L=1..5** (single auxiliary, equality at the self-similar extremal).
- The k=0 (no marks in M) case is trivially disposed of; the k=1 case reduces cleanly to L*(n−1); **the k ≥ 2 case is the only genuine obstruction** on this route, and the per-round peeling (D1) is the most promising untested sub-reduction.

---

### Concrete skeleton for the outliner (slugify this)

```
Lemma L(n): for every ≤ n-mark refinement of the level-n dyadic config, global_A ≥ 1/D(n).
Lemma L*(n): for the level-n dyadic config R refined by ≤ n marks into R',
            and a single auxiliary w with 0 ≤ w ≤ R_largest := 2^n/D(n),
            evensum({w} ∪ R') ≥ w  (equiv. oddsum({w} ∪ R') ≤ total(R')).

Proof by simultaneous induction on n.
  Base n=1: L(1) by hand (round 1); L*(1) by 3-piece casework.
  Step n → n+1:
    L(n+1):
      Decompose level-(n+1) config as {M} ⊎ R, M = 2^{n+1}/D(n+1), R = scaled level-n config.
      Note M − total(R) = 1/D(n+1).   [load-bearing identity — verify explicitly]
      Case k=0 marks in M: global_A = M − A_rest ≥ M − total(R) = 1/D(n+1). ✓ [trivial]
      Case k=1 mark in M (M → (m_1,m_2), m_1 ≥ m_2):
        m_1 ≥ M/2 = R_largest, so m_1 is global rank 1.
        global_oddsum = m_1 + evensum({m_2} ∪ R')  (R' = R refined by n marks)
        ≥ m_1 + m_2   [by L*(n) with w = m_2 ≤ M/2 = R_largest]
        = M ≥ f(n+1). ✓
      Case k≥2 marks in M:  [OPEN — outliner's call: D1 per-round peel, or D2 WLOG-k=1 lemma]
        ... (reduces to L*(n) iterated with a per-round peel, OR a WLOG argument)
      L(n+1) done.
    L*(n+1):  [Xiang-side dual — symmetric argument with roles swapped]
      ...
```

The two OPEN sub-steps are (i) the k≥2 case of L(n+1), and (ii) the L*(n+1) inductive step. Both should be within reach of the per-round peeling (D1) since the value recursion is itself per-round.

**Report ends.**
