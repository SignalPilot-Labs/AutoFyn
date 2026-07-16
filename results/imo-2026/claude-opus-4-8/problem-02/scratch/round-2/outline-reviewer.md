# Outline Review — imo-2026-02 (IMO 2026 P2), Round 2

Reviewed the field the outliner handed up against the two terrain reports, the approach files, the
certified algebraic core, and a fresh numerical check of the revised §3 skeleton across 3 triangles ×
4 alpha values each. Independent verdict below.

## complex-reality-conditions — APPROVE (revise + advance; PRIORITY BUILD)

The technique is right and the revised §3 directed-angle skeleton is **sound in principle**. I stress-tested
every load-bearing claim numerically (12 configs):

- **C1, C2, C3 are real and positive** in every config (imag parts ~1e-13, reals all > 0). Crucially each
  `arg C_i ≈ 0`, never `≈ π` — so the *equal* branch is realized, never the supplementary one. This is the
  exact thing §3 must prove.
- **The midpoint factors `2l−c`, `2k−b` are correct.** I evaluated `C2 = (k−b)(2l−c)/(c(l−b))` and
  `C3 = b(k−c)/((l−c)(2k−b))` directly and got real-positive values. A `l−c` or `k`-in-numerator slip would
  have broken reality — it did not. `∢(NL,NC)=arg(c/(2l−c))` and `∢(MB,MK)=arg((2k−b)/b)` follow verbatim from
  `N=c/2`, `M=b/2` (`L−N=(2l−c)/2`, `K−M=(2k−b)/2`) — this is exact algebra, not an approximation.
- **The interior-positivity facts that pick the equal branch all hold strictly:** `signed_area(B,K,C)>0`,
  `signed_area(N,C,L)>0`, `signed_area(B,M,C)>0`, `signed_area(B,N,C)>0`, `Im(c/(2l−c))>0`, `Im((2k−b)/b)>0`
  in all 12 configs. And they are the *right* equivalences: `Im(c/(2l−c))>0 ⟺ Im((C−N)·conj(L−N))>0`
  (same sign, since `(C−N)conj(L−N)=c(2l̄−c̄)/4` and `c/(2l−c)=c(2l̄−c̄)/|2l−c|²`); `Im((2k−b)/b)>0 ⟺ Im(k b̄)>0`,
  which is exactly "K on the C-side of line AB" — and line `BM` **is** line `AB` (M is the midpoint of AB, so
  B, M, A are collinear), so the outline's "K on C-side of BM" is literally the interior-of-BMC condition. The
  mechanism checks out.

The downstream spine (§1 circumcenter Lemma 1, §4 Cramer solve in monomials `(k̄l̄, k̄, l̄)`, §5 identities
(I) `Rnum=(b−k)(c−l)G` and (II) `num=qN·G`, §6 `G=0 ⟹ TN=0 ⟹ OM=ON`, and the continuity removal of
`det A≠0`) is already machine-certified in `repro.py` and unchanged — I did not re-audit it (certified round 1).

**Issues the builder must close (CHANGES-level, to be done while building — do not hand-wave):**
1. The step "full directed angle ∈ (0,π) ⟹ unsigned angle = that directed angle ⟹ unsigned equality forces
   exact equality of the two directed angles." This is the true hinge and the only place a hidden gap could
   lurk. The builder must state that the unsigned `∠UPV ∈ [0,π]` equals the full argument `arg((V−P)/(U−P))`
   precisely when that argument lies in `(0,π)`, and that the two positivity sub-steps establish exactly this
   for each of the two rays — so the problem's unsigned equality gives difference `= 0` (not merely `≡ 0 mod π`,
   since the difference of two numbers in `(0,π)` lies in `(−π,π)`). Write it, don't assert it.
2. Each of Steps 0–3 must be a genuine signed-area inequality derived from "interior of the named CCW triangle
   / angle," **not** "verified at the audited config." The round-1 downgrade was precisely for numeric-only
   assertion; a repeat will be downgraded again.
3. Keep the reflection remark for the CW-labelling orientation dichotomy (already noted in §3).

This is one translation lemma away from a complete, machine-certified proof and is the only realistic path to
`solved` this round. Build it.

## antipode-perp-bisector — CHANGES REQUESTED (advance; breadth, secondary)

Right technique for an independent route (never touches (★★)). Step 1 (`OM=ON ⟺ A*B=A*C`, A*=2O−A) is a
verified vector identity; Step 2 (Thales location of A*) and Step 3 (projection onto BC) are sound in outline.
**The Step 4 crux (`A*B²=A*C²` from C1,C2,C3) has no validated mechanism** — the file offers only a "candidate
mechanism," which is an unverified hand-off, and the crux terrain warns it "may be no easier than (★★)." This is
genuinely risky. Kept live for breadth because it is a truly distinct route and can now borrow the directed-angle
machinery (midpoint factors, interior signs) just written into complex §3. Realistic outcome this round is a
firmer Step-3 projection identity plus a Step-4 attempt, i.e. a `partial`, not a solve. Build it as breadth
insurance — it must not displace or delay the complex build.

## trig-decoupled-bash — HOLD (do not advance). Shared-gap plateau — agree.

Fully reduced to (★★) in round 1, unchanged since. The crux explorer confirms (★★) ∈ ⟨(I),(II)⟩ only via a
Gröbner certificate with non-human-presentable cofactors, and no clean small-coefficient factorization exists.
Dispatching a builder reproduces a "numerically verified, symbolically unproven" partial. Correct to hold. Note:
the complex route already bypasses (★★) entirely (works with conjugates), satisfying CLAUDE.md's break-the-plateau
guidance without a new explorer this round.

## power-of-point-balance — HOLD (do not advance). Same plateau.

Crux explorer §1 confirms its residual identity is the *same* (★★) as trig (`2O·(B−C)=(b²−c²)/2`), same Gröbner
obstruction. Hold.

## Registration / ranking

No new slugs to register (complex revised in place, keeps its slug; antipode already registered). No copies
requested. Ranking updated head-to-head across the whole field (stale flags cleared):

- complex-reality-conditions **1548** (was 1502) — closest to solved, clear certified path, `advanced` last round → beats all.
- trig-decoupled-bash **1522** — fully reduced but at a confirmed hard plateau → below complex, above antipode.
- power-of-point-balance **1514** — same plateau, drew with trig.
- antipode-perp-bisector **1416** — independent but Step-4 crux entirely open/unvalidated → bottom.

build set: complex-reality-conditions, antipode-perp-bisector
