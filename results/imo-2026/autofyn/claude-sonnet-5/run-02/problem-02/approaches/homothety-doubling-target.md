## Status
unsolved

## Approaches tried
(none yet — this is the initial skeleton, round 1)

## Current best

**Reformulated target (proved equivalence, not yet the final theorem).** Let
h be the homothety centered at A with ratio 2. Since M, N are midpoints of
AB, AC, h(M) = B and h(N) = C exactly. Let O' = h(O) = 2O − A, K' = h(K) =
2K − A, L' = h(L) = 2L − A.

- **O' is the circumcenter of A, K', L'.** Because h scales all distances
  from its center A by the factor 2, and O is equidistant from A, K, L (it
  is their circumcenter), O' = h(O) is equidistant from h(A)=A, h(K)=K',
  h(L)=L' — i.e. O' is the circumcenter of triangle A K' L'.
- **h maps the perpendicular bisector of MN exactly onto the perpendicular
  bisector of BC**, since h(M)=B, h(N)=C and h is an affine bijection whose
  linear part is a positive scalar multiple of the identity (hence preserves
  perpendicularity and midpoint/bisector relations).

Consequently:

  **OM = ON ⟺ O'B = O'C ⟺ O' lies on the perpendicular bisector of BC**
  (the line through the circumcenter O_ABC of the original triangle ABC,
  perpendicular to BC).

**Useful algebraic identities (direct computation, already verified):**
`K' − B = (2K − A) − B = 2K − (A+B) = 2K − 2M = 2(K − M)`, and symmetrically
`L' − C = 2(L − N)`. So K' relates to B exactly as K relates to M (doubled),
and L' relates to C exactly as L relates to N (doubled) — meaning the
conditions (ii) ∠LBK = ∠LNC and (iii) ∠LCK = ∠BMK, which directly reference
M and N, may become more transparent once phrased through K', L' relative to
B, C.

**Planned route (unproved beyond this point).**

1. Apply the same Lemma-0-style algebra used elsewhere, but now with
   reference point O_ABC (circumcenter of ABC, which is trivially equidistant
   from B and C) in place of N9: `O'B² − O'C² = 2(O' − O_ABC)·(C − B)`, so
   the goal becomes `(O' − O_ABC)·(C − B) = 0`.

2. Express O' − O_ABC using the circumcenter-of-AKL formula scaled by h, and
   the identities K'−B = 2(K−M), L'−C = 2(L−N), converting the angle
   conditions (ii), (iii) (originally phrased via M, N) into direct
   statements about K', L' relative to B, C. Carry out the resulting
   sine-rule / coordinate computation to check whether
   `(O' − O_ABC)·(C − B) ≡ 0` — this is the crux computation, not yet
   attempted, and is structurally analogous to the corresponding step in the
   nine-point-center-frame approaches, just in a different (B,C-relative)
   coordinate frame.

## Full proof
(not yet established — Status: unsolved)

## Notes for the builder
- Steps involving the homothety h are bookkeeping and already fully
  justified above; they do NOT by themselves make progress on the hard part
  of the problem. The only genuine bet this approach makes is that phrasing
  the final angle-condition algebra relative to B, C (via K', L') is shorter
  than phrasing it relative to M, N (via K, L directly, as in the
  nine-point-center approaches). If step 2's computation is not visibly
  easier after a reasonable attempt, abandon this approach in favor of the
  nine-point-center-frame approaches rather than duplicating effort.
- No new cases beyond the generic scalene triangle.

## Round-2 finding: algebraically redundant with the leader — deprioritize

A round-2 explorer (`math-explorer-fresh-framing`) checked step 2's crux
computation and found it is algebraically ISOMORPHIC to
`complex-number-argument-bash`'s cubic-locus/cofactor-identity computation
up to an affine change of coordinates (replace `N9` by `O_ABC`, `K/L` by
their `×2`-homothety images `K'=2K-A, L'=2L-A`). This does NOT reach a
genuinely different variety or offer an independent proof route — it is the
same computation in a shifted frame, so it inherits the same gap with no
shortcut. **Recommendation: do not dispatch a builder to this approach this
round.** It is retained in the population as a record of a checked-but-
redundant framing, not as an active line of attack, unless a future round
identifies a concrete reason the shifted-frame algebra is shorter (currently
unverified and considered unlikely).
