## imo-2026-06 — lens: finiteness of Nec / self-sufficiency of Q_min

### Distinct openings
1. **Direct finiteness attack on Nec via "late recruitment is a finite phenomenon."**
   Numerics (below) show that in every tested seed, *all* new primes ever added
   to Nec are first witnessed by a pair $(i,j)$ with $j$ bounded by a modest
   index (never observed beyond $j=26$ across seeds up to $a_1\approx 2\times10^6$
   and sequences run out to 400 terms), and — crucially — pushing the same
   seed's simulation from 100 to 400 terms **adds zero new primes**. This
   suggests a genuine structural fact: only finitely many pairs among an
   initial "settling" prefix can ever be witnesses, and once the sequence's
   prime-recruitment pattern stabilizes, no pair of terms (however far out)
   ever again has a *singleton* prime intersection with a prime absent from
   the already-fixed Nec. A path to formalize: show that beyond some
   $N^*=N^*(a_1)$ every term $a_n$, $n>N^*$, has $R(a_n)\cap Q_{\min}$ already
   containing $\ge 2$ elements of $Q_{\min}$ common with *every* earlier
   accepted-type term (redundant covering), so no new singleton pair can ever
   form. This is essentially a sharper, quantitative form of the still-open
   "$Q_{\min}$ self-sufficient" question, not an independent route — but the
   numerics make it look tractable via an explicit induction that tracks,
   for each term, its *number* of shared Nec-primes with the "generic" class
   of terms, and shows this redundancy count is nondecreasing / eventually
   $\ge 2$.

2. **A "prefix vs. tail" split of Nec.** Since $\mathrm{Nec}\subseteq Q$ for
   any valid $Q$ (certified `nec-necessity.md`), and empirically every
   witness pair $(i,j)$ has $i$ *itself* small (the smaller index of the
   pair is what matters, not $j$ — see data: for $a_1=375$ the witness for 7
   is $(7,26)$, i.e. $i=7$ is still fairly small even though $j=26$ is
   larger), a promising reformulation is: **bound $\mathrm{Nec}$ by bounding
   the set of "generative" first-indices**, i.e. show that only pairs with
   $\min(i,j)\le F(a_1)$ for some explicit function $F$ (not necessarily
   $\mathrm{rad}(a_1)$ or $\omega(a_1)$ — those are refuted, see Dead ends)
   can ever contribute a *new* prime to Nec. This narrows the search to
   understanding the first $F(a_1)$ terms combinatorially (a finite,
   in-principle-checkable computation for each $a_1$), rather than an
   unbounded tail argument.

3. **Reframe via redundant-covering density.** Instead of asking "is Nec
   finite," ask the complementary quantitative question: for each prime
   $p\in R(a_1)\cup\mathrm{Nec}$, does the *density* (or eventual constant
   count) of terms divisible by $p$ stabilize, and does the pairwise
   "collision" of two terms' Nec-type primes become redundant (≥2 shared)
   once each individual prime's recruiting set has "enough" members? This
   connects to a pigeonhole/pattern argument: if $k$ primes are all
   eventually periodic-divisors of the tail (by `lambda-stabilization.md`,
   $\Lambda_n$ stabilizes for the *adjacent*-gcd primes $\le\mathrm{rad}(a_1)$
   only — but Nec's *extra* recruited primes like 19, 103, 97 are NOT
   adjacent-gcd primes, they show up only in non-adjacent pairs), a natural
   open sub-question is whether these extra recruited primes *also*
   eventually stabilize into $\Lambda$-like periodic behavior, or whether
   they are truly one-off "patches." All tested extra primes (7 for 375, 103
   for 194287, 97 for 13871, 17 for 194287) recur many times in the
   simulated range once recruited (i.e. they become permanent dividers of
   infinitely many terms, consistent with eventual periodicity), which is
   itself unproven but numerically robust.

### Candidate technique(s)
- Explicit combinatorial/pigeonhole bound on the number of pairs with
  singleton intersection among the first $M$ terms, as a function of the
  number of primes in play (relates to `hitting-set-lemma.md`'s
  reformulation of self-sufficiency as a set-cover/hitting-set problem).
- An induction on $\omega(a_1)$ combined with the still-open
  `renormalization-induction-on-seed` approach's smaller-instance reduction
  — possibly Nec's finiteness is easier to prove *inductively* on the number
  of distinct primes in $a_1$ than directly.
- A direct "eventually every large term has $\ge2$ elements of a fixed
  finite $Q_0$" argument via the `Adjacent-Link Lemma` + `lambda-stabilization.md`
  (these already give periodicity of *adjacent*-pair gcds within $\{p\le
  \mathrm{rad}(a_1)\}$); the open extension is proving the same kind of
  redundancy for *non-adjacent* pairs and for primes outside
  $\{p\le\mathrm{rad}(a_1)\}$.

### Cheap-kill candidates
- **Any conjectured closed-form bound on $|\mathrm{Nec}|$ or on the
  recruitment index purely in terms of $\mathrm{rad}(a_1)$ or $\omega(a_1)$
  is refuted** by the $a_1=375$ data point: $\mathrm{rad}(375)=15$,
  $\omega(375)=2$, yet the prime 7 (itself $\le\mathrm{rad}(375)$, so not
  even a "big" recruit) is only witnessed at $j=26$, far beyond what a
  linear-in-$\omega$ or linear-in-$\mathrm{rad}$ bound like the refuted
  `bounded-lookahead-insufficiency.md` family would predict. Do not propose
  such a bound without accounting for this counterexample.
- Checking $\gcd(a_i,a_1)$ alone is insufficient (already covered by
  `adjacent-link-neighborhood-insufficient.md`); no new cheap win found
  along "look only at pairs with index 1 or adjacent indices."

### Knowledge-base entries to use
- Compactness / pigeonhole on finite alphabets (generic technique,
  underlies `lambda-stabilization.md` and the `state-compactness-pigeonhole`
  approach) — worth revisiting `knowledge_base.md`'s pigeonhole/finite-state
  entries (not re-read verbatim here, but this is the same family of tool
  already in active use by the population).
- `hitting-set-lemma.md` — reframes the self-sufficiency half of the
  question (part 2 of the two open questions) as hitting-set existence; any
  finiteness result on Nec directly narrows the ground set for this hitting
  problem.

### Analogous past problems (cruxes)
Searched `number_theory` cruxes under `divisibility-and-gcd`,
`sequences-and-recurrences`, `pigeonhole`, `invariants-and-monovariants` for
"greedy smallest-integer gcd sequence" / "eventually periodic gcd sequence"
patterns. **No strong analog found.** The closest tangential hits:
- `aimo-0421` (divisibility-and-gcd): "When every prime divides only
  finitely many elements of an infinite set, only finitely many elements
  share a factor with a fixed pair, so a third element coprime to both can
  be chosen." This is the *opposite* direction (constructing coprimality
  from prime-scarcity) but is a reminder of the contrapositive fact
  relevant here: since in our problem *every* prime in play must divide
  infinitely many terms eventually (periodicity), Nec's primes are exactly
  the "boundary" primes that fail to be redundant only finitely often — the
  same kind of finite/infinite-support dichotomy, worth keeping in mind as
  a proof vocabulary, not a transplantable lemma.
- `aimo-0212` (divisibility-and-gcd): "every prime dividing a polynomial's
  values lies in a fixed finite set ⟹ polynomial is constant" — different
  setting (polynomial values), not applicable, but same *shape* of claim
  (finite prime support forces rigid structure) as what Round 4's
  `nec-necessity.md` already established (finite $Q\Rightarrow$ Nec finite).
  Doesn't help prove Nec IS finite, though.
- No corpus problem matches the "greedy EKG-style smallest-integer sequence
  with a global pairwise-gcd condition" shape closely enough to transplant a
  crux move. Treat this as an open research-style gap, not one solvable by
  pattern-matching a known olympiad trick.

### Prior progress
- `nec-necessity.md` (certified): $\mathrm{Nec}\subseteq Q$ for any valid
  finite self-sufficient $Q$; hence Nec finite is *necessary* for the
  central existence claim (if Nec is infinite, NO finite self-sufficient
  $Q$ can exist at all — this would actually let us conclude the problem is
  FALSE as an approach-route, which cannot happen since the problem is true,
  so proving Nec is finite is fair game and consistent, but note: this
  logical direction only tells us Nec-finite is *necessary*, not sufficient —
  part 2 of the open question, $Q_{\min}$'s self-sufficiency, is separate
  and still fully open even conditional on Nec being finite).
- `hitting-set-lemma.md`: self-sufficiency $\iff$ hitting every
  $W(i,j)=R(a_i)\cap R(a_j)$.
- All of round 3-4's specific closed-form candidates for $Q$
  ($\{p\le\mathrm{rad}(a_1)\}$, $\Lambda$, $\Lambda\cup Q_0$,
  $\Lambda^{(K)}$ for bounded $K$) are refuted or unproven — see Dead ends.

### Dead ends (do not retry)
- `bounded-radical-refutation.md`: $Q=\{p\le\mathrm{rad}(a_1)\}$ is not
  self-sufficient in general ($a_1=375$ witness).
- `chain-transitivity-obstruction.md`: adjacent-chaining induction cannot
  prove self-sufficiency (pure set-theoretic obstruction).
- `adjacent-link-neighborhood-insufficient.md`: $Q=\Lambda$ or
  $\Lambda\cup Q_0$ fails (index-corrected $a_1=99$ witness,
  $(a_3,a_5)=(105,110)$).
- `bounded-lookahead-insufficiency.md` / `windowed-epsilon-automaton-failure.md`:
  no fixed bounded-window statistic (of recent terms or of a "gap to next
  multiple" indicator) can certify or predict the recruitment/exceptional
  step — confirmed again here: my own numerics reinforce this since the
  recruitment index for prime 7 at $a_1=375$ ($j=26$) is far outside any
  small fixed window one would guess from $\omega(a_1)=2$.
- Any bound on the *recruited prime's size* by $\max R(a_1)$ or
  $\mathrm{rad}(a_1)$: refuted by $a_1=194287$ recruiting $103>89$, and by
  $a_1=375$ recruiting nothing above rad but delaying to $j=26$ — i.e. both
  "prime size" and "recruitment index" are unbounded by the naive guesses
  simultaneously in different examples, so no single simple parameter of
  $a_1$ governs recruitment.

### Small-case / intuition notes (all CONJECTURE, not proof)
Computed $(a_n)$ by direct greedy simulation (python, exact integers, `sympy.factorint`)
for many seeds, out to 100–400 terms, and computed Nec exactly (all pairs $i<j$
with $|R(a_i)\cap R(a_j)|=1$):

| $a_1$ | $\mathrm{rad}(a_1)$ | Nec | recruited beyond rad | max first-appearance index $j$ |
|---|---|---|---|---|
| 6 | {2,3} | {2} | — | 3 |
| 15 | {3,5} | {2,3,5} | 2 | 3 |
| 35 | {5,7} | {2,3,5,7} | 2,3 | 4 |
| 105 | {3,5,7} | {2,3,5,7} | 2 | 4 |
| 375 | {3,5} | {2,3,5,7,19} | 2,7,19 | **26** |
| 1001 | {7,11,13} | {2,7,11,13} | 2 | 4 |
| 1155 | {3,5,7,11} | {2,3,5,7,11} | 2 | 6 |
| 2431 | {11,13,17} | {2,3,7,11,13,17} | 2,3,7 | 6 |
| 13871 | {11,13,97} | {2,3,11,13,97} | 2,3 | 10 |
| 1009091 | {97,101,103} | {2,3,97,101,103} | 2,3 | 5 |
| 194287 | {37,59,89} | {2,3,17,37,59,89,103} | 2,3,17,103 | 10 |

Key observations (conjectural, from finite-window simulation only — not proof):
1. **In every tested case, $|\mathrm{Nec}|$ is small (single digits) and
   stabilizes very early** (extending the simulation from ~100 to ~400
   terms adds zero new primes in every case tried, including the
   "slow" $a_1=375$ case). This is strong evidence Nec is always finite,
   but the mechanism is not yet understood well enough to bound it a priori.
2. **The recruitment index is NOT controlled by $\mathrm{rad}(a_1)$ or
   $\omega(a_1)$ alone** — $a_1=375$ (small $\omega=2$) recruits as late as
   $j=26$, far later than seeds with $\omega=3,4$. Manual trace of the
   $a_1=375$ sequence shows *why*: prime 7 divides terms 2,7,12,20,26,30,...
   but only term 7 ($=399=3\cdot7\cdot19$) fails to also carry a 2 or a 5;
   every other early 7-multiple term also shares 2 or 5 with $a_{26}=490$,
   so the *singleton* intersection is a fine combinatorial coincidence
   (which 7-divisible terms also avoid 2 and 5), not something readable off
   $\omega(a_1)$ or $\mathrm{rad}(a_1)$ directly. A genuine bound on Nec
   would need to control this kind of "avoids 2 and avoids 5" combinatorics
   directly, likely via a counting/pigeonhole argument on how many terms in
   a window can simultaneously avoid several fixed small primes (related in
   spirit to Jacobsthal-function covering ideas, per `jacobsthal-covering-bound`,
   but that approach's specific closed-form mechanisms are already refuted).
3. Once a prime enters Nec, it appears to become a **permanent, recurring**
   divisor of the tail (e.g. prime 7 keeps appearing as a factor of many
   later terms after index 26 in the $a_1=375$ run) — consistent with, but
   not proof of, eventual periodicity with that prime in the final period's
   support.
4. No seed tested (including deliberately adversarial multi-large-prime and
   widely-spaced-prime-gap seeds) produced unbounded or still-growing Nec
   at 400 terms; this is evidence for finiteness but only checked to finite
   depth, so it remains conjecture, not proof, and cannot rule out some
   pathological $a_1$ recruiting a genuinely unbounded/never-stabilizing
   Nec (no such example is known, and none of the population's approaches
   or my search found one).
