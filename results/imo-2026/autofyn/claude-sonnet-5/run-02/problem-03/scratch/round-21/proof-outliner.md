## imo-2026-03

greedy-halving-adversary: revise
Target: the problem's actual claim — c(n) = 2^n/(2^{n+1}-1) for every n
  (this approach's slice: the general lower bound, specifically closing the
  TRUE target (Diamond') — Δ(n,v) ≤ v-f(n)-2v·ε(v), not the weaker
  ε=0-only (Diamond) — for Theorem 35's Case (a), "p₃ untouched").
Technique: direct algebraic bookkeeping — keep the ε'(v)/ε(v) correction
  terms alive through the already-certified `upper-truncation-identity` /
  `truncated-alternating-sum-floor` machinery instead of dropping them
  (as Theorem 35a/35b currently do), then cancel the correction via an
  already-certified identity chain (ladder doubling p₂=2p₃ + Lemma 24
  `level-2-dominance-identity`).
Skeleton:
  1. State and prove the **Band-Parity Fact** as a standalone lemma: for
     any finite multiset S sorted descending r₁≥r₂≥…≥r_k, ε(v):=
     𝟙[|S_{>v}| odd] is the parity of v's rank-band — ε(v)=1 iff v lies in
     an odd-indexed half-open band [r_{2j},r_{2j-1}), ε(v)=0 on even-
     indexed bands (including v≥r₁ and v<r_k when k even) — by direct
     induction on which elements of S lie above v as v decreases.
  2. Theorem 35a redo (v<p₃, i.e. R'_{>v}={p₃}∪T'_{>v}): substitute the
     floor lemma's EXACT inequality Ξ:=A(T')-2A(T'_{>v})≥v-s'-2v·ε'(v)
     into Δ(n,v)=-p₃-Ξ, using the parity identity ε(v)=1-ε'(v) (forced
     since |R'_{>v}|=1+|T'_{>v}|). Compare against the target
     Δ(n,v)≤v-f(n)-2v·ε(v). The two sides match term-for-term once
     f(n)=p₃-s' — cite this exactly from already-certified `Lemma 24`
     (p₂-s=f(n)) plus ladder doubling p₂=2p₃: p₃-s'=p₃-(s-p₃)=2p₃-s=
     p₂-s=f(n). This closes the sub-range v≤s' of Theorem 35a for BOTH
     values of ε'(v) — no case split needed, pure substitution.
  3. Theorem 35a's boundary sub-range s'<v<p₃: here T'_{>v}=∅ so ε'(v)=0
     trivially, hence ε(v)=1 (odd band one level up, by step 1's fact).
     Target reduces to A(T')≥v-s'; since v<p₃ strictly, v-s'<p₃-s'=f(n)
     strictly (step 2's identity). Cite Theorem 35b's own already-proved
     bound A(T')≥f(n)·2^{n-3}≥f(n) (via standing IH (⋆_{n-3})) — strictly
     stronger than needed, closes this sub-range with no new derivation.
  4. Theorem 35b (v≥p₃): here R'_{>v}=T'_{>v} directly (p₃ not counted),
     so ε(v)=ε'(v) with no shift — check whether the existing proof
     already carries the correction term through unchanged (likely, since
     there is no "extra +1" from p₃ here) or needs the same substitution
     trick at this level; write out explicitly, do not assume free.
  5. State the general conjecture (from the recursive identity structure
     — `tail-self-similarity` + Lemma 24 recurring at every ladder depth)
     that this same substitution trick closes (Diamond') at every
     induction level, not just n=3,4 — attempt as an inductive step if
     steps 2-4 go cleanly, as a stretch goal.
  6. Theorem 35's Case (b) ("p₃ is cut", Theorem 36's n=3,4 territory):
     redo the same ε-tracking through Theorem 36's 10-sub-range case
     split at n=4, locating via the Band-Parity Fact exactly which
     sub-ranges have ε=1, then check each against Ξ's correction term the
     same way. This is NOT yet verified even in outline form (explorer
     flagged it as a plausible-but-unconfirmed candidate) — treat as a
     genuinely open sub-task, separate from steps 2-4's near-mechanical
     closure.
Key lemmas (claim + mechanism):
  - Band-Parity Fact — because |S_{>v}| increases by exactly 1 each time v
    crosses an element of S descending from ∞ to 0, so its parity flips at
    each crossing, giving the band structure directly.
  - f(n)=p₃-s' — because p₂=2p₃ (ladder doubling, certified) and
    f(n)+s=p₂ (Lemma 24, `level-2-dominance-identity`, certified), so
    p₃-s'=p₃-(s-p₃)=2p₃-s=p₂-s=f(n); this is the exact cancellation that
    makes the ε(v)-carrying floor inequality literally equal to (Diamond').
Open gaps: step 4 (Theorem 35b's own ε-bookkeeping, not yet checked
  explicitly even though structurally likely free) and step 6 (Case (b) /
  Theorem 36's ε-bridge, genuinely unverified — do not overclaim it closes
  "the same way" without doing the 10-sub-range check).
Cases to cover: Theorem 35 Case (a) v≤s' (mechanism 1), s'<v<p₃
  (mechanism 2), v≥p₃ (Theorem 35b, step 4 — verify explicitly), Case (b)
  p₃-is-cut (step 6, open).
Watch out for: do not claim (Diamond') is closed for Case (b) until the
  10-sub-range check is actually done — the explorer only verified
  mechanisms 1/2 (Case a); do not silently extend "closes for free" past
  where it was actually checked. Also verify step 1's Band-Parity Fact
  handles the k-even/k-odd boundary cases (v≥r₁, v<r_k) correctly before
  relying on it in steps 2-3.

rank-pigeonhole-budget: revise
Target: the problem's actual claim — c(n) = 2^n/(2^{n+1}-1) (this
  approach's slice: closing the TRUE target — full (♯) with the ε(v₂)
  correction, not the weaker ε=0 (♯) — for §7.5's n=3 middle band, then
  extending to general n via §7.6).
Technique: same direct-substitution bookkeeping as the sibling, reusing
  the Band-Parity Fact (import as a shared lemma, do not re-derive) plus
  a case-specific tightened bound on v₁+v₂ using the case hypothesis
  v₂<p₃ (not just v₂>0), which the original §7.5 proof had available but
  didn't use for the weaker (♯) target.
Skeleton:
  1. Import the Band-Parity Fact from `greedy-halving-adversary` (or the
     newly-certified standalone lemma file, once written) rather than
     re-deriving: confirm §7.5's 3-case split already isolates exactly the
     ε=1 sub-case as its middle case (v₂∈[p₄,p₃)), per the Fact — cases
     v₂≥p₃ (τ_{>v₂}=∅, ε=0 automatic) and v₂<p₄ (τ_{>v₂}=τ, |τ|=2 even,
     ε=0 automatic) are the two ε=0 bands, confirming this is not a
     coincidence.
  2. In the middle case v₂∈[p₄,p₃): the full ε-corrected target subtracts
     an extra 2v₂ beyond the file's existing (♯) closure, i.e. needs
     v₁+v₂≤s+3p₄=6p₄. Prove this directly: v₂<p₃=2p₄ (case hypothesis,
     tighter than the original proof's v₂>0) and v₁<p₂=4p₄ (domain), so
     v₁+v₂<4p₄+2p₄=6p₄ strictly — write out the full chain explicitly
     with the exact original proof's other cited facts (s-(v₁-v₂)>s-p₂
     etc.) integrated, not just the new inequality in isolation.
  3. Verify this closes ALL of §7.5 (the n=3 case) for the TRUE target,
     not just the middle band — confirm the two automatic-ε=0 cases need
     no extra work (their existing (♯) proof already suffices since
     ε=0 means (♯)=(full target) there).
  4. Attempt §7.6 (general n≥4): the pre-existing gap there is the
     cross-piece tie-vertex enumeration, NOT the epsilon-bridge — the
     epsilon-bridge fix by itself does not close §7.6; state this
     explicitly so the builder doesn't conflate "closed the bridge at
     n=3" with "closed the general-n gap."
Key lemmas (claim + mechanism):
  - Band-Parity Fact (imported, cite the sibling's proof once certified,
    do not re-derive) — same mechanism as above.
  - Tightened v₁+v₂<6p₄ bound — because the case hypothesis v₂<p₃ (not
    merely v₂>0) combined with the domain bound v₁<p₂ gives a strictly
    tighter sum than the original (♯)-only proof needed, and this exact
    slack is what the extra -2v₂ correction term requires.
Open gaps: §7.6's general-n cross-piece tie-vertex enumeration (untouched
  by this fix, remains fully open, pre-existing).
Cases to cover: §7.5's three v₂-sub-cases (only the middle one, v₂∈
  [p₄,p₃), needs new work for the ε-bridge; the other two are automatic).
Watch out for: don't conflate closing the n=3 epsilon-bridge with closing
  §7.6's general-n gap — write the Status/Current-best update to keep
  these explicitly separate, since round 20's reviewer already flagged
  this file for one overclaim risk (§7.6 vs Claim A conflation) in a
  prior round's history.

lp-duality-certificate: revise
Target: the problem's actual claim — the general upper bound c(n)≤a_n for
  arbitrary Liu Bang markings, specifically closing case (b2)
  (T/D_n<p₂<a_nT/2, p₁<T/2) — the sole remaining open region of the
  upper bound, with 7 confirmed-dead mechanism families already on file.
Technique: **Local-Concavity / Chamber-Vertex Maximization over Liu
  Bang's OWN marking p** (not Xiang Yu's response) — a primal
  extreme-point argument, genuinely distinct from all 7 dead mechanisms
  (not explicit-strategy construction, not weighted combination, not
  constraint-side LP dual, not global smoothness/Danskin, not
  probabilistic). Reuses `per-piece-vertex-decomposition-theorem` +
  `odd-run-reduction-lemma`, applied one level up (to p instead of to
  Xiang Yu's fragment multiset F).
Skeleton:
  1. Recall (already certified, cite verbatim, do not re-derive):
     `vertex-minimum-theorem` — for fixed p, Φ_min(p) is attained at a
     vertex of Xiang Yu's response polytope, and `per-piece-vertex-
     decomposition-theorem` — at that vertex every fragment coordinate is
     an affine function of p (Cramer's rule on the tie/zero linear
     system).
  2. Prove the new **within-chamber affinity fact**: a "chamber" is a
     maximal region of p-space over which Xiang Yu's optimal-response
     vertex has one fixed combinatorial tie/zero pattern (type); within a
     single fixed chamber, Φ_min(p) restricted to that chamber IS affine
     in p — direct consequence of step 1's coordinate formula being the
     SAME linear system (same Cramer's-rule matrix) throughout one
     chamber, only p varying. State explicitly why this is weaker than,
     and does not contradict, the already-refuted Danskin/global-concavity
     dead end: the V-shaped local min Danskin found sits exactly at a
     chamber WALL (p₃=p₁-p₂, where the response type switches) — a
     cross-chamber phenomenon, not a within-chamber failure.
  3. Decompose case (b2)'s box (T/D_n<p₂<a_nT/2, p₁<T/2) into its
     finitely many chambers (finite since determined by the same finite
     hyperplane arrangement `per-piece-vertex-decomposition-theorem`
     already certifies exists). On each chamber, by step 2, Φ_min(p) is
     affine on (chamber ∩ box), so its maximum over that intersection is
     attained at an extreme point: either (i) a box-facet is tight
     (p₁=T/2, p₂=T/D_n, or p₂=a_nT/2), or (ii) two of the chamber's own
     defining tie/zero constraints become degenerate/coincide (a
     chamber-wall vertex).
  4. This reduces sup_{p∈box} Φ_min(p)≤a_nT to a FINITE check: verify
     Φ_min(p*)≤a_nT at each such extreme point p* — first for n=3,4
     explicitly (small chamber counts, matches the two known near-tight
     witnesses: round 14/15's n=3 "flat-face" and n=4 "pinned-tie"
     witnesses, both ALREADY described as chamber-boundary points, strong
     corroborating evidence).
  5. Before committing further: (a) verify computationally at n=2,3 that
     Φ_min(p) is genuinely affine within a fixed chamber (no silent
     chamber-boundary crossing corrupting the check); (b) count chambers
     intersecting case (b2)'s box at n=3,4 by brute enumeration
     (exact-Fraction) to get an honest read on chamber-count growth — if
     it explodes with n, flag as a risk for general-n closure but still
     useful incrementally; (c) check whether the two known witnesses are
     literally chamber vertices under this framing.
Key lemmas (claim + mechanism):
  - Within-chamber affinity of Φ_min(p) — because step 1's per-piece
    vertex-decomposition coordinate formula is literally the same affine
    (Cramer's-rule) function of p throughout one chamber; only the
    combinatorial tie/zero pattern (which changes at chamber walls) can
    break affinity, and by definition of "chamber" that pattern is fixed.
  - Chamber-intersected-with-box has finitely many vertices — because the
    box is itself a polytope (3 linear facet constraints) and the chamber
    is a polytope (finite hyperplane arrangement per already-certified
    theorem), so their intersection is a polytope with finitely many
    vertices by standard polyhedral theory.
Open gaps: (a) rigorous general argument that chamber∩box is a polytope
  with finitely many vertices — should follow from cited theorem but
  needs writing out; (b) a bound on how many chamber vertices exist as a
  function of n (real risk: if exponential with no further structure,
  this converts one hard enumeration into another of the same size, not
  obviously easier); (c) the actual Φ evaluation at the resulting vertex
  family against a_nT — where the real work is. Scope the first build
  attempt to n=3,4 explicitly before attempting general n.
Cases to cover: n=3,4 first (small chamber counts, matches known
  witnesses); general n as a stretch goal, explicitly gated on (b) above
  not exploding.
Watch out for: this is a PRIMAL extreme-point argument (maximize Φ_min
  over p), not a dual certificate — do not confuse with the already-dead
  `minimax-lp-response-polytope` (constraint-side dual, proven to only
  ever certify the wrong direction); state this distinction explicitly in
  the write-up so the reviewer doesn't flag it as a resurrection of dead
  mechanism 6. Also do not confuse this with the dead Danskin mechanism —
  this needs only LOCAL (within-chamber) affinity, not global concavity.

build set: greedy-halving-adversary, rank-pigeonhole-budget, lp-duality-certificate
