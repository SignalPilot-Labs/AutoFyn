## orbit-displacement-approximation — CHANGES REQUESTED

This is a whole attempt and its main route is sound. Steps 1–5 follow from the exact residual identities. Step 6 is also valid once quantified: if the two positive displacements are \(a,b\), take \(m\to\infty\) and choose \(n\) nearest to \(((m+1)b+q-p)/a\). Then \(|p+na-(q+(m+1)b)|\le a/2\), while both orbit indices and the denominator in the cone estimate tend to infinity, forcing \(a=b\). Treat the finitely many initial choices for which the nearest integer is not nonnegative separately.

The advertised Step 7 gap is fixable and should not remain an unspecified “limiting or algebraic mechanism.” After Step 6, \(g\) takes values in \(\{0,c\}\) for one fixed \(c>0\), unless one of those classes is empty. Use the two oriented cone bounds to prove both fibers are open. If \(g(p)=0\), then for any \(x\) with \(g(x)=c\),
\[
c\bigl(x+p+f(x)+f(p)\bigr)\le (x-f(p))^2=(x-p)^2,
\]
so no positive-displacement points can approach \(p\). Conversely, if \(g(q)=c\), then for any \(y\) with \(g(y)=0\), the same first cone bound with \((x,y)=(q,y)\) gives
\[
c\bigl(q+y+f(q)+f(y)\bigr)\le(q-y)^2,
\]
so no zero-displacement points can approach \(q\). Thus the two fibers are disjoint open subsets partitioning the connected interval \(\mathbb R_{>0}\), a contradiction. The builder should spell out the local-radius argument rather than merely invoke these inequalities. Then verify \(f(x)=x+c\) in the unsquared original chain (or explicitly invoke positivity to justify equivalence after checking the squared residuals), including \(c=0\).

## cone-graph-rigidity — CHANGES REQUESTED

The exact paired cone estimates and crossed factorization are algebraically correct, and the framing can in principle classify the graph. However, Step 4 currently hands off essentially the entire rigidity theorem without the promised mechanism: no intermediate points are specified, no inequalities are combined, and the crossed factorization itself supplies no sign information because \(U(x,y)-L(y,x)\) has no known sign. A builder must not assert the metric-rigidity lemma from ordinary Lipschitz language or continuity.

To make this buildable, replace Step 4 with an explicit argument. One available rigorous completion starts from the cone estimate at \(x=f(y)\), obtaining orbit invariance and nonnegative displacement; it then aligns positive arithmetic orbits and uses the open-fiber/connectedness argument described above. That completion is sound, but it collapses this proposal into the orbit approach rather than preserving the claimed distinct graph route. Without a genuinely direct graph-classification calculation, this is weaker than the leader and should not be built this round.

## quadratic-interval-collision — RETHINK

Step 4 is not a lemma with a mechanism but a conjectural analogy: it gives no common target value, no two concrete substitutions, no interval endpoints, and no proof that the intervals are tangent rather than overlapping. Feasible sets here are intervals, so the cited discrete candidate-collision paradigm does not imply singleton intersection. Everything proved before Step 4 is exactly the orbit recurrence already available in the leading approach. The builder would be asked to discover the whole missing rigidity argument, so this outline is not ready. Re-propose only after explicitly computing two intervals whose intersection forces equal displacement, or choose a genuinely different route.

## reflected-inverse-dynamics — RETHINK

Steps 1–2 are correct (the displayed residual rewrites were checked), but Steps 3–5 do not form a sound skeleton. “Components contained in \(R\)” has no justified interval/topological structure because no regularity of \(T\) is known; the local inverse identity does not by itself permit two-sided iteration while remaining in \(R\). The threshold classification and cross-region propagation are the entire hard part and are supplied only as goals, not mechanisms. This is especially hazardous because genuine translations have \(T(x)\le0\) on an initial interval. Re-propose only with an explicit invariant region and a proved propagation inequality that covers \(T\le0\), rather than component language.

The field has some framing diversity, but three proposals leave their global classification as an unsupported central lemma. The orbit route is decisively strongest because its only boundary gap closes by a short open-fiber/connectedness argument.

build set: orbit-displacement-approximation