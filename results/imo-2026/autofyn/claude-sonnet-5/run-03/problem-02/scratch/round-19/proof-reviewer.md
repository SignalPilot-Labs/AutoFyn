# Round 19 proof-reviewer adjudication — imo-2026-02

Two built approaches, adjudicated independently. **Neither reaches
`solved`.** Both verdicts: **CHANGES REQUESTED** (Status `partial` in both
cases, correctly self-reported by the builders — no overclaiming caught,
but one important attribution correction required in approach 2).

---

## 1. `coordinate-bash-resultant-boundary-pointwise-tangent`

**Verdict: CHANGES REQUESTED. Status: `partial`** (matches the file's own
self-report — no overclaiming).

### (a) Is the new `f(β1)>0` sub-lemma correct and gap-free?

**Yes, fully verified, independently re-derived.**

- `f(0) = K_c + Q = 2 sinA sin(A+B) − sinA sinB = sinA(2 sinC − sinB)`
  (using `A+B=π−C`, `sin(A+B)=sinC`) — re-derived by hand, matches the file
  exactly.
- The `sinB ≤ sinC` two-case argument (WLOG `B≤C`): if `C≤π/2`, both `B,C∈
  [0,π/2]` with `B≤C`, monotonicity of `sin` on `[0,π/2]` gives `sinB≤
  sinC`. If `C>π/2`: since `A>0` strictly, `π−C = A+B > B`, and `π−C<π/2`
  (as `C>π/2`), so `0<B<π−C<π/2`, monotonicity gives `sinB<sin(π−C)=sinC`.
  Both cases exhaustive (`C∈(0,π)`), no gap. Hence `f(0) = sinA·(sinC +
  (sinC−sinB)) ≥ sinA·sinC > 0` strictly. **Independently re-verified
  algebraically by hand — correct, no gap.**
- `f'(β)=sin(A+β)cosB+sin(A+B−β)>0` on the *whole* `(0,γ)` — this sign
  argument (`cosB>0` since `B<π/2`; both sine arguments in `(0,π)`) is
  *already inside* the certified `lemmas/claim-I-closed-and-claim-II-caseA-
  closed.md`'s own Theorem A proof, confirmed by independently re-reading
  that certified lemma: the proof text literally states "for `β∈(0,γ)=(0,B)`"
  before invoking `β_0` at all — the extension to the whole interval is a
  real, previously-unexploited fact already sitting inside an existing
  certified proof, not a new derivation, and is legitimate to invoke.
- MVT combination `f(β1)>f(0)>0` for all `β1∈(0,γ)`: elementary, correct.

**This closes exactly what round 18/19's dispatch asked for, with no gap.**
Recommend certifying as a lemma (see below).

### (b) Is the counterexample genuine (f(β1)>0 but G(β1)<0)?

**Yes, independently reproduced exactly, from scratch (own fresh `mpmath`,
50 digits, not reusing the builder's script), at the witness `A≈0.010023,
B≈1.499257`:**

```
f(β1) =  0.71947080232542857409...  (>0, matches file exactly)
G(β1) = -0.67945439694943198707...  (<0, matches file exactly)
G(β1) - (2*Kc - f(β1)) = 0           (confirms exact identity G=2Kc−f)
P = 0.99882492106152325...  (>0)
E = -0.49873339578002014...  (<0)
```

The identity `G(β) ≡ 2K_c − f(β)` (an exact algebraic identity, verified
symbolically to residual 0) makes it *obvious* that `f>0` alone can never
imply `G≥0` in general — they are affinely related with a fixed shift
`2K_c`, not proportional, not co-monotone. So this negative finding was
inevitable once the correct target was identified, not a coincidence.

**A broader independent sweep** (own script, `numpy`, 300,000 raw triangle
samples restricted to the file's own literal Case-(a) domain definition —
`β1≤β0(A)`, `β0(A)<γ`, `B≤C`) reproduced: `28,116` valid Case-(a) points,
`G<0` at **71.7%** of them (file: ≈70%, matches closely), `f≤0` at **0%**
(file: 0 violations — matches), and **100%** of the `G<0` failures have
`P>0 ∧ E<0` exactly (file: `232,430/232,430` — matches). **Fully
corroborated, independently, with a different sampling method
(vectorized numpy rather than the builder's presumed sympy loop).**

### (c) Is the identification with the pre-existing `T≥0`/`−q1,−r0` gap
correct, or is this a new distinct gap being conflated with an old one?

**Verified genuine — this is the SAME gap, not a new one, and the
identification is technically correct**, with one important nuance the
file should make more explicit next round:

- `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`'s own "Setup" defines its
  scope as "for a triangle with `A≤π/2`" — i.e. wherever `X_0≥0` makes
  `β1` a well-defined real angle at all — with **no** restriction relating
  `β1` to `β0(A)` anywhere in its Theorems 1–4's statements or proofs
  (independently re-read the lemma text to confirm this). So `G(β1)≥0`
  (equiv. `T≥0` in the `P>0∧E<0` residual) is a fact about the raw
  `(A,B)`-domain, defined purely via `X_0`, not case-restricted.
- `lemmas/case-b-e-lt-0-t-factorization.md` confirms `T=B_c²X_0−E²` reduces
  to `−q_1,−r_0` polynomials in `(σ,τ)=(sin²A,sin²B)` alone — again no
  `β1` vs `β0` case-split baked in anywhere.
- `coordinate-bash-resultant-boundary`'s own long-running LP/SDP search for
  a Positivstellensatz certificate for `−q_1,−r_0` (rounds 10–19, still
  open) is stated over the **residual domain** where `P>0∧E<0` (not a
  domain artificially restricted to `β1>β0(A)`), so it already, by
  construction, was targeting the region round 19's witness falls into.

**Conclusion: this is genuinely the population's pre-existing central gap,
not a new one** — round 19's real finding is that this route (`-pointwise-
tangent`) cannot bypass that central gap via an "easy Case (a)," as the
file's inherited round-11 aside ("`f`, not `G`, is the relevant quantity"
in Case (a)) had assumed without proof. **One residual caveat worth
flagging for the record** (not a flaw in this round's finding, but context
for future rounds): the population's history contains at least
**three different, textually similar "Case (a)/(b)" splits** with
different defining criteria — `Y(γ)≥0` vs `<0` (Theorem 16.2, round 9),
`A≤π/2` vs `>π/2` (`case-b-p-le-0-and-e-ge-0-closed.md`, round 10), and
`β1≤β0(A)` vs `>β0(A)` (this file, round 11+). The round-19 builder
correctly navigated this by checking the actual formula-level definitions
(not the case *names*) and confirming `G(β)` is one fixed function usable
regardless of naming scheme — this is the right approach, and the
"Step 2" citation as re-derived this round is sound. But because "Full
proof" Step 2's own text ("the problem's defining condition on `O` reduces
... to `G(β1)≥0`" for *every* `β1∈(0,γ)`) is itself only a compressed
citation of a long chain from rounds 1–10 ("NOT re-derived from scratch in
this round" — the file's own words), a fully complete write-up should, at
some point, re-verify from the underlying `bilinear-chi-cramer-formula.md`
/`complex-affine-L1-DK-and-r-lo-selection.md` chain that `G(β1)≥0` (rather
than some other quantity) really is the uniform target for *every*
`β1∈(0,γ)`, not only assume Step 2's literal wording is accurate. This is
a residual due-diligence item, not a reason to doubt round 19's finding
(which is internally consistent and numerically overwhelming), but should
be logged.

### Lemma certification

**Certifying** a new lemma extending `claim-I-closed-and-claim-II-caseA-
closed.md`'s Theorem A: `f(β)>0` for every `β∈[0,γ)` (not just `(β0,γ)`),
via `f'(β)>0` on the whole interval (already inside the certified proof)
plus the new `f(0)=sinA(2sinC−sinB)>0` fact (`sinB≤sinC` two-case
argument). Written to `lemmas/f-positive-on-full-interval.md`, with an
explicit caveat (matching the file's own honest framing) that this does
**not** close Case (a) — `G(β1)≥0` (not `f(β1)>0`) is the fact actually
needed there, and `G(β1)≥0` fails at ≈70% of genuine Case-(a) points.

### Net assessment

Real, independently-verified progress (a genuine, gap-free sub-lemma) plus
an important, correctly-diagnosed, honestly-reported *negative* finding
that narrows the route's true difficulty rather than manufacturing a false
closure. No overclaiming. Status `partial` is accurate. **This route's sole
remaining gap (7) is now precisely: prove `T:=B_c²X_0−E²≥0` (equivalently
find a `−q_1,−r_0` Positivstellensatz certificate) — identical to the
population's oldest open target, still unresolved after ~9 rounds of
dedicated LP/SDP search by two sibling approaches.**

---

## 2. `spiral-similarity-bootstrap`

**Verdict: CHANGES REQUESTED. Status: `partial`** (matches the file's own
self-report — concyclicity itself correctly left open, no overclaiming of
the final target) — **but a significant attribution/framing correction is
required for next round.**

### (a) Is `P` really fixed and does circle(AKL) pass through it, checked
independently on fresh triangles/parameters?

**The "fixed" part (independent of `K,L,φ`) is verified — trivially, by
construction (`P` is defined only from `A,B,C`, no `K,L` dependence
anywhere in Steps 1–3).** The "lies on circle(AKL)" part is, correctly, only
numerically evidenced by the file (not claimed as proved) — this is exactly
the still-open target (Open gap 1). I did not attempt to reproduce the
`fsolve`-based genuine-solution numerics (would require standing up the
whole H1–H3 solver, a substantial undertaking not repeated here given time
budget), but the file's own framing (evidence, not proof) is honest and
correctly scoped — no overclaiming of this part.

### (b) Is the `OM=ON ⟺ concyclic(A,K,L,P)` equivalence correct and
unconditional? Independently re-derived.

**Yes, correct — re-derived from scratch (own hand computation, cross-
checked against the two already-certified round-1 lemmas):**
- `OM=ON ⟺ O·(C−B)=(|C|²−|B|²)/4 ⟺ O∈ℓ` — this is exactly the already-
  certified `lemmas/vector-reduction-OM-ON.md`, a genuine two-directional
  `iff` (re-confirmed: it is literally `OM²=ON² ⟺` the displayed equation,
  both directions trivial from the algebra).
- `ℓ` is *by construction* the perpendicular bisector of segment `A,P`
  (reflection formula, `P:=` reflection of `A` in `ℓ`) — this is a
  tautology given how `P` is defined, no computation needed.
- `X∈ℓ ⟺ |X−A|=|X−P|` for any `X` (definition of perpendicular bisector) —
  applying with `X=O` (circumcenter of `AKL`, so `|O−A|=|O−K|=|O−L|`
  automatically) gives `OM=ON ⟺ |O−A|=|O−P| ⟺ P` on circle`(O,|O−A|)=
  (AKL) ⟺ A,K,L,P` concyclic. Every step here is a genuine
  biconditional — **confirmed correct, unconditional, no hidden case**
  (the file's own handling of the `A=P` degenerate edge case, i.e.
  `AB=AC`, is also correctly reasoned: the chain trivializes gracefully,
  no special casing needed for the logical structure).

### (c) Is `P` the SAME point as the previously-established fixed point
`Q` (round 1, `lemmas/amnq-concyclic-and-reduction.md`)?

**YES — P and Q are IDENTICALLY the same point. Verified independently,
both structurally and numerically.**

- Structurally: `amnq-concyclic-and-reduction.md`'s `ℓ` is defined as "the
  perpendicular bisector of segment MN," and `Q:=` the reflection of `A`
  in that `ℓ`. `spiral-similarity-bootstrap`'s `ℓ` is defined via `{X:
  X·(C−B)=(|C|²−|B|²)/4}` — this is *exactly* the perpendicular bisector
  of `M,N` (`M,N` being midpoints, `MN∥BC`, and `{X:XM=XN}` is by
  definition the perp bisector of `MN`, which the file's own Step 1
  derives from the same `XM=XN` condition). Both `P` and `Q` are defined as
  "reflection of `A` across the perpendicular bisector of `MN`" — the
  **identical construction**, just under different names in different
  files.
- Numerically (own fresh Python, 5 random triangles, both formulas
  computed independently from raw coordinates — `Q` via the reflection
  formula, `P` via "foot of perpendicular from circumcenter onto line
  through `A` parallel to `BC`"): **`|Q−P| < 5×10⁻¹⁶` at every trial**
  (machine precision) — an exact identity, not an approximation.
- Consequently, the "iff" `OM=ON ⟺ concyclic(A,K,L,P)` is **also not new
  logical content**: `amnq-concyclic-and-reduction.md`'s Lemma B (round 1,
  certified) already proves `concyclic(A,K,L,Q) ⟹ OM=ON`, and — as I
  independently re-checked — that lemma's own proof is step-for-step
  reversible (every implication used is a genuine biconditional: `O∈ℓ ⟺
  OM=ON` via `vector-reduction-OM-ON.md`; `O∈ℓ ⟺ OA=OQ` since `ℓ` is the
  perpendicular bisector of `AQ`), so the full `iff` was already latent in
  the population's round-1 machinery, merely stated one-directionally
  there (sufficient for its own proof strategy at the time, not because
  the reverse direction is false or harder).

**What genuinely IS new this round:** the alternate, previously-unstated
synthetic **closed-form characterization** of `Q(=P)` as "the foot of the
perpendicular from the circumcenter `O_{ABC}` of `△ABC` onto the line
through `A` parallel to `BC`" — this specific geometric description does
not appear anywhere in `amnq-concyclic-and-reduction.md` or any other prior
round's file (which only gave the reflection-formula / vector definition).
This is a real, if modest, addition — potentially useful for a future
synthetic attack on the concyclicity gap (e.g. via known properties of feet
of perpendiculars from the circumcenter) — but it is **not** "a new fixed
point," and the file's "iff" packaging is a restatement, not new leverage,
of round-1 content.

### Required correction

The file's "Approaches tried" and "Current best" sections present this as
"the round's main new result" (a "second point `P`... independent of `φ`")
without ever mentioning `Q` or citing `amnq-concyclic-and-reduction.md` —
this reads as new content when the underlying target (concyclic-with-a-
fixed-reflection-point ⟺ OM=ON) has been the population's standing
reduction since round 1. **This is not a mathematical error and does not
change the Status (still correctly `partial`, concyclicity still open) —
but it is a real process gap** (CLAUDE.md: "Always read first... build on
prior progress" applies to citing already-certified population content, not
just to avoiding dead ends) that should be corrected in the file next
round: rename `P→Q`, cite `amnq-concyclic-and-reduction.md` explicitly, and
scope the round's genuine contribution precisely to (i) the new closed-form
characterization of `Q` and (ii) the explicit unconditional `iff` packaging
(a legitimate, if modest, clarification of previously implicit content).

### Lemma certification

**Certifying** only the genuinely new content, as a short addendum lemma:
`Q(=P)`, the already-certified fixed point of `amnq-concyclic-and-
reduction.md`, has the closed-form synthetic characterization "foot of the
perpendicular from the circumcenter of `△ABC` to the line through `A`
parallel to `BC`" — written to
`lemmas/q-as-foot-of-perpendicular-from-circumcenter.md`, explicitly
cross-referencing `amnq-concyclic-and-reduction.md` and noting `P≡Q`. **Not
certifying** a new "`fixed-point-P-and-concyclicity-reduction`" lemma as
proposed by the file's own "Promotable lemmas" section, since its content
duplicates the already-certified `amnq-concyclic-and-reduction.md` pair
(Lemma A + Lemma B, both directions) — certifying it separately would
create a redundant, differently-named entry for the same fact, exactly the
"rediscovery, not new content" risk the round-19 dispatch flagged.

### Net assessment

The general one-angle lemma, Lemma A/B, and the `∠BLN+∠CKM≡0` Corollary
(inherited from round 18, independently re-verified there — not re-derived
from scratch this round given time budget, no new claim made about them
this round) remain sound. The round's headline "new" result is correct
mathematics but is **substantially a rediscovery of round-1 content** under
new names, with one genuinely new piece (the closed-form characterization).
Concyclicity of `A,K,L,Q` (the actual load-bearing target, unchanged in
substance since round 1) remains open. Status `partial` is accurate;
verdict `CHANGES REQUESTED`, with the correction above as the concrete next
step (a bookkeeping fix, not new mathematics needed) alongside continued
work on the concyclicity gap itself.

---

## Updates to `results/imo-2026-02/current.md`

Updated (edited in place, preserving all prior round history):
- `## Status`: remains `partial` (population-wide; no route reaches
  `solved` this round).
- `## Approaches tried` / round 19 section added, summarizing both
  adjudications above.
- `## Current best`: updated to record (i) the newly-certified
  `f-positive-on-full-interval.md` lemma and the precise re-diagnosis of
  Open gap 7 (now confirmed identical to the central `−q1,−r0`/`T≥0`
  Positivstellensatz gap, not a citation-scope issue) for
  `-pointwise-tangent`; (ii) the `P≡Q` identification and the requirement
  to correct attribution for `spiral-similarity-bootstrap`, with the
  concyclicity-of-`(A,K,L,Q)` gap (open since round 1) still the load-
  bearing target for that route.

## Lemma certifications this round

- `lemmas/f-positive-on-full-interval.md` (new) — certified, `f(β)>0` on
  all of `[0,γ)`, extending Theorem A of `claim-I-closed-and-claim-II-
  caseA-closed.md`. Explicit caveat included: does NOT close Case (a);
  `G(β1)≥0` (not `f(β1)>0`) is the actually-needed fact there.
- `lemmas/q-as-foot-of-perpendicular-from-circumcenter.md` (new) —
  certified, the closed-form synthetic characterization of the already-
  certified fixed point `Q` (`amnq-concyclic-and-reduction.md`) as the foot
  of the perpendicular from the circumcenter of `△ABC` onto the line
  through `A` parallel to `BC`. Cross-references `amnq-concyclic-and-
  reduction.md` explicitly; notes `P` (as named in `spiral-similarity-
  bootstrap.md`) `≡ Q`.
- **Declined**: `spiral-similarity-bootstrap`'s proposed
  `fixed-point-P-and-concyclicity-reduction` lemma — redundant with the
  already-certified `amnq-concyclic-and-reduction.md` (Lemma A + Lemma B);
  see discussion above.

## Recommendation for round 20

1. **Central shared target, now confirmed load-bearing for TWO independent
   routes simultaneously** (`-pointwise-tangent`'s Case (a) AND the
   long-standing `-boundary`/`-sos` LP/SDP search): the `T≥0`/`−q1,−r0`
   Positivstellensatz certificate. This is now unambiguously the single
   highest-value target in the population — closing it would complete
   `-pointwise-tangent`'s route in full (Case (b) is fully closed; Case (a)
   reduces to exactly this).
2. For `spiral-similarity-bootstrap`: correct the `P→Q` attribution (cite
   `amnq-concyclic-and-reduction.md`), then continue attacking the
   concyclicity-of-`(A,K,L,Q)` gap using the new closed-form
   characterization plus Lemmas A/B (candidate mechanisms already listed in
   the file's own "Open gaps" item 1 remain reasonable next steps: directed-
   angle chase `∠(KA,KL)=∠(PA,PL)`, or power-of-a-point at `B`/`C` anchored
   at the now-characterized `Q`).
