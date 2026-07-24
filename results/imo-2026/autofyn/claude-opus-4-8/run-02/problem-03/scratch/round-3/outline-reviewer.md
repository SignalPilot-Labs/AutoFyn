# Outline review — imo-2026-03, round 3

Two active revises, each a whole end-to-end attempt at `c(n)=2^n/(2^{n+1}-1)` importing the
sibling's bound once certified. They are genuinely far apart in framing (integer-value
chamber-telescoping/parity for GAP-L; amortized multi-peel phase for GAP-U) and attack disjoint
gaps — the productive form of diversity for this two-gap-isolated endgame. Both are one honest
residual from closing their owned bound. One retirement decision confirmed.

Numeric checks I ran (W_2={1,2,4}): global min of f over all real ≤2-cut refinements = **1.0**
exactly; integer values seen at the minimizer are **odd** (1, 3); the "nice interleaving" chamber
(s1>2>s2>1>s3) gives f≡1 on 12,590/12,590 samples — the chamber-telescoping identity holds
exactly. This corroborates the GAP-L mechanism.

---

## self-similar-recursion — CHANGES REQUESTED (build)

Owns GAP-L (`f(P)≥1` for every ≤n-cut refinement of W_n). The re-plan drops the dead "perturb
toward integer vertices" plan and replaces it with **chamber-telescoping + parity-of-the-value**.

**Technique is sound.** Verified load-bearing pieces:
- *Chamber-telescoping identity* (Step 3): on a chamber where every sub-piece of original piece
  `2^k` shares one sign `ε_k`, its signed total is `ε_k·Σ(sub-pieces)=ε_k·2^k` by conservation,
  independent of the (possibly irrational) offsets, so `f=Σ ε_k 2^k ∈ ℤ`. This is a correct
  algebraic identity (not a parity trick), and it is exactly why non-integer cut positions do not
  break the argument — confirmed exactly by my scan.
- *Odd-value floor* (Step 5): `Σ ε_k 2^k ≡ ε_0 ≡ 1 (mod 2)`, and `f≥0` (Lemma E), so `f≥1`;
  `ε_n=+1` forced and minimal positive value is `2^n−(2^n−1)=1`. Airtight, and matches the certified
  Lemma D re-used at the level of the *value* rather than the pieces (the correct fix for the round-2
  `d=3` obstruction, which only kills parity-of-pieces).
- *Mixed piece ⇒ not a local min*: if piece `2^k` has sub-pieces of mixed sign, then along the
  spatial order of its sub-pieces some adjacent pair differs in sign, so the cut between them has
  gradient `±2` — a strict descent direction. This direction is correct.

**THE GAP (Step 4) — flag to builder, this is the whole job.** The descent-terminates-at-a-
monochromatic-or-degenerate-minimizer claim is honestly labelled open. Two things the builder MUST
nail, or the "descent" reads as done when it isn't (my role-memory wall from round 2):
  1. **Termination across rank-ties.** At a wall the descent either (i) degenerates a cut →
     strictly fewer effective cuts → induction on the cut budget (base: uncut W_n, `f=f(W_n)≥1`,
     a Jacobsthal value) — this leg is clean; or (ii) crosses a rank-tie at constant `f` into an
     adjacent chamber. Leg (ii) is where a cycle could hide: prove the cross-tie iteration is
     well-founded (f is non-increasing and bounded below by 0, chambers are finite, but a
     constant-f tie-walk needs an explicit no-cycle/strict-drop-per-visit argument — a bare
     "iterate" is not enough).
  2. **Inter-piece ties and per-piece monochromaticity.** "Monochromatic" is per original piece;
     a chamber can be monochromatic for some pieces and mixed for others, and a tie can be between
     sub-pieces of *different* original pieces (sign reassignment on crossing). The descent must
     remove EVERY mixed piece and handle inter-piece ties, not just a bisection's own halves. The
     outliner flags both — hold the builder to actually discharging them.

The explorer's route (b.1) — prove directly that every chamber's telescoped value is `≥1` with the
nice-interleaving chamber `=1` and "popping strictly raises f" (n=2: `f=5−2s1>1` when `s1<2`) — is
a viable *alternative* finish to the same identity and may sidestep the termination bookkeeping;
the builder may use it in place of the explicit descent if cleaner. Either closes the same residual.

Do NOT reintroduce parity-of-pieces or any integer-cut assumption (dead, `d=3`), and do NOT invoke
any blanket "cutting a non-top piece never helps" domination (FALSE, 28k counterexamples). Only
Lemma A's top-band localization is licensed. Corollary C (`u≥1 ⇒ f≥1`) remains a valid independent
shortcut for that regime.

## alternating-sum-threshold-potential — CHANGES REQUESTED (build)

Owns GAP-U (`g_b(P)≤s/D_b`). Re-plan: replace the lock-step "one cut ⇒ budget −1" step with a
**telescoped multi-peel phase** on the effective top, adaptive length `k∈{1,…,m−1}`.

**Reduction arithmetic checks out.** I verified `1−D_{b−k}/D_b = 2^{b−k+1}(2^k−1)/D_b`
(since `D_b−D_{b−k}=2^{b−k+1}(2^k−1)`), and the telescope
`g_b(P) ≤ g_{b−k}(R_k) ≤ Σ(R_k)/D_{b−k} ≤ s/D_b` closes **iff** `Σ(R_k) ≤ (D_{b−k}/D_b)s`, i.e.
`Σ_{j≤k} r_j ≥ (1−D_{b−k}/D_b)s`. The IH at `b−k` is legitimate: `|R_k|=m−k ≤ (b−k)+1` from
`m≤b+1`. So the skeleton is arithmetically sound; only the mass-removal *existence* claim is open.
STOP, base b=0, one-cut recursion (★), and the geometric step under (H) are all certified.

**THE GAP (Step 3) — flag to builder, and the specific concern the dispatch raised.** The phase
mass-removal inequality — that `f(P)>s/D_b` guarantees some `k≤m−1` with cumulative removal
`≥(1−D_{b−k}/D_b)s` — is currently only **sketched** ("f>s/D_b bounds the gaps from below, which
lower-bounds Σr_j"). As written this is the weakest link: `f` being large (a sum of adjacent gaps
`Σ(a_{2j−1}−a_{2j})`) does not obviously force the successive *effective tops* to carry a large
cumulative fraction — large `f` can come from many moderate gaps, not a heavy top, and in regime
(M) the top is by definition NOT heavy (`a_1,2a_2 < (2^b/D_b)s`). The builder must make the link
`f>s/D_b ⇒ cumulative-top-mass` **precise and explicit** — a bare "bounds the gaps" is an
unverified hand-off.
  - **The hypothesis f>s/D_b MUST be used, and here is why it cannot be skipped:** pure bisect-top
    for all `k` provably UNDERSHOOTS the required fraction on balanced inputs (equal pieces:
    cumulative `< (D_b−1)/D_b·s`) — but balanced inputs have *small* `f` and are killed by STOP, so
    `f>s/D_b` is exactly what excludes the bad case. A proof that does not consume this hypothesis is
    wrong (it would prove a false statement on balanced inputs). Recommended: strengthen the IH to a
    **two-parameter invariant** tracking both `s` and the piece count `m` (crux `aimo-0236` phase
    invariant), and/or a **discharging** argument (crux `aimo-0558`), rather than attacking the raw
    inequality one-shot.
  - **Effective-top / mass conservation.** Recompute the effective residual (subtract invisible
    matched pairs) before each peel and re-decide bisect-top vs top-match at THAT level — do NOT
    peel the physical max blindly (recorded dead end `[0.385,…]→0.153` overshoots). Validate
    `Σ(new)=Σ(old)` on every step; the "top-match to a deeper `a_k`, k>2" move silently drops mass
    if coded as delete-and-replace, and its mass-conserving single-step form is provably too weak
    alone — only the multi-cut phase works.

The claim is numerically true in (M) (explorer: `g_3≈0.032≪1/15`), so this is a proof-architecture
gap, not a false target. Do NOT retry the one-shot dual/LP certificate (dead) or fixed "bisect n
times" (overshoots).

## game-value-recursion — RETIRE to dormant (do NOT build), agree with outliner

Closed no gap in 2 rounds (now Elo 1472, below both leaders); its only open item (budget
non-fungibility) is the SAME GAP-L wall the two revises now attack with concrete new mechanisms, so
it adds no independent shot on goal; Case A is redundant with certified `alt-sum-two-max-minus-total`.
Keep the file as a dormant population member (do not delete). If the GAP-L descent stalls next
round, reconsider reviving it to carry the monochromatic-parity idea in claiming-game language as a
second independent attack. `majorization-smoothing` stays dormant/dead.

## Diversity note (for the orchestrator)

The field is deliberately narrow now (two approaches, one per gap) — correct for a two-gap endgame
where both residuals are pinned and far apart. This is NOT a shared-gap plateau: the two gaps are
disjoint and each has a fresh, concrete, sound mechanism this round. If EITHER residual stalls for
another round, that gap has become the shared wall — then seed a genuinely different framing for
that specific bound (for GAP-L, the game-value/claiming-game reframing of monochromatic-parity is
the on-deck diversity hedge).

## Ranking (Elo after this round)

self-similar-recursion 1584 (advanced, lead — GAP-L residual closest to done, identity verified
exact) > alternating-sum-threshold-potential 1550 (advanced — GAP-U reduction sound, phase
existence open) > game-value-recursion 1472 (partial, retired to dormant) > majorization-smoothing
1394 (dead). No new slugs to register; no branch/copy requested.

build set: self-similar-recursion, alternating-sum-threshold-potential
