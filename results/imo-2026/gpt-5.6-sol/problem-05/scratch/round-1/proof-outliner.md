## imo-2026-05

orbit-displacement-approximation: new
Target: Determine all functions satisfying the chained inequality, proving that they are exactly \(f(x)=x+c\) for constants \(c\ge0\), and verify every such function.
Technique: SOS residual identities, equality-case intersection, arithmetic-orbit invariant, and nearest-integer approximation; this adapts the orbit-extraction/telescoping philosophy of `aimo-0710` and the intersected equality conditions of `aimo-0288`.
Skeleton:
  1. Square the positive inequalities and define the lower and upper residuals \(L,U\) — by positivity and the knowledge-base entries **Standard inequalities** and **SOS / completing the square**.
  2. Derive \(L+U=2(x-f(y))^2\) and \(L-U=2(g(x)-g(y))(x+y+f(x)+f(y))\), where \(g=f-\mathrm{id}\) — by exact expansion and factorization.
  3. Put \(x=f(y)\); since \(L,U\ge0\) and their sum is zero, obtain \(f(f(y))+y=2f(y)\), equivalently \(g(f(y))=g(y)\) — by equality-case intersection.
  4. Iterate to get \(f^n(y)=y+n g(y)>0\) for every \(n\ge0\), hence \(g(y)\ge0\) — by induction and positivity.
  5. From \(|L-U|\le L+U\), obtain the sharp comparison \(|g(x)-g(y)|(x+y+f(x)+f(y))\le(x-f(y))^2\) — by the triangle bound for two nonnegative residuals.
  6. For points \(p,q\) with positive displacements, compare far-out terms of their two arithmetic orbits and choose indices by the nearest-integer principle so that one orbit term stays within a bounded distance of the successor on the other; the denominator tends to infinity, forcing \(g(p)=g(q)\) — by Archimedean approximation.
  7. Prove the boundary lemma excluding coexistence of \(g=0\) and \(g>0\), thereby making \(g\equiv c\ge0\) globally — builder must supply a new limiting or algebraic mechanism, not falsely approximate a stationary orbit by a diverging one.
  8. Substitute \(f(x)=x+c\): both squared residuals equal \((x-y-c)^2\), so both original inequalities hold; positivity of the codomain is equivalent to \(c\ge0\) — by direct verification and **Check the answer**.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Orbit lemma: \(f^n(y)=y+n g(y)\) and \(g(y)\ge0\) — because \(x=f(y)\) annihilates the total residual and positivity forbids a negative arithmetic increment.
  - Positive-orbit comparison: any two positive values of \(g\) coincide — because nearest-integer alignment keeps \(x_n-f(y_m)\) bounded while the coefficient of \(|g(x_n)-g(y_m)|\) diverges.
  - Zero/positive exclusion: \(g(p)=0<g(q)\) is impossible — mechanism still to be discovered; direct orbit alignment does not work because the zero orbit is stationary.
Open gaps: Step 7 is the principal gap; Step 6 needs a fully quantified index-selection argument covering rational and irrational ratios.
Cases to cover: \(g(p),g(q)>0\); one displacement zero and one positive; final parameter \(c=0\) and \(c>0\).
Watch out for: Orbit invariance alone does not imply global constancy. Do not assume continuity, monotonicity, injectivity, or surjectivity. The dynamics explorer's identity-only guess is refuted by every \(c>0\) translation.
Proposed build nomination: yes; this is the strongest route because Steps 1–6 are concrete and the exact remaining boundary is isolated.

cone-graph-rigidity: new
Target: Determine all functions satisfying the chained inequality, proving and verifying exactly the translations \(f(x)=x+c\), \(c\ge0\).
Technique: Geometric reformulation as a two-point cone constraint and rigidity classification of its graph; this adapts the symmetric-pair graph viewpoint of `aimo-0552` but not its unavailable uniqueness hypothesis.
Skeleton:
  1. Square and factor the two residuals as in the first approach, but retain both the original and swapped ordered-pair inequalities — by **SOS / completing the square** and **Exploit symmetry**.
  2. Derive the two cone bounds
     \[|g(x)-g(y)|\le\frac{(x-f(y))^2}{S(x,y)},\qquad |g(x)-g(y)|\le\frac{(y-f(x))^2}{S(x,y)},\]
     where \(S=x+y+f(x)+f(y)>0\) — by applying \(|L-U|\le L+U\) to both orientations.
  3. Also derive the crossed factorization \(U(x,y)-L(y,x)=-(g(x)+g(y))(2(x-y)+g(x)-g(y))\) and its swapped companion — by cancellation of shared squares, analogous to the cancellation move in `aimo-0988`.
  4. Prove a metric graph-rigidity lemma: any graph over \(\mathbb R_{>0}\) satisfying both cone bounds for all pairs lies on a line parallel to the diagonal, so \(g\) is constant — by selecting intermediate domain points near the two reflected centers and combining the two orientations; no regularity may be inserted.
  5. Show the constant is nonnegative because \(x+c>0\) for every \(x>0\) — by taking \(x\downarrow0\) arithmetically, without continuity of \(f\).
  6. Verify the full family directly, with both residuals \((x-y-c)^2\) — by **Check the answer**.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Two-cone rigidity: the paired distances to the reflected centers force every pair of graph points to have equal displacement — because both orientations constrain the same vertical difference by quadratic transverse errors, while crossed factorization supplies the missing sign information.
  - Parameter sign: a constant displacement must satisfy \(c\ge0\) — because if \(c<0\), choosing \(0<x<-c\) contradicts positivity of \(f(x)=x+c\).
Open gaps: Step 4 is a substantial, presently unproved classification lemma; the builder must produce explicit intermediate points and inequalities rather than label the graph “nonexpansive.”
Cases to cover: possible signs of \(g(x)+g(y)\) in the crossed factorization; equal and unequal reflected centers; constant \(c\) positive, zero, or negative.
Watch out for: Ordinary Lipschitz control is too weak. No compactness, extrema, or continuity is available. This is deliberately a different global graph framing, not another orbit proof.
Proposed build nomination: yes as a high-diversity second build, despite its harder central lemma.

quadratic-interval-collision: new
Target: Determine all functions satisfying the chained inequality, proving and verifying exactly \(f(x)=x+c\) for \(c\ge0\).
Technique: Quadratic feasible-interval intersection, adapting the two-substitution candidate collision from `aimo-0186` to real intervals.
Skeleton:
  1. Regard the two squared inequalities as simultaneous quadratic restrictions on one unknown value, first \(f(y)\) with \(x,f(x),y\) fixed and then \(f(x)\) with \(x,y,f(y)\) fixed — by **Quadratic forms** and root-interval analysis.
  2. Compute the interval endpoints/discriminants and record that the total residual width collapses at \(x=f(y)\) — by completing the square.
  3. Obtain \(f(f(y))=2f(y)-y\), so values at \(y,f(y),f(f(y))\) form an arithmetic triple — by the unique-point collision at zero total residual.
  4. For arbitrary \(a,b\), generate two independent feasible intervals for the same target value using the triples based at \(a\) and \(b\); choose concrete substitutions among \((f(a),b)\), \((f(b),a)\), and their iterates so that the intersection is a singleton exactly when \(f(a)-a=f(b)-b\) — by the `aimo-0186` two-substitution pinning paradigm.
  5. Conclude \(f(x)-x=c\) globally, use codomain positivity to get \(c\ge0\), and verify all translations — by direct classification and substitution.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Iterate collision: \(f(f(y))=2f(y)-y\) — because both nonnegative residuals sum to zero at \(x=f(y)\).
  - Two-interval pinning: the two independently generated quadratic intervals for the same value intersect only at the common-displacement value — because their distinct centers and endpoint factorizations eliminate the alternative interval branches, as discrete candidate sets were eliminated in `aimo-0186`.
Open gaps: Step 4 is wholly unproved: the builder must exhibit valid substitutions and calculate the interval intersection. If it only recovers orbit invariance, this approach has collapsed into the first framing and should be rethought.
Cases to cover: nested, crossing, and tangent feasible intervals; degeneracy at \(a=b\) or \(f(a)=a\); final sign of \(c\).
Watch out for: Feasible sets are intervals, not two-point sets, so the analogy with `aimo-0186` may fail without an exact tangency. Do not use continuity to force endpoint contact.
Proposed build nomination: reserve/third choice; build only if the reviewer sees a concrete collision not visible in the current skeleton.

reflected-inverse-dynamics: new
Target: Determine all functions satisfying the chained inequality, proving and verifying exactly \(f(x)=x+c\) for \(c\ge0\).
Technique: Reflected-map substitution, inverse dynamics, and threshold decomposition; inspired by the orbit-recurrence move of `aimo-0588` and composite-then-iterate move of `aimo-0253`.
Skeleton:
  1. Set \(g=f-\mathrm{id}\) and \(T(x)=2x-f(x)=x-g(x)\); rewrite the two residual inequalities as
     \[(T(x)-y)^2+4x(g(x)-g(y))\ge0\]
     and
     \[(T(x)-y)^2-2(g(x)-g(y))(y+f(y)+g(x))\ge0\] — by exact expansion.
  2. Whenever \(T(x)>0\), put \(y=T(x)\); the opposite signs and positive multipliers force \(g(T(x))=g(x)\), hence \(f(T(x))=x\) — by a two-sided squeeze.
  3. Decompose the domain into the reflected region \(R=\{x:f(x)<2x\}\) and its complement, and prove that the inverse identity on \(R\) forces two-sided arithmetic dynamics on every component contained in \(R\) — by iteration and **Invariant / monovariant**.
  4. Use positivity in both time directions to show such a component has zero displacement; separately analyze the threshold/complement where positive translations necessarily have \(T(x)\le0\) for small \(x\) — by arithmetic-sequence positivity and exhaustive casework.
  5. Prove that the threshold boundary propagates one common positive displacement from the complement to all of \(R\), or else all displacement is zero — by feeding boundary points back into the original two-variable inequalities.
  6. Verify \(f(x)=x+c\), \(c\ge0\), directly — by residual computation.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Local inverse lemma: \(f(2x-f(x))=x\) whenever \(2x-f(x)>0\) — because choosing the reflected argument annihilates both square terms and squeezes the displacement difference to zero.
  - Threshold classification: the set where the reflected argument leaves the positive domain determines a single translation intercept — proposed mechanism is propagation through cross-region pairs, still unproved.
Open gaps: Steps 3–5, especially threshold classification. A proof of the false global claim \(f(x)<2x\) would discard all solutions with \(c>0\), so it is not acceptable.
Cases to cover: \(T(x)>0\), \(T(x)=0\), and \(T(x)<0\); the identity branch and positive-translation branch.
Watch out for: The substitution \(y=T(x)\) is legal only when \(T(x)>0\). Two-sided dynamics cannot be asserted globally for translations. Do not repeat the explorer's identity-only conclusion.
Proposed build nomination: reserve as a genuinely different dynamics framing; advance after a threshold propagation lemma is found.
