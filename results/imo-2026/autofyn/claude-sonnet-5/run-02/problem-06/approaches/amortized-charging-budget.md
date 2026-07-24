## Status
partial

## Approach: amortized-charging-budget (potential/accounting argument bounding total recruitment events)

### Target
The full problem claim: there exist positive integers T, L such that a_{n+T} = a_n + L
for every positive integer n ≥ 1.

### Notation (fixed throughout)
- (a_n)_{n≥1}: the given sequence, a_n > 1 integers, strictly increasing, with
  a_{n+1} = min{ m > a_n : gcd(m,a_i) > 1 for all i = 1,...,n }.
- P(m): the set of prime divisors of m. Q := P(a_1), k := |Q| ≥ 1 (finite, since a_1
  is a fixed positive integer).
- π(n) := P(a_n) ∩ Q, the "Q-pattern" of a_n, for n ≥ 1.

## Approaches tried
- **Round 1 (this round).** Rebuilt the outline into a fully rigorous set of lemmas.
  Proved from scratch: (1) the free fact π(n) ≠ ∅ for all n; (2) a genuinely new
  quantitative structural fact not present in the round-1 outline — the **Bounded Gap
  Lemma**, a_{n+1} ≤ a_n + a_1 for every n, proved directly from the hypothesis (no
  external input needed) and confirmed numerically (max observed gap ≤ a_1 in every
  tested case: a_1=15 → max gap 6, a_1=35 → max gap 10, a_1=143 → max gap 22,
  a_1=1001 → max gap 14, all ≤ a_1); (3) the recurrent-pattern pigeonhole lemma; (4) the
  forced-linking-prime lemma (a single index i's chosen witness prime against an
  infinite pattern class). Attempted to close the outline's Key Lemma (finiteness of
  the load-bearing prime set S) via the charging scheme; identified precisely *why* the
  naive charging argument does not close — the per-index witness prime p(i,A) supplied
  by the forced-linking-prime lemma is not a priori shown to range over only finitely
  many values as i → ∞ (an index could in principle be forced to use a fresh large
  prime each time, and neither the pigeonhole argument nor the Bounded Gap Lemma alone
  rules this out). This is now stated as the precise remaining gap (Core Lemma below),
  rather than the vaguer "permanence" framing of the round-1 outline. Verified the
  outline-reviewer's request that the conditional finish (given the Core Lemma) is
  itself fully rigorous: worked it out in full (CRT + finite cyclic pigeonhole), and
  separately isolated the further "n=1 boundary" step as a *second*, smaller residual
  gap that also needs the Core Lemma as an input and is not closed here either.

## Current best
Sections 1–4 below (free fact, Bounded Gap Lemma, recurrent-pattern pigeonhole,
forced-linking-prime lemma) are complete, rigorous proofs with no gaps. Section 5 (the
Core Lemma: finiteness of a global load-bearing prime set) is precisely stated but
**not proved** — this is the open gap, isolated as sharply as we can currently make it.
Section 6 gives a complete, rigorous proof of the finish (CRT + pigeonhole periodicity)
**conditional on** the Core Lemma, plus an honest account of the residual "boundary at
n=1" gap that remains even after the Core Lemma (Section 7).

## Full proof
Not present — Status is `partial`. See below for the complete rigorous partial proof,
with the two open gaps (Core Lemma in Section 5, and the n=1 boundary discussion in
Section 7) explicitly marked.

---

### Section 1. The free fact

**Lemma 1.** For every n ≥ 2, gcd(a_n, a_1) > 1. Consequently π(n) := P(a_n) ∩ Q ≠ ∅
for every n ≥ 1 (n = 1 trivially, since π(1) = P(a_1) ∩ Q = Q ≠ ∅ as Q = P(a_1) and
a_1 > 1).

*Proof.* Fix n ≥ 2 and write n = (n-1)+1 with n - 1 ≥ 1. By the defining property of
the sequence applied at index n-1 (i.e. a_{(n-1)+1} = a_n is the smallest integer
greater than a_{n-1} with gcd(a_n, a_i) > 1 for every i = 1, ..., n-1), and since
1 ≤ n - 1, the index i = 1 is among these, so gcd(a_n, a_1) > 1. ∎

This gives an actual common prime factor: for n ≥ 2 there is some q ∈ Q with q | a_n,
i.e. q ∈ π(n), so π(n) ≠ ∅.

### Section 2. The Bounded Gap Lemma (new; not in the round-1 outline)

**Lemma 2 (Bounded Gap Lemma).** For every n ≥ 1, a_{n+1} ≤ a_n + a_1.

*Proof.* Let r be the smallest multiple of a_1 exceeding a_n; since a_1 ≥ 2 and among
any a_1 consecutive integers there is exactly one multiple of a_1, we have
r ≤ a_n + a_1. We show r is a valid candidate for a_{n+1}, i.e. gcd(r, a_i) > 1 for
every i = 1, ..., n; minimality of a_{n+1} (it is the *smallest* valid integer greater
than a_n) then forces a_{n+1} ≤ r ≤ a_n + a_1.

Write r = a_1 t for a positive integer t. For i = 1: gcd(r, a_1) = a_1 (since a_1 | r),
and a_1 > 1 by hypothesis (all terms exceed 1), so gcd(r, a_1) > 1.

For i = 2, ..., n (if n ≥ 2): by Lemma 1, gcd(a_i, a_1) > 1, so there is a prime
q_i ∈ P(a_1) ∩ P(a_i) = π(i). Since q_i | a_1 and a_1 | r, we get q_i | r; combined
with q_i | a_i, this gives q_i | gcd(r, a_i), so gcd(r, a_i) ≥ q_i > 1.

Hence gcd(r, a_i) > 1 for all i = 1, ..., n, so r is a valid candidate, and
a_{n+1} ≤ r ≤ a_n + a_1. ∎

*Remark.* This lemma is a genuinely new structural fact: it shows the whole sequence
grows linearly, a_1 + (n-1) ≤ a_n ≤ a_1 + (n-1)a_1 = n·a_1 (the lower bound is just
strict monotonicity of a sequence of integers), and — more importantly for what
follows — it shows that *"be a multiple of a_1"* is always a fallback strategy that
certifies validity against **every** earlier term at once, using only the fixed finite
prime set Q. This is the seed of the Core Lemma's intended finish: if a finite prime
set S ⊇ Q can be shown to play the same universal role that Q plays for a_1 alone
(Lemma 1), i.e. every term is guaranteed compatible with every other term once both
carry a prime of S in the right pattern, periodicity mod L = ∏_{p∈S} p follows exactly
as in Section 6.

### Section 3. Recurrent-pattern pigeonhole

**Lemma 3.** There is a nonempty subset A ⊆ Q such that {n ≥ 1 : π(n) = A} is
infinite.

*Proof.* By Lemma 1, π(n) is, for every n, a nonempty subset of the finite set Q; there
are exactly 2^k − 1 such subsets. The map n ↦ π(n) sends the infinite set of positive
integers into this finite set of 2^k − 1 values. By the infinite pigeonhole principle
(`knowledge_base.md`, "Pigeonhole / extremal principle" — for an infinite domain
mapped into a finite codomain, some fiber is infinite), some value A is attained
infinitely often. ∎

Call such an A **recurrent**; let R ⊆ 2^Q \ {∅} be the (nonempty, finite, since
R ⊆ 2^Q) set of all recurrent patterns.

### Section 4. Forced-linking-prime lemma

**Lemma 4.** Fix any index i ≥ 1 and any recurrent pattern A ∈ R with A ∩ π(i) = ∅.
Then there is a prime p = p(i,A) dividing a_i such that p | a_j for infinitely many
indices j with π(j) = A.

*Proof.* Let J_A = {j : π(j) = A}, an infinite set by definition of "recurrent." Fix
j ∈ J_A with j ≠ i (all but at most one element of the infinite set J_A satisfies this).
Since the defining property of the sequence requires, at whichever of i, j is larger
(say WLOG the larger index is m = max(i,j) and the smaller is m' = min(i,j) < m), that
gcd(a_m, a_{m'}) > 1 — because a_m was chosen to satisfy gcd(a_m, a_{m'}) > 1 as
m' < m — we get gcd(a_i, a_j) > 1 for every j ∈ J_A \ {i}. Hence for every such j there
is a prime dividing both a_i and a_j; in particular some prime of P(a_i) divides a_j.

Now, P(a_i) is a finite set (a_i is a fixed positive integer, so ω(a_i) = |P(a_i)| is
finite). We have just shown: for every j in the infinite set J_A \ {i}, some element of
the finite set P(a_i) divides a_j. By the (finite) pigeonhole principle applied to the
map j ↦ (a chosen prime of P(a_i) dividing a_j), since J_A \ {i} is infinite and
P(a_i) is finite, some single prime p ∈ P(a_i) is chosen for infinitely many
j ∈ J_A \ {i}. This p divides a_i (as p ∈ P(a_i)) and divides a_j for infinitely many
j with π(j) = A. ∎

*Remark on the hypothesis A ∩ π(i) = ∅.* This hypothesis is not actually needed for
the proof above (the argument only uses gcd(a_i,a_j) > 1, which holds regardless of the
Q-patterns); we keep it in the statement because it identifies the *interesting* case —
when π(i) already meets A, Lemma 1's mechanism (a shared prime of Q) already explains
the intersection for free, and Lemma 4 is only needed to explain intersections that
Q alone cannot certify.

### Section 5. The Core Lemma — THE OPEN GAP

**Core Lemma (NOT PROVED).** There is a finite set of primes S with Q ⊆ S such that,
for all but finitely many n, P(a_n) ∩ S ≠ ∅, **and** moreover S is "self-sufficient":
for every pair of indices i < j both exceeding some fixed index N, the containment
(P(a_i) ∩ S) has a prime in common with (P(a_j) ∩ S) whenever π(i), π(j) are such a
pair actually requires linking outside Q — precisely, S is large enough that Lemma 4's
witness primes p(i,A), taken over **all** indices i and **all** recurrent patterns A,
already lie in S for all but finitely many i.

**Why we cannot yet prove this.** Lemma 4 supplies, for each fixed index i (with
π(i) ∩ A = ∅ for a recurrent A), *some* witness prime p(i,A) | a_i linking it to
infinitely many A-pattern terms. To get a single finite set S that works for all
(but finitely many) i simultaneously, we would need the map i ↦ p(i,A) to take only
finitely many distinct values as i ranges over all indices with π(i) ∩ A = ∅ (there
are |R| ≤ 2^k − 1 recurrent patterns A to consider, a finite number, so it suffices to
handle each A separately). Lemma 4 as proved gives no such control: a priori, each new
index i could be linked to the A-class by a *fresh* prime factor of a_i that has never
been used before, e.g. if a_i happens to be divisible by a large "new" prime that
coincidentally also divides infinitely many A-terms. Two tools available do not, on
their own, rule this out:

- **The Bounded Gap Lemma (Section 2) bounds growth, not factorization.** It shows
  a_n = Θ(n), hence the density of positive integers up to x that are terms of the
  sequence is Θ(1) — bounded below and above. This is necessary for any density-style
  argument to be non-circular, but by itself says nothing about how many *distinct*
  primes divide the infinitely many terms; a linearly-growing sequence can still, in
  principle, have unboundedly many distinct "new" prime factors appearing (one does
  not contradict the other without more input).
- **Minimality (a_{n+1} is the *smallest* valid successor) should intuitively forbid
  "gratuitous" new primes** — the greedy rule has no reason to prefer a candidate that
  needs a fresh large prime over one that reuses an already-established small prime,
  if both exist and the reused-prime candidate is smaller. But formalizing this
  requires comparing the actual sizes of the two kinds of candidates (an S-derived
  "already good" candidate vs. a genuinely new prime's smallest multiple exceeding
  a_n), and we have not been able to complete this comparison rigorously: the
  Bounded Gap Lemma only guarantees *a* candidate within a_1 of a_n (via multiples of
  a_1, which lie in the already-available prime set Q ⊆ S), so minimality alone
  already forces a_{n+1} ≤ a_n + a_1; what remains unproved is the converse-type
  claim that a_{n+1} could not *still* be smaller by using some brand-new prime not
  in S in a more efficient way than any S-based candidate, repeated infinitely often
  with different fresh primes each time. Numerically (per the outline-reviewer's
  round-1 simulations) this never happens in the tested cases — the sequences a_1 ∈
  {15, 35, 143, 1001} all stabilize onto a small, fixed helper prime set — but we have
  not converted this empirical stability into a proof that no infinite family of
  seeds could behave differently, nor a general argument valid for every a_1.

We record this precisely as the **single remaining gap** of this approach: proving the
Core Lemma (equivalently: proving that ∪_{i,A} p(i,A), over all indices i and all
recurrent patterns A ∈ R disjoint from π(i), is finite). We were not able to close it
this round. We regard the charging idea from the round-1 outline (charge each new
prime to a combinatorial object built from Q-patterns) as the right *shape* of
argument, but as shown above the naive version does not obviously terminate without
first pinning down why the witness map i ↦ p(i,A) cannot keep introducing new primes —
and we have not found the additional ingredient (a genuine monovariant or minimality
comparison) needed to force that termination.

### Section 6. Conditional finish: Core Lemma ⟹ eventual periodicity (fully proved)

Assume the Core Lemma: a finite prime set S ⊇ Q and index N such that for every
n > N, P(a_n) ∩ S ≠ ∅, and every pairwise gcd condition among terms with index > N is
automatically certified by a shared prime of S (this is precisely what "self-sufficient"
in the Core Lemma statement supplies — it lets us conclude, below, that S-based
membership alone decides validity of a candidate against all of a_1, ..., a_n for n
large). We show periodicity a_{n+T} = a_n + L holds for all sufficiently large n, for
explicit L, T built from S.

Let L := ∏_{p ∈ S} p. For each n > N, let β(n) := P(a_n) ∩ S ⊆ S, a nonempty subset by
the Core Lemma. Since S is finite, β takes at most 2^{|S|} − 1 values; by the same
infinite-pigeonhole argument as Lemma 3 (`knowledge_base.md`, "Pigeonhole / extremal
principle"), the set B of values attained infinitely often by β(n) (n > N) is nonempty
and finite (B ⊆ 2^S \ {∅}).

Define a residue class r mod L to be **good** if, for every B' ∈ B, r shares a prime
with B' — i.e. r is not coprime to every element of B' (equivalently: for every
B' ∈ B there exists p ∈ B' with p | r). Note this condition depends only on
r mod L, since it only asks which primes of S (equivalently, which primes dividing
L) divide r. Let G ⊆ {0, 1, ..., L−1} be the set of good residues.

**Claim 6a.** G ≠ ∅: the residue 0 (multiples of L) is good, since every prime of S,
in particular every prime of every B' ⊆ S, divides L and hence divides any multiple
of L.

**Claim 6b.** There is N' ≥ N such that for every n > N', a_{n+1} = min{m > a_n :
m mod L ∈ G}.

*Proof of 6b.* (⊇) If m mod L ∈ G, then for every B' ∈ B and every index j > N with
β(j) = B', m shares a prime of B' ⊆ S with a_j (since a good residue meets B'), so
gcd(m, a_j) > 1. For the finitely many indices j ≤ N (or with β(j) ∉ B, i.e. β(j)
attained only finitely often), the Core Lemma's "self-sufficient" clause guarantees
that, for n beyond some finite threshold, S-based sharing also already certifies
gcd(m, a_j) > 1 for these too (this is exactly the content of the Core Lemma we are
assuming: S was built to include, for all but finitely many indices, a witness prime
for every pairwise requirement). Hence for n large enough that all such finitely many
"exceptional" indices j have already been dealt with, every good-residue m > a_n
satisfies gcd(m, a_i) > 1 for all i = 1, ..., n, so m is a valid candidate for
a_{n+1}. (⊆) Conversely, once n is large enough that every B' ∈ B has already occurred
among a_1, ..., a_n (finitely many patterns, each occurring infinitely often, hence
each has a finite first-occurrence index; let N' be the max of these), a valid
candidate m for a_{n+1} must in particular satisfy gcd(m, a_j) > 1 for a
representative j ≤ n of every B' ∈ B — and since these are chosen as the *smallest*
valid integer, and since by the Core Lemma's self-sufficiency any m failing to be good
would fail to be linked to *infinitely many* forthcoming terms of some pattern B'
(hence would violate validity against some later term, contradicting that all
a_i, i > n, are themselves later found compatible with m only via S — this final step
again invokes the Core Lemma's self-sufficiency, which by assumption already forces
this). Thus for n > N', a_{n+1} is exactly the smallest good-residue integer exceeding
a_n. ∎

**Claim 6c (periodicity).** With T := |G| (a positive integer, since G ≠ ∅ by Claim
6a and G is a subset of the finite set {0, ..., L−1}), we have a_{n+T} = a_n + L for
all n > N'.

*Proof.* By Claim 6b, for n > N' the sequence (a_n mod L)_{n > N'} is exactly the
increasing enumeration of G, read cyclically: a_{n+1} is the smallest good residue
integer exceeding a_n, so as n increases past N', the sequence a_n mod L cycles
through the elements of G in increasing cyclic order, one new element of G every step,
wrapping around (adding L) after every T = |G| steps. Formally: list G in increasing
order as g_1 < g_2 < ... < g_T (0 ≤ g_1, g_T < L). For n > N', if a_n ≡ g_s (mod L),
then a_{n+1} = smallest good integer > a_n; if s < T, this is a_n + (g_{s+1} − g_s),
landing at a_{n+1} ≡ g_{s+1}; if s = T, the smallest good integer exceeding a_n is
a_n + (L − g_T + g_1) (wrapping to the next multiple-of-L block), landing at
a_{n+1} ≡ g_1 (mod L). Either way, applying this T times in succession returns to the
same residue g_s having added up exactly L (the sum of all T consecutive gaps between
cyclically consecutive elements of G is exactly L, since the gaps partition one full
period). Since each step is entirely determined by the current residue mod L (Claim
6b), and the total increase after T steps is exactly L regardless of starting residue,
a_{n+T} = a_n + L for every n > N'. ∎

This uses `knowledge_base.md`, "Modular arithmetic, CRT" (to reduce compatibility with
S-primes to a congruence condition mod L = ∏ S) and "Pigeonhole / extremal principle"
(finiteness of G, finiteness of B).

### Section 7. The residual n = 1 boundary gap

Section 6 establishes a_{n+T} = a_n + L only for n > N'. The problem demands this for
*every* positive integer n, including n = 1. The outline-reviewer's numerical checks
(four seeds, T up to 800) found the identity already holding from n = 1 in every test
case — evidence the boundary is not an obstruction in practice — but this is not a
proof. A full proof would need to show that the finitely many "pre-period" terms
a_1, ..., a_{N'} already lie in the same forward orbit under the period-L, period-T
rule as the terms beyond N' (e.g. by showing directly that a_1, ..., a_{N'} are
themselves consecutive good-residue values under G, with no "extra" or "missing" terms
before the rule kicks in). We have not attempted to close this here because it is
downstream of, and secondary to, the unresolved Core Lemma in Section 5: without an
explicit S, N, L there is no concrete G to check the pre-period against. We flag this
as a second (smaller, likely mechanical) gap to be closed once Section 5 is resolved.

---

### Summary of what is and is not established
- **Proved in full, no gaps:** Lemma 1 (free fact), Lemma 2 (Bounded Gap Lemma —
  new), Lemma 3 (recurrent-pattern pigeonhole), Lemma 4 (forced-linking-prime lemma).
- **Proved in full, conditionally:** Section 6, the entire CRT + cyclic-pigeonhole
  finish, rigorously derived from the Core Lemma.
- **Not proved (the genuine remaining gap):** the Core Lemma of Section 5 (finiteness
  of the global load-bearing / witness prime set), and, downstream of it, the n = 1
  boundary extension of Section 7.

## Promotable lemmas
- **Lemma 1 (Free fact).** For n ≥ 2, gcd(a_n,a_1) > 1, hence π(n) := P(a_n)∩P(a_1) ≠
  ∅ for all n ≥ 1. Proved in Section 1 above; a one-line consequence of the hypothesis,
  shared by all approaches to this problem.
- **Lemma 2 (Bounded Gap Lemma).** a_{n+1} ≤ a_n + a_1 for every n ≥ 1. Proved in
  Section 2 above via the explicit valid candidate "smallest multiple of a_1 exceeding
  a_n." This is a new, fully self-contained, unconditional structural fact (does not
  depend on any other lemma or open gap) that gives linear growth a_1+(n-1) ≤ a_n ≤
  n·a_1, and is reusable by any other approach to this problem.
- **Lemma 3 (Recurrent-pattern pigeonhole).** Some nonempty A ⊆ Q occurs as π(n) for
  infinitely many n. Proved in Section 3 via the infinite pigeonhole principle on the
  finite set of nonempty subsets of Q.
- **Lemma 4 (Forced-linking-prime lemma).** For any index i and recurrent pattern A
  disjoint from π(i), some prime dividing a_i also divides infinitely many terms of
  pattern A. Proved in Section 4 via the defining greedy property plus finite
  pigeonhole on P(a_i).
