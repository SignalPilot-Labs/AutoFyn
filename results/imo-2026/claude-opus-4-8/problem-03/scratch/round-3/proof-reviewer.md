# Proof-reviewer report — imo-2026-03 (IMO 2026 P3), Round 3

Answer c(n) = 2^n/(2^{n+1}−1) is confirmed (not re-litigated). Problem is `compute_and_prove`,
`answer_type: expression`; answer stated explicitly. Reviewed 3 built approaches independently.
All shared load-bearing lemmas (Lemma G, measure form of A, merge identity) re-checked and remain valid.

Independent numerical verification of every NEW claim (all with exact `Fraction` arithmetic, bounded):
- LL t=1 bound A(Q∪R) ≥ 1 (Q={q,2^n−q}, A(R)≥1, max(R)≤2^{n−1}): 5000 configs, n=2,3,4 — **0 violations**.
- Regime A shadow: val = A_1 exactly and ≤ c(n): 301 random spectra, n≤4 — **0 mismatches**.
- Prop 4 replica at G_n: A(replica)=1, val=2^n for n=1..5 — **exact match**.
- Lemma P (odd count, all pieces ≥1 ⇒ A ≥1): 20000 samples — **0 violations**.
- n=2 t=2 casework (A(Q∪{1,2})≥1 and s_0+s_2≥s_1): all 48 partitions of 4 — **0 violations**.
- n=1 maximin V(A): grid confirms **unique** maximizer at geometric a=2/3, V=2/3 (S1 route viable).

---

## Approach 1: geometric-selfsimilar — Status: partial — Verdict: CHANGES REQUESTED

**New content this round, all reviewer-verified correct:**

1. **LL sub-case t=1 (single cut of 2^n).** Re-derived from scratch. Q={q,2^n−q}, q≤2^{n−1} makes S_Q a
   single interval [q, 2^n−q) of measure A(Q)=2^n−2q. Since S_R ⊆ [0,max(R)) ⊆ [0,2^{n−1}), the overlap
   B=meas(S_Q∩S_R) ⊆ [q,max(R)) gives **B ≤ (max(R)−q)^+**. Then A(Q∪R)=A(Q)+A(R)−2B ≥ 2^n−2·max(R)+A(R)
   ≥ A(R) ≥ 1 (using max(R)≤2^{n−1} ⟹ 2^n−2·max(R)≥0). The M≤q case gives B=0 directly. **Rigorous and
   correct.** The bound direction (upper bound on B, which enters with a minus sign) is right; the
   merge identity is the certified one. Conditional on A(R)≥1 (IH), which is legitimate as a reduction
   step. Certified → `lemmas/ll-t1-single-cut.md`.

2. **Upper-bound Regime A (1/2 ≤ A_1 ≤ c(n), shadow strategy).** Re-derived. XY cuts A_1 into
   {A_2,…,A_m, r}, r=2A_1−1≥0, using m−1≤n cuts, all interior to A_1 hence legal/distinct. Every A_i
   (i≥2) then appears twice ⇒ N even except on [0,r) ⇒ A(final)=r ⇒ val=(1+r)/2=A_1≤c(n). **Rigorous and
   correct**; cut budget, distinctness, and part-positivity all check. Certified → `lemmas/shadow-regime-A.md`.

3. **n=2 lower bound (previously a grid assertion) now rigorous.** t∈{1,2}. t=1 via LL t=1; t=2 reduces
   to s_0+s_2≥s_1 with S_Q=[0,q_3)∪[q_2,q_1). The explicit casework is complete and its conclusion is
   confirmed on all 48 partitions. **c(2) ≥ 4/7 is now fully rigorous** (with Case 1 and base). Good.

**Gaps remaining (correctly labelled open, not papered over):**
- **LL sub-case t≥2 with A(Q)>0** — the load-bearing shared lower-bound gap. The two-sided merge bound
  b+|a−A(R)| is honestly shown too weak (34/286). Left explicit.
- **Upper-bound Regime B (A_1<1/2)** and **Regime C (A_1>c(n))** — not written; honestly open.

The Status `partial` recorded in the file is **correct**. Genuine, verified advance on both bound sides.
No overclaim detected. Scores: Correctness 10/10, Rigor 9/10 (open gaps clearly flagged), Progress: high
(two sub-cases closed + n=2 fully rigorous). → **CHANGES REQUESTED**: close LL t≥2 (A(Q)>0) and upper
Regimes B/C.

---

## Approach 2: alternating-sum-value — Status: partial — Verdict: CHANGES REQUESTED

**New content, verified:**

1. **Lemma LL-1** — identical mathematics to geometric-selfsimilar's LL t=1 (single-interval S_Q +
   max(R)≤2^{n−1}). **Correct.** The base n=1 handling (R={1}, max=1≤1, A(R)=1) is valid. Duplicate of
   the certified `ll-t1-single-cut.md`; I certified one canonical file rather than two.

2. **Lemma P** — odd piece count + all pieces ≥1 ⇒ A ≥1, one line: A ≥ trailing term = min piece ≥1.
   **Correct and trivially rigorous.** Honestly flagged as a *restricted* family (requires odd k AND no
   piece <1), so it does NOT close the residual gap. Certified → `lemmas/parity-piece-count.md`.

3. **Greedy potential-decrease upper bound: recorded DEAD-END.** Verified honest: greedy stalls at
   A≈0.287 on (0.649,0.351) at n=2 while target 1/D≈0.143 and the true optimum reaches A≈0. Correctly
   concludes greedy is sub-optimal (needs lookahead). Good discipline (pre-checked before writeup).

**Gaps:** GAP AL (= LL t≥2 residual) and GAP AU (universal upper bound) both open. Status `partial`
recorded is **correct**. Scores: Correctness 10/10, Rigor 9/10, Progress: moderate (t=1 closed for this
file + Lemma P slice + a dead-end mapped). → **CHANGES REQUESTED**: attack GAP AL beyond the parity
slice; GAP AU needs a lookahead strategy (greedy is dead).

---

## Approach 3: extremal-smoothing — Status: partial — Verdict: CHANGES REQUESTED

**New content (first build), verified:**

1. **Props 1–2 (framework).** V(A)=min over XY's ≤n cuts of val is continuous on the compact simplex Δ
   (uniform continuity of a continuous function on compact Δ×K; ties do not make val jump; distinctness
   handled by density → min over closure K), hence attains its max by the **Extreme Value Theorem**
   (KB entry "Extreme value theorem" — legitimate citation). The "Berge Maximum Theorem" name is
   over-stated, but the actual justification given is elementary uniform continuity and is **correct**.
   Rigorous.

2. **Prop 4 (replica bound V(G_n) ≤ c(n)).** Re-derived: midpoint-halving gives value 2^j twice
   (j=1..n−1) and value 1 thrice; N is odd only on [0,1) ⇒ A=1 ⇒ val=2^n=c(n)·D. **Verified exactly for
   n=1..5.** Rigorous.

3. **Prop 3 (reduction).** "upper bound ⟸ S1 + replica, with NO use of LL" — a **valid logical
   implication**: if S1 (every non-geometric A admits A' with V(A')>V(A)) holds, the maximizer must be
   G_n, and Prop 4 caps V(G_n). Correctly separates the upper-bound gap from the lower-bound gap LL.

Framework certified → `lemmas/extremal-framework.md` (Parts 1 continuity/attainment + 2 replica).

**Gaps:**
- **S1 (unique maximizer / smoothing monotonicity)** — the load-bearing bet. OPEN and honestly so;
  Prop 5 correctly shows V is only *cell-locally* concave (not globally), so "stationary ⇒ max" is
  invalid, and the global exchange step is unavoidable. Numerically G_n is the unique maximizer for
  n=1 (I verified independently) and n=2, so the route is **viable**, not dead — hence not RETHINK.
- **LL** — imported lower-bound dependency, shared with the other two approaches.

Status `partial` recorded is **correct**. The claim in the file's "Approaches tried" that Prop 3 is a
clean LL-independent reduction is accurate. Scores: Correctness 10/10, Rigor 9/10, Progress: solid (a
rigorous framework + a genuine bypass of per-config XY strategies, reducing the whole upper bound to one
statement S1). → **CHANGES REQUESTED**: prove S1 (or its non-strict variant sufficient for max V ≤ c(n)).

---

## Certified lemmas this round
- `lemmas/ll-t1-single-cut.md` — LL t=1 single-cut (from geometric-selfsimilar; = alternating-sum-value's
  LL-1). **CERTIFIED.** One canonical file for both proposals (avoid duplicate `case2-single-cut.md`).
- `lemmas/shadow-regime-A.md` — shadow strategy, upper-bound Regime A. **CERTIFIED.**
- `lemmas/parity-piece-count.md` — Lemma P (restricted). **CERTIFIED** (scope note added).
- `lemmas/extremal-framework.md` — V continuous on compact Δ + max attained (Props 1–2) + replica bound
  V(G_n)≤c(n) (Prop 4). **CERTIFIED.**
- Prop 3 reduction: valid as a logical implication but conditional on the open S1; not stored as a
  standalone lemma (it is a proof-structure step, and folding it in would risk reading as unconditional).

## Overclaim check
No approach marked itself `solved`; all three self-report `partial`, matching the true state. No hidden
gaps found in the claimed-closed steps; every "closed" sub-case is genuinely gap-free. The three files
correctly and explicitly flag their open gaps.

## Goal progress (for eval history)
Status stays **partial** (no APPROVE — both bound sides still have load-bearing gaps). Real advances:
lower bound now fully rigorous for n=1,2 (was grid-asserted for n=2); LL t=1 tail closed generally;
upper-bound Regime A closed; a rigorous extremal framework reduces the entire upper bound to a single
LL-independent statement S1. Ranking after R3 (Elo): geometric-selfsimilar **1558.9** (advanced) >
alternating-sum-value **1499.5** (advanced) > extremal-smoothing **1441.6** (advanced, first build).
Shared plateau gap = **LL t≥2 (A(Q)>0)**; upper-bound frontier now splits into Regime B/C (geometric)
vs. S1 (extremal) — the extremal S1 route is the most promising single remaining target and is
LL-independent.

---

### Per-slug verdicts
- **geometric-selfsimilar — CHANGES REQUESTED** (Status: partial)
- **alternating-sum-value — CHANGES REQUESTED** (Status: partial)
- **extremal-smoothing — CHANGES REQUESTED** (Status: partial)
