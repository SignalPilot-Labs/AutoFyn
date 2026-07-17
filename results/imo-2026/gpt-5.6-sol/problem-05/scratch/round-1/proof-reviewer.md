## orbit-displacement-approximation

**Verdict:** APPROVE  
**True Status:** solved  
**Builder-recorded Status:** solved — correct.

### Scores
- **Correctness:** 10/10
- **Completeness / rigor:** 10/10
- **Progress:** 10/10
- **Raw Goal Progress:** 100/100 — complete classification, necessity, and direct sufficiency verification.

### Adversarial verification
The proof answers the actual compute-and-prove characterization problem and explicitly obtains
\[
f(x)=x+c\quad(c\ge0).
\]

The load-bearing residual algebra was independently re-derived. With
\[
L=(f(x)+y)^2-4xf(y),\qquad U=2(x^2+f(y)^2)-(f(x)+y)^2,
\]
one has exactly
\[
L+U=2(x-f(y))^2
\]
and
\[
L-U=2(g(x)-g(y))(x+y+f(x)+f(y)).
\]
Symbolic expansion reproduces both identities with zero residual. Substitution \(x=f(y)\) is legal because the codomain is positive; nonnegativity of \(L,U\) then forces each to vanish, and positivity selects the positive square root to give \(g(f(y))=g(y)\).

The orbit quantifiers are sound: induction yields \(f^n(y)=y+ng(y)\) for every integer \(n\ge0\), and positivity of every iterate excludes \(g(y)<0\). In the alignment argument, for each \(m\) an integer \(n_m\) with \(|n_m-r_m|\le1/2\) exists by the floor construction. Since \(r_m\to+\infty\), \(n_m\ge0\) for every sufficiently large \(m\); no density, rationality, or unstated common-subsequence assumption is needed. The resulting error is uniformly at most \(a/2\), while the coefficient multiplying \(|a-b|\) is at least \(q+mb\to\infty\), forcing \(a=b\).

The topology argument is complete without assuming continuity of \(f\). Once the range of \(g\) is contained in \(\{0,c\}\), estimate (7) supplies an explicit relative neighborhood of each zero-displacement point containing no positive-displacement point, and vice versa. Thus both fibers are relatively open, disjoint, nonempty, and cover \(\mathbb R_{>0}\), contradicting the connectedness theorem for real intervals. The endpoint-at-zero issue is handled by intersection with \(\mathbb R_{>0}\).

For \(f(x)=x+c\), independent symbolic calculation confirms that both squared residuals equal \((x-y-c)^2\ge0\). Positivity makes passage back to the original unsquared chain valid, and the codomain and boundary case \(c=0\) are explicitly checked.

The named ingredients are present and correctly used: sum-of-squares/completing-the-square, induction, the Archimedean property, the floor/nearest-integer lemma, and connectedness of real intervals. The knowledge-base citation requirement is met for the principal reformulation, while the other elementary tools are stated or proved in place.

### Promotable lemma certification
**Admitted:** `orbit-cone-rigidity`. Its statement is no stronger than the proof: the two stated hypotheses alone yield arithmetic positive-domain orbits, equality of all positive displacements, and exclusion of mixed zero/positive fibers by connectedness. A self-contained certified copy was written to `results/imo-2026-05/lemmas/orbit-cone-rigidity.md`.

### Reviewer action
Published the complete proof and set reviewer-owned `current.md` to `solved`. Recorded outcome `verified-milestone` for this slug.
