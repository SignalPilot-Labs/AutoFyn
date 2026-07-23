# proof-builder — caseB-matching — round 4 — imo-2026-03

## Verdict: Status = partial. Core lemma REFUTED; salvaged 3 general-n lemmas.

## Headline
**Lemma M (finite matching menu ⟹ A ≤ 1/D) is FALSE.** The matching menu (each original LB
piece cut at most once: "cut larger at smaller" + halve + keep) is insufficient for the Case-B
upper bound. Exact machine-verified counterexample (rational arithmetic):

- n = 3, a = (5144, 2787, 1386, 683)/10000, sum 1, all pieces > 1/15, all consecutive gaps > 1/15.
- Exhaustive menu search (all matchings × halve/keep, budget ≤ 3): best A = 683/10000 ≈ 0.0683 > 1/15.
- Fragment cascade (cut a₁ at a₂, then residual at a₃; 2 cuts inside a₁): A = 288/10000 ≈ 0.0288 ≤ 1/15.

The theorem itself (Case-B upper bound with GENERAL cuts) is TRUE and the answer c(n)=2ⁿ/D is
correct — full (fragment-allowed) optimization drives A→0 on hard-regime configs. Only the
menu framing fails. The outliner's and reviewer's "kill-switch passed, worst excess −1/D, full
slack" measured the GENERAL-cut optimum, not the menu optimum — the two were conflated. The menu
optimum exceeds 1/D on a positive-measure subset of the hard regime (n=3: ~7/3000 hard configs;
n=4: ~3/3000).

## What is rigorously proved (all general n, all correct) — see approach file
1. **Lemma X (XOR/parity evaluator).** A = μ(⊕_i [0,ℓ_i]); a cut of ℓ into (m,ℓ−m), m≤ℓ/2,
   toggles the A-set by [0,m]∪(ℓ−m,ℓ]. From certified Lemma R.
2. **Reduction 1 (halve-all).** Case B with p ≤ n pieces ⟹ halve all ⟹ A = 0. So Case B ⟹ p=n+1.
3. **Reduction 2 (close-pair).** p=n+1 and min consecutive gap d* ≤ 1/D ⟹ pair closest, halve
   rest ⟹ A = d* ≤ 1/D.
Together with Case A (Lemma H), the Case-B upper bound is now open ONLY in the **hard regime**:
p = n+1, all pieces > 1/D AND all consecutive gaps > 1/D.

## Why this matters for the field
The distinctive value of caseB-matching (induction-free FINITE matching-exchange) does NOT
exist — the finite menu is the wrong strategy class. The required strategy is fragment cascade
cutting = direct-constructive's interleaving Lemma I. So caseB-matching does NOT diversify away
from the shared Case-B wall; it collapses onto it (same hard core as U1). The field is again a
single framing at the wall.

## Recommendation to orchestrator/outliner
- The salvaged Lemma X + Reduction 1 + Reduction 2 are clean, general, and worth CERTIFYING —
  they cut the Case-B upper bound to the single hard-regime sub-case for all n, useful to every
  approach. Promote them.
- caseB-matching as framed is a dead-end. Either RETHINK it into a genuinely fragment-based
  finite optimization (a "cascade menu": allow peeling multiple copies off one piece — still a
  finite combinatorial object, strictly richer than the matching menu, and it DOES reach ≤1/D
  numerically), or retire it and route all Case-B effort through direct-constructive's Lemma I /
  IH(n) on the hard regime.
- The genuine hard core (hard regime: all gaps > 1/D) needs fragment cuts and is config-dependent
  (greedy cascade fails ~99% at n≥3; a single named strategy does not suffice). This is exactly
  the 3+-round U1 wall. A genuinely different framing is still needed there.

## Numerics run (all reproducible)
- Exhaustive menu vs 1/D over random Case-B: 0 fails (dominated by easy configs) — MISLEADING.
- Exhaustive menu over HARD-regime only: fails appear (n=3: 7/3000, n=4: 3/3000).
- Exact rational counterexample verified with fractions.Fraction.
- Full fragment optimization (Nelder-Mead multistart): A→0 on hard-regime n=3 (60 configs, 0 fails).
