semigroup-crossing-binary-descent — APPROVE
- This is a whole end-to-end attempt and the technique is sound. The normalized cut formulas are correct: splitting the angle $a$ into $x$ and $a-x$ gives children $(x,b,a+c-x)$ and $(a-x,c,b+x)$.
- The necessity invariant has the right exhaustive mechanism. Because the unchanged coordinates $b,c$ are nonintegral, an integral coordinate in each child must come from one of the four displayed cross-child pairings; their sums or differences force $a,b,c$, or $s$ integral, a contradiction.
- The sufficiency crossing lemma is viable but must be stated carefully in the built proof. If some coordinate $a>1$, choose either other coordinate as $b$ and use that the open interval $(b,a+b)$ has length $a>1$. If all three are below $1$, their positive integral sum is $n=2$; choose a pair with sum greater than $1$ (indeed every pair has sum $2-c>1$), so $(b,a+b)$ contains $1$. Then $x=r-b$ lies strictly in $(0,a)$, while $r>0$ and $n-r>0$ because $r<a+b<n$.
- In the descent, explicitly describe the geometric cut at the vertex carrying $k$: choose the interior ray making normalized angle $\lfloor k/2\rfloor$ with one incident side. The two surviving labels are $\lfloor k/2\rfloor$ and $\lceil k/2\rceil$, both in $[1,k-1]$ for $k>1$. This gives finite termination independently of Shan-Yu.
- The builder must cite angle chasing, invariants/monovariants, pigeonhole/extremal crossing, and strong induction from `knowledge_base.md`, and explicitly state and verify the final characterization $\theta=180^\circ/n$, $n\ge2$.

backward-attractor-integer-strata — RETHINK
- The attractor language is logically valid, including the finite-tree equivalence and the warning against assuming a uniform bound. However, this is not a genuinely distinct rival approach: both halves use exactly the same four-pair nonintegrality obstruction, the same open-interval crossing cut, and the same balanced integer-label descent as `semigroup-crossing-binary-descent`.
- A separate slug would duplicate every load-bearing gap and violate the whole-population diversity rule. Do not build or register it. If backward-attractor terminology is useful, it may be used locally to organize the approved proof, not treated as a rival route.

fractional-color-safe-branch — RETHINK
- “Safe coloring” is merely the nonintegral-coordinate invariant modulo $1$, and the productive-label argument is exactly the crossing-plus-halving proof. It therefore shares every load-bearing lemma with `semigroup-crossing-binary-descent` and offers no independent route if that skeleton fails.
- Do not build or register this collapsed variant. A genuinely new replacement would need a different obstruction or a different forcing strategy, rather than renaming normalized coordinates as colors and plays as tree branches.

geometric-sector-induction — RETHINK
- Translating normalized coordinates into conceptual $\theta$-sectors does not create a synthetic rival: Steps 1–5 are precisely the same interval crossing, complementary integer labels, balanced descent, and four-pair safe-child calculation.
- The stated geometric-crossing mechanism is also misleading as written: when the normalized total is integral and all coordinates are nonintegral, their fractional parts sum to either $1$ or $2$, not necessarily merely because “the three nonintegral sector remainders sum to an integer” without accounting for the floors. The algebraic approved outline already handles this more cleanly.
- Do not build or register it. The next field expansion should seek a genuinely different whole-game framing if one exists; all four submitted candidates currently collapse to one proof.

Population/ranking note: only `semigroup-crossing-binary-descent` survives and was registered at cold-start Elo. With fewer than two registered approaches there is no sound pairwise comparison to submit this round.

build set: semigroup-crossing-binary-descent