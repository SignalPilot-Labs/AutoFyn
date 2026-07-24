## Statement (CERTIFIED — round 32, proof-reviewer)

**Insertion Sandwich.** For any finite multiset $T$ of nonnegative reals
and any $a\ge0$,
$$A(T)-a\ \le\ A(T\cup\{a\})\ \le\ A(T)+a.$$

## Proof

Let $T$ sorted descending $t_1\ge\cdots\ge t_n\ge0$, and let $a$ land at
rank $k\in\{1,\dots,n+1\}$ in $T\cup\{a\}$. Elements of $T$ at original
rank $<k$ keep rank; elements at rank $\ge k$ shift by one (flipping sign
parity). Writing $U:=\sum_{i\ge k}(-1)^{i+1}t_i$ (the signed tail
contribution, using $T$'s own rank parity),
$$A(T\cup\{a\}) = A(T) - 2U + (-1)^{k+1}a.$$
- **$k$ odd:** $U=A(T_{\ge k})$, the alternating sum of the tail
  $\{t_k,\dots,t_n\}$ (all $\le a$), so by Max Bound and $A\ge0$,
  $U\in[0,a]$; hence $A(T\cup\{a\})-A(T)=a-2U\in[-a,a]$.
- **$k$ even:** $U=-A(T_{\ge k})$, so $U\in[-a,0]$; hence
  $A(T\cup\{a\})-A(T)=-a-2U\in[-a,a]$.

Either way $|A(T\cup\{a\})-A(T)|\le a$. $\blacksquare$

## Verification

Independently re-derived and verified by the proof-reviewer (round 32):
50,000 random exact-`Fraction` trials (multiset sizes 0–6), zero
violations.

## Origin / usage

Proved in `results/imo-2026-03/approaches/rank-pigeonhole-budget.md` §7.19.2,
round 32. Strictly more primitive than the certified
`truncated-alternating-sum-floor`/`-ceiling` lemmas (bounds the effect of
inserting one new element, rather than a threshold split). Used in the
Master Theorem (§7.19.3, this round) to absorb the "other fragments" of
$\sigma_1$'s own split.
