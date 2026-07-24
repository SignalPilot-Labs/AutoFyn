## Status
unsolved

## Approaches tried
- **integer-monovariant-difference-identity** (round 14, new) — genuinely
  searched, from scratch, for a bounded monotone integer statistic of this
  problem's greedy process whose difference identity (in the style of crux
  `aimo-0134`) would pin down *which specific prime* eventually divides every
  sufficiently large term of a persistent type — i.e. a bypass of FAH/Symmetric
  FAH/Cofinite FAH/EEA that does not go through "which prime recurs" language
  at all. Independently re-derived aimo-0134's mechanism in full (see §1
  below), confirmed the outline's diagnosis that the literal transplant (an
  average of the *terms* `a_n`) fails outright because `a_n → ∞`, and then
  tried five candidate integer statistics of the **gap sequence**
  `g_n := a_{n+1} - a_n` and of auxiliary count/gcd statistics (§2). Every
  candidate falls into one of the three documented failure modes: (a) restates
  already-certified content (Persistent-Type Pigeonhole) with no new leverage;
  (b) is literally equivalent to gap (†) itself (boundedness of the statistic
  IS the open question, so "prove it stabilizes by integrality" is circular);
  or (c) is a bona fide new bounded monotone integer statistic but is proved
  (not just observed) to converge to a value that is **structurally forced to
  carry zero identity-level information** about which prime recurs. One
  candidate (§2.1, the naive running average of gaps) is additionally refuted
  computationally: on both documented rogue-pair seeds `a_1 = 4807` and
  `a_1 = 11305` it fails to be monotone at all (fluctuates up on
  roughly half of all steps), confirming in the concrete case what the general
  argument in §2.1 already shows. No counterexample to FAH was sought or
  found; no progress toward closing gap (†) is claimed. Verdict for this
  round: **RETHINK** — this specific technique family (integer-monovariant /
  difference-identity transplants of the aimo-0134 shape) is retired as a
  16th confirmed-dead mechanism against FAH/(†), on top of the 15 already on
  record. This is a genuine, honestly-obtained negative result, not a paper-
  over: the field of candidates checked is documented in full below so no
  future round re-tries any of them without a genuinely new ingredient.

## Current best
No new progress toward the WHOLE problem or toward closing gap (†) is
established by this approach. What follows is the honest record of the search
performed, so it is not repeated.

### §0. The target and why aimo-0134's shape is attractive here

The whole problem's target is eventual periodicity of the gap sequence:
`a_{n+T} = a_n + L` for all `n` beyond some threshold. Via the certified
**Gap–Periodicity Equivalence** (`lemmas/gap-periodicity-equivalence.md`),
this is equivalent to ordinary eventual periodicity of `(g_n)`. Every
mechanism tried in this workspace to date attacks this via "recruit a prime
`q`, show `q` divides literally every sufficiently large term of a fixed
persistent type" — the FAH/Cofinite-FAH/EEA family, now with 15 confirmed-
dead proof mechanisms (see `current.md`'s Rules history). The premise of
this approach is to look for a totally different kind of argument: crux
`aimo-0134` proves an eventually-constant conclusion for its own sequence not
by naming a divisor at all, but by (1) building an auxiliary INTEGER-valued
statistic `b_k` from the sequence's partial sums, (2) proving a genuine
per-step inequality `b_{k+1} < b_k + 1` from the sequence's own defining rule
(there: the bound `a_{k+1} ≤ k`), (3) using integrality of both `b_k` and
`b_{k+1}` to upgrade the strict inequality to `b_{k+1} ≤ b_k`, giving a
non-increasing sequence of nonnegative integers, hence eventual constancy by
the well-ordering of `ℕ`, and finally (4) inverting the difference identity
`a_k = (k+1)b_{k+1} - k b_k` to transfer that constancy back to the original
sequence. If an analogous statistic existed here, its stabilization might
give periodicity information "for free," without ever isolating a single
witness prime — a genuinely different top-level mechanism, not another
variant of FAH.

**Independent re-derivation of aimo-0134's proof (verifying the outline's
claim before building on it).** Source sequence: `a_k` with `a_{k+1} ≤ k`
by the problem's own rule (checked against the crux record above). Set
`b_k := (a_1+\dots+a_k)/k`. That `b_k \in \mathbb Z` is forced by the source
problem's own construction (the crux's `how_used` field: "an integer because
`k` divides the partial sum by definition of `a_k`" — this is a fact about
*that* problem's specific rule, not a generic truth about running averages).
From `(k+1)b_{k+1} = a_1+\dots+a_{k+1} = k b_k + a_{k+1}` and `a_{k+1}\le k`:
`(k+1) b_{k+1} \le k b_k + k`, so `b_{k+1} \le \dfrac{k b_k+k}{k+1}
= b_k - \dfrac{b_k-k}{k+1} \le b_k + \dfrac{k-b_k}{k+1}`. More simply:
`(k+1)b_{k+1} \le k b_k+k < (k+1)b_k+(k+1)`, so `b_{k+1} < b_k+1`; since both
sides are integers, `b_{k+1}\le b_k`. So `(b_k)` is non-increasing, bounded
below (by `0`, since all `a_k>0`), hence eventually constant at some value
`b`. Then for `k\ge` the stabilization index, `a_k = (k+1)b_{k+1}-k b_k =
(k+1)b - kb = b`. This independently confirms the outline's summary is
correct and the mechanism is exactly "integer + per-step inequality forces
monotone integer descent, then a difference identity inverts it."

### §1. Why the literal transplant fails, and the correct object to average

Our `a_n \to \infty` (Bounded Gap Lemma only bounds `g_n\le a_1`, it does not
bound `a_n` itself — indeed `a_n \ge a_1+(n-1)`, certified). So the running
average `(a_1+\dots+a_n)/n` grows without bound (it is `\ge` the average of
an increasing sequence tending to infinity, in fact `\to\infty` since
`a_n\to\infty` implies the Cesàro mean of `a_n` also `\to\infty`). It cannot
be a bounded statistic, so the transplant fails outright at the very first
required property. The natural fix, as the outline notes, is to average the
BOUNDED quantity in the problem — the gap `g_n := a_{n+1}-a_n \in
\{1,\dots,a_1\}` (Bounded Gap Lemma, certified) — instead of the unbounded
terms themselves.

### §2. Candidates tried, each refuted or ruled uninformative

**§2.1 — Running average of gaps, `b_n := (g_1+\dots+g_n)/n = (a_{n+1}-a_1)/n`.**

*Boundedness:* yes — `b_n \in [1, a_1]` since every `g_i` lies in that range,
so any average of them does too. Good start.

*Integrality:* in general **no**. Unlike aimo-0134's `b_k`, there is no
divisibility fact in our recurrence forcing `n \mid (g_1+\dots+g_n)`; the
rule `a_{n+1} = \min\{c>a_n : \gcd(c,a_i)>1 \ \forall i\le n\}` has no
built-in "correction toward a multiple of `n`" structure (this was flagged as
the load-bearing design question by the outline, and it genuinely fails: a
direct computation on both rogue-pair seeds below shows `b_n` is essentially
never an integer).

*Per-step inequality:* aimo-0134's forcing inequality comes from a specific
structural fact of ITS rule (`a_{k+1}\le k`, a bound on the new term BY THE
INDEX). Our rule has no counterpart: the new gap `g_{n+1}` is bounded only by
the fixed constant `a_1` (Bounded Gap Lemma), never by `n` or by any function
of `n` that shrinks relative to the current average. Concretely, one can
attempt the analogous computation:
`(n+1)b_{n+1} = n b_n + g_{n+1}`, so `b_{n+1} = b_n + \dfrac{g_{n+1}-b_n}{n+1}`.
For this to force `b_{n+1}\le b_n` (even approximately) one would need
`g_{n+1}\le b_n` for all large `n` — i.e. the NEXT gap is at most the RUNNING
AVERAGE gap so far. This is not a consequence of any certified lemma (Bounded
Gap Lemma only gives `g_{n+1}\le a_1`, a fixed constant, not `\le b_n`), and
there is no reason for it to hold: a run of many small gaps can be followed
by one large gap without violating any certified fact.

*Computational refutation (this round).* Directly simulating both documented
rogue-pair seeds (`a_1=4807`, with reported `|F'|,|F''|\ge 2`; and
`a_1=11305`, likewise) out to `n=2500` and computing the running average of
gaps at every step:

- `a_1=4807`: max gap 38, min gap 2; the running average of gaps
  **increases** at 1196 of the 2498 checked steps (≈48% of the time) — very
  far from monotone. The running average itself is converging (to
  ≈17.45, presumably the eventual mean gap over the true asymptotic period),
  but it does so by oscillating, not descending.
- `a_1=11305`: max gap 14, min gap 2; the running average increases at 998
  of 2498 steps (≈40%), same qualitative picture.

This directly and concretely confirms the general argument above: there is
no forced monotone descent, so this candidate fails criterion (a) of the
outline's search ("a genuine per-step inequality... not assumed by
analogy") outright, and independently fails computationally as well. **This
candidate is dead**, both in principle and on the documented rogue seeds.

**§2.2 — Running minimum of gaps, `M_n := \min_{1\le i\le n} g_i`.**

This candidate genuinely IS monotone (non-increasing, trivially: the minimum
over a larger index set is `\le` the minimum over a smaller one) and bounded
(`1\le M_n\le a_1` by the Bounded Gap Lemma), hence eventually constant at
some value `m^\*` — but by nothing deeper than the elementary fact that a
non-increasing sequence of positive integers bounded below must stop
decreasing after at most `a_1-1` steps (a standard descent argument, no
pigeonhole or new machinery needed). This is correctly monotone and
correctly bounded, so it passes the two formal requirements the outline
asked for — but it carries **no identity-level information**: knowing
`M_n=m^\*` for all `n\ge N` only says *no gap smaller than `m^\*` ever recurs
again* after `N`; it says nothing about which residue, which prime, or
whether `m^\*` itself recurs even once more. There is no difference identity
recovering an exact term or gap value from `M_n` and `M_{n-1}` alone (unlike
aimo-0134's `a_k=(k+1)b_{k+1}-kb_k`, which recovers the ORIGINAL term
exactly): `M_n - M_{n-1}` only ever tells you whether `g_n < M_{n-1}`, a
one-bit fact with no prime-identity content. **Fails criterion (c):**
provably uninformative for the FAH gap, even though genuinely monotone and
bounded.

**§2.3 — `gcd` of all terms so far, `D_n := \gcd(a_1,\dots,a_n)`.**

Monotone non-increasing (a divisor of more numbers is a divisor of fewer),
bounded (divides `a_1`), hence eventually constant by the same elementary
descent as §2.2 — again passing the outline's two formal requirements.
Checked computationally on both rogue seeds: `D_n` collapses to `1` after
just the second term in both cases (`a_1=4807`: `D_2=11\to D_3=1`;
`a_1=11305`: `D_2=5\to D_3=1`), and stays at `1` forever after. This is
correct but again **structurally uninformative by construction**: pairwise
non-coprimality (Free Facts, certified) says every PAIR of terms shares a
prime, but says nothing about a prime shared by ALL terms simultaneously —
there is no reason to expect `D_n>1` to persist, and the difference identity
one could write down (`D_n = \gcd(D_{n-1},a_n)`) carries no information about
which of the (varying) shared primes is doing the work at each step. **Fails
criterion (c)** even more sharply than §2.2 — it stabilizes almost
immediately, to the least informative possible value.

**§2.4 — Persistent-type count, `S_n := |\{\tau(1),\dots,\tau(n)\}|`
(number of distinct persistent Q-types visited among indices `1..n`).**

Flagged in advance by the outline as dead-on-arrival, and this round
confirms the diagnosis on inspection: `S_n` is monotone non-decreasing and
bounded above by `|\mathcal P|` (certified alphabet size, Persistent-Type
Pigeonhole), hence eventually constant — but "eventually constant" here is
*verbatim* the conclusion of the already-certified **Persistent-Type
Pigeonhole** (`lemmas/persistent-type-pigeonhole.md`), restated as an
integer statistic. No new per-step inequality is needed or available beyond
that already-certified pigeonhole argument, and no periodicity or
identity-level information follows from `S_n` stabilizing (it is an
existence statement — "eventually every index lands in the fixed set
`𝒫`" — with exactly the same shape as every mechanism already retired in
this workspace). **Fails criterion (a):** restates certified content,
supplies no new leverage. Not re-attempted further, per the outline's
instruction not to re-propose it without a genuinely new ingredient — none
was found.

**§2.5 — Recruited-core size, `S_n^{core} := |S_n^{core}|`
(size of the running recruited-prime core, `covering-system-construction`
Step 4c).**

Also flagged in advance as dead-on-arrival, and confirmed on inspection:
`S_n^{core}` is monotone non-decreasing by construction (recruitment only
adds primes, never removes them), but its BOUNDEDNESS — whether the
recruitment process ever stops adding new primes — is **exactly gap (†)
itself** (`current.md`'s "the single remaining crux gap (†)... iff the
process... halts"). Framing "prove `S_n^{core}` eventually constant via
integrality" is circular: integrality of a nonnegative-integer-valued set
size gives no traction on boundedness; boundedness of `S_n^{core}` is
*definitionally* what remains open. **Fails criterion (b).** Not
re-attempted further.

### §3. Diagnosis: why no candidate in this family can work

Comparing §2.1–§2.5, a structural pattern emerges, worth recording for
future rounds attempting the aimo-0134 transplant family in any other
disguise. aimo-0134's mechanism needs a statistic `S_n` with **all four**
of: (i) integer-valued by a genuine divisibility fact built into the rule
itself (not assumed); (ii) a per-step inequality of the shape
`(\text{new denominator})\cdot S_{n+1} \le (\text{old denominator})\cdot
S_n + (\text{something bounded by the SAME denominator, not a fixed
constant})`, so that dividing through gives a strict `<S_n+1` that
integrality then sharpens to `\le S_n`; (iii) boundedness that is *provable
independently of the open crux* (not equivalent to it); and (iv) a
difference identity recovering exact TERM-level (not just count-level)
information once `S_n` stabilizes. Every candidate checked above satisfies
at most two of these four simultaneously:

- §2.1 has (iii) [boundedness] but fails (i) [not integer] and (ii) [no
  forcing inequality — refuted both in principle and computationally].
- §2.2, §2.3 have (i)–(iii) [genuinely integer, monotone by an elementary
  fact, and bounded] but fail (iv): their stabilization values are, by
  construction, aggregates (a minimum, a gcd) that destroy exactly the
  per-occurrence prime-identity information the FAH gap needs; there is no
  difference identity of aimo-0134's shape recovering a specific term or
  divisor from them.
- §2.4 restates (iii) as the already-certified Persistent-Type Pigeonhole —
  no new (ii) is available beyond that pigeonhole argument, and no (iv)
  exists (it is a count statistic, not one from which a term value can be
  recovered).
- §2.5 fails (iii) outright — its boundedness is definitionally gap (†).

The root obstruction is that our recurrence's per-step legality test
(`\gcd(a_{n+1},a_i)>1` for ALL `i\le n`, `a_{n+1}` minimal) is, as the
`greedy-exchange-cost-potential` approach's own **Same-Type Free Facts
Vacuity** and **Selection-Rule Class-Blindness** observations already
established (certified, see `current.md` rounds 9 and 11), *class-blind*: it
never references WHICH prime realizes a shared factor, only THAT one exists.
Any integer statistic built purely from counts, minima, or gcds of the
resulting sequence inherits this same blindness — it can detect that
*something* stabilizes (an alphabet, a minimum gap, an overall gcd) without
ever being forced, by a genuine per-step algebraic identity, to reveal WHICH
prime is responsible. aimo-0134's setting has no such class-blindness
problem because its sequence has only one "kind" of object (integers, no
hidden discrete label like "which prime"); the difference identity there
recovers a NUMBER, not an IDENTITY, and a number is exactly what its problem
needed. Our problem's genuinely missing ingredient is identity-level
(existential-to-universal promotion for a SPECIFIC prime), which is a
different kind of gap than the numeric-stabilization gap this technique
family is built to close. This matches, from yet another independent
angle, the diagnosis first made by round 6's Lemma I and reconfirmed by
every one of the 15 mechanisms retired since: the missing ingredient is a
genuinely class-sensitive source of cross-occurrence information, which no
purely numeric monovariant (bounded, monotone, or otherwise) can supply by
itself.

### §4. Conclusion

No genuine third candidate (beyond the outline's two pre-rejected ones) was
found after a documented five-candidate search covering the natural
statistics available in this problem's structure (running average of gaps,
running minimum of gaps, overall gcd of all terms, persistent-type count,
recruited-core size). Two of the five (§2.1, §2.5) are refuted for
principled reasons plus, for §2.1, a direct computational check on both
mandated rogue-pair seeds; two more (§2.2, §2.3) are proved genuinely
monotone and bounded but shown to be structurally incapable of carrying
identity-level information, closing a possible loophole the outline had not
explicitly foreclosed; the fifth (§2.4) is confirmed to restate already-
certified content exactly as flagged in advance. This is an honest,
informative negative result: **the aimo-0134 integer-monovariant /
difference-identity technique family, as a whole, cannot close gap (†)**,
for a reason (§3) that generalizes past the five specific candidates tried —
the recurrence's own class-blindness (already certified in this workspace)
poisons any purely numeric (count/min/gcd/average) statistic built from it.
This is recorded as the **16th confirmed-dead mechanism** against
FAH/Symmetric FAH/Cofinite FAH/EEA, so no future round re-attempts any
transplant of this shape without a genuinely new ingredient that supplies
class-sensitive (not merely numeric) information.

## Full proof
Not present — Status is `unsolved`. This approach does not (and, per §3's
structural diagnosis, cannot in this family) close gap (†) or the whole
problem.

## Promotable lemmas
None proposed for certification as reusable machinery — every fact proved
this round (§2.2's and §2.3's monotonicity/boundedness, §3's diagnosis) is
either an immediate elementary consequence of already-certified lemmas
(Bounded Gap Lemma, Free Facts, Persistent-Type Pigeonhole) or a negative
/diagnostic finding about why a technique family fails, matching the
round-6/7/9/10/11 precedent that such diagnostic content is recorded in the
approach file and in `current.md`'s Rules history rather than certified as
portable machinery. If the reviewer judges the §3 "four-requirement
diagnosis" table worth certifying as a standing screening checklist for
future integer-monovariant attempts (analogous to the certified
Class-Blindness / Vacuity lemmas already in the lemma bank), that would be a
reasonable promotion, but this builder does not claim it rises to the level
of a new mathematical lemma beyond what §3 already states.
