# proof-builder report: bijective-mersenne-pairing (round 6)

**Verdict: DEAD END, abandoned at the go/no-go gate as instructed.**

## What was tested

Per the outline, ran the go/no-go test on $n=2$ FIRST, using exact
`Fraction` arithmetic (no floats), on the ladder $(p_1,p_2,p_3)=(4,2,1)$
(units of $1/7$), target $A(S)\ge1$.

1. **Degenerate/extremal sanity check** — composition $(1,1,0)$ at its
   known infimum ($a=2,b=1$, i.e. exactly the cascading-halving family's
   $R_2$): $S=\{2,2,1,1,1\}$. Trivially consistent, but this case doesn't
   actually test the pairing mechanism (even region contributes nothing).

2. **The outline's own required test — a generic, non-extremal response**
   — composition $(1,1,0)$ with $a=1.5,b=0.5$:
   $S=\{5/2,3/2,3/2,1,1/2\}$. Even region: length $1/2$. Odd regions:
   $1/2,1/2,1$. No forced $2{:}1$ relationship (the coincidental match to
   $1$ is just $p_3$, not a consequence of any doubling rule).

3. **Decisive falsifying case** — composition $(2,0,0)$, Xiang Yu spends
   both points on $p_1$ with arbitrary cuts: $p_1=4\to\{3,7/10,3/10\}$,
   $p_2=2,p_3=1$ untouched. $S=\{3,2,1,7/10,3/10\}$. Even regions:
   lengths $\{2/5,1\}$. Odd regions: lengths $\{3/10,3/10,1\}$. **No
   pairing exists where an odd region's length is exactly $2\times$ (or
   $1/2\times$) an even region's length.** $A(S)=8/5\ge1$ holds (the
   *bound* is fine), but the proposed *mechanism* (pair regions by a fixed
   $2{:}1$ length ratio, mirroring `ladder-self-similarity-constant`) is
   simply not present in this generic, equally legal response.

## Why it fails

The $2{:}1$ ratio in `ladder-self-similarity-constant` is a fact about
the specific geometric ladder $p_i=2p_{i+1}$ combined with the specific
cascading-*halving* Xiang Yu response family
(`cascading-halving-family-characterization`) — both are built by exact
repeated halving, so of course a $2{:}1$ ratio shows up. It is not a
structural fact about the alternating-sum functional $A$
(`integral-alternating-sum-formula`), nor about generic legal responses,
which may place cuts at arbitrary real points with no relation to any
power of $2$. The approach's entire mechanism presupposes this ratio, so
it has no purchase once cuts are generic — confirmed by exact fraction
computation on two independent generic test cases at $n=2$, the smallest
nontrivial case.

## Action taken

Per the outline's explicit stop condition, abandoned the approach without
proceeding to steps 2–4 (generalizing to $n=3$/general $n$, deriving the
upper bound). Wrote up the full computation (all three test cases, exact
fractions, tables of region/length/parity) in
`results/imo-2026-03/approaches/bijective-mersenne-pairing.md` under
`## Approaches tried` and `## Current best`, so this exact mechanism is
not re-attempted. `## Status` set to `unsolved` (no correct partial result
established — this is a clean negative, not a partial proof).

## Recommendation for future rounds

If the "bijective/pairing" idea is revived, it should pair *pieces* by
some invariant other than a literal length ratio (e.g. by count/rank
alone, in the spirit of the already-certified `odd-run-reduction-lemma`),
not by insisting paired regions' lengths differ by exactly a factor of 2.
This approach should be marked dead in the ranker and not resampled in
this form.
