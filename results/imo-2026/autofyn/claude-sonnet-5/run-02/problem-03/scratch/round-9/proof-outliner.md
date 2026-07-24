## imo-2026-03

greedy-halving-adversary: advance (revised skeleton written in place)
Target: Claim (B) — for fixed F (Xiang Yu's split of p_1 into c<n cuts) and
any legal tail refinement G', A(F∪G') >= a_n. Full problem target unchanged:
c(n) = 2^n/(2^{n+1}-1), lower-bound half.
Technique: window-splitting generalization of the already-certified
Half-Window Vanishing Lemma / Cross-Term Vanishing Lemma, extended from
"two fragments of p_1" to "F = {v} ∪ P with P fully paired, v the single
unpaired residual" (odd-run length ℓ(F)=1) — reuses 100% certified machinery
(cross-term-identity-threshold, safe-window-lemma, odd-run-reduction-lemma).
Skeleton (full detail written to results/imo-2026-03/approaches/greedy-halving-adversary.md
§"Round 9 outline"):
  1. Show u_F ≡ 1[x<v] for F={v}∪P, A(P)=0 — via odd-run-reduction-lemma.
  2. Apply cross-term-identity-threshold to A(F∪G').
  3. Case-split v>=p2 (reuse half-window-vanishing-lemma's proof verbatim —
     Safe-Window forces v_{G'}≡0 on [p2,r), collapsing the integral to the
     already-closed window) vs v<p2 (genuinely new: needs tail-self-similarity
     rescaling + induction on n, not yet derived).
  4. Combine to close ℓ(F)=1 unconditionally.
  5. Numerically re-check (exact Fraction, n=4,5,6, not just n=3) whether
     ℓ(F)>=3 configurations ever come close to a_n; if not, scope Claim (B)'s
     proof honestly to ℓ(F)∈{0,1} rather than claiming full generality.
Key lemmas: single-residual odd-parity indicator (mechanism: odd-run-reduction-lemma
degenerates to one step function); case v>=p2 closes by direct lemma reuse
(same two prerequisites as c1=1 case both hold); case v<p2 is the new open item.
Open gaps: case v<p2 of step 3 is unproved; ℓ(F)>=2 only numerically checked
at n=3.
Cases to cover: ℓ(F)=0 (closed), ℓ(F)=1 with v>=p2 (closes via reuse) and
v<p2 (open), ℓ(F)>=2 (numerically non-binding at n=3 only, unproved generally).
Watch out for: don't assume v=p2 is a forced structural fact (it's one n=3
witness, not a theorem); don't conflate ℓ(F) (odd-run of F alone) with ℓ(S)
for the whole multiset — parity-coincidence-and-zero-iff-dead-end is about
the latter and does not transfer without re-derivation.

lp-duality-certificate: advance (revised skeleton written in place)
Target: the general upper bound c(n) <= a_n for every n and every legal Liu
Bang marking p_1>=...>=p_m>0 (m=n+1), the other, independent half of the
full problem.
Technique: strong induction on m, splitting the marking space into p_1>=T/2
(closes via Theorem A + new recursive Theorem C′) and p_1<T/2 (open, needs
a new move or vertex-enumeration reuse).
Skeleton (full detail in results/imo-2026-03/approaches/lp-duality-certificate.md
§"Round 9 outline"):
  1. Base case m=1: Φ=T=a_0T trivially.
  2. Regime p_1>=T/2: formalize Theorem C′ (bisect p_1, recurse on tail with
     n-1 cuts — exact identity via pair-cancellation-identity, same status
     as certified one-step-peel-identity) for p_1>=a_nT, combined with
     certified Theorem A (Full-Match) for T/2<=p_1<a_nT. Prove (not just
     verify for n<=8) via the telescoping identity a_{k-1}-a_k =
     2^{k-1}/(D_{k-1}D_k) that the two threshold regions are contiguous with
     zero gap, for all n.
  3. Regime p_1<T/2 (genuinely open, both on-file hard witnesses live here):
     try Theorem E (Bisect-Top-Two: bisect p_1,p_2 simultaneously, recurse
     on {p_3,...,p_m} with n-2 cuts) via the same pair-cancellation-identity
     derivation as Theorem D, first cheaply checked against both hard
     witnesses; alternatively reuse the certified vertex-minimum-theorem
     (same LP-vertex fact, polarity-agnostic per round-8's caveat) to
     restrict this regime's minimizing Xiang-Yu response to a finite vertex
     family.
  4. Combine regimes to close c(n)<=a_n unconditionally.
Key lemmas: Theorem C′ exact identity (pair-cancellation-identity instance,
unconditional like certified Theorem B); threshold match p_1>=a_nT
(telescoping identity, needs general-n proof not just n<=8 check); Theorem A
∪ Theorem C′ covers all of p_1>=T/2 with no gap since a_n>=1/2 always.
Open gaps: entire p_1<T/2 regime (Theorem E undreived, vertex-minimum reuse
untried); step 2's general-n induction proof itself still needs writing
(currently only exact-algebra-checked for n<=8).
Cases to cover: p_1>=a_nT (Theorem C′), T/2<=p_1<a_nT (Theorem A), p_1<T/2
(open).
Watch out for: do NOT reuse Theorem D's crude bound (A<=Total) in place of
Theorem E's exact value — already confirmed too weak at both hard witnesses;
do NOT assume a direct recursive-ceiling analog of Theorem D (Theorem D′)
closes p_1<T/2 — explicitly checked and found to still fail at
(3/8,1/4,1/4,1/8) (p_1+p_m=1/2 < threshold 0.8) — the floor-vs-exact-value
gap re-appears one level down and needs something genuinely sharper.

rank-pigeonhole-budget: advance (no changes needed — Claim (A) is fully
closed per round 8; this slug stays live/registered as the certified home of
Claim (A)'s full closure, no new work assigned this round since its target
is complete).

rank-tie-vertex-reduction: not selected for build this round. No genuinely
new mechanism was surfaced for the general c_1>=2 lower-bound gap beyond
what's already ruled out (peel/ℓ-induction confirmed dead, round 8). Per
dispatch instructions, leaving it off the build set rather than forcing an
approach with no new idea; its Parity Coincidence + Zero-Iff dead-end result
remains certified and reusable. Revisit if greedy-halving-adversary's ℓ(F)=1
generalization (which uses genuinely different vocabulary, not peel/ℓ
induction) makes enough progress to suggest a transferable mechanism for the
general c_1 case.

build set: greedy-halving-adversary, lp-duality-certificate
