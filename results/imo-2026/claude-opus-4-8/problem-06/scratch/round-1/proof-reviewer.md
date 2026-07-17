# Proof-reviewer — imo-2026-06 (round 1)

Two candidate proofs reviewed independently. Both are honest, rigorous reductions of
the whole problem to a single finiteness crux, with every supporting step airtight and
non-circular. Neither is `solved`. Verdict for both: **CHANGES REQUESTED** (Status
`partial`). Neither reduction is broken, so no RETHINK.

I re-derived the load-bearing steps from scratch and ran an independent simulation
(a₁ ∈ {143,77,15,221}, 3000 terms): the minimal-clause sets, the essential-prime sets,
and the period L=M all reproduce the approaches' claims exactly (a₁=143 → minimal clauses
{2,11},{3,11},{11,13},{2,3,13}, E={2,3,11,13}, L=M=858, T=64), and Lemma S showed zero
violations over 20000 sampled term-pairs per start.

---

## Approach 1 — `clique-descent`

**Score:** Correctness 10/10 · Completeness/rigor 8.5/10 (one clearly-labeled gap) ·
Progress: large (whole problem reduced to one clean isolated lemma).
**True Status: partial.** (Matches the builder's recorded Status.)

### Supporting steps — all verified airtight
- **Tool 1 (gaps ≤ a₁, every term has a prime ≤ P₁):** correct. Multiple-of-a₁ argument
  is valid; the shared prime with a₁ is ≤ P₁.
- **Tool 2 (pairwise gcd>1; every term ∈ A):** correct via gcd symmetry.
- **Sub-lemma E + Cor E.1:** correct. E localizes w between consecutive terms and uses
  minimality; E.1 correctly upgrades "hits every clause" to "is a clause."
- **Corollary 1.1 (every clause has a small prime):** correct, used in Prop 1.
- **Prop 1 (reduction, assuming Lemma S):** re-derived independently and it is airtight.
  For a minimal clause C with large prime q, T=C∖{q} is nonempty; either T hits every
  clause (⇒ T is a clause ⊊ C, contradicting minimality via Cor E.1) or some clause D has
  C∩D={q} (contradicting Lemma S). The two cases are exhaustive and disjoint. Lemma S is
  used exactly once, here.
- **Stabilization (§2):** correct. "Every clause contains a globally-minimal clause"
  holds (minimal element of the finite nonempty family {clauses ⊆ C}), so once all
  finitely many minimal clauses (⊆ Π) have appeared by stage N, every later constraint is
  redundant and A_n = A_N.
- **§3 finish "for EVERY n":** correct and NON-CIRCULAR. a_{n+1}=min(A∩(a_n,∞)) for all n
  follows from a_{n+1}∈A (Tool 2) and A⊆A_n — it does not use Lemma S or periodicity. The
  sequence is then the greedy enumeration of A from n=1.
- **§4 conclusion:** correct, off-by-one clean. Window (e_k,e_k+M] has exactly T members
  of A, largest e_k+M, so e_{k+T}=e_k+M ⇒ a_{n+T}=a_n+L, L=M. Periodicity of A is an
  INPUT from the crux, never assumed to prove itself.

### The gap (the ONLY gap) — confirmed
**Lemma S:** no two clauses share only a large prime (equivalently any two share a prime
≤ P₁). Left as an explicit GAP; partial progress (first-appearance clauses non-minimal,
subject to b>a₁) is correct but does not cover minimal clauses whose large prime is not a
first appearance. Reduction is otherwise complete: proving Lemma S closes the problem.

**Verdict: CHANGES REQUESTED.** Recorded `partial` with note naming Lemma S as the gap.

---

## Approach 2 — `sieve-closure`

**Score:** Correctness 10/10 · Completeness/rigor 8.5/10 (one clearly-labeled gap) ·
Progress: large (independent closure/fixed-point reduction + reusable monovariants).
**True Status: partial.** (Matches the builder's recorded Status.)

### Supporting steps — all verified airtight
- **T1, T2:** identical content to clique-descent, correct.
- **Lemma 1 (vacuous-constraint / fixed-point):** re-derived; correct. If A_n is
  self-consistent then the next term shares a prime with each m∈A_n, so the new constraint
  is vacuous and A_{n+1}=A_n. Genuinely conditional — it does NOT smuggle in the
  enumeration finish (the outline-reviewer's concern is addressed).
- **Lemma 2 (Reduction):** correct. Finite Π ⇒ every A_n is a union of classes mod the
  single fixed modulus M=∏Π ⇒ descending chain in a finite lattice ⇒ stabilizes.
- **Lemma 3 (density-drop monovariant):** correct AND the builder is honest that it is
  insufficient. Effective step ⇒ S_{n+1} contains no stage-n minimal clause ⇒ the product
  of one prime picked outside S_{n+1} from each minimal clause lies in A_n∖A_{n+1}; its
  whole residue class mod M_{n+1} does too, giving drop ≥ 1/M_{n+1}. Since 1/M_{n+1}→0 this
  does not bound the number of effective steps — correctly stated, not overclaimed.
- **Finish §3 (F1–F4), for EVERY n:** correct, same non-circular structure as clique-
  descent's §3–4. F2's two-inequality min-of-superset argument is valid; F4's period count
  is off-by-one clean.

### The gap (the ONLY gap) — confirmed
**Crux:** the set of essential primes Π (primes in some stage-minimal clause) is finite.
Honestly labeled as GAP; the monovariants are explicitly stated NOT to close it. Reduction
is correct: finite Π ⇒ §2–§3 finish. This is essentially the same wall as Lemma S.

**Verdict: CHANGES REQUESTED.** Recorded `partial` with note naming "essential primes
finite" as the gap.

---

## Cross-cutting note for the orchestrator (shared-gap risk)
Both approaches — and per the ranking sidecar also `finite-state-bijection` — bottom out
on the SAME crux: finiteness of the minimal-clause / essential-prime structure. The two
framings (descending-chain vs. closure fixed-point) are correct and produce reusable
lemmas, but they share one wall. Per CLAUDE.md's single-gap-trap guidance, next round's
outliner should put ≥1 approach attacking the crux itself from a genuinely different
framing (e.g. sunflower/Δ-system on the pairwise-intersecting clause family with bounded
core Π, or a descent on the largest prime ever shared), not another reduction to the same
finiteness statement.

## Certification of promotable lemmas
Admitted into `results/imo-2026-06/lemmas/bounded-gaps-and-clique.md` (all sorry-free,
statements correct and no stronger than proved): Tool 1, Tool 2, Sub-lemma E (+Cor E.1),
the for-every-n Finish package, sieve-closure Lemma 1, and sieve-closure Lemma 3 (flagged
insufficient-alone). NOT certified: Lemma S / "essential primes finite" — that is the open
crux and remains unproved.

## Goal progress
Headline `solved` NOT reached. Real progress: the whole problem is now rigorously reduced
— by two independent, mutually-corroborating framings — to a single isolated finiteness
lemma, with a full suite of certified reusable lemmas and a verified for-every-n finish.
The bound (period L=M, T=|A mod M|) is computationally confirmed. Remaining distance: one
crux (Lemma S / essential-primes-finite), which is the genuine hard core of the problem.
