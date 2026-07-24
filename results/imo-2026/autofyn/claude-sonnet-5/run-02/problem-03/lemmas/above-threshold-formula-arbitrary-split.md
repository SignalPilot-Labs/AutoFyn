## Statement

Fix the $n$-ladder ($n\ge1$), $p_1$ = top piece, $r=1-p_1$ = tail total.
Suppose Xiang Yu splits $p_1$ into $c+1$ fragments $f_1\ge\dots\ge f_{c+1}>0$
(summing to $p_1$, any $0\le c\le n$) and refines the tail separately into a
multiset $G'$ of total $r$. Then the contribution to $A(\{f_1,\dots,f_{c+1}\}
\cup G')$ from the interval $[r,p_1)$ is exactly
$$A_1 = \max(f_1-r,\,0).$$

## Proof

See `results/imo-2026-03/approaches/self-similar-potential-certificate.md`,
Lemma B: since $G'$ has total mass $r$, no piece of $G'$ exceeds $r$, so on
$[r,p_1)$ only $p_1$'s fragments are counted; at most one fragment (namely
$f_1$, if $f_1>r$) can exceed $r$ since $p_1\le2r$ for the ladder at every
$n\ge1$ (with equality at $n=1$). Two-case computation (`$f_1\le r$` vs.
`$f_1>r$`) gives the stated formula. This generalizes the previously-certified
`untouched-top-piece-lower-bound`'s $c=0$ computation (where $A_1=p_1-r=f(n)$
exactly) to every split $c$ of the cut budget, and follows as a special case
of the more general certified `cross-term-identity-threshold` /
`dominant-element-removal-identity` lemmas restricted to the ladder's
specific numeric dominance $p_1\le2r$.

## Certification note (proof-reviewer, round 2)

Independently re-verified by an exact-`Fraction` script: for $n=1,\dots,4$,
500 random fragmentations of $p_1$ into $c+1\le n+1$ pieces, directly
computing the breakpoint integral of the odd-parity indicator over $[r,p_1)$
against the full multiset (fragments $\cup$ tail) and comparing to
$\max(f_1-r,0)$ — zero mismatches. Certified correct. Note: this lemma by
itself only computes the *above-threshold* contribution; the companion
below-threshold contribution ($[0,r)$, where fragments and $G'$ interleave)
is the located, still-open obstruction for $c\ge1$ (see both
`greedy-halving-adversary.md`'s "Missing inequality" and
`self-similar-potential-certificate.md`'s "open gap $1\le c\le n$" — the two
approaches independently converge on the same precise difficulty).
