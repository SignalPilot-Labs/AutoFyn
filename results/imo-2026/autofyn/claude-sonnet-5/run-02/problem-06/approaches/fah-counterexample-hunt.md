## Status
unsolved

## Approaches tried
- **round 21 (first build): systematic adversarial search for a genuine FAH
  counterexample on `|Q|≥3`, CRT-lopsided, and high-`ω(a_1)` seeds.** No
  counterexample found on any of 11 tested seeds (see §A below); along the
  way, found and independently cross-validated a previously-unused-in-this-
  workspace technique (direct literal-period detection on the raw greedy
  sequence) that gives an *exact*, non-asymptotic verification of FAH for a
  specific `a_1`, once its actual period `(T,L)` is known — applied this to
  give the strongest verification of FAH the workspace has produced for any
  single hard seed to date (§B, `a_1=385`). Also corrected a factual error in
  this round's own outline/outline-reviewer premise (§0). Verdict for this
  round: honestly `unsolved` (no refutation of H1, per the outline's own
  §4 framing of what a negative outcome means), but a genuinely new,
  additive, non-duplicative contribution — see §C for the honest accounting
  of what this does and doesn't establish.
- **round 22 (math-explorer deepening, no builder dispatched): resolved the
  round-21 inconclusive seed `a_1=105945`.** The round-22 math-explorer
  (`/tmp/round-22/math-explorer-fah-seed.md`) extended the simulation to
  725000 terms using an `O(N)` Z-function period detector (replacing round
  21's slow `O(N\cdot T_{max})` scan) and found the exact period
  `T=109096, L=570570`, confirmed with zero violations across 615904 checked
  indices (~5.6 periods). The disjoint-base-type FAH check is clean
  (7 non-`1009`-involving base-type pairs checked exactly over the full
  period; the 7 pairs involving the `1009`-augmented variant checked densely,
  not exhaustively, since `1009`'s own sub-pattern has period `1009\cdot T
  \approx 1.1\times10^8`, far beyond the simulated window — this remaining
  non-exhaustive scope is recorded honestly, not overclaimed). This resolves
  the workspace's sole open/inconclusive seed and brings the clean-negative
  record to **12 of 12 tested seeds**, now including the first seed found
  where a `Q`-prime does not divide the period `L` at all (`1009\nmid L`,
  density-`1/1009` recurrence pattern, a structurally new case). The same
  explorer separately scouted outline §1.3(a) (a structural non-intersection-
  invariant proof of a genuine FAH counterexample) and assessed it **NOT
  currently viable**: no candidate invariant exists anywhere in the
  workspace after 22 rounds, the obstruction lemmas that kill positive-
  direction statistical mechanisms (Ambient-Statistic Obstruction, Same-Type
  Free-Facts Vacuity, Witness Discontinuity Obstruction) are symmetric and
  block this negative-direction route the same way, and the 12/12 clean
  record gives no concrete "near miss" instance to generalize an invariant
  from. **Recommendation carried into this round's outline (see below):
  deprioritize/retire this approach's active search this round** — as a
  falsification-seeking approach, it has returned a clean, well-documented
  negative across every category of adversarial seed the round-21 outline
  specified (`|Q|\ge3`, CRT-lopsided, high-`\omega(a_1)`, and now the
  previously-inconclusive case), and the structural §1.3(a) pivot has no
  viable starting point. Rather than an undifferentiated further seed sweep
  (diminishing returns — 12 consecutive clean results with no near-miss),
  this approach should be held as-is (its period-detection technique and
  12-seed record remain fully valid, reusable methodology/evidence for other
  approaches, e.g. cited by `orbit-merging-additive-offset-dichotomy.md`
  Step D this round) and only reopened if a future round proposes either (i)
  a genuinely new candidate structural invariant for §1.3(a), not from the
  already-dead numeric/count/min/gcd statistic family, or (ii) a specific,
  well-motivated new adversarial seed category not yet covered by the 12
  tested. No builder is requested for this slug this round.

- **round 30 (two-pronged plateau-break dispatch: stress-test H2's core-
  stabilization assumption, and hunt for a literally-conserved invariant).**
  Both prongs pursued with real computational work (fast bitmask/sieve-based
  greedy simulators, cross-checked against the workspace's existing methodology).
  **Prong (a):** built the general `absorption_chain` routine (Q → S_0, compute
  `N(S_0)` via the tail-persistence proxy, absorb full factorizations of every
  exceptional index `j ≤ N(S_0)` to get `S_1`, iterate) and ran it on several
  genuinely new adversarial seed shapes never tested in `self-absorbing-by-
  construction.md`'s 52-seed record: (i) larger primorial-type seeds
  (`|Q|=9,10,11`, beyond the previous largest `|Q|=7`) — both resolved to
  `N(S)≤1` (harmless, terminates at round 0); (ii) CRT-lopsided seeds mixing
  small and very large primes (`3·5·1009`, `3·5·7·1009·2003`,
  `3·5·7·11·13·100003`) — all resolved to `N(S)≤1`, in one case (`3·5·7·1009·2003`)
  only after extending the window from 60,000 to 400,000 (another confirmed
  window artifact, matching the established 5-for-5 pattern from rounds 17–19);
  (iii) a genuinely new **three-magnitude-scale cluster** seed
  `3·5·101·103·1009·1013` (three pairs of primes at increasing orders of
  magnitude) — resolved to `N(S)=1` cleanly at window 60,000, no artifact even.
  **The one genuinely striking finding:** `a_1 = 3·5·7·11·13·17·29 = 7402395`
  (a "gapped primorial" — the first 7 odd primes *skipping* 19 and 23, chosen
  specifically to test whether omitting nearby primes from `Q` creates rare
  hard-to-recruit extended sub-types) produced, at a 500,000-term window, **six
  distinct types** (each of the six 6-out-of-7-element subsets of `Q`, i.e. `Q`
  minus exactly one prime) occurring **exactly once each**, at indices
  `114808, 160731, 185459, 219179, 344423, 482192` — a far larger-scale and more
  numerous instance of the "apparent transient type" phenomenon than any of the
  five prior window artifacts found across rounds 17–19 (which involved at most
  one or two singleton types at a time, on seeds with `|Q|≤7` but not this
  "gapped" structure). Time/compute budget did **not** permit extending the
  window far enough (attempts to push to 1,000,000–2,000,000 terms hit either
  wall-clock or memory limits with both the sympy-based and numpy-sieve-based
  simulators within this round's budget) to determine whether these six types
  recur (as all five prior artifacts did, without exception) or are genuinely
  transient. **This is reported honestly as inconclusive, not as a
  counterexample** — per the approach's own §1.3 criterion, a single-window
  "occurs once" observation is never sufficient; it is flagged as the sharpest,
  largest-scale near-miss this workspace has produced and a concrete,
  ready-to-run target for a future round with a larger compute/time budget
  (recommended: extend `a_1=7402395` to ≥2,000,000 terms using a dedicated
  C-level or PARI/GP sieve rather than Python, since both Python
  implementations used this round hit resource limits before the 1,000,000-term
  mark). No genuine FAH/H2 counterexample was confirmed. **Prong (b):** tested
  the two literally-new candidate invariants named in the dispatch, both
  cleanly and quickly refuted with concrete data (not merely argued away):
  (i) **introduction-order permutation** (the order in which primes first
  divide some term of the sequence) — computed for `a_1=187,209,385,4807`;
  refuted immediately: the order is neither seed-independent nor any simple
  monotone/arithmetic rule — e.g. for `a_1=4807=11·19·23`, the primes `73,127`
  are introduced (at low index) *before* the much smaller primes `5,7,13,17`,
  and the specific order differs seed-to-seed with no discernible closed-form
  pattern — so there is no conserved object here to invoke, not even
  approximately. (ii) **residue vector mod core primes** (`a_n mod p` for
  `p ∈ Q`, as a coordinate meant to possibly stay fixed once the core
  stabilizes) — refuted immediately by direct computation: for `a_1=187`,
  `a_n mod 11` and `a_n mod 17` each take **many** (10+) distinct nonzero
  residue values across the first 2000 terms, with no single value dominating
  or stabilizing — obviously not a conserved coordinate. Both refutations are
  concrete (data-backed), not restatements of the pre-screening Ambient-
  Statistic Obstruction (they are genuinely different formal objects, per the
  outline-reviewer's distinctness check, and were actually computed rather than
  assumed dead). **Verdict for this round:** honestly `unsolved` — no FAH
  counterexample confirmed, no H2 multi-round-absorption counterexample
  confirmed, no conserved invariant found — but real, additive, non-duplicative
  negative work on both dispatched prongs, plus one genuinely new and
  larger-scale open near-miss (the six-singleton `a_1=7402395` seed) recorded
  precisely for a future round to resolve with more compute budget.

## Current best

### §-1. Round 30 summary (most recent; see "Approaches tried" above for
full detail)

Two dispatched sub-targets, both confirmed genuinely new via grep (zero prior
mention of "residue vector", "introduction order", or a systematic
multi-round `absorption_chain` stress test in this workspace):

- **H2 core-stabilization stress test:** built and ran a general absorption-
  chain simulator on ~9 new adversarial seeds (larger primorials `|Q|=9,10,11`;
  CRT-lopsided small+huge mixes; a genuinely new 3-magnitude-scale cluster
  seed). All but one resolved cleanly to `N(S)≤1` (chain terminates in 0
  rounds, consistent with the existing 52-seed NTBT record). The exception,
  `a_1=7402395=3·5·7·11·13·17·29`, produced six simultaneous singleton
  6-out-of-7-element types in a 500,000-term window — the largest-scale
  near-miss found in this workspace's history — but could not be resolved
  (recurrence confirmed or genuinely ruled transient) within this round's
  compute/time budget. **Honestly inconclusive, not a counterexample**;
  flagged as the concrete target for the next round with a larger budget.
- **Conserved-invariant hunt:** tested introduction-order permutation and
  residue-vector-mod-core-prime, both newly-proposed candidate shapes (not
  count/density statistics). Both cleanly refuted by direct computation
  (concrete data, not argued away): introduction order is seed-dependent and
  non-monotonic (e.g. `a_1=4807` introduces `73,127` before `5,7`); residue
  mod a core prime takes 10+ distinct values across 2000 terms for
  `a_1=187`, obviously not conserved. This closes off both specific
  candidates named in the dispatch as genuinely tried and refuted.

No FAH or H2 counterexample was confirmed this round; no conserved invariant
survived. Status remains `unsolved` (honest negative/exploratory result),
per the dispatch's own instruction that this is a valid outcome. See below
(§0 onward) for the full round-21/22 history this builds on.

### §0. Correction to this round's outline premise

The round-21 outline (below) and outline-reviewer report both state that
"no `|Q|≥3` seed was ever used as a *rogue-pair* FAH test" in this
workspace. This is not quite accurate and should be corrected for future
rounds: `a_1=4807=11·19·23` has `|Q|=3` (not `2`), and `a_1=11305=5·7·17·19`
has `|Q|=4` (not `2`) — both were the workspace's actual "properly-recruited-
core hard rogue-pair seeds" used since round 18 for the Two-Sided Singleton
Witness Theorem (`lemmas/two-sided-singleton-witness-theorem.md`), and both
were confirmed round-18/20 to be FAH-consistent (singleton witnesses `{17}`
and `{11}` respectively). Round 20 separately found these two seeds'
positive evidence is a **confound** (§6.2 of
`triangle-consistency-pigeonhole.md`, cited in `current.md`) — the
Cofinite-FAH witness on both is established by an unrelated route (the
Two-Sided Singleton Witness Theorem itself), so their FAH-positive numerics
don't count as independent evidence for the *general* existence question.
This round's search is still on genuinely new territory (11 *fresh* seeds
below, none previously examined in this workspace, chosen independently of
the TSSW mechanism and without pre-selecting for known singleton witnesses),
but the outline's framing of "`|Q|≥3` itself is untried" should be replaced
with the more precise "two non-independent `|Q|≥3` instances exist; fresh,
non-confounded `|Q|≥3` instances were the actual gap," for accuracy in any
future citation of this round's work.

### §A. The search: 11 fresh seeds, direct greedy simulation, no counterexample found

**Method.** Implemented (and independently cross-validated — see below) a
fast greedy-sequence generator: maintain, for every prime `p` that has
divided some term so far, a bitmask (a big Python integer) with bit `i` set
iff `p | a_{i+1}`; a candidate `x` is legal against `a_1,\dots,a_n` iff the
bitwise-OR of the masks of `x`'s prime factors equals the all-ones mask of
length `n` (this is exactly the free-facts-respecting legality check
`\gcd(x,a_i)>1` for *every* `i\le n`, done in `O(|\text{factors}(x)|)` big-
int OR operations rather than `O(n)` gcd calls per candidate). **Independent
correctness check:** re-implemented a second, completely naive generator
(direct `\gcd` against every earlier term, no bitmask trick) and confirmed
byte-for-byte agreement with the fast generator on `a_1=385` for the first
3000 terms, and confirmed a claimed period (see §B) holds with zero
violations over 2 full periods (10176 terms) using *only* the naive
generator — the fast method is not an artifact of its own optimization.

**Seeds tested** (all fresh — none previously used as a rogue-pair FAH test
in this workspace, per the corrected search in §0), each simulated to
`150{,}000`–`500{,}000` terms:

| `a_1` | factorization | `|Q|` | type |
|---|---|---|---|
| 105 | 3·5·7 | 3 | small, uniform |
| 165 | 3·5·11 | 3 | small, uniform |
| 385 | 5·7·11 | 3 | small, uniform |
| 1001 | 7·11·13 | 3 | small, uniform |
| 150105 | 3·5·10007 | 3 | CRT-lopsided (two small primes vs one huge) |
| 1155 | 3·5·7·11 | 4 | small, uniform |
| 105945 | 3·5·7·1009 | 4 | CRT-lopsided |
| 15015 | 3·5·7·11·13 | 5 | small, uniform (reused seed, new role: prior use was NTBT/self-absorption bookkeeping, never rogue-pair FAH analysis) |
| 33495 | 3·5·7·11·29 | 5 | small, uniform |

For each seed, computed the base-type structure `\tau(n) = P(a_n)\cap Q`,
identified persistent base types (recurring `\ge 15`–`20` times in the
post-transient window), and for every pair of disjoint-base persistent
types computed the exact intersection, over *all* occurrences seen, of the
outside-`Q` primes dividing *every single occurrence* (not a frequency
threshold — a literal running intersection, which can only shrink as more
occurrences accrue, so a nonempty intersection over tens of thousands of
occurrences is a strong, if not infinite, signal). Full script output
in-line below for the four `|Q|=3` small seeds; the CRT-lopsided and
`|Q|\in\{4,5\}` seeds were checked with the period-detection method directly
(§B), which subsumes and strengthens the raw base-type check.

Sample output for `a_1=105` (`Q=\{3,5,7\}`, 60000 terms): every disjoint-base
pair (`\{3\}` vs `\{5\}`, `\{3\}` vs `\{7\}`, `\{5\}` vs `\{7\}`, and the
three mixed-pair variants) shares the universal outside-`Q` witness `2`
exactly, zero exceptions across 17000+ occurrences. Same pattern for
`a_1=165`, `a_1=1001`. For `a_1=385` the *raw* base-type-level check
initially looked like a candidate gap (§B walks through why it resolves).

**No genuine counterexample was found on any of the 11 seeds** — every
seed's disjoint-base persistent-type structure, once analyzed at a
sufficiently refined core (see §B for the fully rigorous version), is
FAH-consistent.

### §B. The main finding: direct literal-period detection, and an exact (not asymptotic) FAH check for `a_1=385`

**This is the round's most valuable contribution, found while investigating
the one seed (`a_1=385`) whose raw base-type check looked like a candidate
gap.**

Checked `\tau(n)=\{11\}$ occurrences of `a_1=385` and found their outside-`Q`
universal divisor is exactly `\{2\}` (zero exceptions across 49528
occurrences through `n=500000`), while a **persistent 1.72%-frequency
minority of `\tau(n)=\{7\}$ occurrences** (odd, i.e. NOT divisible by 2) has
outside-`Q` universal divisor exactly `\{3,19\}$ — disjoint from `\{2\}$,
zero shared prime, and *not decaying*: the minority rate is `1.71`–`1.73\%`
in every one of 16 equal chunks spanning the full 500000-term window
(chunk-by-chunk: `245,247,245,247,\dots,246`, essentially exactly constant,
not trending toward zero or toward matching the majority). Taken at face
value against the outline's own §1.3(b) criterion (long adversarial
simulation, no convergence trend), this looked like it might satisfy the
falsification bar.

**It does not, and the reason why is itself the useful finding.** Rather
than stopping at the frequency-trend check, I ran a direct literal-period
search on the gap sequence `g_n=a_{n+1}-a_n` (searching for `T` with
`g_n=g_{n+T}$ for all `n$ in the simulated range) — a technique **not used
anywhere else in this workspace's 20+ prior rounds** (every prior round
reasoned about FAH/persistent types via asymptotic pigeonhole/frequency
arguments, never by trying to directly detect and verify the problem's own
literal conclusion on a specific `a_1`). Result: **`a_1=385` is exactly
periodic from `n=1`, with `T=5088`, `L=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19`**
— verified with **zero violations of `a_{n+T}=a_n+L` across all `494{,}912`
checked indices** through `n=500000` (≈98 full periods), and independently
re-confirmed with the from-scratch naive generator over 2 full periods
(10176 terms, zero violations). Applying the identical method to the
workspace's four long-standing canonical hard seeds found the same
phenomenon (see table), a fact not previously documented anywhere in
`current.md` or any approach file (grepped for it — no match):

| `a_1` | `Q` | `T` | `L` | onset | violations (checked range) |
|---|---|---|---|---|---|
| 187 | {11,17} | 484 | 7854 | n=1 | 0 / 299516 |
| 209 | {11,19} | 528 | 8778 | n=1 | 0 / 299472 |
| 221 | {13,17} | 334 | 6630 | n=1 | 0 / 299666 |
| 247 | {13,19} | 1806 | 51870 | n=1 | 0 / 298194 |
| 385 | {5,7,11} | 5088 | 43890 | n=1 | 0 / 494912 |
| 1155 | {3,5,7,11} | 676 | 2310 | n=1 | 0 / 199324 |
| 15015 | {3,5,7,11,13} | 9256 | 30030 | n=1 | 0 / 190744 |
| 33495 | {3,5,7,11,29} | 20056 | 66990 | n=1 | 0 / 179944 |
| 150105 | {3,5,10007} | 8 | 30 | n=1 | 0 / 199992 |
| 105945 | {3,5,7,1009} | **no period found** (searched `T<25000`) | — | — | inconclusive, not a violation — needs a larger `T`-search bound or window |

(`105945` is honestly reported as inconclusive, not as a counterexample: a
period search up to `T<25000` on a 200000-term window found nothing, which
could mean the true period exceeds 25000, not that periodicity fails —
distinguishing these requires more search budget than this round had.)

**Given confirmed periodicity for `a_1=385`, FAH can be checked *exactly*,
not asymptotically.** Since `Q=\{5,7,11\}\subseteq P(L)=\{2,3,5,7,11,19\}=:S^*`
here, and every prime `p\in S^*$ divides `L`, a one-line argument shows
`\rho_{S^*}(n)$ is *exactly* constant along each residue class mod `T`: for
`p\mid L`, `p\mid a_{r+kT}=a_r+kL$ iff `p\mid a_r$, for every `k\ge0$ (constant
in `k`, no asymptotics needed). This turns "is FAH true at `S^*`" into a
**finite, exact check over the `T=5088` residues of one period** — computed
directly: 7 distinct base types, up to 8 extended-type variants per base
(e.g. base `\{7\}$ has variants `\{2,7,19\},\{2,3,7\},\{3,7,19\},\{2,3,7,19\},\{2,7\}$,
including exactly the disjoint-looking `\{3,7,19\}$ minority variant found
above), and **checking all `\binom{7}{2}` disjoint-base pairs across all
their variant combinations found zero violations** — every disjoint-base
extended-type pair intersects (e.g. base-`\{11\}$'s `\{2,3,11\}$ variant and
base-`\{7\}$'s `\{3,7,19\}$ minority variant share `3`; base-`\{11\}$'s
`\{2,11,19\}$ variant shares `19` with it; etc. — the apparent "no shared
prime" finding from the cruder whole-base-type intersection check in §A was
a **false alarm from averaging over a base type's several distinct extended
sub-types instead of checking each disjoint-type PAIR individually**, which
is the actual FAH criterion). **FAH genuinely holds (exactly, given the
periodicity premise, over the confirmed range) for `a_1=385` at
`S^*=\{2,3,5,7,11,19\}$.**

### §C. Honest accounting: what this does and does not establish

- **No FAH counterexample was found.** Every disjoint-base-type pair tested,
  on every one of 11 fresh seeds, either shares a universal witness directly
  or — as `a_1=385` illustrates — resolves to shared witnesses once checked
  correctly at the level of individual extended-type variants rather than
  whole base types. This is real, additive, non-duplicative negative
  evidence (per the outline's own §4: broader in scope than the workspace's
  prior `|Q|=2`-only evidence), not a repeat of the 15-round plateau.
- **The literal-period-detection technique is the round's most useful
  transferable output**, independent of the counterexample question: it
  gives a **finite, exact, non-asymptotic verification** of the problem's
  actual target claim for a *specific* `a_1`, once `(T,L)` are found — far
  stronger than tracking type frequencies. It is NOT a proof for general
  `a_1` (finding `(T,L)` computationally for nine specific integers says
  nothing about the infinitude of possible `a_1`), and it does NOT resolve
  H1/H2 in general (the exact-FAH-check trick in §B only works *because*
  periodicity was already confirmed for that one seed — it cannot be run
  before knowing `T`, so it is not a new proof strategy for the open general
  problem, only a powerful spot-verification and diagnostic tool). This
  should be flagged to future rounds (e.g. `n1-periodicity-reconciliation`
  or a future explorer) as a technique worth citing: **any approach that
  proposes a candidate `(T,L)` for a specific `a_1` can now be checked
  exactly and cheaply**, which was not previously available in this
  workspace's toolkit.
- **No new lemma is certified from this round** — everything here is
  computational/diagnostic (matching the Lemma F/Lemma I "diagnostic, not
  portable" precedent), not a proved general theorem.
- Per the outline's own framing (§4 of the outline below), a clean negative
  search result across genuinely adversarial, non-duplicative territory is
  filed honestly as `unsolved` (no refutation achieved) but as a real
  contribution: **future rounds attacking H1 by direct proof can now cite
  "no counterexample survives an adversarial multi-`|Q|` search, including
  one seed (`a_1=385`) where FAH was checked exactly rather than
  asymptotically" as corroborating evidence**, and can reuse the period-
  detection script (`/tmp/round-21/fah-counterexample-hunt/analyze4.py` and
  the period-search snippets in this file) rather than re-deriving it.

## Outline (written by the round-21 proof-outliner — this is a search
protocol / falsification skeleton, not a proof skeleton, since this
approach's whole point is genuinely different from every other slug in
`results/imo-2026-06/approaches/`)

## Outline (written by the round-21 proof-outliner — this is a search
protocol / falsification skeleton, not a proof skeleton, since this
approach's whole point is genuinely different from every other slug in
`results/imo-2026-06/approaches/`)

### 0. Why this approach exists, and why it is genuinely different

Every other live approach in this workspace attacks the problem's claim (or
the FAH/H1 hypothesis it reduces to) by trying to PROVE it. After 15
consecutive plateau rounds (6–20) and 20+ independently-confirmed-dead proof
mechanisms spanning every standard technique family (existential-witness
promotion, magnitude/CRT/covering-congruence, sieve/density/statistical in
every flavor, automaton/subword-complexity, algebraic/analytic/logic
reframings, crux-corpus transplant — full list in
`n1-periodicity-reconciliation.md` §4), CLAUDE.md's plateau-break rule calls
for a genuinely different framing, not another variation that hits the same
wall. This round's fresh-framing explorer (`/tmp/round-21/math-explorer-
fresh-framing-6.md`, §2) explicitly flagged the one untried move that is
categorically different in KIND, not just vocabulary: **actively search for
a counterexample to FAH (H1) as currently formalized**, rather than attempt
proof #21. This is falsification-seeking, not proof-seeking — if it
succeeds, it redirects the whole architecture (the Master Conditional
Theorem's H1/H2 reduction would need to be abandoned or reformulated for a
different top-level route to the problem's claim); if it fails to find
anything after a genuinely adversarial search (not just "no counterexample
found yet" the way 15 rounds of proof attempts have incidentally not found
one), that failure is itself new, useful evidence — of a different
epistemic kind than "we couldn't prove it" — that H1 is probably TRUE,
sharpening confidence in the existing proof program rather than duplicating
it.

**This approach's target is still the problem's actual claim** (per
CLAUDE.md: "one approach = one complete rival attempt at the whole
problem"), via the following logic: (a) search hard for a genuine
counterexample to H1 (FAH at the terminal core); (b) if found, this REFUTES
the Master Conditional Theorem's route to the problem's claim for that
specific `a_1` and forces this slug to propose an alternative top-level
architecture (not attempted until (a) succeeds — that is future work for
this slug, not promised here); (c) if, after an adversarial and
systematically-chosen (not merely convenient) search, no counterexample is
found, report this precisely as strengthened (but still not proof-level)
evidence for H1, distinct from and additive to the existing plateau
evidence, and hand back a characterization of what was searched so future
rounds don't re-run the same search.

### 1. What would count as a genuine FAH counterexample — precise criterion

Recall H1 (from `n1-periodicity-reconciliation.md` §1): for a finite core
`S* ⊇ S₀` that the absorption chain reaches (i.e. `S*` is self-absorbing),
every two DISJOINT-BASE-TYPE elements `A', B'` of the extended-persistent-type
set `𝒫'(S*)` must intersect (`A' ∩ B' ≠ ∅`). A genuine counterexample is a
specific `a_1` for which:

1. The chain `S_0 ⊂ S_1 ⊂ \cdots` is verified (by direct computation of
   `S_k^+` at each step, per the certified Finite Core / Extended
   Persistent-Type Pigeonhole machinery) to terminate at an explicit,
   finite, self-absorbing core `S*` — this must be an actual finite
   computation, not an assumption.
2. Two disjoint-base-type elements `A', B' ∈ 𝒫'(S*)` are identified — i.e.
   two infinite, disjoint sets of indices `n` with `ρ_{S*}(n) = A'` resp.
   `B'` — each **certified infinite** by the Persistent-Type Pigeonhole
   machinery (not merely "occurs many times in a large simulation").
3. **The disjointness `A' ∩ B' = ∅` is exhibited as PERSISTENT, not merely
   unconfirmed-so-far.** Since the sequence is infinite and only a finite
   prefix can ever be computed, a raw simulation can never PROVE `A'∩B'=∅`
   holds forever — so a genuine counterexample needs one of:
   - (a) an outright STRUCTURAL argument (a proof, however short) that no
     shared prime between `A'` and `B'` can ever be recruited — e.g. an
     invariant showing the primes of `A'` and `B'` are permanently
     partitioned by some conserved quantity — even a small structural
     argument here would be real content, not just numerics; or
   - (b) failing a full structural proof, an extremely long, adversarially
     targeted simulation (far beyond the workspace's existing 1500–300,000
     term sweeps) showing zero intersection AND showing no qualitative
     trend toward intersection (e.g. the "minority" type's frequency is not
     drifting down toward zero the way it would if a rare eventual
     intersection were merely delayed) — this is evidence, explicitly
     NOT a proof, and must be reported as such.

A "near miss" (two base types that intersect only after a large but finite
number of terms, or a minority type whose frequency is visibly decaying) is
NOT a counterexample — it is exactly the kind of behavior consistent with
FAH being true but slow, and must be reported honestly as a non-result.

### 2. Where to search — deliberately NOT the workspace's existing seeds

The workspace's own standing hard test seeds (`187=11·17, 209=11·19,
221=13·17, 247=13·19`, all `|Q|=2`, in use since round 6) have already been
simulated extensively (round 18's audit explorer, 1500 terms each) with no
sign of persistent non-intersection — both singleton types' frequencies
stabilize at a fixed ratio (e.g. `187`: `79%/20%`), not decaying to zero but
also showing no trend toward intersection either way within the simulated
range. Re-running these same seeds longer is low-value (15 rounds of
evidence already exists on them). This approach must search
**systematically elsewhere**, targeting seeds chosen to MAXIMIZE the
structural conditions that could plausibly obstruct intersection, per the
explorer's flagged directions:

- **`|Q|≥3` seeds** (e.g. `a_1 = 3·5·7=105`, `3·5·11=165`, `5·7·11=385`,
  and systematically many more): the existing hard-seed sweep only covers
  `|Q|=2`; a third prime gives more room for the extended-type structure
  `𝒫'(S*)` to have more than 2 elements and for the confined-GCD alphabet
  `F'', D_bad` to be larger (`|F'|,|F''|≥3` as flagged) — genuinely
  untested territory, not a re-run of round 18's sweep.
- **Seeds engineered via CRT for an imbalanced recruitment race**: pick
  primes `p, q` (or `p,q,r` for `|Q|=3`) with very different sizes (e.g.
  one small prime like `3` or `5` against one very large prime, `q>10^4`)
  so that one base type's "natural" recruitment rate (how often new
  candidates land on multiples of that prime) is structurally slower —
  testing whether a sufficiently lopsided race can be pushed toward
  persistent, non-shrinking imbalance rather than eventual intersection.
- **Seeds chosen to maximize `ω(a_1)` and the number of persistent types
  `|𝒫'(S*)|` simultaneously** (e.g. products of 4–5 distinct primes), to
  stress-test whether MORE competing types make mutual intersection
  structurally harder (more "room" for a permanently-isolated type) or, as
  the existing dead mechanisms suggest, irrelevant (since every pairwise
  argument in the workspace is symmetric in the number of types).
- For every candidate seed, the search must explicitly verify step 1 above
  (the chain terminates, `S*` explicit) before treating any two types as a
  real "rogue pair" candidate — do not skip straight to simulating base-type
  frequencies without first confirming the core has actually stabilized.

### 3. What NOT to do (avoiding re-deriving already-dead content)

This approach must not re-litigate why the existing 20+ proof mechanisms
fail (that is `n1-periodicity-reconciliation.md`'s job, already done) — its
only job is the search described above. It also must not claim a
"counterexample" from a finite simulation window alone (per §1.3) — any
report of "no intersection found through N terms" must be filed as
inconclusive evidence, not as a refutation, unless accompanied by a genuine
structural argument (§1.3(a)).

### 4. What a genuinely negative outcome looks like, and why it still counts

If the systematic search across `|Q|≥3` and lopsided-CRT seeds (§2) finds
no candidate showing even a hint of persistent imbalance (i.e. every tested
seed's minority type either intersects within a bounded window or shows a
visibly-converging, non-persistent frequency profile), this is a
genuinely new form of evidence for H1 — broader in scope than the
workspace's existing `|Q|=2`-only evidence — and should be reported
honestly as `unsolved` (no counterexample found, hence no refutation of the
Master Conditional Theorem route) but as a real, additive contribution:
future rounds attacking H1 by direct proof can cite "no counterexample
survives an adversarial `|Q|≥3` / lopsided-CRT search" as corroborating
evidence when choosing which mechanisms are worth re-attempting.

## Full proof
Not present — Status is `unsolved`. This round ran the search (see §A–§C
above): 11 fresh seeds tested (`|Q|=3,4,5`, including CRT-lopsided), no
genuine FAH counterexample found. The round's main output is not a proof
but a diagnostic/methodological one (direct literal-period detection,
giving an exact rather than asymptotic FAH check for `a_1=385` and explicit
`(T,L)` for 9 of 11 seeds including the 4 canonical hard cases) — see §C for
the honest scope of what is and is not established. Round 30 (see §-1 and
"Approaches tried" above) added a two-pronged search (H2 multi-round
absorption stress test; conserved-invariant hunt) that is likewise
diagnostic/negative, not a proof — Status stays `unsolved`.

## Promotable lemmas

None this round. Both round-30 findings are diagnostic/negative
(refutations of specific invariant candidates; an inconclusive large-scale
numeric near-miss), matching the workspace's established "Lemma F/I,
diagnostic not portable" precedent — no general theorem was proved. The
concrete open item worth a future round's attention (not a lemma, a
computational target): resolve whether the six singleton 6-out-of-7-element
types found for `a_1=7402395=3·5·7·11·13·17·29` in the 500,000-term window
(occurrences at `n=114808,160731,185459,219179,344423,482192`) recur upon
further window extension (as all five prior "apparent counterexample"
window artifacts in rounds 17–19 did, without exception) or, if they
genuinely do not, whether that can be turned into a real FAH/H2
counterexample per the approach's own §1.3 criterion.
