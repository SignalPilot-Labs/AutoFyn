# Approach: finite-state-reversible

## Status
unsolved (outline only)

## Target (the exact problem claim)
For the greedy pairwise-gcd sequence (a_n), prove ∃ T,L with a_{n+T}=a_n+L for **every** n≥1.

## Technique / spine
Dynamical / process view (contrast with admissible-set-periodicity's static view). Model the sequence as the orbit of a deterministic map on a FINITE state space; pigeonhole ⟹ eventual periodicity of the gap sequence; then prove the state map is a **bijection** (the process is reversible), which upgrades eventual periodicity to **exact** periodicity from n=1 with no pre-period (adapts crux aimo-0514: a bijective self-map of a finite set has every orbit purely periodic). This route's exactness mechanism (reversibility) is genuinely different from admissible-set-periodicity's (static periodic set), so the two do not fail at the same exactness wall.

## Notation
R = rad(a_1); S ⊇ supp(a_1) a finite prime set (its finiteness is a gap); L = ∏S.

## Skeleton
1. **Bounded gaps.** a_{n+1}-a_n ≤ R, since every multiple of R>a_n is admissible (it is divisible by all of supp(a_1) and every earlier term shares a prime with a_1). [Same cheap kill as the other approaches.]
2. **[GAP A] Finite live-constraint window.** Show that to decide admissibility of a candidate x∈(a_n,a_n+R], one need only check gcd(x,a_i)>1 for i in a bounded window i∈[n-W,n] (older constraints auto-satisfied), where W is bounded. Mechanism candidate: an old term a_i is "covered forever" once a later term a_j (i<j≤n) has supp(a_j) ⊇ (the S-primes needed), so any x divisible by an S-prime of a_j is also compatible with a_i via a shared S-prime; use that terms repeat their S-residue pattern with bounded gap. Requires the finite-S fact.
3. **[GAP B] Finite state.** Define the state at step n as σ_n = ( a_n mod L, and the finite window data from Step 2: the S∩supp pattern of a_{n-W..n} together with a_n mod L ). Show σ_{n+1} = Φ(σ_n) is a deterministic function (the greedy pick of the smallest admissible residue > a_n mod L compatible with the windowed constraints), and σ_n lives in a finite set (bounded by L·2^{W|S|}). Requires finite S (GAP D) and finite W (GAP A).
4. **Eventual periodicity.** Φ is a self-map of a finite set ⟹ the orbit (σ_n) is eventually periodic (pigeonhole). Since a_{n+1}-a_n is a function of σ_n (the gap to the next admissible residue), the gap sequence is eventually periodic: ∃ T,L,n_0 with a_{n+T}=a_n+L for n≥n_0.
5. **[GAP C] Reversibility ⟹ exact from n=1.** Show Φ is INJECTIVE on the (recurrent part of the) finite state space, hence a bijection on its image cycles, so every state on a cycle has no pre-image outside the cycle — forcing the orbit to be purely periodic from n=1 (no pre-period), i.e. a_{n+T}=a_n+L for ALL n≥1. Mechanism (aimo-0514): the greedy step is reversible — given σ_{n+1} (residue + window), the previous term's residue is recovered as the largest admissible residue below a_{n+1} compatible with the window shifted back one; injectivity of this back-map = bijectivity of Φ. Alternatively (fallback), argue the orbit is already on the recurrent set from n=1 because σ_1 is reconstructible as a Φ-image (the sequence extends uniquely backward within the periodic pattern).

## Key lemmas (claim + mechanism)
- **L1 (bounded gaps).** As in admissible-set-periodicity: multiples of R are admissible.
- **L2 (finite S).** Only finitely many primes are ever load-bearing. SHARED crux with the counting approach; here attack it via GAP A's "old constraints die" — if instead one proves each old term is eventually covered by a recurring S-prime pattern, the set of primes that are ever the *sole* connector is finite. (This is the same wall as L3 of admissible-set-periodicity; the two approaches diversify on EXACTNESS, not on this finiteness fact — flag for the reviewer.)
- **L3 (reversibility).** The state map Φ is a bijection on its recurrent set, because the greedy rule run backward (largest admissible residue below the current, given the window) uniquely determines the predecessor state. A bijective finite-state map has purely periodic orbits (aimo-0514) ⟹ exactness from n=1.

## Open gaps (builder fills)
- **GAP D / L2** — finite essential prime set S (shared hard crux).
- **GAP A** — bounded live-constraint window W (old constraints auto-satisfied).
- **GAP B** — assemble the finite state and verify Φ is a well-defined function of it.
- **GAP C / L3** — reversibility / injectivity of Φ to get EXACT (not just eventual) periodicity. This is the distinctive contribution of this approach.

## Cases to cover
None by casework.

## Watch out for
- The naive state "a_n mod L" alone is INSUFFICIENT — admissibility depends on the window of recent terms' prime patterns, not just the last residue (GAP B). Must include the window.
- Do NOT stop at Step 4 (eventual periodicity): that does not prove the claim (pre-period would falsify a_{n+T}=a_n+L ∀n). Step 5 (reversibility) is mandatory and is this approach's whole point.
- Reversibility is subtle because the constraint set GROWS forward in time; the back-map must operate on the *stabilized* window, valid only after GAP A/D pin down finite S and W. Order the lemmas so reversibility is argued on the recurrent finite state, not on the raw growing history.
