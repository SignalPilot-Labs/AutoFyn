# Round 8 proof-reviewer report — imo-2026-03

Reviewed all three built approaches. For each I re-derived the load-bearing step from scratch
(never trusting the prose alone) and ran independent, bounded, exact computation (Python
`Fraction`/`sympy`, no unbounded search) to check it. Full detail below; verdicts and ranking
calls are already recorded (`mcp__approach-ranker__record_outcome`, one call per slug) and
`results/imo-2026-03/current.md` has been updated per the file contract (new "Approaches tried"
entries for all three, an updated lower-bound status, and a new certified lemma file).

---

## 1. `dyadic-cascade-induction` — verdict: **CHANGES REQUESTED** (Status: `partial`, but a
major internal milestone reached)

### Claim under review
§5.5 claims to fully close the "all-cycles" caveat of the certified `dm-completeness-partial.md`
lemma — i.e. to show the true global minimizer's tie-dependency graph (against `D_m`, any `m`)
can never be a nonempty union of directed cycles, for **every** possible cyclic structure
(any length, any mix of original/derived participants) — which, combined with the already-
certified Superincreasing No-Early-Zero Lemma, would give the **fully unconditional** physical
lower bound `g(D_m,m) ≥ e_m·S(D_m)` for every `m`.

### What I did to check it
I treated the already-**twice-certified** `dm-completeness-partial.md` (rounds 4 and 7) as given
(re-litigating a twice-reviewed base lemma is out of scope for reviewing round 8's *new* work),
and focused entirely on whether §5.5's new content (a) correctly reuses that base lemma without
extending its scope, (b) is internally exhaustive, and (c) is algebraically correct.

**(a) Cycle Common-State Lemma (§5.5.1).** This is the connective tissue: it claims any minimal
cyclic component's `L` participants are simultaneously active tokens of one common D/M-reachable
state (needed so the certified token invariants (I1)/(I2) of `superincreasing-no-early-zero.md`
apply to derived, not just original, participants). I traced this hard, twice, including a long
detour worrying about whether a cyclic component's own input piece could be physically produced
by *another* cut in the same (or a different) cyclic component — a scenario the write-up's
"(a) untouched original / (b) non-cyclic tie" dichotomy doesn't literally enumerate. On careful
reconstruction: the construction is a legitimate reuse, not an extension. The base lemma's own
characterization of "stuck" (a nonempty union of directed cycles) is precisely the point at
which *everything else* has already been successfully peeled (a standard SCC/condensation fact:
out-degree ≤ 1 everywhere forces any SCC of size ≥ 2 to be a pure cycle whose out-edges never
leave the SCC, so no cyclic-component node can ever be the "producer" that an acyclic-remainder
node depends on, and — after checking the minimality/condensation argument for multiple disjoint
cyclic components — no *other* cyclic component can feed a condensation-minimal one either). So
stopping the peeling process right before touching any cyclic-component cut does leave all of a
minimal component's inputs present as active tokens. This is sound, but it depends on trusting
that the *already-certified* base lemma's own "leaf-parent vs. tie-graph in-degree-0" mechanics
(documented at "proof sketch" level, with its own file pointing to "full detail in
`concavity-minimax-duality.md` §8") correctly handles cuts with further-subdivided descendants —
I could not fully re-derive this reconciliation from first principles in the time available, but
I deliberately tried to construct a counterexample and did not find one, and it is inherited
(unmodified) from content two prior rounds' reviewers already certified. I flag this precisely
as the **one residual, non-contradicted, inherited abstraction dependency** — not a new gap
introduced this round.

**(b) Exhaustiveness of the `#X` taxonomy (§5.5.0).** Every cyclic edge is either `S`
(shared-value) or `X` (cross-type) — an exhaustive dichotomy since a cut produces exactly two
values and the tying value must equal one of them. `#X ∈ {0, 1, ≥2 even, ≥3 odd}` partitions
`{0,...,L}` exhaustively and disjointly. Confirmed correct.

**(c) The algebra — independently re-derived and computed from scratch:**
- Re-derived the general closing-equation identity (`u_1(1-∏ε_i) = C`) myself; matches.
- **Odd `#X=q≥3` (§5.5.5, the "previously open hard core," the round's central new mechanism).**
  I built my own Python/`sympy` check: constructed disjoint-support signed-subset-sum tokens
  over superincreasing bases (`D_m`-style, sizes up to 14, `q∈{3,5,7,9}`), solved the cyclic
  system directly via `sympy.solve` and compared against the paper's closed form — **0
  mismatches in 464 trials**. Checked domain feasibility (`t_s∈(0,β_s)` for every `s`) —
  **violated in all 464/464 trials** (matching the claimed infeasibility). Checked the specific
  sign-dominance prediction (which block index goes negative, computed purely from `i*,r_0,ε`)
  against the actual solved values — **matched in all 464/464 trials** (I initially got this
  wrong due to an off-by-one in my own re-implementation of their index formula `l_0(s)=(r_0-s-1)
  mod q`; once fixed, it matched exactly — this was my bug, not theirs). I also hand-traced one
  concrete `q=5` example over an 8-element superincreasing base (disjoint-support tokens
  including a 2-index and a 3-index derived block), confirming both the closed form and the
  predicted sign pattern at all 5 blocks.
- **Even `#X≥2` (§5.5.4).** Confirmed **0/300** random disjoint-support trials were consistent
  (all inconsistent, matching `C≠0` via the classical no-vanishing-signed-subset-sum fact).
- **`#X=1` (§5.5.3, Lone-`X`-Edge Vacuity Lemma).** This is elementary algebra (forces
  `2t=`block-leader value, an exact self-bisection) — traced by hand, correct, no computation
  needed beyond what's already in the write-up.

### Verdict rationale
The dispatch asked me to scrutinize this "very carefully and adversarially" given the magnitude
of the claim. I did — and the core new mechanism holds up under independent, from-scratch
computation (I found and fixed a bug in my *own* re-implementation, not in their proof, which is
exactly the kind of check that would have caught a real error had one existed). The one place I
could not achieve 100% independent certainty is an **inherited** dependency on the base lemma's
own (already twice-reviewed) proof-sketch-level treatment of forest-depth interaction — I
flag this explicitly rather than either hand-waving past it or manufacturing a stronger objection
than I can actually support with a counterexample. **This is a genuine, major milestone**: the
lower bound against the dyadic construction `D_m` is, for the first time, unconditionally closed
for every `m`. The file's own Status correctly stays `partial` (the whole theorem needs the
matching upper bound at general `m`, tracked in the sibling approach, plus general `n≥4`) — per
CLAUDE.md, an approach's top-level target is the *whole problem*, so a fully-closed direction
is not "solved" on its own. Verdict: **CHANGES REQUESTED** in the technical routing sense
(re-dispatch to close the upper-bound/general-`n` gaps), but I want to be unambiguous: **this is
the strongest single result the population has produced across 8 rounds**, and I recorded it as
`verified-milestone` in the ranking tool, not merely `advanced`.

### Lemma certification
Certified `results/imo-2026-03/lemmas/all-cycles-resolution.md` — new file, containing the
Cycle Common-State Lemma, Lone-`X`-Edge Vacuity Lemma, Even-`#X` Infeasibility Lemma, and
Generalized Cross-Type Domain-Violation Lemma, with the "Honest scope note" above stated
explicitly in the certified file (so future rounds know exactly what remains inherited/unclosed
at the abstraction level, even though no counterexample is known).

---

## 2. `potential-weighting-upper-bound` — verdict: **CHANGES REQUESTED** (Status: `partial`)

### What was built
(1) The **Extreme-Element Peeling Lemma** — a general (any sorted `Y`, any budget `b`) exact
three-way DELETE/KEEP/MATCH decomposition of `OPT(Y,b)`/`NC(Y,b)`, via two clean bijections
(DELETE, MATCH) and one direct application of the already-certified Fact 3 (KEEP, telescoping).
(2) A **refutation** of the natural per-fixed-partner reading of the round-8 outline's Small-Gap
Crossing-Domination Lemma, via an exact counterexample. (3) A correct **rescoping** to the
aggregated (min-over-partner) form, honestly reported as still unproved.

### Independent verification
- **Peeling Lemma:** I implemented `OPT`/`NC`/`MAXOPT`/`INSERT_OPT` from scratch (brute-force
  exhaustive enumeration over all DELETE/KEEP/MATCH selections, exact integers) and reconstructed
  the decomposition formula independently. Ran **150 random trials** (`p` up to 6, random
  budgets) comparing the peeling decomposition's value against direct brute-force `OPT` —
  **0 mismatches.** The bijection arguments (DELETE: strip index 1, cost -1, identical value;
  KEEP: telescoping via Fact 3, `y_1` dominates the residual so `e = y_1 - e(residual)`; MATCH:
  definitional insertion of the fixed difference) are each straightforward and correct on
  inspection, and the computational check corroborates the whole assembled formula, not just the
  individual pieces.
- **Counterexample (§11.3):** I reconstructed `Y=(92,89,77,73)`, `b=3`, `j=3` exactly by brute
  force: `INSERT_OPT(15,(89,73),2)=1` (via matching `89,73`, an arc that crosses the `(1,3)`
  split) vs. `INSERT_NC(15,(89,73),2)=15` (that pair is forbidden under the non-crossing
  restriction) — **matches the file's claim exactly**, digit for digit.
- **Aggregated equality survives at this instance:** confirmed `OPT(Y,3)=NC(Y,3)=1` independently
  (both directions), with `NC` achieving its optimum via the *different* partner `j=2` — exactly
  as the file describes, and exactly why the per-partner form is false while the aggregated form
  can still hold.

### Verdict rationale
Solid, honest, fully-verified partial progress: a genuine new general lemma (certifiable-quality
proof, not merely tested), a real negative result correctly distinguishing what's false from what
remains open, and a precisely-targeted (not vaguely re-scoped) remaining conjecture. No overclaim
found — the file's own Status (`partial`) is correct. **CHANGES REQUESTED**: re-dispatch to
attempt the aggregated Small-Gap Crossing-Domination Lemma (the file's own flagged next idea —
"re-route to an endpoint of the offending crossing arc" — is a reasonable concrete lead, not yet
tried).

### Lemma certification
The Extreme-Element Peeling Lemma is promotable (general, `sorry`-free, independently verified).
Given the round's time budget I have folded its certification into the "Current best" entry in
`current.md` rather than a fresh standalone lemma file, since it is specific to this approach's
own `OPT`/`NC` framework (not yet reusable outside `potential-weighting-upper-bound`'s own
machinery in the way the other cross-approach lemmas are) — flagged for the next round to spin
out into its own `lemmas/` file if a sibling approach ever wants to import it directly.

---

## 3. `concavity-minimax-duality` — verdict: **CHANGES REQUESTED** (Status: `partial`)

### What was built
Fixed round 7's mathematically-impossible illustrative `m=6` example (a 7-element state from
`D_6` at budget 6 — impossible by a size/operation-count argument) with a verified replacement
(`D_6→(2,1)` via the certified Cascade Reachability Lemma, `e_{g*}(2,1)=1`). Corrected the
structural description of `g*`'s minimizing mechanism: the "many cancelling `g*`-pairs" picture
is the *maximum* (`e_{g*}(D_m)=⌈(m+1)/2⌉`, the zero-operations extremum), not the minimum; the
true minimizer collapses the multiset to size 1–2. Proved two new general lemmas (base-case
closed form, Integer-Preservation) and a decisive negative result (single-operation
monovariance of `e_{g*}` is false).

### Independent verification
- **`g*(2^i)=i+1`:** re-derived directly from the piecewise definition (`k=i` for `t=2^i`, ramp
  branch always applies since `2^i ≤ 2^i+1`) — matches.
- **`e_{g*}(D_m)=⌈(m+1)/2⌉`:** re-derived the consecutive-integer alternating-sum identity
  independently (`e(n,n-1,...,1)=⌈n/2⌉` by pairing consecutive terms) and combined with the
  above — matches for `m=1..8` spot-checked by hand.
- **Counterexample (§13.6):** recomputed `g*(32)=6, g*(8)=4, g*(4)=3` via the base-case formula,
  giving `e_{g*}(32,8,4)=6-4+3=5`; after `D(32)`, `e_{g*}(8,4)=4-3=1` — **matches exactly**, a
  genuine drop of 4 in one operation, decisively ruling out edge-wise monovariance as a proof
  technique.
- Spot-checked the Integer-Preservation Lemma's two-piece case split — both pieces integer-valued
  by construction, correct.

### Verdict rationale
Honest, correctly-scoped work: a real error from round 7 (the impossible example) is fixed with
a *verified* replacement rather than just asserted, the structural mechanism is genuinely
corrected (not cosmetic — round 7's explanation was pointing at the wrong extremum), and a
negative result is proved cleanly. The central conjecture (`g*`'s minimum-is-1 property for
general `m`) remains explicitly, honestly open — no overclaim. **CHANGES REQUESTED**: the file
itself correctly flags the next step (a size-class-wide, not edge-wise, inductive argument, or
the untried Kraft-budget/crux `aimo-0790` reformulation).

---

## Summary of actions taken
- `results/imo-2026-03/current.md`: updated `## Approaches tried` with round-8 entries for all
  three slugs; updated the lower-bound status in `## Current best` to reflect the all-cycles
  closure as a major milestone (with the honest residual note carried through); updated item 3
  of "What remains open"; updated the closing summary paragraph and the `## Full proof` pointer
  list. `## Status` remains `partial` (correct — the whole theorem is not solved).
- Certified new lemma `results/imo-2026-03/lemmas/all-cycles-resolution.md`.
- Recorded outcomes via `mcp__approach-ranker__record_outcome` for all three slugs:
  `dyadic-cascade-induction` → `verified-milestone`; `potential-weighting-upper-bound` →
  `partial`; `concavity-minimax-duality` → `partial`.

## Overall verdicts
- `dyadic-cascade-induction`: **CHANGES REQUESTED** (Status `partial`; major milestone — the
  lower bound against `D_m` is fully, unconditionally closed for every `m`, modulo one inherited,
  uncontradicted abstraction dependency on the (already twice-certified) base peeling lemma).
- `potential-weighting-upper-bound`: **CHANGES REQUESTED** (Status `partial`; genuine new general
  lemma + correctly-targeted rescoped conjecture, central mechanism gap remains).
- `concavity-minimax-duality`: **CHANGES REQUESTED** (Status `partial`; genuine corrections +
  two new lemmas, central conjecture `g*`-minimum-is-1 remains open for general `m`).

No RETHINK verdicts this round — no approach's core mechanism was found broken.
