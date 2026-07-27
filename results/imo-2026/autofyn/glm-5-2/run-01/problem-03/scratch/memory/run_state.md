## Goal
Solve imo-2026-03 (IMO 2026 Problem 3, difficulty 9, combinatorics, compute_and_prove).
Metric: number of hard problems solved (count of results/<id>.md with `## Status` = solved).
Eval: `grep -rl '^solved$' results/ 2>/dev/null | wc -l`. Baseline: 0. Target: ≥1 (imo-2026-03 solved).
Constraint: proof rigorous per CLAUDE.md rigor rules; compute_and_prove → state c(n) explicitly and verify (upper bound + construction).
Also produce: LaTeX file + separate Markdown solution/commentary file, pushed on branch `glm5.2-imo2026-03`.

## Goal Updates
- [2026-07-15] User task: solve imo-2026-03, push branch glm5.2-imo2026-03 with accompanying latex file and separate markdown solution+commentary.

## Eval History
- Round 1: imo-2026-03 Status = PARTIAL. 0 solved. Rigorous: greedy-pick reduction (D=a1−a2+a3−…, LB=(1+D)/2) [VERIFIED by reviewer]; lower bound n=1 (D≥1/3) + Case A general (XY doesn't cut 2^n → D≥1 unit) [VERIFIED]; upper bound n=1 complete incl. L=1/2 boundary (c(1)=2/3 fully solved). OPEN gaps: (a) general lower-bound Case B (XY cuts 2^n); (b) general upper bound. Conjecture c(n)=2^n/(2^{n+1}−1) numerically confirmed n=1..5, equality only at geometric config 1:2:4:…:2^n. PLATEAU on both general gaps after 2 builder rounds.
- Round 3: Status still PARTIAL (0 solved). IMPROVED. NEW RIGOROUS: lower bound n=2 PROVED (L(2): every ≤2-cut refinement of G_2=(1,2,4) has D≥1 ⇒ c(2)≥4/7; exhaustive casework by #cuts on piece 4; VERIFIED by proof-reviewer incl. 2M-sample sweep, 0 violations, min D=1). New clean reformulations: even-sum (D≥1 ⟺ Σ_even≤2^n−1) makes Case A one line; rank/parity integral D=∫1_{r(t) odd} dt with cuts as TOGGLE-PAIRS (+1 on (0,m], −1 on (M,s], equal length m). Halving recurrence D_new=a1−D_old (when a1≥2a2) verified — handles top-heavy regime. Parity-fix (n=1 r_0 even on (0,1], odd on (1,2]). Deliverables produced: results/imo-2026-03.tex (LaTeX) + results/imo-2026-03-commentary.md (Markdown solution+commentary). OPEN: general Case B (toggle lemma on geometric staircase — load-bearing), general U(n), L(3) casework, U(2). PLATEAU on the two general gaps (now 3 rounds); next: L(3)/U(2) exhaustive casework as concrete advance, OR the toggle-lemma induction.

## Rules
- ALWAYS: the answer is c(n)=2^n/(2^{n+1}−1), equivalently minimax D* = 1/(2^{n+1}−1); geometric config 1:2:4:…:2^n is the unique extremum for BOTH bounds (verified by exhaustive search n=1..5). (round 1)
- ALWAYS: greedy alternating claim ⇒ LB gets pieces at odd sorted positions = (1+D)/2 with D=a1−a2+a3−…; this reduction is PROVEN and re-verified — build on it, don't re-derive. (round 1)
- NEVER: retry the "merge inequality" D(F∪T)≥1 for general tails — it is FALSE (counterexample exists); it only holds for *dyadic/geometric* tails. The induction must carry dyadic structure, not just the numeric bound D(T)≥1. (round 1)
- NEVER: use myopic greedy XY (fails: 36/400 n=2, 67/400 n=3 configs exceed 1/S), naive rank-decrement induction (alternating sum is global, doesn't induct on n), or pure Hall-pairing (leftover exceeds 1/S for n≥3). (round 1)
- LEAD to pursue next: the DIFFERENCE GAME (repeatedly replace two largest a≥b by a−b) gives f(G_n)=1 on geometric = the target value; numerically no XY strategy beats 1 on G_n. Formalize whether difference-game value = min_XY D(P); if so it unifies BOTH bounds. (round 1)
- ALWAYS: for n=1 the clean picture is XY forms a "doubled" structure {m,m,leftover}, maximizing m=median; general-n XY target structure is pairs+(small leftover) but NOT pure perfect-pairing (fails n≥3) — relax it. (round 1)
- ALWAYS: use the CORRECTED toggle-pair framework: D=∫1_{r(t) odd} dt, r(t)=#{pieces≥t}; a cut s→(m,M), m≤M, changes r by +1 on (0,m], 0 on (m,M], −1 on (M,s] (two equal-length toggle intervals of length m). The earlier "r_final=r_0+R" (only +1 on (0,m]) is FALSE (n=1 predicts D=2, true 1). (round 3)
- ALWAYS: even-sum reformulation D≥1 ⟺ Σ_even≤2^n−1 ⟺ Σ_odd≥2^n makes lower-bound Case A one line and is the clean target for Case B ("2nd picker's take ≤ tail mass"). (round 3)
- ALWAYS: halving recurrence — when a1≥2a2, halving a1 gives D_new=a1−D_old. Handles the top-heavy regime of the upper bound; the flat regime (a1<2a2) is the precise open obstruction. (round 3)
- NEVER: claim the lower-bound equality is "iff full halving" — D=1 is attained on WHOLE sub-regions (B0 m∈[1,2], B1(i) m=2 any p, B3 f1≥2,f2≥1), not uniquely at full halving. State "attained at full halving (and elsewhere)". (round 3, proof-reviewer)
- NEVER: let a proof-builder run silent — Round 2 builder idled 918s and was force-interrupted. Give builders BOUNDED, time-boxed tasks and instruct them to WRITE results to the file incrementally as they go. (round 3, stuck-recovery)

## State
Done: Round 1 (explore/outline/build/review: n=1 full both bounds, Case A, reduction; U(1) boundary fixed; difference-game lead; merge-lemma-needs-dyadic obstruction; hybrid fails flat regime). Round 2 (interrupted: builder stuck). Round 3 — re-outlined via corrected rank/parity toggle-pair framework + even-sum reformulation; outline reviewed (APPROVE w/ fixes); built: L(2) lower bound PROVED via exhaustive casework (VERIFIED by proof-reviewer + 2M-sample sweep), parity fix applied, halving recurrence + toggle-pair framework established; fixed reviewer's equality-wording defect directly; produced deliverables results/imo-2026-03.tex + results/imo-2026-03-commentary.md. Status=partial.
Broken: general lower-bound Case B (toggle lemma on geometric staircase — load-bearing, unproved); general upper bound U(n) (flat-regime obstruction); L(3) casework not written; U(2) flat regime open. General gaps now PLATEAU 3 rounds.
Next: Round 4 — (a) attempt the toggle-lemma induction on the self-similar staircase (G_n staircase = G_{n-1} + top block (2^{n-1},2^n]) using the +1-gap to force a surviving odd-parity unit; (b) concrete advance: write rigorous L(3) and U(2) exhaustive casework to extend proved frontier from n=2 to n=3; (c) keep deliverables in sync. If general bounds stay stuck, the deliverables already present an honest partial proof with the conjecture clearly flagged.

## [Round 4]
Eval: `grep -rl '^solved$' results/ 2>/dev/null | wc -l` = 0 (overall Status stays `partial` — general n unsolved, which is the actual problem).
- U(2) PROVED (APPROVED by proof-reviewer): four explicit XY strategies S1–S4 give D = a1−a2, a2−a3, |2a1−1|, a3; min ≤ 1/7 for every 3-piece partition; equality at geometric (4/7,2/7,1/7). Combined with L(2) → **c(2)=4/7 FULLY SOLVED** (both bounds).
- L(3) PROVED (verified correct, writeup gap closed this round): every ≤3-cut refinement of G_3=(1,2,4,8) has D≥1 → **c(3)≥8/15**. k8=1 hand proof; k8=2 (59 cells) + k8=3 (13 cells) by vertex-min principle, full self-contained python verification script appended as Appendix B-5A (runs, reproduces 59 cells all minima∈{1,5/3,2,3,5}≥1). BREAKTHROUGH on lower-bound frontier (n=2→n=3).
- Defects fixed: equality-overclaim wording (§D, §B-4), "72"→"59" typo, L(2) §B-3 equality fix (from round-3 reviewer) re-confirmed.
- Deliverables synced: imo-2026-03.md (main), imo-2026-03.tex (LaTeX), imo-2026-03-commentary.md (commentary) all reflect c(1)=2/3, c(2)=4/7 fully proved; c(3)≥8/15 lower bound proved; general n + n=3 upper bound open/conjectured.
- OPEN: general lower-bound Case B (toggle lemma / GML(n) for arbitrary n — proved n≤3, numerically confirmed n≤5); general upper bound U(n) for n≥3; n=3 upper bound (U(2) strategy doesn't lift). PLATEAU 4 rounds on both general gaps.
Status: partial (overall problem open); concrete rigorous results: n=1 fully, n=2 fully, n=3 lower bound.
