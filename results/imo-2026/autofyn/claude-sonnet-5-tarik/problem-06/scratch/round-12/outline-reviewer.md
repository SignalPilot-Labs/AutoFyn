# Outline review — imo-2026-06, round 12

Read: `/tmp/round-12/proof-outliner.md`, all 4 revised approach files as
persisted to `results/imo-2026-06/approaches/`, the 3 round-12 explorer
reports, `results/imo-2026-06/current.md`, `lemmas/lemma-UCR-universal-
class-realization.md`, `lemmas/lemma-RD-restricted-domination-and-
magnitude-bound.md`, `lemmas/theorem-SW-stabilization-sufficiency.md`.
Independently re-derived/re-simulated (own Python + sympy, fresh generator,
not any explorer/builder script) every numeric claim checked below.

## Central finding 1 — "Backbone Permanence + Lemma UCR closes (JW) for
Case A" — verified, sound, correctly scoped

Re-ran the exact mechanism from scratch on 3 of the 7 tested pairs, pushed
**past** the explorer's own tested range on two of them:

- `a_1=2747, (S,S')=({41},{67})`: backbone of the `{67}` class
  `B=comp∩=\{2,3,7\}`, exactly realized at `a_3` — confirmed. Cross-checked
  against the *entire* `{41}`-class up to **`N=60000`** (3x past the
  explorer's `N=20000`): **0/57613 misses**. Backbone itself unchanged
  (`{2,3,7}`) across the extended range — no shrinkage observed.
- `a_1=21528751, (S,S')=({103},{197})` (the workspace's hardest instance):
  `{197}`-class backbone `\{2,3,7\}`, exactly realized at `a_{2575}`;
  `\{103\}`-class (2929 members at `N=3000`), **0 misses**. Matches the
  explorer's table exactly (note: I initially mis-parsed the pair as the
  *union* core `\{103,197\}` vs `\{1061\}` — re-ran with the correct
  singleton-core reading and it matches; flagging this only so a future
  reviewer doesn't repeat the same mis-parse).
- Verified Lemma UCR's proof line-by-line independently: it is a direct,
  order-independent 5-line consequence of the already-certified Lemma P′ +
  set manipulation — no circularity, no domination/well-ordering machinery
  smuggled in. Corollary UCR-JW's derivation from it is likewise a clean
  3-line consequence.

**Verdict on this mechanism: genuinely sound, not overclaimed.** The one
open item — Backbone Permanence (does the frozen prefix-intersection stay
fixed over the *whole* infinite class, not just the tested prefix) — is
correctly and honestly labeled as the crux, open, not proved. My extended
run (3x the tested range on `a_1=2747`, zero backbone shrinkage) is
consistent with, not a proof of, permanence.

## Central finding 2 — G_n exact periodicity / bounded-run-length route to
`(PD_{S,S'})` — verified numerically, logical bridge checked and sound,
non-circular as stated

Independently reproduced, with my own generator:
- `a_1=4087`: `G_n` (the `P_1`-imprint sequence) has exact period `T=64`
  from `n=1`, **0 mismatches** over the full generated range (`N=20000`,
  19936 period-shift comparisons). Max run length avoiding core `(67,)`:
  **3**.
- `a_1=247`: exact period `T=1806`, **0 mismatches** (`N=15000`). Max run
  length avoiding core `(13,)`: 3; avoiding `(19,)`: 5.

Both match the explorer's independently-larger-N findings exactly (period
values, zero-mismatch claim) — good cross-validation of two independently
written generators.

**Checked the logical bridge explicitly** (this is the part the dispatch
asked to scrutinize, not just "periodic therefore probably fine"):
Bounded-Run-Length as stated ("no `R+1` *consecutive natural-number
indices* can all avoid core `S'`") is a statement about **every** window
of consecutive integers, not just windows restricted to `I_S`. This
directly gives, for **every** `i` (in particular every `i\in I_S`),
`|I_{S'}\cap[1,i)|\ge\lfloor(i-1)/(R+1)\rfloor`, which is `\ge c\cdot i`
for `c=1/(2(R+1))`, `i` large enough — exactly `(PD_{S,S'})`. This is a
genuine, non-circular pigeonhole (an *inequality* claim), structurally
different from round 4's dead bounded-window Markov *prediction*
mechanism (which needed the window to fully *determine* `G_{n+1}`, forcing
window size = true period). The bridge step (2′→3′) is valid and does not
smuggle in anything already banned.

**Caveat, flagged honestly in the outline itself and confirmed by me**:
the actual *mechanism* for proving Bounded-Run-Length (Step 2′, the crux)
is currently only a one-sentence heuristic ("reusing a `P_1`-prime is
cheaper than an ever-larger companion bundle"), not a real argument —
this is legitimately open, correctly labeled as such, not a hidden gap the
outline is trying to slip past review.

## Central finding 3 — round-11 `Π` counterexample — verified exactly

Re-derived from scratch: `a_1=247`, `a_{51}=1638=2\cdot3^2\cdot7\cdot13`
(`\mathrm{comp}=\{2,3,7\}`), `a_{739}=21375=3^2\cdot5^3\cdot19`
(`\mathrm{comp}=\{3,5\}`), `\gcd(a_{51},a_{739})=9`, joint comp
intersection `=\{3\}`, and `\{3\}\notin\Pi=\{2,5,7\}`. **Exact match** to
the explorer's and outliner's claim. Retiring §8.3's `Π` construction in
`sunflower-bundle-closure` is correct and well-supported; Lemma CB (the
ingredient it was built from) remains valid and is correctly *not*
retracted.

## Central finding 4 — mrs-s-scoped pivot — warranted, correctly used

The `n=10^7` push (froze at `n=101957`, zero further changes to `10^7`,
~100x past freeze) genuinely adds no new leverage beyond the already-
certified No-Shortcut Corollary (`(MRS_S)` for `\{103,197\}` equi-hard to
the abandoned Multi-Companion target). The outliner's pivot of
`forced-primes-well-ordering` away from direct `(MRS_S)` pursuit is
warranted and the distinction it draws — Backbone Permanence (a coarser,
single-class *intersection*-freeze object) is genuinely NOT the same
object as `(MRS_S)` (the full local *minimal-antichain* freeze) and is not
touched by the No-Shortcut Corollary's equi-hardness proof — is correct; I
independently confirmed `𝓥_S^{loc}\supsetneq` backbone in general (the
backbone only needs the *intersection* to stabilize, a much weaker
condition than every locally-minimal element being pinned).

## REAL GAP FOUND — `forced-primes-well-ordering`'s Case B scoping is
partly vacuous (CHANGES REQUESTED, not fatal)

The outline explicitly restates "the identical Backbone Permanence Lemma"
from `sunflower-inadmissibility-toolkit`'s Step 2 and proposes to apply it
(via a new "Backbone-to-Antichain Bridge") to close (JW) for **Case B**
pairs (`247:(13,19)`, `4199:(13,17)`) — but Case B is, *by the jw-rigidity
explorer's own Finding 3*, precisely the set of pairs where **neither
side's backbone is a nonempty, exactly-realized value**. I checked both
instances directly, both sides, from scratch:

- `a_1=247, (S,S')=(\{13\},\{19\})`: backbone of **both** the `\{13\}`-class
  and the `\{19\}`-class is `\varnothing`, and collapses to `\varnothing`
  already at the **2nd realized member of the class** (position 1). Pushed
  to `N=30000` (both classes grown to 16146/10366 members): still exactly
  `\varnothing`, first-collapse position unchanged. **There is no nonempty
  backbone anywhere in this pair, on either side.**
- `a_1=4199, (S,S')=(\{13\},\{17\})`: `\{13\}`-class backbone `=\{2\}`
  (nonempty) but **never exactly realized** (0 exact matches out of 1394
  tested members); `\{17\}`-class backbone `=\varnothing`.

For `247:(13,19)`, the "Backbone Permanence Lemma" the outline proposes to
restate and the "Backbone-to-Antichain Bridge" it proposes to attempt are
**both vacuous by construction**: there is no nonempty stabilization value
to prove permanent, and nothing for the Bridge to connect to a
locally-minimal antichain element. Proving "Backbone Permanence" for this
pair is trivially true (`\varnothing\subseteq` everything) and
contributes **zero** leverage toward closing (JW) via Lemma UCR (which
needs a nonempty, exactly-realized `C`). This is exactly the class of bug
this workspace has hit before (round 1's `Tight(n)` degenerating to a
content-free singleton): a definitional device secretly forced to a
trivial value by data the outline's own citations already contain.

For `4199:(13,17)`, the situation is less bad (there is a nonempty
backbone `\{2\}` on one side) but the outline gives no concrete idea for
how a *never-exactly-realized* backbone can still be leveraged — Step 2 as
written is only a sanity-check comparison of stabilization indices, not a
constructive mechanism.

**This does not sink the approach** (its certified toolkit — Local
No-Resurrection/Interval/Equivalence — remains valid and reusable, and the
whole-problem architecture via Theorem SW is untouched), but the outline
as written risks the builder spending the round trying to "close Case B"
as if both instances were equally in reach, when one (`247:(13,19)`) is
structurally out of reach for this specific mechanism. **CHANGES
REQUESTED**: before attempting Step 2's Bridge, the builder must (a)
explicitly confirm (cheap, already done above) that `247:(13,19)` has no
nonempty backbone on either side and report this as a scope limitation,
not attempt to force it; (b) restrict the live target to `4199:(13,17)`'s
`\{13\}`-side only, and if no constructive bridge idea surfaces there
either, report a clean negative finding (per the outline's own "Watch out
for" instruction) rather than silently stalling; (c) if `247:(13,19)`
needs closing at all this round, that is entirely `sunflower-bundle-
closure`'s job (its NIDF-pigeonhole mechanism does not have this vacuity
problem, since it never requires a nonempty per-class backbone).

## `sunflower-inadmissibility-toolkit` (Case A) — APPROVE

Sound reduction, verified above. Crux (Backbone Permanence) is real, sharp,
open, and — per jw-rigidity's diagnosis — tractable via single-family
tools (Escape-Confinement/Permanent-Inadmissibility/No-Resurrection style
arguments), genuinely different in character from the previously-stuck
`u=w` rigidity question (no cross-family reasoning needed). Scope (Case A
only, 5/7 tested pairs) is honest and correctly cedes Case B to siblings.

## `sunflower-bundle-closure` (Case B, NIDF pigeonhole) — APPROVE

Correctly retires the refuted `Π` (verified above), correctly re-scopes to
Case B, correctly preserves Lemma CB. The new Step 4′ idea (apply the
already-certified, size-agnostic Lemma NIDF injection argument to the
*escape-prime set* rather than a companion-set family) is a genuinely
untried, plausible adaptation — speculative but not vacuous or circular,
and does not depend on any per-class backbone existing (unlike its
sibling's route), so it is not structurally blocked on `247:(13,19)`.

## `intersecting-family-covering-construction` (bounded-run-length /
`(PD_{S,S'})`) — APPROVE

Sound reduction verified above (Finding 2). Correctly distinguishes itself
from the dead bounded-window-Markov mechanism (inequality vs. prediction)
and from the retired Landau–Turán/`(UB_S)` toolkit (bounded alphabet vs.
unbounded companion-prime set — a real, checked distinction, not just
asserted). Correctly retires the round-11 "dyadic hint" as an artifact of
`a_1=4087`'s small period (I confirmed the other periods, `1806`/`64`, are
not powers of 2 or otherwise dyadic-looking, consistent with this
diagnosis).

## `forced-primes-well-ordering` (Case B via Backbone-to-Antichain Bridge)
— CHANGES REQUESTED (see gap above; not RETHINK — certified toolkit and
whole-problem architecture intact, only this round's specific new content
needs the scope fix before the builder invests real effort)

## Diversity check

Three genuinely distinct sub-targets are live this round: (JW)-Case-A
(near-closed pending Backbone Permanence), (JW)-Case-B (two rival
mechanisms, one of which — per the gap above — needs its scope corrected
before it's really independent content), and `(PD_{S,S'})` via bounded-run-
length (a structurally new, alphabet-bounded target, not a re-cut of any
prior density/magnitude wall). This is real bifurcation, not a repeat of
the single-gap plateau flagged in rounds 7–11 — no action needed on
CLAUDE.md's plateau guidance this round.

## Ranking

Ran `update_ranking` comparing the whole field (not just this round's
cohort): `sunflower-inadmissibility-toolkit` and `intersecting-family-
covering-construction` (drawn) rank highest among this round's cohort
(both made concrete, independently-verified progress toward closing a
real sub-target); `sunflower-bundle-closure` next (real but less concrete
progress, crux still fully open); `forced-primes-well-ordering` lowest of
the four (real certified toolkit contributed, but this round's headline
new content has the vacuity gap above), still beating untouched/parked
`persistent-backbone-monovariant`. Anchored `sunflower-bundle-closure`
against dead-end `global-recruiter-finiteness` and `sunflower-
inadmissibility-toolkit` against parked `backbone-existence-crt`, both as
expected wins. No new slugs to register (all 4 are revisions of already-
registered approaches); no branch/copy needed this round.

Updated Elo: `intersecting-family-covering-construction` 1751.0 (top),
`forced-primes-well-ordering` 1596.2, `sunflower-inadmissibility-toolkit`
1589.8, `sunflower-bundle-closure` 1554.0, `persistent-backbone-
monovariant` 1548.9 (parked), `global-recruiter-finiteness` 1413.3
(dead-end), `backbone-existence-crt` 1399.0 (parked). (Other parked
slugs — `explicit-window-backbone-construction`, `core-depth-induction`,
`imprint-automaton-periodicity`, `bounded-gap-density-covering` — not
touched this round, ratings unchanged from round 11.)

## Instructions for this round's builders

- `sunflower-inadmissibility-toolkit`: attempt Backbone Permanence directly
  as scoped (Case A, 5/7 pairs); no changes to the outline needed.
- `sunflower-bundle-closure`: attempt the NIDF-pigeonhole-on-escape-primes
  idea for Case B (`247:(13,19)`, `4199:(13,17)`) as scoped; no changes.
- `intersecting-family-covering-construction`: attempt the Bounded-Run-
  Length Lemma as scoped; no changes.
- `forced-primes-well-ordering`: **before** attempting Step 2's Bridge,
  explicitly note in the approach file that `247:(13,19)` has no nonempty
  backbone on either side (verified above, both sides `\varnothing` from
  the 2nd realized member through `N=30000`) and is therefore out of scope
  for this specific mechanism; restrict the live attempt to `4199:(13,17)`'s
  `\{13\}`-side (backbone `\{2\}`, nonempty, not-yet-exactly-realized); if
  no constructive bridge mechanism is found even there, report a clean
  negative finding rather than a stall, and note that `247:(13,19)` remains
  entirely `sunflower-bundle-closure`'s responsibility this round.

build set: sunflower-inadmissibility-toolkit, sunflower-bundle-closure, intersecting-family-covering-construction, forced-primes-well-ordering
