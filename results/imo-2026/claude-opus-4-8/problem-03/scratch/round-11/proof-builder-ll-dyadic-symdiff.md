# Proof-builder report — ll-dyadic-symdiff (imo-2026-03), Round 11

**Status: partial** (bucket (iii) general `n` remains open; genuine rigorous advances + one correction).
Wrote to `results/imo-2026-03/approaches/ll-dyadic-symdiff.md` (new §"Bucket (iii), general `n`:
correction to the INC premise, D1-direct, and the level-charge reduction (R11)"; updated Approaches
tried, Current best, Promotable lemmas).

## SPEC / CORRECTNESS CONCERN (top priority — read first)

The dispatch and outline are built on a **false structural premise**. The outline states:

> "S_Q⊆S_R in bucket (iii) FORCES max(Q)≤max(R) (if max(Q)>max(R) then N_Q=1 odd, N_R=0 even on the gap
> interval, violating INC), giving ΣQ'−ΣR'' = 1+(max(R)−max(Q)) ≥ 1."

This is **WRONG**. Machine-checked counterexample (`n=4`): `Q = {15/2, 15/2, 1}`, `R = {7, 4, 2, 1, 1}`.
- `S_Q = [0,1)`, `S_R = [0,2)∪[4,7)`, so `S_Q ⊆ S_R` — **INC holds**.
- yet `max(Q) = 15/2 > 7 = max(R)`.

The parity argument silently assumed `max(Q)` is a **unique** part. Here `max(Q)` has multiplicity 2, so
just below it `N_Q = 2` is *even*, and INC is not violated. Corrected lemma (PROVED, 0 violations over
n=4/n=5 INC sets): **INC ⟹ max(Q) ≤ max(R) OR max(Q) has even multiplicity.**

**Impact:** the intended non-inductive INC closure collapses. Since `max(Q) > max(R)` is possible,
`r − q` can be negative and the "double-REFL slack" `A(Q∪R) = (r−q) + A(Q'∪R'')` with
`ΣQ'−ΣR'' ≥ 1` is not the correct identity (when `q > r`, `q` is the global max and is peeled first). Do
NOT let any downstream builder use "INC forces max(Q)≤max(R)" or the `(r−q)`-slack argument.

The reviewer's own load-bearing check 1 endorsed this closure as "genuinely non-inductive" — but it
checked the *tools* (D1, REFL, Sub-3a) are non-inductive, not that the *premise* holds. The premise fails.

## What I proved rigorously this round (all general `n` unless noted)

1. **Corrected INC top-order lemma** (proved; promotable): INC ⟹ `max(Q)≤max(R)` OR even top-multiplicity.
   Clean point-parity argument. Replaces the false premise.

2. **D1-direct** (rigorous, all `n`, ordering-free): certified Lemma D1 applied to the *original* `Q∪R`:
   if `max_x|N_Q−N_R| ≤ 1` then `A(Q∪R) ≥ |ΣQ−ΣR| = 1`. Works for INC and GAP alike, immune to the
   correction. This is the robust general-`n` slice (needs no reflection, no max-ordering). Closes the
   `max|g|≤1` configs for every `n`.

3. **Uniform reduction** (structural clarification): bucket (iii) — both INC and GAP — is *exactly*
   `measure{g odd} ≥ 1`, `g := N_Q−N_R`, `∫g = 1`, `≤ 2n+1` breakpoints on `[0,2^{n−1})`. INC is **not** a
   genuinely easier sub-case; the R10 INC/GAP split gives no separate simplification of the crux.

4. **Level-charge reduction for `max|g| ≤ 2`** (proved algebra; promotable): with `A_± = measure{g=±1}`,
   `B_± = measure{g=±2}`, `∫g = (A_+−A_-) + 2(B_+−B_-) = 1` and `A(Q∪R) = A_+ + A_-` give exactly
   ```
   A(Q∪R) = 1 + 2(A_- + B_- − B_+),   hence   A(Q∪R) ≥ 1  ⟺  B_+ ≤ A_- + B_-.
   ```
   Verified TRUE (0 violations) over the n=4 and n=5 INC residual and the n=4 GAP residual. This is a
   genuine non-circular reduction of the whole `max|g|≤2` residual to one geometric inequality.

## The honest OPEN gap (unchanged crux, now sharply isolated)

`B_+ ≤ A_- + B_-`: the measure of the `g=+2` excess is dominated by the `g<0` mass. This is the
load-bearing open step. It is **not** implied by `∫g = 1` alone (`g≡2` on `[0,½)` breaks it, `A=0`); a
proof must use `ΣQ = 2^n` forcing wide support of `N_Q`, so a `g=+2` block cannot sit unaccompanied by
`g<0` mass. Plus the `max|g| ≥ 3` extension. So bucket (iii) general `n` stays open; only `n=3` closed (R9).

This is the same crux as `ll-inclusion-gap`'s `G-INC` family (Claim_R): the merge identity gives
`A(Q∪R) = A(R) − A(Q)` on INC, i.e. `A(R) ≥ A(Q)+1`. R11 did not close it; it corrected a false shortcut
and reduced the `max|g|≤2` residual to a single clean, verified-true inequality.

## Verification log (bounded, joint budget `#Q+#R cuts ≤ n` enforced; each run <20s)
- Counterexample `Q={15/2,15/2,1}, R={7,4,2,1,1}`: INC ✓, max(Q)=15/2>7, top-mult 2 (even), A=4.
- Corrected top-order lemma: 0 violations — n=4 (129 INC configs, denom 2), n=5 (1282 INC configs, integer).
- D1-direct closes 37/129 n=4 INC (the `max|g|≤1` slice); residual 92 all `max|g|=2`.
- Level-charge `B_+ ≤ A_-+B_-`: 0 violations over n=4 (129) and n=5 (1282) INC residual; minA=1 (tight).

## Promotable lemmas (for certification)
- **Corrected INC top-order lemma** (see approach file §R11): INC ⟹ max(Q)≤max(R) OR even top-mult.
- **Level-charge reduction (`max|g|≤2`)**: `A(Q∪R) = 1 + 2(A_-+B_-−B_+)`; `A≥1 ⟺ B_+ ≤ A_-+B_-`.

Both proved in full in the approach file. (D1 already certified; REFL/REFL-gen unaffected.)

## Note to the outliner (for re-planning)
The INC/GAP split does not isolate an easier case; both are `measure{g odd} ≥ 1`. The sharpest open
target is now the single inequality `B_+ ≤ A_- + B_-` (measure of `g=+2` excess ≤ `g<0` mass), which needs
a wide-support argument from `ΣQ=2^n`. A future approach should attack that directly (or the `max|g|≥3`
generalization) rather than re-deriving the refuted `(r−q)`-slack or the false max-ordering premise.
