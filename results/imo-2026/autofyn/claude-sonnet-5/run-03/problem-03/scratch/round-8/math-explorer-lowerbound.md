## imo-2026-03 (lens: lower-bound gaps — Branch II of L_0(l,eps), and Insertion-Robustness)

### Gap 1: Branch II of L_0(ℓ,ε) — `self-similar-induction-on-n`

**Precise re-diagnosis (new this round, numerically confirmed, NOT the same
picture as round 7's write-up).** Round 7 says Branch II "needs an upper-bound
direction that does not transplant" and reports no mechanism found. I derived
and numerically verified (exact `Fraction`, 3000 random trials spanning
`ℓ=2..7`, arbitrary piece counts respecting the `≤ℓ+1` cap, **zero
mismatches**) the following *exact identity*, valid throughout Branch II's
whole uncovered range `c_1∈(2^{ℓ-1}-1+ε, 2^{ℓ-1})`:
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1}) = 2^{\ell-1} + \mathrm{OddSum}(C'\cup\Gamma_{\ell-2}),\qquad C':=C\setminus\{c_1\}.$$
Derivation: since `c_1<max(T)=2^{ℓ-1}` here, `T`'s own top `2^{ℓ-1}` must be
peeled first (Peeling Lemma), giving `OddSum(C∪T)=2^{ℓ-1}+EvenSum(C∪T'')`,
`T''=Γ_{ℓ-2}`. Then, crucially, throughout the *actual residual range* (not
round 6's already-closed sub-ranges `c_1<2^{ℓ-2}` or `2^{ℓ-2}≤c_1≤2^{ℓ-1}-1+ε`)
one has `c_1 > 2^{ℓ-1}-1+ε ≥ 2^{ℓ-2}` (true for `ℓ≥2` since `2^{ℓ-1}-1≥2^{ℓ-2}`),
so `c_1 = max(C∪T'')`, and the Companion Peeling Lemma converts
`EvenSum(C∪T'') = OddSum(C'∪T'')` exactly (no approximation, no discarded
term — this is where round 7's framing as "needs an *upper* bound in the
wrong direction" is misleading: `OddSum≥2^ℓ ⟺ EvenSum(C∪T'')≥2^{ℓ-1} ⟺
OddSum(C'∪T'')≥2^{ℓ-1}` are all *equivalent* statements by the fixed-sum
identity `Odd+Even=sum`, not a directional mismatch).

**The reduced target is exactly a lower-level instance of the same family.**
`sum(C')=2^{ℓ-1}+ε'` where `ε':=2^{ℓ-1}+ε-c_1`, and one checks `ε'∈(ε,1)⊂(0,1)`
throughout the window (as `c_1` ranges over `(2^{ℓ-1}-1+ε,2^{ℓ-1})`). The
target `OddSum(C'∪Γ_{ℓ-2})≥2^{ℓ-1}` is **exactly `L_0(ℓ-1,ε')`'s target**
(`Γ_{ℓ-2}=Γ_{(ℓ-1)-1}`), and the piece-count bound transfers correctly:
`C` has `≤ℓ+1` parts ⟹ `C'` has `≤ℓ` parts `=(ℓ-1)+1`, exactly `L_0(ℓ-1,·)`'s
own cap. So this is a genuine strong-induction-on-`ℓ` step, **not** a
different-direction problem.

**Base case check (new): `ℓ=1`'s Branch II is vacuous.** For `ℓ=1`,
`Γ_0={1}`, Branch II range is `c_1∈(ε,1)`; but `sum(C)=2+ε` with `≤2` total
parts forces `max(C)≥(2+ε)/2=1+ε/2>1`, contradicting `c_1<1`. So the base
case holds trivially (vacuous truth) — the induction bottoms out cleanly.

**One loose end I could not fully close in the time budget (flag for the
outliner/builder):** whether `max(C')` staying `<2^{ℓ-1}` (needed to treat
`C'` as a genuine `L_0(ℓ-1,ε')` instance rather than "already done") is
automatic. Checked numerically: whenever `max(C')≥2^{ℓ-1}`, the trivial
**Element Bound Lemma** (`OddSum(S)≥max(S)`, already certified in this
approach's toolkit) closes it immediately (`OddSum(C'∪Γ_{ℓ-2})≥max(C')≥
2^{ℓ-1}`), so this case is *free*, not a gap. Whenever `max(C')<2^{ℓ-1}`,
`C'` is a genuine `L_0(ℓ-1,ε')` instance and the strong induction hypothesis
(covering **all** of `L_0(ℓ-1,·)` — Branch I.A, I.B, and Branch II
recursively) applies directly. **This looks like it closes the whole of
Branch II** via: (peel `T`'s top) + (peel `c_1`) + (case split on `max(C')`
vs. `2^{ℓ-1}`: trivial via Element Bound, or IH) — a genuinely different
framing from round 7's "no mechanism found," worth a dedicated attempt next
round. I did **not** verify every algebraic edge (e.g., whether `ε'` can hit
exactly `0` or `1` at the boundary, or whether the IH needs to be invoked at
`ε'` values not literally in `(0,1)` open — these are the kind of edge
details a builder must check line by line) — flagging as strong lead, not
a finished proof.

**Numeric evidence on extremal shape (labeled conjecture-supporting, not
proof):** searching (Monte Carlo + local descent, exact `Fraction`) for the
minimal `OddSum` over Branch II's whole parameter space shows the minimum
margin over the target `2^ℓ` **shrinks to 0 exactly as `ε→0` and `c_1→
(2^{ℓ-1})^-` simultaneously** (e.g. `ℓ=2`: margin `0.0034` at `ε≈0.0021`,
`c_1≈1.9987`; `ℓ=5`: margin `0.0148` at similarly small `ε`). This is the
*same* limiting equality point as Branch I.B's own equality case
(`c_1=c_1'=2^{ℓ-1}`, `ε→0`) — strong evidence Branch I and Branch II meet
continuously at one true extremal boundary, not two independently-hard
regimes. This supports treating them with a **unified** continuity/limiting
argument rather than genuinely different techniques, consistent with the
strong-induction finding above.

**Cheap-kill / sanity check for the builder:** the identity
`OddSum(C∪Γ_{ℓ-1}) = 2^{ℓ-1}+OddSum(C'∪Γ_{ℓ-2})` (`C'=C\{c_1}`) should be
independently re-verified (trivial, ~10 lines) before building on it — I
confirmed it numerically (0/3000 mismatches) but a builder should re-derive
it symbolically as the first step, since it is the crux of this whole lead.

### Gap 2: Insertion-Robustness — `greedy-reduction-geometric`

**Status check (per dispatch instruction): confirmed still open, not
secretly closed.** Reading `current.md` and Section 11.2 directly: Level-
Absorption (Sub-Problem B) **is** now a corrected, budget-aware statement
with strong numeric support (90k trials, zero violations) but is **explicitly
still unproved** — `current.md` says "budget-constrained ... is clean ...
but also unproven," matching the file. Insertion-Robustness (Sub-Problem A)
is also still explicitly unproved (Section 11.2's own "Net effect" states
"It remains unproved"). Neither has quietly been closed; the round-7 file is
honest about both.

**Inductive/exchange-argument reduction attempt (my contribution).** The
outliner should consider reducing the general `k'` case of Insertion-
Robustness to `k'=1` via an **adjacent-transposition exchange argument**: fix
all of `R_1` except one element and show that any two-element split of a
sub-piece can be replaced, without decreasing `OddSum(B'∪S''∪R_1)`, by a
single insertion whose effect matches the (already-proved-trivial, since
`EvenSum(S'')≥0` gives free slack there) `k'=1` case, **PROVIDED** one can
show that splitting a single element of `R_1` into two pieces (holding sum
fixed) never strictly helps the *adversary* (i.e., never strictly decreases
`OddSum` beyond a bound already accounted for). This is exactly the shape of
the crux move found in the corpus (see below): "reduce invariance under all
permutations/insertions to invariance under a single adjacent
transposition/single insertion." I did **not** verify this reduction holds
here — the single-insertion sanity check the file itself ran (Section 11.2,
"a quick single-insertion sanity check ... shows an individual inserted value
can only ever decrease OddSum by an amount bounded by the value of the
list-element it displaces") is the right partial tool, but "chaining this
bound over an arbitrary number of inserted pieces" (the file's own words) is
exactly the open step — a telescoping/potential-function argument over
successive single-insertions (using the certified **Single-Insertion Lemma**
from `self-similar-induction-on-n`, which gives an *exact* formula for
`ΔAltSum` under one insertion at an arbitrary sorted position, not just the
max) looks like the right tool to attempt this telescoping with, since it is
already proved in full and reusable, but has not yet been applied here.

**Dead end confirmed, do not retry:** "single-element `R_1` is always the
most adversarial shape" — refuted by the file's own 3000-trial exact check
(single-element shape was strictly worse only ~50% of the time). Any
future attempt assuming monotonicity in piece count of `R_1` is wasted
effort.

### Cheap-kill candidates
- Branch II: none beyond the Element-Bound short-circuit already identified
  above (`max(C')≥2^{ℓ-1}` case is free).
- Insertion-Robustness: none obvious beyond the already-tried (and refuted)
  single-element-worst-case reduction.

### Knowledge-base entries to use
- The Peeling Lemma / Companion Peeling Lemma pairing (already certified,
  `lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`) — the
  entire Branch II reduction above rests on these two, used twice in
  sequence.
- Element Bound Lemma (`OddSum(S)≥x` for any `x∈S`, certified
  `lemmas/element-bound-and-j1-theorem.md`) — closes the `max(C')≥2^{ℓ-1}`
  case for free.
- Single-Insertion Lemma (`self-similar-induction-on-n`, proved in full,
  exact `ΔAltSum` formula for insertion at an arbitrary sorted position) —
  candidate tool for a telescoping proof of Insertion-Robustness, not yet
  tried in that file.
- Base fact `OddSum(Γ_n)≥2^n` (certified `lemmas/branch-ib-two-peel-
  theorem.md`) — reusable if the strong induction on Branch II needs a floor
  on `OddSum(Γ_{ℓ-2})` directly (it doesn't, in the derivation above, since
  the recursion is exact not a discard, but worth having on hand).
- General Proof Methods / strong induction guidance in `knowledge_base.md`
  (see "General Proof Methods" section) applies directly to the
  strong-induction-on-`ℓ` framing for Branch II.

### Analogous past problems (cruxes)
- `aimo-0117` (combinatorics, `games-and-strategy`): a two-player
  box-filling game where the crux move is "assign played values as a dyadic
  (power-of-2) sequence so the single largest value strictly exceeds the sum
  of all smaller ones," proved via an induction maintaining "the largest
  power of 2 played so far sits in the target box." This is the *same
  dyadic-dominance flavor* (`2^j > sum of all smaller 2^i`) that underlies
  the Dominant-Chain Theorem and Peeling Lemma already used throughout
  `imo-2026-03`. Genuinely analogous in spirit (not a literal transplant —
  it's a different game), useful as independent corroboration that the
  "largest dyadic element dominates" invariant-tracking style of induction
  is the right family of technique here, not a new crux move to borrow
  verbatim.
- `aimo-0003` (combinatorics, `invariants-and-monovariants` /
  `induction-and-construction`): crux move "reduce an invariant-under-all-
  orderings claim to invariance under a single adjacent transposition." This
  is the closest corpus match to the Insertion-Robustness reduction idea
  above (reduce "robust under inserting an arbitrary-shape `R_1`" to "robust
  under inserting one element at a time," each step an adjacent-position
  change) — a genuine structural analogy worth adapting, though the actual
  potential function here (`OddSum`/`AltSum` under a single insertion) is
  specific to this problem and must be built from the certified
  Single-Insertion Lemma, not copied from `aimo-0003`.
- No corpus problem directly resembles the `L_0(ℓ,ε)` self-similar recursion
  itself (a value-shrinking induction on a geometric-tail lower bound) —
  searched `size-bounding-and-descent` and `sequences-and-recurrences`
  subtopics without finding a close match; this appears to be a genuinely
  problem-specific structure.

### Prior progress
Branch I.B fully closed (round 7, certified `lemmas/branch-ib-two-peel-
theorem.md`). Residual before this round: Branch II's uncovered range
`c_1∈(2^{ℓ-1}-1+ε,2^{ℓ-1})` plus a narrower Branch-I.A-restricted window
`c_1∈[2^{ℓ-1},2^{ℓ-1}+1-ε)` with no second large `C` element. This round's
new finding (above) is a candidate strong-induction closure of Branch II
specifically — the Branch-I.A-restricted window is untouched by this
exploration and remains exactly as round 7 left it.

Insertion-Robustness / Level-Absorption: both open exactly as `current.md`
states (verified, no silent resolution found); Level-Absorption's corrected
(budget-aware) statement is well-evidenced (90k trials) but unproved;
Insertion-Robustness likewise well-evidenced (20k+ trials, adversarial
search, minimum margin `+1.5`) but unproved.

### Dead ends (do not retry)
- Branch II via "peel `T`'s top, then treat it as needing an upper bound on
  `EvenSum`" framed as fundamentally different from a lower-bound argument —
  this round's finding is that this framing is misleading (Odd/Even bounds
  are equivalent by the fixed-sum identity); don't let the outliner discard
  Branch II as "genuinely upper-bound-direction, unlike Branch I.B" without
  re-examining the exact identity given above.
- Insertion-Robustness: "single-element `R_1` is worst case" (refuted,
  3000-trial exact counterexample already in the file).
- Insertion-Robustness: literal reuse of certified Subadditivity/General-
  Insertion Lemmas (checked in file, give upper bounds / exact-doubling, not
  the needed lower bound) — do not re-attempt without a genuine new idea.

### Small-case / intuition notes (labeled conjecture where not proved)
- **Conjecture, numerically well-supported:** Branch I and Branch II of
  `L_0(ℓ,ε)` share one true extremal boundary at `c_1→2^{ℓ-1}⁻`, `ε→0⁺`
  (margin `→0` from both sides, matching Branch I.B's own stated equality
  case `ℓ∈{1,2}`, `c_1=c_1'=2^{ℓ-1}`). This is evidence, not proof, but is a
  strong structural hint that a single unified argument (the strong
  induction above) should be able to handle both branches near the boundary
  rather than needing genuinely different mechanisms.
- **Verified fact (exact, not conjectural):** the reduction identity
  `OddSum(C∪Γ_{ℓ-1})=2^{ℓ-1}+OddSum(C'∪Γ_{ℓ-2})` for Branch II, 0/3000
  mismatches across `ℓ=2..7`, arbitrary piece counts within the `≤ℓ+1` cap.
- **Verified fact (exact):** Branch II is vacuous at `ℓ=1` (piece-count
  arithmetic forces `max(C)>1` whenever `sum(C)=2+ε` with `≤2` parts),
  giving a clean base case for the proposed strong induction.
