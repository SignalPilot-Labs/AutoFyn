# Outline review — round 8, imo-2026-03

Scope per dispatch: independently re-verify the three new sections the outliner just added
(dyadic-cascade-induction §5.5, potential-weighting-upper-bound §10, concavity-minimax-duality
§13) via bounded exact computation, not just trust the outliner's prose. All three approaches
are **revisions** of already-registered slugs; no new slug was proposed this round.

---

## 1. `dyadic-cascade-induction` §5.5 — `#X`-parity dichotomy

**Verdict: CHANGES REQUESTED** (real, independently-verified advance; two precise gaps to close
before the odd-`#X≥3` case can even be attempted).

**What I independently checked (sympy, closed-form, not the outliner's own script):** built the
general cyclic linear system for an arbitrary `S`/`X` edge-type pattern of length `L=3,4,5` (all
`2^L` patterns each), solved exactly, and confirmed:
- `#X=0`: closing equation is trivially `0=0` (full transitive equality) — matches "already
  resolved by family (A)."
- `#X` odd: the coefficient of `u_0` in the closing equation is always `±2` (never 0) — a
  **unique** solution for `u_0` exists, confirming the claimed dichotomy shape.
- `#X` even, `#X≥2`: the coefficient of `u_0` is **always exactly 0** — the closing equation
  collapses to a pure identity among the `b_i`'s (independent of `u_0`), and in every one of the
  `2^L-  (L+1)` patterns checked (`L≤5`) this identity is exactly the claimed **alternating
  signed sum of the X-edge-successor pieces** (e.g. `('X','X','S','S')` at `L=4` gives
  `-b_1+b_2=0`; `('X','X','X','X')` at `L=5` gives `-b_0+b_1-b_2+b_3+b_4`... — always distinct
  positions, always alternating sign, matching the outline's description exactly). **This part
  of the mechanism is correct and now independently confirmed, not just plausible.**

**Gap 1 (must be closed explicitly, not asserted):** the `#X≥2` even bucket's key step —
"the `T_i`'s are pairwise disjoint across the different cycle participants, **already a
certified fact**" — cites `lemmas/superincreasing-no-early-zero.md`'s invariant (I1), which is
literally stated only for tokens that are **simultaneously active** in a single D/M trajectory.
But the pieces `b_1,\dots,b_L` in a general tie-dependency cycle are pieces that get cut (hence
consumed) at potentially *different* times in the overall strategy — they need not all be
"currently active" together. The disjointness needed here is really a **laminar-family**
property (any two tokens ever created along one legal D/M sequence either are ancestor/descendant
of one another or have wholly disjoint original-index supports), which is a natural and very
likely true *strengthening* of (I1)'s literal statement, but it is not what is literally
certified. This exact same gap already existed, unflagged, in round 7's honest-gap writeup (it
reused the same disjointness claim to set up the now-abandoned crude dominance bound) — round 8
inherits it silently. **Required fix:** the builder must either (a) prove the laminar-disjointness
strengthening as a short standalone addendum to the certified lemma (should be an easy induction:
`M`-outputs' supports are unions of already-disjoint parents' supports, and nothing ever
re-merges supports across different root branches), or (b) restrict the `#X≥2` argument to
configurations where the participating pieces provably *are* simultaneously active, and show that
covers every case the theorem needs. Flag this to the builder explicitly — it is fixable, likely
in a few lines, but must not be silently assumed.

**Gap 2 (needs a fully spelled-out chain, not a one-sentence jump):** the `#X=1` reduction
("forces every `u_i` to `t`, plus `2t=b_j` — a self-bisection, exactly the Vertex Lemma's other
breakpoint type, out-degree 0, immediately peelable") is correct in its algebra (I verified the
specific closing equation `2u_0=b_0` for pattern `('S','S','S','X')` at `L=4` via the same sympy
check) but the *logical* chain from "this forces node `j` to be a literal self-bisection" to "this
cycle therefore does not need separate treatment" has an implicit step: it requires arguing that
once the closing equation forces this specific numeric identity, the assumed cyclic dependency
edge through node `j` is *vacuous* (node `j`'s value is pinned by its own self-bisection,
independent of the rest of the cycle), so the "cycle" degenerates into an acyclic
peel-from-`j`-outward chain rather than a genuine unresolved cycle. This is plausible and I
believe it is correct (self-bisection nodes have out-degree 0 by the file's own Step-0 setup,
which structurally cannot be mid-cycle), but the current text compresses this into "which is
exactly... immediately peelable" without stating why a forced self-bisection breaks the cycle
rather than just being one (numerically pinned) edge of it. **Required fix:** the builder must
write this out as an explicit 2-3 line argument, not a cross-reference.

Neither gap is fatal — both are of the "make the mechanism fully explicit" kind CLAUDE.md asks
for, not a wrong technique. This is genuine forward progress: 3 of the 4 parity buckets are now
correctly, verifiably closed (up from "all-cycles caveat, wide open" at the start of the round),
and the remaining odd-`#X≥3` bucket is precisely isolated with a concrete crux pointer.

---

## 2. `potential-weighting-upper-bound` §10 — MAX-companion mutual induction

**Verdict: CHANGES REQUESTED** (the reduction is correct once done properly; the outline's own
wording is exactly imprecise enough to walk a builder into the trap its own "Watch out for" note
warns against).

**What I independently checked:** implemented `OPT(Y,b)`/`MAXOPT(Y,b)` exactly per §9.2's literal
definition (a **flat, one-round** selection over indices of `Y` — matched pairs are pairs of
*original* indices, not recursively re-matchable derived differences), then tested the claimed
3-branch decomposition `OPT(Y,p-1) = min(DELETE, MATCH, KEEP)` on 80 random instances (`p=3..6`).

- **First attempt (following the outline's literal phrasing "new list `Y''`... reduces to a
  same-gap `(p-1)`-instance"):** modeled the MATCH branch as `OPT(Y'', b-1)` where `Y''` includes
  the produced difference as an ordinary, further-matchable element. **This is WRONG** — it gave
  3 mismatches against the true flat `OPT(Y,p-1)` in 60 trials (e.g. `Y=[38,21,15,7,2],b=4`: true
  `OPT=1`, but the naive branch-min gives `0`, because letting the produced difference be
  *further* matched or deleted is strictly more permissive than what a genuine one-shot selection
  allows, silently smuggling in an extra cascading operation that isn't part of the flat
  definition).
- **Corrected version (fixing the produced difference as a non-recursable block-extraction
  element, and only sub-selecting over the remaining `p-2` *original* elements):** reproduces the
  true `OPT(Y,p-1)` **exactly, 0 mismatches in 80 fresh trials** (`p=3..6`).

So the underlying mathematics (the 3-way branch decomposition, and hence the reduction of the
whole induction to the two MATCH branches sharing one lemma) **is sound** — but the file's own
phrasing of §10(b) ("new list `Y''=(Y\{y_1,y_j})\cup\{y_1-y_j\}`... reduces to a same-gap
`(p-1)`-instance") is precisely the loose description that, read literally, produces the wrong
(over-permissive) reduction I just demonstrated fails — i.e. the section's own prose risks
committing exactly the error its "Watch out for" paragraph explicitly warns against ("do not
silently re-treat the reduced list as just another same-gap instance, apply the IH directly").
**Required fix:** rewrite §10(b)'s reduction using explicit block-extraction language (the
produced difference `y_1-y_j` is a *fixed* value contributing to `e` via Fact 3, not a fresh
selectable list element), so a builder cannot mistake the intended structure for a literal
recursive `OPT` call on `Y''`.

The claim that the **Small-Gap Crossing-Domination Lemma is the single shared gap** for both the
MIN-side (gap 1) and MAX-side (gap 0) MATCH branches checks out structurally: both branches, once
correctly stated via block extraction, hit the identical inside/outside-crossing obstruction one
gap level apart, and DELETE/KEEP on both sides are genuinely trivial/self-similar as claimed — I
found no flaw in this part of the unification.

---

## 3. `concavity-minimax-duality` §13 — pairing/telescoping for `g^*`'s minimum

**Verdict: CHANGES REQUESTED** (the headline numeric claim independently corroborates; the
section's own **motivating illustrative example is mathematically impossible**, which undercuts
confidence in the "structural lead" that technique 1 is built on).

**What I independently checked:** re-implemented `g^*` from its closed-form definition (§12.6)
and an independent D/M-reachability BFS from scratch (not reusing the outliner's/builder's code),
and confirmed `e_{g^*}(M)\ge1` with **zero violations** over all reachable states from `D_m`,
`m=1,\dots,6` (fresh corroboration, matching the file's "0 violations" claim in spirit — though my
raw state *counts* differ substantially from the file's reported figures, e.g. my `m=6` gives 3117
distinct value-multisets vs. the file's reported 304190; this discrepancy in exploration
methodology is unresolved and should be reconciled by a future builder, but it does not affect the
zero-violations conclusion, which both searches agree on).

**Decisive, concrete problem found:** the section's own illustrative example for the "cancelling
pairs plus residual" structural lead —
"at `m=6`, the minimizer `(32,26,13,13,8,6,1)`" — **is not a valid reachable state from `D_6` at
all.** `D_6=(64,32,16,8,4,2,1)` has 7 elements; since every legal `D`/`M` operation strictly
decreases the active count by exactly 1 (certified, `lemmas/dm-operation-reformulation.md`), *any*
reachable state with 7 elements must be reached using **zero** operations, i.e. must equal `D_6`
exactly. The cited example has 7 elements but sums to `99`, not `D_6`'s sum of `127`, and its
individual values (`26,13,6`) are not powers of 2 — it is simply not reachable, under any number
of operations, let alone zero. This is a clean, checkable arithmetic error (mismatched element
count forces the only possible interpretation, and that interpretation is contradicted by the sum),
not a subtle judgment call.

**Consequence:** my own fresh BFS (`m=1..6`) never turned up a minimizer with more than 2
elements — every exact minimizer I found is a simple 2-element pair (adjacent `g^*`-bracket gap of
exactly 1), not the richer "several cancelling pairs plus one residual" pattern the section
motivates technique 1 with. This doesn't refute the headline claim (`\min e_{g^*}=1` still holds
in every case I checked), but it means the *specific structural motivation* offered for technique
1 (dyadic-bracket coarsening producing multi-pair cancellation, generalizing Lemma P) has **not
actually been demonstrated on genuine data** — the one example meant to illustrate it is
fabricated/miscalculated, and my independent search didn't find a real substitute. **Required
fix:** before a builder invests in technique 1's induction, they must either locate a genuine
multi-pair-cancellation reachable minimizer (perhaps requiring larger `m`, e.g. `7` or `8`) or
re-derive the motivating pattern from a *correct* worked example — the current motivating evidence
is not solid.

Technique 2 (Kraft-budget reformulation) is honestly flagged as wholly untranslated/speculative
(no claims made yet) — no issue found there; it remains an untried fallback, correctly not
overclaimed.

---

## 4. Dispatch item 4 — probabilistic/averaging idea folded into `potential-weighting-upper-bound`

**Endorsed.** The outliner's reasoning is sound: the randomized existence argument targets the
exact same open sub-lemma (the MATCH-branch crossing obstruction) within the same D/M
one-shot-allocation framing, not a different top-level route to the theorem — per CLAUDE.md's
single-gap-trap rule and the standing memory rule distinguishing "same gap, different technique"
from "genuinely different whole-problem route," this correctly does not warrant a new Elo-bearing
slug. The other three "new framing" candidates (generating-function, entropy, outer-recursion)
were also correctly declined as isomorphic to existing/dead machinery — no action needed.

---

## Field diversity check

All three approaches remain genuinely different routes to the theorem (physical-cut/cycle
casework for the lower bound; one-shot-allocation DP for the upper bound; closed-form Lipschitz
certificate as an independent alternative lower-bound route) — no shared-gap collapse this round.
Each hit its *own* distinct obstruction (odd-`\#X` domain violation; small-gap crossing
domination; `g^*`'s general-`m` induction) — the field is not stalled on one shared wall.

## Ranking

Comparisons submitted this round (`update_ranking`):
- `dyadic-cascade-induction` beat `potential-weighting-upper-bound` — closed 3 of 4 parity
  buckets with independently-verified algebra this round (only two precise, fixable gaps
  remain), vs. a real but narrower advance with one wording-precision risk.
- `dyadic-cascade-induction` beat `concavity-minimax-duality` — same reasoning, and
  `concavity-minimax-duality`'s round included a decisively-wrong illustrative example
  undermining its motivating evidence.
- `potential-weighting-upper-bound` beat `concavity-minimax-duality` — its unification claim
  (single shared lemma for MIN/MAX) held up under independent check; `concavity-minimax-duality`'s
  did not (fabricated example, motivating pattern not yet demonstrated on real data).

Resulting Elo (post-update): `dyadic-cascade-induction` 1684 (top), `potential-weighting-upper-bound`
1473, `concavity-minimax-duality` 1356. No new slug registered (none proposed this round); no
approach copied.

## Build set for this round

All three approaches made genuine, independently-corroborated progress with real but fixable
gaps (no RETHINK) — route per CLAUDE.md's per-approach verdict: CHANGES REQUESTED for all three,
re-dispatch each builder with the specific fixes above (dyadic-cascade-induction: prove/patch the
laminar-disjointness extension and spell out the `#X=1` cycle-breaking chain, then attempt
odd-`#X≥3`; potential-weighting-upper-bound: restate §10(b)'s MATCH branch via explicit block
extraction before attempting the Small-Gap Crossing-Domination Lemma; concavity-minimax-duality:
replace/repair the illustrative example and locate a genuine multi-pair-cancellation minimizer
before committing to technique 1's induction, or pivot to technique 2).

build set: dyadic-cascade-induction, potential-weighting-upper-bound, concavity-minimax-duality
