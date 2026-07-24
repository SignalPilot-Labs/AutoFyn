# Proof review — imo-2026-03, round 2

Reviewed build set: `greedy-halving-adversary`, `smoothing-compactness-certificate`,
`self-similar-potential-certificate`. All independently re-derived load-bearing
computations with exact-`Fraction` Python scripts (not just re-read arithmetic);
scripts and result counts are quoted below for each claim checked.

## 1. greedy-halving-adversary

**Verdict: CHANGES REQUESTED. Status: partial (matches builder's self-report).**

New claims this round: Lemma 7 (dominant-element-removal identity
$A(S)=M_1-A(S\setminus\{M_1\})$ when $M_1$ exceeds half the total), Lemma 8
(general cross-term identity $A(F\cup G)=A(F)+A(G)-2\int_0^r uv$, no
dominance assumption), Lemma 9 (scaling $A(\lambda S)=\lambda A(S)$),
Proposition 10 (decomposition for arbitrary cut-budget split $c$), and a
sharpened, precisely-stated "missing inequality" as the located open gap.

Independent verification:
- Lemma 7: 3000 random multisets (size 1–6), exact `Fraction` arithmetic,
  checked dominance condition then compared both sides directly. **0
  mismatches.**
- Lemma 8: 1000 random pairs of multisets (size 1–5 each), computed both
  sides via exact breakpoint integration. **0 mismatches.**
- Lemma 9: immediate algebraic identity, trivially correct.
- Key Lemma ($p_1\le 2r$ for the ladder, all $n\ge1$, equality at $n=1$):
  re-derived the algebra by hand ($3p_1\le2\iff 2\le2^n$) — correct.
- The "weak bound is too weak" claim (dropping the cross term gives a bound
  below 0 for $n\ge1$): re-derived the arithmetic $2f_1-p_1-r$ by hand,
  confirms negativity near the case boundary — correct, and honestly framed
  as a genuine negative finding rather than papered over.

All new lemmas check out exactly on independent re-derivation. This is real,
reusable general-purpose machinery (Lemma 7/8 need no ladder-specific
structure at all) that strictly generalizes last round's Lemma 6. However,
the actual crux — the general lower bound for $c\ge1$ and the general upper
bound for arbitrary $n$ — remains open. The "missing inequality" is
precisely stated and numerically well-supported (60000 random-cut trials
across $n=1,2,3$, no violation found) but genuinely unproved; the builder
does not claim otherwise. No overclaim found. Gap for next round: prove the
cross-term/anti-concentration inequality in Proposition 10, or find that it
is false and a different mechanism is needed.

## 2. smoothing-compactness-certificate

**Verdict: CHANGES REQUESTED (approach-level Status stays partial, since
general $n$ is untouched) — but the $n=2$ sub-claim is independently
verified as fully correct and is recorded as a milestone.**

This is the flagged claim to check carefully: "closed the 3 remaining n=2
lower-bound compositions (1,1,0),(1,0,1),(0,1,1) exactly and symbolically,
zero numerics."

Independent verification:
- Re-derived the closed-form identities by hand from the sorted-order case
  splits in the write-up: $\Phi=5-\mathrm{median}(p_2,r_1,r_2)$ for
  $(1,0,1)$ and $\Phi=5+q_2-\mathrm{median}(q_2,r_1,r_2)$ for $(0,1,1)$,
  using the max+min = total − median identity for 3 numbers. Algebra
  checks out.
- Tested both identities against a direct sort-and-alternate-sum computation
  of $\Phi$ over 20000 random rational instances each (exact `Fraction`
  arithmetic, uniformly sampled valid splits). **0 mismatches in both
  cases.**
- Case $(1,1,0)$: re-derived the 4-way case split on where the smaller
  $P$-fragment $p_2$ falls relative to the fixed chain $q_1\ge1\ge q_2$;
  checked the claimed boundary-continuity of $\Phi$ at the 3 case seams by
  hand (matches). Ran a 50000-trial random search over the composition's
  parameter space; minimum found was $\approx 4.00001$ (units of $1/7$),
  consistent with the claimed exact infimum $4$, attained at $p_1=p_2=2$.
- Ran an independent 60000-random-trial Monte Carlo search (grid + random
  cuts, not restricted to any one composition family) over all 10
  compositions for the $n=2$ ladder: minima found were $5.0, 4.0, 5.0,
  \approx4.5, 4.0, \approx5.0, \approx4.5, \approx4.0, \approx4.0,
  \approx4.5$ for the 10 compositions in order — matches the claimed exact
  values $5, 4, 5, 4.5, 4, 5, 4.5, 4, 4, 4.5$ in every case.
- Independently re-verified the round-1 upper-bound argument's algebra too
  (strategies A, C, D, E formulas checked exactly on 30000 random instances,
  0 mismatches; strategy B checked approximately via a small-$\varepsilon$
  perturbation since the extremal choice $z=0$ is a boundary limit, not an
  exact valid cut — confirmed $\Phi_B\to p$ correctly; the Region 1/Region 2
  LP-contradiction algebra was re-derived by hand and matches exactly).

**Conclusion: the claim is correct.** Both directions of $c(2)=4/7$ are now
established by fully symbolic, non-numeric arguments (numerics used only as
pre-checks, never as proof steps). This is a genuine milestone: n=2 is fully
solved as a base case. Minor rigor note (does not affect correctness): the
Strategy B feasibility write-up uses non-strict inequalities and an
extremal choice $z=0$ that is not itself a legal cut (a genuine 3-piece
split needs all parts strictly positive); at the single boundary point
$p=1/2$ this makes Strategy B's exact attainability momentarily unclear —
but this is harmless because Region 2 ($p\le1/2$, using strategies A, D, G
instead of B) already covers $p=1/2$ redundantly, so the final upper-bound
theorem is unaffected. Flagging this for the builder to tighten the wording
next time (say $p>1/2$ for B's exact feasibility) but it is not a gap in the
proved result.

Since the approach's own overall target (general $n$) remains untouched, the
Status for this approach file correctly stays `partial`, matching the
builder's own honest self-report — no overclaim. Recorded as
`verified-milestone` in the ranker (the sub-result is a fully closed,
reviewer-certified base case, even though the approach as a whole is not
solved).

## 3. self-similar-potential-certificate

**Verdict: CHANGES REQUESTED. Status: partial (matches builder's self-report).**

First build this round (previously only an outline). New claims: Lemma A
(corrected self-similar scaling identity $f(n)=r(n)f(n-1)$, fixing a broken
recursion flagged by the outline-reviewer), Lemma B (general above-threshold
formula $A_1=\max(f_1-r,0)$ for arbitrary cut-budget split $c$), Lemma C
(trivial budget-monotonicity), full closure of the $c=0$ sub-case (matches
already-certified `untouched-top-piece-lower-bound`), and a negative result
for $c\ge1$ (mass-based interleaving bound provably too weak).

Independent verification:
- Lemma A: re-derived by direct fraction algebra for $n=1,\dots,7$ in a
  script. **Exact match in every case**, including the $n=1$ boundary case.
- Lemma B: 500 random fragmentations of $p_1$ per $n\in\{1,2,3,4\}$, direct
  breakpoint-integral computation of the above-threshold contribution vs.
  the claimed closed form $\max(f_1-r,0)$. **0 mismatches.**
- Lemma C: trivial, immediate, correct.
- The negative result (naive bound degrades to $A(S)\ge f(n)-p_1<0$, hence
  useless): re-derived the arithmetic by hand — correct, $f(n)-p_1<0$ for
  every $n\ge1$ since $p_1>1/2>f(n)$.

All new lemmas check out exactly. This is a genuine, correct, and honestly
reported first build: it identifies (independently of `greedy-halving-adversary`)
essentially the same core obstruction — a rank/interleaving-sensitive
quantity that a pure mass-counting bound cannot control — via a different
route (self-similar potential framing rather than direct threshold-splitting).
This convergence is useful corroborating evidence that the obstruction is
real and not an artifact of one approach's specific machinery, but it also
means this approach has not yet found a way to avoid the wall the other two
approaches are also stuck on. No overclaim found; the gap ($1\le c\le n$,
general $n$) is honestly disclosed as open, with a correct diagnosis of why
the obvious fix (mass-based bound) cannot work.

## Certified lemmas (added to `results/imo-2026-03/lemmas/`)

All held to the full bar (statement correct, no stronger than proved,
independently re-derived/verified this round):
- `dominant-element-removal-identity.md` (Lemma 7, greedy-halving-adversary)
- `cross-term-identity-threshold.md` (Lemma 8, greedy-halving-adversary)
- `alternating-sum-scaling.md` (Lemma 9, greedy-halving-adversary)
- `n2-lower-bound-full-closure.md` (3 new n=2 cases, smoothing-compactness-certificate)
- `ladder-self-similarity-constant.md` (Lemma A, self-similar-potential-certificate)
- `above-threshold-formula-arbitrary-split.md` (Lemma B, self-similar-potential-certificate)
- `budget-monotonicity.md` (Lemma C, self-similar-potential-certificate)

No lemma was rejected this round — everything proposed as promotable passed
independent verification.

## current.md

Updated to reflect the combined strongest state: Status remains `partial`
(problem asks for general $n$, still open); n=1 and n=2 are now both fully
closed (n=2 newly, both directions, zero numerics — the round's headline
result); general-$n$ open gap is now stated more precisely (a specific
cross-term/anti-concentration inequality that two independent approaches
converge on) than at the start of the round. See
`results/imo-2026-03/current.md`.

## Ranking outcomes recorded

- `greedy-halving-adversary` → `advanced` (real new general lemmas proved,
  gap sharpened from vague to precise).
- `smoothing-compactness-certificate` → `verified-milestone` (n=2 fully
  closed both directions, reviewer-verified).
- `self-similar-potential-certificate` → `partial` (correct first build,
  real progress, converges onto the same open obstruction as the sibling
  approaches rather than a novel one).

## Observation for the outline-reviewer

All three approaches now independently point at the *same* precise
combinatorial obstruction for general $n\ge3$: controlling the interleaving
of Xiang Yu's top-piece fragments with his tail refinement in sorted rank,
not just their total mass. Three different framings (explicit strategy +
potential induction, static template+LP, self-similar recursion) converged
here — this is a real signal about where the true difficulty lives, not
just a shared blind spot from too-similar approaches. Worth considering
whether next round should try a genuinely different framing (e.g., an
explicit matching/pairing combinatorial argument on which subsets of
original pieces can be near-matched under a budget of $n$ cuts — flagged
already in `greedy-halving-adversary`'s Open gap 1 as the right shape) rather
than a fourth variant of "integral/threshold decomposition," per the
CLAUDE.md shared-gap-plateau rule.
