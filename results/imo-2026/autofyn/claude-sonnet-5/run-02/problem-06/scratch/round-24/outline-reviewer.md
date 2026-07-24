# Outline review — round 24 (imo-2026-06)

## Summary of independent verification

I re-derived the corrected sieve bookkeeping from scratch (own `sympy` script,
not trusting the explorer's numbers), independently ran the `a1-3aq` numeric
claim from scratch (own greedy simulator), and re-read the H2 lemma chain to
check the new H2 target isn't a repackaged dead framing. Details below.

---

## 1. `a1-3qk-subfamily-theorem` (revise) — APPROVE

**Claimed fix**: round 23's Part IV used the wrong sieve modulus at `k=0`
(`r=ω(qK_0)` instead of `r=ω(K_0)`), because Part III of the same file already
proves `q`-coprimality is free at `k=0` (`t_i≡i-1 mod q`, nonzero since
`n_0<q`). This "fails everywhere" was an artifact of the inflated modulus.

**Independently reverified, from scratch** (own script, not reading the
explorer's/builder's code): recomputed `n_0, s_0, K_0(q,m)=3q^{m-1}+s_0`,
`r=ω(K_0)` and the crude sieve requirement `L≥2^r(r+1)` at `k=0` for
`m=1,2,3`:

```
m=1: 1 failure  (q=11)               -- matches the certified m=1 theorem exactly
m=2: 4 failures (q=11,17,23,29), stable out to q<20000
m=3: 12 failures, largest at q=479, stable out to q<20000
```

This exactly reproduces the explorer's numbers (I did not reuse any of their
code — independent script, independent run). The bookkeeping correction is
**genuine and correct**: dropping the redundant `q` factor at `k=0` converts
"fails at every tested prime" into a small, apparently-finite residual table,
matching the m=1 precedent and matching round 23's own independent full-truth
computation ("zero failures beyond q=443/1103"). I also spot-checked the
`k≥1` band for `m=2` (modulus `qK`, since q-coprimality is *not* free once
`k≥1`) over `q<300,k≤30`: only 5 failures found, all small `k`, consistent
with a genuinely finite (not exploding) residual band — this is a sanity
check, not a proof, but it confirms the target the outline hands the builder
is realistic, not a fantasy.

**Verdict: APPROVE.** The bookkeeping fix independently holds. The outline
correctly scopes the one genuinely open new step (Step 3: whether the m=1
uniform-in-k closure transplants to m=2's q-dependent `K_0=3q+s_0`) as the
builder's primary task, and correctly instructs the builder to re-derive
(not assume) numbers from the explorer's scan. This is well-scoped, likely
closeable this round following the exact 3-round pattern that closed m=1.

---

## 2. `a1-3aq-subfamily-theorem` (new) — APPROVE, genuinely distinct axis

**Distinctness check** (not a repackaging of the stuck `a1-3q^m` direction):
`a1-3qk` exponentiates the LARGE prime `q` (`a_1=3q^m`), which makes
`K_0~3q^{m-1}` grow with `q`, permanently breaking `L/K_0→∞`. `a1-3aq`
exponentiates the FIXED SMALL prime `3` instead (`a_1=3^a q`, `q` to the
first power) — the opposite axis. Algebraically these produce structurally
different `K_0` behaviors (bounded vs. growing), so success/failure of one
says nothing about the other; this is a real fork, not the same gap wearing
different notation.

**Independently reran the numeric claim from scratch** (own Python greedy
simulator, distinct from the explorer's), `a_1=3^a q` for `a=1..5`,
`q∈[7,300)` prime, `q≠3`, 60 terms each:

```
a=1: 0 exceptions (already certified)
a=2: 1 exception — q=11, breaks at n=5 (a_5=110 vs predicted 111)
a=3,4,5: 0 exceptions
```

Exact match to the explorer's report. This gives real, not merely asserted,
support for the outline's target, and confirms the `a=2,q=11` single hand-
checkable exception the outline flags as the load-bearing residual case.

**Verdict: APPROVE.** Genuinely different generalization axis from the stuck
`a1-3qk`; both should stay live as independent peers per the outline's own
instruction. The load-bearing new lemma (K_0(q,a) is q-independent) is
correctly flagged as needing an exact derivation, not an assumption from the
numeric scan — good practice, matches the pattern that worked for a1-3q and
a1-3qk's Parts I-II.

---

## 3. `new-prime-recruitment-rate-bound` (new) — APPROVE for build, with a
flagged equivalence risk to check first

**Distinctness check** (not a single-gap-trap duplicate of the dead
`direct-s0-self-absorption`/S_0-containment line): the S_0-containment family
(certified dead-end via `bounded-witness-insufficiency-for-containment.md`)
tries to show a FIXED, pre-chosen finite core `S` eventually contains every
`P(a_j)` — a presence/containment claim against a specific target set. This
approach instead counts `R(N)` = number of indices introducing a genuinely
new prime, using the greedy minimality rule + the elementary `ω`-bound — it
does not commit to any specific core in advance. This is a real difference
in mechanism (counting/rate vs. fixed-target containment).

**However, I want to flag a subtlety the outline does not fully spell out**:
`R(N)`-finiteness is *logically equivalent* to "the monotone chain
`S_M := S_0∪⋃_{j≤M}P(a_j)` eventually stabilizes" — which is precisely an
instance of the already-certified Monotone Chain Reformulation Lemma (letting
`M→∞`). If `R(N)` is shown finite, that trivially gives a self-absorbing
core (the stabilized `S_M` itself), so the "positive" branch of this
approach, if it succeeds, would not be surprising new machinery so much as a
concrete instantiation of an already-certified reduction. This is **not**
fatal — the *novelty* here is the proposed proof TECHNIQUE (a counting/rate
argument via ω-bound + minimality on `R(N)` directly, never attempted in the
workspace), not the target statement itself, and the outline is honest that
step 2's mechanism is "speculative, not yet found." I require the builder's
first deliverable (after the mandatory simulation pre-screen) to explicitly
verify this equivalence and state clearly whether closing R(N)-finiteness
would in fact just be a new proof of the SAME sub-gap (a) that
`core-growth-monotonicity` and `direct-s0-self-absorption` already found
non-constructive/insufficient — if so, the "genuinely new mechanism" framing
should be scoped down to "a new attempted proof technique for the same known
open target," not sold as a fresh corridor.

**Cheap-kill / risk already correctly identified by the outline**: the
h2-absence explorer's own finding (a_1=4807 decelerating, a_1=11305 flat
`~√N` out to 400k terms) is a genuine risk that R(N) may be unbounded at
11305 — the outline correctly makes the deepened simulation the *mandatory
first task* before any structural attempt, and correctly separates
"R(N)-finiteness false" from "H2 false" (these are not the same claim). This
is good risk management; I did a small independent spot-check (own script,
`a_1=11305`, 4000 terms, counting first-appearances of literal new primes —
not extended-types) and found new-prime events still occurring at ~11% rate
with no visible deceleration in this short window — consistent with, though
far too short to confirm, the explorer's flagged risk. This reinforces:
step 1 (the deepened simulation) must actually be done and reported honestly
before the builder invests in the counting-argument mechanism.

**Verdict: APPROVE for build**, conditioned on the outline's own step-1
mandatory pre-screen, plus the additional requirement above (name the
Monotone-Chain-Lemma equivalence explicitly and don't oversell novelty if the
positive branch just re-derives the same known-insufficient sub-gap by a
different technique).

---

## Diversity check across the whole field

Top of the ranked field now: `covering-system-construction` (established,
long-stale content, not touched this round), `greedy-exchange-cost-potential`,
`n1-periodicity-reconciliation` (consolidation), `a1-3q-subfamily-theorem`
(3rd APPROVE, certified), then the newly-active trio above. The three
approaches in this round's build set attack genuinely different targets: two
are disjoint subfamily-generalization axes of the same certified base
theorem (large-prime exponent vs. small-prime exponent — confirmed
structurally distinct, not variations of one framing), and the third is a
distinct H1-independent hypothesis (H2) via a counting mechanism, not a
persistent-type/FAH argument. No shared-gap collapse observed this round —
good.

## Cut

Nothing cut this round — all three proposed approaches pass distinctness and
soundness checks (with the one caveat/requirement noted on
`new-prime-recruitment-rate-bound`).

## Ranking

Ran `update_ranking` anchoring the newcomers against established siblings:
`a1-3q-subfamily-theorem` (certified) beats `a1-3qk-subfamily-theorem`
(still open); `a1-3qk-subfamily-theorem` beats `direct-s0-self-absorption`
and `cofinite-window-capacity-bound` (both stalled/no-leverage H2/FAH
attempts); `a1-3qk-subfamily-theorem` and `a1-3aq-subfamily-theorem` drawn
(equally well-scoped, independent axes); `a1-3aq-subfamily-theorem` beats
`new-prime-recruitment-rate-bound` (stronger verified numeric support,
lower risk) and beats `direct-s0-self-absorption`; `new-prime-recruitment-
rate-bound` beats `direct-s0-self-absorption` and `core-growth-monotonicity`
(both confirmed dead-ends in the same H2 territory, this is a fresher
mechanism). This also cleared the `stale` flags on `a1-3qk-subfamily-theorem`
and `direct-s0-self-absorption`.

build set: a1-3qk-subfamily-theorem, a1-3aq-subfamily-theorem, new-prime-recruitment-rate-bound
