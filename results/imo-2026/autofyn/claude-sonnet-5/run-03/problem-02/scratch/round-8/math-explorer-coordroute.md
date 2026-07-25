## imo-2026-02 (lens: coordinate-bash-resultant-boundary sibling routes' remaining gaps)

### (a) The 3-sinusoid conditional sign inequality (G2b exclusion, §14 of coordinate-bash-resultant-boundary.md)

**Exact statement checked.** With `A=(0,0),B=(a,0),C=(b,cc)`, `u=tan(β/2)`, the certified trig
forms (`lemmas/yb2z-trig-identification.md`) are
`Y/(1+u²)²=2a cos²β−b`, `B₂/(1+u²)³=−2(b sin3β+cc cos3β)`,
`Z/(1+u²)=p₁sinβ+q₁cosβ` with `p₁=b(2a−b)²+cc²(b−4a)`, `q₁=−cc(4a²−b²−cc²)`.
The forbidden pattern is `(Y,B₂,Z)=(+,+,+)`; i.e. the target is
**`Y>0 ∧ B₂>0 ⟹ Z<0`** (I double-checked the sign convention numerically —
my first pass used the wrong sign for `B₂` and got 40%+ "violations"; only
`B₂>0` ⟺ `b sin3β+cc cos3β<0` reproduces the certified 0/200000 result).

**New reduction found this round (numerically corroborated + one piece fully
proved).** Using scale-invariance (all three of `Y,B₂,Z`'s *signs* are
invariant under `(a,b,cc)→λ(a,b,cc)`, `λ>0`, since they are homogeneous of
degrees 1,1,3 resp.), WLOG set `a=AB=1` and write `b=m cosA`, `cc=m sinA`
where `m=AC>0`, `A=∠BAC∈(0,π)`. Then:
- `B₂ = −2m·sin(A+3β)` — a genuinely cleaner **single-sinusoid-in-(A+3β)**
  form, not previously written this way by the population (the file only had
  it as `b sin3β+cc cos3β` in raw `a,b,cc`). So **B₂>0 ⟺ sin(A+3β)<0**.
- `Y>0 ⟺ m < M₀:=2cos²β/cosA` (when `cosA>0`; automatically true for all `m>0`
  when `cosA≤0`).
- `Z`'s sign (dividing out the always-positive factor `AC=m`) reduces to the
  sign of a **quadratic in `m`**:
  `Q(m) = m²sin(A+β) − 4m sinβ − 4sin(A−β)`.
  So the whole conditional inequality becomes: for fixed `(A,β)` with
  `sin(A+3β)<0`, show `Q(m)<0` for every `m∈(0,M₀)` (or all `m>0` if
  `cosA≤0`).

**One piece is now fully, rigorously proved (a genuine new cheap lemma, not
in any certified file yet): `sin(A+β)>0` always, for every valid
`(triangle,β)`** — not just under the `Y>0∧B₂>0` hypotheses, but
unconditionally on the whole geometric domain. Proof: `β<min(∠B,∠C)≤∠B`, so
`A+β<A+∠B<π` (since `∠C>0` and `A+∠B+∠C=π`); also `A+β>0` trivially. Hence
`A+β∈(0,π)`, so `sin(A+β)>0`. **This means `Q(m)` is always an
upward-opening parabola** — a clean, cheap, fully general fact, worth
certifying immediately (it removes one whole case split from any future
attempt: no need to worry about `Q` being concave).

**Remaining numeric-only pieces (3M-sample sweep, own script, this round,
0 exceptions in every check):** with `Q` upward-opening and its two real
roots `r₁≤r₂` (discriminant found `≥0` in 100% of the ~34k
hypothesis-satisfying samples tested — i.e. `Q` always *has* two real roots
under the hypotheses, itself worth checking further as it may follow from
`sin(A+3β)<0` algebraically), the target `Q(m)<0` on `(0,M₀)` decomposes
into: **(i) `m<r₂` always** (i.e. `M₀≤r₂`) — confirmed 100% of ~34k samples;
**(ii) when `r₁>0`** (only ~2.6% of the hypothesis-satisfying samples).
`m>r₁` also always** — confirmed 100% in that subsample. Neither (i) nor
(ii) was proved symbolically this round; each is now a concrete, standalone
"compare `M₀` (resp. `0`) against a quadratic's root" claim rather than an
amorphous 3-sinusoid conditional — a genuinely smaller target than before.

**Attempted and stalled: closed form for `Q(M₀)` at the `Y=0` boundary.**
Substituting `m=M₀=2cos²β/cosA` into `Q(m)` gives (via `sympy`, exact,
`cos²A` cleared from the denominator)
`Q(M₀)·cos²A = 2sinA·cos3β + 4sin⁴β·sin(A+β) + sin(A−β) − sin(3A−β)`,
which did **not** simplify further under `sympy.simplify`/`expand_trig`
in the time available — a concrete open sub-target (try manual
sum-to-product/product-to-sum identities rather than blind `sympy.simplify`,
or avoid eliminating `m` via `M₀` and instead directly compare `Q`'s roots'
symbolic form via the quadratic formula against `M₀` termwise).

**Recommendation on (a):** tractable-looking but not yet closed. The
scale-reduction (3 essential parameters `A,m,β` instead of 4) plus the
fully-proved `sin(A+β)>0` lemma are genuine, reusable simplifications worth
folding into the file next round. The realistic next step is NOT a blind
SOS/Positivstellensatz search (this is a *conditional*, not bare-positivity,
claim) but rather: (1) prove discriminant of `Q` is `≥0` under
`sin(A+3β)<0` symbolically (a single resultant/discriminant computation,
likely tractable — same machinery already used throughout this population);
(2) prove `M₀≤r₂` symbolically (compare `Q(M₀)` sign — need to finish the
stalled simplification above, or compare via `Q(M₀)≤0` together with
`Q`'s leading coeff `>0` and `M₀>` the vertex `−B/(2A)` type argument);
(3) handle the `r₁>0` sub-case, which is empirically rare (2.6% of samples)
and may be dischargeable by a simpler special-case bound. This looks like
2-3 more resultant/sign-lemma steps of the same kind already used to close
§§11-12, not a fundamentally new obstruction — worth prioritizing next
round.

### (b) The G2a same-root ("matched-sign") sub-gap (coordinate-bash-resultant-boundary-pointwise §Round-7)

**Checked whether it's an easy consequence of Theorem 11.8/§12: it is NOT.**
Theorem 11.8 (`lemmas/cross-product-sign-selection-G2a.md`) and §12
(`lemmas/magnitude-bound-and-sign-coincidence.md`) together pin down a
unique root of `G_{2a}` via the AFFINE test function `L₁` (cross-product
sign). The newly-needed condition is `W:=D_K·D_N>0` where `D_K,D_N` are
each affine in `s₂` individually, but their **product** `W` is quadratic —
so this round's file correctly diagnosed that the standard "both-roots
product via resultant" trick (which gave the new, fully proved
`W(r₁)W(r₂)≤0` lemma) cannot resolve a **same-root** (not
both-roots-product) question, and the file's attempted extension (reducing
`L₁·W mod G_{2a}`) produced an unfactorable degree-20 polynomial — a
genuine, correctly-diagnosed dead end for that specific technique. I did
not find a way to shortcut this from already-certified lemmas: it is
genuinely open, not a trivial corollary.

**A structurally new, untried idea worth flagging for next round:** `L₁` and
`D_K` are literally the cross- and dot-products of the *same* two vectors
`(d(β), L−B)` — i.e. if `L−B` is regarded as a complex-affine (in `s₂`)
function `V₁(s₂)`, then `L₁(s₂)=\mathrm{Im}(\overline{d(β)}·V₁(s₂))` and
`D_K(s₂)∝\mathrm{Re}(\overline{d(β)}·V₁(s₂))` are the imaginary/real parts
of a single **complex-affine** function `W₁(s₂):=\overline{d(β)}V₁(s₂)` of
the real parameter `s₂`. As `s₂` ranges over `ℝ`, `W₁(s₂)` traces a straight
line in `ℂ`; the condition "`L₁<0` and `D_K>0`" is exactly "`W₁(s₂)` lands
in the open fourth-quadrant-type region `\{{\rm Im}<0,{\rm Re}>0\}`" —
determined by where this one line crosses the two coordinate axes (which
are exactly the already-known zero loci of `L₁` and `D_K`) and the line's
direction. `D_N` is similarly the real part of a second complex-affine
function `W₂(s₂):=\overline{V_4}V_3(s₂)` (`V₃=L−N` affine, `V₄=C−N`
constant). This reframes the "same-root" correlation as a question about
**two lines in ℂ parametrized by the same real variable `s₂`**, rather than
raw resultant algebra — I did not develop this further (outside explorer
scope) but it looks like a genuinely different lever than the
resultant-ratio trick already tried and found insufficient, worth handing
to the outliner as a concrete new technique to attempt.

**Recommendation on (b):** genuinely open, correctly diagnosed as harder in
kind than the both-roots-product lemmas already closed. Not a cheap kill.
The complex-affine-line reframing above is a plausible new angle; absent
that, the file's own suggested fallback (explicit closed-form roots via the
quadratic formula, with a discriminant-based sign analysis) is the only
other concrete lead on the table. 377+15 independent samples, 0
counterexamples — strong numeric support, no proof.

### Overall recommendation

Neither sub-gap is a cheap kill, but (a) looks meaningfully more tractable
right now: the scale-invariance reduction + the fully-proved `sin(A+β)>0`
lemma + the clean single-sinusoid form of `B₂` are genuine, reusable
progress from this round's exploration, and the remaining pieces ((i)
`M₀≤r₂`, (ii) the rare `r₁>0` sub-case, (iii) discriminant `≥0`) are each a
concrete, bounded computation of the same shape as prior closed lemmas
(§§11-12) rather than a new kind of obstruction. (b) is real but appears to
need a genuinely new technique (same-root, not both-roots-product,
correlation) — the complex-affine-line idea above is the best concrete new
lead found this round, not yet tried by anyone.

### Cheap-kill / structural facts worth certifying immediately (even before either gap closes)
- `sin(A+β)>0` for every valid `(triangle,β)` — fully proved above, 3 lines,
  reusable (makes `Q(m)`'s leading coefficient's sign unconditional).
- `B₂ ∝ -\sin(A+3β)` and `Y ∝ 2\cos^2β - \cos A\cdot(AC/AB)`-type clean
  single-vertex-angle forms — reusable simplification of the existing
  `Y,B₂,Z` trig-identification lemma, makes the whole population's
  displayed formulas one parameter shorter (3 essential params `A,m,β`
  instead of 4 `a,b,cc,β`).

### Knowledge-base / lemma pointers
- `lemmas/yb2z-trig-identification.md` (the base for this round's polar
  reparametrization).
- `lemmas/cross-product-sign-selection-G2a.md`, `lemmas/magnitude-bound-
  and-sign-coincidence.md`, `lemmas/g2b-true-supplementary-parity.md` (the
  templates whose "both-roots-product via resultant" technique closes
  cleanly but does NOT transfer to (b)'s same-root question).
- knowledge_base.md's resultant/discriminant entries remain the right tool
  for closing (a)'s remaining pieces (discriminant sign, quadratic-root
  comparison) — no new KB entry needed, same toolkit already in use.

### Dead ends / non-transfers (do not retry verbatim)
- Do NOT retry the both-roots-product resultant-ratio trick for the (b)
  same-root correlation — already tried this round (degree-20
  unfactorable remainder), confirmed genuinely insufficient for same-root
  (as opposed to both-roots-product) questions.
- Do NOT trust the naive sign convention "B₂<0 forbidden" — the correct
  forbidden pattern requires `B₂>0` (I initially miscoded this and got
  spurious 40%+ violations; the certified 0/200000 result uses `B₂>0`).

### Small-case / intuition notes (all labeled conjecture except where marked PROVEN)
- PROVEN: `sin(A+β)>0` unconditionally on the whole domain.
- Conjecture (100% of ~34k hyp.-satisfying samples): `Q(m)`'s discriminant
  is `≥0` whenever `sin(A+3β)<0` (i.e. `Q` always has two real roots under
  the hypothesis — `Q`'s having no real roots at all would trivially give
  `Q>0` everywhere since leading coeff is positive, contradicting the
  target, so this is actually *necessary* for the target inequality to be
  meaningful/tight — worth checking as a first easy sanity sub-lemma).
- Conjecture (3M-sample sweep, 0 exceptions): `m<r₂` (`Q`'s larger root)
  always, and (in the rarer `r₁>0` case, ~2.6% of samples) `m>r₁` always.
- Conjecture (377+15 independent samples, two independent codebases, 0
  counterexamples): the `L₁<0`-selected root of `G_{2a}` always also
  satisfies `W>0` (the "true equation" / matched-sign condition) — the (b)
  gap.
