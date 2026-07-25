# Flat/Kink Parity Lemma

Certified round 17, from `approaches/global-lp-vertex-sufficiency.md`,
Section 8.3. Independently re-verified by the proof-reviewer (own fresh
exact-`Fraction` script, not the builder's).

**Setup.** Fix a background multiset $B=\{b_1,\ldots,b_r\}$ and a piece total
$p_i>0$ split into two fragments $x(t):=x_0+t$, $y(t):=p_i-x_0-t$. On any
interval of $t$ where neither $x(t)$ nor $y(t)$ crosses a value of $B$ or of
each other (all ranks in $B\cup\{x(t),y(t)\}$ constant), define
$g(t):=\mathrm{OddSum}(B\cup\{x(t),y(t)\})$.

**Statement.** On any such interval, $g$ is affine in $t$ with slope
$$g'(t)=[\mathrm{rank}(x(t))\text{ odd}]-[\mathrm{rank}(y(t))\text{ odd}]\in
\{-1,0,+1\}.$$
In particular $g$ is flat ($g'=0$) exactly when $x(t)$ and $y(t)$ occupy ranks
of the same parity, and has slope $\pm1$ exactly when they occupy ranks of
opposite parity.

**Proof.** $\mathrm{OddSum}(M)=\sum_{j\text{ odd}}M_{(j)}$, the sum over a
rank-fixed subset of coordinates (since no rank changes on the interval).
Each coordinate is either a constant (element of $B$), or $x(t)=x_0+t$
(coefficient $+1$ if rank odd, else $0$), or $y(t)=p_i-x_0-t$ (coefficient
$-1$ if rank odd, else $0$). Hence $g(t)$ is affine with the stated slope.
$\blacksquare$

**Reviewer independent re-verification.** Own fresh script
(`verify_parity.py`): $20{,}000$ random trials (random background $B$,
random $p_i$, random split point $x_0$, random small perturbation $t$),
filtering to intervals where no rank crossing occurs between $t=0$ and the
tested $t$ (verified by checking ranks agree at both endpoints): zero
mismatches between the actual finite-difference slope and the predicted
$\{-1,0,+1\}$ parity-difference slope, across $19{,}806$ valid (non-crossing)
trials.

**Scope note (carried from the approach file, correctly not overclaimed).**
This lemma is a diagnostic/mechanism-identification tool — it explains *when*
a within-piece bisection tie produces a sharp kink vs. a flat plateau in
$\mathrm{OddSum}$. It does **not** by itself locate where such ties occur as a
function of the adversary partition $p$ alone, nor does it resolve the
Existence Theorem's residual $\Sigma$-shape classification.
