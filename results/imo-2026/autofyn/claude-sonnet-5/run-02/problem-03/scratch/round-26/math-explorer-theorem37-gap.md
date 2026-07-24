# Scouting report: the Theorem 37 "non-maximal-tie" gap (Case (b), v≥a, T'-untouched sub-case)

**Lens assigned:** diagnose whether the repeated round-24/25 overclaim flag
("Theorem 37 does not rule out b tied to a non-maximal element of T'") names
a genuinely distinct hard sub-case, find the smallest instance, hand/numeric-check
it exactly, and propose a mechanism. Not attempting a proof.

## 1. Precise diagnosis — this is genuinely open, not dismissible by an existing lemma

Setup (from `approaches/greedy-halving-adversary.md` lines ~4397–5010, Theorem 36/37):
Case (b), branch v≥a, needs `A(B) ≥ f(n)` where `B = {b}∪T'`, `T' = {p4}∪T''`
(the "T'-leaves-p4-untouched" sub-case), `T''` a legal ≤(n-4)-cut response to
`{p5,...,p_{n+1}}` (using the *full* n-4 budget, since p4 costs 0), and
`b ∈ (0, p4]` (forced by `a+b=p3=2p4`, `a≥b`).

The **Vertex-Minimum Theorem** + **Single-Insert-Point Vertex Lemma**
(`lemmas/single-insert-point-vertex-lemma.md`, certified, elementary) together
say: for *fixed* T', the function `b ↦ A({b}∪T')` is piecewise-affine with
slope ±1, so its minimum over `b∈[0,p4]` is attained at one of the finitely
many breakpoints `{0, p4} ∪ (T' ∩ (0,p4))`. **Theorem 37 (round 23) proves
only the single vertex `b=p4`** (the symmetric split, forced when `a=b=p4`
by `p3=2p4`), via the odd-run-reduction pair-cancellation
`A(B)=A(T'')` followed by the induction hypothesis `(⋆_{n-4})` directly on
`T''` (a full-budget legal response — this is why it terminates in one step).

Neither `single-insert-point-vertex-lemma` nor `vertex-minimum-theorem` nor
any other file on record **resolves which breakpoint is the true minimizer**
— they only certify that the minimizer *is* one of the breakpoints. So the
"b tied to a non-maximal element of T''" vertex (b = some t* ∈ T'', t* < p4)
is a **live, unclosed vertex type of Theorem 37's own claimed domain**, not
subsumed by anything else on file. I checked `vertex-minimum-theorem.md`,
`case-b2-n3-covering-closure.md`, `p-space-chamber-vertex-theorem.md` and
`chamber-a2-p1-tied-to-p2-pair.md` for a general "deep-tie is dominated"
result — none exists; all deep-tie discussion on file is confined to the
*sibling* h(m)/`rank-pigeonhole-budget` problem (the "T'-cuts-p4" sub-case),
not this one. **Conclusion: yes, genuinely open, not cheaply dispatchable.**

At this tie vertex, by the same odd-run-reduction corollary Theorem 37 itself
uses (pair `{t*,t*}` cancels — one copy is `b`, the other is `t*`'s own copy
inside `T''`):
$$A(B) = A(\{p_4\}\cup(T''\setminus\{t^*\})).$$
This is genuinely *not* a full-budget legal response to any rescaled ladder
(`T''\{t*}` has "used up" `t*`'s slot without the usual budget bookkeeping),
so `(⋆_{n-4})` does not apply directly — this is the real content of the gap,
structurally the same shape as the already-acknowledged obstruction in the
*sibling* h(m) problem (Theorem 38/39, `rank-pigeonhole-budget`'s (7.9.1)
deep-tie finding), just on the complementary ("T'-untouched") side.

## 2. Smallest concrete instance, and exact hand/numeric check

**Smallest instance: n=5.** At n=5, budget for T' is n-4=1. Taking `T''`
*untouched* (`T''={p5,p6}={2,1}` in ladder units `p_i=2^{6-i}`, i.e.
`{32,16,8,4,2,1}` for `p1..p6`, well within the budget-1 allowance) already
exposes two deep-tie candidates for `b`: `b=p5=2` and `b=p6=1`, distinct from
the symmetric-split `b=p4=4`. Hand computation (`B={b,4,2,1}`, `f(5)=1` in
these units):
- `b=4` (symmetric, Theorem 37's vertex): `A(B)=A({2,1})=1=f(5)` ✓ (tight).
- `b=2` (deep tie to p5): `A(B)=A({4,1})=3` (pair `{2,2}` cancels) — no violation.
- `b=1` (deep tie to p6): `A(B)=A({4,2})=2` — no violation.

So at n=5 the deep-tie vertex is not the global minimizer for this
particular `T''`, but it becomes the **argmin** (the vertex realizing the
row-minimum over `b`, for *some* legal `T'`) once `T''` itself is nontrivially
split — I confirmed this by exact search (below), so it is not a vacuous
case restricted to trivial `T''`.

**Exact-`Fraction` search, script `/tmp/round-26/check_theorem37_gap.py`.**
For n=5,...,9, ladder `p_i=2^{n+1-i}f(n)`, `f(n)=1/(2^{n+1}-1)`: for each of
5,000–8,000 random legal `T'` (random cut-count in `[0,n-4]`, random exact
dyadic-ish split points), I evaluated `A({b}∪T')` at **every** breakpoint
candidate `b∈{0,p4}∪(T'∩(0,p4))` — this is exhaustive per fixed T' by the
certified Single-Insert-Point Vertex Lemma, not a dense/random sample — and
recorded the row-minimum and which candidate attained it.

Results:
- **Zero violations of `A(B)≥f(n)`** across all of n=5,6,7,8 (8000 trials
  each) and the argmin-distribution run (5000 trials, n=5..9): worst case
  found was always *exactly* `f(n)`, attained at the symmetric-split vertex
  `b=p4`.
- **The deep-tie vertex genuinely is the row-argmin** in a rising, non-negligible
  fraction of trials: n=5 ≈2% (97/5000), n=6 ≈18%, n=7 ≈22%, n=8 ≈27%,
  n=9 ≈29%. (`b=0` argmin frequency correspondingly falls from ~19% at n=5 to
  ~1% at n=9.) So the "deep tie beats/ties the top vertex" phenomenon is real
  and *growing* with n — not a measure-zero edge case, matching exactly the
  ~3.7%–46% deep-tie-argmin rates already found on the sibling h(m) problem.
- Despite the deep tie frequently being the argmin, its **value** never fell
  below `f(n)` in any trial — strong (not proof-grade) evidence the
  underlying inequality is true throughout this vertex family too.

## 3. Proposed mechanism for next round

**Key structural observation (new, not on file elsewhere I could find):** at
*every* deep-tie vertex `b=t*∈T''`, odd-run-reduction collapses the target to
$$A(B) = A(\{p_4\}\cup(T''\setminus\{t^*\})) ,$$
i.e. a **single-fragment-deletion** object: the full-budget legal response
`T''` to the (n-4)-ladder tail, with one element `t*` deleted, re-merged with
the fixed top piece `p4`. This is *exactly* the same shape (fixed anchor
element + a legal-response-minus-one-fragment) as the sibling h(m)/(7.9.1)
deep-tie obstruction on the "T'-cuts-p4" side (there it is `A(S\{t})` alone,
here it is `A({p4}∪(T''\{t*}))` — the extra fixed `p4` is the only
difference).

**Recommended framing for next round:** state and attack a single, general
**Deletion Lower Bound** lemma — for a legal (≤m)-cut response `S` to the
unit m-ladder and any `t∈S`, bound `A(S\{t})` (or `A(\{p_4\}\cup(S\{t*}))`
in the p4-anchored variant) from below in terms of `f` at a *smaller* index.
Concretely, worth trying: relate `S\{t}` to a legal response of an
(m-1)-ladder by "absorbing" the deleted slot's mass into its sorted
neighbour (a merge/coarsening move) — this stays inside the induction
tower rather than needing a wholly new technique, and if it succeeds it
would close **both** sibling gaps at once (Theorem 37's non-maximal-tie
case here, and Theorem 38/39's deep-tie case in `rank-pigeonhole-budget`
§7.8–7.9), since both reduce to the identical single-deletion object. This
double payoff makes it the highest-leverage target for round 26, ahead of
re-attacking either sibling gap in isolation.

**What would NOT work (already effectively ruled out by files on record):**
treating `T''\{t*}` as itself a rescaled ladder instance (Cross-Level
Rescaling Lemma needs the *whole* tail, no deletions — this is the identical
obstruction Proposition 39/round 23's diagnostic already established for the
sibling problem, and it transfers verbatim here); and asserting "top-tie
dominates" as a general fact (directly refuted by the argmin-frequency data
above, mirroring the round-24 3000-trial refutation on the sibling side).

## Files consulted
- `results/imo-2026-03/current.md` (round 23–25 entries)
- `results/imo-2026-03/approaches/greedy-halving-adversary.md` (Theorem 36,
  Theorem 37, the round-23 diagnostic finding, round 24's h(m)/Theorem 38
  section, round 25's Proposition 39/Theorem 39 section)
- `results/imo-2026-03/lemmas/theorem-38-h1-exhaustive-closure.md`
- `results/imo-2026-03/lemmas/theorem-39-h2-closure.md`
- `results/imo-2026-03/lemmas/proposition-39-mass-conservation-obstruction.md`
- `results/imo-2026-03/lemmas/single-insert-point-vertex-lemma.md`
- Numeric verification: `/tmp/round-26/check_theorem37_gap.py` (exact
  `fractions.Fraction`, no floats; reproducible, seeds fixed).
