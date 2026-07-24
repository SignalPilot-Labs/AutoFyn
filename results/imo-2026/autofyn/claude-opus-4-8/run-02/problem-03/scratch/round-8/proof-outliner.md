## imo-2026-03

Context: the whole problem is ONE gap from solved. Upper bound `c(n) ≤ 2^n/D_n` (D_n=2^{n+1}−1) is
CERTIFIED. Answer `c(n)=2^n/D_n` pinned. Sole residual: **f ≥ 1 at the tied non-degenerate minimizer**
= "minimality ⇒ benign visible reduced subsystem" (Cramer certified: primal |det U^★|=1 ≡ dual f∈ℤ).
Round-8 decisive convergence across all three explorers: every LOCAL/variational lever is a V-kink
(dead), and the closing move for BOTH Gap A′ (deg≥3 cycle-piece) AND Gap B (μ=3 even-leaf) AND the dual
Budget Lemma is ONE **global residual-complement strong induction on cut count N**, exploiting that
BF-invisible (even) tie-blocks contribute exactly 0 to f (certified `odd-block-formula`). Field below
advances the three live routes on their distinct machinery and opens ONE new slug that pursues the
unification directly with two gap-fills.

---

### unified-residual-budget-induction: new
Target: The whole IMO-2026-P3 claim — Liu Bang's guarantee is exactly `c(n)=2^n/D_n`. Imports the
CERTIFIED upper bound (Xiang Yu strategy, alternating-sum-threshold-potential) and the CERTIFIED LB
reduction (LBL) that leaves the single tied-non-degenerate residual `f ≥ 1`; this approach closes that
residual via a global induction on cut count N, finishing the lower bound and hence the whole problem.
Technique: Strong induction on N (total cut count), with a **BF-invisible-block removal** step — the
spine is a monovariant/descent on N (Claim(N) ⇐ Claim(N−k)), NOT a determinant or a local variational
move. This is the shared closing engine the three explorers independently converged on.
Skeleton:
  1. Setup: at the Φ=Σx²-max non-degenerate global minimizer P* of a ≤N-cut refinement of W_n,
     import certified S-core (ker U=0), M2 (μ_{k,j}≤3), M3 (odd blocks carry μ_{k,j}≤1), and the
     block formula BF: `f(P*) = Σ_{odd tie-blocks j} σ_{a_j} w_j`; every EVEN tie-block contributes 0.
  2. Dichotomy on P*: either (i) P* is BF-invisible-block-free apart from trivial within-piece
     bisection pairs — then certified leaf-peeling (import concentration Reduction Lemma) reduces to a
     forest, integrality gives `f=Σ ε_k 2^k` odd ≥1; OR (ii) P* carries a NON-trivial BF-invisible
     structure B — one of: a μ=3 even leaf (Gap B), a deg≥3 cycle-piece with off-cycle/chord even mass
     (Gap A′ case (b)), or a multi-piece even tie-block. Case (i) is the certified Claim already in hand.
  3. **Cut-cost bound (KEY, gap):** any non-trivial BF-invisible block B of total size t spanning ≥2
     original dyadic pieces costs ≥ t cuts to manufacture — because its shared value v is never a power
     of two (else it is an uncut piece and B is trivial), so every one of the t copies of v sits inside
     a piece that must be split, and the superincreasing bound Σ_{a<k}2^a < 2^k forbids realizing v as
     an uncut remainder. Hence removing B frees ≥ t ≥ 3 cuts.
  4. **Residual-complement decomposition (KEY, gap):** the complement P' = P* with block B deleted and
     B's donor mass reattached is a legitimate ≤(N−k)-cut refinement of W_n (or of a rescaled
     sub-stick), and by BF (B invisible) `f(P') = f(P*)` EXACTLY.
  5. Apply strong-induction hypothesis Claim(N−k): `f(P') ≥ 1`, hence `f(P*) = f(P') ≥ 1`. Base case
     N small (n≤1, or N=0 = uncut W_n, f=D_n≥1) certified. Closes the residual ⇒ lower bound ⇒ whole
     problem.
Key lemmas (claim + mechanism):
  - BF-invisibility: even tie-blocks contribute 0 to f — because `Δf=σ(σ_{a_j}−σ_{a_j+μ_j−1})` telescopes
    to 0 on an even block (certified `symmetric-odd-block-move`/`odd-block-formula`). This is what makes
    B removable without changing f.
  - Cut-cost ≥ t: a shared value v not a power of 2 forces every copy into a split piece; superincreasing
    powers-of-2 (Σ_{a<k}2^a<2^k) forbid v as an uncut remainder — so t copies need ≥ t cuts.
  - Complement legitimacy: deleting B and reattaching donor mass keeps Uw=b on the surviving pieces
    (donor's leftover 2^m−(copies) is a valid sub-piece), giving a smaller refinement — verified exactly
    by the Gap-B explorer (residual `{2,4/3,1}` of the n=3 leaf is itself an f≥1 Claim instance, f=5/3).
Open gaps: (G1) the cut-cost ≥ t bound rigorously (currently strong numeric evidence only); (G2)
complement-legitimacy — that reattaching donor mass yields a valid ≤(N−k)-cut refinement of W_n and not
a broken dyadic-conservation config, for BOTH the μ=3-leaf shape AND the deg≥3-cycle-piece shape.
Two viable gap-fills for (G2) (this is the copy-worthy fork — both close the SAME "f(P*)=f(complement)≥1"):
  - Fill A (algebraic peel): generalize the certified concentration Reduction Lemma (invisible 2·e_k
    peels, det U=±2 det U', f preserved) to peel a whole even block / attachment, reducing N directly.
  - Fill B (combinatorial recount): the Gap-B explorer's route — exhibit the complement multiset as an
    explicit ≤(N−k)-cut refinement and invoke Claim(N−k) with a parity/positivity top-up.
Cases to cover: μ=3 even leaf (Gap B); deg≥3 cycle-piece with even off-cycle/chord mass (Gap A′ case
(b)); multi-piece even tie-block (dual Budget-Lemma shape). All three are BF-invisible blocks — one lemma.
Watch out for: (a) donor-mass reattachment can break dyadic conservation Σ(sub-pieces of 2^k)=2^k — must
check the complement is still a refinement of the SAME W_n, not a fake; (b) the cut-cost bound must be
proven, not asserted — the n=2 all-even example has p=2<n+1 via a mult-4 class (t≥ size, not p), so count
by BLOCK SIZE t, never by distinct-value count p (that reduction is REFUTED); (c) base case must cover
the leaf-at-the-very-top sub-case where no larger uncut piece dominates (the only f<1 witness, and it is
over-budget for its own n — the induction must confirm it never fits ≤n cuts).

---

### self-similar-recursion: advance   (lead, Elo 1689)
Target: whole claim `c(n)=2^n/D_n`; imports certified upper bound; closes the LB tied residual via the
primal cycle-exclusion route.
Technique: primal integrality via Φ-max incidence-multigraph forest-peeling — close the two surviving
residual shapes (Gap A′, Gap B) with a GLOBAL budget/residual-complement induction (the circulation
V-kink is DEAD, do not retry).
Skeleton:
  1. Import S-core, M2, M3, M4, BF, Lemma CC+ (all-degree-2-cycle-pieces infeasible) — CERTIFIED.
     Residual = {Gap A′: a cycle carrying a cycle-piece of degree ≥3} ∪ {Gap B: μ=3 even-block leaf}.
  2. **Gap B via residual-budget induction (concrete skeleton = Gap-B explorer opening 1):** a μ=3
     even leaf (piece 2^k = {v,v,v}, v=2^k/3, shared with ≥1 donor piece) costs ≥3 cuts (2 to trisect +
     ≥1 donor split, v never a power of 2). The complement (P minus the BF-invisible even block of v's,
     donor leftover reattached) is a ≤(N−3)-cut refinement; Claim(N−3) ⇒ f(complement)≥1; BF ⇒
     f(P)=f(complement)≥1. (Gap-B explorer verified the complement `{2,4/3,1}`/`{2,4/3,1}` resolves as
     its own f≥1 instance, f=5/3, across 5 embeddings n=3,4.)
  3. **Gap A′ via the SAME induction:** a deg≥3 cycle-piece has an off-cycle/chord sub-piece carrying
     even (BF-invisible) mass; peel that even attachment as a removable block, reducing N, and apply
     Claim(N−k) to the complement cycle-minus-attachment (which by CC+ has all-degree-2 pieces ⇒
     already infeasible/forest ⇒ integral ⇒ f≥1).
Key lemmas (claim + mechanism):
  - Gap-B cut-cost ≥3: trisection (2 cuts) + shared v needs a donor split (≥1) because v=2^k/3 is not a
    power of two, so no uncut piece equals it.
  - Gap-A′ attachment is BF-invisible: the off-cycle/chord even mass forms an even tie-block ⇒ contributes
    0 to f ⇒ removable, and its removal drops the offending piece's degree to 2 ⇒ CC+ applies.
Open gaps: (A) the deg≥3-cycle attachment is ALWAYS an even/BF-invisible block that peels cleanly
(needs proof the off-cycle mass can't be an odd block feeding f); (B) the Gap-B cut-cost ≥3 and
complement-legitimacy (shared with the unified slug's G1/G2).
Cases to cover: even cycle with chord; odd cycle with deg≥3 piece; off-cycle degree-≥3 attachment.
Watch out for: this route's Gap A′ case is EXPLICITLY isomorphic to dual-integer-certificate's Budget
Lemma case (b) — flag the shared wall; if the unified slug's cut-cost lemma lands, it closes both here.
Do NOT re-attempt the circulation feasible direction (V-kink, certified 200/200) or any naive
M4-extension to mixed/even pairs (also V-kink, verified round 8).

---

### dual-integer-certificate: advance   (Elo 1557)
Target: whole claim `c(n)=2^n/D_n`; imports certified upper bound; closes the LB residual via the dual
lattice / (D′) f∈ℤ route + Positivity Budget Lemma.
Technique: prove f∈ℤ (then f odd via POS-CHAR ⇒ f≥1) through (D′) |det U^★|=1 on the visible reduced
subsystem, plus the Budget Lemma finishing Positivity — via a peeling induction off certified
top-piece-cut.
Skeleton:
  1. Import Lemma POS-CHAR (f=0 ⟺ all-even; T odd ⟹ f>0), Lemma CRAMER (f·det U ∈ ℤ ⇒ f=M/det U),
     top-piece-cut-alleven (all-even ⇒ w_1≤2^{n-1}, piece 2^n cut). Positivity collapses to the
     **Budget Lemma:** no all-even refinement of W_n within ≤n cuts.
  2. **Budget Lemma via peeling induction (budget-lemma explorer opening 1):** the ≥2 even copies of
     the top value w_1 sit inside piece 2^n (top-piece-cut). Case split on residual mass R=2^n−(mass of
     w_1-copies in piece 2^n):
       - **Case (a) R=0 (w_1=2^{n-1}, exactly 2 copies, self-contained):** piece 2^n contributes exactly
         1 cut and vanishes; the leftover is an all-even refinement of W_{n-1} ⇒ by induction N'≥n ⇒
         N=1+N'≥n+1. CLEAN — the explorer verified this reproduces the certified n=2 minimal example
         exactly (top {2,2}, leftover all-even refinement of W_1 with N'=2). Build this as a certifiable
         sub-lemma.
       - **Case (b) R>0, or a w_1-copy housed outside piece 2^n:** off-budget mass exchange between the
         top piece and the rest — NOT reducible to a clean W_{n-1} instance. **This is structurally the
         SAME as Gap A′ / self-similar's deg≥3 case (b): flag the shared wall explicitly.** Route via
         the unified residual-complement induction (import that lemma once it lands), or via opening 2's
         DELETE/SUBTRACT reachability reuse.
  3. **(D′) |det U^★|=1 via minimality:** on the visible reduced subsystem U^★ (after peeling invisible
     matched-pair 2·e_k columns via certified Reduction Lemma), minimality ⇒ no surviving deg≥3
     cycle-piece ⇒ U^★ benign ⇒ f∈ℤ. Combined with POS-CHAR (f odd) ⇒ f≥1.
Key lemmas (claim + mechanism):
  - Budget-Lemma case (a): R=0 makes the top-piece pair fully self-contained, so deletion yields an
    all-even refinement of W_{n-1} of exactly N−1 cuts — clean strong induction on n.
  - (D′) target must be stated on U^★, NOT raw U: invisible matched pairs make minor-gcd EVEN (verified
    gcd=2 at {3,3,2,2,2,2,1}) — "det/gcd=±1" is literally false on raw U (certified negative).
Open gaps: (D1) Budget-Lemma case (b) — the residual-mass/off-piece-copy case (≅ Gap A′; hand to the
unified induction); (D2) |det U^★|=1 on the visible subsystem via minimality (≡ Gap A′ deg≥3
cycle-piece by Cramer — the same wall in dual clothing).
Cases to cover: (a) R=0 self-contained; (b) R>0 or w_1-copy outside piece 2^n.
Watch out for: p ≥ n+1 as a stand-alone forcing lever is REFUTED (n=2 all-even with p=2 via a mult-4
class) — count total sub-pieces T=Σμ_j, not distinct values p. Do NOT re-attempt the odd-cancellation
branch (POS-CHAR closed it) or small-p as a stand-alone (D′) lever (refuted).

---

### concentration-exclusion-rigidity: advance   (Elo 1498, supplies the peel engine)
Target: whole claim `c(n)=2^n/D_n`; imports certified upper bound; closes the LB residual by reducing
benign-U to the visible concentration-free subsystem then merging with the dual (D′).
Technique: single-column concentration + Cramer + the certified Reduction Lemma as the algebraic peeling
engine that Fill A of the unified slug and step 3 of the dual route both need.
Skeleton:
  1. Import Concentration Exclusion Theorem (only surviving m≥2 is m=2 invisible matched pair) and the
     Reduction Lemma (invisible 2·e_k peels, det U=±2 det U', f preserved) — CERTIFIED.
  2. **Push Gap 1 (benign visible subsystem):** generalize the Reduction Lemma from peeling a single
     invisible 2·e_k column to peeling an entire BF-invisible even block / degree-1 leaf, so the reduced
     visible subsystem U^★ is concentration-free AND leaf-free. This is exactly the peel engine the
     unified slug's Fill A and the dual route's step 3 import.
  3. On the reduced U^★: benign ⟺ no surviving cycle (2-core empty) — merges with the dual (D′) and
     self-similar Gap A′ as ONE target.
Key lemmas (claim + mechanism):
  - Reduction generalization: an even block / degree-1 piece-leaf column contributes a det factor that
    cancels in the Cramer ratio f=M/det U (as the certified 2·e_k case does with factor ±2), so f is
    preserved under the peel — extends invisible-pair peeling to arbitrary even blocks.
Open gaps: (C1) generalize Reduction Lemma to arbitrary even block / leaf (currently only 2·e_k
certified); (C2) benign U^★ = no surviving cycle (≡ Gap A′ / (D′) — the shared wall).
Cases to cover: m=2 invisible pair (certified), general even block (gap), degree-1 leaf (gap).
Watch out for: benign is NOT det/gcd=±1 on raw U (minor-gcd can be even) — always state on the visible
reduced subsystem. This slug's value this round is primarily to SUPPLY the certified/generalized peel
engine to the unified and dual routes; if the unified induction lands, this becomes a certified
sub-component rather than an independent finisher.

---

Nominated field for the outline-reviewer (build set candidates), best-leverage first:
1. `unified-residual-budget-induction` (NEW) — the highest-leverage move; one global induction closes
   Gap A′ case (b), Gap B, and the dual Budget Lemma; opened with two gap-fills (algebraic peel /
   combinatorial recount) for the shared "f(P)=f(complement)≥1" step.
2. `self-similar-recursion` (ADVANCE, lead) — Gap A′ + Gap B via the same global budget induction
   (concrete Gap-B skeleton from the explorer's Claim(N−3)-on-complement).
3. `dual-integer-certificate` (ADVANCE) — Budget Lemma peeling induction (case (a) clean, case (b) ≅
   Gap A′, flagged) + (D′) |det U^★|=1 via minimality.
4. `concentration-exclusion-rigidity` (ADVANCE) — generalize the Reduction Lemma into the peel engine
   the other three routes import; push Gap 1 (benign visible subsystem).
Shared-wall note for the reviewer: routes 2/3/4 all bottom out on the SAME fact (minimality ⇒ no
surviving deg≥3 cycle-piece), now attacked from three distinct machineries (primal cycle / dual lattice
/ concentration peel); route 1 is the genuinely new framing (strong induction on N via BF-invisible-block
removal) that, if its cut-cost + complement-legitimacy gaps close, finishes ALL of them at once.
