## imo-2026-03

greedy-halving-adversary: advance
Target: The problem's actual claim end to end (via the ladder construction
c(n)=2^n/(2^{n+1}-1)): this approach owns the lower-bound direction's Claim
(B) — arbitrary tail refinement combined with any split of p_1 never pushes
Liu Bang's total below f(n)=a_n·T — which combines with the already-closed
Claim (A) to give the full lower bound c(n)>=a_n.
Technique: Strong induction on n consolidating the three separately-chased
sub-branches (v<s, p2-cut-complement remainder, ℓ(F)>=2) into ONE inductive
hypothesis, per the explorer's structural finding that all three are the
same recursive obstruction restated at a smaller scale, plus a
window-difference decomposition for ℓ(F)=2 that reuses ℓ(F)=1 machinery
directly instead of a fresh lemma.
Skeleton:
  1. State the unified target P(n): "for every legal F (Xiang Yu's split of
     p_1) with ℓ(F)<=1, and every legal tail refinement G', A(F∪G')>=f(n)."
     (ℓ(F)=0 and ℓ(F)=1,v>=p_2 already fully closed — cite
     cross-term-vanishing-lemma, single-residual-exact-peel-identity,
     v-geq-p2-budget-reduction, p2-cut-complement-branch-closure.)
  2. Prove P(n) by strong induction assuming P(n-1) AND P(n-2) (two distinct
     recursion depths appear, both needed — by tool: direct algebraic trace
     of which branch invokes which depth, cite the explorer's derivation).
  3. Branch v<s (p_2 untouched): show via cross-term-identity-threshold that
     A(F∪G') reduces to a partial integral ∫_0^v u_{R'} against a refinement
     R' of the SAME ladder one level down (n-2), where R' plays the role of
     an arbitrary legal refinement of the (n-2)-ladder — i.e. this branch
     IS an instance of P(n-2), not a new inequality — by direct substitution
     matching the explorer's derivation ("algebra up to A(F∪G')=p_2-v+A(R')
     unaffected by v vs s; only ∫_0^v u_{R'}=A(R') step needs v>=s" — for
     v<s, replace that step by the P(n-2) hypothesis applied to R' directly
     rather than the exact identity used when v>=s).
  4. Branch p2-cut-complement's uncovered piece w'<p_3: by the identical
     rescaling substitution Q=τ/r (Q the (n-1)-ladder, w=w'/r, q_2=p_3/r)
     already used inside Proposition 25's own proof, this branch IS
     Proposition 24's v<p_2 problem posed one level up at n-1 — hence an
     instance of P(n-1) — by tool: direct substitution + tail-self-similarity.
  5. Branch p2-cut-complement's other piece (p_3 itself cut by G'): by the
     same rescaling, this IS the p_2-cut-complement problem (Prop 25's own
     target) recursed one level down at n-1 — an instance of P(n-1) again.
  6. ℓ(F)=2: derive the length-2 odd-run indicator u_F(x)=1[v_2<=x<v_1] via
     odd-run-reduction-lemma, giving
     A(F∪G')=(v_1-v_2)+A(G')-2∫_{v_2}^{v_1}v_{G'}(x)dx. Split the window
     integral by linearity: ∫_{v_2}^{v_1}v_{G'}=∫_0^{v_1}v_{G'}-∫_0^{v_2}v_{G'},
     and bound EACH single-threshold piece via the already-certified
     ℓ(F)=1 machinery (Prop 20/24/25, applied at thresholds v_1 and v_2
     respectively) — closing ℓ(F)=2 as a direct corollary of ℓ(F)=1, not a
     new lemma, PROVIDED the mixed-regime case (v_1>=p_2>v_2, thresholds
     landing in different ladder regimes) is checked explicitly since the
     two single-threshold bounds may not simply subtract cleanly.
  7. Base cases n<=4: already unconditionally closed by Proposition 22/24's
     own scoping (cite directly, no new work).
  8. Conclude P(n) holds for all n by strong induction (steps 3-6 exhaust
     every branch — no open-ended "new branch" pattern remains once cast
     this way), completing Claim (B) and hence the full lower bound
     c(n)>=a_n.
Key lemmas (claim + mechanism):
  - Branch reduction lemma: "v<s branch of P(n) reduces to P(n-2) applied to
    R'" — because the cross-term identity's algebra is v-independent up to
    the point where dominance (v>=s) is invoked; below that threshold the
    same reduced quantity A(R') is exactly what P(n-2) bounds directly.
  - Rescaling lemma: "p_2-cut-complement's uncovered branches reduce to
    P(n-1)" — because Prop 25's own proof already performs an exact
    ladder-rescaling substitution Q=τ/r that maps the residual sub-problem
    bijectively onto the (n-1)-ladder's own v<p_2 / p_2-cut-complement
    structure.
  - Window-difference lemma for ℓ(F)=2: "∫_{v_2}^{v_1}v_{G'} splits into two
    single-threshold integrals already bounded by Prop 20/24/25" — because
    integration is linear and each single-threshold piece is literally the
    object those propositions already evaluate.
Open gaps: the mixed-regime sub-case of step 6 (thresholds v_1,v_2 landing
in different ladder regimes) needs explicit verification, not just the
generic linearity argument; the two-depth induction's exact base-case
bookkeeping (does P(n) really need BOTH P(n-1) and P(n-2), or can one
recursion depth be eliminated) should be nailed down precisely, not just
asserted; ℓ(F)>=3 is not addressed by this outline at all (only ℓ(F)<=2) —
flag explicitly whether the same window-decomposition scales to ℓ(F)=k in
general via k/2 windows, or whether a genuinely new argument is needed there.
Cases to cover: v>=s vs v<s (p_2 untouched, ℓ(F)=1); p_2 cut, w'>=p_3 vs
w'<p_3, and p_3 itself cut vs untouched (ℓ(F)=1); ℓ(F)=0 (closed),
ℓ(F)=1 (this round's target), ℓ(F)=2 (this round's target),
ℓ(F)>=3 (explicitly flagged as NOT covered by this outline).
Watch out for: do NOT resurrect the ℓ(F)-Collapse Lemma's literal "merge
residuals" move (confirmed dead end, not mass-preserving); the
window-difference idea in step 6 is a genuinely different, non-merge route
and is not affected by that dead end; verify the two-depth induction is not
circular (P(n) using P(n-1) which uses P(n-2) which uses P(n-3)... must
bottom out cleanly at n<=4, check the recursion doesn't skip or double-count
a level).

lp-duality-certificate: advance
Target: The problem's actual claim end to end, upper-bound direction — this
approach owns proving c(n)<=a_n for arbitrary Liu Bang markings (matching
the lower bound from the sibling), completing the full determination of c(n).
Technique: two independent sub-tasks this round — (a) a scoped, low-risk
textual fix to certify an already-proved lemma; (b) a structural
redirection abandoning the too-narrow "cut p_1 only" restriction in favor of
directly applying the marking-agnostic vertex-minimum-theorem to arbitrary
compositions, then attempting a general evaluation argument mirroring the
Case I Closure Theorem's recipe.
Skeleton:
  1. (Pin-set fix.) First prove the general Zero-Pin Harmlessness Lemma: a
     zero-length pinned coordinate cannot change Φ, because a zero element
     sits at the bottom of sorted order and cannot alter the rank-parity of
     any positive element above it — by tool: direct argument from the
     definition of the claiming-subgame reduction (sorted-rank sum).
  2. Restate Lemma A.1/A.2's pin set as {0,τ_1,...,τ_r} (matching what the
     existing proof already uses internally) rather than {τ_1,...,τ_r} —
     by tool: the Zero-Pin Harmlessness Lemma shows this addition changes no
     downstream conclusion (A.3's finite vertex enumeration already
     implicitly allows inert 0-pins), so no re-derivation is needed, only
     the restatement plus one added sentence per the explorer's finding.
  3. Get this corrected Lemma A.1/A.2 certified (closing the round-10 gap).
  4. (Structural redirection — the larger task.) Explicitly retire the
     "cut p_1 only" restriction as insufficient in principle: cite the two
     on-file hard witnesses (Theorem D′'s resolution of (3/8,1/4,1/4,1/8),
     Theorem B_4's resolution of (2/5,3/10,1/5,1/10)) as PROOF (not
     conjecture) that both known hard cases require cuts on pieces other
     than p_1 — so Route A's narrow family can at best give a sufficient
     (not general) upper bound, per rule "round 8" (a bounded/narrow-family
     certificate cannot close a tight equality witness).
  5. Apply the certified, marking-agnostic vertex-minimum-theorem directly
     to an arbitrary legal composition (c_1,...,c_{n+1}) over ALL pieces
     (no per-piece restriction) for arbitrary Liu Bang markings with
     p_1<T/2 — by tool: vertex-minimum-theorem (already proved
     polarity-and-marking-agnostic; note explicitly, per memory rule 6,
     that reusing a MIN-theorem for a MAX-style upper-bound target requires
     restating which extremum is being computed here — Xiang Yu is
     minimizing Φ, so this is literally the theorem's original min form,
     no dualization needed, unlike the lower-bound side's reuse).
  6. Attempt to evaluate the resulting finite vertex family via
     odd-run-reduction-lemma for an ARBITRARY (non-ladder) tail — this is
     the genuinely new content, since Ratio-2 Spacing Lemma and Last-Element
     Bound (the ladder-specific evaluation tools that closed Case I) are
     confirmed NOT to transfer (per round-10 finding/memory rule 9). Name
     candidate new evaluation lemmas: (i) a general "spacing" fact for
     arbitrary (not ratio-2) markings bounding tie-vertex gaps, (ii) a
     general "last-element" analogue bounding the smallest fragment's
     contribution without assuming superincreasing structure.
  7. If the general evaluation closes, conclude c(n)<=a_n unconditionally
     for arbitrary Liu Bang markings, completing the upper bound.
Key lemmas (claim + mechanism):
  - Zero-Pin Harmlessness Lemma: a 0-pinned coordinate is inert to Φ —
    because sorted-rank parity of every positive element is determined only
    by positive elements above it, and 0 can never be "above" a positive
    element.
  - Route-A-insufficiency observation: the cut-p_1-only family cannot close
    p_1<T/2 in general — because both on-file tight witnesses are only
    resolved by tail-touching strategies, a direct proof-by-exhibited-fact
    (not conjecture) that the restricted family's best possible bound is a
    strict sub-case.
  - General-marking evaluation gap: the actual open content of the whole
    upper-bound front is now isolated to finding tail-structure-agnostic
    analogues of Ratio-2 Spacing / Last-Element Bound — because those two
    lemmas' proofs both explicitly use p_i=2p_{i+1} (ladder-specific), which
    an arbitrary marking does not have.
Open gaps: step 6 is the crux — no evaluation argument for arbitrary tails
exists yet; this is genuinely open, not just unattempted busywork. Step 2's
fix is low-risk but still needs the builder to verify A.2/A.3's downstream
claims are literally unaffected (not just spot-checked at one instance as
the explorer did).
Cases to cover: p_1>=T/2 (already closed for n<=3 via Theorem C′, still open
for general n — not this round's focus but should not be silently dropped);
p_1<T/2 (this round's focus, via the vertex-minimum-theorem redirection).
Watch out for: do not conflate "Route A's narrow family is insufficient" as
already fully proved for ALL of p_1<T/2 — it's confirmed insufficient at the
two specific tight witnesses, which is enough to justify abandoning the
narrow-family route in favor of the general redirection, but the general
redirection itself (step 5-6) remains unproved, not a done deal; do not
mechanically transplant Ratio-2 Spacing / Last-Element Bound verbatim into
the general-marking setting (confirmed non-transferable, memory rule 9) —
any reuse must be a genuinely new proof for the arbitrary-tail case.

## Notes on scope
No new slug opened this round: both live fronts have concrete, well-scoped,
non-exhausted sub-lemma plans directly from this round's explorer findings,
and neither shows evidence of a same-framing 3-round plateau (both are
narrowing via genuinely new mechanisms — consolidated induction for
greedy-halving-adversary, structural redirection away from a confirmed-
insufficient narrow family for lp-duality-certificate). Do not resurrect
bisection-only strategies, binary/carry mechanisms, ℓ(S)-induction,
claiming-order-invariant, or iterated-greedy-peel — all confirmed dead ends
on file.
