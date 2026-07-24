## imo-2026-06

### Distinct openings (route: minimality of the greedy rule, applied directly to FAH)

1. **First-failing-index minimal-counterexample (dispatch idea (a)).** Fix a rogue pair
   (A',B'), Lemma-G prime q, and let n* = the smallest n > n_B with ρ(n)=A' and q∤a_n
   (assume for contradiction it exists). By the certified Generalized Bounded Witness
   Lemma, a_{n*} must still be divisible by SOME p ∈ F' \ {q} (F' := P(a_{n_B})\S₀, a
   FIXED finite set — this containment is already unconditionally certified, it is not
   new). The only way to get a contradiction from minimality of a_{n*} is to exhibit an
   explicit integer c with a_{n*-1} < c < a_{n*} that is (i) legal against every
   a_1,...,a_{n*-1} and (ii) divisible by q. **This is EXACTLY
   `greedy-exchange-cost-potential`'s "Attempt 2c"**, already carried out in full in
   round 6 and shown to fail via the certified negative result **Lemma F** ("minimality
   bounds magnitude, not type" — no certified lemma produces a *small* safe candidate,
   only large multiples of a1·q-scale moduli) and generalized in **Lemma I**
   ("Non-Exclusivity of Witness Recruitment" — no composition of Free Facts /
   Generalized Bounded Witness / Gap Lemmas / Critical Prime Dichotomy can promote an
   existential "some prime of F' works" into an identity "q specifically works"). I
   independently re-derived why: Lemma A's construction gives a competing safe
   candidate at modulus Θ(a1·q), and q is typically comparable to or larger than a1
   in magnitude in the observed data (e.g. a1=4807, q=17: modulus ~82000 vs actual gaps
   Θ(a1)~4800) — so the "safe" competitor is generically much LARGER than the actual
   greedy choice, never smaller. **Verdict: this specific idea is a dead end, not
   because it wasn't tried, but because it WAS tried and a proof of its failure exists.**
   Do not re-dispatch it verbatim; any revival needs a genuinely finer competitor
   construction (see opening 3).

2. **Competitor analysis via "what smaller value could a_n have been" (dispatch idea
   (b)).** Same content as (1) — the two dispatch ideas (a) and (b) collapse to the
   identical mechanism once formalized (the "alternative smaller value" IS the
   competing legal candidate of (1)). No new leverage found beyond what Lemma F/Lemma I
   already cover.

3. **Genuinely new candidate: exploit the "blocking data," not just the upper gap
   bound.** Every skipped integer c in (a_{n-1}, a_n) is illegal for a REASON — some
   specific earlier index i ≤ n-1 has gcd(c, a_i)=1. This is a rich source of
   information (a certificate per skipped candidate) that NONE of the four certified
   tools currently use — they only ever use the POSITIVE fact "a_n itself is legal
   against everyone," never the NEGATIVE fact "every smaller candidate is illegal
   against SOMEONE." A genuinely new tool in this direction would need to show that
   *if* q had failed to divide a_n, the specific reason every q-divisible candidate
   below a_n got blocked is itself impossible (e.g., by pinning the blocking index to
   one of finitely many core-type terms and deriving a contradiction from THEIR
   factorizations). I could not construct this in the time available — flagging it as
   an unexplored resource, not a completed mechanism.

4. **Reversing which side is analyzed: apply minimality to a_{n_B} itself (the
   witness), not to a hypothetical failing A'-occurrence.** All existing analysis
   (Lemma G, Lemma H, Lemma I) treats a_{n_B} as a fixed integer and only extracts its
   static factorization F'. None of it uses that a_{n_B} was ITSELF chosen by the
   greedy rule as the smallest legal successor of a_{n_B - 1}. In principle this could
   constrain F' "from below" (why greedy didn't pick something smaller with a smaller
   outside-core factor set) — but any such argument again needs a smaller *legal*
   competitor, hitting the identical Lemma-F obstruction. I checked this collapses to
   the same wall; not a genuinely separate route without a new competitor-construction
   tool.

### Candidate technique(s)
No certified technique closes FAH. The dispatch's two suggested mechanisms are both
subsumed by the already-executed and already-diagnosed-dead Attempt 2c / Lemma F /
Lemma I. A future attempt needs either (i) a fundamentally tighter competitor
construction (modulus far smaller than a1·q — not currently available from any
certified lemma), or (ii) a tool that uses the *negative* information of why skipped
candidates are illegal (opening 3), which is unexploited territory.

### Cheap-kill candidates
None obvious for FAH itself — it is empirically bulletproof (0 counterexamples across
every seed tested by any agent, including my own fresh probes below). No parity/size/
pigeonhole shortcut was found; this matches the population's own repeated conclusion.

### Knowledge-base entries to use
`knowledge_base.md`'s pigeonhole/extremal-principle entry (already the engine behind
every certified lemma in this workspace); no other untried KB entry surfaced as
obviously relevant to FAH specifically — the KB's generic "minimal counterexample"
template is exactly what dispatch ideas (a)/(b) instantiate, and it is what has already
failed (see above).

### Analogous past problems (cruxes)
Queried `past_crux_moves_database.json` filtered to `number_theory` +
`size-bounding-and-descent` / `extremal-principle` / `processes-and-algorithms` /
`invariants-and-monovariants` (122 candidates), plus a targeted scan for
"eventually"/"sufficiently" + "divid"/"gcd"/"prime" language.

- **aimo-0712** (algebra, `sequences-and-recurrences` / `extremal-principle`) — genuinely
  interesting template, worth flagging even though the problem is different in kind
  (polynomial recurrence, not gcd). Its crux: "Apply the extremal principle to the
  minimum of an integer quantity that equals an average of copies of itself, forcing
  every term in the averaging window down to the minimum and propagating it" — i.e.
  once a minimal gap is attained, an averaging IDENTITY forces the whole window to
  equal the minimum, and this propagates forward to ALL later indices. This is
  structurally the kind of "local minimality forces uniform value, then propagates
  forever" result FAH needs (FAH is exactly a propagate-forever claim), but our problem
  has no algebraic averaging identity analogous to aimo-0712's `sum of k gaps = k ·
  (other gap)` — the transfer is NOT direct, flagged as a template shape, not a
  transplantable lemma.
- **aimo-0090** (number_theory, `divisibility-and-gcd` / `size-bounding-and-descent`) —
  "iterate the same additive closure on two same-colored elements of opposite parity to
  force every sufficiently large integer into that color." Different setup (a genuine
  closure/coloring problem, not greedy gcd), but conceptually close to what Symmetric
  FAH needs: an explicit STEP (there, "+2m"; here, hypothetically "the next occurrence
  of type A' after establishing q once") that, once triggered, propagates the property
  to every later instance. The problem's own machinery (Free Facts alone) does NOT give
  this closure step for our problem (checked: nothing certified propagates "q divided
  occurrence m" to "q divides the next occurrence m'" — this is exactly
  `greedy-exchange-cost-potential`'s Attempt 2b, independently confirmed dead: "the
  induction has no engine"). Not directly usable, but the shape (identify an explicit
  forcing step, not a size/index measure) is worth keeping in mind.
- **aimo-0477** (number_theory, `p-adic-valuation` / `divisibility-and-gcd`) — "track
  gcd(fixed term, current term) and show it divides the next one, producing a
  divisor-chain bounded by the fixed term that must stabilize." A genuinely different
  monovariant shape (an ASCENDING divisor chain bounded above by a fixed integer, hence
  eventually constant) from the three size/index descents already tried and killed in
  this workspace (round 3's |A'|+|B'|, round 5's witness-index, this round's implicit
  magnitude-only bounds). Concretely: define d_n := gcd(q^k, a_n) or, more relevantly,
  track how gcd(a_{n_B}, a_n) evolves as n ranges over A'-occurrences — since
  gcd(a_{n_B}, a_n) always divides the FIXED integer a_{n_B}, it lies in a bounded
  divisor lattice. I checked this numerically (a1=4807): the outside-S0 part of
  gcd(a_{n_B}, a_n) is always exactly {17} or {13,17} for A'-occurrences tested — i.e.
  it does NOT vary freely, consistent with (but not a proof of) a stabilizing-divisor
  picture. This is the single most promising *unexplored* structural angle from the
  corpus: unlike the three already-dead well-orderings, "gcd against ONE FIXED witness
  term, viewed as a divisor of that fixed term" is monotone in the RIGHT direction (it
  can only gain factors as evidence accumulates, and is capped by ω(a_{n_B}) — a small
  fixed number) rather than being an unbounded/refinement-manufactured quantity. Not
  attempted as a full mechanism here (recon only, per role) — recommend the outliner
  investigate whether a chain gcd(a_{n_B}, a_n) for successive A'-occurrences n can be
  shown non-decreasing (in the divisibility order) and hence eventually constant at
  a_{n_B}'s full "compatible part," which if it always includes q would directly give
  FAH's tail behavior. Caution: this needs an actual monotonicity proof (not yet
  established) — Free Facts alone gives gcd(a_{n_B},a_n)>1, no monotonicity across
  different n.
- Also checked `aimo-0030` (Banana game) per round-5's prior note — already correctly
  flagged as non-transferable (rules file entry #20); not re-proposed.

### Prior progress
See `current.md` ROUND 6 sections in full. Summary: (†) is unconditionally reduced
(Collateral-Safety Theorem, certified) to base-type-pair-level termination, which is
now pinned exactly to FAH + Symmetric FAH. FAH: for a rogue pair (A',B') with Lemma-G
prime q and n_A<n_B, q divides a_n for EVERY n>n_B with ρ(n)=A' (not just infinitely
many). 0 counterexamples across 7+ seeds / ~90 records, both sides, independently
reconfirmed 4 times by different agents including the critical |F'|=2 case (a1=4807).
Three proof mechanisms (Lemma H branch analysis, inductive chaining, exchange/
minimality) all fail for the identical diagnosed reason (Lemma I).

### Dead ends (do not retry)
- Dispatch ideas (a) and (b) as literally stated — both ARE `greedy-exchange-cost-
  potential`'s round-6 "Attempt 2c" (exchange/minimality at the first failing index),
  already executed and proved dead via Lemma F + Lemma I. Re-dispatching this without a
  genuinely new competitor-construction tool (small modulus, not a1·q-scale) will just
  reproduce the same failure.
- Inductive chaining across successive same-type occurrences ("q divided the last
  occurrence, so it divides the next") — Attempt 2b, proven to have "no engine": Free
  Facts between two A'-occurrences only forces a shared S0-prime (trivial, since both
  have extended type A'), giving zero information about primes outside S0.
- Direct Lemma H branch analysis at a hypothetical failing index — Attempt 2a, shown
  Lemma H is "nearly vacuous at large indices" (branch (a), the stripped-value-drops
  case, is the generic case and gives no exclusion of any specific prime).
- All the recruitment-round-charging framings (ω(a1)/Ω(a1) charging, growth-rate
  charging) — confirmed dead ends round 6, unrelated to but consistent with this
  round's finding that no magnitude-only argument can pin a specific prime.

### Small-case / intuition notes (conjecture, not proof)
- Fresh numerical probes this round (a1 = 1517, 2465, 3289, and 12 more products of 2-3
  mid-size primes from {5,...,31}, none previously tested in the workspace, N=2500-4000
  terms): **zero rogue pairs found** in 14/15 fresh seeds (only a1=187, already a known
  seed, showed one — found incidentally while scanning, not counted as fresh
  confirmation). This is consistent with, but does not newly test, FAH itself (FAH only
  applies when a rogue pair exists) — it does add further (weak) support to the
  separate "V=∅ is the common case" pattern noted in prior rounds, though sample size
  here is small and seeds were not adversarially chosen for missing multiple small
  primes as the round-2 rule recommends; a future round should specifically target
  seeds missing 2-3 of {2,3,5,7} while containing several larger primes to stress-test
  both V≠∅ frequency and FAH more aggressively.
- Direct FAH re-verification on the |F'|=2 seed a1=4807 (rogue pair A'={3,5,19},
  n_A=6, B'={2,11}, n_B=7, F'={13,17}, q=17): scanned A'-side occurrences for n=7..9000
  (14 total) — q=17 divides **all 14/14**; the OTHER element of F' (13) divides only
  **1/14** (exactly at n=n_B=7 itself, where both 13 and 17 happen to divide a_7 by
  construction of F'). This is a clean, freshly-computed data point (not reused from
  round 6's report) showing 13 essentially never recurs on the A'-side after the
  witness index, while 17 recurs with 100% frequency — sharp empirical asymmetry
  between the "correct" q and the "wrong" element of F', worth noting as it suggests
  whatever mechanism eventually proves FAH must explain this asymmetry structurally
  (e.g. why q=17, not 13, is "preferred" — nothing in the current certified toolkit
  distinguishes them a priori, per Lemma I).
