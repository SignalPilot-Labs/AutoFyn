## imo-2026-06

### Context recap (do not re-derive)
Unconditionally certified and reusable by every approach below (see `results/imo-2026-06/lemmas/`):
Free Facts, Bounded/Generalized Bounded Gap Lemma, Persistent-Type Pigeonhole,
Bounded/Generalized Bounded Witness Lemma (+ Recruitment Corollary), Finite Core
Theorem, Extended Persistent-Type Pigeonhole, Canonical-Refinement Lemma,
F_A∩F_B≠∅, Lemma G (Extended Earliest-Witness Intersection), Critical Prime
Dichotomy (Lemma H), Monotonicity of Resolution, Same-Side Ordering, Projection
Lemma, Collateral-Safety Theorem, Hub-Singleton-Batch Lemma. Consequence: gap (†)
is reduced EXACTLY to base-type-pair-level termination over a fixed finite set of
≤ C(|𝒫|,2) pairs (open(k) non-increasing, Collateral-Safety), which in turn (per
`covering-system-construction` Step 8.5) reduces to proving, for every currently
open pair, the **Full-Absorption Hypothesis (FAH)** and **Symmetric FAH**: the
Lemma-G prime q for a rogue instance (A',B') with witnesses n_A<n_B divides
*literally every* later A'-occurrence (FAH) and *literally every* later
B'-occurrence (Symmetric FAH) — not just infinitely many. 0 counterexamples across
every seed tested by 5 independent implementations across 6 rounds; 3 proof
mechanisms (Lemma H branch analysis, inductive chaining, exchange/minimality) are
proved dead via Lemma I. Do NOT re-attempt: Universal Singleton Hypothesis, "V=∅
always", PUCL, universal-glue-prime/cost≤1, reversible-transition-map,
well-ordering descent on witness-index/set-size, recruitment-round-charging's 3
candidates, competitor-construction/minimal-counterexample on FAH via Lemma F/
Lemma I family (all definitively dead per current.md's Rules).

---

greedy-exchange-cost-potential: revise
Target: the whole problem — eventual periodicity a_{n+T}=a_n+L for all n — via
this approach's owned sub-target FAH, combined with the certified reduction chain
above and `covering-system-construction`'s Step 8.5 finish.
Technique: a genuinely NEW mechanism not covered by Lemma I's diagnosis — instead
of composing existential per-occurrence facts (which Lemma I proves cannot yield
an identity), attack FAH via (a) a canonical, uniquely-determined prime obtained
from a SIZE-of-intersection fact between two DIFFERENT witnesses (not an
existential "some prime works" statement), and (b) NEGATIVE information from
illegality certificates of skipped candidates ("blocking data"), which no
certified tool currently uses at all.
Skeleton:
  1. Fix rogue instance (A',B'), earliest witnesses n_A<n_B (WLOG; symmetric case
     n_B<n_A is identical with roles swapped). Let F' := P(a_{n_B})\S₀, F'' :=
     P(a_{n_A})\S₀ — both finite, nonempty, F'∩F''≠∅ by the certified Lemma G.
  2. NEW STEP (open, primary target 1): prove **Two-Witness Intersection
     Uniqueness**: |F'∩F''| = 1. Empirically 34/34 confirmed this round across 10
     seeds including the critical |F'|=2 seed a_1=11305 (F'={11,103}, F''={11},
     intersection={11}) — by `math-explorer-density.md`. Proof strategy to
     attempt: apply the certified Critical Prime Dichotomy (Lemma H) to the
     EARLIEST witness a_{n_B} itself (not a hypothetical failing tail-occurrence,
     which is where all 3 dead mechanisms applied it) for EACH candidate prime
     p ∈ F'∩F'' simultaneously. If |F'∩F''| ≥ 2 with primes p₁≠p₂, Lemma H gives,
     for each p_i, either (branch a) stripping p_i from a_{n_B} drops below
     a_{n_B-1}, or (branch b) some earlier index i has P(a_i)∩P(a_{n_B})={p_i}
     exactly. Use the EARLINESS of n_B (it is the minimal index with base type
     B, not just any index — this is stronger data than Lemma H alone uses) to
     argue the two branch-b witnessing indices i_1, i_2 (if both occur) cannot
     be distinct without contradicting minimality of n_B itself (a genuinely new
     joint argument: apply minimality not to a hypothetical failing A'-occurrence
     but to n_B's own status as earliest B-occurrence, i.e. show that if
     i_1 < i_2 < n_B both critically witness distinct primes against a_{n_B}, one
     of them already forces an earlier index with base type B, contradicting
     n_B's minimality). NOTE: this is NOT a repeat of Attempt 2a/2b/2c — those
     attacked minimality of a hypothetical failing successor; this attacks
     minimality of the FIXED earliest witness a_{n_B} against TWO simultaneous
     primes, which Lemma H's proof never analyzed (its round-5 statement only
     ever discusses a single q').
  3. Given step 2 (call the unique element q), prove unconditionally (should be
     free from the certified Recruitment Corollary): for n>n_B with ρ(n)=A',
     D(n) := P(a_n)∩F' is nonempty. Since F' is a FIXED finite set, D(n) ranges
     over ≤ 2^{|F'|}-1 possible nonempty subsets of F' — apply the infinite
     pigeonhole principle to get some subset D* ⊆ F' occurring as D(n) for
     infinitely many A'-occurrences n. This step is a straightforward corollary
     of already-certified tools (Generalized Bounded Witness Lemma's Corollary +
     pigeonhole) — no new gap, but state it explicitly since no prior file has.
  4. NEW STEP (open, primary target 2, the hard one): prove **Blocking-Data
     Bridging Lemma**: q ∈ D(n) for EVERY n>n_B with ρ(n)=A' (not just
     infinitely often as step 3 gives). Mechanism to attempt: for a hypothetical
     n with q ∉ D(n), consider the integer c := a_n − (a_n mod q) rounded up to
     the next multiple of q that is ALSO legal against a_1,...,a_{n-1} (if such c
     exists and c<a_n, greedy minimality is directly violated — a genuinely
     different competitor than Lemma F/I's magnitude-scale competitors, since c
     is constructed by ADJUSTING a_n's own residue mod q rather than by taking a
     fresh multiple of a large modulus). If no such c<a_n exists, EVERY
     q-multiple below a_n must be illegal against SOME earlier index — extract,
     for each of the finitely many q-multiples in (a_{n-1}, a_n), its specific
     blocking index (the "blocking data" per `math-explorer-minimality.md`
     opening 3) and show these blocking indices are confined to the finite core
     S₀'s canonical witnesses (using the Finite Core Theorem's own construction),
     then derive a contradiction from THEIR fixed factorizations (each already
     known explicitly) failing to block a specific q-multiple candidate that
     step-3's D* analysis guarantees exists. This is the genuinely new mechanism
     requested: it uses NEGATIVE illegality information, which Lemma I's
     diagnosis explicitly does not cover (Lemma I only inspected Free Facts,
     Generalized Bounded Witness, Gap Lemmas, Critical Prime Dichotomy — all
     positive/existential tools).
  5. If step 4 succeeds: FAH is proved (q ∈ D(n) for all such n means q | a_n).
  6. If step 4 stalls: document the precise obstruction with the same rigor as
     Lemma F/Lemma I (do not silently drop it) so the population does not repeat
     it.
Key lemmas (claim + mechanism):
  - Two-Witness Intersection Uniqueness (|F'∩F''|=1) — because Lemma H applied
    jointly to the FIXED earliest witness a_{n_B} against two candidate primes
    creates a minimality conflict with n_B's own earliest-occurrence status
    (new: prior uses of Lemma H never combined two primes against one fixed
    witness's own minimality).
  - Divisor-Restricted Pigeonhole (D(n) nonempty, finite range) — because F' is
    a fixed finite set (Generalized Bounded Witness Lemma Corollary) and
    pigeonhole over a finite powerset.
  - Blocking-Data Bridging Lemma (q ∈ D(n) for ALL n, not just ∞-often) —
    because every skipped q-multiple below a_n has a blocking index confined to
    the finite core's canonical witnesses, whose factorizations are already
    explicitly known and (conjecturally) cannot simultaneously block all
    q-multiples while D* recurs.
Open gaps: step 2 (Two-Witness Uniqueness) and step 4 (Blocking-Data Bridging) —
both genuinely new, unproved, this round's primary targets.
Cases to cover: n_A<n_B (worked) and n_B<n_A (symmetric, same argument with roles
of A',B' swapped — must be checked, not just asserted).
Watch out for: (i) do NOT let step 4's competitor construction collapse back into
Lemma F's magnitude-scale competitor (a "c<a_n legal q-multiple" must be argued to
exist or be blocked using SPECIFIC finite-core factorizations, not a generic
modulus bound, or this repeats the dead Attempt 2c); (ii) step 2's joint-Lemma-H
argument must actually produce a contradiction, not just two coexisting branch-b
facts — check this carefully, since Lemma H's branches are not exclusive (per its
certified, corrected statement, only "at least one" holds) so two primes each
independently satisfying branch (b) via DIFFERENT indices is a priori consistent
unless the earliness of n_B is actually used to force a relationship between the
two indices.

---

covering-system-construction: revise
Target: the whole problem's claim, via the already-proved-conditional Step 8.5
finish (Symmetric FAH for every open pair ⟹ termination in one further round ⟹
CRT+cyclic-pigeonhole ⟹ eventual periodicity), now attacking the Symmetric-FAH
half of the open hypothesis plus the untouched secondary n=1 gap.
Technique: same Two-Witness-Singleton-anchored mechanism as the sibling approach
(import q, once/if `greedy-exchange-cost-potential` certifies Two-Witness
Intersection Uniqueness — coordinate, do not re-derive), applied symmetrically to
the B'-side; plus a fresh direct-computation argument for the secondary gap.
Skeleton:
  1. Import the certified reduction chain (Projection Lemma, Collateral-Safety
     Theorem, Step 8.3's open(k) framework, Step 8.5's conditional finish) — all
     already proved, no re-derivation needed.
  2. Import q (Two-Witness Intersection Uniqueness) once available from
     `greedy-exchange-cost-potential`; if not yet certified when this file is
     built, state the symmetric target conditionally on it and proceed (do not
     block on the sibling's timeline).
  3. NEW STEP (open, primary target): prove **Symmetric FAH** — for m>n_A with
     ρ(m)=B', q | a_m — via the mirror of the sibling's Divisor-Restricted
     Pigeonhole + Blocking-Data Bridging mechanism, with F'' (not F') as the
     fixed reference finite set and B'-occurrences as the index family. Because
     the construction of q via F'∩F'' is already symmetric in A'/B', this
     argument SHOULD be a direct mirror — but explicitly check the one place
     symmetry could break: B'-occurrences strictly between n_A and n_B are
     IMPOSSIBLE (n_B is B's own earliest occurrence, so nothing to check there),
     but B'-occurrences after n_B face the same "was n_B chosen minimally
     against a JOINT two-prime constraint" question as step 2 of the sibling
     approach — verify the same joint-Lemma-H argument transfers without
     modification (it should, since it was stated about a_{n_B} intrinsically,
     not about which side is "A" vs "B"), and flag explicitly if it does not.
  4. Combine (Step 8.5, already proved) FAH + Symmetric FAH ⟹ full termination
     ⟹ eventual periodicity a_{n+T}=a_n+L for n beyond a finite threshold N₀.
  5. NEW STEP (open, secondary target, untouched since round 1): extend to
     literal periodicity from n=1. Mechanism to attempt: since S₁ (the final,
     terminal core after all recruitment) is finite and explicit, and a_1,...,
     a_{N₀} are a FINITE, explicitly computable prefix, directly verify (by
     finite computation on the concrete recursion, not by a general argument)
     that the same period (T,L) — or an integer multiple of it — already
     applies from n=1, using that any prefix of a periodic-from-N₀ sequence can
     be folded into the period by taking T' := T·(smallest k making N₀≤k·T) and
     checking the finite prefix matches a_n = a_{n+T'} − L' for the
     correspondingly scaled L'. This is a finite check + one algebraic
     lcm-scaling argument, not a new structural fact — flag honestly if the
     finite check fails to close (e.g. if early terms are NOT congruent to any
     later residue class, which would require a genuinely different argument,
     not yet explored by any approach in 6 rounds).
Key lemmas (claim + mechanism):
  - Symmetric FAH — because the same q from Two-Witness Intersection Uniqueness,
    by symmetry of its construction (F'∩F'' is symmetric in the two witnesses),
    should satisfy a mirrored Blocking-Data Bridging argument on the B'-side;
    the one genuine asymmetry to check is whether n_B's OWN minimality (used to
    derive q in step 2 of the sibling file) transfers cleanly to statements
    about B'-occurrences AFTER n_B (not just at n_B itself).
  - Literal n=1 periodicity — because the finite prefix a_1..a_{N₀} plus a
    known-eventual period (T,L) can be checked directly by finite computation
    and folded in via period-scaling (T'=k·T for k making the prefix fit), IF
    the finite prefix's residues actually align with the eventual cycle (this
    alignment is the actual open content, not a formality).
Open gaps: step 3 (Symmetric FAH, shared crux with sibling) and step 5 (n=1
literal extension, genuinely new target, never attempted by any prior round).
Cases to cover: none beyond the n_A<n_B / n_B<n_A symmetry already handled by
Step 8.5's case analysis.
Watch out for: do not claim Step 8.5's finish is "done" once FAH+Symmetric FAH
are proved without ALSO closing step 5 — per CLAUDE.md's rigor rules, "solved"
requires the literal claim ("for every positive integer n"), and this gap has
sat untouched and unflagged as urgent since round 1; do not let it become an
overclaim once the primary crux falls.

---

scalar-well-ordering-lock-in: new
Target: the whole problem's claim, via a genuinely different PROOF STYLE (an
exact algebraic gcd-recursion / fixed-point identity, imported from crux
aimo-0678's technique) rather than the existential/combinatorial pigeonhole
machinery (Lemma G/H/I family) that all other live approaches share — per
Lemma I's own diagnosis that the missing ingredient is exactly "a mechanism that
converts an existential fact into a uniform identity," which an algebraic
fixed-point recursion is designed to do and no certified tool currently attempts.
Technique: transplant aimo-0678's two-scalar mechanism (a non-increasing scalar
witness hits a floor by well-ordering; a SECOND, coupled scalar is then shown
CONSTANT by an exact algebraic/gcd identity, not by pigeonhole) onto this
problem's already-certified finite-index-set structure (open(k) over base-type
pairs), replacing the pigeonhole-only "|open(k)| non-increasing" argument with an
attempt at an exact recursive identity for a per-pair "compatible-part" scalar.
Honest caveat (from `math-explorer-fresh.md`): no concrete scalar has been
verified to work; this is a technique import, not a completed lemma — the
skeleton below gives a specific, checkable starting candidate rather than a vague
direction, so the builder has real material to attempt or falsify quickly.
Skeleton:
  1. Import for free (no new work): Free Facts, Finite Core Theorem, Extended
     Persistent-Type Pigeonhole, Projection Lemma, Collateral-Safety Theorem —
     giving the fixed finite index set of base-type pairs and open(k)
     non-increasing (all already certified/proved unconditionally).
  2. Fix a total order on the finitely many base-type pairs (e.g. lexicographic
     on (min(A),min(B))). At each recruitment stage k with open(k)≠∅, define the
     SCALAR w_k := a_{n_B} where (A,B) is the LEXICOGRAPHICALLY FIRST pair in
     open(k) and n_B is its earliest-B-occurrence witness index (well-defined,
     positive integer, since open(k)⊆ the fixed finite pair set).
  3. NEW STEP (open, target 1): show w_k is well-defined and finite at every
     stage (should be free — open(k) finite, n_B always exists by Persistent
     Pigeonhole) — no new content, just bookkeeping to set up steps 4-5.
  4. NEW STEP (open, target 2, the genuinely new mechanism): define the coupled
     scalar g_k := the product over all primes q_1,...,q_j RECRUITED so far
     (via Lemma G's Corollary, at stages 1..k-1) of q_i^{v_{q_i}(a_{n_B})} — i.e.
     the "recruited-prime part" of a_{n_B}'s factorization. Attempt to derive an
     EXACT recursive identity g_{k+1} = f(g_k, w_k, w_{k+1}) analogous to
     aimo-0678's Claim 2 (there: g_{n+1} = gcd(w,s_{n+1}) computed exactly from
     g_n and the recursion's defining equations, no existential quantifier) —
     concretely, try to show that recruiting the Lemma-G prime q_k against the
     lexicographically-first open pair forces q_k | a_{n_B'} for the NEXT stage's
     lexicographically-first witness too, via a DIRECT algebraic consequence of
     the greedy minimality equation defining a_{n_B'} (not via FAH's existential
     "eventually all occurrences" claim, but via a one-step recursive
     substitution, mirroring how aimo-0678's g_{n+1} is computed directly from
     g_n and the problem's defining equations rather than proved by induction
     over infinitely many terms).
  5. If step 4 succeeds: g_k is eventually constant (bounded increasing sequence
     of divisors of a fixed integer product, or an exact recursion showing no
     further growth), giving a finite stage K at which open(K)=∅ WITHOUT
     needing FAH's full "every later occurrence" claim — a genuinely different
     (and if it works, more economical) route to the same conclusion as
     Step 8.5.
  6. If step 4 does not yield a clean identity (the likely outcome, per the
     fresh explorer's honest caveat that the direct transplant "does not
     obviously exist" since this problem's legality depends on ALL prior terms
     simultaneously, not aimo-0678's one-step Markov recursion): fall back to
     documenting PRECISELY where the algebraic-identity mechanism breaks (e.g.,
     if the recursion for a_{n_B'} unavoidably reduces to an existential
     "some legal successor" statement with no closed form) — this negative
     result is valuable and should be recorded with the same rigor as Lemma F/
     Lemma I, since it would show even the algebraic-identity STYLE (not just
     the four previously-diagnosed tools) cannot bypass FAH, strengthening
     Lemma I's diagnosis rather than just re-confirming it via a 4th attempt.
  7. Given step 4/5 (or, failing that, importing FAH+Symmetric FAH from the
     sibling approaches once proved), finish via the certified CRT+cyclic-
     pigeonhole step (Step 5 of `covering-system-construction`) and address the
     secondary n=1 literal-periodicity gap (see the sibling approach's Step 5).
Key lemmas (claim + mechanism):
  - w_k well-defined (free, bookkeeping) — because open(k) is finite (Collateral-
    Safety) and every base type has an earliest occurrence (Persistent Pigeonhole).
  - g_k eventual constancy via exact recursion (open, the genuinely new target) —
    because recruiting a Lemma-G prime against the lex-first open pair is
    hypothesized to force it into the NEXT stage's lex-first witness via a
    direct substitution in the greedy-minimality defining equation, not an
    inductive/existential argument — UNVERIFIED, primary target of this
    approach.
Open gaps: step 4 entirely (does the recursion exist at all — this is the
approach's whole content) and, downstream, step 7's secondary n=1 gap (shared
with the sibling approach — coordinate, do not duplicate work; whichever
approach proves it first should be cited by the other).
Cases to cover: none beyond the lexicographic tie-breaking rule in step 2 (must
be well-defined — check no two pairs can tie under the chosen order, or specify
a deterministic tiebreak).
Watch out for: (i) per the fresh explorer's explicit warning, do NOT force a
literal transplant of aimo-0678's exact formulas (w_n=min{m≥a_n:m∤s_n},
g_n=gcd(w,s_n)) — those are specific to a one-step Markov recursion this
problem's "gcd against ALL prior terms" rule does not have; only the TWO-SCALAR
STYLE (monotone witness + algebraically-locked companion) transfers, and even
that is unverified; (ii) if step 4 turns out to be secretly equivalent to FAH
(recruiting q into a_{n_B} "forcing" it into the next witness IS essentially a
disguised form of Symmetric FAH), that is an acceptable and useful outcome (a
new proof route to the same fact) but must be flagged honestly as such, not
presented as an independent bypass; (iii) this approach must not silently
duplicate the sibling approaches' Blocking-Data/Two-Witness-Singleton work —
its distinguishing content is the ALGEBRAIC RECURSION attempt in step 4, not a
second copy of the combinatorial mechanism.

---

covering-system-construction (alternate note, not a separate slug): if
Two-Witness Intersection Uniqueness (sibling's step 2) fails to be proved this
round, `covering-system-construction`'s step 3 (Symmetric FAH) should fall back
to attempting Symmetric FAH directly from FAH alone (if FAH is proved without a
canonical q, e.g. via some other route) rather than blocking entirely on the
sibling's exact mechanism — record this contingency in the built file so a
CHANGES REQUESTED outcome on the sibling does not automatically stall this file
too.
