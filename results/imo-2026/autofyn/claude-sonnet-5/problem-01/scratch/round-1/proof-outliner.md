## imo-2026-01
Spec review: required
(Two-part IMO-style proof, a non-obvious invariant construction, and an exact
case split the explorer already got wrong once by hand — exactly the profile
that should get an outline-reviewer pass before the builder writes prose.)

Technique: **Reformulate multiplicatively (gcd/lcm on 2026 integers) as
independent additive problems, one per prime, via p-adic valuation.**
Under this lens: `v_p(gcd(m,n)) = min(x,y)`, `v_p(lcm(m,n)/gcd(m,n)) = |x-y|`
where `x=v_p(m), y=v_p(n)`. This is the single "cheap kill" that avoids any
heavy machinery (no Zsigmondy/LTE/analytic NT needed despite the `number_theory`
tag) — every other lever (naive board-gcd, board-lcm, "# of moves") is a
**refuted dead end** (see Watch out for). Part (a) = a monovariant
(`Ψ = Φ·2^c`, strict descent) for termination, plus the same invariant used in
part (b) to rule out total collapse. Part (b) = an exact invariant (`Γ`,
"gcd of p-adic valuations across the whole board, per prime") preserved by
every move, evaluated at the end.

I have verified **every lemma below both by hand (complete elementary proofs,
not sketches) and computationally** (200,000 random `(m,n)` pairs for the
case-split, 3000 full random board-simulations for the Ψ-descent, all
`x,y∈{0,…,200}` for the subtraction lemma, all `m,n∈{1,…,300}` for the squeeze
lemma, and 10 structurally diverse boards × 25 random move-orders each for the
full `Γ`-formula, including large/many-prime/repeated-value/coprime cases —
0 violations everywhere). This is a genuinely correct route, not a plausible
one; the outline below is low-risk on mathematical content, the risk is purely
in **precise write-up of the case split and the logical ordering** (flagged
throughout).

Skeleton:
  1. **Setup lemmas** (proved once, used by both parts): (1a) the
     **gcd·lcm identity** `gcd(m,n)·lcm(m,n) = mn` for all positive integers
     `m,n` — by comparing `p`-adic valuations at every prime
     (`min(v_p(m),v_p(n)) + max(v_p(m),v_p(n)) = v_p(m)+v_p(n) = v_p(mn)`,
     then unique factorization: two positive integers with equal valuation at
     every prime are equal); (1b) the standard `p`-adic valuation identities
     for gcd/lcm (Valuation-transform Lemma, below).
  2. **Lemma Γ (the invariant)** — define, for a finite list of positive
     integers, `Γ := ∏_p p^{gcd of p-adic valuations across the list}`; prove
     one legal move leaves `Γ` of the *whole board* unchanged; extend to any
     finite sequence of moves by induction on the move count. This is proved
     **before** part (a) and does **not** depend on part (a)'s conclusion.
  3. **Part (a), finiteness** — exhibit `Ψ := Φ·2^c` (`Φ` = product of all
     board entries, `c` = count of entries `>1`); note `Ψ` is **always a
     positive integer** (`Φ` is a product of positive integers ⟹ `Φ≥1`,
     `2^c≥1`), and whenever a move is still legal, `c≥2` (a move needs 2
     distinct positions `>1`), so `Ψ_{\text{old}} ≥ 1·2^2 = 4 > 0`. Prove `Ψ`
     satisfies `Ψ_{\text{new}} ≤ Ψ_{\text{old}}/2` on every move via an exact
     3-case split; since `Ψ_{\text{old}}>0`, this bound gives the **strict**
     inequality `Ψ_{\text{new}} < Ψ_{\text{old}}` — a strictly decreasing
     sequence of positive integers is finite (infinite descent /
     well-ordering of `ℕ`) ⟹ the process halts after finitely many moves.
     The process can only halt when `c ≤ 1` (a move needs 2 distinct
     positions `>1`).
  4. **Part (a), ruling out `c=0`** — if the terminal board were all 1's,
     every `v_p(y_i)=0`, so every `γ_p(\text{terminal}) = \gcd(0,\dots,0) =
     0`, giving **`Γ(\text{terminal}) = ∏_p p^0 = 1`** (the all-zero-exponent
     product is `1`, not `0` — `p^0=1` is definitional, not a convention to
     reinterpret). Meanwhile every one of the 2026 *initial* entries is `>1`
     (given), so in particular `x_1>1` has a prime factor `p_0` with
     `v_{p_0}(x_1)≥1`; a gcd of nonnegative integers is `0` only if *all* of
     them are `0`, and `v_{p_0}(x_1)≠0`, so
     `γ_{p_0}(\text{initial}) = \gcd(v_{p_0}(x_1),\dots,v_{p_0}(x_{2026})) ≥
     1`, hence **`Γ(\text{initial}) ≥ p_0^{1} ≥ 2 > 1`** strictly (every other
     prime's factor in the product is `≥ p^0=1`, so none of them can pull the
     product back down). But `Γ` is invariant (step 2), so
     `Γ(\text{terminal}) = Γ(\text{initial})`, i.e. `1 = Γ(\text{initial}) >
     1` — a contradiction, so `c=0` is impossible at termination. Combined
     with step 3 (`c≤1` at termination): `c=1` exactly, i.e. **finitely many
     moves, terminating with exactly one entry `M>1`.** This proves (a).
  5. **Part (b)** — the terminal board is `(1,…,1,M)`; compute
     `Γ(terminal) = M` directly (1 is `Γ`'s identity in each coordinate).
     By step 2, `Γ(terminal) = Γ(initial)`, a quantity depending **only** on
     the original `x_1,…,x_{2026}`, not on any choice made. Hence every legal
     complete play produces the *same* `M = Γ(x_1,…,x_{2026})`. This proves
     (b) and gives the explicit closed form.

Key lemmas (claim + the one-line mechanism that makes it true):

- **Setup Lemma (gcd·lcm product identity).** For all positive integers
  `m,n`: `gcd(m,n)·lcm(m,n) = mn` — because for every prime `p`,
  `v_p(gcd(m,n)) + v_p(lcm(m,n)) = min(v_p(m),v_p(n)) + max(v_p(m),v_p(n)) =
  v_p(m)+v_p(n) = v_p(mn)` (the min/max of two numbers always sum to their
  sum), and two positive integers with equal valuation at every prime are
  equal (unique factorization). This is what licenses "`Φ_{new} = Φ_{old}/g`"
  in the Ψ-descent Lemma (`g·(ℓ/g) = ℓ = mn/g` is this identity rearranged),
  and should be stated as its own lemma rather than left implicit inside that
  proof.

- **Squeeze Lemma.** For integers `m,n>1`, `gcd(m,n) | m | lcm(m,n)` (trivial
  divisibility facts), so `gcd(m,n) = lcm(m,n) ⟺ m=n` — because mutual
  divisibility `gcd(m,n) | m | lcm(m,n) = gcd(m,n)` forces `m = gcd(m,n) =
  lcm(m,n)`, and symmetrically `n = gcd(m,n)`, so `m=n`. Corollary: `m≠n ⟹
  gcd(m,n) < lcm(m,n)` strictly (since `≤` always holds, via the same chain,
  and `=` is excluded). *(Verified: 0 exceptions for all `m,n ∈ 1..300`.)*

- **Valuation-transform Lemma.** `v_p(gcd(m,n)) = min(v_p(m),v_p(n))` and
  `v_p(lcm(m,n)/gcd(m,n)) = |v_p(m)-v_p(n)|` — because `v_p(gcd)=min(v_p)`,
  `v_p(lcm)=max(v_p)` are the defining coordinatewise properties of gcd/lcm on
  prime exponents, and `v_p(lcm/gcd) = max - min = |diff|`. This is what
  decouples the whole problem prime-by-prime — **the central idea**.

- **Subtraction (Euclid-step) Lemma.** For integers `x,y ≥ 0`,
  `gcd(min(x,y), |x-y|) = gcd(x,y)` (convention `gcd(a,0)=a`, `gcd(0,0)=0`) —
  because (WLOG `x≥y`, both sides symmetric in `x,y`) any common divisor of
  `{x,y}` divides `x-y` (linear combination) and `y`, and conversely any
  common divisor of `{y,x-y}` divides `(x-y)+y=x` and `y`; the two pairs have
  identical common-divisor sets, hence equal gcd. This is one step of the
  subtractive Euclidean algorithm — completely elementary, **do not look for
  anything deeper here**. *(Verified: 0 exceptions for all `x,y ∈ 0..200`.)*

- **Grouping Lemma** (routine but must be stated, not asserted). `gcd` of a
  finite list of nonnegative integers is independent of the order/
  parenthesization used to combine it pairwise — because `gcd(a,b,c) =
  gcd(gcd(a,b),c) = gcd(a,gcd(b,c))` etc. follow from associativity/
  commutativity of binary `gcd` (itself immediate: both `gcd(gcd(a,b),c)` and
  `gcd(a,gcd(b,c))` equal the nonnegative generator of the ideal
  `(a,b,c) ⊆ ℤ`, and ideal sums are associative/commutative). Needed to
  isolate "the two touched entries" out of the whole-board `Γ`-computation.

- **Γ-invariance Lemma (the crux of part b, and of ruling out `c=0` in part a).**
  Define, for the current board `y_1,…,y_N` and each prime `p`,
  `γ_p := gcd(v_p(y_1),…,v_p(y_N))` (a gcd of nonneg integers, finite support
  since only finitely many primes divide any `y_i`), and
  `Γ(y_1,…,y_N) := ∏_p p^{γ_p}`. Claim: a single legal move leaves `Γ`
  unchanged. Mechanism: a move only touches two positions `i≠j` (values
  `m,n`); by the Grouping Lemma, `Γ`'s exponent at `p` is
  `γ_p = gcd(gcd(v_p(m),v_p(n)), {v_p(y_k)}_{k≠i,j})`; the untouched part is
  literally unchanged, and `gcd(v_p(m),v_p(n))` is unchanged too because after
  the move the touched values have `v_p = min(x,y), |x-y|` (valuation-
  transform lemma) and `gcd(min(x,y),|x-y|) = gcd(x,y)` (subtraction lemma).
  So every `γ_p`, hence `Γ`, survives one move; by induction on the number of
  moves, `Γ` survives any finite sequence of moves — **this holds regardless
  of whether the process ever terminates**, so it can (and should) be proved
  *before* part (a), as shared infrastructure. *(Verified: 10 structurally
  diverse boards, up to 6 primes and large values, 25 random move-orders
  each — terminal `M` matched `Γ(initial)` in all 250 runs.)*

- **Ψ-descent Lemma (exact 3-case split — pin this down precisely, do NOT use
  a size-based boundary like "`g < min(m,n)`", which is false).** Let
  `Φ := ∏ (\text{all } N \text{ board entries})`, `c := \#\{i : x_i>1\}`,
  `Ψ := Φ·2^c`. For a move on `m,n>1` with `g=gcd(m,n)`, `ℓ=lcm(m,n)`
  (new pair `(g, ℓ/g)`), `Φ_{\text{new}} = Φ_{\text{old}}/g` always (by the
  Setup Lemma, `g·(ℓ/g)=ℓ=mn/g`). The **exact, exhaustive, pairwise-disjoint** case split
  on `(m,n)` with `m,n>1`:
    - **(i) `g=1`.** New pair `(1, mn)`, and `mn>1`. Old pair contributed 2 to
      `c`, new contributes 1 ⟹ `c` drops by 1. `Ψ_{\text{new}} = Ψ_{\text{old}}/2`
      exactly.
    - **(ii) `g>1` and `m=n`.** (Automatic: `m=n>1 ⟹ g=m>1`, so this is really
      just the condition "`m=n`".) By the Squeeze Lemma, `ℓ=g`, so `ℓ/g=1`.
      New pair `(g,1)` ⟹ `c` drops by 1. `Ψ_{\text{new}} =
      Ψ_{\text{old}}/(2g) ≤ Ψ_{\text{old}}/4` (since `g=m≥2`).
    - **(iii) `g>1` and `m≠n`.** By the Squeeze corollary, `ℓ/g ≥ 2 > 1`. New
      pair `(g, ℓ/g)` both `>1` ⟹ `c` **unchanged**. `Ψ_{\text{new}} =
      Ψ_{\text{old}}/g ≤ Ψ_{\text{old}}/2` (since `g≥2`).
    These three cases partition all `(m,n)` with `m,n>1` (`g=1` or `g>1`;
    within `g>1`, `m=n` or `m≠n`; and `(g=1)∧(m=n)` is impossible since
    `m=n>1 ⟹ g=m>1`). In **every** case `Ψ_{\text{new}} ≤ Ψ_{\text{old}}/2`.
    `Ψ` is always a positive integer (`Φ` a product of positive integers,
    `2^c` a power of 2), and whenever a move is legal `c≥2` so
    `Ψ_{\text{old}}≥4>0`; hence `Ψ_{\text{new}} ≤ Ψ_{\text{old}}/2` is a
    **strict** decrease `Ψ_{\text{new}} < Ψ_{\text{old}}` between positive
    integers, which is what licenses the infinite-descent conclusion in
    skeleton step 3.
    Mechanism for *why the product `Φ·2^c` and not `Φ` or `c` alone*: case
    (i) is exactly when `Φ` fails to shrink (`g=1`) — but that's exactly when
    `c` shrinks; case (iii) is exactly when `c` fails to shrink — but that's
    exactly when `Φ` shrinks by a factor `≥2`. The two "stalls" are
    complementary, so the product always moves. *(Verified: 200,000 random
    `(m,n)` pairs for the case-split itself, 3000 full random-board
    simulations, sizes 2–7, logging `Ψ` at every individual move — 0
    violations of `Ψ_new ≤ Ψ_old/2`.)*

Cases to cover:
  - The 3-way split in the Ψ-descent Lemma above — state it by the *exact*
    boolean conditions `g=1` / `g>1 ∧ m=n` / `g>1 ∧ m≠n`, never by relative
    size of `g` to `m,n` (the explorer's own first attempt at "`1<g<min(m,n)`"
    is false: `m=4,n=8` has `g=min(m,n)=4` exactly and still lands in case
    (iii), `c` unchanged).
  - `c=0` vs `c=1` at termination (part a) — both are consistent with "no
    legal move possible"; only the Γ-invariance argument excludes `c=0`.
  - None of the above cases can be skipped or merged — case (ii) genuinely
    differs from (iii) in its effect on `c` (this is what makes `Ψ`, not `Φ`
    or `c` alone, the right potential).

Watch out for:
  - **Logical ordering.** Prove Γ-invariance (the Γ-invariance Lemma, skeleton
    step 2) as shared infrastructure *before* touching part (a) — it needs
    nothing from part (a). Part (a)'s "rule out `c=0`" step needs Γ-invariance *plus*
    independently-established finiteness (so that "the terminal board,
    reached after some finite number of moves, has the same `Γ` as the
    initial board" is a legitimate instance of the induction, not circular).
    Part (b) needs Γ-invariance *plus* part (a)'s "exactly one survivor."
    Getting this dependency order backwards (e.g. trying to use "exactly one
    survivor" to prove Γ-invariance) would be circular — make sure the
    write-up proves Γ-invariance for an *arbitrary* single move with no
    reference to how the process ends.
  - **Universal quantification.** Both parts are "for every sequence of
    choices," not "for some." Confirm the write-up proves the Ψ-descent and
    Γ-invariance lemmas for an *arbitrary* legal move (any `m,n`, any
    position), so induction over an arbitrary finite move-sequence gives the
    claim for literally every possible play, not just an example play.
  - **Do not conflate `Γ` with the board's ordinary `gcd` or `lcm`.** `Γ`
    takes the gcd of *exponents* per prime, which is a different operation
    from gcd of the *numbers*. Refuted dead ends (do not re-derive/retry):
    `M = gcd(x_1,…,x_{2026})` is false (`(4,8) → M=2 ≠ gcd(4,8)=4`; also the
    running board-gcd is not even preserved mid-process, e.g.
    `(128,64,32) → (64,2,32)` drops the board gcd from 32 to 2 in one move);
    `M = lcm(x_1,…,x_{2026})` is false (same `(4,8)` example, `lcm=8≠2`);
    "number of moves" is not an invariant (varies by move order for fixed
    starting data — verified, e.g. `[8,12,20]` terminates in 5, 6, or 7 moves
    depending on order — don't waste effort trying to prove it's fixed).
  - **State the `gcd(0,…,0):=0` / `gcd(a,0)=a` conventions explicitly** where
    first used (Subtraction Lemma and the definition of `γ_p`) — silent use
    without a stated convention is exactly the kind of gap CLAUDE.md's
    "no hand-waving" rule flags.
  - **`p^0=1`, not `0` — do not re-introduce the fixed error.** An all-1's
    board has every `γ_p = gcd(0,…,0) = 0`, but `Γ = ∏_p p^0 = 1` (empty/
    all-zero-exponent product is `1` by definition), **not** `0`. A first
    draft of this outline mis-stated `Γ(\text{all-1's}) = 0`; the corrected
    Part (a)/step-4 argument (above) instead derives `Γ(\text{terminal
    all-1's})=1` and the strict `Γ(\text{initial})>1` (via a prime factor of
    any one of the 2026 initial entries, all of which are `>1` by
    hypothesis), giving the contradiction `1>1`. Make sure the builder's
    prose uses these corrected values, not `0` / `≥1`.
  - **Well-definedness of `Γ`.** State explicitly that only finitely many
    primes have `γ_p > 0` (since only finitely many primes divide any single
    `y_i`, hence only finitely many divide *some* `y_i`), so `Γ = ∏_p
    p^{γ_p}` is a finite product, a genuine positive integer — don't leave
    this as an implicit assumption.
  - **`N=2026` carries no special number-theoretic role** — confirmed: the
    argument is verbatim for any `N≥1` (trivial for `N=1`: no legal move
    exists, `M=x_1`). Do not spend builder effort looking for meaning in
    2026's factorization; it is flavor only.
  - **Grouping Lemma must be stated, not waved at.** "`gcd` of a multiset
    doesn't care how you group it" is standard but CLAUDE.md forbids
    "clearly/obviously" — give the one-line ideal-generation (or induction)
    justification explicitly in the write-up.
  - **Both directions of part (a)** must appear: finiteness (Ψ-descent) *and*
    "exactly one" (ruling out `c=0`) are logically independent halves; a
    write-up that proves only termination-in-general (stopping at `c≤1`
    without excluding `c=0`) is incomplete.
  - Since this is `answer_type: none` / `proof_only`, there is no numeric
    answer to verify by substitution — but the *formula* for `M` (Γ of the
    initial board) should still be sanity-checked by the builder against a
    tiny explicit example (e.g. `(4,8) → M=2`, or a pairwise-coprime tuple
    collapsing to the ordinary product) as a self-check, mirroring
    CLAUDE.md's "verify final answers" spirit even though no single number is
    being asserted.
