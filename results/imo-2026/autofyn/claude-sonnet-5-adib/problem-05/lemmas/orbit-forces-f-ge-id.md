## Lemma ($f(y) \ge y$, and orbit is an arithmetic progression)

Let $f$ satisfy the equality-forcing identity $f(f(y))=2f(y)-y$ for all $y>0$
(lemmas/equality-forcing-identity.md), with $f:\mathbb R_{>0}\to\mathbb R_{>0}$. Then:

1. For every $y>0$, the orbit $y_0=y,\ y_{n+1}=f(y_n)$ satisfies
   $y_n = y+n(f(y)-y)$ for all $n\ge0$ (an exact arithmetic progression with common
   difference $S(y):=f(y)-y$).
2. $f(y)\ge y$ for every $y>0$.

**Proof.** (1) Applying the identity with $y\mapsto y_n$: $y_{n+2}=2y_{n+1}-y_n$, the
second-difference-zero recursion for an AP; solved with initial data $y_0=y$,
$y_1=f(y)$ gives the closed form, proved by a routine induction on $n$.

(2) Since $f$ maps into $\mathbb R_{>0}$, $y_n>0$ for all $n\ge0$ by induction. If
$d:=f(y)-y<0$ then $y_n=y+nd\to-\infty$, contradicting $y_n>0$ for all $n$. Hence
$d\ge0$. $\blacksquare$

Certified by proof-reviewer, round 1, imo-2026-05. Source:
`quadratic-difference-chaining.md` Step 2 / `monotonicity-first.md` Step 2 (identical).
