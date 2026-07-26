# Proof-reviewer — IMO 2026 P5 (imo-2026-05), round 1

Problem. Determine all `f : R_{>0} → R_{>0}` with `sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y))` for all x,y>0.
Conjectured answer: `f(x) = x + c`, `c ≥ 0`.

I independently re-derived every load-bearing identity/estimate with sympy and small cases. Verdicts below are per approach.

---

## 1. `diagonal-diophantine-kill` — Status: **solved**

### Independent verification of the load-bearing steps

- **Lemma 1 (diagonal collapse).** Substituting `x = f(y)` makes the outer pair `(x, f(y))` equal; QM=AM=GM collapse to `f(y)`, forcing `(f(f(y))+y)/2 = f(y)`, i.e. `f(f(y)) = 2f(y) − y`. ✓. Recurrence `a_{n+1}=2a_n−a_{n−1}`, characteristic `(r−1)²`, gives `fⁿ(y) = y + n·g(y)`; `g(f(y))=g(y)` (orbit-invariance). ✓. Positivity of all iterates forces `g ≥ 0`. ✓.
- **Lemma 2 identities (I),(II).** Verified symbolically: `L+R = 2(x−f(y))²`, `L−R = 2(g(y)−g(x))(x+f(y)+f(x)+y)`. The factor `x+f(y)+f(x)+y = 2x+2y+g(x)+g(y) > 0` unconditionally. ✓.
- **Lemma 3 master bound (★).** The equivalence `a,b ≥ 0 ⇔ a+b ≥ 0 ∧ |a−b| ≤ a+b` is elementary (the backward direction: `−(a+b) ≤ a−b ≤ a+b` ⟹ `−2a≤0, −2b≤0`). Applied with `a=L, b=R` and (I),(II) gives `|g(x)−g(y)|·(2x+2y+g(x)+g(y)) ≤ (x−y−g(y))²`. ✓.
- **Section 2 substitution.** `x = a+nd₁, y = b+md₂`, `g(x)=d₁, g(y)=d₂`, gives `(d₂−d₁)(2a+2b+d₁+d₂+2nd₁+2md₂) ≤ (a−b+nd₁−(m+1)d₂)²`. LHS → +∞ as `n,m→∞` (since `d₁,d₂>0`); RHS to be driven to 0 (irrational) or to a constant `(a−b)²` (rational). ✓.
- **Lemma 4 (nonneg-grid Kronecker).** For irrational `α>0`, `{nα−m : n,m∈Z_{≥0}}` is dense in R with arbitrarily large witnesses. Sound: pick target `T`, `ε>0`, lower bound `M`. Kronecker gives arbitrarily large `k` with `{kα}` close to `{T}`. Set `n=k, m=⌊kα⌋−⌊T⌋`. For `k` large, `m ≥ 0` and `m → ∞` (since `α>0`). `|nα−m−T|<ε`. ✓. Applied with `α=d₁/d₂` and `T=(b−a)/d₂+1`, RHS of (★★★) → 0, LHS → +∞, contradiction. ✓.
- **Rational case (Frobenius/exact-zero lattice point).** `d₁/d₂=p/q` lowest, `p<q`, `p≥1`. `n=kq, m=kp−1`. For `k≥1`, `m=kp−1≥0`. `nd₁−(m+1)d₂ = k(qd₁−pd₂)=0`. RHS = `(a−b)²` constant, LHS → +∞. Contradiction. ✓.
- **Edge case `d₁=0 < d₂`.** Lemma 5 (continuity at zero): set `y=a` (g(a)=0) in ★: `g(x)(2x+2a+g(x)) ≤ (x−a)²`. For `|x−a|<a/2`, `2x+2a+g(x) ≥ 3a`, so `0 ≤ g(x) ≤ (x−a)²/(3a) → 0`. ✓. The dichotomy (sub-case (i) vs (ii)) is exhaustive: negation of "every neighbourhood has a positive value" is "g≡0 on some interval". 
  - Sub-case (i): pick `x_n→a, g(x_n)>0`; continuity gives `g(x_n)→0`, so eventually `0<g(x_n)<d₂`; reduce to Section 2. ✓.
  - Sub-case (ii): `I_max=(α,β)` maximal zero-interval, `0≤α<a<β≤∞`. Claim `β<∞`: if `β=∞`, `g≡0` on `(α,∞)`, but `b` (with `g(b)=d₂>0`) must satisfy `b≤α`; the forward orbit `b+nd₂→∞` enters `(α,∞)`, where `g=0` by assumption but `=d₂` by invariance — contradiction. (When `α=0`, `b≤0` directly contradicts `b>0`, so `β=∞` is still impossible.) ✓. Claim `g(β)=0`: take `y∈(α,β), x=β` in ★, let `y→β⁻`; `g(β)(4β+g(β)) ≤ 0`, forcing `g(β)=0`. ✓. Claim g not identically zero on any `(β,β+ε)`: maximality. ✓. Then `x_n→β⁺` with `g(x_n)>0` exists (g≥0, not identically zero); continuity at the zero `β` gives `g(x_n)→0`; reduce to Section 2. ✓.
  - I specifically checked the potential circularity flagged in the dispatch: continuity-at-a-zero uses the `O(h²)` case of (★) (Lemma 5), which is a *separate, valid* local estimate — NOT the main Diophantine kill. The reduction to the main kill uses only the *conclusion* of Lemma 5 (small positive displacement exists), then hands two strictly-positive displacements to Section 2. No circularity.
- **Construction.** Verified: `f(x)=x+c` gives `L=R=(x−y−c)²` (sympy-confirmed); the chain is exactly QM≥AM≥GM on `(x,y+c)`. Codomain forces `c≥0`. ✓.

No gaps. All cases settled, all lemmas proved from scratch, tools named (Kronecker/Weyl equidistribution, Frobenius/exact-zero lattice, QM-AM-GM, SOS/completing the square), final answer verified. The `d₁=0` edge fix is sound.

### Promotable lemmas (certified)
- **diagonal-collapse** (`f(f(y))=2f(y)−y`, `g≥0`, orbit-invariance `fⁿ(y)=y+ng(y)`). sorry-free, statement correct. ✓ admit.
- **lr-identities** (`L+R=2(x−f(y))²`, `L−R=2(g(y)−g(x))(x+f(y)+f(x)+y)`). ✓ admit.
- **master-bound** (`|g(x)−g(y)|·(2x+2y+g(x)+g(y)) ≤ (x−y−g(y))²`). ✓ admit.
- **nonneg-grid-kronecker** (density of `{nα−m}` with large witnesses for irrational `α`). ✓ admit.
- **continuity-at-zero** (`g(a)=0 ⇒ g→0`). ✓ admit.

VERDICT: **APPROVE**

---

## 2. `lipschitz-connectedness` — Status: **solved**

### Independent verification

- §1 diagonal collapse, §2 master bound (★): same as approach 1, verified above. Identities sympy-confirmed.
- **§3 limit at infinity.** For `a≥b`, lattice `b_m=b+mβ` (`m≥0`) covers `[b,∞)` with spacing `β`, so nearest `b_m` is within `β/2` (one-dimensional pigeonhole / Dirichlet; cited as "Three-gap/Steinhaus" but the 1-D case is elementary pigeonhole — citation slightly over-named but the result is the standard nearest-lattice-point bound). Apply ★ with `x=a, y=b_m, g(y)=β`:
  `|g(a)−β|(2a+2b_m+g(a)+β) ≤ (a−b_m−β)²`.
  Set `e=a−b_m`, `|e|≤β/2`: RHS `=(e−β)² ≤ (3β/2)² = 9β²/4`. ✓.
  LHS factor: `b_m=a−e ≥ a−β/2`, so `2a+2b_m+g(a)+β ≥ 2a+2(a−β/2)+0+β = 4a`. ✓.
  Hence `|g(a)−β| ≤ 9β²/(16a) → 0`. ✓. Constant 9/16 confirmed.
- **§4 value set ⊆ {0,β}.** If `g(y₀)=δ>0`, the orbit `y₀+nδ→∞` carries `g=δ` (invariance); §3 forces `g→β` along this subsequence, so `δ=β`. ✓.
- **§5 openness of Z.** At `a∈Z` (g(a)=0), ★ with `y=a, x=a+h`, `|h|<a/2`: factor `≥3a`, so `g(a+h) ≤ h²/(3a)`. For `|h|` small, `h²/(3a)<β`, so `g(a+h)∈{0,β}` forces `g(a+h)=0`. Z open. ✓.
- **§5 openness of P (the key claim).** At `b∈P` (g(b)=β>0), ★ with `y=b, x=b+h`:
  `|g(b+h)−β|(2(b+h)+2b+g(b+h)+β) ≤ (h−β)²`. (∗)
  Suppose `g(b+h)=0`: `β(4b+2h+β) ≤ (h−β)²=h²−2βh+β²`, i.e. `4βb+4βh ≤ h²`, i.e. `Q(h):=h²−4βh−4βb ≥ 0`. Algebra confirmed.
  `Q(0)=−4βb<0`; roots `2β±2√(β²+βb)`, smaller `<0` (since `√(β²+βb)>β`), larger `>0`. So `Q<0` on the open interval `(2β−2√(β²+βb), 2β+2√(β²+βb))` containing 0. The check `2β−2√(β²+βb) > −b` reduces to `0<b²`. ✓. So `b+h>0` throughout, and `g(b+h)=β` on this neighbourhood. P open. ✓.
  This is the bypass the dispatch flagged: it does NOT prove continuity at a β-point directly; it uses the discrete value set `{0,β}` plus the quadratic-sign argument `Q(0)<0`. The bound (∗) used at a β-point IS correctly derived from ★ (it is just ★ with `y=b`). The quadratic-sign argument correctly rules out an interval of `h`-values around 0, not merely a single point: `Q<0` on a whole open interval. ✓. No circularity, no hand-waving.
- **Connectedness close.** `(0,∞)` connected; `Z∪P=(0,∞)`, both open, disjoint; one empty; P nonempty (contains b); so Z empty, `g≡β`. ✓.
- **Construction** verified (same QM-AM-GM on `(x,y+c)`), `c≥0` forced by codomain. ✓.

No gaps. Tools named (QM-AM-GM, SOS, Dirichlet/pigeonhole, connectedness/clopen-partition). The make-or-break continuity-at-nonzero gap is genuinely closed by the open/open+connectedness route.

### Promotable lemmas (certified)
- **master-bound** — same as approach 1. ✓ admit.
- **diagonal-collapse** — same. ✓ admit.
- **orbit-recurrence-limit-at-infinity** — `g(b)=β>0 ⇒ g(a)→β`, with the `9β²/(16a)` bound. sorry-free, statement correct (no stronger than proved). ✓ admit.

VERDICT: **APPROVE**

---

## 3. `swap-cross-inequalities` — Status: **partial** (correctly self-assessed)

### Verification

- **Lemma 1 (cross-inequalities), non-circular.** `A=(f(x)+y)/2` is the AM of `(y, f(x))`, so by the universal QM-AM-GM chain `A∈I₂=[√(yf(x)), √((y²+f(x)²)/2)]` — no hypothesis on f. The problem's hypothesis puts `A∈I₁=[√(xf(y)), √((x²+f(y)²)/2)]`. So `A∈I₁∩I₂`; the single witness `A` gives `G₁≤A≤Q₂` (so `G₁≤Q₂`, i.e. `2xf(y)≤y²+f(x)²`) and `G₂≤A≤Q₁` (so `2yf(x)≤x²+f(y)²`). Non-circular: the upper bound `A≤Q₂` is universal QM≥AM on `(y,f(x))`, NOT the swapped left hypothesis. ✓. Genuine lemma.
- **Lemma 2 (local control at a zero).** Cross-ineq (II) with `y=b, g(b)=0`: `2b·f(x) ≤ x²+b²`, i.e. `g(x) ≤ (x−b)²/(2b)` — recovers the ★-at-a-zero local bound. ✓.
- **Dead-end diagnosis (gap b).** Verified symbolically: degree-2 part of single-cross slack on orbits is `(nd₁−md₂)²` (perfect square, AM-GM level); summed slack degree-2 part is `2(nd₁−md₂)²`. Both ≥0 everywhere — asymptotic identity, no growth contradiction. The structural reason (cross-inequality has no amplifying linear factor, unlike ★'s `2x+2y+...`) is correctly identified. The local two-sided bound at nonzero points yields only boundedness (`g(x) ≤ α+α²/(2a)`), not a squeeze. ✓. Clean partial / dead-end.

This is a legitimate `partial`: a correct, proven, non-circular lemma (Lemma 1) plus a correctly-diagnosed dead end. The Status `partial` matches reality. The "Full proof" section is honestly absent (as it must be).

### Promotable lemma (certified)
- **cross-inequalities** — `2xf(y)≤y²+f(x)²` and `2yf(x)≤x²+f(y)²`, proven non-circularly. sorry-free, statement correct, explicitly flagged as too weak to force constancy of `g`. ✓ admit (as a derived inequality, with the caveat the builder already noted).

VERDICT: **CHANGES REQUESTED** (Status partial — gap b is a genuine dead-end, not closeable within this framing; the route must import the master bound (★) or a continuity/connectedness argument, at which point it collapses into approaches 1/2). The honest self-assessment is correct; the lemma is the contribution.
