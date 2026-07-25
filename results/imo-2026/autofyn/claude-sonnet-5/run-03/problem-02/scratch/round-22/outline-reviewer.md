# Outline review — round 22 — imo-2026-02

## Context

Round 21's proof-reviewer caught a fourth false `solved` claim on
`coordinate-bash-resultant-boundary-pointwise-tangent`: the assembled "Full
proof" only ever split `\beta_1` into two cases — (a) `\beta_1\le\beta_0(A)`
(closed, phantom-gap argument) and (b) `\beta_0(A)<\beta_1<\gamma` (closed,
round 20) — but `\beta_1` (defined by `\cos\beta_1=\sqrt{X_0}`,
`\beta_1\in[0,\pi/2)`) need not lie in `(0,\gamma)` at all: whenever
`Y(\gamma)\ge0` (`\beta_1\ge\gamma`), neither case's write-up covers it, and
this happens in ~51% of the domain-nonempty region. This round's outline
proposes to splice in a Case (c) closing this exact gap by citing
`coordinate-bash-resultant-boundary.md`'s Theorem 16.2 "first branch"
(`Y(\gamma)\ge0\Rightarrow G(\beta)>0\ \forall\beta\in(0,\gamma)`), which was
already proved and certified back in round 9 and has not been re-opened
since. Given this file's history (4 caught false-solved claims, rounds
17/18/19/21), I independently re-derived every load-bearing piece of the
splice from raw definitions before endorsing it — not just re-read the
outline's prose.

## Independent verification performed (fresh sympy/mpmath, this round)

1. **`G ≡ 2K_c − f` exactly.** Confirmed by direct substitution: with
   `K_c=2\sin A\sin(A+B)`, `P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`,
   `Q=-\sin A\sin B`, `f(\beta):=K_c+P\sin\beta+Q\cos\beta`, and
   `G(\beta):=K_c-P\sin\beta-Q\cos\beta` (as used in the tangent file's Step
   2 and elsewhere), this literally equals `2K_c-f(\beta)` by algebra — not
   a nontrivial identity to prove, just bookkeeping. Cross-checked against
   `coordinate-bash-resultant-boundary.md`'s own `f,K` (round 9's
   `f(\beta)=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)`,
   `K=2\sin A\sin(A+B)`): `sympy.expand_trig` gives residual `0` for
   `f_tangent-f_boundary` and (once the naming is reconciled — boundary's
   `K` and tangent's `K_c` are the SAME quantity `2\sin A\sin(A+B)`, not
   off by a factor of 2 as a first careless reading suggests) residual `0`
   for `G_tangent-(2K_{boundary}-f_boundary)`. **Verified exact.** Flag to
   the builder: the naming collision (`K` in the -boundary file =
   `K_c` in the -tangent file) is a real source of the kind of silent error
   this population has hit before — the splice write-up MUST state this
   explicitly rather than silently switching symbols.
2. **Theorem 16.2's core closed form** `2K-f(B)=\sin(A+B)(2\sin A-\sin B)`
   (with `\gamma:=B`) — verified exact via `sympy.expand_trig`, residual 0.
3. **The sign-of-`(2\sin A-\sin B)` sub-mechanism** the outline flags as its
   own self-check item (i): the identity
   `\cos B(2\sin A-\sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-\cos B)`
   for `A=\pi-2B-\delta` — verified exact (residual 0). Checked the
   potential circularity concern by hand: `\delta<B` is not assumed for
   free (a naive check shows `\delta=C-B` need not be `<B` in general) —
   but the file's own text (already established, not new this round)
   proves `\delta<B\iff A+3B>\pi\iff Y(\gamma)\ge0`, i.e. **exactly the
   Case (c) hypothesis itself does the work of forcing `\delta<B`.** This
   is NOT circular: `Y(\gamma)\ge0\Rightarrow\delta<B\Rightarrow\cos\delta
   >\cos B\Rightarrow$ RHS`>0`\Rightarrow$ (combined with `Y(\gamma)\ge0`
   feeding the LHS's subtracted term) `\cos B(2\sin A-\sin B)>0`, and
   `\cos B>0` (`B<\pi/2`) gives `2\sin A-\sin B>0`. Confirmed sound.
4. **The exact witness from round 21's rejection** (`A\approx1.5540,
   B\approx0.7466`, the triangle the proof-reviewer used to prove the gap
   is real and common) genuinely falls into the proposed Case (c):
   independently recomputed `\beta_0(A)\approx0.529<\gamma\approx0.747<
   \beta_1\approx1.483`, and `Y(\gamma)\approx1.062>0` — exactly the
   Case-(c) hypothesis. A 20,000-sample sweep of `G(\beta)` over
   `\beta\in(0,\gamma)` at this witness gives min `\approx0.984>0`,
   consistent with Theorem 16.2's conclusion. **This is the exact
   configuration the splice is designed to close, and it does.**

Conclusion: the splice's mathematical content is sound and rests entirely
on an already-certified 12-round-old theorem (Theorem 16.2, round 9),
reused verbatim, not new computation. This is the lowest-risk kind of
"closing move" this file has attempted in its 4-round string of false
claims — all four prior false claims involved either an unproved numeric
coincidence (round 17), a wrong sub-interval citation (round 18), a
necessary-but-insufficient sub-lemma (round 19), or a silently-omitted
third case (round 21, the one this round fixes). This round's fix is a
citation to a fact that has been proved and independently reproduced
multiple times since round 9 — genuinely lower risk than the prior four
attempts, but NOT zero risk, precisely because "looks obviously right" was
also true of all four prior attempts at the time.

## Verdicts

**`coordinate-bash-resultant-boundary-pointwise-tangent` — APPROVE (with
mandatory build-time conditions).** The outline's proposed Step 3′ (Case
(c)) is mathematically correct and closes exactly the gap round 21's
reviewer identified, using already-certified machinery with no new
symbolic risk. However — **per the outliner's own "Open gaps" checklist
(items i–v) and this file's own 4-false-claim history, the builder MUST**:
- Re-trace the ENTIRE assembled "Full proof" end to end (Steps 1–5 plus the
  new Step 3′), not just verify the new paragraph in isolation. In
  particular check: (a) the trichotomy `{β1≤β0(A)}∪{β0(A)<β1<γ}∪{β1≥γ}` is
  literally exhaustive as re-derived (it is, given domain-nonempty — a pure
  case split on two ordered reals — but restate this explicitly rather than
  asserting it); (b) Steps 4–5 (Reduction Lemma / MVT-Lipschitz, Case (b)
  only) are not silently invoked in Case (a) or Case (c)'s write-up; (c)
  the isosceles/degenerate edge cases and all standing non-degeneracy
  hypotheses (K≠L, genericity) are still respected in the assembled text.
- Independently re-derive (fresh sympy, not reused scripts) both `G≡2K_c-f`
  and Theorem 16.2's `2K-f(γ)=sin(A+B)(2sinA-sinB)` closed form — do not
  merely cite; write these as explicit, self-contained Facts in the tangent
  file itself (currently the `G=2K_c-f` identity is only informal prose per
  the outliner's own note — fix this).
- Run one fresh, independently-seeded large sample sweep (≥100k) over the
  literal final assembled statement `(I)∧(II)` across all three cases as a
  single combined check (not per-case), specifically targeting the
  `β1≥γ`/`Y(γ)≥0` boundary region and its immediate neighborhood (where the
  previous omission lived) for any residual mismatch.
- Do **not** write `Status: solved` until all of the above is done and the
  full chain is retraced one final time as a sanity pass. Given the
  history, treat any temptation to declare `solved` after just checking the
  new paragraph as the exact failure mode that has recurred 4 times.

**`coordinate-bash-resultant-boundary-pointwise-tangent-via-T` — CHANGES
REQUESTED / low priority.** No new content proposed this round beyond
"insurance." Correctly flagged by both round-22 explorers as likely moot if
the tangent splice succeeds (Case (b) is already independently closed via
`t-nonnegative-on-case-b-residual-domain.md`). Sound as population
insurance but not worth a build slot this round given the tangent splice
is close to a full closure and needs the round's attention.

**`ptolemy-trig-identity-synthetic` — APPROVE (diversity, exploratory).**
Already registered (elo 1420→1403 after this round's ranking, never
built). The proposed monotonicity/convexity lever (`\alpha(\theta)` vs
`\beta_L(\theta)` direct comparison) is honestly scoped as untested and
explicitly avoids the five already-exhausted resultant/discriminant/Vieta
reformulations of Ψ (correctly not re-litigating those). Worth a single
exploratory build to keep genuine framing diversity alive in the
population per CLAUDE.md, especially since the coordinate family may be on
the verge of a full solve and it would be a mistake to let the whole
population collapse onto that one route with zero live alternative if the
splice turns out (a 5th time) to have a residual gap.

## Diversity note

The population remains dominated by the coordinate/resultant/tangent
cluster (7 of 15 registered approaches share that lineage). This round's
build set deliberately keeps `ptolemy-trig-identity-synthetic` alive as the
population's only currently-live, structurally distinct route, per
CLAUDE.md's standing diversity guidance — if the tangent splice's Case (c)
turns out to have yet another silent gap, the population should not be
caught with zero alternative in flight.

## Ranking

Ran `update_ranking` with comparisons anchoring both stale approaches
(`coordinate-bash-resultant-boundary-pointwise-tangent`,
`spiral-similarity-bootstrap`, both `stale=True` from round 21's unfolded
outcome) against established siblings: tangent beats via-T, spiral, and the
cold-start ptolemy-synthetic (closest to a full solve, most rigorously
re-verified this round); spiral beats ptolemy-synthetic (spiral has two
certified lemmas and a real structural negative result vs. zero built
content); via-T beats -sos (via-T has a certified cross-check lemma, -sos
has only diagnostics) and beats ptolemy-synthetic. All `stale` flags
cleared. No new approach to register this round (ptolemy-trig-identity-synthetic
was already registered in an earlier round); no copy requested by the
outliner this round.

Post-ranking order (best-first): coordinate-bash-resultant-boundary-pointwise-tangent (1844),
coordinate-bash-resultant-boundary-pointwise-tangent-via-T (1778),
coordinate-bash-resultant-boundary-pointwise (1659, unchanged),
coordinate-bash-resultant-boundary (1652, unchanged),
spiral-similarity-bootstrap (1534), ..., ptolemy-trig-identity-synthetic (1403).

build set: coordinate-bash-resultant-boundary-pointwise-tangent, ptolemy-trig-identity-synthetic
