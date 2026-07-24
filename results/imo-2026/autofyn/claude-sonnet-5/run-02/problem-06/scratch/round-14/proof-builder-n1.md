## Round 14 — n1-periodicity-reconciliation build report

Task: fix the "combining both parts" gap in the Self-Absorbing Core Theorem
(`results/imo-2026-06/approaches/n1-periodicity-reconciliation.md`), flagged by
round 13's proof-reviewer and re-confirmed this round by the outline-reviewer.

### What I verified from scratch

- Grepped `covering-system-construction.md` lines 303-338 (Step 5) myself: confirmed
  it is a one-paragraph argument, no case split, defining G := {r : sig(r) ∈ 𝒫'}
  directly — landing is automatic there only because G is defined by exact type
  membership, a strictly narrower condition than this theorem's G* ("sig(r) meets
  every persistent type"). The outline's proposed "same-base/overlapping-base/
  disjoint-base trichotomy" does not exist in Step 5 (confirmed by direct reading,
  matching the outline-reviewer's independent grep).
- Independently re-derived the correct fix (not just transcribed the outline-
  reviewer's sketch): worked through the full logical structure of what's actually
  needed. Found that the theorem does NOT need a full "iff" for an arbitrary
  candidate c — it needs (S) sufficiency for arbitrary c (already fine in the
  original write-up) plus (L) landing specifically for the realized next term
  a_{n+1}. Verified (L) splits cleanly into two independent facts: the early-term
  conjunct from the certified Free Facts Lemma (`lemmas/free-facts-gcd.md`) plus
  self-absorption, and the persistent-type conjunct from directly unpacking the
  theorem's own "FAH holds at S*" hypothesis applied to the pair of types
  (ρ_{S*}(n+1), B) for arbitrary B ∈ 𝒫'(S*) — no case-split needed since FAH-at-S*
  is a universally-quantified statement about pairs of TYPES, not about which j have
  occurred by index n.
- Checked that (S)+(L) together are enough to force a_{n+1} to be exactly "the next
  element of G* in cyclic order" via a minimality argument (any candidate strictly
  between a_n and a_{n+1} fails (S)'s hypothesis, hence lies outside G*), and that
  this cyclic-advance map is a permutation of the finite set G*, giving a genuine
  (not just eventual) period-T* cycle.

### What I did

Rewrote the "Combining both parts" section of the Self-Absorbing Core Theorem's proof
in `results/imo-2026-06/approaches/n1-periodicity-reconciliation.md` (replacing the
old citation-based hand-wave) with the full (S)/(L) derivation above, spelled out in
complete detail with no hand-waving and no citation to Step 5's construction. Updated
`## Approaches tried`, `## Current best` (§5's assessment), and `## Full proof`
sections to reflect that the theorem itself is now gap-free while the overall
approach's Status stays `partial` (the theorem is still conditional on FAH-at-S* and
on the two open sub-gaps — existence/termination of a self-absorbing S*, and whether
N(S*) = 0 — neither attempted this round, consistent with the prior round's honest
framing).

### Promotable lemma

Certified (submitted, pending reviewer confirmation) the **Self-Absorbing Core
Theorem** to `results/imo-2026-06/lemmas/self-absorbing-core-theorem.md` — now a
complete, gap-free conditional theorem (conditional only on its two stated
hypotheses: S* self-absorbing, FAH holds at level S*). The file states clearly it is
provisional pending independent reviewer re-verification, per the codebase's
"builder proposes, reviewer certifies" convention, but includes it directly per this
round's explicit dispatch instruction.

### Status

`results/imo-2026-06/approaches/n1-periodicity-reconciliation.md` Status remains
`partial` (correct — the problem's actual target, literal periodicity from n=1, is
not established; only a conditional sub-theorem is now gap-free). No overclaiming:
the two open sub-gaps (a) existence/termination of self-absorbing S*, (b) N(S*)=0,
are both still explicitly flagged as unresolved.
