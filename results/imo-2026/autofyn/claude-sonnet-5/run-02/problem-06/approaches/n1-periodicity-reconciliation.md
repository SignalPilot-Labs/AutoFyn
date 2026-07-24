## Status
partial

## Approaches tried
- **n1-periodicity-reconciliation** (round 25, H2 numeric-diagnosis
  reconciliation, §10 below) — Folded in a corrected reading of round 24's
  H2-threatening claim that `a_1=11305`'s new-extended-type arrival rate
  "stays flat `~sqrt(N)`" over `400{,}000` terms. Per this round's
  `math-explorer-h2-asymmetry` (`/tmp/round-25/math-explorer-h2-asymmetry.md`),
  a much larger re-simulation (`4807` to `n=1{,}000{,}000`, `11305` to
  `n=750{,}000`) using a corrected LOCAL-EXPONENT methodology (rather than
  round 24's global power-law fit, contaminated by early-transient growth)
  shows: `11305`'s true local exponent is `\approx0.22$–$0.28`, well below
  `0.5` even at its highest reading (so the literal `\sqrt N` claim is
  withdrawn), and it IS decreasing over time, just more slowly than `4807`'s
  (which shows a sharp late-stage collapse to `0.06$–$0.09` by `n=1M`, only
  visible past `n\approx500$k`, i.e. `11305` may simply need more runway,
  plausibly because its Finite-Core-Theorem-enlarged core is larger, `|S_0|=
  12` vs `9`). Recorded honestly (§10): this is a numeric DE-THREATENING of
  round 24's alarm, not evidence FOR H2 in any proof-theoretic sense — no
  bound on `(N(S_k))_k` follows from any amount of simulation, and `11305`'s
  behavior past `n=750{,}000` (continued deceleration toward collapse vs.
  asymptoting to a positive exponent, which would in fact refute H2 for this
  seed) remains genuinely unresolved by this round's reach. Assessed the
  "does this suggest new H2 machinery" question explicitly and concluded no
  — the one semi-concrete follow-up (a size-normalized statistic
  `T(N)/2^{|S_0|}` for fairer cross-seed comparison) is a measurement
  refinement, not a proof technique, and does not evade the already-recorded
  structural obstruction (§4.2: full-factorization containment, not
  shared-prime or type-count observations, is what self-absorption actually
  requires). No new H2 mechanism attempted this round, per the dispatch's
  own instruction to only attempt one if genuinely novel. Status stays
  `partial`, unchanged; H1 and H2 both remain fully open.
- **n1-periodicity-reconciliation** (round 20, correction + tightened
  write-up) — Two contributions, per this round's dispatch. (1) **Withdrew
  round 19's Generalized Class-Blindness Obstruction** (found circular by the
  round-19 reviewer, independently re-diagnosed as a general screening rule
  by this round's fresh-framing explorer) and replaced it with a correctly
  and narrowly scoped **Ambient-Statistic Obstruction** (§7, fully proved,
  non-circular): restricts to statistics that are, by their defining formula,
  structurally incapable of referencing realized sequence data (matching the
  TRUE scope of the two already-certified predecessors, `escape-cost-
  vacuity.md` and `density-argument-vacuity-corollary.md`), and replaces the
  withdrawn "two REALIZABLE continuations" construction with a "two
  ASSIGNMENTS consistent with the finitely many CITED premises" soundness
  argument — a standard semantic-entailment-failure check requiring no
  construction of alternate legal completions of the (fully deterministic)
  sequence. Explicitly and honestly scoped (§7.3-§7.4): this certifies a
  correct UNIFICATION of the two pre-existing ambient lemmas into one proof,
  NOT an extension to the occupancy-referencing (i.e. practically useful)
  forms of second moment / Borel–Cantelli / finite-Fourier / LP-relaxation,
  which remain formally un-ruled-out — the precise opposite of round 19's
  overclaim, now corrected. (2) Tightened the write-up (new §E, an executive
  summary at the top of "Current best") per this round's audit-insurance
  explorer's 6-point recommended structure: states the problem's claim
  up front, reproduces Theorem A (`2|a_1`) and Theorem B (`a_1=p^k`) as full
  short proofs inline (not mere citations), states the Master Conditional
  Theorem with H1/H2 spelled out precisely, and gives an honest, grouped
  (not just counted) summary of the 20+ dead FAH mechanisms across 14
  plateau rounds. Status stays `partial`; neither contribution touches H1 or
  H2 directly, as instructed.
- **n1-periodicity-reconciliation** (round 19, consolidation + new meta-lemma)
  — Two contributions, per this round's dispatch. (1) Certified a new
  **Generalized Class-Blindness Obstruction** (§7 below), a strict
  generalization of the certified Density-Argument Vacuity Corollary /
  Escape-Cost Vacuity Theorem / Selection-Rule Class-Blindness finding, from
  "density/counting statistics" to the ENTIRE statistical-method family
  (second moment, Borel–Cantelli, finite-Fourier/character-sum, LP-relaxation)
  in one meta-argument, closing off this round's fresh-framing explorer's
  entire item-3/item-4 search space in one certified statement rather than
  requiring four separate refutations. (2) Tightened and consolidated the
  write-up (§8 below) of the run's two guaranteed unconditional deliverables
  — the `2|a_1` theorem and the `a_1=p^k` theorem — as an explicit,
  self-contained "floor deliverable" audit, independent of whether H1/H2 are
  ever resolved. Neither contribution touches H1 or H2 directly (as
  instructed); both are honestly scoped as consolidation/meta-argument, not
  new progress toward either open hypothesis. Verdict: pending review, Status
  stays `partial` at the workspace level.
- **n1-periodicity-reconciliation** (round 18, advance/documentation) — Not a
  new proof attempt on H1/H2 (the Master Conditional Theorem chain, §0-§2, is
  unchanged and was independently re-audited gap-free again this round by the
  outline reviewer). Recorded two new, permanent negative findings from this
  round's audit-insurance explorer, independently re-verified from scratch by
  this builder via fresh Python simulations (§6, scripts at
  `/tmp/round-18/verify_odd2.py`, `/tmp/round-18/verify_q2.py`): (1) the
  **Odd-Prime Non-Trivialization Proposition** (§6.1) — the `2 | a_1`
  trivialization of H1 (§4.1) does NOT generalize to odd primes `p | a_1`;
  concrete counterexample `a_1 = 15` (and `a_1 = 45`, same `Q = \{3,5\}`)
  exhibits an exact, persistent period-4 alternation between disjoint base
  types `\{3\}` (75% of terms) and `\{5\}` (the remaining 25%, at
  `n ≡ 3 \pmod 4` exactly), confirmed unbroken over 3000 simulated terms, with
  a structural explanation (the `p=2` mechanism relies on zero intermediate
  candidates between "definitely illegal" and "next multiple of p," true only
  for `p=2`); (2) confirmation that **`|Q|=2` is NOT a tractable general
  subfamily** for H1 (§6.2) — the explorer's 36-seed sweep reproduces exactly
  the workspace's own long-standing canonical hard test seeds (`187, 209, 221,
  247`, in use since round 6), independently re-confirmed by this builder
  (seed-dependent divisibility ratios `\approx 79\%/20\%, 81\%/18\%,
  62\%/36\%, 58\%/37\%` respectively, no closed form). Both findings are
  honestly filed as permanent negative/documentation results, not progress
  toward H1 or H2 themselves — Status stays `partial`, unchanged.
- **n1-periodicity-reconciliation** (round 16, consolidation/write-up) — Per the
  round-15 escalation rule (option (a): write up the current-best result rigorously
  and honestly, with FAH as the sole open ingredient), this round is a pure
  assembly round, not a new mechanism attempt. Assembled, in one place (§0-§2
  below), the **full conditional theorem chain** — a single "Master Conditional
  Theorem" — proving the problem's actual claim (existence of T, L with
  a_{n+T} = a_n + L for every positive integer n) CONDITIONAL on exactly two
  precisely-stated open hypotheses (H1) FAH at the eventual absorption-chain limit
  and (H2) termination of the absorption chain, each cross-referenced to its
  equivalent certified formulations (Symmetric FAH / Cofinite FAH / EEA for H1 via
  the certified equivalences already established elsewhere in the workspace; the
  Termination Criterion Lemma's boundedness-of-N(S_k) reformulation for H2).
  Explicitly did **not** attempt an 18th FAH mechanism (H1 untouched, as
  instructed) — the sibling approach `core-growth-monotonicity` is this round's
  dedicated, separate attempt at H2, not duplicated here.
  Cross-referenced this round's new **even-a1-full-periodicity-theorem** as a
  genuinely complementary, fully unconditional result covering the 2 | a_1
  subfamily by an entirely different, self-contained elementary argument that
  bypasses the whole S₀/S*/FAH machinery (§3). Attempted the dispatch's
  suggested small stretch — whether 2 ∈ Q trivializes the absorption chain's
  termination (H2) the same way it trivializes FAH (H1) — and found a genuine,
  provable **positive** result for H1 (a clean unconditional corollary: 2 | a_1
  forces FAH to hold vacuously, in fact forces EVERY two extended-persistent
  types, not just disjoint-base-type ones, to intersect — §4.1) but a genuine
  **negative** finding for H2 (the same trick does NOT transfer: self-absorption
  requires containment of an early term's ENTIRE prime factorization in the core,
  a categorically stronger requirement than the mere shared-prime-2 argument that
  settles H1; no mechanism forcing this was found, and none is expected to exist
  from a single shared prime alone — §4.2). This is reported honestly as a
  genuine but incomplete stretch result, not folded into the write-up as if H2
  were resolved for 2 | a_1. No new FAH mechanism (18th) was attempted; the
  workspace's FAH mechanism-graveyard count is unchanged by this round's
  activity on this slug.

## Current best

### §10. Round 25: corrected H2 numeric diagnosis (`a_1=11305` vs `4807`
arrival-rate asymmetry) — reconciliation of round-24's framing, no new proof
content on H1 or H2 themselves

This section folds in the corrected reading of a numeric H2-side finding that
a sibling approach (`h2-absence`-lens explorer work, feeding into
`core-growth-monotonicity` / `new-prime-recruitment-rate-bound`) raised in
round 24 and that this round's `math-explorer-h2-asymmetry`
(`/tmp/round-25/math-explorer-h2-asymmetry.md`) re-examined at larger scale
with a corrected methodology. This file records the reconciled picture so
that no future round cites round 24's original framing without the
correction below.

**What round 24 reported.** Simulating the two canonical hard seeds'
distinct-extended-`S_0`-type arrival counts out to `n=400{,}000`, round 24
fit a single global power law `T(N) \approx C\cdot N^{p}` from `n=25{,}000`
onward for each seed, and reported `a_1=4807`'s exponent `p` as decelerating
while `a_1=11305`'s stayed "flat near `0.51`–`0.57`" — i.e. close to
`\sqrt N` growth, unbounded on the face of it — and flagged this as
H2-threatening for `11305` specifically (H2 requires `(N(S_k))_k` to be
bounded; a genuinely unbounded rate of new-type arrivals at the terminal
core, if it persisted, would suggest `N(S_k)` grows without bound along the
absorption chain rather than stabilizing).

**What this round's larger, methodologically corrected re-simulation
found.** `/tmp/round-25/math-explorer-h2-asymmetry.md` reproduces round 24's
raw counts exactly at the checkpoints they share (a genuine sanity check,
not just a re-assertion), then extends the simulation substantially further
— `a_1=4807` to `n=1{,}000{,}000` (a new checkpoint set: `132, 150, 165, 181,
192, 200, 208, 216, 220` distinct types at `n=25\text{k},\dots,1000\text{k}`)
and `a_1=11305` to `n=750{,}000` (`335, 402, 481, 584, 651, 702, 737, 806` at
the same style of checkpoints) — and recomputes the growth exponent using a
**local** (consecutive-checkpoint) formula `p_{\text{local}} :=
\log(T_2/T_1)/\log(N_2/N_1)`, rather than round 24's single global fit over
the whole range. The global fit is shown to be contaminated by each seed's
own steep early-transient recruitment (the first `\sim 50$–$100$k terms
recruit types fast for any seed, biasing a single global exponent
estimate upward). The corrected local exponents are:

- `4807`: `0.138, 0.134, 0.146, 0.142, 0.176, 0.093, 0.064` across the
  seven consecutive checkpoint intervals from `50\text{k}$–$100\text{k}` out
  to `750\text{k}$–$1000\text{k}` — a clear, sharp late-stage collapse
  (the exponent drops by more than half between the `500$k`-ish plateau and
  the `1M` mark), the signature of a decelerating, likely-convergent-type
  arrival process.
- `11305`: `0.259, 0.280, 0.268, 0.262, 0.218, 0.221` across its six
  available intervals out to `750\text{k}` — mild deceleration (from
  `\sim0.27` down to `\sim0.22`), well below `0.5` even at its highest
  reading (so the literal "`\sim\sqrt N`" claim from round 24's global fit
  does **not** survive the corrected local computation), but with **no**
  sharp late-stage collapse visible yet at the scale reached (`750$k`).

**The corrected verdict, stated precisely (not overclaimed either
direction).** Round 24's specific numeric claim — that `11305`'s
type-arrival rate is flat at `\sim\sqrt N`, in a way qualitatively different
from and more alarming than `4807`'s decelerating behavior — does **not**
survive the corrected local-exponent methodology: `11305`'s true local
exponent (`\approx0.22$–$0.28`) is well under `0.5` throughout the measured
range, and it **is** decreasing over time (from `\sim0.27` to `\sim0.22`),
just more slowly than `4807`'s. So round 24's H2-threatening framing for
`11305` is **withdrawn as originally stated** and replaced by: **both
canonical hard seeds show numerically decelerating type-arrival rates over
this round's extended simulation range; `4807` decelerates faster and has
already reached a small exponent (`0.06$–$0.09`) by `n=1{,}000{,}000`, while
`11305` is still at a moderate, only mildly-decreasing exponent
(`\approx0.22`) at `n=750{,}000`.**

A plausible (not proved) structural account for the asymmetry, also from
this round's explorer report: `11305`'s Finite-Core-Theorem-enlarged core is
larger than `4807`'s (`|S_0(11305)|=12` vs `|S_0(4807)|=9`, itself downstream
of `|Q(11305)|=4` vs `|Q(4807)|=3` distinct base primes recruiting more
witnesses), so its nominal extended-type state space (`2^{12}=4096` vs
`2^9=512`) is `8\times` larger; a bigger nominal state space plausibly needs
more runway before any convergence signature becomes numerically visible,
by direct analogy with the fact that `4807`'s own collapse only appeared
between `n=500{,}000` and `n=1{,}000{,}000` — invisible at the same absolute
scale (`n=500$k`) where `11305` currently sits at `n=750$k`. This is a
plausibility account only, not a mechanism proof; no bound was derived
relating `|S_0|` to the runway needed for observable deceleration.

**What this section does NOT claim (honesty check against overclaiming).**
This is a **numeric de-threatening**, not evidence *for* H2 in any
proof-theoretic sense, and this file does not treat it as such:

1. No finite amount of simulation, however far extended, can establish that
   `(N(S_k))_k` is bounded (H2's precise content, per the certified
   Termination Criterion Lemma, §1 above) — that is a statement about a
   process that could in principle diverge arbitrarily slowly, or converge
   arbitrarily slowly, and no window of numeric checkpoints distinguishes
   "genuinely converging" from "a slowly-saturating curve that merely looks
   like a decaying power law over one order of magnitude" (the explorer
   report's own honest caveat, independently endorsed here: e.g. curves of
   the shape `T(N) = A - B/N^{0.05}` can mimic a slowly-drifting positive
   exponent over exactly this kind of range).
2. The corrected reading removes a specific *pessimistic* numeric flag
   (the appearance of literal `\sqrt N` growth for `11305`) — it does not
   supply a new *positive* mechanism, lemma, or bound toward H2. No lemma in
   `results/imo-2026-06/lemmas/` bounds `(N(S_k))_k`, before or after this
   correction; that remains the entirely open content of H2.
3. `11305`'s trajectory past `n=750{,}000` is genuinely unknown: it could
   continue decelerating toward the same kind of collapse `4807` shows (H2-
   consistent), or it could asymptote to a positive constant exponent
   (a genuine, unbounded, sub-`\sqrt N` power-law growth rate — which would
   in fact REFUTE H2 for this seed, since it would mean the terminal-core
   type inventory, and hence plausibly `N(S_k)` along some cofinal
   subsequence of the chain, grows without bound). This round's data cannot
   distinguish these two futures.

**Does this change what the next concrete H2 mechanism attempt should look
like?** After reviewing the corrected numbers, the honest answer is: **no
genuinely new mechanism suggests itself from this correction alone.** The
one semi-concrete methodological suggestion in the explorer's report — track
a size-normalized statistic such as `T(N)/2^{|S_0|}` (or `T(N)/(\text{a
realized-type ceiling})`) across seeds of differing `|S_0|`, rather than
comparing raw counts `T(N)` — is a reasonable proposal for making
CROSS-SEED comparison fairer, but it is a **measurement refinement**, not a
proof technique: even a perfectly clean normalized statistic showing
"`11305` and `4807` are on the same normalized trajectory" would still only
be numeric evidence, of exactly the same non-proof-theoretic character as
every other simulation result in this workspace (see the extensive existing
numeric record on H2 across rounds 14–24, none of which has ever converted
into a proof). It does not evade the structural obstruction already on
record in this file (§4.2 above): no argument here or elsewhere forces an
early term's FULL prime factorization into a bounded core from any
shared-prime or type-count observation, numeric or otherwise. Consequently
this round does **not** attempt new H2 machinery on the strength of this
correction alone — that would repeat the workspace's own recorded mistake
(round 19's circularity, §7 above) of treating a numeric or definitional
observation as if it supplied deductive leverage it does not.

**Net effect on Status.** This section is honest documentation and
correction of a diagnosis, not new proof content: it neither closes H1 nor
H2, nor opens a new concrete attack route on either. **H2 remains entirely
open, exactly as stated in §1** — the corrected picture is "the round-24
numeric alarm for `11305` specifically does not survive scrutiny; the
general open status of H2 is unchanged." Status stays `partial`.

### §E. Executive summary / quick reference (NEW, round 20 — per this round's
audit-insurance explorer's recommended 6-point structure, so this file is
directly usable as the run's floor/insurance deliverable without requiring a
reader to trace every cross-reference below)

**1. The problem's claim.** Fix a positive integer `a_1`, and define `(a_n)`
by: `a_{n+1}` is the least positive integer not among `a_1,\dots,a_n` with
`\gcd(a_{n+1},a_i) > 1` for every `i \le n`. The claim to be proved is: there
exist positive integers `T, L` such that `a_{n+T} = a_n + L` for every
`n \ge 1`.

**2. Two fully certified, unconditional subfamilies (proofs reproduced in
full, short enough to be self-contained here).**

- **Theorem A (`2 \mid a_1`).** If `2 \mid a_1` then `a_n = a_1 + 2(n-1)` for
  every `n \ge 1` (so `T=1, L=2` works literally from `n=1`). *Proof:* strong
  induction on `n`. Base case `n=1` trivial. Suppose `a_1,\dots,a_n` are all
  even. The candidate `a_n+1` is illegal: `\gcd(a_n+1,a_n)=1` since consecutive
  integers are coprime, so it fails against index `n` alone (no evenness
  needed for this half). The candidate `a_n+2` is legal: it is even, and every
  one of `a_1,\dots,a_n` is even by the inductive hypothesis, so
  `2 \mid \gcd(a_n+2,a_i)` for every `i \le n`. By minimality of the greedy
  rule, `a_{n+1}` is forced to be the least legal candidate exceeding
  `a_n`, and `a_n+1` has just been shown illegal while `a_n+2` has just been
  shown legal, so `a_{n+1}=a_n+2` exactly (nothing strictly between `a_n+1`
  and `a_n+2` exists to check). In particular `a_{n+1}` is even, closing the
  induction; summing the constant increment `+2` over `n-1` steps from `a_1`
  gives `a_n=a_1+2(n-1)`. `\blacksquare` (Certified in full generality, with
  no additional gap, as `even-seed-literal-periodicity-theorem.md`, round 16.)

- **Theorem B (`a_1=p^k`, `p` prime, `k\ge1`).** Then `a_n=a_1+p(n-1)` for
  every `n\ge1` (`T=1,L=p`). *Proof:* strong induction on `n`, identical
  shape to Theorem A but using the full prime-power constraint. Suppose
  `a_1,\dots,a_n` are all divisible by `p` (base case trivial as `a_1=p^k`).
  For each `1\le j\le p-1`: `P(a_1)=\{p\}` is a singleton (as `a_1=p^k`), and
  `p\nmid(a_n+j)` because `p\mid a_n` and `0<j<p`; hence
  `\gcd(a_n+j,a_1)=1`, so `a_n+j` is illegal (fails against index `1`) for
  every one of these `p-1` intermediate candidates. The candidate `a_n+p` is
  legal: `p\mid(a_n+p)` and `p$ divides every one of `a_1,\dots,a_n$ by the
  inductive hypothesis, so `p\mid\gcd(a_n+p,a_i)` for every `i\le n`.
  Minimality forces `a_{n+1}=a_n+p` exactly (every intermediate candidate
  `a_n+1,\dots,a_n+p-1` has just been ruled out), propagating `p\mid a_{n+1}`
  and closing the induction; summing gives `a_n=a_1+p(n-1)`. `\blacksquare`
  (Certified in full generality as
  `prime-power-seed-literal-periodicity-theorem.md`, round 18.)

  These two theorems overlap exactly on `a_1=2^k` (`k\ge1`, both give
  `T=1,L=2`) and are otherwise disjoint: A additionally covers every even
  `a_1` with `|Q|\ge2` (e.g. `6,30,210`), B additionally covers every
  odd-prime-power `a_1` (e.g. `9,25,27,49,121`). Together: **the problem's
  claim is fully, unconditionally proved for every `a_1` in
  `\{a_1 : 2\mid a_1\} \cup \{a_1 : a_1=p^k \text{ for a prime } p\}`.**

**3. The Master Conditional Theorem (full statement, general `a_1`).** For
every OTHER `a_1` (every odd non-prime-power, e.g. `15, 187, 209, 221, 247`),
the problem's claim is reduced — by a complete, independently re-audited,
gap-free chain of certified lemmas (§0–§2 below) — to exactly two precisely
stated open hypotheses:

- **(H1) FAH at the terminal core.** IF the absorption chain
  `S_0 \subset S_1 \subset \cdots` (§1 below) terminates at some `S^*`, THEN
  every two disjoint-base-type elements of the extended-persistent-type set
  `\mathcal P'(S^*)` intersect.
- **(H2) Termination.** The absorption chain reaches a fixed point in
  finitely many steps — equivalently (Termination Criterion Lemma) the
  threshold sequence `(N(S_k))_k` is bounded.

  **(H1) and (H2) together `\Rightarrow` the problem's claim**, for that
  `a_1` (§2's Master Conditional Theorem, proved in full below). Neither
  hypothesis is established for any `a_1` outside the two subfamilies of
  item 2.

**4. Honest summary of the FAH (H1) mechanism graveyard — 14 consecutive
plateau rounds (6–19), 20+ named, independently-confirmed-dead mechanism
families, at a level of detail useful to a reader deciding whether to
re-attempt one.** Grouped by root cause of death, not just counted:

  - *Existential-to-universal promotion attempts* (competitor-construction /
    gcd-pigeonhole family, rounds 6–9): produce a single existential witness
    prime for infinitely many occurrences, but every attempt to promote this
    to a witness for COFINITELY many occurrences collapses back into FAH
    itself (the promotion step IS the open content) — includes the round-7
    Witness Discontinuity Obstruction (a concrete counterexample, `a_1=175`,
    showing the natural repair breaks witness continuity) and the round-9
    Recruitment-Budget Lemma refutation.
  - *Magnitude/sandwich and CRT-glue/covering-system attempts* (rounds 8–11):
    try to force a legal candidate at a specific residue by controlling
    magnitude or gluing moduli via CRT; found to require moduli products that
    overshoot the sequence's actual growth rate by 8+ orders of magnitude
    (round 11's CRT Magnitude Obstruction) — a quantitative, not qualitative,
    death.
  - *Sieve/density/statistical-method family* (density ratios, second
    moment, Borel–Cantelli, finite-Fourier/character-sums, LP-relaxation;
    rounds 10–19): each instance, when it references realized occupancy/value
    data of the sequence (which it must, to say anything FAH-relevant), was
    found NOT provably rulable-out by any certified lemma — see §7 below for
    the precise, now-CORRECTED scope of what IS certified here (a strictly
    narrower "ambient-statistic" obstruction) versus round 19's overclaimed,
    found-circular broader version.
  - *Automaton/graph-walk/Morse–Hedlund/subword-complexity and EEA* (rounds
    12–13): proven EQUIVALENT in difficulty to FAH itself (a reformulation,
    not a bypass) via the certified EEA-implies-periodicity reduction.
  - *Algebraic-number-theory, generating-function, o-minimality,
    computability/priority-argument, nonstandard-analysis, and Baire-category
    reframings* (rounds 15, 17, 19, 20): each checked structurally and found
    either to collapse into already-certified content or to require a genuine
    mathematical structure (definable tameness, a free ensemble of possible
    completions, undecidability) that is simply ABSENT from this fully
    deterministic, arithmetic recursion.
  - *Extremal graph theory on the resolving-prime conflict structure*
    (round 14): subsumed entirely by the certified Hub Singleton Batch Lemma.
  - *Crux-corpus transplant* (rounds 17–20): no genuinely analogous pre-2026
    precedent found after repeated systematic searches (closest matches —
    `aimo-0009`, `aimo-0077`, `aimo-0184` — all fail to transfer for
    precisely stated structural reasons, see the round-20 fresh-framing
    explorer's report).

  The recurring diagnosis, sharpened this round (§7): **every one of these
  families that got as far as a genuine attempted proof did so by implicitly
  assuming an ensemble of "possible" continuations of the sequence consistent
  with a fixed finite prefix — but the recursion is fully deterministic given
  `a_1`, so no such ensemble exists without an explicit construction (e.g. two
  actual seeds sharing a long common core and then verifiably diverging).
  This structural reason, not merely "we tried hard and failed," is why this
  entire proof-STYLE family is unlikely to close H1 without a genuinely new
  ingredient.**

**5. Status: `partial`, honestly.** H1 and H2 are both open. Full detail,
proofs, and citations for everything summarized above are in §0–§9 below;
the two live sibling approaches attacking H1 directly this round are
`triangle-consistency-pigeonhole` and `triangle-critical-dichotomy-witness`
(not duplicated in this file).

### §0. The certified stack this chain is built from (imported, not re-derived)

All of the following are certified, unconditional lemmas already in
`results/imo-2026-06/lemmas/`, reused here by citation only:

1. **Free Facts** (`free-facts-gcd.md`): gcd(a_i, a_j) > 1 for all distinct i, j ≥ 1.
2. **Persistent-Type Pigeonhole** (`persistent-type-pigeonhole.md`): with
   Q := P(a_1) and τ(n) := P(a_n) ∩ Q, the finite set
   𝒫 := {A ⊆ Q : A ≠ ∅, {n : τ(n)=A} infinite} is nonempty, and τ(n) ∈ 𝒫 for all
   n beyond some finite threshold N₀.
3. **Finite Core Theorem** (`finite-core-theorem.md`): an explicit finite core
   prime set S₀ ⊇ Q, built from canonical witnesses (one per element of 𝒫), such
   that the Bounded Witness / Generalized Bounded Witness machinery applies
   relative to S₀.
4. **Extended Persistent-Type Pigeonhole** (`extended-persistent-type-pigeonhole.md`),
   certified generically at any finite core S ⊇ Q (not merely S₀): with
   ρ_S(n) := P(a_n) ∩ S, there is a finite, nonempty set 𝒫'(S) of
   S-extended-persistent types and a finite threshold N(S) with ρ_S(n) ∈ 𝒫'(S)
   for all n > N(S).
5. **Self-Absorbing Core Theorem** (`self-absorbing-core-theorem.md`, certified
   round 14): for a finite core S* ⊇ S₀, define the absorption operator
   S⁺ := S ∪ ⋃_{j=1}^{N(S)} P(a_j) and call S self-absorbing if S⁺ = S. IF S* is
   self-absorbing AND FAH holds at level S* (every two elements of 𝒫'(S*)
   intersect within S*), THEN with L* := ∏_{p∈S*} p and the explicit finite set
   G* ⊆ Z/L*Z defined there, T* := |G*|:
     a_{n+T*} = a_n + L*  for every n ≥ N(S*).
6. **Universal Early Intersection Lemma** (`universal-early-intersection-lemma.md`,
   certified round 15): IF S* is self-absorbing (no FAH needed for this lemma
   alone), THEN P(a_j) ∩ B ≠ ∅ for every j = 1,...,N(S*) and every B ∈ 𝒫'(S*).
7. **Literal n = 1 Periodicity Theorem** (`literal-n1-periodicity-theorem.md`,
   certified round 15): under the SAME two hypotheses as #5 (S* self-absorbing,
   FAH at level S*), the SAME G*, T*, L* satisfy
     a_{n+T*} = a_n + L*  for EVERY n ≥ 1
   (not merely n ≥ N(S*)) — proved by re-running the Sufficiency/Landing/
   Assembling argument of #5 over the extended range, using #6 to cover the new
   range in Landing's second conjunct.
8. **Termination Criterion Lemma** (`termination-criterion-lemma.md`, certified
   round 15): defining S_0 := S₀, S_{k+1} := S_k⁺, the chain (S_k)_{k≥0}
   terminates (reaches a fixed point S_K = S_{K+1}, i.e. a self-absorbing core) in
   finitely many steps **if and only if** the sequence of thresholds
   (N(S_k))_{k≥0} is bounded.
9. **Monotonicity of Resolution** (`monotonicity-of-resolution.md`): FAH holding
   at a core S implies FAH holds at every core S' ⊇ S (used to transport FAH from
   S₀ up the absorption chain to whichever S_k it is assumed to hold at).

### §1. The two open hypotheses, stated precisely

Define the absorption chain S_0 := S₀, S_{k+1} := S_k⁺ (well-defined for every
k, by #4 applied at each finite core S_k in turn). Two, and only two, open
hypotheses remain in this approach's dependency chain:

**(H1) FAH at the (assumed) terminal core.** IF the chain (S_k) terminates at
some S* := S_K (i.e. S_K = S_{K+1}), THEN every two elements A, B ∈ 𝒫'(S*)
satisfy A ∩ B ≠ ∅. (Equivalently, by the certified Precision Note in
`self-absorbing-core-theorem.md`: every two DISJOINT-BASE-TYPE elements of
𝒫'(S*) intersect — the standard formulation of FAH used throughout this
workspace, already proved equivalent to the "every two elements intersect" form
via the free fact that non-disjoint-base-type pairs intersect automatically.
This is the same object as Symmetric FAH / Cofinite FAH / EEA, the equivalent
formulations certified elsewhere in the workspace — see
`eea-implies-periodicity.md` and the round 12 EEA reduction — none of which have
been proved or refuted after 11 consecutive rounds (rounds 6–16) and 17+
independently-confirmed-dead mechanism attempts, catalogued in the "Approaches
tried" history above.)

**(H2) Termination of the absorption chain.** The chain (S_k)_{k≥0} reaches a
fixed point in finitely many steps. By the Termination Criterion Lemma (#8
above), this is EQUIVALENT to: the sequence (N(S_k))_{k≥0} is bounded. This is a
logically distinct object from H1 (per the round-15 analysis, reconfirmed by
this round's own outline-review: N(S) measures the onset-of-persistence timing
at core S, a pigeonhole threshold about *when* types stabilize, whereas H1 is
about whether stabilized types, once occurring, *intersect* each other — no
reduction either way between H1 and H2 is known). H2 is the dedicated target of
this round's sibling approach `core-growth-monotonicity`; it is not attacked
directly in this file.

### §2. The Master Conditional Theorem (this round's consolidation)

**Theorem.** Let a_1 be any positive integer, and let (a_n) be the associated
greedy sequence. If (H1) and (H2) both hold (for the specific chain (S_k)
generated from this a_1), then there exist positive integers T, L such that

  a_{n+T} = a_n + L  for every positive integer n ≥ 1,

i.e. the problem's claim holds for this a_1.

*Proof.* By (H2) and the Termination Criterion Lemma (#8), the chain (S_k)
reaches a fixed point at some finite step K: S* := S_K = S_{K+1}, i.e. S* is
self-absorbing (S*⁺ = S*, in the sense of #5's definition). By (H1), FAH holds
at this specific terminal core S* (this is literally the content of H1 as
stated in §1, phrased relative to the chain's actual terminal point). The two
hypotheses of the certified Literal n = 1 Periodicity Theorem (#7) — S* ⊇ S₀
self-absorbing; FAH holds at level S* — are therefore both satisfied. Applying
#7 directly: with L* := ∏_{p∈S*} p and T* := |G*| (G* the explicit finite set
defined in #5/#7), a_{n+T*} = a_n + L* for every n ≥ 1. Taking T := T*, L := L*
proves the claim. ∎

This is the complete, gap-free, unconditional-modulo-(H1)-and-(H2) reduction of
the whole problem: **every certified step from Free Facts down to the Literal
n = 1 Periodicity Theorem has been independently verified with no gap** (see
the certification notes in each cited lemma file, particularly the round-13/14
"combining both parts" gap that was found and fully closed, and the round-15
Universal Early Intersection Lemma extension). The ONLY two things standing
between this Master Conditional Theorem and a full, unconditional solution of
the problem are H1 and H2, each precisely stated in §1, and each cross-linked
to its already-certified equivalent formulations elsewhere in the workspace so
that no future round mistakes either for a fresh, unstudied question — both
have dedicated prior-round or same-round attempts on record (H1: 17+
independently-confirmed-dead mechanisms across rounds 6–16; H2: the
Termination Criterion Lemma reduction, round 15, plus this round's dedicated
`core-growth-monotonicity` attempt).

**What is NOT claimed.** This theorem does not resolve the problem for general
a_1 — it is a conditional reduction, not a proof. Neither H1 nor H2 is
established for any a_1 for which the chain does not trivially collapse (see
§4.1 for the one case, 2 | a_1, where H1 does trivialize — but note §4.2, where
H2 is shown NOT to trivialize by the same mechanism, so even the 2 | a_1 case is
not closed via this chain; it is closed instead by the entirely separate
argument of §3).

### §3. Complementary result: the even-a1 special case (§3 is a summary/citation
only — the proof itself lives in the sibling approach file, not reproduced here)

This round's new sibling approach, `even-a1-full-periodicity-theorem.md`, proves
— completely, unconditionally, and by a technique entirely independent of the
S₀/S*/FAH machinery of §0-§2 — that if 2 | a_1, then a_n = a_1 + 2(n-1) for
every n ≥ 1, so T = 1, L = 2 works literally from n = 1. The mechanism (stated
here for cross-reference, proved in full in that file, not re-derived here) is
a direct strong induction: if a_1,...,a_n are all even, the candidate a_n + 1 is
always illegal (gcd(a_n+1, a_n) = 1, consecutive integers are always coprime,
no evenness needed for this half), while a_n + 2 is always legal against every
one of a_1,...,a_n simultaneously (all even, so gcd(a_n+2, a_i) ≥ 2 for every
i ≤ n), forcing a_{n+1} = a_n + 2 by minimality of the greedy definition, and
in particular a_{n+1} is even, closing the induction.

**Relationship between this file's target and that one.** These are
**complementary, non-overlapping** contributions to the same workspace, not
competing routes to the same sub-case:

- The Master Conditional Theorem (§2) targets **every** a_1, but only
  conditionally (on H1, H2) — it is honestly `partial` as a whole.
- `even-a1-full-periodicity-theorem` targets exactly the sub-family 2 | a_1, but
  **unconditionally** — it is `solved` for its own restricted target, with no
  dependence on H1, H2, or any part of the S₀/S*/FAH apparatus at all.

Together they show: the problem's claim is fully proved for the (infinite)
subfamily 2 | a_1, and reduced to exactly two named open hypotheses for the
rest. Neither result subsumes the other — `even-a1-full-periodicity-theorem`'s
technique is elementary and does not generalize to smallest-prime-factor p ≥ 3
(as that file's own outline correctly disclaims: p − 2 ≥ 1 intermediate
candidates per step are not automatically resolved by bare consecutive-integer
coprimality alone), while the Master Conditional Theorem's technique is general
but not unconditional. This workspace's overall Status therefore correctly
remains `partial`: a genuine subfamily is fully solved, the general claim is
fully reduced to two named hypotheses, and neither of those hypotheses is
established.

### §4. The dispatched small stretch: does 2 | a_1 trivialize (H1) and/or (H2)
inside the general framework?

This section is an HONEST exploration of the dispatch's suggested stretch goal
— it produces one genuine, fully proved unconditional corollary (§4.1) and one
genuine, fully proved NEGATIVE finding (§4.2), neither smuggled in as more than
it is.

#### §4.1. H1 trivializes when 2 | a_1 — proved, unconditional corollary

**Corollary (Vacuous FAH under 2 | a_1).** If 2 | a_1, then for every finite core
S ⊇ Q, every two elements of 𝒫'(S) intersect (in fact, every two S-extended
types intersect, whether or not their base types are disjoint) — in particular
(H1) holds automatically at every core in the absorption chain, including
whatever core the chain reaches (if it reaches one at all).

*Proof.* First, 2 | a_n for every n ≥ 1. This is exactly the certified
Uniform Evenness Lemma from `even-a1-full-periodicity-theorem` (proved there by
strong induction: 2 | a_1 by hypothesis; if 2 | a_i for all i ≤ n then, as
recalled in §3, a_{n+1} = a_n + 2, which is even since a_n is). We reuse this
fact directly, citing that file rather than re-deriving it, since it is an
elementary, self-contained, and independently checked argument (see that
file's own proof and this round's outline-reviewer's independent 8-seed
numerical confirmation).

Since 2 | a_1, 2 ∈ Q = P(a_1). Fix any finite core S ⊇ Q; then 2 ∈ S. For every
n ≥ 1, 2 | a_n, so 2 ∈ P(a_n), and since 2 ∈ S, 2 ∈ P(a_n) ∩ S = ρ_S(n). Hence
2 ∈ ρ_S(n) for EVERY index n, whether or not n is large enough for ρ_S(n) to
have stabilized into an extended-persistent type. In particular, for every
A', B' ∈ 𝒫'(S) (each of which is, by definition, ρ_S(n) for infinitely many n,
hence for at least one specific n), 2 ∈ A' and 2 ∈ B', so 2 ∈ A' ∩ B', giving
A' ∩ B' ≠ ∅. This holds for every pair, disjoint-base-type or not, so in
particular it holds for every disjoint-base-type pair — exactly the content of
(H1) at level S. Since S was an arbitrary finite core ⊇ Q, this holds at every
core in the absorption chain (S_0, S_1, S_2, ..., and at whatever S* the chain
might reach). ∎

This is a genuine, cheap, fully proved unconditional result: **whenever 2 | a_1,
hypothesis (H1) is automatically true**, at every stage of the chain, with no
further work. It is worth recording as a standing simplification for any
future round that revisits H1 restricted to even seeds (though, per §3, this
sub-case is already fully and more strongly solved without needing H1 at all).

#### §4.2. H2 does NOT trivialize the same way — genuine negative finding, honestly
reported (not resolved, not silently folded into a claim of resolution)

The natural hope, per the dispatch's suggested stretch, is that the SAME
shared-prime-2 mechanism that trivializes H1 might also force the absorption
chain to terminate in 0 rounds (i.e. force S₀ itself to be self-absorbing,
S₀⁺ = S₀), whenever 2 | a_1. On inspection, **this does not hold**, and no
argument achieving it was found — the mechanism behind §4.1 is structurally
too weak for H2, for a precise reason:

**The obstruction.** Self-absorption of a core S requires, by the definition in
`self-absorbing-core-theorem.md`, that P(a_j) ⊆ S for EVERY j = 1,...,N(S) —
i.e. the ENTIRE prime factorization of each early term a_j lies inside S, not
merely that a_j and S share the single common prime 2. The §4.1 argument only
ever uses the single fact "2 ∈ P(a_j) ∩ S" for each j; it says nothing about
whether the OTHER prime factors of a_j (if a_j has any prime factors besides
2, which a generic even a_j will) also lie in S. Concretely: fix any j ≤ N(S₀)
with a_j having an odd prime factor q ∉ S₀ (such j exist for generic even a_1 —
e.g. even for the simplest even seeds, the terms a_2, a_3, ... quickly acquire
odd prime factors beyond the finite witness-generated set S₀, since S₀ is
built from canonical witnesses for the persistent TYPES, a much smaller,
type-level object than "every prime factor of every one of the first N(S₀)
terms"). For such j, P(a_j) ⊄ S₀, so S₀ is NOT self-absorbing, regardless of
2 | a_1. Hence 2 | a_1 alone supplies no general mechanism forcing the chain to
terminate at S₀ (or at any specific, a priori bounded S_k) — the obstruction
that defeats H2 in general (an early term's factorization potentially escaping
any fixed finite core) is not touched by the single shared prime 2, since
self-absorption is a statement about the FULL factor set of each early term,
not about any one shared prime.

**What this means, honestly.** This stretch attempt is a genuine, if small,
negative finding, not a failure to try: it shows the specific "does 2 ∈ Q make
H2 vacuous the same way it makes H1 vacuous" hope, suggested as a cheap
possible win by the dispatch, is FALSE as a general mechanism — matching the
dispatch's own instruction ("if it requires new machinery, do not attempt it —
just note it as a flagged idea for a future round, honestly undeveloped"). We
go slightly further than "undeveloped": we have identified the PRECISE reason
it fails (self-absorption needs full-factorization containment, a
qualitatively stronger condition than FAH's single-shared-prime intersection
requirement), so a future round need not re-attempt this exact idea without a
genuinely new ingredient forcing full containment of early factorizations
into a bounded core — no such ingredient is proposed or claimed here. **H2
remains entirely open, for every a_1 including even ones**, except insofar as
the entirely separate, non-framework argument of §3 bypasses the need for H2
altogether when 2 | a_1.

### §5. Summary of this round's net effect on the workspace

- The full conditional dependency chain for the general problem is now
  assembled in one place (§0-§2), citing every certified ingredient by name,
  with the two remaining open hypotheses (H1, H2) stated with their exact
  mathematical content and cross-referenced to their equivalent formulations
  and attempt histories elsewhere in the workspace. No new mathematical content
  beyond citation and assembly is claimed for §0-§3.
- One new, small, fully proved unconditional corollary is added: **(H1) is
  vacuously true whenever 2 | a_1**, at every core in the absorption chain
  (§4.1) — genuine positive content, though subsumed in practical effect by
  §3's stronger, self-contained result for the same sub-family.
- One new, small, fully proved negative finding is added: **the analogous
  "2 | a_1 trivializes H2" hope is FALSE**, with the precise structural reason
  identified (§4.2) — honestly reported as a dead end for this specific idea,
  not overclaimed as progress on H2 itself, and not resolving H2 for any a_1.
- H1 (FAH) itself is untouched this round, as instructed — no 18th mechanism
  was attempted here (the round's dedicated H2 attempt is in the sibling
  approach `core-growth-monotonicity`, not in this file).
- The workspace's overall Status remains `partial`: the problem's claim is now
  fully solved for the 2 | a_1 subfamily (via the sibling approach), and fully
  reduced — via a complete, independently-certified chain of lemmas with no
  remaining gap in the reduction itself — to exactly two named, precisely
  stated, still-open hypotheses (H1, H2) for the general case.

### §6. Round 18: two permanent negative findings (documentation only — no new
progress toward H1/H2, and no change to the Master Conditional Theorem chain
of §0–§2, which was independently re-audited and confirmed gap-free again this
round)

This round's dispatch asks that two negative findings from the round-18
audit-insurance explorer, independently checked by the round-18 outline
reviewer, be recorded permanently in this file so that future rounds do not
re-attempt either route as a shortcut for H1. Both were independently
re-verified from scratch by this builder as well (fresh Python simulations,
scripts at `/tmp/round-18/verify_odd2.py` and `/tmp/round-18/verify_q2.py`; see
computations below). Neither finding touches the certified Master Conditional
Theorem or its two open hypotheses H1/H2 — Status stays `partial`.

#### §6.1. Odd-Prime Non-Trivialization Proposition: the `p | a_1` trick that
trivializes H1 for `p = 2` (§4.1 above) does NOT generalize to odd `p`

**Recall why `p = 2` works (§4.1).** If `2 | a_1`, the certified Uniform
Evenness Lemma (from `even-a1-full-periodicity-theorem.md`) gives `2 | a_n`
for *every* `n ≥ 1`, so `2` lies in every extended type at every core, making
every two extended types intersect trivially. The proof of Uniform Evenness
itself rests on a fact special to `p = 2`: between the "definitely illegal by
consecutive-integer coprimality" candidate `a_n + 1` and the "next multiple of
`p`" candidate `a_n + p`, there are exactly `p − 2` intermediate candidates
`a_n + 2, ..., a_n + (p−1)` that must ALSO be ruled out before the induction
can conclude `a_n + p` is the forced legal successor. For `p = 2` this count is
`p − 2 = 0`: there are no intermediate candidates at all, so `a_n + 1` illegal
`⟹` `a_n + 2` is immediately the successor, and the induction "every term is
divisible by 2" closes with no extra work. For odd `p ≥ 3`, `p − 2 ≥ 1`, and
each intermediate candidate `a_n + j` (`2 ≤ j ≤ p−1`) is *not* automatically
divisible by `p` (since `p ∤ (a_n+j)` whenever `p | a_n` and `0 < j < p`), so
ruling it out as a successor requires it to fail against some OTHER prime
factor of `a_1` — which is unavailable, or at least not forced, when `a_1` has
more than one distinct prime factor. This is a structural asymmetry between
`p = 2` and odd `p`, not merely an empirical difference; §6.1 below exhibits a
concrete pair of seeds where it genuinely breaks the trivialization.

**Proposition (Odd-Prime Non-Trivialization).** There exist positive integers
`a_1` with an odd prime `p | a_1` such that `p` does NOT divide `a_n` for
every `n` — i.e. the analogue of the Uniform Evenness Lemma is FALSE for
`p = 3`, `a_1 = 15` (and, with an identical sequence of base types, for
`a_1 = 45`). Consequently the analogue of the Vacuous-FAH-under-`2|a_1`
Corollary (§4.1) also fails for these seeds: `Q = {3,5}` splits into two
disjoint, both-infinitely-occurring base types `{3}` and `{5}`, so `p = 3`
alone does not force every two base types to intersect, and FAH must still be
established by other means (i.e. these seeds remain squarely in the general,
unresolved H1 regime — they do not trivialize).

*Proof (direct computation, independently re-derived and re-verified in this
round).* Let `a_1 = 15 = 3·5`, so `Q = P(a_1) = {3,5}`. Generating the greedy
sequence `(a_n)` (each `a_{n+1}` is the least positive integer not among
`a_1,\dots,a_n` with `gcd(a_{n+1},a_i) > 1` for every `i ≤ n`) gives, for the
first 24 terms,

  `15, 18, 20, 24, 30, 36, 40, 42, 45, 48, 50, 54, 60, 66, 70, 72, 75, 78, 80,
  84, 90, 96, 100, 102, ...`

with base types `τ(n) := P(a_n) ∩ Q` given exactly, for `n = 1,\dots,24`, by

  `{3,5}, {3}, {5}, {3}, {3,5}, {3}, {5}, {3}, {3,5}, {3}, {5}, {3}, {3,5},
  {3}, {5}, {3}, {3,5}, {3}, {5}, {3}, {3,5}, {3}, {5}, {3}`,

a strict period-4 pattern from `n = 1` onward: `τ(n) = {3,5}` when `n ≡ 1 (mod
4)`, `τ(n) = \{3\}` when `n ≡ 2` or `0 (mod 4)`, and `τ(n) = \{5\}` when `n ≡ 3
(mod 4)` — i.e. `3 ∤ a_n` exactly at the "fail-indices" `n = 3, 7, 11, 15,
\dots ≡ 3 \pmod 4`. This pattern was confirmed to persist exactly (no drift,
no eventual change) over the first 3000 terms in an independent re-simulation
(`/tmp/round-18/verify_odd2.py`): across 3000 terms, `3 | a_n` for exactly
`2250` of them (`75\%`, matching `3` out of every `4`) and `5 | a_n` for
exactly `1500` of them (`50\%`); the base type `\{5\}` (the "`3` fails" type)
occurs at indices `3,7,11,15,\dots,3+4k,\dots` — an exact, unbroken arithmetic
progression of common difference `4` — and the base type `\{3\}` occurs at all
other indices. Substituting `a_1 = 45 = 3^2 \cdot 5` (same `Q = \{3,5\}`)
reproduces the identical base-type sequence and the identical `75\%/50\%`
divisibility statistics (only the raw term values differ, e.g. `45, 48, 50,
54, 60, \dots`; the *type* pattern is unchanged), confirming the phenomenon is
not an artifact of one specific seed value but of the pair `Q = \{3,5\}`
itself. `\blacksquare`

**Why this matters (structural explanation, not just numerics).** At the
fail-indices `n ≡ 3 \pmod 4`, `a_n` is of base type `\{5\}` — divisible by `5`
but not by `3` — while at `n ≡ 2, 0 \pmod 4` it is of base type `\{3\}` —
divisible by `3` but not `5`. These are two disjoint (as subsets of `Q`),
each-infinitely-occurring base types, exactly the configuration the
Persistent-Type Pigeonhole (`persistent-type-pigeonhole.md`) certifies must
exist for a "rogue" pair whenever `|Q| ≥ 2` and no single prime of `Q` divides
literally every term. `p = 3 | a_1` here does NOT prevent this: unlike the
`p = 2` case, where "next candidate after the immediately-illegal one" IS the
next multiple of `2` (so `2` is forced onto every term), for `p = 3` the very
next candidate after `a_n+1` is `a_n+2`, which is checked against `a_1` only
via `gcd(a_n+2, a_1)`; since `3 ∤ (a_n+2)` (as `3 | a_n`) and `a_1 = 15` also
has `5` as a factor, `a_n + 2` can be legal by being divisible by `5` (or by
sharing some other prime with the earlier terms) instead of `3` — precisely
the `p − 2 = 1` intermediate-candidate slot identified above, realized
concretely. This confirms: **the `2 | a_1` trivialization of H1 (§4.1) is a
genuine special property of the prime `2`, not an instance of a general
"any `p | a_1` trivializes H1" phenomenon** — no such general phenomenon
holds, and no future round should assume it does for a seed with `|Q| ≥ 2`
merely because one prime of `Q` divides `a_1`. (This does not contradict
`prime-power-seed-periodicity-theorem`'s theorem for `a_1 = p^k`, `|Q| = 1`:
that theorem's induction rules out each intermediate candidate `a_n+j`,
`2 ≤ j ≤ p-1`, precisely BECAUSE `a_1` has no second prime factor for it to
use — `\gcd(a_n+j,a_1)=1` outright, by Free Facts illegal. The `a_1=15,45`
counterexample is exactly the `|Q| ≥ 2` regime that theorem explicitly
excludes from its scope.)

#### §6.2. `|Q| = 2` is confirmed NOT a tractable general subfamily for H1

**Finding.** Unlike `|Q| = 1` (fully resolved unconditionally by
`prime-power-seed-periodicity-theorem.md`) and the unconditional `2 | a_1`
subfamily (`even-a1-full-periodicity-theorem.md`), the two-distinct-prime
family `a_1 = p^i q^j` (`p, q` odd distinct primes, `|Q| = 2`) admits NO
uniform simplification of H1/FAH: the round-18 audit-insurance explorer's
36-seed sweep across this family found the time-to-resolution and qualitative
behavior highly seed-dependent, with no formula in `p, q` predicting it, and
— tellingly — the sweep's hardest instances are EXACTLY the four seeds
(`187 = 11·17`, `209 = 11·19`, `221 = 13·17`, `247 = 13·19`) that this
workspace has used as its own canonical standing hard test cases since round
6 (see `Approaches tried` history above, e.g. round 8's Singleton-Side FAH
discussion and round 9's Recruitment-Budget Lemma refutation, both run on
these same four seeds). This builder independently re-confirmed the
qualitative claim on these four seeds this round
(`/tmp/round-18/verify_q2.py`, 1500-term simulation each): the two disjoint
singleton base types occur with seed-dependent, non-uniform frequency ratios —
`187`: `\{11\}` at `\approx 79\%`, `\{17\}` at `\approx 20\%`; `209`:
`\{11\}` at `\approx 81\%`, `\{19\}` at `\approx 18\%`; `221`: `\{17\}` at
`\approx 62\%`, `\{13\}` at `\approx 36\%`; `247`: `\{13\}` at `\approx 58\%`,
`\{19\}` at `\approx 37\%` — with no evident closed-form relationship between
the ratio and `(p,q)` (contrast with the `a_1=15,45` case in §6.1, where the
ratio is a clean, provable `75\%/25\%` forced by the `p=3` structural
argument; here, both primes of `Q` are "generic" odd primes with no
`p = 2`-style asymmetry, so no analogous closed form is expected or found).

**What this means for future work.** `|Q| = 2` should NOT be treated as an
"easy tractable subfamily" the way `|Q| = 1` and `2 | a_1` are — it is, in
effect, already the general hard case, since the workspace's own long-standing
canonical hard test seeds already live inside it. Any future round proposing
to attack H1 "first for `|Q| = 2`, as a warm-up before the general case"
should be redirected: that warm-up is not simpler than the general problem and
should not be separately dispatched as if it were. This finding is negative
and permanent — it records a checked, closed-off shortcut, not new proof
content toward H1 itself; H1 remains completely open in general, exactly as
in §1.

#### §6.3. Effect on Status

Both §6.1 and §6.2 are documentation/negative findings only. They add no new
lemma toward H1 or H2, and do not touch the Master Conditional Theorem's
chain in §0–§2 (re-audited gap-free again this round, unchanged). Status
remains `partial`, with H1 and H2 both open exactly as stated in §1. The value
of this round's addition is purely in permanently narrowing what future
rounds should NOT re-attempt: (a) generalizing the `2 | a_1` H1-trivialization
trick to arbitrary `p | a_1` — false, concrete counterexample on record
(§6.1); (b) treating `|Q| = 2` as an easy warm-up subfamily for H1 — false,
already the hard regime by the workspace's own standing test seeds (§6.2).

### §7. REVISED (round 20): the Ambient-Statistic Obstruction — a correctly-
scoped, non-circular replacement for round 19's Generalized Class-Blindness
Obstruction

**Why round 19's version is withdrawn, precisely.** Round 19's §7.2 "proof"
constructed two scenarios (Scenario I: `E` finite; Scenario II: `E` infinite)
and asserted (§7.2, the parenthetical after the scenario definitions) that
"both scenarios are realizable as consistent extensions of the same finite
prefix... by definition of 'open,' both continuations are a priori
consistent with everything certified so far." This is exactly the circularity
the round-19 proof-reviewer caught (see `current.md`'s round-19 history) and
that this round's fresh-framing explorer independently re-derived as a
GENERAL screening rule (its item 3, `/tmp/round-20/math-explorer-fresh-
framing.md`): the sequence `(a_n)` is **fully deterministic** once `a_1` is
fixed — there is exactly ONE legal continuation, not a free ensemble of
"a priori consistent" ones. Asserting that a second, divergent continuation
of the SAME actual, unique recursively-defined sequence exists (as opposed to
merely being not-yet-excluded by the SPECIFIC premises an argument is
entitled to cite) is not something "openness" of H1 grants for free; it
requires an explicit construction (e.g. two distinct seeds `a_1, a_1'`,
verified to share a long common core and then to provably diverge — exactly
the construction the certified CRT-glue/competitor-construction family
already attempted and found magnitude-infeasible). No such construction was
supplied in round 19, and none is supplied here either. **Round 19's §7 is
therefore permanently withdrawn as stated; it is not certified and should not
be cited.**

This section instead certifies a **strictly narrower, but fully rigorous and
non-circular**, replacement — following the dispatch's option (a): restrict
scope to statistics that are structurally incapable of referencing realized
sequence data, matching the TRUE scope of the two lemmas already certified in
this family (`escape-cost-vacuity.md`, round 10; `density-argument-vacuity-
corollary.md`, round 11). The fix that makes the new proof non-circular is
explained in §7.2 below: it replaces "both scenarios are realizable as actual
continuations of the one true sequence" (an unconstructed existence claim)
with the much weaker and directly verifiable claim "both scenarios are
logically consistent with the FINITE LIST OF PREMISES the argument is
permitted to cite" (a syntactic check on those premises' own definitions,
requiring no construction at all) — this is the same soundness-of-deduction
move already used, correctly, in `escape-cost-vacuity.md`'s certified proof
(which checks that its cited class-blind facts literally do not take `g_m,
g_n` as arguments — a definitional check, not an existence claim).

#### §7.0. What exactly must be ruled out

Recall the target of H1 (Cofinite FAH), precisely: for a rogue base-type pair
`(A',B')` with witnesses `n_A < n_B` and canonical shared prime `q*` supplied
by Free Facts / the certified Bounded/Generalized Bounded Witness machinery,
the open content is whether

  `E := {n > n_B : ρ(n) = A', q* ∤ a_n}` (and the symmetric set for `B'`)

is **finite** — i.e. whether the ALREADY-KNOWN single witness `q*` (obtained
existentially, via pigeonhole, for infinitely many occurrences) can be
promoted to a **universal** witness (for cofinitely many occurrences). Every
mechanism in the "statistical method" family attempts this promotion by
computing some numerical statistic `Φ` over a window of the sequence's
behavior and arguing `Φ` forces `E` to be finite.

#### §7.1. Definition: ambient statistic (the corrected, narrower replacement
for round 19's "window-computable statistic")

Fix `a_1` (hence `Q`, `S₀`), a rogue pair `(A',B')` with its certified finite
data (witnesses `n_A, n_B`; canonical prime `q*`; the Confined-GCD Lemma's
fixed alphabet `F'', D_bad`, all already finite and fixed once the rogue pair
is fixed, per `confined-gcd-lemma.md`). For a real/integer window bound
`X > a_{n_B}`, call a quantity `Φ = Φ(X)` an **ambient statistic** if `Φ(X)`
is computed by a single fixed, explicit formula/algorithm whose ONLY inputs
are `X` and the fixed finite data `(a_1, Q, S_0, n_A, n_B, q^*, F'', D_bad)`
— and whose computation, AS A FORMULA, never mentions, queries, or takes as
an argument: (i) which integers in any range are actual terms `a_n` of the
sequence for `n>n_B`; (ii) the actual value `a_n` for any `n>n_B`; or (iii)
the actual base type `\rho(n)` for any `n>n_B`. Equivalently: `Φ(X)` is
computable by ordinary elementary/analytic number theory (Mertens products,
sieve counts, congruence-class counts over ALL integers in `(a_{n_B},X]`,
etc.) **without ever running the greedy recursion past index `n_B`.**

This is a deliberately NARROWER definition than round 19's "window-computable
statistic," which allowed `Φ(N)` to be built from the array `W(N)` — and
`W(N)`, as round 19 itself defined it, explicitly included "the
realized-occurrence Boolean array `(1[\rho(n)=A'])_{n_B<n\le N}`," i.e.
realized data, in direct violation of items (i)/(iii) above. That inclusion
is exactly the reason round 19's four "verification" bullets (§7.1 of the
prior version) do not actually establish what an ambient-only version needs:
every one of the four named sub-families — density RATIO (which divides by
`|\{n\le N:\rho(n)=A'\}|`, a realized occurrence count), second moment over
PAIRS OF `A'`-OCCURRENCES, Borel–Cantelli over `1[\rho(n)=A']`, and
Fourier/LP built from `\mu(r):=|\{n\le N:\rho(n)=A', a_n\equiv r\}|` — is, AS
ACTUALLY USED to say anything FAH-relevant, built from realized occupancy
data (which indices are `A'`-occurrences, and what their values are), not
from ambient data alone. **This is stated as an honest scope limitation, not
papered over: see §7.4 below for the precise, non-overclaimed consequence.**

Two genuinely ambient examples DO exist and are already certified: (a) a
class-blind fact about a fixed PAIR of indices `(m,n)` that only uses `m,n`
and `a_1`-derived constants, never `g_m,g_n` (`escape-cost-vacuity.md`); (b)
a Mertens/sieve-type count `C(X)` of how many integers in `(a_{n_B},X]`
satisfy a fixed congruence/coprimality condition defined by primes of `S_0
\cup F''` — computed over ALL integers in the window, NOT conditioned on
which of them happen to be realized sequence terms
(`density-argument-vacuity-corollary.md`). Both are literal special cases of
the §7.1 definition above.

#### §7.2. Theorem (Ambient-Statistic Obstruction)

*No finite deductive argument `\mathcal D`, all of whose premises are (a)
finitely many values `\Phi_1(X_1),\dots,\Phi_k(X_k)` of ambient statistics (as
defined in §7.1), possibly followed by a single limiting step `X_j\to\infty`,
together with (b) other already-certified facts that are themselves ambient
in the same sense (Free Facts' STATIC pairwise-legality requirement, the
Bounded/Generalized Bounded Gap Lemma, the Sandwich Genericity Theorem, and
the Confined-GCD Lemma's STATIC definitions of `F'', D_bad` — none of which,
on inspection of their own certified statements, take `\rho(n)` or `a_n` for
`n>n_B` as an argument) — can establish that `E := \{n>n_B : \rho(n)=A',\
q^*\nmid a_n\}` is finite (nor that it is infinite; nor any other conclusion
whose statement quantifies over the realized values/occurrences `a_n,
\rho(n)` for `n` beyond `\max(X_1,\dots,X_k,n_B)`).*

**Proof.** Suppose such `\mathcal D` exists. Since `\mathcal D` is by
hypothesis a FINITE sequence of deductive/computational steps applied to the
finitely many numerical inputs `\Phi_1(X_1),\dots,\Phi_k(X_k)` (and the fixed
finite data), compose these steps into a single explicit function
`\Psi(X_1,\dots,X_k) := \mathcal D(\Phi_1(X_1),\dots,\Phi_k(X_k))` — this is
a purely mechanical, syntactic operation (finite composition of finitely many
explicit formulas is again an explicit formula), requiring no assumption
about what `\mathcal D` "means" or about alternate scenarios.

Because each `\Phi_j` is, by definition (§7.1), computable from `X_j` and the
fixed finite data alone — its DEFINING FORMULA literally contains no
reference to `a_n` or `\rho(n)` for `n>n_B` — the composed function `\Psi` is
likewise computable from `X_1,\dots,X_k` and the fixed finite data alone: a
finite composition of formulas none of which reference the realized data
beyond `n_B` is itself a formula that does not reference it. (This step is a
direct, purely mechanical consequence of function composition and requires
NO existence claim about alternate continuations of the sequence — it is a
syntactic fact about `\Psi`'s formula, checkable by inspection, exactly as
`escape-cost-vacuity.md`'s proof checks that its cited facts do not take
`g_m,g_n` as arguments.)

Now, to see that `\Psi`, so constructed, cannot correctly output "`E` is
finite" as a THEOREM (i.e. as a conclusion validly derived from the cited
premises), apply the standard soundness criterion for deductive validity: a
deduction from premises `P` to conclusion `C` is valid only if every
model/assignment of the relevant data satisfying `P` also satisfies `C`.
Consider the (purely formal, hypothetical — NOT asserted to be an actual
alternate continuation of the true, unique, deterministic sequence)
assignment `\sigma`: for indices `n>\max(X_1,\dots,X_k,n_B)`, declare `\rho(n)
:= A'` and `q^*\nmid a_n` for infinitely many such `n` (so that, under
`\sigma`, `E` is infinite), while for `n\le\max(X_1,\dots,X_k,n_B)`, `\sigma`
agrees with the true realized values. Check directly, one by one, that each
of `\mathcal D`'s cited premises is SATISFIED by `\sigma`:

- Each `\Phi_j(X_j)`, `X_j\le\max(X_1,\dots,X_k)`: satisfied, since
  `\Phi_j(X_j)`'s value, by §7.1, depends only on `X_j` and the fixed data —
  it takes the SAME value under `\sigma` as under the true realized sequence,
  because its defining formula never queries `\rho(n), a_n` for `n>n_B` at
  all (in particular it never queries the indices where `\sigma` was just
  redefined, all of which lie beyond `\max(X_1,\dots,X_k)`).
- Free Facts' static requirement, the Bounded/Generalized Bounded Gap Lemma,
  the Sandwich Genericity Theorem, and Confined-GCD's static definitions:
  each, by inspection of its own certified statement (as already verified,
  fact-by-fact, in `escape-cost-vacuity.md`'s certified proof, reused here by
  citation rather than re-derived), is a class-blind/ambient statement that
  likewise does not constrain `\rho(n)` or `q^*`-divisibility of `a_n` for
  `n>n_B` — hence places no constraint that `\sigma` could violate.

So `\sigma` satisfies every one of `\mathcal D`'s cited premises, yet
`\sigma` makes `E` infinite, i.e. makes the conclusion "`E` is finite" FALSE.
Hence `\mathcal D`'s premises do not entail "`E` is finite," so `\mathcal D`
is not a valid deduction of it. (Symmetrically, an assignment `\sigma'`
agreeing with the true sequence through `\max(X_1,\dots,X_k,n_B)` and making
`E` finite beyond it likewise satisfies every premise, so `\mathcal D` also
cannot validly deduce "`E` is infinite.") If `\mathcal D` includes a limiting
step `X_j\to\infty`, the identical argument applies to every finite-stage
truncation `\mathcal D_M` (premises restricted to `X_j\le M`): for every `M`,
an assignment `\sigma_M` agreeing with the true sequence through
`\max(M,n_B)` and diverging in either direction after it satisfies every
premise of `\mathcal D_M`, so no finite stage — and hence no limit of finite
stages — pins down `E`'s finiteness from ambient data alone. `∎`

**What makes this non-circular, precisely.** Unlike round 19's withdrawn
version, this proof does NOT assert that `\sigma` (or the symmetric
`\sigma'`) is an actual, legally-realizable continuation of the true,
uniquely-determined sequence — it only checks, one premise at a time by
direct inspection of each premise's own certified defining statement, that
`\sigma` violates none of the FINITELY MANY premises `\mathcal D` is actually
entitled to cite. This is the standard, textbook notion of semantic
entailment failure (exhibiting a model of the premises that falsifies the
conclusion) and requires no construction of two genuinely-realizable
completions of the recursion — only the much weaker and directly-checkable
fact that the cited ambient premises' own formulas do not encode the
relevant realized data at all.

#### §7.3. What this restricted lemma actually covers, and does NOT cover
(honest, precise scope — no overclaim)

**Covers (genuinely, non-circularly, certified here).** Any argument for H1
built ENTIRELY from ambient statistics in the strict §7.1 sense — i.e. from
quantities computable without ever consulting which integers are realized
sequence terms or their values/base-types beyond the fixed finite witness
data. This is exactly the scope already occupied by the two lemmas this
section generalizes: `escape-cost-vacuity.md` (pairwise class-blind facts)
and `density-argument-vacuity-corollary.md` (window-class-blind, i.e. pure
Mertens/sieve density of ALL integers in a range, not conditioned on
occupancy). §7.2 subsumes both as special cases of one proof technique,
proved once rather than twice, and additionally covers any AMBIENT
second-moment or AMBIENT Fourier/character-sum computation phrased purely in
terms of static arithmetic properties of integers in a window (e.g. "how many
integers in `(a_{n_B},X]` are `\equiv r \pmod L`" — a fact about integers,
computable with no reference to the sequence at all beyond `L,S_0`).

**Does NOT cover (an honest walk-back from round 19's overclaim, precisely
diagnosed).** Every USEFUL, FAH-relevant instance of the four named
statistical-method sub-families — density RATIOS conditioned on realized
`A'`-occurrences, second moment over pairs of realized occurrences,
Borel–Cantelli criteria over the realized indicator `1[\rho(n)=A']`,
finite-Fourier/character-sum coefficients or LP-relaxations built from the
realized occupation-count vector `\mu(r)` — is, BY CONSTRUCTION, NOT an
ambient statistic in the §7.1 sense (each explicitly queries realized
occupancy or realized values, in violation of items (i)–(iii) of §7.1's
definition), and so **§7.2 does NOT rule these out.** This matches exactly
what the round-19 proof-reviewer's restricted-scope note anticipated and what
this round's dispatch instructed be stated honestly: the certified content
of this section is a correct, non-circular UNIFICATION of the two
already-certified ambient lemmas (no genuinely new certified ground beyond
their existing scope), not an extension to the occupancy-referencing forms
of second moment / Borel–Cantelli / finite-Fourier / LP-relaxation that would
actually be needed to say anything new about H1. **Those four sub-families,
in their practically useful (occupancy-referencing) forms, remain formally
UNREFUTED by any certified lemma in this workspace** — ruling them out (if
possible at all) would require either (i) an explicit two-seed (or
equivalent) construction of the kind flagged as the standing requirement by
this round's fresh-framing explorer, or (ii) a case-by-case direct refutation
of each occupancy-referencing instance, neither of which is supplied here.

§7.2 also, like round 19's version, does not touch (and does not claim to
touch) arguments that reference the REALIZED, actual specific-prime
factorization data of the sequence's own terms directly — e.g. the Confined-
GCD Lemma's own fixed-alphabet observation, the Two-Sided Singleton Witness
Theorem's route, or `triangle-consistency-pigeonhole`'s anatomy-of-integers
attack — all of which are, by design, occupancy/value-referencing and hence
automatically outside this lemma's scope on both the withdrawn and the
corrected version.

#### §7.4. Net effect on the workspace (honest summary)

Round 19's Generalized Class-Blindness Obstruction is withdrawn as overclaimed
and circular. In its place, this round certifies the **Ambient-Statistic
Obstruction** (§7.2): a correct, non-circular unification of the two
already-certified pairwise/window ambient lemmas into one proof, with an
honest, explicit scope note (§7.3) that it does NOT extend certified coverage
to the occupancy-referencing forms of second moment, Borel–Cantelli,
finite-Fourier/character-sum, or LP-relaxation methods — those remain open
(un-ruled-out, but also with no known successful instance) as potential FAH
mechanisms, exactly where they stood before round 19's now-withdrawn claim to
have closed them. **No future round should cite round 19's version, and no
future round should treat the occupancy-referencing statistical-method family
as pre-emptively dead** — only its PURELY AMBIENT special cases are.

### §8. NEW (round 19): tightened audit of the run's two guaranteed
unconditional deliverables

This section restates, in one self-contained place, the exact scope of what
this workspace has established UNCONDITIONALLY — independent of H1, H2, and
every FAH mechanism attempt — as the run's floor deliverable, per this
round's dispatch. No new mathematical content is introduced here beyond
citation and precise scoping; the proofs themselves are certified in full in
the two cited lemma files and are not reproduced.

**Theorem A (`2 | a_1` case, `even-seed-literal-periodicity-theorem.md`,
certified round 16).** If `2 | a_1`, then `a_n = a_1 + 2(n-1)` for every
`n ≥ 1`. In particular `T := 1`, `L := 2` witness the problem's conclusion
literally from `n = 1`. *Proof mechanism (self-contained, no FAH/persistent-
type machinery): strong induction; `a_n+1` is always illegal by
consecutive-integer coprimality (`\gcd(a_n+1,a_n)=1`); `a_n+2` is always
legal because every one of `a_1,\dots,a_n` is even by the inductive
hypothesis, so `2 \mid \gcd(a_n+2,a_i)` for every `i \le n`; minimality of
the greedy definition forces `a_{n+1}=a_n+2` exactly, propagating evenness.*

**Theorem B (`a_1 = p^k` case, `prime-power-seed-literal-periodicity-theorem.md`,
certified round 18).** If `a_1 = p^k` for a prime `p` and integer `k \ge 1`,
then `a_n = a_1 + p(n-1)` for every `n \ge 1`. In particular `T := 1`,
`L := p` witness the problem's conclusion literally from `n = 1`. *Proof
mechanism (self-contained, no FAH/persistent-type machinery): strong
induction; for `1 \le j \le p-1`, `a_n+j` is illegal against index `1` because
`P(a_1)=\{p\}` is a singleton and `p \nmid (a_n+j)` (as `p \mid a_n`, `0 < j <
p`), so `\gcd(a_n+j,a_1)=1`; `a_n+p` is legal because `p` divides every one
of `a_1,\dots,a_n` by the inductive hypothesis and `p \mid (a_n+p)`;
minimality forces `a_{n+1}=a_n+p` exactly, propagating `p \mid a_{n+1}`.*

**Exact overlap.** Theorem A applies iff `2 \in Q`; Theorem B (for the
specific prime `p=2`) applies iff `Q = \{2\}`, a strictly narrower condition.
The two theorems' domains of applicability therefore overlap EXACTLY on
`a_1 = 2^k` (`k \ge 1`) — where both give the identical conclusion `T=1,
L=2` — and are otherwise disjoint in content: Theorem A additionally covers
every even `a_1` with `|Q| \ge 2` (e.g. `a_1=6,30,210,1994,\dots`), while
Theorem B additionally covers every odd-prime-power `a_1=p^k` (e.g.
`a_1=9,25,27,49,121,\dots`).

**What this does NOT cover (stated explicitly, no overclaim).** Every other
`a_1` — i.e. every odd `a_1` that is not a prime power (equivalently, every
`a_1` with `|Q| \ge 2` and `2 \notin Q`, e.g. the workspace's own four
canonical hard test seeds `187=11\cdot17`, `209=11\cdot19`, `221=13\cdot17`,
`247=13\cdot19`, and the `a_1=15,45` (`Q=\{3,5\}`) counterexample seeds of
§6.1 above) is **untouched** by Theorem A or B, and remains entirely
conditional on the Master Conditional Theorem (§2), i.e. on both H1 and H2,
neither of which is established for these seeds. This is not a gap in
Theorem A/B themselves (both are complete, unconditional, and independently
re-verified with no gap, per the certification notes in their respective
lemma files) — it is a statement about the SIZE of the subfamily they cover
relative to the general problem, made explicit here so no future round or
final write-up mistakes "two fully solved subfamilies" for "the general
problem is solved."

**Combined statement of the run's guaranteed floor deliverable.** The
problem's claim (existence of `T, L` with `a_{n+T}=a_n+L` for every `n \ge
1`) is proved, completely and unconditionally, for every `a_1` in the
(infinite) union of two subfamilies — `\{a_1 : 2 \mid a_1\}` and
`\{a_1 : a_1 = p^k,\ p \text{ prime},\ k \ge 1\}` — with `T=1` in both cases
and `L` equal to `2` or to `p` respectively. This is the run's smallest
honest claim to `solved` status (each subfamily individually, not the
general problem) and is recorded here as the explicit floor the run retains
regardless of whether H1/H2 are ever resolved.

### §9. Honest final status paragraph (updated round 20)

H1 (FAH/Symmetric FAH/Cofinite FAH/EEA at the terminal self-absorbing core)
and H2 (absorption-chain termination) both remain entirely open. The FAH
mechanism search is now confirmed exhausted (in the precise, non-overclaimed
sense of §7.3-§7.4) across: existential/pigeonhole competitor-construction;
magnitude-sandwich; CRT-glue/competitor-modulus; the PURELY AMBIENT special
cases of sieve/density (per §7's revised, correctly-scoped Ambient-Statistic
Obstruction — pairwise class-blind facts and pure Mertens/sieve window
density, NOT the occupancy-referencing forms of second moment,
Borel–Cantelli, finite-Fourier/character-sum, or LP-relaxation, which remain
formally un-ruled-out, per the honest walk-back in §7.3–§7.4 from round 19's
overclaimed and now-withdrawn "entire statistical-method family" claim);
automaton/graph-walk/Morse–Hedlund/subword-complexity (EEA, proven
equivalent-in-difficulty, not a bypass); algebraic-number-theory,
generating-function, o-minimality, computability/priority-argument, and
nonstandard-analysis/Baire-category reframings (checked across rounds 15-20
and found to collapse to already-certified content or to require a
structure — a free ensemble of possible sequence completions — that this
fully deterministic recursion structurally lacks, per this round's
fresh-framing explorer); extremal graph theory on the resolving-prime
conflict structure (subsumed by the already-certified Hub Singleton Batch
Lemma); and crux-corpus transplant (no genuinely analogous precedent found in
the pre-2026 corpus across repeated systematic searches, rounds 19-20). The
standing meta-rule this round's fresh-framing explorer sharpened — any future
gap-closing argument premised on "two scenarios/continuations consistent with
the same observed data" must supply an actual two-seed (or equivalent)
construction, never assert existence "by definition of open" — should be
applied as a mandatory pre-certification screening check to any future
attempt in this style, exactly as it caught round 19's §7 before this round's
correction. This round's live sibling approaches (`triangle-consistency-
pigeonhole` and `triangle-critical-dichotomy-witness`, both anatomy-of-
integers/values-based attacks explicitly outside the scope of §7's
obstruction per §7.3; and `core-growth-monotonicity`, a dedicated H2
existence attack, confirmed dead-ended as of round 19) are this run's routes
to H1 and H2 respectively — see their own approach files for current status.
This file's own contribution this round (round 20) is the withdrawal and
correction of §7, plus the §E executive-summary tightening; it does not
itself close H1 or H2, and the workspace-level Status correctly remains
`partial`.

## Full proof
Not present — Status is `partial`. The Master Conditional Theorem (§2) is a
complete, gap-free proof of the problem's claim CONDITIONAL on (H1) and (H2),
both precisely stated in §1 and both still open. The 2 | a_1 special case is
fully and unconditionally solved, but by the sibling approach
`even-a1-full-periodicity-theorem`, not by this file's own (general) target.
The `a_1 = p^k` special case is likewise fully and unconditionally solved,
by the sibling approach `prime-power-seed-periodicity-theorem`, not by this
file's own (general) target. §7's Ambient-Statistic Obstruction (round 20,
replacing the withdrawn round-19 Generalized Class-Blindness Obstruction)
and §8's floor-deliverable audit are fully proved, unconditional additions,
but neither resolves H1, H2, or the general problem — see §9 for the honest
final status.

## Promotable lemmas

- **WITHDRAWN (was round 19) — Generalized Class-Blindness Obstruction.** Not
  promotable; found circular by the round-19 reviewer and confirmed withdrawn
  this round (§7 above now documents the withdrawal explicitly). Do not
  certify; do not cite.
- **NEW this round (round 20) — Ambient-Statistic Obstruction** (§7.1-§7.2
  above, fully proved, non-circular). A correct, narrower generalization of
  the certified `escape-cost-vacuity.md` / `density-argument-vacuity-
  corollary.md` findings, unifying both into one proof for any "ambient
  statistic" (§7.1: a quantity computable from a window bound `X` and fixed
  finite `a_1`-derived data alone, with NO reference to realized occupancy or
  values of the sequence — strictly narrower than round 19's withdrawn
  "window-computable statistic," which improperly allowed realized-occupancy
  data). The proof (§7.2) replaces round 19's unconstructed "two realizable
  continuations" step with a directly-checkable "the assignment `\sigma`
  satisfies every one of `\mathcal D`'s finitely many CITED premises"
  soundness-of-deduction argument — non-circular, and independently
  verifiable premise-by-premise. Recommended for certification as a
  standalone reusable screening lemma alongside its two predecessors (it
  supersedes them as the single general statement, though does not enlarge
  their combined scope). **Certify together with its explicit, mandatory
  scope note (§7.3):** it does NOT rule out the occupancy-referencing
  (practically useful) forms of second moment, Borel–Cantelli,
  finite-Fourier/character-sum, or LP-relaxation — those remain open. Any
  certification of this lemma must carry that scope note, or it risks being
  miscited the same way round 19's version was.
- **NEW this round — Vacuous FAH under 2 | a_1 Corollary** (§4.1 above, fully
  proved, unconditional given 2 | a_1, citing the Uniform Evenness Lemma from
  `even-a1-full-periodicity-theorem`): if 2 | a_1, then every two elements of
  𝒫'(S) intersect, for every finite core S ⊇ Q, in particular (H1)/FAH holds
  vacuously at every stage of the absorption chain. Short, self-contained,
  reusable — ready for certification as a standing simplification lemma (low
  priority, since §3's stronger, independent result already fully covers this
  sub-family without needing it).
- **NEW this round — Master Conditional Theorem** (§2 above): the single
  cleanest statement of "H1 and H2 together imply the full problem," assembled
  from six already-certified lemmas with no new mathematical content beyond the
  assembly itself. Recommend recording this statement (not as a new certified
  lemma file, since it introduces no new proof content beyond citation, but) as
  the canonical top-level conditional statement for `current.md` to point to,
  so future rounds and the final write-up have one clear place stating exactly
  what remains open and why.
- The §4.2 negative finding is diagnostic, not portable machinery (matches the
  Lemma F / Lemma I precedent) — not proposed for certification as a standalone
  lemma file, but worth recording in `current.md`'s standing cautions so no
  future round re-attempts the identical "2 ∈ Q trivializes H2" idea without a
  genuinely new ingredient.
- **NEW this round — Odd-Prime Non-Trivialization Proposition** (§6.1 above,
  fully proved by explicit computation on `a_1=15,45`, independently
  re-verified from scratch by this builder with a fresh consecutive-integer
  legality check, not just re-trusted): `p | a_1` for odd `p` does NOT force
  the analogue of Uniform Evenness (`p | a_n` for all `n`), and consequently
  does NOT trivialize H1/FAH the way `2 | a_1` does — with a precise
  structural reason (the `p=2` mechanism relies on there being zero
  intermediate candidates between "definitely illegal" and "next multiple of
  p," true only when `p=2`). Diagnostic/negative, not portable machinery in
  the sense of a reusable positive tool — but worth certifying as a standing
  documented dead end (matching the Lemma F / Lemma I / Density-Argument-
  Vacuity precedent for "diagnostic, do-not-re-attempt" findings) so no future
  round re-tries generalizing §4.1 to arbitrary `p | a_1`.
- **NEW this round — `|Q|=2` Non-Tractability finding** (§6.2 above, backed by
  the explorer's 36-seed sweep plus this builder's independent 4-seed
  re-confirmation on the canonical hard seeds 187/209/221/247): `|Q|=2` is not
  a simplified warm-up subfamily for H1 — it already contains the workspace's
  own standing hardest test cases. Diagnostic/negative, recommended for
  recording in `current.md`'s standing cautions (not a standalone lemma file,
  since it asserts absence of a shortcut rather than a positive reusable
  fact), so no future round dispatches "attack `|Q|=2` first, as an easier
  case" under the mistaken belief that it is simpler than the general
  problem.

## Round 21 outline: optional light-touch move toward a submission-ready
terminal write-up (per this round's audit-insurance explorer's recommendation
— NOT mandatory this round if builder time is better spent on the a1-3q gap
or the new counterexample-hunt approach; the outline-reviewer should decide
whether to seat this slug in the round-21 build set at all)

This round's audit explorer (`/tmp/round-21/math-explorer-audit.md`) re-
confirmed the Master Conditional Theorem chain (§0–§2 above) is gap-free and
recommends the run treat this file's §E/§0–§9 as the terminal floor
deliverable if H1/H2 are not resolved by the run's end. If this slug is
selected for build this round, the task is NOT to attempt a 21st FAH
mechanism (still explicitly out of scope for this file, per the standing
instruction — H1 is attacked by the sibling approaches, and this round by
the new `fah-counterexample-hunt` approach), but purely editorial/structural:

1. Fold `even-a1-full-periodicity-theorem` (Theorem A) and
   `prime-power-seed-periodicity-theorem` (Theorem B) — already reproduced in
   full in §E above — plus, if `a1-3q-subfamily-theorem` reaches APPROVE this
   round or a future round, its theorem too, into one single "Theorem
   (unconditional floor)" statement covering the full disjoint union of
   solved subfamilies, so a reader sees the complete solved territory in one
   place rather than piecing together three files.
2. Verify (do not just re-assert) that §0–§2's Master Conditional Theorem
   chain and §7's Ambient-Statistic Obstruction remain mutually consistent
   and non-overlapping after any new round-21 findings on `a1-3q-subfamily-
   theorem` or `fah-counterexample-hunt` are recorded elsewhere in the
   workspace — i.e., re-run the "is §7 causally disconnected from §0–§2"
   audit check if anything in this file changes.
3. Do NOT shorten or remove any of the honest gap statements (H1, H2 both
   open in general) — a "submission-ready" write-up must remain exactly as
   honest about what is unresolved as the current version; tightening means
   better organization/cross-referencing, not overclaiming closure.

If the outline-reviewer does not seat this slug this round (e.g. because
build capacity is better spent on the two higher-value slugs above), this
outline remains valid for a later round — no urgency attaches to it beyond
the general goal of having a clean terminal deliverable ready whenever the
run concludes.
