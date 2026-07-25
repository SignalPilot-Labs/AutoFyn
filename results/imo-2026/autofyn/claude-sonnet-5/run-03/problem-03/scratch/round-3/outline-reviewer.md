## imo-2026-03 — outline review, round 3

Reviewed `/tmp/round-3/proof-outliner.md` against `results/imo-2026-03/current.md`,
all four `approaches/*.md`, all `lemmas/*.md`, and the three round-3 explorer
reports (`math-explorer-lemmaX.md`, `math-explorer-freshframing.md`,
`math-explorer-upperbound.md`). All four candidates are **revisions** of
already-registered slugs (no new slug, no branch requested), so no
`register_approach`/`copy_approach` calls were needed this round.

### Verification of the load-bearing global claim (Lemma X′ drop)
Confirmed independently: both `math-explorer-lemmaX.md` (point 2, explicit
counterexample even under the extra restriction `max(A')≤T'/2`) and
`math-explorer-freshframing.md` (point 4, an independent counterexample,
explicitly cross-referenced to a parallel finding in `/tmp/memory/math-explorer.md`)
disprove Lemma X′ ("EvenSum(S')≥T'/2 ⟹ EvenSum(A'∪S')≥T'" for arbitrary
positive multisets) by concrete numeric counterexample. The outliner's global
note correctly states this is doubly confirmed and instructs no outline to
resurface it in this general form. I checked every one of the four outlines
below and **none of them reintroduces Lemma X′** — good, the gate correctly
enforces the dead-end record. Also correctly dropped: the "merging top
fragments / reducing j only helps LB" exchange shortcut, independently
refuted this round (`math-explorer-lemmaX.md` point 3, explicit m=4
counterexample) — none of the four outlines relies on it either.

---

### self-similar-induction-on-n (revise: Recursive Depth Peeling Lemma)
**Verdict: CHANGES REQUESTED** (sound direction, but real open sub-cases must
not be glossed over by the builder).

- The pivot correctly targets the actual failure mode diagnosed by
  `math-explorer-lemmaX.md`: peeling the top fragment often hits the tail's
  own *untouched, exactly-known* top piece `2^{m-1}` next, not an unknown
  refined sub-multiset — so no dual EvenSum bound is needed if you track
  depth-in-hierarchy explicitly rather than an abstract two-sided IH. This
  matches the explorer's own numeric finding (worst case: `a1` barely above
  `2^{m-1}`, tail's own top piece untouched) — the outline is chasing the
  empirically-tight case, not a strawman.
- The outline itself, honestly, flags two sub-cases as genuinely unresolved
  and defers them to "this round's job": (i) `a1 < 2^{m-1}` (top fragment
  does *not* dominate the tail's own top piece — the very first peel then
  hits the tail, not `A`), and (ii) bookkeeping when `j≥2` fragments of `A`
  interleave *among themselves* above level `m-d`. These are correctly
  identified as open, not glossed over — good practice — but the builder
  must not claim the Recursive Depth Peeling Lemma "proved" without covering
  both; if either resists a clean argument this degrades back toward needing
  something Lemma-X′-shaped (watch for this: is "sort A internally first,
  since its values are known once XY's split is fixed" *actually* enough to
  avoid a dual bound in case (ii)? The outline asserts yes but does not
  demonstrate it — this is the single largest risk in the outline).
- No circularity found: the induction bottoms out on the already-certified
  base cases (`j=0`, `j=1`), and depth strictly decreases each recursive
  step (finite hierarchy, `m` levels) — termination argument is sound.

### greedy-reduction-geometric (revise: top-only-splitting sub-case)
**Verdict: CHANGES REQUESTED** (correctly and honestly scoped; one
cross-approach coupling to watch).

- This is a genuine narrowing to a tractable, self-contained sub-problem
  with an *exact known tail* (no unknown refinement ever appears), which is
  exactly right given the diagnosed obstruction — no dual bound is needed
  because nothing is ever abstracted away. The piecewise-linear /
  breakpoint-enumeration technique (step 3) is a legitimate, named KB tool
  (Piecewise-concavity smoothing) and matches what `freshframing`'s numerics
  already exhibited informally (flat 1-parameter faces of exact minimizers
  at `n=3`) — the outline is not inventing an untested mechanism.
- **Scope discipline is explicit and correct**: the outline states plainly
  "this closes only the top-only-splitting sub-problem, not general Case 2"
  and puts the general reduction on `dyadic-potential-invariant` this round
  — good, it does not overclaim.
- **Watch item (not fatal, flag per memory rule on hidden convergence):**
  this creates an explicit two-slug dependency — `greedy-reduction-geometric`
  proves the top-only bound, `dyadic-potential-invariant` is asked to prove
  the reduction that makes top-only WLOG for the full Case 2. Combined, they
  would jointly close Case 2; individually, each remains a standalone,
  honestly-scoped partial result (this is *not* the CLAUDE.md single-gap
  trap in the strict sense — the two lemmas are genuinely different
  mechanisms, and each is independently reusable/certifiable even if the
  other never lands), but the orchestrator should watch next round whether
  this coupling becomes "if dyadic's Exchange Lemma fails, greedy's top-only
  result is stranded and vice versa" — if that happens 2+ rounds running,
  it's time to treat them as one attempt, not two.
- Open gap "uniform in n" (step 3) is correctly flagged as the main
  remaining builder task, not swept under an "it follows" — good.

### dyadic-potential-invariant (revise: Cut-Reallocation Exchange Lemma, first real build)
**Verdict: CHANGES REQUESTED**, but this is the correct call and matches a
standing rule: run the numeric stress test *before* investing in a proof.

- Step 1 explicitly mandates numerically stress-testing the Exchange Lemma
  against adversarial allocations (cuts on *both* a top fragment and a tail
  piece simultaneously, at various depths, `n=3,4,5`) *before* any proof
  attempt, and instructs killing the approach immediately with a reported
  counterexample if it fails. This is exactly right — `freshframing`'s
  support for "opening 1" was informal/partial (it did not report having
  tried the specific adversarial split-both-simultaneously configurations),
  so the outline correctly does not treat it as already-verified.
- The claimed mechanism (moving a cut toward the top is weakly worse for LB)
  is stated as a *local, two-piece* exchange, checkable by finite case
  analysis on adjacent levels — this is a plausible, checkable target, not a
  restatement of Lemma X′ or the already-refuted merge-monotonicity claim
  (verified: it is a different claim — about cut *placement*, not about
  merging *fragments*, and about a fixed ratio-2 dyadic structure, not
  arbitrary multisets).
- No fatal flaw found, but zero confirmed content yet (crux entirely
  unproved) — this is appropriately gapped as CHANGES REQUESTED / early
  stage, not RETHINK, since the numeric-test-first discipline is exactly
  the safeguard needed given this approach's history (3 idle rounds, this
  round replaces vague "local split monotonicity" scaffolding with a
  concrete, falsifiable claim).

### universal-halving-adversary (revise: Perfect-Pairing corollary + bisect-or-match)
**Verdict: CHANGES REQUESTED** (step 1 is essentially already proved; step 3
is honestly conjectural).

- **Verified the Perfect-Pairing / Bisect-Everything Corollary myself**: for
  `k≤n`, bisecting all `k` LB pieces produces a multiset where every value
  occurs in an even-multiplicity block (each original piece contributes two
  equal half-copies; coincidental equal halves across pieces only merge
  blocks, preserving evenness). By the already-certified Doubling-Lemma
  Claim, every even-length tied block splits exactly half to each player
  regardless of rank-parity offset, so `OddSum = sum/2 = 1/2 ≤ c(n)` (since
  `c(n) > 1/2` for all `n`). Hand-checked with `n=2`, two unequal pieces
  `p1>p2`: sorted `p1/2, p1/2, p2/2, p2/2`, odd ranks give
  `p1/2+p2/2=(p1+p2)/2=1/2` — matches. This step is correctly a "should
  close quickly" claim, essentially free from certified machinery — no gap
  here beyond formal write-up.
- Step 3's recursive bisect-or-match rule is explicitly and correctly
  labeled "conjecture verified on 4 instances," not a proof — the induction
  (budget accounting never runs out; the `p_i` vs `S_i` threshold is truly
  optimal, not just optimal on tested examples) is real open work, honestly
  scoped as such. Good — no overclaiming.
- Step 4's near-equal-partition handling correctly incorporates the
  `math-explorer-upperbound.md` counterexample (`(0.336,0.333,0.331)` at
  `n=2` refutes "bisect-all-but-smallest" as a universal rule) rather than
  ignoring it — the outline does not repeat this now-documented dead end.
- No circularity or dropped cases found in the outline's case split
  (`k≤n` vs `k=n+1`, and within `k=n+1`, match-vs-bisect at each level).

---

### Diversity assessment
The outliner's own framing (four genuinely distinct techniques: recursive
depth induction on the geometric hierarchy / exact-tail top-only peeling /
cut-reallocation monovariant / pairing-parity argument) is accurate and
responds correctly to `math-explorer-freshframing.md`'s diversity flag (three
of four approaches had converged on the same "dual EvenSum on an arbitrary
refined tail" wall; `dyadic-potential-invariant` sat idle 3 rounds). Building
`dyadic-potential-invariant` this round is the right diversity move per
CLAUDE.md's plateau-break guidance, and its plan is no longer "zero concrete
content" (memory rule from round 2) — it now has a specific, falsifiable
first step. The `greedy-reduction-geometric` / `dyadic-potential-invariant`
coupling noted above is the one thing to keep an eye on next round; it is
not currently a violation since both retain independent partial value.

### Small-case sanity checks run
- Perfect-Pairing corollary: hand-verified algebraically above (p1>p2 case).
- Lemma X′ counterexamples: independently corroborated by two separate
  explorer reports with different concrete numeric instances — consistent,
  no reason to doubt the drop.

---

build set: self-similar-induction-on-n, greedy-reduction-geometric, dyadic-potential-invariant, universal-halving-adversary
