# Round 2 — proof-reviewer report: IMO 2026 P2

Slugs built this round: `a-star-cyclicity` (claims solved), `analytic-resultant`
(outline only), `miquel-spiral` (numeric gate failed). Reviewed independently per
CLAUDE.md rigor rules. All algebra re-derived from scratch in sympy; nothing
trusted from the file.

## 1. `a-star-cyclicity` — VERDICT: APPROVE (Status: solved)

### Independent re-derivation of the certificate

**Setup.** Normalisation `B=(0,0), C=(P_B+P_C,0), A=(P_B,1)` (verified: scale of
the standard placement `A=(c cos B, c sin B)` by `1/(c sin B)`; `sin A =
(cot B + cot C) sin B sin C` gives `C_x = P_B + P_C`). Angle alphabet
`α=∠KBA=∠ACL, β=∠LBK=∠LNC, γ=∠LCK=∠BMK`, `p=cot α, q=cot β, r=cot γ`.

**K,L formulas — re-derived via sine rule in △BMK, △CNL (NOT copied).**

△BMK: `∠MBK=α` (M∈BA), `∠BMK=γ`, `∠BKM=π-α-γ`. Sine rule
`BK = BM·sin γ/sin(α+γ) = (√(P_B²+1)/2)·sin γ/sin(α+γ)`. BK direction is
`(cos(B-α), sin(B-α))` (BA rotated toward BC by α). With
`sin γ/sin(α+γ) = csc α/(p+r)` and `cos(B-α)/sin B = (P_B p+1)/csc α`, the
`csc α` factors cancel and `K = ((P_B p+1)/(2(p+r)), (p-P_B)/(2(p+r)))`. Matches
the file exactly. The L formula is the C-side analogue via △CNL; verified
identically. ✓

**F1, F2 — independently built.** `B` is the origin, so for (ii) `∠LBK=β` the
two vectors at B are `BL=L, BK=K`, and the cleared numerator of
`L·K − q·det(L,K)` is F1 (degree 4, 16 terms). For (iii) `∠LCK=γ` the vectors are
`L−C, K−C`, giving F2 = cleared num of `(L−C)·(K−C) − r·det(L−C,K−C)` (degree 4,
16 terms). Constructed directly from the cot identity `cot∠(s,t)=(s·t)/det(s,t)`
with the **+q, +r signs** (sign verified below). ✓

**Circumcentre / Π.** O from `2O·(K−A)=|K|²−|A|²`, `2O·(L−A)=|L|²−|A|²`.
`Π = num(O_x − (3P_B+P_C)/4)` (degree 6, 68 terms). ✓

### Gröbner computation (re-run, exact, over Q, grevlex)

```
Gröbner basis of <F1,F2> in Q[p,q,r,P_B,P_C] (grevlex): 6 elements
  G[0]: deg 7, 188 terms
  G[1]: deg 7, 160 terms
  G[2]: deg 6, 105 terms
  G[3]: deg 5,  47 terms
  G[4]: deg 4,  16 terms   (= F1 or F2 up to sign)
  G[5]: deg 4,  16 terms
Computed in 0.12 s.
Normal form of Π modulo G: 0   (exact, rational)
Is remainder zero? True
```

The file claims "6 elements, remainder 0"; **confirmed verbatim**. The
ideal-membership `Π ∈ ⟨F1,F2⟩` is a genuine exact certificate, not a numeric
check.

### Sign/orientation convention — checked (this was the load-bearing subtlety)

`cot∠(s,t) = (s·t)/det(s,t)` equals `cot(unsigned angle)` ONLY when `det(s,t)>0`
(otherwise it is `cot` of the *signed* angle = `−cot(unsigned)`). So F1=0 with
the `+q` sign captures `∠LBK=β` only on the component where `det(L,K)>0`.

Numerically solved `F1=F2=0` for `(β,γ)` given `(α,P_B,P_C)` on 8 triangles
(incl. the degenerate `P_B=P_C` isosceles-at-A case and two extreme scalene
triangles). For every *valid inside* solution (all six angle conditions matching
and points inside the required regions):
- `det(L,K) > 0` and `det(L−C,K−C) > 0`  — so the `+q,+r` signs are correct;
- `O_x − (3P_B+P_C)/4` is `~1e-14` (machine zero) — the conclusion holds.

The geometry forces `det>0`: with A above the x-axis, the counterclockwise sweep
at B is `BC → BL → BK → BA` (K inside angle LBA and K,L inside △BMC, △BNC), so
`BL→BK` is counterclockwise. The proof states these ray orderings ("BA→BK→BL at
B, CA→CL→CK at C") but does not explicitly connect them to the sign of det — a
minor rigor shorthand, not a gap: the orderings are stated and the conclusion is
a one-step reading of them.

### Inside-component sufficiency (the dispatch's question 4)

The inside hypotheses (`K∈△BMC`, `L∈△BNC`, `K∈∠LBA`, `L∈∠ACK`) are **strict
inequalities** — they impose no polynomial *equalities* beyond F1, F2. Conditions
(i),(iii-at-M),(ii-at-N) are built into the K,L parametrisation; F1, F2 are the
*only* polynomial equalities remaining. Hence the inside configuration is an open
subset of `V(F1,F2)`, and `Π∈⟨F1,F2⟩ ⟹ Π=0` on all of `V(F1,F2) ⟹ Π=0` on the
inside component. **Ideal membership is exactly the right, sufficient
statement.** No extra component issue: the spurious components (e.g. where
`det<0` so the unsigned angle is `π−β`) ALSO have `Π=0` (verified numerically:
test triangle `P_B=1.5, P_C=2.5` landed on such a spurious solution and still had
`O_x−target ≈ 8e-14`); this is harmless — the certificate proves *more* than
needed. ✓

### Degenerate case `B=C` (`P_B=P_C`, A*=A)

Verified numerically (`P_B=P_C=1`): all six angle conditions match, `det>0`,
`O_x = target = 1.0` to `1e-16`. The certificate is uniform — `Π∈⟨F1,F2⟩` is a
polynomial identity that does not factor through `(P_B−P_C)`, so the
`0/0`-looking factorisation `Δ_num = −(P_B−P_C)·Π` (also independently verified)
is bypassed; the ideal-membership gives `O_x=target` directly when `B=C`.
Denominators `p+r`, `p+q` vanish only when `α+γ=π` or `α+β=π` (degenerate
workhorse triangles), which are excluded by the inside hypotheses — no
division-by-zero hole. ✓

### Lemma 1 (midpoint-cevian cotangent) — verified

Sine-rule in △XYZ (`YZ = XY sin ψ/sin(θ+ψ)`) and △YWZ
(`YZ = (XY/2) sin δ/sin(θ+δ)`) gives `2 sin ψ sin(θ+δ) = sin δ sin(θ+ψ)`. Dividing
by `sin ψ sin δ sin θ` and simplifying yields `cot ψ = cot θ + 2 cot δ`
(sympy `trigsimp` confirms the reduction). ✓

### Lemma 2 (A* reflection / perpendicular-bisector identity) — verified

`M=(P_B/2,1/2)`, `N=(P_B+P_C/2,1/2)`; midpoint of MN `= ((3P_B+P_C)/4, 1/2)`,
MN horizontal ⟹ `p.bis(MN): x=(3P_B+P_C)/4`. `D=((P_B+P_C)/2,0)`,
`F=(P_B,0)`, `A*=A+(D−F)=((P_B+P_C)/2, 1)`; midpoint of AA* `=((3P_B+P_C)/4,1)`,
AA* horizontal ⟹ `p.bis(AA*)` is the same vertical line. `A*=A ⟺ P_B=P_B ⟺ B=C`. ✓

### Verdict

The core certificate (`Π∈⟨F1,F2⟩`, 6-element Gröbner basis, exact 0 remainder)
is **independently reproduced**. The K,L formulas are re-derived from sine rule.
F1, F2 are the correct cleared numerators with the correct sign on the inside
component (verified numerically + by ray orderings). The inside hypotheses add
no polynomial equalities, so ideal membership is sufficient and uniform over the
degenerate case. Lemma 1, Lemma 2, and the `Δ_num = −(P_B−P_C)·Π`
factorisation all check out. The conclusion `O_x=(3P_B+P_C)/4 ⟹ O∈p.bis(MN) ⟹ OM=ON`
follows.

**Status: solved. Verdict: APPROVE.** Minor non-blocking note: the proof could
state explicitly that the inside ray orderings give `det(L,K)>0`,
`det(L−C,K−C)>0` (so the `+q,+r` cot signs match the unsigned angles); the
orderings are already written, this is a one-sentence completion, not a gap.

## 2. `analytic-resultant` — VERDICT: RETHINK (Status: unsolved)

No proof was built — only an outline with five open GAPs (GAP-1 through GAP-5),
the load-bearing GAP-5 being the general-`(p,q)` elimination that was never run.
The algebraic crux is the same ideal-membership question that `a-star-cyclicity`
has already closed (in a cleaner cotangent parametrisation), so this route is
now strictly dominated. The outline's own warning ("naive 5-var lex Groebner
times out at 9 min") is moot since `a-star`'s grevlex computation terminates in
0.12 s. Recommend the outliner fold this into `a-star` or re-plan a genuinely
different framing.

## 3. `miquel-spiral` — VERDICT: RETHINK (Status: unsolved)

The numeric gate (GAP-2) failed: the conjectured spiral/indirect-similarity
centre `S₀` (for pairings `(B,K)→(C,L)` and `(M,K)→(N,L)`) and the Miquel point
of `(AB,AC,BK,CL)` are neither `O` nor on `p.bis(MN)` on any scalene triangle
tested. The load-bearing transformation does not exist. The approach is dead as
framed; no proof prose was (correctly) built on the refuted conjecture. Kept in
the population only as a recorded negative result.

## Outcomes for the ranker (round 2)

- `a-star-cyclicity` → **verified-milestone** (solved; Gröbner certificate
  independently reproduced: 6-element basis, exact 0 remainder; K,L formulas,
  Lemma 1, Lemma 2, Δ factorisation, degenerate case, inside-component
  sufficiency all verified).
- `analytic-resultant` → **dead-end** (outline only, no proof built; same
  algebraic crux as `a-star`, which already closed it).
- `miquel-spiral` → **dead-end** (numeric gate failed; conjectured
  spiral/Miquel centre does not exist).
