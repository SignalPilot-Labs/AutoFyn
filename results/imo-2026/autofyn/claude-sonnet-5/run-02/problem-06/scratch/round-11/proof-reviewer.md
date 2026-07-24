# Round 11 proof-reviewer report — IMO-2026-06

## Scope
Independently, adversarially reviewed both round-11 builds:
1. `results/imo-2026-06/approaches/greedy-exchange-cost-potential.md` (ROUND 11 BUILD section)
2. `results/imo-2026-06/approaches/sieve-density-exception-bound.md` (new approach)

Also read `current.md`, all other approach files (for context / no cross-drift),
`lemmas/` (density-argument-vacuity-corollary.md, escape-cost-vacuity.md,
sandwich-genericity-theorem.md, minimality-tautology-lemma.md, confined-gcd-lemma.md),
and `knowledge_base.md` context.

## Verdicts

### greedy-exchange-cost-potential — CHANGES REQUESTED (partial)
Genuinely attempted (not merely restated) a rescue of the round-11-opened Forced-
Escape Blocking Construction (killed pre-build by the outline-reviewer's CRT
Magnitude Obstruction, ≈8 orders of magnitude overshoot). Tried a weaker,
partial-signature-matching variant and proved a two-branch dichotomy (Minimal-
Modulus Generalization): any partial-signature CRT-glue construction either (i)
sacrifices the legality guarantee — a genuinely general, seed-independent
structural fact, correctly re-derived by me from Lemma A's own proof (Free Facts
gives no control over WHICH `Q`-prime a given `a_i` shares with `a_1`, so a
legality guarantee needs divisibility by every prime of `Q`, not a subset) — or
(ii) uses the full-`Q` floor, which itself fails magnitude-wise on the tested
seed.

**Independent numeric verification (from scratch, own script, no shared code):**
wrote my own trial-division greedy-sequence generator and reproduced every
reported number exactly for `a_1=4807`: `Q=P(4807)={11,19,23}`; minimal
single-prime-of-`Q` modulus `11·17=187`; 2499 consecutive gaps up to `N=2500`
with max 38, mean 17.4, min 2; **0/2499 gaps reach modulus 187**; and the three
sampled rogue occurrences at `n=561,1114,2223` have local gaps 15/3/19 with
`a_n` factorizations `{3²,5,17,19}`, `{3,5²,17,19}`, `{3³,5,17,19}` — exact match
to the builder's `A'={3,5,19}`, `q*=17` claim. No discrepancy anywhere.

**Scope check:** the file correctly does NOT claim the magnitude half is a
fully general, seed-independent theorem — it is demonstrated on one seed plus a
general structural half. I agree with the builder's decision not to certify this
as a portable lemma (matches the Lemma F / Lemma I precedent for toolkit-
diagnostic, non-portable negative findings). No overclaim found. No
counterexample to FAH found. This is the workspace's 14th confirmed-dead
mechanism, closing the entire CRT-glue/competitor-construction family.

### sieve-density-exception-bound — RETHINK (unsolved, as scoped)
New approach whose entire round-11 content is a mandatory pre-build screening
(per the outline-reviewer's instruction) that correctly found its own dispatched
mechanism dead before any real construction was attempted — this is a legitimate
"screen before you build" negative result, not a shortfall.

Two independent obstructions, both re-derived from scratch by me:
1. **Density-Argument Vacuity Corollary** (newly certified this round): a
   faithful, non-circular extension of the already-certified Escape-Cost Vacuity
   Theorem (round 10) from pairwise class-blind facts to window/counting
   quantities `C(X)`. I re-derived its "class-blind premises cannot entail a
   class-sensitive conclusion" argument and confirmed it depends only on Free
   Facts (via Confined-GCD) and the definitional shape of `C(X)` — never on FAH
   or any other open hypothesis, so it is not circular. It is a genuine,
   toolkit-independent logical principle (matches the certification bar of its
   parent theorem), correctly certified.
2. **Selection-Rule Class-Blindness** (not separately certified, correctly kept
   in-file as a supporting observation): the sequence's defining recursion
   `a_{n+1} := min{c>a_n : gcd(c,a_i)>1 \ \forall i\le n}` decides legality via a
   Boolean predicate blind to which prime realizes each shared factor — an
   elementary, clearly-correct fact I independently confirmed by inspection of
   the problem's own definition, reinforcing (1) via a wholly different route.

Sub-route (b) (Borel–Cantelli on a posited decay rate) is correctly rejected as
smuggling in the open crux rather than offering a genuine alternative, per
CLAUDE.md's "prove, don't conjecture" rule. The `|D_bad|=0` sanity check and the
density-zero-vs-finite note are both correct and unremarkable.

No counterexample, no proof, no overclaim. This retires an entire technique
family (analytic/sieve-density) in one round.

## current.md updated
- Prepended a round-11 paragraph to `## Status` (before the round-10 paragraph).
- Added both approaches' round-11 entries to `## Approaches tried`.
- Appended a full `## ROUND 11` section (mirroring the round-10 section's
  structure) with the independent-verification detail above, lemma
  certification record, "Next-round guidance," and an explicit **convergence
  vs. exhaustion assessment** (see below).
- Recorded outcomes via `record_outcome`: `greedy-exchange-cost-potential` →
  `partial`; `sieve-density-exception-bound` → `dead-end`.

## Honest assessment: converging or exhausted?
Both builds are legitimate, non-overclaiming negative results — no counterexample
to FAH was found anywhere, and no false rescue was manufactured. In that narrow
sense the round is healthy: CLAUDE.md explicitly treats this as legitimate
`partial`/negative progress, not a failed round.

That said, the bigger picture deserves a direct answer. FAH/Symmetric FAH has now
been the SOLE open crux for six consecutive rounds (6–11), and fourteen
structurally distinct mechanisms — spanning existential/pigeonhole, magnitude/
index-sandwich, definitional/tautological-minimality, CRT-glue-competitor, and
now aggregate density/sieve-counting proof shapes — have all been rigorously
shown incapable of closing it, with zero counterexamples across (cumulatively)
several hundred tested seeds. This is real narrowing in the sense that the SHAPE
of any viable mechanism is now sharply characterized (it must supply index-
specific, `g_n`-referencing, cross-occurrence information — not existential,
magnitude, tautological, CRT-competitor, or window-aggregate-density), which is
useful, non-trivial progress. But it is NOT narrowing toward a proof: no round
since round 6 has gotten closer to actually resolving FAH, only closer to
knowing what does not work. Round 10 already flagged this as a "shared-gap
plateau" per CLAUDE.md's diversification rule; round 11's two builds (a
continuation of a magnitude-construction idea, and a new-but-still-doomed
density idea) did not break that plateau with a genuinely different top-level
framing — they extended the same reduction-chain corridor (Free Facts → Finite
Core → persistent-type reconciliation → FAH) that every live approach shares.

**My recommendation for round 12:** the orchestrator should seriously push for at
least one approach that abandons the shared "disjoint persistent types must share
a core prime, proved via [class-blind/window-aggregate technique]" corridor
entirely — e.g. an index-specific (not window-aggregate) analytic argument, or a
top-level route to periodicity that doesn't pass through persistent-type
reconciliation at all. Given the strength of the negative results (five
technique families now provably excluded, not just untried) and the strong
empirical support for FAH being true, it is plausible the remaining gap needs a
technique genuinely outside this workspace's toolkit so far — round 12 should
weigh this seriously rather than dispatching another straightforward variant
within the same corridor. Full detail and concrete directions are recorded in
`current.md`'s new "## ROUND 11" section and "Next-round guidance (current,
round 11)".
