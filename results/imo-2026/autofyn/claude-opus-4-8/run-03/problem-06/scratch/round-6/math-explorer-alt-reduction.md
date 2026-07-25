## imo-2026-06 — Lens: Route (iii), alternative TOP-LEVEL reduction sidestepping 𝓐_∞

### Summary verdict up front
After systematically constructing and stress-testing five candidate alternative
reductions, **none of them is a genuine bypass**: each either (a) is a bare
relabeling of the minimal-support antichain 𝓐_∞ / admissible-set A already in
use (isomorphic, not independent), or (b) has ALREADY been tried under a
different name and PROVEN to collapse verbatim onto the same crux (certified
in the run's own history), or (c) is mathematically inapplicable to this
problem's unbounded-ground-set structure. I report all five honestly, flagged,
plus one genuinely fresh (unattempted) idea with its likely fork already
visible, and the corpus search results.

### Distinct openings surveyed within this lens

1. **Hypergraph/transversal duality restatement.** Model 𝓕={F_n} as hyperedges
   of a hypergraph on the vertex set of primes; "c admissible" ⟺ F(c) is a
   transversal (hits every hyperedge). **VERDICT: NOT independent** — this is
   literally the certified `no-transient-fixed-successor` framing (A = set of
   transversals, 𝓐_∞ = ⊆-minimal hyperedges) under new vocabulary. Zero new
   leverage; flagging so the outliner does not waste a build slot re-deriving
   what's already certified.

2. **Sieve/complement viewpoint.** Complement(A) = {c : ∃F∈𝓐_∞ with
   gcd(c,∏F)=1} = a union, over minimal supports, of "F-avoiding" residue-class
   unions (an Eratosthenes-style sieve). **VERDICT: NOT independent** — proving
   Complement(A) is eventually a finite union of residue classes is the exact
   complement of proving A is (equivalently Π finite); no extra structure is
   exposed by dualizing to the complement, and any finiteness argument on the
   sieve needs the same fact about the sieving family 𝓐_∞.

3. **Gap-word / finite-state automaton on the value stream.** Since gaps
   d_n=a_{n+1}-a_n lie in the FIXED finite alphabet {1,...,M}, M=rad(a_1)
   (certified L2, independent of Π!), one might hope a finite-state
   description of d_n exists WITHOUT first pinning down Π. **VERDICT: ALREADY
   TRIED AND PROVEN TO COLLAPSE** — this is exactly R3's
   `value-stream-double-freeze` pole; its certified K-equiv result shows a
   finite-state deterministic value-stream automaton exists **iff** Π is
   finite. So the bounded-alphabet-of-gaps fact, while true and cute, gives
   no independent leverage — do not re-seed.

4. **Intersecting-family (EKR-type) extremal bound.** Classical
   Erdős–Ko–Rado-style bounds on intersecting families require a FIXED,
   bounded ground set (bound size k of each set, ground set n). Here the
   "ground set" (primes appearing) is a priori unbounded and each F_n can have
   unbounded cardinality/magnitude, so EKR-style counting bounds don't
   transplant — no version of Sperner/EKR gives an a₁-only bound on Π or
   |𝓐_∞| directly. One genuinely CORRECT small fact from this angle worth
   recording: **if Π were finite, then 𝓐_∞ (an antichain of nonempty subsets
   of a finite ground set Π) is automatically finite by Sperner's theorem** —
   so "Π finite ⟹ 𝓐_∞ finite" is elementary and free. But the converse/needed
   direction (Π finite in the first place) is exactly the open crux; Sperner
   gives no traction on that direction. Flag: this is a clean equivalence
   restatement (Π finite ⟺ 𝓐_∞ finite, since 𝓐_∞ finite trivially forces Π
   finite too as Π is a finite union of finite sets), NOT a bypass — it is
   consistent with, not different from, the already-certified E4 form.

5. **Generating-function / Dirichlet-density model of the whole sequence.**
   Considered whether ∑1/a_n or a Dirichlet series encoding of A could pin
   down periodicity directly. **VERDICT: inapplicable** — periodicity is an
   exact combinatorial/structural claim (a_{n+T}=a_n+L for literally every n),
   not an asymptotic-density claim, and R5 already certified that density(A)
   can converge to a fixed positive limit even while Π is infinite (the
   {p*,q_k} obstruction family). Any density-only argument is already a
   forbidden lever per the Rules; a generating-function repackaging inherits
   the same vacuity.

### One fresh (unattempted-in-this-exact-form) idea, with its visible fork flagged

6. **Reverse the aimo-0224 construction mechanism.** The corpus problem
   aimo-0224 (ISL-style: "does there exist a sequence with a_m,a_n coprime iff
   |m-n|=1?") constructs an explicit prime-to-index covering I_n with
   `|I_n| = Θ(log n)` (each I_n must serve arithmetic-progression-indexed
   disjointness/intersection roles growing with n). One could ask: does the
   PAIRWISE-INTERSECTING requirement (certified L4) on our F_n, together with
   the greedy MINIMALITY of a_{n+1} (which keeps ω(a_n) essentially bounded /
   slow-growing, since a_n=Θ(n) by L2 forces log a_n = O(log n) and hence
   ω(a_n)=O(log n / log log n) by trivial bounds), force a growth-rate clash
   with the index-covering-density needed to keep infinitely many DISTINCT
   minimal supports alive? This is a genuinely different kind of argument
   (asymptotic prime-count-per-term vs. covering-density-of-constraints,
   density in the "index" direction rather than the "prime magnitude"
   direction used by every prior pole). **However**, tracing it two steps
   ahead: to turn "growth-rate clash" into a real contradiction you would need
   to lower-bound how many DISTINCT minimal supports must be "alive" (not yet
   fully retired) at index n as a function of n — and the only way found so
   far to make "alive" precise routes straight back to either (a) bounding
   the realizer value/product of a support (forbidden, JSC/R5) or (b) the
   anchor-fiber partition (forbidden, Collapse theorem/R4). I could not find a
   way to state "index density of active constraints" that avoids reintroducing
   ∏G or the anchor partition. Flagging this as the single most promising
   UNEXPLORED angle but with a visible fork into forbidden territory — worth
   one exploratory slot ONLY if the outliner/builder can find a way to bound
   the count of live constraints by n WITHOUT going through ∏G, p_max, |t-t'|,
   or the anchor partition (e.g., a genuinely new counting scheme on the
   *number of distinct terms consumed before a support "closes"*, not on
   prime magnitude) — but I could not certify that such a scheme exists.

### Candidate technique(s)
None of the surveyed reframings is independently load-bearing; the only
partially-fresh angle (6) is speculative and its natural development forks
back into forbidden levers. Sperner's theorem (elementary, KB-adjacent) gives
a free equivalence 𝓐_∞ finite ⟺ Π finite, useful only as bookkeeping.

### Cheap-kill candidates
None obvious specific to this lens — all five standard reframings die on
structural/logical grounds (isomorphism or certified collapse), not on a
computation that could be cheaply falsified; I did not find a numeric
cheap-kill worth running since the negative results (2,3,5) are already
certified proofs from prior rounds, and (1),(4) are elementary logical
observations, not conjectures needing a numeric check.

### Knowledge-base entries to use
- "Order of an element / periodicity of sequences mod m" (KB) — already the
  basis of the Reduction Lemma the run has certified; not new leverage for a
  bypass.
- No KB entry on covering systems, sieve theory, or hypergraph transversals
  was found beyond the generic divisor-analysis / pigeonhole entries already
  in use by the leader approach.

### Analogous past problems (cruxes)
- `aimo-0224` (ISL, "sequence with a_m,a_n coprime iff |m-n|=1?") —
  number_theory, `divisibility-and-gcd`. Genuinely structurally close (same
  prime-to-index assignment mechanics, pairwise-(non)coprimality via disjoint
  prime sets) but it is an EXISTENCE/construction problem, not a periodicity
  proof, and its solution's covering index-density (|I_n|=Θ(log n)) is the
  seed for fresh idea (6) above — worth reading in full if (6) is picked up,
  but it does not hand over a ready-made lemma.
- `aimo-0678` (already used, R2/R3) — same top-level claim shape but its
  two-stage monovariant mechanism is already certified to fail here (frozen
  by the {p*,q_k} obstruction).
- `aimo-0648` (algebra, sequences-and-recurrences, "eventually constant
  floor-average recurrence") — **NOT analogous**: its "confine to bounded
  interval via order-statistic invariant" mechanism needs the sequence to be
  BOUNDED (min/max preserved), but our a_n→∞ strictly increasing; this
  boundedness trick has no foothold here. Recording so no future round wastes
  a slot on it.
- `aimo-0212` ("finitely many prime divisors of polynomial values ⟹
  polynomial is a monomial") — superficially resembles a "finite prime
  alphabet ⟹ rigid structure" shape but its mechanism (Fermat's little
  theorem lifting via rad(n) self-composition) has no analogue in a
  gcd-greedy-selection setting; **not transplantable**, noting for
  completeness only.

### Prior progress
Unchanged from the run's certified state: whole problem reduced (no-transient,
all n≥1) to the single Finite-Alphabet crux (Π finite ⟺ 𝓐_∞ finite by
Sperner, ⟺ E4 bounded cardinality sup|G|<∞, ⟺ E5″ p_max>∏G/a₁ on the
∏G≥a₁ subclass, with ∏G<a₁ subclass fully closed). See `current.md` and
`lemmas/*.md` for the full certified chain.

### Dead ends (do not retry) — reconfirmed under this lens
- Hypergraph/transversal restatement of 𝓐_∞ — isomorphic, no new content.
- Sieve/complement of A — isomorphic dual, no new content.
- Gap-word finite-state automaton bypass — PROVEN (R3, certified) to collapse:
  finite automaton on value stream ⟺ Π finite.
- Any density/Σ1/p argument, including generating-function repackaging —
  PROVEN vacuous (R5): density(A) can be a fixed positive constant with Π
  infinite (obstruction family).
- Any lever bounding ∏G / p_max / |t−t'| (still forbidden per Rules) — this
  includes the natural development of idea (6) above if pursued carelessly.
- Sub-support-realization / anchor-partition-collapse levers (still
  forbidden per Rules) — also a natural but dead endpoint of idea (6).

### Small-case / intuition notes (conjecture, not proof)
- Re-affirming (not re-deriving numerically this round — already established
  R1–R5) that Π appears finite in every tested seed (e.g. a₁=375 → Π=
  {2,3,5,7,19}), consistent with the theorem being true, but the mechanism
  that pins Π's finiteness has resisted every framing tried across 6 rounds
  including this one.
- My honest assessment: **this problem's real difficulty is not in finding an
  alternative CHARACTERIZATION of admissibility** (the no-transient lemma
  already gives the canonical, essentially forced, characterization — every
  reframing I tried reduces to it) — **it is in finding a genuinely new
  COUNTING/GROWTH argument that bounds Π using the interplay between GREEDY
  MINIMALITY (which term gets picked) and the algebraic structure of
  products**, which is precisely what R3's certified obstruction result says
  is required ("must read the greedy CHOICES, not A_n alone") and precisely
  what idea (6) gestures at without landing. I did not find a way to make
  that landing that avoids the already-forbidden levers within my time
  budget. This should be read as evidence supporting the run's own R5/outline
  conclusion that route (iii), as a pure RE-REDUCTION of the problem
  statement, is exhausted — the plateau is not an artifact of a wrong
  reduction (the reduction is canonical) but of a missing genuinely new
  ARITHMETIC counting idea, which is squarely route (i)/(ii) territory, not
  (iii).
