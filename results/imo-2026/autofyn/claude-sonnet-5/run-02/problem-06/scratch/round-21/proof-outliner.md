# Round 21 proof-outliner report

## Context digested

- Read `results/imo-2026-06/current.md` (round 20 review, all approach
  verdicts), all 24 live files in `results/imo-2026-06/approaches/`
  (focused closely on `a1-3q-subfamily-theorem.md` and
  `n1-periodicity-reconciliation.md`), `knowledge_base.md` (no Jacobsthal /
  gap-between-coprimes / covering-system entries beyond the naive single-
  window pigeonhole already known insufficient here), and all three round-21
  math-explorer reports.
- Round 20 status: `partial`, 4 slugs built and independently re-verified,
  the run's floor is two fully unconditional subfamilies (`2|a_1`,
  `a_1=p^k`) plus a gap-free conditional reduction of the general case to
  (H1) FAH-at-terminal-core and (H2) chain termination, both open after 15
  plateau rounds (6–20) on H1 specifically.
- This round's three explorer findings, synthesized:
  1. **Jacobsthal lead (highest value, near-term)**: the `a1-3q-subfamily-
     theorem`'s sole remaining gap (Case (b), `n` even, `k≥1`) is reducible
     to a crude, from-scratch-provable bound `g(n) ≤ 2^{ω(n)}` (elementary
     induction/CRT, no analytic NT) combined with an asymptotic-in-`k`
     comparison, leaving only a residual "small `k`" band to close. The
     explorer flagged, but did not resolve, a uniformity concern: the
     residual band's threshold `k^*(q)` was only bounded per individual
     prime `q`, not shown small/uniform across the infinite family of primes
     `q` — this is a real open sub-gap the builder must confront, not
     silently wave through.
  2. **FAH mechanism search is exhausted, but a genuinely different move was
     flagged**: the fresh-framing explorer's 6th consecutive sweep found
     nothing new with a foothold (every candidate collapses to either
     "ambient ⟹ killed by the round-20 Ambient-Statistic Obstruction" or
     "occupancy-referencing ⟹ collapses into the already-exhausted
     gcd-pigeonhole family"). It explicitly flagged an untried, categorically
     different move: **actively hunt for a counterexample to FAH**
     (falsification-seeking, not proof-seeking) — genuinely far from every
     other approach in the field, satisfying CLAUDE.md's plateau-break
     mandate.
  3. **Audit confirms the chain is gap-free**, finds no new tractable
     subfamily (`a_1=p^2q` reduces to the identical open gap as `a_1=3q`,
     not independent value), and recommends committing remaining effort to
     (a) finishing `a1-3q-subfamily-theorem` and (b) a submission-ready
     terminal write-up of the floor deliverable.

## Field proposed for round 21

**1. `a1-3q-subfamily-theorem` (REVISE)** — highest-value near-term target,
could produce the run's 3rd APPROVE. Updated the file
(`results/imo-2026-06/approaches/a1-3q-subfamily-theorem.md`) with a new
"Outline for round 21" section giving the builder a precise 5-step skeleton:
(1) prove the Crude Prime-Factor Gap Lemma (`g(M) ≤ 2^{ω(M)}` via induction
on `ω(M)`, splitting the window in two and inducting — the scouting report
only sketched this, the builder must complete it rigorously, including the
"both candidates divisible by p" sub-case the report left unresolved); (2)
pin down the EXACT modulus needed (`qK`, not just `K` — the scouting report
was inconsistent about this, and the builder must handle the `q|K` vs `q∤K`
sub-case split explicitly); (3) derive an explicit, computable threshold
`k^*(q)` past which the window provably beats `2^{ω(qK)}`; (4) **explicitly
flagged uniformity requirement** — since `q` ranges over infinitely many
primes, "finitely many small `k` per `q`" is not a valid finite check unless
`k^*(q)` is bounded by a small universal constant (or some other uniform
mechanism closes the small-`k` band for all `q` at once); a per-prime
numerical check repeated over an infinite family is not a proof, and the
builder must say so honestly if this can't be closed; (5) assemble. This
outline explicitly warns the builder against the scouting report's implicit
gap (treating "finite check per q" as if it finishes an infinite family of
primes) so the outline-reviewer and reviewer can hold the builder to it.

**2. `fah-counterexample-hunt` (NEW)** — genuinely different framing after
15 plateau rounds, per CLAUDE.md's mandate to diversify when the field
collapses to one wall. New file
`results/imo-2026-06/approaches/fah-counterexample-hunt.md`, status
`unsolved`. Scoped carefully per the dispatch's instructions:
- **Precise counterexample criterion** (§1 of the file): a genuine
  counterexample needs (a) an explicit, verified-finite self-absorbing
  terminal core `S*` (not assumed), (b) two certified-infinite
  disjoint-base-type extended-persistent types, and (c) either a genuine
  structural argument that they can never intersect, OR (failing that) an
  extremely long, adversarially targeted simulation showing zero
  intersection AND no convergent trend toward eventual intersection — with
  an explicit warning that a raw finite simulation alone is evidence, never
  a proof, and that a "near miss" (bounded-delay intersection, or a decaying
  minority-type frequency) does NOT count as a counterexample.
- **Where to search, deliberately untried territory**: `|Q|≥3` seeds (the
  workspace's existing hard-seed sweeps are all `|Q|=2`), seeds engineered
  via CRT for a deliberately lopsided recruitment race (small prime vs. very
  large prime), and seeds maximizing `ω(a_1)`/`|𝒫'(S*)|` simultaneously —
  explicitly NOT a re-run of the canonical `187/209/221/247` seeds already
  studied to death since round 6.
- **Honest negative-outcome framing**: if no counterexample survives an
  adversarial search, this is new (broader-than-`|Q|=2`) corroborating
  evidence for H1, reported as `unsolved` (not a refutation), additive to —
  not a restatement of — the existing 15-round plateau evidence.
- This approach's top-level target remains the problem's actual claim (per
  CLAUDE.md's "one approach = one complete rival attempt at the whole
  problem"): if a counterexample is found, it would force abandoning the
  Master Conditional Theorem's H1/H2 route for that seed and require a
  different top-level architecture (explicitly future work, not promised
  here); if none is found, that is reported honestly as strengthened (but
  still non-terminal) evidence.

**3. `n1-periodicity-reconciliation` (advance, OPTIONAL this round)** — per
the audit explorer's recommendation to commit to the floor deliverable.
Added a "Round 21 outline" section to the file with a narrow, editorial-only
scope (fold Theorems A/B — and C if `a1-3q` reaches APPROVE — into one
unconditional-floor statement; re-verify §7/§0–§2 mutual consistency after
any changes elsewhere this round; explicitly forbidding any shortening of
the honest H1/H2 open-gap statements). Flagged as genuinely optional this
round: if the outline-reviewer judges build capacity is better spent on the
two slugs above, this can wait — no urgency attaches beyond the general goal
of having a clean terminal write-up ready.

## Explicitly not re-proposed (confirmed dead, per current.md / n1-
periodicity-reconciliation.md §4 and the fresh-framing explorer's report)

Density/statistical family in every flavor (ambient AND the collapse of
occupancy-referencing variants into the exhausted gcd-pigeonhole family),
CRT-glue/covering-congruence, automaton/subword-complexity/EEA,
Kolmogorov-complexity, martingale/renewal/coding-theory/game-theory
reframings, algebraic-NT/generating-function/o-minimality/nonstandard-
analysis/Baire-category reframings, `a_1=p^2q` as a "new" tractable
subfamily (confirmed this round to reduce to the identical open gap as
`a_1=3q`, no independent value), and treating `|Q|=2` as an easy warm-up
subfamily for H1.

## Recommended build set

build set: a1-3q-subfamily-theorem, fah-counterexample-hunt, n1-periodicity-reconciliation
