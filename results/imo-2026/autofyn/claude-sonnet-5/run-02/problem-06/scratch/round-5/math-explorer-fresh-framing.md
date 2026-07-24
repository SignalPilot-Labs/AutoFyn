## imo-2026-06

### Part 1 — fresh top-level framings (far from covering-system-construction / greedy-exchange-cost-potential)

Both live approaches share one skeleton: classify terms by a *finite prime-signature*
(Q-type or S₀-extended-type), prove a finite family of persistent signatures exists
(pigeonhole), then need "disjoint-base-type persistent signatures always share an
S₀-prime" (gap †/V) before a CRT + cyclic-pigeonhole finish. Any approach that still
asks "do two finite signature-classes intersect" is a technique variant of this same
wall, not a fresh framing (see the `NEVER` rule about the automaton framing in
round 4's memory — it collapsed into Step 5 verbatim). To be genuinely different I
looked for framings whose *top-level target is not an intersection-of-families
statement*.

**Framing A — Reversibility / bijective-transition framing (from crux aimo-0514,
USAMO, subtopic `processes-and-algorithms`/`invariants-and-monovariants`).**
aimo-0514's crux move: encode the deterministic process as a map on a *finite* state
space that is a **bijection** (i.e. the successor is not just forward-determined but
also uniquely *backward*-determined from the successor state alone); a bijection on a
finite set decomposes into disjoint cycles, so every orbit is *purely* periodic — no
transient/pre-period at all, and this needs no separate "which classes intersect"
argument.

Concretely for imo-2026-06: define a candidate state not as "the extended type ρ(n)"
(a set — the object at the center of gap †) but as **the actual value a_n mod M for a
large enough fixed M** (M = a suitable multiple of all primes ever relevant), or even
more structurally, as the pair (a_n mod M, "which primes ≤ some bound divide a_n").
The forward map is obviously deterministic (given by the greedy rule + the fact that,
once in the eventual regime, legality reduces to a residue condition). The NEW thing
to attempt is the **backward** direction: is a_n recoverable from a_{n+1} alone (mod
M), i.e. is the eventual transition map injective on its image? If yes, aimo-0514's
argument gives periodicity *with zero pre-period from the point the state becomes
memoryless* directly, and — because injectivity of a self-map on a finite set is
equivalent to bijectivity is equivalent to surjectivity — this could produce the
periodicity conclusion (T,L exist) via a totally different mechanism than "prove every
disjoint pair of persistent types intersects": it would instead need "the map
(residue mod M) ↦ (residue of the next term mod M) is injective," a *single* global
injectivity claim, not a combinatorial family-intersection claim. This is genuinely a
different wall to attack (injectivity of one explicit map, provable perhaps by a
direct minimality argument: if two different current-residues r₁≠r₂ led to the same
next-residue mod M, the smaller-of-the-two-candidates argument in the greedy rule
would force a contradiction on which one is "smallest legal integer"). I did **not**
attempt to prove this injectivity — flagging it as the concrete new target for an
outliner to open as a rival approach. Note it does NOT obviously need gap † at all —
it sidesteps the type-intersection question entirely by working with the actual
integer values (mod M) rather than abstract prime-membership sets, which is the
structural difference that makes it a different framing, not a bypass of the same
wall one step later.

**Framing B — "Recurring primes" (density-of-support) framing, target-first instead
of witness-first.** Both live approaches build the finite core prime pool S
*constructively*, bottom-up from finitely many witness terms, then must prove a
consistency/intersection property about *all* refinements. A different top-level
target: define directly R := {primes p : p divides a_n for infinitely many n} and
try to prove **R is finite by a density/counting argument on R itself** (e.g., a
prime p ∈ R must have positive lower density of multiples among the a_n's, else it
could not divide infinitely many of a bounded-density-growth sequence a_n = O(n) —
Bounded Gap Lemma already gives a_n = O(n) unconditionally), and **separately** prove
that R alone (not any witness-built S) already makes every two large terms of
disjoint "R-type" share an R-prime, via a direct argument about what it means for a
prime to be "in R" (recurs infinitely often) rather than "is a witness's factor."
This targets the SAME conclusion as the Finite Core Theorem but from the density end
rather than the witness-construction end, and could avoid the "canonical witness may
not represent every refinement" issue that gap † is precisely about (since R doesn't
distinguish witnesses/refinements — it is one fixed global set by definition). I
flag this as a second candidate for the outliner; caution (see NEVER rule from round
2, already in memory) — do NOT confuse R with "the set of ALL primes ever appearing"
(that is provably unbounded); R must be defined via the "*infinitely often*"
condition specifically, which is a genuinely different (much smaller, plausibly
finite) set, and its finiteness itself needs its own proof, not assumed.

**Why these are not just the existing wall relabeled.** Framing A's target is a
single injectivity/bijectivity claim about one explicit map — no witness selection,
no "which refinement" ambiguity, no persistent-type family at all. Framing B keeps
the type-language but changes which object is constructed first (R vs. S), which
changes what has to be proved about it (global recurrence density vs.
witness-representativeness) — genuinely different proof obligations, even though the
downstream CRT+cyclic-pigeonhole finish (Step 5, already common ground) would look
similar once either framing's finiteness+intersection facts are established.

### Part 2 — the n=1-literal-periodicity secondary gap

**Status:** still completely untouched by any built approach (confirmed — no
approach file's proved content addresses it; `current.md`'s "Secondary open gap"
section explicitly and repeatedly flags it as open since round 1).

**Computational check (this round, fresh).** I independently simulated the exact
greedy rule (trial-division gcd) for a1 ∈ {4, 15, 35, 105, 143, 175, 1001, 231, 165}
and searched for (T, L) with a stable tail match, then found the MINIMAL index N such
that a_{n+T} = a_n + L holds for all n ≥ N. Result: **N = 1 in every single case that
stabilized within the simulated window** (a1 = 455, 1155 did not stabilize within
1500–3000 terms — long transients, consistent with the existing memory note about
wide-Q seeds needing longer windows, not evidence against N=1). This matches and
extends the prior rounds' spot-checks (a1 = 4, 15, 35, 143, 1001 in round 1's
outline-reviewer notes) with 4 new seeds, all confirming N=1. This remains a
**conjecture**, not a proof — no seed has ever shown a nonzero pre-period, across
~13 tested values of a1 total (old + new) spanning |Q| = 1 to 5.

**What would be needed to promote "eventually periodic with gap L" to "periodic from
n=1 literally," and whether the existing construction already forces it — the key
finding of this pass:**

The existing S₀-level construction does **not** automatically give N=1 for free: the
Finite Core Theorem's threshold N₁ and the extended-persistent-type threshold N₀' are
both defined via "eventually" pigeonhole arguments (Step 1, Step 4 of
`covering-system-construction.md`) that only assert *finiteness* of the exceptional
prefix, not that the prefix is empty. So closing this gap needs a **genuinely new
argument**, not a byproduct of finishing gap †. Two candidate routes, scouted but not
attempted (per role rules):

1. **Reversibility route (aimo-0514's exact template, most promising).** aimo-0514
   (crux: "a deterministic process is reversible so its state graph is a union of
   cycles, forcing the orbit to be purely periodic rather than eventually periodic")
   is the closest analog in the corpus. The template: encode state finely enough
   (there, "turn" = (vertex, incoming edge, outgoing edge); here, plausibly
   "(a_n mod M, the full multiset of primes ≤ some bound dividing a_n)" for M large
   enough to encode S₀ or R) so the one-step map is not just forward-deterministic
   but **backward-deterministic** too (i.e. injective): given a_{n+1}'s state, the
   greedy "smallest positive integer" rule together with minimality could in
   principle recover a unique a_n. If this injectivity can be shown on the (finite)
   eventual state space, the bijection-on-finite-set ⟹ pure-cycles argument gives
   *zero pre-period from wherever the state becomes well-defined* — and since the
   state is well-defined from n=1 (a_1 mod M is just a fixed number), this would
   directly close the gap, PROVIDED the injectivity is checked as holding from n=1,
   not just eventually (this is the part that would need real work — the state space
   must be shown finite and the map injective as a single explicit finite check, not
   an asymptotic one). I did not attempt this proof — it is a genuine gap, but it is
   the single most concrete, corpus-matched lead for this secondary target.

2. **Constraint-monotonicity / redundancy route (not corpus-matched, purely
   structural, sketched only).** The greedy rule requires a_{n+1} to be compatible
   with ALL of a_1,...,a_n, so removing early terms can only *relax* future
   constraints (never tighten them). If one could show that, once n is large enough
   for the persistent/extended-type machinery to apply, compatibility with a_1
   specifically is *already implied* by compatibility with the later core prime set
   S₀ (i.e. a_1's own constraint is redundant given the S₀-driven eligibility
   condition), then the sequence "restarted" from any later index would coincide
   termwise with the original — and pushing this argument down by strong induction on
   the (minimal) index where the periodic pattern first fails would either terminate
   at N=1 or produce a genuine smallest counterexample index to analyze directly.
   This is a minimality/induction-on-first-failure argument in the spirit of
   aimo-0077's "assume nontermination, take the minimal witnessed index in the
   forced cycle, derive a contradiction from restoring it" (already flagged in
   memory as a template for the *primary* gap's recruitment-process induction) —
   here proposed instead as a template for the *secondary* gap. Genuinely
   unattempted; flagged only.

**No crux found that resolves this by "small-case verification via structural
finiteness" alone** — I searched the corpus (`eventually periodic`, `purely
periodic`, `pre-period`, `initial segment`, `from the start` across all three
domains) and found no problem whose crux is "verify the periodic pattern started at
n=1 by a finite check" in a way that generalizes (a1-dependent case checks are not a
proof for all a1). aimo-0514 is the only strong structural analog; it is a bijectivity
argument, not a finite-verification trick.

### Candidate technique(s)
- Part 1: (A) reversibility/bijective-transition-map argument on a finite state
  space (aimo-0514 template) as an entirely new top-level route; (B) "recurring
  primes" R-first framing as a second, more conservative alternative that still uses
  the pigeonhole/CRT vocabulary but inverts which object is constructed first.
- Part 2: same reversibility template (aimo-0514) is the leading candidate; a
  minimality/first-failure induction (aimo-0077 style) is a fallback, unattempted.

### Cheap-kill candidates
- None obvious for gap † itself (already exhaustively probed by 3+ prior rounds).
- For gap 2 (N=1): a cheap partial win worth flagging to the outliner — even without
  a general proof, an explicit, checkable sufficient condition (e.g. "if a_1 is
  already divisible by every prime that will ever recur, i.e. Q ⊇ some minimal
  generating set" ) might cover many cases and narrow the residual; not verified this
  round, just a suggestion.

### Knowledge-base entries to use
- `knowledge_base.md` "Pigeonhole / extremal principle" (already the backbone of
  every persistent-type argument; would also back Framing A's finite-state-space
  pigeonhole).
- `knowledge_base.md` "Modular arithmetic, CRT" (needed regardless of framing for the
  Step-5-style finish).
- No other KB entries stood out as newly relevant this pass (KB is generic; nothing
  specific to reversible finite-state processes is separately named there — this is
  exactly why the crux corpus, not the KB, is the source for Framing A).

### Analogous past problems (cruxes)
- **aimo-0514** (USAMO, `processes-and-algorithms` / `invariants-and-monovariants`):
  strongest analog found. Crux move: encode a deterministic process as a bijection on
  a finite "turn" state space (forward AND backward determined), forcing every orbit
  to be *purely* periodic (no pre-period) rather than merely eventually periodic —
  directly the shape of both the primary gap (if used for framing A) and, more
  cleanly, the secondary n=1 gap. Genuinely analogous in structure (deterministic
  process + finite state + need periodicity with no transient), not just same-domain.
- **aimo-0077** (Germany TST, `extremal-principle` / `invariants-and-monovariants`):
  "assume nontermination ⟹ forced state-cycle ⟹ take the minimal-index object acted
  on in the cycle ⟹ contradiction from restoring it." Weaker analog than aimo-0514
  but useful as the template for a first-failure/minimality induction on the
  secondary gap (route 2 above), already flagged in memory for the primary gap's
  recruitment-round induction — worth reusing on the *different* target (periodicity
  onset index) since it was not attempted there.
- **aimo-0447** (USAMO, `divisibility-and-gcd` / `size-bounding-and-descent`): "gcd
  pairwise >1 on a grid forces min(a,b) large" via covering-grid + prime-density
  counting. Same surface vocabulary (gcd>1 pairwise, prime covering) as the existing
  covering-system-construction approach, but its actual mechanism (2D grid counting
  bound, asymptotic density of small primes) does not transplant — it is a magnitude
  lower bound for a *finite* grid, not a periodicity/finiteness-of-core-set
  statement for an infinite greedy sequence. Judged NOT genuinely analogous beyond
  vocabulary; not recommended as a route.
- aimo-0866 / aimo-0421 (twin problems, `divisibility-and-gcd`, "gcd(fixed,varying)
  has only finitely many values since it divides the fixed element, pigeonhole over
  an infinite family") — this is essentially a restatement of the already-certified
  Free Fact 2 / Bounded Witness Lemma mechanism, not new content; noted but not a
  fresh route.

### Prior progress
See `current.md` for the full certified lemma list (Free Facts, Bounded Gap Lemma,
Persistent-Type Pigeonhole, Bounded Witness Lemma, Finite Core Theorem, Generalized
Bounded Witness Lemma, Extended Persistent-Type Pigeonhole, Canonical-Refinement
Lemma, F_A∩F_B≠∅, |Q|=1 special case) — all unconditional and correct, all upstream
of gap † and gap 2, unaffected by this round's fresh-framing scouting. Gap † is
localized to residual set V (both-sides-non-canonical pairs); ROUND 4's critical
correction shows the *minimally-witnessed* S₀ has V=∅ in 18/18 tested seeds (the
"zero further recruitment rounds" conjecture is revived, not falsified — the
round-3 "falsification" was a computational bug, now corrected).

### Dead ends (do not retry)
- "Universal Glue Prime Lemma" / sparse-Q single-prime mechanism — falsified (a1=35).
- PUCL (Persistent Uniform Core Lemma), literal first-occurrence-anchored form —
  falsified; "generous" S-level form is a trivial corollary with no new content.
- Minimal-counterexample well-ordering on |A'|+|B'| for gap † — proven (round 3) to
  fail structurally (the only refinement operation available strictly increases the
  size measure).
- "Reduce a_n mod fixed M to a finite-state automaton" as a claimed NEW top-level
  framing — traced (round 4) to be isomorphic to the existing Step 5 CRT+cyclic-
  pigeonhole finish; do not re-propose as fresh diversity. (Framing A above is
  different from this: it targets injectivity/reversibility of the transition map
  itself as the PROOF MECHANISM for periodicity, not just a restatement of "reduce
  mod M," and specifically targets the n=1 literal-periodicity gap, which the round-4
  automaton framing did not address.)
- "Total set of all primes that ever divide any a_n is finite" — false (verified
  numerically, grows unboundedly).

### Small-case / intuition notes
- (Conjecture, now with 13 total confirming seeds across all rounds, 0
  counterexamples) periodicity a_{n+T} = a_n + L holds **from n=1 literally** in
  every tested case — this round added 4 fresh confirmations (a1 = 105, 143, 175,
  231, 165) to the prior round-1 set (a1 = 4, 15, 35, 143, 1001), all with N_min = 1.
  No seed has ever shown a nonzero pre-period.
- (Conjecture, revived per round-4 correction) the minimally-witnessed Finite Core
  Theorem's S already gives V = ∅ (zero further recruitment rounds) in all 18 tested
  seeds — the single best-supported concrete target for gap † going into this round,
  independent of which fresh framing (A/B above) is chosen to attack it.
