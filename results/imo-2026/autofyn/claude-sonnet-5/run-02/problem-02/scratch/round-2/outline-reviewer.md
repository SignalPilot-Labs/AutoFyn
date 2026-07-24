# Outline review — IMO-2026-02, round 2

Reviewed: `results/imo-2026-02/current.md`, all 5 `approaches/*.md`, all 4
certified `lemmas/*.md`, `/tmp/round-2/proof-outliner.md`,
`/tmp/round-2/math-explorer-algebraic-closure.md`,
`/tmp/round-2/math-explorer-fresh-framing.md`.

I independently reproduced the whole `complex-number-argument-bash` algebra
chain from scratch in `sympy` (own script, not copied) to check the
outliner's headline claim that gap (a) is "closed."

## complex-number-argument-bash — CHANGES REQUESTED (not yet closed — do not write it up as done)

**What re-verifies cleanly (independent re-derivation, exact match):**
- `eq1` is jointly linear in `(l1,l2)` — confirmed.
- Eliminating `l2` from `eq1` gives `l2 = num_l2/D` with `D = k1p²-k1p-k1q²
  +2k2pq-k2q` — confirmed, matches.
- Substituting into `eq3` and clearing `D` gives an expression linear in
  `l1`, factoring as `±(1-l1)(p²+q²)·X(k1,k2,p,q)` with `X` matching the
  approach file's cubic **exactly** (`sympy.expand` of the difference is
  `0`) — confirmed. The `l1=1 ⟹ L=C` exclusion argument is sound.
- `eq2_num` (eq2 after the same substitution) is degree 2 in `l1` — confirmed
  (my computed total degree in `(k1,k2)` is 3, not the file's claimed 6 —
  minor discrepancy, not load-bearing, builder should recheck but it doesn't
  change the argument).

**The claimed "cofactor identity" (step 6 of the outline, the round's
single highest-value/highest-risk claim per the outliner's own flag) — I
could NOT reproduce it as stated.** Specifically:
- I built `Fn_num` (numerator of `O_x-(p/2+1/4)` via the standard 3-point
  circumcenter formula, with `l2` substituted, brought to a single fraction
  via `sympy.together`/`fraction`) and computed its true denominator at a
  concrete rational specialization `p=7,q=5`. The actual denominator factors
  as `4·D·(second_factor)` where `second_factor` is an irreducible
  degree-1-in-`l1` polynomial **coprime to `D2 = -k1q+k2p-k2`**
  (`gcd(second_factor, D2) = 1`, checked exactly). This directly contradicts
  the outline's claim that `D2` is the relevant second cofactor factor
  alongside `D` in `Fn_num·D2·D − (q−k2)·eq2_num = D²·X·L`.
- I then directly tested the outline's literal equation
  `Fn_num·D2·D − (q−k2)·eq2_num` divided by `D²·X`: the result is **not a
  polynomial** (has a genuine nonzero denominator in `k1,k2,l1`) — so the
  specific identity as written in the outline/approach file is false as
  stated, at least under my reconstruction of `Fn_num`.

**However — the underlying mathematical claim (gap (a) itself) IS almost
certainly true and provable.** I ran an independent, much stronger check:
picked `p=7,q=5,k1=1/3` (exact rationals), solved `X=0` for a real root of
`k2` exactly, substituted into `eq2_num=0` and found both roots of `l1`
exactly, then evaluated `Fn_num` at 60-digit precision at **both** roots:
both are `0` to 54 decimal digits (`~1e-54`), i.e. genuinely zero, not
numerical noise. This is very strong evidence that `Fn_num` really does lie
in the ideal `(X, eq2_num)` (up to the codim-1 exclusions `D,D2≠0` etc.) —
so the *target* of step 6 is correct and achievable, but **the specific
cofactor formula supplied by `math-explorer-algebraic-closure.md` and copied
into the approach file has not been correctly verified and must not be
trusted as-is.**

**Verdict and required changes:**
- Do not let the builder simply transcribe the round-2 explorer's cofactor
  identity into a "proof" — per CLAUDE.md, a borrowed step must be reproven
  from scratch, and here reproving it from scratch **fails to reproduce the
  claimed formula**. The explorer's claim of an exact `sympy.div` zero
  remainder was evidently checked against a different (and apparently
  incorrect, or differently-normalized) definition of `Fn_num`/`D2` than a
  straightforward reconstruction gives.
- The builder should re-derive the exact ideal-membership certificate
  properly from scratch: my 60-digit numeric check confirms it exists, so
  this is very likely closeable within the round, but the exact cofactor
  polynomials must be freshly computed and their **zero-remainder property
  checked via `sympy.div` in the builder's own script**, not asserted from
  the round-2 explorer report. Recommend the builder redo the polynomial
  division of `Fn_num` by `eq2_num` in `l1` directly (as I started), confirm
  the remainder is `l1`-linear, and then divide each remainder coefficient
  by `X` as a rational-function computation over `QQ(k1,k2)` (using
  `sympy.cancel`, not `sympy.div` with mixed generators, which throws
  `PolynomialError` on rational coefficients — a concrete pitfall I hit).
- Gap (b) (orientation/sign-matching) remains open as stated in the outline
  — the round-2 numeric witness is good evidence but not a proof; the short
  synthetic betweenness-of-rays argument (outline step 9) is still required
  and is genuinely cheap; keep it in the build task.
- Step 7 (D≠0, D2≠0 degenerate loci) is still unaddressed; small, keep as a
  task.

This is CHANGES REQUESTED, not RETHINK: the overall technique, the Lemma 0
reduction, the Dictionary Lemma, and the cubic locus for K are all solid and
independently re-confirmed; the specific closing identity is not yet
established even though strong evidence says a correct one exists. The
approach remains the clear leader and should be built again this round, with
the explicit instruction above to re-derive (not copy) the cofactor
identity.

## symmetric-vector-decomposition-sigma — APPROVE the scaffolding, open crux unchanged

- Lemma 0 import: fine, shared and certified.
- σ-symmetry of the full hypothesis system (steps 1-2): this round's
  explorer numerically confirmed σ maps a genuine containment-respecting
  solution to another genuine containment-respecting solution of the
  relabeled system (residuals ~1e-15, all containment tests true) — this is
  solid corroboration of a claim that is, as the outline itself says, "just
  bookkeeping" (direct textual substitution into each condition). No issue.
- The isosceles-case sanity check (step 3/4 numbering is a little
  inconsistent between the file and the outline, but the content is
  unambiguous) is a legitimate, cheap warm-up, not a substitute for the
  general case — correctly flagged as such.
- **The actual crux (telescoping identity, outline step 4) is still
  completely open** — no symbolic or hand computation has been attempted.
  This is honestly reported, not hidden behind a "then it follows." Good.
  The proposed starting point (the certified O-free reformulation lemma,
  which already splits `O·(C-B)` into a K-term and an L-term) is a
  reasonable and non-redundant place to start — it is a genuinely different
  route from `complex-number-argument-bash`'s brute elimination (synthetic
  antisymmetry vs. Gröbner-free elimination), so it adds real diversity to
  the field rather than being a reparametrization of the same computation
  (contrast with `homothety-doubling-target`, see below).
- No fatal flaw found. This is legitimately the field's only distinct-
  framing live alternative to the leader. Verdict: CHANGES REQUESTED is not
  quite right either since nothing is "wrong," it's simply undeveloped —
  treat as APPROVE-to-build, with the outline's own caveat enforced: if the
  telescoping identity does not yield to a bounded effort this round, the
  builder must report RETHINK honestly rather than hand-wave "by symmetry."

## homothety-doubling-target — advance, correctly deprioritized, do not build

This round's explorer finding (the computation is algebraically isomorphic
to the leader's cubic-locus/cofactor computation up to an affine change of
frame) is a legitimate and useful negative result. Confirmed reasonable on
inspection: replacing `N9` by the circumcenter and `K,L` by `2K-A,2L-A` is a
linear reparametrization of exactly the same target variety. Building this
would not add diversity or a shortcut. Correctly left out of the build set.

## nine-point-locus-two-position, spiral-similarity-radical-axis — dead-end, unchanged

Both remain correctly recorded dead ends (Lemma B numerically refuted across
~15 reparametrizations + Möbius model; no concyclic 4-subset exists among
the 70 scanned). No new information this round changes this. Their only
value is the already-certified O-free reformulation lemma (byproduct of
`nine-point-locus-two-position`), which is in active use by
`symmetric-vector-decomposition-sigma`. Correctly excluded from the build
set.

## Diversity assessment

The field has narrowed from 5 to effectively 2 live, non-redundant framings:
`complex-number-argument-bash` (coordinate/algebraic elimination, very
close to closed) and `symmetric-vector-decomposition-sigma` (synthetic
antisymmetry via σ, structurally distinct, crux untouched). This is
acceptable for one more round given the leader is near-solved and the
alternative is real progress on scaffolding (not just relabeling), but if
`complex-number-argument-bash`'s gap does not close this round and
`symmetric-vector-decomposition-sigma`'s telescoping identity also does not
yield, the orchestrator should dispatch a fresh math-explorer next round for
a genuinely third framing (e.g. a synthetic/spiral-similarity argument NOT
centered on the named points already refuted, or an inversive/trigonometric
approach) rather than let the population sit at 2 forever — this is not yet
a 3+-round plateau, so no forced pivot is required this round.

## Registration / ranking

All 5 approaches were already registered in the population (round 1); no
new slugs to register and no branch/copy needed this round (the two
"revise" outputs keep their existing slugs). Ranked the whole field
head-to-head via `update_ranking` (comparisons: leader beats all 4 others;
symmetric-vector-decomposition-sigma beats the 3 dead/redundant approaches;
homothety-doubling-target draws with the two hard dead-ends since none has
live progress). Post-update Elo: `complex-number-argument-bash` 1583 (top),
`symmetric-vector-decomposition-sigma` 1509, `nine-point-locus-two-position`
1493, `spiral-similarity-radical-axis` 1479, `homothety-doubling-target`
1436.

## Build set for this round

Dispatch exactly these two builders:
- `complex-number-argument-bash` — told explicitly: do NOT copy the round-2
  explorer's cofactor identity verbatim; re-derive `Fn_num` and its
  divisibility by `eq2_num`/`X` from scratch and verify via `sympy.div` with
  zero remainder before writing it into the proof; also close the D≠0/D2≠0
  genericity check and the orientation/sign synthetic argument (step 9).
- `symmetric-vector-decomposition-sigma` — push on the telescoping identity
  (outline step 4) starting from the O-free reformulation lemma; report
  RETHINK honestly if it does not yield within this round's budget rather
  than hand-waving.

build set: complex-number-argument-bash, symmetric-vector-decomposition-sigma
