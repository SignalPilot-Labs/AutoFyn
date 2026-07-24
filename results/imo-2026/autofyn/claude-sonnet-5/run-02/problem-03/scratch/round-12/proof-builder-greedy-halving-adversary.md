## imo-2026-03 — round 12 — greedy-halving-adversary

Target this round (per outline + outline-reviewer corrections): close
sub-case (c) of the ℓ(F)=2 branch of restricted Claim (B) — the mixed
regime v1≥p2>v2, reduced by the certified Lemma 25 to the single
inequality (‡): A({v2}∪G') ≤ (p1−v2)−f(n).

## Result: real, unconditional progress — new Proposition 26

**Fully closed the P=∅ (c=1, minimal-cut) instance of sub-case (c),
conditional only on L(n-1)** — the same recursion depth already used
elsewhere in Theorem P(n), no new dependency introduced. This is exactly
the case the round-12 outline itself flagged as "the only case that
matters."

Mechanism (all derived from scratch this round, per the outline-reviewer's
explicit instructions):
1. Used the certified `cross-term-identity-threshold` (Lemma 8) to write
   φ(t):=A({t}∪G') as an explicit closed form in the real variable t
   (purely algebraic, no legality of t needed) — this is the "continuous
   coordinate move" formula the outline wanted, derived fresh via Lemma 8
   rather than by citing Lemma 14 (Lemma 14 splits one element into two;
   it does not manifestly hand over the single-moving-coordinate formula,
   confirmed by direct derivation instead of assumption, exactly as the
   outline-reviewer required).
2. Showed D(t):=(target affine function)−φ(t) has derivative ≤0 a.e., so
   D is non-increasing; this reduces proving (‡) on the whole open
   interval (0,p2) to checking it only at the single boundary value t=p2.
3. Gave the t=p2 boundary an explicit continuity/limit argument (not an
   identification of cases, per the outline-reviewer's caveat): the
   formula is evaluated at t=p2 purely as a limit of the analytic function
   φ, not as an assertion that v2=p2 is itself a legal/attained instance
   of sub-case (c) (it isn't — v1=v2=p2 there, vacuous, exactly as flagged
   for sub-case (a) in round 11).
4. At t=p2, the certified `safe-window-lemma` gives the *exact* truncation
   identity ∫₀^p2 v_G' = A(G'), turning the needed upper bound into the
   single clean requirement A(G')≥f(n) at G''s *full* (n−1)-cut budget —
   which is exactly L(n−1) applied to the rescaled tail (`tail-self-
   similarity` + the certified cross-level identity, Lemma 12), not new
   content.

Independently verified by 6000 exact-`Fraction` trials (n=2..6):
`/tmp/round-12/check_subcase_c.py` — zero violations of the final bound,
the Lemma-25 identity, the boundary truncation identity, and the
monotonicity claim.

## Honest negative/diagnostic finding: P≠∅

Extended the same mechanism to F={v1,v2}∪P with P a nonempty exact
pairing (forces c≥3, per the outline-reviewer's corrected count). Found
(via Lemma 19) that P's presence is *invisible* to the closed form — a
clean fact in its own right — but the admissible boundary shifts to
t*=p2−Total(P)<p2 strictly, where the safe-window truncation identity no
longer applies (only a partial integral is available). Diagnosed precisely
*why* this is not "safely inherited from (†)" as the outline hoped: the
quantity needed at t* is exactly what Propositions 20–24 already analyze,
but every one of those results proves a *lower* bound on it, never the
*upper* bound sub-case (c) needs — a genuinely new, more sharply diagnosed
open item, distinct in direction (not just in case) from anything on
file. Numerically consistent with the overall conjecture (300 trials,
`/tmp/round-12/check_subcase_c_Pnonempty.py`, zero violations) but not
proved for n≥4.

Checked (not assumed) whether this threatens round 11's P(3) closure: at
n=3, P≠∅ forces the *entire* n=3 budget onto p1, so the tail is forced
untouched (no adversarial freedom) — reduced the open item to one finite
computation, worked out explicitly as a 3-piece piecewise-linear formula
for ψ(t), maximum exactly p2−f(3), never exceeded — independently verified
by 200,000 exact-`Fraction` trials
(`/tmp/round-12/check_n3_Pnonempty_edge.py`). So P(3) remains
unconditionally fully closed; the new open item bites only for n≥4.

## Status

partial (real, unconditional progress this round: a whole sub-case closed
at the same recursion depth as the rest of the theorem; the remaining gap
is narrower and more precisely diagnosed than before, not closed).

File updated: `/home/agentuser/repo/results/imo-2026-03/approaches/greedy-halving-adversary.md`
(new Proposition 26, updated Status/Approaches-tried/Current-best, updated
branch trace and base-case discussion in Theorem P(n)'s proof, updated
Open gaps item 4).

## Promotable lemma candidate

**Proposition 26** (closure of ℓ(F)=2 sub-case (c) at P=∅, conditional
only on L(n−1)) is a fully proved, general, reusable result — recommend
the reviewer certify it (parallel to how Proposition 25 was certified
last round) once cross-checked. The general closed-form fact used inside
it (Lemma 19 makes an ℓ(F)=1 residual's contribution to A(F∪G) invisible
to P's content) is also independently reusable and worth noting even
though the P≠∅ extension itself remains open.
