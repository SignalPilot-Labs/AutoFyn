## Surrogate/Majorization Worst-Tail Dead End (round 19, negative result)

**Context.** Case (b2) of the general-marking upper bound $c(n)\le a_nT$
(the region $p_1<T/2$, $T/D_n<p_2<a_nT/2$, i.e. the complement of the
already-closed cases (a) [`unconditional-p2-threshold-closure`/
`sharp-dominant-removal-identity` threshold $p_2\ge a_nT/2$] and (b1)
[Max Domination Lemma threshold $p_2\le T/D_n$]) is the sole remaining open
region of the general upper bound. A natural idea, floated as a possible
transplant of the `aimo-0560` (IMO 2022 P6) "surrogate adversary" crux move,
is: fix $p_1,p_2$ inside case (b2)'s box, replace Xiang Yu's actual optimal
response to an *arbitrary* legal tail $(p_3,\dots,p_m)$ by his optimal
response to a single, explicit, closed-form "worst-case" tail shape
$g(p_1,p_2)$ (a majorizing/dominating surrogate), and then prove the
one-parameter bound $\Phi_{\min}(p_1,p_2,g(p_1,p_2))\le a_nT$ directly. If a
sound choice of $g$ existed with $\Phi_{\min}(p_1,p_2,\text{tail})\le
\Phi_{\min}(p_1,p_2,g(p_1,p_2))$ for *every* legal tail, this would collapse
case (b2)'s continuum of tail shapes to a single explicit family.

**This lemma records that the mechanism is unsound, not merely numerically
weak, for the natural candidate surrogate (the ratio-2 ladder tail), and
that no evident low-dimensional replacement exists.**

### The required soundness condition

For the surrogate mechanism to yield a valid upper bound, the candidate
tail shape $g(p_1,p_2)$ must satisfy, for the *fixed* $p_1,p_2$ under
consideration and *every* legal tail refinement $(p_3,\dots,p_m)$ with
$p_3+\cdots+p_m=T-p_1-p_2$, $p_3\le p_2$:
$$\Phi_{\min}(p_1,p_2,p_3,\dots,p_m)\ \le\ \Phi_{\min}(p_1,p_2,g(p_1,p_2)).
\tag{$\dagger$}$$
That is, $g$ must be a genuine **majorant of the argmax**: the tail shape
that makes Xiang Yu's own best response to the whole marking as large as
possible, among all legal tail shapes, for the fixed $(p_1,p_2)$. Only then
does bounding the single quantity $\Phi_{\min}(p_1,p_2,g(p_1,p_2))$ by
$a_nT$ suffice to bound $\Phi_{\min}$ for *every* tail at that $(p_1,p_2)$.

### The natural candidate fails: the ladder is not the argmax

The most natural candidate is $g_{\mathrm{ladder}}(p_1,p_2)$: the
geometric-ratio-2 tail, $p_{2+j}=p_2/2^j$ for $j=1,\dots,n-1$ (rescaled to
the correct remaining mass $T-p_1-p_2$), matching the ladder construction
that is optimal for Liu Bang's own *marking* choice. This is the surrogate
implicitly used by every prior template-based attempt in this project
(Theorems A-D, Bisect-Top-$k$, Cross-Piece-Sign-Assignment all evaluate
$\Phi$ against an arbitrary tail directly, but no prior attempt tried to
replace the tail itself by a single worst-case shape before this round's
exploration).

**Exact-computation-adjacent evidence that $(\dagger)$ fails for
$g=g_{\mathrm{ladder}}$ (ratio exactly 2).** Round 19's independent
re-derivation (via `differential_evolution` over every legal cut-budget
composition of Xiang Yu's response, evaluated numerically — this is a
numeric optimizer, not exact-`Fraction` arithmetic, but robust across
optimizer seeds and tolerances $10^{-10}$–$10^{-12}$, and independently
reproduces round 18's finding by a freshly-written script) establishes, for
several fixed points $(p_1,p_2)$ inside case (b2)'s box at $n=3$, that the
tail ratio $r=p_3/p_4$ maximizing $\Phi_{\min}(p_1,p_2,\text{tail}(r))$ over
$r\in[1.5,3.0]$ is **not** $r=2$:

| $(p_1,p_2)$ | argmax ratio $r^\ast$ | $\Phi_{\min}$ at $r^\ast$ | $\Phi_{\min}$ at $r=2$ |
|---|---|---|---|
| $(0.40,0.25)$ | $\approx1.8$ | $\approx0.5125$ | $\approx0.5083$ |
| $(0.35,0.20)$ | $\approx1.6$ | (strictly $>$ value at $r=2$) | -- |
| $(0.45,0.28)$ | $\approx1.4$ | (strictly $>$ value at $r=2$) | -- |
| $(0.30,0.15)$ | $\approx2.0$ | (coincidentally close to $r=2$) | -- |

At the first point, $r^\ast\approx1.8$ gives a strictly larger
$\Phi_{\min}$ than $r=2$ ($0.5125>0.5083$): the ladder tail is **not** the
argmax, so $(\dagger)$ fails with $g=g_{\mathrm{ladder}}$ — there exists a
legal tail (namely the one with ratio $\approx1.8$) whose true best-response
value strictly exceeds the value the ladder-tail surrogate would report.
A proof that bounded only $\Phi_{\min}(p_1,p_2,g_{\mathrm{ladder}})$ and
then asserted this bounds every tail would be **actively wrong**, not
merely a weaker/looser argument, because it would understate the true
supremum over tails at these points.

**Non-template optimal response.** At the argmax point
$(p_1,p_2,r^\ast)=(0.40,0.25,1.8)$, the optimal Xiang-Yu response has cut
composition $(2,0,1,0)$ — 2 cuts on $p_1$ (3 fragments), 1 cut on $p_3$ (2
fragments), $p_2,p_4$ untouched — which is not an instance of any certified
closed-form family on file (Theorems A–D, Bisect-Top-$k$, Cross-Piece-Sign-
Assignment each evaluate to $\ge0.55$ at this point, far from the true
$\approx0.5125$ minimum). This shows the difficulty is not confined to
identifying the right tail shape $g$; even the *response* to a fixed tail
at the argmax has no evident closed form in the existing toolkit.

**No evident low-dimensional replacement.** The argmax ratio itself is not
a universal constant: it was checked at four independent points inside
case (b2)'s box and takes four different values ($\approx1.4,1.6,1.8,2.0$),
i.e. it drifts substantially (by $\ge40\%$ relative) as $(p_1,p_2)$ move
within the box, with no closed-form pattern identified. A sound majorizing
surrogate would need $g$ to be an explicit function $(p_1,p_2)\mapsto
r^\ast(p_1,p_2)$ (or, more generally, a full tail *shape*, since nothing
guarantees the argmax stays within the one-parameter geometric-ratio
family at all) matching this drift exactly and provably — i.e. it would
require solving the *same* joint vertex/tie-enumeration characterization
problem that has been the shared obstruction across this project's
lower-bound and upper-bound fronts for 15+ rounds, not a shortcut around
it.

### Conclusion (dead end, precisely scoped)

The surrogate/majorization-by-a-single-explicit-tail-shape mechanism for
case (b2) is **unsound as literally proposed** when instantiated with the
one candidate that has any structural motivation (the ratio-2 ladder): it
does not merely give a loose or unproved bound, it gives a **false**
sufficient condition, since the ladder tail is not always the argmax over
legal tails at fixed $(p_1,p_2)$. No alternative low-dimensional (finite-
parameter, closed-form) candidate for the true argmax tail shape was found;
the true argmax appears to require exactly the same unresolved joint-vertex
characterization that already blocks every other route into case (b2). This
does not rule out *some* future majorization argument with a correctly
characterized (rather than guessed) worst-case family, but it does rule out
"assume the ladder tail is hardest" as a component of any future case-(b2)
proof — that specific premise is false, not merely unproved.

**Certified by:** `lp-duality-certificate` approach, round 19, per the
outline's explicit instruction to certify the round-19 explorer's finding
(`/tmp/round-19/math-explorer-surrogate.md`) as a formal dead-end lemma.

**Fifth confirmed-dead mechanism family for case (b2)**, alongside
peel/bisect/recurse-plus-full-IH (`peel-zero-slack-dead-end`,
`bisect-containment-dead-end`, `recursive-image-escape-dead-end`),
weighted/convex combination of primal strategy values
(`convex-combination-futility-theorem`), naive boundary continuity (round
18 finding, folded into the concavity refutation below), and
Danskin/concavity-in-Liu-Bang's-own-tail-marking (round 18 build: a robust
interior local minimum of $\Phi_{\min}(p_1,p_2,t)$ at $t=p_1-p_2$ refutes
the required concavity-in-$t$ premise).
