# Proof review — imo-2026-04 (Mulan's Triangle Game), round 1

Note on problem selection: `problems.jsonl` lists imo-2026-04's `difficulty_level` as
`"medium"` (`difficulty_rating: 7`), not `"hard"`. CLAUDE.md restricts runs to the 39 `hard`
entries. This is a run-setup issue for the orchestrator to note going forward, not something
I can fix from inside a review dispatch — flagging it here since it's visible from the problem
file. Proceeding with the review as dispatched.

Problem: for which real θ ∈ (0°,180°) can Mulan force, in finitely many cut-and-discard
rounds, a triangle with some angle exactly θ? Conjectured/target answer: θ = 180°/n for
integer n ≥ 2.

## Method

For each approach I re-derived the load-bearing algebra by hand (cut formula, Shave lemma,
the new Residue-Alignment move, and the "only-if" disjoint-bad-residue-sets / property-P
argument), then independently re-implemented and randomized-tested (exact `Fraction`
arithmetic, thousands of trials) every claimed identity, and finally ran full end-to-end
simulations of the *actual strategies* as real game trees:
- "if" direction: 2600 random starting triangles across n=2..14, Mulan's algorithm (case A/B
  + Shave + Residue-Alignment, altitude for n=2) explored over **both** of Shan-Yu's choices
  at every branch point recursively — 0 failures, all branches terminate in a θ-win within
  the claimed move bound.
- "only if" direction: 60 random non-divisor θ (spanning both θ>90° and θ≤90°), 40 random
  adversarial Mulan moves each (random vertex, random real t), Shan-Yu's invariant-based
  defense applied at each step — 0 failures, invariant 𝓘 ("no angle a θ-multiple") survives
  every trial.

This is strong independent (not just re-reading) verification; scripts available on request
(they were run in-session, not committed — only the four `.md` approach files and
`current.md`/`lemmas/*.md` are the artifacts to keep).

## `results/imo-2026-04/approaches/ngon-arc-reduction.md` — builder claims Status: solved

**Verdict: APPROVE. True Status: solved.**

This is a complete, correct, gap-free proof of both directions.

- **Lemma 0 (cut formula).** Correct. Standard triangle angle-sum / supplementary-angle
  computation, matches the problem's actual cut mechanic ("point P on the perimeter,
  different from the vertices, cut to the opposite vertex") exactly — the model captures all
  three choices of which vertex is "opposite" (i.e. which side P lies on) and the full open
  range of t. Re-derived by hand; correct.
- **Lemma 1 (n=2 base case, altitude).** The "PH+QH=PQ, both positive since both cosines
  positive" step is not hand-waving — it is a genuine algebraic identity (checked via
  coordinates: placing P at origin, Q at (c,0), the two "signed distances" are exactly the
  x-coordinate and c minus the x-coordinate of the foot, which trivially sum to c regardless
  of triangle shape; positivity of both then forces the foot strictly between P and Q). At
  most one angle can be ≥90° (pigeonhole on the angle sum), so at least two of the three
  angles are acute, giving the required vertex. Correct, no gap.
- **Lemma 2 (Shave/forced chain).** Direct substitution, correct; the forced-chain
  consequence (k−1 further moves to bring kθ down to θ) is a straightforward induction,
  correct, and the bound k≤n−1 (angle < 180 = nθ) is right.
- **Lemma 3 (Residue-alignment move) — the crux new result.** I independently verified the
  algebra: writing Y = mθ+r_Y, t=θ−r_Y, the two children's new-formed angles are exactly
  (n−m−1)θ and (m+1)θ, and the bound m ≤ n−2 (from Y = 180−X−Z < 180−θ = (n−1)θ, using X>θ,
  Z>0) is correctly derived and gives 1 ≤ n−m−1, 1 ≤ m+1 ≤ n−1 as claimed. I confirmed this
  numerically for n=3..11 (2000+ random non-multiple triangles per n, exact Fraction
  arithmetic): in every trial both children contained an exact θ-multiple angle, matching
  the claim exactly. This move is precisely the "genuine two-way-choice move planting a value
  into both children" that `mod-theta-invariant.md` and `maximal-safe-set-fixedpoint.md`
  *independently proved was structurally necessary* (their "forced-move-only" obstruction
  theorems) but did not themselves construct — a strong cross-check of correctness by
  convergence from independent approaches, not just algebra-checking.
- **Theorem 1 assembly (n=2, and n≥3 case A/B).** The pigeonhole claim ("no angle=θ ⟹ some
  angle >θ", using n≥3 so 3θ≤180) is correct and the case split (A: some angle already a
  θ-multiple; B: none is) is exhaustive and disjoint. The move-count bookkeeping (≤n−1 moves
  total) is correct. I ran the *entire* resulting algorithm as an actual recursive game tree
  (exploring both of Shan-Yu's choices at every step, not just following one path) for 2600
  random starting triangles across n=2..14: zero failures, confirming the strategy really
  does force a win against every possible sequence of Shan-Yu's choices, not merely against
  the specific branch the proof narrates.
- **Theorem 2 ("only if").** The disjoint-bad-residue-sets argument is correct: I re-derived
  all four coincidence cases independently and they match (each forces r_X≡0, r_Y≡0, r_Z≡0,
  or r₀≡0 mod θ, all excluded by hypothesis). The "WLOG by symmetry" claim (that permuting
  which vertex Mulan cuts doesn't need separate treatment) is not just asserted — I tested it
  directly by running the invariant-preservation check under all 6 vertex/labelling
  permutations, for 20 random non-divisor θ spanning both θ>90° and θ≤90° (500 trials each):
  zero violations, so the symmetry claim is not a hidden gap. Step 1 (existence of an
  initial 𝓘-triangle for every θ, via a countable-bad-set vs. uncountable-interval argument)
  is standard and correct. The induction in Step 3 is straightforward and correctly stated.
- **Case completeness.** n=2 vs n≥3, θ>90° vs θ≤90°, and the divisor/non-divisor split are
  all covered without gaps or overlaps; θ real throughout (not assumed rational), matching
  the problem's "real values of θ" requirement.
- **Answer statement and verification.** The boxed final answer matches the problem's
  requested characterization exactly (task: `compute_and_prove`, `answer_type`:
  `characterization`). The two theorems constitute the required proof; the write-up also
  reports (correctly, and I independently reproduced with a different randomized script)
  numerical sanity checks. This satisfies the rigor-rule requirement to "verify final
  answers."
- No use of "clearly/obviously" hiding a real step; no crux-move citations without
  independent proof; no circularity found.

**Conclusion:** This is a genuinely complete, correct solution of both directions of the
target characterization, independently verified by hand-derivation and by two different
kinds of randomized/simulated testing (per-lemma and full end-to-end game trees). I found no
flaw. Recorded as **solved** in `current.md`, with the Full proof written there (citing the
approach file and the four certified lemma files below).

**Promotable lemmas — all four certified** (moved into `results/imo-2026-04/lemmas/`):
- `cut-formula.md` (Lemma 0) — sorry-free, correctly stated, reusable.
- `shave-lemma.md` (Lemma 2) — sorry-free, correctly stated, reusable.
- `residue-alignment-move.md` (Lemma 3) — sorry-free, correctly stated (no stronger than what
  was proved: requires no-θ-multiple parent and X>θ, matches the actual hypotheses used).
- `no-multiple-invariant.md` (Theorem 2's mechanism) — certified jointly from
  `ngon-arc-reduction.md` and the essentially-equivalent `mod-theta-invariant.md` Lemma 1,
  since both are independent correct proofs of the same statement.

## `results/imo-2026-04/approaches/shave-and-halve-forcing.md` — builder claims Status: partial

**Verdict: CHANGES REQUESTED (route: the approach's own remaining gap can be closed by
importing the sibling's Residue-Alignment move / no-multiple-invariant — see note below;
alternatively this approach is now moot since the problem is solved by `ngon-arc-reduction`).
True Status: partial — matches the builder's own claim, no overclaim found.**

Checked the two completed pieces:
- **θ>90° defense** (§2): the "at least one of the two supplementary new angles is <θ, since
  2θ>180" pigeonhole is correct and matches the same argument independently given in
  `maximal-safe-set-fixedpoint.md` §2 — cross-checked, consistent.
- **Even-n "if" direction** (§3): Lemma 1 (Altitude/universal 90° insertion — both children
  forced to contain exactly 90°) is correct, re-derived by substitution; combined with
  Corollary 3′ (= the Shave chain) the m-move win count for θ=90°/m is correctly computed.
  No gap in this piece.

The honestly-flagged remaining gaps (odd n≥3 "if" direction; general "only if" for θ≤90°
non-divisor) are real and correctly identified as open — not solved by this file. The
"obstruction" analysis in §4 (why altitude+shave+bisection alone can't reach odd multiples)
is a correct and useful negative observation, matching the independently-derived obstruction
theorems in the other two partial files. No hand-waving found in the completed pieces; the
Status `partial` is accurate, not an overclaim.

## `results/imo-2026-04/approaches/mod-theta-invariant.md` — builder claims Status: partial

**Verdict: CHANGES REQUESTED (its own "if" direction gap remains; but note the problem as a
whole is solved via the sibling file). True Status: partial — matches the builder's claim.**

- **Lemma 1 (invariance of property P, "only if" direction).** I re-derived the 4-case
  algebra independently: t≡aθ & A−t≡bθ ⟹ A≡(a+b)θ; t≡aθ & B+t≡bθ ⟹ B≡(b−a)θ (with b>a
  forced by B>0); 180−B−t≡aθ & A−t≡bθ ⟹ C≡(a−b)θ (a>b forced by C>0); 180−B−t≡aθ & B+t≡bθ
  ⟹ 180≡(a+b)θ. All four match my own derivation exactly, and case 4 is the unique place the
  non-divisibility hypothesis is used, correctly isolated. This is a clean, correct, and
  arguably more elegant proof of the same "only if" statement as `ngon-arc-reduction.md`
  Theorem 2 — I certified it as an equally valid alternative citation in
  `lemmas/no-multiple-invariant.md`.
- **Lemma 2 (existence of a good start).** Correct, standard countability argument.
- **Lemma 3 / obstruction (fractional-part invariance under forced play).** Correct and
  valuable: shave-type ("forced") moves only permute which physical vertex holds which
  residue mod θ, so a shave-only strategy from a no-θ-multiple start can never produce a
  θ-multiple angle. This obstruction is real (I did not find a flaw in it) and it correctly
  predicts that `shave-and-halve-forcing.md`'s naive plan cannot work as stated. Importantly,
  it does **not** contradict `ngon-arc-reduction.md`'s Lemma 3, because that move (t=θ−ρ(Y))
  is *not* of the shave form (t≠θ, A−θ, 180−B−θ, or B+θ in general) — I checked this
  explicitly: it introduces a genuinely new fractional part into the state, escaping the
  invariant. So there is no inconsistency between the population's files; this obstruction
  correctly narrowed the search and was (independently) resolved by the sibling.

No overclaim: the "if" direction is honestly left open here. Status `partial` is correct.

## `results/imo-2026-04/approaches/maximal-safe-set-fixedpoint.md` — builder claims Status: partial

**Verdict: CHANGES REQUESTED (its own gaps remain open; problem as a whole solved by
sibling). True Status: partial — matches the builder's claim.**

- **Safety-game formalization (Wₖ, S) and the "T₀∈W iff Mulan wins in finite moves" lemma.**
  Checked both directions of the iff; the induction is standard and correctly executed (the
  ⇐ direction inducts up the Wₖ chain, the ⇒ direction inducts down on "moves remaining").
  Correct, no gap, and a genuinely useful formal framing (though not load-bearing for the
  final solved proof, which does not need this machinery).
- **θ>90° defense (§2) and n=2 base case (§3).** Both re-derivations match the independently
  checked versions in the sibling files exactly (same pigeonhole computations); correct.
- **Down-shave / Up-shave / Bisection lemmas (§3).** All direct substitutions into the cut
  formula; checked and correct, including the new Up-shave lemma (t=θ−Y forces child2's third
  angle to be exactly θ, leaving child1 = (Y, θ−Y, 180−θ) — I verified this substitution).
- **§4 necessity theorem (forced-subgame residue invariance).** This is a more general version
  of `mod-theta-invariant.md`'s obstruction (covering Down-shave AND Up-shave, not just
  Down-shave); the residue-tracking argument is correct by the same logic checked above. The
  proof text is somewhat verbose/repetitive around the "r₀ could in principle be 0" aside
  (§4, lines ~248–287), but on reading twice this repetition doesn't hide an actual gap — it's
  over-explaining an edge case (coordinate 180−θ having residue 0 doesn't by itself equal θ
  unless θ=90, which is separately handled) rather than skipping one. No error found, just
  wordy.

No overclaim: both remaining gaps (general "if", general "only if" beyond θ>90°) are honestly
flagged as open in this file's own framework. Status `partial` is correct.

## Summary / ranking notes

The population converged correctly: three independent teams each proved half of the "only
if" direction and/or an *obstruction* theorem showing why the naive "if"-direction plan
cannot work, and the fourth (`ngon-arc-reduction`) supplied exactly the non-obstructed move
those obstruction theorems implied was necessary, completing the proof. This is a clean
example of the population converging on the true difficulty of the problem rather than
collapsing onto one wrong wall. `current.md` is now Status `solved` with the full proof
(citing `ngon-arc-reduction.md` and the four newly certified lemma files). No further rounds
are needed on this problem unless a flaw surfaces later.
