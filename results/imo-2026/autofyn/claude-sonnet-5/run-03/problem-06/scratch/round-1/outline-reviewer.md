# Outline review — imo-2026-06, round 1

Problem: prove the greedy "smallest a_{n+1}>a_n coprime-violating none of a_1..a_n" sequence is
eventually exactly periodic (exists T,L with a_{n+T}=a_n+L).

Verified numerically (python3, gcd-greedy simulation up to 4000 terms):
- a_1=15 -> T=8, L=30=2·3·5
- a_1=35 -> T=34, L=210=2·3·5·7
- a_1=105 -> T=58, L=210=2·3·5·7 (same L as 35, different T — confirms
  jacobsthal-covering-bound's own observation that T is NOT a function of S/L alone)
- a_1=21 -> T=1, L=3 (S stabilizes immediately to {3}, since 21=3·7 but only 3 is ever
  needed again once density from {3} covers everything a_1 needs)
- a_1=33 -> T=1, L=3 (same reason, S={3})

This confirms: (a) the phenomenon is real and periodicity does hold in all sampled cases,
(b) L = ∏(active prime set S), where S can be a PROPER SUBSET of a_1's own prime factors
(not all of a_1's prime factors need recur), (c) T is data-dependent, not a function of S
alone — so any approach promising to compute T in closed form from S/L is doomed and must
fall back to pigeonhole for T specifically. All four outlines already state this correctly
where relevant (jacobsthal-covering-bound explicitly, others implicitly via the pigeonhole
finish) — good, no approach is chasing the wrong invariant.

## Whole-attempt check
All four target the actual problem statement end to end (existence of T,L), not a
sub-lemma sliced across files — no splitting concern. Good.

## Shared-crux check
All four bottom out on the same true hard step: "only finitely many primes are ever
load-bearing" (the active prime set S stabilizes). The outliner flagged this and argued
it is not an artifact of same-framing collapse but a genuine convergence of independent
routes on the actual bottleneck of the problem. I agree: this is the well-known crux of
this style of "greedy-gcd" construction (matches the general shape of such competition
problems — the sieve-forcing/density argument for prime-set stabilization is the real
content), and the four outlines attack it via genuinely different mechanisms:
density-threshold, quantitative growth/counting, a-priori-fixed-state (deferred), and
explicit phase-induction/self-sufficiency. This is legitimate diversity of *mechanism*
even though the wall is shared. Not a RETHINK trigger on its own. Flagging for future
rounds: if 2-3 rounds pass with all four approaches stalled on this exact lemma with no
progress, the next round should recruit ≥1 approach with a framing genuinely outside the
"prime-blocking sieve" picture entirely (e.g. attacking via the complement/gap-sequence
directly, or an entropy/counting argument on the sequence of *gaps* rather than on primes)
rather than another variant of the sieve framing.

## Per-approach verdicts

### active-set-stabilization — APPROVE (build)
Technique (density threshold on active prime set S, then pigeonhole on (a_n mod L,
coverage-state) for periodicity) is sound and standard for this problem type. Lemma 1
(S finite) is stated with a real mechanism (density ≥ threshold makes a fresh prime
never competitive against the greedy smallest-choice rule) — not just a label. Honestly
flags its own central gap: does S_n actually *reach* the self-sufficient threshold in
finite time (rather than growing forever just under it)? That is the one thing the
builder must close; a hand-wave here would be fatal, so it must be either proved with
an explicit bound or the approach demoted.
Issues to fix while building:
- Step 5's claim that the greedy rule is a pure function of (a_n mod L, coverage state)
  needs the per-term (not just eventual) fact that every a_i in the stable regime has a
  prime factor in S — currently only "eventually" is argued.
- The prefix-extension step (finite prefix -> single global T,L) is asserted as
  "standard" but not actually spelled out; needs an explicit argument (e.g. take T a
  suitable multiple of n2-n1 so that a_1's orbit under +T,+L also realigns).
- Do not let the builder assume L=∏S trivially; the numeric check above shows S can
  exclude some of a_1's own prime factors (a_1=21 -> S={3} only), so "L=∏S" must be
  understood as ∏ of the *active* set, proved equal to the actual stabilized value, not
  assumed a priori.

### state-compactness-pigeonhole — APPROVE (build)
Genuinely different architecture (state-first, S-second: fixes K, L_0 a priori rather
than solving for S first) — this is real diversity, not a cosmetic rename of
active-set-stabilization. Its value-add is honestly stated: it doesn't crack the hard
lemma, it isolates the FINISH (periodicity from a repeated state) as a clean, independent
piece via the aimo-0680 "divisibility forces a bounded difference to zero" trick, and
defers the hard content into Lemma 4 ("large primes eventually irrelevant") which it
correctly admits is exactly the same difficulty as active-set-stabilization's Lemma 1.
This is legitimate — a second, more robust proof of the finish is worth having even if
the hard lemma is shared, since it removes dependence on pinning S down exactly.
Issues to fix:
- Lemma 1's "permanently dead" invariant should be spelled out as a one-line proof (R(a_i)
  fixed => blocking status of any m against a_i never changes) — currently correct but
  underspecified; easy to formalize, should not be left informal in the final proof.
- K, L_0 "sufficiently large a priori" is an existence claim, not yet shown to exist —
  builder must either prove existence of a sufficient K (reducing to the same density
  argument as active-set-stabilization) or admit this is not actually independent of that
  lemma after all.

### growth-rate-contradiction — CHANGES REQUESTED (build, but flag the circularity)
Real alternative mechanism (quantitative growth/counting vs. density threshold) — worth
keeping in the population. However the outline itself admits a circularity in Lemma A/the
a_n=O(n) upper bound: that bound is derived by assuming "already-active small primes
cover density ≥ 1-epsilon," which is close to assuming a piece of what Lemma 1 (S
stabilizes) is supposed to prove. Before the builder invests in the counting estimate
(Lemma B), it MUST first fix this circularity: derive an UNCONDITIONAL a_n = O(n) bound
(not dependent on assuming any density threshold already reached) — e.g. from Bertrand's
postulate alone giving a universal bound on gaps once at least one prime is known active
(a_1's smallest prime factor), or explicitly show 2 small primes become active within a
bounded number of steps from a_1 alone, as a genuinely separate, non-circular sub-lemma.
Also: Lemma B conflates "gap ≥ q_k" (correctly flagged as a lower bound only) with the
derived inequality "a_{n_k} grows at least like sum q_j" — this step needs the actual
inequality chain written out precisely, not asserted.
Build note: builder should spend first effort resolving the circularity before the
counting estimate; if it cannot be resolved without importing active-set-stabilization's
own lemma, this approach effectively collapses into the same lemma with different
notation, and should be marked as such rather than presented as independent.

### jacobsthal-covering-bound — CHANGES REQUESTED (do not build this round)
Weakest of the four. Correct and useful contribution: identifies the "self-sufficiency"
stopping criterion for S concretely, and honestly and correctly abandons the constructive
closed-form-T ambition once computational evidence (a_1=35 vs a_1=105, confirmed above)
refutes it. But: (a) Lemma A (phase-count bound) is the least developed of any lemma
across the four files — it just restates "reduces to the same core difficulty" without
adding a mechanism beyond growth-rate-contradiction's Lemma B, so it does not currently
offer independent leverage; (b) the "L=∏S exactly, not a proper multiple" claim in Watch
out for is unproven and could be a real gap (needs to show every prime in S is actually
necessary in the eventual cycle, not just present). Keep in the population (registered),
but not in this round's build set — redundant with growth-rate-contradiction's harder
core lemma without adding new mechanism; revisit if growth-rate-contradiction's
circularity fix reveals the phase-count framing has something to add.

## Dead ends check
`results/imo-2026-06/current.md` is empty (Status: unsolved, no approaches tried yet) —
nothing to avoid repeating this round.

## Ranking (Elo, this round's round-robin)
1. state-compactness-pigeonhole — 1531 (draw vs active-set-stabilization, beat the other two)
2. active-set-stabilization — 1530 (draw vs state-compactness-pigeonhole, beat the other two)
3. growth-rate-contradiction — 1485 (lost to top two, beat jacobsthal-covering-bound)
4. jacobsthal-covering-bound — 1453 (lost all three)

build set: active-set-stabilization, state-compactness-pigeonhole, growth-rate-contradiction
