## Convex-Combination Futility Theorem (round 17, negative/dead-end result)

**Statement.** Let $p$ be a fixed Liu Bang marking and let
$\Phi_1(p),\dots,\Phi_k(p)$ be the values achieved by any *finite* family
of explicit, legal Xiang-Yu strategies at $p$ (e.g. any finite subset of
the certified exact identities Theorem A/B/C/D, Bisect-Top-$k$,
Cross-Piece-Sign-Assignment, Iterated Greedy-Peel, etc.). Fix any target
value $\theta(p)$ (in this problem, $\theta(p)=a_nT(p)$). Then for **any**
choice of weights $\lambda_1,\dots,\lambda_k\ge0$ with $\sum_i\lambda_i=1$
(constant, or depending on $p$ in any way whatsoever — the weights need
not even be computable or closed-form):
$$\min_i\Phi_i(p)\ \le\ \sum_i\lambda_i\Phi_i(p)\ \ \text{always, and}\ \
\Big[\min_i\Phi_i(p)\le\theta(p)\Big]\iff\Big[\exists(\lambda_i)\text{ with
}\sum_i\lambda_i\Phi_i(p)\le\theta(p)\Big].$$
Equivalently: **the set of markings certifiable by taking a weighted
combination of a fixed finite family of explicit strategy-values is
*exactly* the set certifiable by the plain pointwise minimum of that same
family** — no choice of weights, however cleverly (even adaptively)
chosen, can certify a single additional marking beyond what the pointwise
minimum already certifies.

**Proof.**

*($\Rightarrow$, trivial direction).* If $\min_i\Phi_i(p)\le\theta(p)$,
say the minimum is attained at index $i_0$, take $\lambda_{i_0}=1$ and all
other weights $0$; this is a valid weight vector (degenerate convex
combination) and $\sum_i\lambda_i\Phi_i(p)=\Phi_{i_0}(p)=\min_i\Phi_i(p)\le\theta(p)$.

*($\Leftarrow$, the substantive direction — this is the content of
"futility").* Suppose, for contradiction, $\min_i\Phi_i(p)>\theta(p)$,
i.e. $\Phi_i(p)>\theta(p)$ for **every** $i=1,\dots,k$. Let
$(\lambda_i)_{i=1}^k$ be *any* nonnegative weights with $\sum_i\lambda_i=1$.
Since $\sum_i\lambda_i=1>0$, at least one $\lambda_{i^\ast}>0$. For every
$i$, $\lambda_i\big(\Phi_i(p)-\theta(p)\big)\ge0$ (a nonnegative weight
times a positive quantity, since $\Phi_i(p)>\theta(p)$ for all $i$, or
$=0$ if $\lambda_i=0$), and for $i=i^\ast$ this term is **strictly**
positive ($\lambda_{i^\ast}>0$ and $\Phi_{i^\ast}(p)-\theta(p)>0$). Summing
over $i$,
$$\sum_i\lambda_i\big(\Phi_i(p)-\theta(p)\big)\ \ge\ \lambda_{i^\ast}\big(\Phi_{i^\ast}(p)-\theta(p)\big)\ >\ 0,$$
i.e. $\sum_i\lambda_i\Phi_i(p) > \theta(p)\sum_i\lambda_i = \theta(p)$
(using $\sum_i\lambda_i=1$). So **every** weighted combination of the
family also strictly exceeds $\theta(p)$ at $p$ — no weight vector can
bring the combination down to or below $\theta(p)$. This contradicts the
assumed existence of $(\lambda_i)$ with $\sum_i\lambda_i\Phi_i(p)\le
\theta(p)$, proving the $\Leftarrow$ direction by contrapositive.
$\blacksquare$

**Remark (why this rules out the whole "weighted-combination certificate"
strategy as literally posed).** The chain of reasoning
$$\Phi_{\min}(p)\ \le\ \min_i\Phi_i(p)\ \le\ \sum_i\lambda_i\Phi_i(p)$$
(the first inequality because each $\Phi_i(p)$ is the value of *some*
legal Xiang-Yu response, hence an upper bound on the true minimum
$\Phi_{\min}(p)$ over *all* legal responses; the second because the
minimum of finitely many numbers never exceeds any convex combination of
them) is a valid way to derive a *sufficient* condition
"$\sum_i\lambda_i\Phi_i(p)\le\theta(p)\implies\Phi_{\min}(p)\le\theta(p)$."
But by the theorem just proved, the hypothesis of this sufficient
condition holds **only** at markings where $\min_i\Phi_i(p)\le\theta(p)$
already — precisely the markings the plain pointwise minimum already
certifies directly, with no combination needed. Introducing weights
$\lambda_i$ (fixed, structurally derived, or even solved for per-marking
by any method, including equating the combination to the target) therefore
adds **zero new certifying power** over simply reporting
$\min_i\Phi_i(p)\le\theta(p)$: it cannot certify any marking where every
individual $\Phi_i(p)$ already exceeds the target. This is a direct
consequence of convexity (the minimum of a finite set is a lower envelope
for every convex combination of that set), not an artifact of a particular
choice of $\lambda(p)$ — so **no** future choice of weighting rule,
however sophisticated, can repair this within the "combine finitely many
already-exhibited primal strategy values" framework.

**Structural diagnosis (why this framework was the wrong tool for an
*upper* bound in the first place).** $\Phi_{\min}(p)$ is *already* defined
as a minimum over Xiang Yu's legal responses. Proving $\Phi_{\min}(p)\le
\theta(p)$ — an upper bound on a minimum — requires exhibiting only *one*
legal response with value $\le\theta(p)$; the sharpest upper bound
obtainable from a finite family of already-exhibited responses is
literally their pointwise minimum, by definition, and no post-hoc
averaging of their *values* can beat this (Xiang Yu is not permitted to
play a probabilistic mixture of strategies and receive the expected value
— he commits to one legal cut sequence, so "convex combination" here can
only ever be a mathematical relaxation *for bounding purposes*, and
relaxations never improve on the sharpest already-exhibited bound).
Genuine LP-duality-style weighting arguments are the natural tool for
*lower* bounds (bounding a min *from below* via a dual feasible weighting
over the adversary's move space, i.e. for Claim (B)-type statements) —
not for upper bounds on a min, which are witnessed, not averaged.

**Scope.** This theorem is fully general: it applies to *any* finite
family of explicit constructions (not just Bisect-Top-$k$ and
Cross-Piece-Sign-Assignment) and to *any* weighting rule (fixed, or a
function of the marking, however derived) — it forecloses the entire
"weighted/convex-combination certificate over a fixed finite primal
family" approach to proving the upper bound $c(n)\le a_n$ at case (b2), not
merely the specific two-construction instance considered this round.

**Certified by:** `lp-duality-certificate` approach, round 17, per the
outline-reviewer's explicit invitation to report an honest negative
finding if the mechanism collapses to the pointwise-min check.
