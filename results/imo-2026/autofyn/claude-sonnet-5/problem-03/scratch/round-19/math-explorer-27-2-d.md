## imo-2026-03

### Scope of this report
Dispatched to scout (and attempt, since the scope is small/bounded) a proof of §27.2(d)/§30's target
inequality — the KEEP-branch `b0<=w1` sub-case of Two-Touch at `|W|=3` (equivalently `|rest|=2`) — the
exact gap the round-18 proof-reviewer flagged as an overclaim in
`lemmas/match-branch-domination-via-per-partner-domination.md`'s "Scope note". **Result: I found and
verified (numerically exhaustive/random, plus hand algebra) a complete, elementary case-split proof of
this exact target at `|rest|=2`. This is new content beyond anything on file — previously "corroborated
`0/1,239`+`0/14,000`, not proved"; I did the actual case-bash and it closes cleanly.** Reported below at
full precision so the outliner/builder can formalize and independently re-verify it. This is a proof
attempt, not a certified result — needs independent re-derivation before being written into the approach
file or a lemma file, per the project's rigor rules.

### Precise target (restated from the lemma file's own notation, `results/imo-2026-03/lemmas/match-branch-domination-via-per-partner-domination.md`)

Fix `b0>=0`, sorted `W=(w1>=w2>=w3)`, `rest=(w2,w3)`, and the KEEP `h=0` hypothesis `b0<=w1`. Using:
```
TwoTouch(b0,W)      := min( e({b0}), min_w e({b0,w}), min_{i<j} e({b0,|wi-wj|}) )        [7 terms at |W|=3]
ThreeTouch(b0,rest)  := max( e({b0}), max_w e({b0,w}), max e({b0,|w2-w3|}), e({b0,w2,w3}) )  [5 terms at |rest|=2,
                                                                                                no touch-3 term exists at size 2]
```
(`ThreeTouch` is exactly Lemma B's certified closed form, `lemmas/max-element-triple-identity-and-threetouch-basecase.md`,
specialized to `|rest|=2`, where it is UNCONDITIONALLY proved equal to the true `OPT_{-1}({b0},rest)`.)

**Target:**
```
w1 - ThreeTouch(b0, rest)  >=  TwoTouch(b0, W)          (*)
```

### The reduction that makes this tractable (key structural observation, not previously used explicitly for this target)

`ThreeTouch(b0,rest) = max(A1,...,A5)` for 5 explicit terms `Ai`. Since `w1 - max_i(Ai) = min_i(w1-Ai)`,
target (*) is **equivalent** to: `min_i(w1-Ai) >= TwoTouch(b0,W)`, which holds **iff each of the 5
individual per-term inequalities `w1 - Ai >= TwoTouch(b0,W)` holds separately** (min of quantities each
`>=Y` is itself `>=Y`; conversely if the min is `>=Y` then trivially each term is, since each term `>=min`).
So (*) reduces to 5 independent finite sub-claims — each provable by exhibiting an explicit witness
`Bj` (one of `TwoTouch`'s own 7 candidate terms) with `w1-Ai >= Bj` (then `Bj >= min_k(Bk) = TwoTouch(b0,W)`
closes that term). **This is exactly the per-term-domination proof shape that already closed 3/5 of both
Two-Touch's and Three-Touch's own general-induction pieces (§26.5(c)/(d), §28.4(c)/(d))** — I verified
computationally first (0/20,000 failures for each of the 5 per-term claims individually, `/tmp/check1.py`)
before working out the witnesses by hand.

### The 5 per-term proofs (all elementary, all hand-verified + computationally corroborated)

Write `A1=e({b0})=b0`, `A2=e({b0,w2})=|b0-w2|`, `A3=e({b0,w3})=|b0-w3|`, `A4=e({b0,w2-w3})=|b0-(w2-w3)|`
(note `w2>=w3` so `|w2-w3|=w2-w3`), `A5=e({b0,w2,w3})` (keep-all-three, sorted-descending alternating
sum). `TwoTouch`'s 7 candidates: `B1=b0`, `B2=w1-b0` (using `b0<=w1`), `B3=|b0-w2|`, `B4=|b0-w3|`,
`B5=|b0-(w1-w2)|`, `B6=|b0-(w1-w3)|`, `B7=|b0-(w2-w3)|`.

1. **`A1` (delete-all): exact identity, no case split.** `w1-A1 = w1-b0 = B2` exactly (since `b0<=w1`
   makes `w1` the max of `{b0,w1}`). So `w1-A1=B2>=TwoTouch(b0,W)` trivially (`B2` is literally one
   candidate, so the min is `<=B2`). Mirrors the already-proved "delete-branch = exact candidate" pattern
   used throughout the file.

2. **`A2,A3` (keep-one): via one new general lemma.** New elementary fact, call it the
   **Two-Variable Reflection Bound**: *for any `0<=b0<=w1` and `0<=w<=w1`*, `w1-|b0-w| >= |b0-(w1-w)|`.
   **Proof (3-case split on `b0` vs `w`, then `b0` vs `w1-w`):**
   - `b0<=w`: LHS `=w1-w+b0=(w1-w)+b0`. Since `w1-w>=0,b0>=0`, sum `>=` their absolute difference
     `=|b0-(w1-w)|=RHS`. Done (elementary: `p+q>=|p-q|` for `p,q>=0`).
   - `b0>w`, `b0<=w1-w`: LHS `=w1-(b0-w)=w1-b0+w`. RHS `=(w1-w)-b0`. LHS-RHS `=2w>=0`. Done.
   - `b0>w`, `b0>w1-w`: LHS as above. RHS `=b0-(w1-w)`. LHS-RHS `=2(w1-b0)>=0` (using `b0<=w1`). Done.
   Applying with `w:=w2` gives `w1-A2>=B5`; with `w:=w3` gives `w1-A3>=B6`. Both `B5,B6` are genuine
   `TwoTouch` candidates, so `>=TwoTouch(b0,W)` follows. **Exhaustively verified**, `0/2,870` (integer
   grid `w1<=19`) and `0/30,000` random (`vmax=40`), `/tmp/check3.py`. (Geometric remark: `w1-|b0-w|` is
   exactly `e(\{w1,b0,w\})` by Lemma A since `w1=max(w1,b0,w)` — so this lemma says a specific
   "keep-`b0`-and-`w`, background `w1`" value dominates the "match `b0` against `w1-w`" value; it is
   *not* literally an instance of the already-certified Three-Bound Domination Lemma, distinct statement,
   distinct proof, but same flavor/toolset.)

3. **`A4` (match `w2,w3`): 2-region case split, both trivial once split.**
   - **Region `b0>=w2`:** then `b0>=w2>=w2-w3>=0`, so `A4=b0-w2+w3<=b0=A1` (using `w2>=w3`). Hence
     `w1-A4>=w1-A1=B2>=TwoTouch(b0,W)`. (In fact `A4<=A1` in this whole region, so `ThreeTouch=A1=b0`
     here exactly — a clean sub-characterization.)
   - **Region `b0<w2`:** claim `w1-A4>=B4=|b0-w3|`. Sub-split on `b0` vs `w3`:
     - `w3<=b0<w2`: `A4`'s sign depends on `b0` vs `w2-w3`; both signs reduce to `w1+w2>=2b0` (true since
       `b0<w2<=w1` gives `2b0<2w2<=w1+w2`) or `w1+2w3>=w2` (true since `w1>=w2`, `w3>=0`).
     - `b0<w3`: similarly both signs reduce to `w1+w2>=2w3` (true, `w1>=w2>=w3` so `w1+w2>=2w3`) or
       `w1+2b0>=w2` (true, `w1>=w2`, `b0>=0`).
   `0/50,000` random + region-targeted sweeps confirm `B2`/`B4` as valid case-split witnesses exactly as
   above, `/tmp/check5.py`, `/tmp/check6.py`.

4. **`A5` (keep-all-three): identical case split and witnesses as `A4`.**
   - `b0>=w2`: sorted order `(b0,w2,w3)`, `A5=b0-w2+w3=A4` in this region — same proof as term 3,
     `w1-A5>=B2`.
   - `b0<w2`, `b0>=w3`: sorted order `(w2,b0,w3)`, `A5=w2-b0+w3`. `w1-A5=w1-w2+b0-w3`. Target `B4=b0-w3`
     (since `b0>=w3` here). `w1-A5-B4=w1-w2>=0`. Trivial.
   - `b0<w3`: sorted order `(w2,w3,b0)`, `A5=w2-w3+b0`. `w1-A5=w1-w2+w3-b0`. Target `B4=w3-b0`.
     `w1-A5-B4=w1-w2>=0`. Trivial.
   `0/50,000` random confirms `B2`/`B4` witnesses exactly, `/tmp/check7.py`.

### Verification performed (all bounded, exact-`Fraction` arithmetic, no unbounded search)
- Harness validated first against independent brute-force `OPT_{+1}`/`OPT_{-1}` (full DELETE/KEEP/MATCH
  recursive enumeration, not the closed forms) — `0/2000` mismatches each for `TwoTouch` and `ThreeTouch`
  at the relevant sizes (`/tmp/check1.py`).
- Main target (*): `0/20,000` random (`vmax=30`) + `0/1,155` genuinely exhaustive (`w1<=8`) — matches
  and extends the file's own prior `0/1,239`+`0/14,000` corroboration.
- Each of the 5 per-term claims individually: `0/20,000` random, no exceptions (`/tmp/check1.py`).
- The Two-Variable Reflection Bound (new lemma): `0/2,870` exhaustive (`w1<=19`) + `0/30,000` random.
- **Full exhaustive re-check of the target on a slightly larger grid** (`w1<=12`, all valid
  `w2<=w1,w3<=w2,b0<=w1`): `0/4,550`, and Two-Variable Reflection Bound exhaustive to `w1<=19`: `0/2,870`
  (`/tmp/check_final.py`).
- **End-to-end sanity**: for random `(w1,w2,w3,b0)` at `|W|=3`, confirmed via true brute-force recursion
  (not the closed forms) that the actual KEEP-branch value `w1 - OPT_{-1}({b0},rest)` (computed by brute
  force, not by Lemma B's formula) is `>= TwoTouch(b0,W)` in `3000/3000` trials, and that
  `TwoTouch(b0,W)` itself equals the true brute-force `OPT_{+1}({b0},W)` in all `3000/3000` — i.e. the
  closed-form target genuinely reflects the real recursive branch semantics, not just an artifact of the
  formulas (`/tmp/check_final.py`).

**No violations found anywhere, in any of the above** — combined with a from-scratch worked-by-hand proof
of every one of the 5 sub-cases, I am fairly confident this is a genuine, complete, elementary proof, but
it has NOT been independently re-derived by anyone else yet (per project rules, treat as "found this
round, needs independent re-verification before certifying").

### Consequence, if this proof holds up (report only — not something I am certifying)
Combined with what is **already certified**: DELETE branch general (`>=TT`, §26.5(b), candidate-subset
argument), KEEP branch `b0>w1` sub-case (`=w1-b0` exactly, round 16, unconditional), MATCH branch via
`lemmas/match-branch-domination-via-per-partner-domination.md` (conditional on Per-Partner Domination,
which **is** certified unconditionally for `q<=3` — round 14, §22.2 of the approach file) — **all three
branches of the DELETE/KEEP/MATCH trichotomy would be `>=TT` unconditionally at `|W|=3`**, together with
the free direction (`TT` achievable `=>` true `OPT<=TT`), giving **Two-Touch fully, unconditionally
closed for every `|W|<=3`** (base case `|W|<=2` already certified). This is precisely the corollary
round 18's proof-reviewer rejected as an overclaim — the missing ingredient was exactly this proof, which
I believe I have now supplied. **This needs full independent re-verification (hand + code) before the
outliner/builder writes it up as closing anything** — I am reporting a strong candidate proof, not a
certified result.

### On extending beyond `|W|=3` (cheap check performed, not chased further)
Ran the same per-term reduction test at `|rest|=3` (`|W|=4`), using `ThreeTouch` at `|rest|=3` (still
inside Lemma B's certified unconditional scope) against the *conjectural* general `TwoTouch` closed form
at `|W|=4` (not itself proven yet at this size — this is exactly the open general-`q` Two-Touch
induction): **`0/20,000` random failures for the aggregate target, and 0/20,000 for EVERY individual
per-term sub-claim** (`/tmp/check_rest3.py`) — i.e. the same "per-term domination with a small
case-dependent witness" proof *shape* appears to survive at the next size up. This is only numerical
evidence (not attempted algebraically) but is a positive signal that the technique used here for
`|rest|=2` may generalize as the inductive step of the general Two-Touch/Three-Touch joint induction
(exactly the route §27.2(d)/§28.4(d) already recommend), rather than being a `|rest|=2`-only coincidence.
**Flagging, not chasing**: a general-`q` proof would need (a) the general-`q` closed form for `TwoTouch`
candidates to itself be established as the true `OPT` (open, joint induction), and (b) a case-split
covering more `Ai` terms (touch-3 terms appear once `|rest|>=3`), which is a materially larger casework
task than the 5-term bash done here — not a "cheap" extension, left for a future round.

### Distinct openings
- **Primary (this round's main finding): direct finite case-bash of the `|rest|=2` target via the
  per-term reduction + one new general lemma (Two-Variable Reflection Bound) + two elementary 2-region
  case splits.** Complete, elementary, bounded — the target the dispatch asked for.
- Secondary/noted-not-chased: the same per-term reduction shape numerically survives at `|rest|=3`,
  suggesting (but not proving) that this closes as an actual induction, not just a base-case artifact.

### Candidate technique(s)
Per-term domination via explicit closed-form witness matching (same technique family as Lemma B's own
"keep-all-three" case split and §26.5(d)/§28.4(d)'s per-term Lemma-A applications) — finite case analysis
on the rank of `b0` among `{w2,w3}` (and `w1-w2`, `w1-w3` implicitly via the new lemma), no induction
needed at this fixed small size.

### Cheap-kill candidates
None needed here — the whole point was that `|rest|=2` is small enough for direct case-bash, which
succeeded; no pruning shortcut was required.

### Knowledge-base entries used
- `lemmas/max-element-triple-identity-and-threetouch-basecase.md` (Lemma A: max-element triple identity
  `e({a,b,c})=a-|b-c|` when `a=max`; Lemma B: Three-Touch base case, supplies `ThreeTouch(b0,rest)=`
  true `OPT_{-1}` unconditionally at `|rest|<=3`, used here at `|rest|=2`).
- `lemmas/match-branch-domination-via-per-partner-domination.md` (states the exact target and precisely
  why Lemma B alone does not supply it — confirms this is the correct, precise gap to attack).
- §13.2's certified Generalized Multi-Background Peeling Lemma / DELETE-KEEP-MATCH trichotomy (defines
  what "KEEP branch value" means, `w1-OPT_{-1}({b0},rest)` at `h=0`).
- §26.5(b)/(c) (Two-Touch DELETE branch, KEEP `b0>w1` sub-case) and round-14 §22.2 Per-Partner Domination
  (`q<=3` certified) — the other 2 ingredients needed to assemble full Two-Touch closure at `|W|=3` if
  this new result is confirmed.
- (New, not yet in `knowledge_base.md` or `lemmas/`) **Two-Variable Reflection Bound**: `w1-|b0-w|>=
  |b0-(w1-w)|` for `0<=b0,w<=w1` — small, elementary, reusable; candidate for certification if the
  outliner confirms the overall route.

### Analogous past problems (cruxes)
Did not query the crux corpus fresh this round — the dispatch scope was a specific bounded algebraic
target within an already-established proof architecture (peeling + candidate-list domination), not a
fresh top-level framing question; the relevant technique (case-split domination of alternating-sum
expressions) is already the file's own established machinery (Lemma A/B, Three-Bound Domination), not
something needing external crux retrieval. If the outliner wants a crux check for the *general-`q`*
induction (the `|rest|=3+` extension noted above), that would be a more appropriate place to spend a
crux-corpus query.

### Prior progress
`0/1,239` (round 17) then `0/14,000+` (round 18) corroboration of exactly this target, explicitly logged
as "not proved" both times. This round supplies what looks like an actual complete proof (5 per-term
sub-claims, each closed by elementary case-split algebra) — new content, not previously on file.

### Dead ends (do not retry)
- Do not confuse Lemma B's *value* claim (`ThreeTouch(b0,rest)=OPT_{-1}(b0,rest)`) with the target
  *comparison* claim (`w1-ThreeTouch(b0,rest)>=TwoTouch(b0,W)`) — round 18 already flagged this exact
  conflation as the overclaim; the value claim is an *input* to the new proof above (used to identify
  the KEEP branch's true value with `ThreeTouch`), not a substitute for it.
- Do not port the general `|C|=2` "touch `<=2`" Two-Touch formula shortcut (already confirmed false,
  `23.8%`/`35.8%` failure rates, §25.2/§27.2(e)) — irrelevant here, not used in this proof, flagging only
  so it's not mistakenly conflated with the (different, `|C|=1`) target proved here.

### Small-case / intuition notes
- The clean 2-region split found here (`b0>=w2` vs `b0<w2`, with `b0` vs `w3` as a further sub-split only
  inside the second region) recurs identically for both `A4` (match) and `A5` (keep-both) — suggests
  `b0`'s position relative to `w2` (the *second-largest* element of `W`) is the structurally meaningful
  threshold, not relative to `w3` directly. Worth keeping this framing (`b0 vs w2` as the primary split)
  if a future round attempts the general-`q` induction, since it appears to be the actual load-bearing
  threshold, not an artifact of the small size.
- Region `b0>=w2` collapses `A2,A3,A4,A5` all `<=A1=b0` — i.e. `ThreeTouch(b0,rest)=b0` exactly whenever
  `b0` dominates the whole rest list. This is a clean, general-looking sub-fact (conjecture: "if
  `b0>=max(rest)` then `ThreeTouch(b0,rest)=b0`" for `rest` of ANY size, not just `2`) that may be worth
  checking at general `|rest|` cheaply in a future round — plausible mechanism: keeping/matching any
  element of `rest` when `b0` already dominates only ever *decreases* the alternating-sum value relative
  to deleting it, mirroring the intuition of Lemma B's own case-1 argument.
