# imo-2026-03 — round 11 scouting pass: viability of aimo-0043/aimo-0558 charging mechanisms
for the Match-Recovery Lemma, plus a new candidate reformulation

Scope: scouting only, per dispatch. All computation is exact-integer Python, small bounded
sizes (`q<=8` random, `q<=6` fully exhaustive over small integer ranges — no unbounded search).
Code lives in `/tmp/round-11/work/*.py` (self-contained, re-runnable: `defs.py`,
`insert_defs.py`, `general_defs.py`, `level2.py`, `charge_test*.py`,
`refined_conjecture*.py`, `exhaustive_refined.py`). All definitions (`OPT`, `NC`, `INSERT_OPT`,
`INSERT_NC`, `OPT_σ(B,Z)`, `TAGGED_σ(B,Z,s)`) were coded to match
`potential-weighting-upper-bound.md` §9.2/§11.1/§13.2 **exactly**, and cross-checked against
the file's own worked numbers before any new claim was tested (see §1).

## 1. Sanity checks against the file's own claims (all reproduced exactly)

- `INSERT_OPT(15,(89,73))=1`, `INSERT_NC(15,(89,73),s=1)=15` — reproduces the §11.5 `p=4`
  counterexample (`Y=(92,89,77,73)`, partner `j=3`) exactly.
- `OPT_{+1}({2,4},(6,3,2,1))=0`, `TAGGED_{+1}({2,4},(6,3,2,1),0)=1` — reproduces §13.6's
  minimal `|B|=2` counterexample exactly (crossing selection `MATCH(6,2),MATCH(3,1)` gives
  `e({4,4,2,2})=0`; every non-crossing alternative gives `≥1`).
- The Fixed-Support Uncrossing Conjecture's dead end (`current.md`'s dead-end list,
  `Y=(7,5,4,4,3,1),p=6,b=5`): independently reproduced. `OPT(Y,5)=NC(Y,5)=0` (so the
  *aggregate* fact is fine), but among the 30 selections achieving this optimum, several have a
  **crossing** matching (e.g. `K=∅,D={0,5},M={(1,3),(2,4)}`) whose same-support non-crossing
  re-pairing strictly increases the value (`0→2`) — confirms the conjecture's exact failure
  mode: the true recovery must come from a **different support** (here, other optimal selections
  in the same set already happen to be non-crossing, e.g. `K={2,3},D={0,1,4,5}`, no match at
  all), not a repair of the crossing one. This is existential-support, not positional, exactly as
  `current.md`'s dead-end note says.

## 2. The two cruxes, pulled precisely from the corpus (not the round-10 gloss)

**`aimo-0043`** (mine-avoiding lattice paths, prove `≥2^{n-|M|}` paths). Three cruxes on file;
the load-bearing one for this dispatch:
> "When one branch of a peeled first step is entirely unavailable, attribute a dedicated
> obstacle that must block it and delete that obstacle from the resource budget of the
> surviving branch's inductive subproblem." *How used:* inducting on `n`, splitting at
> `(1,0)`/`(0,1)`; if only one branch survives, some mine `(0,k)` must be *forced* to exist to
> block the dead branch; that mine is provably irrelevant to the surviving branch, so its
> induction runs with `|M|-1`, recovering exactly the lost factor of `2`.

**`aimo-0558`** (`±1`-sequence, gap-`≤2` subsequence, `C=506`). The achievability-direction
crux:
> "To lower-bound the achievable majority-minority excess under a bounded-gap selection, run a
> greedy that always takes majority elements and takes a minority element only when forced, then
> charge each forced minority inclusion to a distinct skipped minority element." Gives an
> injection {forced-includes} → {distinct skips}, capping the minority contribution at
> `⌊majority/2⌋` without ever solving per-position.

Both confirmed real, load-bearing, and precisely as the round-10 report glossed them — no
surprises in the full text.

## 3. Direct translation attempts — both are structurally blocked, precisely diagnosed

**aimo-0043's direct translation is exactly the already-dead route.** Its mechanism needs (a) a
clean two-branch split where (b) failure of one branch is *caused* by one identifiable object,
which (c) can be *removed from the surviving branch's own resource count* for free. In this
problem, the natural translation is: DELETE/KEEP branches (free, IH-safe, no crossing at all) vs.
MATCH branch (the one that can fail non-crossing); the "obstacle" would be the specific
crossing-arc element. But the surviving branch's own bookkeeping (per §13.2/§13.6) needs a
*flat background value*, not a discrete removable object — and growing that flat background
past size 1 is exactly what §13.6 proved FALSE (reproduced in §1 above). So the literal
translation is not a new idea, it's a restatement of the dead route. A genuinely working
version would need arc-interval-tagged background bookkeeping (the "richer bookkeeping" §13.6
itself flags as untried) — this is new machinery construction, not an adaptation, and out of
scope for a scouting pass.

**aimo-0558's direct translation has no natural target.** Its majority/minority block structure
requires a global 2-coloring with alternating same-sign runs; this problem's objects (sorted
positive reals, alternating-sign telescoping sum) have no natural "majority/minority" split —
the round-9 outline's own proposed translation ("majority block ~ NC-matched run,
minority block ~ elements between OPT's crossing partners") remains exactly as speculative as
before; I did not find a concrete instantiation worth recommending. **No progress on this
opening this round — still an untested hint, not a lead.**

## 4. What the failed direct translations point to instead — a sharper reformulation
(genuinely new this round, not on file, unproven, needs its own verification pass)

Re-deriving the induction algebra directly (not assuming the file's own framing) gives a cleaner
picture of *exactly* how little is actually needed, and reveals that aimo-0043's real idea — one
specific, always-available, budget-safe fallback absorbs the whole shortfall, no aggregation
needed — **can be surgically applied to the one place it's needed**, instead of to the whole
(dead) flat-background family.

**Setup.** By §13.2's own trichotomy on `Z`'s own top element `z1` (peeling one level inside
`INSERT_OPT`/`INSERT_NC`, background `|B|≤1`), write `D,K` for the DELETE/KEEP branch values
(both IH-safe: `D` recurses to the *same* family one size smaller, same `B`; `K` recurses via
the certified General Rank-Extraction closed form to the same family, `|B_lo|≤|B|≤1`, possibly
sign-flipped — **neither ever grows the background**), and `M_opt:=min_k` INSERT_OPT-of-Z's-own-
match, `M_tag:=min_k` INSERT_NC-of-Z's-own-match (the only branch needing `|B|=2`).

**Trivial half (needs no lemma at all).** If `M_opt ≥ min(D,K)`: `OPT=min(D,K,M_opt)=min(D,K)`,
and `TAGGED=min(D,K,M_tag)≤min(D,K)` (minimizing over *more* candidates only helps), so
`TAGGED≤OPT`; combined with the always-true `TAGGED≥OPT`, done. **No new content — this is
exactly why the DELETE/KEEP escape hatch in the existing Match-Recovery Lemma is "free."**

**The one remaining case.** If `M_opt < min(D,K)` (match strictly, uniquely wins): `OPT=M_opt`,
and closing the induction needs *exactly* `M_tag=M_opt` — this is the genuinely open content,
and it is **the same Match-Recovery Lemma already on file**, just applied one level down (`Z`'s
own peeling, not `Y`'s).

**New this round: a strictly *stronger*, more inclusive trigger condition, tested and NOT yet
refuted.**
```
Refined Delete-Recovery Conjecture (σ=+1/min side). For |B|≤1: whenever matching Z's own
top element z1 to its best unrestricted partner (M_opt) strictly beats simply DELETING z1
(D = OPT_{+1}(B, Z\{z1})) — a WEAKER, more easily-triggered hypothesis than "beats both D
and K" — the tagged/non-crossing match aggregate achieves the identical value: M_tag = M_opt.
```
Since `M_opt<D` is implied by (weaker than) `M_opt<min(D,K)`, this conjecture, if true, **is
sufficient** to close the one remaining case above (a strictly harder target subsumes it) —
but it is stated independent of `K`, which is why it stress-tests cleanly and separately.

**Computational status (this round, exact-integer, both random and exhaustive):**
- Random, `q∈{4,...,8}`, values up to `25`, `sign=+1` (min side): **7000+ trials, 0
  violations** (`refined_conjecture.py`: 4000 trials, 895 with the trigger active, 0
  violations; `charge_test.py`/`charge_test2.py`/`charge_test3.py`: ~7300 more trials via the
  slightly different but related "match-only aggregate mismatch" diagnostic — every one of the
  56 mismatches found is resolved by DELETE specifically, never KEEP, never neither).
- **Exhaustive** (not sampled) over ALL `Z` of a given size/value-range and all `v†`:
  `q=4,vmax=8`: 2640 instances, 450 with trigger active, **0 violations**. `q=5,vmax=6`: 1512
  instances, 159 triggered, **0 violations**. `q=6,vmax=5`: 1050 instances, 74 triggered, **0
  violations**.
- `sign=-1` (max companion, needed for the KEEP branch's flipped recursion): tested the natural
  analogous trigger (`M_opt > max(D,K)`, i.e. match strictly beats both branches for the max
  side) — **0 trigger events in 4000 random trials** (`q` up to 8) — suggesting the match branch
  may be *entirely vacuous* for the max companion (keeping `z1` at full magnitude structurally
  dominates any matched-difference for maximizing an alternating sum) — a clean, easy-looking,
  **separate** structural fact worth a cheap dedicated check next round, not yet attempted here.
- `|B|=0` (needed for the top-level KEEP branch's own recursion): tested the same trigger with
  no background element at all — **0 trigger events in 3000 random trials** — i.e., without any
  external background, deleting `z1` is *never* beaten by matching it to anything. Also directly
  re-confirmed plain `OPT(Z)=NC(Z)` (no background) on 1000 fresh random trials, 0 mismatches.

**Why this is a genuinely different (and not yet dead) target, not a restatement of the
refuted claim.** Round 9's own negative result refuted the *unconditioned* claim
"`min_k A_{3,k}=min_k B_{3,k}` always" (no D/K condition at all) — `3/500` counterexamples on
file. This round's conjecture is explicitly **conditioned** on `M_opt<D` — every match-only
mismatch this round's testing found (56 instances) satisfies `M_opt≥D` (i.e. is *exactly* the
kind of instance round 9's unconditioned counterexamples plausibly are: cases where the
unconditioned claim fails but harmlessly, because DELETE already dominates and rescues the
aggregate regardless). The conditioned form has not been tested by any prior round and has
**zero known counterexamples** after this round's combined ~10,000+ trials (random + exhaustive).

**Honest scope — this is NOT a proof, and is new/unverified.** (1) Sizes tested are still small
(`q≤8` random, `q≤6` exhaustive) — the known `|B|=2` counterexample only needed `q=4`, so this is
not vacuously easy, but larger `q` is untested here due to the combinatorial cost of
`all_Z_selections` (grows roughly like `(2q)!!`). (2) No proof mechanism was attempted — pinning
down *why* `M_opt<D ⟹ M_tag=M_opt` (e.g. via Fact 3/General Rank-Extraction Identity, or via a
direct argument on which specific `k` recovers) is exactly the next round's task, not done here.
(3) The `σ=-1`/`|B|=0` "match branch is vacuous" observations are suggestive, not verified beyond
random sampling — worth a cheap exhaustive check before relying on them.

## 5. Verdict on the two dispatched cruxes

- **`aimo-0043` (obstacle-charging): not directly viable as dispatched** — its literal
  translation reproduces the already-refuted flat-background route (§3). **But its underlying
  idea — a single, specific, always-IH-safe fallback branch absorbs the shortfall, no
  existential aggregation needed — is real and actionable when applied surgically**: §4's
  Refined Delete-Recovery Conjecture is precisely this move, scoped to the *one* place
  (`Z`'s own top-element peeling inside the already-necessary `|B|≤1` recursion) where it can be
  stated without needing the dead general `|B|≥2` machinery. This is the actual payoff of the
  aimo-0043 lens this round — not a direct adaptation, but a redirection of its core mechanism
  to a narrower, not-yet-refuted target.
- **`aimo-0558` (greedy + injective charge): no viable translation found this round.** Remains
  exactly as speculative as the round-9/10 notes describe; no concrete instantiation surfaced.
  Do not spend a dedicated round translating it further unless a concrete majority/minority
  analog is found first — flag as low-priority relative to §4's lead.

## 6. Recommendation for the outliner

Put up (or revise) an approach targeting **the Refined Delete-Recovery Conjecture of §4**
specifically (not the general `|B|≥2` family, which stays dead per §13.6/round 10) as the next
build target:
1. First, a cheap dedicated verification pass: push the exhaustive check to `q=7` if
   computationally feasible, and specifically construct adversarial instances shaped like the
   known `|B|=2` counterexample (`B={2,4},Z=(6,3,2,1)`) but with `|B|=1` background, to actively
   hunt for a counterexample before investing in a proof attempt.
2. If it survives, attempt a proof via the certified General Rank-Extraction Identity /Fact 3 —
   the conjecture's shape (a one-directional "if match beats the simplest fallback, it's already
   achievable non-crossing too") is a strictly narrower, better-scoped target than the
   Match-Recovery Lemma as previously stated, and — critically — its proof, if found, closes
   FSI(1)/FSI(0) by the clean two-case induction in §4, which in turn closes the **entire**
   remaining upper-bound gap (every `m`, every `n`, via the already-certified chain-prefix+tail
   reduction and Slack Collapse) — this is not a partial result if it lands.
3. Separately (cheap, low-risk): verify whether the match branch is provably *always* dominated
   by KEEP for the `σ=-1` (max) companion and by DELETE for `|B|=0` (§4's two "0 trigger events"
   findings) — if provable, these simplify the induction further (fewer live cases) at low cost.

## 7. Dead ends reconfirmed this round (do not re-attempt)

- Flat-background generalized Full-Slack Insertion Lemma / Match-Recovery Lemma at `|B|≥2` —
  independently re-reproduced FALSE (§1), matching round 10's finding exactly.
- Fixed-Support Uncrossing Conjecture — independently re-reproduced FALSE (§1), confirmed the
  failure is existential-support, not positional (matches `current.md`'s dead-end diagnosis).
- Direct literal translation of `aimo-0043`'s mechanism (flat single-object charge) — collapses
  to the already-dead route; a working version needs arc-history bookkeeping, not attempted.
- `aimo-0558` direct translation — still no viable target found (unchanged from round 9/10).
