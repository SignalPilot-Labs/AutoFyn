# Lemma: exponent-pair Euclidean-preservation

**Statement.** Let a board carry 2026 positive-integer entries. For a prime p write
α_i := v_p(a_i) (p-adic valuation, with v_p(1)=0). Define

  g_p := gcd(α_1, …, α_2026),      with the conventions gcd(0,k)=k, gcd(0,0)=0.

When a move replaces two entries (m, n) by (gcd(m,n), lcm(m,n)/gcd(m,n)),
the quantity g_p is unchanged.

**Proof.** Fix p and write α := v_p(m), β := v_p(n). The two new p-valuations are

  v_p(gcd(m,n)) = min(α, β),     v_p(lcm(m,n)/gcd(m,n)) = max(α,β) − min(α,β) = |α − β|,

using v_p(gcd(m,n)) = min(v_p(m), v_p(n)) and v_p(lcm(m,n)) = max(v_p(m), v_p(n)).
So the pair (α, β) is replaced by (α', β') := (min(α,β), |α−β|). We claim
gcd(α, β) = gcd(α', β').

- If α = 0 (or symmetrically β = 0): say α = 0. Then min(0, β) = 0 and |0 − β| = β,
  so the new pair is (0, β) — identical as a multiset to the old pair {0, β}. Hence
  the gcd is unchanged. (Convention gcd(0, β) = β covers β = 0 too: gcd(0,0) = 0.)

- If α, β > 0: assume WLOG α ≤ β (both the gcd and the replacement are symmetric in
  the two entries). Then α' = α and β' = β − α. The **subtractive Euclidean step**
  (the identity gcd(x, y) = gcd(x, y − x) for y ≥ x > 0, which is the one-step form
  of the Euclidean algorithm) gives gcd(α, β) = gcd(α, β − α) = gcd(α', β').

Thus in every case gcd(α, β) = gcd(α', β').

Finally, the whole-board gcd g_p = gcd(α_1, …, α_2026) is obtained from the multiset
of all 2026 valuations by folding pairwise gcds; gcd is associative and commutative,
so replacing two elements of the multiset by a new pair with the same pairwise gcd
leaves the folded whole-board gcd unchanged. Hence g_p is invariant under every move. ∎

**Used by:** monovariant-first (step 6), invariant-first. Importable instead of
re-proving.
