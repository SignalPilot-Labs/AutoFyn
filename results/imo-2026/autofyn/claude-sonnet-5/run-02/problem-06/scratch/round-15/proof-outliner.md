## imo-2026-06

### Pre-screening notes (both dispatch items 1 and 2, done before scoping)

**H-prime-fiber packaging (fresh-framing explorer's opening 6) — NOT opened as a
new approach.** Checked the claimed equivalence directly: define
H := {p prime : p | a_n for infinitely many n}. By the certified Persistent-Type
Pigeonhole, Q ⊆ H (every base-type prime recurs infinitely often by definition of
persistence). H finite ⟺ only finitely many primes ever recur infinitely often ⟺
the recruitment process (covering-system-construction Step 4c) only ever recruits
finitely many NEW primes beyond S₀ ⟺ the recruitment process halts — this is a
literal restatement of "the process defined in Step 4c halts," which current.md
already identifies as the exact halting question equivalent to (†). The one-line
argument: every recruited prime q_k is, by the Generalized Bounded Witness Lemma's
Corollary, forced to divide infinitely many A'-type terms — i.e. q_k ∈ H by
construction — so "H is finite" and "recruitment halts" are the same event viewed
from two ends (H ⊇ every prime ever recruited, and recruitment adds exactly the
primes witnessing H's growth). No new leverage found (confirms the explorer's own
honest risk flag). Do not re-propose H-finiteness as if it were a bypass; if a
future round wants this vocabulary, it must supply new leverage on Σ_{p∈H} 1/p or
similar, not just the reformulation itself.

**Small-|Q| rogue-pair-COUNT enumeration (bespoke explorer's suggestion) — opened
below as `rogue-pair-termination-potential`, verified genuinely distinct from the
16 dead mechanisms.** The distinguishing feature: prior attempts (round 3's
minimal-counterexample-glue, since retired) tried to prove V=∅ outright via a
size measure |A'|+|B'| that was non-decreasing under refinement (documented dead
reason: recruitment always ADDS a prime, so this measure cannot descend). This
new approach instead (a) works at the level of the finite POOL of possible
BASE-type pairs (bounded by 3^|Q|, since each prime of Q is independently "in A",
"in B", or "in neither" for a candidate disjoint pair (A,B) — a hard, computable,
Q-only bound, unlike the extended-type alphabet which can grow with recruitment),
and (b) tracks how recruitment interacts with this fixed-size pool via the
already-certified Monotonicity of Resolution Lemma (once two types share a prime,
every later refinement still shares it — permanent). This is a genuinely
different induction variable (bounded finite base-pair pool + a monotonicity fact
already in hand) than anything in the 16 dead mechanisms, though — as flagged
honestly below — its hardest sub-lemma (whether the weighted extended-pair
potential can be bounded independent of how many times recruitment splits types)
is a real, unresolved risk, not a guaranteed win.

---

rogue-pair-termination-potential: new
Target: the whole problem — ∃ T, L with a_{n+T} = a_n + L for all n (eventually;
n=1-literal case handled downstream by n1-periodicity-reconciliation, conditional
on this approach's FAH-level conclusion).
Technique: well-ordering / finite-descent induction on a NEW potential function
counting (weighted) unresolved rogue extended-type pairs, bounded a priori by a
quantity depending only on |Q| — a fixed-pool finiteness argument, distinct from
prior magnitude/counting/existential mechanisms (17th distinct mechanism attempt).
Skeleton:
  1. Recall the recruitment process (covering-system-construction Step 4c): a
     sequence of finite prime sets S₀ ⊆ S₁ ⊆ S₂ ⊆ ... with S_{k+1} = S_k ∪ {q_k},
     q_k forced by the Generalized Bounded Witness Lemma's Corollary to resolve
     some rogue pair (A'_k, B'_k) of S_k-extended-persistent types with disjoint
     BASE types (A_k, B_k) ⊆ Q. (†) holds iff this process halts (R_k = ∅ for
     some k). — by the certified reduction already in current.md.
  2. **Base-pair pool bound (new, cheap, Q-only).** The set of candidate disjoint
     base-type pairs {(A,B) : A,B ⊆ Q, A∩B=∅, A,B both persistent base types} has
     size at most 3^{|Q|} (each prime of Q lands in exactly one of "A only",
     "B only", "neither"; "both" is excluded by disjointness) — a fixed integer
     depending only on |Q|, computable directly from a_1's factorization, by
     elementary counting.
  3. **Key Lemma (Base-Pair Permanent Resolution).** If a base-type pair (A,B)
     ever has EVERY pair of its extended refinements (A',B') intersect at some
     level S_k (i.e. (A,B) is "fully resolved" at S_k), then by the certified
     Monotonicity of Resolution Lemma, (A,B) remains fully resolved at every
     later level S_{k'} ⊇ S_k — because resolution (a shared prime) is preserved
     under refinement. — mechanism: direct application of the certified lemma,
     no new proof needed for this step alone.
  4. **Open Key Lemma (Splitting-vs-Resolution Balance) — the actual crux of this
     approach.** Recruiting q_k resolves the SPECIFIC triggering rogue pair
     (A'_k,B'_k) (by construction), but simultaneously each existing S_k-extended
     type can split into two S_{k+1}-children (one containing q_k, one not),
     potentially creating NEW candidate rogue pairs among the split children of
     OTHER, previously-unresolved base pairs. Claim to attempt: the total number
     of "still-unresolved base-type pairs" (in the sense of step 3) is
     non-increasing across rounds AND strictly decreases at the triggering pair's
     own base type — i.e. splitting can multiply the extended-type alphabet
     WITHIN an unresolved base pair, but does not create unresolved base pairs
     that were not already unresolved (base types themselves never change,
     only their possible extended refinements). Mechanism proposed: unresolved
     base pair status is defined at the base-type level (∃ ONE bad extended
     refinement pair), so splitting only adds more potential rogue instances to
     an ALREADY-unresolved base pair — it cannot make a previously fully-resolved
     base pair unresolved again (by step 3), and it cannot manufacture a brand
     new disjoint base-type pair not already in the ≤3^{|Q|} pool of step 2
     (base types themselves are fixed subsets of Q throughout the whole process).
     If this holds, the number of unresolved BASE pairs is non-increasing and
     strictly decreases whenever recruitment is triggered (since a trigger
     requires an unresolved base pair, and the round is only "wasted" if it fails
     to fully resolve that base pair — flag this precisely as the sub-case to
     check: does resolving ONE extended-pair instance for a fixed base pair
     leave OTHER extended refinements of the same base pair still rogue,
     stalling on the SAME base pair forever? This is the genuine open risk —
     see Watch out for below).
  5. **If step 4 holds in some form** (even a weaker "strictly decreases within
     ≤3^{|Q|} rounds, amortized" version): the process halts after at most a
     computable-from-Q number of rounds, giving (†) unconditionally. Then apply
     the existing, unconditional CRT + cyclic-pigeonhole finish
     (covering-system-construction Step 5) verbatim: L := ∏_{p∈S₀_final} p,
     T := |eligible residues|, a_{n+T}=a_n+L for n beyond a finite threshold.
  6. n=1-literal periodicity: defer to n1-periodicity-reconciliation's
     Self-Absorbing Core Theorem, imported as-is (conditional on this approach's
     FAH-level conclusion, matching that approach's own stated hypothesis).
Key lemmas (claim + mechanism):
  - Base-Pair Pool Bound: |{(A,B) disjoint base pairs}| ≤ 3^{|Q|} — because each
    prime of Q independently falls in exactly one of 3 categories relative to a
    candidate pair.
  - Base-Pair Permanent Resolution: once fully resolved, stays resolved — because
    the certified Monotonicity of Resolution Lemma gives permanence for any
    SPECIFIC shared prime, and "fully resolved" is a conjunction over finitely
    many (at any fixed stage) extended-pair instances, each individually
    permanent.
  - Splitting-vs-Resolution Balance (OPEN, the hard step): recruitment cannot
    manufacture a newly-unresolved base pair from a previously-resolved one, and
    each triggered round makes genuine progress on its own base pair — because
    base types are fixed subsets of Q for the whole process (only extended
    refinements grow), so the ≤3^{|Q|}-sized pool of step 2 is an a priori
    ceiling on how many "resolution events" can ever be needed IF each base pair
    only needs to be resolved once in the "at least one witness pair" sense
    (this last parenthetical claim — that resolving ONE extended-pair instance
    per base pair suffices, rather than needing to resolve ALL non-canonical
    extended-refinement pairs of that base type — is the specific place this
    approach could collapse back into the open general FAH question; flagged
    honestly, not assumed).
Open gaps: Step 4 (Splitting-vs-Resolution Balance) is entirely open and is the
  load-bearing claim; Step 5 is free once Step 4 holds. Builder's first task
  should be a CHEAP numerical check on the on-record rogue-pair seeds (a_1=175,
  187, 209, 247, 385, 11305) — track the number of DISTINCT unresolved base
  pairs (not extended pairs) across however many recruitment rounds each needs,
  and confirm this count is non-increasing and small (≤3^{|Q|}) before investing
  in a general proof.
Cases to cover: none beyond the general argument (this is a mechanism attempt,
  not casework) — but the builder should explicitly test the |Q|=2 and |Q|=3
  seeds first (base-pair pool sizes 9 and 27) since they are exhaustively
  checkable by hand/computation and would either give a clean proof-of-concept
  or an early, cheap falsification.
Watch out for: the precise risk that "a base pair can require MULTIPLE
  recruitment rounds on itself before its base pair is fully resolved" (i.e. the
  same base pair keeps re-triggering with a different non-canonical extended
  refinement each time) — if true, the process could still take unboundedly many
  rounds even with a fixed finite base-pair pool, collapsing this approach into
  the same open termination question (equivalent-difficulty restatement, like
  EEA/H). The builder must check this directly, not assume it away; if
  confirmed as a genuine obstruction, RETHINK honestly rather than patch.

---

n1-periodicity-reconciliation: advance
Target: the whole problem — the approach's OWN theorem (Self-Absorbing Core
Theorem, certified `lemmas/self-absorbing-core-theorem.md`) already proves
a_{n+T*}=a_n+L* for ALL n≥1 (literal, not just eventual) CONDITIONAL on (i) a
self-absorbing core S* existing (the absorption process terminating) and (ii)
FAH holding at level S*. This round's task is closing sub-gap (i)
(existence/termination of S*) and investigating sub-gap (ii)'s companion
question (can N(S*) be taken to be 0, i.e. is the theorem's threshold literally
n=1 with no exceptions at all).
Technique: direct construction/termination argument for the "absorption
process" (distinct object from rogue-pair-termination-potential's recruitment
process, though structurally similar in shape — both are "does a greedy
prime-set-growing process halt" questions) — reuse the same
Monotonicity-of-Resolution-style permanence fact if applicable, or a direct
pigeonhole on the (finite, by Non-Constructivity observation's own proof) set of
early transient terms needing absorption.
Skeleton:
  1. Restate the Self-Absorbing Core Theorem's precise hypothesis: S* absorbs
     every early term's FULL factorization up to threshold N(S*) — i.e. for
     every n < N(S*), P(a_n) ⊆ S*. Import as-is (certified).
  2. Existence/termination of S*: since each a_n (n≥1) has a FINITE prime
     factorization, and there are only finitely many n < any candidate
     threshold, S* := Q ∪ S ∪ ⋃_{n<N} P(a_n) for the FIRST N such that this
     union, together with FAH holding at that level, gives a self-consistent
     fixed point — by construction this is a finite set for any finite N; the
     open question is whether such an N exists at all (i.e. does enlarging S*
     to absorb more early terms ever stabilize, or does absorbing term N
     always require absorbing a fresh prime that then requires re-checking
     terms 1..N-1 again, non-terminating). State this precisely as the
     termination question (a strict analogue of rogue-pair-termination-
     potential's Step 4, but for absorption rather than recruitment).
  3. N(S*)=0 sub-question: test directly (computationally, then structurally)
     whether the certified 6-seed check (a_1=15,35,105,175,187,209, all giving
     threshold 0 for the WEAKER "plain N₁'" question per round 13's disclosure)
     extends to the theorem's actual N(S*) object once S* is concretely
     computed for at least 2 of these seeds — a cheap, concrete first step
     before attempting a general N(S*)=0 proof.
Key lemmas (claim + mechanism):
  - Absorption process termination (open): each absorption round adds finitely
    many primes (the factorization of one more early term); if this can be
    shown to converge (e.g. because early terms' factorizations only ever
    involve primes already forced into S by the Finite Core Theorem's own
    finite construction, once S is large enough) the process trivially
    terminates in at most (number of early terms needing absorption) rounds —
    because the Finite Core Theorem already gives an UNCONDITIONALLY finite S,
    so the only question is whether absorbing early-term factorizations stays
    within a finite enlargement of that same S, not an unboundedly growing one.
Open gaps: existence/termination of S* (main), N(S*)=0 (secondary, cheaper to
  test first).
Cases to cover: none beyond the construction.
Watch out for: this approach remains explicitly conditional on FAH holding at
  S* throughout — it does NOT touch the main crux even if fully closed this
  round; do not let its Status field imply more progress on the primary crux
  than made. If the termination argument in step 2 turns out to reduce to the
  same "does a greedy prime-recruiting process halt" question as
  rogue-pair-termination-potential, note the structural kinship explicitly
  rather than treating it as independent progress.

---

covering-system-construction: advance
Target: unchanged — the whole problem via the finite-core + CRT/cyclic-
pigeonhole construction, gated on (†).
Technique: unchanged (persistent-type/extended-type reconciliation via a
recruitment process reduced to CRT + cyclic pigeonhole).
Skeleton: unchanged from its current file; no new step proposed this round.
Key lemmas: none new proposed this round — kept live for ranking continuity and
as the canonical home for rogue-pair-termination-potential's Step 5 finish
(already proved there, importable verbatim).
Open gaps: (†) itself, now being attacked by rogue-pair-termination-potential
above using this approach's own machinery (Monotonicity of Resolution, Finite
Core Theorem, CRT finish).
Cases to cover: none.
Watch out for: nothing new; if rogue-pair-termination-potential succeeds, its
result should be merged into this file (or vice versa) since they share the
same finish — don't let them silently diverge into duplicate content.

---

greedy-exchange-cost-potential: advance
Target: unchanged — the whole problem via the integer-cost/witness-prime
pigeonhole framing, gated on the same (†)/FAH content.
Technique: unchanged.
Skeleton: unchanged from its current file; no new step proposed this round.
Key lemmas: none new proposed this round — kept live for ranking continuity.
Open gaps: same FAH/(†) crux, from this approach's own vocabulary (cost/exchange
framing).
Cases to cover: none.
Watch out for: nothing new this round.

build set: rogue-pair-termination-potential, n1-periodicity-reconciliation
