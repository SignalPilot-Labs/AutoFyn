# Approach: reversible-state-bijection

## Status
unsolved (skeleton; crux gap open)

## Framing (deliberately far from the other two)
Do NOT prove eventual periodicity by pigeonhole and then patch the transient.
Instead prove **pure periodicity in one stroke** by dynamical reversibility, in the
spirit of aimo-0577 (Croatia/ISL): confine the process to an explicit finite state
space and show the one-step map is a **bijection** with an explicit inverse. A
bijection of a finite set has *no* pre-periodic tail — every orbit is a cycle — so
`a_{n+T} = a_n + L` holds for every `n ≥ 1` automatically, dissolving the
"eventual vs. for-all-n" gap that the other framings must patch separately. Large
primes are confronted through a rigidity fact, not avoided: a prime dividing two
terms one period apart must divide `L`, so it is small; large primes can therefore
never belong to the periodic *core* and enter only as bounded, invertible "decorations."

## Target
There exist positive integers `T, L` with `a_{n+T} = a_n + L` for every `n ≥ 1`.

## Technique
Reversibility / bijection on a finite state space (KB: Modular arithmetic/CRT;
Pigeonhole/extremal — bijection variant). Borrowed crux: aimo-0577's
"bound the orbit into a finite set, exhibit an explicit inverse ⇒ periodicity."

## Free lemmas (correct, shared)
- **Anchor**, **Gap bound** (`gap ≤ M`, `a_n = Θ(n)`), **Distance–prime**.
- **L-rigidity (the large-prime handle).** IF `a_{n+T}=a_n+L` for all `n`, then for
  a prime `q` and phase `j`: `q|a_j` and `q∤L ⇒ q` divides `a_{j+kT}=a_j+kL` for
  exactly one residue class of `k mod q` — so `q` divides infinitely many terms but
  only 1-in-`q` of each phase. Hence "divides ∞ many terms" is useless; the finite
  invariant is `S := primes(L)`. Verified: `a_1=105`, `q=11∤210` divides terms at
  all 58 phases. This tells us the state must be `residue mod L`, and every prime of
  the *core* divides `L`.

## Skeleton
1. Free lemmas + L-rigidity.
2. **State space.** Define the state `Σ_n := (a_n mod L)` where `L := ∏_{p∈S} p`
   and `S` is the (to-be-shown finite) set of core primes with `S ⊆ {p ≤ M}`.
   `Σ` ranges over the finite set `Z/LZ`. (Existence/finiteness of `S,L` is Crux A.)
3. **Forward map is well-defined on the core.** For `n` past a bounded start, the
   greedy successor of `a_n` is determined by `Σ_n` together with a *bounded,
   invertible* record of the recently-introduced large primes (each large prime,
   by distance–prime, pairs with a term within a bounded number of steps and is
   discharged there). Package this bounded record into a finite augmented state
   `Σ̂_n`; the forward map `F : Σ̂_n ↦ Σ̂_{n+1}` acts on a finite set.
4. **Crux B (backward-determinism / injectivity).** `F` is injective: from `Σ̂_{n+1}`
   one can recover `Σ̂_n`. Mechanism: `a_n` is the *largest* value below `a_{n+1}`
   for which `a_{n+1}` is the greedy successor; the admissibility structure encoded
   in `Σ̂` determines this predecessor uniquely, and the bounded large-prime record
   is popped in reverse (distance–prime bounds how far back a large prime's partner
   lies, so backward recovery is finite). This is the aimo-0577 inverse, adapted.
5. **Bijection ⇒ pure periodicity.** An injective self-map of a finite set is a
   bijection; every orbit is a cycle of some length `T`. Thus `Σ̂_{n+T} = Σ̂_n` for
   ALL `n` in the orbit (no tail), so `a_{n+T} ≡ a_n (mod L)`. One cycle advances the
   value by a constant multiple of `L` (bounded gaps ⇒ finitely many wraps per
   cycle); set `L` := that increment. Hence `a_{n+T} = a_n + L` for every `n ≥ 1`.

## Key lemmas (claim + mechanism)
- **L-rigidity** — `q∤L ⇒ q` divides only a 1/q-fraction of each phase; the finite
  invariant is `primes(L)`, not "recurrent primes."
- **Crux A (finite core `S ⊆ {p≤M}`, `L=∏S` exists)** — core primes recur within
  bounded distance, so distance–prime bounds them by `M`; finitely many.
- **Crux B (injectivity / explicit inverse)** — greedy successor is invertible:
  the predecessor is the unique largest value having `a_{n+1}` as its successor, and
  the bounded large-prime record is reversible because each large prime's partner is
  within a bounded backward window (distance–prime).

## Open gaps
- **GAP-A (crux):** existence and finiteness of the core `S`/modulus `L` with
  `S ⊆ {p ≤ M}`. Shared in spirit with the other approaches' confinement lemma but
  here it defines the state space.
- **GAP-B (crux, the heart):** backward-determinism — `F` injective on the finite
  augmented state, including reversibility of the bounded large-prime record. This
  is the genuinely novel content that makes the bijection mechanism work and is
  where the aimo-0577 transplant must be earned (the successor here is a *global*
  smallest-search, not a 2-branch recurrence).

## Cases to cover
- `L` prime (single-prime lock): `F` trivially bijective, `T=1`.
- Multi-prime `L`: the general bijection.
- Steps where a large prime is active (385-type): must show it is a reversible
  decoration, popped within a bounded window — NOT part of the core cycle.

## Watch out for
- The augmented state `Σ̂` must be genuinely finite; if the large-prime record is
  unbounded, injectivity is vacuous. The bound comes from distance–prime + bounded
  gaps, and must be proven, not assumed (this is exactly the reviewer's refutation
  point — do not smuggle in "bounded memory").
- Injectivity gives periodicity from `n=1` FOR FREE — this is the payoff over the
  pigeonhole approaches, which need a separate no-transient step.

## Approaches tried (refuted premises — do not retry)
- **REFUTED (round 1): finite "recurrent prime set" (primes dividing ∞ many terms).**
  FALSE — verified `a_1=105`: prime `11 ∤ L=210` still divides terms at all 58
  phases, so it divides infinitely many terms. The correct finite object is
  `primes(L)`, targeted here via L-rigidity — NOT "recurrent primes."
- **REFUTED: bounded-memory window of fixed size.** The window is unbounded
  (reviewer: reaches 320+). This approach bounds only the large-prime *record via
  distance–prime*, and must prove that bound; it does not assume a fixed window.
