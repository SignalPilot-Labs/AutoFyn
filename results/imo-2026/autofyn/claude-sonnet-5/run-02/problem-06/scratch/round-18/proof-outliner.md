## imo-2026-06

triangle-consistency-pigeonhole: new
Target: the problem's actual claim — there exist T,L such that a_{n+T}=a_n+L
for every positive integer n (via closing H1 = FAH, the sole remaining
mechanism-gap in the certified Master Conditional Theorem chain of
`n1-periodicity-reconciliation.md`; H2 stays open, untouched by this approach).
Technique: gcd-colored complete graph + triangle-forcing double pigeonhole,
adapted from crux corpus ISL 2021 N8 (`aimo-0866`/`aimo-0421`). This is a
genuinely new mechanism family — not existential single-witness recruitment,
not magnitude-sandwich, not CRT-glue, not density/sieve, not automaton/walk,
not well-ordering descent, not Ramsey/ultrafilter, not per-prime-indicator
decomposition — per the round-18 fresh-framing explorer's systematic sweep
confirming no other new corridor exists. Directly targets the round-11
diagnosis: the missing ingredient is IDENTITY information tying multiple
far-apart terms' factorizations together, not mere existence of one shared
prime with one witness.
Skeleton:
  1. Import unconditionally: Free Facts Lemma (`lemmas/free-facts-gcd.md`)
     gives gcd(a_i,a_j)>1 for EVERY pair i<j (not just consecutive) — the
     precondition making the index set literally the complete graph K_∞ that
     the triangle-forcing technique operates on. — by citation, already
     certified, one-line re-derivation (apply the defining minimality
     property of a_j at index j-1, using i≤j-1).
  2. Fix two disjoint base (Q-)persistent types A, B (occurring infinitely
     often, disjoint under Q, per the certified Persistent-Type Pigeonhole —
     this is the standard FAH setup used by every prior mechanism). Let
     X_A, X_B be their infinite occurrence-index sets. — by
     `lemmas/persistent-type-pigeonhole.md`.
  3. Pick two DISTINCT witnesses m_A, m_A' ∈ X_A (both exist since X_A is
     infinite — this second witness is the genuinely new ingredient versus
     every prior single-witness mechanism). — by infinitude of X_A.
  4. First pigeonhole: since gcd(a_{m_A}, ·) can only take values among the
     finitely many divisors of the fixed integer a_{m_A}, and X_B is
     infinite, some divisor d1>1 of a_{m_A} satisfies gcd(a_{m_A},a_x)=d1 for
     infinitely many x in an infinite subset X_B^{(1)} ⊆ X_B. — by finite
     pigeonhole on Div(a_{m_A}) (finite set, since a_{m_A} is one fixed
     positive integer), mirroring `aimo-0866`'s opening step.
  5. Second pigeonhole, nested inside X_B^{(1)}: analogously, some divisor
     d2>1 of a_{m_A'} satisfies gcd(a_{m_A'},a_x)=d2 for infinitely many x in
     an infinite subset X_B^{(2)} ⊆ X_B^{(1)}. — same mechanism, applied to
     the second witness restricted to the already-pigeonholed subset (this
     nesting, not present in any prior mechanism, is what forces cross-triple
     — not just cross-pair — consistency).
  6. Triangle case-split (the actual `aimo-0866` crux move, adapted): every
     x ∈ X_B^{(2)} simultaneously satisfies gcd(a_{m_A},a_x)=d1 and
     gcd(a_{m_A'},a_x)=d2. Consider gcd(a_{m_A},a_{m_A'}) =: e (>1,
     unconditionally, by Free Facts). Case-split on whether gcd(d1,d2)>1:
     (i) if gcd(d1,d2)>1, some prime p | gcd(d1,d2) divides BOTH a_{m_A} and
     a_{m_A'} AND infinitely many a_x for x ∈ X_B^{(2)} — i.e. p is a
     candidate persistent-on-both-A-witnesses AND B-infinite-occurring prime,
     strictly stronger than any single-witness recruitment; (ii) if
     gcd(d1,d2)=1, examine whether p1|d1, p2|e interact via a THIRD
     pigeonhole step on e's own finitely many prime factors against
     X_B^{(2)} (the genuine `aimo-0866` triangle case, not yet carried out —
     open gap, see below).
  7. IF case (i) can be shown to occur for EVERY choice of m_A,m_A' (not just
     some), or IF case (ii) can be closed by forcing p1=p2 via a third
     witness/pigeonhole layer, conclude: some prime p divides infinitely many
     occurrences of BOTH A and B, i.e. FAH holds for this pair (A,B). — this
     is the open key lemma the builder must attack; do not assume it without
     proof.
  8. Repeat for every disjoint pair of persistent base types at the terminal
     core S* (finite, by the Finite Core Theorem / Master Conditional
     Theorem's own setup) to get full H1. — by finiteness of 𝒫'(S*)
     (Binary Refinement Lemma bound 2^|S*|-1) and step 7 applied pairwise.
  9. Feed H1 into the certified, already-audited Master Conditional Theorem
     (`n1-periodicity-reconciliation.md` §2) together with H2 to conclude the
     problem's claim. — by citation (H2 remains a separate, untouched open
     hypothesis; this approach does not resolve it).
Key lemmas (claim + mechanism):
  - Double-Witness Nested Pigeonhole Lemma: for any two occurrences m_A,m_A'
    of a persistent type A and any infinite occurrence set X_B of a disjoint
    type B, there exist divisors d1|a_{m_A}, d2|a_{m_A'} and an infinite
    X_B^{(2)} ⊆ X_B with gcd(a_{m_A},a_x)=d1 and gcd(a_{m_A'},a_x)=d2 for all
    x ∈ X_B^{(2)} simultaneously — because Div(a_{m_A}) and Div(a_{m_A'}) are
    each finite (fixed integers), so two sequential finite-pigeonhole passes
    on an infinite set always succeed (this is genuinely new content: no
    prior certified lemma nests two pigeonholes on TWO DIFFERENT A-witnesses
    against the SAME shrinking B-subset).
  - (OPEN, the actual crux) Cross-Witness Common-Prime Lemma: gcd(d1,d2)>1 —
    because [mechanism not yet found; candidate route: relate d1,d2 to
    gcd(a_{m_A},a_{m_A'})=e via the aimo-0866 triangle case-split, forcing a
    prime common to d1,d2,e]. This is the honestly-unproved key step — if it
    fails in general, the approach should look for a WEAKER sufficient
    corollary (e.g. cofinitely many pairs (m_A,m_A') give gcd(d1,d2)>1) per
    the workspace's established "cofinite suffices" precedent
    (`lemmas/cofinite-sufficiency-lemma.md`).
Open gaps: Step 6/7 (Cross-Witness Common-Prime Lemma) is the entire
mathematical content — everything else (steps 1-5, 8-9) is either already
certified or routine bookkeeping. The builder's FIRST task must be the
explorer's proposed cheap-kill: compute d1, d2 (and e) explicitly on 2-3
concrete rogue-pair seeds (a_1=175, a_1=4807, a_1=11305 — all already-used
canonical hard test seeds with known persistent types) BEFORE attempting a
general proof, to see whether gcd(d1,d2)>1 actually occurs, and whether it is
informative (shares a prime that is itself part of A's or B's persistent
signature, not an irrelevant bystander prime).
Cases to cover: gcd(d1,d2)>1 vs =1 (the case-split in step 6); if =1, whether
a third pigeonhole layer (on e's prime factors) can force a resolution, per
the literal `aimo-0866` proof structure (consult its full write-up in the
crux corpus, not just the report's summary, before building).
Watch out for: this mechanism must NOT collapse into a disguised repeat of
the confirmed-dead Single-Witness / Growing-Constraint Obstruction family
(round 9-10) — that family's failure mode was "the recruited prime is tied to
ONE witness index and an unboundedly growing pool of intermediate indices,
never provably universal." The double-witness nesting is only genuinely new
if the builder can show the found prime p is tied to TWO (or, after
induction, infinitely many) A-witnesses simultaneously, not just
re-deriving a single-witness fact in fancier notation — require the builder
to explicitly check this distinction against `lemmas/no-restart-lemma.md`
and the Growing-Constraint Obstruction write-up before claiming progress.
Also watch for the case-(ii) triangle step degenerating into "some prime
exists" (existential) rather than "the SAME prime recurs across witnesses"
(identity) — re-read `aimo-0866`'s own proof text carefully, since the crux
report's summary compresses this step and the real difficulty may be exactly
here.

self-absorbing-by-construction: revise
Target: the problem's actual claim, via closing H2 (absorption-chain
termination) in the Master Conditional Theorem chain — this approach's own
scope is H2/NTBT only; it does not touch H1/FAH.
Technique: same as before (self-absorption via the certified Vacuous/Weak
Self-Absorption Lemma), this round's revision is a bookkeeping correction to
the NTBT numeric-evidence record plus documenting that the H2
counting/pigeonhole corridor is now exhausted (per the round-18 H2 explorer's
Task 2), not a new proof mechanism.
Skeleton:
  1. Correct the round-17-flagged "unresolved candidate exception" language
     in this approach's own file and in `current.md`: a_1=255255's flagged
     single-occurrence type {5,7,11,13,17} (first seen n=27184) DOES recur,
     at n=135914 (confirmed via a from-scratch 500,000-term brute-force
     simulation, cross-validated against a naive gcd-based reimplementation
     on small n — see `/tmp/round-18/math-explorer-ntbt-h2.md` Task 1). Zero
     open numeric counterexamples to NTBT remain across ~50+ tested seeds. —
     by direct simulation, already done; the builder's job is to write this
     up as the corrected record, not re-derive it.
  2. Explicitly record, as a documented dead end (not a new attempt), that
     the H2 "counting/pigeonhole" corridor is now exhausted in all three
     forms tried: (a) bounding total absorption rounds via
     |𝒫'(S)|-per-round resolution — proved literally equivalent to bounding
     N(S_k) (already known non-constructive, `binary-refinement-and-
     threshold-recursion.md`); (b) bounding |S_∞| directly — circular, no
     independent finiteness source; (c) bounding |𝒫'(S_k)| alone without
     bounding S_k itself — even if provable, does not imply the absorption
     process HALTS (a genuinely weaker, insufficient target, matching the
     round-12 "vacuous weaker target" trap shape). — by the round-18 H2
     explorer's Task 2, already carried out; cite, do not re-derive.
  3. Optionally (cheap, low priority): add the audit explorer's observation
     that a_1 = p^k for prime powers of ANY prime p (not just p=2) already
     gives T=1,L=p unconditionally via the same elementary argument as
     `even-seed-literal-periodicity-theorem.md`, as a one-paragraph remark —
     but see the new sibling approach `prime-power-seed-periodicity-theorem`
     below, which is the correct home for this as its OWN certified theorem;
     do not duplicate full proof content here, just cross-reference.
Key lemmas: none new this round — this is a correction/bookkeeping round, not
a proof round for H2 itself. The certified Vacuous/Weak Self-Absorption
Lemma (`lemmas/vacuous-self-absorption-lemma.md`) stands unchanged.
Open gaps: NTBT (N(Q) ≤ 1 for every a_1) itself remains completely unproved
in general — now with stronger (but still non-conclusive) numeric support and
a documented account of why the natural counting-corridor attacks don't work.
No new proof route is proposed this round.
Cases to cover: none (bookkeeping only).
Watch out for: do not let "zero counterexamples across 50+ seeds" get
overstated as evidence approaching proof-strength — it is evidence, not a
proof, and the file must say so explicitly, matching the existing workspace
convention (see rule against overclaiming in CLAUDE.md).

prime-power-seed-periodicity-theorem: new
Target: the problem's actual claim, restricted to the subfamily a_1 = p^k for
any prime p and any k ≥ 1 (a genuine infinite subfamily disjoint in general
from, and strictly generalizing the p=2 case of, `even-seed-literal-
periodicity-theorem.md`): prove a_n = a_1 + p(n-1) for every n ≥ 1 (T=1,
L=p, literally from n=1), unconditionally, with no FAH/H1/H2 machinery
needed.
Technique: direct elementary strong induction, exactly the mechanism already
proved for p=2 in `even-seed-literal-periodicity-theorem.md`, generalized to
arbitrary prime p. This is the round-16-precedented move (register a genuine
narrow elementary subfamily theorem as its own approach) applied to a
concrete, previously-unregistered generalization the round-18 audit explorer
identified as "already implicit but never separately certified."
Skeleton:
  1. Base case: gcd(a_1,a_1)>1 trivially; Q = P(a_1) = {p} (single prime,
     since a_1=p^k). — by definition of a_1.
  2. Inductive step: given a_n with p | a_n for n ≥ 1 (by Free Facts, since
     Q={p} forces gcd(a_n,a_1)>1 ⟹ p|a_n for every n), show a_n+1,...,
     a_n+(p-1) are all illegal candidates for a_{n+1} and a_n+p is legal:
     — a_n+1: gcd(a_n+1,a_n)=gcd(1,a_n)=1, illegal by consecutive-integer
       coprimality (same mechanism as the p=2 proof's first branch). — by
       elementary number theory.
     — a_n+j for 2≤j≤p-1: gcd(a_n+j,a_1): since p|a_n, a_n+j ≡ j (mod p),
       and 0<j<p means p ∤ (a_n+j); since Q={p} is a_1's ONLY prime factor,
       gcd(a_n+j,a_1)=1, illegal (fails the constraint against index 1
       specifically). — by p being a_1's unique prime factor.
     — a_n+p: p | (a_n+p) since p|a_n, so gcd(a_n+p,a_i)≥p>1 for every prior
       i (since p | a_i for every i≤n by the induction hypothesis), legal.
       — by the induction hypothesis extended to a_n+p itself, closing the
       induction.
  3. Conclude a_{n+1}=a_n+p for every n≥1 by strong induction, hence
     a_n=a_1+p(n-1) for all n≥1: T=1, L=p. — by steps 1-2.
  4. Verify by substitution on a small example (e.g. a_1=9=3^2: sequence
     9,12,15,18,21,... matches a_n=9+3(n-1) exactly) as the required
     answer-verification step. — by direct computation.
Key lemmas (claim + mechanism):
  - p is a_1's unique prime factor forces gcd(a_n+j,a_1)=1 for 1≤j≤p-1 —
    because a_1=p^k has no prime factors besides p, and a_n+j is not
    divisible by p in that range (since p|a_n), so a_n+j shares no prime
    with a_1 at all.
  - a_n+p is legal — because p | a_n+p and p | a_i for every earlier i (by
    the induction hypothesis, itself maintained since a_i=a_1+p(i-1) has
    p|a_i for all i≤n), so gcd(a_n+p,a_i) ≥ p > 1 uniformly.
Open gaps: none — this is a complete, self-contained, elementary proof, fully
analogous in structure and rigor to the already-APPROVE'd
`even-seed-literal-periodicity-theorem.md` (which is the p=2, k=1 special
case of this). The builder's job is to write the full rigorous proof and
verify it does not conflict with or duplicate the existing p=2 case (it
should cite/generalize it, not redo p=2 from scratch).
Cases to cover: p=2 (already proved, cite as a corollary/special case, do not
re-derive) vs odd p (the new content; note odd p has p-2 ≥1 intermediate
"illegal" candidates to rule out per step, unlike p=2's zero — this is the
one place the proof genuinely differs in complexity from the p=2 case, not
just notation).
Watch out for: this subfamily (prime powers) is DISJOINT in general from
`even-seed-literal-periodicity-theorem.md`'s scope only when p is odd — when
p=2 the two theorems overlap (both apply, same conclusion); state this
overlap explicitly rather than claiming a strictly larger family without
qualification. Do NOT attempt to generalize beyond a_1=p^k (i.e. to a_1 with
two or more distinct prime factors) — that is exactly the genuinely open
|Q|≥2 general case (concretely confirmed still hard this round by the audit
explorer's a_1=15,45,187,209,247,341 computations); this theorem's scope
must stay exactly at |Q|=1.

n1-periodicity-reconciliation: advance
Target: the problem's actual claim, via the audited, gap-free Master
Conditional Theorem reducing it to exactly H1 (FAH at the terminal
absorption core) ∧ H2 (absorption-chain termination) — unchanged scope from
round 16; this round adds two small, genuine, previously-undocumented
negative/positive findings as permanent record, not a new proof of H1 or H2.
Technique: same conditional-reduction framework (already certified,
independently re-audited airtight this round by the round-18 audit-insurance
explorer — no new gap found in the chain itself).
Skeleton:
  1. (Already complete, unchanged) Master Conditional Theorem: H1 ∧ H2 ⟹
     problem's claim — cite `self-absorbing-core-theorem.md` +
     `literal-n1-periodicity-theorem.md` + `termination-criterion-lemma.md`,
     re-audited gap-free this round.
  2. NEW: document, as a certified negative corollary, that the naive
     generalization "p | a_1 trivializes FAH the way 2 | a_1 does" is FALSE
     for odd p — concrete counterexample a_1=15=3·5 (and a_1=45=3²·5): only
     75% of terms are forced divisible by 3, with a genuine persistent
     period-4 alternation between base types {3} and {5} (fail-indices at
     n=3,7,11,15,... exactly). — by direct computation, already done by the
     round-18 audit explorer; the builder's job is to write this up as a
     rigorous, cited proposition (not just report the numbers), explaining
     WHY p=2 is special: the gap between "definitely illegal" (a_n+1, killed
     by bare consecutive-integer coprimality) and "next multiple of p"
     (a_n+p) contains p-2 intermediate candidates for p≥3 versus 0 for p=2,
     and each intermediate candidate can succeed via a DIFFERENT prime of
     a_1 when |Q|≥2 — this is a genuine, checkable structural explanation,
     not just an empirical observation.
  3. NEW: record that |Q|=2 (a_1=pq, two distinct primes) is NOT a tractable
     general subfamily — the round-18 audit explorer's 36-seed sweep found
     resolution time highly seed-dependent and unpredictable from p,q alone,
     reproducing exactly the workspace's own long-standing canonical hard
     test seeds (187, 209, 221, 247). — by citation, already computed;
     write up as a documented "do not re-attempt as an easy subfamily"
     finding, cross-referencing the memory-rule precedent this generates for
     future rounds.
Key lemmas (claim + mechanism):
  - Odd-Prime Non-Trivialization Proposition: for odd p | a_1 with a_1
    having ≥2 distinct prime factors, FAH does NOT trivialize by the p|a_1
    argument alone — because the p=2 mechanism's proof relies specifically
    on there being ZERO intermediate residues between "illegal by
    consecutive-integer coprimality" and "next multiple of p," a fact unique
    to p=2 (p-2=0); for p≥3 the p-2≥1 intermediate residues genuinely open
    the door to other primes of a_1, which the a_1=15/45 example concretely
    exploits.
Open gaps: H1 and H2 both remain entirely open in general; this round adds no
progress toward either, only two permanent negative/documentation findings
that prevent future rounds from re-attempting these two specific dead-end
generalizations. This approach's own target (the conditional reduction) is
already complete and does not change.
Cases to cover: none beyond documenting the two findings above.
Watch out for: do not let this round's write-up work get mistaken for actual
progress on H1/H2 — the file's Status section must continue to say `partial`
with H1 and H2 both open, exactly as audited; the value of this round's work
is purely in narrowing what future rounds should NOT re-attempt (a genuine,
if modest, form of progress per CLAUDE.md's "record everything" rule).
