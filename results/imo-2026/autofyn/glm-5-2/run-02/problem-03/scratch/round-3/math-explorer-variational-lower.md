# imo-2026-03 — variational / exchange route to the LOWER BOUND (gap G1)

Lens: prove `Lemma L(n)` (`global_A ≥ 1/D(n)` for every Xiang refinement of the level-`n` dyadic) via a variational / smoothing / exchange argument, *without* per-mark induction.

Notation: `D(n)=2^{n+1}−1`, `A = Σ(−1)^{i+1} p_i` (pieces sorted desc), `Liu=(1+A)/2`, target `A ≥ 1/D(n)`. Liu plays the dyadic `(1,2,4,…,2^n)/D(n)`.

---

## 1. The terrain — is the variational framing viable?

**Yes, partially, with one genuine new lever and one honest collapse.** The headline finding is a **simpler extremal** that linearizes the odd-count case, plus a **trivial cheap-kill lemma** (`A ≥ smallest piece` for odd piece-count) that reduces the whole problem to a single variational step. The collapse: the natural variational target *is* the "WLOG k≤1" exchange (D2 in `pairing-partner`), already flagged plausible-but-unproven — so the variational route, taken naively, converges back to the same exchange. The diversifying escape is a **direct global weight-function inequality** (Engine C below) that bypasses the exchange entirely.

### The simpler extremal (verified, conjecture)
**Bisect all `n` biggest dyadic pieces into equal halves; leave the smallest piece `1/D(n)` alone.** This uses exactly `n` marks (within budget), produces `2n+1` pieces (ODD count), and gives
```
multiset = {2^{n−1},2^{n−1}, 2^{n−2},2^{n−2}, …, 2,2, 1}/D(n)
A = (2^{n−1}−2^{n−1}) + … + (2−2) + 1  =  1/D(n).   ✓
```
Verified exact (Fraction arithmetic) for `n=1..5` (gives `A=1/3,1/7,1/15,1/31,1/63` and `oddsum=f(n)` each). This is a **k=1 config** in the `M⊎R` decomposition (exactly one Xiang mark lands in `M`, bisecting it), so its `A=1/D(n)` is **already covered by the PROVED k=1 sub-case** (`pairing-partner` §Lemma L(n+1) k=1). The new content is not the extremal itself but its **structural simplicity**: all pairs equal, one leftover singleton = `1/D(n)`.

### The cheap-kill lemma (trivial, conjecture-but-provable)
> **(CK)** If the final piece-count is ODD, `A ≥ (smallest piece)`. 
> *Proof.* `A = Σ_pairs (p_{2i−1}−p_{2i}) + p_{2m+1}` (last piece is the leftover singleton, the smallest). Each pair-excess `≥ 0`, and the leftover `= p_{2m+1} =` smallest piece. ∎

Verified for all `1378` odd-count configs in the `n=2` fine-grid brute force (D=7, k=8 sub-grid): **zero violations**. This is a one-line lemma — the outliner should certify it.

### The single hardest step
Combine (CK) with the conjecture **"at the minimizer, the smallest piece `≥ 1/D(n)`"** (i.e. the smallest dyadic piece is never split at the optimum — verified `n=2`: `0/228` extremals split the smallest piece). Then for odd-count minimizers: `A ≥ smallest ≥ 1/D(n)`. ∎

**The hard step is exactly conjecture (S): "splitting a piece of size `≤ 1/D(n)` never helps Xiang."** Equivalently: any mark placed inside the smallest dyadic piece can be moved elsewhere (to bisect a larger unsplit piece) without increasing `A`. This is a **2-piece variational transfer**, and its hard part is the **ΔA tail term `T`** in the certified `ΔA = 2((−1)^r b − T)` (lemma-delta-a-local-cut): moving a mark changes two pieces simultaneously, and the `−2T` parity-flip-on-tail is what blocked per-mark induction. The variational route must either (i) show `T=0` for the *specific* transfer "out of the smallest piece, into the midpoint of an unsplit bigger piece," or (ii) sidestep `T` globally via a weight function.

---

## 2. Closest crux moves retrieved

Filter: `domain=combinatorics`, then keyword scan of `technique`+`how_used` for exchange/smoothing/majorization/sorted/transfer/merge/dyadic/charging. Three genuinely analogous:

### (C1) `aimo-0119` — extremal minimizer + non-improving single-item transfer  ★ best match
- **Crux** (`invariants-and-monovariants`): "Pick the configuration minimizing the maximum part load, tie-broken by fewest parts attaining that maximum, so that any single-item transfer from the heaviest to the lightest part is non-improving." Order box sums `d_1≤…≤d_100`; minimality forces `d_1 + (moved card) ≥ d_100`. Combined with a pigeonhole "some card `≤ d_100/11`" this yields `91 d_100 ≤ 1000`, i.e. `d_100 ≤ 11 − 1/91`.
- **Why analogous.** This is *exactly* the variational template I need: pick the `A`-minimizing Xiang refinement (tie-broken), then any single-mark transfer must not decrease `A`; read off a structural inequality forcing the pair-pile / bisect-all-big structure. The "non-improving transfer" is the engine; the tie-break picks a canonical extremal.
- **Adaptation (hint, re-prove from scratch).** Replace "max part load" by "`A`", the heaviest/lightest box by "the piece whose split is most uneven / the unsplit piece," and the transfer by "move a mark from an uneven split to bisect an unsplit piece." Minimality forces the post-transfer `A' ≥ A`, which via the `ΔA` closed form becomes an inequality on the pair-excesses. The crux supplies the *proof shape* (extremal + non-improving swap → structural inequality), not the inequality itself.

### (C2) `aimo-0012` — consecutive-pair pigeonhole + merge-pair induction  ★ second match
- **Crux** (`induction-and-construction`): "To shrink an instance for an induction on the number of items, use an averaging/pigeonhole bound on grouped consecutive pairs to guarantee some adjacent pair fits within one unit of capacity, then merge that pair into a single item." Base `d≤2n−1`; step `d≥2n`: the `n` consecutive pair-sums total `≤ n`, so some `a_i+a_{i+1}≤1`; merge.
- **Why analogous.** The pair-pile structure is *built out of consecutive sorted pairs*. An induction that, at each step, finds a "mergeable adjacent pair" (one whose excess is small enough) and fuses it, mirrors the `M⊎R` self-similar peel. The crux's averaging-on-consecutive-pairs is a clean way to find the pair to operate on without per-mark bookkeeping.
- **Adaptation.** Run an induction *down* on the dyadic level: at level `n+1`, the `n+1` dyadic pieces give `n` consecutive (in the sorted sense) pair-sums totaling `D(n)/D(n+1)`; averaging finds a pair whose excess is `≤ 1/D(n+1)`. Fuse (peel one level). This is a *global* induction on the sorted pair structure — not per-mark — and sidesteps the `ΔA` tail by working with pair-sums, not single pieces.

### (C3) `aimo-0019` — dyadic-frontier amortized potential + charging scheme
- **Crux** (`invariants-and-monovariants`): "Maintain a linear potential bounding cumulative resource by a constant times progress, proved by amortized induction that charges each frontier advance against the pieces it absorbs." B keeps `ink_on_[0,x_r] ≤ 3x_r`; each advance costs `≤ 2/2^m + 1/2^m`, giving `3(x_r+1/2^m) < 3x_{r+1}`.
- **Why analogous.** This is the closest corpus example of a **dyadic-length charging scheme with a linear potential** — exactly the shape of a weight-function proof of `A ≥ 1/D(n)` (Engine C). The "at most one interval of each dyadic length" fact is the same structural fact the pair-pile exploits.
- **Adaptation.** Define a potential `Φ = Σ_pieces w(size)` with `w` chosen so that (i) `A ≥ Φ` for every sorted multiset, (ii) `Φ ≥ 1/D(n)` by a per-dyadic-length charging (each `2^k/D(n)` piece, when split, contributes a controlled amount; the total is bounded by the geometric sum `Σ 2^{-k}`). The crux's "linear potential + amortized advance" is the template.

*Non-matches (rejected after reading):* `aimo-0333` (max-plus recurrence, exchange swaps a repeated block — too algebraic, no sorted-pair structure), `aimo-1020` (transversal-swap interpolation — grid coloring, not partition), `aimo-0013` (bichromatic arcs on a circle — geometric, not partition). Same-subtopic but not analogous.

---

## 3. Concrete candidate engines (2–3) for a new `lower-bound-variational` approach

### Engine A — extremal + non-improving transfer (the C1 template, targets the exchange D2)
- **Setup.** Let `𝒞` = all Xiang refinements of the level-`n` dyadic with `≤ n` marks. Pick `C* ∈ argmin A`, tie-broken by (a) fewest marks in `M`, (b) lexicographically smallest sorted piece vector.
- **Transfer.** If `C*` has `k≥2` marks in `M` (the k≥2 sub-case), pick the two smallest sub-pieces `m_k, m_{k+1}` of `M` (so `m_k ≥ m_{k+1}`); MERGE them (remove the mark between them) and RE-PLACE that mark to bisect the largest unsplit `R`-piece. Call the result `C'`.
- **Claim (the hard step).** `A(C') ≤ A(C*)`. If true, `C'` is also a minimizer with one fewer mark in `M`; iterate to `k=1`, where the proved sub-case gives `A ≥ 1/D(n)`.
- **Hard step / blocker.** The `ΔA` closed form for a *two-piece simultaneous change* (merge in `M` + bisect in `R`) involves TWO tail terms `T_M, T_R` and four rank-shifts in the global sort. The certified per-mark obstruction (`−2T`) was for ONE piece; here the tails might cancel, but **this is unverified**. The dispatch explicitly flagged "literal monotonicity in `k` is FALSE" (`n=3`: `k=2,3` extremals more numerous than `k=1`). So the *strict* form `A(C') < A(C*)` is false; only the *weak* form `A(C') ≤ A(C*)` (non-increasing) is needed, and the tie-break (b) handles equality. **This is the single load-bearing unproved step of Engine A.**
- **Diversification from per-mark induction.** Per-mark induction moved ONE mark and tracked a monovariant; Engine A moves a *pair* of marks (one merge + one bisect) and tracks `A` globally. The pairing is what dodges the single-`T` obstruction — *if* the two tails cancel.

### Engine B — consecutive-pair induction on the sorted piece vector (the C2 template)
- **Setup.** Induct on `n`. At level `n+1`, sort the final pieces desc and pair them consecutively: `(p_1,p_2),(p_3,p_4),…`. `A = Σ (p_{2i−1}−p_{2i}) + [leftover]`.
- **Step.** Among the `n+1` "dyadic-source" pieces, averaging on consecutive pair-sums (C2) finds a pair whose excess is `≤ 1/D(n+1)`. Fuse that pair (peel one level of the self-similar `M⊎R` structure); the residual is a level-`n` instance, apply IH.
- **Hard step.** The "consecutive pairs" in the *sorted final partition* do NOT correspond to "dyadic-source pieces" — the sort interleaves `M`-sub-pieces with `R'`-pieces (the interleaving obstruction). So the pairing that C2 averages over is not cleanly available. **This is the same interleaving wall** that blocks the `k≥2` sub-case; Engine B reframes it as a sorted-pair-averaging problem but does not dissolve it.
- **Diversification.** Works on pair-SUMS not single pieces; if the interleaving can be controlled by a pairing lemma ("the sorted final partition admits a pairing with each pair summing to `≤ 2·(next dyadic level)`"), this is genuinely different from per-mark.

### Engine C — global weight-function / charging inequality (the C3 template; BYPASSES the exchange)  ★ most diversifying
- **Setup.** Construct a weight function `w: (piece size) → ℝ` (piecewise-linear, dyadic-length-aware) such that:
  - **(W1)** `A ≥ Σ_{pieces} w(size)` for every sorted multiset (a pairing/matching inequality — independent of *which* dyadic piece the size came from);
  - **(W2)** `Σ_{pieces} w(size) ≥ 1/D(n)` for every refinement of the level-`n` dyadic with `≤ n` marks (a conservation / amortized-charging inequality on the multiset of sizes, à la C3).
- **Why this diversifies.** Engines A, B both ultimately reduce to the "WLOG `k≤1`" exchange (D2) — they prove `A ≥ 1/D(n)` by *reducing* to the proved `k=1` case. Engine C proves `A ≥ 1/D(n)` *directly* on every config, with no exchange, no `k`-classification, no interleaving control. It is the furthest from per-mark induction.
- **Hard step.** Finding `w`. The trivial `w(p)=p` gives `Σw = 1` (too big); `w(p)=0` gives `0` (too small). The pair-pile / bisect-all-big extremals suggest `w` should be `0` on "paired-equal" pieces and positive on the "leftover singleton" — i.e. `w` should detect the *parity of multiplicity* in the sorted multiset, which is NOT a function of piece size alone. **This is the genuine obstruction to a pure size-based `w`.** A position-aware weight (like the mirror certificate) is the alternative, but that's already the certified mirror lemma (dyadic-only, doesn't lift). The open question: is there a *hybrid* weight (size + local-rank) that gives both (W1) and (W2)?
- **Cheap-kill sub-case.** For ODD-count configs, `w(p) = [p is the smallest]·p` works: (W1) is the cheap-kill (CK), (W2) needs "smallest piece `≥ 1/D(n)`" — conjecture (S). So Engine C for odd-count reduces to conjecture (S); the even-count case is the residual.

---

## 4. What would still block it — honest dead-ends

1. **Per-mark smoothing (ONE piece at a time) is DEAD.** Certified (`lemma-delta-a-local-cut`): `ΔA = 2((−1)^r b − T)`, the `−2T` tail-flip breaks per-mark monovariants. Do NOT retry. The variational engines above all move a *pair* of marks or use a global weight to dodge `T`; none moves a single mark.

2. **Pure Schur-convexity / majorization is DEAD.** `A = Σ(−1)^{i+1} p_i` as a symmetric function of the sorted multiset is **neither Schur-convex nor Schur-concave**: the Schur criterion `∂A/∂p_i − ∂A/∂p_j` has the sign of `(−1)^{i+1} − (−1)^{j+1}`, which is `+2` for (i odd, j even) [matches `p_i≥p_j`, OK] but `−2` for (i even, j odd) [contradicts `p_i≥p_j`]. So no Karamata / Robin-Hood-within-a-single-pair argument proves `A`-minimization directly. The outliner should not try Schur.

3. **The exchange route (Engine A) collapses to the already-flagged D2.** "For every `k≥2` config there is a `k≤1` config with `A` no larger" is *exactly* conjecture D2 in `pairing-partner`, flagged plausible-but-unproven (literal monotonicity FALSE, `n=3` brute force). Engine A gives a *proof strategy* for D2 (the 2-piece transfer + tie-break), but if the two `T`-tails don't cancel, Engine A dies the same death as per-mark. **Honest assessment: Engine A is the highest-risk, highest-reward option; it either closes G1 or hits the same wall.**

4. **"Minimizer is always odd-count" is FALSE in general.** The pair-pile (even count, `2n` pieces) is a certified extremal (`lemma-pair-pile-dyadic-cap`). So the odd-count cheap-kill (CK) does NOT cover all minimizers; the even-count case (pair-pile-type) must be handled by a separate argument (e.g. "even-count minimizer → rebalance the bottom pair to equality + split a top piece, turning it odd, `A` non-increasing" — a third transfer, also unproved). Brute force at `n=2` (fine grid, exactly 2 marks) found `228/228` extremals odd-count and `0` splitting the smallest piece — but this is `n=2`, k=2-marks-forced; with `≤2` marks the pair-pile (1 mark) is also extremal and even-count. So odd-count dominance is *config-dependent*, not universal.

5. **Conjecture (S) "splitting a piece `≤ 1/D(n)` never helps" is itself unproved.** Verified `n=2` (0/228 split-smallest extremals) but that's one data point. For `n≥3` the smallest dyadic piece is `1/D(n)`, tiny; splitting it creates two sub-`1/D(n)` pieces, which seems to always create an unequal bottom pair (bad for Xiang), but a proof needs the same `T`-control as Engine A. So (S) and Engine A share the same hard step — they are not independent.

---

## Summary for the outliner

| Engine | Mechanism | Hard step | Diversifies from per-mark? | Risk |
|---|---|---|---|---|
| **A** extremal+transfer (C1) | 2-piece merge+bisect, tie-broken minimizer | two `T`-tails cancel? | YES (pair move vs single) | HIGH (collapses to D2 if tails don't cancel) |
| **B** pair-sum induction (C2) | averaging on consecutive pair-sums | interleaving of sorted pairs | YES (pair-sums vs pieces) | MED (hits interleaving wall) |
| **C** weight function (C3) | global `A≥Σw≥1/D(n)` | find hybrid size+rank `w` | YES (no exchange, no `k`) | MED (pure-size `w` may not exist) |

**Cheap-kill to certify first:** (CK) `A ≥ smallest piece` for odd piece-count (one-line lemma, verified `n=2` no violations). Then the whole lower bound reduces to conjecture (S): "smallest piece `≥ 1/D(n)` at the minimizer" — the variational heart.

**Knowledge-base entries to use:** "Invariants & monovariants" (the alternating advantage `A` is the controlled invariant; the `M−R` identity linearizes the target); "Extremal principle / variational method" (the extremal-minimizer + non-improving-transfer template, C1); "Induction and construction" (the self-similar `M⊎R` peel, C2); "Charging schemes / amortized potential" (Engine C, C3).

**Analogous cruxes:** `aimo-0119` (best — non-improving transfer on extremal minimizer), `aimo-0012` (consecutive-pair merge induction), `aimo-0019` (dyadic-length charging potential).

**Prior progress to build on:** the PROVED `k=0` and `k=1` sub-cases (`pairing-partner`), the `M⊎R` self-similar decomposition + identity `M−total(R)=1/D(n+1)`, the bisect-all-big extremal (a clean `k=1` witness, this report), the cheap-kill (CK) for odd-count (this report).

**Dead ends (do not retry):** per-mark monovariants (ΔA `−2T`, certified dead); pure Schur-convexity (A is neither Schu-convex nor concave, this report); literal monotonicity in `k` (FALSE, `n=3` brute); multi-aux L* (FALSE, counterexample W=(1/9,4/9,1/9)/D=9, round 2).
