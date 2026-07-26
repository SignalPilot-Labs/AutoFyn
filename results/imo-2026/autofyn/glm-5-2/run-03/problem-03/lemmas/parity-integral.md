# Lemma: parity-integral reformulation + parity-XOR toggle

## Statement

Let `a_1 ≥ a_2 ≥ … ≥ a_m ≥ 0` be a multiset of pieces (total need not be 1). Define `j(t) := #{i : a_i ≥ t}` for `t ≥ 0` (a non-increasing step function). Write `D := a_1 − a_2 + a_3 − a_4 + … = S_odd − S_even` (the alternating sum of the descending sort).

**Lemma (parity-integral).** `D = ∫_0^∞ [j(t) is odd] dt`.

**Corollary (parity-XOR toggle).** A split of one piece `p` into two fragments `u ≥ v ≥ 0` (`u + v = p`) toggles the parity of `j(t)` on `[0, v) ∪ [u, p)` and leaves it unchanged on `[v, u)`. Equivalently, `j_new ≡ j_old ⊕ h_p (mod 2)`, where `h_p := 1_{[0,v)} + 1_{[u,p)}` is the indicator of `[0, v) ∪ [u, p)` (two intervals, each of length `v`). For a sequence of splits, `j_final ≡ j_Liu ⊕ (h_{p_1} ⊕ … ⊕ h_{p_k})`, and `D_final = ∫[j_final odd] dt = ∫(f ⊕ h) dt` where `f := [j_Liu odd]` and `h` is the XOR of the per-split toggle indicators.

## Proof

**Parity-integral.** For integer `j ≥ 0`, the identity `1_{j odd} = Σ_{k=1}^{j} (−1)^{k+1}` holds (telescoping alternating sum of `j` terms: `1 − 1 + 1 − …`). Hence `1_{j(t) odd} = Σ_{k ≥ 1} (−1)^{k+1} 1_{j(t) ≥ k}`. Integrate termwise (the sum is finite for each `t`, since `j(t) ≤ m`; Fubini/Tonelli applies — all terms bounded, support `[0, a_1]`):

`∫_0^∞ 1_{j(t) odd} dt = Σ_{k ≥ 1} (−1)^{k+1} ∫_0^∞ 1_{j(t) ≥ k} dt`.

Now `1_{j(t) ≥ k}` means "at least `k` pieces are `≥ t`", i.e. `t ≤ a_k` (the `k`-th largest piece; `a_k = 0` for `k > m`). So `∫_0^∞ 1_{j(t) ≥ k} dt = a_k`. Therefore

`∫_0^∞ 1_{j(t) odd} dt = Σ_{k ≥ 1} (−1)^{k+1} a_k = a_1 − a_2 + a_3 − … = D`. ∎

**Toggle.** The piece `p` contributes `+1` to `j(t)` on `[0, p)` and `0` elsewhere. After splitting into `u, v` (`u ≥ v`), the two fragments together contribute `2` on `[0, v)` (both `≥ t`), `1` on `[v, u)` (only `u ≥ t`), `0` on `[u, p)`. The change `δj(t) = j_new − j_old` is `+1` on `[0, v)`, `0` on `[v, u)`, `−1` on `[u, p)`, `0` elsewhere. Since `±1` flips parity and `0` preserves it, the parity-toggled region is `[0, v) ∪ [u, p)` (total measure `v + (p − u) = 2v ≤ p`). Iterating splits, parities compose by XOR (mod-2 addition), giving the displayed formula. ∎ (KB: *Double counting* / Fubini / *Invariants & monovariants*.)

## Verification

Independently checked: `D = ∫[j odd]` reproduces the alternating sum on 20k random multisets (max error 0); the toggle lemma reproduces `D_final` after splits on 20k configs (max error 0). See proof-reviewer round 3 verification.

## Source

Proved in `pairing-charging` §3 (round 2) and independently in `alternating-potential` §2 (round 2) and `dyadic-induction` §2 (round 1). Canonical location: this file.

## Certification

Reviewer-certified round 3 (proof-reviewer, imo-2026-03). The statement is proved `sorry`-free from Fubini + telescoping; every regime of the split toggle is handled; the conclusion is no stronger than what the proof establishes. Importable by any approach needing a clean `D`-handle on the multiset of piece lengths.
