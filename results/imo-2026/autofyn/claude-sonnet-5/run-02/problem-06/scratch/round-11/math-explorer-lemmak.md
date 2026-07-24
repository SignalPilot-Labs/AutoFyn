# Math-explorer report — Lemma K (Adjacent-Multiple-Blocking) lens, round 11

## Assignment
Investigate concretely (with numerical experiments) whether the now-certified
Confined-GCD Lemma and Window Resolution Lemma can be combined with round-7's
Lemma K (blocking-index extraction from illegal greedy competitors) to finally
control the factorization relationship that round 7 diagnosed as missing. Do NOT
attempt a proof; report the terrain.

## Bottom line
**Stalls, and the experiments pin down precisely why, more sharply than round 7's
qualitative diagnosis.** Confined-GCD and Window Resolution do not close Lemma K's
factorization-control gap because the two mechanisms' informative primes live in
**structurally disjoint universes by construction**: Lemma K's generic
blocking-index witness is `a_1` (or another early, S0-heavy term) sharing an
`S0`-prime with `a_n`, while Confined-GCD's control is specifically over
`F''`-primes (the primes OUTSIDE `S0` that rogueness confines `gcd(a_n,a_{n_B})`
to). These sets are disjoint by the very rogueness argument that makes
Confined-GCD provable, so gluing the two facts together adds no traction. Window
Resolution turns out not to be the relevant obstruction for Lemma K at all (see
below) — a genuinely new, sharper finding than assumed by the round-10 dispatch
note.

## Setup used (reproducing the workspace's standard test bed)
`a_1 = 4807`, greedy sequence generated to `N=1500`–`2500` terms by trial
division/exact gcd (sympy), `S0 = {2,3,5,7,11,19,23,73,127}` (matching
`greedy-exchange-cost-potential`'s round-10 `Q ∪ S`), `Q = P(a_1) = {11,19,23}`.
Extended types `ρ(n) = P(a_n) ∩ S0` computed for all `n ≤ N`; this reproduces the
workspace's known type `{3,5,19}` at indices `[6,561,1114,2223]` exactly, confirming
the generator matches prior rounds'.

### A genuine rogue pair with a *nontrivial* Confined-GCD alphabet
Searched all pairs of disjoint persistent types for one where `F'∩F''≠∅` **and**
`Div(b)` has more than the trivial `{1,q*}` (i.e. `D_bad ≠ ∅`, unlike the
`a_1=11305` case flagged in `cofinite-window-capacity-bound` as vacuously done).
Found: `A' = {3,19,5}` (`n_A=6`, `a_6=4845`), `B' = {2,11}` (`n_B=7`,
`a_7=4862=2·11·13·17`). `F' = {17}`, `F'' = {17,13}`, `q* = 17`, `b = 13·17 = 221`,
`Div(b) = {1,13,17,221}`, `D_bad = {13}`.

- Checked every sampled `A'`-occurrence past `n_B` (`n = 561, 1114, 2223`): in
  **all three**, `q*=17 | a_n` (no observed FAH failure) — consistent with 10
  rounds' worth of failure to find any counterexample.

## Experiment 1 — generic Lemma K behavior across the sequence (q ranging over S0)
Applied Lemma K's construction `c := q·⌊a_n/q⌋` at ~230 sampled `(n,q)` pairs
(`n` up to 1500, `q ∈ S0` with `q∤a_n`), recording branch and (for branch (b)) the
full set of blocking indices and the primes shared between `a_n` and each blocker.
- Branch (b) (the informative branch) fires **350/424 (~83%)** of sampled cases.
- Over **11,107** shared-prime events collected from *all* blockers found (not just
  the first): **3423 in `Q`, 7449 in `S0\Q`, only 235 (~2%) outside `S0`** (pure
  "junk" primes, e.g. 37, 43, 53, 13, matching the round-3 "junk-prime
  contamination" phenomenon) — **zero** tied to any `F'`/`F''`-type prime.
- The **smallest** blocking index `j` (the natural witness Lemma K's proof
  extracts) is `j=1` in **223/234 (~95%)** of branch-(b) cases; the rest are all
  small (`j ≤ 7`), never growing with `n`.

## Experiment 2 — the actually-relevant prime: q = q* = 17 directly
Repeated the exact Lemma K construction with `q := q* = 17` (the rogue pair's own
canonical prime) at every sampled `n` with `17 ∤ a_n` (500 samples, `n` up to 1500):
- Branch (b) fires 334/451 times.
- Smallest blocking index: `j=1` in **296/334 (89%)**, and `j ≤ 5` in **332/334
  (99.4%)** — so the witness index is empirically **well-localized, not
  unboundedly growing** (unlike the Escape-Budget mechanism's Growing-Constraint
  Obstruction — see below, this is a genuinely different situation).
- Shared prime between `a_n` and the blocking `a_j`: **338 events in `Q`, 46 in
  `S0\Q`, 0 outside `S0`, and — the decisive number — 0/384 equal to `q*` itself**.
  Lemma K's blocking mechanism, applied with the actual target prime `q*`, never
  once produces `q*` (or any `F'`/`F''`-prime) as the shared/blocking prime; it is
  always an `S0`-core prime, overwhelmingly literally `Q = P(a_1)`.

## Diagnosis: why Confined-GCD does not rescue Lemma K
Confined-GCD's content is: for an ACTUAL sequence term `a_n` with `ρ(n)=A'`,
`gcd(a_n,a_{n_B})` is confined to `Div(b)`, and its prime factors are confined to
`F''` — this confinement is proved (Confined-GCD's proof, part (a)) precisely
*because* rogueness (`A'∩B'=∅`) rules every `S0`-prime OUT of `g_n`. That is the
lemma's whole mechanism: it controls the non-`S0` residue of a gcd.

Lemma K's blocking-index construction, empirically, produces its usable
(branch-(b)) content almost entirely via the *opposite* pole: the witness `a_j`
(overwhelmingly `a_1` itself, or another early low-index term) blocks `c` because
`c` misses one of `a_j`'s `S0`-primes — the shared prime `P(a_n)∩P(a_j)` found by
the construction is, by the numbers above, essentially always an `S0`-prime (or
occasionally an uncontrolled junk prime outside `S0` altogether), and **never**
the `F'`/`F''`-prime `q*` that Confined-GCD is built to control. So the two
lemmas' "useful primes" occupy disjoint, non-overlapping subsets of `P(a_n)` by
construction — combining them does not produce a new fact, because Confined-GCD
has nothing to say about `S0`-primes (it explicitly excludes them) and Lemma K's
generic witness has nothing to say about `F''`-primes (it never touches them).
This is a sharper, numerically confirmed version of round 7's qualitative
diagnosis ("no established relationship between `P(c)` and `P(a_n)`") — the gap
is not merely "unestablished," it is empirically a structural mismatch between
which prime-classes the two tools each see.

## A genuinely new sub-finding: Window Resolution is not the relevant obstruction here
Round 10's dispatch note framed the hoped-for repair as "Lemma K anchored to the
NOW-CONTROLLED finite alphabet `Div(b)`... directly repairing Lemma K's
factorization-control gap." But Window Resolution / the Growing-Constraint
Obstruction (which killed the sibling Escape-Budget mechanism) is about a
DIFFERENT construction: Escape-Budget's competitor `c` ranges over the whole
telescoped window `(a_{n_j},a_{n_{j+1}})`, so its witness index `i(c)` provably
ranges over an unboundedly growing pool as the window widens. **Lemma K's `c` is
anchored to a single fixed `n`, not a window** — Experiment 1/2 show its witness
index is empirically small and non-growing (`j≤7` essentially always, dominated
by `j=1`). So Lemma K does NOT inherit the Growing-Constraint Obstruction in the
form that killed Escape-Budget; its failure mode is different and, per the data
above, arguably *worse* for closing FAH: the witness is well-localized but
*uninformative* (always an `S0`-prime, structurally disjoint from the `F'`/`F''`
alphabet Confined-GCD controls), rather than *informative-but-unlocatable*. A
future attempt should not expect "controlling the witness index" (which Window
Resolution-style tools address) to help Lemma K at all — the open problem is
entirely about which PRIME the witness shares, not WHICH INDEX it is.

## What new ingredient would actually be needed (per Minimality Tautology Lemma's
scope correction)
The certified Minimality Tautology Lemma explains that Lemma K's blocking
mechanism is a forced, tautological consequence of greedy minimality — it will
always fire, for any `c<a_n`, with SOME blocking index, no matter how `c` is
built. What it does *not* and cannot supply is control over *which prime* the
blocking uses. The experiments above show the deep reason: the dominant blocker is
`a_1` (or another `S0`-saturated early term), and `a_1`'s own prime set is fixed
and disjoint from `F'`/`F''` by definition (`S0 ⊇ Q = P(a_1)`, and `F'`/`F''` are
defined as `P(a_{n_A})\S0` / `P(a_{n_B})\S0`). So no refinement of Lemma K's
construction rule for `c` (rounding down vs. up, choosing a different modulus,
etc.) can escape this: as long as `c` is `O(q)`-close to `a_n`, and `a_1` (or
another `S0`-heavy low-index term) is "cheap" to fail against, the greedy rule
will preferentially route the illegality witness there. What would be needed is a
tool that **excludes `S0`-primes as possible blockers** (forcing the witness index
into the `F'`/`F''`-relevant range) — i.e. a strengthening of Lemma K to show
branch (b)'s witness `j` can be chosen with `P(a_j)` NOT contained in `S0`
whenever some auxiliary condition holds. No certified lemma in the workspace
supplies this (Free Facts, Confined-GCD, Window Resolution, Minimality Tautology
all either work only with `S0`-primes or only with `F''`-primes at the single
fixed index `n_B`); this is a precisely-scoped, currently-open sub-question, not
previously stated this precisely in the workspace's prior round files.

## Recommendation for next round
Lemma K should be considered **re-stalled with a sharper diagnosis**, not
resurrected by Confined-GCD/Window Resolution as hoped. If a future round wants to
keep pursuing negative/illegality data (the one information source distinct from
the twelve dead existence/magnitude mechanisms), the concrete open sub-question to
attack is: *can any construction of `c` force its blocking witness `j` to have
`P(a_j) ⊄ S0` (ideally `P(a_j) ∩ F'' ≠ ∅`)?* This is a different, more specific
target than "combine Lemma K with Confined-GCD" as dispatched, and the numbers
above show why the as-dispatched combination alone does not work — it needs a new
result, not a splice of the two already-certified lemmas.

## Reproducibility
All experiments run via Python (`sympy`) in this session; scripts left at
`/tmp/round-11/experiment.py`, `/tmp/round-11/search.py`, `/tmp/round-11/lemmaK.py`,
`/tmp/round-11/lemmaK_broad.py`, `/tmp/round-11/lemmaK_deep.py`,
`/tmp/round-11/lemmaK_qstar.py` (not part of the permanent workspace; rerun if
independent verification is wanted).
