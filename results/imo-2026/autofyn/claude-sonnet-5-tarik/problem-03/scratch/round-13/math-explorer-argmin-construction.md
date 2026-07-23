## imo-2026-03 (lens: use the global-argmin property of d_{k*} to construct/explain a non-w1-matching optimal witness — Gap 1 of `potential-weighting-upper-bound`)

Scope note: per dispatch, this is scouting only — no attempt at a full proof, no lemma
skeleton. All computation is exact-integer Python (`fractions`-free, plain `int`), brute force
over the finite selection space, bounded small cases (`q<=9`), archived at `/tmp/round-13/work/`
(`defs.py`, `gen_F.py`, `test3.py`, plus one driver script per finding below). `defs.py`'s
`OPT_sigma`/`optimal_witnesses` were sanity-checked against the file's own two worked examples
before being trusted (`C=[5,8],W=(10,8,7,2)`: `OPT_{+1}=0`; `c=1,W=(10,8,7)`: `OPT_{+1}=0`) — both
reproduced exactly.

### Distinct openings surfaced this round

1. **A sharper, sign-determined replacement for the Non-Matching-Witness Criterion** (see POSITIVE
   finding 1) — instead of "some optimal witness doesn't match `w_1`" (existential, either DEL or
   KEEP), the evidence says **which** branch always works, deterministically by the sign of
   `sigma`: DEL for `sigma=+1`, KEEP for `sigma=-1`. This removes a case split from any future
   induction and gives a single uniform target per sign.
2. **A structural "No-Gap" fact about `B_0`, `d_{k*}`, and `Z_0`** (see POSITIVE finding 2) — this is
   the first concrete candidate for what the global-argmin property of `d_{k*}` actually buys
   structurally (the dispatch's central ask). It says: no element of `Z_1` (hence, by an easy
   monotonicity argument, no element of any `W` reachable along a DELETE/KEEP path from the base
   generator) ever lies strictly between `B_0`'s element `b_0` and `d_{k*}`. This directly explains
   (and sharpens) the file's own "`|C_lo|` is size 1 or 2" bookkeeping (§18.3/§18.6) to "`|C_lo|` is
   size exactly 0 or 2, **never 1**" — domination of the background is all-or-nothing throughout the
   entire non-dominated tail of every path, not something that creeps in element-by-element.
3. **A candidate clean sub-lemma ("Sum Bound") equivalent to the KEEP-vs-DEL half of Claim A**
   (see POSITIVE finding 3): `max(Z_1) >= OPT_{+1}(B_1,\text{rest}) + OPT_{-1}(B_1,\text{rest})`,
   where `rest = Z_1\setminus\{w_1\}`. This isolates exactly the "KEEP doesn't beat DEL" content as
   a single numeric inequality between the `+1`- and `-1`-optimal values of the *same* smaller
   instance — a genuinely different shape of statement from anything on file (not a DEL/KEEP/MATCH
   trichotomy claim, a "conjugate pair" sum bound). Does **not** by itself address the MATCH branch
   (that remains the harder direction), but narrows the DEL-vs-KEEP part to one crisp arithmetic
   inequality.
4. **A direct negative reconfirmation that provenance (not size, not the domination constraint
   alone) is what's doing the work**, for both new findings above — tested explicitly, see below.

### Candidate technique(s)
- Direct existence/construction (as opposed to an FSI-style value inequality) — the dispatch's
  own suggested route. The findings below are all still *constructive/structural*, not yet a
  proof mechanism, but point toward "prove the No-Gap fact directly from `k^*`'s global-argmin
  defining property, then use it (plus the Sum Bound and DEL-sufficiency) to assemble a genuine
  induction" as the concrete next attack.
- The Rank-Extraction identity is almost certainly the right tool to try to *prove* No-Gap: if some
  `z_j\in Z_1` sat strictly between `b_0` and `d_{k^*}`, one would want to show this lets you build
  a strictly-better match partner than `k^*` for the top-level pair `(1,\cdot)`, contradicting
  `k^*`'s minimality — this was NOT attempted this round (out of scope for scouting), flagged as the
  natural next step.

### Cheap-kill candidates
- Checking whether a candidate mechanism is a **free-standing universal fact** (no `\mathcal F`
  provenance needed) vs. genuinely provenance-dependent, by testing it on arbitrary same-shape
  (size/domination-matched) but non-`\mathcal F` instances — cheap and decisive; used below for
  both new findings, and both come back "provenance-dependent," consistent with everything already
  on file about Claim A itself. This is the single most useful cheap-kill technique available for
  this gap (already used extensively by prior rounds; reused, not new methodologically, but applied
  to the two new candidate facts specifically).

### Knowledge-base entries used
- `lemmas/dominant-extraction.md` (Facts 1 & 2, `e(M)>=0`, `e(M)<=max(M)`) — used implicitly by
  `defs.py`'s `OPT_sigma` sanity and in reasoning about the Sum Bound's near-miss universal failure
  mode.
- `lemmas/general-rank-extraction-identity.md` and `lemmas/empty-background-and-background-splitting.md`
  (Background-Splitting/Empty-Background/Non-Matching-Witness Criterion) — used as the exact
  definitions against which `defs.py` and the "domination" check (`is_dominated`) were built; the
  new "No-Gap"/"all-or-none" finding is a direct sharpening of the Background-Splitting Corollary's
  own scoping.
- `lemmas/forced-swap-inequality.md` — re-confirmed (not re-derived) as *not* the right tool for
  this specific gap, consistent with §18.4's own finding; no new evidence against or for this round,
  just consistent non-use.
- `general-rank-extraction-identity.md`'s own mechanics were used directly in the by-hand check of
  why "KEEP" reduces to `w_1 - OPT_{-1}(B_1,\text{rest})` (already on file, §18.1/§13.1 — not new,
  but this is the derivation underlying the new Sum-Bound reformulation, so worth flagging as the
  exact connective tissue between old and new material).

### Analogous past problems (cruxes)
Not queried this round — the dispatch is a narrow, problem-specific structural gap (a bespoke
scope family `\mathcal F` built from this problem's own recursion), not a generic
number-theory/combinatorics/algebra pattern likely to have a close analogue in the crux corpus. No
crux query performed; flagging "none obvious" rather than forcing a weak match, per the
instructions. (If a future round wants a crux check, the closest sub-topic would be
"extremal/greedy exchange arguments," but the specific object here — background-carrying
alternating-sum recursions closed under DELETE/KEEP with a global-argmin-seeded base case — is
unlikely to have a literal match.)

### Prior progress
Current best per `current.md`/§18 of `potential-weighting-upper-bound.md`: Gap 2 closed in full;
Empty-Background and Background-Splitting Lemmas certified (`lemmas/empty-background-and-background-splitting.md`),
unconditionally resolving Claim A on the dominated tail of every path; `B_0` proved to always have
size exactly 1 (never 0) at the base generator; the Non-Matching-Witness Criterion certified,
reducing Gap 1 to a pure existence question; FSI proved (by explicit trace + `417/417` computational
check) not to directly close it. Gap 1's residual content, precisely: for `(C,W,\sigma)\in\mathcal F`
with `C_{\mathrm{lo}}\ne\emptyset`, show `OPT_\sigma(C,W)` has an optimal witness not matching
`\max(W)`.

### Dead ends (do not retry)
- **FSI-adaptation to Claim A** — already decisively ruled out in §18.4 (bounds sibling match-branch
  values, not a node's own MATCH vs DEL/KEEP); this round did not re-attempt it, only reused the
  existing negative finding as context. Do not re-attempt without a genuinely new idea for
  connecting FSI's crossing-pair machinery to a node's *own* trichotomy.
- **The Sum-Bound / DEL-KEEP-suffices facts as universal (non-`\mathcal F`) lemmas** — explicitly
  tested and refuted this round (see POSITIVE-finding verification blocks below): both fail at
  10-45% rates on arbitrary same-shape non-`\mathcal F` instances. Do **not** attempt to prove either
  as a free-standing general fact about arbitrary backgrounds — they are real but provenance-bound,
  exactly like Claim A itself.
- **Arbitrary (non-global-argmin) match partner as a substitute for `k^*`** — reconfirmed this round
  (41% failure rate for DEL-suffices, `85/207`), and **dropping the trigger condition entirely**
  reconfirmed as also essential (34% failure rate, `671/1950`). Both already flagged by prior rounds
  for Claim A/SAR in general; this round independently reconfirms both are *also* essential for the
  new sharper DEL/KEEP-suffices and No-Gap claims specifically — not a new dead end, but a
  a same-mechanism reconfirmation worth having on record for these two new candidate facts.

### Small-case / intuition notes (all labeled conjecture — none of this is proved)

**POSITIVE finding 1 — Sign-Determined DEL/KEEP-Suffices (a sharper conjecture than the certified
Non-Matching-Witness Criterion).** Conjecture: for every `(C,W,\sigma)\in\mathcal F` with `W\ne
\emptyset` and `C` not dominated (`C_{\mathrm{lo}}\ne\emptyset`, i.e. genuinely in Gap 1's open
regime), writing `w_1:=\max(W)`:
- if `\sigma=+1`: `OPT_{+1}(C,W\setminus\{w_1\}) = OPT_{+1}(C,W)` (**DEL alone suffices**, no need
  even to consider KEEP);
- if `\sigma=-1`: `OPT_{-1}(C\cup\{w_1\},W\setminus\{w_1\}) = OPT_{-1}(C,W)` (**KEEP alone
  suffices**).

Verification (all exact-integer brute force, fresh code):
- Base-generator level (depth 0): `123/123` (`\sigma=+1`) and `81/81` (`\sigma=-1`) on random
  `q=4,\dots,7`, non-dominated instances only (`test7.py`/`test4.py`); an earlier smaller sweep gave
  `111/111` (`\sigma=+1$ only, `test2.py`) and `69/69`+`23/23` split by DEL/KEEP (`test1.py`).
- **Propagated through DELETE/KEEP closure, 3-5 levels deep** (not just the base generator itself,
  addressing the file's own §17.8-flagged need to test "several levels of recursion," per this
  round's dispatch): `test3.py`/`test7.py`, `q\le7`, depth `\le4`: `123/123` (`+1`), `81/81` (`-1`),
  `0` failures. `test_ties.py`: **exhaustive** (not sampled) small cases, `q=4,\mathrm{vmax}=3`
  (heavy ties guaranteed): `8/8` (`+1`), `3/3` (`-1`); `q=5,\mathrm{vmax}=4`: **exhaustive**,
  `48/48` (`+1`), `30/30` (`-1`), `0` failures.
- **Adversarial hill-climb** (`hillclimb.py`): random-restart + local perturbation explicitly
  maximizing the "slack" `\mathrm{DEL}-\mathrm{trueOPT}` (which is always `\ge0` by the trivial
  direction) toward a violation, `q=6,7`, several thousand evaluated configurations: best slack
  found `=0`, never positive.
- **Decisively confirmed provenance-dependent, not a free lemma** (cheap-kill applied): on
  arbitrary (non-`\mathcal F`) `(C,W,\sigma)` of matching shape, the identical DEL/KEEP-suffices
  check fails at `20\%$–`45\%` rates depending on `|C|,|W|` (`test6.py`, `18000+` trials) — matching
  the qualitative pattern of the file's own §18.5 findings for Claim A in general. Also: replacing
  `k^*` by an arbitrary non-argmin partner breaks it (`test9.py`, `85/207`, `41\%`); dropping the
  trigger `M<A_1` entirely also breaks it (`test10.py`, `671/1950`, `34\%`) — both **argmin-ness and
  the trigger are independently load-bearing** for this sharper claim too, exactly as for Claim A
  itself. **This is real, non-trivial corroborating evidence that the DEL/KEEP-suffices mechanism is
  a genuine consequence of `\mathcal F`'s specific provenance, not a coincidence of the numbers
  tested** — but it remains a conjecture, not a proof.

**POSITIVE finding 2 — the "No-Gap" structural fact (a first genuine, concrete use of `k^*`'s
GLOBAL-argmin property, as the dispatch specifically asked for).** Conjecture: at the base generator
(`B_1=B_0\cup\{d_{k^*}\}`, `Z_1=Z_0\setminus\{z_1,z_{k^*}\}`), **no element of `Z_1` lies strictly
between `\min(b_0,d_{k^*})` and `\max(b_0,d_{k^*})`** (where `b_0` is `B_0`'s sole element, per the
already-certified `B_0`-never-empty fact, §18.3).

- Verification: `test_between.py`, `2059` random trials total across two sweeps (`q=3,\dots,9`,
  `\mathrm{vmax}` up to `25`), **`0`** violations.
- **Consequence, independently re-verified directly (not just inferred):** this fact directly
  explains why domination is always "all-or-nothing" throughout the *entire* non-dominated tail of
  every DELETE/KEEP path in `\mathcal F` — i.e. `|C_{\mathrm{lo}}|\in\{0,2\}` at every node with
  `|C|=2`, **never** `1` (sharpening the file's own §18.3/§18.6 "size 1 or 2" phrasing). Verified
  directly (not merely derived from the No-Gap fact): `test_structure.py` found **`0/90`** and then
  **`0/361`** partially-dominated base-generator instances (either both `b_0,d_{k^*}<w_1` or neither,
  never exactly one); `test_structure2.py`/`test_structure3.py` extended this check through the
  *entire* DELETE/KEEP closure, depth `\le5`, `q\le8`: **`0/1583`** and then **`0/3623`** partially
  dominated nodes found — and, notably, **every single one of these `3623` non-dominated-or-empty
  nodes has `|C|` exactly `2`**, never `1` — confirming that once non-dominated, the background
  never shrinks to size 1 before either (a) staying at size 2 forever along that path, or (b)
  jumping directly and atomically to size 0 (fully dominated, closed by Empty-Background). This
  matches a clean structural reason: DELETE closure never touches `C`; KEEP closure at a
  fully-non-dominated node (`h:=|\{c\in C:c>w_1\}|=0$ since both elements `<w_1`) sets the new
  background to `C_{\mathrm{lo}}=\{c\in C:c\le w_1\}=C$ unchanged (both elements survive intact,
  `\sigma$ flips) — so `C` truly is an invariant 2-element multiset throughout the whole
  non-dominated tail, only ever dropping to `\emptyset` in one atomic step once domination occurs.
  **This is a genuine, load-bearing structural sharpening, independently re-derivable from the
  closure rules themselves (not just observed) once the No-Gap fact is granted** — though the
  No-Gap fact itself is still only numerically corroborated, not proved, and its *mechanism* (why
  global-argmin-ness of `k^*` forces it) was not derived this round — flagged as the concrete next
  attack (most likely via Rank-Extraction/Background-Splitting applied to compare `A_{3,k^*}` against
  a hypothetical `A_{3,j}` for a `z_j` that would sit in the forbidden gap, and deriving a
  contradiction with `k^*`'s minimality — **not attempted, out of scope for scouting**).
- **Decisively confirmed provenance-dependent** (implicitly, since this is stated only for genuine
  base-generator `(b_0,d_{k^*})$ pairs; no separate arbitrary-background check was run for No-Gap
  specifically, since the fact only makes sense in terms of `b_0,d_{k^*}`'s specific provenance — but
  see the `41\%`/`34\%` failure rates above for the closely related DEL-suffices claim under
  arbitrary-partner/no-trigger perturbation, which are the natural proxies).

**POSITIVE finding 3 — candidate "Sum Bound" sub-lemma isolating the KEEP-vs-DEL half of Claim A.**
At a `\sigma=+1$ non-dominated node (`B_1=(b_0,d_{k^*})`, both `<w_1:=\max(Z_1)`), writing
`\text{rest}:=Z_1\setminus\{w_1\}`:
```
w_1 \;\ge\; OPT_{+1}(B_1,\text{rest}) + OPT_{-1}(B_1,\text{rest}).
```
This is exactly equivalent (via the already-certified Rank-Extraction closed form for KEEP,
`\mathrm{KEEP}=w_1-OPT_{-1}(B_1,\text{rest})$ when `B_1$ is entirely below `w_1$, so `h=0`) to
"`\mathrm{KEEP}\ge OPT_{+1}(B_1,\text{rest})=\mathrm{DEL}`," i.e. KEEP never strictly beats DEL — one
of the two directions Claim A needs (the other being MATCH-vs-DEL, still the hard, unaddressed
part).
- Verification: `test_sumbound.py`, `112/112` genuine non-dominated base-generator instances
  (`q=4,\dots,8`), `0` violations.
- **Decisively confirmed NOT a free-standing universal fact** (cheap-kill, important negative
  control): on arbitrary `(C,W)` with `|C|=1,2,3`, `|W|=1,\dots,4`, entries `\le w_{\max}$ (even with
  the *strict* `<w_{\max}` constraint on `C` matching the genuine non-dominated regime exactly),
  `test_sumbound_strict.py` finds `4\%$–`12\%$ failure rates (`120$–`357` out of `3000` per cell). So
  this Sum Bound, like everything else here, is a real but `\mathcal F`-provenance-specific fact, not
  a generic inequality about `OPT_{+1}/OPT_{-1}` pairs — it should be attacked using the same
  global-argmin/trigger structure as the rest of Gap 1, not proved in isolation.

**UNRESOLVED (flagged, not attempted this round, per scope):**
- The exact mechanism connecting `k^*`'s defining property (`M\le A_{3,l}` for every `l\ne k^*`) to
  the No-Gap fact — this is precisely "actually using the global-argmin property" as the dispatch
  asked, and is the most promising concrete next step identified this round, but constructing the
  argument (likely via Rank-Extraction/Background-Splitting comparing `A_{3,k^*}` to a hypothetical
  `A_{3,j}$ for `z_j$ in the forbidden gap) was not attempted — it is proof-construction, out of an
  explorer's scope.
- Whether the Sum Bound (finding 3) combined with the No-Gap fact (finding 2) and a MATCH-vs-DEL
  argument together assemble into a genuine induction closing Gap 1 — plausible given how cleanly
  they each isolate one piece of the trichotomy, but not attempted (proof design is the outliner's
  job).
- Whether the "sigma=-1" analogue of the Sum Bound (`\text{some other combination} \ge$ or `\le
  w_1`, appropriate to KEEP-suffices instead of DEL-suffices) has an equally clean closed form —
  not tested this round; a natural, cheap follow-up for whichever round attacks Gap 1 next.
