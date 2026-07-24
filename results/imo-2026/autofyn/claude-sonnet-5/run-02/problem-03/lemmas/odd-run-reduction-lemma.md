## Statement

Let $S$ be a finite multiset of positive reals. For each distinct value $v$
occurring in $S$ with multiplicity $\mu(v)$, let $S'$ be the multiset
obtained by keeping exactly one copy of $v$ if $\mu(v)$ is odd, and zero
copies if $\mu(v)$ is even. Then
$$A(S) = A(S'),$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order functional
of the certified `integral-alternating-sum-formula` lemma. Since $S'$ has all
distinct values, $A(S')$ is the ordinary alternating sum of $S'$'s (distinct,
sorted) values, with no tie-breaking ambiguity.

This **strictly generalizes** the certified `leftover-formula` lemma, which
required the multiset to decompose as exactly one unpaired element plus
exactly-equal pairs (i.e. at most one value with odd multiplicity); this
lemma allows any number of values to have odd multiplicity simultaneously —
the situation that routinely arises at the "vertex" configurations
identified by `vertex-minimum-theorem`.

## Proof

See `results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`, §2. It
suffices to show that removing any two elements of $S$ that are (a) equal in
value and (b) adjacent in sorted order leaves $A$ unchanged, then apply this
repeatedly, pairing off copies within each value's run two at a time, until
every value's remaining multiplicity is $\le1$; this terminates in finitely
many steps and produces exactly $S'$. For the one-step claim: any two copies
of a value $w$ occupy adjacent sorted ranks $r,r+1$ within that value's
contiguous run (values equal to $w$ form a contiguous block in sorted order,
so any two copies may be relabeled, WLOG, to occupy the last two ranks of
that run without changing which other elements they are adjacent to). Their
combined contribution to $A$ is $(-1)^{r+1}w+(-1)^{r+2}w=0$ (consecutive
signs cancel). After removal, every element originally at rank $>r+1$ shifts
down by exactly $2$, and $(-1)^{(\text{rank}-2)+1}=(-1)^{\text{rank}+1}$
(subtracting an even number preserves sign), so every other term's
contribution to $A$ is unchanged. Hence removing the pair leaves $A$
unchanged.

*(Alternative one-line proof, equivalent in substance: apply
`pair-cancellation-identity` repeatedly — it makes no adjacency assumption,
since it works via the parity of $N_S(x)$ directly, so it independently
confirms this lemma's conclusion by a different, non-inductive route.)*

## Certification note (proof-reviewer, round 3)

Independently re-verified by an exact-`Fraction` script: 20000 random trials,
multisets of size 1–8 with random repeated values, comparing $A(S)$ (direct
sort-and-alternate-sum) against $A(S')$ (odd-run reduction) — zero
mismatches. Cross-checked by hand on the concrete $n=3$ ladder vertex example
$S=\{4,4,3,2,1,1\}$ (units $1/15$): odd-run reduction gives $S'=\{3,2\}$,
$A(S')=1=15\cdot a_3$, matching both a direct brute-force computation and an
independent hand re-derivation in
`results/imo-2026-03/approaches/exchange-argument-extremal-response.md` (via
repeated `pair-cancellation-identity`) of the same instance. The two proofs
(adjacent-pair-removal induction here, vs. direct parity argument for
`pair-cancellation-identity`) are logically independent routes to the same
fact, both verified correct. Certified correct, fully general — no
game-specific structure required, strictly generalizes `leftover-formula`.
