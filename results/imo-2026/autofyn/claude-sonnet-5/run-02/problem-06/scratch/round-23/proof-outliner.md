## imo-2026-06

### a1-3qk-subfamily-theorem: new
Target: for `a_1 = 3*q^m`, `q` prime `q≥7, q≠5`, `m≥1` a fixed positive
integer, literal `T=1, L=3` periodicity from `n=1`: `a_n = 3q^m + 3(n-1)`
for every `n≥1`. (This is a strict generalization of the certified,
APPROVE'd `a1-3q-subfamily-theorem`, which is exactly the `m=1` case; that
approach's Status/solved claim for `m=1` is untouched and stays cited, not
re-derived.)

Technique: same strong-induction skeleton as `a1-3q-subfamily-theorem`
(consecutive-integer coprimality kills `a_n+1`; a Case-(a)/Case-(b) split
on `q | (a_n+2)` kills `a_n+2`; shared factor `3` legitimizes `a_n+3`),
transplanted essentially verbatim because the whole existing proof only
ever used two facts about `a_1`: `3|a_1` and `q|a_1` — both hold for
`a_1=3q^m` exactly as for `a_1=3q`, since `q | q^m` for any `m≥1`.

Skeleton:
  1. Base case `n=1`: `a_1=3q^m` by definition — trivial.
  2. `a_n+1` illegal — by consecutive-integer coprimality (`gcd(x,x+1)=1`),
     unchanged from the `m=1` proof, no `m`-dependence at all.
  3. `3 ∤ (a_n+2)` since `3|a_n` (induction hypothesis) — unchanged.
  4. Case (a) (`q ∤ (a_n+2)`): `a_n+2` illegal via `i=1`, since
     `P(a_1)={3,q}` and neither `3` nor `q` divides `a_n+2` — unchanged,
     `m`-independent (only uses `P(a_1)={3,q}`, true for any `m`, since
     `P(q^m)=\{q\}`).
  5. Case (b), `n` odd (`q|(a_n+2)`): the certified Parity Witness
     mechanism — set `N:=a_n+2=3(q^m+n)-1`; `\gcd(N,a_n)=\gcd(N,N-a_n)
     =\gcd(N,2)`; `N` odd iff `q^m+n` even iff `n` odd (`q^m` is odd since
     `q` is an odd prime) — **transplants verbatim**, replacing `q` by
     `q^m` everywhere; re-derive from scratch (do not just cite, since `m`
     appears inside the parity argument, but the algebra is identical in
     shape).
  6. Case (b), `n` even, `k=0` window (first Case-(b) occurrence for each
     `q`, independent of `m`!): mod `q`, `a_n+2 \equiv 3n-1 \pmod q` since
     `a_1 = 3q^m \equiv 0 \pmod q` for ANY `m≥1` — so the residue class
     `n_0` and the small-window analysis (`K_0\in\{4,5\}`, the exceptional
     primes `q=7,q=11` needing hand resolution) are **identical formulas
     to the `m=1` case**, since they only depend on `n_0`'s residue class
     mod `q`, which is `m`-independent. Re-verify (not just cite) that the
     two hand-checked witnesses (`q=7`,`q=11`) still work, since the exact
     integers being gcd-checked (`a_n` values) now depend on `m` even
     though the residue-class bookkeeping doesn't — this is a genuine
     re-derivation, not a free citation.
  7. Case (b), `n` even, `k≥1` (the hard residual band): apply the
     certified **Legendre Sieve Gap Bound** (`lemmas/legendre-sieve-gap-bound.md`)
     and **Primorial Floor Bound** (`lemmas/primorial-floor-bound.md`)
     unchanged — both are stated generically for a modulus `M` and its
     `ω(M)`, with no reference to `a_1`'s specific value, so they import
     directly. Re-derive the residual finite exceptional-`k` table for
     `m≥2` from scratch (do NOT assume it is empty just because the
     explorer's numeric sweep found zero exceptions for `m=2,3` up to
     `q<400` — that is evidence, not proof; the table must be recomputed
     via the same `q_thresh` monotonicity argument used for `m=1`, and
     could in principle differ since the specific integers `a_n` being
     gcd-checked at small `k` are `m`-dependent even though the modulus
     bookkeeping `(K,ω(K))` is not).
  8. Assemble the induction: every `n` covered by exactly one of steps
     2/4/5/6/7 (odd vs. even `n`, Case (a) vs. Case (b), `k=0` vs. `k≥1`
     within Case (b) even-`n`), no double-count, no skipped subcase.

Key lemmas (claim + mechanism):
  - **Transplanted Parity Witness Lemma** (`m`-generalized): `\gcd(a_n+2,
    a_n)=\gcd(a_n+2,2)` whenever `n` is odd, because `a_n+2 \equiv
    3(q^m+n)-1` has parity fixed by `n`'s parity alone (`q^m` always odd)
    — because `q` is an odd prime for every `m`.
  - **Transplanted `k=0`-Window Criterion** (`m`-generalized): the first
    Case-(b) occurrence's residue class `n_0 \pmod q` and modulus class
    `K_0\in\{4,5\}` are identical formulas to `m=1`, because they are
    derived purely from `a_1 \equiv 0 \pmod q`, a fact true for every
    `m≥1` — the *values* `a_{n_0}` differ with `m`, but the *residue-class
    bookkeeping* does not.
  - **Legendre Sieve Gap Bound / Primorial Floor Bound** (already
    certified, cited not re-proved): generic in the modulus `M`, apply
    unchanged to close the `k≥1` band once the finite residual table (if
    any) is resolved.

Open gaps: (i) re-derive and re-verify the two hand-checked `k=0`
exceptions (`q=7,q=11`) for general `m` — likely easy but not yet done;
(ii) recompute the residual `k≥1` exceptional-`(k,K_0)` table for general
`m` from scratch and confirm it is empty (or, if nonempty, hand-resolve
each entry as the `m=1` proof did for its 2 irreducible cases) — do NOT
assume emptiness from the explorer's `m=2,3` numeric sweep without an
actual derivation; (iii) run the `m=4,5` numeric cheap-kill sweep before
finalizing the theorem statement's `m`-range, to catch any `m`-specific
anomaly the explorer didn't test.

Cases to cover: `n` odd / `n` even; within even, Case (a) vs Case (b);
within Case (b) even, `k=0` vs `k≥1`. All are the same case structure as
the certified `m=1` theorem — just re-verified, not assumed, at general
`m`.

Watch out for: silently assuming any step is "the same, just replace `q`
by `q^m`" without checking where the actual VALUE of `a_1` (not just its
prime support) enters an argument — steps 2–5 are provably value-blind
(only use `P(a_1)`), but steps 6–7's numeric hand-checks and finite tables
use actual `a_n` values and must be recomputed, not copy-pasted.

---

### direct-s0-self-absorption: new
Target: prove H2's existence hypothesis directly and non-inductively — the
canonical core `S₀` from the certified **Finite Core Theorem**
(`lemmas/finite-core-theorem.md`) is *itself* self-absorbing (possibly
after finitely enlarging it by the full factorizations of the pre-
persistence transient terms), i.e. `∃` finite `S* ⊇ S₀` with `N(S*) ≤`
(some explicit bound) and `P(a_j) ⊆ S*` for every `j=1,\dots,N(S*)`. This
is scoped as an attack on H2 alone (the Master Conditional Theorem's other
hypothesis, H1/FAH, is untouched) — genuinely different framing from the
now-provably-dead one-prime-at-a-time chain induction
(`core-growth-monotonicity`, Proposition 3, `dead-end`).

Technique: direct/closed-form verification using `S₀`'s own explicit
construction, NOT an inductive bounded-prefix chain — Proposition 3's
impossibility result applies only to inductively bounding a quantity
(`M_B`) built up one recruitment step at a time from an a priori unknown
starting point; it says nothing about a direct structural argument on the
single, already-fully-specified set `S₀`.

Skeleton:
  1. Recall the exact definitions (import, do not re-derive):
     `S₀ = Q ∪ ⋃_{B∈𝒫}(P(a_{m_B})\Q)` (Finite Core Theorem), `N_0` the
     Persistent-Type Pigeonhole threshold, `N(S)`/`𝒫'(S)` at a general
     core `S` (Extended Persistent-Type Pigeonhole), self-absorption
     `S⁺=S` meaning `P(a_j)⊆S` for `j=1,\dots,N(S)` (Self-Absorbing Core
     Theorem's definitions).
  2. Handle the pre-persistence transient explicitly: define
     `S₀' := S₀ ∪ ⋃_{j=1}^{N_0} P(a_j)` — still a finite, explicit set
     (finitely many extra primes adjoined), and `S₀' ⊇ S₀`, so it is a
     legitimate candidate `S*` for the Self-Absorbing Core Theorem (which
     only needs `S* ⊇ S₀`, not literally `S* = S₀`). This closes the `j
     ≤ N_0` sub-case of self-absorption for free, by construction —
     record it as a trivial step, not a gap.
  3. **Key open gap — the load-bearing claim this approach must supply:**
     for `N_0 < j ≤ N(S₀')`, show `P(a_j) ⊆ S₀'`. Equivalently: every
     term in this range has NO prime factor outside `S₀'`.
  4. Candidate mechanism to attempt: for `j` in this range, `τ(j)` is a
     well-defined persistent base type `B∈𝒫` (since `j>N_0`); the
     certified **Bounded Witness Lemma** gives, for every OTHER persistent
     type `B'≠B` disjoint from `B`, that `a_j` shares SOME prime with
     `P(a_{m_{B'}})\Q ⊆ S₀'` — but **this only shows `a_j` has at least
     one prime IN `S₀'` for each disjoint `B'`, it does NOT show `a_j` has
     NO primes outside `S₀'`** (per the standing round-2/round-22
     false-strengthening caution already on record in this workspace: "at
     least one shared prime" never implies "no extra primes"). **Do not
     present this as closing the gap** — it is exactly the open content.
  5. If step 4's direct route fails (as the honest per-lemma check in step
     4 already suggests it will, without a genuinely new ingredient),
     fall back to reporting the gap precisely: this reduces H2's existence
     half to the single sharp question "is `P(a_j)⊆S₀'` for the finitely
     many explicit `j∈(N_0,N(S₀')]`?" — a concrete, numerically checkable
     (not just asymptotically conjectured) target, distinct in kind from
     the killed inductive `M_B`-bounding family, and report it as the
     approach's residual open gap rather than force a false closure.

Key lemmas (claim + mechanism):
  - `S₀'` (finite enlargement of `S₀` by transient full factorizations)
    is self-absorbing for indices `j≤N_0` — because those primes are
    adjoined to `S₀'` by definition, so `P(a_j)⊆S₀'` trivially for
    `j≤N_0`.
  - (Open, not yet proved) `P(a_j)⊆S₀'` for `N_0<j≤N(S₀')` — would need a
    genuinely stronger fact than Bounded Witness Lemma supplies (that
    fact only gives nonempty intersection with each disjoint witness's
    outside-`Q` prime set, not full containment of `a_j`'s own outside-`Q`
    factorization) — this is the real, hard, currently-unresolved content
    of the approach.

Open gaps: step 3/4 above — the central claim is genuinely unproved; the
approach's honest expected outcome this round is either (a) a real proof
via some mechanism not yet identified, or (b) a precise negative/diagnostic
finding (why Bounded Witness Lemma's "at least one shared prime" content
structurally cannot be upgraded to "no extra primes" without new
machinery) — either outcome is real progress per the workspace's
established diagnostic-lemma precedent (do not force step 4 into looking
solved when it isn't).

Cases to cover: `j≤N_0` (closed, step 2) vs. `N_0<j≤N(S₀')` (open, steps
3–5) — no other cases, since `N(S₀')` is finite by the Extended
Persistent-Type Pigeonhole.

Watch out for: (i) the exact false-strengthening trap already flagged in
this workspace's memory (round 2, imo-2026-06) — "shares at least one
prime with EACH disjoint witness" is NOT "confined entirely to `S₀'`";
(ii) confirm `N(S₀')` is itself well-defined and finite BEFORE attempting
step 3 (it is, by the certified Extended Persistent-Type Pigeonhole
applied at `S=S₀'`, but state this citation explicitly rather than assume
it); (iii) the round-17 numeric evidence (`N(S₀)=0` on 9/9 tested seeds
including both known hard FAH seeds) is suggestive but is NOT proof and
must not be cited as if it closes step 3.

---

### covering-system-construction: advance
(existing file: `results/imo-2026-06/approaches/covering-system-construction.md`,
Elo 1864.6, highest in the population, `partial`, expanded 10 rounds)
Target: unchanged — the problem's actual claim via a covering-system/
residue-eligibility construction at a finite core, narrowing gap (†) (the
"which specific prime pins down the eligible-residue set" question).
Technique: unchanged (covering system + persistent-type intersection),
now sharpened per its most recent reviewer note to a single concrete
residual target — the `|F''|=2`, multiplicity-1 case reduced to one
divisor-class question. Recommend the builder pursue exactly that
flagged fallback target this round (close the specific divisor-class
question, or find and report precisely why it resists closure) rather
than open a new mechanism inside this file — this keeps the advance
distinct in kind from a fresh H1 sweep (per this round's explicit
instruction not to open a new generic H1 mechanism), since it is finishing
a concretely-scoped residual inside an already-narrowed, live gap, not
starting a new corridor search.
Open gaps: the single divisor-class question flagged in the last reviewer
note (see the file's own current gap statement for the precise claim).
Cases to cover: as already enumerated in the file.
Watch out for: do not let this advance turn into a 9th generic FAH-
mechanism hunt — if the concrete divisor-class question itself proves to
require a fundamentally new mechanism rather than direct casework, report
that honestly as a new dead-end/RETHINK rather than smuggling in a fresh
generic attempt under this slug's name.

---

### a1-5q-subfamily-theorem: new (lower priority, second subfamily target)
Target: for `a_1=5q`, prime `q≥7` with `q ∉ \{7,13,19\}` (three primes
excluded, analogous to the certified `q=5` exclusion in `a1-3q`), literal
`T=1,L=5` periodicity from `n=1`: `a_n=5q+5(n-1)`.

Technique: same strong-induction skeleton, structurally generalized
(3 residual bands instead of 1, since `P(a_1)=\{5,q\}` gives THREE
intermediate candidates `a_n+j`, `j=2,3,4`, instead of one).

Skeleton:
  1. Base case, `a_n+1` illegal — unchanged, consecutive-integer
     coprimality.
  2. For `j\in\{2,3,4\}`: `5\nmid(a_n+j)` (since `5|a_n` by induction
     hypothesis and `j\not\equiv0\pmod5`) — so `a_n+j` is illegal via
     `i=1` whenever `q\nmid(a_n+j)` (Case (a), all three `j`).
  3. Residual Case (b) (`q|(a_n+j)`, each `j`): generalize the certified
     Parity Witness identity — `N:=a_n+j`, `\gcd(N,a_n)=\gcd(N,N-a_n)
     =\gcd(N,j)` — so whenever `\gcd(N,j)=1` (true automatically for
     `j=2,3` when `N` is not a multiple of `2` resp. `3`; for `j=4` need
     `N` odd), witness `i=n` is free with no case split on `q`. Re-derive,
     for EACH `j\in\{2,3,4\}` separately, the exact residue condition on
     `n` (or `N`) that makes `\gcd(N,j)=1`, since the certified lemma was
     only stated and proved for `j=2` under `a_1=3q`.
  4. For the residual `\gcd(N,j)>1` sub-cases within each band, apply the
     certified Legendre Sieve Gap Bound / Primorial Floor Bound as before,
     closing each of the three bands independently.
  5. Assemble: every `n`, every `j`, covered by exactly one of steps 2–4,
     across all THREE bands simultaneously (a candidate `a_n+j` is legal
     only if ALL of `j=2,3,4` are shown illegal, so the induction must
     close every band, not just one, before concluding `a_n+5` is forced).

Key lemmas (claim + mechanism):
  - **Generalized Parity/gcd Witness** (`j`-generalized): `\gcd(a_n+j,
    a_n)=\gcd(a_n+j,j)`, because `\gcd(x,y)=\gcd(x,x-y)` applied with
    `x=a_n+j,y=a_n` — an identity, true for any `j`, not just `j=2`; the
    NEW content needed is characterizing exactly when `\gcd(a_n+j,j)=1` in
    terms of `n`'s residue, separately for `j=2,3,4`.
  - Exceptional-prime set `\{7,13,19\}` must be *excluded* (not
    hand-resolved), per the explorer's finding that these show
    persistent, FAH-hard-looking non-periodic behavior out to 300 terms —
    do not attempt to hand-check them into the theorem; state them as a
    genuine exclusion, matching the `q=5` precedent in `a1-3q`.

Open gaps: the full triple-band Case-(b) closure (step 3–4, `j=2,3,4`
each), and independent confirmation (before build) that no fourth bad
prime lurks beyond `q=300` — run a deeper sweep first as the explorer's
cheap-kill recommends.

Cases to cover: `j\in\{2,3,4\}` × (Case (a)/Case (b)) × (`k=0`/`k≥1`
residual band per `j`) — roughly 3× the casework of the closed `a1-3q`
gap, same shape.

Watch out for: this is a secondary/lower-priority target relative to
`a1-3qk-subfamily-theorem` — only worth a build slot if the primary
subfamily approach's slot is already saturated or its build stalls; do
not let it compete for the same builder round unless capacity allows
both, per the outline-reviewer's build-set discretion.
