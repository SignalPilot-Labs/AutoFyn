## imo-2026-06

Shared preliminaries used by every approach below (not a rival approach by itself —
fold into each skeleton as Steps 1-2; do not spend an approach slot on it):

- **Free Lemma P (permanent hub).** For every n≥2, gcd(a_n,a_1)>1 (apply the
  defining condition with i=1), so a_n is divisible by some prime of the FIXED
  finite set P_1 := rad(a_1). This holds for literally every n, not just
  infinitely many — the strongest immediate structural fact available.
- **Free Lemma Q (prime-power base case, fully proved, verified by explorer
  gap-monovariant).** If |P_1|=1, i.e. a_1=p^k, then by induction a_n=a_1+p(n-1)
  for every n≥1: assume a_1,...,a_n are all multiples of p; none of a_n+1,...,
  a_n+p-1 is admissible since gcd(a_n+j,a_1)=gcd(a_n+j,p^k)=1 for 1≤j≤p-1 (p∤a_n+j),
  while a_n+p is a multiple of p, hence gcd(a_n+p,a_i)≥p>1 for every earlier
  multiple-of-p term — admissible and minimal. So T=1, L=p, exactly, from n=1.
  This disposes of the entire "a_1 is a prime power" family (in particular every
  even a_1) completely; every approach below only needs to handle |P_1|≥2.
- **Watch-out baked into every approach:** the problem demands a_{n+T}=a_n+L for
  EVERY positive integer n, not eventually. A pigeonhole/state argument naturally
  gives periodicity only from some transient index N_0 on; each approach's
  skeleton includes an explicit sharpening step to extend this to all n≥1 (or to
  avoid a transient altogether) — this is real, required work, not a formality.
- **Do NOT assume "only finitely many primes divide some a_n" globally** —
  refuted computationally by explorer finite-primes-crt (a_1=6: >100 distinct
  primes appear among the first 600 terms). The correct, still-open target is a
  finite *load-bearing/permanently-sufficient* backbone, not a finite prime
  support.
- **Do NOT assume a fixed formula for the backbone** (e.g. rad(a_1)∪{2,3}) —
  refuted by a_1=247=13·19, which empirically needs an extra prime 7 not
  predictable from a_1 and the two smallest primes, and did not visibly
  stabilize within 15000 simulated terms. Use a_1=247 as the standard stress
  test for any bound claimed.

---

### backbone-existence-crt (new)

Target: for every a_1>1, there exist T,L≥1 with a_{n+T}=a_n+L for every n≥1.

Technique: finite covering-backbone existence + finite-state pigeonhole
(schema of crux `aimo-0678`) + CRT to assemble the periodic residue structure;
finish with a Bezout-style backward-propagation (crux `aimo-0648`) to extend
periodicity to every n, not just eventually.

Skeleton:
  1. Dispose of |P_1|=1 via Free Lemma Q. Assume |P_1|=k≥2 from here.
  2. Define the backbone-growth process: H_0=P_1; whenever the greedy choice of
     a_{n+1} is forced to use a prime q∉H_n to satisfy some constraint against an
     earlier term (no H_n-only-divisible candidate works), set H_{n+1}=H_n∪{q}.
     H_n is non-decreasing in n. — by construction/definition, no separate tool.
  3. KEY LEMMA (backbone finiteness — the central gap): H_n stabilizes at some
     finite H* after finitely many recruitments N_0. Mechanism to pursue: once
     |H_n|≥2, the density of integers divisible by ≥1 prime of H_n is bounded
     below by an explicit constant (inclusion–exclusion / Mertens-style bound —
     KB "Divisor analysis", "Bertrand's postulate" as a density-bound donor); a
     NEW prime is only ever recruited to resolve a constraint against one
     specific old term a_i whose factorization is disjoint from H_n. Argue the
     set of such "exceptional" old indices i is itself finite — because once i is
     resolved (a later term shares a prime with a_i, adding that prime to H),
     that same prime remains available forever after (H only grows), so a_i can
     never again cause a NEW recruitment; hence each index i causes at most one
     recruitment, and recruitments must stop once the (finite, bounded-by-density)
     set of currently-unresolved old indices is exhausted. This needs the
     density bound to be strong enough to guarantee the unresolved-index set
     does not grow faster than it is resolved — the actual hard inequality,
     left as the open gap for the builder.
  4. GIVEN H* finite with L:=lcm(H*): define state s_n = (a_n mod L, together
     with, for each of the finitely many indices i≤N_0 not yet "automatically"
     covered by H*, whether p|a_i for each p∈H* — a finite record). Show that
     for n≥N_0 the map s_n ↦ s_{n+1} is a well-defined deterministic function
     (constraints against indices >N_0 are governed purely by H*-divisibility
     disjunction, constraints against indices ≤N_0 are governed by the finite
     fixed record) — by CRT combine the disjunctive H*-conditions into a
     periodic-mod-L admissibility test (KB "Modular arithmetic, CRT").
  5. Finite state space + determinism ⇒ some state repeats: s_m=s_{m+T} for the
     first repeat (Pigeonhole, KB "Pigeonhole/extremal principle") ⇒
     a_{n+T}-a_n = L' constant for all n≥m, where T = the state's return time
     and L' is the sum of one period's gaps.
  6. SHARPEN to all n≥1 (the required, non-optional finishing step): show the
     transition s_n↦s_{n+1} is not just deterministic forward but that the FIRST
     recurrence is already at n=1 — i.e. s_1 lies on the eventual cycle — by a
     backward-injectivity argument: if two states s_a, s_b (a<b) map to the same
     forward orbit, use crux `aimo-0648`'s Bezout-combination-of-shifts device
     to show the periodic pattern, once established, forces its own initial
     segment to match it (using gcd(T, b-a)-type combinations of index shifts to
     propagate the period backward one step at a time down to n=1). This is a
     genuine open gap, not routine bookkeeping — flag explicitly.

Key lemmas (claim + mechanism):
  - Free Lemma P (see above) — because i=1 is one of the universally-quantified
    constraints in the problem's own definition.
  - Free Lemma Q (see above) — because p^k has only p as prime factor, giving
    a forced clean induction.
  - Backbone finiteness (Step 3) — because each recruited prime, once added,
    permanently resolves its triggering old index, so the recruitment count is
    bounded by the (density-bounded) number of ever-unresolved indices.
  - Finite-state pigeonhole periodicity (Step 5) — because a deterministic map
    on a finite set must revisit a state (KB Pigeonhole).

Open gaps:
  - Step 3 (backbone finiteness): the density argument sketched is not yet a
    complete inequality; this is THE hard gap of the whole approach.
  - Step 6 (periodicity from n=1, not just eventually): the backward-propagation
    argument is sketched but not executed.

Cases to cover: |P_1|=1 (done, Lemma Q) vs |P_1|≥2 (main content, no further
sub-cases needed at the outline level — sub-cases if any arise inside Step 3/6).

Watch out for: a_1=247 (two large odd primes, no small factor) as the stress
test — explorer finite-primes-crt did not detect periodicity for it within 15000
terms, so Step 3's density bound must not silently assume a_1 has a small prime
factor.

---

### intersecting-family-covering-construction (new)

Target: same as above — full existence of T,L for every n≥1.

Technique: reframe the whole problem as an infinite pairwise-intersecting family
of finite prime-sets {P_n = primes(a_n)}_{n≥1} that all meet the fixed hub P_1
(explorer gap-monovariant's opening 1) — then, instead of proving abstract
backbone finiteness first (as in backbone-existence-crt), **explicitly construct**
a candidate periodic covering system and verify by strong induction that the
greedy process both enters it immediately and stays in it forever. This is a
genuinely different order of operations: construct-then-verify rather than
prove-existence-then-derive-structure (Pólya "specialize/construct" heuristic).

Skeleton:
  1. Dispose of |P_1|=1 via Free Lemma Q; assume |P_1|=k≥2.
  2. Formalize: {P_n}_{n≥1} pairwise intersecting (P_i∩P_j≠∅, i<j — immediate
     from the defining condition applied at the later index), with the extra
     structural fact that every P_n (n≥2) meets the SAME fixed hub P_1 (Free
     Lemma P) — this is stronger than generic pairwise-intersection: it's a
     "sunflower-at-the-hub" structure, i.e. P_1 is a common transversal-partner
     for every other set.
  3. Use finite pigeonhole on the hub (crux `aimo-0421`'s "gcd against a fixed
     element has bounded range" schema): label each n≥2 by ℓ(n)∈P_1, a
     canonically-chosen prime of P_1 dividing a_n. Since |P_1|=k is finite, at
     least one label class is infinite — but push further: show (via a direct
     argument on greedy minimality, not yet proven — GAP) that ALL k labels are
     eventually simultaneously "active" (infinite), because if some p∈P_1 only
     ever labeled finitely many terms, greedy minimality would eventually prefer
     other primes over p in a way that produces a detectable smaller gap, giving
     a periodic sub-pattern with p pruned from the hub — i.e. the problem reduces
     to a smaller hub (p replaced-out of the covering), an induction on k=|P_1|.
  4. CONSTRUCT the candidate covering system directly: let H = P_1 ∪ E where E is
     a to-be-determined finite "extra/helper" prime set (start with E=∅, grow it
     by simulating/case-splitting on which pairs among the first few terms fail
     to be covered by P_1 alone — a finite, explicit case check, not an infinite
     induction). Let L=lcm(H) and let R ⊆ Z/LZ be the set of residues divisible
     by ≥1 prime of H. Candidate claim: for n large, a_n mod L cycles through a
     FIXED periodic subsequence of R determined by the greedy-minimality rule
     applied to R alone (ignore actual integer size, just which residue is next
     smallest in R not yet blocked by a live old-term constraint).
  5. Strong induction (KB "Invariants & monovariants"): maintain the invariant
     "a_1,...,a_n all lie in the constructed pattern AND every earlier pairwise
     constraint is already satisfied by H-divisibility alone"; show it is
     preserved at step n+1 by directly checking that the least element of R
     exceeding a_n mod L that is not literally forced-inadmissible by the finite
     set E's specific residues is achievable — GAP: proving E can always be
     chosen finite so this invariant is preservable, symmetric to backbone
     finiteness in the other approach but attacked via explicit residue-covering
     construction instead of abstract density.
  6. Because the invariant is checked from n=1 (not introduced at a transient
     point), periodicity for every n≥1 (not just eventually) falls out directly
     from the strong induction itself — this sidesteps the backward-propagation
     sharpening needed in backbone-existence-crt, which is this approach's main
     structural advantage if Step 5's gap closes.

Key lemmas (claim + mechanism):
  - Hub-labeling pigeonhole (Step 3) — because P_1 is fixed and finite, so
    ℓ:{2,3,...}→P_1 is a finite coloring (crux aimo-0421 schema).
  - Constructed covering system R sufficiency (Step 5) — because membership in
    R already guarantees compatibility with every OTHER term also in H's
    disjunction, by definition of "divisible by some prime of H."

Open gaps:
  - Step 3: all k hub primes eventually simultaneously active (or an induction
    reducing k) — not proven, currently only a plausibility argument.
  - Step 4/5: finiteness of the helper set E and preservability of the
    invariant from n=1 — the central unresolved gap, parallel to (but attacked
    differently than) backbone finiteness in the sibling approach.

Cases to cover: |P_1|=1 (Lemma Q); |P_1|≥2 with an induction on k intended in
Step 3 (each reduction step is a sub-case the builder must actually execute,
not merely gesture at).

Watch out for: explorer gap-monovariant's finding that not every start with
|P_1|≥2 needs a genuine multi-prime pattern — some (e.g. a_1=21=3·7, 55=5·11)
collapse to T=1 with a single dominant prime because a pure prime-power term
(e.g. 27=3^3) appears early and kills the disjunction down to one prime. The
induction in Step 3 must treat "one hub prime silently absorbs all the others"
as the base case of its induction, not an exception to route around.

---

### bounded-gap-density-covering (new)

Target: same — but attempt the CHEAP KILL first: a direct, backbone-agnostic
explicit bound on the gap sequence d_n=a_{n+1}-a_n, via pure density/counting
(no need to first pin down which primes form the backbone), then upgrade
boundedness to full periodicity by a generic pigeonhole argument. This is a
different order of attack from both approaches above (bound-first vs.
structure-first) and mirrors the "size/dyadic-bucket bound before the
sledgehammer" meta-strategy in knowledge_base.md.

Skeleton:
  1. Dispose of |P_1|=1 via Free Lemma Q; assume |P_1|=k≥2.
  2. Attempt a DIRECT explicit bound d_n ≤ D(a_1) for all n≥2, D an explicit
     function of a_1 only (not of n), via a density/covering-system counting
     argument in the flavor of crux `aimo-0447` (place a witnessing prime per
     constrained pair, bound how many pairs small primes can cover via Σ 1/p,
     force existence of a valid small candidate within any window of length D).
     GAP (likely the hardest part of this approach, flagged honestly): a naive
     density bound only shows SOME window of length D contains an integer
     divisible by a chosen prime of P_1 — it does NOT by itself guarantee
     compatibility with every one of the n-1 other earlier terms simultaneously,
     which is exactly the part that made a_1=247 slow to stabilize empirically
     (gaps up to 78 within 800 terms, not yet bounded there in the data). If
     this direct bound cannot be closed, this approach should be treated as
     likely to dead-end at this step and be reported as such rather than
     patched with unjustified assumptions.
  3. GIVEN Step 2 (d_n≤D for all n, some explicit or even just ineffective D):
     the tuple of the last D terms mod lcm(2,3,...,any primes appearing among
     a_1,...,a_1+ (bounded window)) — more carefully, the window
     (a_n, a_n mod m) for an appropriately chosen finite modulus m — takes
     finitely many values; a deterministic bounded-gap process on a finite
     window-state must revisit a state (Pigeonhole, KB "Pigeonhole/extremal
     principle"), giving eventual periodicity, exactly the two-stage skeleton
     of crux `aimo-0648` (bound the sequence into a finite range ⇒ pigeonhole
     ⇒ periodic ⇒ Bezout combination of gap sizes with gcd 1 to propagate a
     property to every index and sharpen the period).
  4. Sharpen eventual periodicity to periodicity for every n≥1 using the
     Bezout/backward-shift device from crux `aimo-0648` (same sharpening need
     as in backbone-existence-crt Step 6 — cite once closed there, or close
     independently here).

Key lemmas (claim + mechanism):
  - Direct gap bound (Step 2) — because a covering-system density argument
    (Σ 1/p over the primes actually available) forces a bounded search window
    to contain an admissible candidate, IF the density bound also handles
    simultaneous multi-term compatibility (the unresolved part).
  - Bounded-window pigeonhole periodicity (Step 3) — because finitely many
    window-states force a deterministic map to cycle.

Open gaps:
  - Step 2 is the honest cheap-kill attempt and may simply fail for the
    multi-term-compatibility reason noted; if the builder cannot close it, this
    approach should report a dead-end AT STEP 2 specifically (not silently
    assume boundedness), so the population doesn't waste a second round
    re-trying the same density bound without a new idea.
  - Step 4, same sharpening gap as backbone-existence-crt.

Cases to cover: |P_1|=1 (Lemma Q) vs |P_1|≥2.

Watch out for: this approach can look deceptively "almost done" once Step 3-4
machinery is written, while Step 2 (the actual hard content) remains unproven —
the builder must not present Step 3's generic pigeonhole template as if it
closes the problem when Step 2's inequality is still a gap.

---

### minimal-witness-index-descent (new)

Target: same — full existence of T,L for every n≥1.

Technique: a structurally different, more elementary mechanism from the three
above: track, for each n, the SET of "tight" earlier indices — those i≤n for
which the constraint gcd(a_{n+1},a_i)>1 is not already guaranteed by any prime
that already covers a MORE RECENT term — and run a descent/extremal argument
directly on this tight-index set (crux `aimo-0503`'s "pass the residual
divisibility constraint down one index until cases exhaust" schema), rather
than on primes (approach 1) or on constructed residue patterns (approach 2) or
on raw gap size (approach 3).

Skeleton:
  1. Dispose of |P_1|=1 via Free Lemma Q; assume |P_1|=k≥2.
  2. Define, for each n, Tight(n) := {i≤n : no prime dividing a_i also divides
     any a_j with i<j≤n} — the earlier terms whose "coverage obligation" toward
     a_{n+1} cannot be discharged by piggybacking on a more recent term's
     already-shared prime. (By Free Lemma P, 1∈Tight(n) is possible only if no
     later term ever re-used a prime of P_1 — track this carefully.)
  3. KEY LEMMA (index-descent finiteness — the central gap, attacked via direct
     descent rather than density): |Tight(n)| stays bounded as n→∞, because
     each time a NEW element enters Tight(n) (an old index i whose prime set
     becomes "orphaned" — no later term shares its prime), the greedy
     minimality of a_{n+1} forces the very next terms to preferentially
     re-share a prime with recently-orphaned indices before drifting further
     (least-successor greedily "cleans up" recent debt first, since re-using an
     already-present small-ish prime is cheaper than recruiting a fresh large
     one) — formalize by descent on max(Tight(n)) (the most recently orphaned
     tight index), analogous to crux aimo-0503's repeated "re-run the bound on
     the preceding pair, passing the residual constraint down one index, until
     cases exhaust."
  4. GIVEN |Tight(n)|≤B (bounded), the primes needed at step n+1 come only from
     ∪_{i∈Tight(n)} primes(a_i) ∪ P_1, a set of size bounded in terms of B and
     the (bounded, by the analogous argument) number of prime factors of the
     finitely many terms involved — giving the same finite-modulus structure as
     backbone-existence-crt Step 4-5, reached via a different route. Finish with
     the same pigeonhole-periodicity + Bezout-backward-sharpening machinery
     (KB Pigeonhole; crux `aimo-0648`) as in backbone-existence-crt Steps 5-6.

Key lemmas (claim + mechanism):
  - Tight-index boundedness (Step 3) — because greedy minimality always clears
    the most recent unresolved obligation before creating a new one, so debt
    cannot accumulate without bound (an extremal/monovariant argument on
    max(Tight(n)), KB "Invariants & monovariants").
  - Finite-modulus reduction (Step 4) — because a bounded tight-set has a
    bounded union of prime factors, giving a finite state exactly as in
    backbone-existence-crt.

Open gaps:
  - Step 3 is unproven and is this approach's whole content; if it fails the
    approach dead-ends there specifically (report which claim about greedy
    "debt-clearing" behavior fails, with a counterexample if found).
  - Step 4's final pigeonhole+Bezout sharpening, shared in form with
    backbone-existence-crt Step 5-6 (may import that lemma if it gets proven
    there first — flag as an explicit reuse opportunity across approaches).

Cases to cover: |P_1|=1 (Lemma Q) vs |P_1|≥2; within Step 3, the sub-case where
Tight(n) never shrinks after some point vs. shrinks-then-regrows must both be
ruled out or handled.

Watch out for: this approach is the most likely to reveal whether "debt
accumulates unboundedly" is possible for a slow-transient start like a_1=247 —
treat that case as the disproof attempt for Step 3, not just a stress test to
pass after the fact.

---

Notes for the outline-reviewer: all four approaches ultimately need to resolve
one of two closely related hard facts — "a finite prime/residue structure is
permanently sufficient" (approaches 1, 2, 4, via three different mechanisms:
abstract density-driven recruitment, explicit constructive covering + strong
induction, and debt/tight-index descent) or "gaps are boundedly bounded without
first identifying the structure" (approach 3, the cheap-kill attempt, likely to
fail fast and should be judged quickly rather than nursed). Approach 2 is the
most structurally distinct (construct-then-verify, sidesteps the "n=1
sharpening" gap by design) and is the best candidate for a second-round pivot
if approach 1's abstract existence argument stalls. No approach should be
graded down merely for sharing the ultimate target lemma with another — they
are legitimately different routes to it; if the outline-reviewer's read is that
all four are "the same wall," the next round's outliner should be told to open
a fifth approach attacking the "for every n, not eventually" requirement as the
PRIMARY target instead of a finishing step (e.g. try to show the process is
periodic from n=1 by a wholly different global symmetry/self-similarity
argument, sidestepping backbone-finiteness entirely) — flagged here as the
reframing fallback if this round's field plateaus.
