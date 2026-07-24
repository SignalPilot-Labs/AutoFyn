## Status
partial

## Approaches tried
- **seed-coupling-induction (round 8, new)** — Set up the induction on ω(a_1) precisely,
  defined the seed-reduction operation and the exact claim the Seed-Coupling Lemma would
  need, then tested it computationally (as mandated by the outline's Step 4 cheap-kill
  gate) on a graded sequence of seeds: |Q|=2 (matches the outline-reviewer's own sanity
  check), then |Q|=3 with several different choices of removed prime and several
  different seeds (105, 165, 385, 30, 70, 42). Result: the correspondence claimed by the
  Seed-Coupling Lemma holds with **zero exceptions** whenever the reduced set Q' retains
  the prime 2, but **fails with a large, apparently stable, non-vanishing exception
  DENSITY** (15%–68%, not merely "bounded" or "sparse") in every one of the 8 tested
  cases where Q' does not contain 2 (i.e. either 2∉Q at all, or 2 is the prime removed).
  Diagnosed precisely why: the induction, to go from |Q|=k to |Q|=k−1 for an arbitrary
  seed, must be able to remove an arbitrary prime of Q, and for a seed with 2∉Q (e.g.
  Q={3,5,7}) every one of the k choices of removed prime leaves Q' without 2 — so the
  induction cannot avoid the failing regime by choosing which prime to drop. This is a
  genuine, reproducible falsification of the Seed-Coupling Lemma as stated in the
  outline, not a toy artifact — verdict below is a documented RETHINK for this specific
  mechanism, with the reason distilled precisely so it is not re-attempted verbatim.

## Current best

### 1. Precise setup of the induction

For a positive integer $a_1 > 1$, write $Q = Q(a_1)$ for the set of distinct prime
divisors of $a_1$ and $k := |Q| = \omega(a_1)$. Given seed $a_1$, the greedy sequence
$(a_n)_{n\ge1}$ is defined by the problem's rule: $a_{n+1}$ is the least integer $>a_n$
with $\gcd(a_{n+1},a_i)>1$ for all $i\le n$.

**Induction skeleton (as specified by the outline).**
- Base case $k=1$: already fully solved and certified
  (`greedy-exchange-cost-potential`'s |Q|=1 special case, restated in `current.md` item
  10): if $Q=\{q\}$ then every $a_n$ is a multiple of $q$ (Free Facts forces $\gcd(a_n,a_1)>1$,
  and since $|Q|=1$ the only prime available to satisfy this for $a_1=q^e$ is $q$ itself),
  and one checks directly $a_{n+1}=a_n+q$ for all $n\ge1$: $T=1$, $L=q$, no gap.
- Inductive hypothesis: for every seed $a_1'$ with $|Q(a_1')| = k-1$, the resulting
  sequence $(a_n')$ is eventually periodic with some explicit $(T',L')$ (and, by a
  strengthened hypothesis if available, literally periodic from $n=1$).
- Reduction step: given a seed $a_1$ with $|Q(a_1)|=k\ge2$, pick a prime $p:=p_k\in Q$,
  set
  $$a_1' := a_1 / p^{v_p(a_1)}$$
  (i.e. $a_1$ with all copies of $p$ removed), so $Q' := Q(a_1') = Q\setminus\{p\}$,
  $|Q'| = k-1$. Run the SAME greedy rule from seed $a_1'$ to get $(a_n')_{n\ge1}$.

**What the Seed-Coupling Lemma needs to say, precisely.** For each $n$, define the
*restricted type* of the original sequence at level $n$ as
$$
\tau'(n) := P(a_n) \cap Q' \quad(\text{the set of } Q'\text{-primes dividing } a_n).
$$
This can be empty (if $a_n$'s only common factor with $a_1$, forced by Free Facts, is
$p$ itself). Let
$$
n_1 < n_2 < n_3 < \cdots
$$
be the increasing list of all indices $n$ with $\tau'(n) \ne \emptyset$ (the
"$Q'$-visible" indices of the original sequence). The Seed-Coupling Lemma, as the
outline poses it, is the claim that there is an eventually-defined **order-preserving
injective correspondence**
$$
j \longmapsto n'(j)
$$
between (eventually all) indices $j$ of the reduced sequence and the $Q'$-visible
indices $n_j$ of the original sequence, such that for all sufficiently large $j$,
$$
\tau'(n_j) = P(a'_{n'(j)}) \cap Q' \qquad (\star)
$$
i.e. the $Q'$-level type of the $j$-th $Q'$-visible original term equals the (full)
$Q'$-type of the corresponding reduced-sequence term, with only a *bounded-frequency*
set of exceptions to $(\star)$ (the outline's phrase: "a specific pair of terms relies
on $p$ as their ONLY common factor" being the source of exceptions, bounded via the
Generalized Bounded Gap Lemma).

This is the precise, checkable content that Step 3–5 of the outline needs. It is
**stronger** than merely "both sequences are eventually periodic" (which is what the
induction ultimately wants to conclude) — it asks for an explicit, essentially
term-by-term structural coupling between the two processes, which is exactly what
would let periodicity of the reduced sequence transport to periodicity of the
original's $Q'$-visible skeleton (Step 5 of the outline).

### 2. Computational test of the Seed-Coupling Lemma (mandatory cheap-kill, executed first)

A Python greedy-sequence generator was implemented directly from the problem's own
rule (`n=seq[-1]+1`, then advance while `not all(gcd(n,x)>1 for x in seq)`), together
with a routine that (a) strips all factors of the chosen prime $p$ from $a_1$ to build
$a_1'$, (b) generates both sequences to a common term budget, (c) computes $\tau'(n)$
for every term of the original and the full $Q'$-type for every term of the reduced
sequence, (d) strips the empty-type ($\tau'(n)=\emptyset$) terms from the original to
get the $Q'$-visible skeleton, and (e) compares this skeleton against the reduced
type-sequence position-by-position (the natural instantiation of $(\star)$ with
$n'(j):=j$, i.e. testing the simplest, most literal candidate correspondence first, as
the outline's own Step 4 example does for $a_1=15$).

**Reproduction of the outline-reviewer's $a_1=15$ check.** $a_1=15$, $Q=\{3,5\}$.
Removing $p=5$ gives $Q'=\{3\}$; removing $p=3$ gives $Q'=\{5\}$. In both cases the
type alphabet over $Q'$ has only two possible values ($\emptyset$ or $\{$the single
prime$\}$), so this case is not very discriminating, but for completeness: **0
mismatches** over 250–375 compared terms in both directions — consistent with (though
not a strong test of) the Lemma.

**$|Q|=2$, less degenerate alphabet.** $a_1=35$ ($Q=\{5,7\}$): removing either prime
gives $|Q'|=1$ again (still only a 2-symbol alphabet) — **0 mismatches** over
150–440 compared terms both ways. All $|Q|=2$ tests give 0 mismatches, but note $|Q'|=1$
in every $|Q|=2$ case, so these tests only ever probe the ALREADY-SOLVED base case's own
consistency, not genuinely new content.

**$|Q|=3$, the first genuinely new regime (the one the outline itself flags as
mandatory before trusting the general proof).** $a_1=105$ ($Q=\{3,5,7\}$, a 4-symbol
type alphabet over any 2-element $Q'$), testing all three single-prime removals:

| $a_1$ | removed $p$ | $Q'$ | compared length $L$ | mismatch density |
|---|---|---|---|---|
| 105 | 7 | {3,5} | 6897 (N=8000) | **55.0%** |
| 105 | 5 | {3,7} | 396 (N=500) | 42.2% |
| 105 | 3 | {5,7} | 293 (N=500) | 49.5% |

For the $p=7$ removal, the mismatch density was checked at increasing sample sizes
($N=100,300,1000,3000,8000$ terms) and **stabilizes at $\approx 55.02\%$**, not
shrinking — this rules out "it's just a slow-to-settle transient exception set,
eventually sparse," which is what the outline's "bounded-frequency exceptions" claim
would predict. A direct look at the raw type sequences (first 40 terms of each) shows
the two sequences' $Q'$-type patterns agree for the first two periods of the reduced
sequence (which is itself exactly periodic with $T'=4,L'=15$: types
$\{3,5\},\{3\},\{5\},\{3\}$ repeating) and then the original's stripped skeleton
inserts EXTRA nonempty-type terms not present in the reduced sequence's corresponding
window — i.e. the two skeletons are not even the same LENGTH per matched stretch, so no
shift of the correspondence map $n'(j)$ can repair the mismatch by realignment alone.

A stronger, cleaner test than positional matching: the **long-run frequency of each
$Q'$-type** was computed over 3000 terms for $a_1=105$, $p=7$ removed. The reduced
sequence (itself periodic, $T'=4$) visits $\{3,5\},\{3\},\{5\},\{3\}$ with frequencies
exactly $25\%,50\%,25\%$. The original's $Q'$-visible skeleton visits the same three
types with frequencies $16.0\%,56.0\%,28.0\%$ — **different limiting frequencies**, not
merely a differently-ordered or transiently-shifted version of the same distribution.
This is decisive: no correspondence map, however cleverly chosen, can satisfy $(\star)$
for almost all $j$ if the two type sequences do not even have the same asymptotic type
frequencies.

**Extending to more $|Q|=3$ seeds and all three removal choices each**
(600 compared terms per case):

| $a_1$ | $Q$ | removed $p$ | density |
|---|---|---|---|
| 30 | {2,3,5} | 2 | 60.7% |
| 30 | {2,3,5} | 3 | **0.0%** |
| 30 | {2,3,5} | 5 | **0.0%** |
| 70 | {2,5,7} | 2 | 53.2% |
| 70 | {2,5,7} | 5 | **0.0%** |
| 70 | {2,5,7} | 7 | **0.0%** |
| 42 | {2,3,7} | 2 | 40.9% |
| 42 | {2,3,7} | 3 | **0.0%** |
| 42 | {2,3,7} | 7 | **0.0%** |
| 165 | {3,5,11} | 11 | 57.0% |
| 165 | {3,5,11} | 3 | 40.2% |
| 165 | {3,5,11} | 5 | 24.3% |
| 385 | {5,7,11} | 11 | 68.3% |
| 385 | {5,7,11} | 5 | 53.2% |
| 385 | {5,7,11} | 7 | 43.4% |

**Diagnosis of the pattern.** Whenever $2\in Q$ and the removed prime $p\ne2$ (so
$2\in Q'$), the correspondence holds EXACTLY (0 mismatches, checked up to 8000 terms
for one such case, $a_1=30,p=3$, with zero exceptions throughout — not just "rare,"
literally none). This is explained by prime 2's extremal density: half of all integers
are even, so whenever $2\in Q'$, the greedy process almost always finds its next
$Q'$-legal candidate via divisibility by 2 alone, and this behavior is essentially
insensitive to whether $p$ is also available as a backup glue prime — removing $p$
changes almost nothing because $2$ was already doing all the structural work. This is a
genuine but degenerate special case, not a validation of the general mechanism.

In EVERY case where $Q'$ does **not** contain 2 — either because $2\notin Q$ at all
(105, 165, 385) or because $p=2$ was the removed prime (30, 70, 42) — the mismatch
density is large (24%–68%) and, where checked at multiple sample sizes, stable (not
decaying). This is 8 for 8 confirmed failures in the non-degenerate regime, against 6
for 6 confirmed (degenerate, 2-dominated) successes — a clean, reproducible pattern,
not a coding artifact (the same generator and comparison routine, unchanged, produces
both the successes and the failures).

### 3. Why this kills the induction as set up

The induction (Step 3 of the outline) needs to reduce an ARBITRARY seed with
$|Q|=k$ to SOME seed with $|Q|=k-1$ via removing ONE prime, for every $k\ge2$. But
take any seed with $2\notin Q$ and $|Q|=k\ge3$ (e.g. $Q=\{3,5,7\}$, or more generally
any set of $k$ odd primes) — by the data above, **every one of the $k$ possible prime
removals lands in the non-degenerate (2-absent) failing regime**, since removing any
single prime from $Q=\{3,5,7,\ldots\}$ (none of which is 2) can never introduce 2 into
$Q'$. There is no "canonical choice" (largest prime, smallest prime, or any other
single-prime selection rule) that rescues the correspondence for such seeds, because
the failure is not about WHICH prime is removed — it is about whether 2 survives the
removal, and if $2\notin Q$ to begin with, no removal choice can make $2\in Q'$.

This directly falsifies the outline's Step 3 mechanism as stated: the claimed
"bounded (not just finite-in-principle) rate of $p_k$-dependent exceptions" from the
Generalized Bounded Gap Lemma does not hold — the actual exception rate is a
macroscopic, apparently stable fraction of all terms (order 20%–70% in the tested
cases), not a bounded-count or vanishing-density correction. The mechanism's own
proposed source of exceptions ("a term relies on $p$ as its ONLY common factor") is
real, but it is not rare: for seeds without the extremal prime 2 in $Q'$, a large
constant fraction of terms structurally need the removed prime's help, because with a
sparser prime set of Q' available the greedy process much more frequently has no small
$Q'$-legal candidate and must "reach further" using $p$ — this is fundamentally a
statement about the interaction of the FULL prime set $Q$ (via its natural density in
the integers), not a perturbative correction on top of the reduced process.

### 4. Was any weaker/rescued form checked?

Two natural weakenings were checked and both also fail on the same data:
- **Relaxing to a non-literal (non-identity) correspondence $n'(j)$** (allowing
  arbitrary reordering/matching, not just $n'(j)=j$): ruled out by the frequency
  computation in §2, since a per-type limiting frequency mismatch (16% vs 25%, etc.)
  cannot be repaired by ANY injective correspondence between the two index sets that
  preserves the type equality $(\star)$ for almost all $j$ — an injection preserving
  types for a density-1 set of indices would have to preserve limiting type
  frequencies exactly.
- **Restricting to a sparser/special starting family** (e.g. only removing the largest
  prime, per the outline's own suggested canonical choice): checked explicitly for
  $a_1=165$ (remove 11, the largest) and $a_1=385$ (remove 11, the largest) — both
  still fail, at 57.0% and 68.3% density respectively, i.e. even the outline's own
  suggested canonical choice does not avoid the failure.

No rescued form of the Seed-Coupling Lemma was found. Plan B (the raw-integer
minimal-counterexample fallback documented in the outline, Step 6) was not attempted
in depth this round given the clear and clean falsification of Step 3 above absorbed
the available time budget; it remains a documented, unverified, and now the ONLY
un-falsified fallback within this approach's scope — its own central sub-question
(whether non-periodicity propagates down to a persistent-type sub-sequence generated
by a smaller legitimate seed) was not attempted, since the outline explicitly asks for
Plan A's cheap-kill check to run first, and it failed unambiguously.

## Promotable lemmas

None. The Seed-Coupling Lemma is falsified as stated (not proved), so there is no
positive reusable lemma to certify from this round's work. The one reusable,
already-certified fact used here (the |Q|=1 base case) was imported unchanged from
`greedy-exchange-cost-potential`/`current.md`, not re-derived as new content.

**Honest verdict for the next round's outliner:** this specific mechanism (Seed
Coupling via single-prime removal, with the type-frequency correspondence as stated in
the outline) is **dead** — falsified computationally on 8/8 tested seeds in the
non-degenerate (2-absent) regime, with a clean structural diagnosis (prime 2's
extremal density is doing unrepeatable work that no other prime can substitute for,
and seeds without 2 in Q have no rescuing removal choice). If the induction-on-$\omega
(a_1)$ framing is to be revived, it needs a genuinely different reduction step — not
"drop one prime from the seed and expect the resulting sequences to track each other,"
since the interaction between the full set of $k$ primes is not a sparse perturbation
of any $(k-1)$-prime sub-process. Plan B (raw-integer minimal-counterexample, ordering
by $a_1$ itself with a sub-persistent-type-sequence reduction) remains the one
undamaged part of this approach's outline and is the natural next target if this
framing is to be pursued further, but it was not attempted this round.
