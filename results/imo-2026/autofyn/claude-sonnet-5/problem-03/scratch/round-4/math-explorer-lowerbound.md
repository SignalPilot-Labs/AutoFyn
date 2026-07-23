## imo-2026-03 — lens: lower-bound direction's §5.2 gap (XY spending ≥2 cuts inside the dominant piece)

### Terrain (what's proved / what failed, per current.md and dyadic-cascade-induction.md §5)

- Target: against LB's specific dyadic construction `D_m=(2^m,…,2,1)/(2^{m+1}-1)`, XY (≤m further
  cuts) cannot force `e` below `e_m=1/(2^{m+1}-1)`. Proved by strong induction on `m` using two
  general facts: **Fact 1** `e(M)≥0` for any sorted `M`; **Fact 2** ("dominant extraction")
  `e(M)=x_1-e(rest)`, hence `e(M)≤max(M)` (`lemmas/dominant-extraction.md`), plus **Lemma P**
  (duplicate-pair invariance, `lemmas/duplicate-pair-invariance.md`).
- **Branch A** (XY's cuts never touch `a_1`): fully closed for every `m`, unconditional over how
  XY distributes cuts on `R=D_m\{a_1}` — two-line proof via Fact 2 twice.
- **Branch B, single cut on `a_1`**: fully closed. Case B1 (bisect `a_1`): Lemma P collapses the
  bisection-created pair against `R`'s existing top duplicate, residual is exactly `D_{m-1}`
  rescaled, IH closes it with equality attainable (`e=e_m` exactly). Case B2 (match `a_1` to some
  `a_i`, `i≥3`): the leftover `a_1-a_i` dominates the rest of `R\{a_i}` (`a_1-a_i≥a_2`), so Fact 2
  gives a clean elementary bound with no induction needed.
- **§5.2, the open gap**: `≥2` of XY's cuts land inside the *currently-dominant* piece (directly
  trisecting/quadrisecting `a_1`, or matching then further cutting the leftover `a_1-a_i`). Strong
  numeric support (exhaustive `m=2`; broad `m=3,4`, up to 300k trials) — minimum found is always
  exactly `e_m`, i.e. a **tie**, never a strict violation. The natural "merging never increases
  `e`" general monotonicity lemma was tested and is **FALSE** (>1/3 of 40,000 random trials with
  the dominance hypothesis `a>sum(Rest)` violate it) — confirmed independently by me: comparing an
  arbitrary 2-part split of a dominant piece against an arbitrary 3-part split of the same piece
  (both combined with a fixed random `Rest`) gives `e_3 < e_2` in ~68% of 20,000 random trials
  (script run this round) — the general inequality really is false for arbitrary side-multisets,
  so ruling this out is correct and should not be revisited as stated.

### A concrete new structural observation this round (not in the file, worth flagging to the outliner)

I reconstructed the `m=3` numerically-found "2-cuts-inside-`a_1`" tying example
(`(a_2,a_3,a_3)=(4/15,2/15,2/15)`, from cascading: bisect `a_1`, then bisect *one* of the two
resulting `a_2`-halves down to `a_3`-size) and traced it through Lemma P by hand
(`Fraction` check, this round):
- Final multiset `{a_2,a_2,a_3,a_3,a_3,a_4} = {4/15,4/15,2/15,2/15,2/15,1/15}`.
- Lemma P cancels the two `4/15`s (one from `a_1`'s first half, one from `R`'s own `a_2`) →
  `{2/15,2/15,2/15,1/15}`; cancels a `2/15` pair → `{2/15,1/15}` → `e=1/15=e_3`. ✓.
- **Key finding:** this is *exactly* algebraically identical (after the two Lemma-P cancellations)
  to "bisect `a_1` once (Case B1, cut 1) **then apply `R`'s own optimal recursive move** — bisect
  `R`'s top element `a_2` (cut 2, spent on `R`, not on `a_1`)." The 2nd cut, though it geometrically
  subdivides a *fragment of `a_1`*, is value-equivalent via telescoping duplicate-cancellation to
  spending that same cut on `R`'s recursive structure instead. **So this particular "multi-cut
  inside `a_1`" strategy is not actually a new strategy at all — it's a disguised re-encoding of
  Branch B1 composed with the level-`(m-1)` IH's own optimal move, which is already covered.**
  This is a hand-derived structural fact (not just a numeric tie), and it suggests the gap may be
  an artifact of casing by *cut location* (inside `a_1` vs. inside `R`) rather than a real second
  obstruction — the natural fix is to stop casing on *where* a cut geometrically lands and instead
  case on the *final multiset of values* (which Lemma P already makes location-independent for
  cancellation purposes). This is a genuinely different top-level reduction, not a variant of the
  falsified merging-monotonicity mechanism — flag as promising but **unverified beyond this one
  instance**; do not present as proved.

### Candidate mechanisms from the knowledge base / crux corpus (query used: `domain=combinatorics`,
subtopics `games-and-strategy`, `extremal-principle`, `induction-and-construction`,
`invariants-and-monovariants`; also cross-checked `crux_moves_documentation.md` schema first)

1. **Minimal-counterexample + extremal secondary-statistic selection with local exchange**
   (crux `aimo-0287`, subtopic `extremal-principle`: "test a single boundary exchange... force the
   exchange not to improve the objective, reading off an inequality"; and `aimo-0438`: "among all
   optimal configurations select one maximizing a secondary alignment statistic, then show any
   local deviation admits an improving exchange, contradiction"). **Adapt as:** suppose for
   contradiction some `m` and some XY strategy against `D_m` beats `e_m`; among all such
   violators, take one minimizing `m`, then (secondarily) minimizing the number of cuts landing
   inside the current dominant piece. Branch A/B already rule out 0 or 1 such cuts, so a minimal
   violator has `≥2`. Show a local exchange (collapse two of its cuts into one, using the specific
   dyadic dominance structure, not a generic side-multiset) either reduces the cut-count (contra
   minimality) or contradicts `m`-minimality. This is **narrower** than the falsified general
   lemma — it only needs to hold *along an assumed minimal violator* (which by minimality already
   satisfies `e<e_m`), not for every configuration with a dominant top piece, so the falsifying
   counterexamples (generic `Rest`, no `e<e_m` assumption) don't automatically apply. This is the
   most promising avenue and matches the requested "exchange-argument... without assuming the
   residual behaves like a top-level fresh instance" framing (item (c) in the dispatch).

2. **Induction-loading / strengthen the claim to a broader class before inducting**
   (crux `aimo-0292`, subtopic `induction-and-construction`: "replace the rigid boundary value
   with an inequality and widen the free parameter's range so the induction hypothesis actually
   applies to the smaller instance" — proved by peeling one block and requiring the *residual*
   hypothesis to be loose enough, `s≤2n` not `s=2n`, to apply after deletion). **Adapt as:**
   the file's own §5.2 write-up already names this option (a): strengthen the IH from "exactly
   `D_j`" to a class of "top-heavy" multisets (`x_1≥`some threshold on `rest`, `rest` not
   necessarily exactly dyadic) so that after `a_1` is cut into fragments interleaved with `R`'s own
   cuts, the residual configuration — no longer exactly a scaled `D_{m-1}` — still lies inside the
   widened hypothesis's scope. The structural observation above (cascading cuts inside `a_1`
   telescope via Lemma P into moves equivalent to cuts on `R`) suggests the right broadened class
   might be: "any sorted multiset expressible as (dyadic-like top run) ∪ (arbitrary further-cut
   residual)," closed under Lemma-P cancellation.

3. **Surrogate/finite-menu reduction for a multi-move adversary**
   (crux `aimo-0560`, subtopic `games-and-strategy`: "replace the adversary with a strictly
   stronger surrogate whose reply is pointwise at least as damaging... the reply collapses to a
   finite per-region menu"). **Adapt as:** complete the "joint vertex enumeration" that the
   approach file's own vertex lemma (§3) gestures at but does not carry out for simultaneous
   multi-cuts on one piece — by the vertex lemma, a joint optimum of `c` cuts on `a_1` is itself at
   a joint breakpoint (each individual cut is a bisect-or-match against the *current* multiset), so
   the candidates for `c` cuts inside `a_1` form a finite, explicitly enumerable tree of
   cascading bisect/match choices (as in the worked `m=3` example above) — not a continuum. Proving
   *every* leaf of this finite tree reduces (via repeated Lemma P) to an already-covered
   Branch A/B/IH case would close the gap without any monotonicity lemma at all.

4. (Lower confidence, structurally different) **Split-and-recombine / average-of-two-shifted-copies
   bound** (crux `aimo-0298`, subtopic `induction-and-construction`: split a configuration into two
   overlapping sub-configurations sharing a common part, retaining only one parity class each, and
   bound the target quantity by the *average* of the two induced sub-instances). Could potentially
   apply by splitting the `c+1≥3` fragments of `a_1` into two groups (e.g. by creation order/parity
   in the cut-cascade tree), each combined with `R`, and bounding `e` by a weighted average of the
   two induced sub-problems — untested, offered only as a structurally-available alternative if
   (1)–(3) stall.

### Assessment

Mechanism **(1)** (minimal-counterexample + extremal local exchange) is the most promising: it
survives exactly the objection that killed the general merging-monotonicity lemma (that lemma
failed because it was asserted for *arbitrary* side-multisets with no `e<e_m` hypothesis; a
minimal-violator argument only needs the exchange step to work *given* the extra structure of an
assumed counterexample). Mechanism **(3)** is a close second and is concretely supported by the
hand-worked `m=3` telescoping example above, which shows at least one class of "genuine" multi-cut
strategies is secretly not new at all — a finite-tree enumeration argument could formalize exactly
this observation across the whole tree. Mechanism **(2)** is the "official" option (a) already
named in the file and is a reasonable fallback if (1)/(3) don't close cleanly, but is likely more
work (need to find and verify the correct broadened invariant class). Mechanism (4) is speculative.

### Cheap-kill candidates
None obvious beyond what's already used (Lemma P duplicate-cancellation, Fact 1/2 dominant
extraction) — the obstruction is genuinely structural (interleaving of `a_1`'s fragments with
`R`'s own cut fragments in sorted order), not a size/parity/pigeonhole shortcut. The telescoping
observation above is the closest thing to a structural shortcut found this round.

### Knowledge-base entries to use
- `knowledge_base.md` "Problem-Solving Heuristics (Pólya)": *Generalize* — "a stronger, cleaner
  statement is sometimes easier to prove by induction (induction loading / strengthening the
  hypothesis)" — directly supports mechanism (2).
- `knowledge_base.md` "General Proof Methods": *Contradiction* / *Pigeonhole / extremal*
  ("take the largest/smallest object and argue it forces the result") — supports mechanism (1)'s
  minimal-counterexample framing.
- No KB entry specifically covers multi-move-inside-one-region game arguments; the crux corpus is
  the primary source here.

### Analogous past problems (cruxes)
- `aimo-0287` (algebra/extremal-principle-adjacent, exact subtopic `extremal-principle`) — boundary
  exchange forcing an inequality from minimality; genuinely analogous *proof shape* (not subject
  matter) for mechanism (1).
- `aimo-0438` (combinatorics, `extremal-principle`) — "select optimal configuration maximizing a
  secondary statistic, any local deviation admits an improving exchange, contradiction" — same
  shape, directly reusable as the template for a minimal-violator argument (mechanism 1). Subject
  matter (lattice paths/coloring) is unrelated; only the proof shape transfers.
- `aimo-0560` (combinatorics, `games-and-strategy`) — surrogate-adversary + finite-menu reduction
  in a two-player alternating game; genuinely analogous proof shape for mechanism (3). Subject
  matter (tree-growing game) is unrelated.
- `aimo-0292` (combinatorics, `induction-and-construction`) — induction-loading example (widen the
  claim so the IH applies after peeling); analogous shape for mechanism (2).
- `aimo-0117` (combinatorics, `games-and-strategy`) — already the source of the dyadic/superincreasing
  insight used elsewhere in this problem; not newly relevant to §5.2 specifically, noted for
  completeness only.
- None of these are subject-matter matches (no crux in the corpus is a literal stick-cutting /
  interval game at this level of generality) — all four are proof-shape analogies to be adapted
  and re-proved from scratch, per CLAUDE.md.

### Prior progress
Current best on this exact gap: Branch A and Branch B (single cut on `a_1`, both bisection and
every match alternative) fully proved for every `m` (`dyadic-cascade-induction.md` §5, §5.1).
`≥2` cuts inside `a_1`: open, numeric tie only (`e=e_m` exactly at every tested minimum, never
below), general "merging monotonicity" fix falsified.

### Dead ends (do not retry)
- The general "merging the two smallest parts of a partition of a dominant piece `a` (holding
  `Rest` fixed, `a>sum(Rest)`) never increases `e`" monotonicity lemma — **FALSE**, re-confirmed
  independently this round (my own 20,000-trial random check: ~68% violation rate comparing
  arbitrary 2-part vs. 3-part splits of the same dominant piece against a fixed random `Rest`).
  Any future fix must restrict to *optimal* (vertex-lemma) splits and/or an assumed-minimal-
  violator hypothesis, not an unconditional inequality over all splits.
- Do not re-derive Lemma G, Lemma P, Fact 1/2 — already certified, import from `lemmas/`.

### Small-case / intuition notes (conjecture, not proof)
- The `m=3` worked telescoping example (this round) suggests the "genuine" multi-cut-inside-`a_1`
  strategies that *tie* the bound are exactly cascading bisect/match sequences that, after
  repeated Lemma P cancellation, reduce to strategies already covered by Branch B1 composed with
  the IH's own recursive move on `R` — i.e., the gap may be a bookkeeping/casing artifact rather
  than a genuinely new adversarial power. This is a conjecture based on one hand-traced instance,
  not a general proof; the outliner/builder should check whether this telescoping argument
  generalizes to the `m=4`, 3-cuts-inside-`a_1` numerically-found tying example noted in the file
  (`§5.2`: "3 of the 4 cuts entirely inside `a_1`, quadrisecting it into 4 parts") before trusting
  it as a real mechanism.
