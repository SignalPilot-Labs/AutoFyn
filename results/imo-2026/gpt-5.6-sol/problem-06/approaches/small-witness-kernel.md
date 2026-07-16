## Status
solved

## Approaches tried
- Small-witness kernel via prime-factor compression and extremal descent — worked: the recursive good set is the greedy sequence, every two good integers share a prime at most `a_1`, and consequently membership is determined by the divisibility mask of the primes at most `a_1`.

## Current best
A complete proof is obtained with `L` equal to the product of all primes at most `a_1`. The good integers form an exactly `L`-periodic set on the whole half-line beginning at `a_1`; if `T` is the number of good integers in the first block of length `L`, then translating the ordered good set by `L` shifts every index by exactly `T`.

## Full proof
Put `k=a_1`; the hypothesis gives `k>1`. We shall use **strong induction**, the **extremal (minimal-counterexample) principle**, **divisor analysis**, and **modular arithmetic with periodic residue masks**, as named in the corresponding entries of `knowledge_base.md`.

We first define, independently of the given sequence, a partition of the integers at least `k` into *good* and *bad* integers. Proceeding in increasing order, declare an integer `m>=k` to be good if there is no good integer `r` satisfying

`k <= r < m` and `gcd(r,m)=1`;

otherwise declare `m` bad. This is a well-defined strong-induction recursion: when `m` is considered, the status of every possible `r<m` has already been determined. In particular, the definition gives both implications we shall use:

- if `m` is bad, then there exists a good `r` with `k<=r<m` and `gcd(r,m)=1`;
- if `m` is good, then no such `r` exists.

The integer `k` is good because there is no integer in `[k,k)`. Moreover, any two good integers have a nontrivial common divisor. Indeed, if `u<v` were both good and `gcd(u,v)=1`, then the smaller good integer `u` would be a witness making `v` bad, a contradiction.

There are infinitely many good integers. In fact, every positive multiple `mk` of `k` is good. If such a multiple were bad, it would have a smaller good witness `r` coprime to `mk`. Then `r` would also be coprime to `k`, contradicting the fact that the two good integers `r` and `k` must have a nontrivial common divisor.

We next prove that the given sequence is exactly the increasing enumeration of the good integers. Let

`g_1<g_2<g_3<...`

be that enumeration, which exists by the preceding paragraph. Its first term is `g_1=k=a_1`. Suppose inductively that `a_i=g_i` for `1<=i<=n`. The good integer `g_{n+1}` has nontrivial gcd with each of the earlier good integers `g_1,...,g_n`, so it is eligible in the rule defining `a_{n+1}`. On the other hand, let `m` satisfy `g_n<m<g_{n+1}`. It is not good and hence is bad, so there is a good integer `r<m` coprime to `m`. There is no good integer strictly between `g_n` and `g_{n+1}`, and therefore `r` is one of `g_1,...,g_n`. Thus `m` is not eligible in the greedy rule. Consequently the least eligible integer greater than `a_n=g_n` is precisely `g_{n+1}`, so `a_{n+1}=g_{n+1}`. Induction proves the claim.

Call a prime *small* if it is at most `k`, and *large* otherwise. Two integers at least `k` will be called *similar* if they have exactly the same small prime divisors.

We need the following compression lemma.

**Compression lemma.** If `b>=k` has at least one small prime divisor, then there exists an integer `x` such that

1. `k<=x<=b`;
2. `x` is similar to `b`; and
3. every prime divisor of `x` is small.

**Proof of the compression lemma.** If `b` has no large prime divisor, take `x=b`; all three assertions then hold.

Now suppose that `b` has a large prime divisor `q`. Let `A` be the product of all the distinct small prime divisors of `b`, and choose one such divisor `p`. The integer `A` exists because the hypothesis says that `b` has a small prime divisor. Let `e` be the least nonnegative integer for which

`x=p^e A >= k`.

Such an `e` exists because powers of `p` are unbounded. The prime divisors of `x` are exactly the prime divisors of `A`, hence exactly the small prime divisors of `b`. Thus assertions 2 and 3 hold, and the choice of `e` gives `x>=k`.

It remains to prove `x<=b`. If `e=0`, then `x=A`, and `A` divides `b`, so `x<=b`. If `e>0`, the minimality of `e` gives `p^{e-1}A<k`, whence

`x=p^eA<pk`.

Because `p` is one of the factors of `A`, we have `p<=A`; because `q` is large, we have `k<q`. Therefore

`x<pk<=Ak<Aq`.

The primes occurring in `A` are distinct small prime divisors of `b`, while `q` is a distinct large prime divisor of `b`. Hence their product `Aq` divides `b`, so `Aq<=b`. Combining the inequalities yields `x<b`. This covers separately the cases of no large prime divisor, a large prime divisor with `e=0`, and a large prime divisor with `e>0`, and proves the lemma. ∎

We now establish the central structural fact.

**Small-witness theorem.** Every two good integers have a common small prime divisor.

**Proof.** Suppose not. A *violating pair* is then a pair of good integers with no common small prime divisor. Order such a pair as `b<=b'`, and, by the extremal principle, choose one for which the larger member `b'` is as small as possible.

The good integers `b` and `k` have a nontrivial common divisor, as proved above. Choose a prime `p` dividing both. Since `p|k`, we have `p<=k`, so `p` is small. In particular, `b` has a small prime divisor and the compression lemma applies to it. Also, `p` cannot divide `b'`, because `(b,b')` has no common small prime divisor. Thus `b` and `b'` are distinct, and their chosen ordering gives

`b<b'`.

Let `x` be supplied by the compression lemma for `b`. Thus `k<=x<=b`, `x` is similar to `b`, and every prime divisor of `x` is small. We claim that `gcd(x,b')=1`. If a prime `s` divided both, then `s` would be small because every prime divisor of `x` is small. Similarity of `x` and `b` would then imply `s|b`; hence `s` would be a common small prime divisor of `b` and `b'`, contrary to the choice of the violating pair.

Now `x<=b<b'`, and `b'` is good. If `x` were good, the two good integers `x` and `b'` would be coprime, contradicting the already proved fact that any two good integers have a nontrivial common divisor. Therefore `x` is bad. By the defining recursion, there is consequently a good integer `b^*` such that

`k<=b^*<x` and `gcd(b^*,x)=1`.

Both `b^*` and `b` are good. They have no common small prime divisor: every small prime divisor of `b` is also a divisor of the similar integer `x`, while `b^*` is coprime to `x`. Furthermore,

`b^*<x<=b<b'`.

Thus `(b^*,b)` is another violating pair, and after ordering it its larger member is exactly `b`, which is strictly smaller than `b'`. This contradicts the minimal choice of `b'`. The contradiction proves the theorem. ∎

We next show that good/bad status is determined entirely by the small-prime mask.

**Similarity invariance.** Any two similar integers `a,b>=k` have the same status.

**Proof.** Suppose they had opposite statuses. Label the bad member `a` and the good member `b`; this labeling does not assume or require either numerical ordering of `a` and `b`. Since `a` is bad, its defining witness gives a good integer `r` with

`k<=r<a` and `gcd(r,a)=1`.

The small-witness theorem applied to the two good integers `b` and `r` gives a small prime `p` dividing both. Because `a` and `b` are similar and `p` is small, `p|b` implies `p|a`. But also `p|r`, contradicting `gcd(r,a)=1`. Therefore similar integers cannot have opposite statuses. ∎

Let

`L = product_(p prime, p<=k) p`.

This is a positive integer; indeed it is greater than `1` because `k>=2`. For every `m>=k` and every small prime `p`, we have `p|L`, and hence

`p|m` if and only if `p|(m+L)`.

Thus `m` and `m+L` are similar. By similarity invariance,

`m is good` if and only if `m+L is good`                                              `(1)`

for every `m>=k`. This is exact periodicity on the entire half-line beginning at `k`, not merely eventual periodicity.

Let `G` denote the set of good integers, and define

`T = |G intersect [k,k+L-1]|`.

This is a positive integer because `k` is good and belongs to that interval. Translation by `L` is an order-preserving bijection

`G -> G intersect [k+L,infinity)`.

Indeed, (1) shows that every good `g>=k` maps to a good `g+L>=k+L`, and injectivity is immediate. Conversely, if `h>=k+L` is good, then `h-L>=k`; the integers `h-L` and `h` have the same small-prime mask, so (1), applied to `h-L`, shows that `h-L` is good. Hence every element of the indicated tail has a unique preimage.

There are exactly `T` good integers below `k+L`, namely those in `[k,k+L-1]`. Since translation by `L` preserves order, it sends the `n`th element of `G` to the `n`th element of the tail `G intersect [k+L,infinity)`. The latter is the `(n+T)`th element of all of `G`. We already proved that the increasing enumeration of `G` is `a_1,a_2,...`; therefore, for every positive integer `n`,

`a_n+L=a_{n+T}`.

The positive integers `T` and `L` constructed above satisfy the required identity for every `n>=1`. ∎

## Promotable lemmas
- **Small-witness theorem.** For the recursively defined good set on `[k,infinity)`, where an integer is good exactly when it has no smaller good coprime witness, every two good integers share a prime at most `k`. Proved in the `Small-witness theorem` subsection by compression and minimal-counterexample descent.
- **Compression lemma for small-prime masks.** Every `b>=k` with a prime divisor at most `k` has a similar representative `x` in `[k,b]` supported only on primes at most `k`. Proved in full in the `Compression lemma` subsection, including all boundary cases.
- **Similarity invariance.** In the same recursion, good/bad status depends only on the set of prime divisors at most `k`. Proved after the small-witness theorem.
