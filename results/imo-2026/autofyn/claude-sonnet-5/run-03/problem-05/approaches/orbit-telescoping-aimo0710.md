## Status
solved

## Approaches tried
- Naive leading-order asymptotic comparison of two orbits `X_n=f^n(x0)=x0+np`, `Y_n=f^n(y0)=y0+nq`
  plugged into the original LEFT and RIGHT inequalities with matched index `n=m`, letting `n→∞`
  — dead end (recorded in round 1, re-verified by the outline-reviewer): at order `n^2` both
  inequalities degenerate to tautological AM-GM/QM-AM facts (`(p-q)^2≥0`, `(p+q)^2≤2(p^2+q^2)`)
  that hold for *any* `p,q`. The dominant term carries zero discriminating information. Do not
  resubmit this exact matched-diagonal (`n=m`) computation.
- **Non-diagonal / mismatched-scaling telescoping (this round)** — **succeeded**. The key fix
  over the diagonal attempt: instead of comparing two orbits at the *same* index `n=m` (which
  forces the useless leading `n^2` term to cancel identically), compare orbit point `Y_m` of one
  orbit against a *deliberately mismatched* index `n(m)` of the other orbit, chosen so that the
  two orbit points stay at *bounded* distance from each other while a genuinely growing
  coefficient (arising from the functional equation, not from the naive `n^2` comparison) is
  forced to blow up — reproducing exactly the "telescoped sum bounded above forces vanishing"
  shape of the `aimo-0710` crux move, but via a nearest-lattice-point argument rather than a
  literal finite sum. A second, genuinely new sub-argument (a "downward-closed fixed-point set /
  supremum" argument) was needed to close the remaining boundary case where one of the two
  points is an exact fixed point of `f`; this was not anticipated in the original outline but
  fits the same overall "bound something that should grow, get a contradiction" philosophy.

## Current best
Full proof completed and verified below (self-contained; re-derives the shared base layer at the
top, so no external lemma import is required, though the derived tools **Lemma S** and **Lemma
T** below are also independently confirmed by symbolic computation and match the "tool (A)"
lemma recorded by sibling approaches `extremal-sup-inf.md` / `cross-substitution-fixed-point.md`
up to relabeling).

## Full proof

### 0. Setup and shared base layer

Let `f : R_{>0} → R_{>0}` satisfy, for all `x,y>0`,
```
sqrt( (x^2+f(y)^2)/2 )  ≥  (f(x)+y)/2  ≥  sqrt( x f(y) ).                      (H)
```
(The left inequality is QM(x,f(y)) ≥ AM(f(x),y); the right is AM(f(x),y) ≥ GM(x,f(y)).)

**Step 0.1 (the functional equation).** Fix `y>0` and substitute `x=f(y)` into (H). Then
`QM(f(y),f(y)) = f(y)` and `GM(f(y),f(y)) = f(y)` exactly, so (H) forces
`f(y) ≥ (f(f(y))+y)/2 ≥ f(y)`, i.e. equality throughout:
```
f(f(y)) = 2f(y) - y   for all y>0.      (*)
```

**Step 0.2 (injectivity).** If `f(a)=f(b)` then by (*), `2f(a)-a = 2f(b)-b`; since `f(a)=f(b)`
this gives `a=b`.

**Step 0.3 (`g:=f-\mathrm{id}` is orbit-invariant and nonnegative).** Define `g(y):=f(y)-y` for
`y>0`. From (*), `g(f(y)) = f(f(y))-f(y) = (2f(y)-y)-f(y) = f(y)-y = g(y)`. So `g` is constant
along the forward orbit of any point. Consequently, writing `f^0(y)=y`, `f^{n+1}(y)=f(f^n(y))`,
induction gives `g(f^n(y))=g(y)` for all `n≥0`, and
```
f^n(y) = y + n·g(y)   for all n≥0.         (**)
```
(Induction: true for `n=0`; if `f^n(y)=y+n g(y)`, then `f^{n+1}(y) = f(f^n(y)) = f^n(y) + g(f^n(y))
= y+n g(y) + g(y) = y+(n+1)g(y)`, using `g(f^n(y))=g(y)`.)
If `g(y)<0` for some `y`, then by (**) `f^n(y)→-∞`, eventually leaving `R_{>0}`, contradicting
`f^n(y)∈R_{>0}` for all `n` (as `f` maps into `R_{>0}`). Hence
```
g(y) ≥ 0   for all y>0.                    (†)
```

**Step 0.4 (sufficiency of `f(x)=x+c`, `c≥0`).** If `f(x)=x+c` with `c≥0`, both inequalities in
(H) reduce to the identity `(x-y-c)^2 ≥ 0`:
- Right: `(f(x)+y)^2 - 4xf(y) = (x+c+y)^2-4x(y+c) = (x-y+c)^2 ... ` — let us verify directly:
  `(x+c+y)^2 - 4x(y+c) = x^2+c^2+y^2+2xc+2xy+2cy -4xy-4xc = x^2+y^2+c^2 -2xy-2xc+2cy
  = (x-y-c)^2` (expand `(x-y-c)^2 = x^2+y^2+c^2-2xy-2xc+2yc`, identical). So `(f(x)+y)^2-4xf(y) =
  (x-y-c)^2 ≥ 0`, giving the right inequality of (H).
- Left: `2(x^2+f(y)^2) - (f(x)+y)^2 = 2(x^2+(y+c)^2) - (x+y+c)^2`. Expand:
  `2x^2+2(y+c)^2-(x+(y+c))^2 = 2x^2+2(y+c)^2 -x^2-2x(y+c)-(y+c)^2 = x^2+(y+c)^2-2x(y+c) =
  (x-(y+c))^2 = (x-y-c)^2 ≥0`, giving the left inequality of (H).

So `f(x)=x+c` works for every `c≥0`. **The target characterization is precisely `f(x)=x+c`,
`c≥0`.** By Step 0.3, this is equivalent to showing `g` is a **global constant** (not merely
orbit-locally constant). The rest of the proof establishes exactly this.

### 1. Two derived algebraic lemmas

**Lemma S (from the RIGHT/GM inequality).** For all `a,b>0`,
```
(a-b)^2  ≥  4 f(a) · ( g(b) - g(a) ).       (S)
```
*Proof.* Substitute `x=f(a), y=b` into the right inequality of (H):
`(f(f(a))+b)^2 ≥ 4f(a)f(b)`. By (*), `f(f(a)) = a+2g(a)`. Writing `p=g(a), q=g(b)`, so
`f(b)=b+q`:
```
(a+2p+b)^2 - 4(a+p)(b+q) = a^2+4p^2+b^2+4ap+2ab+4pb-4ab-4aq-4pb-4pq
                          = a^2-2ab+b^2+4ap-4aq+4p^2-4pq
                          = (a-b)^2 + 4p(a+p) - 4q(a+p)
                          = (a-b)^2 - 4(a+p)(q-p)
                          = (a-b)^2 - 4f(a)(g(b)-g(a)).
```
(I verified this expansion symbolically with a computer-algebra check; it is a routine but
error-prone expansion, reproduced here in full.) Since the left side of (H) forces
`(a+2p+b)^2 ≥ 4(a+p)(b+q)`, we get `(a-b)^2 - 4f(a)(g(b)-g(a)) ≥ 0`, which is (S). ∎

(Special case: if `a=x0` is a fixed point of `f`, i.e. `g(x0)=0`, `f(x0)=x0`, then (S) becomes,
for every `b>0`,
```
(x0-b)^2 ≥ 4x0·g(b).       (S₀)
```
This also follows directly by substituting `x=x0` into the right inequality of (H) and using
`f(x0)=x0`.)

**Lemma T (from the LEFT/QM inequality).** For all `a,b>0`,
```
(a-b)^2  ≥  q^2 + 2q(a+b),   where q = g(a),           (T)
```
*provided `f(a)=a` (i.e. `a` is a fixed point).* More precisely: if `g(a)=0`, then for every `b>0`
with `q:=g(b)`,
```
(a-b)^2 ≥ q^2 + 2q(a+b).                    (T)
```
*Proof.* Substitute `x=b, y=a` into the left inequality of (H): `2(b^2+f(a)^2) ≥ (f(b)+a)^2`.
Using `f(a)=a` and `f(b)=b+q`:
```
2b^2+2a^2 - (b+q+a)^2 = 2a^2+2b^2-(a+b)^2-2q(a+b)-q^2 = (a-b)^2 - 2q(a+b) - q^2
```
(using `2a^2+2b^2-(a+b)^2=(a-b)^2`). The left inequality of (H) gives
`2(b^2+f(a)^2) - (f(b)+a)^2 ≥ 0`, i.e. `(a-b)^2 - 2q(a+b) - q^2 ≥ 0`, which is (T). ∎

Both (S) and (T) were also checked by an independent symbolic expansion (see build notes);
the algebra above is the full, self-contained derivation.

### 2. Lemma A: two points with strictly positive `g`-value must be equal

**Lemma A.** For all `x0,y0>0`: if `g(x0)>0` and `g(y0)>0`, then `g(x0)=g(y0)`.

*Proof.* Suppose not; then, relabelling `x0,y0` if necessary, `p:=g(x0) > q:=g(y0) > 0`.

Let `X_n := f^n(x0) = x0+np` and `Y_m := f^m(y0) = y0+mq` for integers `n,m ≥0` (by (**)); by
orbit-invariance, `g(X_n)=p` and `g(Y_m)=q` for all `n,m`, and `f(Y_m) = Y_m+q` for all `m`.

Apply Lemma S with `a=Y_m, b=X_n` (legal for every `m,n≥0`, since `g(b)-g(a) = p-q>0`, this is the
"useful direction"):
```
(Y_m - X_n)^2  ≥  4 f(Y_m) (p-q)  =  4(Y_m+q)(p-q).                (‡)
```
This holds for **every** choice of `n,m ≥ 0` — it is a fixed consequence of (S), true regardless
of how `X_n,Y_m` are paired.

**Mismatched pairing.** For each `m`, define `n(m) := \text{round}\big( (Y_m - x0)/p \big)`, the
nearest integer to `(Y_m-x0)/p` (round half up, say). Since `q>0`, `Y_m = y0+mq → +\infty` as
`m→\infty`, so `(Y_m-x0)/p → +\infty`; hence there is `M_0` such that for all `m ≥ M_0`,
`(Y_m-x0)/p ≥ 0`, so `n(m)` is a nonnegative integer for `m≥M_0`. By the defining property of
nearest-integer rounding,
```
| n(m) - (Y_m-x0)/p |  ≤  1/2,   i.e.   | X_{n(m)} - Y_m |  =  p·| n(m) - (Y_m-x0)/p |  ≤  p/2.
```
So for all `m≥M_0`,
```
(Y_m - X_{n(m)})^2  ≤  p^2/4  =:  M,
```
a constant **independent of `m`**.

On the other hand, by (‡) with `n=n(m)`,
```
(Y_m - X_{n(m)})^2  ≥  4(Y_m+q)(p-q)  =  4(y0+mq+q)(p-q).
```
Since `q>0` and `p-q>0`, the right side is an increasing affine function of `m` with slope
`4q(p-q)>0`, so it tends to `+\infty` as `m→\infty`. In particular there is `m_1 ≥ M_0` with
`4(y0+m_1q+q)(p-q) > M`.

Combining the two displayed bounds at `m=m_1`:
```
M  ≥  (Y_{m_1}-X_{n(m_1)})^2  ≥  4(y0+m_1q+q)(p-q)  >  M,
```
a contradiction. Hence the assumption `p>q>0` is impossible, and by symmetry so is `q>p>0`.
Therefore `p=q`. ∎

*(Numerical sanity check of the mechanism: with `p=3,q=1,x0=5,y0=2`, at `m=1000` one gets
`n(1000)=336`, `|Y_{1000}-X_{336}|=1.0 ≤ p/2=1.5` (bounded, as claimed) while the lower bound
`4(Y_{1000}+q)(p-q)=8024`, already vastly exceeding `M=p^2/4=2.25` — confirming the inequality
(‡) would be badly violated, exactly as the proof predicts.)*

### 3. Lemma B: the fixed-point set is "downward closed"

Call `x0>0` a **fixed point** if `g(x0)=0` (equivalently `f(x0)=x0`). Let
`F := \{t>0 : g(t)=0\}`.

**Lemma B.** If `x0 ∈ F` and `0<y0≤x0`, then `y0∈F`. (I.e. `F` is downward closed: `x0∈F ⟹
(0,x0] ⊆ F`.)

*Proof.* If `y0=x0` this is immediate. So suppose `y0<x0` and, for contradiction, `q:=g(y0)>0`.

Let `Y_m := f^m(y0) = y0+mq` (`m≥0`), so `g(Y_m)=q` and `f(Y_m)=Y_m+q` for all `m`.

Since `(x0-y0)/q > 0`, let `m^* := \text{round}\big((x0-y0)/q\big) ≥ 0` be the nearest
nonnegative integer to `(x0-y0)/q`. By the nearest-integer property,
```
D := |x0 - Y_{m^*}| = q·\big| (x0-y0)/q - m^* \big| ≤ q/2,   so   D^2 ≤ q^2/4.
```
Since `x0` is a fixed point (`g(x0)=0`), apply Lemma T with `a=x0, b=Y_{m^*}` (using
`g(Y_{m^*})=q`):
```
(x0-Y_{m^*})^2  ≥  q^2 + 2q(x0+Y_{m^*})  ≥  q^2 + 2q\,x0
```
(dropping the nonnegative term `2q\,Y_{m^*}≥0`, since `Y_{m^*}>0`). So
```
D^2  ≥  q^2 + 2q\,x0.
```
Combined with `D^2 ≤ q^2/4`:
```
q^2/4  ≥  q^2 + 2q\,x0  \implies  -3q^2/4  ≥  2q\,x0  \implies  -3q/4  ≥  2x0
```
(dividing by `q>0`, which preserves the inequality direction). The left side is negative
(`q>0`), the right side `2x0` is positive (`x0>0`), so `-3q/4 ≥ 2x0>0` is impossible. This
contradiction shows `q=0`, i.e. `y0∈F`. ∎

*(Numerical check: `x0=10,y0=3,q=2` gives `m^*=4`, `D=1.0=q/2` exactly, and indeed `D^2=1.0 <
q^2+2q(x0+Y_{m^*})=88.0`, the required violation.)*

### 4. Global constancy of `g`

**Claim.** `g` is constant on `R_{>0}`.

*Proof.* Recall `F=\{t>0:g(t)=0\}` and `g≥0` everywhere (†).

**Case 1: `F=∅`.** Then `g(t)>0` for every `t>0`. Fix any `x0,y0>0`; both have `g>0`, so Lemma A
gives `g(x0)=g(y0)`. As `x0,y0` were arbitrary, `g` is constant (equal to some `c>0`) on all of
`R_{>0}`.

**Case 2: `F≠∅`.** By Lemma B, `F` is downward closed: `x0∈F \implies (0,x0]⊆F`. Let
`X^* := \sup F \in (0,+\infty]` (well-defined and positive since `F` is a nonempty subset of
`R_{>0}`).

- **Sub-case 2a: `X^*=+\infty`.** Then `F` is unbounded above: for every `t>0` there is some
  `x0∈F` with `x0>t` (else `t` would be an upper bound for `F` smaller than `\sup F=\infty`).
  By downward closedness, `t∈(0,x0]⊆F`. As `t>0` was arbitrary, `F=(0,\infty)`, i.e. `g≡0` on
  all of `R_{>0}`. `g` is (the constant `0`) — done.

- **Sub-case 2b: `X^*<+\infty`.** First we show `X^*∈F`. For every `ε>0` with `ε<X^*`, since
  `X^*=\sup F`, there exists `x_ε∈F` with `X^*-ε<x_ε≤X^*`. Applying (S₀) (the special case of
  Lemma S at the fixed point `x_ε`) with `b=X^*`:
  ```
  (x_ε-X^*)^2 ≥ 4x_ε\, g(X^*).
  ```
  As `ε→0^+`, `x_ε→X^*` (squeezed between `X^*-ε` and `X^*`), so `(x_ε-X^*)^2→0`, while
  `x_ε→X^*>0` stays bounded away from `0` for `ε` small. Hence for every `δ>0` we may choose
  `ε` small enough that `(x_ε-X^*)^2 < δ`; since this holds for every `δ>0` and `4x_ε g(X^*) ≤
  (x_ε-X^*)^2`, letting `ε→0` forces `4X^*\,g(X^*) ≤ 0`. As `X^*>0` and `g(X^*)≥0` (by (†)),
  this gives `g(X^*)=0`, i.e. `X^*∈F`.

  So `F⊆(0,X^*]` (definition of supremum) and `X^*∈F`, which by downward closedness gives
  `(0,X^*]⊆F`. Hence `F=(0,X^*]` **exactly**.

  Consequently `g(t)>0` for every `t>X^*` (since such `t\notin F`). Pick any two points
  `y_1,y_2 \in (X^*,\infty)`; both have `g>0`, so Lemma A gives `g(y_1)=g(y_2)=:c>0`. Since
  `y_1,y_2` were arbitrary in `(X^*,\infty)`, `g\equiv c>0` on all of `(X^*,\infty)`.

  Now derive a contradiction: let `δ:=\sqrt{X^*c}>0` and `y_0:=X^*+δ \in (X^*,\infty)`, so
  `g(y_0)=c`. Since `X^*` is a fixed point, apply (S₀) with `b=y_0`:
  ```
  (X^*-y_0)^2 \ge 4X^*\,g(y_0)  \implies  δ^2 \ge 4X^*c  \implies  X^*c \ge 4X^*c
  \implies 0 \ge 3X^*c.
  ```
  But `X^*>0` and `c>0`, so `3X^*c>0`, contradicting `0\ge 3X^*c`. This contradiction shows
  **sub-case 2b is impossible**.

So in Case 2, only sub-case 2a can occur, giving `g\equiv 0`.

In both Case 1 and Case 2, `g` is a global constant `c\ge 0` on `R_{>0}` (Case 1: `c>0`; Case 2:
necessarily `c=0`, via sub-case 2a; note sub-case 2b, which would have allowed a genuine "mixed"
`g` with both a fixed point and points of value `c>0`, was **ruled out**). ∎

### 5. Conclusion

By Step 0.3, `g(y)=f(y)-y` is a global constant `c\ge0`, i.e. `f(x)=x+c` for all `x>0`, for some
fixed `c\ge0`. By Step 0.4, every such `f` indeed satisfies (H). Hence:

**The complete solution set is exactly**
```
f(x) = x + c,   for some constant c ≥ 0.
```

This matches the round-1 explorer consensus and is now proved with no remaining gap: sufficiency
is verified by direct algebraic identity (Step 0.4, an SOS reduction to `(x-y-c)^2\ge0` for both
inequalities), and necessity is established by Steps 0.1–0.4 (functional equation, injectivity,
orbit-invariance/nonnegativity of `g`) together with Lemmas A, B and the Section 4 case analysis
proving `g` is a global constant. `∎`

## Promotable lemmas

**Lemma S** (statement and proof in Section 1 above): for all `a,b>0` satisfying the problem's
hypothesis (H), `(a-b)^2 ≥ 4f(a)(g(b)-g(a))` where `g=f-\mathrm{id}`. Derived from the RIGHT/GM
inequality of (H) via the substitution `x=f(a),y=b` and the functional equation `f(f(y))=2f(y)-y`.
(Matches "tool (A)" already recorded independently by `extremal-sup-inf.md` and
`cross-substitution-fixed-point.md`; safe to certify as a single shared lemma.)

**Lemma T** (Section 1): for `a` a fixed point of `f` (`g(a)=0`) and any `b>0` with `q=g(b)`,
`(a-b)^2 ≥ q^2+2q(a+b)`. Derived from the LEFT/QM inequality of (H) via `x=b,y=a`. This is new
(not previously recorded by sibling approaches) and is the key extra tool that made the
fixed-point boundary case (Lemma B / Section 3) tractable.

**Lemma A** (Section 2): any two points with strictly positive `g`-value have equal `g`-value.
Proved via a mismatched-index ("nearest lattice point") orbit-pairing argument using Lemma S —
this is the successful adaptation of the `aimo-0710` telescoping/orbit-bounding idea that the
outline called for.

**Lemma B** (Section 3): the fixed-point set `F=\{t:g(t)=0\}` is downward closed. Proved via
Lemma T plus the same nearest-lattice-point trick.

**Section 4 argument** (downward-closed-set + supremum dichotomy): general technique for
promoting "any two positive-valued points agree" (Lemma A) plus "the zero-set is downward
closed" (Lemma B) to full global constancy, by analysing `sup F` and eliminating a finite
supremum via a limiting/local argument at the boundary. This is a reusable pattern beyond this
specific problem and may be worth recording in `knowledge_base.md` as a general technique for
"orbit-invariant but not obviously globally-constant" functional equation problems.
