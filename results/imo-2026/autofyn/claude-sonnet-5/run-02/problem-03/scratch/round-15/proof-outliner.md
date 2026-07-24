# Round 15 outliner report — IMO-2026-03

No new slugs opened this round: the field is not plateaued (both live fronts
made independent real progress rounds 12–14, and both explorers this round
surfaced a genuinely new, concrete lead rather than a repeat of an old wall).
Revised both live approach files in place with concrete round-15 outlines
(appended as new `## Round 15 outline (proof-outliner)` sections at the end
of each file — no prior content removed or overwritten).

## Current standing (via `mcp__approach-ranker__sample_approaches`, k=10)

`greedy-halving-adversary` (Elo 1605, stale=true, last: `advanced`) and
`lp-duality-certificate` (Elo 1589, stale=true, last: `partial`) remain the
two live fronts for the whole-problem claim; `rank-pigeonhole-budget` (Elo
1708) sits highest but is scoped to Claim (A) only (already fully closed) —
not a build target this round. Both live fronts are marked `stale` (Elo
predates their round-14 outcomes), so the outline-reviewer should re-rank
both after reading this round's builds.

## greedy-halving-adversary — revised outline

**Headline reframing from Explorer 1:** items "ℓ(F)=1, v<s" and "ℓ(F)=2
sub-case (b)" are the *same* gap — Lemma 25 (already certified, round 11)
decomposes sub-case (b) exactly into two v<p2 instances, and Proposition 24
already closes v∈[s,p2). So closing v<s closes both items at once, for free.
This is now the outline's **Target A (primary)**: close v<s via a rescaling
argument at the (n-2)-level sub-tail, adapted to a *partial* window [0,v)
(v<s) rather than Proposition 24's full window — concretely, try to reduce
the partial integral to the known full-window bound plus a correction term
bounded via the already-certified `max-domination-lemma` / `triangle-bound-
for-a` on just the excess mass in [v,s). Flagged that numeric slack here is
the tightest of all four items (0.055–0.14×f(n) at n=3,4) — expect the
argument needs to be close to sharp, not crude.

**Target B (secondary, time-boxed):** item 3 (ℓ(F)=2, P≠∅, τ_P≥p3) — the
numerically most comfortable item (slack up to 17×f(n) at n=6). Explicitly
told the builder NOT to re-attempt the "instantiate Theorem 29 directly"
shortcut (refuted by Explorer 1: hypothesis max(G')≤t*/2 fails structurally,
and the naive conclusion is violated in ~92% of trials even outside the
hypothesis). Instead directed to try a cruder bound combining
`triangle-bound-for-a` with Total(P)≥τ_P≥p3 and the existing A(G')≥f(n)
recursive bound — the generous slack means even a factor-of-2–3-lossy bound
should suffice.

**Target C (deferred):** item 4 (ℓ(F)≥3) — comfortably satisfied
numerically, untouched machinery-wise, flagged for a dedicated future round
rather than splitting this round's budget.

Also recorded (so the builder doesn't repeat them): the two scripting budget
bugs Explorer 1 caught (mass-doubling `exact_pair_set` bug; item-4 script
omitting p2 from the refinable tail) — always assert the constructed
multiset sums to 1 before trusting a numeric check.

## lp-duality-certificate — revised outline

**New lead from Explorer 2:** a "Cross-Piece Sign-Assignment Identity" — a
strict generalization of `pair-cancellation-identity`/`bisect-top-k-lemma`
where a piece's fragments can land on *non-adjacent* ranks of one common
parity (not just adjacent opposite-parity pairs), contributing its whole
original value ±p_i to Φ rather than 0. Verified concretely at round 14's
n=3 near-tight case-(b2) witness, where it telescopes to an exact
split-independent identity on a genuine flat 2-dimensional polytope face.

**Two-part target for this round's builder:**
1. Prove the general Cross-Piece Sign-Assignment Identity from the already-
   certified `pair-cancellation-identity` + `integral-alternating-sum-
   formula`, explicitly importing `odd-run-reduction-lemma` from the
   lower-bound population for the evaluation half — this executes round 9's
   suggestion, never attempted until now. Verify against both of round 14's
   witnesses (the n=3 flat-face case and the structurally different n=4
   pinned-tie case) to confirm it strictly contains, not just duplicates,
   `per-piece-vertex-decomposition-theorem`'s known vertex shapes.
2. Attack the resulting **feasibility question** — which sign vectors ε are
   realizable given cut budget n and a legal composition/order — as a finite
   combinatorial problem (not continuum vertex enumeration), and show the
   resulting minimum achievable Φ stays ≤a_nT throughout case (b2)
   specifically.

Explicitly told **not** to re-attempt literal joint vertex-fixed-point
enumeration this round (reconfirmed intractable/heterogeneous by Explorer
2's two structurally different witness types — matches every prior round's
diagnosis, R11.5/R12.5/R14.3). Fallback recorded (lower priority given this
round's concrete new lead): sharpen case (a)'s conditioning so case (b2)'s
recursive sub-instances land in case (a)/(b1) one level down.

## Build set

build set: greedy-halving-adversary, lp-duality-certificate
