# Outline Review — imo-2026-03, Round 9

Reviewed the 4-approach field against `current.md`, the three explorer reports, and the
decertified/refuted-move ledger in run_state. No approach re-imports a killed move (false
Structural Lemma, `max(Q)<2^{n−1}⟹A≥2`, the deterministic R3-cascade, or the SB-monotone
route). The anchor crux `T(ℓ)` is DONE and none of the four re-push it. Ranking done
head-to-head across the whole field (stale flags cleared).

---

## ll-inclusion-gap (advance, G-INC-2) — CHANGES REQUESTED

Right technique. This is the natural extension of the certified anchor machinery
(top-band-decomposition + forcing-inc-reduction) to refined R, with G-INC-1 used as a genuine
cheap-kill. Case coverage is complete and disjoint: lower-band cut (k₀≤n−3), equal-split top
cut (a=2^{n−2}), non-equal top cut (a<2^{n−2}, sub-split a≥1 / a<1), plus the f⁺≥f⁻ cheap-kill.
No decertified move re-imported (Parity-Condition used correctly; max(Q)≤max(R) explicitly
flagged FALSE; SET IDENTITY explicitly NOT assumed).

Confirmations I ran:
- Step 3 load-bearing arithmetic **verified**: for G_{n−1}, the max forbidden-band width inside
  [0,2^{n−2}) equals exactly 2^{n−3} and satisfies 2^{n−3} ≤ A(G_{n−2})−1 (tight at n=4,5,
  slack for n≥6). So the equal-split spread bound `p₁−p₂ ≤ max band width ≤ A(R)−1` is sound at
  the band-width level.

Gaps to close while building (all honestly flagged by the outliner):
1. **Step 2 well-foundedness (concern).** The lower-band n→n−2 descent does NOT terminate in
   itself — the explorer notes a lower-band cut recurses until it becomes a *top-piece* cut at a
   smaller level, i.e. step 2 depends on steps 3/4 at smaller n. Make the mutual recursion
   (lower-band ↔ top-piece across levels) explicit and well-founded, and confirm A(R_lo)≥1 holds
   at each descent so the IH (which requires A(R)≥1) actually applies.
2. **Step 3 multi-part subtlety (the real crux of the −1).** The "A(Q)=p₁−p₂ = single band
   width" argument is written for exactly two remaining parts. With |Q|≤n there can be >2
   remaining parts ≤2^{n−2}, so S_{Q-remaining} need not be one interval and A equals a sum of
   band occupancies. The strict `−1` must come from the measure deficit ΣQ−ΣR=1, not merely
   `≤ band width`. Write this for general part count.
3. **Step 4 a<1 sub-case.** The flip [0,a) is interior to the bottom piece, not a genuine cut of
   G_{n−3}; needs the separate careful argument (flagged).

None of these is fatal; the mechanism is stated for each lemma. Build it.

## geometric-selfsimilar (advance, m≥4 UB) — CHANGES REQUESTED

Right technique and it directly repairs the R8 refutation: the deterministic cut-at-pⱼ cascade
is REFUTED (creates a triple, odd parity); this outline uses the **complement cut** at p₁−pⱼ
(creates the invisible pair {pⱼ,pⱼ}), reducing m=4→m=3 at budget b−1, closed by certified
Lemma R4 / Case A.A. Explorer verified the mechanism on 24+ instances incl. hard Case D and
near-equal APs, 0 failures. Does not use the certified-dead SB-monotone route.

Gaps to close while building:
1. **Step 2 overstatement (minor, harmless).** "max(sub)≤Σ'/2, so Case A.A never applies to
   sub" is proven only for the p₁−pⱼ piece; the other sub-pieces (p₂,p₃) need not be ≤Σ'/2 in
   Case β. This is not a hole because Case A.A (max>Σ'/2) is itself *certified closed* — so
   route sub to R4 when max(sub)≤Σ'/2 and to Case A.A otherwise. Reword the claim.
2. **Step 4 algebra (the genuine residual).** Sub-targets 1/2/3 — p₄<Σ/(2D_b) in Case α;
   p₂+p₃>Σ(D_b−1)/(2D_b) in Case β; the sub-not-gap regime — plus proving at least one
   j∈{2,3,4} lands <Σ/D_b (per-case, or the averaging bound Σ_j A_j<3Σ/D_b). This is the whole
   remaining upper bound; the averaging fallback is a sound hedge.

## ll-dyadic-symdiff (advance, bucket iii) — CHANGES REQUESTED

Distinct whole-attempt route to the full LB (measure(S_Q△S_R), not the INC formula), so it is a
legitimate rival to ll-inclusion-gap on an overlapping-but-different residual, not a split
proof. Cheap-kill (disjoint sub-case) and double-REFL are both sound and REFL-gen is certified;
the reduction to a smaller (B2*)-ref object is verified on the concrete n=3 instance
Q=[15/4,13/4,1], R=[15/4,2,1,1/4]. n=3 base is concrete casework (parity |Q|=3 vs |R|=4).

Gap to close while building:
- **Step 3 termination is the load-bearing open piece and must be PROVEN, not asserted.** R7
  already recorded that "naive recurse one level" does NOT terminate (q₂>2^{n−2}); the outline
  correctly flags this ("Termination of the telescoping is NOT automatic — prove it") and
  proposes descent on Σ of the reflected multiset. Builder must give the well-founded measure
  explicitly and show each REFL step strictly decreases it down to a certified R-agnostic case /
  the disjoint kill. This is the harder of the two LB residuals — but the technique is right.

## refined-r-alt-tail (NEW) — RETHINK / CUT (not registered, not built)

Fatal-for-this-round on two counts:

1. **Its distinctive load-bearing step has no mechanism.** The slug's only genuinely new content
   over the two advances is the {Claim_R(n,ε), T_R(n)} mutual induction. Its inductive step
   requires a descent identity relating the lower half of S_R to a level-(n−3) refined system.
   The outliner itself flags this identity as **UNKNOWN**, and BOTH explorers independently give
   the structural reason it fails: the anchor's SET IDENTITY `S_{G_{n−1}}∩[0,2^{n−2})=S_{G_{n−3}}`
   does NOT transfer — for refined R it becomes `S_{G_{n−3}} △ flip` with a non-trivial,
   non-empty flip term. A named induction whose central descent lemma is admitted to be unknown
   with a concrete obstruction is an unverified hand-off, not a build.

   This is NOT "the same posture that preceded the anchor breakthrough": the anchor's mutual
   induction already had its key tool (the certified SET IDENTITY) in hand and only had to grind
   T(ℓ); here the key tool is *absent with a proof it doesn't exist in the naive form*. That is
   the difference between "one gap to grind" and "no mechanism."

2. **Its non-distinctive content (step 1) is redundant.** The reduction of G-INC-2 and bucket
   (iii) onto a single T_R is exactly what ll-inclusion-gap step 2 (top-band decomp with A(R))
   and ll-dyadic-symdiff steps 2–3 (double-REFL → (B2*)-ref) already carry. Building this slug
   would re-derive convergence the two advances hold and then stall at the same unknown T_R.

The outliner explicitly invited this cut ("if the outline-reviewer judges it redundant, drop
it"). Cut it — spend the slot advancing the two live LB routes. It may be revived later ONLY if
an explorer produces a concrete candidate for the flip-tracking descent identity; without one it
has nothing a builder can execute.

---

## Ranking (updated, stale cleared)

geometric-selfsimilar 1685.7 > ll-inclusion-gap 1619.9 > ll-dyadic-symdiff 1516.6 >
alternating-sum-value 1398.9 > extremal-smoothing 1279.0.

Rationale: geometric's remaining UB residual (m≥4) now has a concrete, 0-failure-verified
mechanism (complement cut) — cleaner than either LB route's refined-R descent, so it stays
leader. ll-inclusion-gap's G-INC-2 has the more tractable path (band-width arithmetic confirmed,
cheap-kill covers many cases) than ll-dyadic's bucket-iii, whose termination argument is still
unproven — so inclusion > dyadic. Both live LB routes beat the dormant alternating-sum-value
(last built R3) and extremal-smoothing (S1 stuck 4+ rounds, last-placed). No new slug registered
(refined-r-alt-tail cut). No copy warranted.

build set: geometric-selfsimilar, ll-inclusion-gap, ll-dyadic-symdiff
