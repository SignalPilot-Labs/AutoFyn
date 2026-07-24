# Explorer report: two-sided / exact-invariant framing (round 6)

**Lens assignment:** scout an exact recursion invariant I(S) with I(S) = f(I(S'))
at each induction step (equality both directions), as an alternative to the
plateaued "bound top piece, bound tail, add" decomposition. Report only —
no proof attempted.

## 1. What the wall actually is (read from current.md + lemmas)

Four independent framings (mass/cross-term, self-similar bracketing,
LP-vertex/rank-tracking, LP-vertex/exchange) have all converged on: an
induction on $n$ that needs an **upper** bound on $A$ of a reduced
sub-instance, but the machinery only supplies a **lower** bound. Concretely,
the certified `single-cut-perturbation-identity` already gives an **exact**
per-cut recursion:
$$A(S')-A(S) = 2(I_1+I_2) - 2f_2,\qquad I_1,I_2\in[0,f_2].$$
This *is* an equality, not an inequality — but it is not yet a *closed*
recursion, because $I_1,I_2$ (integrals of the tail's odd-parity indicator
over two windows) are not pinned to a value determined by $S$ alone; they
depend on the fine structure of the rest of the multiset. So the "exact
recursion" already exists at the per-cut level; the open problem is that its
correction term is not yet expressed in closed form for the ladder's
specific tail. This reframes the task: **the missing piece is not a new
invariant, but an exact evaluation of $I_1+I_2$ using the ladder's
superincreasing structure ($p_i=2p_{i+1}$), not generic mass bounds.**

## 2. The target constant already has an exact two-sided recursion — but it's about the wrong object

`ladder-self-similarity-constant` and `tail-self-similarity` already prove,
with equality, $f(n) = r(n)\cdot f(n-1)$, $r(n)=1-p_1(n)$. I checked this
collapses to a clean **Möbius/continued-fraction recursion for the target
constant itself**:
$$a_n = \frac{a_{n-1}}{2+a_{n-1}},\qquad a_0:=1,$$
verified exactly with `Fraction` for $n=1,\dots,5$ (all five match
$1/(2^{n+1}-1)$ exactly, zero mismatch). This is a genuine equality-both-
directions recursion — but it is a fact about the **candidate answer**
$a_n$, not about the **adversary-optimal value function** $A^\*(n) :=
\min_{\text{Xiang Yu}} A(\text{final multiset})$. The existing machinery
already proves $A^\*(n)\ge a_n$ is *implied by* $A^\*(n-1)\ge a_{n-1}$ via
this same identity (that's exactly `tail-self-similarity`/Proposition 13's
mechanism). The genuinely open direction is $A^\*(n)\le a_n$, i.e. that no
Xiang Yu strategy beats $a_n$ — and this is a fact about the **value
function**, not the constant, so restating the constant's recursion more
cleverly will not by itself close the gap. **Pitfall for round 6: do not
re-derive this continued-fraction identity as if it were new — it is already
implicit in certified lemmas, and it is not the missing ingredient.**

## 3. A genuinely different candidate: rescale to integers, use the ladder's exact powers-of-two structure

The one lens that looks structurally new: multiply everything by
$D:=2^{n+1}-1$. Then the ladder pieces become the *exact integers*
$2^n,2^{n-1},\dots,2,1$ — a canonical superincreasing/binary set (largest
element exceeds the sum of all the others, at every prefix). This is
precisely the structural fact underlying two crux corpus problems:

- **`aimo-0141`** (combinatorics, pigeonhole/extremal-principle): "a set of
  distinct powers of two has its largest element strictly greater than the
  sum of all the smaller ones" — used there to force a parity contradiction
  after removing the dominant element, then **halve every dimension and
  recurse on the half-size board** (an exact self-similar reduction by
  minimal-counterexample, structurally close to what's wanted here).
- **`aimo-0917`** (combinatorics, invariants-and-monovariants): a game on
  numbers that provably *stay* powers of two under legal moves, terminating
  exactly when "the largest exceeds the sum of the rest" — and a companion
  crux there uses an exact 2-adic-valuation/popcount invariant
  ($S_2(a+b)\le S_2(a)+S_2(b)$) to get an exact lower bound on a count, by
  splitting the invariant additively across the two possible responses
  ($N=N_++N_-$) and using that an odd total forces oddness in one branch —
  a genuinely *exact* (not one-directional) case-split mechanism worth
  studying as a template.
- **`aimo-0764`** (combinatorics, induction-and-construction /
  invariants-and-monovariants): popcount lower bound via "a fixed sum of
  powers of two needs at least as many terms as its binary weight," plus a
  matching *achievability* argument showing every value up to that cap is
  actually reached by a legal single-step chain — i.e. a template for
  proving a bound is *tight*, not just valid, via an explicit step-by-step
  reachability argument. This is the right shape (upper bound + matching
  construction meeting it exactly) but for a monovariant, not yet adapted to
  an alternating-sum functional.

None of these solve the ladder problem directly (they're pigeonhole/popcount
facts on a static set, not a minimax over an adversary's cut choices), but
the transplant idea is: **express $A(S)$ after rescaling by $D$ as a signed
count over the binary digits of the fragment boundaries**, since the ladder,
after rescaling, literally *is* the set $\{2^n,\dots,1\}$, i.e. the binary
digits of $D=2^{n+1}-1$. The odd-parity-indicator machinery already in
`integral-alternating-sum-formula` ($A(S)=\int\mathbb 1[N(x)\text{ odd}]dx$)
integrated over $[0,D)$ against this binary structure might turn $I_1+I_2$
from `single-cut-perturbation-identity` into an exact binary/carry
computation (à la a base-2 digit-DP), rather than a generic real-interval
integral — this is the concrete "genuinely different framing" I recommend
opening as a new approach slug.

## 4. Games-and-strategy crux moves checked (mostly not transplantable, recorded for completeness)

Scanned all 39 `combinatorics/games-and-strategy` cruxes and the algebra/
combinatorics `telescoping-and-summation`, `sequences-and-recurrences`,
`inequalities-SOS-and-convexity` subtopics for "exact/equality invariant,
telescoping potential, two-sided sandwich" moves:

- **`aimo-0019`** (games-and-strategy + invariants-and-monovariants): a
  covering game against dyadic-length intervals maintains an **amortized
  linear potential** ("ink spent on $[0,x_r]$ is at most $3x_r$") proved by
  *charging each step's exact cost against the exact progress it buys* —
  this is the closest crux-corpus analogue to a telescoping potential in a
  cutting/interval game, but it is one-directional (an upper bound on
  cumulative cost, not an equality), so it doesn't itself supply a two-sided
  template; it does, however, model the *style* ("bound this round's exact
  contribution, sum telescopes") that a correction-term bookkeeping for
  $I_1+I_2$ above would need.
- **`aimo-0117`** (already ruled out in `claiming-order-invariant`,
  round 4's dead end) is the "defer commitment" pairing invariant — the
  workspace already correctly diagnosed this doesn't transplant (no
  multi-round loop in the marking stage). Confirmed independently: nothing
  in the other games-and-strategy cruxes changes that diagnosis.
- **`aimo-0596`**, **`aimo-0663`**, **`aimo-0115`**: all mirroring/pairing-
  response strategies for alternating-turn combinatorial games — not
  applicable here since Xiang Yu's move (marking cut points) is a one-shot
  simultaneous-ish Stackelberg choice, not a sequence of turns to mirror
  (consistent with the already-recorded `claiming-order-invariant` dead
  end).
- Algebra `telescoping-and-summation` (44 cruxes) and `sequences-and-
  recurrences` (108): scanned for "exact recursion pinning a minimax," found
  none directly about adversarial min/max value functions — these subtopics
  are dominated by single-player sum/series manipulations, not game values,
  so they inform *bookkeeping technique* (e.g. `aimo-0455`'s "climb a ladder
  of targets via a floor-parity law," a genuinely two-sided membership
  toggle argument) more than a directly transplantable invariant.

## 5. Numeric sanity checks done (exact `Fraction`, no floats)

- Confirmed $a_n=a_{n-1}/(2+a_{n-1})$, $a_0=1$, matches $1/(2^{n+1}-1)$
  exactly for $n=1,\dots,5$ (see §2) — this is a correct but *already-
  implicit* fact, not new leverage.
- Did **not** find a counterexample to `single-cut-perturbation-identity`
  itself (it's already reviewer-certified via 3000 exact-fraction trials);
  flagging it here only because it *is* the exact/equality building block
  the round should build on, rather than re-deriving a fresh "exact
  invariant" from scratch.

## 6. Recommendation for the outliner

Open one new slug attacking **exact evaluation of $I_1+I_2$
(single-cut-perturbation-identity's correction term) via the rescaled-
integer/binary-digit structure of the ladder**, rather than another
top/tail mass-bound variant. Concretely: rescale by $D=2^{n+1}-1$ so the
ladder is exactly $\{2^n,\dots,2,1\}$; re-express the odd-parity indicator
$u_R(x)$ and the windows $[0,f_2)$, $[f_1,M)$ from
`single-cut-perturbation-identity` as functions of the *binary
representation* of $x\in[0,D)$ relative to the tail's own recursive
(superincreasing) structure, aiming for an exact digit-carry formula for
$I_1+I_2$ analogous to the popcount/digit-sum exactness in `aimo-0764` and
`aimo-0917`, rather than a real-interval integral bound. This is genuinely
far from all five plateaued approaches (none of them touch the integer/
binary rescaling) and targets the *actual* remaining gap (an exact
evaluation, not a fresh bound) rather than routing around it.
