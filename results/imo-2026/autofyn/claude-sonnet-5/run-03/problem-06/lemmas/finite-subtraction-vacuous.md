## Lemma (finite subtraction is vacuous for finiteness) — NEGATIVE / cautionary

**Statement.** Let $Q$ be any set and $\Lambda$ a **finite** set. Then
$Q\setminus\Lambda$ is finite if and only if $Q$ is finite.

**Proof.** ($\Leftarrow$) $Q\setminus\Lambda\subseteq Q$, a subset of a
finite set. ($\Rightarrow$) $Q=(Q\cap\Lambda)\cup(Q\setminus\Lambda)$;
$Q\cap\Lambda\subseteq\Lambda$ is finite, so $Q$ is a union of two finite
sets, hence finite. $\blacksquare$

### Why this matters (negative result, round 3)
The round-3 outline for `jacobsthal-covering-bound` proposed: since the
"adjacent-link" prime set $\Lambda$ is now known finite
(`lambda-stabilization.md`), split the target active prime set
$Q=\Lambda\cup(Q\setminus\Lambda)$ and reduce Hypothesis SS to proving
$Q\setminus\Lambda$ finite, hoped to be an easier target. This lemma shows
that reduction is **vacuous**: once $\Lambda$ is finite, "$Q\setminus
\Lambda$ finite" is logically **equivalent** to "$Q$ finite" — the
original, unreduced central gap. No difficulty is removed by peeling off
$\Lambda$, because $\Lambda$ does not confine $Q\setminus\Lambda$ to any
fixed finite universe (unlike how $U=\{p\le R\}$ confines $\Lambda$
itself).

### Provenance
`approaches/jacobsthal-covering-bound.md`, round 3, §6. Verified by the
proof-reviewer round 3: the set-theoretic claim is elementary and
correct, and the round's application of it (showing the $\Lambda$-split
buys nothing) is a legitimate, non-strawman critique of the proposed
reduction — not a misrepresentation of it.

### Status
General-purpose cautionary lemma. Useful to any future approach
considering a "split off a known-finite piece" reduction of the central
gap: such a split only reduces difficulty if the removed piece is known
to intersect the *unbounded direction* of the target set in a way that
genuinely confines the remainder to a fixed finite universe — finiteness
of the removed piece alone is not enough.
