# Round 15 proof-review — imo-2026-06

Build set this round: **n1-periodicity-reconciliation** (revise). One slug built,
one verdict.

## Verdict: CHANGES REQUESTED (Status: partial)

This approach remains explicitly conditional on FAH throughout (as it has since
round 13), so it cannot and does not flip the overall problem Status — assessed
here purely as its own conditional-partial result.

## What was claimed vs. what I independently verified

### (a) Universal Early Intersection Lemma + Literal n=1 Periodicity Theorem — VERIFIED CORRECT, no hidden hypothesis, not a restatement

**Universal Early Intersection Lemma.** Statement: if S* is self-absorbing (i.e.
P(a_j) ⊆ S* for every j = 1,...,N(S*)), then for every such j and every
S*-extended-persistent type B ∈ 𝒫'(S*), P(a_j) ∩ B ≠ ∅.

I re-derived this from scratch independently of the file's prose. Proof: B occurs
at infinitely many indices (definition of persistence), so pick m ≠ j with
ρ_{S*}(m) = B (always possible — an infinite set minus one point is nonempty). The
certified, fully unconditional Free Facts Lemma (gcd(a_i,a_k) > 1 for every pair of
distinct indices — this is a triviality of the problem's own recursive definition:
for i<k, a_k is defined to be legal against a_i, and gcd is symmetric so this
transfers to either ordering of the pair) gives a common prime p ∈ P(a_j) ∩ P(a_m).
Self-absorption forces P(a_j) ⊆ S*, so p ∈ S*; combined with p ∈ P(a_m), this puts
p ∈ P(a_m) ∩ S* = ρ_{S*}(m) = B. So p ∈ P(a_j) ∩ B. This matches my own
re-derivation exactly — correct, and genuinely uses **no FAH hypothesis at all**,
only self-absorption (already part of the existing theorem's hypotheses, not new)
plus Free Facts (already certified, unconditional) plus the bare definition of
persistence. No hidden hypothesis smuggled in.

Is this "just restating" the existing Self-Absorbing Core Theorem? No — the
existing theorem's proof of its "Landing" step used the FAH-at-S* hypothesis to
get intersection between a *late* term's type and other persistent types; this new
lemma gets the analogous intersection for an *early* (index ≤ N(S*)) term with NO
FAH assumption, purely from self-absorption + Free Facts. That is a genuinely new
ingredient not present in the certified theorem's own proof, which is exactly what
the extension from "n ≥ N(S*)" to "n ≥ 1" needed.

**Literal n=1 Periodicity Theorem.** I re-ran the three-step extension
(Sufficiency, Landing, Assembling) myself, checking each range boundary:
- Sufficiency's self-absorption branch (j ≤ N(S*)) never referenced "n ≥ N(S*)"
  in the original certified proof (confirmed by re-reading
  `lemmas/self-absorbing-core-theorem.md` Step 1) — so it transfers verbatim to
  any n ≥ 1. Correct, not an overclaim.
- Landing's first conjunct (early-term intersection) only used Free Facts +
  self-absorption, both unconditional and range-independent — extends to n ≥ 0
  (i.e. covers a_1 itself, n=0) with no new content needed. I specifically
  checked the j = n+1 edge case (P(a_{n+1}) ∩ P(a_{n+1}) reduces to
  P(a_{n+1}) ⊆ S*, nonempty since a_{n+1} > 1) — correct.
- Landing's second conjunct is the one place needing new content for the range
  n+1 ≤ N(S*), and this is exactly where the Universal Early Intersection Lemma
  is applied (j := n+1) — correctly, since self-absorption in this range gives
  P(a_{n+1}) = P(a_{n+1}) ∩ S* = sig(a_{n+1} mod L*), matching the required form.
- Assembling is mechanically unchanged, now valid over the full extended range.

I also checked the N(S*) = 0 edge case explicitly: all the "j ≤ N(S*)" ranges
become empty and the argument correctly degenerates to the original certified
theorem's content with no contradiction.

**Conclusion:** both are correct, genuinely new (not restatements), and introduce
no new hypothesis beyond the two already in the certified Self-Absorbing Core
Theorem. Sub-gap (b) is genuinely closed. I also independently reimplemented (a
fresh, different Python script) the builder's computational sanity check
(a_1=175, 3000 terms, proxy core {2,3,5,7,11,13,17} from the first 20 terms,
persistent-like types = >1% of a long tail window, checking P(a_j) ∩ B for
j=1..30) and reproduced the exact reported numbers: 480 checks, 0 violations.

### (b) Termination Criterion Lemma — VERIFIED CORRECT, both directions

Statement: the absorption chain S_0 ↦ S_0⁺ ↦ ... terminates in finitely many
steps iff the threshold sequence (N(S_k))_{k≥0} is bounded.

**(⟹)** Trivial: past termination, N(S_k) is eventually constant; finitely many
earlier values are each individually finite; max of finitely many finite values
is finite. Correct.

**(⟸)** I re-derived this independently: given a uniform bound M on N(S_k), define
the *fixed* set P*_M := ⋃_{j=1}^M P(a_j), built only from the actual sequence
values a_1,...,a_M — genuinely independent of k, so the induction "S_k ⊆
S_0 ∪ P*_M for all k" is non-circular (I checked this specifically, since a
subtler-looking but circular version of this argument — where P*_M secretly
depends on S_k — would be a red flag; it does not here). The inductive step
correctly uses N(S_k) ≤ M to bound the union's range. Since S_k are subsets of a
fixed finite set, non-decreasing, and strictly increasing at every
non-terminating step (by definition of "not self-absorbing"), the chain can only
strictly increase finitely many times, forcing termination. Correct, standard,
no gap.

The lemma is honestly *not* claimed to resolve sub-gap (a) — boundedness of
N(S_k) is explicitly left open, and the file states clearly that no certified
tool bounds it.

### (c) Is sub-gap (a) really "logically distinct" from the main FAH/recruitment-termination crux?

I checked this claim on its own merits rather than taking the builder's word.
N(S) (from Extended Persistent-Type Pigeonhole) is a pigeonhole threshold about
*when* extended-persistent types first stabilize at a given core S — a purely
"onset timing" quantity. FAH (and the sibling recruitment-process termination
question) is about whether two *already-stabilized*, disjoint-base-type
persistent types intersect within a core. These genuinely are different
questions in their raw statement: one is about the index at which a fixed-point
behavior begins, the other is about a set-intersection property once it has
begun. I looked for (and did not find, in the time available) any argument
reducing one to the other in either direction — e.g. I checked whether FAH
holding at S₀ would obviously bound N(S_k) along the chain (it does not appear
to: N(S) depends on how quickly *any* type — not specifically an FAH-relevant
pair — stabilizes, and enlarging S changes the alphabet 2^S in a way that isn't
controlled by whether disjoint types intersect). So the builder's claim —
"logically distinct object, structurally analogous in difficulty, not proved
equivalent" — is accurate and not overclaimed. It correctly avoids the stronger
(and unjustified) claim that sub-gap (a) is definitely easier or definitely as
hard as FAH; it only asserts a structural kinship (both are "greedy process under
a non-constructive threshold" questions), which is fair given the correct
citation of `witness-discontinuity-obstruction.md`'s independently-certified
"refinement can manufacture new classes" phenomenon as the reason no easy
argument was found.

## Certification decisions

Certified all three new results as promotable lemmas, each independently
re-verified with no gap found:
- `results/imo-2026-06/lemmas/universal-early-intersection-lemma.md`
- `results/imo-2026-06/lemmas/literal-n1-periodicity-theorem.md`
- `results/imo-2026-06/lemmas/termination-criterion-lemma.md`

## Overall assessment

Genuine, permanent progress on this approach's own sub-target: the residual
dependency chain for "literal n=1 periodicity, conditional on FAH" has shrunk
from three open ingredients (FAH; existence of a self-absorbing S*; N(S*)=0) to
exactly two (FAH; existence of S*). Sub-gap (a) is now a precise, proved iff
rather than a vague "does this converge" question, though still genuinely open.
No new FAH mechanism was attempted or killed this round — the main crux is
untouched, as intended by this round's dispatch (a secondary-gap round). Overall
workspace Status remains `partial`.

`results/imo-2026-06/current.md` updated: `## Status` prepended with a new round-15
entry (kept `partial`), `## Approaches tried` given a new round-15 entry for
`n1-periodicity-reconciliation`. No `## Full proof` section added (Status not
`solved`).

## Files touched
- `/home/agentuser/repo/results/imo-2026-06/current.md` (Status + Approaches tried updated)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/universal-early-intersection-lemma.md` (new, certified)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/literal-n1-periodicity-theorem.md` (new, certified)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/termination-criterion-lemma.md` (new, certified)
