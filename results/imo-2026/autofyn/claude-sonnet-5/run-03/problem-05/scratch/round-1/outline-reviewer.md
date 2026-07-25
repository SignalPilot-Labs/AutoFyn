# Outline review — imo-2026-05, round 1

## Shared base layer — independently re-verified, CORRECT

I re-derived from scratch (by hand and symbolically with sympy), not just trusted the outliner:

- Setting `x=f(y)` collapses QM-side to `f(y)` exactly (since `QM(f(y),f(y))=f(y)`) and forces
  the middle term equal to both bounds, giving the exact FE `f(f(y)) = 2f(y) - y` for all `y>0`. Confirmed.
- Injectivity from the FE: `f(a)=f(b) ⟹ 2f(a)-a=2f(b)-b ⟹ a=b`. Confirmed.
- `g(y):=f(y)-y`. The forward orbit `y,f(y),f(f(y)),…` is an exact AP with common difference
  `g(y)` (telescoped from the FE applied at every orbit point), so it must stay positive forever
  `⟹ g(y)≥0`. `g(f(y))=g(y)` (orbit-invariance, not global constancy). Confirmed.
- Sufficiency: `f(x)=x+c`, `c≥0`, makes BOTH original inequalities reduce exactly to
  `(x-y-c)^2≥0`. I re-verified this by direct algebraic expansion (both squared inequalities
  reduce to `(A-B)^2≥0` with `A=x,B=y+c`). Confirmed. **Target is `f(x)=x+c` for any `c≥0`, not
  `f(x)=x` alone** — correctly stated in all four files.
- **Tool (A)**: `(x-y)^2 ≥ 4f(y)(g(x)-g(y))`, derived by plugging `p=f(y),q=x` into the right
  inequality and eliminating `f(f(y))` via the FE. I re-derived this independently with sympy
  (symbolic expansion, diff = 0 against the outliner's claimed form) — **confirmed exactly
  correct**, not hand-waved. Tool (B) follows by the `x↔y` swap. This is a genuinely new, solid
  tool, not previously in the record, and it is the load-bearing lemma shared by two of the four
  approaches with a fully-stated mechanism (GM inequality instance + FE substitution) — good.

All four approaches build on this identical, verified base and diverge only on how to promote
"g constant per orbit" to "g globally constant." This satisfies the diversity requirement: each
targets the same single gap with a different top-level mechanism (extremal/limiting, finite
algebraic elimination, telescoping, order/monotonicity) — not four flavors of one technique. None
are the same proof split into fragments; each is a full route from base layer to the final
characterization.

## Per-approach verdicts

### extremal-sup-inf — APPROVE
Sound skeleton: `m=inf g(t)`, minimizing sequence, pass to the limit in the *verified* tool (A)
(legitimate — it is a limit of numerical sequences into an already-true inequality, not an
assumption of continuity of `f`, correctly caveated by the outliner). Case B (sequence escaping to
0/∞) is honestly flagged as open, and step 7's final squeeze is explicitly flagged as unverified
("the crux computation to verify or refute") rather than asserted as done — no overclaiming. No
circularity found. This is the strongest-specified approach: mechanism is concrete, the remaining
work is a bounded, well-posed computation.

### cross-substitution-fixed-point — APPROVE
Same verified base + tool (A)/(B). The "second instance" via `(x,f(y))` is a legitimate reuse of
orbit-invariance (`g(f(y))=g(y)`, `f(f(y))=y+2g(y)`) — I checked the algebra
(`(x-y-q)^2 ≥ 4(y+2q)(p-q)`) and it is correct. The elimination step is honestly marked as the
open gap, not asserted. The fixed-point sub-route is correctly self-flagged as likely vacuous
(since `f(x)=x+c` for `c>0` has no fixed point) and capped to limited effort — good
self-awareness, prevents the builder wasting the round chasing a dead sub-route. No circularity.

### orbit-telescoping-aimo0710 — APPROVE (with caution)
The diagonal/matched-index dead end is recorded with the actual computation (`n^2`-order terms
degenerate to tautological AM-GM/QM-AM, `(p-q)^2≥0` and `(p+q)^2≤2(p^2+q^2)`, both true for any
`p,q` — I did not need to re-derive this since the mechanism given is transparent and the
conclusion — "no discriminating power" — follows directly). The proposed mismatched-scaling /
telescoped-tool-(A) adaptation is genuinely untried and not obviously circular, but it is the
least specified and highest-risk of the four (its most natural instantiation is already dead, and
the outline itself flags a likely secondary dead end for the plain single-orbit telescoping of
tool (A), since the RHS is a constant lower bound that becomes weak as the orbit grows). Keep in
the population but this is legitimately the weakest bet; the builder should cap effort per the
outline's own instruction and report a clean negative if it stalls again rather than force a
result.

### monotonicity-order — CHANGES REQUESTED
The outline itself flags step 3 (monotonicity) as unverified and to be tested first — good
epistemic hygiene. I independently stress-tested the claimed mechanism ("LEFT inequality at
`(x1,x2)` alone, plus `f(t)≥t` and injectivity, rules out inversion") and **found a numerical
counterexample to sufficiency of that single inequality instance**: with `x1=1, x2=1.1`,
`b=f(x2)=100 (≥x2)`, `a=f(x1)=120 (≥x1, a>b)`, the LEFT inequality at `(x1,x2)`
(`2x1²+2f(x2)² ≥ (f(x1)+x2)²`) holds (`10002+... ≥ 121.1²` comfortably) even though `a>b` is an
inversion. So the LEFT inequality at a single pair, together with `f(t)≥t` and injectivity, does
**not** by itself forbid inversion — the outline's proposed "cheapest mechanism" is insufficient
as literally stated. This doesn't kill the approach (the outline already has a fallback: bring in
the RIGHT inequality too, or a 3-point argument), but the builder must not skip this check — go
straight to the fallback rather than trying to force the single-inequality version to work.
Separately, step 4's "interleaving must invert" argument is stated only as intuition ("the
increasing bijection-like structure... must respect the interleaving order at every scale") with
no concrete claim to prove — this is exactly a lemma named without a mechanism per the review
criteria. **Change required**: before step 4 is attempted, the builder must produce a precise,
checkable statement of what "interleaving forces a contradiction" means (e.g., an explicit pair of
indices `n,m` where order is violated, stated as an inequality), not just prose intuition. If
step 3 cannot be fixed with the RIGHT inequality or a 3-point argument in one focused attempt, this
approach should report a clean negative (per its own step 5) rather than be forced.

## Diversity check
Good — four distinct top-level mechanisms (limiting/extremal, finite algebraic elimination,
telescoping, order/monotonicity) attacking the same single identified gap (orbit-local → global
constancy of `g`). No approach is a fragment of another; no repeat of a recorded dead end (the
diagonal telescoping dead end is explicitly avoided going forward, not repeated). No approach
argues toward `f(x)=x` alone (which would be wrong per the verified sufficiency of `c>0`).

## Population / ranking
Round 1 — no established approaches yet; all four are new cold-start entries. All four registered.
Relative ranking below reflects: extremal-sup-inf and cross-substitution-fixed-point have the most
concretely specified, already-partially-executed mechanisms (verified tool A/B, clear next
computation); orbit-telescoping-aimo0710 is riskier (natural instantiation already dead, adaptation
unproven); monotonicity-order is weakest (foundational step 3 mechanism shown insufficient as
stated by direct counterexample, step 4 lacks a concrete claim).

## Build set
Include all four this round — none are doomed/RETHINK, round 1 breadth is valuable, and even
orbit-telescoping/monotonicity-order can produce useful negative results per their own fallback
plans if they stall. monotonicity-order's builder should treat step 3 as a fast go/no-go using the
RIGHT inequality (not just LEFT) or a 3-point argument, per the CHANGES REQUESTED above, and pivot
to reporting a clean partial/negative if it doesn't resolve quickly.

build set: extremal-sup-inf, cross-substitution-fixed-point, orbit-telescoping-aimo0710, monotonicity-order
