# Proof review — IMO 2026 P2 (imo-2026-02), round 1

Problem: prove `OM=ON` where `O=circumcentre(AKL)`, `M,N` midpoints of `AB,AC`, under the
three angle conditions + region/inside-angle hypotheses. `proof_only`, no numeric answer.

I re-ran `results/imo-2026-02/verify.py` and wrote fully independent sympy/numpy checks
(exact ideal membership; construction of genuine admissible configurations satisfying all
six hypotheses to machine precision).

---

## Slug 1 — `trig-metric-identity`  →  VERDICT: CHANGES REQUESTED (true Status: partial)

Builder recorded **solved**. I override to **partial**: the core is correct and I verified
the hard content exactly, but there is one real, unaddressed logical gap.

**What I verified independently (all pass):**
- **Reduction (1a).** `OM=ON ⟺ O_x=(2p+a)/4` — correct (difference-of-squares, `M,N` share
  height `q/2`). Also matches the `OB²−OC²=(AB²−AC²)/2` form.
- **Branch/orientation lemma (1b).** I re-derived all four sign claims from region
  membership: `K,L` both clockwise of `BA` and CCW of `CA`
  (`cross(A−B,C−B)=−qa<0`, `cross(A−C,B−C)=qa>0`, `cross(A−C,M−C)=aq/2>0`,
  `cross(A−B,N−B)=−qa/2<0`), and the inside-angle betweenness gives the four oriented =
  unsigned angle equalities. Correct; conditions 2,3 convert to `E2=0`, `E3=0` with no lost
  sign. The forward direction "admissible ⟹ E2=E3=0" is exactly what the proof needs, and
  it holds.
- **Decoupling.** `E2=t_K·H(t_L)`, `E3=t_L·G(t_K)`, `H` free of `t_K`, `G` free of `t_L`,
  both quadratic — confirmed in a fresh reconstruction.
- **Crux cofactor identity (1c).** `T = q_G·G + q_H·H` — I recomputed it from scratch:
  `expand(q_G·G+q_H·H − T)=0` and the reduction remainder `=0`, both EXACT symbolic zeros
  (not numeric). I also evaluated `T` at exact rational roots of `G=0,H=0` for several
  random triangles: `T=0` every time.
- **End-to-end geometric sanity.** I constructed genuine admissible configurations
  (solved `G=0,H=0`, selected the root with `K∈△BMC`, `L∈△BNC`, all three angle
  equalities and both inside-angle conditions holding to `~1e-15`) for a scalene triangle
  at several `θ`, computed `O` directly, and got `OM−ON ~ 1e-15` and `O_x=(2p+a)/4`.
  (My first attempt appeared to fail only because of a scaling bug in MY test — the
  symbolic ray direction carries a factor `w=1+s²`; once matched, everything is exact.)

**The gap (single, load-bearing, currently unstated).** The inference
`G=H=0 ⟹ T=0` from `T=q_G·G+q_H·H` is only valid if the cofactors `q_G,q_H` are FINITE at
the configuration — i.e. their denominators are nonzero. `q_G,q_H` are rational functions
of `p,q,a,s` whose denominators are powers of the leading coefficients of `G,H`, which
factor as `(1+s²)²·AB²·AC²·f/…` with
```
      f = 2s(p²+q²) − 2aps + aq(1−s²).
```
Where `f=0`, the identity gives `0·∞` and does NOT yield `T=0`. The writeup asserts "(7) is
a genuine identity for every triangle … so `G=H=0` forces `O_x=(2p+a)/4`" — this conflates
"identity of rational functions" with "specializes to `T=0` at the config", which requires
`f≠0`. This is a real gap, not pedantry: the specialization genuinely fails on `{f=0}`.

**The gap is cleanly closable (one clean line — I verified it).** I found the geometric
meaning: `f = (1+s²)·AB·AC·sin(∠A+θ)` (checked symbolically, `f−rhs=0`). Hence `f=0 ⟺
∠A+θ=π ⟺ θ=π−∠A`. For every admissible config, `θ=∠KBA < ∠ABC` (ray `BK` lies strictly
inside angle `ABC` because `K∈△BMC`), and `∠ABC = π−∠A−∠C < π−∠A`, so `θ<π−∠A`, giving
`f>0`. I also scanned `f` over the entire admissible `θ`-range for four triangles: `f`
stays strictly positive throughout, never crossing zero. Adding this ~2-line argument
(or, equivalently, clearing denominators to a polynomial identity and noting `f≠0`) turns
the approach into a complete, rigorous proof.

**Scores.** Correctness 9/10 (everything present is correct; the one inference needs the
`f≠0` qualifier). Rigor 8/10 (one omitted justification). Progress: very high — this is
essentially a solved proof minus one clean line; furthest of the three by far.

**Certified lemmas from this approach:** goal-reduction, branch-orientation (both admitted
to `lemmas/`).

---

## Slug 2 — `equal-power-secants`  →  VERDICT: RETHINK (true Status: partial)

Builder recorded **partial** and recommended RETHINK of the distinctive move. Agreed.

- **L1 (power reformulation) — verified, certified.** `OM=ON ⟺ pow_M(⊙AKL)=pow_N(⊙AKL)
  ⟺ AO·BC=(AC²−AB²)/4`. Re-derived (power-of-a-point + vector expansion using `|OA|=R`);
  numerically confirmed `AO·BC=0.2=(AC²−AB²)/4` on an admissible config. Clean and reusable
  → promoted to `lemmas/goal-reduction.md` (consolidated with the coordinate form).
- **Distinctive engine (secant through `K`/`L`) is genuinely refuted:** no similarity or
  invariant concyclicity pins the second intersection; the only computable secant (through
  `A`) reproduces the shared reduction verbatim, using none of the angle data. The engine
  cannot advance the proof — routes back to the outliner.

**Scores.** Correctness 9/10 (L1 correct), Rigor 8/10, Progress low (L1 is the shared
reduction, distinctive move dead). Recorded outcome: dead-end (engine), L1 promoted.

---

## Slug 3 — `spiral-involution`  →  VERDICT: RETHINK (true Status: partial)

Builder recorded **partial**, engine RETHINK. Agreed.

- **L1 (σ-invariance) — verified, certified.** The relabelling `σ:(A↦A,B↔C,M↔N,K↔L)`
  fixes cond 1, swaps cond 2↔3, maps region hyps to region hyps, and fixes the conclusion
  (σ permutes `{A,K,L}` so fixes `O`, swaps `M,N`). Relabelling checked term by term.
  Correctly flagged as a formal symmetry, NOT an isometry — proves nothing alone.
- **L2 (supplementary relation) — verified, certified.** `∠LBA+∠NLC=π` (via
  `∠LBA=∠KBA+∠LBK=∠ACL+∠LNC`, `∠LCN=∠ACL`, and angle sum in `△LNC`), σ-image
  `∠KCA+∠MKB=π`. I confirmed both `=180.000°` on an independently-built admissible config.
- **Spiral-similarity engine refuted:** `△KLC≁△KBM` (angle multisets differ grossly), no
  forced similarity among the 7 points; conditions 2,3 give one angle each and cannot be
  upgraded. Engine dead → RETHINK.

L1 and L2 promoted to `lemmas/sigma-and-supplementary.md`.

**Scores.** Correctness 9/10 (L1,L2 correct), Rigor 8/10, Progress moderate (two genuine,
reusable synthetic lemmas), engine dead-end. Recorded: dead-end, L1/L2 promoted.

---

## Is the problem SOLVED?  NO — but very close.

`trig-metric-identity` is a correct proof modulo one cleanly-closable gap (justify `f≠0`,
i.e. `θ<π−∠A`, on the admissible region). Next round: dispatch the `trig-metric-identity`
builder to insert the `f=(1+s²)·AB·AC·sin(∠A+θ)>0` argument (using `θ=∠KBA<∠ABC<π−∠A`);
that upgrades it to `solved`. `current.md` Status set to `partial` with the exact gap.

Certified lemmas: `lemmas/goal-reduction.md`, `lemmas/branch-orientation.md`,
`lemmas/sigma-and-supplementary.md`.
</content>
