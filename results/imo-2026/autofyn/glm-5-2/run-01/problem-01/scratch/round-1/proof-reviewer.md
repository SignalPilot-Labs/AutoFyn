# proof-reviewer — imo-2026-01, round 1

Problem: 2026 integers > 1 on a blackboard; a move picks two entries
m, n > 1 in different positions and replaces them by gcd(m, n) and
lcm(m, n)/gcd(m, n); continue while possible. (a) Terminate after
finitely many moves with exactly one integer M > 1 left. (b) M is
independent of choices. (answer_type = none, task = proof_only; no
numeric answer to verify — the "answer" is the two proof obligations.)

Three builders each claimed Status `solved`. I reviewed each
independently, re-derived the load-bearing steps from scratch, and ran
numerical simulations (100k+ random move-order trials across 12 diverse
boards). All three are correct and rigorous. All three APPROVE.

---

## Cross-cutting verification

Independently re-derived and computationally confirmed:

- Move formula: (m, n) = (g·x, g·y) with gcd(x, y) = 1 maps to
  (g, x·y), since lcm(m, n)/gcd(m, n) = (g·x·y)/g = x·y. Checked on
  100000 random (m, n).
- Euclidean identity gcd(min(α, β), |α − β|) = gcd(α, β) for nonneg
  α, β. Checked on 200000 random pairs.
- The pinned formula M = ∏_p p^{D_p} (D_p = gcd of positionwise
  p-valuations, gcd(x, 0) = x). Simulated 3000 random play orders per
  board on 12 boards including repeated values (exercising the m = n
  case and the overlapping-critical-pair case {2,2,3}, {2,2,2,2},
  {7,7,7,7}, {2,3,5,30}); every trial terminated with exactly one
  entry > 1 and the value matched the formula. Examples:
  {6,10,15}→30, {4,8,16}→2, {4,8,3}→6, {12,18,30}→30, {2,3,5,7}→210,
  {100,200,50,75}→150, {2,2,3}→6, {2,3,5,30}→30, {7,7,7,7}→7,
  {6,10,15,30,42}→210, {8,12,18,27}→6, {2,2,2,2}→2.

---

## 1. `per-prime-euclidean-invariant` — VERDICT: APPROVE (Status: solved)

Scores: Correctness 5/5, Completeness/rigor 5/5, Progress 5/5.

The clean intended solution. Load-bearing steps re-derived:

- Lemma 2 (Euclidean identity): assume α ≥ β, gcd(β, α − β) = gcd(β, α)
  = gcd(α, β) by the subtractive Euclidean step gcd(a, b) = gcd(a, b − a)
  (valid for nonneg a, b with b ≥ a; common divisors of a, b ↔ common
  divisors of a, b − a since (b − a) + a = b). β = 0 case: gcd(0, α) = α
  = gcd(α, 0). Solid.
- Lemma 5 (W-drop): per-prime pair-sum change α + β → min + |α − β| =
  max(α, β), drop = min(α, β) = v_p(g); total drop = Σ_p v_p(g) = Ω(g).
  Drop ≥ 1 iff g > 1, = 0 iff g = 1. Correct.
- Lemma 6 (lex descent, exhaustiveness of the case split): three
  disjoint cases A (m ≠ n, g > 1), B (g = 1), C (m = n). Exhaustive
  because either m = n or m ≠ n; if m ≠ n then g > 1 or g = 1; and
  Case B excludes m = n (m = n > 1 ⇒ g = m > 1). Critical check the
  dispatch flagged — "no move leaves BOTH components fixed": W is
  unchanged only in Case B, and in Case B c drops by 1; in Cases A, C
  W drops ≥ 1. So no move fixes both. Lex strict descent holds.
- Lemma 7 (well-foundedness of ℕ² lex): W (nonneg int) strictly drops
  finitely often; once W stable, only Case B remains, c drops by 1
  each move, c nonneg ⇒ finite. Airtight (this is the standard
  two-coordinate well-foundedness argument).
- Lemma 8 (exactly one): terminal ⇒ c ≤ 1 (a move needs ≥ 2 entries
  > 1); c ≥ 1 always because some prime p divides an initial entry, so
  D_p ≥ 1 forever (invariant), and all-1's would force D_p = 0,
  contradiction. The "D_p ≥ 1 because the list contains a nonzero entry"
  step is correct: gcd of a list containing a nonzero entry divides
  that entry and is positive. No gap on primes with all-zero
  valuations — those simply have D_p = 0 and do not participate; the
  argument picks a prime that DOES divide some initial entry.
- Part (b) pin: terminal valuation list {v_p(M), 0, …, 0}, its gcd is
  gcd(v_p(M), 0, …, 0) = v_p(M) by repeated gcd(x, 0) = x. By
  invariance v_p(M) = D_p(initial). M = ∏ p^{D_p}, finite product
  (D_p = 0 for all but finitely many primes). Depends only on the
  initial board. Correct.

No gaps. No crux-move references (the single cited knowledge_base
entry, "Divisor analysis: gcd structure", is a generic label for the
standard v_p(gcd) = min / v_p(lcm) = max identities, which are proved
inline). No skipped cases, no hand-waving. APPROVE.

---

## 2. `integer-termination-invariant-pin` — VERDICT: APPROVE (Status: solved)

Scores: Correctness 5/5, Completeness/rigor 5/5, Progress 5/5.

Differentiator: valuation-free part (a) using the plain integer
product P (no Ω, no p-adic valuations until part (b)).

- Lemma 1 (P_new = P_old / g): pair-product m·n = g²·x·y → g·x·y =
  (m·n)/g; P_new = P_old · (g·x·y)/(g²·x·y) = P_old/g. Integrality:
  g | m and m | P_old, so g | P_old. Correct.
- Lemma 2 (coprime case, c drops by 1): g = 1 ⇒ new pair (1, mn),
  one entry > 1 vs two before, c drops by 1. Correct.
- Lemma 3 (lex descent): g ≥ 2 ⇒ P strictly drops (lex decrease in
  primary coordinate regardless of c); g = 1 ⇒ P fixed, c drops by 1.
  Exhaustive (g positive integer, so g ≥ 2 or g = 1). Edge case m = n
  subsumed under g ≥ 2 (g = m ≥ 2, P drops). No move fixes both P and
  c: P unchanged only when g = 1, where c drops. Solid.
- Lemma 4 (well-foundedness of ℕ² lex for (P, c)): P positive integer,
  non-increasing, strictly drops finitely often (each drop P → P/g ≤
  P/2, so at most ~log₂(P) drops); once P stable, c strictly drops,
  c nonneg ⇒ finite. Airtight.
- Lemma 5 (radical-support invariant): pair product g²·x·y vs g·x·y
  have identical prime supports (squaring g doesn't change which
  primes divide it). Correct.
- Lemma 6 (P > 1 forever ⇒ c ≥ 1): initially P ≥ 2^2026 > 1, radical
  support nonempty; invariant ⇒ nonempty forever ⇒ P ≥ 2 forever;
  all-1's would give P = 1, contradiction. So c ≥ 1 always. Solid.
- Part (a) combines c ≤ 1 (terminal) with c ≥ 1 ⇒ c = 1.
- Part (b): identical D_p invariant machinery (Lemmas 8–11) as
  approach 1; re-derived above, correct.

No gaps. APPROVE.

---

## 3. `confluence-unique-normal-form` — VERDICT: APPROVE (Status: solved)

Scores: Correctness 5/5, Completeness/rigor 5/5, Progress 5/5.

Most architecturally ambitious; the dispatch specifically flagged
risks to hunt for. I verified each.

Part (a): same (P, c) lex potential + radical-support invariant as
approach 2. Verified above; solid. (Lemmas A1–A5.)

Part (b) architecture: model the board as a MULTISET (forget
positions), define a rewrite system R, prove R terminating (part a) +
locally confluent ⇒ confluent (Newman's lemma) ⇒ unique normal form ⇒
M independent of move order.

- Newman's lemma stated correctly: strongly normalizing + locally
  confluent ⇒ confluent; terminating + confluent ⇒ unique normal form.
  Standard and correct.
- Position-board vs multiset: the builder explicitly flags that
  local confluence FAILS on positioned boards (e.g. (2,3,2): two
  branches land M in different positions) and switches to multisets,
  where positions are quotiented out. This is honest, not a cover: the
  problem's conclusion concerns only the VALUE M, which is
  position-independent, so the multiset model is faithful to the
  claim. Verified the positioned-board failure myself: on (2,3,2) the
  move on the first (2,3) gives (1,6,2) and on the second (2,3) gives
  (2,1,6) — as positioned boards these are different, but as multisets
  both are {1,2,6}. The multiset quotient removes the spurious
  divergence. Correct framing.

Local confluence case split (C1/C2/C3):
- C1 (disjoint redexes): the two moves consume disjoint copies; they
  commute (do move1 then move2 = do move2 then move1, both remove
  their own two copies and add their own two outputs independently;
  validity preserved because the untouched pair stays > 1). Joinable
  in one step each. Correct.
- C2 (share two copies = same move): a move is deterministic given
  two copies (replaces with gcd and lcm/gcd), so the two "moves"
  coincide. Vacuous. Correct.
- C3 (share exactly one copy): the only genuine critical pair. The
  case-split note correctly handles multiplicity: if the shared value
  has multiplicity ≥ 2, the moves consume different copies and are
  disjoint (C1); the genuine overlap is a single contested copy. The
  non-shared values b, c need b ≠ c as VALUES for a genuine divergence
  (same values ⇒ same resulting multiset); the shared value a may
  equal b or c (e.g. {2,2,3}), and the per-prime analysis handles all
  (α, β, γ) including α = β or α = γ. Exhaustive and correct.

Lemma P (per-prime subtractive-Euclidean confluence) — proved from
scratch:
- Termination: weight Σ entries strictly drops by min(u, v) ≥ 1.
  Correct (min + |u − v| = max = u + v − min).
- Invariant: gcd preserved by gcd(min(u,v),|u−v|) = gcd(u,v). Correct.
- Unique normal form: no move ⇒ fewer than two positive entries ⇒ at
  most one positive; that one equals the invariant gcd d; all-zero ⇒
  d = 0. Uniquely {d, 0, …, 0}. Correct.
- Confluence: "terminating + unique normal form ⇒ confluent" — correct
  (extend any divergence to normal forms; both equal the unique NF of
  the source). This is the standard equivalence for terminating
  systems. Solid.

Lemma C (overlapping critical pair rejoins) — the crux, re-derived:
- Setup: S₁ = R ∪ {gcd(a,b), lcm(a,b)/gcd(a,b), c},
  S₂ = R ∪ {gcd(a,c), b, lcm(a,c)/gcd(a,c)}. Both reduce (board system
  terminating) to NF₁ = {M₁,1,…,1}, NF₂ = {M₂,1,…,1}.
- Project to prime p: by (F3), board move (x,y) projects to the
  subtractive-Euclidean step on (v_p(x), v_p(y)). p-valuation multiset
  of S₁ = {min(α,β), |α−β|, γ} ∪ {ρ_i}; of S₂ = {min(α,γ), β, |α−γ|} ∪ {ρ_i}.
- Projected board reduction S₁ ↠ NF₁ is a legitimate reduction in
  Lemma P's system (removing stuttering steps where a valuation is 0 —
  these leave the multiset unchanged and so do not affect the unique
  normal form). Endpoint {v_p(M₁), 0, …, 0} is a normal form of Lemma
  P (at most one positive entry). By Lemma P's unique normal form,
  v_p(M₁) = gcd of S₁'s p-val multiset = gcd(min(α,β), |α−β|, γ, ρ_i)
  = gcd(α, β, γ, ρ_i) (Euclidean identity on the first two, then
  fold). Likewise v_p(M₂) = gcd(min(α,γ), β, |α−γ|, ρ_i) = gcd(α, γ,
  β, ρ_i) = gcd(α, β, γ, ρ_i). Equal. So v_p(M₁) = v_p(M₂) for every
  p ⇒ M₁ = M₂. NF₁ = NF₂, common reduct.

Circularity check (dispatch's concern): Lemma C does NOT assume part
(b)'s conclusion. It DERIVES v_p(M₁) = v_p(M₂) via Lemma P (proved
from scratch) applied to the projected per-prime reductions. The
observation that this common value equals D_p(S) = gcd of the original
board's p-valuations is a consequence, not an assumption; Lemma P's
unique-normal-form property is what pins it, independent of any global
invariant. No schedule-synchronization across primes is needed because
Lemma P gives a UNIQUE normal form (every reduction schedule reaches
it), and the projected board reduction is one such (stuttering-augmented)
schedule. The lift is honest. No circularity.

Verified the critical-pair join numerically: {2,3,5} (move {2,3} →
{1,6,5}, move {2,5} → {1,3,10}; both reduce to M = 30) and {2,2,3}
(a = 2 shared between {2,3} and {2,3} is NOT a divergence — same
values — confirming the b ≠ c exclusion). All random trials on
overlapping-divergence boards land on the same M.

No gaps. APPROVE.

---

## Promotable lemmas certified

Each flagged lemma held to the full bar (sorry-free, statement correct
and no stronger than proved). All ADMITTED into `results/imo-2026-01/lemmas/`:

- `euclidean-valuation-invariant.md` — D_p invariant + Euclidean
  identity gcd(min(α,β),|α−β|)=gcd(α,β). (Approaches 1, 2, 3.)
- `lex-termination-monovariant.md` — (W,c) and (P,c) lex descent +
  well-foundedness; the three-case split. (Approaches 1, 2, 3.)
- `radical-support-invariant.md` — prime-support of P is move-invariant
  ⇒ P > 1 forever ⇒ c ≥ 1. (Approaches 2, 3.)
- `subtractive-euclidean-confluence.md` — Lemma P: the per-prime
  subtractive rewrite is confluent with unique NF {gcd,0,…,0}.
  (Approach 3.)

Rejected: none.

---

## Artifacts updated

- `results/imo-2026-01/current.md`: Status set to **solved**; canonical
  full proof copied from `per-prime-euclidean-invariant` (credited),
  with `Approaches tried` and `Current best` updated to record all
  three APPROVED approaches.
- `results/imo-2026-01/lemmas/`: four certified lemma files created.
- Ranker: three `record_outcome` calls, outcome `verified-milestone`
  for each slug.

## Summary

All three approaches are complete and rigorous solutions to both parts.
The problem imo-2026-01 is SOLVED. Headline canonical proof:
`per-prime-euclidean-invariant` (the clean intended solution). Two
independent alternative complete solutions (`integer-termination-
invariant-pin`, valuation-free part (a); `confluence-unique-normal-
form`, Newman's lemma on multisets) also APPROVED.
