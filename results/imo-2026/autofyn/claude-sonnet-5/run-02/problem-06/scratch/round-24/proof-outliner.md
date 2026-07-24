## imo-2026-06

a1-3qk-subfamily-theorem: revise
Target: Literal T=1, L=3 periodicity for the full a_1=3q^m subfamily
(prime q≥7, q≠5, fixed integer m≥1), for every n≥1. (Currently `partial`:
m=1 already certified as its own theorem `a1-3q-subfamily-theorem`; this
approach targets the strict generalization to all fixed m≥1.)
Technique: Strong induction (same skeleton as certified m=1 proof) +
Legendre Sieve Gap Bound + Primorial Floor Bound (both certified, generic
in the modulus), applied with the CORRECTED sieve modulus.
Skeleton:
  1. Retract Part IV's `r=ω(qK_0)` computation and its "provably
     insufficient for m≥2" conclusion — a bookkeeping error, not a real
     obstruction: Part III of this same file already proves q-coprimality
     is free at k=0, so the correct modulus is K_0 alone, `r=ω(K_0)`.
  2. Recompute the k=0 residual table for m=2 with the corrected bound —
     by explicit computation.
  3. Close the k≥1 residual band for m=2: re-derive (not assume) whether
     the certified m=1 uniform-in-k argument transplants, given K_0(q,2)=
     3q+s_0 is NOT q-independent (unlike m=1's bounded K_0∈{4,5}) — the
     genuinely open technical step.
  4. Stretch goal: attempt m=3 using the conjectural `k*~q^{m-2}` crossover
     scaling to bound casework, only if m=2 closes with time remaining.
  5. Assemble: exhaustive case coverage as in the certified m=1 proof.
Key lemmas (claim + mechanism):
  - Corrected sieve modulus at k=0: r=ω(K_0) not ω(qK_0), because q-
    coprimality is already free by Part III's t_i≡i-1 (mod q) argument
    (n_0<q forces i-1 nonzero mod q for the whole candidate window).
  - Primorial Floor Bound (certified): ω(M)=r ⟹ M≥(r+1)!, reused verbatim
    to prune both residual bands to small finite lists.
Open gaps: Step 3 (k≥1 closure for m=2, given K_0 grows linearly with q
unlike m=1) is the one genuinely open new content — concretely scoped, not
open-ended, per the round-24 a1-3qk-closure explorer's diagnosis.
Cases to cover: n odd/even x k=0/k≥1, same shape as the certified m=1
proof, per fixed m.
Watch out for: do not re-cite the old Part IV numbers (r=ω(qK_0)) as
evidence of anything — redo the computation from scratch with the
corrected modulus during build, not by assuming the explorer's numeric
scan is itself a proof.

a1-3aq-subfamily-theorem: new
Target: Literal T=1, L=3^a periodicity for a_1=3^a*q (fixed integer a≥1,
prime q≥7, q≠3), outside a small a-dependent (not q-magnitude-dependent)
finite exceptional set of primes, for every n≥1.
Technique: Same strong-induction + Legendre Sieve Gap Bound / Primorial
Floor Bound template as the certified a1-3q theorem, applied to the
OPPOSITE generalization axis from a1-3qk (exponentiate the SMALL prime 3,
keep the large prime q to the first power) — chosen because this keeps
K_0 bounded as q→∞ (unlike a1-3q^m, where K_0~3q^{m-1} grows with q),
per the diversity-scout explorer's K_0-boundedness criterion.
Skeleton:
  1. Base case, a_n+1 illegality, Case (a) (q∤(a_n+2)) — transplant
     verbatim from a1-3q; these only use P(a_1)={3,q}, true for any a≥1.
  2. Case (b) odd-n Parity Witness — re-derive from scratch (do not
     copy-paste): gcd(N,a_n)=gcd(N,2), N=a_n+2=3^a*q+3n-1; parity depends
     on parity of q+n via "3^a is odd for any a≥0" (an easier fact than
     a1-3qk's "q^m is odd," since 3 is fixed).
  3. Case (b) even-n, k=0 window — CHEAP KILL FIRST: derive the exact
     K_0(q,a) formula symbolically for a=1,2,3 and verify it is
     q-independent (function of a and q mod 3 pattern only), checking it
     predicts exactly the diversity-scout explorer's numeric findings
     (a=2's sole exception at q=11; a=3,4,5 clean) before committing to
     the general induction.
  4. Case (b) even-n, k≥1 residual band — apply the certified sieve
     toolkit near-verbatim, since K_0(q,a) is conjectured q-independent
     (unlike a1-3qk's stuck m≥2 case), needing only a finite table sized
     by a.
  5. Assembly — exhaustive case coverage, as in a1-3q.
Key lemmas (claim + mechanism):
  - K_0(q,a) is q-independent because the additive shift in K_0's formula
    comes from the FIXED small-prime part 3^a, so a_1/q=3^a stays constant
    as q→∞ (the load-bearing new lemma; must be proved as an exact
    formula, not asserted from the explorer's numeric scan).
  - 3^a is odd for any a≥0 — immediate (product of odds is odd), used in
    the Parity Witness step.
Open gaps: everything beyond step 1 is unbuilt; step 3's exact K_0(q,a)
formula and q-independence proof are the load-bearing new content.
Cases to cover: n odd/even x k=0/k≥1, same shape as a1-3q, a-dependent
(not q-dependent) exceptional table size.
Watch out for: confirm during build (not assume from the explorer's
q<300 sweep) that a=2's exceptional set is exactly {q=11} via a wider
sweep (q<20000); do not conflate this family with the composite-c trap
(even c collapses to the certified 2|a_1 theorem; c with ≥2 distinct odd
primes is FAH-hard) — this family is single-prime-power-times-large-prime,
structurally distinct from both; keep this approach and a1-3qk-subfamily-
theorem BOTH live as genuinely different generalization axes of a1-3q, not
duplicates — one may fail where the other succeeds.

new-prime-recruitment-rate-bound: new
Target: H2 (self-absorbing core existence/termination) — approached via a
genuinely different top-level framing than S_0-containment (which round 23
proved gives no leverage: `direct-s0-self-absorption`'s Proposition 3
certifies the Bounded Witness Lemma cannot establish full-core containment,
and its "direct" framing reduces to a pre-existing lemma instance with no
new content). This targets boundedness of the RATE of brand-new-prime
recruitment directly, via the greedy process's own minimality rule, not via
any fixed-core containment claim.
Technique: Direct counting/growth argument on R(N) := #{j≤N : P(a_j)
introduces a prime never seen before}, using the certified elementary
ω(a_n)≤log_2(a_n) bound plus the Generalized Bounded Gap Lemma's linear
growth ceiling, combined with the greedy minimality rule itself (a_j is
the SMALLEST legal candidate) — genuinely distinct proof mechanism from
every certified H2-adjacent lemma (all of which are containment/presence
arguments, never counting/rate arguments on new-prime arrivals).
Skeleton:
  1. Cheap-kill / mandatory pre-screen: rerun a_1=11305's simulation at
     2-4x the window (millions of terms, faster sieve-based factorization,
     not trial division) to determine whether its observed ~√N new-type
     arrival rate (flat across 400k terms per this round's h2-absence
     explorer) is a genuine structural signal or a finite-window artifact
     — per the standing workspace rule (round 17 precedent: always widen
     before trusting non-stabilization).
  2. If BOTH seeds show genuine deceleration after the larger run: attempt
     the R(N) counting argument (step 2 of the approach file) bounding new-
     prime recruitment via density + minimality — speculative, flag the
     mechanism as the open key lemma, not yet found.
  3. If a_1=11305 still shows no deceleration at the larger window: pivot
     to determining whether this refutes R(N)-finiteness specifically, or
     H2 itself — these may be logically different strengths (H2 only
     needs SOME self-absorbing core to exist, not that all primes are ever
     recruited into one bounded set) — this relationship must be checked
     explicitly before drawing any refutation conclusion.
Key lemmas (claim + mechanism, both genuinely open):
  - R(N)-finiteness (if provable): counting argument combining the
    certified elementary ω-bound with greedy minimality to show new-prime
    recruitment becomes asymptotically rare — mechanism not yet found.
  - R(N)-vs-H2 logical relationship: must be established explicitly (not
    assumed) before any conclusion from step 3's simulation outcome is
    drawn either way.
Open gaps: essentially everything — fresh top-level target, no prior
certified content; step 1's deepened simulation is the mandatory first
task before any structural attempt.
Cases to cover: two branches (H2-supportive vs H2-threatening outcome of
the deepened simulation) — report whichever the data supports honestly,
do not force a predetermined conclusion.
Watch out for: do not conflate R(N)-finiteness (a strictly stronger claim
than H2's "some core exists") with H2 itself — a negative result on R(N)
is not automatically a refutation of H2; also do not let this collapse
back into the confirmed-dead "total prime support stays in a fixed finite
set" circular framing (round 2/17 NEVER rule) — this is a counting/rate
argument on the process, not an assumed-finite ambient state space; this
target is logically distinct from H1/FAH — even full success here leaves
H1 (the harder, more open crux) untouched.

## Notes on approaches not advanced this round
- `direct-s0-self-absorption`: not advanced further — its own framing
  (S_0-containment) was shown by its own Proposition 3 to add no leverage
  beyond the already-certified Monotone Chain Reformulation Lemma; per
  CLAUDE.md's reframe guidance, a refuted framing's siblings are also
  suspect, so effort moves to `new-prime-recruitment-rate-bound`'s
  genuinely different target instead of patching the same wall.
- `a1-5q-subfamily-theorem`: kept low-priority per round 23's own
  recommendation (outline-only, 3x the casework of a1-3q for comparable
  Elo risk) — not included in this round's build set; revisit once
  a1-3qk/a1-3aq's build slots are exhausted.
- No new general H1/FAH fresh-framing approach opened this round — the
  round-24 diversity-scout explorer's crux-corpus resweep confirmed (a
  third time) the well is exhausted (aimo-0648's order-statistic-
  confinement mechanism is a third confirmed-equivalent instance of the
  already-dead "bounded finite state space" corridor); per the standing
  rule (round 17), do not force a 32nd direct H1 mechanism onto the same
  crux this round — channel effort into subfamily scouting and H2 instead,
  as done above.
