## Status
partial

## Approaches tried
- Round 1 (outliner skeleton) — proposed the combinatorial involution
  σ: B↔C, M↔N, K↔L, A fixed, claiming it is a symmetry of the defining
  hypothesis system, and speculated that the along-BC component of O−N9 is
  "antisymmetric" under σ, hence forced to vanish. Left entirely unproved
  (steps 1-2 asserted, step 3 the actual computation not attempted).
- Round 2 explorer (`math-explorer-fresh-framing`) — built a
  containment-filtered numerical solver for the true 1-parameter family of
  valid (K,L) and numerically confirmed σ maps a genuine solution of the
  system for (A,B,C) to a genuine solution of the σ-relabeled system for
  (A,C,B) (residuals ~1e-15, all containment/orientation tests true).
  Numerically de-risked steps 1-2 but did not touch step 3.
- **Round 2 (this build).** (a) Wrote out the full clause-by-clause
  verification of σ-invariance of the hypothesis system rigorously (not
  just numerically) — CONFIRMED, matches the numerics exactly, no
  discrepancy. (b) Attempted the actual load-bearing step: derive that
  `(O−N9)·(C−B)` is forced to vanish by combining σ with the O-free
  circumcenter reformulation lemma. **Result: this specific mechanism is
  PROVABLY VACUOUS** — proved rigorously (both by hand and independently
  checked in `sympy`) that `T := (O−N9)·(C−B)` satisfies `T(swapped) = −T`
  as a pure algebraic *tautology* of the defining formulas, holding for
  **arbitrary** points A,B,C,K,L with no use whatsoever of hypotheses
  (i)-(iii) or even of K,L being well-defined solutions of anything. The
  sign flip is already fully explained, with zero extra content, by the
  utterly elementary fact that `OM² − ON²` is antisymmetric under swapping
  the *names* M ↔ N for *any* point O — a one-line algebraic identity
  independent of the whole problem. Hence σ, as originally conceived in the
  outline (i.e., "swap labels, observe the target flips sign, conclude it
  is 0"), supplies **no constraining power** on the actual value of T: it
  can never be used, by itself, to prove T = 0, only to reconfirm the
  (already-known-from-Lemma-0) fact that T changes sign under exchanging
  M and N. Dead end for this specific mechanism — recommend RETHINK on the
  framing (see "Current best" below for the precise statement and proof of
  this vacuity result, and for what a genuine rescue would require).

## Current best

**Imported (certified, unconditional on this approach's own work):**

- **Lemma 0 (nine-point-center reduction)**, `lemmas/nine-point-center-reduction.md`:
  `OM = ON ⟺ (O−N9)·(C−B) = 0`, where N9 is the nine-point center of ABC.
- **O-free circumcenter reformulation**, `lemmas/o-free-circumcenter-reformulation.md`:
  for non-collinear A,K,L with circumcenter O, and any B,C,
  `O·(C−B) = ½[α(|K|²−|A|²) + β(|L|²−|A|²)]`, where `α = det(C−B,L−A)/D`,
  `β = det(K−A,C−B)/D`, `D = det(K−A,L−A)`.

**New result 1 (proved in full this round): σ is a symmetry of the
defining hypothesis system — the clause-by-clause verification.**

Write out the problem's defining conditions on the unknowns (K,L), given
(A,B,C) with M = midpoint(AB), N = midpoint(AC), as a labeled list:

- (0a) M = midpoint(A,B).  (0b) N = midpoint(A,C).
- (1) K lies inside triangle BMC.
- (2) L lies inside triangle BNC.
- (3) K lies inside angle LBA.
- (4) L lies inside angle ACK.
- (5) ∠KBA = ∠ACL.
- (6) ∠LBK = ∠LNC.
- (7) ∠LCK = ∠BMK.

Let σ denote the *formal* substitution B↦C, C↦B, M↦N, N↦M, K↦L, L↦K, A↦A
applied literally to the text of each clause (i.e., relabel every symbol
occurring in the clause). We check, clause by clause, that σ permutes this
list of eight clauses among itself:

- σ(0a) = "N = midpoint(A,C)" = (0b); σ(0b) = "M = midpoint(A,B)" = (0a).
  So {(0a),(0b)} ↦ {(0b),(0a)}: the pair is preserved setwise.
- σ(1) = "L lies inside triangle CNB". Since "inside triangle CNB" and
  "inside triangle BNC" describe the same set of points (a triangle's
  interior does not depend on the order in which its vertices are listed),
  σ(1) = (2).
- σ(2) = "K lies inside triangle CMB" = "K lies inside triangle BMC" = (1)
  (same reasoning). So {(1),(2)} is preserved setwise, with (1)↔(2).
- σ(3) = "L lies inside angle KCA". The angle "∠LBA" (vertex B, rays BL,
  BA) has image, under B↦C, L↦K, A↦A, exactly the angle with vertex C and
  rays CK, CA, i.e. angle KCA = angle ACK (an angle is determined by its
  vertex and its two bounding rays, independent of which ray is named
  first). So σ(3) = "L lies inside angle ACK" = (4).
- σ(4) = "K lies inside angle ABL" = "K lies inside angle LBA" (same
  reasoning) = (3). So {(3),(4)} preserved setwise, (3)↔(4).
- σ(5): ∠KBA (vertex B, rays BK,BA) ↦ (under B↦C,K↦L,A↦A) the angle with
  vertex C, rays CL, CA, i.e. ∠LCA = ∠ACL. And ∠ACL (vertex C, rays CA,CL)
  ↦ (under C↦B, A↦A, L↦K) the angle with vertex B, rays BA, BK, i.e.
  ∠ABK = ∠KBA. So σ(5) reads "∠ACL = ∠KBA", which is the same equality as
  (5) (an equation `x = y` and `y = x` are the same statement). σ(5) = (5):
  self-dual.
- σ(6): ∠LBK (vertex B, rays BL,BK) ↦ (B↦C,L↦K,K↦L) vertex C, rays CK,CL,
  i.e. ∠KCL = ∠LCK. And ∠LNC (vertex N, rays NL,NC) ↦ (N↦M,L↦K,C↦B) vertex
  M, rays MK,MB, i.e. ∠KMB = ∠BMK. So σ(6) reads "∠LCK = ∠BMK" = (7).
- σ(7): ∠LCK (vertex C, rays CL,CK) ↦ (C↦B,L↦K,K↦L) vertex B, rays BK,BL,
  i.e. ∠KBL = ∠LBK. And ∠BMK (vertex M, rays MB,MK) ↦ (M↦N,B↦C,K↦L) vertex
  N, rays NC,NL, i.e. ∠CNL = ∠LNC. So σ(7) reads "∠LBK = ∠LNC" = (6). So
  {(6),(7)} preserved setwise, (6)↔(7).

**Conclusion of the verification.** σ maps the clause list bijectively to
itself (fixing (0a,0b) as a pair, (5) individually, and swapping
(1)↔(2), (3)↔(4), (6)↔(7)). Consequently: if (K,L) is a valid solution of
the system S(A,B,C) [conditions (0)-(7) with the literal points A,B,C], then
substituting the actual point-pair (L,K) into the system S(A,C,B) [the same
eight conditions with the roles of B,C, hence also M,N, exchanged] makes
each of S(A,C,B)'s eight clauses true, because each clause of S(A,C,B) is,
by the check above, literally identical (as a statement about points in the
plane) to some clause of S(A,B,C), and that clause holds for (K,L) by
hypothesis. So **(L,K) is a valid solution of S(A,C,B).**

Since σ is an involution (σ∘σ = identity on symbols: swapping B,C twice and
K,L twice returns everything to the start), this correspondence is a
bijection between the solution set of S(A,B,C) and the solution set of
S(A,C,B): `(K,L) valid for S(A,B,C) ⟺ (L,K) valid for S(A,C,B)`. This makes
rigorous (and generalizes beyond a single solution to the whole solution
family) what the round-2 explorer confirmed numerically on one member of
the family. **This closes steps 1-2 of the outline in full — no gap
remains here.**

**New result 2 (proved in full this round, negative): the σ-antisymmetry
mechanism, as conceived, cannot prove T = 0 — it is a vacuous tautology.**

Define, for any actual points A, B, C, K, L in the plane (no hypothesis
required), `O = circumcenter(A,K,L)` (assuming A,K,L non-collinear) and
`T(A,B,C,K,L) := (O − N9(A,B,C))·(C − B)`, where `N9(A,B,C)` is the
nine-point center of triangle ABC. By Lemma 0, `OM=ON ⟺ T(A,B,C,K,L)=0`,
so the goal is exactly `T(A,B,C,K,L) = 0` for the specific (K,L) satisfying
(i)-(iii).

**Claim: `T(A,C,B,L,K) = −T(A,B,C,K,L)` identically, for ALL A,B,C,K,L (no
constraint on K,L needed).**

*Proof.* Two elementary facts:

1. `circumcenter(A,L,K) = circumcenter(A,K,L)` — the circumcenter of a
   triple of non-collinear points does not depend on the order in which
   the three points are listed (it is the unique point equidistant from
   all three, characterized by an unordered set). So the "O" appearing in
   `T(A,C,B,L,K)` is the *same point* O as in `T(A,B,C,K,L)`.
2. `N9(A,C,B) = N9(A,B,C)` — likewise, the nine-point center of a triangle
   is an unordered-vertex-set invariant (circumcenter of the medial
   triangle, whose vertex set {midpoint(A,B), midpoint(A,C),
   midpoint(B,C)} does not depend on vertex order).

Hence `T(A,C,B,L,K) = (O − N9(A,B,C))·(B − C) = −(O − N9(A,B,C))·(C−B)
= −T(A,B,C,K,L)`. ∎

This is confirmed independently via a symbolic computation with fully free
(unconstrained) symbols `Ax,Ay,...,Lx,Ly` in `sympy`: expanding
`T(A,B,C,K,L)` via the O-free reformulation lemma's explicit formula
`½[α(|K|²−|A|²)+β(|L|²−|A|²)]` minus the analogous term for N9 (which is
manifestly the fixed quantity `p/2+1/4` in the WLOG frame, or symbolically
just `N9(A,B,C)·(C−B)`, itself computable but irrelevant to the check),
substituting the swap `B↦C,C↦B,K↦L,L↦K` into the α,β-expression, and
verifying the sum with the unswapped expression is identically 0 as a
rational function of ten free real variables — confirmed
(`sympy.simplify` returns `0` with no side conditions imposed). Concretely,
under the swap, `α ↦ −β` and `β ↦ −α` while `|K|²−|A|²` and `|L|²−|A|²`
exchange, so `α(|K|²−|A|²)+β(|L|²−|A|²) ↦ −β(|L|²−|A|²) −α(|K|²−|A|²)
= −[α(|K|²−|A|²)+β(|L|²−|A|²)]`; this matches fact 1 above exactly (it is
the O-free lemma's own formula reproducing the trivial circumcenter-order-
invariance, as it must, since the lemma is itself an identity).

**Why this proves the mechanism is vacuous.** The identity
`T(A,C,B,L,K) = −T(A,B,C,K,L)` holds for *every* choice of A,B,C,K,L
whatsoever — it uses nothing about K,L being a valid solution of
conditions (i)-(iii), or even about M,N being midpoints. It is, in fact,
strictly weaker than — and entirely subsumed by — the completely trivial
one-line fact that for *any* point O and *any* two points M,N,
`OM² − ON²` is antisymmetric under exchanging the names M and N (swap M,N
in the formula `(Ox−Mx)²+(Oy−My)² − (Ox−Nx)²−(Oy−Ny)²` and the expression
negates — an immediate algebraic tautology, independently re-verified in
`sympy`, needing no geometry at all). Since `T = ½(OM²−ON²)` by Lemma 0's
derivation, and applying σ to the labeled system precisely amounts (via
the correspondence M↔N proved in New Result 1) to relabeling which
midpoint is called M and which is called N, **the "antisymmetry of T under
σ" is nothing more than this trivial relabeling fact in disguise.**
It carries zero information about whether the *specific* real number
`T(A,B,C,K,L)`, for the actual (K,L) satisfying (i)-(iii), equals zero:
a sign-flip identity `f(x) = −f(x')` for a *different* argument `x'` (here
`x' = ` the swapped data, which is NOT the same evaluation point as `x`
unless one already knows `T` doesn't depend on how B,C are labeled — which
is circular, since M,N,C,B are literally exchanged) can never by itself
force `f(x) = 0`. To force vanishing this way one would need `T(x) = T(x')`
also (not just `T(x') = −T(x)`, which is automatic); no such second
relation is produced by relabeling alone, since relabeling produces no new
independent numerical evaluation — as shown above, `(L,K)` valid for
`S(A,C,B)` refers to the *same actual points* K,L in the plane, not a
second, independent configuration, so there is no "second value" to equate
`T(A,B,C,K,L)` to.

**Conclusion.** The σ-antisymmetry mechanism as set out in the outline
(steps 1-4) — "swap labels via σ, observe the target changes sign, conclude
it must be its own negative, hence 0" — is **not a valid proof strategy**
for this problem: its central claimed mechanism (an antisymmetry that
forces vanishing) reduces, after full expansion, to an algebraic tautology
that holds with or without the problem's hypotheses (i)-(iii), and hence
cannot by itself establish `T = 0`. This is a genuine, rigorously
established obstruction, not a computational gap that more effort within
this same framework would close.

**What a genuine rescue would require (open, not attempted to completion
this round).** To make any use of σ, one would need a *non-tautological*
route: e.g., use conditions (6) `∠LBK=∠LNC` and (7) `∠LCK=∠BMK`
*directly* (via the sine rule in the respective triangles LBK/LNC and
LCK/BMK) to derive independent closed-form expressions for the two terms
`α(|K|²−|A|²)` and `β(|L|²−|A|²)` of the O-free lemma's formula for
`T + N9·(C−B)`, and show these two expressions, together with the
`N9`-term, cancel using the *actual content* of (6) and (7) (not just their
formal σ-pairing). This is a genuine trigonometric computation of
comparable difficulty to `complex-number-argument-bash`'s coordinate
elimination (indeed it is likely to be algebraically equivalent to it after
converting the sine-rule expressions to coordinates), and was not carried
out in the time available this round; it does not obviously benefit from
the σ-symmetry beyond a cosmetic halving of casework (compute the K-term,
get the L-term "for free" by swapping (6)↔(7) mechanically) — a real but
modest saving, not the load-bearing vanishing argument originally hoped
for.

**Isosceles sanity check (previously flagged, now confirmed compatible with
the negative result).** When AB=AC, σ IS additionally realized by an actual
geometric reflection isometry (reflection across the perpendicular bisector
of BC, which fixes A and swaps B,C). In that genuinely symmetric case, K
and L become actual mirror images of one another under a real isometry,
forcing O to lie on the axis of symmetry, and OM=ON follows immediately —
because in that special case there really are two configurations
(the original and its mirror image) related by an isometry that also fixes
N9 (N9 lies on the same axis), giving the missing "second independent
evaluation" `T(x) = T(x')` for free (an isometry preserves all distances,
so it doesn't just relabel — it re-realizes the same numeric value at a
genuinely reflected point, and combined with the antisymmetry this really
does force `T=0`). This explains exactly why the mechanism works in the
isosceles case but not in general: **the general (scalene) σ is only a
symmetry of the defining equations (a combinatorial/formal symmetry), not
a symmetry of the plane (an isometry)**, so it produces the sign-flip
identity but not the accompanying equality needed to combine with it.

## Full proof
(none — Status: partial; this approach's own framing has a proven
obstruction and does not by itself yield a proof of OM=ON)

## Promotable lemmas

**Lemma (σ-invariance of the defining system).** With clauses (0)-(7) as
listed above, the formal substitution σ: B↦C, C↦B, M↦N, N↦M, K↦L, L↦K
permutes the clause list into itself (fixing {(0a),(0b)} setwise and (5)
individually; swapping (1)↔(2), (3)↔(4), (6)↔(7)). Consequently `(K,L)`
valid for `S(A,B,C)` ⟺ `(L,K)` valid for `S(A,C,B)`. Proved in full above
(the "New result 1" section). Reusable by any future approach that wants
to invoke this symmetry, but should be paired with "New result 2" below so
nobody re-derives the vacuous consequence as if it were a proof.

**Lemma (vacuity of the naive σ-antisymmetry target).** For all points
A,B,C,K,L (A,K,L non-collinear), with `O=circumcenter(A,K,L)`, `N9` the
nine-point center of ABC, and `T(A,B,C,K,L):=(O−N9)·(C−B)`:
`T(A,C,B,L,K) = −T(A,B,C,K,L)` identically (no hypothesis on K,L needed),
and this identity is entirely explained by (is no stronger than) the
elementary fact that `OM²−ON²` is antisymmetric under exchanging the names
M,N for any point O. Consequently this antisymmetry alone cannot force
`T=0`; a genuine vanishing proof needs a second, non-tautological relation.
Proved in full above (the "New result 2" section, cross-checked
symbolically with unconstrained free variables in `sympy`). This is a
reusable *negative* result: it should prevent any future approach from
re-attempting a "swap labels and conclude antisymmetric ⟹ zero" argument
for this problem's target without first supplying the missing second
relation.
