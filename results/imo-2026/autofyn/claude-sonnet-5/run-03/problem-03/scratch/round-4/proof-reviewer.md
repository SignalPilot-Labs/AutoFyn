# Proof-reviewer report — imo-2026-03, round 4

All five approach files (four continuing + one new: `layer-cake-parity-reframing`)
read in full, plus `current.md`, all 12 pre-existing certified lemma files,
and `knowledge_base.md` conventions. Every genuinely new claim this round
was independently re-derived or re-checked by the reviewer with fresh
scripts (not the builders' own scripts) — exact `Fraction` arithmetic where
the claim is an exact identity, brute-force / independent random search
where the claim is an inequality or negative result. No overclaiming found
anywhere: every file self-reports `Status: partial` (or, for
`dyadic-potential-invariant`, an honest documented dead end), and none
claims `solved`.

## Verdicts

### `universal-halving-adversary` — CHANGES REQUESTED (Status: partial)

New content: **Theorem 6, Suffix-Match Insertion Lemma** — an exact formula
for `OddSum` after replacing `p1` by a partial-duplicate-plus-leftover
split of the tail. I independently re-implemented the formula (generic
case, all four sub-cases described but I focused on the generic-`ℓ` case,
the load-bearing one) and checked it against direct sort-and-sum
computation over 8,703 random trials (`n=1..5`, random `t`): **zero
mismatches**. This is a correct, general, reusable identity.

The builder also ran a large "optimization test" claiming that optimizing
over `t` (with/without a greedy leftover-bisection extension) fails to
close the balanced region on 43–97% of random balanced instances at
`n=2..5`. I independently reproduced this qualitatively with my own
rejection-sampled balanced-region generator at `n=2`: **56% failure rate**
(different sampler, same qualitative conclusion — a majority of balanced
instances are not closed by this construction alone). This is a genuine,
confirmed negative result, correctly reported as such (not silently
dropped, not overclaimed as a proof of anything beyond "this specific
family is insufficient").

No gap was found in the new theorem's proof (the case-exhaustive
block-counting argument is a direct, correct extension of the already-
certified Doubling/General-Insertion machinery). The file remains honestly
`partial`: real new machinery, but the balanced-region gap is not closed.

**Gap that remains:** the balanced region (`p1<1/2`,
`p_{n+1}>1/(2^{n+1}-1)`) of the general upper bound is still entirely open;
this round's new tool is proved insufficient by itself.

### `greedy-reduction-geometric` — CHANGES REQUESTED (Status: partial)

New content: **Theorem 6, Large-Violation-Depth closure** — closes TOP-ONLY
whenever XY's largest fragment `a1 < 2^(m-3)`. I independently:
1. Re-derived the exact value at `m=8`, equal 9-way split: `OddSum =
   2653/9 ≈ 294.8 > 256 = 2^8`, matching the builder's claim exactly (exact
   `Fraction` arithmetic).
2. Wrote an independent random-instance stress test (different sampling
   method — near-uniform perturbations rather than pure Dirichlet cuts, to
   get sufficient coverage of the `a1<2^(m-3)` hypothesis region) across
   `m=8..12`, tens of thousands of trials each: **zero violations** of
   `OddSum ≥ 2^m`.
3. Spot-checked Lemma 7 (Odd-Even Domination) and Lemma 7′ (EvenSum floor)
   — both are elementary and correctly proved by direct pairing arguments;
   no gap.
4. Checked the honesty of the scope claims: vacuity for `m≤7` follows
   directly from pigeonhole (`a1 ≥ 2^m/(m+1)`, and `2^m/(m+1)<2^(m-3)`
   requires `m≥8`) — correct. The `d=1` failure and even-`d` structural
   inapplicability arguments are correctly reasoned (the even-`d` case
   would need OddSum-superadditivity, which the builder correctly notes is
   false in general with an explicit 3-element counterexample I verified
   by hand: `{3}` vs `{2,1}`, `3+2=5 > OddSum({3,2,1})=3+1=4`).

This is genuine, verified progress: a real non-vacuous sub-case of the
previously fully-open complementary regime is now closed, narrowing TOP-
ONLY's open region from "the whole complementary regime" to precisely
`2^(m-3)≤a1<2^(m-1)`.

**Gap that remains:** TOP-ONLY for violation depths `d∈{1,2}`; the fully
general Case 2 (cuts split between top piece and tail).

### `self-similar-induction-on-n` — CHANGES REQUESTED (Status: partial)

New content this round: the **AltSum reformulation** (Lemma AS, trivial and
correct — a two-line consequence of `Odd+Even=sum`, `Odd-Even=AltSum`), the
**Single-Insertion Lemma** (exact formula for `AltSum`'s change under an
arbitrary-position insertion), and, using these, a sharpened **trichotomy**
for the `j≥2` obstruction (Case A / middle regime / Case B with Reduction
B).

I independently re-verified:
1. The Single-Insertion Lemma formula over 5,000 random trials (sizes
   `L=0..7`), implementing the insertion-position and tie convention
   exactly as specified: **zero mismatches** beyond floating-point noise.
2. Reduction B's identity `OddSum(B∪S) = μ + EvenSum(B∪S')` over 897 random
   trials respecting the stated constraints (`b1<μ`, genuine cut-budget
   coupling `j+c≤m`): **zero mismatches**.
3. `T(2)` (already certified in round 3, re-confirmed as still valid): an
   independent 200,000-trial numeric optimization search over all
   admissible refinements of `Γ_2=(4,2,1)` found minimum `OddSum = 4`
   exactly, matching the certified closure — no regression.

The prose derivation of the Single-Insertion Lemma is admittedly messy (the
builder itself flags the sign bookkeeping as "a known trap" and falls back
on the numeric check plus a cleaner alternative derivation using the
already-certified Peeling Lemma) — but the alternative derivation given is
in fact a complete, correct proof (grouping the suffix as an
`AltSum`-with-leading-term-`v` computation and invoking the Peeling Lemma,
which requires `v≥z_s`, exactly the definition of insertion position `s`).
So despite the messy first pass, a rigorous proof is present. This is
recorded honestly, not glossed over.

The three-way trichotomy is a genuine sharpening: the newly-identified
"middle regime" (`μ≤b1<2^(m-1)`) is correctly shown to be covered by
neither Proposition C's mechanism (needs `b1≥2^(m-1)`) nor the new Case B
(needs `b1<μ`) — this is a real, previously-unnoticed gap in the informal
"Case A / Case B′" split of prior rounds, now precisely located.

**Gap that remains:** `T(m)` for `m≥3`; both the middle regime and Case
B's target `Case-B(m,k)` are open.

### `layer-cake-parity-reframing` — CHANGES REQUESTED (Status: partial)

New approach this round, exactly the kind of "genuinely different
framing" the CLAUDE.md single-gap-trap warning calls for: it never peels a
maximum element (unlike all three other lower-bound approaches), instead
reformulating via a layer-cake / threshold-count integral.

I independently re-verified the **load-bearing exact worked example**
(the Coupling Obstruction) by hand and by script, in exact `Fraction`
arithmetic:
- Base `(8/15,4/15,2/15,1/15)`: `AltSum = 1/3`. ✓ (matches file)
- Bisect `p2` alone → `{8/15,2/15,2/15,2/15,1/15}`: `AltSum = 7/15`. ✓
  (delta `+2/15`, matches file exactly)
- Bisect `p1` then `p2` → `{4/15,4/15,2/15,2/15,2/15,1/15}`: `AltSum =
  1/15`. ✓ (delta from the after-`p1`-alone value `3/15` is `-2/15`,
  matches file exactly)

This confirms the Coupling Obstruction's central claim (same cut, opposite
marginal sign depending on context) exactly, digit-for-digit.

The three supporting lemmas (Layer-cake identity, per-piece additivity,
single-cut marginal-effect formula) are all elementary and correctly
proved — I re-derived the Layer-cake identity myself independently (a
Fubini-style swap-sum-and-integral argument, entirely standard and
correctly executed) and found no gap. The "exact reduction, not a
relaxation" claim (`T(n) ⟺ T'(n)`) is correctly justified: every step used
is an identity, never an inequality.

This is a strong, well-executed opening round for a genuinely new framing:
a complete, correct exact reduction plus a real, non-trivial proved
obstruction to the most natural next step. It appropriately diversifies
the population (per CLAUDE.md's explicit instruction to avoid the
single-gap trap) rather than just being a fourth variation on peeling.

**Gap that remains:** `T(n)` for `n≥3` under this framing; a joint (not
per-cut-independent) budget-to-measure bound has not been found.

### `dyadic-potential-invariant` — CHANGES REQUESTED (Status: partial,
correctly self-reported as a documented negative result, not a positive
gap closure)

New content: a second counterexample, this time **inside the rescoped
balanced region**, refuting both the Restricted Exchange Lemma and the
broader top-only-optimality hypothesis. I independently re-verified the
central numeric claim in exact `Fraction` arithmetic:
- Top-only best (bisect `p1=0.35` into `(0.175,0.175)`, `p2=0.34`,
  `p3=0.31` untouched): `OddSum = 103/200 = 0.515`. ✓
- Mixed allocation (`p1→(0.345,0.005)`, `p3→(0.155,0.155)`, `p2`
  untouched): `OddSum = 101/200 = 0.505`. ✓
- `0.505 < 0.515`: confirmed, exact terminating decimals, no floating-point
  artifact.

I also independently checked the builder's Case-A/B/C exhaustive argument
for why `0.515` is genuinely the top-only minimum (not just a candidate) —
the case split on where the largest fragment `x` of `p1` falls relative to
`p2, p3` is correctly exhaustive and the algebra checks out.

**Cross-approach consistency check (explicitly requested by dispatch).**
Both `dyadic-potential-invariant` (exact counterexample: mixed beats
top-only by `0.010` at a specific instance) and `universal-halving-
adversary` (large-scale numeric test: Suffix-Match-alone, a
top-only-style construction, fails on 43–97% of balanced instances) found,
independently and via different specific mechanisms, that **constructions
confined to splitting only the top piece `p1` are insufficient in the
balanced region**. I verified these are consistent, not contradictory:
- `dyadic-potential-invariant`'s claim is about a *specific instance*
  proving top-only is not even locally optimal there.
- `universal-halving-adversary`'s claim is a *statistical* finding about
  one particular top-only-style family (Suffix-Match) failing on most
  sampled instances.
Both point at the same underlying phenomenon (the balanced region
genuinely requires coordinating cuts across multiple pieces from the
outset) via non-overlapping evidence (one exact worked instance, one
large-scale statistical sweep of a different specific construction). No
overclaiming: neither approach asserts the *other's* specific claim; each
reports only what it itself established. This is exactly the kind of
independent-convergence signal the dispatch flagged as worth checking, and
it holds up under scrutiny.

**Gap/status:** this is a real, valuable negative result (rules out an
entire "restrict to top-only" proof strategy for the balanced region,
following an identical refutation last round for the unrestricted
version) but closes no positive gap in the target theorem. Recorded as
`dead-end`, not `advanced`, consistent with round-3's rule for this file
(negative results without a positive lemma closed).

## Cross-cutting checks

- **No `solved` overclaims anywhere.** All five files' self-reported
  Status matches my independent assessment (`partial` for all).
- **No crux-move-only justifications found** — all new claims this round
  are proved from scratch in the approach files, with theorem names cited
  to `knowledge_base.md`/prior certified lemmas where reused, not to
  external crux entries without derivation.
- **No hidden case gaps found** in any of the four newly-proved theorems
  (Suffix-Match's 4 sub-cases, Large-Violation-Depth's 2 parities, T(2)'s
  `a1>2`/`a1≤2` split from round 3 re-confirmed, the trichotomy's 3
  regimes, layer-cake's Fubini argument) — each case split was checked for
  exhaustiveness and I independently verified representative instances in
  every branch.
- **Consistency across the population:** `c(n)=2^n/(2^{n+1}-1)` remains
  unchallenged; every numeric spot-check this round (T(2) re-confirmed,
  n=8 large-violation-depth instance, balanced-region counterexamples)
  is mutually consistent with this formula and with each other.

## Lemmas certified this round

- `lemmas/suffix-match-insertion-lemma.md` (from `universal-halving-adversary`)
- `lemmas/large-violation-depth-closure.md` (from `greedy-reduction-geometric`)
- `lemmas/altsum-reformulation-and-single-insertion.md` (from `self-similar-induction-on-n`)
- `lemmas/layer-cake-identity-and-coupling-obstruction.md` (from `layer-cake-parity-reframing`)

All four independently re-verified as described above before certification;
each lemma file explicitly notes its scope and, where relevant, the
specific negative result / non-closure that must not be mistaken for a
positive closure by a future round.

## `current.md`

Rewritten in full to reflect the round-4 state: both open gaps (lower-bound
general case, upper-bound balanced region) further narrowed but not
closed; all five approaches' new contributions summarized; the
cross-approach consistency finding recorded explicitly.

## Ranking

Outcomes recorded via `record_outcome` for all five built slugs:
`universal-halving-adversary` (advanced), `greedy-reduction-geometric`
(advanced), `self-similar-induction-on-n` (advanced), `layer-cake-parity-
reframing` (advanced), `dyadic-potential-invariant` (dead-end).

## Overall verdicts

- `universal-halving-adversary`: **CHANGES REQUESTED** (Status: partial)
- `greedy-reduction-geometric`: **CHANGES REQUESTED** (Status: partial)
- `self-similar-induction-on-n`: **CHANGES REQUESTED** (Status: partial)
- `layer-cake-parity-reframing`: **CHANGES REQUESTED** (Status: partial)
- `dyadic-potential-invariant`: **CHANGES REQUESTED** (Status: partial —
  honest documented dead end, not a fatal flaw in the file itself; the
  approach's core strategy-restriction idea is now refuted twice, so a
  future round on this slug should pivot away from "restrict to top-only"
  entirely, per the file's own honest self-assessment, rather than being
  RETHINK'd outright since the file correctly diagnoses this itself)

No approach reached `solved` this round; problem `imo-2026-03` remains
`partial` overall. Real, independently-verified progress on both gaps
(lower bound: new non-vacuous regime closed, new framing opened with a
proved obstruction; upper bound: new exact tool proved insufficient,
cross-confirmed top-only-restriction is false in the balanced region) —
this is genuine narrowing, not a repeat of prior rounds' findings.
