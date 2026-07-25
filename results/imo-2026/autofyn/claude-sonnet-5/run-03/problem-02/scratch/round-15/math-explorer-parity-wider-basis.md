## imo-2026-02

Lens: WIDER PARITY-GUIDED BASIS SEARCH for the -q1,-r0 Positivstellensatz certificate
(coordinate-bash-resultant-boundary route). All computation below is fresh sympy/numpy
work this round, reproducing/checking round 13-14's lemmas first, then extending.

- Distinct openings (candidate wider bases, all backed by actual computation):
  1. **New degree-6 sign-definite "cross-product" candidates** — instead of only
     bare-c/d multipliers (ct, sd) times a single generator, take PRODUCTS of two of
     the odd-graded generators directly: `G0*Enum`, `G0*Num`, `Enum*Num`. Because
     G0, E_num, Num each live purely in R_10⊕R_01 (round 13's grading), a product of
     two of them automatically lands in R_00 (the "even" graded piece) with NO extra
     bare-c/d multiplier needed — this is a genuinely different (and cheaper) way to
     get into the target's graded piece than the round-13/14 (ct,sd)-multiplier
     recipe. Computed exactly (own sympy, projector `f_00=1/4 Σ f(±c,s,±d,t)`,
     reduced mod the Pythagorean ideal, rewritten in σ=sin²A,τ=sin²B):
     ```
     (G0*Enum)_00   = (σ-1)(128σ²τ³-224σ²τ²+120σ²τ-16σ²-56στ³+70στ²-24στ+2τ³-τ²)   [deg 6]
     (G0*(-Num))_00 = (σ-1)(32σ²τ³-56σ²τ²+30σ²τ-4σ²-6στ²+3στ+2τ³-τ²)                [deg 6]
     (Enum*Num)_00  = (σ-1)(512σ⁴τ³-768σ⁴τ²+288σ⁴τ-16σ⁴-480σ³τ³+576σ³τ²-156σ³τ+16σ³
                            +88σ²τ³-24σ²τ²-24σ²τ-22στ³+9στ²+τ³)                     [deg 8]
     ```
     These are degree 6, 6, 8 respectively in (σ,τ) — degree-6 is an EXACT match
     to q1's own total degree (deg 6), no monomial padding needed at all, which is
     structurally cleaner than the previously-tried B1..B6 (degree 3/3/5/5/5/5,
     always needing a padding monomial).
  2. **Sign-definiteness verified on the TRUE (curved) residual domain, not just the
     loose bounding box.** Sampled the actual domain `{G0>0}∩{Enum<0}∩{c≥2t²-1}∩
     {Num<0}` via rejection sampling on (A,B) (4M draws → 8729 genuine domain points,
     σ∈(0.156,0.261), τ∈(0.625,0.785), matching round 13/14's reported windows
     closely — good cross-check). On this true domain:
     - `G0*Enum > 0` always (min 0.0277, max 0.107) — **sign-definite**.
     - `G0*Num > 0` always (i.e. `G0*(-Num) < 0` always, min -0.078, max -0.012) —
       **sign-definite**.
     - `Enum*Num > 0` always (min 0.0075, max 0.058) — **sign-definite**.
     All three are genuinely new usable positive building blocks, degree-matched (or
     nearly so) to q1, not previously flagged as candidates in the population (round
     13 tested `G0*(-Num)` only for proportionality to q1/r0, found not proportional,
     but never checked it — or the other two products — as sign-definite BUILDING
     BLOCKS for a linear combination).
  3. Re-confirmed **B3, B5 (the mixed-sign basis elements from round 14) remain
     genuinely mixed-sign even on the TRUE curved domain**, not merely on the loose
     box as round 14 suspected might be the issue — B3 ranges (-0.156,0.133), B5
     ranges (-0.115,0.089) on the actual 8729-point domain sample. So restricting to
     the true domain does NOT rescue B3/B5 as usable positive terms; any certificate
     using them needs a genuine compensating combination or case split, not just a
     tighter domain.

- Candidate technique(s): Positivstellensatz / linear-certificate search over an
  extended graded basis {B1, -B2, B4, B6, G0·Enum, G0·Num, Enum·Num} (all verified
  sign-definite on the true domain) plus σ,τ-monomial multipliers; also tested the
  standard "multiply the target by a known-positive slack quantity" trick
  (σ, τ, 1-σ, 1-τ are all trivially positive on (0,1)) to shift degree/rank.

- Cheap-kill candidates / actual negative findings from this round's exact linear
  algebra (LP feasibility via scipy.linprog + sympy rank tests, exact rational
  monomial-coefficient matching, not numeric fitting):
  - Using ONLY the degree-matched sign-definite set {B1,-B2,B4,B6,G0Enum,G0Num} with
    σ,τ-monomial multipliers padded to degree 6: **-q1 is not even in the UNSIGNED
    linear span** (rank A=20 < rank[A|b]=21) — this generator set is structurally
    too small, confirming a genuinely wider search is needed (not just a sign
    search on the existing set).
  - Adding B3, B5 back in (mixed sign, but as unsigned basis elements) makes
    **-q1 still not in the unsigned span at degree 6** (rank 21 vs 22) — so even the
    FULL round-13/14 6-element basis plus the two new degree-6 products together
    still can't reach q1 by simple monomial combination at matched degree.
  - Multiplying the target by a known-positive slack: **-q1·(1-σ) and -q1·(1-τ)
    (both trivially ≥0 multipliers) DO land in the unsigned span at degree 7** using
    the 9-generator set {B1,-B2,B3,B4,B5,B6,G0Enum,G0Num,EnumNum} — but the
    nonnegativity-constrained LP is still **infeasible** for both. This is a genuine,
    exact (not numeric-fit) negative result: the natural "multiply by 1-σ or 1-τ"
    Positivstellensatz trick does not immediately unlock positivity with this
    generator set, but DOES fix the span-rank obstruction — worth trying other
    positive multipliers (τ(1-σ), σ(1-τ), (ct-sd) itself if provably positive, etc.)
    with the same 9-generator set as the next concrete step.
  - Adding ALL pairwise products of the 7 base sign-definite generators (35 total
    generators up to degree 16) did NOT help at degree 6 or 7 (still rank-deficient
    for -q1 and -q1·(1-σ)) when B3,B5 are excluded — confirms B3,B5 (or some other
    NEW, not-yet-found generator) are structurally necessary, not merely a
    convenience; pure "squares/products of already-positive things" cannot substitute
    for them.
  - **r0 is structurally harder than q1 for this generator family**: `-r0` (degree 7,
    direct, no multiplier) is NOT in the unsigned span of the full 9-generator set at
    matched degree (rank 29 vs 30), and `-r0·σ` (degree 8) with the 35-generator
    product-extended set is also NOT in the unsigned span (rank 38 vs 39). r0 likely
    needs its own dedicated generator (not just reuse of q1's basis) — flag this
    explicitly for the outliner: **do not assume a certificate for q1 transfers to
    r0 by the same generator list; r0 needs independent basis work.**

- Knowledge-base entries to use: none new beyond what's already in play (Positivstellensatz
  / SOS certificate search, resultant/Gröbner elimination — both already the population's
  standing toolkit per knowledge_base.md's algebraic-certificate entries).

- Analogous past problems (cruxes): none — per repo state, the crux corpus has no
  geometry-domain entries (confirmed in earlier rounds), and this sub-gap is now pure
  polynomial-inequality/Positivstellensatz search, a domain the crux corpus (number
  theory/combinatorics/algebra, non-geometry) wasn't checked for this narrow a target
  this round due to time; not expected to have a close analogue given how bespoke the
  generator polynomials (q1, r0, G0, Enum, Num) are to this problem's specific
  coordinate construction.

- Prior progress: see current.md / lemmas/parity-obstruction-q1-r0-certificate.md and
  lemmas/parity-basis-b1-b6-corrected.md (both independently re-derived and confirmed
  exactly by this round's computation, no discrepancies found).

- Dead ends (do not retry):
  - The minimal 3-term ansatz using only B1,B4,B6 (round 14) — reconfirmed infeasible.
  - B3, B5 as standalone sign-definite terms, even restricted to the TRUE curved
    domain (not just the loose box) — genuinely mixed-sign, confirmed this round with
    a fresh 8729-point true-domain sample (not just the loose box round 13/14 used).
  - The 6-generator degree-6-padded set {B1,-B2,B4,B6,G0Enum,G0Num} alone — proven
    (exact rank test, not numeric) insufficient even ignoring sign constraints.
  - Multiplying -q1 by (1-σ) or (1-τ) with the 9-generator set — span problem fixed,
    but LP infeasible; don't retry this exact combination without adding a further
    generator or a different multiplier.

- Small-case / intuition notes (all conjecture/numeric-only unless stated exact):
  - The three new products G0·Enum, G0·Num, Enum·Num are EXACTLY sign-definite on
    the true residual domain (8729/8729, comfortable margins ~0.01-0.1, not
    knife-edge) — strong numeric evidence they are genuine additions to the
    population's toolkit, worth certifying as a lemma once independently verified by
    a builder/reviewer (this round only checked them numerically on the sampled
    domain plus symbolically derived their closed forms; the SIGN-DEFINITENESS claim
    itself is numeric-only so far, analogous in rigor-status to B1/B4/B6's numeric
    sign census in round 14 before any symbolic sign proof was attempted).
  - Given r0's apparent structural mismatch with q1's generator family (rank tests
    above), it may be worth the next round explicitly deriving r0-specific graded
    products (e.g. is there an analogue of G0·Enum built from a different pairing,
    or does r0 need a genuinely different generator beyond {G0, Enum, Num, Bc}
    entirely?) rather than assuming symmetry between q1 and r0's certificates.
