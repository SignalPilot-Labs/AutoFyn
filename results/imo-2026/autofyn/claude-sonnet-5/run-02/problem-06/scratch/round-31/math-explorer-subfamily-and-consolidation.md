## imo-2026-06

### Part 1 — is `a1-23q` build-ready?

**Yes — build-ready, routine ~1-round build, same certified template as p=3,5,7,11,13,17,19.**

Independently resimulated the literal greedy `a_1=23q` sequence from scratch
(own Python script, correct "illegal iff `gcd=1` with *some* prior term"
semantics, 8 terms per candidate `q`), for every prime `q` in `(23,200000)`
(17,975 primes tested, two independent runs at `q<20000`, `q<60000`,
`q<200000` all agree, byte-identical):

```
Bad(23) = {29, 31, 37, 41, 43, 61, 67, 73, 79}   (9 primes, all deviate on the diagonal j=r)
```
Exact deviation data: `a_3` deviates for `q∈{29,31,37,41,43}` (values
`696,744,888,984,1032` vs expected `713,759,897,989,1035`); `a_4` deviates
for `q∈{61,67}` (`1464,1608` vs `1472,1610`); `a_5` deviates for
`q∈{73,79}` (`1752,1896` vs `1771,1909`).

This is `9` exceptions, vs `7` for `p=19` — **larger**, but the mechanism
is the same shape and, if anything, *simpler* to prove than p=19's, because
on the diagonal `K_0=p+1=24=2^3·3` (only two prime factors, `2` and `3`,
vs `p=19`'s `20=2^2·5`). I hand-traced the certified Diagonal
Window-Parity Lemma's mechanism (§6 of `a1-19q-subfamily-theorem.md`)
through at `p=23` and it reproduces `Bad(23)` exactly:

- Window length 1 (`n_0=2`, i.e. `q=23+r` prime) is *automatic* (q odd ⟹
  q+1 even) for `r∈{6,8,14,18,20}` ⟹ `q∈{29,31,37,41,43}` — **5** automatic
  exceptions, matching exactly.
- Window length 2 (`n_0=3`, `q=46+r` prime, need `q+2` div by `2` or `3`;
  `q+1` automatic as before): `r=15⟹q=61` (`63=3^2·7`, div 3 ✓); `r=21⟹q=67`
  (`69=3·23`, div 3 ✓). Checked the two "near-miss" primes at this window
  length that do NOT give exceptions (`r=7⟹q=53`: `55=5·11`, not div 2 or
  3, fails — and indeed `53∉Bad(23)`; `r=13⟹q=59`: `61` prime, not div 2 or
  3, fails — `59∉Bad(23)`) — both correctly resolved (non-exceptions),
  confirming the mechanism's "iff" direction, not just the "if" direction.
- Window length 3 (`n_0=4`, `q=69+r` prime, need `q+2,q+3` both div by `2`
  or `3`): `r=4⟹q=73` (`{74,75,76}={2·37, 3·5^2, 2^2·19}`, all hit); `r=10⟹
  q=79` (`{80,81,82}={2^4·5,3^4,2·41}`, all hit) — matches the remaining 2
  exceptions exactly.

So all 9 members of `Bad(23)` are explained by the **same** Diagonal
Window-Parity mechanism with `24=2^3·3` in place of `20=2^2·5` (checking
divisibility by `2` or `3` instead of `2` or `5`) — no new mechanism is
needed at `p=23`; the `a1-19q` file's own "Promotable lemmas" section
already anticipated exactly this generalization ("a future approach
instantiating this machinery at a new prime `p'` need only re-derive
`K_0=p'+1`'s prime factorization and re-check the window elements'
divisibility by those primes"). The only NEW work needed for a full build
is the routine mechanical part already done 7 times: the `23×22=506`-cell
(actually `21×22` for `j∈{2,...,22}`, `r∈{1,...,22}`) `(s_0,K_0)` table,
the `Q_1` threshold computation and witness search for the `k=0` layer's
below-threshold candidates, the `s*` threshold induction for `k≥1` (should
again land near `s*=5`, `k≥`~7–9 given `q_min=29`), and the small residual
`k∈{1,...,~7}` band's below-threshold quadruples. This is the **most
routine and lowest-risk possible next build** in the entire population —
same risk profile as `a1-19q` itself, i.e. essentially certain to close in
one round given the template's 7/7 track record.

**Caveat (label as conjecture, not proof):** the greedy resimulation above
is numerical evidence to `q<200000`, not a proof that `Bad(23)` is
*exactly* these 9 primes and no more — that requires the actual symbolic
`Q_1`-threshold argument (as in every prior instantiation) to rule out
larger `q` rigorously; this is exactly the mechanical work a builder would
do, not new research risk.

### Part 2 — consolidation vs. continued per-`p` grinding

**Two-open-residuals recap (from `a1-pq-subfamily-theorem.md`'s own Status,
round 28, unchanged through round 30):**
1. **`r=1` residual:** the Universal Look-Back Witness Identity's
   corollary gives unconditional closure of `k=0` and every `k` with
   `gcd(k+1,j)=1`, for *every* `p`, for free — but `k≥1` with
   `gcd(k+1,j)>1` is NOT closed in general; it is currently closed
   per-`p` only via the same sieve/witness machinery used for `r≠1`.
2. **`r≠1` residual:** the Universal Look-Back Closed Form (round 28) is a
   fully general, proved bookkeeping identity (`gcd(N,a_n)=gcd(j,(k+1+
   c(p,j,r))\bmod j)`) valid for every `p,j,r` — but it does NOT by itself
   decide legality; the actual `k=0`-layer closure for `r≠1` still requires,
   per `p`, the same sufficient-window/`Q_1` computation and the same
   finite witness search that's been redone by hand at `p=3,5,7,11,13,17,
   19` (and now, per Part 1, would be redone again at `p=23`).

**Is there a genuinely new angle on either, given 7 accumulated data
points?** I looked for one and did not find a promising new lever beyond
what's already tried:
- The per-`p` exceptional sets `Bad(p)` show **no evident closed-form
  pattern** across `p=3,5,7,11,13,17,19,(23)`: sizes are `1,3,2,6,4,8,7,
  (9)` — not monotonic in `p`, not obviously a function of `p mod` anything
  simple. The *mechanism* generalizes uniformly (diagonal window-parity,
  checking the prime factors of `K_0=p+1`), but *which* primes `q` actually
  trigger it depends on which small shifted values `p+r, 2p+r, 3p+r,...`
  happen to be prime AND have the right small-prime-divisibility pattern in
  their windows — this is inherently arithmetic/incidental data, not a
  clean function of `p`. This reinforces (does not contradict) round 26's
  finding that a "Minimal-Window Necessity Conjecture" shortcut was
  real-but-incomplete progress and not a route to full uniformity.
- The `k≥1, gcd(k+1,j)>1` residual (open residual #1) has had **zero new
  attack ideas** proposed in rounds 27–30; every subsequent round instead
  reused the *existing* per-`p` Legendre-Sieve+Primorial-Floor threshold
  machinery to route around it per-`p`, never closing it in general. This
  is a genuine 4+-round plateau on this specific sub-gap, but — importantly
  — it is NOT the reason the per-`p` theorems succeed (those succeed via
  the sieve/threshold route, not via closing this residual), so it is not
  actually blocking further `a1-pq`-style APPROVEs; it only blocks the
  *general-in-p* theorem.
- No new idea found for a uniform-in-`p` proof that "only diagonal-band
  cells can be genuine exceptions" (this remains open per round 26,
  unchanged) that would let one skip the finite per-`p` witness search
  entirely.

**Honest assessment: per-`p` grinding has now clearly hit
diminishing-marginal-value territory for the run's *actual* target.** 11
APPROVEs (soon a 12th at `p=23`, essentially free) are all instances of one
template, and none of them touches H1 (FAH) or H2 (absorption-chain
termination) — the two hypotheses the Master Conditional Theorem says are
necessary and sufficient for the *general* problem, and which have sat in
an unbroken plateau for 23+ rounds (rounds 6–30) despite 30+ distinct FAH
mechanism attempts recorded as dead in the graveyard. Grinding `p=23` (or
`p=29,31,...`) adds population breadth and a safe/cheap APPROVE, but each
additional instance provides essentially zero new insight toward H1/H2 —
by round 7 of this template (p=17) the marginal information content of a
new `p`-instantiation was already near zero, since every one of them
independently confirms "the machinery works, `Bad(p)` is some ad hoc small
finite set found by brute force" rather than revealing new structure.

**My assessment for next-round strategy (terrain report, not a mandate):**
- Building `a1-23q` this round is safe, cheap (one routine builder-round,
  near-certain APPROVE) and keeps the population's floor deliverable
  growing — reasonable to include as ONE build-set slot, but should not be
  the round's only content given CLAUDE.md's directive to diversify and
  the flagged 23+-round plateau on H1/H2.
- The genuinely valuable move given the plateau is what CLAUDE.md's
  "Break a shared-gap plateau" rule calls for: dispatch (in addition to the
  cheap `a1-23q` build) at least one explorer/outliner effort that attacks
  H1 (FAH) or H2 from a framing genuinely far from the graveyard's 32+
  dead mechanisms — not another per-`p` instantiation, and not another
  variant of Free Facts / bounded-witness / bipartite-network framings
  (all independently confirmed dead or reducible-to-dead this run). I did
  not find such a framing myself in this pass (my lens was subfamily +
  consolidation, not FAH), so I flag this as a gap for another lens/round
  rather than force one.
- A pure "write-up/consolidation" deliverable (no new mathematical content,
  just packaging the 11-or-12 APPROVEs) is lower value than either (a) the
  cheap `a1-23q` build or (b) a genuine new H1/H2 attempt — consolidation
  produces no new Elo-worthy content and the file contract already tracks
  everything needed (`current.md`, per-slug files, `.ranking.json`); I do
  NOT recommend spending a full round on pure consolidation while `a1-23q`
  remains an unclaimed one-round win and H1/H2 remain the real bottleneck.

### Cheap-kill / structural notes
- Parity: `q` is always odd (prime `>p>2`), so `q+1` is always even — this
  is the one fully general, `p`-independent fact driving every "automatic"
  diagonal exception across every `p` instantiated so far (`p=3,...,19,23`).
  Any future `p` instantiation should check this first (free exceptions)
  before any sieve computation.
- `K_0=p+1` on the diagonal is a fixed, computable small number for each
  `p`; its number of odd prime factors (beyond the automatic factor `2`)
  directly controls how much extra per-window checking is needed. `p=23`
  needed only one extra prime (`3`) — less work than `p=19`'s `5` or
  `p=17`'s presumably larger `K_0=18=2·3^2` (also just needs mod-3, in
  fact — worth noting `p=17`'s `K_0=18` and `p=23`'s `K_0=24` both reduce
  to a mod-2/mod-3 check, suggesting `p≡1\pmod3$ or `p\equiv2\pmod3` may
  correlate with whether `K_0=p+1$ picks up a factor of `3`; not verified
  further, flagged as a possible cheap lens for the NEXT `p` if picked, but
  not pursued here since it doesn't change build-readiness of `p=23`).

### Knowledge-base / lemma entries relevant
- `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`
- `lemmas/legendre-sieve-gap-bound.md`
- `lemmas/primorial-floor-bound.md`
- `lemmas/universal-look-back-witness-identity.md`
- `lemmas/diagonal-characterization-and-first-risk-theorem.md`
- `lemmas/universal-look-back-closed-form-and-r1-uniqueness.md`
All six are p-uniform/general and require no new proof for `p=23` — only
substitution, exactly as documented in every prior instantiation file's
"§0 Setup and imported machinery" section.

### Dead ends (do not retry)
- Minimal-Window Necessity Conjecture (round 26) — real partial progress
  (Diagonal Characterization + First-Risk Theorem certified) but does NOT
  close the general-`p` theorem; still has a precisely located open gap
  (non-diagonal-band first-deviation instance not ruled out in general).
  Do not re-attempt without a genuinely new idea for that specific gap.
- 32+ FAH/H1 mechanism variants in the graveyard (Free Facts variants,
  bipartite-network framings, density arguments, etc.) — confirmed dead or
  reducible-to-already-dead as of round 29; do not re-propose without a
  framing that is provably NOT equivalent to one of these.

### Analogous past problems (crux corpus)
Did not run a fresh corpus query this pass (lens was numeric/structural
verification of `p=23` and meta-assessment, not new-technique search); the
prior rounds' explorers have already searched the crux corpus extensively
for this problem's FAH/greedy-gcd structure (see round-7's aimo-1000
citation, confirmed still accurate this round) — no new corpus angle to
report from this lens.

### Small-case / intuition notes (conjecture, not proof)
- `Bad(p)` sizes so far: `p=3:1, p=5:3, p=7:2, p=11:6, p=13:4, p=17:8,
  p=19:7, p=23:9 (this round, numeric)`. No monotonic or simple closed-form
  pattern in `p` is apparent — reinforces that a uniform-in-`p` formula for
  `Bad(p)` is unlikely to exist in a form provable without per-`p`
  computation; the *mechanism* (diagonal window-parity against `K_0=p+1`'s
  small prime factors) is uniform, but the *output* is arithmetic data.
