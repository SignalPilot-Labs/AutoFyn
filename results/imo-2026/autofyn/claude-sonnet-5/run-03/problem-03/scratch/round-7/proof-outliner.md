# proof-outliner report — imo-2026-03, round 7

Field this round: **4 approaches** (`layer-cake-parity-reframing` retired,
see §5). All four are revisions of live approaches; no new slug opened —
per the fresh-framing explorer, the crux corpus offers no untried top-level
mechanism, and the diagnosed shared wall ("no additive per-cut/per-piece
budget survives") is best attacked by pushing weight onto the one approach
already structurally outside that pattern (`lp-duality-split-polytope`),
not by adding a fifth slug.

---

## 1. `self-similar-induction-on-n` — fix the bug, then split into two targets

**Step 0 (mandatory, do first): fix the `L0(ℓ,ε)` piece-count bug.**
The lower-bound explorer found an exact rational counterexample
(`ℓ=2, ε=1/10, C={2, 5649/10000, 1407/2500, 9723/10000}`, 4 parts,
`OddSum(C∪Γ_1)=35649/10000<4`) showing the boxed statement of `L0(ℓ,ε)` —
in both `approaches/self-similar-induction-on-n.md`'s round-6 section and
the certified `lemmas/theorem2gen-bounds-and-l0-reduction.md` — is **false
as literally written**, because it omits the inherited cut-budget
constraint. The correct statement must read:

> **`L0(ℓ,ε)`:** for every finite multiset `C` with **at most `ℓ+1`
> parts**, `sum(C)=2^ℓ+ε`, and `max(C)≤2^ℓ-ε`, `OddSum(C∪Γ_{ℓ-1})≥2^ℓ`.

Amend the boxed statement in *both* files (approach file and lemma file)
before doing anything else this round. With this constraint restored, the
explorer's own stress test (thousands of exact-rational trials, `ℓ=2,3,4`)
found zero violations — the corrected statement is well-supported, just
needs the fix recorded before further building on it.

**Step 1 (primary target, high confidence): Branch I.B.**
`C` has a second element `c1'≥2^{ℓ-1}` alongside `c1`. The explorer found
comfortable, *growing-with-`ℓ`* margins here (≈1.03 at `ℓ=3`, ≈5.0–5.25 at
`ℓ=5`) — a much larger cushion than the residual window's ≈0.05–0.1, and
structurally explained: `sum(C)≥2·2^{ℓ-1}=2^ℓ` forces `c1+c1'≥2^ℓ`, so
`sum(C)-c1-c1'<1`, leaving very little mass for the rest of `C`. Attempt a
**direct two-peel argument**: peel `c1`, then peel `c1'` against the
now-explicit small residual, in the same style as the file's own
Two-Level Half-Bound Lemma but applied to `C`'s own top two elements
rather than the merged multiset. This should close Branch I.B outright and
is the cheaper of the two remaining pieces.

**Step 2 (harder, attempt only if time remains after Step 1): the residual
window `c1∈(2^{ℓ-1}-1+ε, 2^{ℓ-1}+1-ε)`.** The explorer's numeric search
shows the tightest instances sit right at `c1≈2^{ℓ-1}` — the exact
Branch-I/II split point — with small but genuinely nonzero margin (not
another exact boundary). **Do not** attempt a third level of the same
peel-then-Lemma-B dichotomy; it is very likely to reproduce the identical
boundary problem one level down (an infinite regress the file itself
already flags as a risk). Instead pursue an **order-statistics argument**:
track `C`'s second-largest element explicitly (not just `c1=max(C)`), in
the spirit of Theorem 1's `m=2,j=2` hand computation (median of the
residual three elements), which is precisely the mechanism that closed the
analogous base-case boundary. This is a genuinely different tool from the
peel dichotomy, consistent with this round's "prefer global/order-aware
arguments over another additive-budget mechanism" steer.

Builder instruction: do Step 0 and Step 1 first (both look tractable and
comfortably in budget); attempt Step 2 only with remaining time, and if
attempted, must use the order-statistics route, not a third dichotomy
level.

---

## 2. `greedy-reduction-geometric` — stress-test before building

Round 6 reduced the `k≥2` Leftover-Fragment Obstruction to two named
sub-problems: **Insertion-Robustness** (weakly supported — no
counterexample found in either round 6's or this round's tests, but both
test families used are acknowledged as structurally weak: round 6 tested
only the `k'=2, b1=b2=2^{m-1}` zero-slack boundary and this round's
explorer only the `k'=1` case, which has a provably constant, non-tight
margin `EvenSum(T)` by the peel identity and so can never expose a
violation) and **Level-Absorption** (not numerically tested at all yet —
different flavor, the inserted mass must *supply* a deficit rather than
merely not hurt).

**Instruction to this round's builder: before investing proof effort,
numerically stress-test Level-Absorption first** (it is currently
completely unexamined, and its "must supply a deficit" character makes it
the more likely of the two to actually fail), using exact rational
arithmetic across several `m` and shapes of the inserted mass `{μ1}∪R1`.
Only after that stress test either (a) finds a counterexample — in which
case report it and mark Level-Absorption as refuted/needs restatement, a
valuable negative result — or (b) finds no violation, in which case attempt
a proof. In parallel/afterward, if time remains, extend Insertion-
Robustness's test family to genuine `k'≥2` near-equality instances (as
round 6's own preamble began but did not fully explore), since the `k'=1`
family used so far cannot logically produce a counterexample.

Do not just proceed straight to writing a full proof of either
sub-problem without the stress test — both are currently underexamined,
and Level-Absorption in particular has zero numeric evidence either way.

---

## 3. `universal-halving-adversary` — redirect to boundary-layer argument

Round 6 closed 65–96% of the residual via best-of-`{k=1,k=2}`
Anchor-Merge and proved `k=3` is *not* monotonically better (dead end,
already recorded — do not revisit `k≥3` variants). This round's explorer
independently corroborated the `k=3` dead end on a fresh random sample and
found a clean structural fact: the residual failure rate is not spread
uniformly over the balanced region but **rises sharply and monotonically
as `p1→1/2⁻`**, saturating near 100% right at the boundary, while the
adjacent regime `p1≥1/2` is already closed unconditionally by a different
(non-Anchor-Merge) construction in this same file.

**Instruction to this round's builder: attempt a boundary-layer /
continuity argument** connecting the residual `p1<1/2` near-boundary cases
to the already-closed `p1≥1/2` construction — e.g. show the `p1≥1/2`
construction (or a small perturbation of it) still closes the target for
`p1` in a neighborhood just below `1/2`, quantify how wide that
neighborhood must be, and check it covers (or can be combined with
best-of-`{k=1,k=2}` Anchor-Merge to cover) the genuinely residual
instances. **Do not** propose or test any new Anchor-Merge `k` variant —
that mechanism is now well-evidenced as a dead end for closing the
remaining gap.

---

## 4. `lp-duality-split-polytope` — highest priority this round

This is the one approach structurally outside the shared "no additive
per-cut/per-piece bound survives" wall diagnosed by the fresh-framing
explorer (its Single-Piece-Split Vertex Lemma is inherently a global
LP-vertex fact, not a decomposed per-element bound) — weight it
accordingly.

Round 6 proved the exact reduction (`lemmas/target-excess-identity.md`):
closing the general-`n` Multi-Piece Necessity theorem for the triangular
family reduces to proving
$$\mathrm{excess}(n):=\mathrm{floor}(n)-\tfrac12 \;>\; \frac{1}{2(2^{n+1}-1)},$$
an exponentially small threshold. Round 6 found (and correctly rejected) a
false *equality* conjecture `excess(n)=1/((n+1)(n+2))` (exact at `n=3,4,5`,
wrong at `n=6`). This round's explorer found strong numeric evidence
(Nelder–Mead, `n=3..16`, matching all 4 exact certified values exactly)
that the corresponding **inequality**
$$\mathrm{excess}(n)\ \ge\ \frac{1}{(n+1)(n+2)}\qquad(n\ge3)$$
holds throughout — `excess(n)/delta(n)` (`delta(n):=2/((n+1)(n+2))`, the
family's AP step) is a weakly-increasing step function never below `0.5`
across all 14 tested points, not a noisy quantity. This is a one-sided
bound, much weaker than pinning the exact minimizer, so it plausibly
sidesteps the number-theoretic non-smoothness that killed the exact
formula. Combined with the certified identity, proving this inequality
**closes the entire general-`n` upper-bound theorem for the triangular
family outright.**

**Instruction to this round's builder:**
1. First, cheaply extend exact certification from `n≤6` to `n=7,8,9` via
   the certified Single-Piece-Split Vertex Lemma (same exhaustive
   exact-rational method already used for `n=5,6` — this is a sanity gate,
   not new mathematics), confirming `ratio(7)=1.0`, `ratio(8)=1.5` (or
   whatever the exact values are) match the numeric prediction.
2. Then attempt to prove `excess(n)≥1/((n+1)(n+2))` for all `n≥3`. Two
   candidate routes, both worth trying:
   - A direct AltSum/pigeonhole "half-credit" argument (style of the
     project's certified dominant-chain/doubling-lemma arguments): show
     any single-piece split of the AP family leaves at least half an AP
     step (`delta(n)/2`) of unavoidable alternating-sum imbalance.
   - The observed parity pattern (numeric search always selects an
     odd-indexed piece `idx∈{1,3,5,...}`, 1-indexed, never even) — if this
     selection pattern itself is provable, it roughly halves the case
     analysis needed for route (a).
   This is the single highest-value target this round: if it lands, it
   closes a whole open theorem, not just narrows a gap further.

---

## 5. Retire `layer-cake-parity-reframing`

Per the fresh-framing explorer: idle two rounds (5, 6), its unique
deliverable (the Coupling Obstruction) is a **completed, proved negative
result** with no half-finished thread, nothing else in the field depends
on it, and its own file gives no lead on either of the two ways forward it
names. Retiring costs nothing structurally.

**Action:** not included in the build set this round. Its three lemmas
(Layer-cake identity, Per-piece additivity of the threshold count,
Single-cut marginal-effect formula) are generic and reusable —
**promotable to `knowledge_base.md`** as a general threshold-count/parity
technique entry, independent of this problem. (Promotion itself is not
done by the outliner; flagging for the reviewer/orchestrator to action.)
`current.md`'s dead-end list should be updated to include this approach's
retirement alongside its already-recorded proved negative result.

---

## Summary of the field (4 approaches, all in build set)

| slug | this round's target | priority |
|---|---|---|
| `lp-duality-split-polytope` | fix `n=7,8,9` exactly, then prove `excess(n)≥1/((n+1)(n+2))` | **highest** — closes a whole theorem if it lands |
| `self-similar-induction-on-n` | fix `L0(ℓ,ε)` piece-count bug; close Branch I.B (two-peel); residual window only with remaining time, via order-statistics not another dichotomy level | high — Branch I.B looks cheap and tractable |
| `universal-halving-adversary` | boundary-layer/continuity argument for `p1→1/2⁻`, connecting to the closed `p1≥1/2` regime; no more Anchor-Merge `k` variants | medium |
| `greedy-reduction-geometric` | stress-test Level-Absorption numerically first (currently untested); extend Insertion-Robustness tests to real `k'≥2` instances | medium |

`layer-cake-parity-reframing` retired from the build rotation this round
(dead-end-adjacent, complete, nothing to build on); its lemmas flagged
promotable to `knowledge_base.md`.

build set: self-similar-induction-on-n, greedy-reduction-geometric, universal-halving-adversary, lp-duality-split-polytope
