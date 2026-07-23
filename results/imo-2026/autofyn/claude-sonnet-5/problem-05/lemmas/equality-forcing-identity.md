## Lemma (equality-forcing identity)

Any $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying
$$\sqrt{\frac{x^2+f(y)^2}{2}} \ge \frac{f(x)+y}{2} \ge \sqrt{xf(y)} \qquad \text{for all } x,y>0$$
satisfies
$$f(f(y)) = 2f(y) - y \qquad \text{for all } y>0.$$

**Proof.** Squaring both halves of the sandwich (valid since all terms are nonnegative)
gives, for all $x,y>0$: $2x^2+2f(y)^2\ge(f(x)+y)^2$ (A) and $(f(x)+y)^2\ge4xf(y)$ (B).
Substitute $x=f(y)$ (legitimate, $f(y)>0$) into (A): $4f(y)^2\ge(f(f(y))+y)^2$.
Substitute $x=f(y)$ into (B): $(f(f(y))+y)^2\ge4f(y)^2$. Both hold simultaneously, so
$(f(f(y))+y)^2=4f(y)^2$; since $f(f(y))+y>0$ and $2f(y)>0$, taking nonnegative square
roots gives $f(f(y))+y=2f(y)$. $\blacksquare$

Certified by proof-reviewer, round 1, imo-2026-05. Source: `quadratic-difference-chaining.md`
Step 1 / `monotonicity-first.md` Step 1 (identical, independently re-derived). Verified
symbolically.
