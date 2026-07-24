## imo-2026-06

### Problem (verbatim, re-read fresh)
a_1,a_2,... positive integers >1; a_{n+1} := smallest integer > a_n with
gcd(a_{n+1},a_i)>1 for every i=1..n. Prove ∃ T,L (positive integers) with
a_{n+T}=a_n+L for all n. (task=proof_only, answer_type=none — no numeric
answer to find, pure existence proof.)

### What I did
Deliberately forgot the workspace's specific machinery names and re-derived
the problem's structure from scratch, then checked each fresh idea against
the certified facts (`free-facts-gcd.md`, `persistent-type-pigeonhole.md`,
`finite-core-theorem.md`) to see whether it is a genuinely new corridor or
silently the same wall in new clothes. I also queried the crux corpus
(`divisibility-and-gcd`, `sequences-and-recurrences`, `pigeonhole` subtopics)
for structurally analogous "gcd with all previous terms" / "prime-divides-
infinitely-many-terms" problems, and scanned `knowledge_base.md` end to end
for untried named tools (linear algebra, Zsigmondy, Ramsey/Sylvester,
equidistribution, Hall's theorem).

### Distinct openings considered (with verdict on each)

1. **Periodic-set-intersection reformulation.** Recast legality directly:
   for candidate c, legal-against-{a_1..a_n} ⟺ c lies in ∩_{i≤n} P_i, where
   P_i := {m : gcd(m,a_i)>1} is a union of arithmetic progressions mod
   rad(a_i). This decreasing intersection of "periodic" sets is nonempty by
   the problem's own hypothesis at every step. On inspection this is
   *exactly* what the Finite Core Theorem / Extended Persistent-Type
   Pigeonhole already formalize (their "type" is precisely the residue
   signature of this intersection restricted to a fixed finite prime set).
   The unresolved content — whether the intersection's periodic *structure*
   stabilizes using only finitely many "responsible" indices, uniformly
   across disjoint families — is FAH itself. **Collapses into FAH**, not new.

2. **Direct compactness / König's lemma on "prime profiles".** Attempted
   to view the sequence of profiles ρ_S(n) (S growing) as a path in a
   finitely-branching infinite tree and extract an infinite branch via
   König, hoping this gives eventual determinism for free. Problem: the
   tree here is NOT finitely branching in the needed sense — at each stage
   the "branch" is which NEW prime gets recruited, and nothing yet bounds
   the number of distinct primes that can ever be recruited (this is
   exactly the content the workspace calls the recruitment process,
   already shown by Lemma-I/Growing-Constraint Obstruction to have an
   unboundedly growing witness-index pool). König's lemma needs a uniform
   finite bound on branching to conclude anything nontrivial; without it,
   compactness gives nothing beyond "some infinite branch exists," which
   is just restating that the process doesn't get stuck (already free from
   Free Facts) — it does not give *periodicity*. **No real traction beyond
   what Extended Persistent-Type Pigeonhole already gives; collapses.**

3. **Ergodic / symbolic-dynamics beyond Morse–Hedlund.** The workspace's
   round 12 already carried subword-complexity/Morse–Hedlund (EEA) as far
   as it goes and proved it EQUIVALENT in difficulty to FAH via the
   Confined-GCD Lemma. I looked for a genuinely different ergodic tool —
   e.g. unique ergodicity / minimal subshift arguments, or a
   Furstenberg-style correspondence principle — but these all require some
   invariant measure or amenable-group action on the symbolic system, and
   the gap sequence here has no known algebraic/group structure to anchor
   such a measure; any attempt to manufacture one (e.g. via density of
   gap-values) runs straight into the already-certified **Selection-Rule
   Class-Blindness** fact (the recursion's own legality test is Boolean-OR
   over primes, never a density/measure quantity) — so any measure-theoretic
   argument is class-blind by the same proof the density/sieve family died
   by. **No new opening found here.**

4. **Additive combinatorics (Schur / Freiman-type).** Checked whether the
   gap sequence, viewed as a sumset-type object, could be attacked via
   Schur's theorem (finite colorings of ℤ⁺ admit monochromatic x+y=z) or a
   Freiman-type structure theorem (sets with small doubling are
   near-arithmetic-progressions). Neither has an obvious foothold: there is
   no coloring of ℤ⁺ given a priori (the "coloring" — which prime realizes
   each gcd — is itself the unknown we need to control, not a fixed input),
   and there's no small-doubling hypothesis on the a_n's (bounded gaps give
   linear growth, not sumset control). I could not construct even a
   plausible reduction; this looks like a red herring for this specific
   problem, not merely a hard corridor.

5. **Linear-algebra-over-a-monoid / transfer-matrix.** The natural
   transfer-matrix object would be a finite-state automaton on residues mod
   L reading off gaps — but this automaton's states and transitions are
   already exactly what EEA / the "single-valued successor" framework in
   `eea-implies-periodicity.md` builds, and its well-definedness (the
   matrix entries being unambiguous) is again FAH. A transfer matrix is
   only a bookkeeping device for a *deterministic* finite automaton; it
   cannot manufacture the determinism itself. **Same wall, different
   vocabulary — not pursued further as a build target.**

6. **aimo-0421-style prime-fiber dichotomy (a genuinely under-tried
   crux move — flagging for the outliner, with an honest risk note).**
   Crux `aimo-0421` (divisibility-and-gcd) proves: for an infinite set S
   with gcd(x,y)>1 always, EITHER some prime p divides infinitely many
   elements of S, OR every prime divides only finitely many elements of S
   (in which case one derives a contradiction/structure by picking an
   element coprime to a fixed non-coprime pair). This is a clean
   two-branch dichotomy not phrased anywhere in the current 17 approach
   files in exactly this form (the workspace's persistent-type machinery
   is built on P(a_1) specifically as the finite alphabet, whereas
   aimo-0421's dichotomy is prime-first: ask, for the FULL sequence, which
   primes divide infinitely many terms at all, without privileging a_1's
   own prime set as the base alphabet). Concretely: define
   H := {p prime : p | a_n for infinitely many n}. By Free Facts + the
   Persistent-Type Pigeonhole applied AT EVERY term (not just via Q=P(a_1))
   one can show H ⊇ Q and, in fact, every a_n (not just a_1) has at least
   one prime of H dividing it and infinitely many later terms — this
   reframes the whole problem as "is H finite, and if so does the sequence
   become eventually a union of H-indexed arithmetic-type structure."
   **Honest risk assessment, checked before recommending:** this H is
   almost certainly the same object as the (open) "does recruitment
   terminate" question — H finite is essentially "the recruitment process
   halts" restated at the level of the raw prime set rather than the
   type/residue level. I could not find a proof technique via this
   dichotomy that avoids re-deriving FAH; aimo-0421's own proof for its
   own problem uses a SPECIFIC size bound (S is given as an arbitrary
   infinite set of positive integers under a global pairwise-gcd>1
   hypothesis, no growth constraint) that this problem does not share (our
   a_n's are constrained to be the *minimal* legal choice at each step,
   which aimo-0421's proof never uses). So while H-finiteness is a clean
   reformulation, it does not obviously come with new leverage — flagging
   as a **candidate reformulation to scope carefully, not a working
   bypass**.

7. **Slicker top-level reformulation sidestepping FAH: attack periodicity
   of L·⌊·⌋-density directly via a two-scalar exact identity, à la
   crux `aimo-0134`/`aimo-0678`.** Already tried twice in this workspace
   (`integer-monovariant-difference-identity`, round 14 — 5 candidates,
   all dead by class-blindness; and `scalar-well-ordering-lock-in`, round
   7 — refuted by explicit counterexample at a_1=175). Do not re-attempt
   without a genuinely new statistic that is provably NOT class-blind
   (i.e., is forced by a per-step algebraic identity to encode which
   specific prime recurs, not just that one does) — no such statistic was
   found in this round's search either (I tried, in addition to the 5
   already-dead ones: "running count of distinct primes ever recruited,"
   which is monotone non-decreasing but unbounded a priori — its
   boundedness is literally equivalent to H being finite, i.e. is (†)
   itself, not a bypass of it).

### Candidate technique(s)
None found this round that provably escapes the FAH/EEA wall. The single
concrete new object worth recording is **H := {p : p divides infinitely
many a_n}** (opening 6 above) as an alternative, prime-first packaging of
the same open content — worth having in the outliner's vocabulary in case a
future round finds leverage specific to H (e.g. via a growth/density bound
on Σ_{p∈H} 1/p, though I could not make this go anywhere either — see
below).

### Cheap-kill candidates
- H ⊇ Q is a one-line consequence of Persistent-Type Pigeonhole; not a kill,
  just bookkeeping.
- Checked (numerically, not proof): does Σ_{p∈H,p recruited by index N} 1/p
  stay visibly bounded as N grows on the two mandated seeds (4807, 11305)?
  This would be suggestive (Mertens-style) evidence either way. See
  Small-case notes below — no sharp signal either way at the sizes tested.

### Knowledge-base entries to use
None beyond what's already in play (Pigeonhole/extremal principle, CRT,
Dirichlet in AP — already exhausted per the workspace's own record). Sylvester–
Gallai, Hall's marriage theorem, quadratic-form/eigenvalue tools, Zsigmondy,
and the equidistribution/three-gap entries were all checked and have no
plausible foothold on this problem (no polynomial values, no exponential
recurrence a^n±b^n for Zsigmondy, no bipartite matching structure for Hall,
no irrational-rotation structure for three-gap/equidistribution).

### Analogous past problems (cruxes)
- `aimo-0421` (divisibility-and-gcd): "gcd(x,y)>1 for all pairs in an
  infinite set ⟹ dichotomy on whether some prime divides infinitely many
  elements" — the closest structural analogue found (Free Facts is
  literally this hypothesis). Its crux move (opening 6 above) is a genuine
  hint but its proof technique does not obviously transfer, since it never
  uses a minimality/greedy-construction hypothesis the way this problem's
  a_{n+1} does.
- `aimo-0212` (divisibility-and-gcd / modular-arithmetic-and-CRT): "prime
  divisors of a polynomial's values lie in a fixed finite set ⟹ polynomial
  is essentially monomial" — structurally distant (this problem has no
  polynomial), but its PATTERN ("finite prime-divisor set forces rigid
  structure") is the same shape as the Finite Core Theorem already
  certified here; not a new hint, confirms the workspace is already using
  the standard version of this pattern.
- `aimo-0447` (divisibility-and-gcd / size-bounding-and-descent): grid-of-
  primes encoding of "gcd(a+i,b+j)>1 for all i,j," with a prime-density
  (Σ1/p, Σ1/p²) counting bound forcing large primes to dominate most cells.
  Structurally close to the already-dead `sieve-density-exception-bound`
  and `density-argument-vacuity-corollary` (round 11) — those already show
  this counting-style argument is class-blind for THIS problem's
  legality rule; aimo-0447's setting differs in a load-bearing way (its
  hypothesis is a fixed FINITE grid with a FIXED pair a,b, not an infinite
  greedily-constructed sequence), so the density bound there has no
  analogue to import.
- No crux found that resembles the actual open gap (promoting "a prime
  exists linking a pair" to "the SAME prime links ALL sufficiently late
  occurrences of both persistent types simultaneously").

### Prior progress
See `current.md` Status (round 14): FAH/Symmetric FAH/Cofinite FAH/EEA is
the sole open primary crux, 16 confirmed-dead mechanisms, 9 consecutive
rounds (6–14) stuck on the same "existential-to-universal promotion" wall.
Secondary n=1 gap has one fully-certified conditional theorem
(Self-Absorbing Core Theorem, `lemmas/self-absorbing-core-theorem.md`)
narrowing it to two sub-gaps: (a) existence/termination of a self-absorbing
core S*, (b) whether N(S*)=0.

### Dead ends (do not retry)
All 16 named mechanisms in `current.md`'s round-14 Status header (existence/
pigeonhole, magnitude-sandwich, tautological-minimality, CRT-glue,
sieve/density, automaton/graph-walk, Central-Sets/Ramsey,
exact-valuation-monovariant, integer-monovariant-difference-identity — see
that file for the full per-mechanism reasons). This round additionally
rules out, with reasons (not previously written down explicitly in this
form): periodic-set-intersection reformulation (opening 1), König's-lemma/
compactness on prime profiles without a branching bound (opening 2),
ergodic/unique-measure arguments beyond Morse–Hedlund (opening 3),
Schur/Freiman-type additive combinatorics (opening 4 — no foothold at all,
not just hard), transfer-matrix/linear-algebra-over-a-monoid (opening 5),
and a "running count of distinct recruited primes" monovariant (opening 7,
literally equivalent to H-finiteness = (†) itself).

### Small-case / intuition notes (conjecture only, not proof)
- Quick numeric check (Python, a_1 = 4807 and 11305, first ~2500 terms,
  reusing the workspace's already-reported factorizations rather than
  re-deriving from scratch since my time budget went to the structural
  search above): the number of *distinct* primes ever appearing as a
  factor of any a_n up to index 2500 is small and appears to plateau
  early relative to n (consistent with H being finite on these seeds, but
  this is exactly the kind of "0 counterexamples in finitely many seeds"
  evidence the workspace has already collected extensively for FAH itself
  — it is not independent evidence of anything new).
- My overall assessment, after actively trying to break the plateau from
  a "start completely fresh" posture: the wall is structural, not a
  failure of imagination in prior rounds. Every route I found either (i)
  re-derives the same "some witness prime exists per pair, but nothing
  forces universality across ALL sufficiently late occurrences
  simultaneously" content, or (ii) is class-blind by the same
  Selection-Rule Class-Blindness argument already certified. The one
  genuinely fresh vocabulary item (H := primes dividing infinitely many
  terms, opening 6) is worth recording for the outliner but I could not
  turn it into a working technique myself, and I flag explicitly that it
  is very likely provably equivalent to (†) rather than a bypass — an
  outliner picking it up should first check that equivalence rigorously
  (one paragraph) before investing a build round in it, to avoid a 17th
  "confirmed-dead-but-in-new-clothes" mechanism.
