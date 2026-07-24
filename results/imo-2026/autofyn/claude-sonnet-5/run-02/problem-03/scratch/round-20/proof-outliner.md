## imo-2026-03

rank-pigeonhole-budget: advance
Target: the whole problem's answer c(n) = 2^n/(2^{n+1}-1) — this slug's own
contribution is the lower-bound front's middle-band closure (Δ(n,v), Claim B).
Technique: discrete case-split / mass-conservation budget accounting (as
already used throughout §7 of the approach file), fixing a boundary bug this
round; no new top-level mechanism needed.
Skeleton:
  1. **Fix the v2=p4 boundary bug in §7.5's n=3 middle-band closure.** The
     current case split is `v2>=p3`, `v2 in (p4,p3)`, `v2<=p4`. The third
     case computes `tau_{>v2} = tau = {p3,p4}` even exactly at `v2=p4`, but
     every other lemma in the file (`truncated-alternating-sum-floor/-ceiling`,
     Theorem 35's own epsilon(v) convention) uses a **strict** `>`, so at
     `v2=p4` exactly `p4` is NOT `>v2` and `tau_{>v2}` should be `{p3}`
     (matching the *second* case's formula), not `{p3,p4}`. Re-split the
     cases as `v2>=p3`, `v2 in [p4,p3)` (closed on the left — absorbs the
     old boundary point), `v2<p4` (now open on the right) — by tool: direct
     substitution, re-verify the middle case's existing closed-form algebra
     for `Delta(3,v2)` is literally unchanged on `v2 in [p4,p3)` (it already
     is, since the formula `Delta = A(tau)-2p_3 = -3p_4` is a single
     continuous expression on that whole half-open interval, not something
     that behaves differently exactly at the left endpoint).
  2. Delete the erroneous `v2=p4` computation from the old third case and
     replace with a one-line pointer to the corrected second case. This is a
     pure case-boundary relabel, not new algebra — should not require
     re-deriving `(sharp)` itself.
  3. Re-state §7.5's conclusion ("all three cases close, strictly, no
     numerics") with the corrected case boundaries; the conclusion itself
     (unconditional n=3 middle-band closure) is unaffected — only the
     intermediate case split changes.
Key lemmas (claim + mechanism):
  - No new lemma; this reuses `truncated-alternating-sum-ceiling` and Lemma
    24 (`level-2-dominance-identity`) exactly as already certified — the fix
    is purely a boundary-relabel correction to an already-correct proof.
Open gaps: general n>=4 middle-band vertex enumeration (§7.6, honestly
diagnosed as re-encountering the project's oldest cross-piece tie-vertex
obstruction) — explicitly NOT in scope for this round's fix, do not attempt.
Cases to cover: the fix must show the corrected case split is exhaustive on
`v2 in [0,s)` (three cases: `[p3,infty)`∩domain, `[p4,p3)`, `[0,p4)`) with no
gap or overlap at the boundary points `p3`, `p4`.
Watch out for: don't accidentally re-open the `v2>=p3` case's boundary too —
check it independently uses `>=` consistently with the strict-`>` convention
(it currently computes `tau_{>v2}=empty` for `v2>=p3`, which is correct
since `p3` is not `>v2` when `v2=p3` either — this boundary is already
right, only the `p4` one needs the fix).

greedy-halving-adversary: advance
Target: the whole problem's lower bound c(n) >= 2^n/(2^{n+1}-1) — this
slug's contribution is completing Theorem 35 (Claim B's Δ(n,v) target) by
closing Case (b), the "p3-is-cut" branch.
Technique: strong induction via `tail-self-similarity` + `sharp-dominant-
removal-identity` (Fact 2), reframing the self-similar object correctly —
NOT a new tool, a corrected scoping of which object is self-similar to what.
Skeleton:
  1. **Reframe the self-similar object.** The stuck attempt (current file,
     "Case (b): p3 is cut... not closed") tries to bound `A(B)` for
     `B={b}∪T'` in isolation and finds `B` is not a clean rescaled ladder
     copy (three routes tried, all dead — do not retry any of the three:
     max-domination-lemma on B alone gives the wrong direction; peeling b
     off B assuming dominance is false in general; treating B as a smaller
     standard ladder response directly is false since b is a free real in
     `(0,p4]`, not forced to `p4/2^j`). The FIX: don't isolate `B`; the
     genuinely self-similar object is the WHOLE `R'={a,b}∪T'`, which is
     *exactly* a legal response to the `(n-2)`-ladder `{p3,p4,...,p_{n+1}}`
     (total mass `s`) using at most `n-3` total cuts (1 to split `p3` into
     `{a,b}`, plus <=`n-4` more for `T'`) — i.e. Xiang Yu peeling a dominant
     fragment `a` off the `(n-2)`-ladder's OWN top piece `p3` and refining
     the rest arbitrarily, which is literally the shape Theorem 31 /
     Propositions 20-22 (ℓ(F)=1) and Theorems 32-35 (ℓ(F)=2, middle band)
     already exist to handle — instantiated one level down at `n-2`. By
     tool: `tail-self-similarity` rescaling from level `n` to level `n-2`.
  2. **Small-case direct-substitution check (do FIRST, before any general-n
     argument).** For `n=3`: level `n-2=1` is the trivial 1-ladder, already
     fully, unconditionally closed (`c(1)=2/3` both directions, round 1).
     For `n=4`: level `n-2=2` is the fully, unconditionally closed 2-ladder
     (`c(2)=4/7` both directions, round 1-2 milestone). Substitute these
     already-closed results directly into the reframed Case (b) statement
     (the full Claim-B lower bound at level `n-2`, not just Claim A's
     narrow sub-case) and check by exact algebra whether Case (b) closes
     for free at `n=3,4`. By tool: direct substitution/exact-Fraction check
     (per the explorer's own recommendation, this is a <10-minute algebra
     check, not a search — do it before committing to the general argument).
  3. **If step 2 confirms the pattern, set up the general-n bootstrapping
     tower.** Level `n`'s Case (b) needs level `n-2`'s FULL theorem (middle
     band included, not just Claim A) as IH — a genuine strong-induction
     dependency (not circular, since `n-2<n`), analogous to the
     telescoping-threshold mechanism already used on the upper-bound front
     (round 9). Once `n=3` is fully closed (step 2 + rank-pigeonhole-
     budget's fixed n=3 middle band), `n=5`'s Case (b) becomes available;
     once `n=4` closes, `n=6`'s becomes available; etc.
Key lemmas (claim + mechanism):
  - Reframed Case (b) statement: `R'={a,b}∪T'` (the WHOLE thing, not `B`
    alone) is a legal `(n-2)`-ladder response with budget `<=n-3` — because
    mass conservation on `{p3,...,p_{n+1}}` (total `s`) is exactly the
    `(n-2)`-ladder's own mass-conservation constraint, and the cut count
    matches (1 cut on the new "p1"-analog `p3` plus `<=n-4` on its tail is
    exactly a legal `(n-2)`-response using `<=n-3` cuts total).
  - n=3/n=4 free closures — because the required IH (full theorem at level
    `n-2 in {1,2}`) is *already unconditionally proved*, so no new
    inequality-proving is needed, only correct substitution.
Open gaps:
  - The general-n bootstrapping tower (step 3) — needs step 2 confirmed
    first, then a from-scratch write-up of the induction, not yet done.
  - **The un-enumerated deeper sub-branch**: a legal "p3 is cut" response
    may use MORE than one cut directly on p3 (splitting it into 3+ pieces,
    or further splitting `b` itself) — the current write-up only treats a
    single cut splitting p3 into exactly `{a,b}`. Flag explicitly, do not
    silently assume this is covered by the same argument without checking;
    likely reachable by repeating the dominant-removal peel (Fact 2)
    recursively, but must be stated as its own sub-case.
  - The ε=1 bridge subtlety from `upper-truncation-identity`'s parity
    correction term, noted open since round 19, still unresolved and
    orthogonal to this fix.
Cases to cover: n=3 (direct substitution using c(1) closure), n=4 (direct
substitution using c(2) closure), general n>=5 (bootstrapping tower,
conditional), the multi-cut-on-p3 sub-branch (separately, not yet attempted).
Watch out for: don't conflate "the whole theorem at level n-2" with "just
Claim A at level n-2" — per round-10 Rule #15, the IH needed here is
the FULL Claim A+B+middle-band closure at level n-2, which is why n=1,2
(unconditionally, fully closed both directions) are the only currently-
available free instantiations; n-2=3,4 aren't usable as IH yet since level
3/4's own middle band (Case (b) itself!) isn't closed — so the bootstrap
genuinely starts at n=3,4 and climbs by +2 each time, not by substituting an
arbitrary n-2.

lp-duality-certificate: advance
Target: the whole problem's general upper bound c(n) <= 2^n/(2^{n+1}-1) —
this slug's contribution is closing case (b2) (`T/D_n < p2 < a_n*T/2`), the
last open regime of the upper bound front, using a genuinely new mechanism
(7th attempt on this front; 6 mechanism families are confirmed dead — do
NOT propose another peel/bisect/recurse, weighted-combination, boundary-
continuity, Danskin/concavity, surrogate-adversary, or constraint-side-LP-
duality variant).
Technique: **probabilistic method** (existence via expectation) +
**derandomization via linearity of expectation** — genuinely distinct in
kind from all 6 dead families: it needs no concavity of Φ_min in Liu Bang's
marking (kills mechanism 4), no combining of several already-fixed numeric
Φ-values by a weight (kills the naive collapse into mechanism 2 — see watch
out below), and no LP dual certificate on the constraint side (kills
mechanism 6).
Skeleton:
  1. **Set up the randomization correctly (critical design choice).** Do
     NOT randomize over a finite family of already-named deterministic
     strategies (Bisect-Top-k, Cross-Piece Sign-Assignment, etc.) with fixed
     or p-dependent weights — `E[Φ]` for such a discrete mixture is
     literally `Σ w_k Φ_k`, i.e. exactly the object the certified
     **Convex-Combination Futility Theorem** already proves can never beat
     `min_k Φ_k` — that collapses straight back into dead mechanism 2. The
     randomization must instead be over a CONTINUOUS family of legal cut
     positions themselves (a single stochastic cutting rule), so that
     `Φ(response)` is a genuinely continuous random variable and `E[Φ]` is
     computed via linearity of expectation piece-by-piece
     (`E[Φ] = Σ_pieces Pr[piece lands at odd rank] · E[length | ...]`, or
     more directly `E[Φ] = ∫ Φ(x) f(x) dx` for a chosen density `f` over the
     cut-position parameter `x`), not by averaging pre-computed Φ-values of
     named strategies.
  2. **Concrete candidate construction.** In case (b2)'s band, let Xiang
     Yu's response be: split `p1` at a single random point `X`, `X ~ f`,
     for a density `f` on `(0,p1)` to be chosen (parametrized by
     `r = p2/(a_nT/2)`, e.g. Beta or a shifted-uniform density concentrated
     near the deterministic templates' failure boundary), leaving the tail
     untouched (or, if needed, combined with a second independent random
     variable for a tail cut). Use the already-certified exact closed-form
     identities (Theorem A-D `bisect-top-recursive-identity`, `bisect-top-
     bottom-recursive-identity`) to write `Φ(x)` (or `Φ(x,y)`) in closed
     form as a function of the cut position(s), THEN integrate against `f`
     to get `E[Φ]` in closed form.
  3. **Prove `E[Φ] <= a_n T` throughout case (b2)'s band** by direct algebra
     on the closed-form integral (a calculus/algebra argument on the chosen
     density's parameters as functions of `p1,p2,r`), not by case-splitting
     on which deterministic template wins.
  4. **Invoke the probabilistic method / derandomization step**: since
     `min_x Φ(x) <= E_X[Φ(X)] <= a_n T`, some specific (deterministic,
     still-legal) response `x*` achieves `Φ(x*) <= a_n T`, i.e.
     `Φ_min <= a_n T` — closing case (b2). By tool: the elementary
     probabilistic-method principle (`knowledge_base.md` "General Proof
     Methods"/probabilistic method; corpus subtopic
     `probabilistic-method`), applied here as pure existence-from-average,
     no concentration/tail bound needed since only existence (not "most")
     is required.
Key lemmas (claim + mechanism):
  - `E[Φ]` is a LINEAR functional of the chosen density `f` (not of a
    finite set of fixed Φ-values) — because `Φ(x)` is a fixed algebraic
    (rational) function of the continuous cut position `x` (via the
    already-certified closed-form identities), so `E[Φ]=∫Φ(x)f(x)dx` is a
    genuinely different mathematical object from `Σw_kΦ_k`; this is the
    precise reason the Convex-Combination Futility Theorem's negative
    result does NOT apply here — it only rules out combining a FIXED,
    FINITE set of already-evaluated numbers, not integrating a continuous
    function against a density.
  - `min_x Φ(x) <= E_X[Φ(X)]` — because the minimum of any function over its
    domain is at most any weighted average (expectation) of its values over
    that domain; this is the elementary derandomization step.
Open gaps: the actual density `f` (or joint density if two random cuts are
needed) that makes step 3's inequality true throughout case (b2)'s band is
NOT yet identified — this is the real remaining design/algebra work, not a
proof gap in the mechanism itself. Do the cheap numeric check first (below)
before committing to a full symbolic derivation.
Cases to cover: case (b2)'s full 2D box `T/D_n < p2 < a_n*T/2` (parametrized
by e.g. `p1,p2` with tail structure free) — the construction/proof must
cover the whole band, not just the two known near-tight witnesses (which
should be used as sanity checks, not the target).
Watch out for: (1) the collapse-into-dead-mechanism-2 risk flagged in step 1
— any candidate must be checked to NOT reduce to a discrete mixture of
named strategies before being trusted as genuinely new; (2) before any
symbolic derivation, run a cheap 10-minute numeric check (exact `Fraction`
or `sympy`) of a simple candidate density (e.g. uniform on `(0,p1)`, or
Beta parametrized by `r`) at the two on-file case-(b2) witnesses (n=3
flat-face, n=4 pinned-tie) plus several fresh random points in the band —
if `E[Φ]` computed this way already exceeds `a_nT` for the simplest density
at even one point, revise the density's shape before writing up a general
proof, per the explorer's cheap-kill recommendation.
