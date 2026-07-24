## imo-2026-06 — outline review, round 8

Read: `/tmp/round-8/proof-outliner.md`, all three math-explorer reports
(`math-explorer-thread-unification.md`, `math-explorer-cross-bucket-direct.md`,
`math-explorer-subset-avoidance.md`), the persisted approach files
(`persistent-backbone-monovariant.md`, `forced-primes-well-ordering.md`,
`sunflower-bundle-closure.md`), `results/imo-2026-06/current.md`, and the
cited lemma files. Independently re-derived/re-ran every claim flagged in the
dispatch (Python spot-checks below), not just re-read the outline's prose.

### Independent verification of the four flagged claims

**(1) "Permanent-bundle-count alone is insufficient for `𝓥_S`-finiteness —
transient members are the real gap."** CONFIRMED. The thread-unification
explorer regenerated both documented depth-3 escape events from scratch
(fresh generator, cross-checked against 7 hand-verified `a_1=247` values and
matched every cited factorization in `current.md` exactly, e.g.
`a_19617=2·3·7·17·23·67`, `a_30017=2^3·3·7·19·41·197`) and traced every
"deep" escape to one of two shapes: (i) a re-realization of an *already
established permanent bundle* at a later, immediately-dominated index
(6 of 7 cases), or (ii) a genuinely transient member (`a_1291`'s
`{2,3,7,41,197}`, alive from `n=1291` to `n=2575` before being dominated by
the permanent bundle `{2,3,7,197}`) — a real, distinct phenomenon the
Permanent Bundle Lemma's scope never covers. `𝓥_S` = permanent ∪ transient
by Theorem V; bounding only the permanent half leaves a genuinely separate,
still fully open count. This is a real, previously-unstated (if implicit
since round 6) sharpening, not a relabeling.

**(2) "Escape-depth-boundedness is a one-directional corollary of
`𝓥_S`-finiteness, not an independent target."** CONFIRMED, and the proof
sketch is sound. The Freeze-Confinement Corollary's mechanism (poset of
realized class-`S` radicals under `⊆`; a newly realized radical is either a
new minimal element, causes a removal, or is a proper superset of an
existing minimal element; once the antichain freezes at `n*`, only the
third case can occur for later indices) is a standard, correct
antichain-maintenance argument — I re-derived it independently and it holds.
This correctly retires round 7's independent depth-hunting program (§G Step
4 had already found the naive branching tree doesn't terminate; this
explains *why*: observed shallow depth is a byproduct of early antichain
freeze, not an intrinsic well-founded structure of the recursion itself).

**(3) The pairwise-disjoint-bundle pigeonhole corollary.** CONFIRMED
correct. Traced the derivation by hand: applying the certified
Escape-Confinement Lemma with `κ:=S` requires `S` itself to be "blocked" by
witness `j_3` (`rad(a_{j3})∩S=∅`); this in turn requires `S` is *never*
exactly realized as a bare value — which follows automatically from the
already-certified Lemma P (`G_i≠∅`, every pair of terms shares a prime): if
some index exactly realized `S`, it would need a common factor with
`a_{j3}`, contradicting the blocking hypothesis. So every actual `i∈I_S` is
a genuine "escape" over `κ=S`, giving `Q_i∩comp(a_{j3})≠∅` for every
realized bundle, and disjoint bundles pigeonhole into `comp(a_{j3})`
(bounded, size 2–4 in every tested case). The outline correctly does *not*
overclaim this bounds the *total* bundle count (only pairwise-disjoint
families) — both approach files that use it (persistent-backbone-monovariant
Step 1, sunflower-bundle-closure Step 3) state this limitation explicitly.

**(4) sunflower-bundle-closure's Δ-system mechanism.** Sound, and it is
genuine (non-circular) progress, not a reformulation in disguise. Checked
specifically whether "(UB_S) ⟹ `Λ_S` finite" collapses into a tautological
equivalence with `Λ_S` finite (which would repeat the H=rad(L_per)/Pool
Lemma "restatement, not reduction" trap this workspace has hit before): it
does not — `Λ_S` finite does *not* trivially give (UB_S) as stated (which
bounds the companion-bundle size over *every* realized index `i∈I_S`, not
just the ones ever minimal in `𝓥_S`; a dominated/never-minimal index could
in principle carry an arbitrarily large bundle while `𝓥_S` itself stays
finite), so the implication only runs one way and is real content. The
classical infinite Δ-system dichotomy for uniformly-bounded-size finite-set
families (any infinite such family has an infinite pairwise-disjoint
sub-family or an infinite sunflower with common core) is standard, and the
outline correctly flags that its proof needs only bounded *set size*, not a
finite ground alphabet — true, and stated explicitly rather than silently
assumed. The Case (b) branch (sunflower with core `Y`) is handled correctly
via Lemma ER's two-way dichotomy (eventually realized ⟹ only finitely many
petals precede it; permanently blocked ⟹ Escape-Confinement forces petal
remainders to pigeonhole again). Is (UB_S) itself proven? No — it is
honestly flagged, repeatedly, as the same open difficulty as round 3's
`ω(a_n)=O(1)`, restricted to a subsequence, not a strictly easier target.
Reducing to it is still real progress (same status as Theorem 5.1's
FCBC-conditional reduction, which this workspace has consistently and
correctly treated as valuable): it supplies a genuinely new mechanism
(extremal/pigeonhole, not construction) that converts an open existence
question into an open *boundedness* question via a route none of the prior
7 rounds tried.

**Shared prerequisite: core-avoiding witness existence.** Spot-checked
directly (fresh Python, exact factorization) on `a_1∈{247,2747,4199,4087}`:
computed `P_1:=rad(a_1)` and, for every distinct proper core `S=C∩P_1`
observed among the first 600 terms, searched for an index `j` with
`rad(a_j)∩S=∅`. A witness was found immediately (index 2, 3, or 4) for
*every* proper core in all four cases (e.g. `a_1=4199`: cores `{17}`,
`{17,19}`, `{19,13}`, `{13}`, `{19}`, `{17,13}` all have witnesses at index
2–4). This is real, not silently false — consistent with the outline's own
honest framing ("flagged as an unproved likely-easy pigeonhole... every
worked example happens to have one, general existence is not established").
The candidate general mechanism (P_1\S≠∅ since S is a proper core, plus
Lemma P applied to another realized core) is plausible but genuinely
unproven — correctly treated as CHANGES REQUESTED content, not silently
assumed in any of the three "cheap" steps that depend on it.

### Per-approach verdicts

**persistent-backbone-monovariant — revise. APPROVE (build).** Step 1
(pigeonhole corollary) is genuinely new, correct, and cheap — verify above.
Step 2 (iterate the confinement recursion for a cumulative bound) is
honestly scoped as open, with the exact prior obstruction named
(pointwise-vs-cumulative, rounds 3–6) and an explicit instruction not to
silently fall back to `ω(a_n)=O(1)`. No fatal flaw; a real, non-redundant
retarget from round 7's proven-insufficient permanent-bundle-count target.

**forced-primes-well-ordering — revise. APPROVE (build).** Step 1
(Freeze-Confinement Corollary) is sound and correctly retires an entire dead
sub-program (independent depth-hunting). Step 2 (`S^+` extended-imprint
necessity, reusing the already-certified Generalized Lemma C with `I_S` in
place of `J_S`) is correct and cheap. Step 3 (`S^{++}` sufficiency
refinement, targeting the one honestly-reported failing instance
`a_1=21528751,S={1061}`) is genuinely open, unattempted by the round-8
explorer, and concrete. No fatal flaw.

**sunflower-bundle-closure — new. APPROVE (build).** Genuinely different
top-level lever (extremal/pigeonhole existence argument, no explicit
construction) from both siblings' construction/counting mechanisms — real
diversity, not a third name for the same wall. Correctly and repeatedly
self-flags that (UB_S) is not an easier target than round 3's open
`ω(a_n)=O(1)`, avoiding the overclaiming trap this workspace has hit before
(H=rad(L_per), Pool Lemma, SA-vs-Λ_S). Watch-out section explicitly warns
against re-deriving ND1/ND2 or silently assuming a finite prime alphabet —
appropriate defensive framing. No fatal flaw.

None of the three approaches is a fragment of the problem — each carries the
full certified reduction chain (Theorem 5.1 → Lemma MS → Theorem CD/V →
Λ_S-Reduction Lemma) down to its own distinct final-gap mechanism, matching
the pattern this workspace has used successfully since round 3. Diversity
check: the three final open targets are genuinely different questions —
persistent-backbone-monovariant's cumulative-confinement-recursion bound,
forced-primes-well-ordering's `S^{++}` sufficiency, and sunflower-bundle-
closure's (UB_S)/`ω(a_n)=O(1)` — not the same wall relabeled three times,
even though all three share the cheap core-avoiding-witness sub-lemma and
(two of three) the pigeonhole corollary. Per this workspace's standing rule,
sharing a sub-lemma via genuinely different routes to the final target is
legitimate diversity, not the single-gap trap.

### Cross-cutting note for the orchestrator

This is round 8 of what is now 6 consecutive rounds (3–8) on the FCBC/
`(MRS)`/`𝓥_S` family. Unlike a flat plateau, round 8's field shows real
forward movement: the population correctly diagnosed and retired a
round-7 confusion (permanent-bundle-count ≠ the actual target), retired an
entire dead sub-program (independent depth-hunting) with a real proof
rather than more empirical search, and opened one genuinely new mechanism
(Δ-system/extremal) not tried in rounds 1–7. If round 9 finds all three
threads stall again — persistent-backbone-monovariant on the cumulative
bound, forced-primes-well-ordering on `S^{++}` sufficiency, and
sunflower-bundle-closure still stuck on `ω(a_n)=O(1)` — that would be a
strong, sharply-localized signal (as the outliner itself flags) that
`ω(a_n)=O(1)`/(UB_S)-equivalent boundedness is the true irreducible core of
the whole 6-round family, worth attacking directly as round 9's sole target
rather than continuing to reformulate around it.

build set: persistent-backbone-monovariant, forced-primes-well-ordering, sunflower-bundle-closure
