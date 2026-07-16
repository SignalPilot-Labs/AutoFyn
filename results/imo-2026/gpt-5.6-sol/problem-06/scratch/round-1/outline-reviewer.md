## small-prime-mask-compression — APPROVE

This is a complete end-to-end route and matches the exact mechanism of the `aimo-0030` analogue: recursive good/bad classification, compression to the primes at most `k=a_1`, minimal-counterexample invariance of the small-prime mask, and enumeration of a periodic marked set. It does not repeat the explorers' warned-against dead end of tracking only primes dividing `k`; it correctly retains every prime `p\le k`.

Specific load-bearing points the builder must make explicit:

1. In the recursive classification, prove both directions: a bad integer has a smaller good coprime witness, while a good integer has no such witness. Then use strong induction on the integers to show that the greedy sequence lists all and only the good integers in increasing order. It is not enough merely to note that selected terms are pairwise non-coprime.
2. In the compression lemma, write the inequalities accurately. If `A` is the product of all small prime divisors of `b`, `p\mid A` is one such prime, and `e>0` is least with `x=p^eA\ge k`, then `x<pk\le Ak<Aq\le b` for a large prime divisor `q` of `b`. Treat separately: no large prime (`x=b`), a large prime with `e=0` (`A\le b`), and a large prime with `e>0`. Also state why `b` always has a small prime factor whenever this lemma is applied.
3. In the minimal opposite-color pair, label the bad member `a` and good member `b` without assuming their numerical order. The witness `r` satisfies `r<a`, and compression gives `r'\le r`, so `max(r,r')<max(a,b)`; minimality therefore makes `r'` good. Since `r'` has only small prime factors, a common prime of the good pair `(r',b)` transfers through both similarities to divide both `r` and `a`, contradicting `gcd(r,a)=1`.
4. For the final indexing, let `G` be the good set and prove that translation by `L` is an order-preserving bijection `G\to G\cap[k+L,\infty)`. Exactly `T=|G\cap[k,k+L-1]|` good elements precede the translated tail, so the translated `n`th good element is the `(n+T)`th good element. This avoids endpoint ambiguity in an informal block count.
5. Name the tools actually used from `knowledge_base.md`: strong induction, minimal-counterexample/extremal principle, divisor analysis, and modular arithmetic/periodic residue masks.

No change of strategy is needed.

## multiplicative-color-descent — APPROVE

This is also a whole proof and the three propagation rules genuinely suffice for similarity invariance. It is mathematically sound, but it is the most technically expensive route because the large-prime propagation lemma contains a nested minimal descent.

Specific load-bearing points the builder must make explicit:

1. For rule (iii), assume a least `n\ge k` such that `n` is bad but `nq` is good, where `q>k` is prime. A good witness `x<n` coprime to `n` must satisfy `q\mid x`, or else it would be a legal move from good `nq`. Write `x=q^r y` with `r\ge1` and `q\nmid y`. Prove `y>1`: if `y=1`, then `x=q^r` is coprime to the good number `k<x` because `q>k`, contradicting goodness of `x`.
2. Let `\alpha` be least with `y^\alpha\ge k`. Since `nq` is good and coprime to `y^\alpha`, the latter is bad. The strict estimate must be displayed:
   `y^\alpha<ky<qy=x/q^{r-1}<n/q^{r-1}`.
   Thus `q^{r-1}y^\alpha<n`. Starting with bad `y^\alpha`, repeatedly apply the minimality of `n` to the bad inputs `q^j y^\alpha<n` for `0\le j<r`, obtaining that `q^r y^\alpha` is bad. But this number is a multiple of the good integer `x=q^r y`, contradicting rule (i). Without this exact chain, rule (iii) remains a gap.
3. In the similar-multiple descent, if `p\mid d/c` and `p\le k`, similarity gives `p\mid c`; hence `p^2\mid d`, allowing `d=(p)(d/p)` in rule (ii). Its contrapositive gives goodness of `d/p`. If `p>k`, use the contrapositive of rule (iii). In both cases verify that `c\mid d/p`, that `c` and `d/p` remain similar, and that `d/p<d`.
4. The game terminology is optional and adds no license to skip the recursion. Prove the P-position recursion directly for this finite decreasing game, then prove its good positions are exactly the greedy enumeration.
5. Give the same exact order-preserving bijection/index argument for the final periodic enumeration as requested above.

No change of strategy is needed, but because rule (iii) is substantially longer than the compression proof, this approach is ranked below the other two and is not in this round's build set.

## small-witness-kernel — APPROVE

This is a valid complete route. Its stronger theorem—every two good integers share a prime at most `k`—is correctly supported by compression and extremal descent, rather than assumed from the fixed prime support of `k`. It therefore avoids the false stronger assertions recorded by the structural explorer.

Specific load-bearing points the builder must make explicit:

1. Define a violating pair as two good integers having no common small prime. Order it as `b\le b'` and minimize `b'`. Since `b` and `k` are good, they share some prime dividing `k`, hence a small prime. That prime cannot divide `b'`, so in particular `b<b'`.
2. Compress `b` to `x` with `k\le x\le b`, the same small-prime mask as `b`, and no large prime factors. Then `gcd(x,b')=1`: a common prime would be small because all factors of `x` are small, but would then be a common small prime of `b,b'`. Thus `x` cannot be good, since `b'>x` is good and good integers cannot be coprime.
3. From badness of `x`, obtain a good witness `b^*<x` coprime to `x`. Every small prime of `b` divides `x`, so no small prime is common to `b^*` and `b`. The new violating good pair `(b^*,b)` has larger member exactly `b<b'`, giving the required strict contradiction. These inequalities and the fact that both members are good are essential.
4. For similarity invariance, if bad `a` and good `b` are similar, take good `r<a` coprime to `a`. The small-witness theorem applied to good `b,r` yields a small prime dividing both; similarity transfers it from `b` to `a`, contradiction. This works regardless of the order of `a,b` and should be stated that way.
5. Supply all compression boundary cases and the exact periodic-enumeration indexing argument specified for the first approach; name strong induction, extremal principle, divisor analysis, and modular arithmetic from `knowledge_base.md`.

No change of strategy is needed. This route is slightly longer than direct similarity invariance but packages the strongest structural lemma cleanly and is worth building in parallel.

## Ranking and selection

All three new approaches were registered. Head-to-head, `small-prime-mask-compression` ranks above `small-witness-kernel` because it reaches mask invariance with one fewer extremal lemma. `small-witness-kernel` ranks above `multiplicative-color-descent` because its descent is short and transparent, whereas the latter's rule (iii) needs a delicate threshold-power iteration. The build set contains the two strongest distinct proof presentations; both target the entire theorem.

build set: small-prime-mask-compression, small-witness-kernel