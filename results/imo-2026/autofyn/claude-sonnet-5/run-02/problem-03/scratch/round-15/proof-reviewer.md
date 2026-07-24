# Round 15 proof-reviewer report — IMO-2026-03

Both slugs built this round: `greedy-halving-adversary`, `lp-duality-certificate`.
All new claims were independently re-verified with fresh exact-`Fraction`
scripts (in `/tmp/round15_review/`), not the builders' own scripts, per the
task instructions.

## Verdict summary

| Slug | Verdict | Outcome recorded |
|---|---|---|
| `greedy-halving-adversary` | CHANGES REQUESTED | `partial` |
| `lp-duality-certificate` | CHANGES REQUESTED | `partial` |

Neither is APPROVE (expected — both are partial sub-fronts of a larger open
problem); neither is RETHINK (both approaches remain viable and made real
progress).

## greedy-halving-adversary

**Verified correct (independently re-derived/re-verified):**
- Upper-Truncation Identity: re-derived from scratch, 3000 fresh trials, 0
  mismatches (`/tmp/round15_review/verify_upper_trunc.py`).
- Proposition 30 (exact formula for $A(F\cup G')$ on all $v\in(0,p_2)$): fresh
  script, $n=3,\dots,6$, 12000 trials total, 0 mismatches
  (`/tmp/round15_review/verify_prop30.py`).
- Target B negative finding: hand-confirmed $\psi(p_3)=1/5>p_3=2/15$ at
  $n=3$. Target B's actual target inequality re-tested independently (fresh
  random-legal-refinement simulator, 5349+ trials, 0 violations,
  `/tmp/round15_review/verify_targetb.py`), and the reported
  margin-vs-$f(n)$ figures ($\approx0.002$ at $n=3$, $\approx0.004$ at
  $n=4$) were reproduced almost exactly by an independent adversarial grid
  search.

**New finding (upgrade of the builder's own flag from "notational
inconsistency" to "confirmed proof gap"):** I investigated the flagged issue
in the already-certified `proposition-29b-partial-closure.md` directly rather
than taking the builder's hedge at face value. The lemma's Statement defines
$G'$ as a refinement of $\{p_3,\dots,p_{n+1}\}$ (excluding $p_2$), but this
cannot represent a physically complete legal final multiset ($p_2$ must
appear somewhere); the natural, game-legal reading (matching sibling
Proposition 26) has $G'$ range over the *full* tail $\{p_2,\dots,p_{n+1}\}$,
in which case $p_2$ can remain untouched and $\max(G')=p_2>p_3$ — directly
contradicting the proof's Step 4 citation "`safe-window-lemma` one level
down, $\max(G')\le p_3$." I confirmed this is a real, exploitable gap in the
proof mechanism (not cosmetic), but then ran an adversarial grid search
($n=3,\dots,7$, $G'=$ full tail deliberately left untouched — precisely the
configuration that breaks the cited step) and found **zero counterexamples**
to the lemma's actual conclusion; margins stayed tiny but strictly positive.
So: the theorem is very likely still true, but the certified proof as
written does not establish it for the game-legal reading of $G'$. I annotated
`lemmas/proposition-29b-partial-closure.md` with a "Reviewer correction
(round 15)" section recording this and downgrading its certification status
(not retracting it, since no counterexample to the conclusion was found).
Future rounds should not treat it as closing the $\tau_P<p_3$ branch until a
repaired proof is supplied.

**Recommendation:** the round's own diagnosis (all three items are one
obstruction — bound $A(S_{>v})$ above for $S$ a legal $(n-2)$-ladder response
and $v$ arbitrary) is correct and well-isolated; it should be the population's
next single target. Separately, `proposition-29b-partial-closure.md` needs a
repaired Step 4 (bounding against $p_2$, not $p_3$, or otherwise reworking
the argument) before further downstream use.

## lp-duality-certificate

**Verified correct (independently re-derived/re-verified):**
- Cross-Piece Sign-Assignment Identity: re-derived and re-verified with an
  independently-written 20000-trial script (7961 trials satisfied the
  monochromaticity hypothesis; 0 mismatches on all of them,
  `/tmp/round15_review/verify_crosspiece.py`).
- Both round-14 near-tight case-(b2) witnesses: I independently constructed
  explicit legal fragment realizations from scratch for both the $n=3$ and
  $n=4$ witnesses (not reusing the builder's constructions) and confirmed
  $\Phi$ exactly matches the predicted closed-form value in both cases and
  beats the respective $a_nT$ threshold
  (`/tmp/round15_review/verify_witnesses.py`,
  `/tmp/round15_review/verify_witness_n4b.py`). The claim that "both
  witnesses are now unconditionally closed" is confirmed.

**New finding — a confirmed sign bug in the Alternating Gap-Cross Lemma:**
The lemma's stated identity uses tail prefactor $(-1)^j$, where $j$ counts
*every* pair including ones left untouched because $p_{2i-1}=p_{2i}$ (an
option the construction explicitly allows). I found an exact counterexample:
pieces $(45,45,31,27)$ sorted descending, $j=2$ (pair 1 equal/untouched,
pair 2 splits $31$ into $(30,1)$ sandwiching $27$) — feasible per the
lemma's own closed-form feasibility test. Direct computation gives
$A(\{45,45,30,27,1\})=4$, but the lemma's formula predicts $-4$. Root cause:
an equal/untouched pair contributes 2 raw elements (an even, parity-
preserving rank shift), not the 3 elements (odd, parity-flipping shift)
every pair is implicitly assumed to contribute. The correct prefactor is
$(-1)^{j'}$ where $j'$ = number of pairs *actually split*. I confirmed via a
further 8000-trial sweep that mismatches occur precisely in the sub-
population with an odd count of equal/untouched pairs, and only there.
Neither headline witness uses an equal/untouched pair, so both witness
closures are unaffected. I annotated `lemmas/alternating-gap-cross-lemma.md`
with a correction note marking it **not certified as currently written**
(left in place, not deleted, per the round-10 precedent for
`simplex-exchange-smoothing-vertex-maximization`), recommending the fix
$(-1)^j\to(-1)^{j'}$ before further reliance — in particular before using it
to claim coverage of any case-(b2) marking with exactly-equal adjacent
pieces.

**Recommendation:** the feasibility characterization itself is correct and
reusable; only the identity's tail-sign needs the $j\to j'$ fix. The honest
coverage quantification (modest gain over `bisect-top-k-lemma` alone) stands
regardless of the bug, since it wasn't measuring the buggy sub-case.

## current.md

Updated with a new Round 15 entry reflecting the above (both approaches'
genuine verified progress, plus the two confirmed bugs and how they were
handled). `lemmas/proposition-29b-partial-closure.md` and
`lemmas/alternating-gap-cross-lemma.md` were both annotated in place with
reviewer correction sections rather than retracted, since in both cases the
underlying conclusion survived adversarial testing even though the specific
proof/statement as written did not (or was sign-flawed in a sub-case).
Status remains `partial`.
