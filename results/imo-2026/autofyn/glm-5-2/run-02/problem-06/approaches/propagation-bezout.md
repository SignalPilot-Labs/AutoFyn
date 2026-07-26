# Approach: propagation-bezout

## Status
partial

## Approaches tried
- (round 2, NEW) Propagation route (Route P, corpus crux `aimo-0648` (ii)+(iii)): propagate small-prime sharing from the consecutive seed (Lemma 3) outward to non-consecutive pairs via Bezout-style composition of index-shifts. **Outcome: route is CIRCULAR AS FILED.** The gap-bound window (Lemma 2) alone yields only the GROWING bound "shift-k pairs share a prime ≤ k·R" — not the FIXED bound "≤ R" needed for Lemma 4. The only natural P6-native shift algebra is the residue-walk map φ from essential-monovariant's Theorem (Section 5), but φ is defined via the transversal family V, whose free-rider-irrelevance claim IS Lemma 4. So propagation as a *proof* of Lemma 4 uses Lemma 4 to define its own composition law. Additionally, "shares-a-small-prime" is NOT a transitive relation along index-shifts in general (concrete obstruction: (a_i,a_{i+1}) shares r, (a_{i+1},a_{i+2}) shares s with r≠s; a_{i+1} carries both but this forces nothing about (a_i,a_{i+2})), so Bezout composition cannot close without an external transitivity mechanism. The only extractable partial ("a_1 shares a small prime with every term a_j, j≥2") is a direct corollary of Lemma 1 (already certified in essential-monovariant) and yields no new promotable lemma. Honest verdict: the propagation framing is genuinely different in mechanism but does not advance the crux; it stays live in the ranker as a registered third route, with the circularity definitively characterized at the sub-step where the shift algebra is defined via V. — partial (route stuck on circularity; partial subsumed by Lemma 1).

## Current best
A complete characterization of *why* propagation cannot close Lemma 4 from pre-Lemma-4 ingredients, plus one weak partial result that is a corollary of an already-certified lemma.

**Partial result (extractable, but subsumed by Lemma 1).** For every j ≥ 2, the pair (a_1, a_j) shares a prime ≤ R. Mechanism: by Lemma 1 (essential-monovariant, certified), a_j is divisible by some prime q ∈ P(a_1); since q | a_1 and q | a_j and q ≤ R (P(a_1) ⊆ Q_R), q is a small shared prime of (a_1, a_j). This is exactly Lemma 1 restated for the pair (a_1, a_j) — it adds nothing beyond the certified anchor and is **not** a new promotable lemma.

**Circularity characterization (the route's main deliverable).** The propagation step (Step 4) requires a shift-composition law: "if (a_i, a_{i+k}) and (a_{i+k}, a_{i+k+ℓ}) each share a small prime, then (a_i, a_{i+k+ℓ}) shares a small prime" (or some Bezout-style analogue). Two obstructions, both fatal for a pre-Lemma-4 proof:

1. **Non-transitivity of "shares-small-prime".** Two integers m, n each sharing a small prime with a common partner z (m via r, n via s, with r ≠ s) need not share any prime at all. Concrete instance in our setting: by Lemma 3, (a_i, a_{i+1}) shares some r ≤ R and (a_{i+1}, a_{i+2}) shares some s ≤ R; if r ≠ s, a_{i+1} carries both r and s, but nothing forces (a_i, a_{i+2}) to share either. Verified: the relation is genuinely non-transitive. So shift-1 → shift-2 propagation is **not automatic**; it requires an extra input.

2. **The only P6-native composition law needs Lemma 4.** The natural "index-shift algebra" on the greedy sequence is the residue-walk map φ : V → V (cyclic successor on the valid-residue set V) from essential-monovariant's Theorem (Section 5). But V is *defined* as { r mod L_0 : τ(r) ∈ H_∞ } where H_∞ is the transversal family of F_∞ = {τ(a_i) : i ≥ 1}, and the **free-rider-irrelevance claim** (a_{n+1} mod L_0 ∈ V for all n) is proved in essential-monovariant's Theorem using Lemma 4. So φ presupposes Lemma 4. Any "Bezout composition of shifts" built on φ is, by construction, a composition built on top of Lemma 4 — making propagation of Lemma 4 *via* φ circular.

3. **The gap-bound window alone gives only the growing bound.** Without φ, the only shift-invariant input is Lemma 2: a_{n+1} − a_n ≤ R. Composing k consecutive gaps gives a_{i+k} − a_i ≤ k·R. So any prime shared by (a_i, a_{i+k}) satisfies p | (a_{i+k} − a_i) ≤ k·R, hence p ≤ k·R. This is the **growing bound** (≤ k·R for shift-k pairs) — exactly the same obstruction the outline-reviewer flagged for grid-counting-shared-primes (Step 6 there gives ≤ (N−1)R). To collapse k·R → R one needs the free-rider dichotomy, which is Lemma 4 itself. So the gap-bound window does not supply a pre-Lemma-4 composition.

Hence: **the propagation route is circular as a proof of Lemma 4.** No promotable new lemma arises; the only partial is subsumed by Lemma 1.

## Full proof
(present when Status is `solved`. The route is `partial`; no full proof.)

---

## Skeleton (Steps 1–5), with the circularity pinned to an exact sub-step

### 0. Definitions and notation (inherited from essential-monovariant)
- P(m) = set of prime divisors of m.
- R := rad(a_1) = ∏_{p | a_1} p ; Q_R := { p prime : p ≤ R } ; L_0 := ∏_{p ∈ Q_R} p.
- Q_R-type τ(m) := P(m) ∩ Q_R (depends only on m mod L_0).
- Essential set E := { p prime : p is the unique shared prime of some pair (a_i, a_j), i < j }.
- The greedy rule: a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1 ∀ i ≤ n }.

### 1. Lemma 1 (cheap structural anchor) — INHERITED (essential-monovariant §1)
**Lemma 1.** *Every term a_n is divisible by some prime divisor of a_1; in particular τ(a_n) ≠ ∅ and τ(a_n) ∩ P(a_1) ≠ ∅.*
Proof in `essential-monovariant.md` §1. **Not reproved.**

### 2. Lemma 2 (gap-bound monovariant) — INHERITED (essential-monovariant §2)
**Lemma 2 (Gap bound).** *a_{n+1} − a_n ≤ R for every n ≥ 1.*
Proof in `essential-monovariant.md` §2 (next-multiple-of-R candidate is admissible by Lemma 1). **Not reproved.**

### 3. Lemma 3 (consecutive seed) — INHERITED (essential-monovariant §3)
**Lemma 3.** *If p ∈ P(a_n) ∩ P(a_{n+1}), then p ≤ R. So every consecutive pair shares a small prime (the consecutive seed).*
Proof in `essential-monovariant.md` §3 (shared prime divides the gap ≤ R). **Not reproved.**

This is the **seed of small-prime sharing**: every shift-1 pair (a_n, a_{n+1}) has τ(a_n) ∩ τ(a_{n+1}) ≠ ∅.

### 4. Step 3 — Extremal-forces-equality sub-lemma (aimo-0648 crux (ii), ported) — PARTIAL / STUCK

**aimo-0648 crux (ii) (corpus).** "If the floored mean of the predecessors equals the maximum M, then every predecessor equals M." Mechanism: extremal value forces all arguments to the extremal, because the sum is pinned and each summand is bounded above by M.

**Ported statement (P6 analogue).** Suppose a_{n+1} is the greedy minimum and suppose there is an index i_0 < n such that (a_{i_0}, a_{n+1}) shares only large primes > R. Then for every "cheap" candidate m ∈ (a_n, a_{n+1}) that hits a_{i_0} via a small prime q ≤ R, m must fail admissibility against some other a_k (k ≤ n, k ≠ i_0); otherwise m would be admissible and < a_{n+1}, contradicting greedy minimality.

This sub-lemma is **true but vacuous as a partial**: it merely restates the greedy minimality of a_{n+1} (any m ∈ (a_n, a_{n+1}) is inadmissible ⇒ for each such m there is a killing index k(m)). The aimo-0648 lever "extremal value forces all arguments to the extremal" does not port cleanly, because P6's "argument list" (the set of earlier terms) is not a finite list whose entries are pinned by a single sum; the "extreme" a_{n+1} is the min admissible, not a max-of-inputs, and there is no conserved sum to pin the entries.

**Extractable partial (subsumed by Lemma 1, NOT promotable).** Applying Lemma 1 to a_{n+1}: a_{n+1} is divisible by some q_* ∈ P(a_1) ⊆ Q_R. Since q_* | a_1 and q_* | a_{n+1}, the pair (a_1, a_{n+1}) shares the small prime q_*. So:

> **(Weak partial.)** For every n ≥ 1, the pair (a_1, a_{n+1}) shares a prime ≤ R.

This is exactly Lemma 1 (the cheap anchor) specialized to the pair (a_1, a_{n+1}); it is already covered by the certified Lemma 1 and yields no new promotable material. Combined with Lemma 3 (the consecutive partner), a_{n+1} shares small primes with at least two distinct earlier terms {a_1, a_n} (for n ≥ 2); but no propagation *between* these two seeds is available without the composition law of Step 5.

**Why the sub-lemma does not yield a stronger partial.** To upgrade "a_{n+1} shares a small prime with a_1 and with a_n" into "a_{n+1} shares a small prime with a_i for *every* i ∈ [1, n]", we would need: for each i ∈ [2, n−1], either q_* (the prime of a_1 dividing a_{n+1}) also divides a_i, or some other small prime of a_{n+1} divides a_i. There is no pre-Lemma-4 reason this should hold: q_* is one prime of a_1, and the a_i (i ∈ [2, n−1]) need not be divisible by q_* — they are each divisible by *some* prime of a_1 (Lemma 1), but possibly a different one. No pigeonhole over the finite P(a_1) closes this for fixed n: P(a_1) has |P(a_1)| elements and we have n−1 indices; pigeonhole would force *some* prime of a_1 to recur among the a_i, but not necessarily q_*. So no strengthening is extracted. [GAP]

### 5. Step 4 — Bezout-propagation (aimo-0648 crux (iii), ported) — **CIRCULAR AS FILED [GAP]**

**aimo-0648 crux (iii) (corpus).** "Choose integers c_i with ∑ c_i d_i ≡ 1 (mod T); compose index-shifts by d_i into a shift by 1, so x_n = M ⇒ x_{n−1} = M, forcing M everywhere." Mechanism: a Bezout combination of available index-shifts, mod the period T, collapses to a shift by 1, propagating the extremal-equality to every index.

**Ported statement (P6 analogue, desired).** Define a shift-composition law on indices: "shift by k" relates a_i and a_{i+k}. If small-prime-sharing is invariant under composition of shifts, and the available shifts have gcd 1 (Bezout), then small-prime-sharing propagates from shift 1 (Lemma 3) to every shift k ≥ 1, yielding Lemma 4.

This is the **load-bearing and speculative step**, and it is **circular as filed**. We pin the circularity to the exact sub-step:

**Sub-step 4a (define the shift algebra).** To compose shifts we need a well-defined map "shift by k" on residues — i.e. a function φ_k with φ_k(r_n) = r_{n+k} (where r_n = a_n mod L_0). The only P6-natural candidate is the residue-walk iterates φ^k where φ : V → V is the cyclic successor on V.

**Sub-step 4b (where Lemma 4 enters).** V := { r ∈ {0, …, L_0−1} : τ(r) ∈ H_∞ }, where H_∞ = { S ⊆ Q_R : S ∩ T ≠ ∅ ∀ T ∈ F_∞ } is the transversal family of F_∞ = { τ(a_i) : i ≥ 1 }. The claim that **a_{n+1} mod L_0 ∈ V** for every n (i.e. r_{n+1} = φ(r_n) for the cyclic successor φ on V) is the *free-rider-irrelevance claim*, proved in essential-monovariant's Theorem (Section 5, "Claim (free-rider irrelevance)") **using Lemma 4**. Specifically, the direction "a_{n+1} has transversal type" in that Claim invokes Lemma 4 to assert that a_{n+1} shares a Q_R-prime with every a_i (not just the earlier ones i ≤ n, but all i ≥ 1). Without Lemma 4, we cannot show a_{n+1} mod L_0 ∈ V, hence φ is not defined as a self-map of V that the orbit {r_n} lives in.

**Sub-step 4c (the circularity).** Propagation of Lemma 4 *via* φ^k would use "r_{n+k} = φ^k(r_n)" — but this identity is the *output* of the free-rider-irrelevance Claim, which uses Lemma 4. So propagation of Lemma 4 via φ presupposes Lemma 4. **The composition law is defined via V; V is defined via H_∞; H_∞'s relevance to the greedy (a_{n+1} mod L_0 ∈ V) is Lemma 4. Circular.**

### 6. Attempt at a pre-Lemma-4 shift algebra — HONEST FAILURE

We attempt to build a composition law from the gap-bound window (Lemma 2) alone, without invoking V.

**Pre-Lemma-4 shift fact (provable, growing bound).** For any i ≥ 1 and k ≥ 1, the pair (a_i, a_{i+k}) shares a prime p with p ≤ k·R.

*Proof.* By the greedy rule at stage i+k−1, gcd(a_{i+k}, a_i) > 1, so a_i and a_{i+k} share some prime p. By Lemma 2 applied k times, a_{i+k} − a_i = ∑_{j=0}^{k−1} (a_{i+j+1} − a_{i+j}) ≤ k·R. Since p | a_i and p | a_{i+k}, p | (a_{i+k} − a_i), so p ≤ |a_{i+k} − a_i| ≤ k·R. ∎

This is the **growing bound**: shift-k pairs share a prime ≤ k·R, not ≤ R. Sharpening k·R → R for all k is exactly Lemma 4. The gap-bound window does not collapse to the fixed window.

**Why Bezout composition cannot close k·R → R here.** In aimo-0648 the Bezout step works because (a) the underlying relation ("x_n = M") is an *equality* (a single value), so composition is literally transitive, and (b) the available index-shifts are the recurrence lags d_i, a fixed finite set, and Bezout mod T (the period) collapses them. In P6:
- (a) The underlying relation "a_i and a_{i+k} share a small prime" is a *relation between two distinct integers*, not a value-equality. Relations of the form "share a prime" are not transitive in general: 6 and 10 share 2; 10 and 15 share 5; 6 and 15 share 3 (lucky here) — but 6 and 35 share nothing while 6 and 10 share 2 and 10 and 35 share 5. Concretely in our setting, the relation "shares a small prime ≤ R" along consecutive-index edges is not transitive (Sub-step 4a obstruction above). So Bezout composition has nothing to compose: the relation does not lift along compositions of shifts.
- (b) The available shifts, as a fixed finite set with gcd 1, do not exist pre-Lemma-4: the only candidate fixed shift-set is {1} (Lemma 3), and Bezout on {1} trivially gives only shift 1, not shift k for k ≥ 2.

**Concrete shift-1 → shift-2 failure (the wall).** Suppose (a_i, a_{i+1}) shares small prime r ≤ R (Lemma 3) and (a_{i+1}, a_{i+2}) shares small prime s ≤ R (Lemma 3). Cases:
- r = s: then r | a_i and r | a_{i+2}; done, (a_i, a_{i+2}) shares r ≤ R. ✓
- r ≠ s: a_{i+1} carries both r and s, but a_i need not carry s, and a_{i+2} need not carry r. The greedy ensures a_i and a_{i+2} share *some* prime (call it p); by the growing bound (Sub-step above) p ≤ 2R. If p ≤ R we are done; if R < p ≤ 2R, we have no lever to push p down to ≤ R. **This is exactly the wall.** [GAP]

Numerical check (a_1 ∈ {15, 21, 35}, first 25 terms): in every case the shift-2 shared prime is in fact ≤ R (consistent with Lemma 4 being true), but the gap-bound argument only ever gives ≤ 2R. The truth of the fixed-R bound is the crux; the gap-bound window cannot reach it.

### 7. Step 5 — Inherit the periodicity Theorem (conditional)
**Theorem (essential-monovariant §5, certified conditional on Lemma 4).** *Assume Lemma 4. Then a_{n+T} = a_n + L_0 for every n ≥ 1, with T = |V| and L = L_0 = ∏_{p ≤ R} p (no transient).*
Proof in `essential-monovariant.md` §5. Inherited, not reproved. The route's contribution would be an independent proof of Lemma 4 via propagation (Step 4); that contribution is **circular as filed** and does not close.

### Summary of rigour status
- Steps 1, 2, 3 (Lemmas 1, 2, 3): inherited, certified in `essential-monovariant.md`.
- Step 3 extremal-forces-equality sub-lemma: true but vacuous (restates greedy minimality); the extractable partial (a_1 shares a small prime with every a_j) is subsumed by Lemma 1 — **not promotable**.
- Step 4 (Bezout-propagation): **circular as filed [GAP]**. Circularity pinned to Sub-step 4b: the shift algebra φ is defined via V, and V's relevance to the greedy is the free-rider-irrelevance claim, which uses Lemma 4.
- Pre-Lemma-4 shift attempt (Step 6): honest failure. Gap-bound window gives only the growing bound (p ≤ k·R for shift-k pairs); "shares-small-prime" is non-transitive, so Bezout composition has no transitive carrier; the shift-1 → shift-2 wall is the concrete obstruction.
- Step 5 (Theorem): inherited, conditional on Lemma 4.
- **No promotable lemma arises from this round's work on this approach.**

## Promotable lemmas
(none — the only extractable partial is subsumed by Lemma 1, already certified in `essential-monovariant.md`; the propagation route is circular as filed and yields no new reusable lemma.)
