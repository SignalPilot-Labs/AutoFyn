# proof-builder round 29 — bipartite-network-invariant-fah

Status: unsolved (RETHINK).

Ran the outline-reviewer's mandated **corrected** Step-1 disambiguation check
(not the outline's original, trivially-true "does a repair prime always
exist" question) in full, rigorously, before attempting any of Steps 2–5.

The corrected question — "does the pool of linking primes used across
network repairs stay bounded, not just does one exist somewhere" — has
exactly two possible formalizations, and both were worked out to completion:

- **Fixed-core reading**: bounded, but this is a one-line corollary of the
  already-certified Generalized Bounded Witness Lemma
  (`lemmas/generalized-bounded-witness-lemma.md`), and it is already known
  insufficient for Cofinite FAH — finite pigeonhole only forces "some class
  infinite," never "cofinite" (the Lemma's own Status line says so
  explicitly, and the standing `a_1=4807` seed's bounded pool `F'={13,17}`
  needed an entirely separate, seed-specific ad hoc argument, round 26's
  Finite-Window Literalization Lemma, to resolve — not derivable from
  boundedness alone).
- **Growing-core reading**: this is definitionally identical to the
  already-open H2 core-growth **Termination Criterion Lemma** (round 15,
  `lemmas/termination-criterion-lemma.md`) — "does the absorption chain
  `(S_k)_k` stabilize" — for which the certified **Witness Discontinuity
  Obstruction** (round 7, `a_1=175`) is a concrete, unconditional obstruction
  to any easy "obviously bounded" shortcut (enlarging the core by the very
  prime that triggered a repair does NOT guarantee the new witness is
  divisible by that prime).

I also pulled the actual `aimo-1000` crux moves from
`past_crux_moves_database.json` (not just the label) and found the real
mechanism is a **deterministic toggle rule** ("closing edge A–B forces
*every* vertex adjacent to exactly one endpoint to gain the missing edge,
guaranteed by the ferry problem's own rewrite rule"). This has **no
arithmetic analog**: the greedy-gcd recursion only ever supplies an
*existential* shared-prime guarantee (Free Facts / Generalized Bounded
Witness Lemma), never a simultaneous, deterministic repair — confirmed by
the Witness Discontinuity Obstruction, which shows the opposite of a toggle
(a recruited prime's own triggering index can become orphaned from the
repaired witness).

Conclusion: the corrected disambiguation, done honestly, does not open new
ground — it collapses either into already-certified-but-insufficient
machinery or into the already-open H2 question, and the transplanted
mechanism itself does not survive contact with the problem's actual update
rule. Reported as a clean, precise, reusable negative result (a new
"Bipartite-Network Reduction Collapse" corollary, proposed for certification,
ruling out the whole graph/network-invariant transplant family for H1/FAH,
not just this one instantiation) rather than forced into a fake positive.
Status set to `unsolved` per the round-5 fast-RETHINK precedent — no
iteration on this approach.

File written: `/home/agentuser/repo/results/imo-2026-06/approaches/bipartite-network-invariant-fah.md`
(full Propositions A–D, citing `lemmas/generalized-bounded-witness-lemma.md`,
`lemmas/free-facts-gcd.md`, `lemmas/witness-discontinuity-obstruction.md`,
`lemmas/termination-criterion-lemma.md`, `lemmas/finite-window-literalization-lemma.md`,
and the retrieved `aimo-1000` crux entries).
