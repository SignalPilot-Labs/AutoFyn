# proof-reviewer per-role rules

## Round 1 (IMO 2026 P5)

ALWAYS: verify the equality-forcing preamble by checking the sandwich explicitly — at x=f(y) both outer bounds equal f(y), so the middle is squeezed. This is the load-bearing step for the whole iterate-orbit framework and it IS rigorous (verified).

ALWAYS: for "fixed point forces g≡0" arguments, check whether the cover iteration goes BOTH directions. A rightward-only cover (x_{k+1} = x_k + √(c·x_k)) leaves (0, x_0 − 2√(cx_0)) uncovered when x_0 > 4c. The maximal-component argument (boundary-push at both α and β) is the correct fix — it does not need continuity/connectedness of {g=0} a priori, only that S is open (proved from the zero-region) and that the single component containing x_0 extends to (0,∞).

ALWAYS: distinguish "the zero-region around x_k" from "the cumulative union of zero-regions". Z(x_k) = (x_k − 2√(cx_k), x_k + 2√(cx_k)) ∩ ℝ₊ is NOT (0, x_k + 2√(cx_k)) unless x_k ≤ 4c. A builder conflating these has a real gap (gm-lipschitz builder, round 1).

ALWAYS: for the close-encounter lemma, the key bound is δ₀ ≤ d/2 ≤ c_a/2 where d = gcd(c_a, c_b) ≤ c_a (since d | c_a). Verify this step explicitly — it is what makes ε = c_a/2 always attainable.

NEVER: accept "trivially true since c_a < c_b" without checking the actual minimum. (star star) with g(x)=c_a < c_b=g(y) IS always ≥ 0, but the minimum over x is 4y(c_b − c_a), not "obvious from c_a < c_b". The claim is true but glib; flag it as cosmetic if unused, as a gap if load-bearing.

NEVER: trust a builder's "solved" claim on Part B without checking the leftward coverage. The rightward cover iteration is the common failure mode — it looks like it covers everything but silently assumes x_0 ≤ 4c.
