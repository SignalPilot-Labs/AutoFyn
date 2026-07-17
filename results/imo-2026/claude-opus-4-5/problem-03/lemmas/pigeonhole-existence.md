# Pigeonhole Existence Lemma

**Statement:** For m+1 positive pieces p_1 <= p_2 <= ... <= p_{m+1} summing to S, at least one index k in {1, ..., m+1} satisfies p_k <= 2^{k-1} * S * t_m where t_m = 1/(2^{m+1}-1).

**Proof:** Suppose for contradiction that all indices fail. Then p_k > 2^{k-1} * S * t_m for all k in {1, ..., m+1}.

Summing over all k:

sum_{k=1}^{m+1} p_k > S * t_m * sum_{k=1}^{m+1} 2^{k-1} = S * t_m * (2^{m+1} - 1) = S.

But sum p_k = S by assumption. Contradiction.

**Certified:** Round 3
