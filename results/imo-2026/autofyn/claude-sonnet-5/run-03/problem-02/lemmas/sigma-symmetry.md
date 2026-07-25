## Lemma (σ-symmetry of the hypothesis set)
Let σ be the relabeling B↔C, K↔L, M↔N (fixing A). If (A,B,C,K,L,M,N)
satisfies every hypothesis of imo-2026-02 (the four containments: K∈△BMC,
L∈△BNC, K inside ∠LBA, L inside ∠ACK; and the three angle equalities
∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK), then so does its image under σ, namely
(A,C,B,L,K,N,M). Moreover σ carries the conclusion OM=ON to itself (ON=OM).

### Proof
Check each hypothesis clause is carried to another clause of the same list
(verbatim angle-notation symmetry ∠XYZ=∠ZYX is used freely):
- K∈△BMC ↦ L∈△CNB = △BNC — hypothesis 2. ✓
- L∈△BNC ↦ K∈△CMB = △BMC — hypothesis 1. ✓
- K inside ∠LBA ↦ L inside ∠KCA = ∠ACK — hypothesis 4. ✓
- L inside ∠ACK ↦ K inside ∠ABL = ∠LBA — hypothesis 3. ✓
- ∠KBA=∠ACL ↦ ∠LCA=∠ABK, i.e. ∠ACL=∠KBA — the same equation. ✓ (self-image)
- ∠LBK=∠LNC ↦ ∠KCL=∠KMB, i.e. ∠LCK=∠BMK — the third angle hypothesis. ✓
- ∠LCK=∠BMK ↦ ∠LBK=∠LNC (symmetric computation) — the second angle
  hypothesis. ✓ (σ swaps the second and third angle hypotheses)

So σ permutes the full hypothesis list into itself. Finally, the circumcenter
O of the unordered set {A,K,L} is unchanged by relabeling K,L, and σ sends
M↔N, so it carries OM=ON to ON=OM, the same statement. ∎

## Source
`results/imo-2026-02/approaches/coordinate-bash.md`, §3. Independently
re-verified clause by clause by proof-reviewer, round 1. No gap found.

## Status
Certified — reusable by any approach (synthetic or coordinate) to halve
casework, or as a consistency check on any proposed intermediate claim (a
claim about K,B,M should have a mirror claim about L,C,N that is
automatically also true).
