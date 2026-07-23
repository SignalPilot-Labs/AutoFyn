# proof-builder report — intersecting-family-covering-construction (round 9)

## Task executed
Per the outliner's directive (a third, independent FCBC technique: per-core-
**pair** witness-pool stabilization, more general than a single universal
window), built on this approach's own already-certified Theorem 5.1
(periodicity-from-`n=1`, conditional on FCBC).

## What was proved (new, this round)

**Theorem SW (Stabilization Sufficiency), proved in full, no gaps.**
Combining the already-certified Theorem CD (core decomposition, `≤2^k-1`
cores) with the already-certified Finite-Class Direct Covering lemma and
Lemma P′, I showed FCBC reduces *unconditionally* to a much narrower target:
a finite witness pool need only be exhibited for pairs of proper cores
`(S,S')` that are **disjoint AND both have infinitely many members**
("doubly-infinite disjoint core pairs") — every other case (coincident
cores, overlapping cores, or a disjoint pair with either side finite) is
disposed of automatically, using only already-certified facts. If this
narrower "Stabilization Conjecture" holds for every such pair (a fixed
finite list, `≤C(2^k-1,2)` of them, once `a_1` is fixed), FCBC holds, and
this file's own Theorem 5.1 then finishes the **entire problem**.

This is a genuine reduction (not a restatement): I checked it against the
already-certified round-5 Channel Assembly/Splitting machinery and confirmed
it is a logically distinct, formally weaker per-channel hypothesis (doesn't
require the minimal-radical antichain to stabilize, just that *some* finite
hitting set exists).

Also proved a small free structural fact, **Lemma SW3 ("peeling")**: any
finite subset of one side of a channel is automatically covered against the
whole other side — confines the Stabilization Conjecture's open content to
the *tail* behavior of both sides.

## Numerical work (Python, fresh generator, independently verified)

Built an efficient greedy-sequence generator (smallest-prime-factor sieve +
trial-division fallback) and tested the Stabilization Conjecture directly
on 7 disjoint proper-core pairs across 4 `a_1` values: `247`, `2747`,
`21528751`, and (deliberately adversarial, chosen because round 3 found the
*global* canonical witness set very likely unbounded there) `4199`, `4087`.

Result: **every single tested channel stabilizes to a tiny (≤7-prime)
witness pool**, verified with full brute-force cross-pair checking up to
~1.9×10^8 pairs per channel — zero exceptions anywhere. This includes an
exact, independent reproduction and explanation of sibling
`explicit-window-backbone-construction`'s "bridge prime 97" finding for
`a_1=21528751`: `a_596` (core `{1061}`) and `a_863` (core `{103,197}`) have
companion sets `{2,3,5,7,97}` and `{11,97}`, intersecting in exactly `{97}`
— exactly the doubly-infinite disjoint-core-pair case my framing predicts is
the hard case. On the adversarial `4199`/`4087` examples, per-channel pools
still stabilized (`≤3` primes, last growth within the first 9 relevant
indices) even though the *global* witness set is very likely unbounded
there — suggesting global unboundedness is a cross-channel phenomenon, not
within-channel difficulty.

## What remains open

The Stabilization Conjecture itself (finiteness of the per-doubly-infinite-
channel witness pool) is **not proved** — this is the honest, sole
remaining gap for this file's whole chain, and (per Lemma SW3) is now known
to live specifically in the *tail* behavior of the two index classes. It is
numerically extremely well-supported (7/7 tested channels, ~370M+ brute-
force-checked pairs, zero exceptions, including two deliberately adversarial
instances) but a general proof was not found in the time available.

## Status: partial

File written: `results/imo-2026-06/approaches/intersecting-family-covering-construction.md`
(Status `partial`; new Round 9 sections added at top: headline update,
Part 8 Theorem SW with full proof, numerical evidence table, Lemma SW3,
updated Approaches-tried and Promotable-lemmas sections. All prior certified
content — Lemma A, Corollary 3.1, Lemma B, Theorem 5.1 — untouched.)

## Promotable lemmas this round
- **Theorem SW (Stabilization Sufficiency)** — full proof in Part 8.
- **Lemma SW1** (automatic coverage for intersecting cores) — 3-line proof,
  Part 8.
- **Lemma SW2** — reproduction/import of the already-certified Finite-Class
  Direct Covering lemma, restated for self-containedness.
- **Lemma SW3 (Peeling)** — full proof in Part 8, a strict generalization
  of Lemma SW2's hypothesis.
All recommended for reviewer certification into `results/imo-2026-06/lemmas/`
(Theorem SW especially — it is directly reusable by any future approach
attacking FCBC, and gives an immediate finish for any `a_1` whose finitely
many doubly-infinite channels can be individually resolved).
