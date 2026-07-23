## imo-2026-03 (lower-bound direction: does Liu Bang's dyadic construction resist every XY response?)

### Setup recap (from certified lemmas + current.md, verified, not re-derived here)
By Lemma G, the game reduces to `e := L−X`, target `e_n = 1/(2^{n+1}-1)`; LB's conjectured
optimal opening at level `n` is the geometric multiset `D_n = (2^n, 2^{n-1}, …, 2, 1)` (n+1
pieces, sum `2^{n+1}-1`); at `n=2`, `D_2=(4,2,1)/7`. The **lower-bound direction** needs: for
this specific `D_n`, no XY response (≤n further cuts) can push `e` below `e_n`. This is
completely open (only ~15 hand-picked candidates spot-checked at n=2 in both approach files).
I did **not** attempt to close this — only scouted routes, per instructions.

### Distinct openings

**1. Dominance/superincreasing structural lemma + recursive "peel off the top piece" induction
(most promising, potentially generalizes to all n — NOT yet tried by either sibling
approach).**
`D_n` is a **superincreasing sequence**: `2^k > 2^{k-1}+…+2+1 = 2^k − 1` for every k (trivial
induction). This is the *exact* structural mechanism behind crux `aimo-0117` ("assign played
values as a two-sided geometric/dyadic sequence so the largest strictly exceeds the sum of all
others") and `aimo-0401` ("when each element dominates the sum of all smaller ones, replace a
running cumulative-sum inequality with a single condition on the current top element") — see
Analogous problems below. Consequence for our problem: **if XY's cuts never touch `a_1`
(=`2^n`), `a_1` is unconditionally locked at rank 1 forever**, no matter how XY subdivides the
rest — because after any cuts to the other pieces, their total is still exactly `2^n−1 < a_1`,
so no single resulting sub-piece (nor `a_1` itself, untouched) can be displaced from rank 1.
This gives a clean case split, `a_1` cut vs. `a_1` untouched, that is *forced* rather than
merely sufficient (a genuine two-sided dichotomy, unlike the upper-bound's Case (i)/(ii) split
which only needed sufficiency):
- **Branch A (`a_1` untouched):** writing the final sorted multiset as `[a_1, r_1, r_2, …]`
  (`r`'s from XY's ≤n cuts on the residual `R=D_n\setminus\{a_1\}`, sum `2^n−1`), a direct rank
  computation gives `e(\text{total}) = a_1 − e_R(R)` where `e_R(R) := r_1−r_2+r_3−…` is R's own
  alternating sum (R's own "first mover", who is effectively XY here since `a_1` claims rank
  1). Bounding `e(\text{total})` from below reduces to bounding `e_R(R)` from **above** — i.e.
  an upper bound on how much a single *unopposed* cutter (no adversary, since LB doesn't move
  again) can boost `R`'s own alternating advantage using ≤n cuts. This is a **new dual claim**,
  not previously stated: "Level-m dual: for k≤m pieces summing to `S`, an unconstrained cutter
  with ≤m cuts can achieve `e ≤` [explicit bound]." It is provable, in principle, with the
  *same* machinery already certified (Lemma P + the vertex/tie lemma, just aimed at
  maximization instead of minimization) — a numeric probe (below) suggests the achievable max
  saturates near `r_1` alone (the rest gets "neutralized" into duplicate pairs via Lemma P,
  contributing zero), which would make Branch A give `e ≥ a_1 − r_1 = 2^n − 2^{n-1}`, an easy
  win over `e_n\cdot S = 1`, so Branch A is not the hard case — this matches the empirical
  finding (both sibling approaches, and my own probe below) that XY's winning n=2 strategies
  all cut `a_1`.
- **Branch B (`a_1` is cut):** by the vertex lemma, XY's cut on `a_1` is a tie or bisection;
  Lemma P then reduces the problem to a residual with ≤n pieces and ≤(n−1) further cuts — this
  is *exactly* the recursive structure of the conjectured recursion
  `e_n = e_{n-1}/(2+e_{n-1})` already verified algebraically in `current.md`. The open task is
  to show that among all of XY's tie/bisect choices for cutting `a_1`, the two canonical ones
  (bisect, or match `a_1` down to `a_2`) are the ones that force `e` down the most, and that the
  resulting residual game genuinely reduces to (a scaled copy of) `D_{n-1}` under adversarial
  optimal play — i.e., this branch needs a **joint induction on both directions simultaneously**
  (the residual's own lower bound requires the (n−1)-level lower bound as IH, exactly mirroring
  how the existing upper-bound Case (i) induction used the (n−1)-level upper bound as IH).
  **Meta-point for the outliner:** this suggests the *cleanest* framing is not "prove the lower
  bound as an isolated approach" but a **single strong induction on `n` proving both directions
  together**, using the dominance lemma to force the branch split and Lemma P to peel off a
  level at each step — a genuinely different top-level target from both sibling approaches
  (which treat n=2's upper bound and n=2's lower bound as separate, already-stuck problems).

**2. Finish the finite vertex enumeration at n=2 (bounded, concrete, but explicitly does NOT
generalize — flagged as a dead end for general n by both siblings' own honest assessment).**
The vertex/tie lemma (proved in general, in both `dyadic-cascade-induction` §3 and
`elementary-exchange-smoothing` Step A) already reduces XY's optimal response, for ANY fixed
input, to a finite set of "tie/bisect" candidate cut-placements. At n=2 (3 pieces, ≤2 cuts) the
combinatorial pattern space is small: 2 cuts on the same piece (3 choices of which piece), or
1 cut each on 2 different pieces (3 choices of pair), or 1 cut total, or 0 cuts — each pattern's
*tie* candidates form a small finite list per the vertex lemma's corollary (already invoked,
not fully enumerated, in both approach files). This is mechanical, bounded casework — doable in
a round, but both approach files independently flag it as **not scaling to n≥3** (residual after
one reduction step can have arbitrarily many pieces, and the number of cut-allocation patterns
across k pieces with ≤n cuts grows combinatorially). Useful only to fully nail n=2 as a
standalone milestone.

**3. Strategy-stealing / logical shortcut from the already-proven upper bound — checked, does
NOT work.** One might hope the fact "XY can always force `e≤e_n` against ANY LB opening" (now
proved for n=2) logically implies "XY cannot force `e<e_n` against the specific dyadic opening"
— it does not: the upper bound is a *sufficiency* statement about the best of several XY
strategies over ALL openings; it says nothing about whether some (possibly different, cleverer)
XY strategy beats `e_n` specifically at the dyadic point. The two directions are logically
independent; no shortcut here. (I verified this is not just an oversight — the upper-bound
proof's own Case (i) closure literally shows `max` over Case (i) triples of a *sufficient-
strategy* value is exactly 1/7 at the dyadic point; this bounds the SUP from one side but says
nothing about the INF of the true game value at that one point.) **Not a viable route — flag as
checked-and-ruled-out so no future round wastes a cycle on it.**

**4. Convex/concave-min-of-affine-functions machinery (already used locally by
`elementary-exchange-smoothing`) extended globally.** Step C's certificate
(`λ=(2/7,1/7,4/7)`, 0 in strict interior of the gradient hull) proves LOCAL uniqueness of the
dyadic point as an LB-side maximizer, but that is the wrong direction for THIS lens: it treats
`(a_1,a_2)` (LB's choice) as the free variable with `f_1,f_2,f_3` as candidate XY strategies
already fixed. To get a genuine lower bound one would instead need to fix `(a_1,a_2,a_3)=
D_2` and treat **the cut positions** as the free variables, then show the piecewise-affine
`e(\text{cuts})` (concave, by the same finite-min-of-affine argument, PROVIDED the relevant
branch structure is enumerated) has NO point below `1/7` anywhere in the (now compact) cut
polytope — concavity alone doesn't give a floor (a concave function's min is at an extreme
point/boundary, i.e. right back to vertex enumeration, opening 2). So this machinery is a
*tool* for organizing opening 2's casework more efficiently (concavity within each combinatorial
branch cuts down how many interior points need checking — only the boundary/breakpoints of each
branch matter) rather than an independent route.

### Candidate technique(s)
Dominance/superincreasing-sequence lock-in (openings 1); Lemma P + vertex lemma reused in the
"maximize e via unopposed cuts" dual direction (opening 1, Branch A); finite vertex/tie
enumeration with concavity-assisted pruning (openings 2 & 4); strong induction on n proving
both directions jointly (meta-point under opening 1).

### Cheap-kill candidates
- **Dominance pruning (strong, already numerically confirmed below):** if XY's ≤n cuts never
  touch `a_1`, `e ≥ a_1 − (\text{max achievable } e_R(R))`, and a quick probe (below) shows this
  branch is nowhere close to the target (best found `e≈0.2857=2/7`, vs. target `1/7`) — so any
  proof attempt can immediately discard "XY leaves `a_1` alone" as a live threat and focus all
  casework on cuts that touch `a_1`, roughly halving the case space at every level of the
  recursion.
- No parity/pigeonhole cheap kill applies (this is a continuous optimization, not a discrete
  counting problem).

### Knowledge-base entries to use
- **"Piecewise-concavity smoothing"** (KB Algebra & Polynomials) — same abstract pattern
  (finite min/max of locally-affine pieces ⟹ piecewise concave/convex ⟹ extremum at a
  breakpoint) as the vertex lemma both siblings independently derived; can be cited directly as
  the general principle underlying the vertex lemma instead of re-deriving convexity facts from
  scratch.
- **General Proof Methods: Induction / strong induction** — for opening 1's joint two-direction
  induction on `n`.
- **Invariants & monovariants** — Lemma P is exactly this kind of invariant (already certified);
  opening 1's "dominance lock" is a rank-invariant in the same spirit.
- No entry in `knowledge_base.md` directly addresses two-player adversary-resistance
  ("this construction beats every reply") arguments — the crux corpus (below) is the better
  source for that pattern.

### Analogous past problems (cruxes)
- **`aimo-0117`** (combinatorics, `games-and-strategy`) — crux: "Assign the played values as a
  two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the
  sum of all the others," used to *lock* which "box" (here: which rank) the current largest
  value occupies regardless of the opponent's rearrangement of everything smaller. This is
  **structurally the same trick** as opening 1's dominance lemma, applied to a genuinely
  different game (stone-placement into two boxes) — strong analogy, directly adaptable in
  spirit (not the details) to lock `a_1`'s rank in `D_n`.
- **`aimo-0401`** (combinatorics, `invariants-and-monovariants`) — crux: "When each element
  dominates the sum of all smaller ones, replace a running cumulative-sum inequality with a
  single condition on the current top element," used on the exact same superincreasing sequence
  `2^0,…,2^{n-1}` to collapse a global balance-pan condition to a single local rank condition.
  **Best analogy found** — same numeric structure (`2^k` vs. `2^k−1`), directly transferable
  reasoning pattern (reduce a global ranking/ordering claim about a superincreasing sequence to
  a statement about the top element only).
- `aimo-0718` (combinatorics, `invariants-and-monovariants`) — less directly analogous (a
  majorization/reference-sequence argument bounding a growing multiset's spread against an
  adversary that can "block" `r` items per round); worth knowing as an example of "bound a
  greedy/adversarial process via a majorizing reference sequence" but the mechanics don't
  transfer cleanly to our continuous cutting game — mention only as a weaker secondary lead.

### Prior progress
`dyadic-cascade-induction` and `elementary-exchange-smoothing` both: (a) fully close the
**upper-bound** direction at n=2 (`c(2)≤4/7`, rigorous, gap-free — not this lens's concern), and
(b) explicitly leave the **lower-bound** direction at n=2 as open, backed only by a small
hand-picked candidate check (~15 patterns in `elementary-exchange-smoothing`, similar informal
check in `dyadic-cascade-induction`'s closing paragraph). Neither approach has attempted the
dominance/superincreasing structural fact (opening 1) — this is a genuinely new angle not
covered by either sibling's current content.

### Dead ends (do not retry)
- **Opening 3 (strategy-stealing from the proved upper bound)** — verified above to be a
  logical non-sequitur; the upper bound (sufficiency over all openings) does not constrain the
  true game value at one specific opening from below. Do not spend a round trying to derive the
  lower bound "for free" from the upper-bound proof.
- **Raw global numeric/symbolic search over all of Case (ii) for general `n`** — round-1's
  unbounded symbolic attempt on Case (ii) hung with no output (909+s, force-killed); the finite
  vertex-enumeration approach (opening 2) works only because n=2's piece count is small enough
  to enumerate by hand — don't retry unbounded symbolic search at higher n.

### Small-case / intuition notes (conjecture, numerically checked, not proof)
- Ran a **broader** randomized numeric check than prior rounds: 400,000 random samples across
  all four XY response-pattern families at n=2 (no cut, single cut, two cuts on the same piece
  = trisection, two cuts on two different pieces) applied to the exact dyadic input
  `(4/7,2/7,1/7)`. Global minimum found: `e ≈ 0.142857142857 = 1/7` (to float precision, matches
  target exactly) — **no sampled response beats `1/7`**, corroborating (but not proving) the
  lower-bound conjecture at n=2, on a materially larger and more systematic search than the
  ~15 hand-picked candidates used previously.
- Separately restricted the search to responses that **never cut `a_1`** (only `a_2,a_3` get
  XY's ≤2 cuts): best `e` found was `≈0.2857 = 2/7`, far above the `1/7` target — numerically
  confirming that "leave `a_1` alone" is a badly suboptimal branch for XY, exactly as opening
  1's dominance argument predicts. This is strong supporting evidence (conjecture, not proof)
  that the dominance-forced case split (`a_1` cut vs. untouched) is the right first move for a
  rigorous lower-bound proof, and that all the real difficulty is concentrated in the "`a_1` is
  cut" branch — consistent with all winning candidates found by both sibling approaches (f1,
  f2, f3 in `elementary-exchange-smoothing`) cutting `a_1`.
- The superincreasing property `2^k > 2^{k-1}+…+1` (hence `D_n`'s dominance chain) is an
  elementary algebraic fact, not merely conjectured — worth stating as a genuine (trivial)
  lemma in any approach that adopts opening 1.
