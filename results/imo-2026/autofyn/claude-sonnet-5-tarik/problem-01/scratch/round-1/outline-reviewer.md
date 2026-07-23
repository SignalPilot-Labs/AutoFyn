# Outline review — imo-2026-01 (Confucius gcd/lcm blackboard)

## Verdict: CHANGES REQUESTED

The technique is right and the skeleton is sound. I independently re-derived
every lemma by hand and cross-checked the two claims the dispatch specifically
flagged (the `g=1` vs `m=n` case split, and the `Γ`-invariance argument across
arbitrary positions) with fresh Python brute-force checks (not by trusting the
outline's self-reported verification numbers). Both check out. **However, I
found one genuine arithmetic error in the "rule out `c=0`" step (Part (a),
skeleton step 4) that appears in both `/tmp/round-1/proof-outliner.md` and the
mirrored "Current best" in `results/imo-2026-01.md`.** It does not require a
new technique — it's a one-paragraph fix — but it must not be carried into the
proof-builder's write-up verbatim, or the "solved" proof will contain a false
claim exactly at the step the dispatch asked to scrutinize most.

## The load-bearing error: Γ(terminal) = 0 is wrong; it is 1

Step 4 (both files) states: *"if the terminal board were all 1's,
`Γ(terminal) = 0`; ... `Γ(terminal) = Γ(initial) ≥ 1` ... Contradiction ⟹
`c=1`."*

This is false as written. By the outline's own definition,
`Γ(y_1,…,y_N) := ∏_p p^{γ_p}` with `γ_p := gcd(v_p(y_1),…,v_p(y_N))`. On an
all-1's board, every `v_p(y_i)=0`, so `γ_p = gcd(0,…,0) = 0` for **every**
prime `p` — but then `Γ = ∏_p p^0 = ∏_p 1 = 1`, not `0`. `p^0=1` is a
definitional fact, not a convention that can be reinterpreted. I verified this
computationally too:

```
Gamma([1,1,1,1,1]) = 1   # not 0
```

This is also **internally inconsistent with the outline's own step 5**, which
correctly uses "1 is Γ's identity in each coordinate" to get
`Γ(1,…,1,M)=M`. Applying that exact same identity-element reasoning to the
degenerate case `M=1` (i.e., all-1's) gives `Γ = 1`, matching my computation
and contradicting step 4's "`=0`."

**Consequence for the argument, and the required fix.** The conclusion (a
contradiction ruling out `c=0`) still holds, but only if both halves are
corrected together — fixing one without the other breaks the logic:
- `Γ(terminal | c=0) = 1` (not 0).
- The other side must then be strengthened from `Γ(initial) ≥ 1` (trivially
  true for *any* board, hence useless against `Γ(terminal)=1`) to
  **`Γ(initial) > 1`, strictly**. This is true and the justification is
  already half-present in the outline's parenthetical — it just needs the
  right conclusion drawn: some initial entry `x_1>1` has a prime factor `p_0`
  with `v_{p_0}(x_1) ≥ 1`; since gcd of a set of nonnegative integers
  containing a term `≥1` is itself `≥1`, `γ_{p_0}(\text{initial}) ≥ 1`, so
  `Γ(\text{initial}) ≥ p_0^1 ≥ 2 > 1`.
- Corrected contradiction: `Γ(terminal)=1=Γ(initial)>1` — false, so `c=0` is
  impossible, hence `c=1`. Same final conclusion, different (correct) numbers.

**Required change:** rewrite skeleton step 4 (in both files, or at minimum in
`proof-outliner.md` before the builder starts) replacing "`Γ(terminal)=0`...
`Γ(initial)≥1`" with "`Γ(terminal)=1`... `Γ(initial)>1`" and the fuller
justification above. This is the single mandatory fix before building.

## What I independently re-verified and confirms as correct

I did not take the outline's "verified" claims on faith; I recomputed
independently.

1. **Valuation-transform, Subtraction, Squeeze, Grouping lemmas** — re-derived
   by hand, all correct, standard, no gaps. `gcd(m,n)·lcm(m,n)=mn` is used
   implicitly inside the Ψ-descent mechanism ("`g·(ℓ/g)=ℓ=mn/g`") but is not
   listed as its own Setup Lemma — minor completeness note, should be stated
   and proved explicitly (from the valuation identities: `v_p(gcd)+v_p(lcm) =
   min+max = v_p(m)+v_p(n) = v_p(mn)` for every `p`) rather than left buried
   inside another lemma's proof.

2. **The `g=1` / `g>1∧m=n` / `g>1∧m≠n` case split (the exact thing a prior
   agent got wrong by hand) — brute-forced over all `m,n∈[2,200]`**
   (40,000 pairs): exhaustive and pairwise disjoint (confirmed each pair falls
   in exactly one case), and in every pair the outline's per-case claims about
   `(c_new, Φ_new/Φ_old)` matched exactly, with worst-case
   `Ψ_new/Ψ_old = 0.5` (never exceeded). This is a correct, tight,
   airtight monovariant — no exceptions found. Independent confirmation, not
   just re-running the outline's own script.

3. **`Γ`-invariance across arbitrary positions among all `N` entries** — the
   Grouping Lemma is stated and applied generically (arbitrary `i≠j` among
   `N`, not "positions 1,2"), so the mechanism genuinely generalizes across
   all 2026 board positions, not just a distinguished pair. I additionally ran
   400 full random-board simulations (sizes 2–10, random move order each
   step, i.e. random pairs of positions every move) comparing `Γ(initial)`
   to the simulated terminal `M`: **0 mismatches**, and `c` never hit 0 in any
   run (consistent with the corrected Part (a) argument above).

4. **Logical ordering / no circularity** — confirmed the write-up plan proves
   `Γ`-invariance for an arbitrary single move with no reference to
   termination, then uses it in both Part (a) (ruling out `c=0`, needs
   finiteness from step 3 to legitimately invoke "the terminal board") and
   Part (b) (needs Part (a)'s "exactly one survivor"). No circularity.

5. **Universal quantification** — both Ψ-descent and Γ-invariance are proved
   for an arbitrary legal move (arbitrary board state, arbitrary chosen
   positions), so induction over an arbitrary finite move sequence correctly
   covers every possible play, not a single example. Correct for "for all
   choices" as required by both parts of the problem.

6. **Dead-end avoidance** — confirmed this is not a repeat of anything in
   `results/imo-2026-01.md`'s "Approaches tried" (board-gcd, board-lcm,
   move-count invariants are separately, correctly refuted there and are not
   what this outline uses).

## Other (minor, non-fatal) gaps to close during build

- State explicitly that `Ψ = Φ·2^c` is always a positive integer, and that
  `Ψ_old ≥ 4` whenever a move is still possible (`c≥2 ⟹ 2^c≥4`, `Φ≥1`), so
  `Ψ_new ≤ Ψ_old/2 < Ψ_old` is a **strict** decrease of positive integers —
  currently the outline states only the `≤ half` bound and leaves strictness
  to be inferred.
- `gcd(m,n)·lcm(m,n)=mn` should be promoted to an explicit Setup Lemma (see
  above) rather than living only inside the Ψ-descent proof's parenthetical.
- (Housekeeping, not math) `problems.jsonl` lists `imo-2026-01`'s
  `difficulty_level` as `"medium"`, not `"hard"` — CLAUDE.md scopes this round
  to hard problems only. Flagging for the orchestrator; does not affect the
  mathematical verdict above since I was dispatched specifically to review
  this outline.

## Bottom line

Do not send this to the builder unmodified. The fix is small and localized
(skeleton step 4 / the `Γ`-invariance-based "rule out `c=0`" argument): swap
`Γ(terminal)=0` → `=1` and `Γ(initial)≥1` → `>1`, with the tightened
justification given above. Everything else in the outline — the
reformulation via `p`-adic valuation, the exact 3-case Ψ-descent split, the
Γ-invariance mechanism and its generality across all 2026 positions, the
dependency ordering between the lemmas and the two parts — is correct, and I
verified it independently rather than trusting the outline's own reported
checks. Once step 4 is corrected, this outline is ready to build.
