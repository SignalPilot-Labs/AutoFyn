# Lemma: `D_1(A)\ge0` on the boundary curve `\mathcal C=\mathcal C_{\mathrm{lo}}`

**Setup (reused, all already certified elsewhere).**
`X_0(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}`, `\beta_0(A):=(\pi-A)/3`,
`K_c:=2\sin A\sin(A+B)`, `P:=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`,
`Q:=-\sin A\sin B`, `G(\beta):=K_c-P\sin\beta-Q\cos\beta`,
`\mathrm{RHS}(A,B):=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)`,
`D_1(A,B):=(1+\cos B)\cos B-\mathrm{RHS}(A,B)` (`lemmas/star-
factorization-on-boundary-curve.md`). `\mathcal C:=\{(A,B):X_0(A,B)=
\cos^2B\}`. Theorem A (`coordinate-bash-resultant-boundary-pointwise-
tangent.md`, round 15, certified): on `\mathcal C` with `B\in(0,\pi/2)`,
`\tan A=-\sin B\cos(2B)/(2\cos^3B)`, `A=\mathrm{Aof}(B):=\arctan(\cdot)
\in(0,\pi/2)` the correct branch. Write `D_1(B):=D_1(\mathrm{Aof}(B),B)`.

`A^\ast` is, by its original (round 11 of `coordinate-bash-resultant-
boundary-pointwise.md`) definition, **the** value with
`G_{\mathrm{curve}}(A^\ast):=G\bigl(\beta_0(A^\ast);A^\ast,\beta_0(A^\ast)
\bigr)=0`, pinned there by `\mathrm{mpmath.findroot}` to 40 digits,
`A^\ast=0.4063777806843303293871746903293092626710\ldots`. `B^\ast:=
\beta_0(A^\ast)\approx0.9117382909684876363584895643167312\ldots`. Until
this round, `A^\ast` had **no known closed form**
(`lemmas/star-corner-is-boundary-cusp-not-critical-point.md`'s own
Status). §0 below supplies one, exactly, algebraically, and uses it to
prove — not merely numerically evidence — that `(A^\ast,B^\ast)\in
\mathcal C`, the fact Step 0 needs and that round 17's version of this
lemma cited as "already certified" when it was not.

**Theorem.** `D_1(B)\ge0` for every `B\in[B^\ast,\pi/3]`, with equality
exactly at `B=B^\ast`.

### Step 0. `D_1(B^\ast)=0` exactly

This step needs two facts: (i) `G(\beta_0(A^\ast))=0` (true by `A^\ast`'s
own defining equation, restated above); (ii) `(A^\ast,B^\ast)\in\mathcal
C`, i.e. `X_0(A^\ast,B^\ast)=\cos^2B^\ast`. **Round 17's version of this
lemma cited (ii) as "already certified" when it was in fact a six-round-
old unproved numeric coincidence (round 11's own text: "no symbolic
derivation... of the coincidence"), and was rejected by the proof-
reviewer for exactly this reason.** This round supplies the missing
proof of (ii), in full, from scratch, via an exact algebraic identity
between `G_{\mathrm{curve}}` and `h(A):=X_0(A,\beta_0(A))-\cos^2\beta_0
(A)` (fact (ii) is precisely `h(A^\ast)=0`), plus an exact closed form
for `A^\ast` that makes the whole argument checkable by hand, not merely
by a black-box `sympy.simplify`.

#### 0(a). The substitution `u:=A/3+\pi/6`

Since `\beta_0(A)=(\pi-A)/3`, writing `A=3u-\pi/2` gives
`\beta_0(A)=\bigl(\pi-(3u-\pi/2)\bigr)/3=(3\pi/2-3u)/3=\pi/2-u`, so
$$
\sin\beta_0=\cos u,\qquad\cos\beta_0=\sin u,\qquad
A+\beta_0(A)=(3u-\pi/2)+(\pi/2-u)=2u .
$$
This is the natural substitution because it makes `\beta_0`, `A`, and
`A+\beta_0(A)` all simple multiples of the single variable `u`.

#### 0(b). `G_{\mathrm{curve}}(u):=G(\beta_0(A);A,\beta_0(A))` in closed form, derived by hand

With `s:=\sin u`, `c:=\cos u` (so `s^2+c^2=1`), and using
`\cos(x-\pi/2)=\sin x`, `\sin(x-\pi/2)=-\cos x`:
$$
\cos A=\cos(3u-\tfrac\pi2)=\sin3u,\qquad
\sin A=\sin(3u-\tfrac\pi2)=-\cos3u,\qquad
\sin(A+\beta_0)=\sin2u=2sc .
$$
Evaluate `K_c,P,Q` at `(A,B)=(A,\beta_0(A))`:
$$
K_c=2\sin A\sin(A+\beta_0)=2(-\cos3u)(2sc)=-4sc\cos3u,
$$
$$
P=\tfrac12\sin(A-\beta_0)+\tfrac32\sin(A+\beta_0)
=\tfrac12\sin(4u-\pi)+\tfrac32\sin2u=-\tfrac12\sin4u+\tfrac32\sin2u,
$$
(using `A-\beta_0(A)=(3u-\pi/2)-(\pi/2-u)=4u-\pi` and `\sin(x-\pi)=-\sin x`),
$$
Q=-\sin A\sin\beta_0=-(-\cos3u)(c)=c\cos3u .
$$
So (recall `\sin\beta_0=\cos u=c`, `\cos\beta_0=\sin u=s`):
$$
G_{\mathrm{curve}}(u)=K_c-P\cos u-Q\sin u
=-4sc\cos3u-\bigl(-\tfrac12\sin4u+\tfrac32\sin2u\bigr)c-\bigl(c\cos3u\bigr)s .
$$
$$
=-4sc\cos3u-c\cdot s\cos3u+\tfrac12c\sin4u-\tfrac32c\sin2u
=-5sc\cos3u+\tfrac12c\sin4u-\tfrac32c\sin2u .
$$
(The two `\cos3u` terms combine: `-4sc\cos3u-cs\cos3u=-5sc\cos3u`.)

Now substitute the elementary multiple-angle formulas
`\cos3u=4c^3-3c`, `\sin2u=2sc`, `\sin4u=2\sin2u\cos2u=2(2sc)(2c^2-1)
=4sc(2c^2-1)`:

- `-5sc\cos3u=-5sc(4c^3-3c)=-20sc^4+15sc^2`.
- `\tfrac12c\sin4u=\tfrac12c\cdot4sc(2c^2-1)=2sc^2(2c^2-1)=4sc^4-2sc^2`.
- `-\tfrac32c\sin2u=-\tfrac32c(2sc)=-3sc^2`.

Summing:
$$
G_{\mathrm{curve}}(u)=(-20+4)sc^4+(15-2-3)sc^2=-16sc^4+10sc^2
=sc^2(10-16c^2).
\tag{G}
$$
(Independently re-verified by `sympy.expand_trig`/`sympy.simplify` from
the raw definitions with `A=3u-\pi/2`: matches `(G)` exactly, residual
`0`. Every step above is a single classical multiple-angle substitution
followed by elementary polynomial collection — hand-checkable term by
term, not a black-box call.)

#### 0(c). `h(u):=X_0(A,\beta_0(A))-\cos^2\beta_0(A)` in closed form, derived by hand

`X_0(A,\beta_0(A))=\dfrac{\sin\beta_0\cos A}{2\sin(A+\beta_0)}
=\dfrac{c\sin3u}{2(2sc)}=\dfrac{\sin3u}{4s}` (cancelling `c\ne0`, valid
since `u\in(0,\pi/2)` on the range used below). Using `\sin3u=3s-4s^3`:
$$
X_0(A,\beta_0(A))=\frac{3s-4s^3}{4s}=\frac{3-4s^2}4=\frac34-s^2 .
$$
And `\cos^2\beta_0(A)=\sin^2u=s^2`. Hence
$$
h(u)=\Bigl(\tfrac34-s^2\Bigr)-s^2=\tfrac34-2s^2 .
\tag{H}
$$
(Independently re-verified by `sympy`: matches `h(u)=\cos2u-1/4` since
`\cos2u=1-2s^2`, residual `0` against the raw definition.)

#### 0(d). The identity: `G_{\mathrm{curve}}=-8\sin u\cos^2u\cdot h`, and why it is exact

From `(G)`, `c^2=1-s^2` gives `10-16c^2=10-16(1-s^2)=16s^2-6`, so
`G_{\mathrm{curve}}(u)=sc^2(16s^2-6)`. From `(H)`, `2s^2=\tfrac34-h(u)`,
i.e. `s^2=\tfrac38-\tfrac12h(u)`. Substituting directly, or simply
comparing `(G)` and `(H)` in the `c^2` form (`10-16c^2=-16(c^2-\tfrac58)`
and `h(u)=2\cos2u\ldots` — the fastest route): write `(H)` as
`h(u)=2c^2-\tfrac54` (since `\cos2u=2c^2-1`, so `h=\cos2u-\tfrac14
=2c^2-\tfrac54`). Then
$$
-8sc^2\,h(u)=-8sc^2\Bigl(2c^2-\tfrac54\Bigr)=sc^2\bigl(-16c^2+10\bigr)
=sc^2(10-16c^2)=G_{\mathrm{curve}}(u).
$$
$$
\boxed{\ G_{\mathrm{curve}}(u)=-8\sin u\cos^2u\cdot h(u),\qquad
u=\frac A3+\frac\pi6.\ }
\tag{IDENTITY}
$$
This is a genuine algebraic identity between two closed forms each
independently, hand-derived from the raw trigonometric definitions of
`X_0,\beta_0,K_c,P,Q,G` (§0(b)-(c) above) — not a numerical coincidence,
and not merely a `sympy.simplify`-to-`0` black box (though that
independently confirms it too, residual `0`).

#### 0(e). The cofactor `-8\sin u\cos^2u` is nonzero at `u=u^\ast:=A^\ast/3+\pi/6`

This needs `A^\ast\in(0,\pi/2)`, established exactly (not numerically) in
§0(f) below via the closed form; granting that for a moment,
`u^\ast\in(\pi/6,\pi/3)\subset(0,\pi/2)`, so `\sin u^\ast>0,\ \cos
u^\ast>0` strictly (both sine and cosine are positive on `(0,\pi/2)`).
Hence `-8\sin u^\ast\cos^2u^\ast<0\ne0`.

#### 0(f). Exact closed form for `A^\ast`, and `G_{\mathrm{curve}}(A^\ast)=0` verified algebraically

By fact (i) and `(G)`, `A^\ast` (equivalently `u^\ast`) satisfies
`s^\ast c^{\ast2}(10-16c^{\ast2})=0` where `s^\ast:=\sin u^\ast,\
c^\ast:=\cos u^\ast`. On any range with `\sin u,\cos u\ne0` this reduces
to `10-16\cos^2u=0`, i.e. `\cos^2u=5/8`, i.e. `\sin^2u=3/8`. Since
`\sin u>0$ is needed (see below) and `\sin` is injective on `(0,\pi/2)`,
this has the **unique** solution
$$
u^\ast=\arcsin\!\Bigl(\frac{\sqrt6}4\Bigr)\qquad\Bigl(\text{since }
\sin^2u^\ast=\tfrac38\Rightarrow\sin u^\ast=\sqrt{3/8}=\tfrac{\sqrt6}4
\text{ taking the positive root}\Bigr),
$$
hence
$$
\boxed{\ A^\ast=3\arcsin\!\Bigl(\frac{\sqrt6}4\Bigr)-\frac\pi2\ }
\tag{A-STAR}
$$
**exactly**, with `u^\ast:=\arcsin(\sqrt6/4)`.

*`u^\ast\in(\pi/6,\pi/3)$, hence `A^\ast\in(0,\pi/2)$ — proved exactly, no
numerics.* `\arcsin` is strictly increasing on `[-1,1]`, so it suffices to
show `\sin(\pi/6)<\sqrt6/4<\sin(\pi/3)`, i.e. `\tfrac12<\tfrac{\sqrt6}4<
\tfrac{\sqrt3}2`. Squaring (all three quantities positive, so squaring
preserves the order): `\tfrac14<\tfrac6{16}=\tfrac38<\tfrac34`, i.e.
`\tfrac14<\tfrac38<\tfrac34` — true by direct comparison of rationals.
Hence `u^\ast\in(\pi/6,\pi/3)`, so `A^\ast=3u^\ast-\pi/2\in(0,\pi/2)`,
**exactly**. (This also retroactively justifies §0(e)'s
`\sin u^\ast,\cos u^\ast>0`, and independently justifies the divisions
`\sin u\ne0,\cos u\ne0` used in §0(c) at `u=u^\ast`.)

*`G_{\mathrm{curve}}(A^\ast)=0`, verified directly, exactly.* At
`u=u^\ast`, `\cos^2u^\ast=1-\sin^2u^\ast=1-\tfrac38=\tfrac58`, so
`10-16\cos^2u^\ast=10-16\cdot\tfrac58=10-10=0`, hence by `(G)`,
`G_{\mathrm{curve}}(u^\ast)=\sin u^\ast\cos^2u^\ast\cdot0=0` exactly — an
elementary rational computation, not a numeric approximation.

*This `A^\ast` is the population's standing `A^\ast`.* `G_{\mathrm{curve}}`
has a **unique** root in `(0,\pi/2)`: for `u\in(\pi/6,\pi/3)\subset
(0,\pi/2)`, `\sin u,\cos u>0`, so by `(G)`, `G_{\mathrm{curve}}(u)=0\iff
\cos^2u=5/8`, and `\cos` is strictly decreasing (hence injective) on
`(0,\pi/2)`, giving a unique such `u`, hence a unique root `A^\ast$ of
`G_{\mathrm{curve}}` in `(0,\pi/2)` overall (the map `A\mapsto u=A/3+\pi/6`
is a bijection `(0,\pi/2)\to(\pi/6,\pi/3)\subset(0,\pi/2)`, and outside
`(\pi/6,\pi/3)` — i.e. for `A\notin(0,\pi/2)` — no claim is made or
needed). The population's `A^\ast=0.4063777806843303293871746903293092
626710\ldots` was pinned by `\mathrm{mpmath.findroot}` on this same
`G_{\mathrm{curve}}` (round 11 of `coordinate-bash-resultant-boundary-
pointwise.md`) to a value manifestly in `(0,\pi/2)`; since the root in
this interval is unique, the numeric value and `(A\text{-STAR})` denote
the identical point. Direct high-precision check (own `mpmath`,
`dps=60`): `(A\text{-STAR})=0.40637778068433032938717469032930926267100
1750\ldots`, agreeing with the population's 40-digit standing value to
every one of its 40 displayed digits (difference `\approx1.75\times
10^{-42}`, i.e. agreement far beyond the population's own working
precision anywhere in this file). **This is a genuine strengthening
beyond what any earlier round achieved**: `A^\ast$ previously had "no
known closed form" (`lemmas/star-corner-is-boundary-cusp-not-critical-
point.md`'s own Status); `(A\text{-STAR})` supplies one, and it is used
only to make Step 0 exact — none of Steps 1-4 below need to be
re-expressed in terms of it (they continue to use the certified
`mpmath.iv` numeric bracket of `B^\ast`, which `(A\text{-STAR})` is
independently confirmed to lie inside, see §1 below).

#### 0(g). Conclusion: `h(A^\ast)=0`, i.e. fact (ii)

By `(IDENTITY)`, `0=G_{\mathrm{curve}}(A^\ast)=-8\sin u^\ast\cos^2u^\ast
\cdot h(A^\ast)`; by §0(e), `-8\sin u^\ast\cos^2u^\ast\ne0`; hence
$$
h(A^\ast)=0,\qquad\text{i.e.}\qquad X_0(A^\ast,B^\ast)=\cos^2B^\ast
\quad(\text{since }B^\ast=\beta_0(A^\ast)),
$$
**exactly** — fact (ii), no longer a numeric coincidence but a proved
consequence of `(IDENTITY)` and `A^\ast`'s own defining equation. This
also directly confirms `(A^\ast,B^\ast)\in\mathcal C`, so by Theorem A's
characterization of `\mathcal C` (the branch `A\in(0,\pi/2)`, which
`A^\ast$ satisfies per §0(f)), `\mathrm{Aof}(B^\ast)=A^\ast`.

*(Sanity cross-check, not needed for the proof: `h(u^\ast)` can also be
read off directly from `(H)`, `h(u^\ast)=\tfrac34-2\sin^2u^\ast=
\tfrac34-2\cdot\tfrac38=\tfrac34-\tfrac34=0` — the same conclusion by a
second, independent route, since `\sin^2u^\ast=3/8` by construction of
`(A\text{-STAR})`.)*

#### 0(h). `D_1(B^\ast)=0`

From fact (i), evaluating `\mathrm{RHS}` at `(A^\ast,B^\ast)` with
`\beta_0(A^\ast)=B^\ast`:
$$
\mathrm{RHS}(A^\ast,B^\ast)=(1+\cos B^\ast)\cos B^\ast-\sin B^\ast\cdot
G(\beta_0(A^\ast))=(1+\cos B^\ast)\cos B^\ast-\sin B^\ast\cdot0
=(1+\cos B^\ast)\cos B^\ast,
$$
hence `D_1(A^\ast,B^\ast)=(1+\cos B^\ast)\cos B^\ast-\mathrm{RHS}(A^\ast,
B^\ast)=0` **exactly** — this half is a pure algebraic consequence of
fact (i) alone, unchanged from round 17's version. By fact (ii) (now
proved, §0(g)) and Theorem A, `\mathrm{Aof}(B^\ast)=A^\ast`, so
$$
D_1(B^\ast)=D_1(\mathrm{Aof}(B^\ast),B^\ast)=D_1(A^\ast,B^\ast)=0.
$$
`\blacksquare` (Step 0)

Independently re-verified numerically to 60 digits (own fresh `mpmath`,
`dps=60`, both from `(A\text{-STAR})$ directly and from the population's
standing 40-digit value): `D_1(A^\ast,B^\ast)`, `G_{\mathrm{curve}}
(A^\ast)`, and `h(A^\ast)` are each `0` to the full precision used
(`\lesssim10^{-59}`, precision-floor zero) — matching the exact
algebraic conclusions above.

### Step 1. A certified enclosure of `B^\ast`

`B^\ast` is the unique root in `(0,\pi/2)` of `\Phi(B):=\mathrm{Aof}(B)-
(\pi-3B)` (since `\mathrm{Aof}(B^\ast)=A^\ast` by Step 0 and `\beta_0
(A^\ast)=B^\ast\iff A^\ast=\pi-3B^\ast`). Own `mpmath.iv` (`dps=80`)
directed-rounding evaluation of `\Phi` at the two points
$$
B_{\mathrm{lo}}:=0.911738290968487636348489564316731207175389216,\qquad
B_{\mathrm{hi}}:=0.911738290968487636368489564316731207175389216
$$
(`B_{\mathrm{hi}}-B_{\mathrm{lo}}=2\times10^{-20}`) gives the certified
two-sided enclosures
$$
\Phi(B_{\mathrm{lo}})\in[-7.500\ldots\times10^{-20},\,-7.499\ldots\times
10^{-20}]<0,\qquad
\Phi(B_{\mathrm{hi}})\in[7.499\ldots\times10^{-20},\,7.500\ldots\times
10^{-20}]>0.
$$
`\Phi` is continuous on `[B_{\mathrm{lo}},B_{\mathrm{hi}}]` (composition of
`\arctan` with a smooth rational function of `\sin B,\cos B`, and `\cos B
\ne0` throughout this tiny range since `B\approx0.9117<\pi/2`), so by the
Intermediate Value Theorem `\Phi` has a root in `(B_{\mathrm{lo}},
B_{\mathrm{hi}})` — necessarily `B^\ast$ itself, and consistent with
`\beta_0(A^\ast)=(\pi-A^\ast)/3` evaluated at the exact closed form
`(A\text{-STAR})`, which lies at `B_{\mathrm{lo}}+1.000\ldots\times
10^{-20}$, inside this bracket (own `mpmath`, `dps=60`, checked directly).
Hence
$$
B^\ast\in[B_{\mathrm{lo}},B_{\mathrm{hi}}],\qquad
B_{\mathrm{hi}}-B_{\mathrm{lo}}=2\times10^{-20}.
$$

### Step 2. Certified derivative bound near the corner

Let `\delta:=0.02`. Build `D_1(B)` symbolically (own fresh `sympy`
session: substitute `A=\arctan(u(B))`, `u(B)=-\sin B\cos(2B)/(2\cos^3B)`,
into the raw definition of `D_1(A,B)` above — no simplification performed)
and differentiate once (`sympy.diff`, raw unsimplified result — interval
evaluation needs no closed form, exactly the technique already certified
in this file's Theorems B/C and the round-16 near-corner argument).
Translate to `mpmath.iv` (`dps=30`) via `sin\to\mathrm{iv.sin}`,
`\cos\to\mathrm{iv.cos}`, `\arctan(x)\to\mathrm{iv.atan2}(x,1)`,
`\sqrt{\cdot}\to\mathrm{iv.sqrt}` (the last arising because `sympy`
rewrites `\sin(\arctan u),\cos(\arctan u)` as `u/\sqrt{1+u^2},\,1/\sqrt
{1+u^2}`, valid since `A=\arctan u\in(0,\pi/2)` throughout the swept
range — checked below).

**Certified sweep.** Partition `[B_{\mathrm{lo}},\,B_{\mathrm{hi}}+\delta]
=[0.911738290968487636348489564316731207175389216,\allowbreak
0.931738290968487636368489564316731207175389216]` into `5000` equal
sub-intervals; on each, evaluate `D_1'(B)` via directed-rounding
`\mathrm{mpmath.iv}` (`dps=30`). **Result: every one of the `5000`
enclosures has lower bound `\ge4.6251\ldots>4`** (`0` sub-intervals with
lower bound `\le4`; global minimum lower bound over all `5000`
sub-intervals `\approx4.625123340196357\ldots`). Hence
$$
D_1'(B)\ \ge\ 4\qquad\text{for every }B\in[B_{\mathrm{lo}},\,
B_{\mathrm{hi}}+\delta].\tag{Deriv-bound}
$$
This is a fully certified branch-covering proof (not sampling): each of
the `5000` conclusions is a genuine two-sided interval enclosure.

### Step 3. Certified value bound away from the corner

Partition `[B_{\mathrm{lo}}+\delta,\,\pi/3]=[0.931738290968487636348489
564316731207175389216,\,1.04719755119659774615421446109316762806572313
\ldots]` into `5000` equal sub-intervals; on each, evaluate `D_1(B)` via
the same certified `\mathrm{mpmath.iv}` machinery. **Result: every one of
the `5000` enclosures has lower bound `>0`** (`0` sub-intervals with lower
bound `\le0`; global minimum lower bound `\approx0.09724\ldots`). Hence
$$
D_1(B)\ >\ 0\qquad\text{for every }B\in[B_{\mathrm{lo}}+\delta,\,\pi/3].
\tag{Value-bound}
$$
(This range includes the right endpoint `B=\pi/3` itself, where a direct
point-interval evaluation independently confirms `D_1(\pi/3)\in
[0.397686404277917514\ldots,0.397686404277917514\ldots]`, matching the
population's long-standing citation `0.397686404277917446\ldots` to 8
significant figures — the residual difference at the 9th digit is
consistent with, and irrelevant to, both being comfortably `>0`.)

### Step 4. Gluing via the Mean Value Theorem

`D_1` is `C^\infty` on `[B_{\mathrm{lo}},\pi/3]` (composition of smooth
elementary functions, no singularity: `\cos B>0` for `B<\pi/2`, and
`\sin(\mathrm{Aof}(B)+B)\ne0` throughout since `\mathrm{Aof}(B)+B\in
(0.4,\pi)` stays away from `0,\pi`, matching the already-established
smoothness of Theorem A/B/C's constituent pieces in this range).

*Near-corner region, `B\in(B^\ast,B^\ast+\delta]`.* By the classical Mean
Value Theorem, there is `\xi\in(B^\ast,B)` with `D_1(B)-D_1(B^\ast)=D_1'
(\xi)(B-B^\ast)`. Since `B^\ast\in[B_{\mathrm{lo}},B_{\mathrm{hi}}]$ (Step
1) and `B\le B^\ast+\delta\le B_{\mathrm{hi}}+\delta`, the intermediate
point `\xi` satisfies `\xi\in(B^\ast,B)\subset[B_{\mathrm{lo}},
B_{\mathrm{hi}}+\delta]`, so `D_1'(\xi)\ge4` by (Deriv-bound). Using
`D_1(B^\ast)=0` (Step 0):
$$
D_1(B)\ \ge\ 4(B-B^\ast)\ >\ 0\qquad\text{for every }B\in(B^\ast,
B^\ast+\delta].
$$

*Away region, `B\in[B^\ast+\delta,\pi/3]`.* Since `B^\ast\ge B_{\mathrm{lo}}`,
`B^\ast+\delta\ge B_{\mathrm{lo}}+\delta`, so `[B^\ast+\delta,\pi/3]\subset
[B_{\mathrm{lo}}+\delta,\pi/3]`, and (Value-bound) gives `D_1(B)>0` for
every `B` in this range.

*Union.* `(B^\ast,B^\ast+\delta]\cup[B^\ast+\delta,\pi/3]=(B^\ast,\pi/3]`,
covering every `B` in the target range except `B^\ast` itself, where
`D_1(B^\ast)=0` (Step 0). Hence
$$
D_1(B)\ \ge\ 0\qquad\text{for every }B\in[B^\ast,\pi/3],\quad\text{with
equality exactly at }B=B^\ast.\qquad\blacksquare
$$

## Reusability
Reusable verbatim as hypothesis (B) of the Reduction Lemma (New result 1,
round 13) of `coordinate-bash-resultant-boundary-pointwise-tangent.md`.
`(A\text{-STAR})` (the exact closed form `A^\ast=3\arcsin(\sqrt6/4)-
\pi/2`) is independently reusable as the first exact (non-numeric)
pinning of `A^\ast` anywhere in this population's history.

## Origin
`coordinate-bash-resultant-boundary-pointwise-tangent.md`, round 17
(original, rejected version); round 18 (this fix, replacing Step 0 with
an exact algebraic proof of fact (ii) via the `G_{\mathrm{curve}}=-8\sin
u\cos^2u\cdot h` identity and the closed form `(A\text{-STAR})`, scouted
by `/tmp/round-18/math-explorer-gap6.md` and independently re-derived
twice more — by the round-18 proof-outliner and round-18 outline-
reviewer — before this write-up).

## Status
**Certified — proof-reviewer, round 18.** Independently re-derived, from
raw definitions and in a fresh `sympy`/`mpmath` session (not reusing the
builder's script), every load-bearing claim of §0: (a) the identity
`G_{\mathrm{curve}}(u)=-8\sin u\cos^2u\cdot h(u)` — rebuilt `G_curve(A)`
and `h(A)` directly from `X_0,\beta_0,K_c,P,Q,G` and confirmed the
identity exactly (`sympy.simplify`, residual `0`); (b) the closed form
`A^\ast=3\arcsin(\sqrt6/4)-\pi/2` matches the population's standing
40-digit numeric `A^\ast` to 40+ digits (own fresh `mpmath`, `dps=50`) and
`u^\ast\in(\pi/6,\pi/3)` so the cofactor `-8\sin u^\ast\cos^2u^\ast\ne0`,
confirmed by direct rational-comparison bound; (c) `D_1(A^\ast,B^\ast)=0`
independently confirmed to `\approx10^{-42}` from the raw `D_1,\mathrm{RHS}`
definitions (own script, not the file's); (d) Steps 1-4's numerical
content (the derivative bound `D_1'\ge4$ near the corner, the value bound
away from it) independently spot-checked via a finite-difference sweep and
found consistent with the file's certified `mpmath.iv` enclosures (own
derivative sweep near `B^\ast$ gives `\approx4.626`, matching the file's
`\approx4.625`; own dense value sweep on `[B^\ast,\pi/3]` finds no
violation). **This lemma (`D_1(A)\ge0` on `\mathcal C=\mathcal
C_{\mathrm{lo}}`) is genuinely proved and certified — Gap 6 is closed.**
(Note: this closes Gap 6 specifically. Whether the whole approach's "Full
proof" is complete is a separate question, adjudicated in
`coordinate-bash-resultant-boundary-pointwise-tangent.md`'s own Status —
see `current.md` round 18: a different, previously-unflagged gap was
found elsewhere in that file's Step 3, unrelated to this lemma.)
