## imo-2026-06 — lens: FAH direct-mechanism, scoped to |F'|,|F''| >= 2

### What structurally distinguishes the |F'|,|F''| >= 2 case
Recall the setup (from `covering-system-construction` Step 8.9 / `lemmas/singleton-side-fah.md`):
rogue pair (A',B') at core S₀, witnesses n_A<n_B, F':=P(a_{n_A})\S₀, F'':=P(a_{n_B})\S₀,
q*:=min(F'∩F''). The already-certified **Generalized Bounded Witness Lemma** gives, for
*every* n>n_B with ρ(n)=A': a_n divisible by **some** prime of the fixed finite set F''
(this is unconditional, already proved, applies to every n not just infinitely many n —
the "existential" half of FAH is free). FAH is exactly the "existential → universal
single-witness" promotion: that the same fixed q* ∈ F'∩F'' can be taken for *cofinitely
many* n, not merely "some prime, possibly varying with n." When |F''|=1 this promotion
is free (Singleton-Side FAH, certified) — there is nothing to promote, the disjunction
has one disjunct. When |F''|>=2, the promotion is a genuine claim: it says the map
g(n) := "which prime of F'' divides a_n" (well-defined up to ties, since a_n could be
divisible by several) does *not* have infinitely many n falling outside the q*-fiber.
Structurally this is a claim about the *relative asymptotic frequency* of competing
divisors in a fixed finite menu — nothing in the certified stack (Free Facts, gcd
pigeonhole, magnitude-only Gap Lemmas) controls frequency, only existence (see Lemma I /
Lemma F precedent, both correctly diagnose this: the toolkit proves "≥1 occurrence" or
"infinitely many," never "cofinitely many" or "density 1").

No sub-case split by |F'∩F''| exactly 2 vs ≥3 has been explored in the certified stack
or in the approach files — I did not find evidence in the workspace that this size
matters mechanically (Lemma H / Critical Prime Dichotomy is stated for a single prime
q' at a time and gives no joint handle regardless of |F'| size). My own fresh probe below
suggests instead that what actually matters is whether q* happens to be an *early,
widely-recruited* prime (see below), not |F'∩F''|'s cardinality per se — this is a new,
untested distinction worth flagging to the outliner.

### What has been tried and failed (verified against current.md / lemma files)
1. **Fixed-Witness Divisor-Chain (Step 8.9, round 8, `covering-system-construction`).**
   Define d_n := gcd(a_{n_A}, a_n) for A'-type n; well-defined, finite-valued
   (`lemmas/divisor-chain-well-definedness.md`, certified). Pigeonhole the "exceptional"
   set E (n with q*∤a_n) over Div(a_{n_A})\{1} to get a fixed alternate divisor d,
   hence a prime r|d dividing infinitely many n∈E. **Dead end, precisely diagnosed**: the
   proposed dichotomy ("r∈S₀ ⟹ contradicts rogueness, else r is a new candidate") is
   FALSE at branch (a) — r∈S₀ only forces the tautological r∈A' (every element of A'
   divides every A'-type term by definition of extended type), which says nothing about
   B' or rogueness. I re-verified this is correct: r∈A'⊆S₀ is a real, unblocked outcome
   of the pigeonhole (nothing in Free Facts / Bounded Witness / Divisor-Restricted
   Pigeonhole / Critical Prime Dichotomy rules it out), so the whole mechanism can
   collapse into a content-free tautology. **Root cause: gcd(a_{n_A}, a_n) is the wrong
   fixed witness to pigeonhole against** — it re-derives (badly) what Generalized
   Bounded Witness Lemma already gives directly via gcd(a_{n_B}, a_n) (which correctly
   isolates F'' as the relevant menu, no tautology risk since F''∩A'=∅ by rogueness).
   Do not re-attempt gcd-with-the-SAME-side-witness pigeholing; any future divisor-chain
   attempt must pigeonhole against the OPPOSITE side's witness (a_{n_B} for A'-type n),
   which is exactly what the already-certified Single-Witness-Prime Pigeonhole Refinement
   does — and that only gives "infinitely many," not "cofinitely many," so it is not
   itself new ground, just the correct non-tautological base to extend from.
2. **Joint Lemma-H branch analysis / Two-Witness Intersection Uniqueness** (round 7) —
   dead, confirmed both abstractly (Lemma H's branch (b) gives no S₀-type data about the
   witnessing index) and computationally (a_1=4807: both candidate primes 13,17 land in
   branch (a) trivially).
3. **Blocking-Data Bridging** (Lemma K, round 7) — the constructed "adjacent multiple"
   competitor's factorization has no controlled relation to the witness's, so Free
   Facts' guaranteed shared prime cannot be pinned to q*. Dead as scoped.
4. **aimo-0678-style algebraic-recursion transplant** (Witness Discontinuity Obstruction,
   round 7) — dead: enlarging the core can push a type's earliest witness to an unrelated
   later index with no forced relation to the recruited prime.
5. **Charging/potential arguments** (ω(a_1), growth rate O(n)) — both confirmed dead
   ends (round 6); "batch resolution" reduces to open FAH, not independent.
6. Lemma I / Lemma F (both round diagnostics, not certified as portable) both correctly
   state: no composition of Free Facts + magnitude Gap Lemmas + existential pigeonhole
   can promote "some prime of a ≥2 set works" to "one specific prime always works" —
   this is the single load-bearing obstruction every dead mechanism above hits.

### NEW finding this round (computational, my own from-scratch probe — labeled conjecture/evidence, not proof)
I regenerated a_1=4807 from scratch (own greedy simulator, trial-division factorization
via sympy, N=2500 terms) and found something the workspace had not previously isolated:
**testing FAH-style divisibility at the coarse BASE-TYPE level (as round 8's "un-recruited
core, 6%" finding did) is measuring the wrong object and gives a misleading non-cofinite
signal — likely a measurement artifact, not a genuine near-counterexample.**

- Base type {11} (n>4, 895 occurrences up to n=2500): divisibility by 2 is **literally
  100.000%, 0 exceptions** in every window sampled (n=5..140, 143..419, 421..841,
  844..2499) — a genuine, stable, non-decaying full-absorption signal for prime 2.
  Divisibility by 3, by contrast, is stable at ≈66-68% across every window — neither
  trending to 0 nor to 1. This is exactly consistent with the **already-certified
  Extended Persistent-Type Pigeonhole**: base type {11} is not a single S₀-persistent
  cell but a union of (at least) two distinct extended-persistent sub-types ({11,2,3,...}
  and {11,2,¬3,...}), each individually stable at its own positive frequency. Testing
  "does 3 divide base-type-{11} terms" therefore measures a MIXTURE of cells, not the
  single specific rogue extended type FAH is actually a claim about — a stable
  intermediate fraction here is not evidence against FAH, it is exactly what the
  certified pigeonhole lemma predicts happens when you test at too coarse a granularity.
- Directly checking round 8's own "6%, |F'|,|F''|≥2, genuinely open" evidence: its own
  text says the test was done "at the smaller core S₀=Q, before the Finite Core Theorem's
  own recruitment is applied," using "base types {19} and {11}" — i.e. it explicitly
  tested the coarse object, the same one I just showed gives a stable-but-not-0/1 rate
  for unrelated structural reasons. **This raises a genuine possibility (not proved)
  that round 8's "~6%, genuinely NOT cofinite" finding does not actually falsify or even
  probe FAH — it was never testing a single extended-persistent type, so a fractional
  rate there is expected regardless of whether FAH is true.** This should be flagged to
  next round's builder: re-test FAH's exception rate specifically WITHIN the properly
  identified (post-recruitment) rogue extended-persistent type A', not the base type —
  this is exactly what round 6's 0/10, 0/151 tests did (small samples, but correct
  granularity) and what should be extended to a much larger sample before trusting either
  a positive or negative verdict.
- I separately found a genuine |F'∩F''|≥2 rogue-adjacent instance at the raw core S₀=Q:
  pair (base-{11}, base-{23}), earliest witnesses n_A=2 (a_2=4818), n_B=4 (a_4=4830),
  F'=P(a_2)\Q={2,3,73}, F''=P(a_4)\Q={2,3,5,7}, so F'∩F''={2,3}, q*=min=2 — a genuine
  (non-singleton) F'∩F'' menu. At this q*=2, divisibility is **literally 100% (0/895)**
  — full, not merely cofinite, absorption, even though the raw menu has 2 elements. This
  is real positive evidence for FAH surviving a genuine |F'∩F''|≥2 case, but it is also
  consistent with a narrower, unproven mechanism: q*=2 might be winning simply because it
  is the *smallest, earliest-recruited* prime, behaving almost like a "hidden singleton"
  (a dominant, near-universal prime) rather than genuinely resolving a close two-way
  competition. I did not find or test an instance where the competition between two
  primes of comparable "recruitment strength" is genuinely close (e.g. both appearing at
  roughly equal, non-trivial rates) — that would be the sharpest possible test of FAH and
  was not attempted this round due to time; flagged as the highest-value next probe.

### Candidate new mechanism (idea only, not attempted, not developed into steps)
The 100%-for-2 vs 67%-for-3 asymmetry suggests a **density/asymptotic-domination**
argument (explicitly flagged as unexplored in round 6/7 guidance: "density/asymptotic-
domination arguments... remain unexplored"): once a prime p has been recruited and
achieves a positive density among terms, later greedy candidates increasingly "prefer"
p-divisible values because satisfying gcd>1 simultaneously against a growing number of
earlier terms is cheapest via a prime that already divides many of them — a
rich-get-richer selection pressure. This would need a genuinely new (counting/density,
not existence-only) lemma — nothing in the certified stack currently measures density,
only existence/infinitude. This matches the shape the dispatch asked about
(existential→universal promotion) but via a *quantitative* route rather than a
combinatorial pigeonhole — a different flavor from every dead mechanism above (1–5),
since those all tried to force a *logical* contradiction from a single witness, not a
frequency argument over the whole tail.

### Crux corpus check (per crux_moves_documentation.md; domain=number_theory, subtopics divisibility-and-gcd / pigeonhole / sequences-and-recurrences)
- **aimo-0421** (divisibility-and-gcd) — "gcd of a fixed element with a varying one is
  always a divisor of that fixed element, hence finite-valued; pigeonhole over an
  infinite family forces a constant value on an infinite subfamily." This is exactly the
  mechanism already fully absorbed into the certified stack (Divisor-Chain
  Well-Definedness + Single-Witness-Prime Pigeonhole Refinement) — not new ground, and
  its second half ("arrange a shared prime avoided by the fixed element to force a
  contradiction") is structurally what Step 8.9 tried and found tautological. Analogous,
  but already fully mined.
- **aimo-0477** (sequences-and-recurrences-flavored divisibility) — "track
  d_n=gcd(a_1,a_n) and show it divides the next term, producing a divisor chain bounded
  by the fixed term that must STABILIZE" — the key extra ingredient beyond Divisor-Chain
  Well-Definedness is **monotonicity** (v_p(d_n) nondecreasing in n for every p, because
  the sequence there has a genuine recursive relation a_{n+1} from a_n). This is a
  genuinely different, NOT-yet-tried idea for FAH: ask whether e_n := gcd(a_{n_B}, a_n)
  restricted to F''-primes is monotone (nondecreasing in a suitable per-prime valuation
  sense) along the ordered list of A'-type occurrences n_1<n_2<...; if provable, a
  bounded-above (by Div(a_{n_B})) nondecreasing chain must stabilize, which is exactly
  the cofinite-divisibility shape FAH needs. **Caveat**: our sequence is greedily
  defined, not recursively defined from a fixed earlier term the way aimo-0477's is, so
  there is no a priori reason for such monotonicity — this needs to be checked
  computationally before any proof attempt (not done this round, flagged as the most
  promising literally-new mechanism from the corpus).
- **aimo-0728** (divisibility-and-gcd) — "the very first branch choice fixes a prime
  that divides every later first-difference" — same shape as FAH (an early choice
  propagating to force universal divisibility) but relies on a strict multiplicative
  recursion (b_{n+1}/b_n ∈ {2,3}) absent here; likely not directly transplantable, but
  worth noting as the closest thematic match for "first choice locks in forever."
- No crux was found that performs a genuine density/frequency argument over an infinite
  greedy sequence's factorizations (nothing in the sampled subtopics matches "positive
  density implies cofinite" reasoning) — the density-domination idea above appears to be
  genuinely outside what the corpus offers directly; it would need to be built from
  scratch if pursued.

### Recommendation for the outliner
1. Do not re-dispatch the Fixed-Witness Divisor-Chain (Step 8.9) in its literal
   same-side form (gcd(a_{n_A}, a_n)) — dead, precisely diagnosed, tautology risk
   unfixable without extra machinery.
2. High-value cheap probe before any proof attempt: rerun round 8's "6%" computation but
   restricted to the actual, properly-refined extended-persistent type A' (post
   recruitment, matching round 6's setup), with a MUCH larger sample (n up to several
   thousand, not ~150/1200), to see whether the exception rate trends to 0 (supports
   FAH) or stabilizes at a fixed positive rate (would be a genuine, much stronger
   counterexample than currently on record). This directly resolves whether round 8's
   negative evidence is real or an artifact — worth doing before investing in a new
   mechanism.
3. If pursuing a new mechanism, the two live candidates are: (a) an aimo-0477-style
   monotone divisor-chain (needs a from-scratch monotonicity check first, not yet done);
   (b) a density/asymptotic-domination counting argument (currently the least mined,
   flagged twice by prior rounds as unexplored, and now with fresh empirical
   support — literal 100% absorption by an early-dominant prime in a genuine |F'∩F''|≥2
   instance).

## Status labels
- Everything under "What has been tried and failed" is **verified against current.md
  and the lemma files**, not merely restated — the Step 8.9 tautology gap was
  independently re-derived from the definitions above, matching the existing record.
- Everything under "NEW finding this round" is **fresh, this-round computation**
  (own Python/sympy simulation, N=2500 for a_1=4807), reported as **empirical evidence /
  conjecture, not proof**. The "measurement artifact" hypothesis about round 8's 6%
  figure is a plausible reinterpretation, NOT a retraction of that finding — it needs
  to be checked by a proper same-granularity rerun before anyone treats either verdict
  as settled.
