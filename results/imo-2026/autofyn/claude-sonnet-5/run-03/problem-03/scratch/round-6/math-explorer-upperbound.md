## imo-2026-03 (lens: upper-bound "large consecutive gaps everywhere" balanced sub-case)

- Distinct openings surfaced this round:
  1. **"Clean-instance vs. generic-instance" split.** Both certified Multi-Piece
     Necessity instances (`lp-duality-split-polytope`, n=3: `(2/5,3/10,1/5,1/10)`;
     n=4: `(1/3,4/15,1/5,2/15,1/15)`) are *exactly rational with hidden additive
     relations built in* — e.g. at n=3, `p1=2·p3` and `p2=p3+p4` exactly, which is
     precisely what makes a clean 2-piece "duplicate" response exist at all
     (splitting `p1→(p3,p3)` and `p2→(p3,p4)` gives the multiset
     `{p3,p3,p3,p3,p4,p4}`, all-even blocks, `OddSum=1/2`). This is evidence the
     hard region is a *low-dimensional, highly structured* locus of the simplex
     (partitions with built-in rational relations), not a generic open set — a
     genuinely different way to think about "how much of the balanced region is
     still open" than the population's current gap-in-a-family framing.
  2. **"All-even-blocks via pairwise merge chain" as a closed-form candidate.**
     Formalized and stress-tested a fully explicit rule: repeatedly take the two
     largest values in a working pool, split the larger into (smaller-copy,
     remainder) — an exact, real-valued cut, so no genericity issue — creating one
     exact tie per cut, until one leftover remains; then spend any spare cut budget
     bisecting the leftover (this provably reduces `OddSum` from `S+ℓ` to
     `S+ℓ/2` via the certified General Insertion / Doubling identity, an exact new
     one-line fact worth recording). This is a genuine multi-piece, adaptive,
     closed-form construction (not hand-tuned per instance) — see "Cheap-kill
     candidates" for its actual failure rate.
  3. **"Structured-optimum via LP vertex enumeration, statistics across random
     instances" — a data-driven opening.** Ran the true (numerically exact via
     multistart Nelder–Mead over every cut allocation) global optimum on 25 random
     balanced `n=3` partitions: **zero failures**, every instance closed with room
     to spare (best value `0.46`–`0.52` vs. target `0.5333`), and the *winning*
     cut allocation was overwhelmingly just **2 pieces split, 1 cut each** — most
     often `(top,2nd)` or `(top,bottom)` — i.e. genuinely a "small" multi-piece
     response, not requiring the full `n`-cut budget. This suggests the truly
     adversarial region (where 2-piece isn't enough, or where the specific pair
     matters) is a thin/extremal boundary set, and the right target for a general
     proof may be a **case split by codimension of the tie structure** (generic
     partitions vs. a finite-dimensional boundary family) rather than one uniform
     formula.

- Candidate technique(s):
  - **Merge-chain-plus-leftover-bisection** (opening 2): closed-form, adaptive,
    worth keeping in the population as a supplementary tool even though it does
    not close the region alone (see below) — its new sub-fact ("bisecting the
    leftover of a General-Insertion response strictly improves `S+ℓ→S+ℓ/2`") is a
    clean, reusable, one-line lemma not yet in any approach file.
  - **Vertex-enumeration-based case analysis stratified by "how many pieces need
    splitting"** (opening 3): use the Single-Piece-Split Vertex Lemma
    (`lp-duality-split-polytope`) plus its natural generalization to
    Two-Piece-Split (same LP-vertex machinery, extended to two simultaneously-split
    pieces — not yet written up by any approach but mechanically the same proof)
    to attempt: "for every balanced partition, SOME 2-piece response closes it" —
    a strictly weaker, more tractable target than a universal closed-form rule,
    and consistent with the empirical allocation statistics above (almost every
    random instance's optimum used exactly 2 split pieces).

- Cheap-kill candidates:
  - **Merge-chain family is provably insufficient, exhaustively.** Full exhaustive
    search over *every* order of "pairwise subtract-and-tie" moves (not just
    greedy two-largest) at `n=2` still fails on ~50% of random balanced
    instances (31/60 in one run) — a genuine negative result: the entire
    "reduce-to-one-leftover-via-exact-value-chain" family is structurally too
    narrow. Root cause identified: this family forces *every* piece into the
    matching chain, but the true optimum sometimes leaves several pieces
    completely untouched and unequal (e.g. splits *only* the smallest piece and
    leaves the top two alone) — a response shape merge-chain cannot represent
    since it always reduces the whole pool to size 1. This is a clean,
    checkable structural pruning fact for the next round: any future
    closed-form construction must allow "leave ≥2 pieces both untouched and
    mutually unequal," not just chains of ties.
  - Greedy two-largest / largest-smallest / closest-pair merge variants (with
    optimal leftover-bisection use of spare budget) all **fail 35%–100%** of
    random balanced instances across `n=2..8` (two-largest is best at ~35–65%
    failure, worsening with `n`) — confirms these specific closed-form rules are
    dead ends as *universal* rules (see numeric table below), though the
    underlying identity (`OddSum(R∪R∪{ℓ})→OddSum` improves to `S+ℓ/2` after one
    more bisecting cut) is a genuine new reusable fact.
  - "Bisect only the smallest piece, leave everything else untouched" — works on
    the specific `n=2` counterexample instance by coincidence (closes it,
    `0.513<0.571`) but **fails on 97%–100% of random balanced instances for
    `n≥3`** (488–500/500) — confirmed dead end as a general rule, not previously
    documented this precisely; worth recording so it is not retried as a
    candidate "simple fix."

- Knowledge-base entries to use: none beyond what the population already cites
  (LP/vertex-of-polytope facts, Extreme Value Theorem) — this lens found no new
  knowledge_base.md entry to invoke; the relevant tools are the population's own
  certified lemmas (`doubling-lemma-and-generalized-duplicate-the-rest.md`,
  `vertex-pinning-lemma.md`, `single-piece-split-vertex-lemma.md`,
  `anchor-merge-lemma.md`).

- Analogous past problems (cruxes): searched `combinatorics` /
  `games-and-strategy`, `extremal-principle`, `processes-and-algorithms`,
  `induction-and-construction` for adaptive dual-response / merge-pairing
  constructions. **None are genuinely analogous.** The closest superficial
  matches — `aimo-0012` (bin-packing into `k` groups of bounded sum, via a
  "mergeable adjacent pair" pigeonhole argument) and `aimo-0117` (dyadic/geometric
  power-of-two game where the largest value exceeds the sum of the rest) — are
  both single-player extremal/packing arguments or a different two-player
  mechanic (sealed-bid dyadic assignment), not a first-mover-claims-odd-ranks
  minimax game; borrowing their crux moves would not transfer any load-bearing
  step. Report: no true analog found in the corpus for this problem's specific
  "OddSum-of-a-refined-multiset" minimax structure.

- Prior progress: unchanged from `current.md` — Anchor-Merge Lemma (2-piece,
  closed-form, covers shrinking fraction of balanced region), Vertex Pinning
  Lemma (finite-search characterization for any *fixed* partition), Single-
  Piece-Split Vertex Lemma + two exact Multi-Piece Necessity instances (n=3,4).
  This round adds: (a) an exhaustive-search proof that the *merge-chain* family
  (not just single fixed rules already tried) is itself structurally
  insufficient, closing off a whole class of future candidate constructions at
  once; (b) the `S+ℓ→S+ℓ/2` leftover-bisection improvement as a small reusable
  fact; (c) numeric evidence (25/25 random `n=3` instances, 0 failures, mostly
  2-piece optimal responses) supporting a scoped-down target: prove a
  **Two-Piece-Split Vertex Lemma** (LP-vertex generalization of the certified
  single-piece one) and attack "some 2-piece response always suffices" as a
  more tractable intermediate goal than a universal closed-form rule.

- Dead ends (do not retry — new this round, in addition to the population's
  existing list of Suffix-Match-alone, Anchor-Merge-alone, single-piece-only):
  - **Merge-chain / greedy pairwise-tie-and-reduce-to-one-leftover, in any order**
    (exhaustive search over all orders, not just a fixed rule) — proved
    insufficient by direct exhaustive counterexample search at `n=2` (~50%
    failure even with the full search over all merge orders). Root cause: this
    family cannot represent "leave several untouched pieces mutually unequal,"
    which the true optimum sometimes requires.
  - **"Bisect smallest piece only, leave rest untouched"** as a general rule —
    fails 97–100% for `n≥3` (only coincidentally works on one specific `n=2`
    instance already in the population's record).
  - **Two-largest / largest-smallest / closest-pair greedy merge (+ optimal
    leftover bisection)** as standalone universal rules — all fail on a large
    fraction (35%+, worsening with `n`) of random balanced instances; do not
    resubmit any fixed-order merge heuristic without first checking it against
    this round's negative exhaustive-search result.

- Small-case / intuition notes (all conjecture/numeric, not proof):
  - Random (non-adversarially-constructed) balanced partitions appear to have
    large slack: in 25/25 sampled `n=3` instances the true numeric optimum was
    well under target (`0.46`–`0.52` vs. `0.5333`), achieved almost always by
    splitting only 2 of the 4 pieces (1 cut each) — far under the `n=3` cut
    budget. This suggests the *hard* instances are concentrated near a thin
    boundary/extremal set (matching the fact that both known Multi-Piece
    Necessity instances are exactly-rational, structured constructions, not
    generic points) — worth the next outline explicitly targeting "prove a
    Two-Piece-Split Vertex Lemma, then a general existence argument that *some*
    pair always works" rather than continuing to search for one closed-form
    formula that must handle every instance uniformly.
  - The numeric table for the merge-chain family (illustrative, `n=2..8`,
    300 random balanced-region trials each, two-largest variant):
    `n=2`: 42% fail; `n=3`: 41%; `n=4`: 40%; `n=5`: 51%; `n=6`: 55%; `n=7`: 58%;
    `n=8`: 65% (largest-smallest and closest-pair variants are strictly worse
    at every `n`) — failure rate roughly flat-to-worsening with `n`, consistent
    with the population's existing pattern that single fixed-rule constructions
    degrade as `n` grows.
