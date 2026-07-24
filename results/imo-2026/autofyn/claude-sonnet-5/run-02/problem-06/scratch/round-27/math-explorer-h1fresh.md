## imo-2026-06 — H1/FAH fresh-corridor hunt (lens: ONE genuinely new corridor, round 27)

### Verdict up front
**No genuinely new concrete corridor found.** This is the second consecutive round
(26, 27) of a dedicated "fresh H1 corridor" search returning a clean negative — 20
consecutive plateau rounds (6-26) on H1 itself is now reinforced by two back-to-back
targeted searches that each independently swept a different slice of technique-space
and found nothing live. I did not manufacture a fake corridor; below is exactly what
was checked and why each candidate either restates an already-dead mechanism or hits
the same certified/diagnosed wall.

### What round 26 already ruled out (read first, not re-proposing)
Per `/tmp/round-26/math-explorer-h1-fresh.md` and the `current.md` dead-mechanism
trail: ambient statistics (all kinds, certified `ambient-statistic-obstruction.md`),
occupancy-conditioned statistics (density-ratio/2nd-moment/Borel-Cantelli/Fourier on
the REALIZED occupation vector — checked and found practically blocked by the same
local-density obstruction, not a live loophole), sieve/density on the path-dependent
index set (`triangle-consistency-pigeonhole.md` §5.3), singleton-witness variants,
competitor/CRT-glue constructions, orbit-merging/additive-offset dichotomy (circular —
see below, I independently re-confirmed why), priority-argument/computability,
o-minimality, nonstandard analysis, spectral/operator, Kolmogorov complexity,
martingale/optional-stopping, renewal theory, Rauzy graphs, coding theory, game theory,
Zsigmondy, Dirichlet-in-APs, amortized charging/exchange-cost, reversible-transition-map/
automaton bijection (round 5, proved S-sufficiency ⟺ gap(†) itself — not a bypass).
Also: weakening H1 to a syndetic/density-1 version was checked and found NOT sufficient
for the actual finish (`covering-system-construction.md` Step 5 needs the literal
finite-exceptions form).

### This round's search: combinatorics/algebra crux domains for the missing ingredient
Per the dispatch, I queried `past_crux_moves_database.json` directly (exact field
names per `crux_moves_documentation.md`) across combinatorics and algebra domains not
yet exhaustively mined, specifically for "existential-to-universal/cofinite promotion"
and "local density control" moves:
- Full-corpus keyword scan (2434 cruxes) for `eventually periodic`, `infinitely often`,
  `cofinite`, `absorb`, `syndetic`, `coupling`, `path-dependent`, `two runs`: surfaced
  ~40 hits, all either (a) already-transplanted-and-dead in this workspace
  (aimo-0016, aimo-0051 — flagged by memory rule, do NOT re-propose), (b) require an
  explicit closed-form/finite-ambient-state-space (aimo-0678, aimo-0982, aimo-0514,
  aimo-0648, aimo-1025 — all presuppose a state space the greedy recursion does not
  independently have), or (c) are algebraic/functional-equation orbit-merging arguments
  that need a FOR-FREE, unconditional, closed-form coincidence identity between two
  orbits, supplied directly by evaluating the functional equation at specific inputs
  (see below, aimo-0907 — the single most structurally relevant new find this round).
- `combinatorics/invariants-and-monovariants` (181 entries), `combinatorics/
  extremal-principle` (166), `combinatorics/processes-and-algorithms` (48),
  `combinatorics/linear-algebra-method` (16), `algebra/sequences-and-recurrences` (108):
  skimmed via keyword filter; nothing beyond the hits above resembles an "occurs
  infinitely often ⟹ occurs cofinitely" promotion for a recursively/adaptively
  (not closed-form) defined index set.

**New finding this round: aimo-0907 (IMO 2022-style FE, "orbit index offset"
technique) examined closely and confirmed NOT a live opening, with a precise reason.**
Its crux (`algebra/functional-equations`, technique: "Build an additive integer index
on orbits that eventually merge... show it is well-defined... pin it from one base
coincidence") is exactly the shape of this workspace's already-dead
`orbit-merging-additive-offset-dichotomy` (round 22, RETHINK — confirmed circular).
The reason aimo-0907's version WORKS there but this workspace's attempt does NOT: in
aimo-0907, the functional equation directly hands you, for EVERY input `a`, an
unconditional closed-form coincidence `f^{a²+1}(a-1) = f^{a²}(a)` (from evaluating
`E(a,-1)` — pure algebra, no case-dependent history) — this is what lets the offset
`X(a,b)` be pinned globally without first knowing periodicity. Our greedy sequence has
no such closed-form coincidence between two divisor-class orbits: whether/when
`ρ_S(n) = ρ_S(m)` for two indices depends on the entire adaptive legality history (which
prime happened to already supply `gcd>1` at every intermediate step), not on a formula
you can evaluate independently of the recursion. This is the same "no closed
form/independent local-density control on a path-dependent index set" obstruction
`triangle-consistency-pigeonhole.md` §5.3 already diagnosed, now confirmed to also kill
this specific, previously-uncompared crux (aimo-0907) rather than merely restating the
already-tried aimo-0016/aimo-0051/aimo-0477 transplants. **Net effect: one more
confirmed-dead analog identified, no new lever.**

### Computational stress test (per dispatch instruction)
Wrote an independent bitmask-based greedy simulator (`/tmp/h1explore/sim.py`) plus a
direct-gcd simulator for very-large-prime seeds (`/tmp/h1explore/direct_gcd.py`,
needed because a naive SPF sieve up to `40·a_1` is infeasible once `a_1` has a
~10^7-scale prime factor — sieving would need a multi-GB array). Tested:
- `a_1 = 11305` (known hard `|Q|=4` seed) to `N=60000`: reproduces the already-known
  qualitative picture (many small-count "rogue" disjoint-base-type pairs at the raw-`Q`
  level, consistent with all prior rounds' findings on this seed — this is at the
  un-enlarged `Q` level, not the certified `S₀`-enlarged extended-type level, so it is
  not itself a new FAH check, just a sanity confirmation the simulator is right).
- **New CRT-lopsided seeds** (one huge prime `10000019` combined with 1-3 small
  primes): `a_1 = 3·10000019` (`|Q|=2`), `a_1 = 3·7·10000019` (untested further, time
  budget), `a_1 = 3·5·7·10000019` (`|Q|=4`, to `N=4000`). **Conjecture (small-case,
  not proof) from this new class:** the huge prime is effectively "exiled" —
  it appears in `Q` but essentially never recurs as part of any persistent base type
  in the tested window (0 occurrences among persistent 2nd-half types at
  `a_1=3·5·7·10000019`); the persistent dynamics collapse to exactly the same
  qualitative small-prime cycling already studied in the certified `a_1=3q`/`a_1=pq`-
  family theorems and the `11305`-style hard seeds (disjoint-base-type pairs occur
  among the small primes only). **No qualitatively new class of behavior was found** —
  lopsided CRT configurations look like a degenerate/easier case (fewer live primes
  in practice), not a harder or structurally different one, within this round's
  (modest, ~4000-40000 term) reach. This is weak, small-scale evidence, not a proof,
  and does not rule out a huge prime recurring at much larger `N`.
- Did not reach genuinely large `|F'|≥3` (three-way mutually-disjoint persistent
  extended types) stress seeds at the enlarged-`S₀` level within this round's time
  budget — building `S₀` correctly (Finite Core Theorem's canonical-witness
  enlargement) from scratch is itself a nontrivial multi-step computation (as
  round-25's reviewer noted when it declined to attempt it under time pressure); a
  future round with a dedicated computational slot could push this further, but it was
  not reached here.

### Candidate technique(s)
None new for H1 itself. The productive frontier remains, as round 26 also concluded,
the subfamily-theorem track (`a1-pq-subfamily-theorem`'s per-`p` `Bad(p)` computation;
`a1-3qk-subfamily-theorem`'s `m≥4`) and H2's untried "attack `N(S_0)=0` directly on the
explicit `S_0`" mechanism (memory rule, round 23) — neither is a new H1 corridor.

### Cheap-kill candidates
None obvious for H1 itself.

### Knowledge-base entries to use
No new `knowledge_base.md` entries surfaced as applicable to H1 (consistent with
rounds 19-26's exhaustive sweeps).

### Analogous past problems (cruxes)
- **aimo-0907** (new this round) — examined in detail above; structurally the closest
  un-transplanted analog in the corpus, but confirmed dead-on-arrival for the same
  reason as `orbit-merging-additive-offset-dichotomy`: it needs a for-free closed-form
  orbit-coincidence identity that the greedy recursion does not supply.
- aimo-0016, aimo-0051, aimo-0477 — already transplanted and dead (do not re-propose,
  per standing memory rule).
- No genuinely new analog found beyond aimo-0907.

### Prior progress
Unchanged by this round's exploration: Master Conditional Theorem (gap-free) reduces
the general case to H1+H2; 6 certified subfamily theorems/APPROVEs to date (`2|a_1`;
`a_1=p^k`; `a_1=3q`; `a_1=3^a q`, `a∈{1..5}`; `a_1=5q`, `q∉{7,13,19}`; plus standalone
`a_1=3q^2`, `a_1=3q^3`); certified `p`-uniform `a_1=pq` machinery (`Bad(p)` open for
`p≥5`); the `a_1=4807` single-seed literal Joint FAH closure (Finite-Window
Literalization Lemma). H1 itself: 20 consecutive plateau rounds (6-26), unchanged by
this round.

### Dead ends (do not retry)
All previously-catalogued ~30+ mechanisms (see list above and `current.md`'s full
history) — this round adds no new certified-dead mechanism to that list, only a new
confirmed-dead *analog check* (aimo-0907, functionally the same failure mode as
`orbit-merging-additive-offset-dichotomy`). Do not re-propose: ambient or
occupancy-conditioned statistical methods, weakened/syndetic H1, automaton/reversible-
transition-map framings, or any orbit-index-offset construction (algebraic or
otherwise) that needs a for-free closed-form coincidence between two divisor-class
orbits — the greedy recursion's adaptive, history-dependent legality rule structurally
lacks one.

### Small-case / intuition notes
New this round (conjecture, small-scale, not proof): CRT-lopsided seeds (one very
large prime factor of `a_1` alongside a few small ones) show the large prime becoming
dynamically inert/exiled after the initial transient, with persistent behavior driven
entirely by the small primes — i.e., lopsided seeds look like a degenerate case of the
already-well-studied small-prime family, not a new hard regime. This is consistent with
(does not contradict) all prior rounds' seed sweeps; it does not suggest a
counterexample to H1, nor does it suggest a new proof lever.
