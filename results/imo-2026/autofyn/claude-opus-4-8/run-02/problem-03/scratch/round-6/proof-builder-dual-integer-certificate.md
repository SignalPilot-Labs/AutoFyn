# Build report — dual-integer-certificate — round 6 — imo-2026-03

Status: **partial** (honest). Wrote `results/imo-2026-03/approaches/dual-integer-certificate.md`.

## What I proved (complete, rigorous)
- **Lemma DUAL (dual value identity).** For `U∈ℤ^{(n+1)×p}` with `ker U=0`, `Uw=b`, any `s`:
  `Uᵀλ=s` is ℚ-solvable; for every solution `λ`, `λᵀb = sᵀw` (invariant across `λ`); hence
  `f(P*) = sᵀw = Σ_k λ_k 2^k`. Proof = associativity `λᵀUw=(Uᵀλ)ᵀw` + `ker Uᵀ ⟂ b`. Fully rigorous.
  Promotable.
- **Proposition R (reduction).** `f(P*)≥1` follows from Gap D (∃ integer `λ`) + Positivity (`f≠0`),
  using the certified `f≥0`. Clean.
- Imported the certified reduction, S-core (`ker U=0`), block formula (`f=sᵀw`, `Uw=b`), and UB.

## What remains open — and the decisive new finding
The gate asked: does Gap D genuinely bypass Gap A AND Gap B? My numerics give a sharper, partly
negative answer than the gate's spot-check suggested:

**Gap D (integer solvability of `Uᵀλ=s`) is FALSE as a universal S-core property.**
Counterexample: the reachable tied refinement `{2,4/3,4/3,4/3,1}` of `W_2` (cut piece `4` into
three thirds; `f=5/3`) is S-core (`det U=±3≠0`) but `Uᵀλ=s` forces `3λ_2=−1`, no integer solution;
gcd of the maximal minors of `U` is `3`. So:
- Gap D is NOT a pure lattice/incidence fact — a proof MUST invoke minimality of `P*`. It therefore
  does NOT cheaply escape the primal route's difficulty class, contrary to the "clean bypass" hope.
- It IS still a genuinely different OBJECT: the condition is `s∈Uᵀℤ^{n+1}` (sufficient: gcd of the
  `p×p` maximal minors of `U` = 1, "(GCD-1)"), which is strictly weaker than primal `det=±1`
  (round-5 `[[1,2],[2,1]]`: primal det `−3` fails, dual `s=(1,−1)` solvable `λ=(−1,1)`). So it is a
  legitimately distinct framing, just not an easier one.

**Sharpened residual (the structural fact needed):** at a Φ-max global minimizer, minimality forces
(GCD-1) — the maximal minors of `U` are coprime. Mechanism to try: laminar/rank-contiguity peeling
excluding a "concentrated" block (one column with multiplicity `≥2` in a single piece coprime to
nothing), which is exactly what makes the `5/3` config fail. Unproven.

**Positivity (`f≠0`) is a SECOND independent gap** (as the gate warned). `f∈ℤ` is only available
through Gap D, so it can't be gotten circularly. Sub-cases: (all-even) = certified bisect-all,
should need `≥n+1` cuts but only `n` available — reduces to an unwritten budget lemma "`f=0` needs
`≥n+1` cuts" (verified by hand n=2); (odd-cancellation among ≥3 blocks) genuinely hard. The
outliner's "λ_0 odd ⇒ f odd" idea is NOT invariant (λ non-unique; f mod 2 is choice-free), so that
specific positivity mechanism does not work as stated.

## Gap D exhaustive-ish check on n≤4 (evidence)
Sampling S-core tied configs via random integer `U`, solving `Uw=b` for positive distinct `w`:
- n=2: Gap D holds on ALL 9 configs with `f=1`; fails only at `f>1` (the `5/3` config). gcd dist at
  minimizers = 1.
- n=3: Gap D holds on ALL 34 sampled `f=1` tied configs; failures only at `f≠1`.
- n=4: sampler too sparse for tied minimizers (Uw=b rarely gives valid distinct positive w); no
  counterexample found, gate independently reports 0 failures / min f=1.
Pattern: at minimizers (GCD-1)⇔`f∈ℤ`⇔`f=1`. Consistent with the conjecture, not a proof.

## Spec concerns
- The approach is a valid, genuinely-different member of the population (different wall: lattice
  coprimality vs det±1). But its two gaps are entangled with minimality, so it is NOT closer to a
  solve than self-similar — it is a diversity hedge with a clean identity, not a near-finish.
- Recommend the reviewer CERTIFY Lemma DUAL and the "Gap D not universal" fact (both fully proven),
  and record Gap D's minimality-dependence so no future round retries a minimality-free lattice
  closure.

## Proposed lemmas for certification
1. **Lemma DUAL** — statement + proof in §1 of the approach file. Unconditional, reusable.
2. **Fact: Gap D not universal** — the `{2,4/3,4/3,4/3,1}` counterexample (§3). Prevents a dead-end
   retry.
