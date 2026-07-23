## imo-2026-03 (D/M-completeness "all-cycles" gap — cycle-elimination lens)

### 0. Context recap (verified against the files, not re-derived from scratch)
The single remaining obstruction to promoting `lemmas/superincreasing-no-early-zero.md`'s
D/M-*sequence* lower bound to the TRUE physical lower bound for `D_m` is
`lemmas/dm-completeness-partial.md`'s "all-cycles" case: a global minimizer whose tie-dependency
graph (out-degree ≤1 per genuine cut, edge `c→c'` iff `c` ties to a value produced by `c'`) is a
nonempty union of directed cycles. Round 7 (`lemmas/shallow-cycle-resolution.md`) closed this for
every **uniform, all-original** cycle (Shared-Value Cycle-Breaking Lemma for any `L≥2` shared-value
type; Cross-Type Cycle Infeasibility Lemma for any `L≥3` pure cross-type). Two residuals remain,
as stated in the dispatch: (a) any cycle with ≥1 derived participant, (b) any cycle mixing
shared-value and cross-type edges among all-original participants.

### 1. Distinct openings found this round

**Opening 1 (the main finding): a "parity of cross-type edges" dichotomy that subsumes and
generalizes BOTH existing lemmas at once, and appears to close gap (b) outright — strongly
supported, not proved.**

Model a general cycle of length `L` on pieces `b_1,\dots,b_L` (cyclic order) where each edge
`i\to i+1` is one of two kinds: **S** (`u_i=u_{i+1}`, a shared-value tie) or **X** (`u_i+u_{i+1}
=b_{i+1}`, a cross-type/chain tie — the shape used in the existing Cross-Type Lemma). This is
strictly more general than "uniform shared" (`L` S-edges) or "uniform cross" (`L` X-edges): it
lets several *separate* shared-value blocks (each its own free parameter) alternate with chain
segments around one cycle — exactly the kind of "mixed" cycle the residual (b) describes, and
more general than what the round-7 reviewer's exhaustive search checked by hand.

Composing the `L` affine relations once around the loop and solving for `u_1` gives a single
closing scalar equation whose sign is `(-1)^{\#X}` (each S-edge composes with sign `+1`, each
X-edge with sign `-1`), and whose "offset" is *always* a plain **signed subset sum, with
coefficients exactly `\pm1`, of the pieces `b_j` that are the immediate successor of an X-edge**
(never any other piece, never a coefficient other than `\pm1`) — verified symbolically with
generic symbols (`sympy`, `linsolve` on symbolic `b_1,\dots,b_6`, four hand-picked mixed
patterns of `L=6`, see below). Consequences, checked both symbolically (generic `b`'s) and
numerically (2200+ trials, exact `Fraction`/`sympy`, `D_3..D_7`, `L=3..7`, every `\#X` from 0 to
`L`, zero exceptions in every category):

- `\#X=0` (pure shared): the existing free-parameter family — Shared-Value Cycle-Breaking Lemma
  applies verbatim (never the true minimizer).
- `\#X=1`: **degenerate, not a new case.** The single X-edge forces every `u_i` in the cycle to a
  single common value `t`, PLUS the extra coincidence `2t=b_j` for the one piece `b_j` at the
  X-edge — i.e. `t` bisects one of the participating pieces. This is exactly the Vertex Lemma's
  *other* breakpoint type (self-bisection, `t=\ell/2`) rather than a tie to the guaranteed-
  untouched original — a case the existing family-(A) writeup does not spell out explicitly but
  which the cited Vertex Lemma already covers (its part (b) lists both breakpoint types). A
  self-bisection cut has out-degree 0 in the dependency graph by definition (immediately
  peelable), so this reduces to the same conclusion via a different, already-licensed exit.
- `\#X\ge2` even: the closing equation is `0 = (\text{nonempty signed subset sum, coeffs }\pm1)`
  — an outright **algebraic inconsistency** (no free parameter, no solution at all, regardless of
  minimality) whenever that signed subset sum is nonzero. For **all-original** participants this
  is exactly the **no-vanishing-signed-subset-sum fact** (Step 1 of
  `lemmas/superincreasing-no-early-zero.md`) applied to the (necessarily distinct) successor
  pieces — an **exact** fact, not a magnitude/dominance bound. Zero feasible instances in every
  symbolic and numeric trial (1880+ trials at `\#X\ge2`, all `INCONSISTENT`, matching the generic
  symbolic `EmptySet` result exactly).
- `\#X\ge3` odd: the closing equation gives a **unique**, fully determined solution for every
  `u_i` (a linear combination, coefficients `\pm1/2`, of only the X-edge-successor pieces) — no
  freedom at all, so (like the existing Cross-Type Lemma) the only question is whether this
  unique solution satisfies `u_i\in(0,b_i)` for every `i`. Zero feasible instances found in
  600+ trials; this is the direct generalization of the existing Cross-Type Cycle Infeasibility
  Lemma's dominance argument (which is the special case "all `L` edges are X"), and the same
  "relabel so the max piece anchors one edge, subtract" trick should adapt (untried in detail —
  this is exactly where a proof would need to be written, not scouted further).

**Net effect on gap (b):** the taxonomy "shared-value vs. cross-type vs. mixed" collapses to a
single integer invariant, `\#X` (number of cross-type edges) mod 2 and whether `\#X\ge2`; only
two of the four resulting buckets (`\#X=0,1`) need the *perturbation/never-a-minimizer*
argument (already have it — Vertex Lemma, general purpose); the other two (`\#X\ge2` even/odd)
are outright **infeasibility** arguments, generalizing the existing Cross-Type Lemma's algebra.
This looks like a genuinely promising, nearly-complete repair for gap (b) as a *proof template*
— but it is NOT proved (the `\#X\ge3` odd sub-case's domain-violation step was only checked
numerically/symbolically, the general "relabel + subtract" dominance argument was not carried
out by hand for the mixed case).

**Opening 2: partial transfer to derived participants (gap (a)), narrower than a full fix.**

I substituted an actual derived value into the same framework: `D_3=(8,4,2,1)`, derived piece
`b=6` (the surviving output of tying original `8` against the untouched original `2`, i.e.
`T=\{8,2\}` with signs `(+,-)`), alongside originals `4,1`. Running all `2^3=8` edge-type
patterns on `(6,4,1)` (`sympy`, exact): every `\#X\ge2` pattern is again `EmptySet`
(inconsistent) — matching the all-original prediction even with a derived participant present.
**Why this is not a coincidence:** the closing equation's "offset" is a signed subset sum over
the *original indices* underlying the X-edge-successor pieces (via the token invariant's
`(S(v),\varepsilon(v))` decomposition, certified in `lemmas/superincreasing-no-early-zero.md`);
since distinct cycle participants have pairwise-disjoint `T_i`'s (same invariant), the combined
offset is still a genuine, well-signed (no index appears with conflicting sign) nonempty signed
subset sum over *original* indices — and the **no-vanishing-signed-subset-sum fact is exact**,
with no magnitude/dominance hypothesis, so it does not care whether the pieces being summed are
"large" or "small," only that the sum is a nonempty subset with well-defined signs. This is
precisely the fact that the round-7 crude derived-participant fix did NOT need to fail on —
that fix broke because it needed the *magnitude* comparison `a_{i^*}>2\sum_{l>i^*}a_l` (a
dominance/size fact), not the *exact* non-vanishing fact. **So gap (a) may split cleanly along
the same `\#X` axis as gap (b):** the `\#X\ge2` even sub-case (outright inconsistency) plausibly
extends to derived participants via the *exact* fact alone (promising, only spot-checked once);
the `\#X\ge3` odd sub-case (unique solution, need domain violation) is exactly where the
magnitude/dominance argument is needed and is exactly where the round-7 attempt is *shown* to
fail (`a_{i^*}<2` needed, false) — so **the true, fully general hard core of the whole all-cycles
gap, across both (a) and (b), collapses to one precisely-stated question: does the unique
solution of an odd-`\#X\ge3` cyclic system (participants possibly derived) ever satisfy every
domain constraint `u_i\in(0,b_i)`?** This is one shared bottleneck, not two separate ones.

**Opening 3 (re-derivation of exhaustiveness, dispatch item 4).** Re-checked: `FINAL`'s
dependency graph can in principle be a union of *several disjoint* cycles simultaneously. This
does not add a third case: breaking (infeasibility) or de-optimizing (perturbation) any *one*
cycle, holding every cut outside that cycle fixed, already contradicts `FINAL` being a joint
minimizer (perturbation case) or its very existence (infeasibility case) — the other,
disjoint cycles are untouched by the argument and irrelevant. So single-cycle analysis, if made
exhaustive over (participant-type pattern) × (edge-type pattern), *is* exhaustive for the whole
"all-cycles" case; no additional combination (multiple simultaneous cycles, cycles of unbounded
length) needs separate handling beyond what one cycle's own case-split requires. One caveat
worth flagging to the outliner: the "shared-value edge" formalization itself (`L` cuts
independently choosing an identical value `t`, none literally "produced by" any other) is a
slightly looser notion than the strict `c\to c'` "ties to a value produced by another specific
cut" definition in `dm-completeness-partial.md` — round 7 treated it as a cycle via Lemma P's
pairing without fully justifying *which* specific cut-to-cut edges this corresponds to. This has
already passed review twice, so it is not a new gap, but the outliner should be aware it is an
assumption inherited, not re-derived, by this round's parity framework.

**Opening 4 (a finer split of the derived-participant space not yet tried).** The round-7 crude
bound treats "derived" uniformly via the worst-case bound `\sum_{l>i^*}a_l`, with no split by
*how* a participant was derived. Two structurally different sub-cases were not distinguished:
(i) a participant derived by **self-bisection** (`v=\ell/2` for some ancestor `\ell`) — a very
rigid relationship to a single ancestor, no cancellation at all; (ii) a participant derived by an
actual **tie** (`v=x-y`, a genuine signed difference, potentially over many original indices,
where cancellation is what breaks dominance). A case split on *this* axis (not on cycle length)
might isolate a tractable sub-case (self-bisection-derived participants) even within the hard
odd-`\#X` bucket, since such a participant's value is pinned to exactly `\ell/2` rather than an
arbitrary signed sum. Untried; flagging as an opening, not a result.

### 2. Candidate technique(s)
- The existing **Vertex Lemma** (`lemmas/vertex-lemma.md`) — already sufficient for the `\#X\in
  \{0,1\}` buckets, including with derived participants (it never assumed originality).
- A generalized **sum-and-dominance / non-vanishing-subset-sum** argument (extending the proof of
  `lemmas/shallow-cycle-resolution.md`'s Cross-Type Cycle Infeasibility Lemma) for `\#X\ge2`,
  split by parity — this is the concrete technique to hand the outliner for gap (b), and
  possibly for half of gap (a).
- For the genuinely hard remaining core (`\#X\ge3` odd, participants possibly derived): nothing
  found this round beats "prove a domain violation for a fully explicit unique linear solution" —
  might need a sharper token-level (signed, not absolute-value) argument, per Opening 4.

### 3. Cheap-kill candidates
- The `\#X` **parity classification itself** is a cheap structural pruning: it immediately
  disposes of `\#X\in\{0,1\}` (already-licensed Vertex Lemma exits) and `\#X\ge2` even (outright
  inconsistency, exact non-vanishing fact, no magnitude argument needed) — leaving only `\#X\ge3`
  odd as work. This alone shrinks the residual search space substantially before any hard
  analysis, and should be presented as a structural lemma before attempting the odd case.
- Disjointness of `T_i`'s (already certified) is what makes the "combined offset is a genuine
  signed subset sum over disjoint original indices" step free — no new machinery needed to invoke
  it.

### 4. Knowledge-base entries to use
- `knowledge_base.md`: check for any general "linear-algebra / cyclic system" or "pigeonhole on
  dependency graphs" entries — I did not find a directly-named generic technique beyond what's
  already cited (Vertex Lemma, Lemma P) in the certified lemma files themselves; the repair here
  is closer to bespoke algebra than a new KB citation. (Did not find a new KB entry to add beyond
  what's already cited in `lemmas/*.md`.)

### 5. Analogous past problems (cruxes)
Queried `past_crux_moves_database.json` filtered by `domain=combinatorics`,
`subtopic∈{games-and-strategy, invariants-and-monovariants, processes-and-algorithms}`, plus a
keyword scan for cycle/dependency/subset-sum techniques across all domains (per
`crux_moves_documentation.md`'s field names).
- **`aimo-0440`** (USAMO, number_theory, technique: "pin the sign of a coefficient combination by
  replacing every term of the dependency relation with the extreme ordered value before
  comparing," "track an auxiliary integer linear relation... read off how each operation rewrites
  its coefficients"). Genuinely analogous mechanism: it studies a linear dependency
  `a_1r_1+a_2r_2+a_3r_3=0` reduced by a `y\gets y-x` subtraction operation (structurally close to
  our D/M `M(x,y)` operation!) and proves a sign contradiction by substituting the *ordering*
  (largest/smallest term) into the dependency relation — exactly the "relabel so `b_1=\max`,
  subtract" trick our Cross-Type Lemma already uses and that the `\#X\ge3` odd bucket would need
  to generalize. Worth reading in full if the outliner wants a second worked example of this
  proof pattern.
- **`aimo-0117`** (combinatorics, games-and-strategy: "assign the played values as a two-sided
  geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all
  the others"). Confirms the "dominance" property (largest term beats the sum of the rest) is a
  recognized, reusable crux move in a *different* dyadic combinatorial game, not just folklore
  for this problem — supports treating the superincreasing dominance fact as a legitimate
  standalone tool, but the actual game mechanics (box-filling, not stick-cutting) are not close
  enough to transfer a proof step directly.
- No crux found that performs cycle-elimination on a *tie-dependency graph* specifically (the
  object here is fairly bespoke to this problem's D/M formalism); nothing closer than the above
  two was found after filtering by subtopic and by keyword scan across all three domains.

### 6. Prior progress
See §0 — `lemmas/shallow-cycle-resolution.md` (certified) resolves all-original uniform cycles;
`lemmas/dm-completeness-partial.md` (certified) sets up the dependency-graph formalism;
`lemmas/superincreasing-no-early-zero.md` (certified) supplies both the no-vanishing-subset-sum
fact (exact) and the token invariant `(S(v),\varepsilon(v))` with disjointness, both load-bearing
for this round's finding.

### 7. Dead ends (do not retry)
- The round-7 crude extension of the Cross-Type dominance argument to a general derived
  participant (bound `a_{i^*}>2\sum_{l>i^*}a_l`, reducing to false `a_{i^*}<2`) — confirmed still
  a dead end for the **odd-`\#X`** bucket specifically (this round's finding narrows *why*: it's
  a magnitude/dominance argument, and dominance is exactly what cancellation in a derived value
  can break). Do not re-attempt this exact bound; a fix (if any) needs sign-level, not
  absolute-value, information.

### 8. Small-case / intuition notes (all conjectural, numerically/symbolically supported only)
- **Conjecture A:** For `\#X\ge2` (any mix of S/X edges, all-original participants), the cyclic
  tie-system is always algebraically inconsistent — supported by 1880+ exact trials (`D_5,D_6,D_7`,
  `L=4..7`) plus 4 generic-symbolic checks (`sympy` `linsolve` on symbolic `b`'s), zero exceptions.
- **Conjecture B:** For `\#X\ge3` odd (all-original), the unique solution always violates some
  domain constraint `u_i\in(0,b_i)` — supported by 600+ exact trials, zero feasible instances.
- **Conjecture C (weaker, single spot-check only):** Conjecture A extends to cycles containing a
  derived participant, via the exact no-vanishing-signed-subset-sum fact rather than a magnitude
  bound — supported by exactly one hand-built example (`D_3`, derived piece `6=8-2`), not a
  systematic search. Needs more trials before it should be trusted as strongly as A/B.
- **Conjecture D (open, no evidence either way):** whether Conjecture B (odd-`\#X` domain
  violation) extends to derived participants — no evidence gathered this round beyond the
  round-7 negative finding that the *naive* bound fails; this remains the genuine hard core.
