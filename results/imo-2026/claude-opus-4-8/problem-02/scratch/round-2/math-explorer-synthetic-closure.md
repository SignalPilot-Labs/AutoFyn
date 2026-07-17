## imo-2026-02 — SYNTHETIC CLOSURE lens (power-of-point-BC core identity)

### Headline finding (new this round, numerically verified to be a COMPLETE closed chain)

The Law-of-Sines closure the dispatch asked me to scout **exists and demonstrably
closes the core identity end-to-end**, verified across the whole 1-parameter family
on a from-scratch numeric configuration (6 family members, scalene triangle A=(0.3,1.4),
B=(0,0), C=(1,0)). It is the most promising opening found. Concretely:

**Step A — E1 injects directly into `A'`.** Since `A'` (second meet of line `AB` with
`ω=⊙AKL`) lies on line `AB`, the ray `BA'` **is** ray `BA` (or its opposite). Hence
`∠A'BK = ∠ABK = ∠KBA = θ` **exactly**, by E1 itself — no concyclicity needed. Verified
to machine precision (`∠A'BK − θ = 0` on all 6 samples). This is a genuinely new,
cheap, and load-bearing fact not recorded in the round-1 files.

**Step B — inscribed angle gives the OTHER angle of `△A'BK` for free.** By the
inscribed-angle theorem on chord `AK` of `ω`, `∠BA'K = ∠AA'K = ∠ALK` (same arc,
confirmed numerically: e.g. `∠BA'K=75.4689°=∠ALK` to 4 decimal places on every
sample — this is the "automatic from concyclicity" fact already in the approach
file, but here it is *exactly the missing angle* needed to close the triangle, not
a dead end).

**Step C — Law of Sines in `△A'BK` closes `BA'`.** Since `△A'BK` now has one full
side (`BK`, known from the certified lemma L4) and both non-included angles
(`θ` at `B`, `φ_L := ∠ALK` at `A'`), `BA' = BK·sin(θ+φ_L)/sin(φ_L)`. Mirror:
`CA'' = CL·sin(θ+φ_K)/sin(φ_K)`, `φ_K := ∠AKL`.

**Step D — `φ_K, φ_L` pin down via a clean SAS chain that also injects E1-E3, with
NO further unknowns:**
- `△ABK`: side `AB`, angle `∠ABK=θ` (E1), side `BK` (L4) — full SAS, gives
  `∠BAK`, `AK` via Law of Cosines/Sines.
- `△ACL`: side `AC`, angle `∠ACL=θ` (E1), side `CL` (L4) — full SAS, gives
  `∠CAL`, `AL`.
- **Angle decomposition at `A`:** `∠BAC = ∠BAK + ∠KAL + ∠LAC` — verified EXACTLY
  (`38.65981° = 38.65981°` to 5 decimals on all 6 samples). This says rays `AK,
  AL` lie inside `∠BAC` in the order `B,K,L,C` — plausible consequence of "K
  inside ∠LBA & inside △BMC" and "L inside ∠ACK & inside △BNC," but **not yet
  synthetically derived from those hypotheses** — currently only numerically
  confirmed.
- `△AKL`: now SAS with `AK, AL` (from above) and included angle `∠KAL` (from
  decomposition) — gives `φ_K=∠AKL`, `φ_L=∠ALK` via Law of Cosines/Sines.

**End-to-end numeric confirmation.** Substituting the whole chain (using only
`θ`, the fixed triangle angles, and the lemma L4 formulas — no direct access to
`K,L` coordinates), the formula `BA'=BK·sin(θ+φ_L)/sin(φ_L)` reproduces the
coordinate-computed `BA'` to 6 decimal places on all 6 samples, and
`pow(B)-pow(C) = AB·BA' - AC·CA''` reproduces `(AB²-AC²)/2 = -0.200000` **exactly**
on every sample. This is strong evidence the chain is the *right* decomposition,
not just a plausible-looking one — full python transcript available on request
(`/tmp/probe2.py`, `/tmp/solve_imo2.py` in this container).

### What remains to make this a proof (concrete, scoped gaps for the builder)

1. **Directed-angle rigor for Step B.** Must show `∠BA'K=∠ALK` (not the
   supplement) is forced by the given orientation/containment hypotheses — a
   genuine directed-angle argument (mod π, then resolve the sign using "K inside
   ∠LBA," "L inside ∠ACK"), not an observation. Same for the mirror `∠CA''L=∠AKL`.
2. **Prove the angle decomposition at A** (`∠BAC=∠BAK+∠KAL+∠LAC`) synthetically
   from the containment hypotheses. This is the one purely "configuration" fact
   in the chain with no metric content — likely the most tractable gap (it's an
   ordering/betweenness statement, provable from "K inside triangle BMC and
   inside angle LBA" forcing ray AK between AB and AC, etc.)
3. **Close the final trig identity.** Once Steps A–D give `BA', CA''` as explicit
   functions of `θ` and the fixed angles `A,B,C` (with `β,γ` themselves functions
   of `θ` via the E2′/E3′ closing relations already certified numerically in
   `trig-lawofsines`), `pow(B)-pow(C)=(AB²-AC²)/2` becomes one explicit
   trig identity in `θ`. This is content-equivalent to the trig approach's
   identity `(T)`, but derived through clean SAS triangles rather than coordinate
   elimination — it may telescope more transparently (each step is a
   Law-of-Sines/-Cosines closure of a genuine sub-triangle, so cross terms may
   cancel via product-to-sum identities before any CAS is needed). Worth trying
   by hand / with sympy trig.simplify before falling back to Gröbner.

### Distinct openings surfaced

- **(Primary, new) SAS-chain Law-of-Sines closure** (Steps A–D above): the
  concrete mechanism requested by the dispatch. Strongest candidate; numerically
  airtight; three well-scoped remaining gaps (2 synthetic, 1 trig-identity).
- **Miquel-point / spiral-similarity auxiliary point**: scouted but no fixed
  auxiliary circle or spiral center was found (see dead ends below) — do not
  pursue further without a new idea; the SAS-chain route above supersedes it
  because it already gets the needed angles without an auxiliary point.
- **Direct trig-identity fallback**: if the two remaining synthetic gaps (2
  above) resist a clean directed-angle proof, the whole Step A–D chain can be
  *asserted with the numeric branch-selection argument already used in
  trig-lawofsines* (same physical-branch argument, since `φ_K,φ_L` are pinned by
  the same 0<θ<... domain) and the final identity attacked purely as a trig
  identity in `θ` — giving a second, independent route to the SAME final
  scalar identity as trig-lawofsines. This means power-of-point-BC and
  trig-lawofsines can genuinely CONVERGE on one shared final trig identity
  proof, which — once done once — certifies both approaches simultaneously (not
  duplicated work, since the identity is provably the same object via Step C).

### Candidate technique(s)
Law of Sines / Law of Cosines (SAS triangle closure), inscribed-angle theorem
(directed angles mod π), power of a point — all named in knowledge_base.md
§"Geometry (synthetic & analytic)": *Synthetic toolkit: angle chasing, power of
a point (and concyclicity converse), ... trig cevians (Ceva/Menelaus)*.

### Cheap-kill candidates (all already ruled out, extending round-1's list — do not retry)
- Spiral similarity centered at `K` sending `M→C, B→L`: FALSE (checked `KM/KC ≠
  KB/KL` and `∠MKC ≠ ∠BKL` numerically on all 6 samples — ratios off by up to
  10×, angles off by up to 40°).
- Spiral similarity / direct similarity centered at `A` sending `B→C, K→L`
  (i.e. `△ABK ~ △ACL`): FALSE — `∠BAK ≠ ∠CAL` numerically (e.g. 6.3° vs 10.5°),
  so E1 alone does NOT make `A` a spiral center.
- Concyclicity of any quadruple among `{B,K,M,N}`, `{C,L,M,N}`, `{M,K,L,C}`,
  `{N,L,K,B}`, `{B,K,L,N}`, `{C,L,K,M}`: none found concyclic (determinant test,
  2 independent samples, no near-zero hits) — extends round 1's "BKLC not
  concyclic" to the midpoint-inclusive quadruples.
- `φ_L = γ` / `φ_K = β` (the "too easy" hope that would make the core identity
  split termwise in `AB², AC²`): FALSE — checked numerically, `∠ALK ≠ ∠LCK` and
  `∠AKL ≠ ∠LBK` (differ by tens of degrees, not even close to a fixed offset).
  Do not assume this shortcut.

### Knowledge-base entries to use
- "Synthetic toolkit" (knowledge_base.md, Geometry section): power of a point,
  angle chasing, trig cevians, Law of Sines/Cosines — directly used above.
- Inscribed-angle / concyclicity converse (`PA·PB=PC·PD`) — used in Step B.

### Analogous past problems (cruxes)
None. The crux corpus (`crux_moves_documentation.md`) has only three domains —
`number_theory`, `combinatorics`, `algebra` — **no geometry subtopic exists**, so
there is no genuinely analogous crux to retrieve for this synthetic angle-chase
problem. (Confirms round-1's note "geometry not in crux corpus.")

### Prior progress
See `results/imo-2026-02/current.md` and `lemmas/*.md`: the shared certified
reduction `OM=ON ⟺ pow(B,ω)-pow(C,ω)=(AB²-AC²)/2` (L2a+L1+L2, `reduction-power-
to-core.md`) and the cevian lengths `BK=(AB/2)sinγ/sin(θ+γ)`, `CL=(AC/2)sinβ/
sin(θ+β)` (L4, `cevian-lengths.md`) are gap-free and reused directly as the
Step-D SAS inputs above — no need to re-derive them.

### Dead ends (do not retry)
All four items under "Cheap-kill candidates" above, plus (from round 1, re-
confirmed): `A'` not on `BK/BL/CK/CL`; `BKLC` not concyclic; `ω` not tangent to
`BK`/`CL`; `AK/BK ≠ AL/CL`.

### Small-case / intuition notes (all conjecture / numeric, not proof)
- The SAS-chain (Steps A–D) reproduces `pow(B)-pow(C) = -0.200000 = (AB²-AC²)/2`
  to 6 decimal places on all 6 independently-solved family members of one
  scalene triangle — strong evidence the decomposition is exactly right, but
  this is numeric evidence, not yet a symbolic proof of the final trig identity
  or of the two ordering/directed-angle facts (Steps B, D-decomposition) it
  relies on.
- The angle decomposition `∠BAC=∠BAK+∠KAL+∠LAC` held to 5 decimals across the
  whole family — conjectured to be a clean consequence of the containment
  hypotheses (not yet proved).
