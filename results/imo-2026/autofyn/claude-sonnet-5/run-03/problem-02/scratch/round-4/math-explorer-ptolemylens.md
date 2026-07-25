# math-explorer report — "ptolemy lens" (round 4, imo-2026-02)

Scope: (a) hunt for a synthetic/algebraic proof of `∠BAK < ∠BAL`, the
single open gap in `ptolemy-trig-identity`; (b) determine precisely what
happens to the whole problem when `AB=AC`. Not a builder — no proof
written to the approach file.

## (a) The `∠BAK<∠BAL` inequality

**New simplification found (exact, not numerical).** Substituting (III)
into (I) (i.e. using the *proved* relation `R(θ,ψ) = sinψ/(2 sin(θ+ψ))`,
which follows algebraically from Lemma 3's (III), into Lemma 2's
`tanα = R sinθ/(1−R cosθ)`) collapses to the clean closed form

```
tan α = sinθ sinψ / (2 sinθ cosψ + cosθ sinψ)  =  tanθ tanψ / (2 tanθ + tanψ)
```

equivalently, dividing through:

```
cot α = cot θ + 2 cot ψ          (exact identity, sympy-verified)
```

and symmetrically `cot α' = cot θ + 2 cot φ` (α′:=∠CAL, so β_L=A−α′).
Verified symbolically with sympy (`sympy.simplify`/`trigsimp` on the
difference, both directions, = 0 identically) — this is a genuine new
closed-form simplification, not in the approach file yet, and is a clean
candidate to hand to the builder: it turns "∠BAK<∠BAL" into "cotθ+2cotψ
compared against cot(A − arccot(cotθ+2cotφ))", i.e. it isolates the whole
problem into understanding `ψ(θ)` vs `φ(θ)` (the two decoupled
transcendental equations (III), (IV)) and nothing else — `α, α'` no
longer need to be tracked separately once this substitution is made.

**Tried and failed to close it further this session:**
- Checked whether `ψ<φ` (or any fixed sign) always holds, hoping it would
  directly force the inequality via the cot identity. **Numerically
  false** — sign of `ψ−φ` flips between triangles (confirmed on 5 distinct
  triangles × 6 θ values, `check2.py`): e.g. triangle `A=1.0,B=1.2,C=0.942`
  has `ψ<φ` throughout, but `A=0.5,B=1.0,C=1.642` has `ψ>φ` throughout.
  So a naive "compare ψ,φ directly" route does **not** work; whatever
  forces the inequality must use the *specific* asymmetric dependence of
  ψ on `(A,C)` and φ on `(A,B)` via (III)/(IV), not just their sign
  relative to each other.
- Did not find a monotonicity-in-θ argument or a derivative-sign proof in
  the time available — this needs someone to actually invert or bound
  (III)/(IV) (e.g. show ψ(θ) is bounded above/below by some explicit
  function of θ,A,C that composes cleanly with the cot identity).

**Recommendation for next builder:** hand off the `cotα=cotθ+2cotψ`
identity (cheap, exact, sympy-checked in `/tmp/check1.py` logic above) as
a starting point — it strictly reduces the target to a statement purely
about `ψ(θ)` vs `φ(θ)`, which is one transcendental-equation-comparison
away from closing, not a 4-variable mess. This is real narrowing but the
inequality itself is still open — do not report it as closed.

## (b) The isosceles case `AB=AC` — NOT a genuine separate difficulty; free proof found

This is the headline finding. **When `AB=AC` (equivalently `B=C` as
angles), the entire family of valid configurations is forced to be
mirror-symmetric, and `OM=ON` follows immediately from reflection
symmetry — completely bypassing Q, Ptolemy, and the central identity.**

Reasoning:
1. `AB=AC` forces `∠B=∠C` (standard). The two decoupled constraint
   equations from `ptolemy-trig-identity`'s Lemma 3 are: (III) in `θ,ψ`
   depending on `(A,C)` only, and (IV) in `θ,φ` depending on `(A,B)` only.
   When `B=C`, (III) and (IV) become the **identical equation** (same
   coefficients), each solved (per the file's own root-finding, single
   root in the valid bracket) by the same value. So **`ψ=φ` for every
   valid `θ`** — confirmed both symbolically (equations become
   syntactically identical after substituting `B=C`) and numerically to
   machine precision (`/tmp/check3.py`: `A=1.0, B=C=(π−1)/2`, 6 values of
   θ, `ψ−φ` = 0.00e+00 at every one).
2. Given `ψ=φ` and `b=c` (from `AB=AC`), Lemma 2's closed forms
   `AK = c sinθ/sin(θ+α)`, `AL = b sinθ/sin(θ+α')` and the (now-derived)
   `cotα=cotθ+2cotψ`, `cotα'=cotθ+2cotφ` force `α=α'` and `AK=AL` exactly
   — i.e. **`K` and `L` are reflections of each other across the
   perpendicular bisector of `BC`** (which, since `AB=AC`, passes through
   `A` — the triangle's own axis of symmetry). This is the geometric
   content of the well-known `σ`-symmetry (swap `B↔C,K↔L,M↔N`) becoming an
   *actual* isometry rather than just an abstract relabeling, precisely
   because the ambient triangle itself is symmetric.
3. Consequences, with **no reference to Q**: the reflection across this
   axis fixes `A`, swaps `B↔C` hence `M↔N`, and swaps `K↔L`. Hence it maps
   circle(`A,K,L`) to circle(`A,L,K`) — the same circle — so its center
   `O` is a fixed point of the reflection, i.e. `O` lies on the axis.
   Since the reflection is an isometry sending `M↦N` and fixing `O`,
   `OM = O(refl(M)) `... more directly: `d(O,M) = d(refl(O),refl(M)) =
   d(O,N)`. **`OM=ON` immediately.**

This is a genuinely free, self-contained proof of the isosceles case,
independent of resolving branch selection or the `∠BAK<∠BAL` gap, and it
does not hit the `Q=A` degeneracy at all (Q is never used). The only
things it needs, which look routine but should be stated explicitly by
whichever approach writes this up:
- `A,K,L` non-collinear (so the circumcircle exists) — should follow from
  genericity/containment (`K,L` interior to `BMC,BNC` resp.), same as
  elsewhere in the population.
- Uniqueness of the root of the (III)/(IV)-type equation in the valid
  bracket (used to conclude `ψ=φ` rather than merely "some solution
  equals some solution") — the existing numerics (brentq single-root
  search in a bracket already used throughout `ptolemy-trig-identity`)
  supports this but a rigorous monotonicity argument for existence/
  uniqueness of the root on that bracket has not itself been written out
  by any approach; likely easy (the LHS and RHS of (III) are each
  monotonic pieces on the relevant sub-interval) but should be confirmed,
  not assumed.

**Bottom line:** the isosceles case is not a genuine hard sub-case
requiring the main machinery — it has a two-line symmetry proof once you
note `ψ=φ` is forced. Recommend the next round have a builder write this
up formally as its own short self-contained lemma/appendix (reusable by
*any* approach, not just `ptolemy-trig-identity` — the mirror-symmetry
argument for `K,L` under `B=C` is a general fact about the configuration,
not specific to the Ptolemy route) and close the "isosceles case
unaddressed" flag that has persisted since round 1.

## Files/scripts used (for reproducibility, not committed)
- `/tmp/check1.py` — sympy verification of `cotα=cotθ+2cotψ`.
- `/tmp/check2.py` — numeric sweep testing sign(ψ−φ) vs sign of the target
  inequality across 5 triangles.
- `/tmp/check3.py` — numeric confirmation `ψ=φ` exactly when `B=C`.
