# IMO Problem 5 — Verification Record

**Problem:** Determine all $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ such that
$\sqrt{\tfrac{x^2+f(y)^2}{2}}\ \ge\ \tfrac{f(x)+y}{2}\ \ge\ \sqrt{xf(y)}$ for all $x,y>0$.

**Answer verified:** $f(x)=x+c$ for an arbitrary constant $c\ge0$.

## Timeline (all times PDT, 2026-07-22)

| Time | Event |
|---|---|
| 15:55:56 | Work started; recognized the chain as QM ≥ (middle) ≥ GM of the pair $(x, f(y))$, conjectured $f(x)=x+c$ |
| 15:56–15:57 | Derived full proof: equality case $x=f(y)$ ⟹ $f(f(y))=2f(y)-y$; orbit argument ⟹ $f(y)\ge y$; substitution $x=f(z)$ ⟹ pointwise bound $\lvert g(z)-g(y)\rvert\le (z-y)^2/(4\min(y,z))$; telescoping ⟹ $g$ constant |
| 15:56:30 (approx) | Numeric/symbolic check round 1 (`check1.py`): sufficiency on 200k samples ✔; non-solutions $f(x)=kx$ fail at $x=f(y)$ ✔ |
| 15:57:10 (approx) | Numeric check round 2 (`check2.py`): all Step-3 algebraic identities verified over 100k random substitutions ✔; telescoping bound → 0 ✔ |
| 15:57–15:58 | Independent adversarial referee agent reviewed the complete proof line by line against a 6-point checklist; verdict: **PROOF CORRECT**, no gaps |
| 15:58:14 | Solution finalized and written to `problem5_solution.md` |
| 16:03:53 | Consolidated verification script `problem5_verification.py` re-run in project folder: **ALL CHECKS PASSED** |

## 1. Mechanical verification (`problem5_verification.py`)

Re-run 2026-07-22 16:03:53 PDT — all checks passed:

1. **Sufficiency.** For 200,000 random triples $(c,x,y)$ with $c\in[0,10]$, $x,y\in(0.001,100)$: the full chain holds for $f(x)=x+c$ (tolerance $10^{-12}$).
2. **Necessity bites.** For $f(x)=kx$, $k\in\{1.1, 1.5, 2.0\}$, the chain **fails** at $x=f(y)$ — confirming the equality-case squeeze $f(f(y))=2f(y)-y$ genuinely constrains non-solutions.
3. **Step-3 identities** (each over 100,000 random substitutions):
   - $2f(z)-z+y = A+B+\delta$ where $A=f(z),\ B=f(y),\ \delta=g(z)-g(y)$;
   - $2A^2+2B^2-(A+B+\delta)^2 = (A-B)^2-2(A+B)\delta-\delta^2$;
   - $A+B-(z-y) = 2y+g(y)+g(z)$.
4. **Telescoping.** The bound $|g(b)-g(a)|\le (b-a)^2/(4an)$ demonstrably tends to 0 as the partition refines (e.g. $a=2,b=7$: $3.125 \to 0.0003$ for $n=1\to10^4$).

## 2. Adversarial referee review (independent agent, 15:57–15:58 PDT)

The complete proof was submitted to an independent checker instructed to *refute* it,
with an explicit 6-point checklist. Verdict: **PROOF CORRECT.** Findings per item:

1. **Step 1 squeeze** ($x=f(y)$): substitution legal; both outer terms equal $f(y)$; equality correctly forced. This is the *only* step using the right inequality (R), where it is essential.
2. **Step 2 orbit:** positivity of all $a_n$ by induction; recurrence $a_{n+1}=2a_n-a_{n-1}$ correctly derived from $(\ast)$ at $a_{n-1}$ for $n\ge1$; indexing consistent; closed form $a_n=y+n(f(y)-y)$ correct; contradiction for $f(y)<y$ valid.
3. **Step 3 estimate:** squaring legitimate (right side $=\tfrac{f(f(z))+y}{2}>0$ before squaring); all three identities verified by hand; $\delta^2$ cancels without flipping the inequality; only division is by $2(2y+g(y)+g(z))\ge 4y>0$; the $y\leftrightarrow z$ swap is fully symmetric and the combined $\min(y,z)$ bound is weaker than each case-specific bound, hence valid.
4. **Step 4 telescoping:** purely pointwise — needs **no** continuity, monotonicity, measurability, or other regularity; partition points all $\ge a$; triangle inequality assumption-free.
5. **Answer set exact:** all $c\ge0$ work (including $c=0$); $c<0$ excluded both by codomain and by Step 2; $f(x)=kx$ excluded by $(\ast)$ ($k^2=2k-1\Rightarrow k=1$); piecewise/non-constant shifts killed by Step 4.
6. **No silent assumptions:** (R) is used only in Step 1; its content propagates through $(\ast)$; Steps 2–4 use only $(\ast)$ and (L); no hidden continuity/injectivity/surjectivity anywhere.

The referee additionally probed: squaring of possibly-negative quantities (none — positivity established first), division by nonpositive quantities (none), need for $z\ne y$ or injectivity (not needed; $z=y$ gives $\delta=0$ trivially). It also identified the problem as IMO Shortlist 2022 A4 and noted the answer matches the known classification.

## 3. Solution summary (proof verified above)

1. $x=f(y)$ makes QM = GM, squeezing the middle: $f(f(y))=2f(y)-y$ $(\ast)$.
2. Orbits under $f$ are arithmetic progressions $y+n(f(y)-y)$; positivity forces $f(y)\ge y$. Set $g=f-\mathrm{id}\ge0$.
3. $x=f(z)$ in the left inequality + $(\ast)$ gives $(A-B)^2\ge 2(A+B)\delta+\delta^2$ with $A=f(z),B=f(y),\delta=g(z)-g(y)$, which yields the pointwise bound $|g(z)-g(y)|\le\dfrac{(z-y)^2}{4\min(y,z)}$.
4. Telescoping over an $n$-part uniform partition of $[a,b]$ bounds $|g(b)-g(a)|$ by $\dfrac{(b-a)^2}{4an}\to0$, so $g\equiv c\ge0$, i.e. $f(x)=x+c$.
5. Conversely every $f(x)=x+c$, $c\ge0$ works since the middle term is exactly $\mathrm{AM}(x,f(y))$ and the chain is QM ≥ AM ≥ GM.

**Record written:** 2026-07-22 16:04 PDT
