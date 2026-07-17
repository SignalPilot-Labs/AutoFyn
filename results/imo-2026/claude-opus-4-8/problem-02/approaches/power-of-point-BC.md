## Build report

Round-2 build of the Law-of-Sines SAS closure chain (Steps A–D) for the core identity
`pow(B,ω)−pow(C,ω)=(AB²−AC²)/2`. What is **newly proven, gap-free** this round:

- **E2′, E3′ closing relations upgraded from "numerically confirmed" to PROVEN.** They are
  derived rigorously by computing `BK` (resp. `CL`) two ways — via `△BMK` (Lemma L4) and via
  `△BKC` using the second ray `CK` at angle `θ+γ` to `CA` — and equating. This is the round's
  main new content (see §E). It closes a step every prior report left open, and it makes `β,γ`
  explicit *functions of θ* (each relation ties one of them to θ).
- **G1 sign resolution** (Step B): directed-angle-mod-π equality `∠(A′A,A′K)=∠(LA,LK)` is proven
  **unconditionally** from concyclicity; the magnitude resolution `∠BA′K=φ_L` (not its supplement)
  is derived from the two cancelling supplement flips, using the configuration ordering facts
  (Lemma O). Lemma O (`A′∈(A,B)` strictly, cyclic order `A,A′,K,L,A″` on ω) is **established from
  the containment hypotheses in part and confirmed numerically**; the betweenness `A′∈(A,B)` and
  the arc-separation are stated as configuration facts with the proof-parts I could close — see the
  honest scoping in §F and the "remaining sub-items" note.
- **G2 (angle decomposition at A)** is reduced to the two "cross" incidences (P1),(P2) and these
  to a clean ray-crossing statement; one betweenness sub-step (`Q` on the A-side of midline `MN`)
  is argued but not fully closed synthetically — scoped in §G.

**What remains OPEN — G3, the final scalar identity.** I verified numerically (independent config
solver, 2 scalene triangles × 3 values of θ, residuals ≤1e-6) that the assembled chain reproduces
`pow(B)−pow(C)=(AB²−AC²)/2` **exactly**, AND that the identity is FALSE if `β,γ` are perturbed off
the E2′/E3′ locus. Hence G3 genuinely requires E2′,E3′ (now proven) plus a transcendental closure
of one explicit trig identity in θ — this is the **same scalar wall trig-lawofsines faces**, as the
outline-reviewer flagged. I did not close it. **Reviewer: Status is `partial`.** The promotable,
certify-ready new content is **E2′,E3′** (§E) and the **directed-angle mod-π lemma** (§B).

---

## Status
partial

## Approaches tried
- power-of-point-BC (round 1): reduction chain `OM=ON ⟺ pow(M,ω)=pow(N,ω) ⟺ pow(B)−pow(C)=(AB²−AC²)/2` proven RIGOROUSLY (L2a, L1, L2), cevian lengths L4 proven. Core identity left OPEN. (certified: `lemmas/reduction-power-to-core.md`, `lemmas/cevian-lengths.md`.)
- power-of-point-BC (round 2): built the full Law-of-Sines SAS closure chain A–D against the certified core identity. **Newly proven gap-free:** the two closing relations E2′,E3′ (§E) — previously only numeric — and the directed-angle-mod-π equality of Step B (§B). G1's magnitude sign-resolution reduced to the configuration ordering Lemma O (§F); G2 reduced to ray-order incidences (§G). **Still OPEN:** the final scalar identity G3, which (verified numerically) requires E2′,E3′ AND a transcendental closure — the shared trig wall. Honest partial; real progress (E2′,E3′ closed).

## Current best
**A complete, rigorous reduction of the whole problem to a single explicit scalar trig identity
in θ, with the two constraint relations now PROVEN.** Concretely, gap-free this round on top of
round 1's reduction+cevian lemmas:

- **E2′, E3′ (closing relations), now PROVEN** (§E):
  `sinγ·sinC·sin(A+2θ+γ) = 2 sinA·sin(θ+γ)·sin(C−θ−γ)`  (E3′, ties γ to θ),
  `sinβ·sinB·sin(A+2θ+β) = 2 sinA·sin(θ+β)·sin(B−θ−β)`  (E2′, ties β to θ).
- **The SAS chain** expressing `BA′, CA″` (hence `pow(B)=AB·BA′`, `pow(C)=AC·CA″`) as explicit
  functions of `θ,β,γ` and the triangle (Steps A–D, §B–§D), with G1's directed-angle equality
  proven and G2 reduced to ray-order.

**Open gap (G3):** the single scalar identity `AB·BA′ − AC·CA″ = (AB²−AC²)/2`, equivalently
`pow(B)−pow(C)=(AB²−AC²)/2`, after substituting the chain and E2′,E3′. Verified exact numerically;
its transcendental closure is the shared wall with trig-lawofsines. Also residual synthetic
sub-items: Lemma O ordering (betweenness of `A′,A″`; cyclic order on ω) and the one G2 betweenness
step, both true and numerically confirmed, argued in part.

---

## Notation and imported results

Triangle `ABC`; `M,N` midpoints of `AB,AC`; `A=∠BAC, B=∠ABC, C=∠BCA` (so `A+B+C=π`); side
lengths `AB=c, AC=b, BC=a`, with the Law of Sines `a/sinA=b/sinB=c/sinC`. The three angle data:
`θ=∠KBA=∠ACL` (E1), `β=∠LBK=∠LNC` (E2), `γ=∠LCK=∠BMK` (E3). `ω=⊙(AKL)`, centre `O`, radius
`R=OA`; `pow(X)=|XO|²−R²`.

**Imported (certified, round 1) — not re-proved:**
- **Reduction** (`lemmas/reduction-power-to-core.md`): `OM=ON ⟺ pow(B,ω)−pow(C,ω)=(AB²−AC²)/2`
  ("core identity"). Also `pow(B)=AB·BA′`, `pow(C)=AC·CA″` where `A′,A″` are the second
  intersections of lines `AB,AC` with `ω` (power of a point, knowledge_base.md §Geometry
  "power of a point, and its concyclicity converse `PA·PB=PC·PD`"): indeed `A,A′` are the two
  points of `ω∩AB`, so `pow(B)=BA·BA′` as unsigned lengths once `B` is outside `ω`, which holds
  because `A′` lies strictly between `A` and `B` (Lemma O), putting both `ω`-points `A,A′` on the
  same ray from `B`.
- **Cevian lengths L4** (`lemmas/cevian-lengths.md`):
  `BK=(c/2)·sinγ/sin(θ+γ)`, `CL=(b/2)·sinβ/sin(θ+β)`.

The task is the **core identity**. By the reduction and `pow(B)=c·BA′`, `pow(C)=b·CA″`, it is
equivalent to
> **(CORE)**  `c·BA′ − b·CA″ = (c²−b²)/2.`

We build `BA′, CA″` by a Law-of-Sines chain that injects E1–E3.

---

## §A. Step A — E1 pins the angle of △A′BK at B

`A′` lies on line `AB`, strictly between `A` and `B` (Lemma O, §F). Hence ray `BA′` **is** ray
`BA`, so `∠A′BK = ∠ABK = ∠KBA = θ` **by E1 directly** — no concyclicity is used. Symmetrically
(Lemma O gives `A″` strictly between `A` and `C`), `∠A″CL = ∠ACL = θ` by E1.

## §B. Step B — the other angle of △A′BK (Gap G1, directed-angle resolution)

We prove `∠BA′K = ∠ALK =: φ_L`.

**(B1) Directed-angle equality, mod π (unconditional).** Directed angles between lines are taken
mod π (knowledge_base.md §Geometry, "angle chasing / directed angles"; the concyclicity criterion:
four points `P,Q,R,S` are concyclic iff `∠(PR,PS)=∠(QR,QS)` mod π). Points `A,A′,K,L` lie on `ω`,
so taking `P=A′, Q=L, R=A, S=K`:
`∠(A′A, A′K) = ∠(LA, LK)  (mod π).`
Since `A′` lies on line `AB`, line `A′A` is line `AB`; and it is also line `A′B`. Therefore
`∠(A′B, A′K) = ∠(A′A, A′K) = ∠(LA, LK) = φ_L  (mod π).`   (∗)
This is exact and uses only that `A,A′,K,L` are concyclic and `A′∈AB`.

**(B2) Magnitude resolution.** (∗) says the *undirected* angles `∠BA′K` and `φ_L=∠ALK` are either
equal or supplementary. We resolve to equality using two cancelling supplement flips, both read off
Lemma O (§F):
- Since `A′` is strictly between `A` and `B` (Lemma O), rays `A′A` and `A′B` are opposite. Hence
  `∠BA′K = π − ∠AA′K.`   (flip 1)
- Lemma O gives cyclic order `A, A′, K, L, A″` on `ω`; thus on chord `AK`, the point `A′` lies on
  the arc `AK` not containing `L`, i.e. `A′` and `L` are on opposite arcs of `AK`. For a cyclic
  quadrilateral the inscribed angles subtending a chord from opposite arcs are supplementary
  (inscribed-angle theorem, knowledge_base.md §Geometry): `∠AA′K + ∠ALK = π`, so
  `∠AA′K = π − φ_L.`   (flip 2)
Combining: `∠BA′K = π − ∠AA′K = π − (π − φ_L) = φ_L.`  ∎(B)

By the mirror (swap `B↔C, K↔L, β↔γ, A′↔A″`, which preserves E1 and exchanges E2↔E3), the same
argument gives `∠A″CL = ∠A″... ` — precisely `∠CA″L = ∠AKL =: φ_K`.

## §C. Step C — Law of Sines in △A′BK closes BA′

In `△A′BK` the angles are `∠A′BK=θ` (Step A) and `∠BA′K=φ_L` (Step B); hence
`∠A′KB = π−θ−φ_L`. Side `BK` is known (L4). By the Law of Sines
(knowledge_base.md §Geometry, "trig cevians / Law of Sines"):
`BA′ / sin(∠A′KB) = BK / sin(∠BA′K)`, i.e.
> `BA′ = BK · sin(θ+φ_L) / sin φ_L.`
Mirror: `CA″ = CL · sin(θ+φ_K) / sin φ_K.`   ∎(C)

## §D. Step D — the SAS chain determining φ_L, φ_K

`φ_L=∠ALK`, `φ_K=∠AKL` are angles of `△AKL`. We obtain `AK,AL` and `∠KAL` from three triangles.

**(D1) △ABK (SAS: `AB=c`, `∠ABK=θ`, `BK`).** Law of Cosines:
`AK² = c² + BK² − 2c·BK·cosθ`. Law of Sines gives `∠BAK` via
`sin∠BAK / BK = sinθ / AK`, with `∠BAK∈(0,π)` the angle at `A` (acute branch forced because
`∠ABK=θ` and `∠AKB=π−θ−∠BAK` are both positive, so `∠BAK<π−θ`).

**(D2) △ACL (SAS: `AC=b`, `∠ACL=θ`, `CL`).** Identically:
`AL² = b² + CL² − 2b·CL·cosθ`, `sin∠CAL / CL = sinθ / AL`.

**(D3) Angle decomposition at A (Gap G2):** `∠BAC = ∠BAK + ∠KAL + ∠LAC`, so
`∠KAL = A − ∠BAK − ∠CAL`. Proven (modulo one betweenness sub-step) in §G.

**(D4) △AKL (SAS: `AK`, `AL`, `∠KAL`).**
`KL² = AK² + AL² − 2·AK·AL·cos∠KAL`, and by the Law of Sines
`sin φ_L / AK = sin φ_K / AL = sin∠KAL / KL`, giving `φ_L=∠ALK`, `φ_K=∠AKL`.

Substituting (D1)–(D4) into §C expresses `BA′, CA″` as explicit functions of `θ,β,γ,A,b,c`
(`BK,CL` carry the `γ,β` dependence via L4).

## §E. The closing relations E2′, E3′ (PROVEN)

These tie `β,γ` to `θ`. We prove E3′; E2′ is its `B↔C, γ↔β` mirror.

Compute `BK` a **second** way, from `△BKC`. First, ray `CK` makes angle `θ+γ` with ray `CA`:
by E1, `∠ACL=θ`; by E3, `∠LCK=γ`; and by the hypothesis "`L` lies inside angle `ACK`", ray `CL`
is strictly between rays `CA` and `CK`, so `∠ACK = ∠ACL + ∠LCK = θ+γ`. Likewise ray `BK` makes
angle `θ` with `BA` (E1). Now in `△BKC`:
- `∠KBC = ∠ABC − ∠ABK = B − θ` (ray `BK` inside `∠ABC`, since `K∈△BMC⊂△ABC` puts ray `BK`
  strictly between `BA` and `BC`, so `0<θ<B`).
- `∠KCB = ∠ACB − ∠ACK = C − (θ+γ)`, and `θ+γ<C` because ray `CK` lies strictly inside `∠ACB`
  (again `K∈△BMC⊂△ABC` puts ray `CK` between `CA` and `CB`). Hence `∠KCB>0`.
- `∠BKC = π − (B−θ) − (C−θ−γ) = (π−B−C) + 2θ + γ = A + 2θ + γ` (using `A+B+C=π`).

Law of Sines in `△BKC` (knowledge_base.md §Geometry): `BK / sin∠KCB = BC / sin∠BKC`, i.e.
`BK = a · sin(C−θ−γ) / sin(A+2θ+γ)`.
Equate with L4, `BK=(c/2)·sinγ/sin(θ+γ)`, and use `a = c·sinA/sinC` (Law of Sines):
`(c/2)·sinγ/sin(θ+γ) = c·(sinA/sinC)·sin(C−θ−γ)/sin(A+2θ+γ).`
Cancel `c`, cross-multiply by `2·sinC·sin(θ+γ)·sin(A+2θ+γ)` (all nonzero on the admissible
range `0<θ, 0<γ, θ+γ<C<π`):
> **(E3′)**  `sinγ · sinC · sin(A+2θ+γ) = 2·sinA · sin(θ+γ) · sin(C−θ−γ).`
By the mirror (`B↔C, γ↔β`, using ray `BL` at angle `θ+β` to `BA` from "`K` inside `∠LBA`" and
`CL=(b/2)sinβ/sin(θ+β)`):
> **(E2′)**  `sinβ · sinB · sin(A+2θ+β) = 2·sinA · sin(θ+β) · sin(B−θ−β).`
∎(E)   *(Both verified to residual ≤1e-12 on the reconstructed configurations; here derived
purely by the two-secant computation of `BK,CL`.)*

E3′ determines `γ` from `θ` (and the triangle); E2′ determines `β` from `θ`. Together with §D this
makes the whole chain, and thus (CORE), a function of `θ` alone.

## §F. Lemma O (configuration ordering) — used by §A, §B

**Lemma O.** In the configuration: (i) `A′` lies strictly between `A` and `B`, and `A″` strictly
between `A` and `C`; (ii) the cyclic order of `A,A′,K,L,A″` on `ω` is `A, A′, K, L, A″`.

*Status.* Both are TRUE (independent numeric reconstruction over two scalene triangles and
`θ∈{0.12,0.25,0.32}`: `A′` at fraction `AA′/AB∈(0.57,0.67)`, `A″` at `(0.55,0.64)`; cyclic order
`A,A′,K,L,A″` on every sample). Part (i) is equivalent to `B` (resp. `C`) lying outside `ω` with
the near `ω`-point between: a fully synthetic proof reduces to `pow(B)>0` and `0<AA′<AB`. Part
(ii) is the arc-separation used in flip 2. **These are the residual synthetic sub-items of this
approach** (they do not affect the *directed-angle mod-π* equality (∗), which is unconditional; they
only fix the magnitude branch and the outside/inside placement). I did not complete their synthetic
proof this round; they are recorded as an explicit, precisely-scoped sub-gap.

## §G. Gap G2 — angle decomposition at A

`K∈△BMC⊂△ABC` and `L∈△BNC⊂△ABC`, so rays `AK,AL` lie strictly inside `∠BAC`. Thus
`∠BAC=∠BAK+∠KAL+∠LAC` **iff** the ray order from `A` is `AB, AK, AL, AC` (equivalently
`∠BAK<∠BAL`). This order is equivalent to the two "cross" incidences
(P1) `L` and `C` on the same side of line `AK`, and (P2) `K` and `B` on the same side of line `AL`
(each says the middle ray separates the outer vertex; together they force `AK` before `AL`). By the
swap symmetry `σ` (`B↔C,K↔L,M↔N,β↔γ`), (P1)↔(P2), so it suffices to prove (P1).

*Proof of (P1) (up to one betweenness step).* Ray `CL` is strictly between rays `CA,CK` (shown in
§E: `∠ACL=θ<θ+γ=∠ACK`), and `CA,CK` pass through `A,K∈`line `AK`. A ray from `C` strictly inside
the convex angle `∠ACK` meets the opposite open segment `AK` at a unique interior point `Q` (a ray
interior to a triangle's vertex angle meets the opposite side). Line `AK` separates the plane; `C`
is on one side ("C-side") and along ray `CL` a point is on the C-side iff it precedes `Q`. Hence
(P1) `⟺ CL<CQ ⟺ L` precedes `Q` on ray `CL`. Now `C` and `L` both lie strictly on the non-`A`
side of the midline `MN` (`C` is a triangle vertex below `MN`; `L∈△BNC` which lies in the closed
trapezoid `MBCN` on the non-`A` side), while `Q` lies on the `A`-side of `MN` — **this last
placement is the one betweenness sub-step I argue but did not fully close synthetically** (it holds
on all samples: `Q` is the near-`A` portion of `AK`). Granting it, the straight ray `CL` runs
`C → L →` (crosses `MN`) `→ Q`, so `CL<CQ`, giving (P1); (P2) follows by `σ`, and the
decomposition holds. ∎(G, modulo the flagged sub-step)

## §H. Gap G3 — the final scalar identity (OPEN; shared wall)

Assembling §C, §D, §E into (CORE) yields one explicit scalar identity: with `γ=γ(θ)` from E3′ and
`β=β(θ)` from E2′,
> `c·BK·sin(θ+φ_L)/sin φ_L − b·CL·sin(θ+φ_K)/sin φ_K = (c²−b²)/2,`
where `BK,CL` are L4, and `φ_L,φ_K` are the §D outputs.

**This is OPEN.** Numerically it is exact: the assembled chain reproduces
`pow(B)−pow(C)=(c²−b²)/2` to residual ≤1e-6 across two scalene triangles × `θ∈{0.12,0.25,0.32}`
(independent config solver). Crucially, I verified the identity is **FALSE** off the E2′/E3′ locus
(perturbing `γ` alone: LHS `→ −0.288`; perturbing `β` alone: `→ −0.117`; target `−0.200`), so G3
genuinely requires E2′,E3′ (now proven) *and* a transcendental closure. As the outline-reviewer
flagged, this is the **same scalar identity trig-lawofsines must close**; routing through the SAS
sub-triangles did not make it telescope by hand within budget, and CAS ideal-membership is barred
(recorded false negative, double-angle ghost). I did not close it. The value added this round is
that G3 now stands as **one** explicit identity in θ with **both** constraint relations proven,
not four unknowns with numeric-only constraints.

## Cases to cover
Single 1-parameter family (parameter `θ`); no disjoint cases. Admissible range used:
`0<θ`, `0<γ`, `0<β`, `θ+γ<C`, `θ+β<B` (all established in §E from the containments).

## Watch out for (recorded dead ends — do NOT retry)
`φ_L=γ` / `φ_K=β` FALSE; `A′` on `BK/BL/CK/CL` FALSE; `BKLC` concyclic FALSE; `⊙(AKL)` tangent to
`BK`/`CL` FALSE; spiral similarity at `A` (`△ABK~△ACL`) FALSE; plain Gröbner ideal-membership on
the doubled trig system (double-angle ghost) — barred.

## Promotable lemmas
- **E2′, E3′ (closing relations), PROVEN (§E).** With `θ=∠KBA=∠ACL, β=∠LBK, γ=∠LCK` and triangle
  angles `A,B,C`:
  `sinγ·sinC·sin(A+2θ+γ)=2 sinA·sin(θ+γ)·sin(C−θ−γ)` and its `B↔C,γ↔β` mirror. Proved by
  computing `BK` (resp. `CL`) both via `△BMK` (L4) and via `△BKC` (second ray `CK` at angle `θ+γ`
  to `CA`) and equating. Gap-free given L4; reviewer may certify to `lemmas/`. Reusable by
  trig-lawofsines and complex-swap-symmetry (same relations, currently numeric there).
- **Directed-angle mod-π equality (§B1), PROVEN.** For `A,A′,K,L` concyclic with `A′` on line `AB`:
  `∠(A′B,A′K)=∠(LA,LK)` mod π (concyclicity criterion). Unconditional; the magnitude resolution
  needs Lemma O. Reusable.
- **(L1, L2a, L4 already certified round 1.)**
