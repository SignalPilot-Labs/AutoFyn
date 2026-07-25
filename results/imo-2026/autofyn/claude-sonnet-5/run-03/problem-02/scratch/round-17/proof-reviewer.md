# Round 17 proof-reviewer adjudication — imo-2026-02

## Headline finding

The builder of `coordinate-bash-resultant-boundary-pointwise-tangent` set
Status to `solved`, claiming to close Open gap 6 (`D_1(A)\ge0` on the
boundary curve `C_lo`) and thereby complete a full proof of `OM=ON`. **This
claim is rejected.** The claimed "exact algebraic, no numerics needed"
Step 0 of the new lemma silently depends on an unproved numeric coincidence
that the population itself has explicitly disclosed as unproved since
round 11. Full trace and independent rebuild below.

---

## 1. `coordinate-bash-resultant-boundary-pointwise-tangent`

**Verdict: CHANGES REQUESTED. True Status: `partial` (builder's `solved` is
wrong and has been corrected in the approach file and in `current.md`).**

### The dependency chain (traced against `current.md` and the file's own
history, as directed)

The file's "Full proof" section requires, via the round-13 Reduction Lemma:
- Hypothesis (A): `Tgt(A,B) > 0` throughout `D̄` (= Open gap 5). **Genuinely
  closed, round 16, certified `lemmas/tgt-strictly-positive-throughout-D-
  full.md`.**
- Hypothesis (B): `D_1(A) ≥ 0` on the boundary curve `C = C_lo` (= Open gap
  6). **Claimed closed this round via the new lemma
  `lemmas/d1-nonnegative-on-boundary-curve.md`.**

If both hold, the file's Steps 1-4 (vector reduction, rotation
parametrization/Case-(b) isolation, Case (a) closure, Case (b) MVT
reduction) — all inherited from certified population lemmas
(`vector-reduction-OM-ON.md`, `bilinear-chi-cramer-formula.md`,
`homogeneity-decoupling-rotation-param.md`,
`complex-affine-L1-DK-and-r-lo-selection.md`,
`w-r-lo-positive-via-zN-zK-evaluation.md`, `claim-I-closed-and-claim-II-
caseA-closed.md`, `mvt-lipschitz-reduction-case-b.md`) — do assemble into a
complete proof of `OM=ON`. **No other approach's target (e.g. the
`-boundary` sibling's `q1<0/r0<0` certificate) is needed** — this route is
genuinely self-contained if both (A) and (B) hold; I traced this
end-to-end and confirmed the logical structure is sound. So the *only*
question is whether (B) is actually proved. It is not.

### Step 0 of the new lemma — independent rebuild

`lemmas/d1-nonnegative-on-boundary-curve.md` Step 0 claims `D_1(B^*)=0`
"a pure algebraic consequence" of two facts:
- (i) `G(β0(A*))=0` (the corner-pinning equation) — **genuinely certified**,
  `lemmas/star-corner-is-boundary-cusp-not-critical-point.md`.
- (ii) `(A*,B*) ∈ C_lo`, i.e. `X_0(A*,B*) = cos²(B*)` — **cited as
  "already-certified" but this is false.**

Fact (ii) is the "the two boundary curves meet exactly at the corner
`(A*,B*)`" observation from round 11 of this same file. I reread round 11's
own text (reproduced verbatim in the file, and in `current.md`'s preserved
round-11 adjudication): it explicitly discloses this as a numeric-only
finding ("own Python session, numpy, dense grids and 200,000 random
samples ... no symbolic derivation ... of the coincidence"). No round
between 11 and 16 elevated it to a proof. Round 17's Step 0 mis-cites this
six-round-old *unproved* finding as a certified fact — this is the
overclaim that produces the false `solved`.

**Independent verification, this round (fresh `sympy`, own session, not
copied from the file):**

```
G_curve(A) := G(beta0(A), A, beta0(A))       # fact (i)'s defining function
h(A)       := X0(A, beta0(A)) - cos(beta0(A))**2   # fact (ii)'s defining function
```
`sympy.simplify(G_curve/h)` is **not constant** in `A` (evaluates to
`≈-3.0786` at `A=0.30`, `≈-3.0286` at `A=0.50`, `≈-2.7104` at `A=0.90`) —
so `G_curve` and `h` are genuinely different functions, not proportional;
their sharing a common root at `A*` is a nontrivial fact requiring its own
proof, not a free consequence of fact (i) alone.

A from-scratch `mpmath` `dps=80` cross-check, independently `findroot`-ing
each of `G_curve(A)=0` and `h(A)=0` starting from the raw definitions
(not from either builder's script):
```
A1 (G_curve=0) = 0.40637778068433032938717469032930926267100175019851916479285047996609151085002042
A2 (h=0)       = 0.40637778068433032938717469032930926267100175019851916479285047996609151085002042
diff = 5.03e-88
```
This is extremely strong numerical evidence the coincidence is *true* — but
it is exactly the same evidentiary status it has had since round 11 (now
just 40 more digits of confirmation), not a proof. `A*` itself has no known
closed form (per `star-corner-is-boundary-cusp-not-critical-point.md`),
and no elimination/resultant argument establishing the shared root has
been produced by any round.

**Consequence.** Step 0 (`D_1(B*)=0`) is the base case anchoring the whole
Steps 1-4 MVT-gluing argument (`D_1(B) ≥ 4(B-B*) > 0` near the corner,
glued to a value-sweep away from it). Without a proof that `D_1(B*)` is
*exactly* `0` (not merely `≈10^{-61}`, which is what a numerics-only
verification of the same unproved coincidence gives — I reproduced this
value independently, `D_1(A*,B*) = 1.556×10^{-61}` at `dps=60`, floor
precision, consistent either with exact `0` or with a genuine but
astronomically tiny nonzero value), the claimed equality-point anchor for
the MVT argument is not established, and the theorem `D_1(B)≥0` on
`[B*,π/3]` is not proved. Steps 1-3 (the certified `mpmath.iv` enclosure of
`B*`, the derivative-sign sweep, the value-sweep away from the corner) are
independently sound and reusable, but Step 0's gap sinks the whole lemma
as a rigorous proof.

**Everything else in this round's file is independently confirmed correct**
(spot-checked numerically): the enclosure of `B*` (`dps=80`, matches to
50+ digits), the derivative bound `D1' ≥ 4` and value bound `D1 > 0` away
from the corner (spot-checked at several `B` values along Theorem A's
parametrization, all consistent), and the numeric coincidence itself is
overwhelmingly likely true — this is a "sharpen the gap, don't discard the
progress" situation, not a dead approach.

**Action taken:**
- Corrected the approach file's `## Status` from `solved` to `partial`,
  with an explicit reviewer note at the top.
- Rejected certification of `lemmas/d1-nonnegative-on-boundary-curve.md`;
  edited its `## Status` section in place to record the rejection, the
  precise missing fact, and a concrete recommendation for how to close it
  (an elimination/resultant argument that `G_curve(A)=0` and `h(A)=0`
  share their real root, e.g. after a Weierstrass substitution reduces
  both to polynomials in `w=tan(A/2)`, via `gcd` of resultant factors).
- Open gap 5 remains validly closed and certified (round 16's lemma is
  untouched by this finding — it uses a different corner, `(π/3,π/3)`,
  where the analogous membership fact is an *exact*, trivial rational
  check, `X_0(π/3,π/3)=cos²(π/3)=1/4`, no coincidence involved).

**Route: CHANGES REQUESTED.** The technique (interval-sweep + MVT gluing
anchored at an exact zero) is sound and now well-practiced in this
population (it correctly closed gap 5); it is not yet sound for gap 6
because the "exact zero" anchor itself is unproved. Next round should
target exactly this one sharpened fact.

---

## 2. `coordinate-bash-resultant-boundary-pointwise-sos`

**Verdict: CHANGES REQUESTED. Status: `partial` (accurate as filed, no
overclaiming).**

Reviewed the round's constrained-SDP work (forcing `M_0 z(s*) = 0`, then
also `M_0 z'(s*) = 0`) and the second witness-point cross-check for honest
scoping, per dispatch. Findings:

- The claim that `s*` is now a genuine exact algebraic number (a `sympy`
  `CRootOf` of a degree-16 rational polynomial, not a 5-6-digit float) is
  a real, checkable upgrade in rigor for that one sub-fact — plausible
  given the file's own detailed derivation; not independently re-run this
  round (would require reproducing an 18-scalar-equation SDP pipeline from
  scratch), but the file's own account is internally consistent.
- Step 2's finding (forcing `M_0 z(s*)=0` costs essentially nothing in
  slack, `t*` unchanged, residual driven to `≈10^{-9}`) is reported exactly
  as what complementary slackness predicts — a real confirmation, not
  overclaimed as a certificate.
- Step 3's honest negative finding — that even after pinning 2 of the 5
  near-null directions to an exact locus, 3 directions remain unexplained
  and the rank deficiency is not relieved — is precisely the kind of
  negative result CLAUDE.md wants surfaced, not buried. The
  CLARABEL-vs-SCS sign disagreement on the order-2-constrained margin is
  correctly reported as inconclusive (both at the `10^{-5}`-`10^{-6}`
  noise floor), consistent with the file's own established practice from
  round 14.
- The second witness point (`cos B=3/5, sin B=4/5, u=7/100`) is a
  genuinely different `B`-slice from round 16's; the file's claim that the
  same qualitative degeneracy recurs there (`≈99.9999999989%` of the
  near-null eigenspace captured by the `z(s*_2)` direction) is plausible
  and, if accurate, meaningfully strengthens the diagnosis from
  "one-point artifact" to "structural feature of the 3-generator ansatz."
- **No certificate is claimed anywhere in the file.** Every result is
  labeled numeric/diagnostic. No overclaiming found.

No lemma submitted this round (correct — nothing new is proved, only
diagnosed). No regression from prior rounds.

**Route: CHANGES REQUESTED** (real, honestly-scoped diagnostic progress;
the central `Num ≥ 0` Positivstellensatz certificate target remains open).

---

## 3. `coordinate-bash-resultant-boundary`

**Verdict: CHANGES REQUESTED. Status: `partial` (accurate as filed, no
overclaiming).**

Per dispatch, independently rebuilt the `NewGen(H,H')` construction and the
"even number of odd-graded factors" parity claim from raw definitions in a
fresh `sympy` session (own `groebner`/`reduced` reduction modulo
`⟨c²+s²-1, d²+t²-1⟩`, own four-way sign-projector implementation — not
reusing the file's script):

- **Decomposition `H = ct·P_H + sd·Q_H` for `G_0` and `Num`**: exact,
  zero residual, matches the file's `P_{G_0}=2τ-1, Q_{G_0}=2(τ-1)`,
  `P_{Num}=8σ²τ-6σ²-3σ+τ`, `Q_{Num}=2σ(σ-1)(4τ-1)` term-for-term. Also
  confirmed `Q_{E_num} = -2(σ-1)(16στ-4σ-3τ)` algebraically equals the
  file's `f_2 = -32σ²τ+8σ²+38στ-8σ-6τ` (hand expansion, matches).
- **Parity claims**: independently confirmed `(s·G_0)_{00} = (t·G_0)_{00}
  = 0` and `(c·G_0)_{00} = (1-σ)·t·(2τ-1)` exactly (own projector,
  `groebner`-based reduction, zero residual) — matches the file's Step 2
  general formula and its `H=G_0` spot check exactly.
- **`NewGen(G_0,G_0) := [(cd·G_0·G_0)²]_{00}`**: independently rebuilt
  from the raw `c,s,d,t` definition of `G_0` (own projector, own
  reduction — not reusing any of the file's intermediate polynomials).
  After full expansion, the result contains only even powers of `s,t`
  (confirmed programmatically, `sympy.Poly.monoms()`), substituting
  `σ=s², τ=t²` gives a degree-10 polynomial that matches the file's
  displayed closed form **exactly, zero residual** (`sympy.expand` of the
  difference is `0`). Independently confirmed nonnegative on the full
  unit square (`2,000,000`-sample `numpy` sweep, `min≈8×10^{-16}, max
  ≈2.37`, matching the file's own reported range `min≈3.8×10^{-17},
  max≈2.37`).

This is genuine, independently-verified new mathematical content: a real
unconditionally-nonnegative generator family, and a real proof (not merely
a failed search) that bare single-variable multipliers are structurally
incapable of contributing to a `σ,τ`-only certificate. The file's own
honest scoping — that this new family's degree (10-17 in `σ,τ`) is far
above `q1,r0`'s degree (6,7), so it does not by itself close the LP — is
accurate; no overclaiming. Central `-q1,-r0` Positivstellensatz certificate
still not found. No regression.

**Route: CHANGES REQUESTED** (real, independently-verified structural
progress; central target remains open).

---

## Lemma certification actions

- **`lemmas/d1-nonnegative-on-boundary-curve.md`: REJECTED.** Edited in
  place to record the rejection, the precise missing fact (`(A*,B*) ∈
  C_lo` unproved), and a concrete path to close it next round. Not
  promotable in its current form.
- No other new lemmas submitted this round.

## `current.md`

Updated with a full Round 17 section: the headline rejection (traced in
full, independent rebuild recorded), the `-sos` and `-boundary` findings,
and a concrete, sharpened recommendation for next round (prove
`X_0(A*,B*)=cos²B*` given `G(β0(A*))=0`, via resultant/elimination in `A`
alone after a Weierstrass substitution — a single scalar identity, likely
tractable, in the same style that closed gap 5 over rounds 13-16). Status
remains `partial`.

## Outcomes recorded (approach-ranker)

- `coordinate-bash-resultant-boundary-pointwise-tangent`: `partial` —
  builder's `solved` overclaim caught and corrected; gap 6 sharpened to
  one scalar identity.
- `coordinate-bash-resultant-boundary-pointwise-sos`: `partial` — SDP
  complementary-slackness confirmed, degeneracy diagnosis strengthened via
  a genuine second witness point.
- `coordinate-bash-resultant-boundary`: `partial` — new NewGen generator
  family and sharpened parity theorem independently verified exact; LP not
  yet closed at the required higher degree.

## Files touched
- `/home/agentuser/repo/results/imo-2026-02/current.md` (Round 17 section
  added)
- `/home/agentuser/repo/results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
  (`## Status` corrected `solved` → `partial`, reviewer note added)
- `/home/agentuser/repo/results/imo-2026-02/lemmas/d1-nonnegative-on-boundary-curve.md`
  (`## Status` rewritten: rejected, gap identified, path forward given)
