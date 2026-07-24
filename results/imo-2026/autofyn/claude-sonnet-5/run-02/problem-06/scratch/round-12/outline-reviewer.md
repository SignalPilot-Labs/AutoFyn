# Outline review — round 12 — imo-2026-06

Context checked: `results/imo-2026-06/current.md`, `results/imo-2026-06/approaches/{seed-coupling-induction.md, covering-system-construction.md}`, `/tmp/memory/run_state.md`, and `/tmp/round-12/proof-outliner.md`. I ran fresh from-scratch numerical checks on both new claims (scripts below, seeds up to N≈9000, trial-division gcd generator matching the workspace's established simulation pattern).

## Process note (fix before dispatch)
`results/imo-2026-06/approaches/subword-complexity-periodicity.md` **does not exist on disk** — the outliner described the approach fully in its round report but never wrote the approach file (register_approach's own contract says the outliner seeds this file). I registered the slug in the ranker anyway since the content is sound (see below), but the dispatched builder for this slug must **first create the approach file** from the outline's skeleton (Target/Technique/Skeleton/Key lemmas/Open gaps as given in `/tmp/round-12/proof-outliner.md`) before adding any new content — do not let it silently start from a blank/absent file.

---

## subword-complexity-periodicity (NEW) — Verdict: APPROVE (build, with mandatory first-task gate)

**Honesty check (the dispatch's main ask).** The outline is unusually candid: it states outright, twice, that proving bounded factor-complexity of (g_n) is logically EQUIVALENT to the problem's actual claim (Morse–Hedlund is an iff), so this is explicitly NOT a bypass of FAH — it's a different toolset (window/pumping combinatorics) aimed at the same wall. This is the correct, non-deceptive framing; nothing here secretly re-derives one of the 14 dead mechanisms under new vocabulary while claiming novelty — it owns the equivalence up front. That satisfies round 11's mandate ("a genuinely different corridor, not a reroute within the same one") in spirit: same ultimate wall, new attack surface.

**Is the "weaker target" real progress or circular?** I scrutinized step 4 (Finite-Defect Boundedness) myself: "finitely many colliding residue classes" is logically weaker than FAH's "zero collisions," but the outline is honest that even this weaker claim needs an ADDITIONAL unproved step to actually yield bounded complexity — "provided every sufficiently long run of visits eventually lands only in safe classes." This second condition is not automatic and is not swept under the rug; the outline flags it explicitly as unresolved. So the target is genuinely weaker than FAH (real, not circular relabeling) but the outline does NOT overclaim that weaker-target ⟹ done; it correctly scopes the residual gap. Good discipline — approve as stated, don't let the builder skip past that "provided" clause.

**Numerical sanity check (I ran this, matching the outline's own mandated first task).** Simulated gap sequences and computed factor-complexity p(k) for k=5..30 on a_1 = 105, 4807, 11305, 315 (N up to 9000 terms):
- a_1=105: p(k) plateaus at 58 for k≥10 — consistent with (short-period) eventual periodicity, matches the outline's own reported figure exactly.
- a_1=4807, 11305: p(k) grows nearly linearly with window count (≈N-k, i.e. almost all windows distinct) over the sampled range — NOT yet plateaued. This is consistent with these being long-transient FAH rogue-pair seeds (large L₀ = product of a bigger S₀) rather than evidence against the mechanism; the outline is correct to call this "empirical curiosity only, not evidence either way," and I confirm that framing — a non-plateau at N≈6000 says nothing when the true period could need L₀ ≫ 6000.
- a_1=315: also growing, no plateau by N=9000 (confirms the outline's characterization of it as a fresh long-transient seed).

This is consistent with — not contradicting — the mechanism. No falsification found; the approach is a legitimate speculative attempt.

**Gate to enforce on the builder:** do exactly what the outline says — FIRST compute, on a_1=4807/11305/315, the number of DISTINCT colliding S₀-residue classes (not just eyeball p(k)). If that count is not visibly small/finite (e.g. grows with sample size the way p(k) itself does), retract immediately rather than forcing the mechanism — this is the outline's own instruction and I endorse it as the correct falsification-first discipline this workspace has used successfully before (rule #6 in outline-reviewer memory).

Watch-outs from the outline (Morse-Hedlund cited by name is not a proof; finite-defect must not silently become empty-defect; p(k) curiosity is not evidence) are all correctly stated — no changes needed there.

---

## seed-coupling-induction (REVISE) — Verdict: RETHINK (do not build this round)

The outline's own text calls Lemma A (Base-Type Correspondence, Aggregate Form) "completely open and UNTESTED even numerically — mandatory first step before any deeper work." **I ran that mandated test myself before approving**, per outline-reviewer memory rule #9/#12 (always independently verify a claimed numeric-sensitive lemma before trusting it as a build target). Result: **Lemma A is already falsified**, not merely untested.

Method: for the SAME 12 (a_1, removed-prime) pairs the outline asks to check, I compared the SET of Q'-restricted types visible in the original a_1-sequence against the SET of (full) types occurring in the reduced b_1-sequence (b_1 = a_1 with the chosen prime's full power stripped), i.e. exactly the "aggregate/set-level, not positional" claim the revision proposes. Findings:

| a_1 | removed p | Q' | orig type set | reduced type set | SET_MATCH |
|---|---|---|---|---|---|
| 105 | 5 | {3,7} | {3},{3,7},{7} | {3},{3,7} | **False — missing {7}** |
| 165 | 3 | {5,11} | {5},{5,11},{11} | {5},{5,11} | **False — missing {11}** |
| 315 | 5 | {3,7} | {3},{3,7},{7} | {3},{3,7} | **False — missing {7}** |
| (9 other pairs) | | | | | True |

I then extended the two clearest failures (b_1=21, Q={3,7}; b_1=55, Q={5,11}) to **15,000 terms** each: the "missing" type (lone-7 for b_1=21; lone-11 for b_1=55) genuinely **never occurs**, while the corresponding original-sequence restricted type occurs with substantial frequency (e.g. 2586/15000 ≈ 17% for the a_1=105 case, restricted to the same Q'={3,7}). This is not a small-transient artifact — it is a robust structural fact: whichever prime of Q' is locally denser (3 vs 7; 5 vs 11) comes to dominate the reduced 2-prime process so completely that the "sparser prime alone" type becomes structurally unreachable, exactly as round 8's diagnosis found for prime 2 specifically — except this generalizes it: it is not just "2 is special," it is "whichever prime dominates locally in the SMALLER prime set does unrepeatable work that the larger original prime set doesn't need it to do." That is precisely the same underlying mechanism that killed the round-8 positional/frequency version of this Lemma, now recurring at the strictly weaker set-level formulation the outline proposes as the escape.

**This is the exact "secretly repackaging a falsified claim" risk the dispatch asked me to check for, and it is confirmed.** The revision's own stated defense ("this is a much weaker and possibly true claim even though the falsified stronger form is false") does not hold up — the weaker claim fails too, for the same reason, on 3/12 tested pairs including two robustly reconfirmed at 15k terms. Per outline-reviewer memory rule #17/dispatch instructions and the workspace's established protocol (round 8: falsify cheaply, don't spend a build round chasing a doomed rescue), I am RETHINKing this before build rather than dispatching a builder to discover exactly what I already found.

**What survives:** Lemma B (New-Prime Pair Resolution / D_bad-collapse corollary) does not depend on Lemma A and is a genuine, valid, modest bookkeeping fact (a corollary of the already-certified Confined-GCD + Singleton-Side FAH lemmas). It should be captured as covering-system-construction's already-scheduled "Reduced-Alphabet Corollary" bookkeeping task this round (the outline already plans this), not as a standalone seed-coupling build.

**Guidance for next round's outliner if this framing is revived:** any single-prime-removal reduction (whether tracked positionally, by frequency, or now by type-SET) inherits the same failure: removing one prime from Q can silently eliminate an entire reachable-type class in the reduced process whenever the remaining primes have a large enough relative-density gap. A genuinely different reduction step is needed (e.g. removing a prime chosen so the remaining set's density profile is preserved — untested, no candidate construction currently exists), not a repair of "drop one prime and compare."

---

## covering-system-construction (ADVANCE, bookkeeping only) — Verdict: APPROVE (no new FAH content, correctly scoped)

Correctly scoped as continuity/ranking-anchor only — no new mechanism dispatched, matching round 11's bar against a 15th same-corridor variant. The one live task (certifying the Reduced-Alphabet Corollary, importable now that seed-coupling-induction's Lemma B is orphaned) is a real, bounded, low-risk task independent of any open FAH gap. Approve as scoped; explicitly reject (per the outline's own watch-out) any attempt to sneak a 15th FAH-corridor mechanism in under this slug.

---

## Diversity assessment (per CLAUDE.md)

The field this round genuinely diversifies: subword-complexity-periodicity is a different toolset (combinatorics on words) even though it targets the same ultimate crux (honestly disclosed, not hidden) — this satisfies the "different framing, not just different technique on the same gap" bar better than most of the last 6 rounds' variants, since it changes what OBJECT is being reasoned about (the gap sequence's word-complexity) rather than another divisor-recruitment variant. seed-coupling-induction, even in its revised aggregate form, is now confirmed to collapse back into the same corridor's failure mode (extremal-density-prime obstruction) — cutting it before build is exactly the right move to avoid wasting a slot re-discovering a known wall under new notation.

---

## Ranking

Registered `subword-complexity-periodicity` (new, cold-start). Ran update_ranking anchoring the new arrival against established approaches: covering-system-construction (leader) beats both seed-coupling-induction (re-failed) and subword-complexity-periodicity (new, unproven); subword-complexity-periodicity beats seed-coupling-induction (sound-and-honest vs re-falsified) and greedy-exchange-cost-potential beats seed-coupling-induction; subword-complexity-periodicity draws cofinite-window-capacity-bound (comparable speculative/partial status). Post-update: covering-system-construction ~1863 (leader), greedy-exchange-cost-potential ~1785, cofinite-window-capacity-bound ~1528, subword-complexity-periodicity ~1514 (new), seed-coupling-induction ~1503 (down from re-failure).

build set: subword-complexity-periodicity, covering-system-construction
