## imo-2026-03 (lens: Route 1 primal — Gap A′ non-isolated cycles, via geometric/laminar structure)

### Headline finding (verified by direct computation, not just theory)
The dispatch's suggested lever — "laminar/interval-nesting geometry of the actual stick
subdivision forbids non-isolated cyclic configurations that pure algebra allows" — **does NOT
exist as an extra constraint**, and chasing it is a likely dead end. Re-reading
`self-similar-recursion.md` §1: the domain `K` is explicitly established (already certified,
round 1) to be the *full* product of simplices `∏_k Δ_k` — "every point of `K` is a legal
refinement." `f` and `Φ` depend only on the **multiset** of sub-piece lengths, never on which
physical interval of the stick a sub-piece occupies. So there is no hidden "physical adjacency /
laminar nesting" fact beyond the algebraic system `(★)` `Uw=b` plus positivity — the 479
counterexamples the round-6 explorer built (abstract positive solutions on non-isolated cyclic
supports) genuinely ARE realizable as points of `K`. Do not resurrect a "geometric position on
the stick" argument; it was already fully used to establish that `K` is unconstrained.

### What I actually found: the even/odd cases split much more sharply than the write-up states
Re-examining Lemma CC's even-cycle kernel-witness proof mechanically (not the abstract "isolated"
framing) shows it is **already immune to most of the "non-isolated" shapes** listed in Gap A′,
and only fails on a narrow residual. I verified all of the following numerically (`numpy`/`sympy`,
small explicit incidence matrices, see commands below — all confirmed exactly as stated):

- **Off-cycle piece attachment does NOT break the even kernel witness.** If a cycle piece
  `2^{a_i}` has an *extra* edge to an off-cycle component `Q'` (private singleton or shared with
  other pieces), the alternating vector `d` (±1 on the cycle's own components `Q_1,…,Q_r`, `0`
  elsewhere) still satisfies `Ud=0` globally: the extra row/column contributes `μ·d(Q')=μ·0=0`.
  Verified: 4-cycle `P1..P4/Q1..Q4` plus off-cycle piece `P5` attached to `Q1` → `Ud=0` exactly.
  So the "off-cycle degree-≥3 **piece**" case is a FALSE alarm for the even sub-case — Lemma CC
  already covers it, contrary to the write-up's residual list.
- **Uniform multiplicity scaling along the cycle does NOT break it either.** Cycle edges all of
  multiplicity `m` (any `m≥1`) still give `Ud=0` (the `m` factors out of the alternating
  cancellation). Verified `m=2` on a 4-cycle: `Ud=0` exactly.
- **What DOES break the even kernel witness (genuine residual), verified:**
  1. A genuine **chord** — an extra edge between a cycle piece and a *non-adjacent* cycle
     component (or vice versa) — makes `U` full column rank (`Ud=[−1,0,0,0]≠0`; rank jumps to 4
     on a 4×4 system that would otherwise be rank-deficient). This is the same
     `[[1,2],[2,1]]`-type obstruction already flagged in the Rules (det `±3`, invertible, still
     not a forest).
  2. A **cycle component** (not a piece) touching an **off-cycle piece** (component degree ≥3)
     — this DOES break `Ud=0` at that off-cycle piece's row. This is the real "off-cycle
     attachment" danger — but it attaches to a *component*, not a piece as the write-up's residual
     list implies.
  3. **Non-uniform** multiplicity along the cycle (e.g. one edge mult 2, rest mult 1) — full rank,
     kernel trivial, genuine residual (same flavor as the chord case).
  So: **Gap A′ even-cycle residual narrows to exactly {chord} ∪ {cycle-COMPONENT off-cycle
  degree≥3} ∪ {non-uniform cycle multiplicity}** — strictly smaller than "any non-isolated shape."
  This is a concrete, provable narrowing the outliner/builder can use directly (all three
  surviving cases are exactly the ones where `U` restricted to the cycle's own rows/columns gains
  full column rank — i.e. they are exactly where the previously-known `det=±3` style
  non-forest-but-full-rank obstruction lives, so they may be attackable by the SAME machinery
  already flagged for that obstruction, not by new geometry).
- **Sharp asymmetry: the odd case does NOT get the same free extension.** For odd cycles, an
  off-cycle-piece attachment reduces the *effective* budget at that piece (`b_i → b_i − e_i` for
  off-cycle mass `e_i≥0`), and I confirmed numerically this DOES defeat the superincreasing
  argument: isolated `b=(1,2,4)` gives `u=(1.5,−0.5,2.5)` (correctly excluded, one negative), but
  reducing only the largest budget to `b=(1,2,2.5)` (simulating `e=1.5` of off-cycle mass stolen
  from the piece carrying budget 4) gives `u=(0.75,0.25,1.75)` — **all positive**, a genuine
  algebraic escape. So odd non-isolated cycles via off-cycle piece attachment are a real open gap,
  not closable by extending Lemma CC's argument; consistent with (and now more precisely
  localized than) round 6's 479-counterexample finding.

### Distinct openings
1. **Narrowed even-case residual (chord / component-off-cycle-attachment / non-uniform mult) —
   attack via the det/rank machinery already flagged for `[[1,2],[2,1]]`,** since all three
   surviving even shapes are precisely where the local cycle sub-system gains full column rank.
   This is a MUCH smaller target than "any non-isolated cycle" and should be handed to the builder
   as the concrete next step for the even sub-case.
2. **Odd non-isolated cycles via off-cycle piece attachment need a genuinely different (probably
   minimality-based, not pure-algebra) argument** — confirmed algebraically escapable. The
   plausible lever: such a configuration, even if algebraically feasible, may never actually be
   the argmin of `f` (minimality is a strictly stronger condition than "solves `(★)` with positive
   values") — i.e. check whether the specific escaping solutions are ever Φ-maximal minimizers of
   the REAL functional `f` over `K`, not just feasible points of the abstract linear system. This
   is a different question from what round 6 tested (it tested only algebraic feasibility of the
   abstract system, not whether it's an actual critical point of `f`).
3. **A crux-corpus technique (aimo-0913, see below) is structurally close but doesn't directly
   transfer** — worth noting as inspiration, not a working route (see Analogous problems).
4. **Gap B (μ=3 even-block leaf):** I did not find new progress this round (out of primary lens
   scope); the existing write-up's finding stands — no local move excludes it, degenerate-Φ-
   domination (Lemma BD) is the right target but unconstructed. Flagging one untested idea: since
   Gap B's leaf has value `v=2^k/3`, a component of even size shared with another piece, the
   SAME "which shapes preserve `Ud=0`" computational method used above for Gap A could be applied
   to check whether a `μ=3` leaf can coexist with `ker U=0` at all — i.e. treat it as a graph-rank
   question rather than a variational one. Not attempted this round; a cheap next check.

### Candidate technique(s)
- Rank/kernel computation on small explicit incidence matrices (as above) to map exactly which
  non-isolated shapes survive vs. die — already partly done, should be extended to a general proof
  (not just examples) for the "chord / component-off-cycle / non-uniform-mult" trio.
- For odd case: shift from "is the abstract system feasible" to "is the feasible point actually
  Φ-maximal / a genuine local minimum of `f`" — a variational (not purely linear-algebraic)
  argument, in the spirit of Lemma S-core's use of `Φ`-maximality (feasible-shift ⇒ trivial
  kernel) but applied along directions that move mass between a cycle component and its off-cycle
  attachment.

### Cheap-kill candidates
- For the narrowed even residual: check computationally whether "chord ⇒ full column rank" is a
  DEFINITIONAL/general fact (not just the 4-node example) — likely yes, since a chord in a
  bipartite graph turns a cycle (rank deficiency `1`) into two cycles glued (rank deficiency `0`
  generically) — worth a clean general lemma statement and proof (should be short: a chord adds a
  θ-graph, and matrix-tree-style arguments on θ-graphs typically give full rank except in special
  ratio cases — check whether the RHS-being-powers-of-2 can still force positivity failure even
  when `ker=0`, since `ker=0` alone does NOT give a forest, as already known).
- For odd off-cycle-piece attachment: since it genuinely escapes algebraically, don't spend more
  budget trying to force a contradiction from `(★)` alone; pivot to minimality/Φ-maximality.

### Knowledge-base entries to use
- No new named `knowledge_base.md` entry surfaced beyond what's already in use (rank/kernel
  argument entry noted at line ~42-46 of `knowledge_base.md`, "Rank / image / kernel: det=0 iff
  nontrivial kernel — argue via shared kernel" — already the exact tool self-similar-recursion
  uses for Lemma S-core / Lemma CC).

### Analogous past problems (cruxes)
- **aimo-0913** (number_theory / graph-theory-and-connectivity? — actually filed under a Fibonacci
  differences problem, IMO-style): builds a graph on set elements with edges labeled by DISTINCT
  Fibonacci numbers (a superincreasing-like sequence) and proves acyclicity via triangle
  inequality: "the longest edge in any cycle exceeds the sum of the shorter distinct edges,
  contradiction." This is structurally the SAME idea as Lemma CC's odd-cycle superincreasing
  argument (distinct powers of 2 instead of alternate Fibonacci sums), but it is an **equality**
  argument (`x−y` differences, triangle inequality on an actual metric) not directly transferable
  to our **sum**-type cyclic system `u_{i-1}+u_i=b_i`. I checked whether its triangle-inequality
  style could rescue the odd non-isolated case (inequality-relaxed budgets) — it does not: the
  relaxation in our problem makes budgets SMALLER, which is the wrong direction for a
  longest-edge-exceeds-sum contradiction (that argument needs the target quantity to be forced
  larger than a sum of others, but our escape shows a reduced target can still be satisfied). So:
  cite as a close structural cousin / sanity check that Lemma CC's own technique is the "right
  kind" of argument for superincreasing RHS, but it does not itself close the odd non-isolated
  residual.
- No other genuinely analogous corpus entries found under `graph-theory-and-connectivity` for this
  specific "cyclic sum system with power-of-two RHS" shape; the corpus skews toward difference
  systems / spanning-tree edge counts, not sum-cyclic systems.

### Prior progress
As recorded in `current.md`/`self-similar-recursion.md`: upper bound fully certified; lower bound
reduced to (LBL) → Φ-max minimizer integrality → Gap A′ (non-isolated cycles) + Gap B (μ=3 leaf).
Lemma CC (certified) closes ALL isolated cycles. This round's contribution narrows Gap A′'s even
sub-case to a strictly smaller residual (chord / component-off-cycle-attachment / non-uniform
multiplicity) and sharply distinguishes it from the odd sub-case (off-cycle piece attachment is a
genuine open escape for odd cycles, confirmed feasible by explicit numeric counterexample).

### Dead ends (do not retry)
- Laminar/interval-position geometry of the stick as an extra constraint beyond `(★)` — does not
  exist; `K` is already known (round 1, certified) to be the unconstrained product of simplices.
- Extending Lemma CC's odd-cycle superincreasing bound to off-cycle-piece-attached odd cycles by
  using the REDUCED (not full power-of-2) budgets — fails, confirmed by explicit numeric
  counterexample `b=(1,2,2.5)` giving all-positive `u=(0.75,0.25,1.75)`.
- aimo-0913-style triangle-inequality direct transplant to the odd non-isolated residual — wrong
  direction of inequality, does not produce a contradiction.
- (Carried from round 6, still valid) full-cycle superincreasing telescoping with uncontrolled
  off-cycle signs; Gap D as a universal S-core property; λ₀-parity Positivity mechanism.

### Small-case / intuition notes (labeled conjecture where not proved)
- CONJECTURE (numerically consistent, not proved): the true even-case Gap A′ residual (chord /
  component-off-cycle / non-uniform-mult) never actually arises at a genuine Φ-maximal minimizer
  of `f`, i.e. minimality itself (not just the algebra) kills it — this is untested this round but
  is the natural next computational experiment: brute-force small `n` (3–4) refinements, find
  Φ-max ties, and check whether any exhibits one of these three narrow shapes.
- CONFIRMED (not conjecture, direct computation): even Lemma-CC-style kernel witnesses survive
  under uniform-multiplicity scaling and under off-cycle piece attachments; they die under chords,
  component-level off-cycle attachments, and non-uniform multiplicity.
- CONFIRMED (not conjecture): odd cyclic systems with off-cycle piece attachment can be fully
  positive (explicit instance above) — the odd sub-case genuinely needs a non-algebraic
  (minimality/variational) argument, it is not just an unfound clever telescoping.
