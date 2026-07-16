# Approach: finite-state-window-pullback

## Status
unsolved

## Approaches tried
- (round 1) Opened as a hedge: the only approach in the field that does NOT route through the "sequence = sorted valid set" reduction. Dynamic/finite-state route: effective-window stabilization ⟹ eventual quasi-periodicity ⟹ pull-back to n = 1.

## Current best
Nothing proved beyond the shared elementary facts (pairwise sharing of terms; strict monotonicity). Skeleton only.

## Proof (with explicit gaps)

**Target.** The full claim: ∃ positive integers T, L with a_{n+T} = a_n + L for all n ≥ 1.

**Route (finite-state dynamics; knowledge_base.md entries: "sequences are eventually periodic mod m", pigeonhole, invariants/monovariants; crux analogy aimo-0514: a reversible deterministic process on a finite state space is purely periodic, and aimo-0678: reduce a coupled recurrence modulo the lcm of a bounded coordinate).**

### Skeleton

1. **Bounded increments.** Show ∃ N₀ and a modulus Λ (a product of finitely many primes determined by the first N₀ terms) with a_{n+1} − a_n ≤ Λ for all n: any interval (a_n, a_n + Λ] contains a multiple of Λ, and a multiple of Λ is a valid candidate at every step provided every earlier term shares a prime with Λ — by pigeonhole some finite prime product hits all constraints. **[GAP C1: identify Λ from the dynamics — needs: every term has a prime factor from a fixed finite set. This is the same hard nut the rivals crack; here it must be proven dynamically: show that once a term equal to a multiple of a "locked" pattern appears, all constraints thereafter are hittable inside a fixed finite prime set.]**
2. **Effective window stabilization.** Show ∃ N₁ ≥ N₀ and C such that for all n ≥ N₁, the valid set restricted to the moving window (a_n, a_n + C] is determined by a_n mod Λ alone: constraints from terms with "junk" primes are inert on the window because any number in the window sharing ONLY a junk prime with an old term exceeds the window's cheapest candidate. **[GAP C2: prove new constraints stop affecting the window — the "no new essential constraints" statement, dynamically.]**
3. **Finite-state pigeonhole.** For n ≥ N₁ the next increment a_{n+1} − a_n is a function of the state s_n = a_n mod Λ. The state space is finite; the orbit of s_n is eventually periodic with some period T₀; summing increments over a period gives a_{n+T₀} = a_n + L₀ for all n ≥ N₂, where L₀ ≡ 0 mod ... (verify L₀ is the same each period: the increment function is a fixed function of the state, so the sum over a cycle is constant — proved once Step 2 holds).
4. **Pull-back to n = 1.** From eventual (n ≥ N₂) quasi-periodicity, deduce validity for all n ≥ 1. Mechanism to try: (i) reversibility (aimo-0514 crux): show the state map s ↦ s' is injective on the reachable set, so the orbit is purely periodic — but the EARLY dynamics (n < N₁) are not governed by the state map, so injectivity alone does not reach n = 1; (ii) direct verification: prove gcd(a_n + L₀, a_i) > 1 for ALL i and all n, and minimality of a_n + L₀ at step n + T₀, by strong induction downward from N₂. **[GAP C3: the downward induction needs "every pair of terms shares a prime dividing L₀" — which is essentially the rivals' core lemma again. Without the sorted-V identity this is the weakest point; if it forces importing the rivals' core, this approach collapses into them and should be marked dead.]**
5. Conclude a_{n+T} = a_n + L for all n with T = T₀, L = L₀.

## Open gaps
- GAP C1, C2, C3 — all three open; C3 is likely fatal unless a genuinely dynamic argument (greedy minimality used along the orbit) is found.

## Cases to cover
- none enumerated yet (the route is not case-based).

## Watch out for
- "P* = primes dividing infinitely many terms" is the WRONG finite object: for the all-even sequence every odd prime divides infinitely many terms; P* is infinite. Any state definition must use *essential/locked* primes, not P*. (Explorer structure/analogy reports both stumbled here.)
- Eventual quasi-periodicity alone does NOT imply the problem's claim: the claim is for all n ≥ 1. The pull-back is mandatory, not a formality.
- This approach is the population's hedge against a flaw in the sorted-V reduction; if the reviewer certifies that reduction, this approach's marginal value drops and it should be ranked accordingly.
