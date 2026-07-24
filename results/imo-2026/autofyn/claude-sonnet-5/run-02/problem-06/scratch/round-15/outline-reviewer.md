## imo-2026-06 — outline review (round 15)

### 1. H-prime-fiber packaging pre-screening — CONFIRMED correctly rejected

Independently re-checked the outliner's equivalence argument (H := {p : p | a_n
for infinitely many n} finite ⟺ recruitment halts). Q ⊆ H by the certified
Persistent-Type Pigeonhole (base-type primes recur infinitely often by
definition of persistence); every recruited prime q_k is forced (Generalized
Bounded Witness Lemma's Corollary) to divide infinitely many A'-type terms, so
q_k ∈ H by construction — the two events genuinely coincide. This is correct
and the outliner was right not to open it as a new approach; it supplies zero
new leverage over the existing recruitment-process halting formulation already
in `current.md`. No objection.

### 2. rogue-pair-termination-potential — **RETHINK** (not a new mechanism; it
duplicates already-certified round-6 content and its "genuinely new" open step
is verbatim the already-known-equivalent-to-FAH reduction)

This is the load-bearing finding of this review. The outline's pre-screening
note claims this is "genuinely different from the 16 dead mechanisms" and
frames it as "the 17th distinct mechanism attempt." That framing is wrong at a
more basic level than novelty-vs-dead-mechanism: **steps 2 and 3 of the
skeleton are not new content at all — they are a verbatim restatement of
round 6's already-certified Collateral-Safety Theorem and its own stated
"Consequence" paragraph**, and step 4 (billed as "the actual crux of this
approach," "an open key lemma") **is exactly FAH itself**, already identified
as such in round 6's own text.

Concretely, comparing the new outline to `lemmas/collateral-safety-theorem.md`
(certified, round 6):

- New Step 2 ("Base-pair pool bound," ≤3^{|Q|} disjoint base-type pairs,
  computable from Q alone) = Collateral-Safety Theorem's own certified
  **Corollary**: "the finite list of disjoint base-type pairs {(A,B): A,B∈𝒫,
  A∩B=∅} (at most C(|𝒫|,2) ≤ C(2^k−1,2) of them) are fixed once and for all at
  round 0... [refinement] never creates or destroys a base-type pair." Same
  object, same finiteness fact, different (looser) bound formula.
- New Step 3 ("Base-Pair Permanent Resolution": once fully resolved, stays
  resolved, via Monotonicity of Resolution) = the Collateral-Safety
  **Theorem** itself, word for word: "If (A,B) is fully safe at S₀, then (A,B)
  is fully safe at every S₁ ⊇ S₀" — proved in round 6 by combining the
  Projection Lemma with Monotonicity of Resolution, exactly the mechanism the
  new outline cites.
- New Step 4 ("Splitting-vs-Resolution Balance," open, "the actual crux of
  this approach") = the Collateral-Safety Theorem's own certified
  **Consequence**, already spelled out in round 6: "Defining open(k) := {(A,B)
  : not fully safe at S₀^(k)}... (†) holds iff open(k) = ∅ for some finite
  k... Whether open(k) reaches ∅ is precisely the question of 'full
  absorption' — does recruiting a Lemma-G prime against one witnessed rogue
  instance make the WHOLE base-type pair safe... This is exactly the
  sibling's Full-Absorption Hypothesis (FAH)." That is a **direct,
  word-for-word statement, already on record since round 6**, that this
  outline's "genuinely open Step 4" is FAH — the exact hypothesis 16
  mechanisms have already failed to prove, not a new termination question in
  disguise.

So the honest characterization is: this outline re-derives an already-
certified reduction under new vocabulary ("base-pair pool," "fully resolved")
and then re-arrives, with zero new ingredient, at the identical FAH wall that
has stood since round 6. It is not isomorphic to the dead Recruitment-Budget
mechanism (round 9, which bounded the *set of primes* ever recruited and was
refuted by an explicit escaping prime) or the CRT-glue/competitor-construction
family (round 10-11, which builds an explicit integer competitor via CRT) —
those really are different shapes, correctly ruled out as candidates by the
dispatcher's suspicion. The actual problem is worse: this isn't a rival
mechanism to compare against the dead ones at all, it's a relabeling of
content the workspace already has, proposed as if it were new. Building it
would spend a builder slot re-deriving the Collateral-Safety Theorem (already
certified, no new value) and then hitting FAH (already the standing crux,
already attempted 16 times) with no new tool — a wasted round.

**Verdict: RETHINK.** Do not build. Not registered in the ranker (a RETHINK
angle is never registered, per the tool's own policy). Instruct next round's
outliner: any future "bound a finite base/type pool + show recruitment makes
monotone progress" proposal must be checked directly against
`lemmas/collateral-safety-theorem.md`'s own "Consequence" paragraph first —
that paragraph already IS this reduction, and it already names its own open
step as FAH. A revival needs a genuinely new ingredient for closing FAH
itself (identity-level information about an intermediate term's
factorization, per the round-10 Rules diagnosis), not a new name for the
existing reduction.

(I did not run a numerical sanity check on the "does the same base pair
require multiple recruitment rounds" risk the outline itself flagged, because
the more basic finding above makes that check moot — even a full resolution
of that risk would only reprove round 6's own reduction, not touch FAH.)

### 3. n1-periodicity-reconciliation — advance — APPROVE

This approach remains honestly and consistently scoped as conditional on FAH
throughout (correctly does not claim to touch the main crux). Its round-15
continuation targets the two disclosed open sub-gaps from round 14: (a)
existence/termination of a self-absorbing core S*, (b) whether N(S*) can be
taken to be 0. Checked the proposed mechanism for (a): the claim that "each
absorption round adds finitely many primes... if this can be shown to
converge... the process trivially terminates" is not itself proved (correctly
left open, not asserted) — sub-gap (a) genuinely reduces to a "does a
greedy prime-set-growing process halt" question structurally analogous to (but
a distinct object from) rogue-pair-termination-potential's recruitment
process, and the outline explicitly and correctly flags this kinship rather
than claiming independent progress ("Watch out for" section) — this is
exactly the right honesty per the workspace's established precedent (e.g.
round 5's EEA-reduces-to-FAH disclosure). No fictitious mechanism found this
time (unlike round 14's grep-failure incident) — the plan cites only
already-certified machinery (Finite Core Theorem, Extended Persistent-Type
Pigeonhole, Non-Constructivity observation) and states its own open step
plainly. Sub-gap (b)'s proposed first step (compute S* concretely for 2 of the
6 already-checked seeds and test whether the theorem's actual N(S*) is 0, not
just the weaker N₁' object from round 13) is a reasonable, cheap, concrete
next check. Approve for build.

### 4. covering-system-construction / greedy-exchange-cost-potential — advance,
kept live for ranking continuity

No new step proposed this round for either; correctly not padded with filler
content. Fine to keep live in the ranking (both remain the strongest
main-crux-adjacent approaches, both stalled at the same FAH wall as everyone
else), but there is nothing to build this round — dispatching a builder on
either with "no new step proposed" would waste a slot. Not included in the
build set.

### Diversity note (per CLAUDE.md's plateau-breaking mandate)

The field this round is thinner than usual: the one candidate new corridor for
the MAIN crux (rogue-pair-termination-potential) turned out, on inspection, to
be a repackaging of existing certified content rather than a new corridor at
all. This means round 15, like round 13, has **no genuinely new attack
surface on FAH** — the main crux is now on its 10th-11th consecutive round
(6-15, minus the round-12 subword-complexity plateau-break) without a live
new mechanism. Escalate per the round-14 Rules: the general-mechanism well may
be structurally exhausted (16 confirmed-dead + this round's non-mechanism);
next round's outliner should seriously weigh the bespoke |F''|=2,
multiplicity-1 single-fixed-integer-divisibility question (round 12's
Reduced-Alphabet Corollary target) as the most concrete remaining path, or
mine the crux corpus once more but explicitly screening any candidate against
the round-6 Collateral-Safety "open(k)" reduction before proposing it as new.

### Build set

build set: n1-periodicity-reconciliation
