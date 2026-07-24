## Statement (CERTIFIED — round 32, proof-reviewer)

**Fact 2.** For any finite multiset $S=\{L_1\ge L_2\ge\dots\ge L_k\}$ of
nonnegative reals, with $A(S):=\sum_{i=1}^k(-1)^{i+1}L_i$ the
alternating-sum-of-sorted-descending-order functional of the certified
`integral-alternating-sum-formula` lemma,
$$0\ \le\ A(S)\ \le\ \mathrm{Total}(S),\qquad \mathrm{Total}(S):=\sum_{i=1}^k L_i.$$

(Only the upper bound $A(S)\le\mathrm{Total}(S)$ is the content newly
extracted here as a standalone, citable fact; the lower bound $A(S)\ge0$ is
already part of `integral-alternating-sum-formula`'s stated consequence.
Both hypotheses used throughout this problem's approach files require only
$L_i\ge0$, not $L_i>0$.)

## Proof

**Direct combinatorial proof (pairing).** Sort $S$ descending
$L_1\ge\dots\ge L_k\ge0$. Group consecutive elements into pairs
$(L_1,L_2),(L_3,L_4),\dots$; if $k$ is odd, the last element $L_k$ is left
unpaired. Then
$$A(S)=\sum_{i=1}^{\lfloor k/2\rfloor}(L_{2i-1}-L_{2i})\ +\ [k\text{ odd}]\cdot L_k.$$
For each pair, $L_{2i-1}-L_{2i}\le L_{2i-1}+L_{2i}$ holds because this is
equivalent to $-L_{2i}\le L_{2i}$, i.e. $L_{2i}\ge0$, which holds by
hypothesis. Summing this pairwise bound over all pairs, and bounding the
possible unpaired last term trivially by itself ($L_k\le L_k$), gives
$$A(S)\ \le\ \sum_{i=1}^{\lfloor k/2\rfloor}(L_{2i-1}+L_{2i})\ +\ [k\text{
odd}]\cdot L_k\ =\ \sum_{i=1}^k L_i\ =\ \mathrm{Total}(S).$$
(The lower bound $A(S)\ge0$ follows identically: each pair contributes
$L_{2i-1}-L_{2i}\ge0$ since the sequence is sorted descending, and the
possible last unpaired term $L_k\ge0$ by hypothesis; summing nonnegative
terms is nonnegative.) $\blacksquare$

**Cross-check via the already-certified integral formula.** This is also an
immediate restatement of a fact already recorded, without being separately
named, inside `integral-alternating-sum-formula`'s own stated consequence
"$\Phi(S)=(\mathrm{Total}(S)+A(S))/2$ and $0\le A(S)\le\mathrm{Total}(S)$" —
i.e. Fact 2's content was already implicitly certified there (round 1); this
lemma file exists only to give it a standalone name and an independent
from-scratch (non-integral, purely combinatorial) proof, since it is now
being cited by name across multiple approach files
(`rank-pigeonhole-budget.md` §5.2, used informally there; and this round's
`greedy-halving-adversary.md` closure of $h(m)$'s vertex $c=t\in S''$, Case
(ii)).

## Origin / usage

Extracted as a standalone lemma in round 32 of `imo-2026-03`, per the
proof-outliner's instruction, from informal use in
`rank-pigeonhole-budget.md` §5.2 and this round's need to cite it by name
from `greedy-halving-adversary.md`. Used to close $h(m)$'s vertex
$c=t\in S''$, Case (ii) ("$q_2$ untouched, $t\ne q_2$"): combined with mass
conservation under refinement and the ladder's telescoping identity, it
gives $A(S''\setminus\{t,q_2\})\le\mathrm{Total}(S''\setminus\{t,q_2\})
=q_2-f(m)-t<q_2-f(m)$ directly, with no vertex enumeration and no
dependence on $\mathrm{MaxCeil}$.
