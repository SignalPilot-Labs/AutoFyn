# Run State

## Goal
Solve **imo-2026-05** (IMO 2026 P5, hard, algebra, difficulty 8, compute_and_prove, characterization).

**Problem.** Determine all $f : \mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that
$$\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$$
for every $x,y\in\mathbb{R}_{>0}$.

**Metric:** proof-reviewer verdict = APPROVE and `results/imo-2026-05/current.md` ## Status = `solved`, with the full characterization stated and both existence (every member of the family satisfies) and uniqueness (no other functions) proven rigorously.

**Eval command:** `grep -A2 '^## Status' results/imo-2026-05/current.md 2>/dev/null; cat results/imo-2026-05/approaches/.ranking.json 2>/dev/null`

**Baseline (round 1):** no workspace, no approaches, Status absent. Target: solved.

**Constraints (rigor rules from CLAUDE.md):**
- No skipped cases, no hand-waving, name every tool (cite knowledge_base.md), verify final answer.
- "Determine all" ⇒ prove (a) every member of the claimed family satisfies the condition, AND (b) every solution lies in the family (uniqueness).
- Prose Markdown proof, no Lean.

## Seed findings (round-1 orchestrator analysis — to orient the team, not dictate)
Conjectural answer: $f(x) = x + c$ for any constant $c \ge 0$.
- **Existence:** for $f(x)=x+c$, $f(x)+y = x+(y+c) = x+f(y)$, so the middle $\frac{f(x)+y}{2}=\frac{x+f(y)}{2}=$ AM of the pair $(x,f(y))$; the outer bounds are GM and RMS of the same pair, so both inequalities are the universal AM-GM / QM-AM. Works for all $c\ge 0$ (positivity: $x+c>0$ for $x>0$ iff $c\ge0$).
- **Key derived relation:** setting $x=f(y)$ forces both inequalities to equality (the outer AM-GM $\sqrt{xf(y)}\le\sqrt{(x^2+f(y)^2)/2}$ is tight at $x=f(y)$), giving $\boxed{f(f(y))=2f(y)-y}$. Hence $f$ injective; with $g=f-\mathrm{id}$, $g\circ f=g$ (orbits are arithmetic progressions $x, x{+}g(x), x{+}2g(x),\dots$); forward-orbit positivity forces $g\ge0$ (i.e. $f\ge\mathrm{id}$).
- **Crux = uniqueness.** Need to show $g$ is constant using the inequalities at general $(x,y)$ (the symmetric/orthogonal substitutions all reduce to tautologies — the content is genuinely asymmetric). Periodic perturbations of $g$ around a constant FAIL the right inequality off the diagonal (numerically verified), so the family is plausibly exactly $\{x+c:c\ge0\}$ — but the rigorous uniqueness argument is the open gap.

## Goal Updates
- [2026-07-25 14:02:20] Initial task: solve imo-2026-05.

## Eval History
- [Round 1] **BREAKTHROUGH — SOLVED.** `orbit-close-encounter` → proof-reviewer **APPROVE**, Status = `solved`, Elo 1516 (outcome: verified-milestone). Full characterization **$f(x)=x+c$ for any constant $c\ge0$** proven end-to-end (existence via AM-GM/QM-AM on pair $(x,f(y))$; uniqueness via $f(f(x))=2f(x)-x$ + orbit close-encounter forcing $g=f-\mathrm{id}$ to one positive value + maximal-connected-component fixed-point exclusion). `gm-lipschitz-partition` → CHANGES REQUESTED (partial, Elo 1484): Fact 5 lemma certified, Part (A) via Fact 5 correct, Part (B) cover-iteration only goes rightward and leaves $(0,x_0-2\sqrt{cx_0})$ uncovered when $x_0>4c$. `asymptotic-vanishing-coefficient` → RETHINK (not built/registered): all three closures of the $(x-y-c)^2$-swallowing obstruction dead (iterate-equality is a verified tautology).
- Ranking snapshot: orbit-close-encounter 1516 / gm-lipschitz-partition 1484. 5 lemmas certified into `results/imo-2026-05/lemmas/`.
- [Round 2] **HARDENING — TWO APPROVED PROOFS.** `orbit-close-encounter`: two reviewer-noted cosmetic corrections applied (Step 0 QM²−AM² = $(f(y)-x)^2/4$ not $/2$; Step 2 (⋆⋆) justification tightened to the explicit within-$c_b$-level-set tautology $(x-y+c_b)^2\ge0$). `gm-lipschitz-partition`: Part (B) gap closed — rightward-only cover iteration replaced by maximal-connected-component boundary-push argument (same `(†)` zero-region radius $2\sqrt{cs}$; Part A Fact 5 engine untouched) → proof-reviewer **APPROVE** (verified-milestone). **Two independent certified proofs** of the same characterization now: orbit route (raw `(⋆)` + close-encounter) and gm route (Fact 5 self-referential bound + close-encounter), both closing Part B via maximal-component. Ranking re-run: orbit-close-encounter **1530.5** (stale cleared), gm-lipschitz-partition **1469.5** (stale set post-outcome, will fold next round — expected to rise toward orbit). `current.md` Status = `solved` maintained. `asymptotic-vanishing-coefficient` still dead/unregistered.

## Rules
- ALWAYS: one problem per run — imo-2026-05 only; all rounds push this one problem.
- ALWAYS: rank every round (outline-reviewer runs every round); no "skip reviewer / advance leader" fast path.
- ALWAYS: each slug is a whole competing solution to the whole claim, end to end — never split one proof across slugs.
- ALWAYS: diversify approach FRAMING/ROUTE, not just technique — rival approaches must stay far apart, else they share one wall (single-gap trap).
- NEVER: hand-edit `results/<id>/approaches/.ranking.json` — only the ranker tools touch it.
- ALWAYS (round 1): next outliner must put ≥1 approach attacking uniqueness (the fixed-point / "$g\equiv0$ if any fixed point" step) from a genuinely different framing — both surviving approaches share the (A) close-encounter + (B) fixed-point-exclusion walls (single-gap convergence flagged by outline-reviewer).
- NEVER (round 1): re-derive the `3+2√2` lower bound for the fixed-point step — it assumed $f$ surjective / seed $a\le c$, which fails ($f$ is non-surjective). Use the zero-region radius $2\sqrt{c\,x_0}$ from the global bound $g(y)\le(y-x_0)^2/(4x_0)$ + a maximal-connected-component (boundary-push) or bidirectional cover-iteration argument instead.
- NEVER (round 1): build an approach whose uniqueness rests on symmetric substitutions ($x=y$, $y=f(x)$, symmetric product, iterate re-plugging, setting middle=AM) — they all collapse to $(f(x)-x)^2\ge0$ tautologies.
- ALWAYS (round 1): the close-encounter number-theory lemma needs BOTH ratio cases — irrational (Kronecker/density) AND rational (Bézout: $d=\gcd(c_a,c_b)\le c_a$ gives encounter $\delta\le c_a/2$). The rational fix is the Bézout family $Pn-Qm=k_0\to\infty$, NOT $K=(b-a)/d$ (which is not generally integral).
- ALWAYS (round 1): cover-iteration for fixed-point exclusion must go BOTH directions (rightward $x_{k+1}\approx x_k+\sqrt{cx_k}\to\infty$ AND leftward toward $0$); rightward-only leaves $(0,x_0-2\sqrt{cx_0})$ uncovered when $x_0>4c$.
- PREFERRED (round 2): for the fixed-point-exclusion Part (B), the **maximal-connected-component boundary-push argument** is the validated closure (APPROVED in BOTH orbit-close-encounter and gm-lipschitz-partition) — `S={g=0}` open via the $(†)$ zero-region radius $2\sqrt{cs}$, component $I=(\alpha,\beta)$ containing $x_0$, push $s\to\beta^-$ ⇒ $\beta=\infty$, $s\to\alpha^+$ ⇒ $\alpha=0$. Prefer it over cover-iteration (which is bidirectional-bookkeeping-prone). The `(†)` global bound $g(y)\le(y-x_0)^2/(4x_0)$ from $(\star)$ at $x=x_0$ is the source of the radius and is approach-independent.

## State
### Done
- Round 1: full flow executed (3 explorers parallel → outliner → outline-reviewer → 2 builders parallel → 1 reviewer). **Problem SOLVED** via `orbit-close-encounter` (APPROVE). 5 lemmas certified. `current.md` Status=solved with full proof.
- Seed findings confirmed by team: answer $f(x)=x+c$ ($c\ge0$); key relation $f(f(x))=2f(x)-x$; uniqueness crux cracked by orbit close-encounter + maximal-component fixed-point exclusion.
- Round 2: applied 2 cosmetic corrections to `orbit-close-encounter` (Step 0 QM²−AM² factor-of-2 fix; Step 2 (⋆⋆) justification). Re-dispatched `gm-lipschitz-partition` builder → closed Part (B) via maximal-connected-component argument (Part A Fact 5 untouched) → proof-reviewer **APPROVE** (verified-milestone). Outline-reviewer re-ranked field (orbit 1530.5 / gm 1469.5). **Two independent certified proofs** now on record.

### Broken
- (none active) `asymptotic-vanishing-coefficient` remains RETHINK/dead/unregistered — all closures of the $(x-y-c)^2$ swallowing obstruction failed (iterate-equality is a verified tautology). Would need a fundamental reframe to revive; low priority since problem is solved with two proofs.

### Next
- Problem is SOLVED with two APPROVED independent proofs. Goal fully achieved. Remaining work (if rounds continue) is optional: (a) let next round's outline-reviewer fold gm-lipschitz's verified-milestone outcome into Elo (currently stale=true post-outcome); (b) optionally revive `asymptotic-vanishing-coefficient` from a genuinely different framing for a third independent route — only if a fresh non-tautological obstruction closure is found.
