# Round 12 math-explorer report — hunting the recursive invariant for SAR

**Lens (assigned):** find the recursive invariant specific to the family of instances arising
from repeatedly peeling an `|B|<=1`-seeded argmin branch, per round 11's diagnosis (§16.3.3 of
`potential-weighting-upper-bound.md`) that a correct proof of Sharp Argmin Recovery (SAR) needs
exactly this, not an arbitrary-triple induction (the "one-step compatible winner" / GML skeleton).
**Role: scout only — no proof attempted, no build.** All code fresh, written from the file's own
prose definitions (§13.2, §16.1), sanity-checked against the file's own certified `|B|=2`
counterexample (`B={2,4},Z=(6,3,2,1)`: reproduced `OPT=0,TAGGED=1` exactly) before being trusted for
anything new. Code archived at `/tmp/round-12/work/` (`wclean.py` + 7 driver scripts).

## Headline finding

A **strictly stronger, cleaner candidate invariant** than SAR was found and stress-tested with
**zero violations in 1600+900+240+110 = 2870+ trigger-scoped exact-integer trials** (`q` up to `9`,
plus dyadic/AP/heavy-duplicate structured families), and its scope was **precisely delimited**
computationally (shown to fail, ~15-16% of the time, the moment either of its two defining
conditions is dropped — a real, not vacuous, restriction, exactly the shape the round-11 reviewer
asked for). This looks like a genuine candidate for the missing recursive invariant, but it is
**NOT proved** — this is a scouting report, not a build.

## 1. Tracing the family concretely (as asked)

Restating §13.2/§16.1's setup: `|B_0|\le1`, sorted `Z_0=(z_1\ge\dots\ge z_q)`,
`A_1=\mathrm{OPT}_{+1}(B_0,Z_0\setminus\{z_1\})`, `A_{3,l}=\mathrm{OPT}_{+1}(B_0\cup\{z_1-z_l\},
Z_0\setminus\{z_1,z_l\})`, `k^*=\arg\min_lA_{3,l}`, `M=A_{3,k^*}`. **One level of peeling the argmin
branch** produces the derived instance `(B_1,Z_1,s_1):=(B_0\cup\{z_1-z_{k^*}\},\,
Z_0\setminus\{z_1,z_{k^*}\},\,k^*-1)`.

Nine concrete `q=4,5,6` case-2-triggering examples (`M<A_1` and `M<A_2`), exact integers:
```
B0=(7,)  Z0=(8,5,3,1)         -> k*=4, d=7,  B1=(7,7), Z1=(5,3),      s1=3, M=0
B0=(2,)  Z0=(10,8,3,3)        -> k*=2, d=2,  B1=(2,2), Z1=(3,3),      s1=1, M=0
B0=(7,)  Z0=(10,2,1,0)        -> k*=2, d=8,  B1=(7,8), Z1=(1,0),      s1=1, M=1
B0=(6,)  Z0=(9,8,4,3,0)       -> k*=4, d=6,  B1=(6,6), Z1=(8,4,0),    s1=3, M=0
B0=(1,)  Z0=(10,9,2,0,0)      -> k*=2, d=1,  B1=(1,1), Z1=(2,0,0),    s1=1, M=0
B0=(1,)  Z0=(9,8,8,5,5)       -> k*=2, d=1,  B1=(1,1), Z1=(8,5,5),    s1=1, M=0
B0=(8,)  Z0=(10,6,5,4,2,0)    -> k*=5, d=8,  B1=(8,8), Z1=(6,5,4,0),  s1=4, M=0
B0=(3,)  Z0=(10,8,7,7,6,2)    -> k*=3, d=3,  B1=(3,3), Z1=(8,7,6,2),  s1=2, M=0
B0=(8,)  Z0=(10,6,5,1,0,0)    -> k*=4, d=9,  B1=(8,9), Z1=(6,5,0,0),  s1=3, M=1
```
Every one of these (and every triggered instance found this round, see §2) had `|B_0|=1` — a fresh,
independent reconfirmation of §15.4's own sampled note ("`|B|=0`: 0 trigger events in 3000 random
trials"): with `q` up to `9` and several thousand fresh trials, **the trigger never once fired at
`|B_0|=0`** (I did not exhaustively verify this, only sampled, same caveat the file already flags —
but it is now corroborated at larger `q` than the file's own `\le8`).

## 2. The candidate invariant: "Delete-Suffices" (no internal matching is ever needed)

**Observation, then hypothesis.** Inspecting actual optimal witnesses for `A_{3,k^*}` (not just the
scalar value) in the trigger examples above, every single optimal witness I found used **only
Keep/Delete — never a single Match** within the residual `Z_1=Z_0\setminus\{z_1,z_{k^*}\}`. This is
much stronger than SAR (SAR only needs *some* non-crossing-and-split-compatible witness; a
K/D-only witness has literally **zero arcs**, so it is vacuously non-crossing and vacuously
compatible with *every* split, at *every* future recursion depth simultaneously).

Precisely, define `\mathrm{OPT\_KD}(B,Z):=\min_{S\subseteq Z}e(B\cup S)` (only subset-keep,
everything else deleted — no matching branch at all; trivial to compute, `2^{|Z|}` subsets, no
matching-structure enumeration needed).

**Candidate "Delete-Suffices Lemma."** *For `|B_0|\le1`, sorted `Z_0`, if `M:=\min_lA_{3,l} < A_1`
(RDRC's own weak trigger hypothesis — I did NOT need the stronger `M<A_2` too), then, writing
`k^*` for a global argmin and `(B_1,Z_1)` for the resulting argmin-branch instance,*
```
OPT_KD(B_1, Z_1)  =  M   (=  A_{3,k^*}  =  OPT_{+1}(B_1,Z_1) with matching fully allowed).
```
I.e. **whenever the trigger holds, the entire downstream sub-problem needs no internal matching at
all to reach its true optimum** — not merely "some witness happens to avoid one specific crossing."
This trivially implies SAR (a K/D-only selection is non-crossing and split-`s_1`-compatible for
free), and, if it composes recursively (see §4), it resolves exactly the objection that killed the
"one-step compatible winner" GML skeleton (§16.3.3): GML failed because compatibility was only
checked at the top level and could evaporate one level down; a **match-free** witness has nothing
that *could* evaporate — there are no arcs to conflict with any future split, ever.

## 3. Computational testing — where it holds, and where it precisely does NOT (the scope is real)

All exact-integer, brute force (no heuristic pruning of the correctness-critical enumerations, only
instance sampling is random), fresh code (`wclean.py`, independent of the builder's/reviewer's
round-11 harnesses, though cross-checked against the file's own `|B|=2` example first).

| Test | Scope | Result |
|---|---|---|
| `driver2.py` | trigger (`M<A_1`), `k=k^*` (global argmin), `q=4..9`, `\|B_0\|=1` | **900/900**, zero violations |
| `driver7.py` | same, `q=4..8`, `v_{\max}\in\{5,10,15,20\}` (wider value spread) | **1600/1600**, zero violations |
| `driver1.py` | same, stronger trigger `M<A_1` AND `M<A_2` (the file's own "case 2") | **110/110**; weak-trigger-only variant **240/240** |
| `driver6.py` | structured: dyadic `D_m` (`m=2..5`), arithmetic progressions, heavy-duplicate lists | **zero violations within scope** — 2 apparent "failures" both had the trigger FALSE, i.e. outside the lemma's own hypothesis, not counterexamples |
| reproduced the file's own §16.3.1 worked example, `B=[1],Z=(9,8,8,8,5,3,0)` | as corrected by the round-11 reviewer | trigger true, `M=0`, `OPT_KD(B_1,Z_1)=0` — **matches** |

**Two decisive negative controls, precisely delimiting the scope (this is the important part — it
shows the invariant is a real restriction, not vacuously true everywhere):**
- `driver3.py`: drop "`k=k^*`" (use an *arbitrary* match partner `k`, no argmin requirement, no
  trigger condition either): **504/600 (84%)** — **96 clean counterexamples**, e.g.
  `B=(0,),Z=(8,7,4,2),k=3` (not the argmin): `OPT_KD=2 \ne 1=` true value. So argmin-ness is
  load-bearing, not cosmetic.
- `driver4.py`: keep `k=k^*` (global argmin) but drop the trigger condition entirely (no requirement
  `M<A_1`): **513/600 (85.5%)** — **87 clean counterexamples**, e.g.
  `B=(2,),Z=(5,5,3,1),k^*=2` (here `A_1=A_2=M=0`, trigger does NOT hold since `M` is not *strictly*
  less than `A_1`): `OPT_KD(B_1,Z_1)=1\ne0`. So the trigger condition is *also* independently
  load-bearing.

So the candidate invariant is precisely tied to **both** "recovery partner is the true global
argmin" **and** "matching strictly beats the trivial delete fallback" simultaneously — exactly the
two structural facts the round-11 negative results (§16.3.2, §16.3.3) already flagged as the load-
bearing restrictions, now sharpened into one clean, much stronger, and (importantly) *cheaply
checkable* combinatorial claim (subset optimization, not matching enumeration).

## 4. Why the level-2 trigger essentially vanished, and what that suggests

`driver5.py` chained two levels of peeling: of `800` fresh level-1-triggered instances (`q=6..9`),
**exactly `0`** had a live level-2 trigger inside `(B_1,Z_1)` (i.e. `(B_1,Z_1)`'s *own* match-branch
never strictly beat *its own* delete branch, in every instance checked). This is consistent with,
and plausibly *explained by*, the Delete-Suffices Lemma being a **global** fact about the whole
residual sub-problem (not just about one witness): if `\mathrm{OPT}(B_1,Z_1)` already equals
`\mathrm{OPT\_KD}(B_1,Z_1)` exactly, then decomposing `Z_1` again via its own top element can only
ever be won by *its own* DELETE/KEEP branches (recursing the same match-free mechanism down) — the
match branch cannot win against them, because winning would require the match branch to reach a
value the KD-only search does not already reach, contradicting Delete-Suffices at that level. **If
this reasoning can be made rigorous, it would mean the trigger condition itself becomes
self-terminating after one level** — a strong hint about *why* this specific family (not arbitrary
`(C,W,s)` triples) might make a genuinely-recursive proof of SAR tractable where GML's naive version
failed: the invariant to carry is not "the winner is compatible" (GML, false) but **"the winner
needs no further matching at all"** (Delete-Suffices, survives every test this round) — a strictly
stronger, all-arcs-free property that, if provable, is automatically inherited through unboundedly
many further levels for free (nothing to check against future splits).

## 5. Crux corpus search — one thematically relevant precedent, no magic bullet

Per `crux_moves_documentation.md`, filtered `combinatorics` domain, subtopics
`games-and-strategy`/`invariants-and-monovariants`/`processes-and-algorithms`/
`induction-and-construction`/`extremal-principle`, then narrowed by keyword (`non-crossing`,
`crossing`, `peel`, `recursive`, `argmin`):

- **`aimo-0894` (RMM 2018/5, non-crossing arrow configurations)** is the closest structural
  precedent found: its crux is "at a cyclically-adjacent in/out-of-`S` boundary index `k`, the
  non-crossing + forbidden-quadrangle rule **forces** the arrow `a_k\to a_{k+1}` to exist directly
  (a *forced local/adjacent link*, not a repair of an existing one), which can then be stripped,
  reducing to a strictly smaller instance of the identical problem for the induction." This is the
  same *shape* of move Delete-Suffices is reaching for — proving a strong **structural** fact about
  the optimal witness (not just its value) that is preserved under peeling — but the mechanism
  itself (forced-adjacent-arrow via a forbidden-quadrangle contradiction) does not transplant
  directly: our problem's objective is the globally rank-coupled alternating sum `e(\cdot)`, not a
  local forbidden-pattern rule, so there is no local contradiction to derive a forced *link*;
  instead the candidate invariant found here forces the **absence** of any link. Recorded as a
  useful precedent for the *proof shape* (strengthen to a structural/positional claim about the
  optimal witness, not just the scalar value, so it survives peeling), not a reusable lemma.
- **`aimo-0392` (USA TSTST 2019/8, minimum non-crossing-matching count)** uses "a hull point `P`
  splits the rest into two non-interacting halves via one segment, apply strong induction to each
  half separately" — this is mathematically the same inside/outside-independence mechanism the
  approach file's own certified Non-crossing inside/outside independence lemma
  (`layer-cake-and-noncrossing-independence.md`) already supplies; **no new leverage**, already
  in the population's toolkit.
- Hall's-theorem-style and averaging leads were not re-searched (already ruled out decisively in
  round 11, §15.2/§16.3.1 — no reason found this round to revisit either).
- No crux was found whose load-bearing move is literally "prove the optimum needs no matching at
  all, recursively" — the Delete-Suffices candidate above appears to be a genuinely new formulation
  for this problem, not an adaptation of an existing crux mechanism.

## 6. Honest assessment and recommended next step

- **Not proved.** This is a scouting report: a new, sharper, more strongly-scoped candidate
  invariant, found and stress-tested this round (2870+ trials, zero violations within its own
  precisely-delimited scope; two clean negative controls showing the scope is real). No proof
  attempt was made (out of scope for this role).
- **Recommended build target for next round:** attempt a direct proof of the Delete-Suffices Lemma
  by strong induction on `q` — it is a strictly cleaner target than SAR because its conclusion
  (`\mathrm{OPT}=\mathrm{OPT\_KD}$, i.e. "matching is never beneficial in this residual") is a
  subset-optimization statement, which may be more tractable via an exchange argument using the
  already-certified **General Rank-Extraction Identity** and/or **Forced Swap Inequality**
  (§13.1/§16.2 of the approach file) than the crossing-based machinery that has repeatedly stalled.
  If Delete-Suffices is provable by induction (using itself, or a comparably-scoped statement, as
  the IH on the strictly smaller `(B_1,Z_1)`), it closes SAR/RDRC and hence the entire remaining
  upper-bound gap in one shot (per §15.4's own accounting of what closing SAR/RDRC yields).
- **Recommended cheap pre-build step:** before committing a full proof-builder round to it, push
  the adversarial testing further than I had budget for here — specifically a hill-climbing/
  simulated-annealing search explicitly minimizing `OPT_KD(B_1,Z_1)-M` toward a negative value
  (the same style of search round 11's reviewer used for SAR itself), and an exhaustive (not
  sampled) sweep at `q=7,8` to upgrade "zero violations in thousands of random trials" to
  "zero violations, exhaustively, at this size" — I did not have budget to do either this round.
- **If Delete-Suffices turns out to be false at some larger/adversarial scale**, the diagnosis in
  §4 above (that it's about the whole residual sub-problem, not one witness) is itself a useful,
  fallback-scoped statement worth re-testing at a coarser grain (e.g. "no crossing arc is ever
  needed," which is exactly SAR, already well-supported) — so this round's work does not put all
  the weight on one untested idea; it sharpens the target while leaving SAR itself as the safe
  fallback, exactly as the round-11 diagnosis asked for.
