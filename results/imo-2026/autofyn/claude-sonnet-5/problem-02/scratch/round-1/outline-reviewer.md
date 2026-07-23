# Outline review — imo-2026-02, round 1

Read: `/tmp/round-1/proof-outliner.md`, all five `results/imo-2026-02/approaches/*.md`,
`problems.jsonl` entry for imo-2026-02, `knowledge_base.md` (synthetic toolkit,
coordinates/complex/barycentric, power-of-a-point sections). `results/imo-2026-02/current.md`
does not yet exist — no prior progress to conflict with. No `.ranking.json` existed before
this round; all five slugs registered fresh at Elo 1500 (see below).

Problem (imo-2026-02, hard, geometry, rating 8): triangle ABC, M/N midpoints of AB/AC,
K inside △BMC, L inside △BNC, with K inside ∠LBA, L inside ∠ACK, ∠KBA=∠ACL,
∠LBK=∠LNC, ∠LCK=∠BMK; O = circumcenter of AKL. Prove OM=ON.

General note on process: none of the explorers/outliner ran a from-scratch numeric
verification I could independently re-run in this review pass (time budget), but the
outliner's account is specific and consistent (three independent explorers converging on
the same O_x=p/2 identity to 1e-14, with an explicit list of confirmed dead ends). I treat
that as credible terrain evidence but flag it in each verdict below where an approach's
correctness still hinges on an unverified numeric claim.

## coordinate-trig-bash — APPROVE

Whole-attempt: yes, targets OM=ON end-to-end via one continuous computation.
The reduction OM=ON ⟺ O_x=p/2 is a correct, mechanical consequence of N−M=(1,0) in the
chosen frame (perpendicular bisector of a horizontal-difference segment is a vertical
line) — this is not hand-waved, it's derived from OM²−ON²=2·O·(N−M)+|M|²−|N|², a standard
identity (knowledge_base.md coordinates section). No circularity.
Technique (coordinate + trig bash with resultant elimination) is a legitimate sledgehammer
for a "prove this identity holds along a parametrized family" problem, and the terrain
support (independent numeric convergence, ~1e-14, across three explorers) makes it the
best-justified route in the field.
Open risk, correctly flagged by the outliner itself, not by me newly: (a) the resultant
elimination for r1(t), r2(t) may be intractable — acceptable, since a fallback (isosceles
AB=AC special case) is named for partial credit; (b) branch/orientation tracking is
explicitly called out as mandatory (the coordinate explorer found wrong branches give
OM≠ON) — good, this is exactly the kind of "avoid the plausible wrong answer" step that
must not be skipped. Nothing to add here; build as specified, but require the builder to
actually exhibit the branch conditions (signs on t, r1, r2 vs. the containment hypotheses)
as inequalities, not just assert "the right branch is chosen."

## labeling-duality — CHANGES REQUESTED (approved as a build candidate, but the central
mechanism is honestly unproven)

Whole-attempt: yes. Genuinely distinct framing from coordinate-trig-bash — no explicit
parametrization of the family, a symmetry/duality argument instead. Good diversity value.
The σ-invariance observation (step 1) is a real, checkable, mechanical fact (rewriting
∠KBA=∠ACL as ∠KBM=∠LCN via ray BA=ray BM, ray CA=ray CN, since M∈AB, N∈AC) — sound.
The linear Cramer's-rule expansion of O(A,K,L) (step 2) is standard and correctly derived
(2·O·(K−A)=|K|²−|A|² is the correct perpendicular-bisector-of-AK linear equation, not the
erroneous "2(O−A)·(K−A)=0" the outline explicitly flags and rejects — good, the outline
self-corrects a wrong formula before committing to it, which is the right instinct).
Issue: steps 3–4, the actual mechanism ("look for forced cancellation," "nail down the
mechanism... this is the hardest and least understood step") are a bare label with no
stated identity or substitution yet — this is exactly a "lemma named without its mechanism"
per my brief. It is not fatal (the outline is honest that this is open, not asserting it as
already proved), so RETHINK is too harsh, but the builder must not proceed by assuming
cancellation happens — it must derive the σ-anti-symmetric residual explicitly (write Φ out
in full using law of sines in the sub-triangles) and only then check whether conditions 2/3
kill it. If after one builder pass no concrete cancellation identity is found, downgrade
hard next round (this is a real risk noted by the outline itself: "if it doesn't fully
close, expect to fall back to partial credit").
One caution reinforced from the outline: BMK and CNL are confirmed NOT similar (numeric
refutation cited) — the builder must not silently reintroduce that as a "helper" fact.

## nine-point-link — CHANGES REQUESTED, but deprioritized this round (not in build set)

Whole-attempt: yes, target is still OM=ON via O sharing a line with the nine-point center,
not a substitute sub-lemma. The nine-point-circle-through-M,N fact (step 1) is completely
standard and correctly justified (medial-triangle homothety ratio −1/2 at centroid) — fine
as a certifiable, reusable lemma regardless of what happens to the rest of the approach.
Issue: the actual mechanism (steps 3–4, "find a transformation... inversion at A or a
two-step spiral similarity") is pure speculation with zero confirmed instance — the outline
itself admits the single obvious inversion at A (power AM·AB matching AN·AC) fails unless
AB=AC, and no alternative has been tried. This is the weakest-grounded approach in the
field: it is not circular and not a repeat of a recorded dead end (O=nine-point-center is
correctly flagged as already refuted and NOT what's being claimed), so it does not merit
RETHINK, but it should not consume round-1 builder time when three other approaches have
either stronger terrain support or a concrete, cheap first test. Keep registered for
population breadth; revisit if the top three stall.

## two-step-spiral-chain — CHANGES REQUESTED (approved, contingent on an immediate,
cheap numeric gate)

Whole-attempt: yes, and it is honest about its own risk profile — the outline explicitly
states "EVERYTHING here is provisional" pending a numeric check (spiral-similarity ratio
BK/BL=NL/NC, and a concyclicity C,M,K,X) that no explorer has yet run. This is the right
instinct (a falsifiable gate before synthetic write-up), and it targets angle-pairings
(∠LBK=∠LNC; ∠LCK=∠BMK) genuinely distinct from the already-refuted global BMK~CNL
similarity and MKNL-concyclic hypotheses — correctly distinguished, not a resurrection of a
dead end.
Requirement for the builder: the FIRST action must be exactly the numeric side-ratio and
concyclicity checks (step 1–2), using the same fsolve/1-parameter-family setup the
explorers already built — if both fail, mark this approach dead-end within this round
rather than forcing a synthetic write-up on a false premise. This is a cheap, well-defined
gate so it's worth including in the build set despite being unverified.

## complex-circle-power — CHANGES REQUESTED, but deprioritized this round (not in build
set)

Whole-attempt: yes. Genuinely different computational strategy (O at origin vs. B,C
symmetric about origin) — correctly distinguished from coordinate-trig-bash in setup, even
though both ultimately rest on the same linear-in-O expansion of OM²−ON² (that's shared
structure, not duplication — the target expansion is forced by geometry regardless of
frame). The outline is self-aware about the real risk: it flags its own step-3 reconciliation
as unfinished business and explicitly instructs the builder to downgrade priority if the
computation converges to literally the same grind as coordinate-trig-bash. Power-of-a-point
via secants (step 4) is a standard, correctly-cited technique, but the specific secant to use
is not yet identified — real open gap, not hidden.
Given coordinate-trig-bash already occupies the "linear-in-O expansion, brute force" slot
with stronger terrain support, and this approach's own outline flags the redundancy risk,
it's reasonable to leave it in the population but not spend round-1 builder time on it.

## Diversity assessment

The five approaches split into three real families of framing, not five independent ones:
(1) brute-force reduction to the linear-in-O identity via explicit parametrization
(coordinate-trig-bash, and to a real extent complex-circle-power — same target equation,
different secant/algebra machinery); (2) formal symmetry/duality argument on the same
linear-in-O expansion (labeling-duality); (3) rigid-map / spiral-similarity or Miquel-point
search (two-step-spiral-chain, nine-point-link — both look for a transformation forcing O
onto the fixed line, differing in whether the transformation is local (spiral similarity on
K,L) or global (inversion/homothety tied to the nine-point circle)).
This is acceptable diversity for round 1 (three genuinely different mechanisms are present),
but the orchestrator should note for future rounds: if coordinate-trig-bash and
labeling-duality both stall on "the same residual term doesn't cancel," that is the same
wall wearing two coats (both work with the identical Cramer's-rule expansion of O), and a
genuinely orthogonal 4th framing (e.g. a projective/cross-ratio argument, or trying to
locate the whole 1-parameter family as an explicit envelope) should be solicited rather than
another variant of the linear-O expansion.

## Ranking

Registered all five slugs fresh this round (previously unregistered — outliner's tool
access did not include `register_approach`). Ranked head-to-head by outline strength (no
outcomes exist yet, so this is a round-1 prior anchored to terrain evidence and gap
concreteness, not built results):

1. coordinate-trig-bash (1559.7) — strongest terrain support (independent triple numeric
   confirmation), most concrete/checkable mechanism.
2. two-step-spiral-chain (1517.9) — has a cheap, well-defined falsifiable first test.
3. labeling-duality (1515.9) — genuinely distinct framing, but central mechanism (step 3-4)
   is a named-without-mechanism gap.
4. complex-circle-power (1468.2) — real but largely overlapping with coordinate-trig-bash's
   target equation; outline itself flags the redundancy risk.
5. nine-point-link (1438.4) — most speculative, no confirmed transformation candidate at
   all; only the standalone nine-point-circle-through-M,N fact is solid.

## Build set

Prioritizing the strongest terrain-supported line plus genuine diversity of framing per
CLAUDE.md, and matching the outliner's own recommendation: build coordinate-trig-bash
(hardest, most likely to close), plus one representative each of the symmetry-argument
framing (labeling-duality) and the rigid-map/spiral framing (two-step-spiral-chain, gated
on its cheap numeric check). nine-point-link and complex-circle-power stay registered for
population breadth but are not built this round.

build set: coordinate-trig-bash, labeling-duality, two-step-spiral-chain
