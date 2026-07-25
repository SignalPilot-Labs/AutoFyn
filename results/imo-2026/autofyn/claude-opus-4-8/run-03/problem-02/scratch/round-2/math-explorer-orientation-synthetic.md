## imo-2026-02

### Assigned lens
Synthetic / directed-angle-mod-π route to the SAME shared orientation gap (interiority ⟹
correctly-oriented equalities), kept independent of the coordinate-identity framing.

### Distinct openings

**Opening 1 — Betweenness-order argument (the strongest candidate; numerically confirmed, buildable without any numeric "sign check").**
The key realization: the containment hypotheses "K inside ∠LBA" and "L inside ∠ACK" are not
just qualifying remarks — they are literally **angular betweenness statements at a single
vertex**, and they alone (not the interior-of-△BMC / △BNC conditions) pin the rotational
sense needed for the mod-π (or full mod-2π) directed-angle equalities:
- At B: since (by (2)) ray BK is ray BA rotated by θ *into the triangle* (a definite,
  single-point-interiority fact — see Opening 2), "K inside ∠LBA" means ray BK lies
  angularly **between** ray BA and ray BL. Hence the rotation BA→BL has the *same sense*
  (same sign) as BA→BK, and is **larger in magnitude**: rot(BA→BL) = θ + rot(BK→BL) with
  rot(BK→BL) same sign as rot(BA→BK). This pins the sign of ∠(BK,BL) directly from
  betweenness, with no case split and no numeric check.
- At C: symmetrically, "L inside ∠ACK" gives ray CL between ray CA and ray CK, so
  rot(CA→CK) = θ + rot(CL→CK), same-sign, pinning ∠(CL,CK)'s sign directly.
- These two sign pins are exactly what Steps 3–4 of `synthetic-sigma-spiral.md` need for
  the "matching sign" bullets in the ∠(CL,CK)=∠(MB,MK) and ∠(CA,CL)=∠(KB,BA) chase (their
  current proof invokes "[Verified numerically]" at precisely this spot) — and they are what
  `coordinate-identity.md`'s EA=Im[...] / EB=Im[...] sign choice needs.

I **numerically tested this exact mechanism** (script below) on triangle
B=(-3,0), C=(5,0), A=(0.7,4) at θ=20° and θ=30° (both in the admissible range: unique
u,v roots, K,L verified interior to △BMC,△BNC, OM=ON confirmed to 1e-15). In both cases:
`s_BK` (signed rotation BA→BK) and `s_BL` are **same sign**, with `|s_BK|=θ < |s_BL|`
— i.e. K is angularly between A and L as seen from B, confirming "K inside ∠LBA" ⟺ this
order. Symmetrically `s_CK`,`s_CL` same sign with `|s_CL|=θ < |s_CK|`, confirming
"L inside ∠ACK" ⟺ this order. At θ=60° (outside the admissible range for this triangle:
no branch has both K,L interior), the algebraically-forced-T=0 branch has u,v so large that
K,L fall **outside** the plane region near the triangle, and (separately) it is exactly the
branch where the "same-sign, |rot to K/L| < |rot to L/K|" order holds too — i.e. the
order-condition and the T=0-forcing branch coincide even off the truly admissible range,
which is consistent with (but does not by itself prove) the claim that order alone (not
full △BMC/△BNC interiority) is what selects the correct sign.

This is a genuinely different mechanism from Opening 2/3 below: it treats the compound
hypothesis "K inside ∠LBA" / "L inside ∠ACK" as the PRIMARY selector (a single betweenness
inequality at one vertex, elementary and rigorous — no continuity or limiting argument
needed), rather than routing orientation through global CCW-labeling + a connectedness/
continuity closure over the whole family.

**Opening 2 — Single-vertex CCW/interior-angle argument for condition (2)'s sign (cheap, already essentially settled).**
K∈int(△BMC) alone (without reference to L) forces the *sense* of the rotation BA→BK: since
△BMC has the same orientation as △ABC (M on segment AB, so cross((M−B),(C−B)) has the same
sign as cross((A−B),(C−B))), and K∈int(△BMC)⟹K∈int(∠ABC) on the C-side of AB, the rotation
BA→BK is forced to be the SAME rotational sense as BA→BC (the fixed interior-angle sense of
the CCW-oriented △ABC). This is a one-line cross-product argument (no numerics, no
continuity) and cleanly settles the sign of θ in the parametrisation "K = B + u·rot(BA,
∓θ)" used by both coordinate-identity and synthetic-sigma-spiral. It does NOT by itself
settle the harder conditions (3),(4) sign — that needs Opening 1 (or 3).

**Opening 3 — Connectedness + single symmetric-case fallback (insurance if Opening 1's chase gets stuck on a specific inscribed-angle step).**
Show the admissible parameter set (θ or the pair (u,v)) is a connected interval — the
defining conditions are open (strict interiority + strict betweenness), and the
configuration space is parametrised continuously by one real parameter, so if it is
nonempty and the "wrong branch" is excluded by a strict inequality that cannot vanish on
the admissible set (no boundary crossing without a forbidden degeneracy — e.g. B,K,L
collinear or N,L,C collinear), then the sign is LOCALLY constant, hence constant on the
whole connected admissible set. Then verify the sign ONCE at an exactly-computable
symmetric configuration (e.g. isosceles AB=AC, which by the σ-symmetry (B↔C,M↔N,K↔L)
forces a symmetric admissible point with u=v, θ determined by a single trig equation
solvable in closed form) — this is an EXACT special-case check, not an "approximation",
so it is legitimate as a proof step, unlike blanket numeric verification across the family.
This is weaker/more machinery-heavy than Opening 1 but is a safety net if the direct
betweenness chase in Opening 1 runs into an inscribed-angle subtlety for a specific pair of
rays.

### Candidate technique(s)
- Directed angles mod π for the concyclicity chases in `synthetic-sigma-spiral.md` Steps
  3–4 (KB "Synthetic toolkit": inscribed-angle converse, angle addition).
- The sign itself needs a genuinely *oriented* (mod 2π, not mod π) fact — angular
  betweenness ("ray X lies between ray Y and ray Z") — since mod-π addition alone does not
  resolve the ±φ ambiguity (φ vs −φ are distinct mod π unless 2φ≡0). This is exactly the
  gap: it needs an oriented-plane argument, not just the inscribed-angle machinery.
- Cross-product/orientation-of-triangle argument (elementary, no KB entry needed by name
  beyond "signed area / orientation") for Opening 2.
- Connectedness-of-admissible-region + degenerate-configuration exclusion (topological
  argument) for Opening 3, using the problem's own strict-interiority hypotheses as the
  excluded-degeneracy set.

### Cheap-kill candidates
- None that kill the problem; but a cheap **sanity check** worth doing before committing to
  Opening 1: verify (once, symbolically/by hand, not numerically) that "K inside ∠LBA"
  really is equivalent to the betweenness order I used (same-sign + magnitude order) and not
  to some other configuration (e.g. reflex-angle ambiguity if ∠LBA could exceed π) — this is
  a one-line check (∠LBA<π always since it's an angle of a triangle-like configuration with
  A,B fixed and L,K on the same side) but should be stated explicitly, not assumed.

### Knowledge-base entries to use
- "Synthetic toolkit" (KB): inscribed-angle theorem/converse (directed-angle form),
  power of a point, spiral similarity — for the concyclicity chase itself (orthogonal to
  the sign gap, already used correctly by synthetic-sigma-spiral).
- No KB entry directly addresses "orientation from betweenness hypotheses" — this piece is
  elementary planar-orientation reasoning (signed area / cross product), standard but not
  named as a KB entry; should be stated and proved inline (2–3 lines, as in Opening 2).

### Analogous past problems (cruxes)
None. `crux_moves_documentation.md` states geometry crux moves are **not yet in the
corpus** ("geometry — Not in the corpus yet; the problems DB includes geometry problems
with solutions, but no geometry cruxes have been extracted"). No forced match attempted.

### Prior progress
See `current.md` / round-1 reports: reduction lemma and spiral-similarity lemma certified;
coordinate-identity's algebraic engine (the exact polynomial identity a_K a_L T = a_L QK
FK + QL FL) is fully verified and is EXACTLY the same structural fact this orientation
lens needs to feed — closing the sign gap here closes coordinate-identity's gap too, and
simultaneously upgrades synthetic-sigma-spiral's Steps 3–4 from "numerically verified sign"
to rigorous. Not yet closed in any approach.

### Dead ends (do not retry)
- Justifying the sign purely by "numerical model confirms the directed equality" (both
  coordinate-identity and synthetic-sigma-spiral's current write-ups do this) — reviewer
  showed this is load-bearing and non-automatic (θ=0.8 counterexample: unsigned equations
  hold, directed EB≠0, OM≠ON, because interiority fails there). Do not re-submit a numerics-
  only sign justification; it will be rejected again.
- midpoint-doubling-phantom's Lemma B (OK′=OL′) — flagged unverified in round 1, not
  re-tested this round (out of scope for this lens); still open per current.md.

### Small-case / intuition notes (all labeled CONJECTURE / numeric evidence, confirmed this round)
- On triangle B=(−3,0), C=(5,0), A=(0.7,4): at θ=20° and θ=30° (single-root, genuinely
  admissible cases: K,L verified strictly interior to △BMC,△BNC via a sign-consistent
  point-in-triangle test, OM=ON to 1e−15), the signed rotations satisfy exactly the
  betweenness pattern of Opening 1: sign(rot(BA→BK)) = sign(rot(BA→BL)) with
  |rot(BA→BK)|=θ < |rot(BA→BL)|; sign(rot(CA→CK)) = sign(rot(CA→CL)) with
  |rot(CA→CL)|=θ < |rot(CA→CK)|. This is exactly "K between A,L as seen from B" and
  "L between A,K as seen from C" — i.e. the two containment hypotheses given in the problem,
  read literally as rotational betweenness, are the sign-selectors. This is evidence FOR
  Opening 1 being the right (and rigorously closeable) mechanism, not proof — the chase from
  "these order inequalities" to the exact ∠(CL,CK)=∠(MB,MK) mod-π equality (Step 3 of
  synthetic-sigma-spiral) still needs to be written out.
- At θ=60° for the same triangle (outside the admissible window — no branch has both K,L
  interior), the algebraically-T=0-forcing branch is also the one satisfying the same
  order/sign pattern, even though the points themselves lie outside the geometric region —
  i.e. the order condition, not literal △BMC/△BNC-interiority, appears to be the operative
  selector algebraically. This narrows the target: the outliner/builder should try to prove
  the sign pin from the TWO betweenness containments alone (Opening 1), and treat
  △BMC/△BNC-interiority as auxiliary (needed elsewhere, e.g. to fix θ∈(0,∠ABC) range, but
  not the load-bearing piece for the (3)/(4) signs).
- Reproducibility: `/tmp/explore2.py` in this session (not committed; ad hoc probe) built
  the family via the SAME parametrisation as coordinate-identity (K=B+u·rot(A−B,−θ),
  L=C+v·rot(A−C,+θ)), solved the two UNSIGNED magnitude conditions (∠LBK=∠LNC, ∠LCK=∠BMK)
  independently in v and u respectively (confirming the decoupling claim independently,
  from scratch, via a different unsigned-angle formulation, not reusing the FK/FL
  polynomials from round 1), and cross-checked interiority + OM=ON + the betweenness sign
  pattern.

### Verdict on independence from coordinate framing
Genuinely independent as an insurance approach: this lens uses plane orientation (signed
area / rotation sense) and angular betweenness directly on rays, never coordinates or
determinants. It shares only the TARGET fact (the sign pin) with coordinate-identity, not
the method. If Opening 1's betweenness chase is written out fully, it independently
certifies the sign lemma that BOTH coordinate-identity (to promote its `partial` engine to
`solved`) and synthetic-sigma-spiral (to certify Γ_C, Γ_B rigorously) need — a single proved
lemma ("Sign Lemma": the containment hypotheses force rot(BK,BL) and rot(CL,CK) to have the
sign matching ∠(MB,MK), ∠(KB,BA) resp.) would unblock two of the three live approaches at
once. Recommend the outliner state this as a standalone importable lemma target for round 2,
built via Opening 1's order argument (not numerics), with Opening 3 kept as a fallback if a
specific inscribed-angle step in the chase resists direct order-based justification.
