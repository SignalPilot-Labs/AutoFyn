## imo-2026-06

Reduction is DONE and reviewer-certified (Lemmas 1-6 in `admissible-set-periodicity.md`,
mirrored in `lemmas/enumeration-and-bounded-gaps.md`, `lemmas/finite-hitting-set-periodicity.md`):
any FINITE hitting set S (a finite prime set meeting every pair of terms in a common prime)
⇒ a_{n+T}=a_n+L for every n≥1, exact from n=1. The ONLY open problem is (HS) finiteness.
Notation: term = element of the sequence; A = admissible set; S₀ = supp(a₁); R = rad(a₁);
"small prime" := prime ≤ a₁, "big prime" := prime > a₁. All terms are ≥ a₁.

---

admissible-set-periodicity: revise
Target: the full theorem — ∃ T,L with a_{n+T}=a_n+L for every n≥1. Keep the certified route
  (static admissible set + periodicity machine, Lemmas 1-6); re-plan ONLY the open (HS) gap by
  grafting on a proof that **S = {primes ≤ a₁} is a finite hitting set**. Once (HS) holds with
  this S, Lemmas 4-6 (certified) finish the whole problem verbatim — do NOT touch them.
Technique: minimal-counterexample / extremal-pair descent + an extremal "compression witness"
  (aimo-0030 Claim 4 + Claim 5), re-proven from scratch in our static admissible-set language.
  Spine theorem to prove: **(SP) Any two terms share a prime ≤ a₁.** (SP) ⇒ S={p≤a₁} hits every
  pair; S is finite since a₁ is a fixed integer ⇒ (HS) ⇒ done.
Skeleton (all new work is Steps A-D; Steps 1-6 are the certified reduction, reused unchanged):
  1. Import certified Lemma 1 (pairwise non-coprimality: any two terms share SOME prime; every
     term ∈ A) and Lemma 2 (greedy characterization a_{n+1}=min(A∩(a_n,∞)); sequence = increasing
     enumeration of A∩[a₁,∞); no element of A strictly between consecutive terms).
  A. **Static "bad-has-a-move" characterization (★)** — the bridge replacing aimo-0030's game
     recursion. Claim: for n ≥ a₁, n is a term ⟺ n shares a common prime with every term < n.
     — Proof of ⟸: assume gcd(n,m)>1 for every term m<n. Let j be maximal with a_j<n. Then
       F_j(n) ["gcd(n,a_i)>1 ∀ i≤j"] holds, so by Lemma 2 a_{j+1}=min{x>a_j:F_j(x)} ≤ n; by
       maximality of j, a_{j+1} ≥ n; hence a_{j+1}=n, a term. ⟹ is immediate from Lemma 1.
     Corollary (G3): if x ≥ a₁ is NOT a term, then some term b* < x has gcd(b*,x)=1
     (contrapositive of ★). This is the ONLY place the greedy rule is used in the finiteness
     argument, and it is exactly the load-bearing greedy-minimality input the counting wall lacked.
  B. **Every term has a small prime factor.** A term b and a₁ are both terms, so by Lemma 1 they
     share a prime p; p | a₁ ⇒ p ≤ a₁ ⇒ p small. (This is the seed fact Step D needs.)
  C. **Compression witness (Claim 4, static).** For any term b, there is an integer x with:
     supp(x) = {small primes dividing b}, no big prime factor, and a₁ ≤ x ≤ b.
     — Construction: if b has no big prime factor take x=b. Else let p be a small prime of b,
       q a big prime of b, α = product of ALL small primes dividing b; let x = p^N·α with N ≥ 0
       least such that x ≥ a₁. Size chain proving x ≤ b: N-minimality ⇒ x < p·a₁; p ≤ α (p|α);
       a₁ < q; so x < p·a₁ ≤ α·a₁ < α·q ≤ b, the last since α·q is a product of DISTINCT primes
       all dividing b, hence divides b. (KB: "Divisor analysis: bounding a finite search by size".)
  D. **(SP) via minimal-counterexample descent (Claim 5, static).** Suppose two terms share no
     small prime. Among all such violating pairs {b,b'} (b' ≥ b) take one with b' MINIMAL
     (well-ordering / KB "extremal principle: take the minimal witness").
       (i) b and a₁ share a small prime p (Step B); p ∤ b' (else p is a common small prime of
           b,b'), and p | b, so b' > b (strict).
       (ii) Apply Step C to b: get x with supp(x) = small primes of b, a₁ ≤ x ≤ b. b' shares no
           small prime with b (violating hypothesis), so gcd(x,b')=1.
       (iii) x is NOT a term: if it were, x and b' would be two terms with gcd=1, contradicting
           Lemma 1. Since x ≥ a₁ and not a term, corollary (G3) gives a term b* < x with
           gcd(b*,x)=1.
       (iv) {b,b*} is a strictly smaller violating pair: both terms (share a prime by Lemma 1);
           any common prime r of b,b* is big — if r were small then r | b ⇒ r | α | x, but
           gcd(b*,x)=1 with r|b* forces r ∤ x, contradiction. And max(b,b*)=b (since b* < x ≤ b)
           < b'. This contradicts minimality of b'. Hence no violating pair exists: (SP) holds.
  E. Conclude: (SP) ⇒ every pair of terms shares a prime in S={primes ≤ a₁}, a finite hitting
     set ⇒ (HS). Feed S into certified Lemmas 4-6 ⇒ a_{n+T}=a_n+L for all n≥1, with
     L=∏_{p∈S}p, T=|A∩[a₁,a₁+L)|. (S is far from minimal — harmless: the machine accepts ANY
     finite hitting set. State this so no one thinks a tight S is needed.)
Key lemmas (claim + mechanism):
  - (★)/(G3): a non-term x≥a₁ has a smaller term coprime to it — because the greedy step
    a_{j+1}=min{x>a_j:F_j(x)} forces any n that meets all earlier terms to already BE the next
    term; contrapositive yields the coprime smaller term. (Replaces the game's "bad→move→good".)
  - Compression witness (Step C) — because among integers with b's exact small-prime footprint,
    the least one ≥ a₁ is < p·a₁ ≤ α·a₁ < α·q ≤ b (distinct-prime-product divides b).
  - (SP) descent (Step D) — because the compressed witness x of the smaller pair-member is a
    non-term coprime to b', whose coprime predecessor b* forms a strictly smaller violating pair.
Open gaps: none intended — this is a complete proof of (HS), hence of the theorem. The builder
  must render Steps A-D fully rigorous; the only places to watch are (★)'s ⟸ direction and the
  size chain in C. Reduction Steps 1-6 are certified; reuse, do not re-prove.
Cases to cover: Step C's two cases (b has / has no big prime factor). Step D(i) strictness
  b' > b. Confirm S={p≤a₁} finite and that the certified machine accepts non-minimal S.
Watch out for:
  - (★) ⟸ uses maximal j with a_j < n; handle n = a₁ (then n is a term trivially).
  - In C, α·q must be a product of DISTINCT primes dividing b (α square-free = radical of the
    small part; q ∉ supp(α) since q big) — this is why α·q | b, giving α·q ≤ b.
  - In D(iv) the common prime r of {b,b*} must be shown big BEFORE claiming the pair violates;
    also that {b,b*} actually shares a prime (Lemma 1, both terms) so it IS a genuine pair.
  - Do NOT reintroduce any counting/density (Σ1/p²) — the whole point is this route avoids it.

---

profile-class-recruitment: new
Target: the full theorem, via a DIFFERENT framing of (HS) — reframe finiteness as termination of
  a greedy recruitment process over a FIXED finite alphabet, kept far from the descent route above
  so the field does not collapse to one framing (anti-collapse rule). Diversity hedge: if a hidden
  flaw surfaces in the descent's (★)-bridge or size chain, this route shares none of those pieces.
Technique: finite S₀-profile alphabet (CRT/pigeonhole partition) + gap-divides-difference size
  bound + a monovariant/well-ordering on unresolved disjoint-profile class-pairs ("cheapest patch"
  greedy minimality). KB: "Modular arithmetic, CRT"; "Pigeonhole/extremal principle";
  "Invariants & monovariants". Corpus support: aimo-0503 (gcd | positive difference bound),
  aimo-0421 (gcd with a fixed element takes only finitely many divisor-values ⇒ finite coloring).
Skeleton:
  1. Import certified Lemmas 1-6 (reduction to (HS)); import Step B above (every term has a small
     prime factor).
  2. **Finite profile alphabet.** Color term n by its profile τ(n)=supp(a_n)∩S₀, a NONEMPTY subset
     of the fixed finite set S₀ (Step B). At most 2^|S₀|−1 profiles, fixed from n=1. Two terms with
     INTERSECTING profiles are hit by S₀ already. So (HS) reduces to: hit every CROSS pair (terms
     whose profiles are disjoint), and there are only ≤ C(2^|S₀|,2) ordered disjoint-profile class
     pairs (π,π') — a FIXED finite index set of "obligations".
  3. **Cheap kill — connector size bound.** If prime p is the sole connector of pair (a_i,a_j),
     i<j, then p | gcd(a_i,a_j) | (a_j−a_i), so p ≤ a_j−a_i ≤ (j−i)·R (certified bounded gap).
     Large sole connectors ⇒ large index separation of their witnessing pair.
  4. **Recruitment monovariant (the gap).** For each disjoint-profile obligation (π,π'), let its
     connector-set be the primes that are the sole connector of some (π-term, π'-term) pair. Claim
     each obligation's connector-set is finite; since there are finitely many obligations, Π is
     finite ⇒ (HS). Mechanism to establish: by greedy minimality, once a small prime r has been
     "recruited" to hit (π,π') (i.e. r divides a π-term and a π'-term that recur infinitely often),
     every later cross-(π,π') pair can be met by r, so no FRESH sole connector for (π,π') is ever
     forced; a fresh large prime would violate minimality of the greedy step (a smaller admissible
     candidate divisible by an already-recruited r exists in the length-≤R window above a_n).
Key lemmas (claim + mechanism):
  - gap | difference — p | a_i, p | a_j ⇒ p | (a_j−a_i); bounded gap R caps the difference by
    (index-gap)·R. (aimo-0503 crux, re-proven.)
  - Finite alphabet — profiles ⊆ fixed S₀, so ≤ 2^|S₀|−1 colors and finitely many obligation
    class-pairs, independent of sequence length.
  - Recruitment termination (OPEN) — each disjoint-profile obligation is permanently discharged by
    the first small prime recruited for it; greedy minimality forbids a later fresh large connector.
Open gaps: Step 4 (recruitment termination) is the hard, unproved nucleus — the "greedy forces a
  smaller already-recruited candidate" lemma is not closed here. Steps 1-3 are rigorous now.
Cases to cover: enumerate obligations = ordered disjoint pairs of occurring profiles; the finitely
  many profiles that occur only finitely often (drop out) vs infinitely often.
Watch out for: an obligation's two profile classes must BOTH occur infinitely often for the
  periodic argument; the recruited prime r need not divide a₁ (numerically r=2 recurs even when
  2∤a₁ — do not assume r ∈ S₀). This is genuinely open; it is the diversity hedge, not the
  expected closer — the descent route above is the expected closer.

---

De-prioritize (do NOT nominate): `essential-prime-counting` — its interval-occupancy Σ1/p²
  attack is the reviewer-confirmed dead counting wall (cannot exclude sparse density-zero disjoint
  families); it has no new mechanism to add. `finite-state-reversible` — its reversibility step
  attacks exactness-from-n=1, which the certified static machine already delivers for free; it does
  NOT attack (HS) finiteness. Both are superseded by the descent route.

Recommended build set: admissible-set-periodicity (primary, expected to close the whole problem),
  profile-class-recruitment (diversity hedge, keeps a second framing live per anti-collapse rule).
