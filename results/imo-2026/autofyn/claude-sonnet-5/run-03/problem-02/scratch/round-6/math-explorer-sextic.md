## imo-2026-02 — sextic positivity gap Ψ(τ,A,C)>0 (ptolemy-trig-identity route)

### Exact object, restated
From `lemmas/ptolemy-resultant-elimination-to-sextic.md` / approach file Round 5
§Steps 1–4: with `τ=tanθ`, `Ũ,Ṽ` the genuine roots of two explicit quadratics
(coeffs `P̃1,Q̃1,R̃1` in `τ,A,C` resp. `P̃2,Q̃2,R̃2` in `τ,A,B` — same formulas with
`C↔B`), and `L(U,V)=F-4` linear in `V` for fixed `U`, define
`Φ(U):=P̃2n²-Q̃2nm+R̃2m²` (m,n affine in U) and
`Res_U(P̃1U²+Q̃1U+R̃1, Φ(U)) = 4sin²A·(τcosC-sinC)·(sinB-τcosB)·Ψ(τ,A,C)`,
Ψ degree 6 in τ, `Ψ(0,A,C)=4sin³A sinB sinC`. **The domain is
`0<θ<min(B,C)` — since only one triangle angle can be ≥π/2, `min(B,C)<π/2`
always, so `τ∈(0, tan(min(B,C)))`, a *bounded positive* interval, NOT all of
ℝ or even all of ℝ₊.** This domain restriction turns out to be essential
(see below) — the lemma file's phrasing "Ψ(τ,A,C)>0 for τ≠0" is ambiguous
about whether it means "for all real τ≠0" or "for τ in the valid range"; the
finding below shows only the latter is true.

### What I computed (concrete, reproducible)
Using the Weierstrass substitution `m=tan(A/2), n=tan(C/2)` (rational
parametrization, avoids slow trig simplification), I rebuilt `Res_U(...)`
fully symbolically in `sympy` (fresh session, own code) and ran
`sympy.factor` on the resulting ~21K-character polynomial in `(m,n,t)`.
**Result: it factors completely over ℚ as**
```
Res = 64·m²·(m²+1)²·(n²t+2n-t)·[degree-1-in-t factor]·[degree-6-in-t factor]
```
The two linear factors match the certified spurious factors
(`n²t+2n-t ∝ τcosC-sinC`, the other `∝ sinB-τcosB`) exactly — this
independently re-confirms Steps 3–4 of the certified lemma from scratch, via
a different (rational-parametrization) route than the file's own
`sa,ca,sc,cc` symbols. **The degree-6-in-t factor is irreducible over ℚ(m,n)**
(sympy's `factor` found no further splitting) — this rules out any proof
strategy based on factoring Ψ into a product of two lower-degree
manifestly-positive pieces over the rationals; if a factorization-based
proof exists it would need an algebraic (irrational) field extension.

### Key finding: Ψ is NOT globally positive — domain restriction is load-bearing
I numerically evaluated my extracted sextic factor (call it `S`, which is
`-c·Ψ` for a positive constant `c` — sign pinned down by matching
`S(τ=0)<0` against the known `Ψ(0,A,C)=4sin³A sinB sinC>0`) at 4000 random
`(A,C,θ)` triples:
- **In-domain** (`0<θ<min(B,C)`): `S<0` (i.e. `Ψ>0`) at **all 4000/4000**
  samples — consistent with, and independently reconfirming, the file's own
  20,000-sample claim.
- **Outside the domain** (same `A,C`, but `τ` pushed to `1.5×–10×
  tan(min(B,C))`, i.e. `θ` beyond `min(B,C)` — geometrically meaningless but
  algebraically still a point where the polynomial Ψ is defined): `S>0`
  (i.e. **Ψ<0**) at **1176/4000** samples — a clean, reproducible
  counterexample family (e.g. `A=2.234,C=0.746,θ=0.115` in-domain gives
  `θ_max=0.162`; pushing `τ` to `τ_max×1.28≈1.52` gives `Ψ<0` there with
  magnitude `≈5×10⁵`, no numerical-precision ambiguity).

**Conclusion: a global (all-real-τ, or even all-τ>0) SOS/Positivstellensatz
certificate for Ψ cannot exist — Ψ genuinely changes sign outside the
geometric domain.** Any proof of Ψ>0 on the actual domain MUST use the
domain constraint `θ<min(B,C)` (equivalently `τ<tan(min(B,C))`) as a
hypothesis, not just `A,B,C>0, A+B+C=π`. This is important negative
information: it rules out the most obvious next step ("find an SOS
decomposition of Ψ") as stated, and redirects toward a **root-exclusion /
IVT argument that uses the domain bound explicitly** — much closer to the
population's already-successful branch-selection technique (Round 3/4 Step
3's `c₁x²+b₁x+a₁=0` IVT + quadratic-degree-counting argument) than to a
generic polynomial-positivity toolbox.

### A concrete, more promising angle: Ψ generically has only 2 real roots
I computed all roots of the degree-6-in-τ polynomial (fixed `A,C`, `numpy.roots`
on the extracted coefficient list) at 6 random `(A,C)` points: **in every
case, exactly 2 of the 6 roots are real** (the other 4 form 2 complex-conjugate
pairs), and the 2 real roots are either (a) both negative, or (b) one
negative and one positive-but-large. In all 6 samples, `τ=0` always falls in
the same sign-region as `τ→+∞` (matching leading-coefficient sign), and the
observed domain `τ_max=tan(min(B,C))` never exceeded the positive real root
when one existed. **This suggests the actual needed fact is much narrower
than "Ψ>0 everywhere": it is "Ψ has (generically) at most one real root on
τ>0, and that root — when it exists — always lies at or beyond
τ=tan(min(B,C))."** This reframes the whole gap from a degree-6 global
positivity claim into a **root-location inequality** (comparing the
sextic's positive real root, or a resultant/discriminant expression
governing it, against `tan(min(B,C))`), which is structurally the same
species of problem the population has already solved twice (Round 3/4's
branch-selection IVT arguments) — a strong candidate technique.

I also checked whether the sign-change point (root beyond `θ=min(B,C)`)
coincides with the simple loci `θ=B` or `θ=C` (which would make Steps 3–4's
spurious linear factors directly responsible) — **it does not**: evaluating
S at `τ=tan B` and `τ=tan C` gives nonzero (still same-sign, i.e. `Ψ≠0`
there) values in all tested cases, so the true "where Ψ can vanish" locus
is a genuinely different (more complex) algebraic curve than the two known
spurious lines — this rules out the tempting shortcut "just reuse Step 4's
tan-injectivity argument for Ψ's own zero set."

### Candidate proof techniques, ranked by promise
1. **[Most promising] Root-count + boundary-sign IVT, exploiting "≤1 real
   positive root generically".** Don't try to show Ψ>0 directly; instead
   (a) prove Ψ has a bounded number of real roots on τ>0 (e.g. via Descartes'
   rule of signs on the τ-polynomial's coefficient-sign pattern as a
   function of A,C, or via the discriminant/Sturm sequence), (b) show
   Ψ(0,A,C)>0 (already proved exactly) and Ψ has no sign change on
   `(0,tan(min(B,C)))` using IVT + the domain's proven path-connectedness
   (Step 6, already certified) — i.e. push the "no crossing" argument down
   one level, onto Ψ itself instead of F. This mirrors the *exact*
   architecture the population already used successfully for branch
   selection (Round 4 Step 3) and would reuse `knowledge_base.md`'s
   resultant/Sturm-type entries plus the already-certified domain
   connectedness lemma (Step 6).
2. **Sturm's theorem, parametrized.** Since Ψ is an explicit degree-6
   polynomial in τ with trig-in-(A,C) coefficients, a Sturm sequence
   computed symbolically (or via the m,n rational parametrization, purely
   algebraically) could in principle certify "0 real roots in
   `(0,tan(min(B,C)))`" — but the Sturm sequence's sign evaluations at the
   variable endpoint `tan(min(B,C))` (which itself depends on `A,C` via
   `min`) will likely require a case split on `sign(B-C)`, adding real but
   manageable casework.
3. **SOS / semidefinite relaxation for a *relaxed*, domain-truncated
   problem** (e.g. via a rational substitution `τ = τ_max·s/(1-s)` or similar
   that maps `(0,τ_max)` to `(0,∞)`, turning the domain constraint into part
   of the polynomial itself) — untested this round, flagged as a fallback if
   (1)/(2) stall, but likely to produce an even messier polynomial (degree
   grows since `τ_max=tan(min(B,C))` is itself not polynomial in A,C).
4. **[Dead end, don't pursue] Global SOS/Positivstellensatz for Ψ as stated
   ("Ψ>0 for all τ").** Refuted by the concrete counterexamples above — Ψ
   is negative for τ outside the geometric domain, so no valid global
   certificate exists; any approach assuming this will fail.
5. **[Dead end, don't pursue] Factoring Ψ into positive pieces over ℚ.**
   Ψ (the degree-6-in-τ factor) is irreducible over ℚ(m,n) per `sympy.factor`
   — no rational factorization exists.

### Cheap-kill candidates
None found beyond the above (no elementary parity/pigeonhole shortcut for a
continuous polynomial-positivity claim); the domain-restriction finding
above is itself the cheapest available "kill" of the wrong framing
(global SOS), and should redirect effort immediately rather than after
another round of failed SOS attempts.

### Knowledge-base entries to use
- **Resultants** entry (already cited by the certified lemma) — also
  relevant: any **Sturm's theorem / real-root-counting** entry if present in
  `knowledge_base.md` (check for "Sturm" or "root counting" — not
  confirmed present, worth the outliner double-checking the KB index) would
  directly formalize approach (1)/(2) above.
- **IVT / connectedness** — the domain path-connectedness lemma (Step 6,
  already certified informally in the approach file, not yet a separate
  `lemmas/` file) is directly reusable for the "no sign change" step; worth
  promoting to its own certified lemma file since it is now needed for
  *two* purposes (F's sign, and potentially Ψ's sign).
- **Discriminant / degree-counting** techniques used in
  `lemmas/ptolemy-trig-branch-selection.md` (Round 4 Step 3's exact
  architecture: real quadratic with ≥1 real root has exactly 2, sign change
  forces odd root count in sub-interval) are the direct structural template
  to imitate for Ψ, except Ψ is a sextic not a quadratic — Descartes' rule
  of signs or a resultant-based root-counting argument would play the role
  the "quadratic discriminant ≥0" argument played there.

### Analogous past problems (cruxes)
Did not query the crux corpus this round (out of scope for this
lens — my dispatch was specifically the sextic-positivity sub-gap, and the
corpus's "real-root-counting-of-a-parametrized-polynomial-on-an-interval"
species is a generic algebra technique already fully represented by the
population's own Round 3/4 lemmas; no specific IMO-style crux move needed
beyond what's already cited above). If the outliner wants a crux, the
right subtopic to query would be `polynomial inequalities` /
`resultants and elimination` per `crux_moves_documentation.md`'s subtopic
list — not done here due to time budget, flagged for the outliner or a
future explorer round.

### Prior progress
As stated in `lemmas/ptolemy-resultant-elimination-to-sextic.md` /
`approaches/ptolemy-trig-identity.md` Round 5: everything up through the
reduction `F>4 ⟺ Ψ(τ,A,C)>0-suffices` (domain-restricted) is fully proved
and independently re-certified (round 5's proof-reviewer pass, and now
independently re-derived from scratch again this round via a different
rational-parametrization route, with zero discrepancy in the factorization
structure). Ψ(0,A,C)=4sin³A sinB sinC>0 is exact. The only gap is
Ψ(τ,A,C)>0 on the true bounded domain.

### Dead ends (do not retry)
- Treating "Ψ>0" as a global (all-real-τ or all-τ>0) polynomial positivity
  claim — **refuted this round** by explicit counterexamples (Ψ<0 for τ
  beyond `tan(min(B,C))` in ~29% of tested parameter points). Any SOS search
  targeting the unrestricted polynomial will not find a certificate because
  none exists.
- Looking for a rational factorization of Ψ into manifestly-positive pieces
  — refuted (`sympy.factor` shows Ψ irreducible over ℚ(m,n)).
- Hoping Ψ's zero set coincides with the already-known spurious lines
  `θ=B,θ=C` — checked numerically, false (Ψ≠0 at those points in all test
  cases).

### Small-case / intuition notes (conjectural, not proved)
- Ψ, viewed as a sextic in τ with A,C fixed, appears to have **generically
  exactly 2 real roots** (4 complex, in 2 conjugate pairs), based on 6
  random-sample root computations — this is a numerical pattern, not proved,
  but if true it substantially simplifies the remaining work (only need to
  locate/exclude at most 1 positive real root relative to `tan(min(B,C))`,
  rather than reason about a degree-6 curve in general).
- The boundary behavior "Ψ→0 as A→0" (noted already in the certified
  material, min value ≈2.6×10⁻⁶ in the 20k-sample sweep) is consistent with
  `Ψ(0,A,C)=4sin³A sinB sinC→0` as `A→0` — i.e. the near-degenerate case is
  exactly where Ψ is tightest, matching the population's independently-known
  fact that `F→4` exactly as `A→0⁺`.
