## Status
Certified (round 29). Negative/diagnostic result, in the same class as the
certified `same-type-free-facts-vacuity.md` and
`density-argument-vacuity-corollary.md` — a toolkit-independent screening
lemma, not a portable positive tool.

## Statement (Bipartite-Network Reduction Collapse)

For the greedy-gcd sequence's FAH problem (imo-2026-06), any "growing
bipartite index-set network with local repair on failure" mechanism — in the
sense of tracking evolving finite sets `𝒜_k, ℬ_k` of occurrence indices with
a complete-bipartite shared-prime-edge invariant, repaired by enlarging the
reference core `S₀` on edge failure, adapted from crux `aimo-1000`'s
ferry-islands toggle mechanism — reduces, under its two only possible
formalizations, either:

- **(a) Reading α (fixed core):** to the already-certified Generalized
  Bounded Witness Lemma's bounded-but-not-singleton linking pool
  `F'_{A',B'} := P(a_m)\S₀` (fixed once a single witness `m` with `ρ(m)=B'`
  is fixed), which is already known insufficient for Cofinite FAH — finite
  pigeonhole from this pool only gives "some prime of the pool links
  infinitely many n," never "cofinitely many n"; or
- **(b) Reading β (growing core):** to the already-open H2 core-growth-
  termination criterion (`termination-criterion-lemma.md`'s boundedness of
  `(N(S_k))_k`), for which the certified Witness Discontinuity Obstruction
  (`witness-discontinuity-obstruction.md`, `a_1=175`) is a genuine,
  unconditional obstruction to any "obviously bounded" shortcut.

## Proof

See `results/imo-2026-06/approaches/bipartite-network-invariant-fah.md`,
Propositions A–D (round 29 build). Proposition A shows Reading α's pool is
exactly `F'_{A',B'}`, a direct one-line corollary of the round-2 Generalized
Bounded Witness Lemma (no new leverage, no repair step ever required — the
guarantee is already universal in `n>m`). Proposition B shows this
boundedness is strictly weaker than what Cofinite FAH needs, citing the
certified Lemma's own Status line ("Does NOT by itself close gap (†)").
Proposition C identifies Reading β's repair operator `S_k\to S_k\cup\{q_k\}`
as verbatim the certified Self-Absorbing Core Theorem's `S_k\to S_k^+`
operator, so "bounded total recruitment across repairs" is definitionally
`(S_k)_k` stabilizing, i.e. the already-open H2 termination question.
Proposition D additionally shows the crux `aimo-1000`'s load-bearing move (a
deterministic "toggle-if-adjacent-to-exactly-one" rewrite rule, guaranteed to
fire by that problem's own hypothesis) has no arithmetic analog in the
greedy-gcd recursion, which supplies only an existential linking guarantee
(Free Facts / Generalized Bounded Witness Lemma) — a structural mismatch
independently verified against the crux database
(`past_crux_moves_database.json`, `problem_id="aimo-1000"`).

## Scope

Rules out the entire "growing bipartite/network-invariant transplant with
local repair" mechanism family (not just one instantiation) as a route to
H1/FAH, until and unless H2's termination question is separately resolved
(at which point the network framing becomes moot anyway, since H2 + the
existing Master Conditional Theorem already suffices). Does not resolve H1
or H2 itself.

## Independent verification (round-29 proof-reviewer)

Independently re-checked: (i) the Generalized Bounded Witness Lemma's own
Status line does say "Does NOT by itself close gap (†)" (grepped directly);
(ii) the Self-Absorbing Core Theorem's operator is indeed
`S_k\to S_k\cup\bigcup_{j\le N(S_k)}P(a_j)`, matching Proposition C's
identification exactly; (iii) the `aimo-1000` crux quote in Proposition D
matches `past_crux_moves_database.json` verbatim. No gap found; certified.
