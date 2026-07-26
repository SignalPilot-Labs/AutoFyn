# Lemma: large-prime-span-divides-at-most-one-term

**Context.** IMO 2026 Problem 6. Let $a_1,a_2,\ldots$ be the greedy sequence of the problem, and write $R:=\operatorname{rad}(a_1)$. We use the certified **Gap bound** (Lemma 2 of `essential-monovariant`, see `approaches/essential-monovariant.md` §2):
$$ a_{n+1}-a_n \le R \qquad \text{for every } n\ge 1. $$

## Statement

**Large-prime-span lemma.** *For every $N\ge 2$ let*
$$ S_N := a_N - a_1 \;(=\text{the span of the first } N \text{ terms}). $$
*Then $S_N \le (N-1)\,R$. Moreover, every prime $p > S_N$ divides **at most one** of the integers $a_1,a_2,\ldots,a_N$.*

## Proof

**Span bound.** By telescoping and the Gap bound (Lemma 2),
$$ S_N = a_N-a_1 = \sum_{k=1}^{N-1}(a_{k+1}-a_k) \le \sum_{k=1}^{N-1} R = (N-1)R. $$
This proves the first assertion.

**Large-prime uniqueness.** Suppose for contradiction that a prime $p>S_N$ divides two distinct terms $a_i,a_j$ with $1\le i<j\le N$. Then $p\mid (a_j-a_i)$. Since the sequence is strictly increasing ($a_{n+1}>a_n$ by the greedy rule), $a_j-a_i>0$, so $a_j-a_i$ is a **nonzero** multiple of $p$; hence $a_j-a_i\ge p$. On the other hand $a_i,a_j\in[a_1,a_N]$, so
$$ 0 < a_j-a_i \le a_N-a_1 = S_N < p, $$
contradicting $a_j-a_i\ge p$. Therefore at most one of $a_1,\ldots,a_N$ is divisible by $p$. $\square$

## Corollary (shared primes lie below the span)

*Every prime that is shared by two distinct terms among $\{a_1,\ldots,a_N\}$ satisfies $p\le S_N\le (N-1)R$.*

*Proof.* A shared prime divides two distinct terms, so by the lemma it is not $>S_N$, i.e. $p\le S_N$. $\square$

## Remarks

- The threshold produced here is the **span** $S_N\le(N-1)R$, which **grows linearly with $N$**. It is *not* the fixed threshold $R$ required by the crux (Lemma 4 of `essential-monovariant`): the crux needs every shared prime to satisfy $p\le R$, independent of $N$. Sharpening $S_N\rightsquigarrow R$ is exactly the free-rider dichotomy / Lemma 4, the open crux of the whole problem. The counting route (`grid-counting-shared-primes`) reaches the growing-window analogue $\le (N-1)R$, not the fixed $R$.

## Promotable lemmas
- (this file is itself a promotable lemma; see the importing approach `grid-counting-shared-primes`.)
