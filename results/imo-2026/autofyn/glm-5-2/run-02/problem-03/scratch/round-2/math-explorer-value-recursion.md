## imo-2026-03 — value-recursion / minimax-saddle route

### CRITICAL CORRECTION (the dispatch recursion is wrong)
The dispatch asks to prove `V(n+1) = (1+V(n))/2`. This is **mathematically inconsistent** with the verified closed form `f(n)=2^n/(2^{n+1}−1)`: with `V(1)=2/3`, it predicts `V(2)=(1+2/3)/2=5/6`, but the verified value is `V(2)=4/7`. The two recursions `V(n+1)=(1+V(n))/2` and `1/V(n+1)=1+1/(2V(n))` are **not equivalent** (setting them equal gives `2V^2−V+1=0`, discriminant −7).

The **correct** value recursion (verified algebraically AND numerically, see below) is

> **(R)** `1/V(n+1) = 1 + 1/(2·V(n))`,  equivalently `V(n+1) = 2·V(n)/(2·V(n)+1)`.

In advantage-sum coordinates `A = 2·V − 1` (so `A(n) = 1/D(n) = 1/(2^{n+1}−1)`), the cleanest form is the **Mersenne recursion**

> **(M)** `B(n+1) = 2·B(n) + 1`,  with `B(n) := 1/A(n) = D(n) = 2^{n+1}−1`, `B(1)=3`.

Equiv: `A(n+1) = A(n)/(A(n)+2)`, or `1/A(n+1) = 2/A(n) + 1`. The outliner MUST use (R)/(M), never `(1+V)/2`.

- Distinct openings:
  1. **Mersenne-recursion target (R)/(M).** Prove `1/V(n+1) = 1 + 1/(2V(n))` directly at the VALUE level — a round-level (one mark added to EACH player) recursion, not a per-partition monovariant (the per-mark route is a certified dead end, see dead-ends). The "+1" in `B(n+1)=2B(n)+1` is the load-bearing hard term.
  2. **Mirror strategy = clean dyadic-cap certificate (NEW this round).** Xiang's *mirror* — place marks at `1−x` for each Liu mark `x` — gives oddsum **exactly** `f(n)` on Liu's dyadic config for n=1..5 (verified). This is a SECOND, cleaner certificate of the dyadic saddle's Xiang side (alternative to the certified pair-pile), with a clean combinatorial proof via the symmetric-partition structure. **Caveat:** mirror FAILS as a general upper bound (counterexample: Liu marks `{1/5, 2/5}` → mirror oddsum = 3/5 > 4/7 = f(2)); also collides when Liu has a symmetric mark. So mirror is a dyadic-only certificate, NOT Lemma U.
  3. **Self-similar restriction via reflection** (the mirror mechanism's real power). The (n+1)-dyadic config = [largest piece `2^{n+1}/D(n+1)`] ∪ [n-dyadic config scaled to total `1−V(n+1)=D(n)/D(n+1)`]. The reflection `x ↔ 1−x` (mirror) creates a symmetric merged partition whose restriction to the "small half" is a scaled copy of the n-game. This is the value-recursion mechanism's closest structural analogue (cf. crux **aimo-0131**: restrict `B_{n+1} → B_n` via the reflection `x ↔ 2^{n+1}−x`).
  4. **Surrogate-adversary / saddle framing.** Treat (Liu config, Xiang config) as a zero-sum continuous game with payoff = oddsum. von Neumann/Sion do NOT apply directly (strategy spaces `[0,1]^n` minus diagonals are not convex; payoff is neither convex nor concave). No clean minimax theorem short-circuits Lemma U. Surrogates (stronger Xiang dropping the refinability constraint) are too strong (value → 0); weaker Liu surrogates reduce to Lemma L. So the saddle must be EXHIBITED, not derived from a general theorem: Liu's dyadic config + Lemma L (lower) vs a Xiang strategy + Lemma U (upper). The value-recursion route is a REPHRASING of (L+U) into one statement, not a bypass.

- Candidate technique(s):
  - **Round-level value induction on n** with the Mersenne recursion (M) as target — load the lower and upper halves into ONE induction (cf. Pólya "stronger statement easier by induction", already used in certified Lemma G).
  - **Mirror (point-reflection `x ↔ 1−x`) as Xiang's saddle strategy on the dyadic config** — clean combinatorial proof via symmetric-partition counting.
  - **Self-similar restriction** (crux **aimo-0131** analogue): the (n+1) game restricted to its "small half" is a scaled n-game; the reflection identifies the sub-instance.
  - In the advantage coordinate `A = 2·Liu − 1`, the target `A(n) = 1/D(n)` and recursion `1/A(n+1) = 2/A(n) + 1` are the natural "linearized" form (cf. the certified `ΔA` lemma's spirit — work in `A`-space, not partition-space).

- Cheap-kill candidates:
  - **Mirror-as-dyadic-cap** is a near-trivial proof (symmetric partition → oddsum = (1+c)/2 where c = central piece; for dyadic, c = 1/D(n) = smallest, lands at an odd rank by a counting argument on the pair structure). This REPLACES the pair-pile construction as the cleaner dyadic-cap certificate and is a genuine cheap kill for the dyadic half of the saddle.
  - **v_2 / Mersenne structure of `D(n) = 2^{n+1}−1`** — the recursion `B(n+1)=2B(n)+1` is the Mersenne recurrence; `B(n)+1 = 2^{n+1}` is a pure power. This power-of-2 structure is what makes the dyadic config (powers of 2) the unique fixed point.
  - No cheap kill for the GENERAL upper bound (Lemma U) — the interleaving obstruction is the real wall.

- Knowledge-base entries to use:
  - **Invariants & monovariants** — the advantage sum `A = Σ(−1)^{i+1} p_i` and its certified `ΔA` closed form are the linearization engine.
  - **Induction (strong, loading both bounds into one induction)** — cf. certified Lemma G's structure; the round-level value recursion wants the same "prove a stronger statement" trick.
  - **Extremal principle** — the dyadic config is the unique extremal (two-regime insight: cap tight ONLY at dyadic; cap ≤ 1/2 < f(n) elsewhere — sibling explorer's lever, usable here as the regime-split for Lemma U).
  - **Pigeonhole/extremal** — the "largest unclaimed piece ≥ target rank" invariant already used in Lemma G.

- Analogous past problems (cruxes):
  1. **aimo-0131** (`induction-and-construction`, `bijections-and-encoding`) — *the strongest analogue*. Crux: "Restricting a funny `M ⊂ B_{n+1}` to `B_n` yields a funny `A ⊂ B_n`; each upper-half element `y = 2^{n+1}−x` lies in `M` iff `x` is NOT in `A`." The **reflection `x ↔ 2^{n+1}−x`** creates a self-similar sub-instance and drives the count recursion `B_{n+1} → B_n`. This is *exactly* the mirror mechanism (`x ↔ 1−x` on [0,1]) and the self-similar-restriction engine for the value recursion (M). Adapt (do not cite): the mirror's merged partition restricted to its small half is a scaled n-game.
  2. **aimo-0019** (`games-and-strategy`, `invariants-and-monovariants`) — dyadic-interval covering game; B responds by painting the "next dyadic interval just right of the frontier," bounding swallowed pre-painted pieces by "twice the largest." Crux: dyadic-length pieces of pairwise distinct sizes are bounded by twice the largest. Directly analogous to the dyadic dominance (largest piece `2^n/D` exceeds the sum `2^n−1` of all others by `1/D`). Adapt: the dyadic config's "largest exceeds sum of rest by `1/D`" is the load-bearing structural fact.
  3. **aimo-0117** (`games-and-strategy`) — "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." This IS the dyadic-dominance principle in a two-player game. Adapt: Liu's dyadic config realizes exactly this "largest exceeds all others" structure, and the boundary case (second-largest = largest/2 exactly) is what makes the dyadic config the unique tight saddle.

- Prior progress (certified, importable):
  - **Lemma G** (greedy → oddsum) — fully proved (`lemmas/lemma-g-greedy-picking.md`).
  - **Parity identity** `Liu = (1+A)/2`, `A = Σ(−1)^{i+1} p_i` — corollary of Lemma G.
  - **ΔA local-cut** `ΔA = 2((−1)^r b − T)` (`lemmas/lemma-delta-a-local-cut.md`) — explains the parity-flip-on-tail obstruction (the `−2T` term).
  - **Pair-pile construction** (`lemmas/lemma-pair-pile-dyadic-cap.md`) — Xiang caps dyadic at `f(n)`, all n. NOW SUPERSEDED-IN-SPIRIT by the cleaner mirror certificate (this round) — outliner may swap pair-pile for mirror as the dyadic-cap half of the saddle.
  - n=1 complete; L(2), U(1) proved.

- Dead ends (do not retry):
  - **Per-Xiang-mark induction on the partition** (the `induct-one-mark` Lemma U gap) — VERIFIED FATAL: the recursion (R) is per-ROUND (both players add a mark), not per-mark; a single Xiang mark does NOT drive `A → A/(A+2)` (counterexamples: on `A=1/3`, Xiang bisect gives `A'=1/3` not `1/7`; on `A=1/2`, bisect gives `A'=1/4` not `1/5`). The `−2T` parity-flip-on-tail term is the obstruction (certified `ΔA` lemma). Do NOT re-attempt per-mark monovariants.
  - **Hall matching for Lemma U on non-dyadic configs** (the `pairing-partner` gap) — Hall-condition dominance fails on simple non-dyadic examples. Dead.
  - **Bare dominant-piece claim** ("largest interval exceeds sum of rest → pins top odd rank") — FALSE (counterexample `M=0.6 → (0.3,0.3)`, `R=0.4 → (0.2,0.2)`, oddsum=0.5 < M). The correct lever is dyadic self-similarity (R's largest = M/2), not bare dominance.
  - **Mirror as a GENERAL upper bound (Lemma U)** — FALSE (this round): mirror gives exactly `f(n)` on dyadic but FAILS on non-dyadic (counterexample Liu `{1/5, 2/5}` → mirror oddsum `3/5 > 4/7 = f(2)`; also collides when Liu has a symmetric mark). Mirror is a dyadic-only certificate.

- Small-case / intuition notes (CONJECTURE / evidence, not proof):
  - **Full minimax `V(2) = 4/7` re-confirmed this round** by exhaustive grid (denom 28, 351 Liu configs × full Xiang best response): max-min = 4/7 exactly, matching `f(2)`. Multiple Liu configs attain 4/7 (dyadic `1/7,3/7` AND others e.g. `3/28, 9/28`) — the optimum is flat near the dyadic config (suggests a continuum of optimal configs, consistent with the two-regime insight "cap tight only at dyadic" being about the Xiang cap, not Liu's uniqueness).
  - **Xiang best-response oddsum on the dyadic config = `f(n)` exactly for n=1,2,3** (this round, exact rational grid): n=1→2/3, n=2→4/7, n=3→8/15. Corroborates Lemma L's tightness AND the pair-pile/mirror cap simultaneously (lower = upper = f(n) on the dyadic saddle).
  - **Mirror on dyadic gives exactly `f(n)` for n=1..5** (this round): the merged symmetric partition has pieces = pairs `(2^k/D, 2^k/D)` for `k=1..n−1` plus THREE copies of `1/D` (one pair + the central). Sorted: the three `1/D`'s occupy ranks `2n−1, 2n, 2n+1`; Liu captures ranks `2n−1` and `2n+1` (two of the three). Oddsum = `Σ_{k=1}^{n−1} 2^k/D + 2/D = (2^n−2)/D + 2/D = 2^n/D = f(n)`. ✓ This is a CONJECTURE-grade clean combinatorial proof skeleton (the rank-counting needs rigorous verification that the central `1/D` lands at an odd rank — verified numerically n=1..5, proof by the pair-counting above).
  - **The hard step for a clean round-level proof of (R)/(M):** the interleaving obstruction (round 1, certified) persists at the value level. The (n+1)-dyadic config = [piece `V(n+1)`] ∪ [scaled n-dyadic config of total `1−V(n+1)`], but the global descending sort INTERLEAVES pieces from the large piece and the small sub-config (the dyadic config's second-largest = `V(n+1)/2` exactly, the boundary case). So "the value of the (n+1) game = `V(n+1) + (1−V(n+1))·(value of n-game scaled)`" does NOT hold by simple additivity — the recursion's `+1` term is precisely the interleaving-boundary correction. A clean value-level proof would need to show this correction equals exactly `+1` in `1/A`-space via a potential that accounts for the global sort. **No such potential is identified this round** — the honest assessment is that the round-level recursion (R) is the right TARGET but a slick proof is not yet found; the outliner should attempt it but fall back to (Lemma L + Lemma U) if the value-level argument doesn't close.

### Concrete skeleton for the outliner (slugify as `value-recursion` or `mirror-saddle`)

**Target.** `c(n) = 2^n/(2^{n+1}−1) = f(n)`, via the Mersenne recursion `B(n+1)=2B(n)+1` on `B=1/A=1/(2·Liu−1)`, `B(1)=3`.

**Lower bound `V(n) ≥ f(n)` (Liu side).** Liu plays the dyadic config. Three sub-options for the proof (the outliner picks the most closable):
  - (a) **Lemma L general-n** (interleaving) — the open gap from round 1; the self-similar-reduction `B_{n+1}→B_n` (cf. aimo-0131) is the unpicked lever: induct on n by splitting the (n+1) dyadic config into its largest piece + the n-dyadic sub-config, using the reflection `x↔1−x` (mirror) to identify the sub-instance and control interleaving.
  - (b) **Round-level value recursion (lower half)** `1/V(n+1) ≥ 1 + 1/(2V(n))` — Liu's (n+1)-game ≥ `f(n+1)` given the n-game ≥ `f(n)`. Hard step: the interleaving correction.
  - (c) Fall back to certified L(1), L(2) + Lemma L as open gap (honest).

**Upper bound `V(n) ≤ f(n)` (Xiang side).** Two sub-options:
  - (a) **Mirror certificate for the dyadic config** (NEW, clean) — proves the dyadic saddle's Xiang side cleanly (replaces pair-pile). Combinatorial proof via symmetric-partition rank-counting (skeleton above). This pins `V(n) ≤ f(n)` ONLY for Liu's dyadic config — NOT a general upper bound.
  - (b) **Lemma U general-n** (the main gap) — for arbitrary Liu configs, Xiang forces ≤ `f(n)`. The two-regime split (sibling explorer): mirror/pair-pile achieves exactly `f(n)` on dyadic (regime 1); for non-dyadic configs Xiang forces ≤ 1/2 < f(n) (regime 2, via bisect-largest or surrogate). The outliner should pair this value-recursion approach with the sibling's two-regime route to close Lemma U.

**Recursion verification.** State (R)/(M) explicitly; verify `f(n)` satisfies it by substitution (already done in `induct-one-mark`); verify `B(n)=D(n)=2^{n+1}−1` satisfies `B(n+1)=2B(n)+1`. Crucially, CORRECT the dispatch's wrong `(1+V)/2` form.

**Importable certified lemmas.** Lemma G, parity identity `Liu=(1+A)/2`, ΔA local-cut. The mirror certificate can be proposed for certification (replaces/simplifies pair-pile).

### Honest bottom line
- The recursion `1/V(n+1)=1+1/(2V(n))` (Mersenne form `B(n+1)=2B(n)+1`) is the right value-recursion target, algebraically solid and numerically corroborated (n=1..5).
- **A clean round-level proof is NOT in hand.** The interleaving obstruction blocks the partition-level reduction, and the value-level argument needs a potential not yet identified. The outliner should ATTEMPT the round-level recursion but treat (Lemma L + Lemma U) as the fallback — the value-recursion route is best used as the UNIFYING FRAME (one statement packaging both bounds) rather than a bypass.
- The **mirror certificate** is this round's concrete, closable contribution: a clean new dyadic-cap proof (replaces pair-pile) and the structural key (`x↔1−x` reflection, aimo-0131's self-similar-restriction mechanism) for any future round-level induction.
