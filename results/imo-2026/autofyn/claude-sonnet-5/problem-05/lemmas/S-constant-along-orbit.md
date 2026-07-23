## Lemma ($S$ is constant along each orbit)

Let $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfy $f(f(y))=2f(y)-y$ for all $y>0$
(lemmas/equality-forcing-identity.md), and let $S(t):=f(t)-t$. For $y>0$, let
$y_0=y$, $y_{n+1}=f(y_n)$ be its orbit. Then $S(y_n)=S(y)$ for every $n\ge0$.

**Proof.** By lemmas/orbit-forces-f-ge-id.md, $y_n=y+nS(y)$ for all $n\ge0$, so
$S(y_n)=f(y_n)-y_n=y_{n+1}-y_n=(y+(n+1)S(y))-(y+nS(y))=S(y)$. $\blacksquare$

Certified by proof-reviewer, round 1, imo-2026-05. Source: `monotonicity-first.md`
Step 4. This is a genuine one-line structural fact (every point visited by an orbit
shares that orbit's common difference as its $S$-value); it does not by itself resolve
monotonicity or global constancy of $S$ (two disjoint arithmetic progressions with
different common differences need not intersect — see the numeric witness in
`monotonicity-first.md` Step 5, Attempt C), but is correct and reusable on its own.
