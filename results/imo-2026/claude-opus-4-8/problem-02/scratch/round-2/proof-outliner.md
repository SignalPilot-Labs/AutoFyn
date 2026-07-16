## imo-2026-02

### Situation (verified against terrain reports + approach files)

- `complex-reality-conditions` is the closest approach. Its entire algebraic closure (§4–§6: Lemma 1
  circumcenter, conjugate elimination via the 3 monomials `(k̄l̄, k̄, l̄)`, the 3×3 Cramer solve, the
  consistency relation `k̄l̄=(k̄)(l̄)`, and the two symbolically-certified factorizations `Rnum=(b−k)(c−l)G`,
  `num=qN·G` forcing `G=0` ⟹ `TN=0` ⟹ `OM=ON`) is **rigorous and machine-certified** (`repro.py`). The
  **only** gap is §3: deriving the three reality conditions C1,C2,C3 synthetically from the unsigned angle
  equalities + interior hypotheses. This round I have **revised §3** to lay in the directed-angle skeleton
  (Steps 0–4) from the translation explorer, leaving each signed-area inequality as the identified hard step
  for the builder to write out.
- `trig-decoupled-bash` and `power-of-point-balance` are a **genuine shared-gap plateau** — both bottom out on
  the identical scalar identity (★★). The crux explorer confirms (★★) is provably in `⟨(I),(II)⟩` but only via a
  Gröbner certificate with non-human-presentable cofactors; no clean factorization exists (gradient probing
  shows non-constant messy coefficients). Per CLAUDE.md shared-gap guidance: **do NOT nominate these to advance
  this round.** The complex route already bypasses (★★) entirely (works with conjugates directly).

---

complex-reality-conditions: revise + advance (PRIORITY BUILD)
Target: OM = ON, O = circumcentre of △AKL — the whole claim, end to end.
Technique: Complex coordinates with A=0; three angle conditions → three reality (∈ℝ) conditions on
  cross-ratio affixes; conjugate elimination (3×3 Cramer in monomials `k̄l̄,k̄,l̄`) + consistency relation
  drive the target polynomial `TN` to 0. Spine unchanged; only §3 (geometry→algebra translation) re-planned.
Skeleton (revised §3 is the only changed part; §0–§2,§4–§6 already rigorous & certified):
  0. Orientation: `Im(c·b̄)>0`; `signed_area(B,M,C)=¼Im(b̄c)>0` (BMC CCW); `signed_area(B,N,C)=½·area(ABC)>0`
     (BNC CCW) — by the midpoint area formula. — one-line signed-area algebra.
  1. C1 (∠KBA=∠ACL): `arg C1 ≡ ∢(BK,BA) − ∢(CA,CL)` (mod π); K∈int(BMC)⟹`signed_area(B,K,C)>0`⟹`∢(BK,BA)∈(0,π)`;
     L∈int(BNC)⟹`signed_area(N,C,L)>0`⟹`∢(CA,CL)∈(0,π)`; both in (0,π) & equal unsigned ⟹ equal ⟹ C1∈ℝ.
  2. C2 (∠LBK=∠LNC): `arg C2 ≡ ∢(BL,BK) − ∢(NL,NC)` with `∢(NL,NC)=arg(c/(2l−c))` (midpoint factor 2l−c);
     "K inside ∠LBA"⟹`∢(BL,BK)∈(0,∠LBA)⊂(0,π)`; L∈int(BNC)⟹`Im(c/(2l−c))>0`⟹`∢(NL,NC)∈(0,π)`; ⟹ C2∈ℝ.
  3. C3 (∠LCK=∠BMK): `arg C3 ≡ ∢(CL,CK) − ∢(MB,MK)` with `∢(MB,MK)=arg((2k−b)/b)` (midpoint factor 2k−b);
     "L inside ∠ACK"⟹`∢(CL,CK)∈(0,π)`; K∈int(BMC)⟹`Im((k−b/2)·b̄/2)>0`⟹`∢(MB,MK)∈(0,π)`; ⟹ C3∈ℝ.
  4. C_i∈ℝ ⟺ C_i=C̄_i ⟺ E_i=0 (5) — immediate. Hands off to the already-certified §4–§6.
Key lemmas (claim + mechanism):
  - Directed angle ↔ arg: `∢(PU,PV)=arg((V−P)/(U−P))∈ℝ/πℤ`; product/quotient real ⟺ directed angles equal or
    supplementary mod π. The unsigned equality gives "equal OR supplementary"; the interior hypotheses pin the
    "equal" branch — because forcing BOTH directed angles into (0,π) rules out the supplementary case (sum=π).
  - The three midpoint sign facts are exactly `Im(c/(2l−c))>0` and `Im((2k−b)/b)>0`, each equivalent to the
    interior point lying on the correct side of the midpoint segment (signed-area > 0). The factors `2l−c`,
    `2k−b` are the algebraic fingerprints of N=c/2, M=b/2 — a `l−c` or `2l` slip gives the WRONG condition.
Open gaps (the builder fills): write out Steps 0–3 as full signed-area inequalities — specifically the three
  positivity facts `signed_area(B,K,C)>0`, `signed_area(N,C,L)>0` (⟹ `Im(c/(2l−c))>0`), `Im((k−b/2)b̄/2)>0`,
  each from "interior of the named CCW triangle / angle." Everything downstream (§4–§6) is done and certified.
Cases to cover: only the orientation dichotomy — CCW vs CW labelling, handled by the reflection remark (OM=ON
  reflection-invariant). No other casework: the `det A=0` locus is already handled by the §6 continuity argument.
Watch out for:
  - The supplementary trap: the unsigned equality alone does NOT give C_i∈ℝ — the interior positivity is
    essential and is the whole point of the gap. Do not let the builder skip a positivity sub-step.
  - Midpoint factors: `∢(NL,NC)=arg(c/(2l−c))` NOT `arg(c/(l−c))`; `∢(MB,MK)=arg((2k−b)/b)` NOT `arg(k/b)`.
    A wrong factor still passes the numeric check by coincidence of sign but breaks the polynomial E_i.
  - Numeric confirmation of C_i∈ℝ is NOT a proof (per the round-1 reviewer downgrade) — Steps 0–3 must be
    genuine inequalities, not "verified at the audited config."

antipode-perp-bisector: advance (breadth — a route that never uses (★★))
Target: OM = ON — the whole claim.
Technique: Synthetic. A* = 2O−A (antipode of A on ⊙AKL); reduce OM=ON ⟺ A*B=A*C (A* on perp-bisector of BC);
  right angles ∠AKA*=∠ALA*=90° locate A*; angle-chase the three conditions into A*B²−A*C²=0. Bypasses (★★)
  and the reality-condition machinery entirely — a genuinely independent line, kept live for breadth.
Skeleton: as in the existing file (Step 1 antipode equivalence [verified], Step 2 Thales location, Step 3
  projection onto BC, Step 4 the angle-chase crux).
Key lemmas: OM=ON ⟺ A*B=A*C (vector identity, verified 1e-13, round 1); A* = intersection of ⊥AK at K and
  ⊥AL at L (angle in semicircle).
Open gaps: Step 4 — the directed-angle / length chase proving A*B²=A*C² from C1,C2,C3. NOTE for the builder:
  the directed-angle framework now written into complex-reality-conditions §3 (the midpoint factors 2l−c, 2k−b
  and the interior positivity signs) is the natural crutch for this chase; borrow the cevian-length formulas
  from power-of-point-balance if a pure synthetic close stalls.
Cases to cover: A* inside vs outside △ABC (Step 1 identity is position-independent; only Step 3 projection needs
  the sign handled). Confirm A≠A* (A,K,L non-collinear).
Watch out for: this is the riskiest route; its Step-4 crux may be no easier than (★★). It is breadth insurance,
  NOT the primary path — do not let it displace the complex build.

trig-decoupled-bash: DO NOT ADVANCE (shared-gap plateau — record)
Target: OM = ON. Technique: coordinates + law of sines; O_x=(M_x+N_x)/2 as scalar identity (★★).
Plateau reasoning: fully reduced to (★★) in round 1; unchanged since. Crux explorer confirms (★★) is a genuine
  consequence of (I),(II) but only via a Gröbner certificate with non-human-presentable cofactors; no clean
  small-coefficient factorization `E=A·F_I+B·F_II` exists. Sending a builder here reproduces a
  "numerically-verified, symbolically-unproven" partial. Keep live but do not nominate.

power-of-point-balance: DO NOT ADVANCE (same shared-gap plateau — record)
Target: OM = ON. Technique: power of a point, pow(M)=pow(N) ⟹ same identity (★★)/(♦5).
Plateau reasoning: identical residual identity (★★) as trig-decoupled-bash (crux explorer §1 confirms they are
  the SAME identity, `2O·(B−C)=(b²−c²)/2`). Same Gröbner obstruction. Do not nominate.

---

### Recommended field for the outline-reviewer

- **complex-reality-conditions** — revise + advance. **PRIORITY BUILD.** Revised §3 in place; remaining hard
  step is exactly the Steps 0–3 signed-area positivity derivation of C1,C2,C3. One translation lemma from a
  complete, machine-certified proof — the only realistic path to `solved` this round.
- **antipode-perp-bisector** — advance (breadth). Independent synthetic route that never touches (★★); Step-4
  crux open but can borrow the newly-written directed-angle machinery. Secondary.
- **trig-decoupled-bash** — hold (do not advance; shared-gap plateau on (★★), 1 round unchanged, obstruction
  is a non-presentable Gröbner certificate).
- **power-of-point-balance** — hold (do not advance; same (★★) plateau).

Recommended build set: **complex-reality-conditions** (priority), **antipode-perp-bisector** (breadth).
