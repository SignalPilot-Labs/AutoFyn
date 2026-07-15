# Build report — round 1 — imo-2026-03 — slug: self-similar-induction

## Status: solved (claimed complete; ready for proof-reviewer)

## What happened

The reviewer's hole (n = 3, q = (0.35, 0.245, 0.235, 0.17): no strip-k move, U1 fallback fails) exposed that the whole strip-k/cascade upper-bound architecture was fragile. Instead of patching it, I replaced BOTH hard mechanisms with two new, much cleaner lemmas, and closed the entire problem. The approach file `results/imo-2026-03/approaches/self-similar-induction.md` now contains a complete, self-contained prose proof of

**c(n) = 2^n / (2^{n+1} − 1)**, D = 2^{n+1} − 1.

## Architecture of the proof (all in the approach file, §1–§10)

Everything routes through δ(q) = min over nonzero x ∈ {−1,0,1}^k of |x·q| for LB's piece vector q:

1. **Lemma C** (§1): claiming value = Odd(P) — both one-sided guarantees by simultaneous exchange induction (case computation for the second player's greedy reply written out for i even/odd). Works for nonnegative multisets, so endpoint-mark/zero-piece interpretation issues vanish.
2. **Lemma D + D′** (§2): layer-cake identity Δ = |{x : N(x) odd}|; pairs-plus-leftovers gives Δ ≤ Σ leftovers.
3. **Lemma R** (§4): for ANY nonzero x ∈ {−1,0,1}^{m+1}, XY can realize "equal pairs + leftovers of total |x·q|" with ≤ m legal marks: halve the x_i = 0 pieces (self-pairs), superpose the +1 pieces against the −1 pieces laid end-to-end (≤ |A|+|B|−1 cuts). Mark count |Z| + |A| + |B| − 1 = m exactly. Cut positions strictly interior, pairwise distinct, distinct from LB's marks.
4. **Lemma P** (§5): subset-sum pigeonhole — 2^{m+1} subset sums in [0,S] into 2^{m+1}−1 boxes ⇒ some nonzero x has |x·q| ≤ S/(2^{m+1}−1). This bound is exactly tight at the geometric configuration (subset sums equally spaced) — zero slack, as required.
5. **Upper bound** (§6): m < n marks ⇒ halve everything, Δ = 0; m = n ⇒ P + R give Δ ≤ 1/D ⇒ LB ≤ 2^n/D. The reviewer's counterexample is handled as a worked example: x = (0,+1,−1,0), Δ = 0.01 ≤ 1/15, 3 marks.
6. **Lemma T** (§7) — the new lower-bound mechanism, replacing gap L1 entirely: any refinement of k pieces by ≤ k−1 cuts has Δ ≥ δ(q). Proof: sort and pair consecutively (Σ gaps + odd leftover = Δ); build the home multigraph on the k original pieces, one edge per pair; #edges ≤ ⌊(2k−1)/2⌋ = k−1 < k = #vertices ⇒ some component is a loopless simple tree; properly 2-color it, extend by 0 ⇒ nonzero x ∈ {−1,0,1}^k with |x·q| ≤ Δ(P).
7. **Lemma G** (§8): δ(geometric) = u by uniqueness of binary representation (mod-2^{j0+1} argument).
8. **Lower bound** (§9): geometric marking + T + G ⇒ Δ ≥ 1/D ⇒ LB ≥ 2^n/D.
9. **Conclusion** (§10): answer stated and verified at n = 1 (2/3) and n = 2 (4/7), equality plays exhibited both ways.

## Verification performed (checks, not proof steps)

- Lemma C vs exact recursive game solver: 200 random multisets, |P| ≤ 6 — exact match.
- Lemma T (Δ ≥ δ(q)): 3000 random refinements (m ≤ 4) + adversarial random search (2000 replies per config) — no violation.
- Lemma P bound: 5000 random configs, m ≤ 6 — holds.
- End-to-end upper bound (pigeonhole x + Lemma R construction, mark counting included): 4000 random configs, n = 1..5 — marks ≤ n and Δ ≤ 1/D always; reviewer's counterexample reproduced (Δ = 0.01, 3 marks, LB = 0.505 ≤ 8/15).

## Remaining gaps

None claimed. Points the reviewer should scrutinize:
- Lemma C's case computation for i odd/even (the sums telescope into Σ(p_{2k−1} − p_{2k}) ≥ 0 — written out).
- Lemma R's cut-count bookkeeping and mark-legality (strict interiority, coincidence handling — argued explicitly).
- Lemma T's "some component is a loopless simple tree" step (E = V−1 + connectivity ⇒ no loops/parallel edges — argued via underlying simple graph edge count).
- Endpoint-mark/zero-piece interpretation note in §0 (both readings give the same value via Lemma C on nonnegative multisets).

## Promotable lemmas

C, D+D′, R, P, T, G — all fully proved in the approach file; listed with statements in its `## Promotable lemmas` section. C/D are the shared cache candidates the outline requested; R+P+T+G are the new load-bearing quartet, and T in particular is a general-purpose lower-bound tool the sibling approaches (pairing-defect G4, exact-value E3) could import to close their own lower-bound gaps.

## Spec concerns

None. The problem statement's "marked points are distinct" and "at most n" are both respected in every construction; the answer type (expression) is stated explicitly: c(n) = 2^n/(2^{n+1} − 1).
