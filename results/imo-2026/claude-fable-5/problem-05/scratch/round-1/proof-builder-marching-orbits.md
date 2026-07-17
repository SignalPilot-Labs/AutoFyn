# Build report — marching-orbits (imo-2026-05), round 1

## What I closed

Filled the outline into a complete rigorous proof; Status set to **solved** in `results/imo-2026-05/approaches/marching-orbits.md`. All reviewer-flagged gaps addressed:

- **Squaring legality** stated once up front: all three chain quantities positive, so (∗) ⟺ (L) ∧ (R).
- **Part 1 (sufficiency):** both slacks derived by hand to equal $(x-y-c)^2$; $c<0$ excluded by codomain; numeric spot-checks included.
- **Part 2:** core identity, $d(f(y))=d(y)$, AP orbits, and $d\ge 0$ via full induction + Archimedean argument (Lemmas 1–2).
- **Part 3 (marching lemma):** explicit $n$ satisfying $y_n>\max(x+p,\ p^2/(q-p))$, $m=\lceil(y_n-x)/p\rceil\ge 2$ shown a positive integer, $S\in[0,p)$ from the ceiling bounds, slack expanded by hand to $4y_n(p-q)+(S+p)^2-4Sq$, O(1) terms bounded explicitly ($(S+p)^2<4p^2$, $-4Sq\le0$) — no limits used. Symmetric swap kills $q<p$.
- **Dichotomy** stated in exactly the required form: $\operatorname{range}(d)\subseteq\{0,c\}$ (or $d\equiv0$), three exhaustive mutually exclusive cases.
- **4a:** exclusion $(s-a)^2\ge 4ac$ derived; the note that it needs $f(a)=a$ exactly (licensed by the dichotomy) is recorded.
- **4b:** quadratic solved with discriminant check, lower root $<a$ shown ($\sqrt{4ac+2c^2}>c$), strictness at endpoints handled; bootstrap induction $a_k=a+kc$ all fixed, so fixed points unbounded.
- **4c:** explicit constants $a'\ge\max(16c,\,2b+1)$ give $\alpha\ge a'/2>b$ and interval length $4\sqrt{a'c}\ge 16c>c$; least-$n_\ast$ (well-ordering) argument lands $b_{n_\ast}\in(\alpha,\beta)$, contradicting 4a.

All load-bearing identities re-verified with sympy this round (sufficiency slacks, step-3 slack, 4a expansion, 4b roots) — the written proof stands on hand derivations alone.

## Promotable lemma

**core-identity-ap-orbits** (statement + full proof) drafted at `results/imo-2026-05/lemmas/core-identity-ap-orbits.md`, marked PROPOSED/uncertified for the proof-reviewer to certify. It is exactly the shared Part-2 machinery that two-point-pinch also needs.

## Remaining gaps

None known. Points deserving reviewer scrutiny: (i) the ceiling-bound derivation $0\le S<p$ in Part 3; (ii) endpoint strictness in Lemma 5's half-open interval; (iii) the constants in 4c.

Spec concerns:
