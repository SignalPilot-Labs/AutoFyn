## Statement

For any fixed multiset of pieces and any $0\le k\le n$, the minimum over
Xiang Yu responses using **at most $k$** marks of $A(\text{response})$ is
$\ge$ the minimum over responses using **at most $n$** marks. (I.e.
restricting a player's budget can only weakly help the opponent's
minimization.)

## Proof

Trivial: every $\le k$-mark strategy is in particular a $\le n$-mark
strategy ("at most $n$" is a threshold, not a requirement to use all
marks), so the feasible set for budget $k$ is a subset of the feasible set
for budget $n$, and the minimum over a subset is $\ge$ the minimum over the
superset. See
`results/imo-2026-03/approaches/self-similar-potential-certificate.md`,
Lemma C.

## Certification note (proof-reviewer, round 2)

One-line, immediate from monotonicity of $\min$ over nested feasible sets —
no computation needed to certify. Certified correct. Useful for composing
partial-budget lemmas (e.g. applying `untouched-top-piece-lower-bound`'s
tail bound, which was proved at the tail's *own* full budget, in a context
where the tail is only given $n-c\le n$ marks).
