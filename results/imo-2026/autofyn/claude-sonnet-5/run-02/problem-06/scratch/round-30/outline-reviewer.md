# Outline review — round 30 (imo-2026-06)

## 1. a1-19q-subfamily-theorem (new) — APPROVE

Independently re-derived every numeric claim from scratch (fresh sympy-based
literal greedy simulator, `for all i` legality, not reusing the explorer's
code):

- **Bad(19) reproduced exactly.** Ran `a_1=19q` for every prime `q` in
  `(19,20000)` (2254 primes), checking the first 8 terms against the literal
  `T=1,L=19` formula. Got **exactly {23,29,31,37,43,53,73}** — matches the
  outline/explorer's claim digit for digit, with a completely independent
  simulator.
- **Diagonal + parity/mod-5 mechanism reproduced.** For each of the 7
  exceptions, computed `r = q mod 19` and the claimed window
  `{q+1,...,q+n_0-1}` with `n_0=1+(q-r)/19`:
  - `q=23,29,31,37` (`r=4,10,12,18`): window length 1 = `{q+1}`, always
    even → shares factor 2 with `K_0=20`. Confirmed for all four.
  - `q=43,53` (`r=5,15`): window length 2, confirmed one element divisible
    by 5 (`44,45` and `54,55`).
  - `q=73` (`r=16`): window length 3, `{74,75,76}`, `75=3·5^2`. Confirmed.
  - All 7 land on the diagonal `j=r` as claimed, consistent with the
    certified Diagonal Characterization Lemma.

This closes the two things I was asked to re-check independently, and both
check out with zero discrepancy. The technique (mechanical instantiation of
the already-certified p-uniform machinery) is exactly the 7th repetition of
a 6/6-successful template (p=3,5,7,11,13,17 all APPROVEd this way already),
so there is no technique risk. The only real work left for the builder is
the routine (but non-trivial to write out) 306-cell sieve/threshold closure
for the ~299 non-diagonal cells and the rigorous (not just numeric) writeup
of the diagonal parity/mod-5 argument — both flagged correctly as "must
actually be carried out," not hand-waved by analogy. No changes needed to
the outline itself.

## 2. fah-counterexample-hunt (revise) — APPROVE, with scope discipline

Checked both new sub-targets against the ~30+ dead-mechanism list in
`current.md` / `approaches/*.md`:

- **Prong (a) — adversarial seeds stressing S* stabilization (forcing
  multiple absorption rounds).** Grepped `self-absorbing-by-construction.md`
  (the workspace's dedicated H2-numerics file): across ~52 tested seeds
  (`|Q|=1..7`, primorial, skewed, prime-power) the file explicitly reports
  **`N(Q)=0` on every single tested seed** — i.e. the workspace has *never
  even observed one absorption round*, let alone stressed multi-round
  chaining. So a deliberate search for seeds that force several forced-new-
  prime absorption rounds is genuinely virgin territory, not a repackaging
  of the existing sweep (which happened to always land on immediate
  self-absorption by accident of seed choice, not by design). This is a
  real, new sub-target.
- **Prong (b) — literally-conserved invariant search (residue vectors,
  introduction-order permutations).** Grepped the whole workspace for
  "residue vector", "introduction order", "permutation" in this context —
  zero hits. Round 14's `integer-monovariant-difference-identity` tried 5
  different candidates (running average of gaps, running min of gaps,
  running gcd, persistent-type count, recruited-core size) — all are
  *bounded scalar statistics*, none is a *vector/sequence-structured* object
  like a residue vector or an introduction-order permutation. The outline's
  own framing (only "counts/densities/statistics" are pre-emptively dead,
  per the h1-fresh explorer's Ambient-Statistic Obstruction) is correctly
  applied here — this is a different shape of object, not a relabeled dead
  mechanism.

Both sub-targets pass the distinctness check. The outline is explicit that
a "no counterexample found" result stays `unsolved`, never gets reported as
a proof — good discipline, keep enforcing it. One thing to tighten: step 2's
seed-engineering heuristic ("each absorption round's forced new prime is
itself small enough to trigger yet another round") is a plausible design
principle but not yet a guaranteed construction — instruct the builder that
if the *first* few engineered seeds still show `N(Q)=0`, that is itself a
reportable (negative but real) finding, not a failed round.

## 3. a1-pq-subfamily-theorem (advance, low priority) — CHANGES REQUESTED (housekeeping only, do not give it its own build slot)

The outline already restricts this to a housekeeping-only pass (append the
missing round 21–29 `Approaches tried` entries, refresh `Current best`) and
explicitly instructs not to force either residual gap (general r≠1 k=0
closure; r=1,k≥1,gcd(k+1,j)>1) without a genuinely new idea — correct, this
matches what the consolidation explorer found (no new angle this round). I
am cutting this back further: this should **not** consume a dedicated
proof-builder dispatch at all. Fold the housekeeping edit into the
a1-19q-subfamily-theorem builder's task (it is the one touching current.md
this round for its own APPROVE anyway) rather than spinning up a separate
builder whose only output is bookkeeping. This avoids scope creep risk
entirely — there is no proof content to build here this round.

## Diversity check

The two build-set approaches are genuinely orthogonal in framing: one
extends the certified small-prime constructive machinery (positive,
mechanical, doesn't touch H1/H2), the other is a deliberate plateau-break on
the negative/disprove side of the stuck general H1/H2 conditional theorem.
They do not share a wall — good diversity. The housekeeping-only third item
correctly stays out of a build slot so it can't be mistaken for a third
independent line of attack (it has none this round).

## Ranking

Registered `a1-19q-subfamily-theorem` (new, cold-start 1500) and folded
comparisons into `update_ranking`: it beat `a1-pq-subfamily-theorem`
(mechanical/build-ready vs. genuinely stuck-with-no-new-idea general
target), drew with `a1-17q-subfamily-theorem` (same quality/rigor, not yet
built but independently pre-verified to the same standard as a completed
milestone), `fah-counterexample-hunt` beat the two most comparable dead
FAH-mechanism siblings (`bipartite-network-invariant-fah`,
`core-growth-monotonicity`, `witness-depth-bound` — all confirmed dead-ends
in this workspace), and `a1-13q-subfamily-theorem` (verified milestone) beat
`a1-pq-subfamily-theorem` (still partial/stuck) for the same reason. Ranking
tool applied and stale flags cleared on all touched approaches.

build set: a1-19q-subfamily-theorem, fah-counterexample-hunt
