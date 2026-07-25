## Lemma (isosceles case `AB=AC`: `OM=ON` by reflection symmetry, no `Q`/Ptolemy/branch-selection needed)

**Statement.** Let `ABC` be a triangle with `AB=AC`, `M,N` the midpoints of
`AB,AC`, and `K,L` points satisfying imo-2026-02's hypotheses (the
containments `K\in\triangle BMC`, `L\in\triangle BNC`, `K` inside
`\angle LBA`, `L` inside `\angle ACK`, and the angle equalities
`\angle KBA=\angle ACL`, `\angle LBK=\angle LNC`, `\angle LCK=\angle BMK`).
Suppose in addition `K\ne L` (see "What remains open" below). Then `A,K,L`
are non-collinear, `O:=$ circumcenter of `A,K,L` exists, and `OM=ON`.

This is proved directly by an explicit reflection isometry — **no
reference to** the auxiliary point `Q` (whose own definition degenerates,
`Q=A`, exactly when `AB=AC`, which is why no prior approach in this
population's history could handle this case via the `Q`-based reduction),
**no** Ptolemy-type identity, and **no** appeal to the rotation-
parametrization/Weierstrass/Gröbner branch-selection machinery used for
the scalene case elsewhere in the population.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant.md`, §10 (round
4), building on imported machinery from `approaches/ptolemy-trig-identity.md`
(angle notation `θ,ψ,φ`, Lemma 1's two-ray construction of `K,L`, and the
decoupled constraint equations (III),(IV)) and the already-certified
`lemmas/sigma-symmetry.md` (the abstract relabeling `σ`: swap
`B\leftrightarrow C, K\leftrightarrow L, M\leftrightarrow N`, here realized
as an honest Euclidean isometry because the ambient triangle is itself
symmetric). Originally identified (informally, as a "free proof," not yet
with the existence/uniqueness step closed) by this round's ptolemy-lens
math-explorer; the existence/uniqueness gap it flagged is closed here.

## Setup (imported notation)
`a=BC,b=CA,c=AB` (so `AB=AC \Leftrightarrow b=c`); `θ:=\angle KBA=\angle ACL`
(hypothesis 1's shared parameter); `ψ:=\angle LCK` (hypothesis 3's left
side); `φ:=\angle LNC` (hypothesis 2's left side). Lemma 1 of
`ptolemy-trig-identity.md`: `K` is the intersection of (ray from `B` at
angle `θ` from ray `BA`, on the `C`-side of line `AB`) and (ray from `C`
at angle `θ+ψ` from ray `CA`, on the `B`-side of line `AC`); `L` is the
intersection of (ray from `B` at angle `θ+φ` from ray `BA`, `C`-side of
`AB`) and (ray from `C` at angle `θ` from ray `CA`, `B`-side of `AC`).
Lemma 3 of the same file: `ψ` solves (III), a transcendental equation in
`θ,ψ,A,C` only; `φ` solves (IV), the same equation with `B,C` swapped.

## Proof

### Step 1 — `B=C`
`AB=AC` and the Law of Sines `b/\sin B=c/\sin C` give `\sin B=\sin C`.
Since `B,C\in(0,\pi)` and `B+C=\pi-A<\pi` (as `A>0`), the alternative
`B=\pi-C` (also compatible with `\sin B=\sin C`) would force `A=0`,
excluded. Hence `B=C`.

### Step 2 — the domain of `(θ,ψ)` (resp. `(θ,φ)`), made explicit
In Lemma 2 of `ptolemy-trig-identity.md`, triangle `BKC` has
`\angle KBC=B-\theta`, `\angle KCB=C-\theta-\psi`; for a genuine triangle,
both must be positive, giving the domain `\theta\in(0,B)`,
`\psi\in(0,C-\theta)`. Symmetrically, triangle `CLB` gives
`\theta\in(0,C)`, `\varphi\in(0,B-\theta)`. When `B=C` (Step 1) these two
domains coincide: `\theta\in(0,B)`, `\psi,\varphi\in(0,B-\theta)`.

### Step 3 — existence and uniqueness of the common root: `ψ=φ`
When `B=C`, (III) and (IV) become the **identical** equation (swapping
`B\leftrightarrow C` in (IV)'s formula and setting `B=C` returns (III)'s
formula verbatim). Fix `θ\in(0,B)` and write this common equation as
`\Phi(\theta,x)=0` for `x\in(0,B-\theta)`, where
$$f(x):=\frac{\sin x}{\sin(\theta+x)},\qquad g(x):=\frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta-x)}{\sin(A+2\theta+x)},\qquad \Phi(\theta,x):=f(x)-g(x).$$

**Well-definedness and positivity.** For `x\in(0,B-\theta)`:
`\theta+x\in(0,B)\subset(0,\pi)`, so `\sin(\theta+x)>0`;
`B-\theta-x\in(0,B)`, so `\sin(B-\theta-x)>0`; and
`A+2\theta+x<A+2\theta+(B-\theta)=A+B+\theta=A+C+\theta<A+B+C=\pi` (using
`B=C` then `\theta<B`), while `A+2\theta+x>A>0`, so
`A+2\theta+x\in(0,\pi)` and `\sin(A+2\theta+x)>0`. Hence `f,g` are
well-defined and strictly positive throughout `(0,B-\theta)`.

**Monotonicity.** The angle-subtraction identity
`\sin(\theta+x)\cos x-\cos(\theta+x)\sin x=\sin\theta` gives
$$f'(x)=\frac{\cos x\sin(\theta+x)-\sin x\cos(\theta+x)}{\sin^2(\theta+x)}=\frac{\sin\theta}{\sin^2(\theta+x)}>0,$$
so `f` is strictly increasing. For `g`, set `u:=B-\theta-x` (`u'=-1`),
`v:=A+2\theta+x` (`v'=1`); the same identity applied to `u,v` gives
$$g'(x)=-\frac{2\sin A}{\sin B}\cdot\frac{\sin(u+v)}{\sin^2 v},\qquad u+v=A+B+\theta=(\pi-C)+\theta=\pi-B+\theta\ \ (\text{using }B=C),$$
so `\sin(u+v)=\sin(\pi-B+\theta)=\sin(B-\theta)>0` (as `B-\theta\in(0,B)`),
giving `g'(x)=-\frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta)}{\sin^2 v}<0`.
So `g` is strictly decreasing, and `\Phi(\theta,\cdot)=f-g` is **strictly
increasing** on `(0,B-\theta)`.

**Boundary values and existence.** As `x\to0^+`: `f\to0`,
`g\to\frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta)}{\sin(A+2\theta)}>0`,
so `\Phi\to` a negative value. As `x\to(B-\theta)^-`: `g\to0`,
`f\to\sin(B-\theta)/\sin B>0`, so `\Phi\to` a positive value. `\Phi(\theta,\cdot)`
is continuous on `(0,B-\theta)` (quotient of continuous, non-vanishing-
denominator functions there), so by the intermediate value theorem it has
at least one root, and by strict monotonicity at most one. Hence a
**unique** root `x(\theta)\in(0,B-\theta)`.

Since `ψ` solves `\Phi(\theta,\cdot)=0$ (via (III)) and `φ` solves the same
equation (via (IV), identical when `B=C`), both equal this same unique
root:
$$\psi=\varphi=x(\theta)\qquad\text{for every }\theta\in(0,B).$$

### Step 4 — reflection sends `K` to `L`
Let `\sigma_{\mathrm{refl}}` denote reflection across the perpendicular
bisector of `BC` (the triangle's axis of symmetry, which passes through
`A` exactly because `AB=AC`). `\sigma_{\mathrm{refl}}` fixes `A`, swaps
`B\leftrightarrow C`, and maps the closed triangle `ABC` to itself as a
set. Consequently it sends ray `BA\mapsto` ray `CA` and ray
`CA\mapsto` ray `BA` (a ray from `P` through the fixed point `A` maps to
the ray from `\sigma_{\mathrm{refl}}(P)` through `A`), preserves angle
magnitudes, and — since it maps the triangle to itself while swapping
`B,C` — sends "`C`-side of line `AB`" to "`B`-side of line `AC`" (and vice
versa); this side-swap is exactly the combinatorial content already
certified in `lemmas/sigma-symmetry.md`'s abstract relabeling `σ`, here
realized as an actual isometry because the triangle itself is symmetric.

Applying `\sigma_{\mathrm{refl}}` to `K`'s two defining rays (Lemma 1):
- (ray from `B`, angle `θ` from `BA`, `C`-side) `\ \mapsto\ ` (ray from
  `C`, angle `θ` from `CA`, `B`-side) — exactly `L`'s second defining ray;
- (ray from `C`, angle `θ+ψ` from `CA`, `B`-side) `\ \mapsto\ ` (ray from
  `B`, angle `θ+ψ` from `BA`, `C`-side) `=` (ray from `B`, angle `θ+φ` from
  `BA`, `C`-side) (using `ψ=φ`, Step 3) — exactly `L`'s first defining ray.

`K` is the intersection of its two rays, so `\sigma_{\mathrm{refl}}(K)` is
the intersection of the two images — which are exactly `L`'s two defining
rays. Hence
$$\sigma_{\mathrm{refl}}(K)=L.$$

### Step 5 — `OM=ON`
`\sigma_{\mathrm{refl}}` fixes `A`, sends `B\mapsto C` hence
`M=$midpoint`(A,B)\mapsto$ midpoint`(A,C)=N`, and sends `K\mapsto L$ (Step
4). Since `\sigma_{\mathrm{refl}}` is an involution, applying it to
`\sigma_{\mathrm{refl}}(K)=L` gives `\sigma_{\mathrm{refl}}(L)=K`. Hence
`\sigma_{\mathrm{refl}}` maps the point set `\{A,K,L\}` to
`\{A,L,K\}=\{A,K,L\}` (the same set). Given `A,K,L` non-collinear (Step
6), the circumcircle `\omega=\mathrm{circle}(A,K,L)` exists and is
unique, and `\sigma_{\mathrm{refl}}(\omega)` is the circle through the
same point set, i.e. `\omega` itself: `\sigma_{\mathrm{refl}}(\omega)=\omega`.
The center of a circle is an isometry-equivariant invariant, so
`\sigma_{\mathrm{refl}}(O)$ is the center of `\sigma_{\mathrm{refl}}(\omega)=\omega`,
i.e. `\sigma_{\mathrm{refl}}(O)=O`. Since `\sigma_{\mathrm{refl}}` is an
isometry,
$$OM=d(O,M)=d(\sigma_{\mathrm{refl}}(O),\sigma_{\mathrm{refl}}(M))=d(O,N)=ON.\qquad\blacksquare$$

### Step 6 — non-collinearity of `A,K,L`
Two ways `A,K,L` could fail to determine a genuine circle: (i) `K` lies on
the axis of symmetry, forcing `K=L` (since `\sigma_{\mathrm{refl}}` fixes
points of the axis, and `\sigma_{\mathrm{refl}}(K)=L`); or (ii) `K\ne L`
but line `AK` is the *other* line through `A` mapped to itself by
`\sigma_{\mathrm{refl}}`, namely the line through `A` perpendicular to the
axis, i.e. parallel to `BC` (a reflection fixes, as a set, exactly the
mirror line and the lines perpendicular to it through points of the
mirror line) — combined with `\sigma_{\mathrm{refl}}(K)=L`, this would put
`A,K,L` on that one line, i.e. collinear.

**(ii) is ruled out unconditionally.** Coordinates: `A=(0,h)`, `B=(-d,0)`,
`C=(d,0)`, `h,d>0` (axis = `y`-axis; `AK\parallel BC \iff K$ has
`y`-coordinate `h`). `M=(-d/2,h/2)`; the closed triangle `BMC` (vertices
`B=(-d,0),M=(-d/2,h/2),C=(d,0)`, all with `y\le h/2`) is convex, hence
entirely contained in `\{y\le h/2\}`, so no point of it — interior or
boundary — has `y=h$. Since `K` is hypothesised strictly interior to
`\triangle BMC`, its `y`-coordinate is `<h/2<h`, so `K` is never on the
line `y=h`: (ii) cannot occur, for **every** isosceles triangle and
**every** genuine `K`.

**(i) is not independently excluded here.** Whether the axis passes
through the interior of `\triangle BMC` at exactly the specific point
`K(\theta,x(\theta))` for some `\theta\in(0,B)` is not ruled out by
containment alone (unlike (ii): the axis `x=0` does separate `B,M`
(`x<0`) from `C` (`x>0`) and so genuinely crosses the interior of
`\triangle BMC` for a range of triangle shapes). Excluding it for every
`θ` would require the explicit `x`-coordinate of `K` through the
Weierstrass/rotation parametrization used elsewhere in the population, a
further symbolic computation not carried out this round.

## What remains open

`K\ne L` (equivalently: `K` does not lie exactly on the axis of symmetry)
is **not independently proved** here for the isosceles sub-case. This is
not a new gap introduced by this lemma: every approach in the population
already assumes `A,K,L` form a genuine, non-degenerate triangle whenever
it speaks of "the circumcenter `O` of `A,K,L`" (implicit in the problem's
own claim, which presupposes `O` exists). This lemma inherits exactly
that standing assumption for the one remaining degeneracy mode (i); it
does *not* need any assumption beyond that standing one, and it *does*
independently and unconditionally rule out the other possible degeneracy
mode (ii, `AK\parallel BC`). A future round wishing to remove this last
inherited assumption would need to track `K`'s coordinate through the
explicit rotation parametrization (`K=B+t_1(-\cos\beta,\sin\beta)` etc.,
as in `coordinate-bash-resultant.md`) specialized to `b=c`, and show its
component along the axis direction never vanishes for `\theta\in(0,B)`.

## Status
**Certified by the proof-reviewer (round 4).** Independently rebuilt Step
3's monotonicity/IVT argument from scratch (own `sympy` differentiation,
imposing the isosceles constraint `A=\pi-2B` in place of the general
`A+B+C=\pi`): confirmed `f'(x)=\sin\theta/\sin^2(\theta+x)` and
`g'(x)=-\frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta)}{\sin^2(A+2\theta+x)}`
exactly (symbolic difference identically 0), and confirmed the boundary
signs `\Phi(\theta,0^+)<0`, `\Phi(\theta,(B-\theta)^-)>0` numerically over
3000 random `(\theta,B)\in(0,\pi/2)` samples with zero exceptions — the
existence-and-uniqueness argument for the shared root `x(\theta)=\psi=\varphi`
is correct and complete, no gap found. Step 6(ii)'s non-collinearity
argument (elementary convexity/height bound) was also independently
checked and found sound. Steps 4–5 (the reflection argument giving
`OM=ON`) are elementary isometry reasoning and contain no gap.

**One precisely isolated point remains open, honestly disclosed by the
file and confirmed still open by the reviewer**: Step 6(i), `K\ne L`
(equivalently, `K` does not lie exactly on the triangle's axis of
symmetry) is **not** independently proved for the isosceles sub-case — it
is inherited from the population's standing non-degeneracy assumption
(that `A,K,L` form a genuine triangle, implicit whenever "the circumcenter
of `A,K,L`" is invoked). This is an acceptable standing assumption
consistent with how every other approach in the population treats
non-degeneracy (no approach has independently verified `A,K,L`
non-collinear in general either), so it does not block certification of
the *stated* result (existence/uniqueness of `x(\theta)` and the
reflection-symmetry conclusion conditional on `K\ne L`), but it should be
carried forward explicitly as a residual item if a future round seeks a
fully unconditional isosceles-case proof.

**Certified**: for every isosceles triangle `AB=AC` and every `\theta\in(0,B)`
with `K\ne L` (the one inherited, not-independently-verified
non-degeneracy condition above), `OM=ON`.
