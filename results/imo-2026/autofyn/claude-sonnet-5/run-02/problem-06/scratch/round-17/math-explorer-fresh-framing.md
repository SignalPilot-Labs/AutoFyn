## imo-2026-06 (fresh whole-problem framing lens)

### Distinct openings tried this round (all evaluated concretely, not just cited)

1. **Nonstandard-analysis / ultraproduct compactness** (the dispatch's suggested
   angle, distinct from the already-dead Ramsey/idempotent-ultrafilter attempt
   in round 13). Idea: take a nonprincipal ultrafilter U, form a hyperfinite
   index ν, and study the "germ" k ↦ a_{ν+k} − a_ν as an internal function to
   extract periodicity via overspill. **Verdict: collapses to the same wall.**
   Concretely: for this internal shifted sequence to satisfy any clean
   self-contained recursion (the thing overspill/transfer would need to push
   back down to a real bound), its legality rule would have to depend only on
   a *bounded* amount of history around ν — but legality of a_{ν+k+1} depends
   on gcd > 1 against **every** a_i for i ≤ ν+k, including the hyperfinitely
   many terms before ν. This is exactly the certified **No-Restart Lemma**
   (`lemmas/no-restart-lemma.md`) obstruction transported into the nonstandard
   model: you cannot treat the germ near an infinite index as a fresh
   self-contained instance without already knowing a finite covering core
   governs it — which is FAH itself. So the compactness step needs FAH as an
   input, not a substitute for it. This is a genuinely different vocabulary
   from round 13/15's Ramsey attempts (confirmed not a re-run of those), but it
   independently re-derives the same diagnosis. Do not re-propose a "shift the
   index to infinity and take a limit" argument without first supplying a
   *bounded-memory* justification (which is FAH-equivalent).

2. **Per-prime decomposition**: instead of attacking the joint
   extended-type-intersection question, ask whether each individual prime's
   divisibility indicator χ_p(n) := [p | a_n] (for p a persistent prime) is
   *independently* eventually periodic, with the idea of combining single-prime
   periods via lcm/CRT to get the joint period without ever needing FAH's
   pairwise-type-intersection claim. **Tested numerically** (a_1=187,
   a_1=209, real greedy sequence via `math.gcd`, 4000 terms): both seeds'
   gap sequences ARE empirically eventually periodic (T=484 for a_1=187,
   T=528 for a_1=209 — new concrete data point, not previously recorded
   in current.md), and — as expected — every χ_p for p ∈ Q matches that
   same global period exactly on the tail. But this is the wrong direction:
   χ_p's periodicity here is a *trivial corollary* of already having the
   global period, not an independently easier target. There is no way to
   establish a single χ_p's eventual periodicity in isolation, because
   whether p divides a_n depends on the ENTIRE joint legality computation
   (which candidate wins the race), which is exactly as entangled with all
   other primes as the full problem. **Conjecture-level verdict: this
   decomposition does not disentangle the problem; not a viable independent
   route.** (New negative finding — not documented elsewhere in current.md.)

3. **Transfer-operator / generating-function framing**: model the process via
   a linear operator on a space of "state distributions" (state = residue mod
   some M plus divisibility pattern) and look for a spectral-gap /
   Perron-Frobenius argument forcing eventual periodicity. **Verdict: the
   operator itself is not well-defined without first fixing a FINITE state
   space** (i.e., a finite core S_0 governing legality by residue mod
   L=∏S_0) — exactly FAH's conclusion, not a route to it. Same
   pre-requisite problem as items 1 and the already-dead
   automaton/graph-walk framing (round 11, confirmed equivalent to
   Successor Claim / reversible-transition-map). Not a new corridor;
   flagging only so it isn't independently re-tried.

4. **Hypergraph/hitting-set LP-duality relaxation** (assign fractional weights
   x_p to primes, require Σ_{p|a_i} x_p ≥ 1 for every i, hope a dual/rank
   argument bounds the "essential support"). **Verdict: doesn't get
   traction** — the constraint set (one row per term a_i) grows unboundedly
   with n, so this is an infinite LP; there is no known argument bounding the
   support of an optimal/extremal solution independent of n without already
   assuming the persistent-type finiteness (Finite Core Theorem) that's
   already certified — and even granting that, the LP relaxation is strictly
   weaker information than the exact hitting-set condition FAH needs (a
   fractional cover doesn't imply a genuine shared prime between two SPECIFIC
   disjoint-type terms). This is essentially `hypergraph-transversal.md`
   (already recorded partial/superseded by Finite Core Theorem) with LP
   dressing; not new.

### Crux-corpus mining (combinatorics domain, outside number_theory)

Searched `past_crux_moves_database.json`/`past_problems_database.json` per
`crux_moves_documentation.md` for `eventually periodic` / `periodic` /
`greedy` / `covering system` / `hitting set` / `transversal` / `ultrafilter` /
`compactness` in `technique`/`how_used` text across all three domains.
Closest candidates found:
- **aimo-0077** (combinatorics, extremal-principle): "assume nontermination
  forces a repeating state-cycle, take the minimal-index object acted on
  within the cycle, show restoring it needs a forbidden smaller-index move."
  Checked concretely against our H2 (core-absorption-chain termination) gap:
  this template needs the **finite state space bound already established in
  advance** (their bound is a hard combinatorial ≤2^2008 from the problem's
  physical setup) before the minimal-index contradiction can even be run.
  Our absorption chain's state space (round 16's N(S_k) / M_B object) is
  exactly NOT known finite/bounded a priori — that's the open content of H2
  itself (per `binary-refinement-and-threshold-recursion.md`, M_B is
  provably non-constructive). So this template doesn't transplant without
  first solving H2's own finiteness question — not a shortcut, same
  ordering problem as everything else tried. Worth a second look ONLY if a
  future round finds an a priori finite state-space bound for the absorption
  chain by some other means (not found this round).
- **aimo-0514** (already tried/imported, rounds 5/13 — reversible-transition-
  map; re-confirmed dead per existing notes, did not re-attempt).
- **aimo-0982** (number_theory, modular-arithmetic-and-CRT): "digit
  subsequence sampled at moving indices is eventually periodic by tracking
  the sampling index mod the source's own eventual period" — this assumes an
  ALREADY-periodic source and derives periodicity of a sampled sub-sequence;
  structurally the wrong direction for us (we need to establish the source's
  own periodicity, not propagate a known one). Not analogous.
- No genuinely new corridor for the MAIN FAH crux found in the corpus this
  round, consistent with round 15's conclusion that the gcd-pigeonhole-family
  well (and its adjacent technique families) is exhausted for this exact
  crux.

### Candidate technique(s)
None of the four fresh framings tried this round survive independently of
FAH; all four require a finite covering core / bounded-memory fact as an
input, which is exactly what FAH supplies. This is now independently
reconfirmed (a distinct check from rounds 13/15's Ramsey/König passes) via
four concretely different mechanisms (nonstandard/ultraproduct, per-prime
decomposition, transfer-operator, LP-duality-on-hitting-sets).

### Cheap-kill candidates
None obvious beyond what's already certified (Bounded Gap Lemma, Sandwich
Genericity). No new parity/pigeonhole/injection shortcut surfaced this round.

### Knowledge-base entries to use
No new entries beyond what's already cited workspace-wide (Pigeonhole /
extremal principle, CRT — `knowledge_base.md`). This round's four attempts
didn't reach a point of needing a fresh KB entry; they died on a structural
prerequisite (finite core), not a missing tool.

### Analogous past problems (cruxes)
- `aimo-0077` — minimal-index-in-repeating-cycle contradiction; potentially
  useful for the SECONDARY gap H2 (absorption-chain termination) if a future
  round first establishes an a priori bound on the absorption chain's state
  space by other means; not directly usable as-is (checked concretely, not
  assumed).
- No genuinely new analog found for the MAIN FAH crux itself; `aimo-0514` and
  `aimo-0016`/`aimo-0051` (already tried, rounds 5/9/13) remain the closest
  and are already exhausted.

### Prior progress
Per `current.md`: Finite Core Theorem, Singleton-Side FAH, Confined-GCD
Lemma, Successor-Transport Reduction Lemma, Self-Absorbing Core Theorem,
Termination Criterion Lemma, Literal n=1 Periodicity Theorem, and (round 16)
the fully solved `even-a1-full-periodicity-theorem` (2|a_1 subfamily,
T=1, L=2, unconditional) are all correct and certified. Main crux FAH/
Symmetric FAH/Cofinite FAH/EEA (all proved equivalent-difficulty) remains
open, 17 confirmed-dead direct mechanisms, 11 plateau rounds.

### Dead ends (do not retry)
All 17 previously-recorded mechanisms (see current.md's round-by-round
history) — not re-attempted here. This round adds FOUR more independently-
checked-and-killed candidate framings (see above): nonstandard/ultraproduct
compactness (collapses via No-Restart-Lemma-style obstruction), per-prime
decomposition (trivial corollary of global periodicity, not an independent
route — genuinely new negative finding), transfer-operator/generating-
function (needs a finite state space as an input, doesn't supply one),
LP-duality hitting-set relaxation (infinite constraint set, no known support
bound without already having Finite Core Theorem, and even then is strictly
weaker than the exact intersection FAH needs).

### Small-case / intuition notes (conjectural, not proof)
- New data point: a_1=187 has true empirical gap-period T=484 (not
  previously recorded); a_1=209 has T=528. a_1=4807 needs more than 4000
  terms / a larger window to exhibit its true period within this round's
  time budget (search up to 2000-term tail found no period ≤1000 — larger
  L=∏S_0 expected since |F'|,|F''|=2 there per Reduced-Alphabet Corollary,
  consistent with prior rounds' notes on long transients for wider Q).
- Per-prime indicators χ_p for p ∈ Q match the global period exactly once the
  global period is known — consistent with (not contradicting) FAH being
  true, but gives no new proof leverage as argued above.

### Recommendation to outliner
This round's dedicated fresh-framing sweep (4 genuinely distinct mechanisms:
nonstandard compactness, per-prime decomposition, transfer-operator,
LP-duality) found no surviving new corridor for the MAIN FAH crux — all four
concretely require FAH-equivalent content as an input. Combined with round
15's 4-angle sweep and round 13's Ramsey/idempotent-ultrafilter attempt, this
is now 3 rounds' worth of fresh-framing sweeps (13, 15, 17) all independently
converging on "the general-mechanism well is exhausted." Per CLAUDE.md's
plateau-breaking guidance and round-15/16's own recommendation: the most
promising remaining paths are (a) continue banking secondary/scoped
deliverables (H2/core-termination, the bespoke |F''|=2 narrow case) as
concrete partial results, or (b) seriously consider writing up the current
best conditional/partial result plus the solved 2|a_1 subfamily as the run's
honest final deliverable if no genuinely new mechanism surfaces in the next
round or two either.
