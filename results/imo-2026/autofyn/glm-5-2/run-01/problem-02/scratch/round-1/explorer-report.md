## imo-2026-02 (IMO 2026 P2, geometry — OM=ON)

### Candidate technique(s)
- **Antipode / Thales reduction (the load-bearing reformulation).** Let `A'` be the antipode of `A` on the circumcircle of `AKL`, i.e. `A' = 2O − A`. Then `OM = A'B/2` and `ON = A'C/2` (exact identities, derived below), so
  `OM = ON  ⟺  A'B = A'C  ⟺  A' lies on the perpendicular bisector of BC.`
  By Thales, `A'K ⊥ AK` and `A'L ⊥ AL`, so equivalently `A'` is the intersection of the line through `K` perpendicular to `AK` and the line through `L` perpendicular to `AL`. **Target to prove: this point `A'` is equidistant from `B` and `C`.** This is a clean, rigorous reformulation (not a conjecture) and is where the outliner should start.
- Then attack `A'B = A'C` via the three angle equalities + midpoint structure. Candidates: spiral similarity, isogonal-style angle chase, or a synthetic reflection (cf. aimo-0021's reflection trick). Analytic (place `A` at origin, `B,C` arbitrary, solve for `A'` from the two perpendiculars) is also fully tractable as a fallback.

### Cheap-kill candidates
- **Homothety observation (already gives the reduction).** The homothety `h` centered at `A` ratio `1/2` sends `B→M`, `C→N`, and sends the perpendicular bisector of `BC` to the perpendicular bisector of `MN`. Hence `OM=ON ⟺ O∈perp-bis(MN) ⟺ h^{-1}(O)=2O−A∈perp-bis(BC)`. With `O` circumcenter of `AKL`, `2O−A` is precisely the antipode `A'` of `A` on `(AKL)`. This is exact and free.
- **Angle-chain decoding.** Writing `α=∠KBA=∠ACL`, `γ=∠BMK=∠LCK`, `β=∠LBK=∠LNC`: the conditions `∠ACL=α` and `∠LCK=γ` with `L∈∠ACK` force `∠ACK = α+γ` (consistency constraint on `K`), reducing `K` to a 1-parameter family; `β` is then fixed by the self-consistency `∠LBK = ∠LNC`. So the configuration is genuinely 1-parameter and the theorem must hold identically over it — useful as a sanity structure and for an analytic proof (one free parameter `α`).

### Knowledge-base entries to use
- **Geometry (synthetic & analytic)** block (knowledge_base.md L127–145): angle chasing, power of a point / concyclicity converse, spiral similarity, Miquel point, trig cevians (Ceva/Menelaus); coordinates/complex/barycentric with axes rotated to a key line. The "place coordinates to exploit symmetry" + complex numbers entries are the analytic fallback.
- No dedicated "antipode/Thales" or "perpendicular-bisector of MN" entry exists; the antipode reduction is problem-specific (derived here, verified numerically).

### Analogous past problems (cruxes)
The crux corpus has **no geometry cruxes** (per crux_moves_documentation.md L73–75: "geometry — Not in the corpus yet"). From `past_problems_database.json` (295 geometry problems with full solutions), the genuinely analogous ones:
- **aimo-0021 (IMO-SL 2013, Iran).** `M,N` midpoints of `AB,AC`; `OM⊥AB, ON⊥AC`; the crux move is **reflection about the perpendicular bisector of `AT`** (a symmetry axis that swaps the `AB`-direction with the `AC`-direction), mapping `OM↔ON` and the circle `γ↔γ`, hence `M↔X`, `N↔Y`. Directly analogous in spirit: an equality `OM=ON`-type proved by a reflection that swaps the two midpoint/side directions. *Adapt as a hint, not a citation — our triangle is not necessarily isosceles and there is no given angle bisector, so the symmetry axis must come from the `A'`/antipode structure instead.*
- **aimo-0603 (IMO-SL 2014).** Midpoint `M` of `EF`, perpendicular bisector of `EF`, cyclic condition; crux = **symmetry about the perpendicular bisector of `ST`** (`K` and `L` symmetric ⟺ `KL ∥ ST`). Reinforces that perpendicular-bisector + midpoint configs reduce to a reflection-symmetry statement.
- **aimo-0644 / aimo-0525 (USA_TSTST 2011/2017).** Both feature `M,N` midpoints of `AB,AC` with circumcenter `O` of `ABC` and orthocenter `H`; the workhorse is the nine-point-circle / Euler-line reflection `O ↔ H` under `h_{A,1/2}`. Useful background for midpoint-of-`AB`,`AC` + circumcenter identities; less directly load-bearing here since we have circumcenter of `AKL`, not `ABC`.

### Prior progress
- None. `results/imo-2026-02.md` does not yet exist (round 1).

### Dead ends (do not retry)
- None yet (first exploration). One caution: an earlier buggy sign convention for the rays `B→K` (rotating `BA` the wrong way) and `C→L` produced extraneous non-interior configurations that falsely gave `OM≠ON`; the outliner/builder must respect the interior placement (`K∈BMC`, `L∈BNC`, `K∈∠LBA`, `L∈∠ACK`) — the theorem only holds for the valid branch.

### Small-case / intuition notes (CONJECTURE, evidence only — not a proof)
- Numerically constructed the full 1-parameter family for triangle `A=(0,0), B=(4,0), C=(1.5,3)` over `α = ∠KBA ∈ [1°,49°]`. For every valid `(K,L)` satisfying all three angle equalities and the interior conditions:
  - `OM = ON` holds to machine precision (errors `~1e-13`), and
  - the antipode `A' = 2O−A` satisfies `A'B = A'C` to machine precision (e.g. both `≈2.0005` at `α=14°`).
- `A'K ⊥ AK` and `A'L ⊥ AL` verified numerically (dot products `~1e-15`).
- `A'` is **not** a spiral center sending `K→L, B→C` with one ratio: `A'K/A'L ≈ 0.63–0.67` (varies with `α`) while `A'B/A'C = 1`. So the simple "spiral similarity at `A'`" reading is false; the isosceles-at-`A'` conclusion needs the angle-chain + perpendicular structure, not a single spiral.
- `∠BA'C` (apex angle of the isosceles triangle `A'BC`) varies with `α` (146.9°, 166.9°, 173.1° at `α=10,20,30`), so `A'` is not fixed — the proof must use the full configuration, not a fixed point.
- **Recommendation to outliner:** build the outline around the antipode reduction `OM=ON ⟺ A'B=A'C` (with `A'K⊥AK, A'L⊥AL`), then prove `A'B=A'C` from `∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK` and `M,N` midpoints. The angle conditions couple the directions `BK` (↔`BA`, since `∠KBA=α`) and `CL` (↔`CA`), the perpendiculars `KA'⊥KA`, `LA'⊥LA`, and the midpoint rays `MB∥AB`, `NC∥AC` — likely via an angle chase showing `∠A'BC = ∠BCA'` (isosceles at `A'`). If synthetic resists, an analytic coordinate proof with `A` at origin is a viable direct route since the identities are polynomial.
