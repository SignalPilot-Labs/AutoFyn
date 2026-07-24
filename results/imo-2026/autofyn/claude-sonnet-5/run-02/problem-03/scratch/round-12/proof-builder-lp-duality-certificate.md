# Round 12 — lp-duality-certificate build report

## What was done

Per the outline-reviewer's hard redirect, steps 3-4 of the round-12 outline
(a "close every gap with one cut" pigeonhole selection-rule construction)
were **not** built — the outline-reviewer independently confirmed by
exhaustive brute-force this whole move family is insufficient (~60% failure
at n=3, ~99.6% failure at n=4 for the literal reading), so no time was spent
repeating or trying to salvage it.

**Built and certified (steps 1-2 of the outline):**
- **Equal-Pieces Closure** (`lemmas/equal-pieces-closure.md`): for every n,
  the equal-pieces marking is closed by a 2-line construction (0 cuts if m
  even, 1 cut if m odd, both giving Phi=T/2 < a_n*T via
  `pair-cancellation-identity` + the certified `a_n>1/2` fact). This
  resolves, for good, a specific configuration flagged in round 11 as
  independently defeating three unrelated crude mechanisms.
- **Spare-Cut Bisection Corollary** (`lemmas/spare-cut-bisection-corollary.md`):
  whenever the certified Iterated Greedy-Peel Construction finishes with
  spare cut budget and a nonzero leftover, bisecting that leftover gives
  Phi=T/2<a_n*T immediately. General, marking-agnostic.

Both are full, unconditional, non-numeric proofs (verified independently
with exact-Fraction Python checks, not used as proof steps, only as
sanity checks per project rigor rules). Both written up in
`approaches/lp-duality-certificate.md` §R12.1-R12.2 and certified as
standalone lemma files.

**Attempted target (b)** (the outline-reviewer's redirect: evaluate the
Per-Piece Vertex Decomposition Theorem's joint vertex family against
a_n*T for arbitrary markings — R11.5's "single cleanest remaining item"):
made honest, non-closing progress, not a solve:
- §R12.3: quantified how generic the still-open residual (Iterated
  Greedy-Peel uses full budget with zero mid-process ties) actually is —
  a fresh 4000-trial exact-Fraction check found mid-process ties in only
  3/4000 trials for generic rational markings, i.e. the residual is
  essentially the WHOLE generic marking space, not a small sliver. This is
  an important honest calibration downward from the outline's own ~66%
  figure (which apparently reflected smaller-denominator sampling).
- §R12.4: tested a second natural non-tie-based greedy candidate,
  "bisect the current largest fragment n times," and refuted it by an
  exact witness: n=2, marking (177, 6/5, 62/123), gives Phi=65561/492
  ≈133.3 vs target a_2*T=439612/4305≈102.1 — fails by a large margin, and
  fails on 2330/3000 random trials generically. Diagnosed as the
  mirror-image failure mode to greedy-peel's own residual (leaves a
  still-dominant fragment unpaired instead of degrading it too slowly).
- §R12.5: honest diagnosis that the core R11.5 obstruction (no
  tail-structure-agnostic replacement for the ladder-specific Ratio-2
  Spacing Lemma / Last-Element Bound) is not resolved — two more concrete
  attempts this round each only closed a narrow sub-case or failed
  generically, sharpening rather than closing the gap.

## Status: partial (unchanged from round 11 in overall closure, but two
new certified general lemmas added, and target (b) has a sharper,
honestly-quantified diagnosis).

## Files touched
- `results/imo-2026-03/approaches/lp-duality-certificate.md` (updated:
  new Round-12 entry in Approaches tried, Current-best update note, new
  §Round 12 build section with R12.1-R12.5, two new entries in the
  in-file Promotable lemmas list).
- `results/imo-2026-03/lemmas/equal-pieces-closure.md` (new, certified).
- `results/imo-2026-03/lemmas/spare-cut-bisection-corollary.md` (new,
  certified).

## Recommendation for next round
Target (b) (joint-vertex evaluation, or an equivalent single sufficient
strategy family for arbitrary markings) remains the single cleanest open
item on the upper-bound front. Two more concrete constructions are now
ruled out (greedy-peel's "match top two", bisect-largest-cascade); Theorem
C's exact recursive value remains the strongest single mechanism on file
but is not yet proved sufficient in general (needs the full both-regime
induction one level down, per round 9's diagnosis). A genuinely new idea
is needed for the "generic, no built-in symmetry, no dominant piece"
regime — possibly attacking the R11.4 joint vertex family's evaluation
directly via a two-piece-at-a-time reduction (bound the contribution of
the two largest pieces' own vertex jointly, recursing on the rest) rather
than a single greedy pass over the whole marking.
