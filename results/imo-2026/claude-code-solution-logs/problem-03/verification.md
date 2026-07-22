# IMO Problem 3 — Verification report

Companion to `problem3_solution.md` (answer: $c = \dfrac{2^n}{2^{n+1}-1}$, with $s = \dfrac1{2^{n+1}-1}$, $c = \dfrac{1+s}2$).
Verification was done in two independent ways: **(A)** a skeptical line-by-line audit of every lemma and both bounds, and **(B)** exhaustive computer search on integer grids for $n = 1, 2, 3$.

---

## A. Logical audit of the proof

### Lemma 1 (claiming game value = odd-index sum $O(Q)$)

- **Game model.** Finite, perfect information, constant-sum (every piece ends up claimed, since a player never benefits from stopping — the rules have players alternate until no unclaimed piece remains). Backward induction defines the value $V(Q)$ of the player to move; the recursion $V(Q) = \max_j [q_j + E(Q\setminus q_j)]$ is exactly "take $q_j$, opponent extracts $V(Q\setminus q_j) = O(Q\setminus q_j)$ from the rest, mover gets the complement $E(Q\setminus q_j)$."
- **Term-by-term comparison** for $j \ge 2$ checked separately for $j$ odd and $j$ even, including boundary/parity effects at the end of the list (indices beyond $r$ contribute $0$; the injection into odd indices is into *distinct* odd indices). Equality at $j=1$ gives both directions at once: A guarantees $\ge O(Q)$ and B holds A to $\le O(Q)$. ✓
- Ties among equal lengths are harmless: fix any nonincreasing enumeration. ✓

### Lemma 2 ($E(Q) \ge \sum \min$ over any disjoint pair system)

- Sorted pair-minima $m_1 \ge \dots \ge m_k$; the first $t$ pairs supply $2t$ elements $\ge m_t$, so $q_{2t} \ge m_t$; and $2k \le r$ guarantees the indices $q_{2t}$ exist. ✓

### Lower bound (Section 2): every Xiang Yu reply to the geometric partition leaves $O(Q) \ge \frac{1+s}2$

- **Counting.** B adds $p \le n$ marks ⇒ $r = n+1+p \le 2n+1$ parts ⇒ $k = \lfloor r/2 \rfloor \le n$ consecutive pairs; the graph on the $n+1$ pieces has $\le n$ edges, so some component has (exactly) $|C|-1$ edges, i.e. is a tree — **note the argument never needs the "non-bipartite ⇒ cycle" direction**, only "connected with $|C|-1$ edges ⇒ tree ⇒ 2-colourable", which is elementary. ✓
- **Isolated-vertex component** ($Y = \varnothing$): then no pair touches $C$, (2.2) reads $0 \le (a_v - s)/2$, true since every piece has length $\ge s$. ✓
- **Distinct-powers step.** $\sum_X a_i / s$ and $\sum_Y a_i / s$ are sums over disjoint sets of distinct powers $2^0,\dots,2^n$; equality would force $X = Y = \varnothing$ by uniqueness of binary representation, contradicting $C \ne \varnothing$; two distinct nonnegative integers differ by $\ge 1$. ✓
- **Part accounting.** Each part lies in exactly one piece; distinct consecutive pairs are disjoint; parts within a piece are disjoint sub-segments — so summing "the $X$-side part of each pair in $C$" is bounded by $\sum_X a_i$. The unpaired part (odd $r$) never appears in $E(Q)$. ✓
- Both (2.2) and (2.3) are stated for the *same* single component $C$, and add to $\frac{1-s}2$ exactly. ✓

### Upper bound (Section 3): Xiang Yu caps Liu Bang at $\frac{1+s}2$ against any marking

- **Case $p \le n-1$**: halving all $p+1 \le n$ pieces is legal (interior midpoints, distinct) and gives $E \ge \frac12$, and $\frac12 < c$ since $c > \frac12$ for all $n \ge 1$. ✓
- **Pigeonhole**: $2^{n+1}$ subset sums in $[0,1]$ including $0$ and $1$; the $2^{n+1}-1$ consecutive gaps sum to exactly $1$, so the minimum gap is $\le s$. Distinctness of $T, T'$ gives $P \cup N \ne \varnothing$; positivity of pieces rules out $P = \varnothing$ (else $\sigma(T) < \sigma(T')$). $N = \varnothing$ is allowed: then $d = \Sigma(W) \le s$ and Lemma 3 degenerates correctly (no pairs, unpaired length $d$). ✓
- **Lemma 3 audit**: induction preserves (i) disjointness of segments, (ii) the imbalance $d$ (both side-sums drop by $|y|$ in both branches), (iii) mark budget $w-1$ ($0$, resp. $\le \max(w-3,0)$, resp. $1 + (w-2)$), (iv) legality of marks — each is strictly interior to a positive-length segment, so distinct from all endpoints (in particular from Liu Bang's marks) and from all earlier marks. Termination: one side empties; remaining unpaired length $= d$ by the invariant. ✓
- **Budget total**: $(|W|-1) + (n+1-|W|) = n$. ✓
- **Conclusion chain**: equal pairs of total length $1-d \ge 1-s$ ⇒ (Lemma 2) $E(Q) \ge \frac{1-d}2 \ge \frac{1-s}2$ ⇒ $O(Q) \le \frac{1+s}2$ ⇒ (Lemma 1, B claims second) Liu Bang gets $\le c$. ✓

### Consistency cross-checks

- $n=1$: formula gives $\tfrac23$; direct hand analysis (pieces $(\tfrac23,\tfrac13)$; B's best reply analysis over one cut) agrees.
- The two bounds are tight against each other: B meets $\frac{1+s}2$ exactly against the geometric partition (split $2^k s \to 2^{k-1}s + 2^{k-1}s$ repeatedly, leaving the $s$-piece unpaired), so no sharper constant is possible in either direction.

---

## B. Computational verification (`problem3_verification.py`)

The claiming phase is replaced by its exact value $O(Q)$ (Lemma 1), and the resulting max–min over cut placements is computed exhaustively on integer grids (Liu Bang's pieces on a coarser sub-grid so that Xiang Yu's integer-position cuts retain the halving/difference strategies relevant at the optimum).

Output of the run (2026-07-16, Python 3, Darwin):

```
n=1, L=12  : max-min = 8/12   at [(8, 4)]   expected 8/12  = 2/3    [0.0s]
n=2, L=140 : max-min = 80/140  at [(80, 40, 20)]   expected 80/140 = 4/7   [0.2s]
n=3, L=120 : geometric A=(64,32,16,8) -> min = 64/120  expected 64/120 = 8/15   [0.0s]
n=3, L=120 : coarse full scan -> max-min = 64/120  at [(64, 32, 16, 8)]   [0.7s]

All checks passed. Total verification runtime: 0.9s
```

All four checks match the closed form $c(n) = \frac{2^n}{2^{n+1}-1}$, and in each scan the **unique** optimal partition on the grid is the geometric one $\propto (2^n, \dots, 2, 1)$, exactly as the proof predicts.

---

## C. Time log

All times US Pacific, 2026-07-16 (wall clock, measured from session/file timestamps and command timing):

| Phase | Interval | Duration |
|---|---|---|
| Deep-think solving session (reduction to odd-index sum, pairing/packing reformulation, discovery of the pigeonhole upper bound and the powers-of-2/tree-component lower bound, dead ends included) | 01:14:24 → 01:39:05 | ≈ 25 min |
| Coding + running brute-force checks ($n=1,2$ full scans, $n=3$ geometric + coarse scan) and skeptical re-derivation of every lemma during write-up | 01:39:05 → ≈ 01:46 | ≈ 7 min |
| **Solving turn total** | 01:14 → ≈ 01:46 | **≈ 32 min** |
| Write-up of `problem3_solution.md`, `problem3_verification.py`, this report; final verification re-run | 09:44 → 09:49 | ≈ 5 min |
| Final verification suite runtime (this file, Section B) | — | 0.9 s |
| **Grand total (both turns)** | — | **≈ 37 min** |

Dead ends explored and discarded during the solving session (for the record): equal-length partitions for Liu Bang (lose to direct pairing, value $\to \tfrac12$); the "alternating chain" bound $\min_j T_j$ alone (only yields $\tfrac{n+1}{2n+1}$, not tight); a naive two-case induction on Xiang Yu's halve/pair moves (fails for $\ge 4$ pieces, fixed by the subset-sum pigeonhole + difference-tree realization).
