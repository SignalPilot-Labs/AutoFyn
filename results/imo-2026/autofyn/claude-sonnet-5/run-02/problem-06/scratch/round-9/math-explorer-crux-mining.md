## imo-2026-06 (lens: crux-corpus mining for existential-to-cofinite/universal promotion)

### What FAH actually needs (re-read, important framing note)
`greedy-exchange-cost-potential.md` line 891 states FAH literally: "q | a_n for
**every** n > n_B with ρ(n)=A′ (not merely infinitely many...)" — i.e. the target as
currently written demands *zero exceptions*. But `covering-system-construction.md`'s
own Step 8.5 finish (lines ~291-292, and the Current-Best §12 "Given (†) ... the CRT
+ cyclic-pigeonhole finish") only actually needs "**every sufficiently large** term ...
is divisible by p*" for the periodicity conclusion a_{n+T}=a_n+L, which already only
holds "beyond a finite threshold." **This is a real opening the population has not
exploited**: the literal zero-exception form of FAH is strictly stronger than what the
finish uses. A cofinite (finitely-many-exceptions) version of FAH would suffice, and —
per the corpus leads below — cofinite statements are provable by *counting/pigeonhole
capacity* arguments even when the literal "every occurrence" form resists direct proof.
This reframes the open target from "prove q divides every A′-occurrence" to "bound the
number of A′-occurrences q fails to divide," a different and possibly more tractable
shape of claim. Flag this to the outliner as a legitimate weakening of the FAH target,
not a retreat — Singleton-Side FAH already over-delivers (zero exceptions) precisely
because the Bounded Witness Lemma gives it for free; the |F′|≥2 case may only need the
weaker cofinite form.

### Concrete crux leads (number_theory + combinatorics, filtered per instructions)

**1. `aimo-0016` (combinatorics, subtopics: induction-and-construction, pigeonhole,
invariants-and-monovariants) — IMO-level "prove the sequence is periodic" problem,
structurally the closest analog in the corpus.**
- Crux move: "Upgrade an 'equal infinitely often' shift relation on state-tuples to
  'holds for all indices' by a one-step **downward induction**, using an auxiliary
  windowed-sum sequence to transport the relation one index earlier." Concretely:
  define D = {d : A_d = A_{d+p}}; show D is infinite (unbounded); then prove
  "d+1 ∈ D ⟹ d ∈ D" using a reappearance lemma on an auxiliary windowed-sum sequence
  b_k := S(k,k+p); since D is unbounded and closed under predecessor-inheritance, D
  becomes literally everything, not just cofinite.
- Adaptation idea (not a proof): FAH wants D := {n : ρ(n)=A′, n>n_B, q|a_n} to be
  cofinite in the A′-occurrence index set. We already have D infinite (Single-Witness-
  Prime Pigeonhole Refinement / Generalized Bounded Witness Lemma). The missing
  ingredient is a **downward-transport step**: some auxiliary quantity tying a_n's
  divisibility by q to the *previous* A′-occurrence's divisibility by q (e.g. via
  gcd(a_n, a_{n'}) for n' the prior A′-occurrence, or via the Bounded Gap Lemma's
  a_{n+1} ≤ a_n + a_1 controlling how a_n can drift). If such a one-step "q divides the
  next A′-occurrence ⟸ q divides this one, modulo finitely many escapes" lemma could be
  proved, combined with D's infinitude this pattern would deliver cofiniteness (or even
  literal universality) directly — a genuinely different mechanism from anything tried
  so far (divisor-chain pigeonhole, Lemma H branch analysis, algebraic-recursion
  transplant). Caveat: the certified **Witness Discontinuity Obstruction** already shows
  one naive "recruited prime persists to the next witness" recursion is FALSE in
  general (a_1=175 example) — so any downward-transport lemma here must be built on the
  *A′-type occurrence sequence itself* (not on core-refinement stages), which is a
  different object than what Discontinuity Obstruction refutes; this distinction should
  be checked carefully before building on it.

**2. `aimo-0051` (algebra, functional-equations/sequences-and-recurrences) — "Δ is
unbounded" problem; contains a directly-named crux "Upgrade a finite-orbit bound to a
single cofinite orbit by counting how many index-window outputs each length-(B-A)
window can miss."**
- Crux move: with finitely many chains (an a priori finite structural bound), a
  counting argument shows a fixed-width window [A,B] can contain at most O(1) values
  NOT achieved by a single chain, so the "bad" (excluded) count is uniformly bounded
  independent of window length — hence at most finitely many integers are missed
  overall, giving cofiniteness of the single good chain.
- Adaptation idea: this is the cleanest template for exactly the reframed cofinite-FAH
  target above. If the number of A′-occurrences NOT divisible by q in any window of
  length W can be bounded by a constant independent of W (using some finite structural
  bound already in hand — e.g. |F′| itself, or the size of Div(a_{n_A}) from the
  certified **Divisor-Chain Well-Definedness Lemma**), the same "grow the window, bad
  count stays bounded ⟹ globally finitely many bad indices" argument closes cofinite
  FAH without ever pinning down a single fixed prime a priori. This directly reuses
  already-certified machinery (Divisor-Chain Well-Definedness, Single-Witness-Prime
  Pigeonhole) in a new role — as a window-capacity counting bound rather than a direct
  identity-forcing pigeonhole (which Lemma I already showed cannot work).

**3. `aimo-0098` (number_theory, divisibility-and-gcd/p-adic-valuation) — weaker
analog, functional-equation flavored, worth a one-line mention.**
- Crux move: "When the defining relation only promises SOME prime divisor satisfies
  it, evaluate at prime powers (where the prime divisor is unique) to turn the
  existential into a forced equation," then "the existential choice is immaterial
  because every prime carries the same value" — i.e. side-step needing "a specific
  witness" by showing all possible witnesses give the same downstream consequence.
- Adaptation idea (weaker fit, flag as a fallback framing only): rather than proving
  a SPECIFIC canonical prime q works cofinitely, show that WHICHEVER prime of F′ (or
  F″) witnesses a given A′-occurrence's divisibility, the CRT/period-finish conclusion
  is the same — i.e. try to make the choice of witnessing prime immaterial to the final
  periodicity claim, rather than forcing a single q. This would be a genuinely
  different top-level target ("period is forced regardless of which F′-prime shows up
  where") rather than proving FAH as literally stated. Less developed than leads 1–2,
  but worth noting since it sidesteps the single-fixed-prime requirement entirely,
  which is exactly what Lemma I diagnosed as the missing ingredient in every existing
  mechanism.

**Not a match (checked, ruled out):** `aimo-0889` (per-prime extremal counting under a
k-subset-product-divides-complement condition) — superficially about "forcing a prime
to divide many elements," but the mechanism (adversarial-subset extremal counting) has
no natural analog to a sequence's forward index structure; would require force-fitting.
`aimo-0415`, `aimo-0916` (finite self-map image-stabilization) — reference finiteness-
forces-stabilization intuition already fully captured by the workspace's own Finite
Core Theorem / Persistent-Type Pigeonhole; no new mechanism beyond what's certified.

### Distinct openings surfaced
- (a) **Reframe the target**: prove cofinite FAH (finitely many exceptions), not
  literal zero-exception FAH — sufficient for the Step 5/Step 8.5 finish, and matches
  the `aimo-0051` window-capacity-counting template. This is a genuinely different
  top-level claim than what every approach in the population is currently attacking.
- (b) **Downward-transport induction** (`aimo-0016` style): build a one-step lemma
  linking q's divisibility of the current A′-occurrence to the next/previous one via
  an auxiliary quantity (candidates: gcd chains via Divisor-Chain Well-Definedness, or
  the Bounded/Generalized Bounded Gap Lemma's growth control), then combine with the
  already-certified infinitude of q-divisible A′-occurrences to promote to cofinite or
  universal.
- (c) **Witness-immateriality reframe** (`aimo-0098` style, weaker/fallback): make the
  final periodicity conclusion independent of which prime of F′/F″ witnesses each
  occurrence, sidestepping the need to fix a single canonical q at all.

### Candidate technique(s)
Window-capacity counting / pigeonhole-on-bounded-exception-count (from aimo-0051);
downward one-step transport induction on an infinite-but-not-yet-cofinite index set
(from aimo-0016). Both are combinatorics/algebra-domain techniques being proposed for
adaptation into this number-theory problem — genuinely different in kind from the
divisor-chain/Lemma-H/algebraic-recursion mechanisms already exhausted.

### Cheap-kill candidates
None obvious for these new leads themselves (they are constructive proposals, not
claims to falsify) — but before building on lead (b), re-verify the Witness
Discontinuity Obstruction's scope note above (it refutes core-refinement-stage
persistence, not necessarily same-type-occurrence-to-occurrence persistence); a 10-line
computational check on a_1=4807 (does q=17 divide consecutive {19}-type occurrences in
runs, or is failure scattered/isolated?) would cheaply indicate whether lead (b)'s
one-step transport has any hope, or whether failures are so scattered that no local
transport lemma can exist (in which case only lead (a)'s counting template survives).

### Knowledge-base entries to use
Not separately consulted this pass (out of scope for this lens per dispatch — crux-
corpus mining only); the certified lemma stack already in `results/imo-2026-06/lemmas/`
(Divisor-Chain Well-Definedness, Single-Witness-Prime Pigeonhole Refinement,
Generalized Bounded Witness Lemma, Bounded/Generalized Bounded Gap Lemma) is the
relevant reusable toolkit for adapting leads (a)/(b).

### Analogous past problems (cruxes)
- `aimo-0016` (IMO, combinatorics) — best match: infinite-often-equal ⟹ periodic, via
  downward-transport induction on an unbounded index set using an auxiliary windowed
  sequence. Crux move quoted above.
- `aimo-0051` (algebra/functional equations) — best match for the reframed cofinite
  target: finite-structure-bound ⟹ cofinite orbit, via window-capacity counting.
- `aimo-0098` (number theory) — weaker match: existential-witness-immateriality trick;
  offered as a fallback reframing only, not a strong structural analog.

### Prior progress
See `current.md` / `lemmas/singleton-side-fah.md` (read fully) — unchanged from round
8: Singleton-Side FAH certified (unconditional, zero exceptions, when F′ or F″ is a
singleton); general |F′|,|F″|≥2 case open, confirmed genuinely non-cofinite-by-brute-
force at the un-recruited core (a_1=4807, ~6% rate) — but note this 6% figure is
measured at S₀=Q (before Finite-Core-Theorem recruitment), a different core level than
where FAH is actually invoked in the finish (post-recruitment S₀ with witnesses n_A,
n_B already fixed); round 6's own re-test of the SAME seed at the recruited core found
0/10 and 0/151 failures. This discrepancy between round 6 and round 8's a_1=4807
numbers is not a contradiction (different S₀ levels, different extended types A′/B′)
but is worth the outliner flagging explicitly so no approach conflates "FAH fails at
the raw Q-level core" with "FAH fails at the level it's actually needed."

### Dead ends (do not retry)
Per current.md, unchanged: Two-Witness Intersection Uniqueness (Lemma-H branch
analysis), aimo-0678-style algebraic-recursion transplant (Witness Discontinuity
Obstruction), Fixed-Witness Divisor-Chain's dispatched dichotomy (branch (a) false),
seed-coupling-induction, all three recruitment-round-charging variants, Universal
Singleton Hypothesis. None of the leads in this report repeat these.

### Small-case / intuition notes
Conjecture only, not verified this round (no new computation run — deferred to
builder/outliner given the reframing is the main contribution here): if lead (a)'s
cofinite reframing is adopted, the exception count for a_1=4807's rogue pair should be
boundable by something like |Div(a_{n_A})| or |F′|·(a small constant) rather than
requiring literal zero — worth a builder checking whether the ~6% "failure rate" at the
un-recruited core is actually a *bounded absolute count* (not a bounded density) as n
grows, which is the precise thing the aimo-0051-style counting argument would need to
establish.
