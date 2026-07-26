# Four-coset closure lemma (safe triangles cannot split into two marked children)

**Statement.** Fix θ with 0°<θ<180° and suppose 180° is NOT a positive multiple of θ (equivalently θ ≠ 180°/n for every integer n≥2). If a triangle state (a,b,c) (a,b,c>0, a+b+c=180°) is θ-safe — meaning none of a,b,c is a positive integer multiple of θ — then for every legal cut (any vertex, any parameter in the legal range), at least one of the two children is again θ-safe.

**Proof.** Relabel so the cut is to vertex A (angle a) with parameter x∈(0,a); the other angles are b,c. By the cut-geometry lemma the children are C1=(x,b,a+c−x) and C2=(a−x,c,b+x). Since b,c are θ-safe:
- C1 is θ-marked ⟺ x is a positive multiple of θ OR (a+c−x) is;
- C2 is θ-marked ⟺ (a−x) is a positive multiple of θ OR (b+x) is.

Suppose for contradiction both children are θ-marked. The conjunction of two two-term disjunctions expands to four pairwise conjunctions, each settled:
1. x ∈ θZ_{>0} AND (a−x) ∈ θZ_{>0}: x=mθ, a−x=pθ ⟹ a=(m+p)θ ∈ θZ_{>0}, contradicting a safe.
2. x ∈ θZ_{>0} AND (b+x) ∈ θZ_{>0}: x=mθ, b+x=pθ; b+x>x (b>0) ⟹ p>m ⟹ b=(p−m)θ ∈ θZ_{>0}, contradicting b safe.
3. (a+c−x) ∈ θZ_{>0} AND (a−x) ∈ θZ_{>0}: a+c−x=mθ, a−x=pθ; a+c−x>a−x (c>0) ⟹ m>p ⟹ c=(m−p)θ ∈ θZ_{>0}, contradicting c safe.
4. (a+c−x) ∈ θZ_{>0} AND (b+x) ∈ θZ_{>0}: summing, (a+c−x)+(b+x)=a+b+c=180°=(m+p)θ ∈ θZ_{>0}, contradicting 180°∉θZ_{>0}.

The four cases are exhaustive; each is a contradiction. Hence no cut makes both children marked; at least one child is safe. ∎

**Geometric restatement (external-angle form).** The four "new" angles created by a cut satisfy the exterior-angle identities ∠ADC = B+α and ∠ADB = (A−α)+C; together with the safe±unsafe=safe lemma, this yields the same four-case closure. (See approach altitude-halving §4.)

**Certified by:** proof-reviewer, round 1 (all three approaches proved it from scratch, in equivalent algebraic/external-angle form). **Source:** approaches/lattice-coset-descent.md §3 (Lemma A), approaches/altitude-halving.md §4c (Lemma 4), approaches/safe-unsafe-pairing.md §I.1.
