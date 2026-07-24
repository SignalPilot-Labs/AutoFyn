## imo-2026-06 — fresh crux-corpus mining pass (identity-level vs existence-level information)

### Task recap
15 mechanisms are dead, all sharing the same diagnosis: everything certified in
`results/imo-2026-06/lemmas/` proves EXISTENCE ("some prime of a fixed finite set
divides a_n") or MAGNITUDE ("a_n is sandwiched"), never IDENTITY ("prime q, and no
other, divides literally every sufficiently large A-type term"). I mined
`domain=number_theory` (`p-adic-valuation`, `invariants-and-monovariants`,
`sequences-and-recurrences`) and `domain=combinatorics`
(`invariants-and-monovariants`, `processes-and-algorithms`,
`sequences-and-recurrences`) hunting specifically for a technique that pins an
identity via a valuation-monovariant or an exchange/bijective argument, and for
any crux that genuinely exploits a_1's exact factorization (not just its prime
support Q) for a greedy/minimality sequence.

### One genuinely new candidate: aimo-0134's integer-average monovariant
`aimo-0134` ("Let a_1=n, a_k = the unique residue in [0,k-1] with k | a_1+...+a_k;
prove the sequence eventually becomes constant") is a strong subtopic AND surface
match — it is exactly "prove a sequence built by a per-step legality rule is
eventually periodic (here: eventually literally constant)," the same shape of
conclusion as our target `a_{n+T}=a_n+L`. Its crux move (tagged in BOTH
`size-bounding-and-descent` and `sequences-and-recurrences`) is:

> Replace the sequence by the integer-valued running average `b_k :=
> (a_1+...+a_k)/k`. Show `b_{k+1} ≤ b_k` (elementary telescoping), so by
> integrality `(b_k)` is a non-increasing sequence of NONNEGATIVE INTEGERS, hence
> eventually constant. Then a difference identity, `a_k = (k+1)b_{k+1} - k·b_k`,
> converts "eventually b_k = b constant" DIRECTLY into "eventually a_k = b" — i.e.
> the exact identity of every later term, not just its existence-level
> divisibility class.

**Why this is a genuinely different mechanism than anything killed so far.** All
15 dead mechanisms in this workspace are prime-set / covering-system /
divisor-class arguments (persistent types, recruitment, singleton hypothesis,
CRT-glue, density/sieve). None of them is "construct an auxiliary
INTEGER-valued statistic of the sequence itself, prove it monotone and bounded,
invoke integrality to force it eventually constant, then invert a difference
identity to recover the term's exact value." This sidesteps "which prime" chasing
entirely — the promotion from existence to identity happens via *integrality of
an average*, not via *tracking which prime survives a pigeonhole*. This is the
kind of "genuinely different top-level target" CLAUDE.md's plateau-break rule
asks for.

**Necessary honesty about the transplant gap (I did not attempt to close it —
just flagging the opening).** `aimo-0134`'s statistic is monotone because the
rule keeps partial sums balanced (each new term "corrects" the sum toward a
multiple of k). Our sequence's terms grow (a_n → ∞, gaps bounded but not
shrinking), so `a_n` itself is not a candidate for a bounded monotone monovariant
directly. But a DERIVED quantity might be: e.g., candidates worth an outliner's
scrutiny —
  - `c_n := a_n − n·λ` for a guessed asymptotic slope λ (if a_{n+T}=a_n+L holds,
    the true slope is L/T; a monovariant argument here would need to prove
    boundedness/monotonicity of `c_n` WITHOUT presupposing L/T, which is circular
    unless some other integer emerges — this is the open design question, not a
    proof).
  - the gap sequence `g_n = a_{n+1}-a_n` (already used via the certified
    Gap-Periodicity Equivalence, Lemma A) — is there an integer-valued running
    statistic of `g_1,...,g_n` (e.g. a partial-sum-of-gaps mod some fixed L, or a
    count of "distinct extended-persistent types visited so far") that is
    provably non-increasing and integer, in the aimo-0134 style? Not attempted by
    any of the 15 dead mechanisms as far as the certified lemma list shows — the
    closest, `greedy-exchange-cost-potential`'s "cost potential," tracks a
    PIGEONHOLE COUNT of witness primes recruited (existence-style bookkeeping),
    not a bounded monotone integer statistic in the aimo-0134 sense. These are
    different tools even though both use the word "potential."

This is a genuine gap in the population's toolkit, not a proof — I stopped here
per instructions (found the opening, did not develop it).

### Second candidate, weaker: aimo-0889 (extremal-element-by-valuation forcing)
`aimo-0889` ("product of any 100-subset of S divides the product of the other
1919 elements; max number of primes in S?") uses: *"apply the divisibility
condition to the k elements of LARGEST ν_p among S, for each fixed prime p, to
get a per-prime lower bound on how many elements p divides."* This is an exchange
argument that turns an aggregate hypothesis into a per-prime, per-EXTREMAL-element
identity statement. It is suggestive (use the witness of extremal valuation, not
an arbitrary witness, to force identity) but the disanalogy flagged in round 10 for
the closed-form-recurrence family applies here too in a different way: aimo-0889's
hypothesis is a single GLOBAL, ALL-AT-ONCE divisibility condition over a fixed
finite set S (checkable by choosing extremal elements once), whereas our problem's
constraint is generated one step at a time by a GREEDY MINIMALITY search over an
unboundedly growing history — there is no fixed finite "S" over which to run a
single extremal-element argument; the extremal element (e.g. "the term of highest
ν_p seen so far") keeps changing as n grows, which is precisely the "Growing-
Constraint Obstruction" round 10 already certified as fatal to this style of
argument (`greedy-exchange-cost-potential`'s Escape-Budget attack). **I checked
this before recommending it: the disanalogy holds up — do not pursue aimo-0889's
mechanism literally**, though the general idea "let the witness be extremal in a
valuation, not merely persistent-type-canonical" is not obviously subsumed by
anything already dead (worth one cheap sanity check by the outliner: does an
extremal-valuation witness, rather than the earliest-occurrence witness the
Finite Core Theorem currently uses, behave differently under recruitment? Not
tested by any prior round as far as `current.md` records — all witness
constructions to date use "earliest occurrence," never "maximal ν_p occurrence.")

### Third candidate, checked and rejected: aimo-0514 (reversibility ⟹ purely periodic)
"Show a deterministic process is reversible so its state graph is a union of
cycles, forcing purely periodic (not just eventually periodic) behavior." Not
useful here: it strengthens "eventually periodic" to "periodic from step 1" — that
is exactly this workspace's SECONDARY n=1 gap, not the primary FAH crux — but the
mechanism needs the state space to be FINITE and the map REVERSIBLE (injective on
that finite space). Our "state" (the extended-persistent type / residue data) is
finite, but the map "current type → next type" is a many-to-one FUNCTIONAL graph,
not shown injective (indeed several extended-persistent types can plausibly map to
the same successor type, e.g. via different specific successor integers with the
same type) — no certified lemma establishes injectivity, and proving it would
likely be exactly as hard as FAH itself (it would need to know which prime is
forced, to rule out two different current-states mapping to the same next-state
via different primes). Not a shortcut; flagging only so it is not independently
re-discovered and mistaken for new.

### Closed-form-recurrence family — reconfirmed still disanalogous
Re-checked `aimo-0477`, `aimo-0678`, `aimo-0680`, `aimo-0682` (already ruled out in
round 10): all four assume a fixed algebraic/CRT-style recurrence or a fixed
finite family of candidate differences known in advance, never a term defined by
"the smallest integer passing an existential test against an unboundedly growing
history." Confirms round 10's finding; no new angle found here this round.

### Verdict on "has a_1's exact factorization (not just support Q) been
exploited anywhere in the corpus for a similar greedy/eventually-periodic
argument?"
No. Across all subtopics searched (`p-adic-valuation` ×57 number_theory,
`invariants-and-monovariants` ×2 number_theory / ×181 combinatorics,
`processes-and-algorithms` ×48 combinatorics, `sequences-and-recurrences` ×6
number_theory / ×2 combinatorics), the closest analogues either (a) work with a
FIXED finite algebraic structure known in advance (aimo-0889, the closed-form
family), or (b) use exponent VALUATIONS purely as bookkeeping for a fixed
divisibility identity (the p-adic-valuation list), never as a monovariant that
grows/shrinks along a greedily-defined, history-dependent process the way this
problem's a_n do. I found no crux that uses the exact multiplicities (e_p for
p | a_1) as opposed to merely the prime SET Q. This remains a genuinely
unexploited structural fact of the problem itself (every certified lemma in
`results/imo-2026-06/lemmas/` is stated in terms of prime SETS/types, never
exponents) — worth flagging to the outliner as untried raw material, independent
of the corpus.

## Summary for the outliner
- **Distinct opening (new, from this mining pass):** try an aimo-0134-style
  integer monotone-average monovariant built from the GAP sequence `g_n` (or a
  count of distinct extended-persistent-types-visited-so-far, or some other
  integer statistic of the greedy process), aiming to force eventual identity
  directly via integrality + a difference identity, bypassing "which prime"
  entirely. This is untried; no certified lemma or dead approach matches this
  shape. Concretely: this is a genuinely different top-level target from the
  existence/covering-system framing that has occupied all 15 dead mechanisms —
  it does not ask "which prime divides a_n" at all.
- **Weak secondary opening:** test whether choosing witnesses by MAXIMAL ν_p
  (extremal-valuation witness, aimo-0889-style) rather than earliest-occurrence
  changes recruitment behavior; likely runs into the same Growing-Constraint
  Obstruction, but not literally tested — cheap to check computationally before
  committing to a full attempt.
- **Rejected on inspection:** aimo-0514's reversibility trick (needs injectivity
  of the type-transition map, which is exactly as hard as FAH); aimo-0682/0477/
  0678/0680 closed-form family (re-confirmed disanalogous, per round 10).
- **Untried raw material independent of the corpus:** exact exponents `e_p` of
  a_1's factorization (not just Q) — no certified lemma uses this; the corpus
  offers no direct transplant for it either, but the outliner should not assume
  it's been tried just because Q-level facts have been exhaustively mined.

## Candidate technique(s)
Integer monotone-average / difference-identity monovariant (aimo-0134 style) as a
genuinely new top-level target, distinct from the existence/covering-system
family that has occupied all prior rounds.

## Knowledge-base entries
None beyond what's already in use (Modular arithmetic/CRT, Linear
recurrences/eventual periodicity mod m, Invariants & monovariants — the generic
KB entry for "a quantity preserved or monotone across moves" is the closest
match to the aimo-0134 mechanism, but the KB entry itself is too generic to cite
as a specific tool; it's a pointer, not a lemma).

## Analogous past problems (cruxes)
- `aimo-0134` — best match: same conclusion shape (eventually-periodic/constant
  sequence from a per-step legality rule), crux move is the integer-average
  monovariant + difference-identity described above. Genuinely worth adapting;
  the actual invariant construction is NOT solved by transplant (a_n grows, so
  a_n itself isn't the bounded statistic — a derived quantity is needed, open
  design question).
- `aimo-0889` — weaker analogy: extremal-valuation-witness exchange argument;
  disanalogy (fixed finite hypothesis set vs. unbounded greedy history) checked
  and confirmed to reproduce the already-certified Growing-Constraint
  Obstruction if transplanted literally.
- `aimo-0514` — checked, not analogous (would need injectivity of the type map,
  circular with FAH itself).

## Prior progress
See `results/imo-2026-06/current.md`: 15 mechanisms dead, all existence/
covering-system framing; No-Restart Lemma and Self-Absorbing Core Theorem
(gap identified) are round 13's latest certified/near-certified content. Not
re-summarized in full here — this report is scoped to the crux-mining task only.

## Dead ends (do not retry)
All 15 listed in `current.md`'s Rules history (FAH, Symmetric FAH, Cofinite FAH,
EEA, CRT-glue family, density/sieve family, seed-coupling-induction, etc.) —
unchanged this round. Additionally, per this mining pass: aimo-0514's
reversibility trick and the closed-form-recurrence family (aimo-0477/0678/0680/
0682) are confirmed non-transplantable — do not re-mine these again in future
rounds without new information.

## Small-case / intuition notes
No new computation run this round (task was corpus mining, not case-checking);
prior rounds' extensive empirical support for FAH-adjacent claims (0
counterexamples across hundreds of seeds) stands unchanged. The new monovariant
opening is a structural suggestion, not yet checked on any seed — the outliner's
first move, if it takes up this thread, should be a quick numerical trial (e.g.
on a_1=175, 187, 209) of candidate integer statistics (partial average of gaps,
or count of distinct types seen) to see if any is empirically monotone before
investing in a proof attempt.
