## imo-2026-05

- Distinct openings:
  1. **[Strongest — retrieval-independent, self-derived, verified]** Split the
     sandwich into a right inequality (R): `(f(x)+y)/2 ≥ sqrt(x·f(y))` and a
     left inequality (L): `sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2`, both holding for
     ALL `x,y>0`. Substitute **`(x,y) = (f(t), t)`** into both simultaneously.
     Since the pair fed into the QM/GM on the outer slots becomes `(f(t),f(t))`
     (a repeated value), QM(f(t),f(t)) = GM(f(t),f(t)) = f(t) exactly — the
     sandwich collapses to an *equality*, not just an inequality:
     `f(t) ≥ (f(f(t))+t)/2 ≥ f(t)`, forcing `f(f(t)) = 2f(t) − t` for every `t`.
     This is exact (no error term), derived directly from the hypothesis with
     no casework — algebraically verified by hand and spot-checked numerically
     with f=id (see Small-case notes). Defining `g(t) = f(t) − t`, the identity
     rereads as `g(f(t)) = g(t)`: **g is constant along f-orbits**. This is the
     natural target for the outliner to develop (orbit/iterate argument).
     Also gives the free bound `f(t) > t/2` for all `t` (since `f(f(t))>0`).
  2. Pitfall to flag: the "obvious" substitution `x=y=t` is a **trap** — it
     only recovers the tautological QM(t,f(t)) ≥ AM(t,f(t)) ≥ GM(t,f(t)),
     which is true for ANY positive `t,f(t)` by the standard QM-AM-GM chain.
     It carries zero information about which `f` works. Do not waste a round
     rediscovering this; go straight to opening 1's asymmetric substitution.
  3. Reformulation view: (R) says `AM(f(x),y) ≥ GM(x,f(y))` and (L) says
     `QM(x,f(y)) ≥ AM(f(x),y))` — i.e. `AM(f(x),y)` is sandwiched between the
     GM and QM of the *swapped* pair `(x,f(y))`. Since ordinarily
     `GM(a,b) ≤ AM(a,b) ≤ QM(a,b)` for the SAME pair, forcing this to hold
     with a swapped pairing for all `x,y` is exactly the kind of rigidity that
     pins `f = id`. Swapping `x↔y` in the original two inequalities gives a
     dual pair; combining/subtracting the swapped versions is a second
     concrete lever the outliner can use alongside opening 1.
  4. Once `f(f(t))=2f(t)−t` is in hand, the standard next moves (not
     developed here, left for outliner) are: (a) show `f` injective or
     strictly monotonic using (L)/(R) directly, then (b) iterate the affine
     recursion `f(f(t)) = 2f(t) - t` — this says the orbit `t, f(t), f(f(t)), …`
     is an arithmetic progression with common difference `g(t) = f(t)-t`, and
     `g` is invariant along the orbit. Bounding `g` (e.g. via the positivity
     constraint `f(t) > t/2`, or via injectivity/boundedness arguments) should
     force `g ≡ 0`.

- Candidate technique(s): "asymmetric self-substitution to collapse an
  inequality sandwich to an equality" (opening 1); orbit/iterate telescoping
  once an exact affine iterate relation `f(f(t))=2f(t)-t` is established;
  QM-AM-GM equality-case analysis; injectivity-from-strict-inequality.

- Cheap-kill candidates: the `x=y` substitution is a **cheap non-kill** — it's
  cheap to try but yields no constraint at all (flagged above as a pitfall,
  not a route). The genuine cheap win is the `(x,y)=(f(t),t)` substitution in
  opening 1, which is a one-line computation and immediately yields an exact
  functional identity `f(f(t))=2f(t)-t` plus the bound `f(t)>t/2` — this
  should be the first thing any approach establishes before anything heavier.

- Knowledge-base entries to use: **Standard inequalities: AM-GM, Cauchy-Schwarz,
  QM-AM ... Equality cases pin down the extremal configuration** (KB §Algebra
  & Polynomials) — directly the mechanism behind opening 1. **Functional
  equations: test special values, check injectivity/surjectivity** (same
  section) — for the follow-up once `f∘f` is pinned. **Meta-Strategy: check
  small cases first / specialize at extreme or symmetric values** — but note
  the symmetric value `x=y` is here a false lead (see pitfall above); the
  informative specialization is the *asymmetric* self-referential one
  `x=f(y)` paired with `y=x`.

- Analogous past problems (cruxes):
  - `aimo-0008` (Bulgaria, ISL-style): functional INEQUALITY system
    `f(x)f(y)≥f(xy)`, `f(x+y)≥f(x)+f(y)`, `f(a)=a` for some `a>1` ⟹ `f=id`.
    Crux move: *"Convert a one-sided bound into equality by sandwiching
    against a known exact value at a large point... letting the inequality
    force each summand to be tight."* Genuinely analogous in spirit — a pair
    of one-directional inequalities is combined/iterated until tightness is
    forced, ultimately pinning `f(x)=x` exactly. The mechanism differs (their
    tightness comes from an additive telescoping argument at scale, ours from
    a single self-referential substitution) but the *meta-pattern*
    "two inequalities + a clever combination ⟹ forced equality ⟹ f=id" is the
    same, and their solution's overall shape (prove `f(x)≥x`, then squeeze
    equality via an additive split at a large point) is a good template for
    finishing once opening 1's `f(f(t))=2f(t)-t` and `f(t)>t/2` are in hand.
  - `aimo-0191` and `aimo-0010`: both have cruxes about turning an iterate
    relation into a *closed affine formula* along an orbit (`"telescope the
    per-step increments to get a closed affine formula"`, `"Bootstrap a
    functional equation into a global affine identity h^N(n)=n+c"`). These
    are close analogs for the SECOND stage of this problem: once we have the
    exact `f(f(t)) = 2f(t) - t` (an affine iterate law), the natural next
    step — orbit telescoping to pin the constant increment to 0 — mirrors
    these cruxes' machinery, though those are on integers/naturals and ours
    is on `R>0`, so the boundedness/injectivity argument must be redone from
    scratch for the real setting.
  - No crux in the corpus directly matches the "QM ≥ AM ≥ GM sandwich with
    swapped arguments" surface form — opening 1's substitution appears to be
    a fresh derivation specific to this problem, not a retrieved pattern.

- Prior progress: none (round 1, no approaches filed yet in
  `results/imo-2026-05/approaches/`; `current.md` Status = unsolved).

- Dead ends (do not retry): none recorded yet from prior rounds. Self-found
  pitfall to record: **the symmetric substitution `x=y=t` is vacuous** — it
  only reproduces the trivial QM-AM-GM chain for the pair `(t,f(t))`, true for
  any positive `f(t)`; it should not be presented as a "step" in any approach
  since it establishes nothing about which `f` satisfies the hypothesis.

- Small-case / intuition notes: **Verified algebraically** (not just
  numerically) that substituting `x=f(t), y=t` into both halves of the given
  sandwich forces the equality `f(f(t)) = 2f(t) - t` for all `t>0` — this is
  a *proved* fact from the hypothesis alone, not a conjecture, though the
  outliner/builder still needs to re-derive and write it rigorously (do not
  cite this report as a proof). Numerically spot-checked with the candidate
  `f=id` (5 random `t∈(0.1,10)`): all three terms of the sandwich coincide
  exactly at `f=id`, consistent with `f=id` being the answer (this is
  necessary-condition evidence for `f=id`, not yet a full verification that
  `f=id` satisfies the ORIGINAL two-variable inequality for all `x,y` — that
  substitution check, `sqrt((x²+y²)/2) ≥ (x+y)/2 ≥ sqrt(xy)`, is just the
  textbook QM-AM-GM chain and is immediate/always true, so `f=id` is
  conjectured (very likely provably) to be a valid solution and, by the
  rigidity from `f(f(t))=2f(t)-t` plus the extra freedom needed to rule out
  other affine-orbit solutions, is conjectured to be the *unique* solution.
  The remaining gap for the outliner: turn `f(f(t))=2f(t)-t` (+ `f(t)>t/2`,
  + whatever monotonicity/injectivity comes from (L)/(R) directly) into
  `f(t)-t ≡ 0`.
