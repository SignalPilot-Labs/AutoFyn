# Approach: essential-prime-counting

## Status
partial

## Approaches tried
- Round 1 (outline only) — skeleton for a quantitative sieve/interval-occupancy attack on the finiteness nucleus.
- Round 1 (build) — Converted the outline into a fully rigorous reduction of the ENTIRE
  problem to a single clean finiteness lemma, and proved the reduction (bounded gaps,
  static set, enumeration, CRT periodicity, exactness-from-n=1) with no gaps. Attacked the
  finiteness nucleus head-on with the aimo-0447 interval-occupancy / Σ1/p² counting: obtained
  a rigorous *density* bound on "bad pairs" but could NOT upgrade it to *finiteness* of the
  essential set, because sparse (density-zero) disjoint prime-type families evade a pure
  pair-count and closing them requires a greedy-minimality input not yet supplied. Outcome:
  strong partial — everything except the finiteness crux is airtight; the crux is isolated as
  the single Main Crux Lemma (MCL) with a partial counting attack.

## Current best
The whole problem is **rigorously reduced** (no gaps) to:

> **Main Crux Lemma (MCL).** There is a finite set of primes S such that any two terms
> a_i, a_j share a prime in S (equivalently, the set Π = { min(supp a_i ∩ supp a_j) : i<j }
> of primes that ever occur as the least common prime factor of a pair of terms is finite).

Given MCL, an explicit (T, L) with a_{n+T} = a_n + L for **every** n ≥ 1 is produced, exact
from n = 1 (no pre-period), with L = ∏S. All of Lemmas A–D below are complete and reusable.
The remaining open gap is MCL itself; a rigorous partial (interval-occupancy Σ1/p² bound
plus a "no two disjoint heavy prime-types" corollary) is recorded, together with the precise
statement of what is still missing (excluding sparse essential families via greedy minimality).

Notation: for m ∈ ℤ_{>1}, supp(m) = set of primes dividing m. R = rad(a_1) = ∏_{p|a_1} p.

---

## Full proof of the reduction (complete) + partial attack on MCL

Throughout, "term" means some a_n, and (a_n) is the greedy sequence of the statement.

### Lemma A (bounded gaps, linear growth). For all n, a_{n+1} − a_n ≤ R; hence
### a_1 + (n−1) ≤ a_n ≤ a_1 + (n−1)R.

*Proof.* First, every term is divisible by a prime dividing a_1. For n = 1 this is clear.
For n ≥ 2, a_n is admissible at its step, so in particular gcd(a_n, a_1) > 1, giving a prime
q_n | gcd(a_n, a_1); thus q_n | a_1 and q_n | a_n.

Now fix n and let m be any multiple of R with m > a_n. For each i ≤ n we have q_i | a_1, hence
q_i | R | m, and q_i | a_i, so q_i | gcd(m, a_i), i.e. gcd(m, a_i) ≥ q_i > 1. Therefore m
satisfies every admissibility constraint for the (n+1)-st term. The least multiple of R
exceeding a_n is at most a_n + R, so by minimality of the greedy choice, a_{n+1} ≤ a_n + R.
Combined with a_{n+1} ≥ a_n + 1 (strictly increasing integers) and iterating from a_1, we get
a_1 + (n−1) ≤ a_n ≤ a_1 + (n−1)R. ∎

*(Technique: elementary divisibility; "every multiple of rad(a_1) meets all prior terms."
No knowledge-base theorem needed.)*

### Lemma B (static reformulation and enumeration). Let
### A = { x ∈ ℤ_{>1} : gcd(x, a_i) > 1 for every i ≥ 1 }.
### Then every term lies in A, and (a_n)_{n≥1} is precisely the increasing enumeration of
### A ∩ [a_1, ∞); more precisely A ∩ [a_1, a_n] = {a_1, …, a_n} for every n.

*Proof.* **Each a_n ∈ A.** Fix n and any i. If i < n, then gcd(a_n, a_i) > 1 by admissibility
of a_n. If i > n, then gcd(a_i, a_n) > 1 by admissibility of a_i (its constraint set includes
index n < i). If i = n, gcd(a_n, a_n) = a_n > 1. As a_n > 1 this shows a_n ∈ A.

**Enumeration.** We show by induction on n that A ∩ [a_1, a_n] = {a_1, …, a_n}.

Base n = 1: every element of A ∩ [a_1, ∞) is ≥ a_1, and a_1 ∈ A (just shown), so
a_1 = min(A ∩ [a_1, ∞)); in particular A ∩ [a_1, a_1] = {a_1}.

Step: assume A ∩ [a_1, a_n] = {a_1, …, a_n}. Put y = min(A ∩ (a_n, ∞)) (this min exists since
A ∩ (a_n, ∞) ⊇ {a_{n+1}, a_{n+2}, …} ≠ ∅). We claim a_{n+1} = y.
- Since a_{n+1} ∈ A and a_{n+1} > a_n, we have a_{n+1} ≥ y.
- Since y ∈ A, gcd(y, a_i) > 1 for all i, in particular for all i ≤ n; and y > a_n. So y is an
  admissible candidate for the (n+1)-st term, and by minimality a_{n+1} ≤ y.
Hence a_{n+1} = y, and moreover there is no element of A strictly between a_n and a_{n+1}
(that is what y = min gives). Therefore A ∩ [a_1, a_{n+1}] = {a_1, …, a_{n+1}}, completing the
induction. Since a_n → ∞ (Lemma A), taking the union over n gives
A ∩ [a_1, ∞) = { a_n : n ≥ 1 }. ∎

### Lemma C (increasing enumeration of an L-periodic set). Let B ⊆ [a_1, ∞) be infinite and
### suppose L ≥ 1 satisfies: for every integer x ≥ a_1, x ∈ B ⇔ x + L ∈ B. Let
### T = |B ∩ [a_1, a_1 + L)|. Then T ≥ 1 and the increasing enumeration b_1 < b_2 < … of B
### satisfies b_{k+T} = b_k + L for every k ≥ 1.

*Proof.* If B ∩ [a_1, a_1 + L) were empty, then by the biconditional (applied repeatedly)
B ∩ [a_1 + jL, a_1 + (j+1)L) = ∅ for all j ≥ 0, forcing B = ∅, contradicting B infinite. So
T ≥ 1. The map x ↦ x + L is injective; we show it maps B bijectively onto B ∩ [a_1 + L, ∞).
If x ∈ B (so x ≥ a_1), then x + L ∈ B and x + L ≥ a_1 + L, so x + L ∈ B ∩ [a_1 + L, ∞).
Conversely if y ∈ B with y ≥ a_1 + L, then y − L ≥ a_1, and by the biconditional y − L ∈ B,
with x := y − L. Hence B ∩ [a_1 + L, ∞) = { x + L : x ∈ B } = B + L.

Now b_1, …, b_T are exactly the elements of B in [a_1, a_1 + L) (the T smallest elements of B,
since B ⊆ [a_1, ∞)), and b_{T+1}, b_{T+2}, … are exactly the elements of B that are
≥ a_1 + L, listed increasingly. But that latter set equals B + L = { b_1 + L < b_2 + L < … },
also listed increasingly. Two increasing enumerations of one set agree termwise, so
b_{T+k} = b_k + L for every k ≥ 1. ∎

*(Technique: order-preserving shift bijection on a periodic set — knowledge_base.md "eventual
periodicity / periodic residue structure"; here upgraded to exact from a_1 because periodicity
holds on all of [a_1, ∞), not just a tail.)*

### Lemma D (finite pairwise-connecting S ⇒ exact periodicity from n = 1). Suppose there is a
### finite set S of primes such that for all i, j ≥ 1, supp(a_i) ∩ supp(a_j) ∩ S ≠ ∅. Then,
### with L = ∏_{p∈S} p and T = |A ∩ [a_1, a_1 + L)| ≥ 1, we have a_{n+T} = a_n + L for every
### n ≥ 1.

*Proof.* Note each supp(a_i) ∩ S ≠ ∅ (apply the hypothesis to the pair (i, j) for any j ≠ i;
the shared S-prime divides a_i). Let 𝒯 = { supp(a_i) ∩ S : i ≥ 1 }, a finite family of
nonempty subsets of the finite set S. Define
    A_S = { x ∈ ℤ_{>1} : for every σ ∈ 𝒯, supp(x) ∩ σ ≠ ∅ }.

**Claim 1: A ∩ [a_1, ∞) = A_S ∩ [a_1, ∞).**
- (A_S ⊆ A.) Let x ∈ A_S and fix any i. With σ = supp(a_i) ∩ S ∈ 𝒯 we get
  supp(x) ∩ σ ≠ ∅, so supp(x) ∩ supp(a_i) ≠ ∅, i.e. gcd(x, a_i) > 1. As x > 1, x ∈ A.
  (This inclusion needs no hypothesis and holds over all of ℤ_{>1}.)
- (A ∩ [a_1, ∞) ⊆ A_S.) Let x ∈ A ∩ [a_1, ∞); by Lemma B, x = a_j for some j. For any
  σ = supp(a_i) ∩ S ∈ 𝒯, the hypothesis gives supp(a_j) ∩ supp(a_i) ∩ S ≠ ∅, and this set is
  contained in supp(x) ∩ σ. Hence supp(x) ∩ σ ≠ ∅ for all σ ∈ 𝒯, so x ∈ A_S.

**Claim 2: A_S is a union of residue classes modulo L.** For a prime p ∈ S, whether p | x
depends only on x mod p, hence (by the Chinese Remainder Theorem, since L = ∏_{p∈S} p is
squarefree) only on x mod L. Membership of x in A_S is a Boolean combination of the
conditions "p | x" for p ∈ S (namely: for every σ ∈ 𝒯, at least one p ∈ σ divides x).
Therefore x ∈ A_S depends only on x mod L; A_S is a union of residue classes mod L, and for
every integer x ≥ 1, x ∈ A_S ⇔ x + L ∈ A_S.

Now set B = A ∩ [a_1, ∞) = A_S ∩ [a_1, ∞) (Claim 1); by Lemma B, B = { a_n } is infinite.
By Claim 2 the biconditional "x ∈ B ⇔ x + L ∈ B" holds for every x ≥ a_1 (both sides are
membership in A_S, using that x, x+L ≥ a_1). Lemma C applies and gives T ≥ 1 and, for the
increasing enumeration b_k = a_k of B, a_{k+T} = a_k + L for every k ≥ 1. Finally
T = |B ∩ [a_1, a_1 + L)| = |A ∩ [a_1, a_1 + L)| by Claim 1. ∎

*(Technique: Chinese Remainder Theorem — knowledge_base.md "Modular arithmetic, CRT"; plus a
hitting-set/Boolean structure making A_S a covering-system union of residue classes.)*

### Reduction complete. By Lemma D, the theorem a_{n+T} = a_n + L (for all n ≥ 1) follows once
### MCL is established. Indeed, if MCL holds with witnessing finite set S, apply Lemma D to S.

Equivalently, take S = Π := { min(supp(a_i) ∩ supp(a_j)) : i < j }. For any pair (i, j),
p := min(supp(a_i) ∩ supp(a_j)) lies in supp(a_i) ∩ supp(a_j) ∩ Π, so the pairwise-connecting
hypothesis of Lemma D holds automatically. Thus:

    THE THEOREM IS EQUIVALENT TO: Π is finite.  (★)

*(Numerically verified end-to-end: for a_1 = 15, 143, 1001 the min-common-prime set Π computed
over the first 300 terms is {2,3,5}, {2,3,5,7,11,13}, {2,3,7,11,13} respectively, and the
residue-class set A_S mod L = ∏Π reproduces the sequence exactly from n = 1. This confirms the
reduction and that a valid — not necessarily minimal — L is L = ∏Π.)*

---

### Partial attack on MCL (the finiteness nucleus) — the remaining gap

We record the rigorous progress and isolate exactly what is missing.

**Interval-occupancy bound (rigorous).** For a prime p and real Y > 0, at most ⌊Y/p⌋ terms
that are ≤ Y are divisible by p (such terms are among the multiples of p in [1, Y]). Write
N_p(Y) ≤ Y/p.

**Bad-pair density bound (rigorous).** Fix a threshold K ≥ R. Call an unordered pair of terms
{a_i, a_j} *K-bad* if a_i, a_j share no prime factor ≤ K. Every K-bad pair shares some prime
p > K (they do share a prime, and it must exceed K). Hence, counting K-bad pairs with both
terms ≤ Y:
    #{K-bad pairs ≤ Y} ≤ Σ_{p > K} C(N_p(Y), 2) ≤ Σ_{p > K} N_p(Y)²/2
                        ≤ (Y²/2) Σ_{p > K} 1/p² < (Y²/2) Σ_{n ≥ K} 1/n² < Y² / (2(K−1)).
This is the aimo-0447 interval-occupancy / Σ1/p² mechanism, made rigorous: the K-bad pairs
occupy at most a 1/(K−1)-fraction of all O(Y²) pairs.

**"No two disjoint heavy types" corollary (rigorous).** Group terms by their *small type*
τ(a_n) = supp(a_n) ∩ {p ≤ K} (nonempty by Lemma A, since it contains a prime | a_1, all ≤ R ≤ K).
For two disjoint small types τ_a ≠ τ_b, every cross pair (one term of each) is K-bad, so
applying the same covering bound to just these two families:
    U_a(Y)·U_b(Y) ≤ Σ_{p>K} N_p(Y)² ≤ Y²/(K−1),
where U_a(Y), U_b(Y) count terms ≤ Y of each type. Hence min(U_a(Y), U_b(Y)) ≤ Y/√(K−1):
**among small types that are pairwise disjoint, at most one can have positive density**
> 1/√(K−1). Consequently the small types of positive density are pairwise intersecting.

**What remains open (the honest gap).** To finish (★) it suffices to show: *for some finite K,
only finitely many pairs are K-bad* (then Π ⊆ {primes ≤ K} ∪ ⋃_{those finitely many bad pairs}
supp, a finite set, giving MCL). The corollary controls *positive-density* (heavy) types, but
does **not** exclude the following scenario: two small types τ_a, τ_b that are disjoint and each
occur *infinitely often but with density zero* (sparse). These would generate infinitely many
K-bad pairs while contributing only o(Y²) — even O(Y) — pairs, evading the density bounds above
for every K. Ruling out sparse essential families cannot be done by the pair-count alone; it
requires feeding in the **greedy minimality** of the sequence (a non-greedy sequence with the
same pairwise-gcd property can in fact have infinitely many essential primes, so any complete
proof must use that a_{n+1} is the *least* admissible integer). The precise missing statement is:

> **Gap (MCL-finiteness).** There exist a finite prime set S₀ and index N₀ such that for every
> j > N₀ and every i < j, supp(a_i) ∩ supp(a_j) ∩ S₀ ≠ ∅. (Equivalently: only finitely many
> primes ever serve as the least common prime of a pair.)

The counting above proves this *modulo* excluding sparse disjoint essential types; the exclusion
is where greedy minimality must enter and is not yet supplied. This is the single remaining gap;
Lemmas A–D reduce the entire IMO problem to closing it.

---

## Promotable lemmas
All four are proved in full above and are reusable across every approach to this problem:

- **Lemma A (bounded gaps / linear growth).** a_{n+1} − a_n ≤ R = rad(a_1); hence
  a_1 + (n−1) ≤ a_n ≤ a_1 + (n−1)R. [Proof: every multiple of R exceeding a_n is admissible.]
- **Lemma B (static set + enumeration).** With A = {x>1 : gcd(x,a_i)>1 ∀i}, every term is in A
  and (a_n) is the increasing enumeration of A ∩ [a_1, ∞); A ∩ [a_1, a_n] = {a_1,…,a_n}.
- **Lemma C (enumeration of an L-periodic set).** An infinite B ⊆ [a_1,∞) with x∈B⇔x+L∈B for
  all x ≥ a_1 has increasing enumeration satisfying b_{k+T}=b_k+L, T=|B∩[a_1,a_1+L)| ≥ 1.
- **Lemma D (finite pairwise-connecting S ⇒ exact periodicity from n=1).** If a finite prime
  set S has supp(a_i)∩supp(a_j)∩S ≠ ∅ for all i,j, then a_{n+T}=a_n+L for all n≥1 with
  L = ∏_{p∈S} p and T = |A ∩ [a_1, a_1+L)|. Reduces the theorem to MCL (finiteness of the
  essential/min-common prime set).

These certify the exactness-from-n=1 mechanism and the reduction shared with
admissible-set-periodicity; once certified, the outstanding work for every approach is exactly
the MCL-finiteness gap.
