# Proof-reviewer report — imo-2026-03, Round 13

Reviewed three approaches built this round. All three builders self-reported **partial** with honest gaps
— none claimed `solved`, and I confirm no overclaim in any of them. Each delivered a rigorous, certifiable
lemma. Verdict per slug: **CHANGES REQUESTED** (partial, real progress, gap remains) for all three.

Run Status stays **partial**. The problem is NOT solved: the upper bound is still blocked past n=3
(T5/n=4 UB open) and the lower bound still needs distinct-top |Q_lo|≥3, refined multi-cut R, and the
non-containment (non-Q-top) piece.

---

## 1. geometric-selfsimilar (UB) — CHANGES REQUESTED — Status: partial

**Lemma HS-A2: CERTIFIED.** Closes the Sub-A-P branch of T5 (m=5, δ>2t): `pair2_3` leaves
`Y″={p₁,d₂,p₄,δ}` at budget 3 with `min A(Y″,3) ≤ t`, hence `μ(X,4) ≤ t` on that branch.

Verification performed:
- Re-derived the Σ-P bound `[*] 2d₂ ≤ 31t−7δ−6d₄−4d₃` from scratch (telescoping `d₁=31t−5δ−4d₄−3d₃−2d₂`,
  `D1_{Y'}=d₁−p₃=31t−6δ−5d₄−4d₃−2d₂`, firing `≥ δ+d₄`). Correct.
- Re-derived all 6 case bounds by hand: A (`d₂−p₄<t/2`), B1 (`d₂−δ<t`), B2 (`d₄−t<t/6`), C1 (`δ−d₂≤t`),
  C2 (custom halve-p₁ ⟹ `|d₄−d₂|<t`, both `d₂,d₄∈(t,2t)`), C3 (`[*]` ⟹ `2d₂<0`, vacuous). All correct.
  Split is exhaustive (on `d₂` vs `p₄,δ`) and disjoint.
- **Independently confirmed the CONCLUSION** `min A(Y″,3) ≤ t` via an achievable-strategy search
  (matching/halving cuts — an upper bound on the true game minimum, so `≤t` proves XY can force it) over
  targeted off-grid exact-Fraction configs hitting **all live cases** (A=27, B1, B2=21, C1, C2=556; worst
  achievable value = 1.0·t; **0 violations**). C3 confirmed empty.
- **C2 correction verified.** The outline's "P fires, `A_P ≤ d₂/2`" is genuinely false; the custom
  halve-p₁ closure (halve p₁ invisibly, cut p₄@δ → effective `{d₄,d₂}`, finish) is valid and achieves
  `A ≤ |d₄−d₂| < t`. My search found C2 configs exist and are all `≤ t`.

**No overclaim.** Builder correctly states T5 and the n=4 UB are NOT proven: the pair1_2 success region
(Sub-A-C, Sub-B, all δ≤2t; gap G1, ~40k configs, numerics only) is open, and m≥6 (G3/HS-A3) untouched; the
step tree is not uniform in m. Recorded Status `partial` is correct.

**Gap remaining:** G1 (the pair1_2 merge family for δ≤2t / Sub-A-C / Sub-B) and m≥6. The builder's suggested
"halve-p₁-then-3-piece" template for G1 is a reasonable next target.

## 2. ll-inclusion-gap (LB) — CHANGES REQUESTED — Status: partial

**Lemma size2-Qlo-closure: CERTIFIED (within its stated scope `a∈[1,2^{j+1})`).** For the `a≥1`, `h=2` top
cut, the size-2 `Q_lo` case closes for EVERY `n`, every `a∈[1,2^{n−2})`: `A(R_lo)−A(Q_lo)≥A(G_{j−1})≥1`.

Verification performed:
- Re-derived Regime A (`a<2^j`: `ΣQ_lo>ΣR_lo` forces `p₁>2^j`; if `p₁>p₂` then `S_{Q_lo}` reaches above
  `2^j` but `S_{R_lo}⊆[0,2^j)` — contradiction, so `p₁=p₂`, `A(Q_lo)=0`, Floor Lemma) and Regime B
  (`a≥2^j`: `A(R_lo)=a−A(G_j)`; parity forces `p₂≥2^j` and `p₁≤a`, so `A(Q_lo)≤a−2^j`, giving the bound
  `≥2^j−A(G_j)=A(G_{j−1})`). Both correct.
- Confirmed the identity `A({a}∪G_j)=a−A(G_j)` for `a∈[2^j,2^{j+1})` (exact, j=1..4).
- Verified **0 violations over 18386 off-grid configs** (`a≥1`, dens 8, j=1,2,3), 225 tight at `A(G_{j−1})`.
- **Scope note:** violations DO appear for `a<1` (e.g. j=1, a=1/8, `A(R_lo)−A(Q_lo)=7/8<1`), but `a<1` is
  outside this lemma's scope; the approach's usage (`a∈[1,2^{n−2})`) is entirely `a≥1`, and the `a<1`
  branch is handled by the separately certified Family Lemma `sigma-family-a-lt-1`. Not a gap.
- **Verified the KEY NEGATIVE FINDING:** the "large slack for size≥3" premise is FALSE. Reproduced the tight
  size-4 witness `n=6, a=2, R={1,2,4,8,16,2,30}, Q={30,16,8,4,3,3}`: A(R)=19, A(Q)=18, `A(R)−A(Q)=1`
  exactly, INC (`S_Q⊆S_R`) holds. So the distinct-top `|Q_lo|≥3` crux is genuinely tight — same tier as the
  anchor mutual induction; it cannot be closed by a band-accounting slack argument. Corrected target
  `DFB≥1−deficit_top` is right.

**No overclaim / honesty.** Did NOT revive the refuted `T'(j)`/`{Claim_R,T_R}` mutual induction, nor
"INC⟹max(Q)≤max(R)", nor unconstrained L1. Recorded Status `partial` is correct.

**Gap remaining:** distinct-top `|Q_lo|≥3` (tight), the `h=0, a∈(2^{n−2}−1,2^{n−2})` sliver, refined
multi-cut R (G-INC-2), and G-GAP (non-containment).

## 3. ll-dyadic-symdiff (LB) — CHANGES REQUESTED — Status: partial

**Lemma BR (bottom-restriction): CERTIFIED.** `A(Q∪R) ≥ measure{x∈[0,τ):g odd}`; with `τ=min(Q)`,
`A(Q∪R) ≥ B=measure{x∈[0,min(Q)):N_R(x)≢|Q| mod 2}`.

Verification performed:
- The proof is a correct one-line measure-monotonicity argument (`{g odd}⊇{g odd}∩[0,τ)`) plus the fact
  that `N_Q≡|Q|` on `[0,min(Q))`. Rigorous.
- **Confirmed it is a genuine BYPASS**, not a disguised alternating-tail argument: it uses no bound on
  `max|g|`, no reflection identity, and no Sub-3a hypothesis. `Q` enters only through the single integer
  `|Q|`.
- **Q-top reduction sound.** For `min(Q)≥2^{n−2}`: `|Q|∈{3,4}` (each part in `[2^{n−2},2·2^{n−2})`,
  `ΣQ=4·2^{n−2}` ⟹ `2<m≤4`). The within-bottom parity identity (PAR) correctly eliminates `Q`, reducing
  `A(Q∪R)≥1` to the R-only (★R): `|Q|=4⟹A_R^{bot}≥1`, `|Q|=3⟹A_R^{bot}≤2^{n−2}−1`. Reduction is valid.
- **n=3 not presented as new progress** — builder explicitly notes it was closed in R9 and that the
  single-R-cut sub-case is subsumed by the certified Sub-3a. Correct.

**No overclaim.** (★R) is verified (0 violations, n=3,4,5, both tight) but explicitly **NOT proved** — the
honest open residual. The non-Q-top slice (`min(Q)<2^{n−2}`) is not covered. Recorded Status `partial` is
correct.

**Gap remaining:** prove (★R) (Q-free parity inequalities on a budget-`≤n−m+1` refinement of `G_{n−1}`),
and the non-Q-top residual (bottom window shorter than one level).

---

## Certifications

| Lemma | File | Verdict |
|---|---|---|
| HS-A2 (Sub-A-P branch, m=5, δ>2t) | `lemmas/HS-A2.md` | **CERTIFIED** |
| size2-Qlo-closure (a≥1, size-2 Q_lo) | `lemmas/size2-Qlo-closure.md` | **CERTIFIED** (scope `a∈[1,2^{j+1})`) |
| BR (bottom-restriction bypass) | `lemmas/BR-bottom-restriction.md` (created) | **CERTIFIED** |

All three lemma files updated with certification status; `current.md` updated with an R13 progress block.

## Goal Progress

- **Status: partial** (unchanged — no solve; all three verdicts CHANGES REQUESTED).
- **Elo snapshot (post-outcome, stale pending outline-reviewer re-rank):**
  geometric-selfsimilar 1771.74 > ll-inclusion-gap 1644.75 > ll-dyadic-symdiff 1501.63 >
  alternating-sum-value 1368.37 > extremal-smoothing 1213.52.
- **Net movement:** three certified lemmas this round (HS-A2, size2-Qlo-closure, BR), all `advanced`. The
  UB leader closed one more m=5 branch (Sub-A-P/δ>2t) but the m=5 UB (G1) and n=4 UB remain the real
  blocker. Both LB tracks sharpened but hit *tightness walls* on their next sub-target (distinct-top
  |Q_lo|≥3 is provably tight for inclusion-gap; (★R) is verified-tight-but-unproved for dyadic-symdiff),
  confirming the shared LB crux is genuinely hard, not an artifact.
