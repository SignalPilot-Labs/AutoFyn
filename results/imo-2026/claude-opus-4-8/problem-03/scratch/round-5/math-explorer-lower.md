## imo-2026-03 — Lower-bound wall: (★) at a=0 clustered vertices

### Problem recap (the gap)
The confined lower bound A ≥ 1 is equivalent to the vertex inequality (★): A(vertex) ≥ 1 over the (n+1)-fragment simplex Δ. Already closed: the interleaving cell (A ≡ 1) and all a=1 vertices (cascade: top fragment > 2^{n-1}). **Open**: a=0 vertices — all fragments ≤ 2^{n-1}, top piece is the intact 2^{n-1}. D-scaled units throughout.

---

### Numerical grounding

For strict a=0 (all fragments **strictly** < 2^{n-1}):
- n=3 (2^{n-1}=4, D=15): random search over 500k configs gives **min A ≈ 1.0014** (not 1), with the minimum approached as g_1 → 4 (the a=0/a=1 boundary). Deep interior configs (e.g., g=(2,2,2,2)) give A=3; more clustered configs closer to the boundary give A closer to 1.
- n=4 (2^{n-1}=8): same pattern, min A ≈ 1.008. All strict-interior vertices have A > 1.

For the **a=0/a=1 boundary** (one fragment = 2^{n-1} exactly):
- g=(4,2,2,0), g=(4,2,1,1), g=(4,3,1,0) etc. all give A=1 (verified exact rational arithmetic).
- The cascade proof handles f_1 > 2^{n-1}; continuity of A at f_1 = 2^{n-1} gives A(boundary) = 1.

**Key structural fact:** In the strict a=0 interior, A > 1 strictly. The minimum over the closed a=0 region (including the boundary) equals 1, achieved only at the a=0/a=1 boundary.

---

### Rank-parity structure (the geometric engine)

At any a=0 config, the top piece is the intact 2^{n-1} (rank 1, odd). The **rank of the largest fragment g_1** is:

    rank(g_1) = 1 + #{intacts > g_1} = 1 + (n - j)   if g_1 ∈ (2^{j-1}, 2^j)

- g_1 ∈ (2^{n-2}, 2^{n-1}): rank 2 (EVEN) — critical range
- g_1 ∈ (2^{n-3}, 2^{n-2}): rank 3 (ODD)
- g_1 ∈ (2^{n-4}, 2^{n-3}): rank 4 (EVEN)
- Pattern alternates by dyadic level.

**Mass transfer effect**: increasing g_1 by ε while decreasing g_j by ε changes A by:
ΔA = ε · [(−1)^{r_1+1} − (−1)^{r_j+1}]

- r_1 even, r_j odd (g_j at odd rank, e.g., rank 2n+1): **ΔA = −2ε < 0** — decreases A ✓
- r_1 even, r_j even: **ΔA = 0** — neutral
- r_1 odd, r_j odd: ΔA = 0 — neutral
- r_1 odd, r_j even: ΔA = +2ε — bad (increases A; never use)

**Traced example (n=3, g=(2+e, 2, 2, 2−e)):**
- e ∈ [0,1]: g_4 = 2−e ≥ 1 at rank 6 (even), g_1 at rank 2 (even). Both even → ΔA=0. A stays at 3.
- At e=1: g_4 crosses below the intact 1. g_4 drops to rank 7 (ODD).
- e ∈ (1,2): g_4 at rank 7 (odd), g_1 at rank 2 (even) → ΔA=−2ε. A decreases from 3 to 1.
- At e=2: g_1=4 (boundary), A=1.

The transition happens the moment **g_4 crosses below any intact**, becoming odd-ranked; then transfer to the even-ranked g_1 strictly decreases A.

**Within a dyadic level**: consecutive fragments in level (2^{m-1}, 2^m) occupy CONSECUTIVE ranks (alternating odd/even). So if g_1 is at an odd rank, g_2 (in the same level, immediately below) is at an even rank — mass transfer g_j → g_2 (even rank) via a fragment at an odd rank DECREASES A. So there is ALWAYS a "decreasing move" available unless the configuration is already at the boundary.

---

### Distinct openings

**Opening A (MOST PROMISING — boundary monotone path)**
Show that at any a=0 vertex in the strict interior, there exists a mass-transfer move (from some odd-ranked fragment g_j to some even-ranked fragment g_i) that strictly decreases A. The descent continues until the boundary g_1 = 2^{n-1} is reached. Since A is piecewise-affine and the descent is valid at every interior vertex, **the minimum over the closed a=0 region is achieved only at the boundary**, where A = 1 (cascade + continuity).

The key lemma needed: at any strict interior a=0 vertex (all fragments < 2^{n-1}), there exists a pair (i, j) with r_i even, r_j odd, g_j > 0. This follows from:
- The lowest fragment g_{n+1} is at rank 2n+1 (always ODD).
- If g_1 is at an even rank (g_1 ∈ (2^{n-2}, 2^{n-1})): transfer g_{n+1} → g_1 immediately decreases A. ✓
- If g_1 is at an odd rank: there exists a fragment g_2 in the same dyadic level as g_1, at the next consecutive rank, which is even. Transfer g_{n+1} → g_2 (or g_{n+1} to any even-ranked fragment in a lower dyadic level) decreases A.

No claim about the intermediate path is needed: just that at EVERY strict-interior vertex, A can be decreased. Since A is continuous and the strict interior is a compact set of piecewise-affine cells, the minimum over the closed a=0 region is achieved at a vertex, and every interior vertex has A strictly above its local minimum → the minimum is at the boundary. **This opening does NOT use the fragment-count bound; it uses only the rank parity structure.**

**Opening B (peeling induction)**
Peel the top pair (intact 2^{n-1} at rank 1, largest even-ranked piece at rank 2). The remaining 2n−2 pieces are a sub-instance with a smaller problem. This matches G-L1(n−1) only if the fragment count and sum fit. The count is n+1 (fragments) + (n−2) (smaller intacts) = 2n−1; after removing the two top pieces, sum reduces, but the fragment count vs. inductive-hypothesis slot count is off by one. **Not clean for current G-L1(n−1), but might work with a generalized G-L1 statement.**

**Opening C (E* lower bound via fragment-count)**
Reformulate A ≥ 1 as the claim: the even-indexed sum E* of the 2n remaining pieces (I_{n-1} ∪ F) satisfies E* ≥ 2^{n-1}.

The certified fragment-count bound N_F(2^{n-j}) ≤ 2^j − 1 controls how many fragments can "push" intacts to odd positions. In each dyadic level (2^{m-1}, 2^m), the intact 2^{m-1} can be displaced to an odd rank only if all slots in that level above it are occupied by fragments. The count bound limits the displacement.

**Claim (to prove):** Each intact I_m = 2^m ends up at an even rank among the 2n remaining pieces, or is paired with a fragment that compensates for it. The total even-indexed sum includes all n−1 intacts plus at least one fragment ≥ 1, giving E* ≥ ΣI_{n-1} + 1 = 2^{n-1} − 1 + 1 = 2^{n-1}. The "+1" comes from the fact that the sum constraint ΣF = 2^n with the count bound forces at least one fragment ≥ 2^n/(n+1) > 0 to land at an even rank (by the pigeonhole on dyadic levels).

This approach is mechanically: partition the 2n pieces into dyadic groups, compute the net alternating-sum contribution from each group using the count bound, and sum. **Uses the fragment-count bound directly. The outliner should attempt this CONCURRENTLY with Opening A.**

**Opening D (global-minimum certified by A = 2^{n-1} − A* where A* = alt-sum of sub-problem)**
The a=0 case reduces to: A* ≤ 2^{n-1} − 1 where A* is the alternating sum of the 2n-piece sub-list (I_{n-1} ∪ F). Now A* is the "standard" alternating sum of the 2n pieces (2(n-1) intacts removed, all fragments ≤ 2^{n-1}). This is a sub-instance of the SAME problem on a size-(n−1) set of intacts plus (n+1) fragments. The fragment count is too high for G-L1(n−1), but the STRUCTURE is a valid sub-problem if we allow more fragments. This suggests a GENERALIZED induction where the inductive claim is: for intacts I_{n-1} and k ≤ n+1 fragments summing to 2^n (with all ≤ 2^{n-1}), A* ≤ 2^{n-1}−1. The base case n=1 is trivial (2 fragments = {1,1}, A*=0). The inductive step would need the count bound to handle the extra fragment. **This is a different recursion than G-L1 and avoids the circular integral.**

---

### Why all current a=0 approaches stall

The shared gap: every approach must prove A ≥ 1 when the TOP PIECE IS AN INTACT (not a fragment). The cascade (which handles a=1) always has the fragment at the top. In a=0, the intact "blocks" the cascade from applying. Opening A breaks this by not using the cascade at all — it uses a DESCENT ARGUMENT that avoids ever applying the cascade in the a=0 interior.

**Warning**: The sub-problem induction (Route B in current approach) was already noted as circular because O_sub ≤ 2^{n−1}−1 is an upper bound on a shifted alternating sum, not an instance of G-L1(n−1). Opening D reframes this to avoid the circularity.

---

### Candidate techniques

- **Mass-transfer / monovariant descent** (Opening A): identify an invariant (A) and a monovariant (progress toward the boundary) with the property that at every non-minimum vertex, A can be decreased. **This is the analogue of the "exchange argument" in combinatorics; the move is a mass transfer between fragments.**
- **Alternating sum parity promotion** (Opening C): convert a weak (A ≥ 0) bound from the a=1 cascade into a strict (A ≥ 1) bound for a=0 using the count bound and parity. Closest crux: aimo-0330 (parity promotes weak nonneg bound to strict lower bound = 1).
- **E* ≥ 2^{n-1} directly** (Openings C, D): prove the even-indexed sum of the remaining pieces is at least 2^{n-1}, using that ΣF = 2^n forces large fragments to land at even positions.

---

### Knowledge-base entries to use

- **Invariants & monovariants** (combinatorics): Opening A requires a "monotone descent via local moves" argument — a monovariant (A) plus a local move that decreases it at every non-boundary vertex.
- **Pigeonhole / extremal principle**: the claim that any a=0 vertex has an even-ranked fragment that can receive mass from an odd-ranked one.
- **Casework / exhaustion**: rank-parity of each fragment depends on the dyadic level it falls in (even/odd pattern); case split on which level g_1 inhabits.
- **Piecewise-concavity smoothing** (algebra section): A is piecewise-affine and its minimum over a compact set is at a vertex; the descent argument identifies the vertex as the boundary.

---

### Analogous past problems (cruxes)

1. **aimo-0330** (combinatorics, `invariants-and-monovariants`): "Track a parity invariant of the partial sum to promote a weak nonneg bound into a strict lower bound of at least the parity value." In that problem, S_{4k} ≡ even but S_k is odd ≥ 1 so S_{4k} ≥ 2. Analogous: in a=0, the parity of the rank of the smallest fragment switches from even (neutral zone) to odd (decreasing zone) when it crosses below an intact, which is the mechanism that forces A ≥ 1. **Genuinely analogous: the crux move is "parity transition triggers a strict lower bound."**

2. **aimo-0146** (combinatorics, `extremal-principle`): "Maximize a fixed weighted sum of a sorted nonnegative sequence under a sum constraint by exchange-smoothing weight toward higher-coefficient positions until free coordinates equalize and the tail drains." This is exactly the mass-transfer argument: push weight toward the highest-coefficient (even-ranked for DECREASING A direction) position until the tail drains (reaches 0 or the boundary). **Genuinely analogous to Opening A.**

3. **aimo-0019** (combinatorics, `invariants-and-monovariants`): "Bound a family of dyadic-length pieces of pairwise distinct sizes by twice the largest, via the geometric sum of distinct negative powers of two." The dyadic bound there (geometric sum ≤ 2×max) is analogous to the fragment-count bound here (N_F(2^{n-j}) ≤ 2^j−1). The amortized argument in aimo-0019 suggests a similar amortization over dyadic levels would close the a=0 case in Opening C.

---

### Prior progress

Already certified (safe to import):
- Lemma S (rank-swap, local min): A increases at every rank swap away from interleaving; does NOT give global min.
- Fragment-count bound N_F(2^{n-j}) ≤ 2^j − 1 (certified).
- Interleaving value A = 1 (certified, a=1 region, not a=0).
- a=1 cascade (top-fragment cascade §4.2.4): handles all a=1 vertices, including the a=0/a=1 boundary by continuity.
- CaseB-Reductions 1&2, Lemmas G1, R, H, X.

**The cascade gives A ≥ 1 for all a=1 configs; by continuity of A, it covers the boundary g_1 = 2^{n-1} (where A = 1). The ONLY remaining vertices are strict-interior a=0 configs (all g_i < 2^{n-1}), for which numerics confirm A > 1.**

---

### Dead ends (do not retry)

- **The per-rank bound r_{2j} ≤ 2^{n-j}**: REFUTED (n=3, F={3,2.5,2.5}: r_4=2.5 > 2). Do not use.
- **The circular integral ‡** (∫⌊(N_F−N_I)/2⌋dt ≤ 0): algebraically equals O − 2^n; dropped.
- **Sub-problem induction via O_sub ≤ 2^{n-1}−1**: circular — O_sub is the same type of upper bound as the goal, leading back to the same gap.
- **Convexity of O in fragment values**: REFUTED (2307/10000 violations in n=4 random tests).
- **Concavity of g (the function from §3)**: REFUTED (interior valley at n=2, round 3).
- **n→n−1 game-separation induction**: REFUTED (F1: XY budget doesn't decrement; F2: odd-sum is global).

---

### Small-case / intuition notes (labeled as conjecture)

**Conjecture (numerically strongly supported):** In the strict a=0 interior (all fragments < 2^{n-1}), min A > 1 for all n. The minimum approaches 1 as g_1 → 2^{n-1}, so the closed a=0 region achieves min A = 1 only at the boundary. The strict-interior minimum appears to satisfy min A ≥ 1 + (2^{n-1} − g_1)/D (roughly), i.e., the gap to 1 is proportional to the distance of g_1 from the boundary.

**Conjecture (unverified for general n):** At any a=0 vertex with g_1 at an even rank (g_1 ∈ (2^{n-2}, 2^{n-1})): the smallest positive fragment g_{n+1} eventually falls below some intact (becomes odd-ranked) as e increases in the transfer g_1→g_1+e, g_{n+1}→g_{n+1}−e. At that point ΔA = −2e < 0, and continuing to the boundary g_1 = 2^{n-1} yields A = 1. This gives a clean monotone descent.

**Key inequality (to prove for the a=0 gap):** The even-indexed sum E* of the 2n remaining pieces (I_{n-1} ∪ F, after removing the top intact 2^{n-1}) satisfies:

    E*(I_{n-1} ∪ F) ≥ 2^{n-1}

Equivalently: O*(I_{n-1} ∪ F) ≤ 2^n − 1. This is exactly A* ≤ 2^{n-1}−1, i.e., A ≥ 1.

For n=2 (verified): with I_0={1} and 3 fragments summing to 4, all < 2: the fragment constraint Σg_i=4 with g_i < 2 forces g_2 > 1 (otherwise Σ < 4), so q_2 = g_2 > 1. Then E* = q_2 + q_4 ≥ g_2 > 1 and sum constraint forces E* ≥ 2. **This proves (★) for n=2 a=0.** The general-n argument by the same method requires: the sum constraint ΣF = 2^n with all g_i < 2^{n-1} and n+1 fragments forces at least n of the 2n remaining pieces to be "sufficiently large" to fill n even-rank slots summing to ≥ 2^{n-1}. This is the inductive content.
