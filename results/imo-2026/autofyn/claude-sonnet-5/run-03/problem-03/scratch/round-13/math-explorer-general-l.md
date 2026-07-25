# Math-explorer report — lens: general-ℓ / general-m window closure (round 13)

Scope: how to extend GT($m$) (`lemmas/general-peeling-theorem-and-window-endpoint-closure.md`,
proved by round 12 for $m=0,1,2,3$) to all $m\ge4$, which is what closes gap (a) of
the shared Branch-I.A window for all $\ell\ge5$ (Branch-I.A window at level $\ell$
is $\mathrm{GT}(m)$ at $m=\ell-1$).

## 1. Exactly how the $m\le3$ proof works

$\mathrm{GT}(m)$: for $|D|\le m+1$, $\max(D)\le2^m$, $\mathrm{sum}(D)<3\cdot2^{m-1}$
(reviewer's certified scope restriction — see below),
$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\min(\mathrm{sum}(D),2^m)$.

Proof mechanism (all in `approaches/self-similar-induction-on-n.md`, "The General
Theorem GT($m$)" section, ~lines 2962–3203):

- Split on $p:=\#\{a_i>2^{m-1}\}\in\{0,1,2\}$ ($p\ge3$ excluded by the sum bound).
  - $p=2$: closes **unconditionally**, no recursive call (Lemma P2).
  - $p=1$: closes via $\mathrm{GT}(m-1)$ applied to the remainder $R$ (Lemma P1).
  - $p=0$: reduces to $\mathrm{EvenSum}(D\cup\Gamma_{m-2})\ge2^{m-1}$, then a
    **second** split on $r:=\#\{a_i>2^{m-2}\}\in\{0,1,2\}$:
    - $r=2$: closes via $\mathrm{GT}(m-2)$ (Lemma R2).
    - $r=1$: closes via $\mathrm{GT}(m-1)$ (Lemma R1).
    - $r=0$ ("all-tiny residual", $\max(D)\le2^{m-2}$, still up to $m+1$ pieces):
      handled **only by proving it's infeasible** — the Feasibility Lemma shows
      $(m+1)\cdot2^{m-2}\ge2^m+\varepsilon$ fails for $m\le3$ (not enough total
      mass in $m+1$ pieces each $\le2^{m-2}$ to reach the target), so the case
      is vacuous for $m\le3$. Exact boundary at $m=3$: $4\cdot2=8<8+\varepsilon$.

So for $m\le3$, every branch either terminates unconditionally, recurses into an
already-proved smaller $\mathrm{GT}$, or is empty. That's the whole induction.

## 2. What breaks at $m\ge4$ — a genuine, unbounded-depth obstruction, not case explosion

The Feasibility Lemma itself proves $r=0$ becomes **feasible** for every $m\ge4$
(RHS of the feasibility inequality $4+\varepsilon2^{2-m}<5\le m+1$). So starting at
$m=4$, the "$r=0$ is vacuous" trick that closed $m\le3$ stops working — there
really do exist admissible, all-tiny, $(m+1)$-piece $D$ in this residual, and the
proof has no lemma covering them.

The root cause is structural, not just "more cases to write down": each level of
the $p$/$r$-style split *drops the value cap by one factor of 2* (comparing against
$2^{m-1}$, then $2^{m-2}$, …) but the **piece-count cap stays fixed at $m+1$**
(inherited unchanged from $\mathrm{GT}(m)$'s own hypothesis, not reduced to
$(m-i)+1$ as a genuine two-levels-down $\mathrm{GT}(m-2)$ call would use). That is
a **constant 2-piece slack** relative to what a legitimate $\mathrm{GT}(m-2i)$ call
could absorb, injected fresh at every level. A residual with $j$ levels of splitting
has value cap $2^{m-j}$ but still $m+1$ pieces; it becomes infeasible only once
$(m+1)\cdot2^{m-j}<2^m+\varepsilon$, i.e. once $j\gtrsim\log_2(m+1)$. So the
**recursion depth needed to reach a vacuous base case grows like $\log_2 m$**, not
$O(1)$. The $m\le3$ proof got away with depth $\le2$ (one $p$-split, one $r$-split)
purely because $\log_2(m+1)\le2$ in that range; it was never going to generalize by
literally the same two-level scheme. The approach file's own "Honest scope" section
(lines 3143–3167) already reaches this diagnosis in different words ("the new $s=0$
residual inherits the same count-cap-exceeds-supply-by-2 mismatch, recursively") but
does not push it to a closed form. This confirms it is a genuine structural feature
of the case-split method, not an artifact of insufficient bookkeeping — so patching
finitely many more explicit levels ($m=4,5,6,\dots$ by hand) never terminates; only
a *uniform* argument (closed-form in $j$ and $m$) or a *different* method closes all
$m$ at once.

## 3. Numeric check: is GT($m$) even true for $m\ge4$, and where's the tight case?

Wrote exact-`Fraction`-based checkers (`/tmp/gt_check.py`, `/tmp/gt_check2.py`,
kept from this session) reimplementing $\mathrm{OddSum}$/$\mathrm{EvenSum}$ directly
as sums over odd/even sorted ranks (verified consistent with the file's Global-max/
Companion Peeling identities). Random search over $D$ with $k\le m+1$, various sums
up to $\approx2^m$, $m=0,\dots,8$: **zero violations**, margin (LHS $-$ target) only
ever $\ge0$ (matches round 12's own stress test, extended a couple more $m$).

More targeted: hill-climbed for the *worst* (smallest) margin at fixed
$\mathrm{sum}(D)=2^m+\varepsilon$, $k=m+1$:

```
m=0: min margin ≈ 0        m=5: min margin ≈ 0.0008
m=1: min margin ≈ 0.0007   m=6: min margin ≈ 0.0009
m=2: min margin ≈ 0.0009   m=7: min margin ≈ 0.12   (search likely not converged)
m=3: min margin ≈ 0.0009   m=8: min margin ≈ 0.34   (search likely not converged)
m=4: min margin ≈ 0.0008   m=9: min margin ≈ 3.0    (search likely not converged)
```

Up through $m=6$ the theorem stays essentially **tight** (margin $\to0$), exactly as
it is at $m\le3$ — i.e. numerically there is no jump in tightness at the $m=4$
threshold where $r=0$ turns feasible; the extremal $D$'s found by hill-climbing
don't look like "many-tiny-equal-pieces" (the shape that makes $r=0$ feasible) but
rather small-support configurations resembling Theorem W's tied-pair witness shape
(`lemmas/theorem-w-window-endpoint-witness.md`: $C=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}
\setminus\{1\})\cup\{r,r\}$). By contrast, the literal "$m+1$ equal parts" instance
that *witnesses feasibility* of $r=0$ has margin growing large and positive
(computed directly: $m=4\Rightarrow2.6$, $m=6\Rightarrow9.6$, $m=9\Rightarrow85$) —
so the configurations that make the case-split's bookkeeping fail are **not** the
configurations that threaten the inequality; they're comfortably safe. This is
strong evidence $\mathrm{GT}(m)$ is true for all $m$ with the true extremizer always
tied-pair-shaped, and that the case-split's difficulty is a proof-method artifact,
not a fact about the extremal instances.

(Caveat: the $m=7,8,9$ hill-climb numbers going up rather than staying near 0 is
probably non-convergence of the local search in higher dimension, not a real
trend — should be rerun with more restarts/annealing before trusting the $m\ge7$
numbers.)

## 4. Distinct viable routes to closing general $m$

**Route A — push the case-split to a closed-form uniform induction (direct
continuation of round 12's method).** Instead of re-deriving a fresh Feasibility
Lemma at each depth, prove one lemma parametrized by depth $j$: "within
$\mathrm{GT}(m)$, the depth-$j$ residual (all elements $\le2^{m-j}$, still $\le m+1$
pieces) is infeasible once $j>\log_2(m+1)$ (roughly), and for $j\le\log_2(m+1)$ the
same Global-max/Companion-peeling identity chain reduces it to $\mathrm{GT}(m-j)$ or
$\mathrm{GT}(m-j-1)$ composed $j$ times." This requires (a) a clean induction on $j$
(not $m$) proving the peeling identity generalizes ($\mathrm{OddSum}$ /
$\mathrm{EvenSum}$ alternation under repeated Global-max+Companion peeling against
$2^{m-1},2^{m-2},\dots,2^{m-j}$ is already suggested by the file's own $p$/$r$
computations — should generalize mechanically), and (b) closing the final
$j=\lceil\log_2(m+1)\rceil$ base case's algebra uniformly in $m$ rather than by
hand per $m$. This is the most direct continuation but is exactly the thing round
12 flagged as "not completed" — likely tractable but fiddly (a genuine induction on
two parameters $m,j$ with a variable stopping depth).

**Route B — exchange-smoothing to pin the extremizer shape, then check GT($m$)
only at that shape (the approach file's own "Route (b), not attempted this round",
line 3169–3177).** Numeric evidence in §3 supports this: the worst case looks
tied-pair-shaped (à la Theorem W), not many-tiny-pieces-shaped, for all $m$ tested.
If one can show (by an exchange/smoothing argument: given optimal $D$ minimizing
$\mathrm{OddSum}(D\cup\Gamma_{m-1})-\mathrm{sum}(D)$ subject to the cap/count
constraints, any two "generic" coordinates can be exchanged to weakly decrease the
objective, standard majorization move) that the minimizer is always of a specific
low-parameter family (e.g. one or two "free" values plus dyadic filler, matching
the $\Gamma$-block shape), then $\mathrm{GT}(m)$ reduces to checking that single
family by direct algebra/induction on $m$ — sidestepping the case-split's growing
depth entirely, because the family has $O(1)$ free parameters regardless of $m$.
This is the route most likely to give a **uniform, $m$-independent proof**. Crux
corpus support (§5) is specifically for this exchange-smoothing move.

**Route C — import machinery from a sibling approach (LP/vertex framing).**
`lp-duality-split-polytope.md` and `global-lp-vertex-sufficiency.md` both frame the
adversary's optimal response as a vertex of a polytope (cell-wise-affine objective ⇒
optimum at a vertex; LP duality pins the vertex's combinatorial shape). If GT($m$)'s
statement can be recast as an LP/optimization over $D$ (fixed $k\le m+1$, cap
$2^m$, sum fixed) of the piecewise-linear function
$\mathrm{OddSum}(D\cup\Gamma_{m-1})$, a vertex-sufficiency argument would show the
minimizer is at a vertex of the feasible polytope — vertices of "$k$ bounded
coordinates with a fixed sum" are exactly extreme points where all but one
coordinate sits at $0$ or the cap $2^m$, or coordinates coincide — a finite,
$m$-independent description. This would formally justify Route B's numeric
observation instead of just corroborating it. Not attempted by any approach yet;
worth a scouting pass by whoever owns `global-lp-vertex-sufficiency` to see if its
existing cell-wise-affine reduction machinery applies directly to $\mathrm{OddSum}$
as the objective (it's piecewise linear in $D$ once the sort order is fixed on each
cell — very plausible fit).

**Route D — strengthen the induction hypothesis to carry the "slack" explicitly.**
Prove a generalized $\mathrm{GT}(m,j)$: for $D$ with $|D|\le m+1$ (not $(m-j)+1$),
$\max(D)\le2^{m-j}$ (extra $j$-fold cap-shrink but no matching count-shrink),
$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\min(\mathrm{sum}(D),2^m)$ still. This is
literally Route A phrased as a single clean two-parameter statement rather than an
ad hoc per-$m$ feasibility check — proving it by induction on $j$ for fixed $m$ (or
double induction) might be cleaner to write than Route A's per-depth bookkeeping,
since it makes the "extra 2 pieces of slack" the explicit thing being inducted on
rather than rediscovered every level.

## 5. Ruled out / already tried

- Direct extension of the $m\le3$ two-level case split to $m=4,5,\dots$ by hand,
  case by case: works in principle (mechanism identified) but doesn't terminate —
  depth needed grows like $\log_2 m$ (see §2). Round 12 explicitly stopped here.
- Naive numeric-only closure: round 12's own stress test plus this round's extended
  check (up to $m=8$–$9$) find zero violations, but this is evidence, not proof, and
  the orchestrator's rigor rules require a full proof, not numerics.

## 6. Crux corpus hints (adapt, don't cite)

Queried `past_crux_moves_database.json` filtered to `domain=combinatorics`,
`subtopic` in `extremal-principle`/`induction-and-construction`/`invariants-and-monovariants`,
for "exchange-smoothing extends small-case induction to general case" patterns
(referenced already by the approach file as `aimo-0146`/`aimo-0119`; verified these
directly and found one more good match):

- **`aimo-0146`** (extremal-principle): *"Bound a fixed weighted sum of a sorted
  nonnegative sequence under a sum constraint by exchange-smoothing weight toward
  the higher-coefficient positions until the free coordinates equalize and the tail
  drains, then enumerate the few surviving profiles."* Directly the Route B
  template: exchange smoothing collapses an $m$-dependent search space to a handful
  of profiles checkable by hand, independent of $m$. Same paper also has a crux on
  replacing an extremal object by one with a "universal vertex" via a monotone
  local-surgery move that provably doesn't decrease the objective — the structural
  analogue of "WLOG the extremal $D$ is tied-pair shaped."
- **`aimo-0119`** (extremal-principle/pigeonhole): *"Pick the configuration
  minimizing the maximum part load … so that any single-item transfer … is
  non-improving"* — the minimality-based exchange argument, same flavor, simpler
  (good template for a first pass at Route B before attempting the fuller
  `aimo-0146`-style smoothing).
- **`aimo-0156`** (induction-and-construction, new find this round): *"Achieve an
  extremal configuration by splitting the ground set into two sublattices each
  isomorphic to the smaller instance, solving each recursively, and linking them
  with a single connecting move."* This is the crux most structurally analogous to
  what Route A/D actually need: a **single clean recursive step** (not a
  case-split whose depth grows with the parameter) reducing size-$2^{n+1}$ to two
  copies of size-$2^n$ joined by one hop. If GT($m$)'s $p=0,r=0,\dots$ residual can
  be reframed as "$D\cup\Gamma_{m-1}$ decomposes into two self-similar copies of a
  smaller $\Gamma$-block problem plus one connector," this pattern gives a
  constant-depth (not $\log m$-depth) recursive step — worth checking whether the
  Companion/Global-max peeling identities admit such a "split into two smaller
  copies" reformulation instead of the current "peel one threshold at a time."
- **`aimo-0084`** (induction-and-construction): *"Strengthen the target into an
  induction that peels off one certified object at a time, leaving a smaller
  instance of the same shape for the hypothesis"* — generic template for Route D
  (strengthen the statement so the induction step is uniform), with the caveat
  (also present in that problem) that a few small/extremal periodic cases needed
  separate hand treatment — i.e. even with a strengthened hypothesis, expect a
  handful of $m$-independent boundary cases to check directly, not zero.

## 7. Recommended concrete next step

Most promising near-term move: **Route B**, since the numeric evidence (§3) already
shows the extremal $D$ is tied-pair-shaped (not many-tiny-pieces-shaped) across the
tested range, including exactly the $m\ge4$ zone where the case-split's own
bookkeeping breaks down — i.e. the numerics say the case-split is failing to prove
something that isn't even close to being violated. Concretely:

1. Formalize the exchange move: for $D$ minimizing
   $f(D):=\mathrm{OddSum}(D\cup\Gamma_{m-1})-\mathrm{sum}(D)$ (want to show $f(D)\ge
   \min(0,2^m-\mathrm{sum}(D))$) subject to $|D|\le m+1$, $\max(D)\le2^m$,
   $\mathrm{sum}(D)$ fixed, show that if two coordinates $a_i,a_j$ are both strictly
   interior (not at $0$, cap, or tied with a $\Gamma$-block value) an exchange
   $a_i\to a_i\pm t,a_j\to a_j\mp t$ is weakly improving in one direction — forcing
   the minimizer's coordinates to collapse onto $\{0,\text{cap},\text{tied with
   }\Gamma\}$, i.e. Theorem W's family (or a small finite list of such families).
2. Re-run the hill-climb (§3) with proper simulated annealing (not plain greedy) at
   $m=7,8,9,10$ to get trustworthy tight-margin numbers and confirm the extremizer
   shape numerically before investing in the exchange-argument proof — the current
   $m\ge7$ numbers are suspect (see caveat in §3) and should be redone first so the
   next round doesn't chase a proof of the wrong extremal shape.
3. In parallel, a quick scouting question for whoever owns
   `global-lp-vertex-sufficiency.md` / `lp-duality-split-polytope.md` (Route C):
   does their existing vertex-sufficiency machinery already cover
   $\mathrm{OddSum}(D\cup\Gamma_{m-1})$ as an objective over the $D$-polytope? If yes,
   that may give Route B's conclusion for free without a fresh exchange-argument
   proof.
