# Lemma — self-compensation pairing (`e_M ≤ o_R` reduces to a residual Hall-type match)

**Status: CERTIFIED** (round 3, reviewer). Trivial within-pair sortedness; the residual (Match) is the open step.

**Setup.** Same as the `e_M ≤ o_R` reduction (`lemmas/lemma-em-or-reduction.md`). Pair the global sorted-desc list as `(p_1, p_2), (p_3, p_4), …`; in each pair `(p_{2i−1}, p_{2i})` the odd-position piece `p_{2i−1} ≥ p_{2i}` (sorted). Classify each pair by the *origins* of its two pieces:

- Type **MM**: both `M`-sub-pieces. Contributes `m_even` to `e_M`, `m_odd` to `o_M`; `m_odd ≥ m_even`.
- Type **RR**: both `R'`-pieces. Contributes `r_odd` to `o_R`, `r_even` to `e_R`; `r_odd ≥ r_even`.
- Type **MR**: odd is `M`-sub, even is `R'`-piece. Contributes `r_even` to `e_R`, `m_odd` to `o_M`. (No `e_M`, no `o_R`.)
- Type **RM**: odd is `R'`-piece, even is `M`-sub-piece. Contributes `m_even` to `e_M`, `r_odd` to `o_R`; by within-pair sortedness, `r_odd ≥ m_even`. (**Self-compensating.**)

**Lemma (self-compensation).** In every **RM** pair, `r_odd ≥ m_even` (within-pair sorted order), so the pair's contribution to `e_M` is paid in full by its contribution to `o_R`.

**Corollary (the reduction).** `e_M ≤ o_R` reduces to
> **(Match)** `Σ` over `MM` pairs of `m_even` ` ≤ ` `Σ` over `RR` pairs of `r_odd`.

*Proof.* `e_M = Σ_{MM} m_even + Σ_{RM} m_even` and `o_R = Σ_{RR} r_odd + Σ_{RM} r_odd`. By self-compensation `Σ_{RM} m_even ≤ Σ_{RM} r_odd`. Subtracting, `e_M ≤ o_R ⟺ Σ_{MM} m_even ≤ Σ_{RR} r_odd`. ∎

So the interleaving obstruction, after self-compensation, is reduced to a single inequality comparing the *smaller half* of each `M`-`M` pair against the *larger half* of each `R'`-`R'` pair — a Hall-type injective-matching condition.

**Open step (honest).** The residual (Match) is verified by exact enumeration at `n = 2, 3` (0 violations) and 500k random reals at level 3 (0 violations; reviewer spot-confirmed), but is **NOT analytically proved for general `n` over the reals**. It is the live open handle of the lower-bound route.

**Equality case.** At the pair-pile extremal (`e_M = o_R = 0`): there are no `MM` and no `RR` pairs — all pairs are `MR`/`RM` and self-compensate exactly (`r_odd = m_even` by the pair-pile's equal-pair structure). (Match) holds as `0 ≤ 0`. ✓

**Knowledge-base tools.** Hall's marriage theorem (the (Match) residual is an injective-matching condition: match each `MM`-pair's smaller half to a distinct `RR`-pair's larger half `≥` it); Invariants & monovariants (within-pair sortedness is the self-compensation monovariant).

**Where proved.** `approaches/pairing-partner.md` (round 3, §"Self-compensation pairing lemma").
