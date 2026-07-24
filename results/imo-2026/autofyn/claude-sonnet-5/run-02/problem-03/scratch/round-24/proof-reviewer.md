# Round 24 proof-reviewer report — imo-2026-03

Reviewed all 3 builds this round: `greedy-halving-adversary`,
`lp-duality-certificate`, `rank-pigeonhole-budget`. Independently
re-derived/re-verified all load-bearing new claims with fresh exact-
`Fraction` scripts (not the builders' own), per the standing rules.
Whole-problem `## Status` in `current.md` remains **partial** (unchanged,
was already correct).

---

## 1. `greedy-halving-adversary`

**Verdict: CHANGES REQUESTED (Status: partial — not the "n=5 full closure"
the file's Open-gaps section headlines).**

**What is genuinely proved.** New Theorem 38 defines the standalone
induction target h(m) := inf_{c,S} A({c}∪S) over the unit m-ladder, and
proves h(1) = f(1) **exactly**, via a fully exhaustive case analysis: at
m=1 the tail-refinement budget is 0, so S is forced to be the entire
untouched 2-piece ladder {2,1} (in f(1)-units), making A(c) an explicit
3-piece function of the single free variable c whose minimum over its
whole domain (0,2] is computed directly by hand: A=1+c on (0,1] and
A=3-c on [1,2], minimum exactly 1 at both endpoints c=0,2. I re-derived
this by hand from scratch and it is correct; this piece is a real,
complete, non-circular proof (no reliance on the confirmed-dead
Cross-Level Rescaling route on {c}∪S itself, as the file correctly
avoids). **Certified** as `lemmas/theorem-38-h1-exhaustive-closure.md`,
scoped precisely to the m=1 result.

**The overclaim.** The file's "Open gaps" section states: "Combined with
Theorem 37 (the 'p4-untouched' sub-case, unconditional for n<=6, so in
particular n=5), Case (b)'s whole 'v>=a' branch is now fully,
unconditionally closed at n=5." This does not follow from what is
actually proved. Theorem 37's own "Scope" paragraph (round 23, unchanged
this round) explicitly says: "This closes exactly one member of the
vertex family... It does not establish that this vertex is the global
minimum of A(B) over the entire legal (b,T') family." Theorem 37's proof
establishes the identity A(B)=A(T'') **at the specific vertex b=p4=
max(T')** (when T' leaves p4 untouched) and then bounds A(T'') via the
fully general (star_{n-4}); it never rules out that the true joint
(b,T')-vertex minimizer could instead have b tied to a **non-maximal**
element of T' — e.g., if T' spends its cut budget splitting p5 (not p4)
into fragments d1,d2, the joint vertex could in principle have b=d1
rather than b=p4=max(T'). If that were the true minimizer, the reduced
quantity would be A({p4,d2,p6-type-remainder}), not A(T''), and Theorem
37's mechanism does not address it. This is exactly the same failure
mode that this round's **own new numeric finding** demonstrates is real
in the *recursive* h(m)/c-vs-S sub-problem: a 3000-trial search found
"deeper ties" (c tied to the 3rd, 5th, ... largest element of a
reference multiset, not just the top) beat the naive top-tie/boundary
candidates in ~46% of arbitrary-multiset trials and ~3.7% of genuine
legal-ladder-refinement trials at m=2..5. The file discovered and
honestly reported this failure mode for the c-vs-S sub-problem, but did
not check whether the analogous failure mode also applies to the
*original*, un-recursed b-vs-T' problem that Theorem 37 addresses — and
it does apply there in principle (the vertex-minimum theorem allows b to
tie to any element of the merged multiset, not just the max).

**Independent stress test.** I wrote two independent exact-`Fraction`
scripts and ran 200,000+ random trials each at n=5, deliberately
including cases where b ties to non-maximal fragments of T' (produced by
splitting p5 or p6 instead of p4) — **zero violations of A(B)>=f(5)
found** in either script. So the underlying claim ("Case (b)'s v>=a
branch is closed at n=5") is very likely true, but this is corroborating
evidence for the *result*, not a substitute for the missing case in the
*written proof*. Per CLAUDE.md's rigor rules ("No skipped cases... every
case in a casework proof must be settled"), this claim should be
downgraded from "fully, unconditionally closed" to "strongly supported
numerically, not yet proved" until the b-tied-to-non-maximal-T'-fragment
vertex type is either ruled out by argument or explicitly evaluated.

**Certified this round:** `theorem-38-h1-exhaustive-closure.md`
(m=1 result only, with the overclaim explicitly flagged and excluded
from certification in the same file).

---

## 2. `lp-duality-certificate`

**Verdict: CHANGES REQUESTED (Status: partial, exactly as the file's own
Status field already says — no overclaim found).**

Six new chambers this round, all re-derived from scratch (explicit legal
Xiang-Yu cut composition + exact application of the certified
`cross-piece-sign-assignment-identity`, not numeric curve-fitting):

- **Double-Sandwich-Below/Above**: closed forms Φ_Below = p2+p3+p4/2
  (feasible iff p3+p4/2 < p1 < p2+p3) and Φ_Above = p1+p4/2 (feasible
  iff p1 > p2+p3). I independently re-verified both formulas AND both
  exact feasibility regions with a fresh 20,000-trial exact-`Fraction`
  script (construct the midpoint of the derived feasible interval,
  recompute Φ directly from the full 6-element multiset via sort-and-
  alternate-sum) — zero mismatches. Certified.
- **Bisect-Subset Lemma**: strictly generalizes the certified
  `bisect-top-k-lemma` from prefixes {1,...,k} to arbitrary subsets S,
  Φ_S = (T+A(R))/2 for R = untouched pieces. The proof is a direct,
  one-paragraph corollary of `cross-piece-sign-assignment-identity` (same
  same-piece-pair-cancellation mechanism as every prior chamber) — not a
  curve fit; I spot-checked one row (S={2,3}) by hand, exact match.
  Certified as fully general (any m, any n, any S with |S|<=n).
- **Triple-Pin, Chamber B1/B2, P1P2-tied-to-p3**: I wrote three
  independent verification scripts (20,000 trials each). Triple-Pin and
  P1P2-tied-to-p3 matched with zero mismatches on the first attempt.
  Chamber B1/B2 initially showed near-100% "mismatches" in my first-draft
  script — traced to my own script bug (it dropped the untouched copy of
  p2 from the constructed multiset, per the standing memory rule to
  always double-check the exact multiset construction before trusting a
  discrepancy); once fixed, 14,932 in-region trials, zero mismatches.
  All three certified.

**The covering-family claim is correctly, honestly NOT claimed as a
closure.** The file explicitly states the 20-member family (all 15
Bisect-Subset instances + the 6 new chambers + 3 prior chambers) hits
zero uncovered points on a 1577-point deterministic grid and a
3351-point random sample at n=3 case (b2), and explicitly flags this as
"strong evidence... but an exhaustive finite-vertex/case-split proof of
the covering property... was not completed this round — recorded
honestly as the remaining gap." This is accurate self-scoping; no
overclaim. Status should remain `partial` for this target, exactly as
the file's own Status field already reads.

**Certified this round:** `double-sandwich-chambers.md`,
`bisect-subset-lemma.md`, `triple-pin-and-chamber-b1-b2.md`.

---

## 3. `rank-pigeonhole-budget`

**Verdict: CHANGES REQUESTED (sub-case not closed) — file's own "Status:
solved" header is internally consistent (correctly scoped to Claim A
only, unchanged since round 8); `current.md`'s top-level Status was
already correctly `partial`, no fix was needed there.**

The round-24 dispatch fixed a real polarity bug the outline-reviewer had
flagged (reusing the certified max-direction `exchange-smoothing-vertex-
maximization` for an upper-bound need). The fix (§7.9) is a careful,
correct, breakpoint-by-breakpoint case analysis of the "T'-cuts-p4"
sub-case's 4 candidate values of b:

- b=0: reduces to A(T'), already closed via (star_{n-3}). Correct,
  I re-verified the reduction algebra.
- b=p4: **new Box-Endpoint Domination Fact** — I independently re-derived
  this from scratch (one line: on (c,M], T_{>b}=empty so A({b}∪T)=b-A(T)
  is affine with slope +1, so g(M)>=g(c) always) — correct, fully
  general, no ladder structure used. Certified as
  `lemmas/box-endpoint-domination-fact.md`.
- b=c1: recursion in the *same* (lower-bound) direction, correctly
  identified as not the flagged bug, genuinely open (the standing h(m)
  obstruction).
- b=c2: **the one genuine instance of the flagged direction issue**,
  reducing via `sharp-dominant-removal-identity` to A({c1}∪T''')=
  c1-A(T'''), needing the new inequality (7.9.1): A(T''')<=c1-f(n). The
  file proves by exact symbolic algebra that this does **not** follow
  from the certified cheap bound A<=Total(T''') (I independently
  re-derived the same symmetric-split counterexample: at c1=c2=p4/2,
  Total(T''')=p4-p_{n+1} via the certified R(tau)+tau_m=2tau_1 identity,
  and the needed bound p4/2 <= p_{n+1}-f(n) is false since
  p_{n+1}=f(n) identically, making the right side 0 < p4/2). Correct,
  and correctly left open (no false closure attempted).

This is solid, precisely-scoped, non-overclaiming work. The T'-cuts-p4
sub-case remains open as stated.

**On the Status-field question raised by the dispatch:** the file's own
header text says "Status: solved (Scope note: 'solved' here means this
approach's own target, Claim (A)...)" — this is unchanged from round 8
and is self-consistent; it does not claim the T'-cuts-p4 addendum or the
whole problem is solved. `current.md`'s `## Status` field already reads
`partial` (I did not need to change it). No correction to current.md's
Status field was required; I did add the round-24 narrative entry
recording this round's results (see below).

**Certified this round:** `lemmas/box-endpoint-domination-fact.md`.

---

## Files updated

- `results/imo-2026-03/current.md` — appended a Round 24 entry under
  Approaches tried recording all three builds' true status (including
  the greedy-halving-adversary overclaim downgrade); `## Status` field
  unchanged (`partial`).
- `results/imo-2026-03/lemmas/theorem-38-h1-exhaustive-closure.md` (new,
  scoped to the true m=1 result only, overclaim explicitly excluded).
- `results/imo-2026-03/lemmas/box-endpoint-domination-fact.md` (new).
- `results/imo-2026-03/lemmas/double-sandwich-chambers.md` (new).
- `results/imo-2026-03/lemmas/bisect-subset-lemma.md` (new).
- `results/imo-2026-03/lemmas/triple-pin-and-chamber-b1-b2.md` (new).
- `record_outcome` called for all 3 slugs (outcome: partial for all
  three; ranking left to the ranker's Elo mechanics, not touched
  directly).

## Recommendation for next round

`greedy-halving-adversary`'s highest-leverage next step is closing the
gap I found: either (a) prove that the joint (b,T')-vertex minimizer,
when T' leaves p4 untouched, is always at b=max(T')=p4 (ruling out
deeper ties analogous to this round's own h(m) finding), or (b)
explicitly extend Theorem 37's argument to cover deeper-tie candidates
the way Theorem 38 did exhaustively for h(1). Given 400k+ trials found
no counterexample, this is likely a "fill in the missing case" task, not
a dead end. `lp-duality-certificate` should attempt the actual finite
covering-family proof now that a strong 20-member candidate family with
zero numeric residual exists — the next natural step is a case-split /
vertex argument over case (b2)'s box showing every point falls in some
chamber's feasibility+success region, rather than further chamber
construction. `rank-pigeonhole-budget`'s (7.9.1) is now the single
sharpest open item in this whole front — worth dedicated attention next
round.
