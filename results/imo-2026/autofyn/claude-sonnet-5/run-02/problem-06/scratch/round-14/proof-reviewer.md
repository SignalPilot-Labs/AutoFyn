# Round 14 proof-reviewer report — imo-2026-06

Two slugs built this round. Independent, adversarial review of each below.
`results/imo-2026-06/current.md` and `results/imo-2026-06/lemmas/self-absorbing-core-theorem.md`
have been updated to reflect this review's findings.

## 1. `n1-periodicity-reconciliation` (revise) — Self-Absorbing Core Theorem gap fix

**Verdict: CHANGES REQUESTED. True Status: `partial`.**

Round 13's proof-reviewer flagged that the theorem's "combining both parts" step
cited `covering-system-construction` Step 5's construction (a one-paragraph proof
for a strictly NARROWER set `G := {r : sig(r) ∈ 𝒫'}`, no case-split) to justify a
claim about this theorem's own, more broadly defined `G*`. This round's builder
removed the citation entirely and replaced it with a self-contained
Sufficiency/Landing decomposition. I independently re-derived every step from
scratch rather than trusting the builder's or the outline-reviewer's assessment:

- **Sufficiency (S)** for an arbitrary candidate `c`: split into `j ≤ N(S*)` (via
  self-absorption `P(a_j) ⊆ S*` + the standard CRT signature fact) and
  `N(S*) < j ≤ n` (via the second conjunct of `G*`'s definition, taking
  `B := ρ_{S*}(j) ∈ 𝒫'(S*)`, using Extended Persistent-Type Pigeonhole applied
  AT LEVEL S*). I checked `lemmas/extended-persistent-type-pigeonhole.md` directly
  — it is stated and proved generically for "any fixed finite S₀ ⊇ Q," so
  instantiating it at S* is legitimate reuse of already-certified content, not a
  new unproved step. Valid, no gap.
- **Landing (L)** for the real `a_{n+1}`: the early-term conjunct follows directly
  from `lemmas/free-facts-gcd.md` part 1 (I confirmed this lemma literally states
  `gcd(a_{n+1},a_i)>1` for every `i≤n`, exactly what's invoked) plus
  self-absorption; the persistent-type conjunct follows from directly unpacking
  the theorem's OWN stated hypothesis "FAH holds at level S*" applied to the pair
  of types `(ρ_{S*}(n+1), B)` for arbitrary `B ∈ 𝒫'(S*)` — no citation to Step 5
  anywhere in this branch. Valid, no gap. This genuinely fixes what round 13
  flagged: the theorem no longer borrows an argument that was never actually run
  for its own broader object.
- **Assembly**: minimality of `a_{n+1}` plus the contrapositive of (S) shows every
  integer strictly between `a_n` and `a_{n+1}` has residue outside `G*`, while
  `a_{n+1}` itself lands in `G*` by (L) — forcing `a_{n+1}` to be exactly the next
  `G*`-residue in cyclic order, hence a single `|G*|`-cycle. This re-derivation of
  the cyclic-pigeonhole mechanism (already used unconditionally in the original
  Step 5) is correct and does not circularly depend on Step 5's own proof.

**One precision issue I found, not flagged by the builder** (does not sink the
theorem, but matters for future use): the theorem's hypothesis is phrased "FAH
holds at level S* — every two elements of 𝒫'(S*) intersect," while everywhere
else in this workspace "FAH" specifically means "every two DISJOINT-BASE-TYPE
extended-persistent types intersect." These sound different (the theorem's
version applies to ALL pairs, including same/overlapping-base-type ones). I
independently verified they are in fact mathematically EQUIVALENT, not that the
theorem secretly assumes something stronger: since `Q ⊆ S*` and `ρ_S(n)∩Q = τ(n)`
exactly, any two extended-persistent types with NON-disjoint base types
automatically satisfy `A'∩B'≠∅` for free (a shared base-type prime is already in
both extended types) — no FAH-type hypothesis is needed for those pairs. So
"every two elements of 𝒫'(S*) intersect" reduces to exactly "every two
disjoint-base-type elements intersect" (standard FAH) plus this always-true free
fact. The approach file asserts the equivalence ("unpacked literally, this is
exactly the statement...") without deriving it. I have added the missing
one-line derivation to the certified lemma file so a future round attempting to
discharge this theorem's hypothesis doesn't mistake it for a strictly stronger
burden than standing FAH-at-S*.

I also double-checked the two honestly-disclosed open sub-gaps are still
genuinely open, not smuggled as proved:
- (a) existence/termination of a self-absorbing S* (the absorption operator
  `S ↦ S⁺` reaching a fixed point in finitely many steps) — correctly left
  untouched, no argument given either way in this round's file.
- (b) whether `N(S*) = 0` — correctly left untouched; the reported 6-seed
  computational check (§4) tests a strictly weaker question (plain tail-derived
  `N₁'` can be taken as 0, not literally `N(S*)`), and the file is explicit and
  accurate about this scoping, not overclaiming it settles (b).

**Conclusion.** The theorem's proof, as fixed this round, is complete and
rigorous, strictly conditional on its two disclosed hypotheses. **Certified**
to `lemmas/self-absorbing-core-theorem.md` (updated: removed the "provisional,
pending review" note, added this review's confirmation plus the precision note
on hypothesis-equivalence). Because the theorem is still conditional on two
open, FAH-adjacent hypotheses, and the primary FAH/Symmetric FAH crux elsewhere
in the population is untouched, the approach's overall Status remains
`partial` — this is genuine, certified progress, not a full solve.

## 2. `integer-monovariant-difference-identity` (new) — negative result

**Verdict: RETHINK. True Status: `unsolved`** (matches the builder's own
self-report — no overclaim to correct).

The approach imports crux `aimo-0134`'s bounded-integer-monovariant +
difference-identity mechanism (integer statistic, forced per-step inequality
sharpened by integrality to monotone descent, then a difference identity
recovering exact term values) and searches for an analogue in this problem that
sidesteps "which specific prime recurs" language.

**Independent verification performed:**

1. Re-derived `aimo-0134`'s own mechanism from scratch (not trusting the
   builder's summary) — confirmed correct: `b_k := (a_1+\dots+a_k)/k` is an
   integer by that problem's rule, `(k+1)b_{k+1} \le kb_k+k` gives strict
   `b_{k+1}<b_k+1`, integrality sharpens to `\le`, descent+boundedness give
   eventual constancy, and `a_k=(k+1)b_{k+1}-kb_k` transfers constancy back to
   the original sequence. Matches the builder's §0 summary.
2. **Reimplemented this problem's greedy sequence completely independently**
   (fresh Python script, no reuse of the builder's code) for both mandated
   seeds and reproduced the reported computational claims EXACTLY:
   - `a_1=4807`: max gap 38, min gap 2; running average of gaps increases at
     1196 of 2498 checked steps (≈48%); `D_2=11 → D_3=1`.
   - `a_1=11305`: max gap 14, min gap 2; running average increases at 998 of
     2498 steps (≈40%); `D_2=5 → D_3=1`.
   Exact match to every number the builder reports — strong independent
   confirmation, not merely re-running the same script (I wrote my own
   simulation from the problem statement).
3. Checked the five candidates' individual arguments (running average of gaps —
   dead, not integer/no forcing inequality, computationally refuted; running
   minimum of gaps — monotone+bounded but only ever reveals a one-bit "is the
   new gap smaller" fact, no prime identity; running gcd of all terms —
   monotone+bounded but collapses to 1 almost immediately, structurally
   uninformative; persistent-type count — an exact restatement of the
   already-certified Persistent-Type Pigeonhole, no new leverage; recruited-core
   size — its boundedness IS gap (†) itself, circular) — all five arguments are
   individually sound as described.
4. Independently re-derived the general §3 diagnosis: this problem's greedy
   legality rule (`gcd(c,a_i)>1` for all `i≤n`, minimal `c`) only ever asserts
   THAT a shared prime exists, never WHICH one (already certified in this
   workspace via Same-Type Free Facts Vacuity / Selection-Rule
   Class-Blindness) — so any statistic built purely from counts, minima, gcds,
   or averages inherits this blindness and can never be forced, by a genuine
   per-step algebraic identity, to reveal a specific prime's identity. This is
   a sound, general structural argument, not hand-waving, and I could not find
   a sixth candidate (within my review budget) escaping it — e.g. a
   core-size-plus-fixed-witness-marker combination still only encodes counts,
   not identities.

**Conclusion.** This is a genuine, honestly-obtained negative result: a
technique family genuinely new to this workspace (no prior round tried a
bounded-integer-monovariant/difference-identity transplant) is closed off with
a sound general reason, not just a failed search. No counterexample to FAH was
sought or found, and none is claimed. This correctly counts as the 16th
confirmed-dead FAH-adjacent mechanism. No lemma proposed for certification
(correctly — every individual fact used is an elementary consequence of
already-certified lemmas, and the diagnostic content matches the established
Lemma-F/Lemma-I "toolkit-diagnostic, not portable" precedent, kept as
in-file/current.md documentation rather than a standalone lemma file).

## Workspace-level update

`results/imo-2026-06/current.md` updated:
- New round-14 paragraph prepended to the `## Status` history block.
- New entries added to `## Approaches tried` for both slugs this round.
- New `## ROUND 14` section appended (detailed re-derivation record), plus
  `## Lemma certification this round (round 14)` and
  `## Next-round guidance (current, round 14)` sections.
- Overall Status remains **`partial`**: the Self-Absorbing Core Theorem is now
  a fully certified conditional result (real, non-trivial progress on the
  secondary n=1 gap), but neither its own two open hypotheses nor the primary
  FAH/Symmetric FAH/Cofinite FAH/EEA crux is resolved. 16 FAH-adjacent
  mechanisms are now confirmed dead across 9 consecutive rounds (6-14) on the
  same underlying obstruction — this round's negative result used a genuinely
  new technique (not a repeat of a prior dead framing), which is useful
  narrowing even though it did not break the plateau in the "new corridor
  opened and survives" sense.

`results/imo-2026-06/lemmas/self-absorbing-core-theorem.md` updated: removed
the "provisional, not yet reviewed" note; added this review's confirmation and
a precision note about the FAH-at-S* hypothesis's equivalence to the standard
disjoint-base-type formulation used elsewhere (a documentation improvement,
not a change to the theorem's content).

## Summary of per-approach verdicts

| Slug | Builder-reported Status | Reviewer-confirmed Status | Verdict |
|---|---|---|---|
| n1-periodicity-reconciliation | partial | partial | CHANGES REQUESTED |
| integer-monovariant-difference-identity | unsolved | unsolved | RETHINK |

No overclaim found in either file — both builders' self-reported Status
matches this review's independent assessment.
