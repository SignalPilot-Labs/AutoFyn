# Build report — lp-duality-split-polytope, round 10

## Correction to stale outliner claim
The round-10 outliner dispatch claims an "idx=1 Multi-Piece Necessity gap"
remains open for this approach. This is **stale**: `current.md`'s
"Round-8 update" and this approach file's own round-8 section already
record that idx=1 was fully closed in round 8 (a direct double-peel/
case-split proof, `lemmas/idx1-closure-and-full-multi-piece-necessity.md`,
certified). No idx=1 work was needed or done this round. This correction
is now stated explicitly at the top of the approach file (new "Round 10
update" section) so future rounds don't repeat the stale dispatch.

## Tool-supply role
Confirmed the Consecutive-Block AltSum Formula and Bottom-Block-Doubling
theorem are already certified in citable form
(`results/imo-2026-03/lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`,
certified round 9) — no further wiring needed. Checked
`global-lp-vertex-sufficiency.md` (as it stood mid-round); it hasn't yet
reached the evaluation stage that would invoke this tool.

## New result: Multi-Piece Sufficiency Theorem for the triangular family
Found and fully proved (exact arithmetic throughout, no numerics in the
proof itself) a general construction that closes round 9's own flagged
open question ("a construction using Θ(n) or more split pieces... was not
tried"): splitting n of the triangular family's n+1 landmarks (using the
*entire* cut budget, not just 2 pieces) via an explicit ε-tuned
construction achieves

    OddSum = 1/2 + (1/2)(c(n) - 1/2) < c(n)

for **every** n≥3 simultaneously, by one uniform formula. Key mechanism:
split landmarks N and N-1 to nearly cancel (leaving residual ε), split
every landmark j=2,...,N-2 into two exact halves (each an isolated
self-canceling pair), leave landmark 1 unsplit — the four resulting
copies of value "1" form an even block (also contributes 0). Net AltSum
= 2ε exactly, verified independently in exact `Fraction` arithmetic for
N=4..40 (37/37 exact matches, both via the construction's own formula and
via full direct sort-and-alternate computation from a completely
independently-written script).

Proved and stated in full generality:
- A general scaling identity (OddSum(X) = 1/2 + (d/2)AltSum(X/d)) valid
  for *any* legal response, not just Theorem A's single-piece-split
  framing.
- The Even-Block-Neutrality Lemma (general form: an isolated block of an
  even number of exactly-tied values contributes 0 to AltSum and doesn't
  disturb other elements' rank parity) — extracted as a standalone
  reusable fact (previously only used ad hoc inside Bottom-Block-Doubling).
- An induction proof that N(N+1)/2 ≤ 2^N-2 for all N≥4 (needed to bound
  the tuning parameter ε below 1/4).

This gives, for the triangular family specifically, a complete
Necessity+Sufficiency picture: no single piece suffices (round 8), but
this specific n-piece response always does (round 10, this file). It also
gives an exact, all-n confirmation of the qualitative phenomenon
`global-lp-vertex-sufficiency`'s Section 5 found only numerically at one
instance (n=6, a different partition): richer, ≥3-piece responses
succeed where narrower tool families fail.

A numerical (not exact) sanity check on LB's own geometric partition
confirms the analogous construction does *not* achieve a comparable margin
there (ratio ≈1 at the threshold across n=3,4,5) — consistent with the
geometric partition being the actual extremal case, and confirming this
finding is a genuine structural feature of the triangular family's AP
landmark spacing, not a universal trick that would otherwise contradict
c(n)'s known value.

## Status
Approach file Status remains `partial` — this closes the triangular
family's own sufficiency question completely, but the whole problem's
general balanced-region upper-bound direction (needed for all balanced
partitions, not just this one AP family) remains open, owned elsewhere
(`global-lp-vertex-sufficiency`, `universal-halving-adversary`) per
`current.md`.

## Promotable lemmas proposed for certification
- **Multi-Piece Sufficiency Theorem for the triangular family** (new,
  full proof, exact-arithmetic verified N=4..40).
- **Even-Block-Neutrality Lemma** (general form, standalone, reusable).

File updated: `results/imo-2026-03/approaches/lp-duality-split-polytope.md`
