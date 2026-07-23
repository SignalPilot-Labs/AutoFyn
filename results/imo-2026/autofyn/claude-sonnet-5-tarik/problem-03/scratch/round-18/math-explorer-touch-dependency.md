## imo-2026-03 — Two-Touch KEEP `b_0<=w_1` dependency on Three-Touch: precise trace + a promising new sibling-domination angle for Three-Touch's MATCH branch

### Answering the dispatch's core question directly

**Two-Touch's KEEP branch `b_0<=w_1` genuinely needs an upper bound on `OPT_{-1}({b_0},rest)` valid
for the WHOLE quantity, at the SAME size `|rest|=|W|-1`** (§26.5(d)/§27.2(d)/§27.1's own notes already
establish this; re-traced and reconfirmed here). By the certified Generalized Multi-Background Peeling
Lemma (§13.2, an unconditional identity, not a conjecture), `OPT_{-1}(c,Z)=max(DELETE_val,KEEP_val,
MATCH_val)` **exactly**, for the SAME peeling of `Z`'s own current max. So a "just use DELETE/KEEP as
an upper bound, drop MATCH" argument is **not literally valid on its face** — `MATCH_val` could in
principle exceed `max(DELETE_val,KEEP_val)`, and if it ever does, `max(DELETE_val,KEEP_val)` under-
estimates the true `OPT_{-1}`, breaking soundness of any bound built from it. **So strictly speaking,
some fact about MATCH is unavoidably needed** — the real question (per the dispatch) is whether that
fact must be "MATCH_val `\le` `ThreeTouch`'s full 5-candidate closed form" (the file's current, still-
open target, §28.4(e)) or something narrower/easier.

**New finding this round: a narrower, much more robust-looking target exists and was NOT tried by any
prior round or by the parallel `match-branch` explorer's mirror attempt (see reconciliation below).**

### The new candidate: "MATCH is dominated by its own DELETE/KEEP siblings" (branch-value domination, not closed-form domination)

**Candidate Lemma (new, unproved, heavily corroborated).** For every background singleton `c\ge0`
and every sorted list `Z`, peeling `z_1:=\max(Z)` via the certified Peeling Lemma's `\sigma=-1` DELETE
/KEEP/MATCH trichotomy:
```
MATCH_val := max_j OPT_{-1}({c, |z_1-z_j|}, Z\{z_1,z_j})   \le   max(DELETE_val, KEEP_val)
```
where `DELETE_val:=OPT_{-1}(c,Z\{z_1})`, `KEEP_val:=OPT_{-1}(\{c,z_1\},Z\{z_1})` are the SAME two
sibling branch **true values** (not simplified closed-form candidates) that Three-Touch's induction
(§28.4(b)-(d)) has **already fully and unconditionally proved** `\le ThreeTouch(c,Z)` for every size.
**If this candidate lemma is proved, Three-Touch's MATCH branch (§28.4(e), the sole remaining open
piece) closes in 2 lines as a pure corollary of already-certified content** — `MATCH_val\le
max(DELETE_val,KEEP_val)\le ThreeTouch(c,Z)` — with **zero new candidate-matching case analysis**
against `ThreeTouch`'s 5 explicit candidate shapes (touch-1/2/3). This would fully close Three-Touch
(5/5), and per the already-established (round 17, reconfirmed non-circular) mutual induction, would
then fully close Two-Touch's KEEP `b_0\le w_1` sub-case at every size too — completing Two-Touch modulo
only Gap 1a's own MATCH-branch equivalent (Per-Partner Domination at general `q`, see the parallel
`match-branch` explorer's report — Two-Touch's own MATCH branch reduces to that, a *different* open
item from this one).

**Computational support (this round, exact `Fraction` arithmetic, brute-force `OPT_\sigma` over ALL
selections — not the conjectural closed form, so this is a fully rigorous computational check of the
TRUE branch values, no reliance on unproven machinery):**
- Random, `q\in\{2,\dots,8\}`, `v_{\max}\in\{4,\dots,25\}`: **`0/16{,}000`** combined across several
  batteries.
- Exhaustive small grids (`q\le4`, `v_{\max}<5`): **`0/720`**.
- Adversarial "engineered duplicate + big tail" (deliberately construct `z_1-z_j=c` exactly, forcing
  the Lemma-P cancellation `\{c,c\}\to\emptyset` the file's own §27.2(d) flags as the mechanism behind
  the closed-form's touch-3 candidate being load-bearing, then attach a large/spread residual tail to
  maximize `MATCH`'s potential upside): **`0/4{,}301`**.
- Duplicate-heavy (repeated/near-duplicate `Z` values, stress-testing chained Lemma-P cancellation):
  **`0/2{,}000`**.
- **Directly within Two-Touch's own genuine `b_0\le w_1` recursive-call scope** (generate `(b_0,W)`
  with `b_0\le w_1=\max(W)`, set `rest:=W\{w_1\}`, test the candidate lemma on `(b_0,rest)` exactly as
  the induction would invoke it — the most targeted test): **`0/4{,}000`**, AND (as a second, even more
  direct check) using `\max(DELETE_val,KEEP_val)` as a literal surrogate for the true `OPT_{-1}(b_0,
  rest)` and checking the FULL downstream target `w_1-\text{surrogate}\ge TwoTouch(\{b_0\},W)` still
  holds: **`0/4{,}000`** failures — i.e. the surrogate-based bound-only route, if the candidate lemma
  holds, closes the actual needed inequality end-to-end.
- **Total combined: `0` counterexamples across `\approx28{,}500` trials** (`/tmp/round-18/touch_dep/
  test1.py`–`test9.py`).

**Sharp asymmetry (new, worth flagging on its own).** The mirror check on the `\sigma=+1` (Two-Touch)
side — is `MATCH_val` (same peeling, minimization) ever the STRICT unique minimizer over `DELETE_val,
KEEP_val` (the true branch values, not candidates)? — **fails at a real rate**: `763/6{,}000` random,
`28/600` exhaustive (`q\le4,v_{\max}<5`). So sibling-domination is **asymmetric between the two signs**:
false (needed, and known-hard — this is exactly Two-Touch's own still-open MATCH piece) for `\sigma=
+1`, apparently always true (0 counterexamples found despite real adversarial effort) for `\sigma=-1`.
This is a **new, sharper form** of the touch-depth asymmetry the file already documents (Two-Touch
needs touch `\le2`, Three-Touch needs touch `\le3`) — it now appears at the branch-VALUE level too, not
just the candidate-count level.

**One naive proof route tried and REFUTED (record so it isn't re-attempted as "the" mechanism):**
"background-value monotonicity" (`OPT_{-1}(\{c,y\},X)` non-decreasing in `y`, for fixed `c,X`) is
**FALSE** — `486/3{,}000` (`\approx16\%`) failures (e.g. `c=13,X=[7,5,0]`: `y=2\to13`, `y=14\to8`,
value goes DOWN as `y` increases). So the obvious two-step chain ("KEEP's pool `X\cup\{z_j\}\supseteq`
MATCH's pool `X`" [Shrink-List Monotonicity, already certified] `+` "KEEP's background value `z_1\ge`
MATCH's background value `d=z_1-z_j`" [background-value monotonicity]) does **NOT** give a free proof —
the real mechanism (if the candidate lemma is true) must use the *specific* relationship `d=z_1-z_j`
together with the pool difference `\{z_j\}`, not a generic two-lemma composition. Flag this as the
honest state: **strongly corroborated, zero counterexamples despite real adversarial search, but no
proof route found yet — do not report as closed.**

**Reconciliation with the parallel `math-explorer-match-branch.md` report's "Secondary finding."** That
report tried what looks like the same idea (`\sigma=-1` "Mirror Per-Partner Domination", `A'_{3,l}\le
\max(A'_1,D'_l)`) and found it **FAILS** `7$-`15\%` of the time. The difference, and the reason this
round's version is not the same failed claim: that report's `D'_l:=|c-d_l|` is a **single scalar
candidate** (Three-Touch's own touch-1-style term), not the full recursive `KEEP_val`. `KEEP_val` (via
§13.2's Rank-Extraction formula, `h=0`: `u_1-OPT_{+1}(c,rest')`) is typically far larger/richer than
the bare scalar `|c-d_l|` — it is itself a whole optimized sub-problem's value. Swapping the weak scalar
proxy `D'_l` for the TRUE `KEEP_val` is exactly what turns the `7$-`15\%` failure rate into `0/28{,}500`
here. **This is a genuine refinement of that finding, not a duplicate of the already-failed idea** — the
other explorer's negative result and this one are consistent (their weaker claim is false; the version
using the true branch value survives).

### Answering the dispatch's remaining points

1. **Recursive call structure trace:** confirmed — Two-Touch's KEEP `b_0\le w_1` branch needs `w_1-
   OPT_{-1}(\{b_0\},rest)\ge TwoTouch(\{b_0\},W)`, i.e. an upper bound on `OPT_{-1}(\{b_0\},rest)`
   at size `|rest|=|W|-1` (one level down, matching round 17's already-established non-circular mutual
   induction — nothing new here, reconfirmed). Structurally this bound **must** account for all of
   `OPT_{-1}`'s value (`=max` of 3 branches, an identity) — you cannot literally ignore MATCH. But
   which FACT closes MATCH is open: the file's current target (`MATCH_val\le ThreeTouch`, closed form)
   vs. this round's new candidate (`MATCH_val\le\max(DELETE_val,KEEP_val)`, sibling values). Both would
   suffice; the new one is untried, structurally simpler (no candidate-shape casework), and much more
   robust computationally (`0/28{,}500$ vs. the file's own `0/4{,}475` for the closed-form target).

2. **Tested computationally whether DELETE/KEEP alone suffice:** YES as an *empirical bound* (never
   observed to fail, `0/28{,}500`, including instances specifically engineered to make MATCH's
   Lemma-P-cancellation trick attractive) — but this is a genuinely different, narrower, and so far
   UNPROVED claim from what's on file; it is not yet a closed sub-lemma, just a strong, previously-
   untested new corroborated conjecture. No instance was found where MATCH must be the strict
   maximizer (in sharp contrast to the `\sigma=+1$ mirror, where it strictly wins `\sim13\%` of random
   instances) — so at this experimental scale, "MATCH's contribution is load-bearing" for `\sigma=-1`
   appears FALSE, i.e. the DELETE/KEEP-only bound genuinely looks sufficient, not just approximately so.

3. **Bound-only route sketch, with verification counts:** stated precisely above as the "Candidate
   Lemma." If proved: `MATCH_val\le\max(DELETE_val,KEEP_val)` (`0/28{,}500`, see breakdown above) `\Rightarrow`
   `OPT_{-1}(c,Z)=\max(DELETE_val,KEEP_val)` exactly `\Rightarrow\le ThreeTouch(c,Z)` (already proved,
   §28.4(b)-(d)) `\Rightarrow` Three-Touch closes (5/5) `\Rightarrow` Two-Touch's KEEP `b_0\le w_1`
   branch closes (already-established mutual induction, round 17) `\Rightarrow` Two-Touch closes (5/5,
   modulo Per-Partner Domination's separate general-`q` gap, unaffected by this). **No proof written —
   this is scouting only**, per dispatch scope.

4. **Round-17 dead end** (letting `d` become optional instead of forced in Two-Touch's MATCH branch,
   `b_0=5,W=(8,10,8),w_j=8` counterexample) — noted, **not retested**, per instructions. Unrelated to
   this round's finding (that dead end concerned Two-Touch's own `\sigma=+1` MATCH branch directly, not
   Three-Touch's `\sigma=-1` sibling-domination angle explored here).

### Recommended next step for the outliner/builder

Attempt to PROVE the Candidate Lemma (`MATCH_val\le\max(DELETE_val,KEEP_val)` for `OPT_{-1}`'s own
peeling, `\sigma=-1`) directly — this is now the single most promising untried angle for finishing
Three-Touch (and hence Two-Touch's KEEP branch) found this round, strictly more tractable-looking than
bounding against the 5-candidate closed form (§28.4(e))'s existing framing. The ruled-out
"background-value monotonicity" route should NOT be the starting point; a real proof will need to use
the specific algebraic relationship `d=z_1-z_j` (not a generic `y`) together with the pool difference
`X` vs. `X\cup\{z_j\}` simultaneously — likely via a direct exchange/domination argument comparing a
MATCH witness against an explicit KEEP witness constructed from it (replace `d` by `z_1` in the
background, replace the "used-up" `z_j` back into the pool, then argue the resulting KEEP-side
selection dominates), rather than two separately-proved monotonicity lemmas.

### Dead ends / cautions for this angle specifically

- Do NOT use the "background-value monotonicity" lemma as a proof ingredient — refuted, `486/3{,}000`
  (`\approx16\%`).
- Do NOT confuse this new candidate with the already-tried-and-failed "Mirror Per-Partner Domination"
  (`match-branch` explorer's report) — that one used a weak scalar `D'_l` in place of the true
  `KEEP_val` and fails `7$-`15\%`; this round's version uses the TRUE branch value and has 0 failures
  so far. They look superficially similar but are different statements.
- This candidate lemma, even if proved, does **not** touch Two-Touch's own MATCH branch (Match-Branch
  Domination) — that is a separate item, already reduced by the parallel explorer this round to Gap
  1a's Per-Partner Domination Lemma (general `q`, still the standing top-priority gap).

### Summary table

| Piece | Status before this round | This round's finding |
|---|---|---|
| Three-Touch DELETE/KEEP (both parity) | fully proved | unchanged, reused as-is |
| Three-Touch MATCH | open, target = full closed-form domination (`0/4475` corroborated) | new NARROWER target found (`0/28,500` corroborated), untried before, no proof yet |
| Two-Touch KEEP `b_0\le w_1` | conditional on full Three-Touch | confirmed still needs full Three-Touch (all branches) at size `|W|-1`; the new narrower MATCH target, if closed, suffices |
| Two-Touch KEEP `b_0\le w_1` end-to-end via the new route | untested | `0/4,000` on the genuine recursive-call scope — the bound-only chain works empirically end-to-end |

### Small-case / intuition notes (all labeled conjecture — none of this is proved)

Conjectured: `OPT_{-1}`'s own top-level peeling trichotomy never needs its MATCH branch to strictly
beat its DELETE/KEEP siblings — intuitively because MATCH sacrifices the full value of the current max
`z_1` for a strictly smaller quantity `d=z_1-z_j\le z_1` (since all values are nonnegative — stick-piece
lengths), while KEEP retains `z_1` at full value; the maximizer's own recursive freedom inside KEEP's
sub-problem seems to already capture whatever Lemma-P cancellation benefit MATCH could offer, without
sacrificing `z_1`'s raw size. This is a heuristic, not a proof (the naive formalization of it via
background-value monotonicity is false), but it is consistent with the total absence of counterexamples
across a genuinely adversarial search (~28,500 trials, engineered duplicate-cancellation cases
included). The mirror asymmetry (`\sigma=+1$ MATCH strictly wins `\sim13\%$ of the time) is consistent
with the file's own existing diagnosis that duplicate cancellation only ever *helps* the minimizer,
never (net) the maximizer once the maximizer's own KEEP alternative is available — worth a future round
trying to state this heuristic as a clean lemma hypothesis (e.g. induction on `|X|` comparing MATCH's
optimal witness to an explicit KEEP-side witness built from it) rather than treating it as unexplained.
