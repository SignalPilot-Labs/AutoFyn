## imo-2026-06

Context: round 19, 14th consecutive round with the main FAH crux (H1) unresolved
(19+ confirmed-dead mechanisms), 4th consecutive fresh-framing sweep (rounds 13,
15, 17, 19) finding zero new corridor for H1 directly. Per CLAUDE.md's
plateau-breaking rule and this round's dispatch, the field below (a) puts up a
genuine insurance/consolidation approach so the run's best conditional
deliverable is airtight, (b) tries exactly one genuinely new angle on H1 (the
Two-Sided Singleton Witness existence gap, via a density/anatomy-of-integers
route — a different PROOF STYLE, not another existential-pigeonhole variant),
(c) tries one genuinely new angle on H2 (the weaker "some self-absorbing S*
exists" target, distinct from full NTBT), and (d) advances the numeric-hardening
NTBT record. None of the ~19+ confirmed-dead FAH mechanisms, the refuted
`a_1=p·q` clean-threshold family, or the exhausted H2 counting/pigeonhole
corridor (3 sub-routes, round 18) are re-proposed.

---

n1-periodicity-reconciliation: revise
Target: the problem's actual claim (eventual periodicity for every `a_1 > 1`),
via the certified Master Conditional Theorem's reduction to exactly two named
open hypotheses (H1: FAH/Symmetric FAH/Cofinite FAH/EEA at the terminal
self-absorbing core; H2: absorption-chain termination), plus a clean audit of
what is unconditionally already solved.
Technique: consolidation/audit round — certify one new general meta-lemma that
formally closes off an entire proof-technique family (rather than attempting a
20th individual FAH mechanism), and tighten the write-up of the run's
guaranteed deliverable.
Skeleton:
  1. Restate the Master Conditional Theorem exactly as already certified: the
     problem's claim follows from H1 ∧ H2 — cite the existing certified chain
     (Free Facts → Persistent-Type Pigeonhole → Finite Core Theorem → Extended
     Persistent-Type Pigeonhole → Self-Absorbing Core Theorem → Universal Early
     Intersection Lemma → Literal n=1 Periodicity Theorem), no new content here.
  2. Certify the **Generalized Class-Blindness Obstruction** (new lemma, this
     round's fresh-framing explorer's finding): for ANY statistic computable as
     a function of the window of past legality-predicate (`gcd(c,a_i)>1`)
     Boolean outcomes — density, running average/count, second moment,
     Borel–Cantelli count, a finite-Fourier/character-sum coefficient, an
     LP-relaxation value — no such statistic can ever yield a class-
     DISCRIMINATING (which specific prime) conclusion. Mechanism: the recursive
     definition consults only the Boolean predicate `gcd(c,a_i)>1`, never the
     identity of the prime realizing it; two histories that are Boolean-
     identical but arise from different specific shared primes are literally
     indistinguishable to any function computed purely from that window, by a
     one-line "function of a coarser quotient carries no finer information"
     argument. This is a genuine strict generalization of the already-certified
     Density-Argument Vacuity Corollary / Selection-Rule Class-Blindness
     finding (previously stated only for density/counting statistics).
  3. Write up, as the run's guaranteed deliverable, the exact scope of what is
     unconditionally solved: `2 | a_1` (T=1,L=2, `even-seed-literal-
     periodicity-theorem`) and `a_1 = p^k` for any prime p, k≥1 (T=1,L=p,
     `prime-power-seed-literal-periodicity-theorem`), overlapping exactly at
     `a_1=2^k`; state plainly this does NOT cover the general case.
  4. Honest final status paragraph: H1 and H2 remain open; the FAH mechanism
     search is now confirmed exhausted across existential/pigeonhole,
     magnitude-sandwich, CRT-glue, sieve/density (now formally the ENTIRE
     statistical family per step 2), automaton/Morse-Hedlund, algebraic-
     number-theory, generating-function, and crux-corpus-transplant corridors.
Key lemmas (claim + mechanism):
  - Generalized Class-Blindness Obstruction — because the greedy recursion's
    legality test is a Boolean predicate blind to prime identity, so is every
    real/vector-valued function computable from a window of its outcomes; this
    is an information-theoretic fact about the recursion's definition, not a
    seed-specific computation, hence applies uniformly to every member of the
    "statistical method" family in one proof.
Open gaps: H1 and H2 themselves — this approach does not and cannot resolve
either; it only formally closes off one entire family of future H1 attempts and
tightens the write-up.
Cases to cover: none (a single general lemma + documentation).
Watch out for: do not let the write-up imply Status is anything but `partial`
at the workspace level — the two unconditionally solved subfamilies are real
but the general claim remains conditional on H1 ∧ H2.

---

triangle-consistency-pigeonhole: revise
Target: the problem's actual claim, by attempting to close the Two-Sided
Singleton Witness Theorem's open residual hypothesis (existence, for a rogue
base-type pair, of matching singleton out-of-core witnesses on both sides) —
which would close H1 (Cofinite FAH) in general via the already-certified
theorem.
Technique: a genuinely different PROOF STYLE from all 19+ dead mechanisms —
an anatomy-of-integers / smooth-number density argument about the VALUES a_n
themselves (not about the greedy selection rule, so it is not obviously
subject to the Class-Blindness Obstruction above, which is about statistics of
the selection process, not about arithmetic properties of the resulting
integers) plus a second, finite-alphabet pigeonhole layer to force the same
prime on both sides.
Skeleton:
  1. Fix a rogue pair (A',B') at the properly-recruited terminal core S0 (Finite
     Core Theorem, already certified).
  2. Cite the certified Bounded/Generalized Bounded Gap Lemma: for n with
     ρ(n)=A' (resp. B'), `a_n ≤ a_1 + (n-1)·a_1`-type linear ceiling — hence
     `ω(a_n) = O(log a_n / log log a_n)` by the standard elementary
     prime-counting bound on ω (cite as an anatomy-of-integers fact — NOT
     currently in `knowledge_base.md`; must be stated and proved from scratch,
     e.g. via `a_n ≥ 2^{ω(a_n)}`... — a one-line elementary bound, not deep
     analytic number theory).
  3. **Key Lemma (OPEN — the actual new content), Density/Occurrence Lemma for
     Singleton Signatures**: among occurrences n with ρ(n)=A' in a window
     [1,N], INFINITELY MANY have out-of-core cofactor `a_n / (S0-part of a_n)`
     equal to a single prime (a "singleton" occurrence) — attempt via an
     anatomy-of-integers heuristic made rigorous: the out-of-core cofactor is
     an increasing sequence of integers constrained only by the S0-legality
     predicate, and a positive proportion of integers in ANY sufficiently
     regular subsequence of density-comparable growth are themselves prime or
     "almost prime" (few prime factors) by sieve-theoretic lower bounds (e.g.
     a Brun-sieve-style lower bound for almost-primes in a linearly growing
     sequence) — try the WEAKER "infinitely often" target first (cheaper),
     not a positive-density claim, since infinitely-often is all Step 5 needs.
  4. Symmetric statement for B'.
  5. **Second pigeonhole layer**: from the certified Generalized Bounded
     Witness Lemma's Corollary, the set of primes that can EVER serve as a
     singleton witness for occurrences of A' (resp. B') is confined to
     `F' := P(a_{m_A}) \ S0` for a FIXED witness index `m_A` (this alphabet
     IS already finite and fixed, independent of n, by the certified Confined-
     GCD Lemma — re-derive explicitly here since it is the load-bearing finite-
     alphabet fact the whole mechanism needs) — so infinitely many singleton
     A'-occurrences pigeonhole into some fixed `q ∈ F'` occurring as sole
     singleton witness infinitely often; likewise some fixed `q' ∈ F''` for
     B'. If `F' ∩ F'' ≠ ∅` is forced to contain a common q (a THIRD pigeonhole
     step, needs its own argument — not yet available), apply the Two-Sided
     Singleton Witness Theorem to close Cofinite FAH for the pair.
  6. Generalize over the finitely many rogue pairs at S0 to close H1 fully at
     S0.
Key lemmas (claim + mechanism):
  - Density/Occurrence Lemma for Singleton Signatures (OPEN, the real gap) —
    heuristically true because a linearly-growing constrained cofactor
    "typically" has few large prime factors (anatomy-of-integers normal
    order), but NOT yet proved to survive at the genuinely hard,
    properly-recruited terminal cores (where empirical singleton rate is only
    5–37%, not the 85–92% seen at easy/under-recruited cores per this round's
    explorer data) — this is the crux the builder must attack, not assume.
  - Finite-Alphabet Confinement (already certified via Confined-GCD Lemma,
    reuse directly, do not re-derive from scratch) — because any single fixed
    witness index `m_A` bounds every later occurrence's escaping divisors to
    divisors of the fixed integer `P(a_{m_A})`.
Open gaps: Step 3/4 (the density/infinitely-often lemma itself — genuinely
unproved, may be FALSE at hard cores) is the whole new content. Step 5's "common
q forced across F' ∩ F''" sub-step is a THIRD pigeonhole layer with no argument
yet — F' and F'' are two different fixed finite sets and nothing yet forces
them to share an element, let alone share the specific infinitely-recurring one
from each side.
Cases to cover: none yet — this is exploratory; if Step 3 fails outright
(counterexample found where singleton occurrences are finite in number), the
approach dies cleanly and should be recorded as such rather than patched.
Watch out for: this is the one place in the current field genuinely at risk of
being vacuous or false — require the builder's FIRST task to be a direct
computational check, on the two known hard seeds (a_1=4807, 11305), of whether
singleton A'-occurrences are truly infinite (not just present at low rate in a
finite window) before attempting any general proof; if the rate is low but the
COUNT keeps growing with the window (as the round-19 explorer's data already
suggests: 12/32, 26/452, 36/614, 18/206 non-zero absolute counts), this is
mild positive evidence but not a proof of infinitude — flag this distinction
explicitly to the builder.

---

core-growth-monotonicity: revise
Target: the problem's actual claim, via H2 — but attacking the strictly WEAKER
sub-target flagged by this round's H2-subfamily explorer as untried: existence
of SOME self-absorbing core S* (however large), not necessarily S*=Q
(that's NTBT) and not necessarily N(S*)=0 — this weaker existence claim is all
the Master Conditional Theorem's H2 hypothesis actually requires.
Technique: an existential/compactness argument on the deterministic refinement
sequence S_0 ⊆ S_1 ⊆ S_2 ⊆ ... (each S_{k+1} enlarging S_k by exactly the
primes needed to resolve the finitely many new exceptions found at S_k), using
the ALREADY-CERTIFIED fact that base types τ(n) := P(a_n) ∩ Q live in the FIXED
finite set 2^Q (Q does not grow — only the recruited core S_k does) — a
different mechanism from the already-exhausted counting/pigeonhole corridor
(which tried to bound N(S_k) itself; this tries to show the REFINEMENT PROCESS
cannot run forever without contradiction, via the primes-recruited sequence
being non-repeating and the base-type alphabet being fixed).
Skeleton:
  1. Cite the certified Termination Criterion Lemma (terminates iff (N(S_k))
     bounded) and Binary Refinement Lemma (adjoining one prime splits each
     S_k-persistent type into at most 2 sub-types, a subset of {B, B∪{p}}).
  2. Observe (already implicit, make explicit): every S_k-persistent type's
     BASE type τ(n) = P(a_n) ∩ Q lies in the fixed finite set 2^Q, independent
     of k — the core enlarges but Q never does.
  3. **Key Lemma (OPEN, new sub-target), Non-Recurrence of Refinement Primes**:
     each prime p adjoined at step k (k=0,1,2,...) is adjoined at most once
     (cores strictly increase, primes are never removed) — so if the process
     ran forever it would recruit infinitely many DISTINCT primes; try to
     derive a contradiction from this together with the FIXED base-type
     alphabet 2^Q and the certified Binary Refinement Lemma's "at most
     doubling" bound on type count per refinement step: since only finitely
     many primes ever actually occur among a_1,...,a_n for any finite n (each
     a_n has finitely many prime factors), and the refinement rule only ever
     adjoins a prime that ALREADY occurs as a factor of some already-emitted
     a_n, an infinite refinement sequence would require infinitely many
     distinct primes among the (infinite) sequence a_1,a_2,... — which is true
     and not immediately contradictory (the sequence does have infinitely many
     distinct prime factors overall) — so THIS naive version does not yet give
     a contradiction; the builder must find a sharper invariant (e.g. tie the
     refinement rate to the GAP growth rate via the certified Bounded Gap
     Lemma, to get a genuine finite bound on how many refinement rounds can
     occur before index N, then argue by contradiction against unbounded
     N(S_k)) — flagged HONESTLY as unresolved, not claimed solved.
  4. If Step 3 succeeds in any form, existence of S* (as the limit/eventual
     stable core) follows, closing H2's weaker form.
Key lemmas (claim + mechanism):
  - Fixed Base-Type Alphabet (already implicit/certified via Persistent-Type
    Pigeonhole, reuse directly) — because Q = P(a_1) is fixed once and for all,
    independent of the enlarging core S_k.
  - Non-Recurrence of Refinement Primes (OPEN, genuinely new sub-target,
    honestly flagged as NOT yet reducing to a contradiction — the naive
    version fails as shown in Step 3; a real new invariant tying refinement
    rate to index growth is needed) — the actual gap.
Open gaps: Step 3 is unresolved and, on first pass, does not obviously work;
this is disclosed explicitly rather than smuggled. The approach may die at
Step 3 exactly as `core-growth-monotonicity`'s Proposition 3 already showed for
the STRONGER N(S_k)-bounding target — the builder must explicitly check
whether the weaker existence-only target evades Proposition 3's "two
consistent finite-prefix extensions" obstruction (which was about bounding a
NUMBER from finite data) since mere existence is a different kind of claim
(existential, not a numeric bound) — if it does not evade it, report cleanly as
a further-confirmed dead end for this sub-target too, rather than forcing
progress.
Cases to cover: none — a single existential argument, or an honest negative
report if it fails.
Watch out for: do not let "existence of S*" quietly collapse back into
"N(S_k) bounded" (the same open quantity under a different name) — the builder
must show the weaker target is actually attacked with different tools (the
fixed base-type alphabet + prime non-recurrence, not the M_B threshold
machinery Proposition 3 already refuted) or else honestly report it is the
same wall.

---

self-absorbing-by-construction: advance
Target: the problem's actual claim, via the open NTBT conjecture (`N(Q) ≤ 1`
for every `a_1`) as a sufficient special case of H2.
Technique: continued numeric hardening (no new proof mechanism attempted or
claimed — the counting/pigeonhole corridor is confirmed exhausted, per round
18's own finding and this round's H2-subfamily explorer's re-confirmation; do
NOT re-attempt it).
Skeleton:
  1. Fold in this round's two new adversarial-seed results as further
     hardening of the empirical record: `a_1=510510` (`|Q|=7`, largest tested
     to date) — two apparent single-occurrence types at window 60,000 both
     confirmed to recur by window 200,000, zero surviving exceptions; and
     `a_1=209370` (skewed: one huge prime 997 with four small primes) — a
     genuine candidate single at window 60,000 recurs by window 300,000, even
     the trivial full-Q type recurs, zero singles surviving. Record both as
     independently-reproducible data points (already independently verified
     by the explorer with a naive-generator cross-check for correctness).
  2. State plainly: this is evidence only, at the largest `|Q|` and most
     skewed seed shape tested to date; NTBT itself remains unproved; the
     counting/pigeonhole corridor (3 sub-routes) remains exhausted and should
     not be re-attempted without a genuinely new mechanism.
Key lemmas: none new this round (pure numeric hardening).
Open gaps: NTBT itself, entirely open.
Cases to cover: none.
Watch out for: do not let repeated "resolved window artifact" findings be
read as approaching a proof — each is a single data point; state the standing
window-artifact pattern explicitly (per memory rule: re-run at 2-4x window
before trusting non-recurrence) so future rounds do not need to rediscover it.
