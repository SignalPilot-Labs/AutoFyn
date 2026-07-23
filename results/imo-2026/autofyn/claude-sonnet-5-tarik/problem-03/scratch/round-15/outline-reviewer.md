# Outline review — round 15 — imo-2026-03

Reviewed: `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` new §23 (23.1–23.4),
against `current.md`, `lemmas/`, and the 3 round-15 explorer reports. Independently re-implemented
`OPT_sigma`/`e()` from scratch (own harness, `/tmp/round-15/verify/defs.py`), validated against the
file's own worked example (`C={5,8},W=(10,8,7,2)`: reproduced `OPT_{+1}=0`, `OPT_{-1}=10` exactly)
before trusting it for anything new.

## Verdict: potential-weighting-upper-bound — CHANGES REQUESTED

Real, honestly-scoped progress (a confirmed shared-mechanism link, a new general lemma found and
correctly kept non-load-bearing, a correctly-retargeted Gap 1b base case). But one of this round's
two headline computational claims in §23.1 — the precise "true-argmin-descended" necessity claim and
its reported "~15% failure when the argmin restriction is dropped one level deeper" — does **not**
reproduce under my independent fresh test. This needs re-verification before a builder treats it as
settled; it does not invalidate the mechanism itself (the underlying half-step lemma still looks
true and useful), but the *scoping story* built around it is currently unconfirmed and possibly
wrong. Also one framing overclaim risk (`q=4` "closes directly / mechanically") that conflates a
proven sub-claim with the whole case.

### 1. "True-argmin-descended" scoping (§23.1) — well-defined, not circular, but its central new
computational claim does not reproduce

**Well-definedness/circularity:** the definition (reachable from a genuine base generator via a
chain of DELETE/KEEP steps or MATCH-at-current-list's-true-global-argmin steps) is a legitimate
inductive definition, well-founded because list size strictly decreases at every step (by ≥1 for
DELETE/KEEP, by 2 for MATCH). "The current list's true global argmin partner" is determined by
evaluating `OPT_{+1}` of each candidate resulting sub-instance — this is a fact about the (already
well-defined) game value, not a presupposition of the theorem being proved, so there is no
circularity in the "assumes the conclusion" sense. This part is sound.

**But the claimed sharp transition does not reproduce.** I built an independent generator
(`/tmp/round-15/verify/halfstep_test.py`, `halfstep_final.py`) that: (a) builds a genuine base
generator `(b0,Z0)` with the real trigger `M<A1` and real global argmin `k*` (exactly `\mathcal F`'s
own item 1, §17.2), giving `B_1=\{b0,d_{k*}\}`, `Res=Z_0\setminus\{z_1,z_{k*}\}`; (b) peels `Res`'s
own top element `u1` and matches it against **every** possible partner `u_j\in Res\setminus\{u_1\}`
(not just the argmin), testing the half-step `OPT_{+1}(B_1\cup\{u_1-u_j\}, X)\ge OPT_{+1}(B_1,X)` at
each. Result, exhaustive over partners, `q=5` (`vmax=6,9`, 300+400 genuine-trigger instances) and
`q=6,7` (100–200 instances): **minimum margin across ALL partners = exactly 0, never negative** —
i.e. the half-step held for the true argmin, the worst partner, the second-best partner, and the
"nearest-value" partner alike, with **zero exceptions**, not the ≈15% failure rate §23.1 reports for
"argmin dropped." As a sanity check that my harness *can* find failures, I also tested (c) fully
arbitrary `(C,W)` with no base-generator provenance at all — this fails at a hefty 26–37% rate,
confirming the harness correctly detects real violations when they exist; and (d) a base "generator"
with the trigger explicitly **not** required (`M\ge A_1`, i.e. genuinely not a member of `\mathcal
F`) — this reliably finds violations (e.g. margin `-4` on a concrete instance), confirming the
*top-level trigger* is load-bearing, exactly as round 12/14 already established.

**Conclusion:** my evidence points to the load-bearing condition being "the top-level match is a
genuine triggered global-argmin match" (i.e. plain `\mathcal F`-provenance of `B_1`), **not** an
additional requirement that the *second-level* match partner also be a true argmin — contradicting
§23.1's specific claim that dropping argmin-ness *one level deeper* reproduces round 14's ~15%
failure rate. Two explanations are consistent with what I see: either the explorer's "arbitrary
partner" test was contaminated by the same wrong-root bug they themselves caught and fixed earlier
in the same report (testing `(B_0,Z_0)` instead of `(B_1,Z_1)`), or "partner satisfying only the
local trigger" means something narrower/different from "any partner," which the write-up does not
define precisely enough to be sure. Either way, this is a real precision gap: **before the builder
commits to "never test the half-step outside true-argmin-descended scope" as a hard constraint
(§23.1/§23.4's explicit "Watch out for" item), have them re-run a fresh, from-scratch adversarial
sweep at exactly the level-2-partner-choice question (not the wrong-root question, which is already
correctly resolved) and confirm the ~15% figure, or drop the extra argmin-recursion requirement if
it doesn't hold — this would actually be a simplification of the half-step's hypothesis, not a
setback.** Not fatal to the approach (the half-step still looks true and useful either way, and
"true-argmin-descended" is a subset of what my test also confirms works), so this is CHANGES
REQUESTED precision, not RETHINK.

### 2. Reduction chain "half-step closes Gap 1a's MATCH branch, but not DELETE/KEEP" — complete, no
case silently dropped

Re-read §23.1's "Gives / Does NOT give" bullets against §22.2's own induction sketch. The claim is
honestly and completely scoped: half-step (+Shrink-List) closes only the MATCH sub-case of the
general-`q` Per-Partner Domination induction's peel-`Res`'s-top step; DELETE/KEEP still explicitly
need the separate "generalized `A_1`-bound family" (§22.2's flagged next step (ii)), and this is
stated as a still-open, separate requirement, not glossed over. I checked this is not silently
assumed to be free anywhere else in §23 (grepped for "generalized `A_1`-bound" and "does not give" —
consistent throughout). No case dropped here.

### 3. `q=4` mechanical claim — the MATCH-sub-case argument is correct, but "closes directly,
likely mechanical" overstates what's actually shown

The concrete combinatorial fact — at `q=4`, `|Res|=2`, so matching `Res`'s own top element consumes
both remaining elements, forcing `X=\emptyset` always — is elementary and correct (a pure counting
argument, no computation needed): I confirm `|Res|=q-2`, matching removes 2, leaves `q-4=0` at
`q=4`. This does mean the MATCH sub-case at `q=4` needs no half-step.

**But** this only disposes of the MATCH branch. The DELETE and KEEP branches of the *same* `q=4`
induction still compare `A_{3,l}` against `A_1`, and `A_1`'s own search space at `q=4` has 3
elements (`Res\cup\{z_l\}`, `|Res|=2`), not the 2-element space the certified `q=3` proof's exact two
bounds (`A_1\le b_0`, `A_1\le|b_0-w|`) were built for — a `q=4` closure genuinely has *more*
candidate free bounds available (e.g. a "keep both `Res` elements" bound), and whether the `q=3`
proof's exact two bounds suffice, or whether `q=4` already needs a piece of the "generalized
`A_1`-bound family" that §23.4 explicitly defers to item 4 (labeled `q\ge5` only), has **not been
computationally or algebraically checked by anyone this round** — the shared-mechanism explorer only
verified the MATCH sub-case is trivial, not that DELETE/KEEP close with existing machinery. §23.1's
own language ("closes directly... likely mechanical... no new lemma needed") and §23.4's build-order
framing ("Cheapest available win in the whole population") both go slightly beyond what's actually
established. **Recommend the builder verify this explicitly as the very first step of `q=4`** (cheap
— it's a finite case check) rather than assume it, since if it turns out `q=4` also needs a piece of
the generalized-bound family, the recommended build order's item 4 scoping ("`q\ge5` DELETE/KEEP
branches") would itself need correcting.

### 4. Gap 1b base case (`w_1\ge2|c_1-c_2|`) — confirmed genuinely unproved, zero proof attempts

Grepped the whole file (`2|c_1-c_2|`/`w_1\ge2` occurrences, lines 25, 324-325, 4272-4283, 4451,
4458+, 4990-, 5045, 5084): every occurrence through round 13/14 is phrased as "checked directly",
"finding a margin", "corroborated" — never a derivation from `M<A_1`/`k*`'s global-argmin property.
§23.3's claim that this is "honestly NOT proved anywhere on file" and "the single most under-attacked
should-be-easy item" is accurate, not an overclaim, and the retargeting to prove it *before* the
recursion-depth inductive step (rather than treating it as a free anchor, §21.2's old framing) is the
right correction — a flat/isolated-witness inductive step without a proved base case would be
unsound regardless of how good the inductive machinery is.

### 5. Background-Release Domination Lemma (§23.2) — correctly isolated, not silently repurposed

Grepped every occurrence of "Background-Release" in the file: confined entirely to §23.2 (statement,
its own two refuted chaining routes) plus one line in the round-15 preamble and one in the build
order (item 6, "certify standalone... does not block any of items 1-5"). It is not cited or reused
as a mechanism anywhere in §23.1's half-step reduction or §23.3's Sum Bound retargeting. Correctly
characterized as certifiable-but-not-load-bearing; both its refuted chaining routes (full telescoping
to background-free, single-release direct chain to `A_1`) are clearly marked dead with concrete
counterexamples, consistent with the file's broader "positional not magnitude" pattern documented
across all three gaps this run.

### Diversity / plateau check

Population unchanged in structure: `potential-weighting-upper-bound` is still the sole active build
target (7th consecutive round); `dyadic-cascade-induction` (lower bound fully closed, milestone) and
`concavity-minimax-duality` (no leverage on the actually-open upper-bound gap) remain correctly
benched, reconfirmed again this round with no new leverage surfaced by any of the three explorers.
This is not a fresh plateau-break trigger — real, if partial, forward motion continues (shared
mechanism confirmed, Gap 1b base case correctly re-targeted) even though the central half-step
lemma itself is still unproved and one of this round's own new computational claims about it needs a
redo. No single-gap-trap concern: this is one whole-problem approach with one shared internal target
(Claim A via the Non-Matching-Witness criterion), not multiple approaches sharing a wall.

## Ranking

Registered slugs unchanged (`dyadic-cascade-induction`, `potential-weighting-upper-bound`,
`concavity-minimax-duality` all already registered; no new slug opened this round, no branch/copy
requested). Updated via `update_ranking`:
- `potential-weighting-upper-bound` beats `concavity-minimax-duality` (continued active, real
  progress vs. a benched approach giving no leverage on the open item).
- `dyadic-cascade-induction` beats `potential-weighting-upper-bound` (dyadic-cascade-induction's
  unconditional lower-bound milestone remains the population's most solid, fully-closed result;
  potential-weighting-upper-bound's central gap is still open and this round even needs a precision
  correction on its own new claim).

Resulting Elo (stale cleared on all three): `dyadic-cascade-induction` ≈1697 (top, benched),
`potential-weighting-upper-bound` ≈1549 (live), `concavity-minimax-duality` ≈1313 (benched).

## What to change before/while building

1. Re-verify §23.1's "argmin dropped one level deeper ⇒ ~15% failure" claim with fresh, from-scratch
   code before relying on the "Watch out for: do NOT test the half-step outside true-argmin-descended
   scope" instruction — my independent test found 0 violations across ALL second-level partners given
   a genuine top-level (triggered, real-`k*`) base generator; if this holds up under a careful redo,
   the half-step's hypothesis can be simplified (drop the recursive-argmin requirement, keep only
   top-level `\mathcal F`-provenance), which is good news, not a setback.
2. Before claiming `q=4` "closes directly / mechanically," have the builder explicitly check whether
   the `q=3` proof's exact two `A_1`-bounds suffice for `q=4`'s DELETE/KEEP branches, or whether a
   piece of the generalized-bound family is already needed there too — don't assume it transfers.
3. Gap 1b's base case must be attempted as its own standalone lemma (using the trigger + `k*`'s
   global-argmin property directly) before any inductive-step work — confirmed correctly zero-proved
   on file, this is real, not already-easy, work.
4. Certify the Background-Release Domination Lemma whenever convenient (cheap, general, unconditional,
   doesn't block anything) — no objection.

build set: potential-weighting-upper-bound
