# imo-2026-03 — Sub-3b Lens Report (Round 6)

## Problem context
Lemma LL, sub-case t≥2, A(Q)>0: Q partitions 2^n into ≥3 parts (A(Q)>0, max(Q)≤2^{n-1}), R refines G_{n-1} with A(R)≥1, max(R)≤2^{n-1}. Prove A(Q∪R)=measure(S_Q△S_R)≥1. Cases 1/2/Sub-3a are CLOSED. Sub-3b (no dyadic level I_k is fully in S_Q△S_R) is the live gap, 85/187 n=3 residual configs.

---

## Key finding 1: Sub-3b decomposes into exactly INC ∪ GAP

The 85 Sub-3b configs at n=3 (with R=G_2) split as 4 INC (S_Q⊆S_R) + 4 GAP (S_Q⊄S_R) in the fine enumeration; broader enumeration confirms both sub-types exist. This means:

**Sub-3b = G-INC-1 ∪ G-GAP from ll-inclusion-gap.** The two approaches (ll-dyadic-symdiff and ll-inclusion-gap) are attacking the SAME residual gap. Their open stubs are provably equivalent:
- Sub-3b INC sub-case ⟺ G-INC-1 (S_Q⊆S_R ⟹ A(R)≥A(Q)+1)
- Sub-3b GAP sub-case ⟺ G-GAP (S_Q⊄S_R with no full level odd ⟹ measure(S_Q△S_R)≥1)

**Recommendation to outliner:** merge these two routes. A single new approach can close Sub-3b by addressing INC and GAP as complementary branches rather than rediscovering the same split in two files.

---

## Key finding 2: NEW algebraic identity (verified, n=3, 9 configs)

When max(Q) = 2^{n-1} exactly, let Q' = Q \ {max piece} (Q' partitions 2^{n-1} into t≥2 parts with max(Q')<2^{n-1}). Then:

**A(Q∪R) = 2^{n-1} − A(Q'∪R)**

*Proof sketch (elementary):* For x ∈ [0, 2^{n-1}): N_Q(x) = 1 + N_{Q'}(x) (the piece 2^{n-1} always exceeds x). So parity(N_Q(x)) = 1 − parity(N_{Q'}(x)), giving S_Q ∩ [0,2^{n-1}) = [0,2^{n-1}) \ S_{Q'}. Therefore:

measure(S_Q△S_R) = measure(([0,2^{n-1})\S_{Q'})△S_R) = measure([0,2^{n-1}) \ (S_{Q'}△S_R)) = 2^{n-1} − A(Q'∪R).

Verified for all 9 n=3 configs with max(Q)=4=2^{n-1}.

**Consequence:** A(Q∪R)≥1 ⟺ A(Q'∪R)≤2^{n-1}−1.

This converts the lower bound into an UPPER BOUND on A(Q'∪R). Q'∪R has max ≤ 2^{n-1} and sum = 3·2^{n-1}−1.

---

## Key finding 3: Tight cases all have max(Q) = 2^{n-1}

**Verified (n=3):** Within Sub-3b, configs with max(Q) < 2^{n-1} = 4 give A(Q∪R) ≥ 2 (minimum is 2, not 1). The tight bound A(Q∪R) = 1 is only achieved when max(Q) = 4 = 2^{n-1} exactly.

This suggests a **TWO-PART SPLIT within Sub-3b**:

**(a) max(Q) = 2^{n-1}:** Use the identity — reduces to showing A(Q'∪R) ≤ 2^{n-1}−1. The tight cases land here; this is the harder part.

**(b) max(Q) < 2^{n-1}:** These configs have A(Q∪R) ≥ 2 with slack; a separate (potentially simpler) argument applies. For these, some dyadic level in S_Q△S_R has contribution ≥ 2^{k-1} ≥ 1 from Q's partial overlap with R, or the Sub-3a argument almost fires (giving ≥ 2·measure(I_k) ≥ 2).

---

## Key finding 4: INC sub-case general-n structure (G-INC-1)

For S_Q ⊆ S_R with R = G_{n-1}: the Structural Lemma (ll-inclusion-gap, Step 4, certified) gives:
- A(Q) = Σ_{allowed bands k} Δ(band k) where Δ(band k) = sum of (p−q) for each consecutive pair {p≥q} of Q-pieces in [2^{k-1}, 2^k].
- A(G_{n-1}) = Σ_{allowed k} u_k where u_k = 2^{k-1} = lower bound of I_k.
- Each pair deficit: u_k − Δ(pair) = 2^{k-1} − (p−q) > 0 (since p < 2^k and q ≥ 2^{k-1}, so p−q < 2^{k-1}).
- **Total deficit = A(G_{n-1}) − A(Q) > 0 strictly.** (Already proves A(Q) < A(G_{n-1}); need ≥ 1.)

**Open step (G-INC-1):** Why total deficit ≥ 1? The argument uses ΣQ = ΣG_{n-1} + 1:

Each Q-pair {p,q} in allowed band [u,2u) contributes p+q ≥ 2u to ΣQ and deficit = u−(p−q). The total ΣQ = Σ_{pairs} (p+q) = 2^n, while Σ_{pairs} 2u = 2·Σ_{pairs} u gives a lower bound. The EXCESS ΣQ − ΣG_{n-1} = 1 must appear in the pairs, and telescoping should force Σ deficit ≥ 1.

**Concrete n=3 check:** Q={4,3,1}: pair {4,3} in [2,4) gives deficit=2−1=1. No pair in [0,1). Total deficit=1. ✓ Q={4,5/2,3/2}: pair {5/2,3/2} in [2,4)... wait both are <2. Actually {5/2,3/2}: 5/2 is in [2,4)? No, 5/2 = 2.5 ∈ [2,4) ✓. 3/2=1.5 ∈ [1,2) (FORBIDDEN!). Contradiction with "S_Q ⊆ S_R"? Let me recheck: Q={4,5/2,3/2} is in the Sub-3b GAP category (S_Q ⊄ S_R), not INC. So the Structural Lemma does NOT apply to it. The INC examples from the data are Q={1,3,4},{1/2,7/2,4},{1/2,1,5/2,4},{1/2,1,3,7/2} — all with max=4.

**For G-INC-2 (refined R, not just G_{n-1}):** When R has extra cuts with A(R) possibly < A(G_{n-1}), the Structural Lemma applies to S_Q ⊆ S_R but with S_R having a non-dyadic structure. The per-band deficit argument breaks. This is harder and may require a strengthened IH.

---

## Key finding 5: GAP sub-case tight structure

For S_Q ⊄ S_R in Sub-3b (n=3, R=G_2): the tight GAP cases all have exactly TWO pieces in the symdiff, from two different dyadic levels, each of measure ½, summing to 1:

- Q={3/2,5/2,4}: S_Q△S_R = [1,3/2)∪[2,5/2). Each piece has measure ½.
- Q={1/2,3/2,2,4}: S_Q△S_R = [0,1/2)∪[1,3/2). Each piece has measure ½.

The mechanism: a piece of Q (say at value v ∈ I_k) creates a "partial overlap" with S_R that contributes measure (v − 2^{k-1}) or (2^k − v) to the symdiff in level I_k, AND creates a compensating miss in another level I_j. The two partial contributions sum to 1 by the integral constraint ΣQ − ΣR = 1.

**Conjecture (not proved):** For the GAP sub-case in Sub-3b, measure(S_Q△S_R) = Σ_k m_k where each m_k ∈ [0, measure(I_k)), and their sum ≥ 1 follows from a "level-budget" argument using ΣQ − ΣR = 1 plus the dyadic structure of R.

---

## Key finding 6: The identity is circular but structurally useful

The identity A(Q∪R) = 2^{n-1} − A(Q'∪R) does NOT enable a simple induction because Q'∪R is NOT a valid refinement of G_{n-1} (its sum is 3·2^{n-1}−1 ≠ 2^n−1 = Σ(G_{n-1})). Q'∪R has excess mass from Q'.

HOWEVER: the identity IS useful for the UPPER BOUND direction. If we can show A(Q'∪R) ≤ 2^{n-1}−1 from the upper bound side (e.g., by showing val(Q'∪R) ≤ ΣR = 2^n−1 = Σ(G_{n-1})), that would close Sub-3b for max(Q)=2^{n-1}. This reformulation connects Sub-3b to the UPPER BOUND problem (Regimes B/C).

---

## Distinct openings for the outliner

**Opening 1: INC deficit via pairing + sum constraint (general n)**
For S_Q⊆S_{G_{n-1}}: prove A(G_{n-1})−A(Q)≥1 using: (a) all Q-pairs in allowed bands have positive deficit, and (b) ΣQ=ΣG_{n-1}+1 forces total deficit≥1. The algebraic constraint links pair sums to ΣQ=2^n, and the "1 excess" propagates into deficit≥1. This should be provable by induction on n using the self-similar structure of allowed bands (each level is half the next).

**Opening 2: Split Sub-3b at max(Q) vs 2^{n-1}**
(a) max(Q)<2^{n-1}: show A(Q∪R)≥2 (slack available; might follow by applying Sub-3a to a "shifted" level or by a direct interval argument). (b) max(Q)=2^{n-1}: use the identity A(Q∪R)=2^{n-1}−A(Q'∪R) and prove A(Q'∪R)≤2^{n-1}−1 via the upper bound (val(Q'∪R)≤ΣR or similar).

**Opening 3: Direct algebraic proof for max(Q)=2^{n-1} cases**
With max(Q)=2^{n-1} and Q partitioning 2^n: the INC sub-case reduces via identity to A(Q'∪R)≤2^{n-1}−1, while the GAP sub-case has two symmetric contributions to the symdiff summing to 1. For the GAP case: the piece v=max(Q)=2^{n-1} exits level I_{n-1}=[2^{n-2},2^{n-1}) at its top, and the "shift" from v creates a split symdiff contribution. The two contributions (one in I_{n-2}, one in I_{n-1}) sum to exactly 1 by the integral constraint.

**Opening 4: Merge ll-dyadic-symdiff and ll-inclusion-gap under one roof**
Build a new approach that handles Sub-3b by first splitting on S_Q⊆S_R (INC, use Structural Lemma + deficit) vs S_Q⊄S_R (GAP, use partial-overlap argument). This avoids duplicating work across the two existing slugs and can import the certified Forcing Lemma and INC-Reduction from forcing-inc-reduction.md.

---

## Candidate techniques (knowledge base entries)

- **Invariants & monovariants**: ΣQ−ΣR=1 is an exact invariant; the per-band deficit is a monovariant.
- **Pigeonhole/extremal**: the 1-unit excess in ΣQ over ΣG_{n-1} must appear in at least one band's deficit.
- **Double counting**: relate Σ_{pairs}(p+q) = ΣQ = 2^n to Σ_{pairs}(deficit) = A(G_{n-1})−A(Q).
- **Direct proof/induction**: the INC general-n argument should follow by induction on n using the self-similar band structure.
- **Casework/exhaustion**: the max(Q) split within Sub-3b.

---

## Analogous past problems

None found in the crux corpus that directly map to the "pairing in dyadic bands + excess forces deficit≥1" structure. The closest analogy is the n=3 Step-6 calculation in ll-inclusion-gap, which handles the specific case and should generalize.

---

## Concrete Sub-3b examples (n=3, R=G_2={1,2,4})

**INC tight cases (S_Q⊆S_R, A(Q∪R)=1):**
- Q={1,3,4}: S_Q=[0,1)∪[3,4)⊆[0,1)∪[2,4)=S_R. A(Q)=2, A(R)=3. Symdiff=[2,3), measure=1. Deficit=A(R)−A(Q)=1.
- Q={1/2,1,5/2,4}: S_Q=[1/2,1)∪[5/2,4)⊆S_R. A(Q)=2, A(R)=3. Symdiff=[0,1/2)∪[2,5/2), measure=1/2+1/2=1.

**GAP tight cases (S_Q⊄S_R, A(Q∪R)=1):**
- Q={3/2,5/2,4}: S_Q=[0,3/2)∪[5/2,4). S_Q\S_R=[1,3/2)(measure 1/2). S_R\S_Q=[2,5/2)(measure 1/2). Total=1.
- Q={1/2,3/2,2,4}: S_Q=[1/2,3/2)∪[2,4). S_Q\S_R=[1,3/2)(measure 1/2). S_R\S_Q=[0,1/2)(measure 1/2). Total=1.

In all GAP tight cases: the two pieces of the symdiff are one from "S_Q outside S_R" and one from "S_R outside S_Q", with equal measures summing to 1.

---

## Prior progress
- Cases 1, 2, Sub-3a: CLOSED and certified.
- Sub-3b INC for n=3, R=G_{n-1}: PROVED (Step 6 of ll-inclusion-gap).
- Sub-3b INC for general n, R=G_{n-1}: OPEN (G-INC-1, the crux).
- Sub-3b INC for refined R: OPEN (G-INC-2, harder).
- Sub-3b GAP: OPEN (G-GAP).
- The REVIEWER NOTE flags the Structural Lemma part (a) as having a false claim for the "no piece in forbidden band interior" when the reviewer found Q={3/2,3/2,2,3} as a counterexample (but this was for the OVERCLAIM that S_Q⊆S_R implies no piece in (1,2)—the actual Structural Lemma is conditioned on S_Q⊆S_R, so the counterexample is a config where S_Q⊄S_R).

---

## Dead ends (do not retry)
- Naive integral bound: ∫(N_Q−N_R)=1 does NOT force measure{parity odd}≥1 (counterexample: g≡2 on [0,1/2) integrates to 1 but is never odd). Already documented.
- Merge bound b+|a−A(R)|: provably insufficient (34/286 failures). Already documented.
- Peeling one Q-cut (induction on t): non-monotone, circular. Already documented.
- Per-level identity m_k=f_k: FALSE for sub-configs with max(Q)<2^{n-1} (e.g., Q={4,7/2,1/2} has f_0=−1/2 but m_0=1/2). The identity holds in special cases but not universally.
- The "invalid R" apparent counterexample (A(Q'∪R)=4 with R={1,4,1}): this R has sum 6≠7=ΣG_{n-1}, so it is NOT a valid refinement. The identity cannot be violated by valid configurations.
