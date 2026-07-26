# Approach: two-coincidence-periodicity (IMO 2026 P6)

Technique: `aimo-0907` (IMO-SL 2020 A6) coincidence-doubling ⇒ eventual periodicity of a deterministic process. Target: the whole theorem (∃ T,L with a_{n+T}=a_n+L eventually), end-to-end, by proving the increment-word d_n = a_{n+1}−a_n is eventually periodic directly and telescoping.

## Status
partial

## Approaches tried
- (Round 5, this build) `aimo-0907` coincidence-doubling route — **partial, with the central premise shown to collapse to Gap A.** The `aimo-0907` coincidence criterion is re-proved from scratch in full (Lemma 1 below; promotable). Building it exposed a mechanism confusion the outline-reviewer flagged and the probe confirms: (i) for a *single* forward-deterministic orbit, ONE self-coincidence already forces eventual periodicity — the "second coincidence" is redundant for the orbit itself; the two-coincidence content of `aimo-0907` is a *between-two-orbits* argument that does not transfer to the single greedy orbit. (ii) The route's true load-bearing requirement is "exhibit a finite **forward-deterministic determining** statistic α" (forward-deterministic so a pigeonhole self-coincidence propagates; determining so α-periodicity lifts to d-periodicity). That requirement is *exactly* Gap A (finiteness of the determining state = finiteness of governing primes = L-periodicity of B_∞); the route does NOT go around Gap A as the outliner claimed — Step 3's pigeonhole IS a finiteness assumption. (iii) The new T-unbounded-in-M_1 impossibility (rad-77 witness a_1=77→T=18 vs a_1=847→T=1744 at the same M_1=77) fences the *entire class* of f(M_1)-bounded forward-deterministic determining statistics: such an α would give d-periodicity with T ≤ |alphabet| ≤ f(M_1), contradicting T unbounded in M_1. (iv) A computational probe on a_1 ∈ {15,35,77,91,175} confirms every natural candidate abstraction (witness-prime-tuple, d_n itself, a_n mod M_1) is NOT forward-deterministic (all have successor-conflicts) and does NOT determine d_{n+1}; the witness-prime word has only 2–3 realized states but a sub-period that is a *proper divisor* of T (the structural sub-period leak), so its self-coincidences do not propagate to d-periodicity. Verdict: the route is honest-partial; it supplies one certified reusable tool (the `aimo-0907` criterion) and a clean diagnosis that the "two-coincidence" framing cannot bypass Gap A.

## Current best

**Certified reusable tool (Lemma 1, promotable):** the `aimo-0907` coincidence criterion, proved from scratch below in two parts — (A) one self-coincidence of a single-valued map ⇒ eventual periodicity of that orbit; (B) two between-orbit coincidences at distinct iterate-offsets ⇒ finiteness (hence eventual periodicity) of the orbits.

**Diagnosis (rigorous):** the two-coincidence route's true antecedent — "∃ a finite forward-deterministic determining statistic α for the greedy orbit" — is *equivalent* to Gap A and is fenced by the T-unbounded-in-M_1 impossibility whenever α is f(M_1)-bounded. The "second coincidence" is redundant for a single orbit (one suffices once α is forward-deterministic); the genuine `aimo-0907` two-coincidence mechanism is between-orbits and does not port to one greedy orbit. The probe confirms the named abstractions are not forward-deterministic.

**Open gap (the wall):** exhibit a finite forward-deterministic determining statistic α for the greedy orbit *that is not f(M_1)-bounded* (so the impossibility does not bite) yet still has a finite alphabet (so pigeonhole gives a self-coincidence). No such α is identified; the natural candidates all leak (probe, below). This is Gap A in coincidence-doubling costume. Without it, the `aimo-0907` criterion's antecedent cannot be met.

## Full proof
Not complete. The conditional argument is rigorous up to the open antecedent; it is recorded in full below so the gap is explicit and the reusable lemma is isolated.

---

### Setup and notation

Let a_1,a_2,… be the greedy sequence of the problem, d_n := a_{n+1}−a_n the increment word. Let P_1 be the set of prime divisors of a_1 and M_1 := rad(a_1) = ∏_{p∈P_1} p. We import the certified lemma `linchpin-and-gap-bound` (round 1): every a_n is divisible by some p∈P_1, and **d_n ∈ {1,…,M_1} for all n** — so the increment word is a well-defined infinite word over the *finite* alphabet {1,…,M_1}. We also import `cyclic-successor-bijection` + `greedy-equals-cyclic-successor` (round 1) as the certified endgame: *if* B_∞ = ⋂_n B_n is L-periodic, then a_{n+T}=a_n+L for all n≥1 with T=|A|, L the period.

### Step 1 — The `aimo-0907` coincidence criterion (re-proved from scratch)

We restate and prove the load-bearing move of `aimo-0907` (IMO-SL 2020 A6, Case 2) in the general form we need. The proof uses only forward-determinism (single-valuedness) of an iterate map; no finiteness assumption is made.

**Lemma 1 (aimo-0907 coincidence criterion).** Let X be a set and f:X→X an arbitrary map. For x∈X write the (forward) orbit as the sequence O(x) = (x, f(x), f²(x), …), and write f^k for the k-th iterate (f⁰=id).

**(A) One-coincidence ⇒ eventual periodicity.** If for some x∈X and integers 0≤a<b one has f^a(x)=f^b(x), then O(x) is eventually periodic with period δ:=b−a>0: namely f^{a+k}(x)=f^{b+k}(x) for every k≥0.

*Proof of (A).* From f^a(x)=f^b(x)=f^{a+δ}(x), apply f^k to both sides (f is a single-valued function, so equal inputs give equal outputs): f^{a+k}(x)=f^{a+δ+k}(x)=f^{b+k}(x) for all k≥0. This is exactly eventual periodicity of the sequence (f^n(x))_{n≥0} from index a onward, with period δ. ∎_(A)

**(B) Two between-orbit coincidences at distinct offsets ⇒ finiteness.** Suppose O(x) and O(y) are each infinite (no self-coincidence, i.e. f^r(x)=f^s(x) ⇒ r=s, and likewise for y). Suppose further there exist two pairs of nonnegative integers (n,m) and (p,q) with f^n(x)=f^m(y) and f^p(x)=f^q(y), and that the iterate-offsets n−m and p−q are *distinct*. Then O(y) is eventually periodic (hence O(y) is finite as a *set*), contradicting the hypothesis that O(y) is infinite.

*Proof of (B).* WLOG n−m > p−q (otherwise swap the two pairs). Set Δ := (n−m)−(p−q) > 0. Compute f^{p+m}(y) in two ways using the two coincidences and the single-valuedness of f:

- From f^n(x)=f^m(y): apply f^p. Then f^{p+n}(x)=f^{p+m}(y).
- From f^p(x)=f^q(y): apply f^n. Then f^{n+p}(x)=f^{n+q}(y).

The left-hand sides are equal (both f^{n+p}(x)). Hence f^{p+m}(y)=f^{n+q}(y). But n+q − (p+m) = (n−m)−(p−q) = Δ > 0, so f^{p+m}(y)=f^{p+m+Δ}(y). By part (A), O(y) is eventually periodic with period Δ. An eventually periodic orbit visits only finitely many points, so O(y) is finite as a set — contradicting the hypothesis that O(y) is infinite (a self-coincidence-free orbit visits a new point at every step and is infinite as a set). ∎_(B)

This is exactly the argument of `aimo-0907` Case 2 (the source writes it for f:ℤ→ℤ with orbits of integers; the proof uses only single-valuedness of f, so it ports verbatim to any map on any set). ∎

**Remark (mechanism clarification, per the outline-reviewer's flag).** Part (A) shows that for a *single* forward-deterministic orbit, **one** self-coincidence already yields eventual periodicity. The "second coincidence" earns its keep only in part (B), which is a *between-two-orbits* argument (it produces the iterate-offset function X(a,b)=n−m and pins it from one seed coincidence). Our greedy problem has a **single** orbit (the sequence a_n), so the between-orbits mechanism (B) does not directly apply. Consequently the "two-coincidence" framing of the outline is mis-stated for our setting: what we actually need is one self-coincidence of a forward-deterministic statistic, and the genuine load-bearing requirement is the **forward-determinism + determining** of that statistic, not a second coincidence.

### Step 2 — Define the orbit-abstraction α concretely

The outline named two candidate abstractions, both functions of the greedy orbit with alphabet bounded in terms of P_1 (hence f(M_1)-bounded):

- **(a) Skeleton abstraction:** α_n = {p∈P_1 : p | d_n} (the set of small primes dividing the increment). Alphabet ⊆ 2^{P_1}, size ≤ 2^{|P_1|} ≤ 2^{ω(M_1)}.
- **(b) Witness-prime abstraction:** α_n = the small prime p∈P_1 carrying gcd(a_{n+1},a_n) (or the tuple of such). Alphabet ⊆ P_1 ∪ {⊥}, size ≤ |P_1|+1.

(The residue abstraction α_n = a_n mod M_1 is the round-3 fenced modular-residue statistic — minimal functional modulus = L — and is included only as a baseline; it is not a candidate.)

### Step 3 — The first self-coincidence (pigeonhole)

**Lemma 2 (first coincidence, finite alphabet).** For either candidate abstraction α in Step 2, since its alphabet is finite (size ≤ 2^{|P_1|+1}), pigeonhole gives indices a<b with b−a ≤ (alphabet size) and α_a=α_b.

*Proof.* Among the first (alphabet-size + 1) values of α_n, two coincide by the pigeonhole principle. ∎

This is the "first coincidence." It is non-circular (it does not use the cofactor AP k_{i+s}=k_i+L/q, which `schur-cofactor-premise-fails-in-periodic-regime` certifies is circular as a proof of periodicity). It is, however, *only a coincidence of the abstraction symbol*, not yet of any determining state — see Step 4.

### Step 4 — The lift: the load-bearing GAP (honest)

To apply Lemma 1(A) and conclude α-periodicity from the coincidence of Step 3, we need α to be the orbit of a **single-valued map** f, i.e. α_{n+1}=f(α_n) for some f (forward-deterministic). To then lift α-periodicity to d-periodicity, we need α to be **determining**: α_n → d_{n+1} single-valued (so that α_{n+T}=α_n forces d_{n+T}=d_n).

This is the genuine fork the outline-reviewer identified, and the route's survival turns entirely on it. We settle each branch:

**Branch (i): α is forward-deterministic AND determining.** Then by Lemma 1(A) + Step 3, α is eventually periodic with period ≤ (alphabet size) ≤ f(M_1); by determining, d is eventually periodic with the same period T ≤ f(M_1). **This branch is FENCED** by the round-5 T-unbounded-in-M_1 impossibility: T is not bounded by any function of M_1 (rad-77 witness: a_1=77 → T=18 vs a_1=847 → T=1744 at the same M_1=77; the exponent-1→exponent-2 jump is 97×). An f(M_1)-bounded determining forward-deterministic α would force T ≤ f(M_1), contradiction. So no f(M_1)-bounded α can occupy branch (i).

**Branch (ii): α is forward-deterministic but NOT determining.** Then Lemma 1(A) gives α-periodicity (one coincidence suffices — the "second coincidence" is redundant), but α-periodicity does **not** lift to d-periodicity. The `aimo-0907` two-coincidence mechanism (Lemma 1(B)) is a between-orbits tool and supplies no lift for a single orbit. **This branch gives nothing for d_n.**

**Branch (iii): α is NOT forward-deterministic.** Then a coincidence α_a=α_b does not propagate (f is not single-valued on α), and no periodicity follows at all — the `syndetic-divisible-closed-not-periodic` guardrail (round 3) certifies that "finite alphabet + bounded gaps ⇒ periodic" is false without single-valuedness.

**Computational probe — which branch do the named abstractions occupy?** (Naive correct gcd-greedy, periods verified against the known a_1=15→(T=8,L=30), a_1=35→(T=34,L=210); d_n ≤ M_1 re-confirmed in every case per `linchpin-and-gap-bound`.)

| a_1 | P_1 | M_1 | T(d) | T(α_a) | α_a realized | α_a fwd-det conflicts | α_a determines-d conflicts |
|-----|-----|-----|------|--------|--------------|----------------------|---------------------------|
| 15  | {3,5}  | 15  | 8   | 4  | 2 | 2 | 2 |
| 35  | {5,7}  | 35  | 34  | 34 | 2 | 2 | 2 |
| 77  | {7,11} | 77  | 18  | 18 | 2 | 2 | 2 |
| 91  | {7,13} | 91  | 20  | 10 | 2 | 2 | 2 |
| 175 | {5,7}  | 35  | 274 | 274| 3 | 3 | 3 |

(α_a = witness-prime-tuple = the set {p∈P_1 : p|d_n}; "fwd-det conflicts" = number of α-values with ≥2 distinct successors — *every* realized α-value has a conflict in every row; "determines-d conflicts" = number of α-values mapping to ≥2 distinct d_{n+1}. The d_n-itself abstraction is also not forward-deterministic — 4/6/8/8/12 conflicts respectively, every realized value with a conflict. The a_n mod M_1 baseline has 1/6/1/1/8 conflicts.)

**Read-out of the probe.** *Every* named candidate abstraction occupies **branch (iii)** (not forward-deterministic): the witness-prime word has only 2–3 realized symbols but each symbol is followed by ≥2 distinct successors in every tested case. Moreover the witness-prime word's period is a **proper divisor** of T(d) when it is a proper divisor (a_1=15: 4|8; a_1=91: 10|20) — the structural sub-period leak already certified in the round-5 minimal-counterexample explorer — so its self-coincidences do not pin position within T and cannot lift to d-periodicity. The d_n word itself is not forward-deterministic (each value is followed by multiple successors). The a_n mod M_1 abstraction is the round-3 fenced residue statistic.

So **no named abstraction is forward-deterministic**, and the antecedent of Lemma 1(A) cannot be met by any of them. The "second coincidence" (Step 4/GAP A3 of the outline) is moot: there is no first propagating coincidence to double.

### Step 5 — Apply the criterion ⇒ increment-word periodicity

This step is conditional on Step 4 supplying a finite forward-deterministic determining α. **It does not.** For completeness, the conditional close is: were such an α exhibited, Step 3 (pigeonhole) gives α_a=α_b; Lemma 1(A) gives α eventually (b−a)-periodic; determining gives d eventually (b−a)-periodic; telescoping then gives a_{n+(b−a)}=a_n + L₀ with L₀ = ∑ of one period of d. (Equivalently, once d is eventually periodic, the certified `cyclic-successor-bijection` + `greedy-equals-cyclic-successor` endgame yields a_{n+T}=a_n+L for all n≥1.) Both finishes are rigorous *given* the antecedent; the antecedent is the wall.

### Step 6 — Diagnosis: the route is Gap A in coincidence-doubling costume

Collecting Steps 4–5: the route's true load-bearing requirement is

> (∗) Exhibit a finite forward-deterministic **determining** statistic α for the greedy orbit.

This is *exactly* Gap A. Indeed: a forward-deterministic determining α is a finite state on which the greedy next-increment is a single-valued function; finiteness of the state is the finiteness of the determining information, which (by the round-1 endgame `cyclic-successor-bijection`) is equivalent to L-periodicity of B_∞ = finiteness of the governing-prime set — the single open wall. The route does not go *around* Gap A; it presupposes it.

Moreover (∗) is fenced whenever α is f(M_1)-bounded (the T-unbounded impossibility, Branch (i)). To escape, α would have to be finite-alphabet (for pigeonhole) yet *not* f(M_1)-bounded (for the impossibility not to bite) — i.e. a finite determining state whose size depends on a_1's full prime-power structure (not just rad(a_1)). No such state is currently identified, and the probe shows the natural candidates (witness-prime, d-skeleton, residue) all fail forward-determinism. The honest conclusion: the `aimo-0907` coincidence-doubling mechanism, however sound in itself, does not supply the missing antecedent; it is a *criterion for periodicity given a forward-deterministic map*, not a construction of one.

### Honest summary of what is proved and what is not

- **Proved (and promotable):** Lemma 1 — the `aimo-0907` coincidence criterion, in two parts (one-coincidence ⇒ eventual periodicity for a single-valued map; two between-orbit coincidences at distinct offsets ⇒ finiteness). Fully re-proved from scratch, no finiteness assumption.
- **Proved (diagnostic):** the route's antecedent (∗) is equivalent to Gap A; the f(M_1)-bounded sub-case is fenced by the T-unbounded-in-M_1 impossibility; the named abstractions are not forward-deterministic (probe, 5 cases).
- **Not proved (the wall):** no finite forward-deterministic determining statistic α is exhibited. The "second coincidence" (GAP A3) is shown to be *redundant* for a single orbit (one suffices), not load-bearing as the outline claimed; the genuine load is the forward-determinism + determining of α, which is Gap A.

The proof is therefore incomplete at Step 4/5. Status: **partial**, with the open gap recorded explicitly as (∗) above.

---

## Lemma proposal

**Lemma (aimo-0907 coincidence criterion).** Let f:X→X be any single-valued map. (A) If f^a(x)=f^b(x) for some 0≤a<b, then the orbit (f^n(x)) is eventually periodic with period b−a. (B) If two orbits O(x),O(y) are each self-coincidence-free (infinite as sets) but admit two cross-coincidences f^n(x)=f^m(y), f^p(x)=f^q(y) with n−m≠p−q, then O(y) is eventually periodic (contradiction). Proof: part (A) by applying f^k to the equality; part (B) by composing the two cross-coincidences to get f^{p+m}(y)=f^{p+m+Δ}(y) with Δ=(n−m)−(p−q)>0, then invoking (A). — Proved in full in this approach file (Step 1). Reusable by any approach that needs a deterministic-process periodicity criterion; the antecedent (a forward-deterministic map) is the consumer's responsibility.
