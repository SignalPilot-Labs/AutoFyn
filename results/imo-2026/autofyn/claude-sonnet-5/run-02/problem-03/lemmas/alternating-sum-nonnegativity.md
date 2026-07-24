## Alternating-Sum Nonnegativity (new, round 19, certified by reviewer)

**Statement.** For any finite multiset $S$ of nonnegative reals sorted
descending $r_1\ge r_2\ge\cdots\ge r_k\ge0$,
$$A(S)=r_1-r_2+r_3-\cdots\ \ge\ 0.$$

**Proof.** Group consecutive pairs from the front:
$(r_1-r_2)+(r_3-r_4)+\cdots\ge0$, since $r_{2j-1}\ge r_{2j}$ for each $j$
(sorted descending); if $k$ is odd, the single unpaired last term $r_k\ge0$
is simply added on. Every summand in this grouping is $\ge0$ (each is
either a nonnegative difference of consecutive sorted terms, or the final
nonnegative unpaired term), so the total is $\ge0$. $\blacksquare$

**Provenance and verification.** First stated and proved (as "Fact 1") in
`approaches/greedy-halving-adversary.md`, Theorem 35 (round 19), where it
is used together with the certified `dominant-element-removal-identity`
(Fact 2 there) to close the "$p_3$ untouched" sub-case of the middle-band
target $\Delta(n,v)\le v-f(n)$. The proof is elementary and correct
(a standard telescoping/grouping argument); the proof-reviewer confirms it
directly, and notes it is presumably implicit in the proof machinery of
`max-domination-lemma` and similar existing facts, but was not previously
stated as a standalone reusable lemma.

**Usage.** General-purpose: applies to any finite nonnegative multiset,
no ladder or refinement structure required. Reusable wherever a bare
nonnegativity fact about a sorted alternating sum is needed as a building
block (as opposed to the sharper `max-domination-lemma`, which bounds
$A(S)$ above by $\max(S)$).
