## imo-2026-01 (monovariant route)

- **Distinct openings (all close the whole problem from the monovariant side):**
  1. **W = Σ Ω(entry)** (total prime factors with multiplicity) as the primary integer monovariant. Per move on (m,n) with g=gcd(m,n): write m=g·a, n=g·b, gcd(a,b)=1. Then the pair becomes (g, ab). Accounting: old Ω-sum = Ω(g)+Ω(a) + Ω(g)+Ω(b) = 2Ω(g)+Ω(a)+Ω(b); new = Ω(g)+Ω(a)+Ω(b). **ΔW = −Ω(g) ≤ 0**, strict iff g>1. Verified numerically.
  2. **C = #{entries > 1}** as companion monovariant. Three exhaustive cases on a move (m,n)→(g, ab) with m,n>1:
     - coprime (g=1): pair → (1, mn); one entry collapses to 1, so **C drops by 1**, W unchanged.
     - equal (m=n): g=m, ab=1; pair → (m,1); **C drops by 1**, W drops by Ω(m).
     - intermediate (g>1, a>1, b>1): pair → (g, ab), both >1; **C unchanged**, W drops by Ω(g)≥1.
     C is non-increasing; whenever C is unchanged, W strictly decreases.
  3. **Lex monovariant (W, C) strictly decreases** every move (coprime: (W,C)→(W,C−1); equal: both down; intermediate: (W−Δ, C)). Both bounded below by 0 → termination in ≤ W_init + C_init moves. (Equivalently: W non-increasing integer ⇒ ≥1-drop moves ≤ W_init; once W stable only coprime moves remain ⇒ ≤ C_init more.) **This closes part (a)'s "finitely many moves".**
  4. **Invariant ruling out the all-1s terminal state AND giving uniqueness (part (b)):** for each prime p, define G_p := gcd of the multiset {v_p(entry_i) over all i}, using gcd(0,k)=k. Under a move the pair of p-valuations (α,β) (assume α≤β) becomes (min(α,β), max(α,β)−min(α,β)) = (α, β−α), which is one subtractive-Euclidean step; **gcd of a pair is preserved: gcd(α,β)=gcd(α,β−α)**, hence the gcd over the whole board G_p is **invariant**. The product Q := ∏_p p^{G_p} (finite product, only primes hitting some entry contribute) is an **invariant of the board**.

- **Candidate technique(s):** integer-valued monovariant for termination (knowledge_base "Invariants & monovariants"); subtractive-Euclidean / gcd-of-valuations invariant for the structural conclusion. The p-adic perspective (one prime at a time) is what makes both the monovariant and the invariant transparent.

- **Cheap-kill candidates:**
  - The all-1s terminal state is killed for free by the invariant Q: in an all-1s board every v_p=0 so G_p=0 and Q=1; but initially every entry >1, so some prime p divides at least one entry, giving G_p ≥ 1 there, hence **Q > 1** — contradiction. (No heavy construction.)
  - Uniqueness (part (b)) is the same invariant: in the one-entry terminal state the board's v_p multiset is {v_p(M)}, so G_p = v_p(M); thus **M = Q**, determined solely by the initial board. Done — no separate argument.
  - The "exactly one" then needs no work: termination ⇒ ≤1 entry >1; Q>1 forbids 0; hence exactly 1.

- **Knowledge-base entries to use:** "Invariants & monovariants" (line 117); strategy "Invariant / monovariant" (line 191); "p-adic valuation" subtopic framing. The "combinatorial descent / infinite descent" sibling (line ~185) is the structural twin for the integer-potential drop.

- **Analogous past problems (cruxes):**
  - **aimo-0193** — crux: "Prove a process terminates by exhibiting an integer-valued quantity that strictly [monotone] every move" + "Cap the strictly-increasing monovariant by identifying a quantity the operation leaves invariant." Directly the (W,C)+Q template: integer potential that monotones each move, plus an invariant that pins the terminal state. Strongest analog.
  - **aimo-0595** — crux: "Replace a real-valued termination potential with an integer count of how many fixed objects…" mirrors using Ω (an integer factor count) rather than the real-valued product, to get a genuine termination count.
  - **aimo-0917** — crux: "Assign each board entry a conserved 'weight'" + "preserve a chosen 2-adic residue as invariant" — spirit-match for the G_p invariant (a gcd-of-valuations conserved quantity) constraining the terminal board.

- **Prior progress:** none (round 1, empty workspace).

- **Dead ends (do not retry):** none yet. Pitfall to flag for the builder: do **not** try to use the total product ∏ entries as the monovariant — it is non-increasing (mn → lcm ≤ mn) but not integer-useful for a strict per-move drop and gives no uniqueness; the right monotone quantity is W = Σ Ω, and the right invariant is Q (gcd-of-valuations), not the product.

- **Small-case / intuition notes (conjecture, then verified):**
  - Simulated the process to termination on {[6,10],[4,8],[12,18],[8,8],[4,4,8],[6,10,15],[2,3,5,7],[12,18,24],[100,75,30],[30,42,70,105]} (20 random play-outs each). **Every play-out terminated in a single entry, and that entry equalled Q = ∏ p^{gcd of v_p's} in every case.** (E.g. [6,10]→30; [4,8]→2; [12,18]→6; [8,8]→8; [4,4,8]→2; [30,42,70,105]→210.) This is verified evidence, not a proof — the proof is the W/C-lex descent (part a) and the G_p invariance (part b), sketched above and left for the outliner to formalize.
  - The accounting ΔW = −Ω(gcd(m,n)) was checked move-by-move on a tracked run ([12,18,24,30]→30): coprime moves gave ΔW=0, ΔC=−1; all others gave ΔW<0. Matches the case table exactly.
  - **Pitfall:** the "equal" case m=n must be listed separately from "intermediate" because its C-account (−1, since lcm/gcd=1) differs from the generic g>1 case (C unchanged). A sloppy two-case split (coprime vs. not) mishandles C; the rigorous split is {coprime, equal, intermediate}.
