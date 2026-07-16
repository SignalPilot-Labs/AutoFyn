# Lemma (Dyadic-level parity, Sub-3a)

**Status:** CERTIFIED (proof-reviewer, round 5). Proposed by `ll-dyadic-symdiff`. Correct and
rigorous (elementary once the measure form is granted); certified as a reusable structuring lemma.
NOTE: this is a *conditional* lemma — it fires only when some full dyadic level is odd; it does NOT
close Lemma LL t ≥ 2 (the residual Sub-3b, where no full level is odd, remains open).

Levels partitioning `[0, 2^{n−1})`: `I_0 = [0,1)`, `I_k = [2^{k−1}, 2^k)` (1 ≤ k ≤ n−1);
`measure(I_k) ≥ 1` for every k.

## Statement
Let `P = Q ∪ R` with `S_P = {x : N_P(x) odd}` and `A(P) = measure(S_P)` (Lemma M0). If there is a
level index `k` with `N_P(x)` odd for **every** `x ∈ I_k`, then `A(P) ≥ measure(I_k) ≥ 1`.

A checkable sufficient condition for the hypothesis:
`(∗)` no piece value of `P` lies in `int(I_k)` with odd multiplicity, and `#{pieces of P with value
≥ sup I_k}` is odd.

## Proof
If `N_P` is odd throughout `I_k`, then `I_k ⊆ S_P`, so `A(P) = measure(S_P) ≥ measure(I_k) ≥ 1`.

For `(∗)`: crossing (as x decreases through) a value of even multiplicity flips `N_P` by an even
amount, preserving parity; so if no interior value has odd multiplicity, `N_P` has constant parity on
`I_k`. That constant parity equals the parity of `N_P` just below `sup I_k`, which is
`#{pieces ≥ sup I_k}`. If this count is odd, `N_P` is odd throughout `I_k`. ∎
