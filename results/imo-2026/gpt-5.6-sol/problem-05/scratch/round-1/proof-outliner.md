## imo-2026-05

orbit-collision-clopen: new
Target: Characterize all functions satisfying the two-sided inequality as exactly \(f(t)=t+c\) for constants \(c\ge 0\), proving necessity and verifying both inequalities.
Technique: Forced equality at an image point, arithmetic-orbit iteration, Archimedean nearest-lattice-point collision, and a clopen-set argument; this adapts the iterate/positivity move of `aimo-0710`, but the resulting invariant is a translation increment rather than an involution gap.
Skeleton:
  1. Square both inequalities (all quantities are positive) and introduce \(g(t)=f(t)-t\). Record the exact paired-slack identity
     \[
     |g(x)-g(y)|\,[2x+2y+g(x)+g(y)]\le (x-y-g(y))^2. \tag{D}
     \]
     — by expanding the lower and upper squared slacks and observing that the second factor is positive after Step 3.
  2. Put \(x=f(y)\). The outer two expressions both equal \(f(y)\), so the middle one must equal them, yielding \(f(f(y))=2f(y)-y\), equivalently \(g(f(y))=g(y)\) — by simultaneous equality in the two-sided sandwich.
  3. Iterate Step 2 to obtain \(f^n(y)=y+n g(y)\) for every \(n\ge0\), and conclude \(g(y)\ge0\) because every iterate remains positive — by induction and positivity; also note that the same identity makes \(f\) injective.
  4. Prove that any two positive values of \(g\) are equal. If \(g(u)=a>0\) and \(g(v)=b>0\), use the orbit points \(X_n=u+na\), \(Y_m=v+mb\). For each large \(n\), choose \(m\ge0\) so \(|X_n-f(Y_m)|=|u+na-(v+(m+1)b)|<b\). Applying (D) to \((X_n,Y_m)\) gives a bounded right side, while its left side is \(|a-b|(2X_n+2Y_m+a+b)\), which diverges unless \(a=b\) — by the Archimedean nearest-multiple/floor principle.
  5. Hence the range of \(g\) is either \(\{0\}\), \(\{c\}\), or \(\{0,c\}\) for one \(c>0\). Exclude the mixed case: for \(Z=\{t:g(t)=0\}\), (D) shows sequential closedness by applying it to \((x,y)=(z,z_n)\) with \(z_n\in Z\to z\), and shows openness because near \(p\in Z\), the alternative value \(c\) would force \(c(2x+2p+c)\le(x-p)^2\). Since \((0,\infty)\) is connected, a nonempty clopen \(Z\) is the whole domain — by connectedness of an interval.
  6. Conclude \(g\equiv c\) for some \(c\ge0\), hence \(f(t)=t+c\).
  7. Verify every \(c\ge0\): after squaring, both slacks are exactly
     \[
     (f(x)+y)^2-4xf(y)=2x^2+2f(y)^2-(f(x)+y)^2=(x-y-c)^2\ge0,
     \]
     and positivity of \(f\) and of all displayed quantities makes the squared verification equivalent to the original inequalities — by SOS/completing the square and the knowledge-base “Check the answer” rule.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Exact displacement bound (D) — because the two squared slacks are \((x-y-g(y))^2\pm(g(x)-g(y))(2(x+y+g(y))+g(x)-g(y))\).
  - Orbit lemma \(f^n(y)=y+n g(y)\) with \(g(y)\ge0\) — because \(x=f(y)\) pinches both endpoint bounds to the same number and a negative arithmetic orbit eventually leaves \(\mathbb R_{>0}\).
  - Positive-increment uniqueness — because two positive arithmetic orbits can be chosen within a bounded distance using a nearest multiple, while (D) demands linearly growing separation whenever their increments differ.
  - No mixing of zero and positive increments — because the zero-increment locus is both open and closed once the positive range is the singleton \(\{c\}\).
Open gaps: Builder must write the expansion leading to (D) without a sign error; formalize the choice of \(m\) and show both orbit coordinates diverge; give explicit epsilon/sequential arguments for openness and closedness of \(Z\). The core route otherwise appears complete.
Cases to cover: \(g\equiv0\); \(g>0\) everywhere; hypothetical mixed range \(\{0,c\}\); all parameters \(c\ge0\) in sufficiency.
Watch out for: Do not infer the answer is only the identity; every nonnegative translation works. Do not assume continuity of \(f\) or \(g\): closedness/openness must be deduced directly from (D). The diagonal \(x=y\) is tautological and should not be presented as progress.

lattice-envelope-amplification: new
Target: Characterize all functions satisfying the two-sided inequality as exactly \(f(t)=t+c\) for constants \(c\ge 0\), proving necessity and verifying both inequalities.
Technique: One arithmetic orbit generates a global asymptotic affine envelope, then exact orbit invariance amplifies asymptotic agreement to exact agreement; this adapts the “lattice shift gives \(Kx+O(1)\), then send a variable to infinity” crux of `aimo-0234`.
Skeleton:
  1. As in the direct SOS reformulation, set \(g=f-\mathrm{id}\), derive the exact bound (D), and specialize \(x=f(y)\) to obtain \(f^n(y)=y+n g(y)\) and \(g(y)\ge0\).
  2. If no point has positive displacement, conclude \(f=\mathrm{id}\). Otherwise fix \(v\) with \(g(v)=c>0\); its orbit is the exact lattice \(v+nc\), all carrying displacement \(c\).
  3. Prove a global tail estimate. For every sufficiently large \(t\), choose \(n\) so \(t\) lies within distance at most \(c/2\) (or \(c\)) of the equality center \(f(v+nc)=v+(n+1)c\). Apply (D) with \(x=t,y=v+nc\) to obtain
     \[
     |g(t)-c|\,[2t+2(v+nc)+g(t)+c]\le c^2,
     \]
     hence \(|g(t)-c|=O(1/t)\) uniformly as \(t\to\infty\) — by nearest lattice point and positivity of the denominator.
  4. For an arbitrary \(u\) with \(g(u)=a>0\), its exact orbit \(u+na\to\infty\) and has displacement identically \(a\). Evaluating the tail estimate along this orbit gives \(a=c\). Thus every positive displacement equals \(c\) — by amplification of an asymptotic estimate along an exact invariant orbit.
  5. Exclude coexistence of displacement \(0\) and \(c\) using the clopen zero-set argument directly from (D): the zero locus is closed under limits and open because a nearby point with displacement \(c\) violates the quadratic-vs-positive-constant bound. Connectedness forces either no zero points or all points zero.
  6. Therefore \(g\) is constant, so \(f(t)=t+c\) with \(c\ge0\).
  7. Verify the whole family by the identical SOS slacks \((x-y-c)^2\) for the lower and upper squared inequalities, and then unsquare using positivity.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Tail envelope \(g(t)=c+O(1/t)\) from one positive orbit — because equality centers form a fixed-step lattice covering the tail within bounded error, while (D)'s coefficient grows linearly.
  - Exactification of the envelope — because every positive displacement produces an unbounded arithmetic orbit on which that displacement is exactly invariant.
  - Zero-locus dichotomy — because after exactification the range is \(\{0,c\}\), and (D) makes the zero fiber clopen.
Open gaps: Builder must quantify the uniform tail coverage and denominator lower bound, and must carefully handle the initial case where no positive displacement exists. The clopen details remain to be written rigorously.
Cases to cover: no positive displacement; at least one positive displacement; possible zero points in the latter case; sufficiency for \(c=0\) and \(c>0\).
Watch out for: This route may use limits only on explicit numerical bounds, never an assumed continuity of \(f\). State that `aimo-0234` is inspiration, not a citation, and prove the envelope here from (D).

swapped-order-rigidity: new
Target: Characterize all functions satisfying the two-sided inequality as exactly \(f(t)=t+c\) for constants \(c\ge 0\), proving necessity and verifying both inequalities.
Technique: Swap-and-combine the two quadratic inequalities to seek an order/regularity theorem, then use invariant translation intervals to force a constant displacement; this is the genuine non-lattice-collision rival, conditionally analogous to the injectivity–monotonicity–boundary route of `aimo-0909`.
Skeleton:
  1. Square safely and define \(g=f-\mathrm{id}\). Apply the exact displacement identity to both \((x,y)\) and \((y,x)\) to obtain the symmetric squeeze
     \[
     |g(x)-g(y)|[2x+2y+g(x)+g(y)]
     \le \min\{(x-y-g(y))^2,(x-y+g(x))^2\}. \tag{S}
     \]
  2. Use \(x=f(y)\) to get the exact orbit identity, nonnegative displacement, and injectivity, but do not compare two arithmetic lattices.
  3. Prove the central order lemma: (S), injectivity, and the freedom to vary a positive auxiliary argument imply that \(f\) (or equivalently the appropriate displacement ordering) is nondecreasing. The intended mechanism is the `aimo-0909` forbidden-slope idea: if two points reverse order, use the continuous auxiliary variable in the two squared inequalities to realize a forbidden crossing/equality, contradicting injectivity or (S).
  4. From monotonicity and \(f(x)=x+g(x)\ge x\), use \(g(f(x))=g(x)\) to show \(g\) is constant on every interval \([x,f(x)]\): monotonicity bounds \(f(x)\le f(t)\le f(f(x))\), and the endpoint difference is exactly the common displacement.
  5. Prove the interval-propagation lemma: the family of intervals \([x,x+g(x)]\), together with (S) at their endpoints and connectedness of \((0,\infty)\), cannot support two different plateau heights; adjacent/overlapping plateaus have equal displacement, while a positive gap between plateau components contradicts the quadratic squeeze at its boundary.
  6. Conclude \(g\equiv c\ge0\), and verify \(f(t)=t+c\) by the two identical SOS slacks \((x-y-c)^2\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Symmetric squeeze (S) — because swapping \((x,y)\) changes the equality-center distance from \(x-y-g(y)\) to \(x-y+g(x)\) but leaves the positive coefficient unchanged.
  - Order lemma — intended because an order reversal creates a positive forbidden secant slope that an auxiliary parameter can match, as in the mechanism of `aimo-0909`; the exact algebra must be developed for this inequality.
  - Plateau propagation — because monotonicity plus equal values at \(x\) and \(f(x)\) forces equality throughout the intervening interval, and (S) should prevent a jump at a boundary.
Open gaps: Step 3 is a major unproved lemma; the `aimo-0909` forbidden-slope argument does not transfer automatically because the present hypothesis is an inequality rather than an equality with a freely scalable argument. Step 5 also needs a complete boundary/no-jump proof. If Step 3 cannot be established directly from (S), this approach should be marked RETHINK rather than silently reverting to arithmetic-orbit collision.
Cases to cover: fixed points \(g=0\); positive translation intervals; possible jump/boundary between two plateaus; final \(c=0\) and \(c>0\) verification.
Watch out for: Do not assume monotonicity or continuity. Injectivity alone does not imply monotonicity. Do not borrow the conclusion of `aimo-0909`; only its forbidden-slope mechanism is potentially transferable.

quadratic-zero-locus-propagation: new
Target: Characterize all functions satisfying the two-sided inequality as exactly \(f(t)=t+c\) for constants \(c\ge 0\), proving necessity and verifying both inequalities.
Technique: Local quadratic stability at every equality center, propagation of displacement labels, and connectedness; the spine is SOS/equality-locus geometry rather than an asymptotic comparison of two full orbits.
Skeleton:
  1. Derive (D), the forced iterate identity, and \(g\ge0\) exactly as above.
  2. Establish the local quadratic stability estimate at every image point:
     \[
     |g(f(y)+h)-g(y)|\le \frac{h^2}{2(f(y)+h)+2y+g(f(y)+h)+g(y)}
     \]
     whenever \(f(y)+h>0\) — by putting \(x=f(y)+h\) in (D).
  3. Develop a propagation lemma saying that two distinct displacement labels cannot accumulate near the same equality-center chain. The intended mechanism is to iterate the estimate at \(y,f(y),f^2(y),\ldots\), where the denominators grow while a bounded transverse offset \(h\) is retained, forcing the label variation to zero faster than quadratically.
  4. Prove from the propagation lemma that the nonzero range of \(g\) is discrete and in fact a singleton, without invoking a direct nearest-point collision between two arithmetic orbits. Then show every fiber of a displacement label is open and closed using the local estimate and its swapped form.
  5. Connectedness forces a single displacement label on all of \((0,\infty)\), hence \(g\equiv c\ge0\).
  6. Verify the translation family via the identical squared SOS slacks \((x-y-c)^2\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Quadratic stability at equality centers — because the right side of (D) is exactly the square of the distance to \(x=f(y)\), while the coefficient on the left is positive and grows along the orbit.
  - Label propagation/discreteness — intended because repeated equality centers amplify the denominator while preserving the orbit's label, so a competing label at bounded transverse distance is forced to coincide.
  - Connected-fiber collapse — because separated labels with locally stable fibers would partition the positive interval into disjoint nonempty clopen pieces.
Open gaps: The central Step 4 is unproved: local stability along one orbit does not by itself guarantee that an arbitrary second orbit remains at bounded transverse distance. The builder must either find a genuine local/connectedness argument or reject this approach; importing the nearest-lattice collision would collapse it into `orbit-collision-clopen` and should not be disguised as a rival.
Cases to cover: zero label; one positive label; two hypothetical positive labels; accumulation versus isolated labels; sufficiency.
Watch out for: Local control is centered at \(f(y)\), not at arbitrary \(y\). This centering issue is the main danger and must not be hand-waved.