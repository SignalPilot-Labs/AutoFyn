## Lemma: Decoupling Lemma and Sweep Lemma (general, reusable)

**Source approach:** coordinate-trig-bash (round 2). Certified by proof-reviewer, round 2.
Independently re-derived and numerically confirmed by the reviewer (angle
values agree to machine precision as r1/θ vary while r2 is held fixed, and
vice versa).

### Setup
Working in the frame `B=(-1,0)`, `C=(1,0)`, `A=(p,q)`, `q>0`, with
`M=(A+B)/2`, `N=(A+C)/2`. Let `φ_B = atan2(q,p+1)` (polar angle of ray BA
from B), `φ_C = atan2(q,p-1)` (polar angle of ray CA from C). For
`θ ∈ (0,min(β,γ))` the containment hypotheses force
`K = B + r1·(cos(φ_B−θ), sin(φ_B−θ))`, `r1>0`, and
`L = C + r2·(cos(φ_C+θ), sin(φ_C+θ))`, `r2>0` (this ray parametrization is
Lemma 3 of `coordinate-om-on-reduction.md`'s companion approach file,
`approaches/coordinate-trig-bash.md`).

### Lemma 4 (Decoupling)
`F1(θ,r1,r2) := ∠LBK − ∠LNC` depends only on `(θ,r2)`, not `r1`.
`F2(θ,r1,r2) := ∠LCK − ∠BMK` depends only on `(θ,r1)`, not `r2`.

*Proof.* For any vertex `V`, fixed unit direction `u`, and point
`P = V + r·u` (`r>0` free) on a fixed ray from `V`, and any other point
`Q ≠ V`: `∠(V;P,Q) = arccos[u·(Q−V) / (|u|·|Q−V|)]` — the scale factor `r`
cancels top and bottom of the defining cosine formula, so the angle depends
only on the ray's direction `u`, never on how far along it `P` sits. Apply
this with `V=B,P=K` (angle `∠LBK`, `Q=L` fixed given `θ,r2`) to see no
`r1`-dependence, and with `V=N` (angle `∠LNC`, no `K` or `r1` appearing at
all) to see `F1` depends only on `(θ,r2)`. Symmetrically with `V=C,P=L`
(angle `∠LCK`) and `V=M` (angle `∠BMK`, no `L` or `r2` appearing) for `F2`. ∎

### Lemma 5 (Sweep Lemma)
Let `V` be a fixed point and `P(t) = V+v0+t·u` (`t ∈ ℝ`) a point moving along
a line through direction `u` (`|u|=1`), with `v0` not parallel to `u` (so
`V` does not lie on the line). Writing `v(t) := P(t)-V = v0+t·u`, the polar
angle `ψ(t) := arg(v(t))` is differentiable with
`dψ/dt = cross(v0,u) / |v(t)|^2`, where
`cross(v0,u) := (v0)_x u_y − (v0)_y u_x`, a quantity **independent of `t`**
(hence of constant sign throughout the motion). In particular `ψ(t)` is
strictly monotonic in `t`, increasing if `cross(v0,u)>0`, decreasing if `<0`.

*Proof.* `dψ/dt = (v_x v_y' − v_y v_x')/(v_x^2+v_y^2) = cross(v(t),u)/|v(t)|^2`
(standard derivative of `atan2` along a curve, `v_x'=u_x,v_y'=u_y`).
`cross(v(t),u) = cross(v0+t·u,u) = cross(v0,u) + t·cross(u,u) = cross(v0,u)`
since `cross(u,u)=0` identically. As `V` is not on the line, `v(t)≠0` for all
`t`, so `|v(t)|^2>0` throughout, giving `dψ/dt` a constant sign equal to
`sign(cross(v0,u))` (nonzero exactly when `v0 ∦ u`). ∎

### Status and scope
Both lemmas are fully general and elementary (pure calculus/vector algebra);
they are reusable well beyond this problem for any "point sliding along a
fixed ray, angle from a fixed external vertex" computation. They do **not**
by themselves establish the monotonicity of `F1` in `r2` or `F2` in `r1` on
the *literal* geometric angles `∠LBK, ∠LNC, ∠LCK, ∠BMK` over their claimed
full domain — see the caveat below.

**Important caveat (found by the proof-reviewer, round 2 — NOT part of the
certified content, recorded here to prevent re-use error):** applying the
Sweep Lemma gives monotonicity of the *polar angle* `ψ_V(r)` of the moving
point as seen from `V`. To conclude monotonicity of the *geometric angle*
`∠(V;P,Q)` itself (an unsigned quantity in `[0,180°]`, obtained from
`arccos`), one must additionally know that the *sign convention*
`∠(V;P,Q) = |fixed direction of Q from V| − ψ_V(r)` (or its mirror) holds
with a **fixed order** throughout the whole domain — i.e., that the moving
ray `VP` never crosses the fixed ray `VQ`. This ordering was **asserted**
(not proved) in the "Sign convention" paragraphs of `coordinate-trig-bash`'s
round-2 Lemma 6/7 write-up, and the reviewer found an explicit numerical
counterexample where it fails (see review notes / `current.md`): for
`(p,q)=(0.0025,5.0)` and `θ` beyond `~32°`, the ray `BL` sweeps past the ray
`BK` before `r2` reaches `r2max(θ)`, so `∠LBK` (the unsigned angle) is *not*
monotonic on the full domain `(0,r2max(θ))`, even though the polar angle
`ψ_B(r2)` is (as the Sweep Lemma guarantees). **Do not certify or reuse
"F1/F2 monotonic on the full domain `(0,r2max(θ))`" as an established fact**
— only the Decoupling Lemma and the Sweep Lemma itself (stated purely in
terms of the polar angle `ψ`) are certified here.
