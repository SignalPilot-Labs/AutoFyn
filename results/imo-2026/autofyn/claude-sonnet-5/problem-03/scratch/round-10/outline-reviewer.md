# Outline review — imo-2026-03, round 10

## Headline result (verify-before-trust): the outline's ONLY proposed new mechanism this
round, the §14 Fixed-Support Uncrossing Conjecture, is FALSE — independently refuted, at the
theorem's actually-needed budget `b=p-1`, at the induction's own **base case** (`|M|=2`). This
directly contradicts the outline's own claimed "204+ zero-failure instances at `b=p-1`." The
whole build plan for `potential-weighting-upper-bound` this round cannot be built as stated.
The §13.6 retirement (old generalized Full-Slack Insertion / Match-Recovery Lemma at `|B|≥2`,
FALSE) is independently confirmed correct. Net effect: BOTH of this round's proposed proof
routes for the single remaining theorem bottleneck are now dead; the top-level target
`OPT(Y,p-1)=NC(Y,p-1)` itself remains unrefuted (re-confirmed fresh, 40/40 trials plus every
counterexample instance below individually checked).

---

## 1. Independent re-verification of §13.6 (old Match-Recovery Lemma at `|B|≥2` is FALSE)

Re-implemented `OPT_σ(B,Z)`/`TAGGED_σ(B,Z,s)` completely from scratch (fresh Python, exact
integer arithmetic, full enumeration of `(K,D,M)` selections and all perfect matchings on the
match-support, exact crossing test `i<i'<j<j'`), directly from the file's own §11.1/§13.2
definitions — not copying the builder's or explorer's harness.

**Reproduced the claimed minimal counterexample exactly:**
```
B = {2,4}, Z = (6,3,2,1):  OPT_{+1}(B,Z) = 0,  TAGGED_{+1}(B,Z,0) = 1.
```
Confirmed by my own independent script (`0 != 1`, matching the file's arithmetic step for
step: the crossing witness MATCH(6,2)=4, MATCH(3,1)=2 → {4,4,2,2}, e=0; the only way to
reproduce {4,2} without crossing the arcs (0,2)/(1,3) costs ≥1).

Extended my own random sweep (fresh seed, independent of both the builder's and explorer's):
`|B|=0`: 0/300 mismatches. `|B|=1`: 0/300 mismatches. `|B|=2`: **4/300 mismatches** (~1.3%,
same order of magnitude as the explorer's fresh 22/500 ≈ 4.4%; round 9's own claimed "500/500
clean" is confirmed WRONG, not merely a different sample). **Verdict: §13.6's retirement is
correct — approve, keep as a permanent recorded dead end.**

## 2. Independent re-verification of §14 (NEW Fixed-Support Uncrossing Conjecture) — FOUND FALSE

Wrote a second, independent brute-force harness for `OPT(Y,b)`/`NC(Y,b)` directly from §9.2's
definitions (full enumeration of every `(K,D,M)` selection with cost `≤b`, not sampling the
selection space). First reproduced the outline's own reported pattern faithfully on a
matched-methodology sweep (p up to 6, random Y): `b=p-1`: 0/25 violations, `b=p-2`: 0/22
violations, `b=p-3`: **2/13 violations** — same sharp cutoff shape the outline reports (its own
25/78 at `b=p-3`), and confirmed the correlation the outline flagged: every `b=p-3` violation I
found used strictly less than the full budget (cost `2 < b=3`).

I then **pushed the check beyond the outline's own tested range** (p up to 8, more seeds, wider
value ranges) — per this project's standing rule to extend verification past what's already on
file — specifically at `b=p-1`, the regime the outline claims is clean (204+/204 zero
failures):

```
seed 99, p=8, b=7: 6 violations / 66 crossing-optimal instances checked
seed 1,  p=8, b=7: 2 violations / 26
seed 2,  p=8, b=7: 4 violations / 89
seed 4,  p=8, b=7: 3 violations / 28
seed 11, p=7, b=6: 6 violations / 24
```
Non-trivial, reproducible failure rate (5–20%) at exactly the budget the outline claims is
clean, at `p=7` and `p=8` — not just `p=8`, and not deep in the tail of the sample space.

**Minimal, hand-verified counterexample (found and re-derived by hand, not just by script):**
```
Y = (7, 5, 4, 4, 3, 1),  p=6,  b=p-1=5.

Selection achieving OPT(Y,5)=0 (cost 2, well under budget 5):
  K = {4,3} (positions 3,4),  D = ∅,  M = {(7,4)@(0,2), (5,1)@(1,5)}
  combined multiset {4,3} ∪ {3,4} = {4,4,3,3},  e = 4-4+3-3 = 0.
The matching M={(0,2),(1,5)} CROSSES (0<1<2<5).

Support = {0,1,2,5}. The only two non-crossing re-pairings of this exact support:
  (0,1)-(2,5): values 7-5=2, 4-1=3 → combined {4,3,3,2}, e = 4-3+3-2 = 2.
  (0,5)-(1,2): values 7-1=6, 5-4=1 → combined {6,4,3,1}, e = 6-4+3-1 = 4.
min(2,4) = 2 > 0 = OPT(Y,5).
```
Both alternatives strictly exceed OPT — a direct, hand-checkable violation of §14's Fixed-
Support Uncrossing Conjecture **at the base case `|M|=2` itself** (Step 2 of the outline's own
skeleton), at the exact budget `b=p-1` the theorem needs. Verified `OPT(Y,5)=NC(Y,5)=0` by full
exhaustive search (a *different*, already non-crossing, selection achieves the same value 0) —
so the theorem's actual top-level target is untouched, only the specific "any crossing
OPT-witness can be locally repaired holding K,D fixed" mechanism is false.

A second, larger hand-traceable counterexample at `p=8` (`Y=(88,76,60,50,48,28,28,20)`,
`b=7`, `K=(4,6)`, `D=(3,7)`, `M=((0,2),(1,5))`, `OPT=0`, both non-crossing re-pairings give 32
and 24) is also fully hand-verified in my working notes and available on request.

**Why this is fatal, not a fixable gap.** I checked the natural patch — restrict the claim to
selections using the *full* budget (`cost=b` exactly): by the index identity
`|K|+|D|+2|M|=p` and `cost=|D|+|M|=b=p-1`, full-budget selections force `|M|≤1`, which can
*never* cross — so that restriction makes the conjecture **vacuously true and useless** (300
trials, 0 full-budget crossing OPT-witnesses found at all). The genuine content of the
conjecture lives entirely in slack selections (`cost<b`), exactly where my counterexamples
live, and there it is false. A weaker, purely *existential* reformulation ("some OPT-achieving
selection is non-crossing or fixable") would sidestep my counterexamples (both instances above
do have an already-non-crossing OPT-achieving witness) but that existential form is not a
fixed-support local-exchange lemma at all — it collapses back to exactly the same "does a good
witness exist" question the aggregated Match-Recovery/Small-Gap Crossing-Domination Lemma
already tracks (i.e. no genuine simplification, same difficulty class as the just-retired
§12.2/§13 route).

## 3. Dispatch's specific question: is §14 "genuinely different" from the dead round-6/7 claim?

**Partially confirmed, partially not — important nuance.** The outline is *correct* that this
is a narrower, differently-scoped claim than round 6/7's dead general-budget local exchange: I
independently re-tested the exact round-6 dead-end instance `Y=(43,33,20,16,11,8,2)` at
`b=p-1=6` and found **0 violations** (matches the outline's claim exactly) — along with all 4
other adversarial instances on file (`Y=(92,89,77,73)`, `Y=(39,36,30,28,22,18,14)`,
`Y=(400,218,194,187,169,27,3)`, `Y=(463,461,372,291,237,180)`), all clean at `b=p-1`. So §14 is
genuinely NOT a disguised rehash of the round-6/7 claim — it is a distinct, more narrowly
scoped statement, as claimed. **But it is a new, independently false claim of its own** (§2
above) — the outline's "not a rehash" defense is true and irrelevant to soundness; a narrower
claim can still be false, and this one is, via fresh counterexamples the outline's own sample
(evidently biased toward smaller `p` and/or too few trials at `p=7,8`) never found.

## 4. `concavity-minimax-duality` benching — confirmed justified

Re-read the file's round-10 benching note and the plateau-check explorer's Task 1. The
reasoning is sound and unchanged from round 9: the entire §14/§15 machinery (`g*`,
Distinct-Bucket, Superincreasing Preservation, Value-Order=Dominant-Index-Order) is proved only
for states reachable from a superincreasing base via legal D/M sequences; even a full proof of
the Local Claim yields a bound on `e(D_m, XY-response)` — i.e. re-derives the already-closed
lower bound (round 8) via an independent mechanism — not a bound for an arbitrary (non-
superincreasing) opening `A`, which is what the open upper-bound gap needs. No step in §14/§15
produces an `A`-generic statement. Confirmed: no leverage, correctly benched. Also confirmed
`dyadic-cascade-induction`'s benching is unaffected (its machinery is likewise `D_m`-specific;
the plateau-check explorer's grep found no unused general-opening content there either).

## 5. Approach-by-approach verdicts

- **`potential-weighting-upper-bound` — RETHINK (for this round's proposed plan only).** §13.6's
  retirement of the old |B|≥2 route is correct and stays on file as a permanent dead end. But
  §14's Fixed-Support Uncrossing Conjecture — the round's sole proposed replacement mechanism,
  and the only thing scheduled to be built — is independently found FALSE, including at its own
  base case (`|M|=2`), at the exact budget the theorem needs (`b=p-1`), with hand-verified
  counterexamples above. Per CLAUDE.md's RETHINK routing, this cannot go to a builder as
  outlined; it must return to the proof-outliner. The file's OTHER content remains fully valid
  and certified (Slack Collapse, chain-prefix+tail rescoping `§9.4`, General Rank-Extraction
  Identity, the DELETE/KEEP closed-form branches of §13.2) — none of this is touched by either
  refutation. The top-level target `OPT(Y,p-1)=NC(Y,p-1)` remains open, unrefuted, and
  well-supported (re-confirmed fresh this round).
- **`concavity-minimax-duality` — benched, confirmed correct**, no build task.
- **`dyadic-cascade-induction` — benched, confirmed correct**, no build task (top Elo, milestone
  content already complete within its own scope).
- **`elementary-exchange-smoothing` — retired**, unaffected.

## 6. Consequence for the population (flag for next round's math-explorer/outliner)

Both proof routes this round for the single remaining theorem bottleneck (recursive
background-set peeling, §12/§13; fixed-support local uncrossing, §14) are now dead, in the same
round. This is a real, not cosmetic, setback: the population currently has **zero live
mechanism** for `OPT(Y,p-1)=NC(Y,p-1)`. Recommend next round's explorer treat this as a genuine
plateau-break trigger (per CLAUDE.md's guidance) and prioritize a mechanism that does not rely
on "take one canonical/frozen optimal witness and locally repair it" — both dead mechanisms
share exactly that shape (a witness-repair claim), and the diagnosis in both cases is the same:
**the true optimal witness's identity (which elements participate, not just how they're paired)
is not locally stable** — an inherently existential fact. The two still-untried crux leads on
file (`aimo-0043` obstacle-charging between branches; `aimo-0558` greedy+injective charge-to-a-
distinct-witness, both flagged in §12.3/§14's "possible accounting-step imports") are exactly
the two candidate techniques built to handle this *existential* character rather than a
per-witness local fix — recommend the next outliner develop one of these into a real skeleton
instead of another local-exchange variant.

## 7. Ranking

Registered: no new slugs this round (§14 was a revision inside `potential-weighting-upper-bound`,
not a new slug — correctly avoids CLAUDE.md's single-proof-split trap). No copy_approach calls
(no branching requested). Ran `update_ranking` (clears `stale` on all three active approaches):
`dyadic-cascade-induction` > `potential-weighting-upper-bound` (unconditional milestone content
vs. two consecutive dead ends this round, despite correct diagnostic work); `potential-weighting-
upper-bound` > `concavity-minimax-duality` (still holds the critical-path certified content vs.
confirmed zero leverage). Resulting Elo: `dyadic-cascade-induction` 1706 (top), `potential-
weighting-upper-bound` 1480, `concavity-minimax-duality` 1327.

## 8. Build set

No approach has a live, sound, buildable task this round: `potential-weighting-upper-bound`'s
only proposed task is refuted (RETHINK → back to outliner with the counterexamples above); the
other two are correctly benched. Per CLAUDE.md, a RETHINK routes back to the outliner rather
than to a builder, and forcing a build on a refuted plan would waste builder effort re-deriving
what is already disproved above. Recommend next round's outliner start directly from §6's
existential-mechanism redirection rather than patching §14.

build set: (none this round — potential-weighting-upper-bound RETHINK, returns to outliner with the counterexamples in this report; dyadic-cascade-induction and concavity-minimax-duality remain correctly benched)
