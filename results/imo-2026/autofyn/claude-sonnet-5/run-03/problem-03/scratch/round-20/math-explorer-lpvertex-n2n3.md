## imo-2026-03 — lens: n=2 achievability closure (6 remaining shapes) + n=3 2-cut/3-fragment witness

### Part (a): the 6 unresolved n=2 two-cut shapes — SOLVED exactly, ready to certify

The approach file (`global-lp-vertex-sufficiency.md`, Section 10.6) leaves
six two-cut response shapes at the witness partition $p^*=(4/7,2/7,1/7)$
only grid-search-verified: $(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)$
(the three "split-one-piece-into-3" shapes and the three
"split-two-different-pieces-into-2-each" shapes). I ran a **complete,
exact (`sympy`/`Fraction`) vertex enumeration** for all six, using exactly
the mechanism the file's own Global Vertex Lemma already licenses: on each
shape, $\mathrm{OddSum}$ restricted to a fixed rank-order region is affine
in the free split parameters (2 real degrees of freedom per shape, since
the piece-sum constraint eliminates one), so the minimum over the
compact feasible domain (a triangle for the 3-way splits, a box for the
2-piece splits) is attained at a **vertex of the hyperplane arrangement**
cut out by all pairwise-equality boundaries among the free fragments and
the fixed background pieces (plus the boundary $=0$ constraints). I
enumerated every such vertex by solving all $\binom{\text{constraints}}2$
systems in `sympy.Rational` and evaluated $\mathrm{OddSum}$ exactly at
each feasible one (12–15 constraint lines per shape, 7–19 feasible
vertices found per shape). This is a finite, complete, non-numeric
calculation — not a grid search — closing exactly the gap the file
flags as "well-defined but not-yet-executed."

**Exact results** (all confirm $\ge 4/7=c(2)$, matching/upgrading the file's grid-search numbers):
- $(2,0,0)$: min $=4/7$ exactly, at $(a,b,c)=(0,\,2/7,\,2/7)$ — degenerates to the multiset $\{2/7,2/7,2/7,1/7\}$ (matches the file's own "$a=b=2/7$" tie point).
- $(0,2,0)$: min $=5/7 > 4/7$, at $(a,b,c)=(0,0,2/7)$ (splitting $p_2$ further can never help — same value as the un-split $(0,1,0)$ shape's constant $5/7$).
- $(0,0,2)$: min $=9/14 > 4/7$, at $(a,b,c)=(0,1/14,1/14)$ (matches shape $(0,0,1)$'s $9/14$ exactly).
- $(1,1,0)$: min $=4/7$ exactly, at $(a,b)=(1/7,0)$ — degenerates ($b=0$ means $p_2$ untouched) to $p_1\to(1/7,3/7)$, multiset $\{3/7,2/7,1/7,1/7,0\}$.
- $(1,0,1)$: min $=4/7$ exactly, at $(a,b)=(2/7,0)$ — degenerates ($b=0$, $p_3$ untouched) to $p_1\to(2/7,2/7)$, multiset $\{2/7,2/7,2/7,1/7,0\}$.
- $(0,1,1)$: min $=9/14>4/7$, at $(a,b)=(0,1/14)$.

**Conclusion: $V(p^*)\ge c(2)$ is now fully, exactly closed for all 10 finite response shapes** (the 4 already-analytic ones plus these 6). Combined with the already-proved $V(p^*)\le c(2)$ (exact witness in shape $(2,0,0)$ or $(1,1,0)$), this gives **$V(p^*)=c(2)$ exactly, fully rigorous, no numerics** — the achievability half of the $n=2$ Existence Theorem is complete. My exact code: `/tmp/round-20/n2_shapes.py`, `n2_shapes2.py`, `n2_shapes3.py`. The outliner/builder can lift these six vertex-enumeration arguments directly into the approach file's Section 10.6 (each is a short, mechanical case-check once the vertex list is given — the *hard* part, finding and confirming the finite candidate set, is what I just did).

### Part (b): n=3 2-cut/3-fragment witness — the natural candidate is REFUTED (with exact counterexample); an algebraic identity was found but only partially closes the region

**Candidate tested**: split $p_1$ into $(p_2,\,p_3,\,r)$ with $r=p_1-p_2-p_3$, leaving $p_2,p_3,p_4$ untouched — giving the 6-element (even!) multiset $M=\{p_2,p_2,p_3,p_3,r,p_4\}$. This is exactly the "even multiset size" fix the parity diagnosis (current.md Section 10.8) motivates.

**Positive finding (a genuine, forced, exact algebraic identity, exact analogue of the $n=2$ mechanism)**: writing $g_1=p_1-p_2,g_2=p_2-p_3,g_3=p_3-p_4$ (the region's own gap variables) and using the normalization $p_1+p_2+p_3+p_4=1$, I derived in closed form (verified symbolically, `/tmp/round-20/n3_probe.py` region shows 100% consistency, then confirmed algebraically):
$$r - p_4 = \tfrac12(-1+3g_1+2g_2+g_3), \qquad p_1-\tfrac12 = \tfrac14(3g_1+2g_2+g_3-1).$$
**These two quantities have the same sign** — i.e. $r<p_4 \iff p_1<1/2$, exactly analogous to the $n=2$ identity $p_3>(p_1-p_2)\iff p_1<1/2$. So **whenever the region hypothesis $p_1<1/2$ holds (always true in $B(3)$) and $r>0$ (a genuine extra feasibility condition, not automatic), $r$ is forced to be the smallest of the six elements**, pinning $\mathrm{OddSum}(M)=p_2+p_3+p_4=1-p_1$ — confirmed by $34{,}617$ exact-`Fraction` feasible trials, zero violations of the ordering.

**But the construction is REFUTED as a universal witness — found by targeted LP, not random sampling.** Feasibility ($r>0$) requires $5g_1+2g_2-g_3>1$; minimizing $p_1=(1+3g_1+2g_2+g_3)/4$ subject to $g_1,g_2,g_3\ge\gamma(3)=1/15$ and this feasibility constraint (via `scipy.optimize.linprog`) shows $p_1$ can be pushed down to $11/25=0.44$ (LP optimum, attained in the limit $r\to0^+$, $g_2,g_3\to\gamma(3)^+$). Since $\mathrm{OddSum}=1-p_1$ needs $p_1>7/15\approx0.4667$ to beat $c(3)=8/15$, and $0.44<7/15$, **there is a genuine sliver of $B(3)$ where this witness fails**. Concrete exact counterexample, fully in the open region (`/tmp/round-20/n3_probe.py` follow-up): $p=(44081/100000,\ 75949/300000,\ 55919/300000,\ 11963/100000)$, all region inequalities strict, $r=1/800>0$, $\mathrm{OddSum}(M)=55919/100000=0.55919 > c(3)=8/15\approx0.53333$ — a clean, verified violation. **Random sampling alone (34,617 trials, 0 violations) missed this because the failing sliver is thin (near $g_2,g_3\to\gamma(3)$); this is a cautionary methodological note — always run a targeted LP/optimization search for the true worst case before trusting bulk random sampling on a "no violations found" claim, echoing the same pitfall flagged in round 17's odd-excess residual and round 16's low-restart-optimizer bug.**

**Alternate witness tested and also refuted (worse)**: split $p_1$ into $(p_3,p_4,r')$, $r'=p_1-p_3-p_4$, giving $M'=\{p_2,p_3,p_3,p_4,p_4,r'\}$ — fails broadly, **22% of sampled feasible region points violate** $c(3)$ (`/tmp/round-20/` follow-up script), strictly worse than the $(p_2,p_3,r)$ candidate. Not promising.

**Net assessment for (b)**: the parity-fix mechanism (even multiset size via a 2-cut/3-fragment split of $p_1$) is directionally right and produces a genuine forced rank-pinning identity ($r$-smallest $\iff p_1<1/2$) mirroring $n=2$'s mechanism exactly — but a **single global witness of this shape does not cover all of $B(3)$**; the true supremum over $B(3)$ needs a **case split** (e.g. this witness for $p_1>7/15$-ish, a different witness/shape for the remaining sliver near $p_1\in(0.44,0.4667)$ with $g_2,g_3$ near $\gamma(3)$) — precisely the kind of two-piece casework the $n=2$ proof managed to avoid. This is a concrete, well-scoped open sub-problem for the next round, not a dead direction: the failing region is a specific, LP-characterizable corner (small $g_2,g_3$, moderate $g_1$), and a natural next probe is a witness that ties $p_1$'s fragments to $p_3,p_4$ preferentially exactly in that corner, or a hybrid/min-of-two-witnesses argument.

### Cheap-kill notes
- The vertex-enumeration argument for part (a) is itself a structural cheap method (piecewise-affine-on-cells ⇒ extrema at arrangement vertices) — no heavy computation needed once the arrangement is set up; this generalizes and should be the template for any future "verify $V(p^*)=c(n)$ at a fixed witness point" task.
- For part (b): always LP-minimize $p_1$ (or whatever the pinned bound is) over the *feasibility region* of the candidate witness intersected with $B(n)$'s constraints, rather than relying on random sampling, before declaring a witness safe — random sampling under-weights thin failing corners near the region's boundary.

### Knowledge-base / lemma entries relevant
- `lemmas/global-vertex-lemma-and-lipschitz-continuity.md`, `lemmas/single-piece-split-vertex-lemma.md`, `lemmas/two-piece-split-vertex-lemma.md`, `lemmas/vertex-pinning-lemma.md` — license the vertex-enumeration argument used in part (a) (exactly the finite-candidate-set mechanism already certified for this problem).
- `lemmas/n2-existence-theorem-upper-bound.md` — the already-certified upper-bound half; part (a) supplies the missing lower-bound (achievability) half at the same witness point.
- `lemmas/singleton-interleaving-and-k-anchor-merge.md` — potentially relevant machinery for constructing the case-split witness needed to patch part (b)'s failing sliver.

### Crux corpus check (per dispatch)
Searched `combinatorics` × `games-and-strategy` and `coloring-and-parity` subtopics (per `crux_moves_documentation.md`'s field/subtopic list) for an odd/even-multiset-size case-split mechanism analogous to what's needed here. **No genuinely analogous crux found.** Closest candidates, neither a real match:
- `aimo-0357` (`coloring-and-parity`) — "prove a parity-count inequality by factoring the even-minus-odd difference into a product of two sub-part differences," from a stable-set-counting problem. The *flavor* (even-vs-odd counting argument) rhymes with this problem's OddSum, but the actual mechanism (pivot-point decomposition of a poset-stable-set count) has no structural correspondence to multiset-rank splitting.
- `aimo-0117` (`games-and-strategy`) — dyadic/geometric powers-of-two construction where the top value dominates the sum of the rest; loosely analogous to this problem's "geometric partition" $p^*=(4/7,2/7,1/7)$ already used elsewhere in the approach, but not to the $n=3$ parity obstruction specifically.
No crux in the corpus addresses "case-split a witness by which sub-region of the parameter simplex it covers, patched by a second witness" in a form transplantable here — this appears to be genuinely bespoke casework for this problem, not a retrievable move.

### Prior progress recap
- `current.md` / `global-lp-vertex-sufficiency.md` Round 19: $n=2$ Existence Theorem (upper bound, $V(p)\le c(2)$) fully closed and certified (`lemmas/n2-existence-theorem-upper-bound.md`). Achievability ($V(p^*)\ge c(2)$) proved for 9/10 shapes, last 6 only grid-verified — **now closed exactly by this report's Part (a)**.
- $n=3$: parity obstruction correctly diagnosed (odd- vs even-sized lifted multiset) but no working witness yet found — **this report's Part (b) shows the most natural even-fix candidate fails on a real (LP-characterized) sliver of $B(3)$**, and a worse alternate also fails broadly. Both are genuine dead ends for *this exact shape*, not for the parity-fix idea in general.

### Dead ends (do not retry as stated)
- Witness "split $p_1\to(p_2,p_3,r)$, background $p_2,p_3,p_4$" as a **single universal witness for all of $B(3)$**: refuted, exact counterexample above. (The forced rank-pinning identity it relies on, $r<p_4\iff p_1<1/2$, is itself correct and reusable — only the claim that this witness alone suffices everywhere is false.)
- Witness "split $p_1\to(p_3,p_4,r')$": refuted, 22% broad failure rate — do not pursue further as a standalone candidate.
