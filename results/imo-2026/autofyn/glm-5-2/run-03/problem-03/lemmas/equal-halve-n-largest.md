# Lemma: equal-halve-n-largest

## Statement

Let `n ≥ 1`. Given `n + 1` pieces `p_1 ≥ p_2 ≥ … ≥ p_{n+1} ≥ 0` summing to 1 (an arbitrary Liu config with `≤ n` marks), Xiang equal-halves the `n` largest pieces `p_1, …, p_n` (one mark each, `n` marks total), leaving `p_{n+1}` unsplit. The final multiset is `{p_1/2, p_1/2, p_2/2, p_2/2, …, p_n/2, p_n/2, p_{n+1}}` (2n + 1 pieces). Then

> `D = p_{n+1}`  (unconditionally, for every `n` and every Liu config).

## Proof

The final multiset consists of `n` equal pairs (the two copies of `p_k/2` for `k = 1, …, n`) and one lone piece `p_{n+1}`. Sort descending as `a_1 ≥ … ≥ a_{2n+1}`.

The two copies within each equal pair are equal, so they occupy **two adjacent ranks** in the descending sort. The `n` pairs thus occupy `n` blocks of 2 consecutive ranks, consuming `2n` of the `2n + 1` ranks and leaving exactly one rank for the lone `p_{n+1}`.

**Claim: the lone rank is odd.** The `2n` non-lone ranks form `n` disjoint pairs of consecutive integers (`{i, i+1}` for various `i`). The sum of all ranks `1 + 2 + … + (2n+1) = (2n+1)(n+1)`. Each block `{i, i+1}` sums to `2i + 1` (odd). The sum of `n` such blocks is `n` odd numbers, which has parity `n (mod 2)`. Hence the lone rank `= (2n+1)(n+1) − (sum of blocks) ≡ (n+1) − n = 1 (mod 2)`, i.e. the lone rank is **odd**.

Each equal pair `{i, i+1}` contributes `±(a_i − a_{i+1}) = 0` to `D = Σ_k (−1)^{k+1} a_k` (since `a_i = a_{i+1}`). So all paired contributions vanish. The only surviving term is the lone `p_{n+1}` at an odd rank, contributing `+p_{n+1}`. Hence `D = p_{n+1}`. ∎

## Corollary (regime closure, general n)

If `p_{n+1} ≤ 1/D_n` (where `D_n = 2^{n+1} − 1`), Xiang achieves `D = p_{n+1} ≤ 1/D_n` with `n` marks, i.e. `S_odd ≤ 2^n/D_n` for **all Liu configs whose smallest piece is `≤ 1/D_n`**, at **every** `n`. Tight at the dyadic config (where `p_{n+1} = g_0 = 1/D_n`, equality).

## Verification

Independently checked for `n ∈ {1, 2, 3, 4, 5}` on 5000 random Liu configs each: `|D − p_{n+1}|` max error `0` (exact); the lone piece always lands at an odd rank (parity argument confirmed). See proof-reviewer round 3 verification.

## Source

Proved in `pairing-charging` §6.1 (round 2). Canonical location: this file.

## Certification

Reviewer-certified round 3 (proof-reviewer, imo-2026-03). The statement is proved `sorry`-free; the odd-rank claim follows from the mod-2 sum of `n` odd-length blocks (an arithmetic parity argument, not a sort-order casework); the conclusion is no stronger than what the proof establishes. Closes the upper-bound regime `p_{n+1} ≤ 1/D_n` for arbitrary Liu marks at every `n`, tight at dyadic. Importable by any approach needing this regime of the upper bound.
