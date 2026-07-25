## imo-2026-06 — lens: growth-vs-density / recruitment-counting

### Scope note
Everything except the **Finite Alphabet crux** (𝓐_∞ finite, equiv. Π=primes(L)
finite) is certified (see `lemmas/no-transient-fixed-successor.md`,
`lemmas/free-lemmas.md`). This report only scouts that one crux, from the
growth/density/counting angle. No proof attempted.

### Distinct sub-openings within this lens

1. **Distance–prime + linear-growth density bound (the "standard" density
   argument, already sketched in §7(c) of `redundant-constraint-antichain.md`,
   NOT completed).** By L3 (Distance–prime), if prime `q` divides two terms
   `a_i,a_j` then `q ≤ |a_i−a_j|`; consecutive `q`-divisible terms are ≥`q`
   apart in value. Combined with L2 (`a_n = Θ(n)`, gap ≤ M), a fixed prime `q`
   can divide at most `O(N·M/q)` of the first `N` terms — a genuine `≤ M/q`
   density cap. This bounds how often ONE large prime can recur but does
   **not** by itself bound how MANY distinct large primes get recruited
   (budget argument incomplete — see dead end below). This is the natural
   place to try a "sum over recruited primes of their density must exceed 1,
   contradiction" argument, analogous to the crux corpus's `aimo-0447` /
   `aimo-0643` moves below — but I could not complete a convergent-sum
   obstruction; see "why it doesn't obviously close" below.

2. **"Excess ratio is a1-dependent, not M-dependent" opening (new, from this
   round's simulation).** The previously recorded refutation showed `19 | L`
   for `a1=375` (`M=rad(375)=15`) — a prime **exceeding M** persists. I found
   a *second*, sharper data point this round: `a1 = 9375 = 3·5^5` (same
   `M=15`) gives `L = 14070 = 2·3·5·7·67`, i.e. the excess prime jumps from
   `19` to **`67`** — strictly larger — while `M` is unchanged. This shows
   the size of a persisting "excess" prime is **not** capped by any function
   of `M` alone; it must depend on `a1` itself (its actual size / prime-power
   structure), not just its radical. **Any approach that tries to bound
   `primes(L)` purely in terms of `M = rad(a1)` is doomed** — this
   strengthens (does not just repeat) the already-recorded M-threshold
   refutation: it's not a one-off anomaly, it's a family that gets worse as
   the prime-power exponent grows (`3·5^1=15`→no excess, `3·5^3=375`→excess
   19, `3·5^5=9375`→excess 67). Any finiteness argument needs to use `a1`'s
   actual magnitude (or `ω(a1)`, or the specific gaps between `a1`'s prime
   power "witnesses"), not a fixed M-threshold — a genuinely different
   framing from the M-based ones already refuted.

3. **Per-minimal-support decomposition (empirical structural opening).**
   Directly computed the ⊆-minimal antichain 𝓐_∞ for `a1=375` (not just its
   union `Π`): it has exactly 5 minimal supports: `{2,3},{3,5},{2,5,19},
   {3,7,19}` — note NO singleton {p} is minimal (no term is ever a bare prime
   power in this run), and the "large" prime 19 only ever appears **paired**
   with a small anchor prime (`{2,5,19}`, `{3,7,19}`), never alone. This
   suggests the real mechanism recruiting a prime `q` into Π is: `q` becomes
   the sole surviving witness of gcd between some term `a_i = (\text{small
   factors}) \cdot q` and some other term, and `q` gets "locked in" precisely
   because no term ever later has support exactly the smaller set. This is a
   finer target than "bound Π's size" — it points toward "show every
   sufficiently-recruited prime must eventually be dominated by a pure-power
   (or small-support) term appearing later" as the actual mechanism to prove
   — a genuinely different top-level target than a pure counting/density bound
   (it's closer to a *recurrence/domination* argument than a *counting*
   argument, worth flagging to the outliner as an alternative framing even
   though it's outside my strict density lens).

4. **Reformulating via `aimo-0932`'s divergence-of-`Σ1/p` mechanism (a
   candidate technique, unexplored).** `aimo-0932`'s crux move: "a uniform cap
   of `C` primes per dyadic block would force `Σ1/p` to converge, contradicting
   known divergence" gives a template for proving a set of primes is
   **unbounded** via density. We need the OPPOSITE conclusion (Π finite), so
   this technique in its raw form doesn't directly transplant — but its
   contrapositive shape (bound a count via `Σ 1/p` convergence, cf.
   `aimo-0643`'s `Σ_p 1/p^2` covering argument) is the right kind of tool IF
   one can show recruited primes have density decaying like `1/p` or faster
   in a way whose sum is controlled by the fixed growth rate `M`. I did not
   find a way to set this up rigorously (see "why it doesn't close" below) —
   flagging as a candidate technique to try, not a working argument.

### Candidate technique(s)
- Distance–prime (L3) + Gap bound (L2) density counting (already-certified
  free lemmas), pushed toward a "budget/sum" argument — incomplete.
- `aimo-0447`-style "assign a witnessing prime per constraint, then
  small-primes-cover-most vs large-primes-are-rare-and-forced-distinct"
  pigeonhole, adapted from a 2D grid to our 1D admissibility-against-all-
  earlier-terms setting.
- `aimo-0643`-style calibration: bound contribution of primes `≤ threshold`
  by `Σ 1/p^2` (converges) and contribution of primes `> threshold` by a
  count-of-large-prime-factors-per-integer argument, then calibrate the
  threshold. Structurally close to what's needed but I could not adapt the
  "disk of radius ρ" geometry to our "window of size M" setting cleanly —
  the obstruction is that our windows are only size `M` (a FIXED constant,
  not growing with `n`), so there's no room to let a threshold `ρ→∞` the way
  `aimo-0643` lets its disk radius grow with `log r`. This is the sharpest
  reason the direct transplant fails — worth recording as a structural
  mismatch, not just "didn't try hard enough."

### Cheap-kill candidates
- None found that resolve the crux outright. The one useful cheap fact:
  **no singleton `{p}` needs to be minimal for the mechanism to work** (seen
  in the `375` antichain: minimal supports are all size ≥2) — so an approach
  hoping "eventually some term becomes a pure prime power for every relevant
  prime" is NOT how it actually plays out; the domination can happen via a
  size-2 (or larger) minimal support just as well. Do not assume pure prime
  powers are the recruitment mechanism.
- Parity is not a discriminator here — 2 gets recruited or not recruited
  depending on delicate spacing (already known from round 1), not a clean
  parity split.

### Knowledge-base entries to use
- **Divisor analysis** (`d(n)`, gcd structure) — for the per-window
  density bound in opening 1.
- **Pigeonhole / extremal principle** — for any budget/counting argument.
- **Bertrand's postulate** — could supply an explicit prime in a needed
  dyadic range if the outliner wants to *construct* a witness prime at a
  particular scale (untested direction, flagging only).
- No KB entry for covering congruences / Jacobsthal's function (confirmed
  absent again this round, consistent with round-1 finding).

### Analogous past problems (cruxes)
- **`aimo-0447`** (`gcd(a+i,b+j)>1 ∀i,j∈{0..n} ⟹ min{a,b}>(cn)^{n/2}`,
  number_theory/`divisibility-and-gcd`+`size-bounding-and-descent`) — the
  single **best structural analogue**: its grid-covering-by-witnessing-primes
  + "small primes cover <half the grid, so large primes are forced and
  distinct" pigeonhole is the closest template for bounding how a prime
  "occupies" positions in our admissibility structure. Genuinely analogous in
  mechanism (gcd>1 hypothesis ⟹ assign witnessing primes ⟹ count small vs
  large prime occupancy), though the target conclusion (a size lower bound
  vs. our finiteness-of-support-alphabet) differs, so it's a technique
  donor, not a template to copy verbatim.
- **`aimo-0643`** (Diophantine approximation via coprime lattice points near
  any real point, `size-bounding-and-descent`) — analogous in the
  "small-primes-converge (`Σ1/p^2`), large-primes-are-rare-and-controllable"
  two-regime calibration, but the structural mismatch noted above (their
  window/radius can grow with the input scale; ours is capped at the fixed
  constant `M`) means it does not transplant directly. Worth reading for the
  calibration *shape* of argument, not the formula.
- **`aimo-0932`** (`φ(d(n))/d(φ(n))` unbounded, `size-bounding-and-descent`) —
  only loosely analogous: its `Σ1/p` divergence argument proves a set of
  primes is UNBOUNDED, the opposite of what we need. Mentioned because it's
  the only corpus hit using "cap per dyadic block ⟹ Σ1/p bound" reasoning
  that could conceivably be inverted, but I found no clean inversion. Judge
  this one weak — flag, don't rely on it.

### Prior progress
`redundant-constraint-antichain.md` §7 already has: (a) the correct
reformulation of the crux via "small companion" prime-sets; (b) a proof that
the merely intersecting/anchor structure (L1, L4) does NOT suffice (explicit
counterexample family of intersecting sets with infinite antichain); (c) the
same distance-prime + linear-growth density heuristic as opening 1 above,
also flagged incomplete there. My work this round adds: the sharper
`9375→67` data point (opening 2) showing the excess-prime size is `a1`-driven
not `M`-driven, the 5-element minimal-antichain decomposition for `375`
(opening 3), and the crux-corpus analogues (`aimo-0447`, `aimo-0643`,
`aimo-0932`) with an honest account of why they don't transplant cleanly.

### Dead ends (do not retry)
- **M-threshold confinement (`p|L ⇒ p≤M`)** — already recorded FALSE
  (`a1=375` gives `19|L`, `M=15`). Confirmed again this round AND shown to
  be not just a one-off: `a1=9375` (same `M=15`) gives an even larger excess
  prime `67`. Do not attempt any bound on `primes(L)` that depends only on
  `M=rad(a1)`; it must depend on `a1` itself (or a finer invariant).
- **Density argument via distance-prime + linear growth alone (opening 1),
  used as a "budget" bound on the NUMBER of distinct recruited primes** — I
  attempted (this round, not previously recorded) to turn "each prime `q`
  has density `≤ M/q` among terms" into "the primes recruited must have
  `Σ 1/q` bounded, hence finitely many," but this does **not** close: the
  bound `≤ M/q` only says a SINGLE already-recruited prime is rare, it gives
  no obstruction to always finding a NEW, never-before-used prime once in a
  while (the "budget" would need an argument that recruiting a new prime
  costs a fixed amount of "density," and the total available density is
  bounded by 1 — but the density used by DIFFERENT primes' terms can
  overlaps in a term with several relevant witnesses, i.e. it's not a
  disjoint partition, and I found no way to make the counting additive
  rather than just a per-prime cap). This is a genuine gap in the density
  framing, not merely unexplored — record so the next round doesn't retry
  the same "sum the per-prime density caps" idea expecting it to trivially
  close.
- **Direct transplant of `aimo-0643`'s radius-calibration** — fails because
  our window is a FIXED constant `M` (not growing with `n`), so there is no
  free parameter to calibrate a "large prime" threshold against a growing
  scale the way that problem does. Flag as attempted-and-blocked this round.

### Small-case / intuition notes (all conjectural)
- Finite Alphabet held in **every** simulated case this round, including
  previously-untested hard ones: `a1=385` (`T=5088, L=43890=2·3·5·7·11·19`,
  needed 25000 terms to detect), `a1=45045=3²·5·7·11·13` (did not find exact
  period in 20000 terms, but verified **every one of 20000 terms**, up to
  value ~110000, is divisible by one of `{2,3,5,7,11}` — i.e. Π is almost
  certainly `⊆{2,3,5,7,11,13}`, NOT growing with the many large primes
  (13,17,19,...,18313) that appear as *extra, redundant* factors of composite
  terms but never as necessary/minimal witnesses). This is strong conjectural
  support for the crux, but it is evidence, not proof.
- New systematic sweep `a1 ∈ [2,700)` with ≥2 distinct prime factors: only
  `a1=375` shows a prime exceeding `M=rad(a1)` in `primes(L)`; all ~250 other
  seeds tested settle to `primes(L) ⊆ {2}∪{p≤M}` within budget. So
  "M-exceedance" is **rare but real and gets worse for higher prime-power
  seeds** (`375=3·5³→19`, `9375=3·5⁵→67`) — worth the outliner treating
  "exceedance size grows with the prime-power exponent of a1" as a concrete
  numeric pattern to explain, not dismiss as noise.
- The minimal-antichain elements recruiting a large prime `q` always paired
  `q` with 2–3 small primes (never a bare `{q}`) in every case checked —
  conjectural mechanism note for opening 3.
