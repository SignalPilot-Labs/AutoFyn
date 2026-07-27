## Goal

Solve **IMO 2026 Problem 5** (`imo-2026-05`, difficulty 8, algebra, answer_type=characterization):
Find all $f:\Rpos\to\Rpos$ with $\sqrt{(x^2+f(y)^2)/2}\ge (f(x)+y)/2 \ge \sqrt{xf(y)}$ for all $x,y>0$.

- **Metric:** proof-reviewer verdict on `results/imo-2026-05/current.md` `## Status`.
- **Eval command:** read `results/imo-2026-05/current.md` `## Status` + `results/imo-2026-05/approaches/.ranking.json`; a proof-reviewer APPROVE = solved.
- **Baseline:** no approaches yet (round 1). Conjectured answer: $f(x)=x+c$, $c\ge 0$ (equality in both QM-AM and AM-GM chains). Uniqueness is the crux.
- **Target:** `solved` — complete rigorous proof that the family is exactly $\{x\mapsto x+c : c\ge 0\}$: (a) exhibit and verify the family; (b) prove no other $f$ works, all cases.
- **Constraints:** prose Markdown, no Lean; name tools via knowledge_base.md; no skipped cases; verify the final characterization by substitution.

## Goal Updates

## Eval History

- **Round 1 (setup+explorers):** workspace created, 2 explorers mapped terrain (structural + crux). Status `unsolved`. No approaches built.
- **Round 2 (BREAKTHROUGH):** Founded field of 4 approaches (outliner), ranked (reviewer), built 3 (orbit-monotonicity-sandwich, density-contradiction, master-sos-identity). proof-reviewer verdicts:
  - **orbit-monotonicity-sandwich — APPROVE, SOLVED.** Full verified proof: orbit invariance $g\circ f=g$; $g\ge0$ (codomain sign kill); **master squeeze** $|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^2$ (SOS, sympy-verified, equivalent to chain both directions); asymptotic pinning along arithmetic orbit forces $\lim_{x\to\infty}g(x)=\alpha$ for every positive value $\alpha$ of $g$ ⇒ all positive values coincide at single $\beta$; $g\equiv\beta$ on a tail; boundary contradiction at $q=\sup\{g=0\}$ ($\beta(\beta+4q)\le\beta^2\Rightarrow q\le0$, contradicting $q>0$). All edge cases covered (no-zeros = conclusion; no-positive-value = $g\equiv0$; nonconstant-$g>0$ ruled out by Cor). Answer $\boxed{f(x)=x+c,\ c\ge0}$, exhibit verified.
  - **master-sos-identity — partial, CHANGES REQUESTED.** Master Squeeze Lemma PROVEN both directions, sympy-verified, CERTIFIED into `lemmas/master-squeeze.md`. Direct algebraic kill honestly open (optimization "bound" correctly retracted as non-result).
  - **density-contradiction — partial, CHANGES REQUESTED.** Correct weaker squeeze (independently derived, denominator $\ge a+b>0$ correctly defuses Kronecker rate concern); correct rational-ratio R1/R2 kill. Two gaps: (A) irrational-case Kronecker target off by $\alpha$ ($c_0=a+\alpha-b$ should be $a-b$); (B) Stage B $a-b\in\beta\mathbb Z$, $k\le-1$ sub-case sign error. Also erroneously rejected master squeeze as false (it is a true theorem equiv to the chain) — non-propagating (proof uses own weaker squeeze).
  - **extremal-infimum — CHANGES REQUESTED (sent back to outliner), not built.**
- **Status: SOLVED.** `current.md` `## Status` = solved, full proof present.

## Rules

- ALWAYS: treat the **master squeeze** $|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^2$ as a TRUE theorem EQUIVALENT to the original chain (both directions), via SOS identities $A+B=2(x-f(y))^2$, $A-B=2(g(x)-g(y))(g(x)+g(y)+2x+2y)$ + $A,B\ge0\Rightarrow|A-B|\le A+B$. Certified in `lemmas/master-squeeze.md`. (round 2)
- NEVER: present a "counterexample" to a chain$\Rightarrow$squeeze lemma using a candidate $f$ that does NOT satisfy the original chain — the lemma is an implication; test the chain (both $A\ge0$ and $B\ge0$) at the point first. (round 2 — density-contradiction's bogus "$a=1,b=3$" rejection)
- ALWAYS: for a Kronecker/equidistribution squeeze, the cross-distance is $b-a+m\beta-(n+1)\alpha$ (note the $n+1$ from $f(y)=a+(n+1)\alpha$), so the Kronecker target must be $a-b$, NOT $a+\alpha-b$. The RHS is quadratic in cross-distance; the "denominator $\ge a+b>0$" only defuses the rate concern because the bound is $\mathrm{num}^2/(a+b)$ with $\mathrm{num}\to0$. (round 2)
- ALWAYS: enumerate edge cases explicitly before declaring a uniqueness proof complete — for this problem: "$g$ has no zeros", "$g$ has no positive value", "$g>0$ everywhere nonconstant". orbit-monotonicity covered all three. (round 2)
- ALWAYS: re-derive (not cite) any shared lemma a builder's proof depends on; verify SOS/identity lemmas with sympy before trusting them. (round 2)

## State

### Done
- (round 1) Setup: read CLAUDE.md/README/problems.jsonl/knowledge_base.md; installed numpy/scipy/sympy; created workspace `results/imo-2026-05/{approaches,lemmas}` and `current.md`; 2 explorers (structural, crux).
- (round 2) Founded field of 4 approaches (outliner); outline-reviewer registered+ranked, emitted build set (3). Built orbit-monotonicity-sandwich, density-contradiction, master-sos-identity. proof-reviewer adjudicated master-squeeze conflict (TRUE), verified orbit-monotonicity SOLVED, certified master-squeeze lemma, flagged density's 2 gaps. `current.md` updated to solved with full proof. Master squeeze independently re-verified by orchestrator (sympy).

### Broken
(none)

### Next
- (optional, robustness) Re-dispatch density-contradiction builder to close Gap A (target $a-b$) and Gap B (sign error) — gives a second independent verified solution. Not required for the goal (already solved).
- (optional) master-sos-identity direct-kill still open; not required.
- **Goal ACHIEVED.** If session continues, harden the second/density route for cross-verification.

## Eval History (round 3)

- **Round 3 (HARDENING — second independent solution):** Goal already SOLVED (orbit route, round 2). Re-dispatched density-contradiction builder to close reviewer-diagnosed Gaps A & B: **Gap A closed** (Kronecker target $c_0=a-b$, cross-distance $\to0$, sympy-verified); **Gap B closed** (case-independent zero-set propagation, $\eta_+(v)^2-2v\beta=\beta\eta_+(v)>0$). Retracted erroneous master-squeeze rejection (clean). proof-reviewer: CHANGES REQUESTED — re-audit found a pre-existing Section 7 R2 off-by-one (orbit index `m` vs image index `m+1` in Bézout, dropping `-dq`; conclusion robust but algebra step wrong). Builder fixed via re-index to $(n+1)p-mq=k^*$, sympy-verified $|D_{m,n}|=\rho$. **Density route now complete per builder; pending reviewer re-verification.** Orbit route remains SOLVED (verified round 2). `current.md` Status: solved (orbit route full proof). Density outcome recorded: partial (CHANGES REQUESTED, round 3).
