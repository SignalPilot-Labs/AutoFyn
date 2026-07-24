## imo-2026-03 — lens: LOWER BOUND, GAP-L Case 2

### What GAP-L Case 2 actually is
Scaled setup (all three approaches agree): LB plays dyadic `W_n = {2^0,...,2^n}`
(sum `D_n = 2^{n+1}-1`). XY responds with `<=n` cuts. `self-similar-recursion`
proved the exact decoupling when XY puts `j>=1` cuts into the top piece `2^n`
(splitting it into `s_1>=...>=s_{j+1}`, remaining `<=n-j` cuts fall on
`R = W_{n-1}` giving `R'`):
```
f(P) = (s_1 - 2^{n-1})^+ + f(Q),   Q = (top pieces capped at 2^{n-1}) ∪ R'.
```
Open crux: prove `(s_1-2^{n-1})^+ + f(Q) >= 1`. This is the genuine extremal
case (numerically the minimum `f=1` IS attained here, not in Case 1).

### New finding this round: the right induction target (conjecture, numerically solid)
I ran a global numeric search (scipy `differential_evolution`, continuous cut
positions, no restriction to "top vs R" — cuts can go anywhere) for
`min f(final)` over **exactly `k` cuts** (any placement) applied to `W_n`, for
`n=1..4`, `k=0..n`. Result (exact integers, optimizer converged to machine
precision):
```
n=2: k=0->3, k=1->1, k=2->1
n=3: k=0->5, k=1->3, k=2->1, k=3->1
n=4: k=0->11, k=1->5, k=2->3, k=3->1, k=4->1
```
These match **exactly** `f(W_{n-k})`, where `f(W_m) = (2^{m+1}+(-1)^m)/3`
(the alternating sum of `{1,2,...,2^m}` itself — a Jacobsthal-type sequence
`1,1,3,5,11,21,...` satisfying `f(W_m) = 2^m - f(W_{m-1})`, the same identity
used in the certified Case-1 argument).

**Conjecture (GAP-L strengthened form):**
```
For any placement of <= k cuts (k <= n) anywhere on W_n:  f(final) >= f(W_{n-k}).
```
Setting `k=n` gives exactly the target `f(final) >= f(W_0) = 1` — i.e. this
single strengthened statement (proved by induction on `k`) would close **all**
of GAP-L (both Case 1 and Case 2 at once — no case split needed).

### Why this is plausible / the mechanism (verified by hand, not yet a proof)
The extremal strategy achieving equality is a **bisection cascade**, and it is
driven entirely by the already-certified **matched-pair invisibility (P1)**
lemma (in `lemmas/layer-cake-alt-sum.md` and restated in
`alternating-sum-threshold-potential.md`): bisecting the (unique) top piece
`2^m` of `{2^m} ∪ W_{m-1}` produces two copies of `2^{m-1}`; combined with the
existing `2^{m-1}` in `W_{m-1}` this makes **three** (odd) copies of `2^{m-1}`,
two of which cancel by P1 (matched-pair invisibility), leaving exactly
`{2^{m-1}} ∪ W_{m-2}` — i.e. `f` after the bisection is **exactly**
`f(W_{m-1})`. Iterating (always bisect whichever copy currently sits at the
new top — always odd count, since parity is preserved by cancellation)
telescopes: `k` bisections send `f(W_n) -> f(W_{n-1}) -> ... -> f(W_{n-k})`.
I hand-verified this chain of multisets for `n=3,4` (see below) and it matches
the DE optimizer's output digit-for-digit.

Example (`n=4`, cascading bisections): `W_4={1,2,4,8,16}`
- 1 cut (bisect 16): `{8,8,8,4,2,1}`, `f=5=f(W_3)`.
- 2 cuts (bisect an 8): `{8,8,4,4,4,2,1}`, `f=3=f(W_2)`.
- 3 cuts (bisect a 4): `{8,8,4,4,2,2,2,1}`, `f=1=f(W_1)`.
- 4 cuts (bisect a 2): `{8,8,4,4,2,2,1,1,1}`, `f=1=f(W_0)` (unchanged — the
  4th cut is *redundant*, since `f(W_1)=f(W_0)=1` already).

**Equality-case corollary:** the floor `f=1` is already reached at budget
`k=n-1` cuts — the `n`-th cut is never strictly necessary for XY to reach the
minimum. This matches CLAUDE.md's warning that "bisect `n` times" as a *global*
strategy overshoots for the **upper**-bound direction, but is consistent here
because this is the *lower*-bound (LB-favorable) direction where XY is
already capped at the floor with one cut to spare.

### What is NOT yet proved (the real remaining gap)
The DE search is strong numerical evidence (matches to machine precision,
n=1..4, all k) but it is **not a proof** that no other cut placement/order
beats the cascade — i.e. the inequality direction `f(final) >= f(W_{n-k})`
for *arbitrary* (non-cascading, cuts split between top and R in any way,
non-bisecting cuts) placements is still open. What would close it: an
induction on `k` (number of cuts used so far) with inductive step "the first
cut XY makes cannot lower `f` by more than `f(W_n)-f(W_{n-1})`, whatever piece
it targets and wherever it cuts" — this needs the single-cut damage bound
(Lemma 3 in `alternating-sum-threshold-potential.md`: a cut of a piece `p` at
offset `x<=p/2` flips parity on a set of measure `<=p`, changing `f` by at
most that much) combined with a monotonicity/exchange argument that cutting
anything other than the current (odd-multiplicity) top is never better for
XY — structurally very similar in spirit to the already-certified
monotonicity sub-lemma (M) inside `lemmas/endgame-greedy.md`, but for *cutting*
rather than *removing* an element. I did **not** attempt this proof (out of
scope for exploration) — it is the concrete next target.

I also spot-checked that cutting a **non-top** piece is strictly worse for XY
(consistent with the conjecture): e.g. `n=3`, bisecting the `4`-piece instead
of the top gives `{8,2,2,2,1}`, `f=8-2+2-2+1=7 >> f(W_2)=3`. So "always attack
the current top" really does look load-bearing, not accidental.

### Distinct openings for the outliner
1. **(Primary, new this round) Strengthened-invariant induction.** Prove
   `min_{<=k cuts} f(W_n) = f(W_{n-1})` for ONE cut first (base case of the
   telescoping cascade), using P1 + a "cutting the top is optimal for XY"
   exchange lemma, then induct on `k`. This closes GAP-L (Case 1 and Case 2
   together, no split) in one shot if the one-cut base case and the exchange
   step both go through. This is the most promising lead found this round.
2. **Direct Case-2 decoupling closure (original self-similar-recursion path).**
   Keep the `(s_1-2^{n-1})^+ + f(Q)` decoupling and prove it directly via the
   same cascade/P1 mechanism restricted to the top sub-pieces — a special case
   of opening 1 but framed within the existing approach file (lower risk,
   less novel).
3. **Matching-cost / LP-duality framing (alternating-sum-threshold-potential's
   Lemma 2).** Since `f` = min-weight perfect matching cost, GAP-L asks: every
   matching of every `<=n`-cut refinement of `W_n` costs `>=1`. A dual
   certificate (weights `y_i` on original marks with `sum y_i <= 1` per cut,
   LP-duality style) might give a one-shot proof avoiding induction on `k`
   altogether — untried, worth a shot if the induction route stalls.

### Cheap-kill candidates
- None obvious for ruling out configurations wholesale, BUT: the exact
  telescoping numbers above (`f(W_m)` Jacobsthal recursion) are a strong
  *consistency check* / cheap falsification test any proposed proof of GAP-L
  should reproduce — a proof attempt whose bound doesn't recover
  `f(W_{n-k})` exactly for all k is likely not tight enough.
- Parity: `f(W_m)` alternates being `1,1,3,5,11,21,...` — note `f(W_0)=f(W_1)`,
  a mild non-strict-monotonicity worth flagging so no one assumes `k`-budget
  strictly improves XY's position every step.

### Knowledge-base entries to use
- `lemmas/layer-cake-alt-sum.md` (matched-pair invisibility P1, single-cut
  parity-flip action) — directly powers the cascade mechanism above.
- `lemmas/endgame-greedy.md` (monotonicity sub-lemma (M)) — structural
  template for the "cutting the top is optimal" exchange lemma opening 1 needs
  (analogous proof technique: compare two candidate moves via a monotonicity
  argument, induction on multiset size).
- Check `knowledge_base.md` generically for "extremal principle" / "invariant
  under smoothing" entries — I did not find a named KB entry specific to this
  (the population's own certified lemmas are the load-bearing tools here, not
  generic KB entries); if `knowledge_base.md` has an entry on min-weight
  matching on a line or telescoping recursions it would support opening 3.

### Analogous past problems (crux corpus)
Searched `combinatorics` subtopics `games-and-strategy`, `invariants-and-
monovariants`, `extremal-principle` for stick/interval/cutting/matching/
alternating-sum keywords. **No strong analog found.** The closest thematic hit
is `aimo-0225` (UK, IMO-style counter game on an n-gon, P/N analysis via
2-adic valuation of a difference that halves at each recursive step) —
structurally resonant (recursive halving / self-similar reduction, `games-
and-strategy` subtopic) but the actual mechanics (isosceles-triangle counter
game, win/loss not a sum-value game) are not close enough to adapt a concrete
move from. I recommend not forcing this citation; the load-bearing mechanism
here (matched-pair cancellation under bisection) is already internal to the
population's own certified lemmas, not something the corpus supplies.

### Prior progress
See `results/imo-2026-03/current.md` and `approaches/self-similar-recursion.md`:
Lemma 0 (endgame-greedy), layer-cake identity, LB dyadic construction, Case 1
of GAP-L fully proved, Case 2 exact decoupling `f(P)=(s_1-2^{n-1})^+ + f(Q)`
proved. This round's finding (the `f(W_{n-k})` telescoping conjecture) sits
directly on top of that decoupling and unifies Case 1/Case 2.

### Dead ends (do not retry)
- "Apply IH `f(R')>=1` directly, then bound `f(Q)` by adding capped top
  pieces" — recorded as failing (adding pieces can decrease `f` by up to their
  full total, too lossy). Confirmed still correct reasoning; the fix is not to
  add pieces post-hoc but to run the induction on the **combined** multiset
  from the start (opening 1 above), tracking budget `k` not "top vs R".
- "Blanket exchange lemma: moving a cut out of a non-max piece into the top
  never raises `f`" — FALSE in general (28k counterexamples per round 1); only
  provably true when restricted to attacking the *current, uniquely/oddly-
  multiplicit top* of a partially-cascaded `W_n`-like multiset, which is
  exactly the narrower claim opening 1 needs (not the blanket one).

### Small-case / intuition notes (all labeled conjecture except where noted PROVED)
- **PROVED (round 1, re-verified here):** Case 1 (`j=0`), `f(P) >= 1` via
  `f(P) = 2^n - f(R') >= 2^n - Sigma(R') = 1`.
- **Conjecture, strong numeric support (n=1..4, all k, machine precision):**
  `min_{<=k cuts anywhere on W_n} f = f(W_{n-k})`, `f(W_m)=(2^{m+1}+(-1)^m)/3`.
  This directly implies GAP-L (`k=n` case) and unifies Case 1/2.
- **Conjecture (hand-verified n=3,4 explicit multisets, matches DE):** the
  extremal XY strategy is the bisection cascade always splitting the current
  (odd-multiplicity) top value in half.
- **Verified by direct computation:** cutting a non-top piece is strictly
  worse for XY (e.g. `n=3` bisecting the `4` instead of top `8` gives `f=7`
  vs. the cascade's `f=3`) — supports "attack the top" being essential, not
  incidental.
