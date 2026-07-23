# Proof review — round 15 — imo-2026-03

Reviewed: `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` new §24 (this round's
build), against the round-15 dispatch (outline-reviewer's 4 action items, `/tmp/round-15/outline-
reviewer.md`), the 3 round-15 explorer reports, `results/imo-2026-03/current.md`, and
`results/imo-2026-03/lemmas/`. All claims re-derived and re-tested from scratch with fresh,
independently written code (`/tmp/round-15/verify_reviewer/`), not reusing the builder's, outliner's,
or outline-reviewer's harnesses. Harness validated first against all four of the file's own worked
examples (`OPT_{+1}([5,8],(10,8,7,2))=0`, `OPT_{-1}(\cdot)=10`, `OPT_{+1}([1],(10,8,7))=0`,
`OPT_{-1}([2,4],(5,3))=4`) — all reproduced exactly before trusting the harness for anything new.

## Verdict: potential-weighting-upper-bound — CHANGES REQUESTED

Status stays `partial` (matches the file's own self-report — no overclaim found). Real, honestly
scoped, non-trivial progress on all 4 dispatched items; the central open mechanism (half-step lemma,
Gap 1b's base case, the generalized `A_1`-bound family) remains unproved.

## Independent re-verification of the 4 claims

### Claim 1 (highest priority) — the contested `~15%` half-step claim: RESOLVED in the builder's
favor, confirmed by a third independent codebase

Built my own genuine `\mathcal F` base generators (real trigger `M<A_1`, real global argmin `k^*`,
`B_1=\{b_0,d_{k^*}\}`, `Res=Z_0\setminus\{z_1,z_{k^*}\}`) and tested the half-step
`OPT_{+1}(B_1\cup\{d\},X)\ge OPT_{+1}(B_1,X)` against **every** possible second-level match partner
`u_j\in\mathrm{Res}\setminus\{u_1\}`, not just the argmin, exactly as the dispatch specified:

- `q=5`: `0/906` violations (453 triggered instances). `q=6`: `0/441` (147 instances). `q=7`:
  `0/252` (63 instances). Minimum margin found = exactly `0`, never negative, across all sizes.

This is a **third, independently-coded confirmation** (after the outline-reviewer's and the
builder's own) that the half-step holds against every second-level partner given a genuine
top-level `\mathcal F`-provenance root — directly contradicting §23.1's originally-reported
`1067/7216` (`~15%`) figure and confirming both the outline-reviewer's finding and this round's
builder re-verification are correct.

I also independently reproduced **both** of the builder's diagnostic negative controls, from my own
fresh code:
- **Wrong root** (comparing against `B_0=\{b_0\}` instead of the correct `B_1`): `q=5`: `101/262`
  (`38.5%`); `q=6`: `46/138` (`33%`); `q=7`: `8/72` (`11%`).
- **Dropped top-level trigger** (accepting `M\ge A_1`): `q=5`: `208/1200` (`17%`); `q=6`:
  `146/720` (`20%`); `q=7`: `65/480` (`14%`).

Both independently land in the same order-of-magnitude neighborhood (`11%`–`38%`) as the file's
originally-reported `~15%` figure, strongly corroborating (from a third codebase) the builder's
diagnosis that the round-14/§23.1 figure was a scoping/provenance artifact, not a real fact about
second-level partner choice. **This genuinely settles the contested claim** — the simplification of
the half-step's hypothesis (drop the recursive second-level-argmin requirement, keep only genuine
top-level `\mathcal F`-provenance) is justified. I grepped the rest of the file (`true-argmin-
descended` occurs only within §23/§24) and confirmed no other proof step elsewhere in the file
silently relies on the now-dropped recursive-argmin requirement, so the simplification introduces
no inconsistency. **Honest scope confirmed:** the half-step itself remains an open, unproved
conjecture — the file does not overclaim otherwise anywhere I could find (checked the Status
section, §24.1's own "Honest scope note", and §24.5's summary — all consistent).

### Claim 2 — `q=4`'s DELETE/KEEP free, MATCH needs the generalized `A_1`-bound family: CONFIRMED
exactly, including the root-cause diagnosis

Wrote an independent, differently-structured `q=4` brute-force sweep (direct `OPT_sigma` calls for
DEL/KEEP/MATCH rather than the builder's closed-form Peeling-Lemma derivation): `10,500` genuine
`(b_0,Z_0,l)` checks. Result: `0/10,500` DEL-family-certification failures, `0/10,500`
KEEP-family-certification failures, `72/10,500` (`\approx0.69\%`) MATCH-family-certification
failures — matches the builder's own `439/62,580` (`\approx0.70\%`) rate almost exactly, at a
different sample size, from independent code. Confirmed **every one** of the `72` failures occurs
precisely when `A_1<\min(\text{simple bound family})` (`72/72`), independently reproducing the
builder's exact root-cause diagnosis (internal cancellation inside `A_1`'s own search space).
Confirmed the true target `A_{3,l}\ge\min(A_1,D_l)` (using the real `A_1`) holds in **all**
`10,500` checks — this is a proof-technique gap, not a counterexample to the underlying Per-Partner
Domination Lemma, exactly as claimed.

**Three-Bound Domination Lemma** — independently re-derived the elementary 3-case symbolic proof
(case-split on the rank of `x` among `\{x,y,z\}`) from scratch, before reading the builder's
version — matches exactly, no gap. `200,000/200,000` fresh random trials (arbitrary `x,y,z`), `0`
violations. **CERTIFIED**, together with the Keep-Top Bound (see below), in
`lemmas/three-bound-domination-and-keep-top-bound.md`.

The outline-reviewer's own flag (item 3: "`q=4` closes directly / mechanically" was an overstatement
— only the MATCH sub-case is trivial, DELETE/KEEP were unchecked) is now correctly and fully
resolved by this round's build: DEL/KEEP genuinely are free (my own independent check confirms `0`
failures for both), but MATCH is not — so the recommended build order correctly moved this piece of
work one case earlier (`q=4`, not `q\ge5`). No overclaim found in §24.2's own careful wording.

### Claim 3 — Gap 1b's base case: genuinely reduced, correctly reported as NOT closed

Independently re-derived both new elementary facts from scratch:
- **Keep-Top Bound** (`OPT_{+1}(C,W)\le w_1-|c_1-c_2|` at `h=0`) — one-line "keep `w_1`, delete the
  rest" candidate-selection argument, re-checked, correct.
- **Exact `q=3` dichotomy** (`M=\min(D_{k^*},w_1-D_{k^*})` exactly, since a singleton residual list
  has only two candidate selections) — re-derived, correct.

Built my own genuine `q=3`, `h=0`-triggered base generators: `308` such instances (out of `1,728`
triggered, `v_{\max}\in\{1,\dots,50\}`). Result: `0/308` Keep-Top-Bound violations, `0/308`
dichotomy-formula mismatches, and `M=D_{k^*}` (DELETE beats KEEP, i.e. the base case target holds)
in **`308/308`** instances — corroborates, but (as the file itself is careful to state) does not
prove, the still-open base case.

Independently re-derived the file's one forced-consequence lead symbolically: assuming the negation
`w_1<2D_{k^*}` (KEEP wins), combined with the free bound `A_1\le|b_0-w_1|` (delete `z_{k^*}`, keep
`w_1`) and `w_1>b_0` (from `h=0`), plus the trigger `M<A_1`: `w_1-D_{k^*}<w_1-b_0`, giving
`D_{k^*}>b_0` strictly. This algebra is correct and the derivation is sound — but, exactly as the
file states, it is not reconciled into a full contradiction; the base case remains genuinely open,
not silently assumed anywhere else in the file (checked). No overclaim.

### Claim 4 — Background-Release Domination Lemma, strengthened (uncapped) form: CONFIRMED correct,
ready to certify

Independently re-derived the one-line search-space-inclusion proof from scratch: the map
`(K,D,M)\mapsto(K\cup\{y\},D,M)` bijects `W`'s full selection space (background `C` fixed) onto the
"`y` forced kept" sub-space of `W\cup\{y\}`'s selection space (background `C'=C\setminus\{y\}`),
value-preserving; minimizing over a superset is `\le` minimizing over any particular subset — no
gap, no hidden case. `0/3,000` (`|C|\le4,|W|\le4`) violations, both signs; widened to `0/1,500`
(`|C|\le5,|W|\le5`) — no violation at any scale tested, independently reproducing the builder's own
`0/18,000`+`0/18,000` figures in substance. **CERTIFIED** in
`lemmas/background-release-domination.md`. Grepped the file for "Background-Release" — confirmed
both refuted chaining routes (full telescoping; single-release direct chain to `A_1`) remain
correctly unresurrected and are not silently reused anywhere else, consistent with §23.2/§24.4's own
scoping.

## No overclaim found

Checked the top-of-file Status, the round-15 build's own summary paragraph, and §24.5's "Summary"
against every independently-verified finding above — all consistent, nothing oversold. The file
consistently and correctly distinguishes "corroborated/reduced" from "proved" throughout §24. The
Status correctly stays `partial`.

## Lemma certification

Three new lemmas certified this round, written to `results/imo-2026-03/lemmas/`:
- `background-release-domination.md` (strengthened, unconditional form; superseding the weaker
  capped form the round-15 outliner originally proposed in §23.2).
- `three-bound-domination-and-keep-top-bound.md` (both new elementary lemmas from §24.2/§24.3).

The "exact `q=3` dichotomy" identity was **declined for standalone certification** (same reasoning
the round-13 reviewer applied to the Coincidence Identity: narrow scope, single still-incomplete
use, trivial one-line consequence of "a singleton list has exactly two candidate selections") —
recorded instead as a Remark inside the Keep-Top Bound lemma file.

## current.md updated

Added a new round-15 entry at the top of `## Approaches tried` in `results/imo-2026-03/current.md`
documenting all 4 independently-verified findings above. `## Status` remains `partial` (no change
needed — already accurate). No changes made to the historical entries below it.

## Outcome recorded

`mcp__approach-ranker__record_outcome` called for `potential-weighting-upper-bound`, round 15,
outcome `partial`, noting all 4 items addressed, the resolved cross-round discrepancy, the corrected
build order, and that the central mechanism remains unproved.

## Summary for the run

Round 15 delivered genuine forward motion without a closure: (a) a previously-contested
cross-round numerical discrepancy is now resolved (independently, by a third codebase) in the
simplifying direction — a real reduction in the half-step's proof burden, not merely a wash; (b) a
build-order assumption (`q=4` "free") is corrected before any future builder could waste effort
assuming it; (c) a previously completely unattempted lemma (Gap 1b's base case) now has real partial
structure and a concrete forced-consequence lead; (d) one more general-purpose lemma is certified.
The theorem is not solved; `dyadic-cascade-induction` (lower bound, milestone, benched) and
`concavity-minimax-duality` (benched, no leverage) are unaffected. No RETHINK triggers found — the
approach's central mechanism (Claim A / Sharp Argmin Recovery via the half-step + generalized
`A_1`-bound family + Gap 1b) is not shown dead; it is sharpened and, on the half-step's scoping
question specifically, simplified.
