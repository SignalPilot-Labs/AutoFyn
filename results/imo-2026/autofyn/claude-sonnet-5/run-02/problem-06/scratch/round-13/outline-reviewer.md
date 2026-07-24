## Outline review — round 13 (imo-2026-06)

Field proposed by proof-outliner.md: (1) `central-sets-idempotent-recurrence` (new),
(2) `greedy-exchange-cost-potential` (revise — No-Restart Lemma), (3)
`n1-periodicity-reconciliation` (new, secondary gap, conditional on FAH).

---

### 1. central-sets-idempotent-recurrence — Verdict: **RETHINK**

The outline is honest about the risk that Step 3 only delivers IP-density, not
syndeticity/cofiniteness (matching the explorer's own flag), and it pre-registers a
cheap fail-fast check. I did that check analytically rather than by building, and
found a **more basic problem than the one flagged**, not just the speculative bridge
in Step 4.

The plan (Steps 2–3) is: partition the occurrence-set of a persistent type A' into
finitely many cells by "which divisor class of q wins," then invoke a minimal
idempotent / the Central Sets Theorem to conclude the target cell (`q divides,
A'-type`) is *central*, hence syndetic. But the only fact general Ramsey/idempotent
theory supplies for a finite partition is: **some** cell of the partition lies in a
minimal idempotent (is central) — it does **not** let you steer which cell that is.
Nothing in the outline establishes that the specific target cell (as opposed to
"not A'-type," "A'-type but a different divisor class," etc.) is the central one; nor
does it establish that the target set is even an IP-set (membership in *some*
idempotent, not necessarily minimal) — not every infinite set is. This is exactly the
same "pigeonhole gives you SOME infinite/structured class, never provably the ONE you
picked" wall that Lemma I already diagnosed and that has now killed 15 mechanisms
(most recently round 12's EEA route, independently landing on the identical crux).
Central Sets Theorem/idempotent-ultrafilter language does not escape this — it
restates it in a fancier vocabulary. This is a fatal, not merely gap-y, flaw: the
technique as set up cannot be steered to say anything about the specific
already-known-infinite set the problem needs it to say something about.

(Side check: "central ⟹ syndetic" is indeed a true, standard fact in this theory —
that part of the outline's claimed mechanism is not wrong in isolation. The failure
is one step earlier, in ever getting the *target* cell to be central at all.)

Per CLAUDE.md, this is a wrong-technique RETHINK, not a fixable gap: sending it back
to the outliner would need it to identify a mechanism that forces centrality
specifically onto the target set (e.g. via some structural property of THIS
problem's recursion, not generic finite-partition Ramsey theory) — nothing in the
outline suggests such a mechanism, and none is evident. Do not register; do not
build this round. If revisited, the outliner should either drop Ramsey/idempotent
tools entirely or find a problem-specific reason the target set (not just some cell)
is central/IP before re-proposing.

### 2. greedy-exchange-cost-potential (No-Restart Lemma) — Verdict: **APPROVE**

Narrow, defensive/bookkeeping scope, explicitly not a new FAH attempt (correctly
avoids re-hitting the 15-times-dead wall). I independently verified the concrete
example numerically:
`a_1=15` gives true sequence `15,18,20,24,30,36,40,42,45,48,50,54,...`; restarting
from `a_5=30` under the shorter constraint set `{30}` gives `30,32,34,36,38,40,42,44`
— diverging from the true continuation `30,36,40,42,45,48,50,54` at the very next
term (`32` vs `36`), exactly as the outline claims. The general mechanism (legality is
a conjunction over the FULL history; dropping constraints can only ever admit MORE
candidates, never fewer, so exact reproduction is non-generic) is a correct,
elementary, non-circular argument — no case is missing, and the stated hypothesis
(`n_0 ≥ 2`, some earlier term genuinely constrains a candidate) is precisely what is
needed. This is sound and worth certifying so future rounds don't re-lose time to
restart-style inductions (already happened independently in rounds 3, 5, 8).

### 3. n1-periodicity-reconciliation — Verdict: **APPROVE** (build now)

This is honestly framed as attacking the *secondary* gap (n=1 extension), explicitly
conditional on FAH for the "T,L exist eventually" half — the outline repeatedly
flags this and instructs the builder not to imply the main crux is closer to solved.
That is the correct scoping, not an overclaim.

Is it worth a build slot now, with FAH still open? Yes: (a) it is a genuinely
different wall from the FAH corridor (per CLAUDE.md's plateau-break guidance, the
field should diversify away from a 15-times-dead shared gap, and this is untouched
since round 5's `reversible-transition-map`, which correctly found the pure-
injectivity route insufficient but did not use the *explicit finiteness* of N₁' — a
genuinely different lever, correctly identified as such here); (b) it reuses, rather
than re-derives, the certified Exact-Equality Reduction Lemma (round 7), so its
finite-verification framing is well-grounded and cheap to attempt; (c) it is
explicit that if the general argument fails and only seed-by-seed verification is
achievable, this must be reported honestly rather than forced — an acceptable,
non-overclaiming target. The one risk to watch: round 7 already showed the naive
"period-rescaling" fix is NOT automatic, and the outline correctly requires a
different closing argument (residue-set containment, not rescaling) — the builder
must not quietly re-derive the dead rescaling fix under new notation.

No case-coverage or circularity issues found. Approve to build, conditional framing
intact.

---

### Diversity assessment

Two of the three proposed approaches are genuinely orthogonal in framing:
`greedy-exchange-cost-potential`'s task this round is pure bookkeeping (does not
touch FAH at all), and `n1-periodicity-reconciliation` attacks a structurally
different gap (the secondary n=1 extension) using a lever (explicit finiteness of
N₁') that has not been tried before. Neither shares the wall that the (correctly
cut) `central-sets-idempotent-recurrence` would have hit. This keeps the population
from collapsing to one framing this round, consistent with the plateau-break mandate
— though note neither approved approach attacks the primary FAH crux directly this
round; per round-12 guidance, if round 14 still has no genuinely new FAH ingredient,
escalate to the flagged `|F''|=2` single-divisor-class bespoke fallback
(`covering-system-construction`'s Reduced-Alphabet Corollary already sets this up).

### Ranking

Registered `n1-periodicity-reconciliation` (new). Did not register
`central-sets-idempotent-recurrence` (RETHINK, per gate rule). Anchored the newcomer
against established dead-ends (beats `witness-index-descent`,
`reversible-transition-map`, `sieve-density-exception-bound` — all confirmed dead,
while the newcomer is a live, unfalsified outline) and drew with
`cofinite-window-capacity-bound` (comparable live-but-unresolved status). Also
confirmed `greedy-exchange-cost-potential` beats the dead-end
`confined-competitor-construction` and drew it against the leader
`covering-system-construction` (both remain the field's strongest, most-developed
lines). Updated ranking applied via `update_ranking`.

build set: greedy-exchange-cost-potential, n1-periodicity-reconciliation
