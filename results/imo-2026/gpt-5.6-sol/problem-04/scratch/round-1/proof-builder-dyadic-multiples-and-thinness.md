## Build result: dyadic-multiples-and-thinness

## Status
solved

## Summary
Completed the whole proof and wrote it to the owned approach file. The winning angles are exactly
\[
\theta=180^\circ/n\qquad(n\in\mathbb Z,\ n\ge2).
\]

The reciprocal direction uses a cumulative \(t\)-grid mark to create complementary multiples in the two possible children, followed by balanced splitting of an integer multiple. All cuts are shown legal, the boundary-mark case is handled, \(n=2\) is included, and an explicit finite depth bound is proved.

For necessity, the finite-horizon sets are nested as required:
\(W_{r+1}=W_r\cup\operatorname{Pre}(W_r)\). The proof establishes the exact finite-strategy/rank equivalence, including the nonuniform finite-horizon direction through König's infinity lemma on the response tree of one fixed strategy and initial state.

The principal affine gap was closed with a stronger normal form. Under the nonreciprocal hypothesis \(1\notin t\mathbb Z_{>0}\), each \(W_r\) is contained in finitely many lines on which one parent angle equals \(kt\). For a cut from angle \(a\), inherited witness coordinates immediately give a parent multiple. The four remaining ordered witness pairings give respectively
\[
a=(p+q)t,\quad b=(q-p)t,\quad c=(p-q)t,\quad 1=(p+q)t.
\]
Positivity handles the signs and excludes zero coefficients; the final pairing is precisely the forbidden reciprocal dimension jump. This also proves fixed-depth finiteness and handles strict cut legality. An elementary countable-line avoidance argument then produces a state outside every finite horizon.

## Promotable lemmas
- Finite-rank multiple-line lemma.
- Finite-strategy/rank equivalence for binary reachability games.
- Grid-mark fork and dyadic descent.

## Output
`results/imo-2026-04/approaches/dyadic-multiples-and-thinness.md`
