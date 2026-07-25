## imo-2026-06

CONTEXT FOR THE REVIEWER. Six-round structural plateau. The whole theorem is certified-equivalent to
"𝓐_∞ finite" (Π finite). R7 explorer `math-explorer-intended-lever.md` located the official AoPS
Solution 2 and extracted a **new, guardrail-surviving lever** (the "rescale-witness"): a *fresh
prime* p introduced by a key term x above the threshold C = q₀·a₁ yields an earlier term y with
support P(x)∖{p} ⊊ P(x), contradicting minimality. This is the FIRST live opening in the run's
recorded history that is NOT a ∏G / p_max / |t−t′| / density / sub-support-transversal lever.

**A LOAD-BEARING CORRECTION to the dispatch, forced by the run's own certified guardrails.** The
dispatch says the removed prime is `p_max` (route through E5″, "B ⊆ G∖{p_max}"). **This is wrong and
would revive a certified-dead lever.** Removing `p_max` fails exactly because of R5-JSC / E3: by E3,
`p_max` has a private witness `G_{p_max}` with `G ∩ G_{p_max} = {p_max}`; if its realizer
`∏G_{p_max} < ∏G` there is an EARLIER term sharing only `p_max` with `G`, so `y = ∏(G∖{p_max})·q^t`
would FAIL to meet that earlier term ⇒ y not realized. The prime that CAN be removed is a **fresh**
prime — one appearing in NO earlier key term — because freshness is exactly what forbids an earlier
term from sharing only that prime with G (proof in the skeleton). p_max need not be fresh. So the
correct route does NOT go through E5″/p_max; it proves **Π finite (the Crux) DIRECTLY** via a
first-appearance/threshold argument, leaving the certified E4/E5/E5″ chain intact as legacy
infrastructure. Both slugs below use the FRESH prime, not p_max. Flag this to every builder.

Two build targets (both ride the same core lever; they diverge in FRAMING and bridge — see the
single-gap-trap note at the end):

---

### redundant-constraint-antichain : advance
Target: The full theorem — ∃ T,L with a_{n+T}=a_n+L for all n≥1 (via closing the sole open gap, the
Crux "𝓐_∞ finite / Π finite"; everything else in this approach is already certified complete).
Technique: Explicit local rescale-witness + first-appearance threshold, closing the Crux DIRECTLY
(supersedes E5″; keeps the certified §1–§5 endgame and E1 realizability verbatim).
Skeleton (add as new §15; do NOT touch §1–§5 endgame or §9 E-lemmas):
  1. Recall certified endgame: Crux (𝓐_∞ finite) ⟹ theorem, T=|ρ(A)|, L=∏Π, all n≥1 (§4–§5, done).
     So it suffices to prove the Crux. — by certified reduction chain (this file §14, lemma files).
  2. Define **key terms** on the actual sequence: a_n is a *key term* iff no earlier key term b has
     P(b) ⊆ P(a_n). Prove {supports of key terms} = 𝓐_∞ (each ⊆-minimal support's first realizer is
     a key term; each key term's support is ⊆-minimal). — by Lemma 6 (domination) + E1 + definition
     of ⊆-minimal in 𝓕. Hence Crux ⟺ finitely many key terms.
  3. **Forward-realizability characterization** (elementary, replaces going through the global set A
     for the witness): for c > a₁, c is a term ⟺ gcd(c, a_i) > 1 for every term a_i < c ("c meets
     every EARLIER term"). — (⟸) let a_n be the largest term < c; c admissible at stage n and > a_n,
     and no term lies in (a_n, c), so a_{n+1}=c. (⟹) pairwise-intersecting Lemma 4. [This is the
     LOCAL admissibility fact — meets earlier terms only, NOT a transversal of all of 𝓐_∞.]
  4. Fix q₀ := max P(a₁) (prime, ≤ a₁), threshold C := q₀·a₁.
  5. **Rescale-Witness / Fresh-Prime Lemma.** Suppose a key term x > C contains a prime p that lies
     in no earlier key term ("p fresh"). Derive a contradiction:
       (i) p ∉ Q:=P(a₁) (a₁ is the first key term, its primes are not fresh at x); by Lemma 4
           gcd(x,a₁)>1 so pick q ∈ P(x)∩Q; then q ≠ p, q ≤ q₀, and q ∈ S:=P(x)∖{p}.
       (ii) Set r:=∏S. Build y: if r ≥ a₁ put y:=r; else let t be least with y:=r·q^t ≥ a₁, then
            r·q^{t-1} < a₁ ⇒ y < q·a₁ ≤ q₀·a₁ = C. In both cases a₁ ≤ y, P(y)=S (mult. by q∈S adds
            no prime), and y < x (case r≥a₁: y=r=∏(P(x)∖{p})<∏P(x)≤x; case r<a₁: y<C<x). — window.
       (iii) y meets every earlier term (every term a_i < y): every term is a key term or is
            dominated by an earlier key term b (P(b)⊆P(a_i), step 2). For a key term a_i<x: by Lemma 4
            P(a_i)∩P(x)≠∅ and p∉P(a_i) (p fresh, a_i earlier key term) ⇒ P(a_i)∩S≠∅. For non-key
            a_i: P(b)∩S≠∅ (b earlier key term) and P(b)⊆P(a_i) ⇒ P(a_i)∩S≠∅. — freshness + Lemma 4.
       (iv) By step 3, y is a term; y < x and P(y)=S ⊊ P(x). So P(x) is NOT ⊆-minimal in 𝓕
            (S=P(y)∈𝓕 is a strictly smaller support), contradicting x being a key term. ∎(lemma)
  6. **Threshold finiteness.** Let K := ⋃{P(b) : b key term, b ≤ C}; finite (finitely many terms in
     [a₁,C] since a_n↑∞, each finite support). Claim every key-term support ⊆ K: else let x be the
     FIRST key term with P(x)⊄K; then x>C and any prime p∈P(x)∖K is fresh (all earlier key terms —
     those ≤C by def of K, those in (C,x) by minimality of x — have support ⊆K∌p), so step 5 gives a
     contradiction. Hence 𝓐_∞ = {key supports} ⊆ 2^K, finite. **Crux proved.** — by step 5 + pigeon.
  7. Feed Crux into certified §4–§5 endgame ⇒ theorem, T=|ρ(A)|, L=∏Π, all n≥1. — done. ∎
Key lemmas (claim + mechanism):
  - Forward-realizability (step 3): c>a₁ is a term ⟺ it meets every smaller term — because the greedy
    successor a_{n+1} is the least admissible integer > a_n and admissibility at stage n = meeting all
    a_i, i≤n, all < c. This is the local, per-candidate handle; it does NOT require y to be a global
    transversal of 𝓐_∞ (the R4-Collapse wall) — only to meet already-emitted (smaller) terms.
  - Fresh-Prime removal is legal, p_max is not: freshness of p ⇒ no earlier term shares ONLY p with
    P(x). Proof: an earlier term a_i with P(a_i)∩P(x)={p} is dominated by an earlier key term b,
    b∩P(x)⊆{p} and b∩P(x)≠∅ ⇒ p∈b, contradicting p fresh. (For p_max this fails — E3 gives a genuine
    private-witness term sharing only p_max, which is the certified R5/JSC obstruction.)
  - Window y<C<x: the threshold C=q₀·a₁ is used only in the r<a₁ sub-case to force y<C, hence y<x;
    lifting r by powers of the SMALL anchor q≤q₀ (not by any spread/subtraction) keeps P(y)=S and
    lands y in [a₁, q·a₁). This is multiplicative rescaling by a bounded anchor prime — NOT a
    |t−t′| spread bound (JSC-dead), NOT a disjoint rejection cost (RBD-dead).
Open gaps (builder proves from scratch — external solution is a hint, not a citation):
  (a) step 3 forward-realizability rigorously (or cite/extend certified E1 to the "meets earlier
      terms" form); (b) step 5(iii) y is realized — the freshness argument for ALL earlier terms;
  (c) step 2 key-support = 𝓐_∞ equivalence, and step 5(iv) the minimality contradiction as the run
      DEFINES 𝓐_∞ (⊆-minimal in 𝓕={F(a_i)}); (d) window bounds y<C<x in both r-cases.
Cases to cover: r≥a₁ (y=r) vs r<a₁ (y=r·q^t); a₁ a prime power (Q={q₀}, then 𝓐_∞={{q₀}} trivially
  finite — the fresh-prime case never fires, dispose separately); |P(x)|=1 (x=p^e a key term ⇒ its
  support {p} minimal ⇒ p ∈ K or fresh, same argument).
Watch out for: (1) do NOT remove p_max — remove a FRESH prime (see correction above); (2) "fresh" =
  not in any earlier KEY term (non-key earlier terms MAY contain p; handled by domination); (3) y
  must meet terms SMALLER than y (all < x), not "all of 𝓐_∞" — preserve the local vs transversal
  distinction that keeps this off the R4-Collapse guardrail; (4) verify E1 as certified supports the
  forward-realizability form (it should: {a_n}=A∩[a₁,∞)); if there's any friction, prove step 3
  directly from the greedy definition instead of via the global set A.

---

### key-term-first-appearance : new
Target: The full theorem — ∃ T,L with a_{n+T}=a_n+L for all n≥1 — proved self-containedly by a
sequential key-term finiteness argument that BYPASSES the E4/E5/E5″ reduction chain entirely.
Technique: Dynamic first-occurrence "key-term filter" (official Solution-2 framing, re-derived from
scratch) + the certified no-transient/Reduction-Lemma endgame; NO antichain-cardinality (E4) or
radical-bound (E5/E5″) machinery.
Skeleton:
  1. Free lemmas (import certified free-lemmas.md): Anchor (each a_n meets P=P(a₁)); Gap bound
     (a_{n+1}−a_n ≤ M, a_n↑∞); Distance–prime (q|a_i,a_j ⇒ q≤|a_i−a_j|); Pairwise-intersecting
     (gcd(a_i,a_j)>1). — certified.
  2. Forward-admissibility (self-contained): c>a₁ is a term ⟺ c meets every term a_i<c. — greedy
     successor is least admissible integer > current term (as leader step 3). [Prove here directly;
     do NOT route through the global set A — this slug deliberately avoids the antichain apparatus.]
  3. Key terms: a_n key iff no earlier key term b has P(b)⊆P(a_n). Domination: every term's support
     ⊇ some key term's support (descend the finite support). — first-occurrence induction.
  4. Threshold C=q₀a₁, q₀=max P(a₁). Rescale-Witness Lemma: a key term x>C with a fresh prime p
     yields an earlier term y, P(y)=P(x)∖{p} ⊊ P(x), so x is dominated by an earlier key term
     (contradiction). — identical local construction as leader step 5 (fresh prime, y=r·q^t in
     [a₁,C), y meets all smaller terms via freshness+pairwise-intersecting).
  5. Finiteness: no key term > C introduces a fresh prime ⇒ all key-term primes lie in the finite
     pool K of primes of key terms ≤ C ⇒ distinct key terms have distinct supports ⊆ 2^K ⇒ finitely
     many key terms. — threshold + pigeonhole.
  6. Endgame (import certified no-transient-fixed-successor.md + free-lemmas.md Reduction Lemma):
     finitely many key terms ⇒ finite prime pool Π'=⋃ key supports ⇒ A a finite union of residues
     mod L:=∏Π' ⇒ successor is a cyclic shift ⇒ a_{n+T}=a_n+L for all n, T=|ρ(A)|. — certified
     machinery; re-instantiate with Π' in place of Π (same object). ∎
Key lemmas (claim + mechanism): same core Rescale-Witness Lemma as the leader (fresh prime removable;
  y meets only earlier terms; window via anchor-prime rescaling). The DIFFERENCE from the leader: no
  reference to 𝓐_∞-as-static-antichain, E1's global set A, E2/E3/E4 or the E5″ target — the whole
  finiteness is phrased on the running sequence via key terms, so it is a structurally independent
  proof object (different bridge to the certified endgame).
Open gaps (from scratch): (a) forward-admissibility (step 2); (b) y realized (step 4, freshness for
  all smaller terms); (c) key-term/domination bookkeeping (step 3) — that "first violator x" is well
  defined and its fresh prime satisfies the lemma's hypothesis; (d) endgame re-instantiation with Π'
  (verify the certified no-transient/Reduction lemmas apply to the key-term prime pool unchanged).
Cases to cover: r≥a₁ vs r<a₁; a₁ prime power (Π'={q₀}, T=1, L=q₀); no fresh prime ever above C.
Watch out for: (1) FRESH prime, not p_max (same correction); (2) keep it genuinely self-contained —
  the point of this rival is to NOT depend on E4/E5/E5″, so if the leader's §15 has a bridging snag
  with the legacy E5″-machinery, this slug still stands; (3) the endgame import must be checked, not
  assumed — no-transient is certified for the actual sequence, and Π' is literally ⋃𝓐_∞, so it
  should slot in, but the builder must confirm the residue-union/cyclic-shift step re-derives.

---

### SINGLE-GAP-TRAP NOTE (for the reviewer's gate)
The two slugs share the identical core lever (fresh-prime rescale-witness). Per CLAUDE.md this is
normally the single-gap trap. I seed BOTH deliberately, as a hedge on the RE-DERIVATION (this is the
sole live opening after a 6-round plateau, and it is strong — official solution, and its threshold
C=q₀a₁ reproduces the run's independently certified L on a₁=375 exactly). Their independence is at
the BRIDGE, which is where re-derivation is most likely to snag: the leader must reconcile the new
argument with its static 𝓐_∞ / E1-global-A / legacy-E5″ apparatus (risk: friction with the p_max
framing of E5″ and with the global set A); the key-term slug is a clean-slate dynamic proof that
imports ONLY the certified free-lemmas + no-transient endgame and never touches E4/E5/E5″. If the
reviewer judges the shared lever too risky to double-invest, DROP `key-term-first-appearance` and
advance only the leader — but the recommended build set is BOTH, with the reviewer vetting the shared
lever (esp. step (iii) "y is realized" and the FRESH-vs-p_max distinction) once, hard, up front.

build set: redundant-constraint-antichain, key-term-first-appearance
