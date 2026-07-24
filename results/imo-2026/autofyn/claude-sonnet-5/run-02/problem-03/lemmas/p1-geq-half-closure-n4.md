# Theorem: p1 >= T/2 closure at n=4

**Certified: round 28 (proof-reviewer), from `lp-duality-certificate.md`
§R28.2.**

## Statement

For every 5-piece marking $p_1\ge p_2\ge p_3\ge p_4\ge p_5>0$ with
$T=\sum p_i$ and $p_1\ge T/2$,
$$\Phi_{\min}(p_1,\dots,p_5;\,4)\ \le\ a_4T=\frac{16}{31}T.$$

## Proof sketch (full proof in the approach file, §R28.1-R28.2)

Two sub-cases partitioning $[T/2,T)$ exactly (since $a_4=16/31\in(1/2,1)$,
proved via the general Telescoping Threshold Lemma re-indexed at $n=4$:
$a_3=a_4/(2(1-a_4))$):

- **$T/2\le p_1<a_4T$.** `full-match-achievability` (Theorem A) gives a
  legal 4-cut Xiang Yu response achieving $\Phi=p_1<a_4T$ exactly.
- **$p_1\ge a_4T$.** `bisect-top-recursive-identity` (Theorem C′): bisect
  $p_1$ (1 cut), leaving the tail $\{p_2,p_3,p_4,p_5\}$ untouched; the
  tail is an arbitrary 4-piece marking, so round 27's certified
  `gap-filler-four-chamber-covering` (combined with case (a)/(b1)/(b2),
  the complete $n=3$ upper bound $P(4)$) applies unconditionally, giving
  $\Phi_{\min}(\text{tail};3)\le a_3T'$. Substituting into Theorem C′ and
  using $a_3>1/2$ (so the resulting affine bound in $p_1$ is maximized at
  the left endpoint $p_1=a_4T$) plus the telescoping identity
  $a_3(1-a_4)=a_4/2$ gives $\Phi_{\min}\le a_4T$ exactly.

## Verification

Reviewer independently re-derived the telescoping algebra by exact
`Fraction` computation ($a_4/(2(1-a_4))=a_3$, $a_3(1-a_4)+a_4/2=a_4$,
both confirmed exactly) and independently re-verified the underlying
Theorem A construction (2000 exact-`Fraction` trials, zero mismatches).

## Scope

Covers only the $p_1\ge T/2$ half of the general $n=4$ upper bound; the
$p_1<T/2$ half is untouched. Reusable verbatim as the induction
hypothesis $P(5)$'s $p_1\ge T/2$ half needs for a future $n=5$ attempt at
the identical sub-target, exactly as this round's proof reused round 27's
$P(4)$.
