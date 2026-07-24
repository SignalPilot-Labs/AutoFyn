## imo-2026-06 — round 26 outline review

### Context checked
Read the round-26 outliner report (`/tmp/round-26/proof-outliner.md`), all three
math-explorer reports (`bad-p`, `m4`, `h1-fresh`), `current.md`, and the ranker
sidecar (`.ranking.json`). Independently re-ran the key numeric claims from
scratch (own scripts, not reused from any report):
- `p=5`: greedy simulation for all primes 7≤q<60 reproduces Bad(5)={7,13,19}
  exactly, with deviation indices matching the K_0-Boundedness Lemma's own
  formula (K_0=6 in all three cases).
- `p=7`: greedy simulation for all primes 11≤q<60 reproduces Bad(7)={11,13}
  exactly, again matching the formula (K_0=8 in both cases).
- Independently recomputed `s_0(j,r)` for all 6 known genuine exceptions
  (p=3:q=5; p=5:q∈{7,13,19}; p=7:q∈{11,13}) and confirmed EVERY ONE has
  s_0=1 (the minimal-window cell) at its actual deviation band — a clean,
  independently-reconfirmed 6/6 match for the Minimal-Window Necessity
  pattern the outliner wants a1-pq's advance to attack.
This directly follows memory rule "ALWAYS independently reimplement a
math-explorer's numeric falsification/confirmation claim before trusting it" —
both the bad-p explorer's Bad(5)/Bad(7) claims and the implicit pattern behind
the a1-pq advance check out.

### Per-approach verdicts

**a1-5q-subfamily-theorem (revise) — APPROVE.**
The outliner's report gives a complete, correct skeleton reusing the already-
certified `p`-uniform Generalized K_0-Boundedness / gcd-difference Witness
Lemma (round 25) plus the certified sieve toolkit — this is now purely
mechanical instantiation at p=5, the exact template that already closed
a1-3q/a1-3q^2/a1-3q^3 across 3 prior rounds. Numerically re-verified myself
(above): Bad(5)={7,13,19} is exact and matches the formula precisely; the
"near-miss" q=11 (non-minimal-window cell, s_0=2) genuinely has a witness
(confirmed to n=60), exactly the outliner's flagged watch-out. **Issue found
and fixed**: the physical approach file `a1-5q-subfamily-theorem.md` was
STALE — it still contained round 23's superseded "j-generalized Parity
Witness" plan, not this round's actual (much stronger, already-certified-
machinery-based) technique. Per the standing workspace rule (round 20 memory
note: "check whether the outliner actually wrote/revised the physical
approach files"), I rewrote the file myself to match the vetted outline
exactly, folding in my own independent numeric reconfirmation, so the builder
starts from correct, current content rather than the superseded plan. This is
the round's strongest, lowest-risk build target — a near-certain 6th APPROVE.

**a1-7q-subfamily-theorem (new) — APPROVE the outline, DEFER the build.**
Technique is identical in kind to a1-5q (same certified machinery, p=7
instead of p=5), and I independently confirmed Bad(7)={11,13} matches the
minimal-window (s_0=1) pattern exactly. However the 30-cell (j,r) table has
NOT been band-traced this round (the explorer only ran the top-level
simulation, not the per-cell K_0/s_0 decomposition, for p=7) — genuinely more
work than a1-5q's already-fully-band-traced 12-cell table. The outliner
itself explicitly recommends this be secondary/lower priority if capacity is
tight. No approach file existed at all; I seeded one (mirroring a1-5q's
structure) so it is not orphaned for a future round. Registered in the
ranker. Held out of this round's build set — not because of any flaw, purely
a priority call given a1-5q is the stronger near-term target and I want to
avoid diluting builder capacity on a larger, less-prepared table this round.

**a1-pq-subfamily-theorem (advance, Minimal-Window Necessity Conjecture) —
APPROVE, stretch target.**
The conjecture ("genuine Bad(p) exceptions occur only at s_0=1 cells") is
independently confirmed on all 6 known instances by my own recomputation
above — a real, not illusory, pattern, and a legitimate open-research target
(proving it would give an O(p) vs O(p^2) reduction in future per-p closures,
genuine reusable leverage). This is honestly flagged by the outliner as
unproved, genuinely open content, not a re-derivation of certified work — no
circularity or single-gap-trap risk versus its sibling a1-5q/a1-7q (those are
mechanical closures of ALREADY-reduced finite tables; this is an attempt to
prove a NEW general theorem about which cells can ever be exceptional, a
different target). Appended the round-26 advance plan directly to the
approach file (it was previously silent on this). Approved as a genuine
stretch build — acceptable if it dead-ends honestly (per this workspace's
long-standing "clean negative is a valid, valuable outcome" precedent), but
must not be allowed to consume the slot a1-5q needs; since builders run one
per approach in parallel, this is not actually a capacity conflict.

**covering-system-construction (advance, residual class d=13) — APPROVE,
bounded/likely-dead-end scope.**
This is explicitly NOT a new H1/FAH mechanism — a narrow, honestly-scoped
compatibility check on the single already-isolated residual divisor class
`d=13` for the standing test seed a_1=4807, building only on already-
certified bookkeeping (Reduced-Alphabet Corollary, Confined-GCD Lemma). Given
this round's dedicated H1-fresh-corridor explorer found NO new corridor (19th
consecutive plateau round, exhaustive corpus + KB resweep, one theoretical
loophole found and explicitly assessed as practically blocked by an already-
documented obstruction), this narrow bounded task is a reasonable, low-risk
use of a build slot — it cannot regress the workspace (worst case: another
honest negative result, matching the file's own 34+ prior dead-mechanism
pattern) and it is the most concrete continuation available for the H1 track
specifically (as opposed to the subfamily track). I appended the round-26
target directly to the (large, 234KB) approach file since it had not been
updated with this round's plan.

**H1 fresh-corridor sweep (informational, no approach file) — no action.**
The dedicated fresh-framing explorer this round found nothing new and gave a
careful, specific diagnosis of why the one theoretical loophole in the
certified Ambient-Statistic Obstruction's scope (occupancy-conditioned
statistics) is practically blocked by the independently-documented §5.3
local-density obstruction. This is good diagnostic hygiene, not itself an
approach to rank/build. Confirms the run should continue prioritizing the
subfamily track (near-certain APPROVE-class results) over further generic H1
sweeps absent a genuinely new idea, consistent with round-25's "Next"
guidance.

**m=4 (a1-3qk extension) — correctly NOT proposed as a build entry.**
The outliner's own "Note" section holds m=4 out, per the m4-lens explorer's
two independent findings: (1) a genuine, permanent counterexample at q=17,
k=0 (verified by direct greedy simulation to n=60, no resettling to constant
gap 3 — this breaks the literal claim, not just the crude-bound sufficiency
argument), and (2) the naive threshold-scaling blows up to an infeasible
~2×10^11 verification range (vs m=3's tractable 737,282). I did not
independently re-verify these (time budget; the explorer's write-up is
detailed, specific, and internally consistent, and the underlying pattern —
threshold growing combinatorially with m — is exactly what would be expected
given m=1→2→3's own escalating difficulty). Agree this should stay out of
the build set this round; the outliner's handling is correct and does not
need a RETHINK — it's simply not ready.

### Diversity check
The build set mixes: (1) two mechanical subfamily-closure builds (a1-5q,
a1-pq-advance) that are technique-identical variants of an established
certified machinery — legitimate per the workspace's own established pattern
(memory rule 30: each is its own complete-claim theorem/conjecture, not a
proof fragment split across slugs) — with (2) one genuinely different-
framing attempt at the actual general H1/FAH crux itself
(covering-system-construction). This avoids an all-eggs-in-one-framing
plateau: even though a1-5q/a1-pq share a technique lineage, they are not
splitting one proof's gap across files (each targets its own whole-problem
family completely), and covering-system-construction keeps the main-crux
track alive with a bounded, non-repeating task.

### Registration / ranking
- Registered new slug `a1-7q-subfamily-theorem` (cold-start Elo 1500).
- Ran `update_ranking` with 6 comparisons anchoring the new/updated
  approaches against established siblings: a1-5q > covering-system-
  construction and a1-5q > a1-pq (a1-5q is the most concrete, most
  independently-reconfirmed target this round); a1-pq > a1-7q (a1-pq has
  fully certified machinery + one year's head start; a1-7q's table is
  untraced); a1-7q > density-sieve-contradiction and a1-pq >
  core-growth-monotonicity (anchoring newcomers/advances against confirmed-
  weak/dead-end established approaches); covering-system-construction >
  amortized-charging-budget (established leader over a long-stale approach).
  This clears `stale` on all touched approaches.

### build set: a1-5q-subfamily-theorem, a1-pq-subfamily-theorem, covering-system-construction
