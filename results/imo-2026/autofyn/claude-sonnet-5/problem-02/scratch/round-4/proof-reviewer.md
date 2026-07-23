# Proof review — imo-2026-02, round 4 (SECOND adversarial review this round)

## Verdict
**`coordinate-trig-bash`: APPROVE.** Status confirmed **`solved`**. This is
the third "solved" claim on this approach within one round; unlike the
first two (round 4 first pass — two confirmed errors; and the prior
proof-reviewer pass this round, which caught them), this build's fixes hold
up under a fully independent, from-scratch, adversarial re-derivation. No
gap found. `current.md` updated (Status remains `solved`, Full proof
retained, new confirmation note appended). New lemma certified.

---

## Independent re-derivation (own sympy/numpy sessions, not reusing any
builder or prior-reviewer script)

### 1. R1,R2 rescaling relation
Re-derived from first principles that `u_K(θ)` (direction of ray `BK`) is
the unit vector obtained by rotating `(A-B)/|AB|` by `-θ`:
symbolically, with `A-B` normalized to `(cB,sB)` (`cB²+sB²=1`),
`(cos(φ_B-θ),\sin(φ_B-θ)) - \mathrm{rot}((cB,sB),-θ) = (0,0)` exactly
(`sympy.simplify`). Hence `K=B+r_1u_K(θ)=B+(r_1/|AB|)\cdot d_1(θ)` where
`d_1(θ):=|AB|u_K(θ)`, confirming the write-up's corrected relation
**`R1:=r1/|AB|`** (not `r1|AB|`) is right. Matches the current write-up
exactly.

### 2. Q1,Q2 closed forms and the Bézout identity — full independent rebuild
Built `K(R1)=B+R1\cdot\mathrm{rot}(A-B,-θ)`, `L(R2)=C+R2\cdot\mathrm{rot}(A-C,θ)`,
`M,N`, and from these the raw `Cross_i,Dot_i` definitions of Lemma T1
(never touching the write-up's coefficient tables). Result: my from-scratch
`Q1(R2),Q2(R1)` match the write-up's claimed closed forms **exactly**
(`sympy.simplify` of the difference `=0`). Likewise built `D,Nx,T` from the
standard Cramer's-rule circumcenter formula (independent of the write-up),
and `P1,P2` exactly as stated.

**Key finding: the Bézout identity `ΔT=P1Q2+P2Q1` is unconditionally true**
as a polynomial identity in the six **free** real variables
`(p,q,ct,st,R1,R2)` — confirmed by `sympy.expand(ΔT-(P1Q2+P2Q1)) == 0`
(the literal zero object, not merely "simplifies to 0 at a point"), and
independently re-confirmed at 6 fresh random non-Pythagorean rational
6-tuples (`ct²+st²≠1` in each). This is *stronger* than the current
write-up's (still-true, still-sufficient) conditional claim
("holds whenever `ct²+st²=1`").

Crucially, I directly re-evaluated the **exact rational point** that the
round-4-first-pass review cited as a "confirmed disagreement"
(`(p,q,ct,st,R1,R2)=(3/10,11/5,7/11,-2/9,13/4,5/3)`, off the unit circle,
`(7/11)²+(-2/9)²=4453/9801≠1`):
```
ΔT             = 1849467953299/476328600000  ≈ 3.8827564695863317
P1·Q2+P2·Q1    = 1849467953299/476328600000  ≈ 3.8827564695863317
```
**These agree exactly** — contradicting the prior review's claim of
`ΔT=3.8828` vs `P1Q2+P2Q1=8.5755` at this same point. I traced the two
individual products: `P1·Q2 ≈ 18.2959`, `P2·Q1 ≈ -14.4131`, summing to
`3.8828`, matching `ΔT` — so the prior review's reported sum (`8.5755`) was
itself a computational slip somewhere in that independent check (not
reproducible from a correct construction), not a real flaw in the
mechanism. This does **not** retroactively make the current write-up wrong
— it only asserts the weaker conditional version, which is true a fortiori
and is all the proof logically needs (since `θ` is always a genuine real
angle in this argument, `ct²+st²=1` always holds where it's invoked). I
certified the stronger unconditional fact as a new lemma,
`lemmas/bezout-identity-Q1Q2-T.md`, and flagged the correction inline in
`coordinate-trig-bash.md`'s promotable-lemmas section for the historical
record.

### 3. Full end-to-end re-verification on 2 fresh configurations
Own root-finder (no `brentq` code reused from either builder or prior
reviewer), using genuine `arccos`-based **unsigned** angle equations
`F1(θ,r2)=∠LBK-∠LNC=0`, `F2(θ,r1)=∠LCK-∠BMK=0` — no `Q1,Q2` algebraic
shortcut anywhere in this step. Chose `(p,q,θ)=(0.6,1.5,20°)` and
`(-0.2,2.0,10°)`, neither reused from any prior round or either builder
pass.
- Scanned the **entire** range `r∈(10^{-6},5)` for sign changes in both
  `F1,F2`: found exactly **one root each** in both configurations (no
  spurious second root to worry about) — direct confirmation of Theorem A's
  uniqueness claim on fresh data.
- Verified the containment/sign conditions (SC1) `ψ_B(r_2)<φ_B-θ` and (SC2)
  `ψ_C(r_1)>φ_C+θ` **hold** at both found roots in both configurations
  (this is exactly the repeated failure point flagged by the dispatch, e.g.
  round 2's sign-convention bug) — genuinely checked, not assumed.
- Computed the true circumcenter of the resulting genuine `A,K,L` via the
  standard formula: `O_x-p/2 = 1.7\times10^{-16}` and `-2.1\times10^{-13}`
  respectively (machine precision), with `D=2.55, 2.56` (both bounded away
  from `0`).
- Separately, substituted the genuine root-found `(r_1,r_2)` into the
  algebraic `Q_1,Q_2` via the corrected `R_1=r_1/|AB|,R_2=r_2/|AC|`: both
  vanish to machine precision (`≤10^{-12}`) in both configurations,
  confirming the "F=0⟹Q=0" sign-matching mechanism on genuinely fresh data,
  not just re-symbolically.
- Independently re-verified the two Sweep-Lemma cross-product facts
  (`cross(B-M,u_K(θ))=+½|AB|\sinθ`, `cross(C-N,u_L(θ))=-½|AC|\sinθ`) on 4
  configurations including both fresh ones — exact match in all four.
- Independently re-verified Lemma Δ's closed form
  `Δ=2q\sin(θ+α)/\sinα` and `k=\cotα` (circumcenter height) on 3
  configurations including a more extreme shape `(p,q)=(2.5,0.4)` — exact
  match in all three.

### 4. `D≠0` nondegeneracy treatment
Re-affirm the prior reviewer's judgment: relying on the problem statement's
own phrase "the circumcentre of triangle `AKL`" (which presupposes
non-degeneracy, i.e. a genuine triangle) is a legitimate, standard olympiad
proof move, not hand-waving under CLAUDE.md's rigor rules — it is an
explicit, reasoned resolution ("a triangle is non-degenerate by
definition, exactly as `let ABC be a triangle` is never re-derived"), not
an unjustified assertion. This is not a step the problem's hypotheses need
to independently force; it is part of the initial data the problem itself
supplies. I decisively accept this as sufficient for `solved`, consistent
with the prior reviewer pass.

### 5. Composition with the corrected R1,R2 (existence/uniqueness + sign lemma)
§3 (the exact, not-mod-π sign-matching argument) works entirely in raw
`r_1,r_2`, never touching `R_1,R_2` — confirmed by direct reading and by
the fact that my fresh numerical check (item 3 above) verifies both the
raw-angle version (SC1/SC2, `F=0`) and the algebraic version (`Q_1,Q_2=0`
via the corrected `R=r/|side|` substitution) agree at the same genuine
point. No hidden dependency on the old (wrong) `R=r|side|` convention
survives anywhere in the composed chain.

## Overall assessment
Every load-bearing piece — the rescaling relation, the `Q1,Q2` closed
forms, the Bézout identity (now known to be even stronger than claimed),
the sign-matching cross products, the `Δ>0` formula, the existence/
uniqueness machinery, the `D≠0` well-posedness resolution, and the final
assembling arithmetic — was independently rebuilt from scratch in this
review and found to match the write-up (or to support an even stronger
version of one of its claims). Two fresh, never-before-used numeric
configurations were verified end-to-end via genuine unsigned-angle
root-finding, with the containment/orientation conditions explicitly
checked (not merely assumed), addressing the exact class of subtle failure
that broke round 2. I find no remaining gap, of any size.

**Status: solved. Verdict: APPROVE.**

## current.md
Status remains `solved`; Full proof (already present, matching
`approaches/coordinate-trig-bash.md`) is retained. Appended a new "Round 4
(third pass)" entry to `Approaches tried` documenting this independent
re-review, the fresh confirmation of every piece, and the correction that
the prior round's "Error (B)" finding (Bézout identity requires the
Pythagorean relation) was itself a computational mistake — the identity is
actually unconditional, though the current write-up's more cautious
conditional claim is true and was never itself an error.

## Promotable lemmas
- New lemma `lemmas/bezout-identity-Q1Q2-T.md`: **certified** — the
  Bézout-style cofactor identity `ΔT=P1Q2+P2Q1`, proved **unconditionally**
  in the six free variables `(p,q,R1,R2,ct,st)` (stronger than the
  conditional version cited in `coordinate-trig-bash.md`), independently
  re-derived from the vector construction, verified by full symbolic
  expansion (`=0` exactly) and cross-checked at the specific rational point
  a prior review claimed refuted it (both sides agree exactly there).
- All previously-certified lemmas (`Q1,Q2` closed forms, sign-matching,
  Lemma Δ, existence/uniqueness, decoupling/sweep, coordinate reduction,
  angle-matching-ray-quadratic, antipode-reduction, median-length-power-
  reduction, radical-axis-form-of-TI, signed-isosceles-reduction) stand
  unchanged; no new issues found with any of them this pass.

## Files touched
- `/home/agentuser/repo/results/imo-2026-02/current.md` — Status kept
  `solved`; new Round-4-third-pass confirmation entry appended.
- `/home/agentuser/repo/results/imo-2026-02/approaches/coordinate-trig-bash.md`
  — inline note added flagging the stronger unconditional Bézout identity
  and pointing to the new lemma.
- `/home/agentuser/repo/results/imo-2026-02/lemmas/bezout-identity-Q1Q2-T.md`
  — new, certified.
