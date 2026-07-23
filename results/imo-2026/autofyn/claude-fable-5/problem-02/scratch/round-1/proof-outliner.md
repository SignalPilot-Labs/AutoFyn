## imo-2026-02

Round-1 field: four new rival approaches, all targeting the full claim OM = ON.
All four share only the FREE unconditional reduction (median formula:
OM = ON ⟺ OB² − OC² = (c²−b²)/2, equivalently pow(B,ω) − pow(C,ω) = (c²−b²)/2,
ω = ⊙(AKL), b = CA, c = AB) — beyond that their load-bearing gaps are disjoint.

New verified facts produced while outlining (probes in
`/tmp/round-1/scratch/outliner_probe.py`, machine precision on the solved family):
- The trig constraint system E1–E6 (below) holds exactly; it decouples into a
  K-side 2×2 system in (α_K, χ) and an L-side 2×2 system in (α_L, ψ).
- Tangent-chord parametrization at A: AP = 2R sin δ, AQ = 2R sin(δ+∠A),
  AK = 2R sin(δ+α_K), AL = 2R sin(δ+∠A−α_L) with one consistent orientation.
- Goal in secant form verified: c·AP − b·AQ = (c²−b²)/2 exactly along the family.
- Reflection dictionary exact: K* = 2M−K, L* = 2N−L give ∠K*AB = ∠L*AC = φ
  (isogonal rays through A), AK* = BK, AL* = CL, ∠AMK* = ∠LCK, ∠ANL* = ∠LBK.
- Refuted while probing (do NOT use): B,K,N collinear; C,L,M collinear; P ∈ ⊙(BMK);
  Q ∈ ⊙(CNL); tangencies of BK/BL/CK/CL to ⊙(CNL)/⊙(BMK); tangency of AB to
  ⊙(BKL); KL ∥ BC; {A,K,L,K*}, {A,K,L,L*}, {K,L,K*,L*}, {B,C,K*,L*} concyclic;
  AK·CL = AL·BK; ⊙(AK*L*) having the OM = ON property; ⊙(BMK) ∩ ⊙(CNL) on ω
  (they don't even intersect); radical axis of ⊙(BMK), ⊙(CNL) fixed in φ.
  (Note pow(A,⊙BMK) = c²/2 and pow(A,⊙CNL) = b²/2 hold but are trivial — B, M
  both lie on line AB.)

Crux corpus: no geometry cruxes exist (per crux_moves_documentation.md); none used.

---

secant-trig-identity: new
Target: OM = ON (full claim).
Technique: power of a point + tangent–chord + law of sines; reduce to one trig
identity and prove it by elimination.
Skeleton:
  1. OM = ON ⟺ OB² − OC² = (c²−b²)/2 — median/parallelogram formula (unconditional).
  2. ⟺ c·AP − b·AQ = (c²−b²)/2, P, Q second meets of AB, AC with ω — power of B, C
     along the secants through A ∈ ω.
  3. AP = 2R sin δ, AQ = 2R sin(δ+∠A), AK = 2R sin(δ+α_K), AL = 2R sin(δ+∠A−α_L)
     — tangent–chord angle δ at A + extended law of sines in ω (verified).
  4. Hypotheses ⟺ trig system: E1: AK = c sinφ/sin(φ+α_K); E2: AL = b sinφ/sin(φ+α_L);
     E3: 2 sinα_K sin(φ+χ) = sinχ sin(φ+α_K) (BK two ways, MB = c/2 — the midpoint IS the 2);
     E4: 2 sinα_L sin(φ+ψ) = sinψ sin(φ+α_L); E5: AK = b sin(φ+χ)/sin(φ+χ+∠A−α_K)
     (∠ACK = φ+χ); E6: AL = c sin(φ+ψ)/sin(φ+ψ+∠A−α_L) (∠ABL = φ+ψ). All verified 1e-15.
  5. Eliminate (R, δ) linearly, reduce goal to one identity modulo the decoupled
     K-side (E1,E5,E3) and L-side (E2,E6,E4) systems.
Key lemmas (claim + mechanism):
  - E3 — because BK computed in △ABK and in △MBK must agree and MB = c/2: the
    midpoint hypothesis enters as exactly the factor 2.
  - ∠ACK = φ+χ, ∠ABL = φ+ψ — because L inside ∠ACK and K inside ∠LBA split the
    angles additively.
  - Goal identity ⟺ 2R(c sinδ − b sin(δ+∠A)) = (c²−b²)/2 — substitution of step 3
    into step 2.
Open gaps: the final trig identity (step 5) — the single load-bearing gap; plus
orientation bookkeeping in steps 2–3 (directed lengths/angles).
Cases to cover: none (single identity).
Watch out for: refuted similarity △LBK ~ △LNC (only angles equal, not ratios);
mirrored sign branches.

midpoint-reflection-isogonal: new
Target: OM = ON (full claim).
Technique: synthetic — reflect K in M and L in N; parallelogram dictionary sends
the problem to two points on isogonal rays through A; goal becomes a power
identity at the reflected points.
Skeleton:
  1. K* = 2M−K, L* = 2N−L; AKBK*, ALCL* parallelograms — so AK* = BK, AL* = CL,
     ∠K*AB = ∠L*AC = φ (isogonal rays), ∠AMK* = ∠LCK, ∠ANL* = ∠LBK (all exact).
  2. OM = ON ⟺ pow(K*,ω) − KK*²/2 = pow(L*,ω) − LL*²/2 — median formula at M, N
     (M midpoint of KK*, K ∈ ω).
  3. KK*² = 2AK² + 2BK² − c² — parallelogram law; pow(K*,ω) = BK² − BK·AP₁ with
     P₁ the second meet of ray AK* with ω — secant from K* through A.
  4. Goal ⟺ BK·AP₁ + AK² − CL·AP₂ − AL² = (c²−b²)/2 (verified numerically).
  5. Use isogonality of the rays + transferred angle conditions to prove step 4.
Key lemmas (claim + mechanism):
  - The dictionary of step 1 — because M, N are midpoints, so the reflections are
    parallelogram diagonals; hypotheses map to angle conditions at M, N against
    the SIDES (M ∈ AB, N ∈ AC make ∠BMK, ∠LNC angles against the side lines).
  - Step 2 — because OK = R kills the R-dependence in the median formula.
Open gaps: step 5 is load-bearing and the synthetic object (a tangent circle at
M/N, or a spiral map at A pairing the isogonal chords) is not yet identified;
naive candidates are all refuted (see list above). If it collapses to the trig
grind it duplicates secant-trig-identity and should be pruned.
Cases to cover: none beyond orientation.
Watch out for: refuted concyclicities {A,K,L,K*} etc.; arc-side errors in
tangent–chord readings at M, N.

complex-certificate: new
Target: OM = ON (full claim).
Technique: complex-number algebra with an explicit polynomial certificate
(machine-assisted discovery, human-checkable identity in the write-up).
Skeleton:
  1. A = 0; K = B(1 − t e^{−iφ}), L = C(1 − s e^{iφ}) — condition 1 consumed by
     the parametrization (rotation of rays BA, CA by ±φ; signs fixed by interior
     hypotheses).
  2. H₁ := Im((K−B)(L−N)/((L−B)(C−N))) = 0, H₂ := Im((K−C)(B−M)/((L−C)(K−M))) = 0
     — conditions 2, 3 as equal signed arguments, branch pinned by Re(·) > 0.
  3. Goal G' := pow(B,ω) − pow(C,ω) − (|B|²−|C|²)/2 = 0 with pow(P,ω) = |P|² −
     Re(conj(w)P), w the circle parameter solving |K|² = Re(conj(w)K),
     |L|² = Re(conj(w)L) — circle through 0, K, L in center-power coordinates.
  4. Certificate: μ·G' = λ₁H₁ + λ₂H₂ on the branch component (or resultant chain),
     μ ≠ 0 on the configuration region.
Key lemmas (claim + mechanism):
  - A, K, L never collinear (denominator Im(conj(K)L) ≠ 0) — because K, L lie in
    disjoint open angular sectors at A (from the interior hypotheses).
Open gaps: the certificate itself (step 4) — including handling the KNOWN mirror
branches where H₁ = H₂ = 0 but OM ≠ ON, so plain ideal membership over the full
variety is false; the branch conditions must enter.
Cases to cover: degenerate denominators; mirror components.
Watch out for: conjugation-convention drift; certifying on the wrong component.

family-invariance-boundary: new
Target: OM = ON (full claim).
Technique: deformation/invariance — show F(φ) = pow(B,ω_φ) − pow(C,ω_φ) is
constant along the 1-parameter family, evaluate at one computable limit member.
Skeleton:
  1. OM = ON ⟺ F = (c²−b²)/2 — median formula.
  2. The valid family is a real-analytic curve in φ — implicit function theorem on
     the decoupled K-side/L-side 2×2 systems.
  3. F' = −2⟨O'(φ), B−C⟩, so constancy ⟺ the centre O moves ⊥ BC — because
     pow(P, ·) is affine in the circle's (center, power-at-0) coordinates and ω
     always passes through the fixed point A.
  4. Anchor: identify the boundary/degenerate member in closed form, evaluate
     F = (c²−b²)/2 there, extend by continuity.
Key lemmas (claim + mechanism):
  - Step 3's reformulation — because circles through a fixed point form an affine
    2-space on which P ↦ pow(P) is affine; only the component of O' along BC
    matters.
Open gaps: ⟨O', B−C⟩ = 0 from the differentiated constraints (load-bearing);
identification + justification of the anchor limit; branch/connectivity of the
valid set. Highest rigor risk of the field — analytic care needed.
Cases to cover: every connected branch of the family; b = c.
Watch out for: mirror branches at the boundary; "numerically smooth" is not a step.

---

Why the field is spread: #1 is a closed finite identity grind (trig),
#2 is synthetic structure-hunting in a transformed configuration (reflections /
isogonal rays), #3 is component-aware polynomial algebra, #4 is a
deformation/constant-of-motion argument. Their load-bearing gaps are pairwise
different in kind (a trig identity; a missing auxiliary circle; a Positivstellensatz-
flavored certificate; a differential identity + limit). #2's fallback degenerates
into #1 — flagged for pruning if that happens.

Recommendation: build secant-trig-identity first (most concrete: everything up to
one identity is already verified and the constraint system is decoupled), and
complex-certificate second (robust, machine-assisted, independent failure mode).
midpoint-reflection-isogonal and family-invariance-boundary are the diversity
holdings — advance whichever survives ranking.

build set: secant-trig-identity, complex-certificate
