# Lemma — integer-grid parity theorem (`A ≥ α(n)` for grid-aligned refinements)

**Status: CERTIFIED** (round 3, reviewer). Rigorous but restricted to grid-aligned refinements; does NOT lift to reals (honestly stated).

**Statement.** For the level-`n` dyadic config `(1, 2, 4, …, 2^n)/D(n)` and any Xiang refinement whose marks (combined with Liu's marks) are all at multiples of `1/D(n)` (so every final piece is a positive multiple of `1/D(n)`), the alternating advantage sum satisfies
```
A ≥ 1/D(n) = α(n).
```

**Proof.** Scale all lengths by `D(n)`: the pieces become positive integers `q_1 ≥ q_2 ≥ … ≥ q_M` with `Σ q_i = D(n)` (an ODD integer, since `D(n) = 2^{n+1} − 1`). The scaled advantage is `A* := A·D(n) = Σ (−1)^{i+1} q_i`. Pair consecutive sorted pieces:
- **Even `M` = `2m`:** `A* = Σ_{i=1}^m (q_{2i−1} − q_{2i})`. Each pair-excess `e_i := q_{2i−1} − q_{2i} ≥ 0` (sorted). Moreover `e_i = (q_{2i−1} + q_{2i}) − 2 q_{2i}`, so `e_i ≡ q_{2i−1} + q_{2i} (mod 2)`. Summing: `Σ e_i ≡ Σ (q_{2i−1} + q_{2i}) = Σ q_i = D(n) ≡ 1 (mod 2)`. So `Σ e_i` is a non-negative odd integer, hence `Σ e_i ≥ 1`. Therefore `A* ≥ 1`.
- **Odd `M` = `2m+1`:** `A* = Σ_{i=1}^m (q_{2i−1} − q_{2i}) + q_{2m+1}`. Each pair-excess `≥ 0`, and the leftover `q_{2m+1} ≥ 1` (a positive integer, being the smallest piece). Therefore `A* ≥ 0 + … + 0 + 1 = 1`.

In both cases `A* ≥ 1`, i.e. `A ≥ 1/D(n) = α(n)`. ∎

**The lift fails (honest).** The argument is tied to the grid spacing `1/D(n)` (the unit `1` is the grid quantum). For a finer grid `1/(K·D(n))` with `K` odd, the scaled total `K·D(n)` is still odd, but the parity argument yields `A ≥ 1/(K·D(n))`, strictly weaker than `1/D(n)` for `K > 1`. So the parity mechanism does NOT extend to arbitrary real marks — only to marks at multiples of `1/D(n)`. Real marks can produce a sub-`1/D(n)` smallest piece, defeating the CK cheap-kill on the odd-count sub-case; the integer-grid parity survives only because all pieces are positive multiples of `1/D(n)`.

**Verification.** `A·D(n) = 1` (the minimum) for all grid refinements: `n = 1` (2 responses), `n = 2` (7 minimizers among responses at `1/7`-grid), `n = 3` (40 minimizers among 232 responses at `1/15`-grid). Reviewer spot-confirmed: `n = 2` grid min `A = 1/7`, `A·7 = 1`; `n = 3` grid min `A = 1/15`, `A·15 = 1`.

**Knowledge-base tools.** Pigeonhole / extremal principle (the parity is a mod-2 pigeonhole on the pair-excesses); Invariants & monovariants (the alternating sum's parity is locked to the total's parity).

**Where proved.** `approaches/pairing-partner.md` (round 3, §"Integer-grid parity theorem").
