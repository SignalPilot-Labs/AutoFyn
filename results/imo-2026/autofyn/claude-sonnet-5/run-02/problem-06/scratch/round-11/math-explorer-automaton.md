## Status
unsolved (terrain report only — no proof attempted, per dispatch instructions)

## Lens
Automaton / finite-state-graph-walk encoding of the greedy process (nodes =
divisor-classes / extended-types, edges = transitions between consecutive
occurrences), investigated as a possible new route to FAH / Symmetric FAH /
Cofinite FAH, or even a bypass of FAH altogether.

## Headline finding
**The encoding exists cleanly (it is exactly the certified Confined-GCD Lemma's
divisor-class alphabet), but the automaton framing is not new — it is FAH itself,
already tried under other names, and already killed. Concretely, this lens
re-derives (independently, via graph-walk vocabulary) findings already certified
in rounds 5, 9, and 10, and adds one new piece of numerical evidence (a genuine
|F''|≥2 walk over 8000 terms) that corroborates rather than escapes the existing
diagnosis. Recommend: do NOT open this as a new approach; it collapses onto
already-explored (and already-dead) mechanisms once made precise.**

## 1. The state space exists and is already certified
The natural node set for a "divisor-class automaton" is exactly the certified
**Confined-GCD Lemma** (`lemmas/confined-gcd-lemma.md`): for a rogue pair
`(A',B')` with witnesses `n_A<n_B`, `F'' = P(a_{n_B})\S₀`, `b :=` the `F''`-part
of `a_{n_B}`, every later `A'`-occurrence `n` has `g_n := gcd(a_n,a_{n_B})` a
divisor of the FIXED integer `b` — a genuine finite alphabet `Div(b)`, with
`g_n>1` always, and `q*|a_n ⟺ q*|g_n`. So "nodes = divisor classes, walk = the
sequence `g_{n_1}, g_{n_2}, ...` over successive `A'`-occurrences" is a clean,
already-proved object. This part of the lens is real and not wasted — it is
literally the vocabulary the round-9/10 approaches already use.

## 2. The transition function is exactly the open crux, not a bypass of it
Three independent, already-certified/diagnosed results kill the "build the
transition function so it's identity-preserving by construction" hope:

- **Round 5's S-sufficiency ⟺ (†) Theorem** (`approaches/reversible-transition-map.md`,
  proved both directions, flagged for certification but not yet certified as a
  standalone lemma file — still valid, independently re-derivable). For ANY
  fixed finite core `S`, "the state `σ_S(n) = P(a_n)∩S` determines the legality
  of future candidates" (forward well-definedness of a finite-state transition
  map) is proved logically EQUIVALENT to "every two disjoint-base-type
  `S`-extended-persistent types intersect," i.e. exactly gap (†) at level `S`.
  This is the general reason no finite-state recast at a FIXED level can be an
  easier route: building the transition map's legality rule by construction
  already presupposes the type-intersection fact FAH is trying to establish.

- **Round 9's Successor-Transport Reduction Lemma + stall**
  (`lemmas/successor-transport-reduction-lemma.md`): the natural one-step
  "absorbing state" transition — `q*|a_{n_j} ⟹ q*|a_{n_{j+1}}` for all large `j`
  (the **Successor Claim**) — is PRECISELY the "transition edge is
  identity-preserving" property this lens was sent to look for, phrased already
  in exactly this graph-walk shape. It is a certified, correct reduction (if the
  Successor Claim holds, Cofinite FAH follows by induction along the walk). But
  round 9 showed both routes to proving the Successor Claim itself stall: (a)
  Critical Prime Dichotomy applied to a hypothetical failing occurrence gives no
  traction, and (b) applying Free Facts to two consecutive same-type occurrences
  is a tautology — certified as the **Same-Type Free Facts Vacuity Lemma**
  (`lemmas/same-type-free-facts-vacuity.md`): any two indices `n,n'` with
  `ρ(n)=ρ(n')=A'` automatically share every prime of `A'` itself, which is
  already inside `S₀` and carries zero outside-core information. So the "edge"
  of the walk (what forces `g_{n_{j+1}}` to relate to `g_{n_j}`) is provably
  uninformative via the only tool (Free Facts) that could link two occurrences.

- **Round 10's Growing-Constraint Obstruction**
  (`approaches/greedy-exchange-cost-potential.md`, Step on the "Escape-Budget"
  attack on the Successor Claim): even granting the Successor Claim's premise
  is true (checked concretely), the illegality-witness data needed to force the
  transition is not anchored to a single fixed index (unlike Confined-GCD's
  fixed `a_{n_B}`) — it ranges over an UNBOUNDEDLY GROWING pool of intermediate
  indices as `j` grows. This is the graph-theoretic content of "the transition
  function cannot be built by construction to be identity-preserving": doing so
  would require reading off information from an ever-larger, not-fixed set of
  earlier terms, i.e. the process is not finite-memory in any exact sense at the
  level needed. The same round also flags **Return-Time Boundedness** (are the
  gaps between consecutive `A'`-occurrences even uniformly bounded?) as
  independently open and empirically NOT obviously true (a_1=4807: max gap grew
  503→670 as the sampled range extended from N=4000 to N=6000, not stabilizing)
  — so even the walk's "clock" (how many steps between edges) may be unbounded,
  a second obstruction to any clean finite-automaton picture.

- **Round 10's Sandwich Genericity / Escape-Cost Vacuity Theorem**
  (`lemmas/sandwich-genericity-theorem.md`): any state or transition rule built
  only from the certified magnitude/index sandwich `n-m ≤ a_n-a_m ≤ (n-m)a_1` is
  provably "class-blind" — identical for every pair of indices regardless of
  type or divisor class. This rules out any BOUNDED-memory/local-window
  transition rule (the natural fallback once "transition determined by current
  state alone" fails) from ever being class-discriminating, closing off the
  most obvious rescue of the automaton idea.

## 3. New computational experiment this round
Built the actual walk for a genuine `|F''|≥2` rogue pair (the only one found
with the property across all seeds any round has tested): `a_1 = 11305`,
`S₀={2,3,5,7,13,17,19,23,29,37,43,101}`, rogue pair `A'={2,5}` vs `B'={3,7}`,
`n_A=7, n_B=4` (direction-swapped: earliest witness order gives `n_B` the later
one used as fixed anchor), `F'={11}`, `F''={11,103}`, `b=1133=11·103`, canonical
prime `q*=11`. Extended the search from the previously-reported window (N≤3000,
~29–92 occurrences) out to **N=8000** using a from-scratch, independent
simulation (plain-integer greedy generation, not reusing any builder's code):

- 79 `A'`-occurrences past `n_B`, spanning raw index up to `n=7457`.
- `g_n` sequence: 77 occurrences at state `11`, exactly **2** excursions to state
  `1133` (at occurrence-positions 15 and 73, raw indices `n=1552` and `n=7457`),
  **zero** visits to the one "bad" (non-`q*`-divisible) reachable state `103`
  (`Div(1133)\{1\} \ {q*-multiples} = {103}`).
- This is a 4th independent confirmation of zero FAH exceptions for this seed
  (matching round 9's builder, round 9's reviewer, and round 9's outline-reviewer
  numbers), now at roughly 4× the previously-tested range.
- The two excursions to the non-trivial-but-still-good state `1133` occur at
  occurrence-positions 15 and 73 — no arithmetic relationship found between them
  (not a multiple of any obvious period; `73-15=58` does not divide or relate
  cleanly to `L=∏S₀` or any other certified quantity checked). This is consistent
  with — and does not contradict — the Growing-Constraint Obstruction's
  diagnosis that no small fixed-memory rule governs these transitions: if a
  bounded-memory automaton were secretly driving the walk, one would expect the
  excursion positions to show some periodic or locally-triggered structure,
  which was not found in this data (a negative/exploratory observation, not a
  proof of absence of structure — the sample is too small to be conclusive on
  its own, but it adds a data point against the automaton-with-small-memory
  hypothesis rather than for it).

## 4. Crux corpus check
Searched `past_crux_moves_database.json` (all domains) for automaton /
eventually-periodic-walk / graph-walk techniques. Found a real and relevant
cluster (`aimo-0514`, `aimo-0678`, and others): "a deterministic process is
reversible ⟹ its state graph is a union of cycles ⟹ purely periodic, not merely
eventually periodic" and "reduce a coupled recurrence's second coordinate modulo
the lcm of the first coordinate's attainable values, turning the pair into a
deterministic map on a finite set" (`aimo-0678`). **The disanalogy that matters:**
every one of these techniques applies to a problem where the update rule is
already an EXPLICIT CLOSED FORMULA (`b_{n+1} = f(a_n,b_n)` for a concrete `f`),
so reducing a bounded coordinate mod a fixed modulus turns the formula itself
into a finite-state deterministic map — determinism is free, supplied by the
problem statement. In IMO-2026-06, the update rule is not a closed formula: `a_n`
is defined by a MINIMALITY condition over legality against the ENTIRE prior
history (`a_{n+1}` = smallest integer `> a_n` with `gcd(a_{n+1},a_i)>1 ∀ i≤n`).
There is no bounded coordinate whose reduction turns this into an explicit
formula — the Growing-Constraint Obstruction (§2 above) is precisely the
statement that no such bounded reduction is currently derivable, and the S-
sufficiency⟺(†) theorem shows that ASSUMING one exists is exactly assuming what
FAH needs. So the corpus's automaton/cycle techniques are the right template in
form, but their determinism premise is unavailable here without first proving
(†) — matching, from a fourth angle, the diagnosis every other mechanism has
independently reached.

## 5. Verdict: promising-looking encoding, confirmed dead end for THIS purpose
- The divisor-class state space is real, clean, and already certified
  (Confined-GCD Lemma) — no new content to add there.
- The "transition built to be identity-preserving by construction" idea is not
  achievable: attempting to build it either (a) collapses to restating (†)
  itself (round 5's equivalence, for the S₀-signature version), or (b) is
  exactly the Successor Claim / one-step absorption property, already reduced
  to a certified conditional lemma and already shown to stall on both available
  proof routes (round 9), with the stall itself explained by an unbounded
  witness-pool obstruction (round 10) plus a proof that no bounded/local
  transition rule can be class-discriminating (round 10's Sandwich Genericity
  Theorem).
- New computation (a_1=11305 out to N=8000, 79 occurrences) adds a 4th
  independent zero-exception confirmation and mild further evidence against a
  small-memory automaton structure (no periodicity found in the 2 excursion
  positions), but does not change the mechanism-level conclusion.
- Crux corpus techniques for this pattern (bijection/reversibility ⟹ periodic
  cycles) all presuppose an explicit closed-form update rule, which this
  problem's minimality-based definition does not supply — a structural
  disanalogy, not a gap in search effort.

**Recommendation to the outliner:** do not open "automaton / graph-walk" as a
13th distinct mechanism — it is isomorphic to mechanisms 2 (Successor
Claim / one-step transport, round 9) and, at the S₀-signature level, to the
round-5 finding, both already retired. If a future round wants graph/automaton
language for exposition it may reuse the Confined-GCD alphabet, but the actual
missing ingredient is unchanged from Lemma I's original diagnosis (round 6),
reconfirmed independently for the 4th time this round: a genuinely new source of
IDENTITY-level, cross-occurrence information — not obtainable by any
composition of Free Facts, the gap lemmas, pigeonhole, or Confined-GCD — that
none of the twelve killed mechanisms nor this automaton reframing supplies.

## Files consulted
- `results/imo-2026-06/current.md` (rounds 1–10 history)
- `results/imo-2026-06/approaches/reversible-transition-map.md`
- `results/imo-2026-06/approaches/cofinite-window-capacity-bound.md`
- `results/imo-2026-06/approaches/greedy-exchange-cost-potential.md` (round 9–10 sections)
- `results/imo-2026-06/lemmas/confined-gcd-lemma.md`
- `results/imo-2026-06/lemmas/successor-transport-reduction-lemma.md`
- `results/imo-2026-06/lemmas/same-type-free-facts-vacuity.md`
- `results/imo-2026-06/lemmas/sandwich-genericity-theorem.md` (referenced via current.md's round-10 summary and `escape-cost-vacuity.md`)
- `past_crux_moves_database.json`, `crux_moves_documentation.md`
- Fresh Python simulation: `/tmp/round-11/sim3.py` (independent from-scratch
  greedy-sequence generator, `math.gcd`-based; used for the a_1=11305, N=8000
  divisor-class walk experiment in §3)
