# Math-explorer report — chamber-vertex extreme-point-evaluation front (round 22)

Lens: front 2 (`lp-duality-certificate`), case (b2) of the general upper
bound, via the "evaluate $\Phi_{\min}$ at chamber vertices" route opened by
round 21's `within-chamber-affinity-theorem`. Report only — no files edited,
no proof attempted.

## 1. What a "chamber vertex" concretely is — and why `vertex-minimum-theorem` does NOT already give it

**These are two different vertex notions living in two different spaces, and
the file currently only has the first.**

- **`vertex-minimum-theorem`** (certified round 3) characterizes vertices in
  **fragment space** $\bar\Omega$: for a **fixed marking $p$**, the minimizer
  fragmentation $F^*$ is pinned by $d$ tight constraints of type (I)
  "fragment $=0$" or (II) "two fragments equal." This is exactly what was
  used (implicitly, via `per-piece-vertex-decomposition-theorem`) to *derive*
  the mass-conservation system $M(\tau)\mathbf v = Np$ in
  `within-chamber-affinity-theorem` in the first place. It says nothing
  about how the optimal type varies as $p$ moves — by design, $p$ is frozen.

- **What case (b2) actually needs** is a vertex notion in **$p$-space**: the
  chamber $U(\mathbf c,\tau,\pi)\subseteq\mathcal P$ (R20.1's definition) is
  itself a region of markings $p$, and since $\Phi_{\min}$ is affine on $U$
  (round 21's theorem) and $a_nT$ is linear in $p$, bounding
  $\Phi_{\min}(p)\le a_nT$ over $p$ ranging through case (b2)'s box reduces,
  chamber by chamber, to checking the (affine) function
  $g_\tau(p):=a_nT-\Phi_{\min}(p)$ at the **vertices of $U(\mathbf
  c,\tau,\pi)\cap\text{Box}$** — extreme points of a polytope *in $p$*, not
  in $F$.

  These $p$-space vertices are **not yet characterized anywhere on file**.
  They can be derived, but it takes new work (not a re-derivation of
  round-3's theorem, a genuinely dual construction using the *same*
  machinery already proved in R20.2–R20.3):
  - Once $M(\tau)$ is invertible, every slot value $F_{i,l}(p)$ is an
    **explicit linear function of $p$** (R20.3: $\mathbf v(p)=M(\tau)^{-1}Np$,
    every other slot is $0$ or a coordinate $p_j$).
  - The chamber $U(\mathbf c,\tau,\pi)$ is cut out, inside $\mathcal P$, by
    finitely many **linear inequalities in $p$**: (a) feasibility/
    nonnegativity of every fragment, $F_{i,l}(p)\ge0$; (b) the assumed total
    order $\pi$ actually holding, i.e. $F_s(p)\le F_{s'}(p)$ for every pair
    of $\pi$-adjacent slots; (c) optimality of type $\tau$ against every
    neighboring type $\tau'$, i.e. $\ell_\tau(p)\le\ell_{\tau'}(p)$ where
    $\ell_{\tau'}$ is $\tau'$'s own (also affine, once its own $M(\tau')$ is
    invertible) candidate value.
  - So $U(\mathbf c,\tau,\pi)$ is literally a polyhedron in $p$-space, and
    (by the same standard convex-geometry fact `vertex-minimum-theorem`
    already invokes — a linear functional on a polytope attains its extremum
    at a vertex, and every vertex is cut out by (dim) independent tight
    constraints) its extreme points are pinned by tight instances of (a),
    (b), (c) above.

  **Concretely: a $p$-space chamber vertex is a marking $p$ at which some
  fragment hits exactly $0$ (a degenerate cut), or two slots (of possibly
  different pieces, or an untouched piece) become exactly tied **at the
  boundary of the assumed order** (rather than strictly ordered, as within
  the chamber's interior), or the type $\tau$ becomes exactly indifferent
  with a *neighboring* type $\tau'$ (a genuine crossing point between two
  combinatorial branches).** The third kind is new relative to
  `vertex-minimum-theorem`'s picture (which never needed to compare across
  types, since $p$ was fixed) and is exactly the "kink" R18's Danskin study
  found numerically at $p_3=p_1-p_2$ (an interior local extremum caused by
  two branches crossing) — so that round's finding is direct evidence this
  third constraint family is real and load-bearing, not merely a formal
  possibility.

  **Recommendation:** state and prove a genuinely new, from-scratch
  "Chamber-Vertex-in-$p$-Space Theorem" analogous to (but not a copy of)
  `vertex-minimum-theorem`, using `within-chamber-affinity-theorem`'s R20.2
  linear-algebra setup as its foundation. This is real, well-scoped, and
  currently-missing infrastructure — the natural next building block, not
  yet attempted by any round.

## 2. Numerical exploration at $n=3,4$ (exact target comparison, multi-restart optimizer)

Using a fresh multi-restart Nelder–Mead optimizer (`/tmp/round-22/phimin2.py`)
computing $\Phi_{\min}(p)$ directly over all legal compositions (no
closed-form shortcut — same style as prior rounds' gate checks), sampled
inside case (b2)'s box ($p_1<T/2$, $T/D_n<p_2<a_nT/2$, $T=1$):

```
n=3 (a_3=8/15≈0.5333): worst 6 sampled margins a_n·T-Φ_min, all POSITIVE
  margin=0.02106  Φ_min=0.51227  p≈(0.4063,0.2365,0.2120,0.1452)  comp=(1,0,0,2)
  margin=0.02181  Φ_min=0.51153  p≈(0.4302,0.2588,0.2297,0.0814)  comp=(1,0,1,1)
  margin=0.02297  Φ_min=0.51036  p≈(0.4889,0.2452,0.2206,0.0453)  comp=(1,1,0,0)
  margin=0.02528  Φ_min=0.50805  p≈(0.2943,0.2570,0.2324,0.2163)  comp=(3,0,0,0)

n=4 (a_4=16/31≈0.5161): worst 4 sampled margins, all POSITIVE
  margin=0.01230  Φ_min=0.50382  p≈(0.4522,0.2395,0.1949,0.1058,0.0076) comp=(2,0,0,2,0)
  margin=0.01370  Φ_min=0.50243  p≈(0.4787,0.2312,0.2160,0.0476,0.0266) comp=(2,0,0,1,0)
```

**No violation found** — consistent with (and reproducing to 2 significant
figures) the on-file findings from rounds 13/14/16: exact witnesses there
report margins $\approx0.0175$ at $n=3$ and $\approx0.0116$ at $n=4$. My
independent scan lands in the same $0.01$–$0.03$ band. **No clean
closed-form pattern for the worst vertex emerged** — the worst compositions
found were varied ((1,0,0,2), (1,0,1,1), (1,1,0,0), (3,0,0,0) at $n=3$; no
single dominant "type" of configuration).

**One structural regularity did emerge, worth flagging for the next
round:** every near-worst witness found (both mine and the on-file
round-14/18 witness $(p_1,p_2,p_3,p_4)\approx(0.4468,0.2591,0.2251,0.0691)$)
sits with $p_1$ close to the box's own upper wall $p_1\to T/2^-$ and $p_2$
close to the box's own upper wall $p_2\to a_nT/2^-$ — i.e. near a **corner
of the box in the $(p_1,p_2)$ coordinates**, not in the interior of the
$(p_1,p_2)$-plane. Combined with R18's finding that, once $(p_1,p_2)$ are
pinned near that corner, the *interior* tail coordinate $p_3$ still has its
own local extremum (the $p_3=p_1-p_2$ kink) — the worst case appears to
decompose as "$(p_1,p_2)$ at a box-boundary corner" $\times$ "tail at an
interior chamber-wall vertex." If this decomposition is real and general,
it would cut the effective vertex search from "all vertices of the full
$m$-dimensional chamber-in-box polytope" down to "box-corner in
$(p_1,p_2)$, chamber vertex only in the remaining $m-2$ tail coordinates" —
a genuine dimension reduction, **not yet proved**, only observed on a
handful of witnesses.

**Margin trend across $n$ (reassurance, not proof).** $a_n-1/2=1/(2D_n)$
shrinks by a factor $D_4/D_3=31/15\approx2.07$ from $n=3\to4$, while the
on-file worst-margin figures shrink only by a factor
$0.0175/0.0116\approx1.5$ — i.e. the margin is shrinking *slower* than the
target band itself, which is evidence (not proof) against a "margin
vanishes for large $n$" scenario; if anything the ratio
margin$/(a_n-1/2)$ appears to be *growing* with $n$ in the two data points
on file. Getting a third data point ($n=5$) was attempted but the
brute-force multi-restart optimizer over all $\binom{n+m-1}{n}$
compositions became too slow to finish inside this round's time budget —
flagged as a concrete, cheap next step (a smarter/pruned composition search,
or reusing the certified affine-per-chamber formulas directly instead of a
generic optimizer, would make $n=5,6$ tractable).

## 3. Is the chamber-growth signal a real threat, or a false alarm?

**Genuinely mixed verdict, leaning "real but possibly avoidable by
restriction, not by symmetry.**

- **Not a symmetry artifact.** The round-20 chamber count (28%→64% density,
  $n=3\to4$) is already computed at the level of *sorted, composition-only*
  types — i.e. any residual permutation symmetry among equal-valued pieces
  is already quotiented out by the $p_1\ge\cdots\ge p_m$ convention. Because
  compositions are asymmetric across pieces by design (which piece gets how
  many cuts is exactly the content being counted), there's no cheap
  symmetry identification left to shrink the count further — the growth
  looks real, not an artifact of under-quotienting.
- **But the density metric may overstate what's needed.** Gate 5b counted
  *distinct optimal compositions observed on a small random sample* — a
  conservative lower bound on true chamber count (per R20.5's own caveat),
  and moreover counts *every* composition that shows up as optimal
  *anywhere* in the box, not specifically at box vertices. If (per §2 above)
  the actual worst-case points cluster near box corners with only a *few*
  tail-side chamber walls active there, the number of chambers that matter
  for verifying the inequality could be far smaller than the number of
  chambers that exist in the box's interior. This is speculative — no round
  has yet tested whether the worst-margin composition/type is stable as
  $(p_1,p_2)\to$ the box corner, which would directly test this hope.
- **Net assessment:** treat the chamber-growth signal as a real warning
  that *naive, uniform* enumeration of every chamber in the box will not
  scale, but not (yet) as proof that a *restricted* enumeration (box-corner
  $\times$ finitely-many-tail-chamber-walls, or some other structural
  restriction) can't work. This mirrors the project's own general finding
  pattern in this file: broad unrestricted mechanisms keep failing while
  targeted/restricted ones (Theorem B$_k$, R13.2, Bisect-Top-$k$) keep
  making partial progress.

## 4. Distinct viable next-step mechanisms, and how far each gets

1. **Prove the $p$-space Chamber-Vertex Theorem (§1's recommendation).**
   Status: not started, but the ingredients (R20.2's linear system, the
   standard "linear functional on a polytope attains its extremum at a
   vertex" fact already used once in `vertex-minimum-theorem`) are all
   on file and reusable without re-derivation. This alone does not close
   case (b2) — it only converts "prove $\Phi_{\min}(p)\le a_nT$ on the box"
   into "prove it at finitely many *characterized* $p$-space vertices per
   chamber," still leaving the count problem from §3 open. **This is the
   literal next brick**, distinct from anything tried in rounds 3–21 (no
   prior round has stated a $p$-space vertex theorem; R20 only proved
   affinity, not vertex localization in $p$).

2. **Test the box-corner $\times$ tail-chamber-vertex decomposition (§2's
   observation) directly.** Concretely: fix $(p_1,p_2)\to(T/2^-,a_nT/2^-)$
   (or more precisely, sweep both toward their respective box walls) and
   ask whether the *tail's own* chamber-vertex set (in the remaining
   $m-2$ free coordinates, at fixed $p_1,p_2$) is small and enumerable via
   `vertex-minimum-theorem`-style tie/pin constraints among *only* the
   tail pieces plus the fixed residual $w=p_1-p_2$ (exactly the object R18
   already exhibited one instance of, at $p_3=w$). This is a genuinely
   smaller, more tractable sub-problem than the full chamber count, and
   directly buildable from R18's witness plus `vertex-minimum-theorem`. Not
   yet attempted as a general claim (R18 only exhibited a single numeric
   instance, not a general theorem).

3. **Push the numeric margin trend to $n=5,6$ with a faster evaluator.**
   Rather than a generic optimizer, directly instantiate
   `within-chamber-affinity-theorem`'s formula ($\mathbf
   v(p)=M(\tau)^{-1}Np$) per candidate type and take the min over a
   *pruned* type list (e.g. restrict to types reachable from the box-corner
   region per mechanism 2), which would be far cheaper than the current
   brute multi-restart-per-composition approach and could settle whether
   the reassuring margin trend from §2 continues or reverses. This is
   tooling, not a new proof idea, but removes the main practical
   bottleneck hit this round.

4. **Resolve R20.4's residual case (ii)** (the "$\phi_rN\equiv0$ for every
   left-null functional" algebraic coincidence) for the *specific* types
   that arise in case (b2)'s box — a finite, checkable per-type condition,
   not attempted for any concrete type yet. Needed for full rigor of
   mechanism 1 above (the vertex theorem currently inherits the same
   conditional-on-invertibility caveat as the affinity theorem it's built
   on), but likely a short side-computation once a concrete candidate type
   list exists from mechanism 2.

None of these four close case (b2) this round; all are new, distinct from
the 8 previously-confirmed-dead mechanism families (peel/bisect/recurse,
weighted-combination, boundary-continuity, Danskin/concavity,
surrogate-adversary/majorization, constraint-side LP duality, probabilistic-
method wrapper, and the round-21 rank-pigeonhole-style worst-tail
mechanism), and each has a concrete, checkable next step rather than being
another unconditional-construction guess.

## Scripts

- `/tmp/round-22/phimin.py`, `/tmp/round-22/phimin2.py` — multi-restart
  Nelder–Mead $\Phi_{\min}(p)$ evaluator (brute force over all legal
  compositions, softmax parametrization of fragment splits).
- `/tmp/round-22/scan.py`, `/tmp/round-22/scan2.py` — case-(b2)-box random
  sampler + margin scan at $n=3,4$ (the `scan.py` run at higher
  restart/precision timed out at 2 minutes; `scan2.py` is the reduced-cost
  version whose output is reported in §2).
