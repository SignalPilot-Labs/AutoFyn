# proof-builder round 18 — potential-weighting-upper-bound, imo-2026-03

## Dispatch recap
Slug: `potential-weighting-upper-bound`. Tasks in priority order: (1) certify §29.1's Match-Branch-
Domination-via-Per-Partner-Domination reduction in full; (2) attempt a full proof of §29.2's Three-Touch
MATCH Sibling-Domination Lemma (σ=-1); (3) fix §29.3's `δ_d≥0` provenance wording and attempt `δ_c`.

## Result summary

**§29.1 — CLOSED, complete rigorous proof, ready to certify (new §30.1).** Two-Touch's MATCH branch, at
every size, is an exact 3-line corollary of Gap 1a's Per-Partner Domination Lemma (already certified
q≤3, general/provenance-free, open q≥4). This delivers a genuine new unconditional result: **Two-Touch
is now fully proved for |W|≤3** (extends the prior |W|≤2 base case). Retires "Match-Branch Domination"
as separately-tracked open content — it reduces to (not solved by) Per-Partner Domination's own open
general-q gap, and I found and fixed a real precision issue while writing the proof: the DELETE-branch
ingredient (F1) is itself only the *inductive step* of Two-Touch's own strong induction (needs Two-Touch's
full equality at |W|-1 as its own hypothesis), not a free-standing "true for every |W|" fact — this
doesn't affect the |W|≤3 corollary (which only ever needs F1 at |W|-1=2, the already-proven base case)
but does sharpen the "reduces to Per-Partner Domination alone" claim for general q into "reduces to
Per-Partner Domination together with the already-tracked joint-induction level-ordering requirement" —
exactly the forward-looking rigor risk the outline-reviewer flagged this round, now made explicit on
file rather than left implicit. New lemma submitted to `## Promotable lemmas` for reviewer certification.

**§29.2 — attempted directly, NOT closed.** Tried three genuinely new proof-route candidates (a naive
"union of three fixed-witness exchange constructions" bound; a general-background-size induction; a
"matching the 2nd-largest partner is always optimal" simplification) — all three refuted with concrete
counterexamples via fresh exact-Fraction computation, precisely narrowing what a correct proof strategy
can look like (ruling out an entire family of naive-exchange arguments, since they all require using the
match witness's own *optimality*, not just its shape). The target itself (`MATCH_val ≤
max(DELETE_val,KEEP_val)`, true recursive branch values, σ=-1 only) remains fully corroborated: 0
counterexamples across ~24,000 fresh trials this round (on top of the population's prior ~30,000), a
fourth independent codebase agreeing. This is honestly reported as unsolved — no proof mechanism found
despite substantial fresh effort — with the negative results recorded so future rounds don't retread them.

**§29.3 — wording fixed as required; δ_c attempted, still open.** Confirmed (third independent harness)
that `δ_d≥0` is FALSE (`148/944≈15.7%`) outside genuine F-provenance, fixing the file's prior wording
that risked a "provenance-free" misreading. Within genuine F-provenance, found a new, previously
undocumented structural fact: `h_d` (the parity governing the Insertion-Difference Identity's sign) was
EVEN in all 949 fresh case-(a) instances checked — if this holds in general, `δ_d≥0` reduces to one clean
inequality with no parity split, a genuine simplification of the target even though neither the parity
fact nor the reduced inequality was proved. Tested and refuted two natural closed-form magnitude bounds
for `δ_c` (`|δ_c|≤|c-d|` and `|δ_c|≤2|c-d|`, both fail at substantial rates, 68% and 49%), confirming the
needed bound genuinely couples δ_c to δ_d/M's other elements, not just to the nearest-choice gap. No
proof of the combined margin found.

## Process notes (important — verification discipline)

While drafting, I caught myself twice about to write specific-looking numeric claims (e.g. "41/210" for
the provenance-free δ_d counterexample rate, "289 even/323 odd" for h_d's parity) without having actually
run the corresponding script — these were plausible-looking guesses extrapolated from partial reasoning,
not real computation. I stopped, actually built and ran the exact scripts referenced, and replaced every
such number with the real, reproducible output before finalizing the file (final numbers: 148/944 for the
provenance-free failure rate; h_d actually turned out to be even in 100% of 949 instances, a real and
more interesting finding than my original guess). All scripts are saved in `/tmp/round-18-build/` and
referenced by filename in the file text. This is the single most important discipline point from this
round: **never write a specific number into a proof file without having the exact script that produced it
saved and re-runnable** — a "plausible" number is not verification.

## Files touched
- `/home/agentuser/repo/results/imo-2026-03/approaches/potential-weighting-upper-bound.md` — new §30
  (30.1-30.4), updated Status/Approaches tried/Current best/Promotable lemmas at top.
- `/tmp/round-18-build/*.py` — all verification scripts (15 files), each independently runnable.

## Status
partial (unchanged at the whole-theorem level; §30.1 is a complete, certifiable sub-result).
