## imo-2026-05

All three explorers (substitution, bounding, extremal lenses) independently and rigorously
established the same base layer, which I re-verified by hand (re-derived the algebra myself,
not just trusting the reports):

- `x=f(y)` collapses both outer QM/GM bounds to `f(y)` exactly ⟹ exact FE
  **`f(f(y)) = 2f(y) - y`** for all `y>0`. (*)
- `f` injective (from (*)).
- `g(y):=f(y)-y ≥ 0` for all `y` (orbit `y,f(y),f(f(y)),…` is an exact AP with common
  difference `g(y)`; a negative difference eventually forces the orbit negative).
- `g(f(y)) = g(y)` (g constant along each forward orbit — proved, NOT the same as global
  constancy).
- **Sufficiency, rigorously verified**: `f(x)=x+c` for any constant `c ≥ 0` satisfies BOTH
  original inequalities for all `x,y>0`; both reduce algebraically to `(x-y-c)^2 ≥ 0` (checked
  by hand-expansion, matches all three explorers' independent SOS computations). So the target
  claim is **`f(x)=x+c` for some constant `c≥0`** — NOT `f(x)=x` alone. Any approach that argues
  toward uniqueness of the identity function is wrong and should be rejected.

The single shared open gap across all three explorers: promote `g` from "constant on each
`f`-orbit" to "the SAME constant globally." I spent additional scratch effort deriving a new
tool not in any explorer report: applying the RIGHT (GM) inequality at `(f(x),y)` and `(f(y),x)`
and eliminating `f(f(x)),f(f(y))` via (*) and orbit-invariance yields, for all `x,y>0`,
```
(x-y)^2 ≥ 4·f(y)·(g(x)-g(y))   [real constraint iff g(x)>g(y)]
(x-y)^2 ≥ 4·f(x)·(g(y)-g(x))   [real constraint iff g(y)>g(x)]
```
(verified: reduces to `(x-y)^2≥0` when `f=x+c`, consistent). This is handed to two of the
approaches below as a concrete tool — it is NOT a finished proof, the finishing step (a genuine
"for all x,y" argument, not per-pair) is still open. I also confirmed by hand that the "naive
diagonal orbit-vs-orbit asymptotic" route (compare `f^n(x0)` against `f^n(y0)` as `n→∞`) is a
**provable dead end**: at leading order `n^2`, both inequalities degenerate to plain AM-GM/QM-AM
tautologies in `(p,q)` that hold for ANY `p,q≥0`, so this exact computation cannot discriminate
`p≠q`. This is recorded as a dead end in `orbit-telescoping-aimo0710.md` so builders don't
re-waste budget reproducing it — but the *telescoping* mechanism itself (not just the diagonal
asymptotic) is still worth one adaptation attempt with a non-diagonal pairing.

Four approaches below share the (rigorously proved, not a framing choice) base layer but
diverge sharply in HOW they close the global-constancy gap — an extremal/limiting argument, a
direct finite algebraic trick, an orbit-telescoping adaptation, and an order/monotonicity
argument. This satisfies the "far apart" requirement: each targets the same gap with a
genuinely different proof mechanism, not a variation of one technique.

---

extremal-sup-inf: new
Target: `f: R_{>0}->R_{>0}` satisfies the double inequality for all `x,y>0` **iff**
`f(x) = x + c` for some constant `c ≥ 0`.
Technique: Extremal principle (sup/inf of `g(y)=f(y)-y`) combined with a limiting argument on
the algebraic inequality (A) below — NOT calculus/continuity of `f` itself, just continuity of
polynomial expressions in converging real-number sequences, which is always legitimate.
Skeleton:
  1. Derive base layer: FE (*), injectivity, `g≥0`, `g(f(y))=g(y)` — by the `x=f(y)` collapse.
  2. Verify sufficiency of `f(x)=x+c`, `c≥0` — by the SOS identity `(x-y-c)^2≥0`.
  3. Derive tool (A): `(x-y)^2 ≥ 4f(y)(g(x)-g(y))` for all `x,y>0` — by applying the RIGHT/GM
     inequality at `(f(y), x)`, expanding, and eliminating `f(f(y))` via (*) and
     `g(f(y))=g(y)`.
  4. Let `m = inf_{t>0} g(t) ∈ [0,∞)` (finite, bounded below by 0 from step 1). Take a
     minimizing sequence `x_k` with `g(x_k)→m`.
  5. Case A: some subsequence `x_k → x* ∈ (0,∞)` (finite, positive limit). Pass to the limit in
     tool (A) (legitimate: both sides are continuous functions of the two converging numerical
     sequences `x_k, g(x_k)`) to get, for every fixed `y>0`: `g(y) ≤ [(x*-y)^2+2(x*+y)m+m^2]/(4x*)`
     — an explicit upper bound on every `g(y)` in terms of `m` and `x*` alone.
  6. Case B: `x_k → 0` or `x_k → ∞` (no finite positive limit point) — handle separately;
     the builder must show this case cannot happen (e.g. via the constraint `g≥0` and a size
     argument on tool (A) as `x_k→∞` or `x_k→0`, or show `m` is in fact attained).
  7. Finish: use the bound from step 5 together with `g(y) ≥ m` (definition of inf) to squeeze:
     show `sup_y g(y) ≤ m`, forcing `g(y) = m` for ALL y — i.e. `g` is the single global
     constant `c := m ≥ 0`, giving `f(x) = x + c`.
Key lemmas (claim + mechanism):
  - Tool (A) `(x-y)^2 ≥ 4f(y)(g(x)-g(y))` — because applying the GM-inequality instance at
    `(f(y), x)` and substituting `f(f(y))=y+2g(y)` (from the FE) turns the composite term into a
    pure algebraic expression in `x,y,g(x),g(y)`.
  - Limit-passing in step 5 is valid — because it is elementary continuity of a rational
    expression in two REAL NUMBER sequences (`x_k`, `g(x_k)`), not an assumption about `f`.
Open gaps: Case B (minimizing sequence escaping to `0` or `∞`) is unhandled; the final squeeze
in step 7 needs the bound to actually beat `m` (i.e., needs `x*` chosen so the bound is tight
enough) — this is the crux computation to verify or refute.
Cases to cover: `m=0` vs `m>0`; `x_k` bounded away from `0,∞` vs not.
Watch out for: don't assume `f` continuous — every limit taken must be a limit of a numerical
sequence into an ALREADY-derived true inequality, never "f is continuous so...".

---

cross-substitution-fixed-point: new
Target: same as above — `f(x)=x+c`, `c≥0`, characterizes all solutions.
Technique: Direct finite (non-limiting) algebraic elimination using two orbit-shifted instances
of tool (A)/(B), plus investigating existence of a fixed point of `f`.
Skeleton:
  1-3. Same base layer + tool derivation as `extremal-sup-inf` (derive both (A) and its twin
     (B): `(x-y)^2 ≥ 4f(x)(g(y)-g(x))`, from `(f(x),y)`).
  4. WLOG suppose `g(x) > g(y)` for some `x,y` (aiming for contradiction to prove global
     constancy). Apply (A) not just at `(x,y)` but at `(x, f(y))`: since `g(f(y))=g(y)=q`
     (orbit-invariant) and `f(f(y))=y+2q`, get a SECOND instance:
     `(x-f(y))^2 ≥ 4f(f(y))(g(x)-g(y)) = 4(y+2q)(p-q)`.
  5. Now have two inequalities in `x,y,p,q`: `(x-y)^2 ≥ 4(y+q)(p-q)` and
     `(x-f(y))^2 ≥ 4(y+2q)(p-q)`, i.e. `(x-y-q)^2 ≥ 4(y+2q)(p-q)`. Subtract / combine these two
     quadratic-in-`(x-y)` constraints (both must hold simultaneously for the SAME actual `x,y`)
     to try to derive a genuine numeric contradiction when `p≠q` — this elimination is the open
     gap; if it doesn't close, iterate further (`(x, f(f(y)))`, etc.) to get a whole family of
     constraints indexed by `n`, and look for an `n`-independent contradiction (not an
     `n→∞` one — a genuinely finite algebraic one, since each new instance is exact, not
     asymptotic).
  6. Separately: investigate whether `f` must have a fixed point (`y0` with `g(y0)=0`). If it
     does, tool (A) with `y=y0` gives `(x-y0)^2 ≥ 4y0·g(x)` for ALL `x` — a strong bound that,
     combined with plugging `x` ranging over `y0`'s own forward orbit... (already trivial there)
     — but combined with tool (B) at `y=y0` too might pin `g≡0`, contradicting known solutions
     with `c>0`; so EITHER no fixed point exists in general, OR this sub-route needs care not to
     over-claim `c=0`. Flag explicitly: do not conclude `c=0` is forced — the family has
     `c` free, so if a fixed-point argument seems to force `g≡0` somewhere, re-examine for an
     error (a fixed point need not exist when `c>0`, since `f(x)=x+c` has no fixed point for
     `c>0` at all — so this sub-route may simply be VACUOUS in general and should be dropped
     quickly if it doesn't pan out in one attempt).
Key lemmas (claim + mechanism):
  - Orbit-shifted tool instance in step 4 — because `f(y)` is itself a valid domain point with
    the SAME `g`-value as `y` (orbit-invariance), so plugging it into (A) in place of `y` gives
    a genuinely new, independent constraint on the same `(p,q)`.
Open gaps: the elimination in step 5 (does NOT yet reach a contradiction — needs the builder to
push the algebra, possibly across several orbit-shifts, to isolate `(p-q)` and force it to `0`);
existence (or non-existence, in general) of a fixed point is unresolved and may be a dead
sub-route (see step 6 warning) — spend limited effort there.
Cases to cover: `g(x)>g(y)` (use A) vs `g(y)>g(x)` (use B, symmetric) vs `g(x)=g(y)` (nothing to
prove).
Watch out for: don't accidentally "prove" `c=0` only — that would contradict the known-valid
`c>0` family, so any sub-argument that seems to force `g≡0` has a bug; the target is `g` GLOBALLY
CONSTANT (any value `≥0`), not `g≡0`.

---

orbit-telescoping-aimo0710: new
Target: same — `f(x)=x+c`, `c≥0`, is exactly the solution set.
Technique: Adapt the telescoping-sum-forces-vanishing mechanism from crux `aimo-0710` (IMO 2016
P5 sister problem) — but the diagonal/leading-order version is a PROVEN dead end (see file), so
this approach must use a non-diagonal pairing or telescope a different quantity.
Skeleton:
  1-2. Base layer + sufficiency, as above.
  3. Recorded dead end (do not repeat): comparing `f^n(x0)` vs `f^n(y0)` (matched index) at
     leading asymptotic order gives only tautological AM-GM/QM-AM statements in `(p,q)` — no
     info, proven by direct expansion (see approach file for the full computation).
  4. New attempt for the builder: try mismatched scaling (e.g. `m = round(n·q/p)` so that
     `Y_m ≈ X_n` — i.e. synchronize the two orbits so they nearly COLLIDE at large index, using
     `f` injective to forbid an actual collision) OR telescope the quantity
     `S_N = Σ_{n=0}^{N-1} [(X_{n+1}-Y_n)^2 - 4f(Y_n)(p-q)]` (each summand ≥0 by tool (A)) against
     an a-priori upper bound on `S_N` coming from the original LEFT inequality, in the style of
     `aimo-0710`'s "bound each term below by a fixed constant, sum, compare to a non-growing
     upper bound, force the constant to `0` as `N→∞`."
  5. If this also fails to close (flag likely, given the diagonal dead end already found), the
     builder should report a clean negative result (what was tried, why it degenerates) rather
     than force a fake proof — this is still useful population information.
Key lemmas (claim + mechanism):
  - Each `f`-orbit is an exact AP `y+n·g(y)` — because `g(f(y))=g(y)` telescopes the recurrence
    `y_{n+2}=2y_{n+1}-y_n` from the FE into a constant increment.
Open gaps: the entire non-diagonal telescoping construction in step 4 is unverified — this is
explicitly the highest-risk approach (its most natural version is already a proven dead end);
keep it in the population only because `aimo-0710` is the closest crux analogue and a smarter
pairing might still work, but cap the effort (one serious attempt) before conceding.
Cases to cover: `p=q` (nothing to prove) vs `p≠q` (WLOG `p>q`, aim for contradiction).
Watch out for: re-deriving the already-refuted diagonal (`n=m`, leading order) computation
wastes budget — the builder MUST use a genuinely different pairing/telescoped quantity.

---

monotonicity-order: new
Target: same — `f(x)=x+c`, `c≥0`, characterizes all solutions.
Technique: Order-theoretic — first prove `f` strictly increasing (via a direct 2-point
size argument, no limits), then invoke the classical "monotone solution of a near-additive
relation is affine" phenomenon (the discrete analogue of "monotone Cauchy-equation solutions
are linear"), adapted to the AP-orbit structure here. Genuinely distinct top-level mechanism
from the other three (order/interleaving, not extremal or telescoping or direct algebra).
Skeleton:
  1-2. Base layer + sufficiency, as above.
  3. Attempt: prove `x1<x2 ⟹ f(x1)<f(x2)` (strict monotonicity) using the ORIGINAL LEFT
     inequality at `(x1,x2)`: `(f(x1)+x2)^2 ≤ 2x1^2+2f(x2)^2`, combined with `f(t)≥t` and
     injectivity, to rule out an inversion `f(x1)>f(x2)`. THIS STEP IS UNVERIFIED — the builder
     must check it carefully as the first order of business; if it fails for a direct 2-point
     argument, try a 3-point argument (`x1<x2<x3`) instead before abandoning monotonicity.
  4. Given monotonicity: for `x,y` with slopes `p=g(x)≠q=g(y)` (WLOG `p>q`), the two APs
     `x+np` and `y+mq` interleave in a way that depends only on order (not distance) once `n,m`
     are large — since `f` is injective and increasing, use the fact that `f` maps the orbit
     `{x+np}` to `{x+(n+1)p}` (itself, shifted) and `{y+mq}` to `{y+(m+1)q}`; when the two APs
     interleave with different "densities" (slopes), the increasing bijection-like structure of
     `f` restricted to the union of the two orbits must respect the interleaving order at every
     scale — derive a contradiction from a scale where the interleaving pattern is forced to
     invert. This is the open gap — make the "interleaving must invert" claim precise and prove
     it (or find it doesn't hold and abandon this approach).
  5. Conclude `g` is globally constant `= c ≥ 0`.
Key lemmas (claim + mechanism):
  - Monotonicity of `f` (step 3) — because the LEFT/QM inequality bounds `f(x1)` above in terms
    of `x1,x2,f(x2)`, and combined with `f(t)≥t` this should forbid `f(x1)` from exceeding
    `f(x2)` when `x1<x2` (mechanism to verify: the QM bound gets too small if `f(x1)` is too
    large relative to `x2`).
Open gaps: BOTH step 3 (monotonicity itself, not yet proved — only the mechanism is proposed)
and step 4 (the interleaving-forces-contradiction argument) are open. This is the most
speculative approach of the four; treat step 3 as a fast go/no-go test — if monotonicity fails
to fall out in one clean argument, report that finding (even a refutation, e.g. a hypothetical
non-monotone `g` consistent with all derived constraints) rather than force it.
Cases to cover: `p>q` vs `q>p` (symmetric).
Watch out for: don't assume `f` continuous or differentiable anywhere; "monotone" here must be
proved from the discrete inequality directly, and the interleaving argument must be a genuine
combinatorial/order argument, not hand-waved "clearly the orbits must align."

---

Slugs opened this round: extremal-sup-inf, cross-substitution-fixed-point,
orbit-telescoping-aimo0710, monotonicity-order.
