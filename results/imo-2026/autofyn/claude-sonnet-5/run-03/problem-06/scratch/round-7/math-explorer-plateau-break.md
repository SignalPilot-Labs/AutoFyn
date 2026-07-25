## imo-2026-06 (plateau-break lens: scalar-difference-pigeonhole / scalar-difference-majorization)

### Verdict on the assigned lens: this framing has hit its wall — recommend deprioritizing (not necessarily deleting) both scalar-difference-pigeonhole and scalar-difference-majorization

Evidence, read directly from the approach files and independently checked against
the reasoning (not re-derived from scratch, but re-verified logically):

1. **Round 5** opened the framing as "structurally independent — pure integer
   arithmetic on `(a_n)`'s own values, no prime-set bookkeeping." Free results:
   pigeonhole (`Y_T` infinite), Positive-Density Upgrade (`limsup` density
   `≥1/(TR−T+1)`), Sharpened Bounded-Gap Lemma. Both attempted upgrades to
   syndeticity (Fekete/Cesàro-average; combine density+gap-bound) **stalled**,
   diagnosed honestly as needing "which primes recur when" — i.e. reducing back
   to the Q/Nec machinery this framing was meant to avoid.
2. **Round 6** forked into two mechanisms and killed both:
   - `scalar-difference-pigeonhole`'s Morse-Hedlund reformulation: proved
     Theorem 6.2.2 (Unified Central Claim ⟹ `p(k)≤T` exactly) — but this is
     **conditional on already having Q** (imports
     `transient-free-finishing-theorem.md`), so it supplies no independent
     leverage. The converse direction (bounded `p(k)` ⟹ IMO conclusion) needs
     **two separate un-closed gaps** (Morse-Hedlund only gives *eventual*
     periodicity, and no transient-removal argument exists outside the
     Q-machinery — §6.3 Gap (i),(ii), explicitly conceded by the builder).
   - `scalar-difference-majorization`: proved the Excess Growth Rate Lemma —
     a **provably circular** obstruction: any single-affine-rate candidate
     needs `c = L/T` exactly, and `L/T` is exactly the theorem's unknown
     output. This is now certified as a negative lemma
     (`lemmas/excess-growth-rate-lemma.md`).
3. Pattern across both forks, checked and confirmed sound (not a strawman):
   **every route this framing has tried to close its own "syndeticity" or
   "majorization" gap terminates in "first you must already know `(T,L)`/`Q`"**
   — i.e. the framing has *proved*, not merely observed, that it cannot make
   progress independent of the shared Q/Nec central gap it was opened
   specifically to avoid. That is a structural dead end, not a technique
   failure — three rounds (5, 6, 6-fork) converging on the same reduction from
   different angles is exactly CLAUDE.md's "stuck shared gap ⟹ direction is
   wrong" signal.

**What's still nominally open in this framing** (listed for completeness, not
recommended as the next lever): Mechanism B (ISL 2015 N6 / `aimo-0680`-style
sandwich, needs an independent substitute divisibility fact for
`d | a_{n+d}-a_n`-type relation — searched for one and found none across 2
rounds; no new idea surfaced this round either). Not worth another round
without a genuinely new substitute-fact idea, which none of my searches this
round produced.

### Two genuinely different top-level framings (far from all 5 live approaches)

**Framing A (primary recommendation): explicit covering-system CONSTRUCTION +
exchange/local-optimality argument, instead of existence-via-pigeonhole.**

All 5 live approaches (and both scalar-difference forks) try to prove `Q`
(or `L`, or the rate `c`) **exists** via an indirect/existential mechanism
(pigeonhole, minimality, induction on seed structure). None of them
*constructs* a candidate `Q`/`L` directly and then proves the greedy
sequence must match it. Propose instead:

1. **Construct** an explicit finite set of primes `Q^\star` and modulus
   `L^\star := \prod_{q\in Q^\star} q` via a classical Erdős-style covering-system
   recipe: start from `R(a_1)`, and greedily add the smallest prime `p \notin Q`
   such that the "density deficit" (the density of integers not yet forced to
   share a factor with every sufficiently long window of the sequence, in the
   Jacobsthal-density sense already used by `jacobsthal-covering-bound`) drops
   below a fixed threshold, **stopping the construction after a bounded number
   of steps determined purely by `\mathrm{rad}(a_1)` and the certified
   `bounded-gap-via-rad-a1.md`** (not by observing the true sequence). This
   differs from `jacobsthal-covering-bound` (deprioritized, stuck on
   *proving* `K(a_1)` bounded) by inverting the order of attack: instead of
   trying to prove the greedy sequence's *own* enlargement process
   `\Lambda^{(K)}` stabilizes, build the covering system **first and
   independently** of the greedy sequence, then prove convergence via a
   **direct exchange/local-optimality argument**: show that if the true
   greedy sequence `(a_n)` ever deviates from the arithmetic progression
   induced by `(Q^\star,L^\star)` at some index `n_0`, minimality of the
   greedy rule (i.e. `a_{n_0+1}` is the *smallest* legal candidate) forces a
   specific, boundedly-checkable contradiction with the covering system's
   density guarantee. This is a genuinely different proof shape (construct →
   verify-by-exchange, not exist → pigeonhole/majorize), and it uses the
   already-certified `bounded-gap-via-rad-a1.md`, `sharpened-bounded-gap-lemma.md`,
   and `minimum-gap-lemma.md` as inputs to the construction step rather than
   as majorization ingredients.
   **Caveat — unverified, not yet cheap-tested**: I did not find time this
   round to run a numerical test of whether such a "density-threshold
   greedy construction of Q^\star" actually reproduces the true `Q`/`L` for a
   handful of seeds (e.g. `a_1=35,99,375,20735`, all already-worked instances
   in the lemma set). **This is the mandatory cheap-kill check before the
   outliner commits to this framing**: if a natural density-threshold
   construction of `Q^\star` disagrees with the true `(Q,L)` on any of these
   four seeds, the framing needs a different construction rule before being
   built out.

**Framing B (secondary, weaker/more speculative): rigidity via a minimal
first-divergence argument between two independently-constructed
completions.** Instead of building one sequence forward, consider two
*a priori distinct* infinite legal continuations of the greedy rule from some
common finite prefix (this is not what the problem's sequence itself is — the
greedy rule is deterministic and unique — but the technique is: assume for
contradiction there exist two proposed periodic tails `(T,L)` and `(T',L')`
both consistent with the sequence's behavior "densely" (or beyond some large
`N`), take the FIRST index where they diverge, and derive a contradiction
from minimality plus a covering-density argument at that single index. This
is closer in spirit to `aimo-0514`'s "assume two runs must coincide by
reversibility" and to `aimo-0077`'s "minimal-index witness ⟹ contradiction
with minimality" cruxes (see below), but adapted to *uniqueness of the
eventual period* rather than *existence*. **I rate this weaker than Framing
A**: it likely still needs the same "local data determines the next term"
ingredient that `windowed-epsilon-automaton-failure.md` already proved
impossible for *bounded* windows — so it would only be a genuinely new
framing if it can be made to work with an *unbounded but structured* state
(e.g. state = current residue mod the *constructed* `L^\star` from Framing A,
not the raw prefix), in which case it essentially becomes the finishing step
of Framing A rather than an independent framing. I recommend the outliner
treat B as a fallback finishing lemma for A, not a fully separate approach.

### Candidate technique(s) / knowledge-base entries
- `knowledge_base.md` "Invariants & monovariants" and "Pigeonhole /
  extremal principle" (already exhausted in various forms by the population).
- `knowledge_base.md` has **no entry on covering systems / Erdős covering
  congruences or on Jacobsthal's function** — this is a genuine knowledge-base
  gap for this problem; if Framing A is pursued, it's worth asking the
  orchestrator to add a covering-systems entry (classical: finite set of
  congruences `a_i (mod n_i)` covering all sufficiently large integers;
  Jacobsthal's function `g(n)` bounds the largest gap between integers
  coprime to `n`).
- No generating-function / formal-power-series technique from `knowledge_base.md`
  applies cleanly here (rationality of a GF is equivalent to eventual
  periodicity, but constructing the GF requires exactly the same finite-state
  data the population is stuck on — this is a repackaging, not new leverage;
  I checked and do NOT recommend it as a distinct framing).

### Cheap-kill candidates
- **Mandatory pre-check for Framing A** (see above): test a density-threshold
  greedy construction of `Q^\star` against the 4 already-worked seeds
  (`a_1=35,99,375,20735`) before committing a round to building it out.
- No cheap parity/pigeonhole kill found for Framing A or B this round; both
  need the numerical sanity check above before further investment.

### Analogous past problems (cruxes)
- `aimo-0678` (ISL, gcd/lcm-coupled recurrence, "eventually periodic") — already
  flagged in `run_state.md` rule (round 5) as the closest analog; its
  frozen-invariant mechanism is proven inapplicable
  (`aimo-0678-mechanism-inapplicability.md`), but its *shape* (bound one
  coordinate, then reduce the other mod the lcm of the bounded coordinate's
  values) is exactly what Theorem 6.2.2 already replicates conditionally —
  no new leverage from re-reading it.
- `aimo-0514` (3-regular planar graph turning-walk, "largest number of visits")
  — its crux ("a deterministic process on a state with unique
  predecessor+successor is reversible ⟹ orbit is purely periodic, not just
  eventually periodic") is a genuinely different *proof shape* than anything
  tried on imo-2026-06 so far, but I could **not** find a way to make it
  transplant: aimo-0514's state space is a priori finite (six turn-types per
  vertex, finitely many vertices) — that finiteness is given, not derived. For
  imo-2026-06 the analogous "state" (the active prime set / type) is exactly
  the unknown-finiteness quantity the whole problem hinges on, so this crux's
  precondition is not available without first solving the central gap. Listed
  for completeness; **do not build directly from it** without first
  establishing finiteness some other way (which is the actual problem).
- `aimo-0341` (IMO Shortlist covering-progressions counting bound) — genuine
  covering-systems / exact-cover theory, but its combinatorial setup (disjoint
  exact covers, bounding the *number* of progressions via a grid/Hall's-lemma
  argument) doesn't match our "self-sufficient but not necessarily disjoint,
  not necessarily exact" covering condition closely enough to transplant a
  specific lemma — useful only as motivation that "explicit covering-system
  construction" is a legitimate, well-studied technique family, not as a
  source of a specific transplantable move.
- `aimo-0077` (German MO, card-flipping game, prove termination) — its crux
  ("assume nontermination, get a repeating cycle in a *finite* state space,
  take the minimal index acted on within the period, contradict minimality")
  is the same reversibility/minimal-witness shape as `aimo-0514`; same caveat
  applies (needs a priori finite state, which we don't have). Not directly
  transplantable, listed for completeness only.

### Prior progress
See `results/imo-2026-06/current.md`: central gap (finiteness of `Nec`/
self-sufficiency of `Q_min`) open after 6 rounds; even-seed sub-case fully
solved (`even-seed-universal-lock-theorem.md`); 9-10 dead mechanisms recorded
in `run_state.md` Rules. scalar-difference-pigeonhole/majorization's furthest
progress: Theorem 6.2.2 (conditional exact factor-complexity bound) and the
Positive-Density Upgrade / Sharpened Bounded-Gap Lemma (both free but
insufficient).

### Dead ends (do not retry)
All items already listed in `run_state.md`'s Rules section (9-10 mechanisms)
apply. Specific to this round's lens, freshly confirmed as dead (not
re-attempted, only re-verified from the approach files):
- Single-affine-rate majorization (any constant `c`, including any rate
  extracted from Positive-Density Upgrade) — `excess-growth-rate-lemma.md`.
- Window-sum-counting bound on factor-complexity `p(k)` — killed round 6.
- "Two/three consecutive matches propagate forever" for `Y_T` membership —
  killed round 5, `a_1=99, T=1`.
- Morse-Hedlund's converse direction as an independent route — proven to need
  two separate un-closed gaps (§6.3 of `scalar-difference-pigeonhole.md`), not
  merely "harder," genuinely blocked without new input.

### Small-case / intuition notes (conjecture, not proof)
- No new small-case computation was run this round (time was spent on
  structural/logical re-verification of the plateau and on crux-corpus
  search); the four seeds `a_1=35,99,375,20735` already have fully worked
  `(a_n)`, `(T,L)`, and `Q`/`Nec` data in the existing lemma files and should
  be reused (not recomputed) as the test bed for Framing A's cheap-kill check.
