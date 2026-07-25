## imo-2026-05

- Distinct openings (this lens — structural identity / equality-case / extremal):

  **Opening 1 (equality-forcing degenerate substitution — the strongest find this round).**
  Substitute **x = f(y)** into the original chain. Then the QM term collapses:
  `sqrt((f(y)^2+f(y)^2)/2) = f(y)` (equal entries under the square root), and the GM term
  also collapses: `sqrt(f(y)*f(y)) = f(y)`. So BOTH outer bounds equal `f(y)` exactly, and
  the chain `f(y) >= (f(f(y))+y)/2 >= f(y)` is squeezed to **equality**:
  ```
  f(f(y)) + y = 2 f(y)     for all y > 0.        (*)
  ```
  This is a clean, gap-free functional equation (no inequality residue) derived purely from
  an equality-case argument — QM = value and GM = value both trigger at x = f(y) simultaneously.
  I verified this algebraically and it is airtight (x=f(y) is a legal substitution since
  f(y) > 0 lies in the domain).

  From (*), two rigorous consequences follow immediately (both fully checked, no gaps):
  - **Injectivity of f.** If f(a) = f(b), apply (*) at a and at b: f(f(a)) = 2f(a) − a,
    f(f(b)) = 2f(b) − b. Since f(a) = f(b), the LHS's are equal (f applied to equal values),
    so 2f(a) − a = 2f(a) − b ⟹ a = b.
  - **f(y) ≥ y for every y (via an "arithmetic-progression orbit" argument).** Fix y, set
    y_0 = y, y_n = f(y_{n-1}). Applying (*) at each y_n gives y_{n+2} = 2y_{n+1} − y_n for
    all n ≥ 0, so (y_n) is an exact arithmetic progression: y_n = y + n·d where
    d = f(y) − y. Since f maps R_{>0} → R_{>0}, every y_n > 0, including as n → ∞; if d < 0
    then y_n → −∞, contradiction. Hence d ≥ 0, i.e. **f(y) ≥ y for all y.**

  **Opening 2 (the family f(x) = x + c, c ≥ 0, is a genuine 1-parameter solution family —
  NOT just the identity).** I tested and then algebraically confirmed: for f(x) = x + c
  (any constant c ≥ 0), BOTH original inequalities reduce to the *same* perfect square:
  - Left (QM bound): `2x^2 + 2f(y)^2 − (f(x)+y)^2 = (x − y − c)^2 ≥ 0`.
  - Right (GM bound): `(f(x)+y)^2 − 4x f(y) = (x − y − c)^2 ≥ 0`.
  Both algebraic identities check out term-by-term (I expanded both sides by hand) and
  numerically (spot-checked several (x,y,c) triples, including asymmetric/extreme ones like
  x=100,y=0.001; x=0.001,y=100; c=5). **This means the answer is very likely the whole family
  `f(x) = x + c` for constant `c ≥ 0`, not the identity alone.** This is an important
  correction to the "obvious guess f(x)=x" — any approach that tries to prove f(x)=x is the
  *unique* answer will fail because f(x)=x+1, x+5, etc. are also valid. (Sanity check that
  NOT everything works: f(x) = 2x fails — at x=5, y=1: QM = sqrt((25+4)/2) = 3.808 but
  middle = (f(5)+1)/2 = 5.5 > 3.808, violating the left inequality. So the family is special,
  not "any f(x) ≥ x works.")

  **Opening 3 (remaining gap — pin down that d(x) := f(x) − x is a GLOBAL constant, not
  just orbit-invariant).** From (*), g(y) := f(y) − y satisfies g(f(y)) = g(y) (constant
  along each forward f-orbit, matching the AP step d used in Opening 1), but this alone
  does NOT yet force g to be the same constant across *different* starting points / orbits.
  The finishing step needs the **general** (non-degenerate) inequality for arbitrary
  (x,y) pairs, not the special substitution x=f(y). Two candidate finishing routes from this
  lens:
    (i) **Extremal/variational finish**: having shown d(x) ≥ 0 for all x (Opening 1), consider
        `m = inf_x d(x)` and `M = sup_x d(x)` (in [0,∞], not yet known finite) and try to derive
        m = M using the general two-sided inequality applied at extremal or near-extremal x.
        This needs boundedness of d first — plugging generic x,y into the expanded left/right
        inequalities (I expanded these; they produce cross terms like `-2x d(x)` and
        `-4x d(y)` that should force d bounded / eventually pin the constant) — this is
        unfinished, flagged as the key gap for the outliner.
    (ii) **Self-dual swap (x↔y) argument**: write the chain for (x,y) and for (y,x)
        simultaneously (both valid instances of the hypothesis) and combine; I did not find
        a clean forcing argument here in the time available, but it's a genuinely distinct
        angle from (i) — combining `(f(x)+y)^2 <= 2x^2+2f(y)^2` with the swapped version
        `(f(y)+x)^2 <= 2y^2+2f(x)^2` by subtracting may isolate `d(x)-d(y)` linearly.

- Candidate technique(s): equality-case forcing in AM-GM/QM chains (degenerate substitution
  x=f(y) collapsing both bounds simultaneously — this is the load-bearing move); orbit /
  telescoping arithmetic-progression argument on iterates; extremal principle (inf/sup of
  d(x)=f(x)-x) for the finishing uniqueness step; SOS identity recognition
  ((x-y-c)^2 factoring) to verify sufficiency of the answer family.

- Cheap-kill candidates: the perfect-square factoring done above is itself a cheap
  structural check — it immediately confirms sufficiency of f(x)=x+c (c≥0) without any
  calculus/growth machinery. Also: plugging x=f(y) is a "cheap" one-line kill that produces
  the full functional equation (*) essentially for free — should be step 1 of any approach.

- Knowledge-base entries to use: **Standard inequalities (AM-GM, Cauchy-Schwarz, QM-AM,
  Schur — "equality cases pin down the extremal configuration")** — directly used in
  Opening 1. **Sum of squares (SOS)/completing the square** — used in Opening 2 to verify
  the family (both inequalities reduce to (x−y−c)^2 ≥ 0). **Functional equations: test
  special values, check injectivity/surjectivity** — matches Openings 1 and 3.
  **Pigeonhole/extremal principle** and **Invariants & monovariants** (general entries) are
  relevant to the Opening 3(i) finishing argument once formalized.

- Analogous past problems (cruxes): queried `past_crux_moves_database.json` filtered to
  `domain=algebra`, `subtopic` in {functional-equations, extremal-principle,
  inequalities-SOS-and-convexity} (416 hits total).
  - `aimo-0010` (ISL/IMO-style, f: Z≥0→Z≥0, f(f(f(n)))=f(n+1)+1) — genuinely analogous
    **mechanism**: cruxes there include "Compute one higher iterate of the unknown function
    two ways ... to collapse the awkward triple composition into a clean shift-recurrence"
    and "Bootstrap a functional equation into a global affine identity h^N(n)=n+c by
    producing a one-step shift relation for a high iterate and inducting from a single base
    value." This mirrors exactly my Opening 1/3 structure: derive an iterate recurrence,
    show it forces an affine/AP shift, then need a separate argument to pin the constant
    globally. Worth reading in full for the "how do you nail down the constant `c` globally"
    step, since that's our exact remaining gap.
  - `aimo-0008` (f:Q>0→R, f(x)f(y)≥f(xy), f(x+y)≥f(x)+f(y), f(a)=a ⟹ f=id) — analogous
    **flavor**: two-sided-squeeze-to-equality via sandwiching against an exact value,
    "splitting that point additively and letting the superadditive inequality force each
    summand to be tight." Useful pattern for `Opening 3(i)`: turning an inequality that's
    "almost tight" into exact equality by a clever additive/multiplicative splitting — a
    technique to try when pinning down c.
  - No crux found that is a direct hit on "two-sided QM-AM-GM sandwich functional
    inequality" specifically — this problem's exact shape (an inequality trapped between
    QM(x,f(y)) and GM(x,f(y))) doesn't have a close corpus analogue; the above two are
    analogous in *mechanism* (iterate recurrence → affine family → pin the constant) rather
    than surface form.

- Prior progress: none in `results/imo-2026-05/` (no approach files yet, current.md is
  empty/unsolved, `sample_approaches` returned 0 approaches — this is genuinely round 1).

- Dead ends (do not retry): none recorded yet by others. From my own exploration this
  round: plugging y = f(x) (the "dual" degenerate substitution) after already knowing (*)
  produces only the trivial identity `d^2 ≥ 0` / `2d^2 ≥ d^2` — it does NOT give new
  information beyond (*) (I checked both the resulting left- and right-inequality
  consequences reduce to tautologies). So iterating degenerate substitutions along the
  orbit is a dead end for the finishing step — the outliner needs a genuinely
  off-orbit (x,y) pair (Opening 3) to close the gap.

- Small-case / intuition notes (labeled as conjecture where not fully proved):
  - **Proved (not just conjectured) this round**: (*) `f(f(y)) + y = 2f(y)` for all y;
    f injective; f(y) ≥ y for all y.
  - **Proved (algebraic identity, fully rigorous)**: f(x) = x + c satisfies the full
    original double inequality for every constant c ≥ 0 — sufficiency of this whole family
    is established, not just conjectured.
  - **Conjectured** (strong numerical/structural evidence, not yet proved): the answer is
    *exactly* the family `f(x) = x + c, c ≥ 0`, i.e. the remaining necessity direction is
    to show `d(x) = f(x) - x` is the same constant for every x (not merely orbit-invariant).
    I could not close this in the scouting budget; flagged as the key open gap for the
    outliner (see Opening 3).
