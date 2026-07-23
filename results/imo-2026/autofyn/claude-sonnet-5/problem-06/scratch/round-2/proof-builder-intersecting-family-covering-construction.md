# Build report — intersecting-family-covering-construction (round 2)

## What I did

Read the outline-reviewer's critique (`/tmp/round-2/outline-reviewer.md`): Step 4's
claim "`H` must equal `B`" (the persistent-divisor set) was independently proven
false by the reviewer (an AP-density argument showing `B` is essentially cofinite),
with the correct replacement target identified as the canonical minimal witness set
`W := ⋃_{i<j} {w(i,j)}`, `w(i,j) := min(rad(a_i)∩rad(a_j))`.

Retargeted Step 4 onto `W` as directed, then pushed the Step 5 strong-induction
architecture substantially further than the round-1/round-2-outline sketch, arriving
at three new, fully proved results (all conditional on `W` finite — that finiteness
itself, `(†)`, is the shared open gap with the sibling approaches and was **not**
attempted here, per the outline-reviewer's routing to `persistent-backbone-monovariant`
for that piece):

1. **Theorem 2.2 (H-hitting characterization)** — a clean, unconditional-given-`(†)`
   derivation that `a_{n+1} = min{x > a_n : x's H-signature hits every earlier term's
   H-signature}`. This is a pure logical consequence of the definition of `W`, needing
   no numerical verification — it converts the whole problem into finite combinatorics.
2. **Lemma 2.3 (Σ-stabilization)** — the finite family of distinct "H-signatures"
   seen among `a_1,…,a_n` stabilizes by an explicit finite index `N_1 ≤ 2^|H|-1`.
3. **Theorem 2.4 (conditional eventual periodicity)** — combining 1 and 2 with a
   pigeonhole/functional-graph argument on the finite state space `ℤ/Lℤ`
   (`L=lcm(W)`), proved: if `W` is finite, there exist `T, L_per, N_2` with
   `a_{n+T} = a_n + L_per` for **all** `n ≥ N_2`. This is new — no approach in the
   population had previously shown a clean bridge from "backbone/witness finiteness"
   to periodicity, even eventual periodicity.

I then attempted to close the remaining gap (periodicity from `n=1`, not just
eventually) and tested a natural candidate mechanism computationally (whether the
minimal candidate under a partial constraint set always already satisfies the full
eventual constraint set). This **holds for `a_1=15`** but **fails for `a_1=35` and
`a_1=65`** under the naively-guessed `H=rad(a_1)` (as opposed to the true `W`, not
yet pinned down for those examples). I report this as an honest negative finding —
it does not disprove periodicity-from-1 in general, only rules out this specific
naive route under a possibly-wrong `H`, and flags that the correct next step is to
first pin down the true `W` for these examples before re-testing.

## Status: partial

Case I of the problem's dichotomy (Proposition D, round 1) remains fully solved.
For Case II, the round-1 gap ("no bridge from finiteness to periodicity") is now
closed conditionally (Theorem 2.4). Two gaps remain, both honestly flagged in the
file: (1) finiteness of `W` itself (shared, open — `persistent-backbone-monovariant`'s
live attempt), (2) periodicity from `n=1` rather than eventually (shown to require
more than the tested naive mechanism; genuinely open).

## Key file

`results/imo-2026-06/approaches/intersecting-family-covering-construction.md`
(updated in place). New content is Part 1–3 (canonical witness definition,
Theorems 2.2/2.4, Lemma 2.3, and the honest gap analysis in Part 3). Round-1
content (Lemma P, Q, R, S′, Proposition D) preserved unchanged and cited from
`lemmas/`.

## Promotable lemmas proposed for certification

- **Theorem 2.2 (H-hitting characterization)** — general (works for any finite `H`
  with `w(i,j)∈H` for all `i<j`, not just `H=W`), fully proved, reusable by
  `backbone-existence-crt` once/if it establishes any finite covering set.
- **Lemma 2.3 (Σ-stabilization)** — general finite ascending-chain argument, cheap
  and reusable.
- **Theorem 2.4 (conditional eventual periodicity)** — the main new result: `W`
  finite ⟹ eventual periodicity. This is the cleanest available "if backbone
  finiteness then periodicity" bridge in the whole population and should be
  certified so any future proof of `(†)` (by any approach) immediately yields
  eventual periodicity for free, leaving only the from-`n=1` gap.

All three are stated and proved in full inside the approach file (Part 2, Steps
2.1–2.4) and restated in the "Promotable lemmas" section at the end of the file.
