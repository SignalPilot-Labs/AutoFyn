# Outline-review — round 11

## Verification method
Read `current.md`, all 13 approach files, all 32 lemma files (focused reads on
`minimality-tautology-lemma.md`, `adjacent-multiple-blocking.md` (Lemma K),
`confined-gcd-lemma.md`, `cofinite-sufficiency-lemma.md`), the three round-11
explorer reports, and the outliner's report. Independently re-derived the key
claims rather than trusting the outliner's text, and ran a fresh numerical check
(Python/sympy) on Approach 1's literal construction, reconstructing the greedy
sequence for `a_1=4807` from scratch.

## Approach 1 (`greedy-exchange-cost-potential` REVISE — Forced-Escape Blocking
Construction): scoping confirmed correct, but literal construction is
magnitude-doomed — decisive computational kill, 13th mechanism

**Scoping check (the task's specific concern).** Confirmed: this construction is
genuinely scoped as Lemma-K-style blocking-index extraction, not a full-legality-
competitor construction. Its Step 3 deduction ("if `c` illegal against `j<n`, no
`S₀`-prime can be shared between `a_j` and `a_n`") is a valid, checkable algebraic
consequence of the CRT-matching (`p|a_n ⟺ p|c` for `p∈S₀`) — independently
re-derived here, correct. This is NOT the disqualified full-legality-competitor
shape the Minimality Tautology Lemma (`lemmas/minimality-tautology-lemma.md`)
kills in one line; that lemma's certified scope explicitly carves out
blocking-index-based (Lemma K-style) mechanisms as still open in principle.

**But the outline's own "Risk 2" contains a live error.** It flags, as "the most
promising sub-case to check computationally FIRST": *if `c` is fully legal
against every `j<n` and `c<a_n`, this directly contradicts `a_n`'s minimality and
would PROVE Cofinite FAH directly.* This is not merely unlikely — it is a
**logical impossibility**, unconditionally, by the certified Minimality
Tautology Lemma's own Corollary (no integer strictly between `a_{n-1}` and `a_n`
can ever be fully legal against every earlier term, for any `n`, by definition).
This branch can never fire, for this or any construction; recorded as a
correction so no builder wastes effort "checking" it.

**Independent numerical kill (more serious than the outline's flagged risks).**
Ran the actual construction (seed `a_1=4807`, rogue pair `A'={3,5,19}` vs.
`B'={2,11}`, `q*=17`, `S₀={2,3,5,7,11,19,23,73,127}`, `M=∏S₀≈9.36×10⁹`) on all
three sampled `A'`-occurrences past `n_B` (`n=561,1114,2223`). Result: **`c ≥ a_n`
in all three, by roughly 8 orders of magnitude** (`q*M ≈ 1.59×10¹¹` vs. observed
local gaps `a_n−a_{n-1} ∈ {15,3,19}`). This is not a sampling artifact: `q*M` is a
product of the (currently 9) primes of `S₀` with no relationship to the local gap
size, which by the certified Bounded/Generalized Bounded Gap Lemma depends only
on `a_1` and the index difference (here 1), not on `|S₀|`. Even the much smaller
modulus `M=a_1` alone gives `q*a_1=81719`, still ≫ the local gaps. **Structural
conclusion: Lemma K's dichotomy never reaches its informative branch (b), because
that branch requires `a_{n-1}<c<a_n`, which a full-S₀-signature CRT glue
essentially cannot achieve once `|S₀|≥2` (and gets worse as `S₀` grows with later
recruitment rounds).** This is a genuine, previously-untried, correctly-scoped
construction that fails for an orthogonal (magnitude, not legality) reason — a
clean new negative result (**CRT Magnitude Obstruction**), recorded in
`approaches/greedy-exchange-cost-potential.md`. Retiring this as the workspace's
**13th confirmed-dead FAH mechanism**.

**Verdict:** cut the literal construction from the build queue (it is doomed, not
merely gap-bearing). Redirect the builder: write up the CRT Magnitude Obstruction
as a rigorous, complete negative result (retiring mechanism 13 cleanly, matching
the standard set by mechanisms 9–12), explicitly correct the Risk-2 error, and do
NOT attempt to patch the construction with a different modulus without first
addressing why any multi-prime-matching CRT glue faces the same order-of-
magnitude problem (checked above for two moduli sizes, both fail).

## Approach 2 (`covering-system-construction`, ADVANCE, no new mechanism)
Confirmed: no new mechanism dispatched this round; three explorer lenses plus
Approach 1's (now-dead) construction all confirm this approach sits at the same
wall (Collateral-Safety Theorem's reduction to base-type-pair FAH/Symmetric FAH).
The outliner's conditional note (repair Round 8's Fixed-Witness Divisor-Chain IF
Approach 1 succeeds) is now moot — Approach 1's construction died this round, so
that combination is not worth dispatching. Kept live for ranking continuity only,
not in the build set.

## Approach 3 (`sieve-density-exception-bound`, NEW): genuinely targets the open
quantity, not moot — but needs a mandatory pre-build screening check

**Mootness check (the task's second specific concern).** Confirmed NOT moot: this
approach targets Cofinite FAH (`|E|<∞`, `E:={n>n_B:ρ(n)=A',q*∤a_n}`), the actual
open crux per the certified Cofinite Sufficiency Lemma — distinct from, and not
already answered by, the Finite Core Theorem/Collateral-Safety Theorem (which
settle the *different*, already-free question of eventual prime-core finiteness).
The outliner's own diagnosis of why the round-1 `density-sieve-contradiction`
file is not revivable (its gap literally is the now-free core-finiteness
question) is correct and independently re-verified here by reading that file's
Step 3/5 and comparing to `finite-core-theorem.md` + `collateral-safety-
theorem.md`.

**New required check, not in the outliner's report.** Approach 3's sub-route (a)
("Mertens' estimate... the greedy process cannot systematically prefer the
sparser `D_bad` classes") is at serious risk of being a **class-blind** argument
in the precise sense already proved fatal by the certified **Escape-Cost Vacuity
Theorem** (`lemmas/escape-cost-vacuity.md`, `sandwich-genericity-theorem.md`):
any argument built only from magnitude/counting premises that don't reference a
specific divisor class or prime identity per occurrence cannot yield a
class-sensitive conclusion. A generic "sparse classes get squeezed out" density
heuristic, phrased only in terms of aggregate counts over `S₀∪F''`, is exactly
this shape. Added as a **mandatory pre-build screening step** in the approach
file: the builder must identify a class-sensitive ingredient before investing in
the Mertens machinery, or record in one paragraph that sub-route (a) is dead on
arrival by this Theorem (a cheap check that could save a full round of wasted
sieve computation, the same way this Theorem already retired mechanism 10).

**Verdict:** genuinely new technique family, correctly targets the open crux,
worth building — with the screening requirement made explicit up front.

## Other approaches
No changes proposed to `confined-competitor-construction` (dead, RETHINK
standing), `witness-index-descent`, `recruitment-round-charging`,
`scalar-well-ordering-lock-in`, `reversible-transition-map` (all previously
dead-ended, correctly not re-proposed), or the three never-expanded approaches
(`density-sieve-contradiction`, `hypergraph-transversal`, `seed-coupling-
induction`) — inspected briefly, no new information this round changes their
status.

## Ranking actions taken
- Registered new approach `sieve-density-exception-bound` (Elo 1500 cold start).
- Wrote `approaches/sieve-density-exception-bound.md` (skeleton + mandatory
  screening check) since the outliner's report proposed it but did not write the
  file.
- Appended a round-11 section to `approaches/greedy-exchange-cost-potential.md`
  documenting the CRT Magnitude Obstruction (13th dead mechanism) and correcting
  the Risk-2 error, so no future round re-attempts either.
- Ran head-to-head Elo update: `covering-system-construction` beats
  `greedy-exchange-cost-potential` (highest-developed, no new dead branch this
  round) and beats `sieve-density-exception-bound` (untested vs. established);
  `greedy-exchange-cost-potential` beats `sieve-density-exception-bound` (has
  substantial proven content — Window Resolution Lemma, Growing-Constraint
  Obstruction, now CRT Magnitude Obstruction — vs. sieve-density's fully-open key
  lemma); both beat the dead-ended `confined-competitor-construction`. Resulting
  order: `covering-system-construction` (1855) > `greedy-exchange-cost-potential`
  (1780) > `confined-competitor-construction` (1524) > `sieve-density-exception-
  bound` (1491, cold-start-adjacent).

## Summary
Fourteen mechanisms now confirmed dead in total (twelve from rounds 6–10, plus
this round's Automaton/Successor-Claim-isomorphism confirmation not counted as a
new distinct mechanism per the automaton explorer's own recommendation, plus the
newly-killed CRT Magnitude Obstruction as mechanism 13). No FAH counterexample
found anywhere, on any seed, across 11 rounds — strong evidence FAH is true; the
difficulty remains entirely in proving it with a genuinely new identity-level
(not magnitude-level, not tautological) source of cross-occurrence information.
Build set below dispatches (1) a clean write-up of the newly-found negative
result (valuable, retires a mechanism formally) and (2) the one live genuinely-
new-technique-family approach, with an explicit screening requirement attached
so it cannot silently repeat mechanism 10's failure mode.

build set: greedy-exchange-cost-potential, sieve-density-exception-bound
