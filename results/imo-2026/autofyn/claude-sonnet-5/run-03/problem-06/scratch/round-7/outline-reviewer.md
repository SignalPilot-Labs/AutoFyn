# Outline review — round 7 — imo-2026-06

## 1. renormalization-induction-on-seed — "p=3 Near-Total Lock Theorem"

**Verdict: CHANGES REQUESTED (not RETHINK — the core lemma is sound, but
the scope of the target claim as stated is FALSE and must be narrowed
before the builder invests further).**

- **Necessity Lemma is not circular.** Checked the logic directly: given
  the inductive hypothesis "3 | a_i for i=1..n", the claim "a_{n+1}≠a_n+3
  requires gcd(a_n+2,a_1)>1" follows from (a) a_n+2 ≡ 2 mod 3 so 3∤(a_n+2),
  (b) the certified Minimum Gap Lemma free-excludes a_n+1, (c) validity
  against index 1 is one of the simultaneously-required constraints
  (`pairwise-non-coprimality.md`). This is a genuine one-step deduction
  from an inductive hypothesis, not an assumption of the conclusion — it's
  sound.
- **Numerically re-verified the explorer's headline finding myself**
  (independent Python simulation, exact integer gcd, not the outline's own
  numbers): for `R(a1)={3,q}`, q prime, 5≤q<600, 5∤a1, tested 106 seeds —
  **zero failures**, matching "106/106 pass when q≠5" and consistent with
  the outline's "106/107 pass, sole exception a1=15 (q=5)" once q=5 is
  counted back in. The unique exception is confirmed real, not a
  transcription artifact.
- **CRITICAL FINDING (new, not caught by the outliner): the general
  "New Target" statement is FALSE for ≥3-prime seeds.** The outline itself
  flags "≥3-prime seeds with 3∈R(a1), 5∉R(a1)" as "untested by the
  explorer" and asks the builder to check e.g. `a1=3·7·11`. I ran this
  check (and others) directly:
  - `a1=21=3·7`, `a1=231=3·7·11`, `a1=273=3·7·13` — all lock at L=3
    forever (consistent with the theorem).
  - **`a1=429=3·11·13` — does NOT lock at L=3.** Simulated 60 terms:
    `429,432,435,438,440,444,450,...` — the gap sequence is
    `3,3,3,2,4,6,6,6,...`, i.e. the lock breaks at step 4→5 (438→440,
    recruiting a factor of 5 and evenness), even though `5 ∤ 429`. This is
    a genuine, hand-verifiable counterexample to the claim "for every
    a_1 with min R(a1)=3 and 5∤a1: a_n=a1+3(n-1) for n≥2" as literally
    stated in this round's revision.
  - **Required fix before/during build:** the builder MUST restrict the
    "New Target" to the two-prime case `R(a1)={3,q}` (where all available
    numeric evidence, including mine, supports it) and treat 3+-prime
    seeds with min R(a1)=3 as a *separate, currently-false-as-conjectured*
    case, not an "untested but presumably fine" one. Do not let step 3's
    proof attempt implicitly assume $R(a_1)=\{3\}\cup S$ with $|S|=1$; if
    the mechanism is meant to generalize to $|S|\ge2$, it must explain why
    `a1=429` breaks it (candidate: with 3 primes, TWO different escape
    races can compound, giving the "5"-like near-prime role to a
    *combination* of 11 and 13 acting together — this needs a genuinely
    new idea, not a corollary of the two-prime proof).
- The "q<2p" distinguishing-invariant candidate (step 3) and the
  exceptional-family characterization (step 4) both remain open exactly as
  the outline says; I did not find a proof either way for these, only
  confirmed step 4's own examples (a1=45, a1=75 both fail to lock at L=3
  and reproduce the same non-trivial multi-prime tail as a1=15 — consistent
  with the outline's caution not to assume it's "solved by hand").
- **Action for the builder:** (1) certify the Necessity Lemma as stated
  (sound); (2) restrict the "New Target" theorem statement to `R(a1)={3,q}`
  two-prime seeds only, citing the `a1=429` counterexample as the reason
  the broader ≥3-prime version is false-as-stated; (3) attempt step 3 for
  the two-prime case only; (4) treat ≥3-prime, 5∤a1, min-R=3 seeds as an
  explicitly flagged **new, distinct open sub-case** for a future round,
  not folded silently into "cases to cover: untested."

## 2. state-compactness-pigeonhole — Generalized Multiple-of-r Realization Lemma

**Verdict: APPROVE (build).**

- Correctly guards against the circularity trap flagged by both this
  round's explorer and round 6's Contamination Dichotomy write-up: the
  CRT-density step (step 2) is explicitly labeled "free/elementary" and
  the actual load-bearing claim is isolated in step 3 (the
  density-to-bounded-index bridge), explicitly marked OPEN and explicitly
  distinguished from "density among all integers."
- One subtlety worth flagging to the builder (not a flaw in the outline,
  a sharpening for the write-up): "clean multiples of r avoiding all
  primes in E" is a union of residue classes modulo a *fixed* modulus
  `M = r·∏_{s∈E}s`, hence automatically periodic with a maximum gap
  ≤ M between consecutive clean multiples — this is a stronger, purely
  structural fact than "positive density," and it's available for free
  (no probabilistic/averaging argument needed). The real open content is
  showing the greedy sequence's own advance-by-≤rad(a1) steps actually
  *lands on* one of these residue classes at a bounded index — landing
  "near" a clean multiple doesn't mean the greedy process outputs it as a
  term (it must additionally survive against every earlier, non-r,
  non-E-related term too, i.e. a fresh check against the full prefix, not
  just against E). The builder should make this exact distinction
  explicit rather than conflating "bounded gap between clean multiples"
  with "greedy realizes one."
- The mandated sanity check (a1=35409, witness index 95 for prime 23) is
  appropriately required as a live falsifier of any explicit bound
  produced — keep this gate.

## 3. active-set-stabilization — global counting/second-moment bound on |Nec|

**Verdict: APPROVE (build).**

- Confirmed this is a genuinely distinct mechanism from
  state-compactness-pigeonhole's per-prime CRT-density route: one
  localizes to a single recruited prime r and tries to realize it via a
  density-to-bounded-index bridge; this one aggregates over *all* pairs
  (i,j), i<j≤N, and tries to bound the total count of distinct
  singleton-intersection-witnessing primes as N→∞ — a structurally
  different counting object (per-prime existence vs. global cardinality).
  Not the same idea in different notation.
- Appropriately self-flags the exact trap that would make this
  vacuous: a bound f(N) that merely grows with N (e.g. O(log N) or
  O(√N)) does NOT establish |Nec|<∞ — only a genuine convergence/ceiling
  argument would. This is stated correctly and explicitly as the thing to
  avoid.
- Also correctly self-flags the risk of silently reproducing the already
  -refuted Redundancy Growth Lemma (ρ(n)≥2 per-index mechanism, round 5) —
  since the target here is a global cardinality bound, not a per-index
  statistic, this is a different claim, but the outline is right to
  require the builder verify this explicitly rather than assume it.
- No mechanism is yet supplied for f(N) (honestly labeled "untried,
  promise unclear"); nothing to fix pre-build, this is an honest open
  step.

## 4. covering-system-construction-exchange (new)

**Verdict: CHANGES REQUESTED, with a mandatory gate the outliner already
proposed — I'm making it binding rather than advisory.**

- The outliner's own cheap numeric check (a1=375 recruiting prime 19, no
  closed-form threshold in rad(a1)) is a real warning sign but does not by
  itself doom the approach — it correctly rules out only the *naive
  closed-form* sub-mechanism, not the adaptive/exchange framing per se.
- **However, this approach is much closer to a rehash than the outliner's
  framing suggests.** Its step 2 "Termination Lemma" is explicitly
  admitted (by the outliner's own text) to be "structurally the same open
  question as jacobsthal-covering-bound's un-derived K(a1) boundedness" —
  and jacobsthal-covering-bound has been deprioritized for 3 rounds on
  exactly this un-derived bound. Separately, active-set-stabilization's
  Contamination Dichotomy Lemma already reduces Nec-finiteness to "does an
  uncontaminated multiple appear at bounded index" — which is the same
  underlying question again, just posed as "does the adaptive process
  terminate." So this new slug currently overlaps in substance with TWO
  already-tracked open gaps (one dead-ish, one live), not zero. It is a
  genuinely different top-level *architecture* (construction-first vs.
  existence-first, satisfying the whole-attempt requirement — it is not a
  fragment of another slug's proof), so it's legitimate to register and
  build once, but the population is now carrying three-and-a-half
  approaches (state-compactness, active-set, covering-system, plus
  deprioritized-jacobsthal) all bottomed out on essentially the same
  Nec/Q-finiteness wall. Flagging this explicitly per the dispatch
  instruction: **this is the shared-gap risk CLAUDE.md warns about**, even
  though the individual mechanisms (CRT-density, global counting,
  adaptive-construction+exchange) are legitimately different in kind.
- **Binding condition for this round's build:** the builder must produce
  either (a) a genuinely new idea for bounding the termination stage
  count K(a1) (not "no counterexample found after N steps," which is
  exactly jacobsthal's already-exhausted evidence), or (b) explicit,
  provable non-identity with jacobsthal's Λ^(K) mechanism and
  active-set-stabilization's Contamination Dichotomy (i.e., show the
  adaptive process's obstruction-resolution order or termination
  criterion differs in a way that actually helps). If neither is
  produced, the builder must self-report **RETHINK**, not "partial" — per
  the outliner's own stated gate, which I am endorsing and making
  mandatory, not optional.

## 5. Deprioritizing scalar-difference-pigeonhole / scalar-difference-majorization

**Justified — concur with the outliner.** Both forks have independently
certified negative lemmas (Excess Growth Rate Lemma: single-affine-rate
majorization is circular because the only workable rate is L/T itself,
the theorem's unknown output; Morse-Hedlund window-sum-counting: dead)
across 3 rounds converging on the same wall ("must know Q/(T,L) first"),
which matches CLAUDE.md's explicit plateau-break criterion (3+ rounds,
same wall from different angles). Their certified lemmas remain reusable
and their Elo correctly reflects "still live but not worth builder time
this round" rather than a hard kill — no action needed; do not build this
round, revisit only if a genuinely new non-affine/two-rate/substitute-
divisibility idea (Mechanism B, aimo-0680-style) surfaces.

## Diversity assessment (per CLAUDE.md's mandate)

Three of the four build candidates (state-compactness-pigeonhole,
active-set-stabilization, covering-system-construction-exchange), plus
the deprioritized jacobsthal-covering-bound, all ultimately attack the
same central gap (finiteness/self-sufficiency of Nec/Q_min) via different
mechanisms. This is not an automatic collapse (per memory rule: different
mechanisms attacking the same hard lemma reflect the problem's real
bottleneck, not lack of diversity) — but it does mean the field's only
genuinely different top-level architecture right now is
renormalization-induction-on-seed (induction on the seed itself, no
Q-machinery at all). If round 8 shows the Nec/Q-finiteness wall still
unmoved on all three fronts, the orchestrator should treat that as a
3-way (not 1-way) confirmation that this specific formulation of the
central gap needs a genuinely different framing, not just another
mechanism variant.

## Ranking

Registered `covering-system-construction-exchange` (cold-start 1500).
Ran `update_ranking` comparing the new slug against established peers
(state-compactness-pigeonhole, active-set-stabilization,
renormalization-induction-on-seed all beat it — untested, admitted
overlap with a deprioritized mechanism) and drew it against
jacobsthal-covering-bound (genuinely comparable difficulty/status).
Confirmed state-compactness-pigeonhole and active-set-stabilization as
a near-draw at the top (both produced honestly-gapped, genuinely new
mechanisms this round of comparable rigor), both above
renormalization-induction-on-seed this round (whose general "p=3" claim
needed a correction after my counterexample), which in turn remains above
the deprioritized scalar-difference forks and jacobsthal-covering-bound.

Post-ranking Elo: state-compactness-pigeonhole ~1691 (highest),
active-set-stabilization ~1640, renormalization-induction-on-seed ~1551,
scalar-difference-majorization ~1533 (dead-end, deprioritized),
scalar-difference-pigeonhole ~1505 (deprioritized),
covering-system-construction-exchange ~1458 (new, unbuilt),
jacobsthal-covering-bound ~1390 (deprioritized).

## Build set

All four candidates are worth building this round: the top two
(state-compactness-pigeonhole, active-set-stabilization) for continued,
genuinely distinct progress on the central Nec/Q gap; renormalization-
induction-on-seed to attempt the corrected (two-prime-only) p=3 target;
covering-system-construction-exchange under the binding termination-
mechanism-or-RETHINK gate above, to test whether the plateau-break
framing has real legs or should be cut next round.

build set: state-compactness-pigeonhole, active-set-stabilization, renormalization-induction-on-seed, covering-system-construction-exchange
