# Round 21 outline-reviewer report

## 1. `a1-3q-subfamily-theorem` — verification of the Jacobsthal-bound mechanism

Read the file's round-21 outline (Steps 1–5) and the scouting explorer's
report, then did independent numeric/algebraic sanity checks rather than
taking either at face value.

**Step 4 (the "uniformity" concern) — LESS of an obstruction than flagged,
and I found the fix.** The outliner worried that `k*(q)` (the threshold
past which the crude bound `window ≥ 2^{ω(qK)}` beats the pigeonhole
requirement) might depend on `q` in a way that turns "finitely many small
`k`" into an illegitimate infinite per-prime check. I checked this
directly: `window(k,q) = n_0(q)-1+kq ≥ kq ≥ 7k` (using `n_0≥1` and the
universal minimum `q≥7`), while the required bound `2^{ω(qK)+1} ≤
2^{ω(K)+2}` depends on `k` **only through `K=K_0+3k`, K_0∈{4,5}** — i.e.
it does NOT depend on `q`'s actual magnitude at all, only on which of two
residue classes `q` falls in mod 3. So the inequality `7k ≥ 2^{ω(K)+2}`
that needs to hold for `k≥1` is **q-independent**: a single finite
verification (I ran it for `k=1..39`, both `K_0` values, zero failures —
`sympy` factorization) plus one asymptotic tail argument (linear beats
sub-polynomial `ω(K)=O(log k/log log k)`) closes ALL primes `q≥7`
simultaneously. This is a genuine, valuable finding: **the uniformity gap
is resolvable**, and cheaply — the builder should be told this directly
(save them from re-deriving it) so they can go straight to nailing the
tail-asymptotic argument and the finite check, rather than treating Step 4
as an open research question.

**Step 1 (the crude Jacobsthal bound itself) — genuinely more fragile than
portrayed; this is the real remaining risk.** I independently verified
`g(M) ≤ 2^{ω(M)}` numerically (checked every `M` up to 3000, zero
violations, matches OEIS A048670 on primorials, tight at small cases like
`M=4,6`) — the STATEMENT is almost certainly true. But I tried to actually
carry out the "split window into two halves, apply IH to each half,
resolve the case where both candidates are divisible by `p`" induction
sketched in the outline, and it does **not** close cleanly. Concrete test:
`M=6=2·3`, window `{1,2,3,4}`. IH at `r=1` (`M'=3`) on each half of length
2: first half `{1,2}` has candidates coprime to 3 (both 1 and 2 qualify);
second half `{3,4}` has one candidate coprime to 3 (namely 4; 3 itself is
excluded). If the induction's witness-selection happens to land on `2`
(from the first half) and `4` (from the second half) — both **even** —
the sketched argument has no way to rule out "both are divisible by `p=2`"
even though the window plainly *does* contain a coprime-to-6 point (`x=1`,
which the argument never surfaces because IH only asserts existence, not
which point). This shows the literal two-halves argument, as sketched, is
**incomplete in a way that isn't just a "sub-case to spell out"** — a
naive fix I attempted (shifting by `M':=p_1···p_{i-1}` to preserve
coprimality to earlier primes while cycling through residues mod the new
prime) gives a MUCH weaker bound, on the order of `rad(M)`-scale window
length, i.e. it reproduces the bound the file has *already shown
insufficient*, not `2^{ω(M)}`. I could not find, within the time
available, a repaired elementary induction that actually delivers the
`2^r` bound — it's plausible one exists (the statement is true), but it
may require tracking a stronger invariant (e.g., a count of surviving
residues, not mere existence) or, in the worst case, genuine sieve
machinery (Brun's sieve gives bounds of a similar flavor but is a
nontrivial named theorem, not "standard CRT/pigeonhole" as the scouting
report characterized it). **Verdict: Step 1 is not confirmed
provable-from-scratch as an elementary fact by anything produced so far —
it is the outline's true crux, more fragile than the "should be a clean
lemma" framing suggested, and the builder must be told explicitly that a
naive two-halves argument will not work as written; if no elementary
repair is found this round, that must be reported honestly (gap
identified, not closed) rather than waved through via the sketch's
current wording.**

**Net assessment:** this approach is still the highest near-term value
target (closest to a 3rd APPROVE, floor deliverable material either way),
and is worth a build slot — but the round's outline slightly
mischaracterizes where the difficulty lives (it flagged Step 4 as the risk
and treated Step 1 as routine; my check finds the reverse: Step 4 is
cheaply closable, Step 1 is the genuine open problem). The build dispatch
should carry both corrections forward.

## 2. `fah-counterexample-hunt` — genuinely different, precisely scoped, untried territory confirmed

Checked against CLAUDE.md's plateau-break mandate and against the
workspace's actual history (grepped the seed values used across all
approach files and `current.md`'s round history):

- **Genuinely different in kind, not a repackaging of 15 rounds of seed
  testing.** Every prior round's simulation work (rounds 6–20) either (a)
  spot-checked a proof mechanism's numeric claims on the four canonical
  `|Q|=2` seeds (`187,209,221,247`) or a handful of others chosen for
  convenience (`4807=11·19·23`, `11305=5·7·17·19`, `510510`, `209370`,
  `255255`, `15,45`, `30030`, `15015`), or (b) re-derived/re-verified a
  proposed theorem's own worked examples. None of these were run as a
  *falsification search* — i.e., nobody previously chose seeds
  specifically engineered to maximize the chance of exhibiting persistent
  non-intersection, nor specified in advance what would count as success.
  This is a real difference in epistemic stance (adversarial search vs.
  incidental non-discovery), matching what CLAUDE.md asks for when a field
  bottoms out on one wall.
- **Scoping is precise enough to build.** §1 of the file gives a concrete,
  checkable three-part criterion (verified-finite `S*`; two
  certified-infinite disjoint-base-type types; persistent, not
  merely-so-far, disjointness via either a structural invariant or an
  adversarially-targeted long simulation with an explicit no-decaying-trend
  check) and explicitly rules out "near miss" (bounded-delay intersection
  or decaying minority frequency) as a non-result. This is buildable: a
  builder can run the search, and both "found a candidate meeting the
  criterion" and "searched hard, found nothing, here's what was tried" are
  well-defined, reportable outcomes.
- **The flagged search territory is confirmed genuinely unexplored.**
  Cross-checked every `a_1` value appearing anywhere in
  `results/imo-2026-06/` — all documented hard/rogue-pair seeds have
  `|Q|=2` (two distinct primes) except the bookkeeping/monotonicity seeds
  (`30030,15015,255255,510510,209370` etc., which are `p^k`-adjacent or
  used for NTBT/self-absorption checks, not FAH rogue-pair racing). No
  seed in the workspace was constructed via a deliberate CRT-engineered
  size-imbalance between two primes, and no `|Q|≥3` seed was ever used as
  a *rogue-pair* FAH test (only as an NTBT/self-absorbing-core numeric
  record). So both directions in §2 (`|Q|≥3` rogue pairs; lopsided-CRT
  recruitment races) are real gaps in the workspace's search coverage, not
  disguised re-runs.
- **Honest-outcome framing is sound and matches CLAUDE.md's rigor rules**:
  a negative outcome is correctly scoped as `unsolved` (not "FAH proved"),
  additive evidence rather than a restatement of the plateau. A positive
  outcome (an actual counterexample) is correctly scoped as forcing
  future architectural work, not promised as solving the whole problem
  this round.

**Verdict: worth a build slot.** This is the correct instantiation of
CLAUDE.md's plateau-break rule — a genuinely different framing (attacking
the hypothesis itself, not another proof mechanism for it), not a
bypass that will hit the same wall one step later.

## 3. `n1-periodicity-reconciliation` — optional touch, not worth a slot this round

The proposed round-21 touch is purely editorial (folding Theorems A/B into
one floor statement, a consistency re-check, no new mathematical content
by design). Given only two other slugs are genuinely live and
high-value this round (the a1-3q gap and the counterexample hunt), and
this file's own outline explicitly says "no urgency attaches... if the
outline-reviewer judges build capacity is better spent" elsewhere — I
judge build capacity is better spent on the two mathematically live slugs.
Editorial consolidation carries no risk of going stale (nothing else this
round is expected to reach APPROVE that would obsolete it — a1-3q is not
expected to fully close this round given the Step-1 fragility found
above), so deferring it costs nothing. **Decision: not built this round.**

## 4. Ranking and build set

Registered `fah-counterexample-hunt` (new, cold-start Elo). Ran head-to-head
comparisons reflecting this round's relative standing: `a1-3q-subfamily-
theorem` (highest near-term value, closest to a 3rd APPROVE, most
build-ready) beats both `n1-periodicity-reconciliation` (pure bookkeeping,
not selected for build) and `fah-counterexample-hunt` (new and unproven,
but correctly seated per the plateau-break mandate); `fah-counterexample-
hunt` and `n1-periodicity-reconciliation` are roughly a draw this round
(both non-primary but for different reasons — one is deliberately
speculative-but-mandated, the other is deliberately deferred-as-optional).
Updated ratings recorded via `mcp__approach-ranker__update_ranking`.

Two builder slots this round. Both builders should receive this review's
corrections verbatim:
- `a1-3q-subfamily-theorem`'s builder: Step 4's uniformity concern is
  RESOLVED (use the q-independent `7k ≥ 2^{ω(K)+2}` argument above,
  don't re-derive it from scratch); Step 1's crude bound is the REAL open
  risk — the naive two-halves induction has a genuine hole (see the
  `M=6` counterexample-to-the-argument above), not merely an
  unwritten sub-case; if it cannot be repaired elementarily this round,
  report exactly that, honestly, rather than asserting Step 1 closed.
- `fah-counterexample-hunt`'s builder: follow §2's search directions
  exactly (`|Q|≥3`, CRT-engineered lopsided pairs, high-`ω(a_1)` seeds);
  do not re-run the canonical `187/209/221/247` sweep; apply the precise
  criterion in §1 before calling anything a candidate counterexample.

build set: a1-3q-subfamily-theorem, fah-counterexample-hunt
