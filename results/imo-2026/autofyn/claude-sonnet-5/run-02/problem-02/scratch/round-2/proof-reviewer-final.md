# Final-pass review: complex-number-argument-bash (IMO-2026-02)

## Verdict: APPROVE — Status: solved

The proof in `results/imo-2026-02/approaches/complex-number-argument-bash.md`
(§0-§6 "Full proof") is correct and complete. `current.md` has been rewritten
by this review to Status `solved` with the full proof text (it previously
said `partial`, reflecting the pre-round-3-builder-update state — now fixed).

## What was independently re-verified (all from raw definitions, fresh sympy,
not from the builder's intermediate formulas)

1. **Lemma 0 (nine-point-center reduction).** `PM²-PN²=(2P-M-N)·(N-M)` is
   the standard difference-of-squares identity — re-derived by hand and
   confirmed. `OM=ON ⟺ O_x=p/2+1/4` in the WLOG frame follows exactly as
   claimed (N9 on the vertical perpendicular bisector of the horizontal
   segment MN, at x=(p/2+(p+1)/2)/2=p/2+1/4). Already certified round 1;
   re-confirmed here.

2. **eq1, eq2, eq3.** Rebuilt directly from `cross`/`dot` on `K-B,A-B,A-C,
   L-C` etc. Matches the file's displayed expansions exactly.

3. **l2-elimination (Step 1).** Used `sympy.solve(eq1=0, l2)` directly (not
   the builder's displayed closed form) and got exactly `-l2_num/D` — i.e.
   the corrected sign flagged by the round-2 (intermediate) reviewer. Fresh
   confirmation, matches.

4. **Cubic locus X (Step 2/§4).** Substituting the l2-solution into eq3 and
   factoring gives `eq3_num = -(l1-1)(p²+q²)·X` with `X` matching the file's
   displayed cubic term-for-term. `sympy.factor_list` confirms `X` is a
   single irreducible factor over `Q(p,q)[k1,k2]`.

5. **eq2_num (Step 3/§4).** Degree 2 in `l1`, total degree 3 in `(k1,k2)` —
   confirmed exactly, matching the (corrected) round-2 figure, not the
   round-1 figure of 6 (a bookkeeping slip, non-load-bearing, already noted
   in the file).

6. **Closing identity (‡) (§5).** Computed the circumcenter of `A,K,L` via
   the standard formula, eliminated `l2`, formed `Fn_num_raw`, `Fn_den_raw`,
   `D_circ`, and checked `Fn_den_raw = 4·D·D3`, `D_circ = 2·D3/D`, and the
   identity `Fn_num_raw·D2 − (k2−q)·eq2_num = D·X·(E1·l1+E0)` by
   `sympy.expand(LHS-RHS)` — result is the exact zero polynomial. This is
   the single deepest load-bearing computational claim in the whole proof
   and it reproduces exactly, independently, from scratch.

7. **Orientation argument (§3, "Master Fact" toolkit) — the new closure.**
   Re-derived every one of the six cross-product sign facts (a)-(f):
   - (a) `cross(A-C,K-C)>0` (from K∈△BMC at vertex C): confirmed
     `cross(A-C,B-C)=q>0` by hand.
   - (b) `cross(L-B,A-B)>0` (from L∈△BNC at vertex B): confirmed
     `cross(A-B,C-B)=-q<0` ⟹ sign flip gives the claim.
   - (c) `cross(K-B,A-B)>0`, `cross(L-B,K-B)>0` (from K∈∠LBA + (b)):
     confirmed via the cone criterion.
   - (d) `cross(A-C,L-C)>0`, `cross(L-C,K-C)>0` (from L∈∠ACK + (a)):
     confirmed via the cone criterion.
   - (e) `cross(L-N,C-N)>0` (from L∈△BNC at vertex N): confirmed
     `cross(B-N,C-N)=q/2>0` by direct hand computation.
   - (f) `cross(B-M,K-M)>0` (from K∈△BMC at vertex M): confirmed
     `cross(B-M,C-M)=q/2>0` by direct hand computation.
   All six checks reproduce exactly (I re-derived each cross product by
   hand, not just trusted the file). These give `ε1=ε2=+1` for all three
   Dictionary-Lemma pairings used to build eq1, eq2, eq3.

   **Non-circularity check (specifically requested).** The sign facts (a)-
   (f) are derived purely from the four containment hypotheses (K∈△BMC,
   L∈△BNC, K∈∠LBA, L∈∠ACK) applied to a fixed-but-arbitrary valid pair
   `(K,L)` — at no point does the derivation assume `eq1=0`, `eq2=0`, or
   `eq3=0`. The containment hypotheses are given data of the problem,
   independent of the angle-equality hypotheses that eq1/eq2/eq3 encode.
   So there is no circularity: the argument establishes orientation-
   matching *before* concluding eq1=eq2=eq3=0, using only the four
   containment facts, which is the correct logical order.

   **Necessity check (specifically requested).** I verified by hand that
   the orientation-matching step is load-bearing, not vacuous: expanding
   the Dictionary Lemma's cross-dot combination with `θ1=θ2=θ` but
   `ε1≠ε2` gives `2|u||v||w||z|sinθcosθ`, which is generically NONZERO —
   i.e. if the orientations were mismatched, `eq1=0` would encode the
   *supplement* `θ1+θ2=π`, not the given equality `θ1=θ2`. So proving
   `ε1=ε2=+` for all three pairs really is necessary to legitimize
   `eq1=eq2=eq3=0` as the correct translation, and this is exactly what §3
   accomplishes, generally (for every valid `(K,L)` at every triangle shape
   `q>0`), not just at a numeric witness.

   **General validity for all q>0.** Every step in §3 is symbolic in
   `p,q,k1,k2,l1,l2` with only `q>0` used (never a specific numeric
   triangle) — confirmed by re-deriving all the cross-product formulas
   symbolically. So the closure genuinely covers the whole family, not
   just the numeric witness triangle mentioned earlier in the file.

8. **D≠0, D2≠0 (§3, replacing round-2's resultant/continuity argument).**
   Re-verified `eq1 = S(l1-1) - D·l2` as an exact polynomial identity
   (`sympy.expand(eq1 - claim)==0`). Re-verified `D2 = -cross(K-B,A-C)`
   exactly. Re-verified the determinant of the `D=S=0` linear system
   equals `-|A-B|²|A-C|² < 0` exactly (`sympy.expand` match). Both proofs
   are fully elementary: `D≠0` from `l1≠1` (L≠C, an open-interior exclusion)
   plus a nonsingular 2×2 linear system forcing `K=B` (contradicting K's
   strict interior); `D2<0` from a positive-combination expansion of
   `K-B` at vertex B of △BMC combined with `cross(A-B,A-C)=cross(C-B,A-C)
   =q>0`. Neither invokes genericity, resultants, or continuity — this is a
   strictly stronger and fully closed replacement for the round-2
   Step-5 argument (which the round-2 intermediate reviewer had flagged as
   having one honestly-admitted bookkeeping gap). That gap no longer exists
   in the final proof.

## Answer-format check

Read `problems.jsonl` for `imo-2026-02`: `"task": "proof_only"`,
`"answer_type": "none"`. This is a pure proof problem (prove OM=ON), no
numeric/expression answer to state or verify. The rigor-rule requirement
"verify final answers" does not apply here beyond proving the stated
equality, which §0-§6 does in full.

## Case completeness / hand-waving check

- All four containment hypotheses (K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK) and all
  three angle-equality hypotheses are used explicitly and are load-bearing
  (traced explicitly in the file's "Summary" section and independently
  confirmed here): the three angle equalities build eq1/eq2/eq3; the two
  triangle-containments give (a),(e),(f) and the D≠0/D2≠0 proofs; the two
  angle-containments give (c),(d).
- The `l1=1` branch (L=C) is correctly excluded as violating L's strict
  interior to △BNC — not silently dropped.
- Non-degeneracy of triangles BMC, BNC (needed for the barycentric/cone
  characterizations in §3) follows automatically since M,N lie on lines
  AB,AC respectively and ABC is non-degenerate.
- No hand-waving words ("clearly", "obviously", "it follows") hide any
  non-trivial step; every claimed cross-product sign and every polynomial
  identity is derived or points to an explicit computation, and I checked
  every one of them.
- No skipped cases: the genericity conditions D≠0, D2≠0 are now proved
  unconditionally (not "for all but finitely many configurations"), so
  there is no residual exceptional-case bookkeeping left, unlike the
  round-2 intermediate version.

## Lemma certification

- `lemmas/dictionary-lemma-equal-signed-angle.md` — already certified
  (round 1), re-confirmed; the file's own caveat about needing a separate
  orientation-matching argument is exactly what §3 supplies.
- `lemmas/nine-point-center-reduction.md` — already certified (round 1),
  re-confirmed.
- `lemmas/cubic-locus-for-K.md` — was flagged with an open "geometric
  certification" caveat (orientation-matching not yet proved). I updated
  this lemma file to mark the caveat RESOLVED, referencing §3's closure,
  since it is now proved and independently re-verified.
- `lemmas/closing-polynomial-identity-step4.md` — already certified
  (round 2), re-confirmed exactly by fresh independent recomputation in
  this review (identity (‡) reproduces byte-for-byte with the file's
  stated polynomials `D2, E1, E0`).
- `lemmas/sigma-invariance-and-vacuity.md`, `lemmas/o-free-circumcenter-
  reformulation.md` — not used in the final proof; no action needed
  (already certified/negative-result lemmas from prior rounds, left as is).

## current.md

Rewrote `results/imo-2026-02/current.md`: `## Status` set to `solved`,
`## Full proof` populated with the complete §0-§6 argument plus a
verification-notes section documenting this review's independent
re-derivation. `## Approaches tried` updated to record the APPROVE.

## Outcome recorded

`record_outcome` called for `complex-number-argument-bash`, round 2,
outcome `verified-milestone`, noting the final gate passed (independent
re-derivation of every symbolic claim + non-circularity/necessity checks
on the new orientation argument).

## Files touched by this review

- `/home/agentuser/repo/results/imo-2026-02/current.md` (rewritten:
  Status → solved, Full proof added)
- `/home/agentuser/repo/results/imo-2026-02/lemmas/cubic-locus-for-K.md`
  (caveat marked resolved)

No changes made to the approach file itself (it was already correct as
written).
