## Theorem: Literal n = 1 Periodicity Theorem — CERTIFIED, round 15

**Source.** `n1-periodicity-reconciliation`, round 15 build. Independently
re-derived in full and confirmed correct by the round-15 proof-reviewer.

**Status of conditionality.** Strictly strengthens the conclusion of the certified
`self-absorbing-core-theorem.md`, under the IDENTICAL two hypotheses — no new
hypothesis is introduced. Both hypotheses (existence of a self-absorbing S*; FAH
holding at level S*) remain open elsewhere in the workspace; this theorem does not
touch either.

**Statement.** Suppose S* ⊇ S₀ is self-absorbing and FAH holds at level S* (every
two elements of 𝒫'(S*) intersect within S*) — exactly the hypotheses of the
Self-Absorbing Core Theorem. Then, with the SAME G*, T* := |G*|, L* := ∏_{p∈S*} p
as in that theorem,

  a_{n+T*} = a_n + L*  for EVERY n ≥ 1

(not merely for n ≥ N(S*)). In particular N(S*) may always be taken to be 0.

**Proof (sketch of the extension; full detail in the approach file, §5a).** Re-run
the Self-Absorbing Core Theorem's three-step proof (Sufficiency, Landing,
Assembling), extending each step's range from n ≥ N(S*) to n ≥ 1 (Sufficiency,
Assembling) / n ≥ 0 (Landing):

- *Sufficiency* extends verbatim to every n ≥ 1: its self-absorption branch
  (j ≤ N(S*)) never used n ≥ N(S*) in its derivation, only j ≤ N(S*); its
  persistent-type branch (N(S*) < j ≤ n) is unchanged.
- *Landing*, first conjunct (early-term intersection), extends to every n ≥ 0
  using only the unconditional Free Facts Lemma (no FAH needed) plus
  self-absorption, exactly as in the original proof.
- *Landing*, second conjunct (persistent-type intersection), splits into two
  ranges: n+1 > N(S*) uses the original FAH-at-S* argument unchanged; the NEW
  range n+1 ≤ N(S*) is covered by the newly certified **Universal Early
  Intersection Lemma** (`universal-early-intersection-lemma.md`), applied with
  j := n+1, giving P(a_{n+1}) ∩ B ≠ ∅ for every B ∈ 𝒫'(S*), which — since
  self-absorption gives P(a_{n+1}) = P(a_{n+1}) ∩ S* = sig(a_{n+1} mod L*) for
  this range — is exactly the needed second conjunct.
- *Assembling* is unchanged in mechanism, now valid for every n ≥ 1 since
  Sufficiency and Landing now hold in that full range; the resulting residue
  sequence (a_n mod L*)_{n≥1} is the orbit of a_1 mod L* ∈ G* (by Landing at
  n=0) under the same fixed permutation of G*, hence a single |G*|-cycle from
  n=1 onward.

**What this resolves.** Sub-gap (b) of `n1-periodicity-reconciliation` (whether
N(S*) can be taken to be 0) is now proved TRUE unconditionally relative to the two
standing hypotheses — no longer merely conjectured or left open. The approach's
residual dependency chain is reduced from three open ingredients (FAH itself;
existence of S*; N(S*)=0) to exactly two (FAH itself; existence of S*).

**What this does NOT resolve.** Sub-gap (a) (existence/termination of a
self-absorbing S*) and FAH itself (the primary, workspace-wide crux) remain fully
open; this theorem is conditional on both, exactly as its predecessor was.

**Verification note (round 15 proof-reviewer, CERTIFIED).** Independently
re-derived every extended step from scratch, checking in particular: (i) the
Sufficiency step's self-absorption branch genuinely never referenced n ≥ N(S*)
anywhere in its own derivation (confirmed by re-reading the certified theorem's
Step 1 — the branch only uses j ≤ N(S*), independent of n); (ii) the j = n+1
edge case in Landing's first conjunct (P(a_{n+1}) ∩ P(a_{n+1}) reduces correctly
to P(a_{n+1}) ⊆ S* via self-absorption, nonempty since a_{n+1} > 1); (iii) the
N(S*) = 0 vacuous-range edge case is handled correctly with no contradiction
(when N(S*)=0, the "j ≤ N(S*)" ranges in both Sufficiency and Landing are empty,
and the argument reduces to exactly the original theorem's already-certified
content). No gap found. **Certified.**
