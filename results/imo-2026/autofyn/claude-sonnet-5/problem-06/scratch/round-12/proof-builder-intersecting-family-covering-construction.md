# Build report — intersecting-family-covering-construction, round 12

## Task
Fill in this round's outline (retargeted Step 2/3: Bounded-Run-Length /
pigeonhole route to `(PD_{S,S'})`) into a complete, rigorous proof, as a
CONDITIONAL theorem per the dispatch: "IF `G` (the coarse `P_1`-core
sequence) is periodic THEN `(PD_{S,S'})` holds," being explicit about what
is proved vs. what remains open.

## What was done
Read the round-12 outline (in `approaches/intersecting-family-covering-
construction.md`), the outline-reviewer's independent verification
(`/tmp/round-12/outline-reviewer.md`, "Central finding 2" — confirmed the
logical bridge is sound and non-circular), the math-explorer's periodicity
data (`/tmp/round-12/math-explorer-pd-density.md`), `current.md`, and the
cited lemma files (`theorem-SW-stabilization-sufficiency.md`, `lemma-RD-
restricted-domination-and-magnitude-bound.md` for Proposition 9.4's exact
`(PD_{S,S'})` statement, `lemma-W2-W3-patch-and-minimal-radical-
reduction.md` for Lemma W3).

Wrote a new **Part 11** in the approach file with three fully proved,
gap-free results:

1. **Lemma BRL-from-Periodicity.** If the coarse core sequence `G` is
   eventually periodic (pre-period `n_0`, period `T`), then for any core
   `S'` with `I_{S'}` infinite, no run of `n_0+T+1` consecutive indices can
   avoid `I_{S'}` entirely. Proved by pure modular-arithmetic/pigeonhole on
   the definition of eventual periodicity — no dependence on `(\dagger')`
   or any other open hypothesis of this workspace, so it does not
   reintroduce the circularity round 11 diagnosed for "eventual
   near-periodicity" (Part 10.3).
2. **Lemma PD-from-BRL.** Bounded-Run-Length with constant `R` gives
   `|I_{S'}\cap[1,N]|\ge\lfloor N/(R+1)\rfloor` for every `N` (elementary
   block-partition pigeonhole), hence `(PD_{S,S'})` with explicit
   `c=1/(2(R+1))`, `i_0=2R+4` — exactly the hypothesis Proposition 9.4
   (round 10, already certified) needs.
3. **Theorem PD-Conditional + Corollary.** Combines the two: IF `G` is
   eventually periodic for a given `a_1`, THEN every doubly-infinite
   disjoint core pair of that `a_1` satisfies both `(PD_{S,S'})` and
   `(PD_{S',S})` with a uniform constant, and hence (via the already-
   certified Proposition 9.4) a uniform conditional `O(\log i)` magnitude
   cap on the pigeonhole witness prime, across every doubly-infinite
   disjoint pair of that `a_1`.

Verified the block-partition pigeonhole formulas and the modular-arithmetic
occurrence-recurrence argument by hand (twice, carefully), and cross-checked
the explicit constants numerically for `a_1=247` (`n_0=0,T=1806`, predicted
`R=1806` vs. actual max observed run lengths `3`/`5` — confirms the bound is
valid, if far from tight, exactly as expected of a worst-case pigeonhole
argument) using a fresh, from-scratch generator (`/tmp/round-12/
work_check.py`), cross-validated against the outline-reviewer's own
independent numbers.

**Honestly attempted, and honestly reported as not closing**, one fresh
angle on the periodicity hypothesis itself (Part 11.5): whether the
already-certified Lemma W3 (admissibility reduces to the `n`-minimal-index
set `M_n`) supports a bounded-state argument for `G`. It does not — Lemma
W3's own certified "Discussion" already records `|M_n|` growing
unboundedly (`a_1=221`: `|M_{199}|=42`), which kills this specific route.
This reconfirms, in the sharper Bounded-Run-Length language, round 11's
general circularity diagnosis (any bounded-state reduction of admissibility
is currently known only via Theorem 2.2, which needs `(\dagger')` itself) —
not a new proof, but a concrete, targeted negative finding rather than a
restatement.

## Outcome
- `(PD_{S,S'})` itself remains **open, unconditionally**, exactly as
  before — the periodicity hypothesis is not proved in general (numerically
  confirmed via two independent KMP-based generators for 4/5 tested
  instances — `4087\to T=64`, `247\to T=1806`, `2747\to T=2062`,
  `4199\to T=105250` — but genuinely inconclusive for the hardest instance,
  `a_1=21528751`, within the tested range `N\le4\times10^5`).
- New, genuinely closed content this round: the **implication**
  "periodicity `\Rightarrow(PD_{S,S'})`" is now a complete, gap-free,
  reusable conditional theorem with fully explicit constants — this is real
  progress the dispatch explicitly said would count, even without closing
  the hypothesis.
- Even granting the periodicity hypothesis in full, the separate Step 5
  reuse/pooling gap (Part 9.6, open since round 10) remains untouched and
  is still needed to close the full Stabilization Conjecture — recorded
  explicitly so this round's progress is not overclaimed as finishing the
  chain.
- Status stays `partial` (correct per CLAUDE.md: an implication is proved,
  its hypothesis is not; the whole problem remains open).

## Files touched
- `results/imo-2026-06/approaches/intersecting-family-covering-construction.md`
  — updated in place: new "Round 12 update" headline section, new
  "Approaches tried (round 12, this round)" section, new "Part 11" (full
  proof of Lemma BRL-from-Periodicity, Lemma PD-from-BRL, Theorem
  PD-Conditional + Corollary, honest status/attempt sections), updated
  "Full proof" placeholder note, three new "Promotable lemmas" entries
  appended at the end. Status kept at `partial`. All prior-round content
  preserved verbatim (no deletions).
- No new file written to `results/imo-2026-06/lemmas/` — per this
  workspace's "Builder proposes, reviewer certifies" contract (CLAUDE.md),
  the three new lemmas are proposed in the approach file's "Promotable
  lemmas" section for the proof-reviewer to certify, not self-certified.
- `/tmp/memory/proof-builder.md` — replaced the least-generalizable
  existing rule (round-11 Lemma-UCR-specific) with a new rule about
  cleanly separating conditional-theorem proofs from hypothesis-closing
  attempts, keeping the file at the 30-line cap.

## Recommendation for next round
- If a future round finds any `H`-independent mechanism for eventual
  periodicity of `G` (or even just the weaker Bounded-Run-Length property
  directly, without full periodicity), Theorem PD-Conditional makes
  `(PD_{S,S'})` an immediate corollary — this is now the single sharpest
  open sub-target for this whole approach's remaining path to the density
  hypothesis.
- Push the `a_1=21528751` periodicity search past `N=4\times10^5` with a
  faster factorization backend (the current generator's trial-division
  fallback beyond its `1.5\times10^8` sieve limit is the bottleneck) — a
  confirmed (even if only numerical) period there would round out the
  evidence base to 5/5 tractable instances.
- Even if periodicity (or Bounded-Run-Length) is eventually proved, Part
  9.6's Step 5 reuse/pooling gap is a separate, independent obstruction to
  the full Stabilization Conjecture and will need its own dedicated attempt
  — flagged again here so it is not forgotten once Step 4 is closed.
