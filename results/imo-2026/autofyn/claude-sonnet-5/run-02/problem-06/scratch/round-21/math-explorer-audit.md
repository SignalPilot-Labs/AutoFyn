# Round 21 math-explorer report — audit + secondary-gap scouting

## 1. Master Conditional Theorem chain — re-audited, gap-free

Traced the full dependency graph independently (not trusting the round-20
report at face value):

`Free Facts` → `Persistent-Type Pigeonhole` → `Finite Core Theorem` →
`Extended Persistent-Type Pigeonhole` (generic at any core `S ⊇ Q`) →
`Self-Absorbing Core Theorem` (H1+self-absorption ⟹ periodicity for `n ≥
N(S*)`) → `Universal Early Intersection Lemma` (self-absorption alone,
no FAH, ⟹ `P(a_j)∩B≠∅` for early `j`) → `Literal n=1 Periodicity Theorem`
(same two hypotheses as Self-Absorbing Core, extends range to all `n≥1`,
using the Universal Early Intersection Lemma to cover the new range) →
`Termination Criterion Lemma` (H2 ⟺ `(N(S_k))` bounded) → assembled into
the **Master Conditional Theorem** (§2 of `n1-periodicity-reconciliation.md`):
H1 ∧ H2 ⟹ the problem's claim.

**Key finding: §7 (the Ambient-Statistic Obstruction, this round's
replacement for the withdrawn round-19 lemma) is causally disconnected
from this chain.** §0–§2 (the actual reduction to H1/H2) cite only items
#1–#9 of the certified stack (Free Facts through Monotonicity of
Resolution) — none of which depend on or reference §7 in any way. §7 is a
*meta-theorem about which proof techniques cannot close H1*, not an
ingredient the H1/H2 reduction itself relies on. So round 19's circularity
(which was entirely inside §7) never touched §0–§2, and round 20's fix to
§7 is correctly orthogonal to the reduction chain's validity — the report's
claim that "this round's changes don't affect the Master Conditional
Theorem" is accurate, not just asserted.

**Independently re-checked the fixed §7 proof itself for the specific
circularity the round-19 reviewer flagged.** The new argument's soundness
step (construct a formal assignment `σ` agreeing with the true sequence up
to a finite point and diverging after it, then check `σ` satisfies every
*cited* premise because none of those premises' defining formulas reference
data past that point) is a legitimate model-theoretic non-entailment
argument: it does NOT assert `σ` is a realizable second continuation of the
deterministic recursion (which would be circular, exactly as round 19 did
assert) — it only needs `σ` to satisfy the finitely many cited premises,
which is a syntactic/definitional check on those premises' formulas. This
is the same style of argument `escape-cost-vacuity.md` already uses
(checking a cited fact's formula doesn't take `g_m,g_n` as arguments). I
re-verified this is non-circular. The scope walk-back (§7.3: does NOT rule
out occupancy-referencing density ratios / second moment / Borel–Cantelli /
Fourier / LP-relaxation, only their purely-ambient special cases) is stated
honestly and matches what's actually proved.

**Conclusion: the chain is gap-free, and round 20's correction is real,
not cosmetic.**

## 2. Lemma-set cleanup candidates (not urgent)

Skimmed the 58 files in `lemmas/`. Two clusters worth flagging for a future
cleanup pass (no action needed now):

- `escape-cost-vacuity.md`, `density-argument-vacuity-corollary.md`, and the
  new `ambient-statistic-obstruction.md` — the workspace's own round-20 note
  says the third "unifies the two existing certified predecessors... into
  one proof." All three remain separately certified; a cleanup round could
  fold the first two into the third as named special cases rather than
  keeping three files for what is now one proof technique. Not redundant in
  content (the scope note distinguishes them) but redundant in
  *certification bookkeeping*.
- `same-type-triangle-vacuity.md` and `same-type-free-facts-vacuity.md` —
  the round-19 certification note itself already flags the former as "a
  disguised instance of" the latter. Same situation: candidate to
  demote to a one-line corollary of the general lemma rather than a
  standalone file.
- Not a duplicate, for the record: `bounded-gap-lemma.md` /
  `generalized-bounded-gap-lemma.md` and `bounded-witness-lemma.md` /
  `generalized-bounded-witness-lemma.md` are legitimate base+generalization
  pairs, not overlapping content — no cleanup needed there.

## 3. Scouted a 4th restricted subfamily: `a_1 = p^2 q` — negative result

Ran greedy-sequence simulations (fast SPF/factorint + per-prime bitmask
implementation, up to 300,000 terms per seed) on `a_1 = p^2 q` for `p=3`
and many primes `q` (5–47), and spot-checked `p=5` too.

**Finding: this family does NOT structurally vanish the FAH obstruction —
it inherits the exact same open gap as the in-progress `a_1=3q` family,**
just relocated:

- For `a_1 = 9q`, the sequence literally matches the closed form
  `a_n = 9q + 3(n-1)` in every case checked (confirmed exactly for `q=7`
  through 300,000 terms, zero deviation) — this LOOKS like a clean p^k-style
  result at first glance.
- But the underlying mechanism is identical in structure to the *unsolved*
  part of `a1-3q-subfamily-theorem.md`: candidates `a_n+1` (illegal,
  consecutive integers), `a_n+2` Case (a) (`q∤`, illegal via `i=1`) are
  the same; Case (b) (`q|(a_n+2)`) still needs a witness argument, and the
  "odd-n Parity Witness" and "k=0-window criterion" lemmas from that file
  transfer verbatim (they only use `a_n = (\text{base}) + 3(i-1)` generically,
  not the specific value of `a_1`). The genuinely open sub-case (Case (b),
  `n` even, `k≥1`) is exactly as open here as in the `a_1=3q` file — I found
  no elementary reason it closes for the `p^2` exponent.
- Numerically the small-`q` exceptions do NOT disappear cleanly with the
  extra factor of `p`: `q=5` and `q=11` both show an *early, real* lone-`q`
  occurrence for `a_1=9q` (breaking the naive closed form almost
  immediately, e.g. `a_1=45`: lone-`5` at `n=3`; `a_1=99`: lone-`11` at
  `n=5`), while `q=7,13,17,19,23,...` show none through 30,000–300,000
  terms — a different exception set than the `a_1=3q` family's `{5,7,11}`
  exceptions (there `q=7,11` were hand-resolved, `q=5` was structurally
  excluded). This is exactly the confound risk round 20's own §6.2 finding
  warned about: absence of a counterexample in a large but finite window is
  not a structural vanishing, it's the SAME unresolved Jacobsthal-style
  witness-existence question in a new numerical guise.

**Recommendation: do NOT open `a_1=p^2q` as a 4th tractable subfamily.** It
would not be a genuinely new target — it's the same open gap as
`a1-3q-subfamily-theorem` wearing a different seed shape, so a dedicated
approach on it would just duplicate that file's still-open Case (b) content
without adding independent value. If a future round wants a real 4th
family, it needs one where the *elementary mechanism itself* changes kind
(like `2|a_1`'s "zero intermediate candidates" or `p^k`'s "singleton `Q`"
trick) — I found no such candidate among `p^2 q`, `3^k q` variants tried
here; all reduce to the same Case-(b)-witness-existence obstruction.

## 4. Recommendation: commit to the floor deliverable now

15 consecutive plateau rounds (6–20) on H1 itself, 20+ independently
confirmed-dead mechanism families spanning every standard proof style
(pigeonhole/witness-promotion, magnitude/CRT, sieve/density/statistical,
automaton/subword-complexity, algebraic/analytic/logic reframings,
crux-corpus transplant), and this round's own audit finds the *remaining*
theoretically-live surface (occupancy-referencing second
moment/Borel–Cantelli/Fourier/LP-relaxation) has never had a single
concrete attempted instance in 20 rounds that got past the "collapses to
already-dead content" diagnosis — every listed "not yet ruled out" item is
un-ruled-out because no one has found a way to instantiate it with actual
sequence data, not because it looks promising.

**Honest assessment: it is time to commit fully to the floor deliverable
as the terminal answer for H1/H2-general, while still finishing the
in-progress `a_1=3q` subfamily (which is genuinely new, unsolved-but-not-
dead, and close: only one case remains, with a precisely diagnosed
Jacobsthal-style gap).** Reasoning, not a hedge:

- The dead-mechanism graveyard is not merely large, it is *structurally
  exhaustive* by proof-STYLE: every classical technique family for this
  shape of problem (existential witness promotion, magnitude/covering
  arguments, density/statistical arguments in every standard flavor,
  automaton/complexity arguments, and now crux-corpus analogy) has been
  tried and killed by a *specific, named, certified reason*, not by
  fatigue. The round-20 fresh-framing explorer's diagnosis — every style
  that reaches an actual proof attempt implicitly needs an ensemble of
  possible continuations of a deterministic recursion, which does not
  exist without an explicit two-seed construction, and no such
  construction has ever been found feasible (the CRT-glue family's own
  8-order-of-magnitude overshoot is the closest anyone got) — is a
  genuine structural reason, independently re-confirmed by this round's
  audit of §7, not a rhetorical flourish.
- The two "not yet ruled out" occupancy-referencing statistical families
  are not live leads with untried ideas — they are the same four
  sub-families (density ratio, second moment, Borel–Cantelli,
  Fourier/LP) whose AMBIENT special cases are already dead, and nobody
  in 20 rounds has proposed a concrete way to make the occupancy-
  referencing versions say anything, only a scope note that they're
  formally un-refuted. That is a documentation gap, not a promising
  frontier.
- My own attempt this round to find a genuinely new elementary family
  (p^2 q) came back negative in the informative way: it reduces to the
  SAME open witness-existence gap as the in-progress `a_1=3q` approach,
  reinforcing (rather than contradicting) the diagnosis that the
  remaining open content across this whole workspace is really one
  gap (a Jacobsthal-function-style bounded-gap-of-coprimality-witnesses
  result), appearing in slightly different clothes in every subfamily
  tried.
- Against continuing: the run has a strong, real, three-subfamily floor
  (`2|a_1`, `a_1=p^k`, and substantial-but-incomplete progress on
  `a_1=3q`) plus a complete, independently-verified conditional reduction
  of the general problem to exactly two named hypotheses. That is a
  legitimate, well-documented terminal deliverable for an IMO P6-level
  problem where full resolution may simply be out of reach within this
  run's tooling.

**Concrete recommendation for next round:** stop opening new "restricted
subfamily" or "new FAH mechanism" approaches from scratch. Spend the
remaining rounds (a) finishing `a1-3q-subfamily-theorem`'s Case (b)/n-even/
k≥1 gap if a genuinely new idea for the Jacobsthal-style bound appears —
otherwise formally close it out as "partial, gap identified and precisely
diagnosed" — and (b) tightening `n1-periodicity-reconciliation.md` into a
single, submission-ready terminal write-up (Master Conditional Theorem +
the two/three unconditional subfamilies + the honest H1/H2 gap statement)
as the run's actual final answer, rather than dispatching further
speculative H1-mechanism rounds that the evidence says will not land.
