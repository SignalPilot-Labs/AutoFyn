## Statement

Let $p_1>p_2\ge\dots\ge p_{n+1}$ be Liu Bang's ladder pieces,
$p_i=2^{n+1-i}/(2^{n+1}-1)$, $r:=p_2+\dots+p_{n+1}=1-p_1$. If Xiang Yu's
response leaves $p_1$ completely uncut (all cuts confined to the other $n$
pieces, refined however he likes), then $\Phi(\text{final multiset}) \ge
p_1 = 2^n/(2^{n+1}-1)$.

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 6:
split the integral of the certified integral-alternating-sum-formula lemma
at $x=r$, using that every piece of the refinement $G'$ of the bottom $n$
pieces is $\le r < p_1$.

## Certification note (proof-reviewer, round 1)

Independently spot-checked numerically for $n=1,2,3,4$: generated the exact
ladder, applied 2000 random refinements of the bottom $n$ pieces each (random
number of random cuts per piece), and confirmed $\Phi \ge p_1$ held in every
trial with no violation. The written integral-splitting proof is also
algebraically sound (checked by hand). Certified correct **for the stated
special case only** — it does NOT cover Xiang Yu also cutting $p_1$ itself,
which remains open (see the "Open gaps" section of
`greedy-halving-adversary.md`).
