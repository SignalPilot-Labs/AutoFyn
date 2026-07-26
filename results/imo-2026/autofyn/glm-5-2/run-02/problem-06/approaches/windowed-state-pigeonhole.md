# Approach: windowed-state-pigeonhole

## Status
unsolved

## Framing
Avoid naming or computing L. Instead prove the greedy transition depends only on a FINITE STATE — a TUPLE of recent residues mod a modest modulus M (built from a_1 plus a few forced primes) — because the "next valid m" lives in a BOUNDED WINDOW above a_n (gcd(k,k+1)=1 structure bounds the window). Pigeonhole on the finite state space gives recurrence of a state, hence a_{n+T}≡a_n (mod M); lift to exact translation.

## Target
Prove ∃ T,L>0 with a_{n+T}=a_n+L for all n.

## Technique
Pigeonhole/extremal on a finite-state tuple + gcd-structure window bound (knowledge_base "Pigeonhole/extremal", "Divisor analysis / gcd of consecutive integers").

## Skeleton
1. **Modulus choice.** Let M = rad(a_1)·(product of primes forced early, e.g. 2 once 2 appears). A finite, modest modulus. — mechanism: M captures all primes that could divide a_1 and the parity anchor.
2. **Window bound (the crux).** Prove: a_{n+1} − a_n ≤ W for some absolute W depending only on M (or on a_1). Mechanism: among any W consecutive integers, one is divisible by some prime in P(a_1) AND by some prime in P(a_{n-1}) (so it hits both a_1 and a_{n-1}); need it hits ALL of a_1,…,a_n. Refine: among W consecutive integers above a_n, one has gcd>1 with each a_i simultaneously — by CRT pigeonhole (for each a_i, the "bad" set is the units mod rad(a_i); the intersection of complements is nonempty in a window of size ≈ ∏ rad(a_i) — too large). The window bound is the hard sub-step.
3. **Finite state.** Define state s_n = (a_n mod M, a_{n−1} mod M, …, a_{n−k+1} mod M) for window length k. Choose k so that the greedy transition s_n → s_{n+1} is a DETERMINISTIC function of s_n alone. — mechanism: the next valid m lives in the window [a_n+1, a_n+W]; whether m hits each a_i (i≤n−k) is ALREADY determined by the recent residues (because a_i for i≤n−k are "far" and their relevant prime structure is captured by the tail... [THIS IS THE SUBTLE STEP — see gap]).
4. **Pigeonhole recurrence.** State space has size ≤ M^k (finite). The deterministic transition ⇒ orbit eventually periodic: s_{n+T} = s_n for n ≥ N. — pigeonhole.
5. **Lift to translation.** s_{n+T}=s_n ⟹ a_{n+T} ≡ a_n (mod M). Need EXACT: a_{n+T} = a_n + L. Argue: once the state recurs, the SAME window computation produces identical increments, so a_{n+T} − a_n is constant (= L) for n in the periodic regime. — by determinism of the transition + induction on the periodic cycle.
6. **"For all n" / transient.** Same load-bearing ambiguity; absorb transient if needed.

## Key lemmas (claim + one-line mechanism)
- **Lemma A (window bound) — the crux:** a_{n+1} − a_n ≤ W(a_1) for all n — mechanism: in any run of W consecutive integers, one is non-coprime to each of finitely many fixed moduli simultaneously (CRT + Chinese-Remainder-density). The tight bound is hard; a crude W = ∏ rad(a_i) over a finite family suffices for finiteness but may be huge.
- **Lemma B (transition is a function of the state):** given s_n (recent residues mod M), a_{n+1} mod M is determined — mechanism: the greedy scans the window [a_n+1, a_n+W]; admissibility of m against a_i for i ≤ n−k is captured by a_i mod M (because all that matters is shared primes, and shared primes are bounded by M's factor set). The "far" terms' prime structure must be shown captured by the recent residues.
- **Lemma C (state recurrence ⟹ exact translation):** once s recurs, the integer increments repeat exactly (not just mod M) — mechanism: the window bound makes the increment an exact integer determined by the state.

## Open gaps
- Step 2 / Lemma A: the window bound is genuinely hard. The naive CRT gives W enormous (product of rad(a_i), growing). Need a SHARP bound independent of n. This may be the approach's fatal wall — the window might grow with n. NUMERICS: for a_1=15 the gaps are bounded (period 8, gaps ∈ {2,3,4,5,6}); but is this universal? The gap a_{n+1}−a_n within a period is bounded by L, but L might be huge for hard starts (a_1=1001). If the window grows with L (which is what we're trying to prove exists), this is circular. FLAG.
- Step 3 / Lemma B: showing the "far" terms are captured by recent residues is subtle — it's essentially the same stabilization claim as the other approaches, restated. This approach may not escape the crux.
- Step 5: the lift from mod-M recurrence to exact translation needs the window bound to be state-determined, not just bounded.

## Cases to cover
- Even a_1, prime-power a_1: window trivially W=2 resp. W=p, state single residue, T=1. Handled.

## watch out for / Watch out for
- The window bound (Lemma A) is the likely fatal gap: it may be circular (window bound needs L, which is what we're proving). The approach is a BET: that a window bound INDEPENDENT of L can be proved via gcd-structure of consecutive integers (gcd(k,k+1)=1) and the fixed prime set P(a_1). If this bet fails, the approach collapses — but it is a genuinely different framing worth fielding.
- Do NOT conflate with crude-reduced-type: that approach stabilizes the full valid set V_0 (one-step residue map); THIS approach uses a TUPLE state and a window bound, never stabilizing V. The distinction is the state-tuple + window, not the modulus.
- The "far terms captured by recent residues" step is the hidden stabilization — be honest that this may reduce to the same crux.
