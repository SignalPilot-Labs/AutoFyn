## Status
solved

## Approaches tried
- `extremal-sup-inf` — worked. Derives continuity of `g=f-id` directly from the unconditional
  cross-inequality "Tool A/B" via real-perturbation (not orbit) points, then uses continuity +
  injectivity ⇒ strict monotonicity, then a discrete crossing/zero-set argument to force `g`
  globally constant. Fully rigorous; APPROVE.
- `cross-substitution-fixed-point` — worked, and gives the cleanest closing argument: a purely
  finite telescoping/partition bound (`|g(a)-g(b)| ≤ (b-a)^2/(4aN)` for every `N`) forces
  `g(a)=g(b)` for all `a,b>0` directly, with no continuity, monotonicity, or orbit-pairing
  machinery needed at all. Fully rigorous; APPROVE. Chosen as the proof recorded below.
- `orbit-telescoping-aimo0710` — worked. Uses a nearest-lattice-point orbit-pairing argument
  (adapting the `aimo-0710` crux idea, but re-derived from scratch here) to show any two positive
  `g`-values coincide, plus a fixed-point-set downward-closedness + sup/inf limiting argument
  (via Tool S₀/T) to rule out the "mixed" case. Fully rigorous, more elaborate than necessary;
  APPROVE.
- `monotonicity-order` — worked. Same escaping-double-orbit mechanism as
  `orbit-telescoping-aimo0710` for the "two positive values coincide" lemma, plus an
  infimum/supremum limiting argument applied to a LEFT-inequality-derived "Tool C" to rule out
  the mixed zero/positive case. Fully rigorous; APPROVE.

All four approaches independently and correctly establish the shared base layer (exact functional
equation `f(f(y))=2f(y)-y`, injectivity, `g:=f-\mathrm{id}\ge0`, orbit invariance `g(f(y))=g(y)`
and exact AP structure `f^n(y)=y+n g(y)`) and the two "cross tools" (algebraic consequences of
substituting `x=f(y)` into the RIGHT/LEFT inequalities and eliminating `f(f(y))` via the exact
FE), and each supplies an independent, valid closing argument forcing `g` to be a single global
constant `c\ge0`. All algebraic identities were independently re-verified with `sympy`; the
sufficiency direction was independently spot-checked numerically for `f(x)=x` and `f(x)=x+3`
(pass) versus `f(x)=2x` and a non-affine perturbation `f(x)=x+\sin x+2` (both correctly fail).

## Current best
(superseded — see Full proof below)

## Full proof

**Theorem.** A function `f:\mathbb R_{>0}\to\mathbb R_{>0}` satisfies
$$\sqrt{\frac{x^2+f(y)^2}{2}} \;\ge\; \frac{f(x)+y}{2} \;\ge\; \sqrt{x f(y)} \qquad (\star)$$
for all `x,y>0` **if and only if** `f(x)=x+c` for some constant `c\ge0`.

Throughout, since all quantities in `(\star)` are non-negative (in particular `f(x)+y>0`),
squaring is an equivalence, so `(\star)` is equivalent to the pair, for all `x,y>0`:
- **L**: `2x^2+2f(y)^2 \ge (f(x)+y)^2`,
- **R**: `(f(x)+y)^2 \ge 4xf(y)`.

### Part 1 — Necessity

**Step 1 (exact functional equation).** Fix `y>0`, set `x=f(y)` in `(\star)` (legal since
`f(y)>0`). The QM and GM of the pair `(f(y),f(y))` both equal `f(y)`, so `(\star)` reads
`f(y)\ge (f(f(y))+y)/2 \ge f(y)`, forcing equality:
$$f(f(y)) = 2f(y)-y \qquad \text{for all } y>0. \tag{$*$}$$

**Step 2 (injectivity).** If `f(a)=f(b)`, then by `(*)`, `2f(a)-a=f(f(a))=f(f(b))=2f(b)-b`, so
(using `f(a)=f(b)`) `a=b`.

**Step 3 (`g:=f-\mathrm{id}\ge0`, orbit invariance, exact AP orbit).** Define `g(y):=f(y)-y`.
From `(*)`, `g(f(y))=f(f(y))-f(y)=(2f(y)-y)-f(y)=f(y)-y=g(y)`. By induction on `n`,
`f^{(n)}(y)=y+n\,g(y)` and `g(f^{(n)}(y))=g(y)` for every integer `n\ge0` (base case trivial;
inductive step uses `f^{(n)}(y)=f^{(n-1)}(y)+g(f^{(n-1)}(y))=f^{(n-1)}(y)+g(y)`). Since every
`f^{(n)}(y)\in\mathbb R_{>0}`, if `g(y)<0` then `y+n\,g(y)\to-\infty`, eventually negative —
contradiction. Hence
$$g(y)\ge0 \quad\text{for all } y>0. \tag{NN}$$

**Step 4 (cross tools A and B, valid for ALL `x,y>0`).** Apply **R** at `(u,v)=(f(y),x)` (legal,
`f(y)>0`): `(f(f(y))+x)^2\ge4f(y)f(x)`. By `(*)`, `f(f(y))=2f(y)-y=y+2g(y)`. Writing `p:=g(x)`,
`q:=g(y)` (so `f(x)=x+p`, `f(y)=y+q`), expand:
$$(x+y+2q)^2-4(y+q)(x+p) = (x-y)^2+4(q-p)(y+q) = (x-y)^2-4(p-q)f(y).$$
(Verified by full symbolic expansion; identity holds for all real `x,y,p,q`.) Since `R(f(y),x)`
says the left side is `\ge0`, this gives, for **all** `x,y>0`:
$$\textbf{(A)}\quad (x-y)^2 \ge 4f(y)\big(g(x)-g(y)\big).$$
Relabelling `x\leftrightarrow y` in this universally-quantified statement gives, for all `x,y>0`:
$$\textbf{(B)}\quad (x-y)^2 \ge 4f(x)\big(g(y)-g(x)\big).$$

**Step 5 (local quadratic bound).** Combining (A) and (B): from (A),
`g(x)-g(y)\le(x-y)^2/(4f(y))`; from (B), `g(y)-g(x)\le(x-y)^2/(4f(x))`, i.e.
`g(x)-g(y)\ge-(x-y)^2/(4f(x))`. Hence, for all `x,y>0`,
$$|g(x)-g(y)| \;\le\; \frac{(x-y)^2}{4\min(f(x),f(y))}. \tag{LQB}$$

**Step 6 (global constancy of `g`, via finite telescoping — no continuity assumed).** Fix
`x,y>0` with `x\ne y`; let `a:=\min(x,y)`, `b:=\max(x,y)`. For a positive integer `N`, partition
`[a,b]` into `N` equal steps `z_i:=a+i(b-a)/N`, `i=0,\dots,N` (each `z_i\ge a>0`). By `(NN)`,
`f(t)\ge t` for all `t`, so `f(z_{i-1}),f(z_i)\ge a`, hence `\min(f(z_{i-1}),f(z_i))\ge a`. By
(LQB) applied to each consecutive pair,
$$|g(z_i)-g(z_{i-1})| \;\le\; \frac{\big((b-a)/N\big)^2}{4a}.$$
Summing via the triangle inequality over `i=1,\dots,N`,
$$|g(b)-g(a)| \;\le\; N\cdot\frac{(b-a)^2/N^2}{4a} \;=\; \frac{(b-a)^2}{4aN}.$$
This holds for **every** positive integer `N`. The left side is a fixed non-negative real number
independent of `N`; the right side `\to0` as `N\to\infty`. A fixed non-negative real number
bounded above by a sequence tending to `0` must itself be `0`, so `g(a)=g(b)`, i.e. `g(x)=g(y)`.

Since `x,y>0` were arbitrary, **`g` is constant on `\mathbb R_{>0}`**: `g\equiv c` for some
constant `c\ge0` (by (NN)). Hence
$$f(x) = x+c \qquad \text{for all } x>0, \text{ for some constant } c\ge0.$$

### Part 2 — Sufficiency

Let `f(x)=x+c`, `c\ge0`, and `x,y>0`. With `A:=x`, `B:=y+c=f(y)`:
$$2x^2+2f(y)^2-(f(x)+y)^2 = 2A^2+2B^2-(A+B)^2 = (A-B)^2 = (x-y-c)^2\ge0,$$
$$(f(x)+y)^2-4xf(y) = (A+B)^2-4AB = (A-B)^2 = (x-y-c)^2\ge0.$$
Both **L** and **R** hold for all `x,y>0` (with equality iff `x=y+c`), hence, since all quantities
in `(\star)` are non-negative, `(\star)` itself holds for all `x,y>0`. So `f(x)=x+c` is a solution
for every `c\ge0`.

### Conclusion

Combining Parts 1 and 2: the complete solution set is exactly
$$\boxed{f(x) = x+c, \quad c\ge0 \text{ an arbitrary constant}.}$$
`\blacksquare`

**Theorems/techniques invoked:** QM-AM and AM-GM inequalities (`knowledge_base.md`, "Standard
inequalities"); elementary real-analysis facts (a non-negative real number bounded above by a
null sequence is `0`; induction). No external "crux move" citations are used as proof — the
`aimo-0710`-flavored orbit ideas explored by two of the four sibling approaches were fully
re-derived from scratch and are not needed for this shortest closing argument, though they
independently also complete the proof.
