# Build report — self-blocking-clutter-induction (round 1)

## Headline: the pure combinatorial theorem is REFUTED

Per the outline-reviewer's directive, I attacked the target theorem of this slug
("every identically self-blocking clutter of finite sets on a countable ground set is finite")
with refutation attempts FIRST — and found an explicit counterexample. The theorem is **false**.

**The ladder clutter.** Take the one-way infinite ladder graph G (rungs r_i = u_i v_i, rails
a_i, b_i), s = u_0, t = v_0, and two fresh ground elements 1, 2. Let L1 = edge sets of simple
s–t paths, L2 = minimal finite s–t cuts (both infinite families of finite sets), and

  M = {{1,2}} ∪ {{1} ∪ P : P ∈ L1} ∪ {{2} ∪ C : C ∈ L2}.

Then M is an infinite intersecting antichain of finite sets and every finite transversal of M
contains a member (full proof: Lemmas 1–6 in the approach file; the crux is graph duality —
a finite edge set hitting every minimal finite cut contains an s–t path, proved by taking the
boundary δ(S) of the s-component S, which is a finite cut disjoint from the edge set). So
b(M) = M: an infinite identically self-blocking clutter.

Computer sanity check (truncations, both-sided cut enumeration, 2^11 candidate transversals):
0 failures on the crux lemma (292 cases) and on the self-covering property (1023 cases).

## What this means for the field

The ladder clutter also satisfies the witness lemma AND the clutter-level consequence of the
dodging lemma (E0 = {1,2} meets every member; the member {1,2} avoids any finite B disjoint
from E0), and it is consistent with the proved sunflower kill (5b): its common-trace
subfamilies have unbounded sizes — exactly the open case (5c). Therefore:

- **GAP B is dead; this slug's original induction plan is cancelled.**
- **GAP 1 (sunflower route) cannot be closed from the current clutter-level property list**
  (intersecting antichain + self-covering + witness + "some member avoids any finite big B").
  Any purported pure closing is false. New candidate lemmas for GAP 1 should be tested against
  the ladder clutter first.
- Surviving levers are genuinely number-theoretic: window/location control of dodging (avoiding
  terms exist in EVERY length-g window, no ladder analog), and counting/density (V has bounded
  gaps and density ≥ 1/g; {m : P(m) ⊇ X} has density 1/∏_{p∈X} p) — matching the reviewer's
  suggested density line. The lock-in target ∪M ⊆ E0 of the CRT rival is also not pure-derivable
  (∪M is infinite in the ladder), consistent with that approach's number-theoretic spine.

## File updated

- results/imo-2026-06/approaches/self-blocking-clutter-induction.md — Status: partial.
  Full rigorous proof of the no-go theorem; dead-end verdict for the pure induction recorded
  under Approaches tried; consequences and a hypothesis-filter rule recorded under Watch out for.

## Promotable lemma

- "No-go: infinite identically self-blocking clutters exist (ladder clutter)" — proved in full
  in the approach file; recommend reviewer certification into results/imo-2026-06/lemmas/ as a
  hypothesis-filter for all future attacks on the finiteness gap.

## Spec concerns

- None on the problem statement itself. One field-level concern: the shared foundation's phrase
  "M identically self-blocking ⟹ ..." is safe, but any round summary should now avoid implying
  that self-blockingness *per se* carries finiteness information — it does not. The Elo of this
  slug should reflect that its outcome is decisive negative information, not zero progress.
