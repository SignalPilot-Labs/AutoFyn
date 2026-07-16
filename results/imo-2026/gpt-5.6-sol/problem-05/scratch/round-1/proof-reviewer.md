## lattice-envelope-amplification

**Verdict: APPROVE**

**True Status: solved.** The builder's recorded `solved` status is correct.

**Scores**
- Correctness: 10/10
- Completeness / rigor: 10/10
- Progress: 10/10

**Raw Goal Progress**
- Actual goal checked: determine all positive-real functions satisfying the two-sided inequality, with an explicit characterization and direct verification.
- Necessity is complete. The proof first derives the two exact squared slacks, then forces arithmetic forward orbits and nonnegative displacement. A positive orbit supplies a tail lattice; nearest-lattice comparison yields the uniform estimate \(|g(t)-c|\le c^2/(8t)\). Evaluating this estimate along every other positive-displacement orbit forces every positive displacement to equal \(c\). The remaining range \(\{0,c\}\) is reduced to a constant by a direct, non-continuity-dependent clopen argument.
- Sufficiency is complete for every \(c\ge0\): both squared slacks are exactly \((x-y-c)^2\), and positivity makes the passage between original and squared inequalities reversible.
- All cases are present: no positive displacement gives \(c=0\); existence of positive displacement gives \(c>0\); the possible mixed zero/positive case is excluded.

**Independent load-bearing check**
I independently expanded the central identities with symbolic algebra and obtained exactly
\[
(f(x)+y)^2-4xf(y)=q+dC,
\qquad
2x^2+2f(y)^2-(f(x)+y)^2=q-dC,
\]
where \(q=(x-y-g(y))^2\), \(d=g(x)-g(y)\), and \(C=2x+2y+g(x)+g(y)\). I also re-derived the lattice estimate: the rounded integer \(k=\lfloor (t-v)/c+1/2\rfloor\) is at least one for \(t\ge v+c/2\), places \(t\) within \(c/2\) of \(v+kc\), and makes (D)'s right side at most \(c^2/4\), while its coefficient is at least \(2t\). Thus the claimed \(c^2/(8t)\) constant is correct. The candidate verification independently factors both squared slacks as \((x-y-c)^2\).

**Rigor checks**
- Squaring is reversible because every compared quantity is nonnegative (indeed positive).
- The displacement coefficient is positive; in fact it equals \(x+y+f(x)+f(y)>0\), so no hidden sign assumption is used.
- Orbit induction includes \(n=0\), and negative displacement is correctly contradicted using a positive iterate.
- The floor construction covers the entire stated tail and keeps the chosen orbit predecessor in the domain.
- Exactification treats only \(a>0\), exactly where the orbit tends to infinity.
- Closedness and openness are proved numerically from (D), without assuming continuity.
- Named knowledge-base tools are stated correctly and used appropriately.

**Promotable lemmas**
Certified and admitted to the shared cache:
- `arithmetic-orbit.md`
- `one-orbit-tail-envelope.md`
- `envelope-exactification.md`
- `zero-locus-dichotomy.md`

Each statement was narrowed to its proved hypotheses and supplied with a complete standalone proof or explicit imported hypothesis. No lemma was rejected.

**Ranking outcome:** `verified-milestone` — complete proof independently verified, including the tail estimate and direct sufficiency.

## orbit-collision-clopen

**Verdict: APPROVE**

**True Status: solved.** The builder's recorded `solved` status is correct.

**Scores**
- Correctness: 10/10
- Completeness / rigor: 10/10
- Progress: 10/10

**Raw Goal Progress**
- Actual goal checked: determine and verify all solutions. The proof obtains the same complete characterization
\[
\boxed{f(t)=t+c\ (t>0),\quad c\ge0}.
\]
- Necessity is complete through a route independent of the tail-envelope step: exact squared slacks imply (D), forced equality at \(x=f(y)\) gives arithmetic translation orbits, and a floor-based collision of any two positive-increment orbit lattices forces their increments to agree. The resulting two-valued displacement is made constant by the clopen zero-fiber argument.
- Sufficiency directly checks every member of the characterized family.

**Independent load-bearing check**
The load-bearing orbit-collision step is valid. For \(X_n=u+na\), choose
\[
k_n=\left\lfloor\frac{X_n-v}{b}\right\rfloor,
\qquad m_n=k_n-1.
\]
For all sufficiently large \(n\), \(m_n\ge0\), \(m_n\to\infty\), and
\[
0\le X_n-[v+(m_n+1)b]<b.
\]
Putting \(y=Y_{m_n}=v+m_nb\) in (D) makes its square exactly the square of this bounded residual. Hence
\[
|a-b|(2X_n+2Y_{m_n}+a+b)<b^2.
\]
If \(a\ne b\), the left side diverges because both orbit points diverge, an immediate contradiction. There is no omitted rational/irrational step-size case: the bounded floor residual works uniformly for arbitrary positive real \(a,b\).

I also independently expanded the paired squared slacks and obtained exactly (4)–(5), and independently factored both candidate slacks as \((x-y-c)^2\).

**Rigor checks**
- The displacement coefficient is correctly identified as \(x+y+f(x)+f(y)>0\); (D) does not depend circularly on the later proof that \(g\ge0\).
- The special substitution \(x=f(y)\) is legal, and both endpoints are computed.
- Orbit invariance and orbit formulas are proved by induction; the unused injectivity claim is also correctly proved.
- The floor indices are eventually nonnegative, and both orbit sequences tend to infinity.
- The no-positive-value and positive-value cases are exhaustive.
- Relative closedness and openness of the zero fiber use explicit inequalities, not continuity.
- The connectedness theorem is applied to the correct ambient interval.
- The final family includes and verifies the endpoint \(c=0\).
- Named knowledge-base tools are stated correctly and used appropriately.

**Promotable lemmas**
- The proposed orbit-displacement rigidity lemma is mathematically certified. Its arithmetic-orbit part is admitted as `arithmetic-orbit.md`; its positive-value equality conclusion is also fully proved by the reviewed floor-collision argument. I did not create a duplicate cache file for the combined formulation because the shared arithmetic-orbit lemma plus the approach's explicit collision proof already records the certified content.
- The proposed zero-fiber clopen lemma is certified and admitted as `zero-locus-dichotomy.md`.

No proposed lemma is false or stronger than proved.

**Ranking outcome:** `verified-milestone` — complete proof independently verified, including the floor collision and direct sufficiency.

## Overall certification

Both built approaches independently meet the repository definition of `solved`; both receive APPROVE. `current.md` has been updated to `solved` and contains the complete lattice-envelope proof. The explicit answer is \(f(t)=t+c\) for an arbitrary constant \(c\ge0\).
