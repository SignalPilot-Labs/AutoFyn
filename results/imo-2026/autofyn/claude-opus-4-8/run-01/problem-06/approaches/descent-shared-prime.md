## Status
solved

## Approaches tried
- **descent-shared-prime** (round 2): minimal-counterexample / infinite-descent proof of the corrected finiteness crux. Imports the certified reduction (lemmas/bounded-gaps-and-clique.md, Tools 1–2, Sub-lemma E, Cor E.1, finish package). Establishes **Prop 1′** (Lemma S′ ⟹ every minimal clause ⊆ {primes ≤ a₁} ⟹ finitely many minimal clauses ⟹ conclusion) and then closes the sole gap, **Lemma S′** ("any two clauses share a prime ≤ a₁"), by descent on the larger index of a violating pair, adapting Claim 4 + Claim 5 of the IMO-2024-P5 (aimo-0030) second solution. **Outcome: complete.** The descent's size argument (Lemma S4) and the "small-shadow is not admissible" step (via greedy minimality + Sub-lemma E) close the b≤a₁ branch that stalled the outline. Verified computationally: 0 violations of S′ and all minimal clauses ⊆ {primes ≤ a₁} for a₁ ∈ {15,35,77,143,210,255,385,1001,2310,4199}.
- **clique-descent** (round 1): reduced the whole problem to Lemma S (FALSE as stated with P₁); superseded by the corrected S′ here.
- **sieve-closure** (round 1): reduced to "Π finite"; same crux, different framing.

## Current best
Complete proof. The whole problem is solved: the certified reduction turns it into Lemma S′ ("any two clauses share a prime ≤ a₁"), and Lemma S′ is proved from scratch by infinite descent (Lemmas S1–S4 below). No open gap.

## Full proof

Throughout, we import the reviewer-certified results of `lemmas/bounded-gaps-and-clique.md`
without re-deriving them; they are quoted where used.

### 0. Setup and vocabulary (imported)

Let a₁ > 1 and, for n ≥ 1,
  a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1 for every i ≤ n }.
For a positive integer m write supp(m) for its set of prime divisors. Say **m hits a
prime-set S** iff supp(m) ∩ S ≠ ∅. Put S_i = supp(a_i); call each S_i a **clause**.
Let A_n = { m ≥ 1 : m hits S_i for all i ≤ n }, so a_{n+1} = min(A_n ∩ (a_n, ∞)), and let
A = ⋂_{n≥1} A_n = { m ≥ 1 : m hits every clause }. Let P₁ be the largest prime factor of a₁.
Call a prime **small** if p ≤ a₁ and **big** if p > a₁; let G = { primes p ≤ a₁ } (a finite set).
For a prime-set S write σ(S) = S ∩ G for its **small shadow**.

We use the following certified facts verbatim.

- **Tool 1.** Every positive multiple of a₁ lies in every A_n; hence 0 < a_{n+1} − a_n ≤ a₁, the
  sequence is strictly increasing with a_n → ∞, and **every term a_k has a prime factor ≤ P₁**
  (so σ(S_k) ≠ ∅ for every k, since P₁ ≤ a₁).
- **Tool 2.** gcd(a_i, a_j) > 1 for all i ≠ j; hence **any two clauses intersect**: S_i ∩ S_j ≠ ∅.
  Also every a_n ∈ A.
- **Sub-lemma E.** If w ∈ A and w > a₁ then w = a_j for some j (the greedy sequence takes every
  admissible value above a₁).
- **Cor E.1.** A nonempty prime-set T that hits every clause is itself a clause (i.e. T = supp(a_j)
  for some j): pick a number of support exactly T that exceeds a₁ — e.g. (∏_{p∈T} p)^r for large r —
  it lies in A because it hits every clause, hence is a term by Sub-lemma E.
- **Finish package.** If there are finitely many minimal clauses (equivalently A is a periodic union
  of residue classes mod some M ≥ 2 and A_n = A for all n ≥ some N), then there exist T, L > 0 with
  a_{n+T} = a_n + L for every n ≥ 1.

A clause C is **minimal** if no clause is a proper subset of C.

### 1. Reduction to Lemma S′ (Prop 1′ and the finiteness crux)

> **Lemma S′.** Any two clauses share a small prime: for all i, j, the set S_i ∩ S_j contains a prime ≤ a₁.

We first show Lemma S′ implies the theorem; §§2–4 then prove Lemma S′.

**Proposition 1′.** If Lemma S′ holds, then every minimal clause is a subset of G.

*Proof.* Let C be a minimal clause and put C′ = C ∩ G = σ(C). By Tool 1, C = S_i for some term a_i
has a prime factor ≤ P₁ ≤ a₁, so C′ ≠ ∅. We claim C′ hits every clause D. Indeed, by Lemma S′ the
clauses C and D share a prime p ≤ a₁; then p ∈ C ∩ D and p ∈ G, so p ∈ (C ∩ G) ∩ D = C′ ∩ D, whence
C′ hits D. Since C′ is a nonempty prime-set hitting every clause, Cor E.1 makes C′ itself a clause.
But C′ ⊆ C and C is minimal, so C′ = C; therefore C = C′ ⊆ G. ∎

**Finiteness of minimal clauses.** By Prop 1′ every minimal clause is a subset of the finite set G,
so there are only finitely many minimal clauses C₁, …, C_r (at most 2^{|G|} of them). Each C_t is a
clause, i.e. C_t = S_{n_t} for some index n_t; put N = max_t n_t and M = ∏_{p ∈ C₁∪…∪C_r} p ≥ 2
(the union is nonempty because r ≥ 1: S₁ is a clause and contains a minimal clause, since a finite
poset of finite sets under ⊊ has a minimal element below every element).

We check the two hypotheses of the finish package.

*A is periodic mod M.* Whether m hits C_t depends only on which of the finitely many primes of C_t ⊆ G
divide m, hence only on m mod M. As A = { m : m hits every minimal clause } (hitting a set forces
hitting every superset, and every clause contains some minimal clause, so hitting all minimal clauses
is equivalent to hitting all clauses), A is a union of residue classes mod M; let T = |A mod M| ≥ 1
(A ≠ ∅ as it contains every multiple of a₁ by Tool 1).

*A_n = A for n ≥ N.* Always A ⊆ A_n. Conversely, if m ∈ A_n with n ≥ N then m hits S₁, …, S_n, and
in particular m hits each minimal clause C_t = S_{n_t} (as n_t ≤ N ≤ n); hence m hits every clause
and m ∈ A. So A_n = A for all n ≥ N.

By the certified finish package there exist positive integers T (= |A mod M|) and L (= M) with
a_{n+T} = a_n + L for every n ≥ 1. Thus Lemma S′ implies the theorem, and it remains only to prove
Lemma S′.

### 2. A violating pair and the descent set-up

Call an unordered pair of clauses {S_i, S_j} (with i ≠ j, so the two clauses are two distinct terms'
supports) **violating** if S_i ∩ S_j contains no small prime; equivalently, since S_i ∩ S_j ≠ ∅ by
Tool 2, **all** primes shared by S_i and S_j are big. Lemma S′ is exactly the assertion that **no
violating pair exists.** Assume, for contradiction, that a violating pair exists. Writing a violating
pair with its indices as (S_j, S_k), j < k, its **height** is the larger index k.

> Choose a violating pair (S_j, S_k), j < k, of **minimum height** k (and among those, minimum j).

Two immediate structural facts.

**(2a) j ≥ 2, and S_j contains a big prime.** The shared prime of a violating pair is big and lies
in S_j. In particular S_j has a big prime factor. Also S₁ ⊆ G (every prime factor of a₁ is ≤ P₁ ≤ a₁),
so any pair involving index 1 shares only small primes and is never violating; hence j ≥ 2.

**(2b) σ(S_j) ∩ S_k = ∅.** A prime in σ(S_j) ∩ S_k would be a small prime shared by S_j and S_k,
contradicting that (S_j, S_k) is violating.

### 3. Lemma S4 (a small-only companion of a_j of bounded size)

> **Lemma S4.** Suppose the clause S_j has a big prime factor and σ(S_j) ≠ ∅. Let R = ∏_{p ∈ σ(S_j)} p
> (the product of the small primes of a_j), let p₀ = min σ(S_j), and let n ≥ 0 be the least integer
> with x := p₀ⁿ R ≥ a₁. Then supp(x) = σ(S_j) and a₁ ≤ x < a_j.

*Proof.* Since p₀ ∈ σ(S_j) divides R, multiplying R by p₀ⁿ does not change the set of prime divisors:
supp(x) = supp(R) = σ(S_j). By the choice of n, x ≥ a₁.

Let q be a big prime factor of a_j (exists by hypothesis; q > a₁). The primes dividing R are exactly
the distinct small primes of a_j, and q is a big prime of a_j not among them, so R·q is a product of
distinct primes each dividing a_j; hence R·q divides a_j and R·q ≤ a_j. (⋆)

- If n = 0: x = R divides a_j and R·q ≤ a_j gives R ≤ a_j / q < a_j, so x = R < a_j.
- If n ≥ 1: by minimality of n, p₀^{n−1} R < a₁, so x = p₀ · (p₀^{n−1} R) < p₀ a₁. Since p₀ | R we
  have p₀ ≤ R, and since q is big, a₁ < q. Therefore
      x < p₀ a₁ ≤ R a₁ < R q ≤ a_j,
  using p₀ ≤ R, then a₁ < q, then (⋆). So x < a_j.

In both cases a₁ ≤ x < a_j. ∎

### 4. Proof of Lemma S′ (closing the descent)

Take the minimum-height violating pair (S_j, S_k), j < k, from §2. By (2a), S_j has a big prime factor,
and σ(S_j) ≠ ∅ by Tool 1. Apply Lemma S4 to S_j to obtain the integer x with

  supp(x) = σ(S_j),  a₁ ≤ x < a_j.  (†)

Note two consequences of (†) and (2b):
  gcd(x, a_k) = 1, because supp(x) = σ(S_j) and σ(S_j) ∩ S_k = ∅ (by (2b)).  (‡)

We split on whether x is a term of the sequence.

**Case A: x is a term, x = a_m for some m (this includes x = a₁, which is a₁ = a₁·1 = the term a₁).**
Then supp(x) = S_m, so S_m = σ(S_j). By Tool 2, gcd(a_m, a_k) > 1, i.e. S_m ∩ S_k ≠ ∅. But
S_m = σ(S_j) and, by (2b), σ(S_j) ∩ S_k = ∅ — equivalently gcd(x, a_k) = 1 by (‡). This contradicts
gcd(a_m, a_k) > 1. So Case A is impossible.

**Case B: x is not a term.** Since x ≥ a₁ and, in fact, x > a₁ (if x = a₁ we would be in Case A with
m = 1), Sub-lemma E gives: were x ∈ A, then x > a₁ ∈ A would force x to be a term — contradiction.
Hence x ∉ A.

Now locate x among the terms. By (†), a₁ < x < a_j, and the terms strictly increase to ∞, so there is
an index s with
  a_s < x < a_{s+1},  1 ≤ s ≤ j − 1,
where the inequalities are strict because x is not a term (Case B), and s + 1 ≤ j because x < a_j.

We claim x ∉ A_s. Indeed a_{s+1} = min(A_s ∩ (a_s, ∞)); if x ∈ A_s, then x ∈ A_s ∩ (a_s, ∞) with
x < a_{s+1}, contradicting the minimality defining a_{s+1}. Hence x ∉ A_s, i.e. x fails to hit some
clause S_i with i ≤ s. Let t be the **least** index with x ∉ A_t, so
  supp(x) ∩ S_t = ∅,  and  t ≤ s ≤ j − 1 < k.

We finish by showing (S_t, S_j) is a violating pair of height j < k, contradicting the minimality of k.

- supp(x) = σ(S_j), and supp(x) ∩ S_t = ∅, so σ(S_j) ∩ S_t = ∅: **S_t contains no small prime of S_j.**
- By Tool 2, S_t ∩ S_j ≠ ∅. Take any prime r ∈ S_t ∩ S_j. Then r ∈ S_j; if r were small it would lie
  in σ(S_j), but r ∈ S_t and S_t ∩ σ(S_j) = ∅ — impossible. Hence r is big. So every prime shared by
  S_t and S_j is big, and the intersection is nonempty: **{S_t, S_j} is violating.**
- Its height is max(t, j) = j (since t ≤ j − 1 < j), and j < k.

This violating pair has height j < k, contradicting the choice of (S_j, S_k) as a violating pair of
minimum height. Case B is therefore impossible.

Both cases are impossible, so **no violating pair exists.** By the definition of violating pair, this
is exactly Lemma S′: any two clauses share a small prime. ∎ (Lemma S′)

### 5. Conclusion

By §1 (Prop 1′ and the finiteness of minimal clauses) together with Lemma S′ proved in §§2–4, there
are finitely many minimal clauses, all contained in G. The certified finish package then yields
positive integers T and L (concretely T = |A mod M| and L = M = ∏_{p ∈ ⋃ minimal clauses} p) such that

  a_{n+T} = a_n + L  for every positive integer n.

This is the required statement. ∎

### Verification of the reduction (computational sanity check, not part of the proof)

For a₁ ∈ {15, 35, 77, 143, 210, 255, 385, 1001, 2310, 4199}, simulating the greedy sequence to depth
400: every pair of clauses shares a prime ≤ a₁ (0 violations of Lemma S′), and every minimal clause is
a subset of {primes ≤ a₁} (Prop 1′), including the genuinely-large essential prime 19 ≤ 385 for
a₁ = 385 that falsified the round-1 P₁-threshold Lemma S. The corrected threshold a₁ is exactly right.

## Promotable lemmas

- **Lemma S′ (shared small prime).** *For the greedy sequence, any two clauses S_i, S_j share a prime
  ≤ a₁.* Proved in full in §§2–4 by minimum-height-violating-pair descent, using only certified Tools
  1–2, Sub-lemma E and greedy minimality. Reusable by any approach needing the finite ground set G.
- **Prop 1′ (small-shadow of a minimal clause).** *Assuming Lemma S′, every minimal clause C equals its
  small shadow C ∩ G, hence C ⊆ {primes ≤ a₁}.* Proved in §1 via Cor E.1 + minimality. This is the
  clean corrected replacement for the round-1 (false) P₁-threshold Prop 1.
- **Lemma S4 (bounded small-only companion).** *If a clause S_j has a big prime factor, there is an
  integer x with supp(x) = σ(S_j) and a₁ ≤ x < a_j.* Proved in §3; an adaptation of Claim 4 of the
  IMO-2024-P5 (aimo-0030) second solution to the greedy-sequence setting.
