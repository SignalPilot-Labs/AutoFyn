## imo-2026-06

**Mandate**: fresh whole-problem framing search for FAH (Full/Symmetric/Cofinite FAH,
equivalently EEA), stuck rounds 6-18 with 19+ confirmed-dead mechanisms. Verdict up
front: **I did not find a genuinely new corridor that survives first-pass scrutiny.**
The most useful output of this pass is a meta-level strengthening of the existing
"class-blindness" obstruction that (if the outliner accepts it) *pre-emptively kills
an entire family the dispatch explicitly asked me to scout* (statistical/probabilistic
methods), saving a round of building it out from scratch — plus one narrower,
honestly-flagged, unproven-but-untried idea (character-sum/finite-Fourier reframing)
that is close enough to already-dead mechanisms that I do not recommend it as a full
build, only as an optional cheap probe.

### What FAH actually says (for calibration)
For a rogue base-type pair (A',B') with Lemma-G witness prime q (first co-occurrence
at n_A<n_B), FAH says: q divides a_n for EVERY n>n_B with ρ(n)=A' (not just some/
infinitely many); Symmetric FAH adds the same on the B'-side. All 19+ dead mechanisms
are different routes to promote "q divides SOME/infinitely many occurrences" (which
is easy, already certified via Lemma G / pigeonhole) to "q divides ALL occurrences."

### Distinct openings considered this pass (each explicitly checked against the
dead-mechanism list before being surfaced)

1. **Algebraic number theory / p-adic completion of a specific number field.**
   Checked whether embedding a_1's factorization in a genuinely different algebraic
   structure (ideal factorization in a number field beyond Z, or working in the
   p-adic completion Z_p for p in the core) adds real leverage. Conclusion: the
   gcd(a_{n+1},a_i)>1 condition is a statement purely about *rational* prime
   divisors; there is no algebraic-number-theoretic structure (no norm form, no
   quadratic/cyclotomic reciprocity, no non-principal ideal) anywhere in the
   problem for a bigger number field to exploit. A p-adic-completion reframing of
   the CORE primes collapses to ordinary CRT/valuation bookkeeping already fully
   used in the certified toolkit (Confined-GCD Lemma, Lemma G, Reduced-Alphabet
   Corollary). **Not a new corridor** — same content, heavier notation.

2. **Generating functions / formal power series.** Tried to see whether the gap
   sequence g_n = a_{n+1}-a_n, or the per-type indicator series f_A(x) =
   sum_{n:τ(n)=A} x^n, satisfies any algebraic or rational functional equation
   that a Skolem–Mahler–Lech- or Christol-type theorem could exploit to force
   periodicity. The recursive definition of a_{n+1} is a *minimum over a
   Boolean-legality predicate*, not a polynomial/linear recurrence — there is no
   candidate functional equation to write down; any attempt to encode the
   min-legal-candidate step as a formal power series operation would need to
   express "gcd(c,a_i)>1 for all i≤n" algebraically, which is exactly the
   per-residue/automaton encoding already tried and killed
   (`subword-complexity-periodicity`, EEA). **Same wall, different notation —
   not surfaced as new.**

3. **Probabilistic / second-moment / Borel–Cantelli.** This is the one I spent
   the most effort trying to make genuinely different from the already-dead
   `sieve-density-exception-bound`. A natural-looking second-moment idea: count,
   over a window [1,N], the number of pairs of same-type occurrences (n,n') with
   ρ(n)=ρ(n')=A' and n,n' not both divisible by q, use Cauchy–Schwarz on the
   indicator vectors to bound this count, and try to force it to 0 for large N
   (i.e., force cofinite absorption via a growth-rate contradiction). **This
   is structurally the same move density-argument-vacuity already refuted**:
   the certified **Selection-Rule Class-Blindness** finding
   (`self-absorbing-by-construction`/`n1-periodicity-reconciliation` lineage,
   round 11) proves the recursive definition only ever consults the *Boolean*
   predicate gcd(c,a_i)>1 — it never references *which* prime realizes the
   shared factor, nor any count/density/second-moment statistic of prior terms.
   Any second-moment or Borel–Cantelli argument necessarily aggregates counts
   over indices to derive a probabilistic/density conclusion, so it inherits
   the identical vacuity: **you cannot derive a class-DISCRIMINATING (which
   specific prime) conclusion from a class-BLIND selection rule, no matter how
   the aggregation is dressed up (density, sieve, second moment, or Fourier —
   see item 4).** I regard this as a genuine (if modest) strengthening of the
   existing obstruction, worth stating explicitly to the outliner so this whole
   *family* — not just its density/sieve instance — is understood as closed.

4. **Finite Fourier analysis / multiplicative character sums mod N (N = product
   of core primes).** The one candidate I could not fully collapse onto an
   already-named dead item by a one-line argument, so I flag it honestly as
   "probably dead by the same class-blindness argument in item 3, but not
   literally identical in form to any of the 19+ named mechanisms." The idea:
   represent residue classes mod N via multiplicative characters χ mod N,
   express the legality predicate for the greedy step via character-sum
   orthogonality (Σ_χ χ(c)χ̄(residue) machinery) instead of a per-prime
   indicator or a raw density count, hoping cross terms between characters
   carry cross-prime information (identity of q) that a plain per-prime
   decomposition or plain density count cannot. On reflection this still
   reduces to a statistic (Fourier coefficient) computed from counts of the
   legality predicate over a window — it is a linear transform of exactly
   the class-blind data in item 3, so any information it could extract is
   already present (or absent) in the raw counts. I predict it dies by the
   same argument but have NOT run it to a proof; if the outliner wants a
   cheap probe before writing this off entirely, this is the only item from
   my search not already on the confirmed-dead list. I do **not** recommend
   building a full approach slug around it without a much stronger reason to
   believe cross terms carry new information — my honest assessment is this
   is a repackaging, not a corridor.

5. **Extremal graph theory on the "resolving-prime" conflict structure.**
   Checked whether a genuinely different graph (vertices = persistent types,
   edges = disjoint rogue pairs, labeled by resolving prime) has extremal
   structure (bounded chromatic number, perfection, Ramsey-type forcing of a
   single dominant label) that would force cofinite single-witness resolution.
   This is closely related to — and I believe strictly subsumed by — the
   already-certified **Hub Singleton Batch Lemma** (round 6,
   `lemmas/hub-singleton-batch-lemma.md`), which already found the relevant
   phenomenon (one prime resolving several simultaneous rogue relationships at
   a "hub" type) and already showed it only explains a minority (3/19) of
   sampled hub instances, with the rest reducing to the open FAH question
   directly. I do not see a genuinely new graph-theoretic invariant beyond what
   that lemma already extracts. **Not surfaced as new** — same wall.

6. **Totally different reformulation of the greedy process itself
   (self-map/reversibility, per corpus).** Searched the crux corpus
   (combinatorics/`processes-and-algorithms`) for a structurally different
   top-level target. Found two candidate techniques, both checked and both
   inapplicable/subsumed:
   - `aimo-0514` ("reversibility forces PURE periodicity, not just eventual"):
     requires the state transition to be *invertible* (each state has a unique
     predecessor) on a finite alphabet. Our process is not reversible in this
     sense — a_{n+1} is a forward minimum over a growing constraint set with no
     canonical inverse map, and the "state" that would need to be finite (the
     full history/legality context) is not literally finite the way a
     3-regular-graph turn is. Inapplicable as stated.
   - `aimo-0916` ("stabilize a descending chain of images of a self-map on a
     finite set, then take the stabilizing power"): this is, in substance,
     already what the certified **Finite Core Theorem** / **Self-Absorbing Core
     Theorem** machinery does (persistent-type stabilization over a finite
     alphabet as the core enlarges). Re-deriving it via this corpus problem's
     framing would not add new content — it is the same finite-state
     stabilization idea already fully exploited in this workspace.

### Cheap-kill candidates
None new. The existing Selection-Rule Class-Blindness argument (item 3 above,
already certified) is itself the sharpest cheap-kill tool in the workspace and I
am recommending its scope be explicitly broadened in write-up (see below) rather
than proposing a new one.

### Candidate technique(s)
None I can recommend as a genuinely new attack with real hope, after this search.
The one item not literally identical to a named-dead mechanism (item 4, finite
Fourier/character sums mod N) is offered only as an optional cheap probe, with an
explicit prediction that it dies by the same argument as items 3/5. If the
outliner wants a slug on it, scope it narrowly and require it to explicitly state
what NEW information a character-sum reformulation could extract that a raw
density count (already proven vacuous) cannot — if no answer, kill pre-build per
the outline-reviewer's usual class-blindness screening protocol (as done for
`sieve-density-exception-bound` in round 11).

### Knowledge-base entries consulted
`knowledge_base.md`'s Number Theory section (Dirichlet's theorem, linear
recurrences) and General Proof Methods / Meta-Strategy sections — none offer a
technique beyond what the workspace has already certified or ruled dead; the KB
is generic and has no entry specific enough to suggest a new mechanism for this
problem (it has no character-sum, generating-function, or ergodic-theory entry at
all — I checked by grep).

### Analogous past problems (cruxes)
Searched `past_crux_moves_database.json` filtered by `subtopic` in
`processes-and-algorithms` (combinatorics), `cyclotomic-and-roots-of-unity`,
`p-adic-valuation`, `orders-and-primitive-roots`, `pigeonhole` (number_theory),
plus keyword search for "periodic"/"gcd"/"greedy"/"sequence" in `technique`/
`how_used`. Best candidates, both ultimately judged NOT genuinely analogous
(reported honestly per the role instructions rather than forced):
- `aimo-0514` (3-regular planar graph traversal, turn-alternation problem) —
  crux "reversibility of a finite-alphabet state transition forces pure
  periodicity." Superficially about forcing periodicity from finiteness, but the
  reversibility hypothesis genuinely does not hold for our greedy process
  (no invertible state transition exists here) — not analogous, do not adapt.
- `aimo-0916` (self-map stabilization on a finite set) — the stabilizing-chain
  idea is already the substance of this workspace's certified Finite Core /
  Self-Absorbing Core Theorems; would not add anything.
- The two `pigeonhole` NT entries (`aimo-0079`, `aimo-0274`, windowed-pattern
  pigeonhole forcing two equal windows) are exactly the Morse–Hedlund/EEA
  mechanism already certified-and-stuck in this workspace
  (`lemmas/eea-implies-periodicity.md`) — confirms, rather than opens, that
  corridor's boundary.
**Conclusion: no genuinely new analogous crux found in the corpus for this
specific crux (single-witness-to-all-occurrences promotion). This is consistent
with the problem's IMO P6/2026 provenance — the corpus is pre-2026 and this
specific hard combinatorial-number-theory mechanism does not appear to have a
close precedent in it.**

### Prior progress
(For context, not re-derived here — see `current.md` rounds 1-18 for full detail,
verified by explorer/outline-reviewer/proof-reviewer chains already.) Three
disjoint infinite sub-families fully solved unconditionally: `2|a_1`; `a_1=p^k`
(any prime p, any k≥1); their overlap is `a_1=2^k`. The general problem is
reduced via the certified Master Conditional Theorem to exactly two named open
hypotheses: H1 (FAH/Symmetric FAH/Cofinite FAH/EEA, the subject of this report)
and H2 (absorption-chain termination / boundedness of N(S_k)), both open. The
Two-Sided Singleton Witness Theorem (round 18) gives a correctly-scoped, not
fully-general, sufficient condition for H1 with its own open existence
hypothesis.

### Dead ends (do not retry — all independently re-confirmed dead by prior
rounds' reviewers, and cross-checked against this round's search, nothing here
resurrects any of them)
Existential/pigeonhole competitor-construction; magnitude-sandwich (Bounded /
Generalized Bounded Gap Lemma linear sandwich, "class-blind"); tautological-
minimality (Minimality Tautology Lemma, scope-narrowed); CRT-glue (Minimal-
Modulus Generalization, ~8 orders of magnitude overshoot); sieve/density
(Density-Argument Vacuity Corollary + Selection-Rule Class-Blindness — see my
item 3 above for why this actually kills a WIDER family than previously
documented); automaton/graph-walk and Morse-Hedlund/subword-complexity (EEA,
proven equivalent-in-difficulty, not a bypass); ultraproduct/compactness;
per-prime indicator decomposition; transfer-operator; LP-duality relaxation;
Central-Sets/idempotent-ultrafilter/Ramsey-recurrence; same-type-triangle
(Same-Type Triangle Vacuity, round 18); the Recruitment-Budget/Fixed-Witness
Divisor-Chain/Successor-Transport-Reduction family (all reduce to the identical
existential-to-universal promotion gap, per Lemma I and its round-9/12
reconfirmations); the Escape-Budget/Growing-Constraint Obstruction family; the
integer-monovariant-difference-identity family (5 candidate statistics, all
dead by the general class-blindness diagnosis).

### Small-case / intuition notes
No new numeric experiments were run this pass (the mandate was framing/terrain,
not computation, and the existing computational record — 0 FAH counterexamples
across ~270+ seeds, cross-validated by 4+ independent implementations — already
strongly supports FAH/Symmetric FAH as TRUE; the obstruction is proof-technique,
not truth). My one substantive addition is the observation (item 3) that the
already-certified Selection-Rule Class-Blindness finding is a general theorem
about the recursive definition's information content, not specific to density
arguments — it applies verbatim to second-moment, Borel–Cantelli, and (by a
one-step-further linear-transform argument) finite-Fourier/character-sum
methods too. I recommend the outliner record this explicitly as a **strengthened,
generalized Class-Blindness Obstruction** (extending the existing lemma's stated
scope from "density/counting statistics" to "any statistic computable as a
function of the window of past legality-predicate outcomes, including linear
transforms thereof") so future rounds do not have to independently rediscover
this for each new statistical variant (density, second-moment, Fourier, LP-
relaxation are now ALL covered by one meta-argument rather than four separate
refutations). This is itself a candidate certifiable corollary, not a proof
attempt — I flag it, I do not develop it, per my role.

**Bottom line for the outliner:** after a genuinely fresh search across algebraic
number theory, generating functions, probabilistic/second-moment methods,
extremal graph theory, and the crux corpus's `processes-and-algorithms`
subtopic, I did not find a corridor that survives contact with the already-proven
obstructions. The most defensible next move is NOT another mechanism attempt in
this family, but either (a) accept the strengthened Class-Blindness Obstruction
as ruling out the entire statistical-method family in one certified lemma
(closing off a large swath of remaining search space in one step, which is
itself useful progress), and pivot fully to constructive/witness-based routes
(the Two-Sided Singleton Witness Theorem's residual existence question, or a
genuinely case-by-case direct-strong-induction generalization of the successful
`2|a_1`/`a_1=p^k` pattern to small |Q|≥2 families one at a time, bypassing FAH
language entirely for those families), or (b) if the run's remaining budget is
limited, formally accept H1/H2 as the terminal open residue and ensure `current.md`
states the conditional result as cleanly and completely as possible as the
run's best deliverable.
