## Statement (negative result — record to prevent re-derivation)

The Xiang-Yu strategy "repeatedly bisect the current largest piece, using
all $n$ available points, unconditionally" does **not** cap Liu Bang's
payoff at $2^n/(2^{n+1}-1)$ against every Liu Bang marking. Counterexample:
$n=2$, Liu Bang marks $0$ points (single piece of length 1). Bisecting twice
gives $\{1/2,1/4,1/4\}$, so $\Phi=1/2+1/4=3/4 > 4/7=c(2)$.

## Certification note (proof-reviewer, round 1)

Verified directly: $\Phi(\{1/2,1/4,1/4\}) = 1/2+1/4 = 3/4$ by the certified
claiming-subgame-reduction lemma (odd-rank sum of the sorted multiset
$1/2,1/4,1/4$), and $3/4 > 4/7$ is immediate. This is a genuine, correct
counterexample to the naive "always bisect the global max" strategy as a
universal capping strategy. Recorded here (not as a reusable positive
lemma, but as a certified dead end) so future rounds do not re-attempt this
exact strategy as the mechanism for the general-$n$ upper bound.
