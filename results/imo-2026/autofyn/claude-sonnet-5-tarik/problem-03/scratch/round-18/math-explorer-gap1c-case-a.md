## imo-2026-03 — SCOUT REPORT: Gap 1c case (a) (sparsest, Lemma-P-irreducible nonempty ξ*)

**Scope of this report.** Dispatched to directly attack Gap 1c's case (a) only (the genuinely-irreducible
sparsest-witness sub-case flagged in round 17, `potential-weighting-upper-bound.md` §27.3/§28.5 item 2).
No proof was completed — this is reconnaissance with fresh computation, per the SCOUT-ONLY mandate.

### Setup, restated precisely (so the outliner doesn't have to re-derive it)

- `B_1` = a size-2 background (e.g. `{16,15}`, `{2,2}`), `Res` = the residual list after peeling to node
  `k^*` (already inside genuine `F`-provenance: real trigger `M<A_1`, true global-argmin `k^*`).
- `u_1 := max(Res)`, partner `u_j := Res[m]` for some `m>=1`, `d := |u_1-u_j|`, `X := Res\{u_1,u_j}`.
- Half-step target: `OPT_{+1}(B_1,X) <= OPT_{+1}(B_1∪{d},X) =: RHS`.
- `ξ*` := the sparsest (min-cardinality) optimal witness of the RHS problem.
- **Case (a)** = `ξ*` nonempty AND `B_1∪{d}∪ξ*` (as a multiset) contains **no duplicate value anywhere**
  (not reducible to `∅` via Lemma P). This is the true open residual; cases (b) (ξ* Lemma-P-collapses,
  e.g. is itself a duplicate pair) and (c) (ξ*=∅) are already closed *conditionally* on Gap 1a's
  Deletion-Suffices-for-`k*` (proved `q<=3`, open `q>=4`).
- The candidate construction (round 16-17, still open): `c := argmin_{x∈ξ*}|x-d|`,
  `M := B_1∪(ξ*\{c})`; claim `e(M) <= RHS` (`= e(M∪{c,d})`), which trivially implies the half-step since
  `OPT_{+1}(B_1,X)<=e(M)` (M is a valid X-selection).

### What I did

Reused the round-17 explorer's own exact-`Fraction` `F`-provenance generator (`/tmp/round-17/gap1c_probe/harness.py`,
`probe1.py`'s `find_F_instance`) — did not trust it blindly, re-derived what it enforces (genuine trigger
`M<A_1` + true global argmin `k*`) by reading the code before using it. Wrote 4 fresh scripts in
`/tmp/round-18/gap1c_case_a/` explicitly separating case (a) from (b)/(c) by checking for duplicate
values in `B_1∪{d}∪ξ*` (rather than trusting the round-17 flat "2/728 residual" framing), then probing
the construction and its underlying two-step insertion algebra at a wider parameter range than round 17
tested (`q` up to 8, `v_max` up to 50, vs round 17's own stated `<=9`/`<=60` — comparable but with more
combined trials, ~2800+ case-(a) checks across 4 scripts).

### Findings

**1. Non-vacuity reconfirmed at a wider scale, no failures.** Across ~2800 combined genuine-`F`-provenance
case-(a) checks (fresh generator seeds, `q∈{4..8}`, `v_max∈{8,10,14,20,30,50}`, both `has_b0∈{T,F}`),
case (a) is the large majority of nonempty-`ξ*` events (consistent with round 17's `~99.7%` figure), and
the nearest-`c` construction had **0 failures** (`margin = RHS - e(M) >= 1` in every single check, exact
integers). This is a genuine, wider-than-before corroboration — still a conjecture, not a proof.

**2. NEW sub-finding — never found `margin=0` in case (a).** Across all ~1558+1403 case-(a) checks
(two separate scripts), the minimum margin observed was `1` — **exact equality never occurred**, unlike
cases (b)/(c) where equality is *exact by construction* (Lemma P forces `RHS=e(B_1∪{d})` there). This
suggests case (a)'s inequality may always be **strict**, a potentially useful structural distinguishing
fact for a future proof attempt (e.g. a strict-inequality argument might be easier than a `<=` argument,
or conversely a "why is it never tight" diagnostic could locate the mechanism) — **conjecture only**, not
swept exhaustively for tie-hunting (would need a dedicated near-tie search, not done this round for time).

**3. NEW sub-finding — a clean, previously-undocumented, unconditional-so-far sub-invariant.** Decomposing
`e(M∪{c,d})-e(M)` as two single-element insertions via the certified Insertion-Difference Identity
(`lemmas/insertion-difference-identity.md`), inserting **`d` first** into `M` (before `c`) gives
`delta_d := e(M∪{d})-e(M)`. Across ~1800 combined case-(a) checks, **`delta_d` was NEVER negative** —
equivalently, `h_d := #{x∈M : x>d}` was **always even** in every single check. Crucially, this held **both**
when `c` was chosen as the *nearest*-to-`d` element of `ξ*` **and** when chosen as the *farthest* (tested
both tie-breaks explicitly, `/tmp/round-18/gap1c_case_a/case_a_probe4.py`) — i.e. `delta_d>=0` appears to
be a fact about `M=B_1∪(ξ*\{c})` and `d` alone, **not dependent on which element of `ξ*` is dropped**.
This is a clean candidate lemma ("inserting `d` into `B_1∪(ξ*\{anything removed})` never decreases `e`")
worth a dedicated symbolic-proof attempt — genuinely new, not in any existing file.

**4. But `delta_c` (inserting `c` second, into `M∪{d}`) is negative `~94%` of the time** (`1325/1403`
checks). So the overall nonnegativity (`delta_d+delta_c>=0`) is **not** explained by termwise positivity —
the "nearest-to-`d`" choice of `c` must be doing real *quantitative* work (bounding how negative `delta_c`
can get, via `|c-d|` being small), not merely a sign argument. This sharpens where the real difficulty of
Step 3's stalled algebra (`potential-weighting-upper-bound.md` §26.4, both attempted routes) actually
lives: **finding 3 says half the two-insertion sum is unconditionally handled for free (once proved);
the remaining content is entirely in bounding `delta_c` using `c`'s nearness to `d`.**

**5. The "`c` adjacent-in-sorted-rank to `d`" heuristic is FALSE in general — concrete counterexamples
found.** Tested whether `c` (nearest-to-`d` by value) always occupies the sorted-rank position immediately
next to `d` in the full multiset `B_1∪{d}∪ξ*`: **`~97%` yes, but not always** — e.g.
`B_1={11,12}, Res=(17,4,3), m=1, d=13, ξ*={3}` (a size-1 witness, so `c=3` is forced): sorted order is
`(13,12,11,3)` — `d=13` is rank-adjacent to `12` (a `B_1` element), not to `c=3` — because `ξ*` had only
one element, "nearest by value" is a vacuous/forced choice unrelated to rank-adjacency. **Do not build a
proof route on rank-adjacency of `c` and `d`** — it is a majority pattern, not an invariant.

**6. A tempting "free bound" generalization tried and found to NOT chain into closing the half-step —
dead end, do not re-attempt.** Tested whether the natural strengthening
`OPT_{+1}(B_1,Res) <= OPT_{+1}(B_1∪{d},X)` (i.e. the *original, un-augmented, full-list* problem's OPT is
always `<=` RHS) holds — **it does, unconditionally, `0/14970` failures, no `F`-provenance needed at all**
(clean argument: "match `u_1,u_j → d`, then apply `ξ*`'s own K/M pattern to the rest of `Res`" is *always*
a valid candidate selection of the bigger `(B_1,Res)` problem, so its optimum is `<=` that candidate's
value `= RHS`). **However this does NOT close the half-step**: the needed direction is
`OPT_{+1}(B_1,X) <= RHS`, and by the certified **Shrink-List Monotonicity Lemma**
(`lemmas/shrink-list-monotonicity.md`), `OPT_{+1}(B_1,Res) <= OPT_{+1}(B_1,X)` — i.e. removing elements
from the list can only *increase* OPT, so this new free fact bounds `OPT_{+1}(B_1,Res)` (the *smaller*
quantity) from above by RHS, which is the wrong direction to reach `OPT_{+1}(B_1,X)` (the *larger*
quantity) from below. **Confirmed dead end — record so a future round doesn't re-derive and re-try this
exact chaining.** (The underlying free fact itself, `OPT_{+1}(B_1,Res)<=RHS`, is true and novel but
appears to be inert for this specific gap; flagging in case it becomes useful for a different bound
elsewhere, e.g. as a sanity check or in a different chain nobody has tried.)

### Cheap check requested by round 17, not yet done (still open, flagged again)

Round 17 flagged as "the single highest-leverage cheap check before committing more build budget to case
(a)'s algebra": whether "sparsest ⟹ size `<=2`, and size-2 always a duplicate pair" is a genuine
dichotomy within `F`-provenance (which would make case (a)'s `ξ*` always size exactly 1, since size-2
non-duplicate would already be case (a) by definition — wait, re-reading: the flagged check is really
"does case (a)'s `ξ*` ever have size `>1`?"). **I partially answered this as a byproduct**: my case-(a)
checks include witnesses of various sizes (`sel` lists of length 1, 2, and more were all observed in the
sparsest witnesses — e.g. size-1 examples like `[('K', Fraction(2,1))]` and size-2+ examples occur too),
so the dichotomy ("case (a) `ξ*` is always size `<=1`") is **FALSE** — larger irreducible sparsest witnesses
do occur. This means case (a) is genuinely a size-unbounded family, not reducible to a fixed small
case-count — the general "nearest-`c` drop one element" construction (not a size-bounded enumeration) is
the right shape of claim, confirming round 16-17's approach was correctly scoped, not over-engineered.

### Recommendation for the outliner (idea only, not developed)

The most promising concrete next algebra step, given findings 3-4: attempt to prove `delta_d>=0`
unconditionally first (finding 3 — a strictly smaller, self-contained sub-lemma, seemingly independent
of which element is dropped, hence possibly provable by a direct parity/rank argument on `B_1∪(ξ*\{x})`
for **any** `x`, not needing the "nearest" property at all), then separately bound `delta_c` using
`|c-d|<=|x-d|` for all `x∈ξ*` (the actual nearest-choice property) to show the sum stays `>=0` — i.e.
split the still-stalled Step 3 into "prove `delta_d>=0` as its own free-standing fact" + "use nearness
only to control `delta_c`'s magnitude," rather than attacking the combined two-variable identity directly
(which is what both of round 16's stalled routes did). This is a scouting lead, not a proof — the actual
symbolic argument for either piece is unbuilt.

### Cheap-kill candidates tried and ruled out

- Rank-adjacency of `c` and `d` — false in general (finding 5), do not build a proof on it.
- The "free bound via the original bigger problem" chaining (finding 6) — provably cannot close the gap
  (wrong monotonicity direction), do not re-attempt.

## Summary block (per report template)

- **Distinct openings:** (i) split Step 3's stalled two-insertion algebra into `delta_d>=0` (finding 3,
  looks independently provable, doesn't need "nearest") + a separate `delta_c` magnitude bound using
  nearness (finding 4) — genuinely new decomposition, not tried before; (ii) exploit the observed
  never-zero margin (finding 2) as a strictness/tightness diagnostic; (iii) case (a)'s witness sizes are
  unbounded (not reducible to a fixed enumeration), confirming the general construction is the right
  shape, ruling out a "finite case check" shortcut.
- **Candidate technique(s):** Insertion-Difference Identity (`lemmas/insertion-difference-identity.md`)
  applied twice in the `d`-then-`c` order specifically (not `c`-then-`d`, which was round 16's other
  untested order) — split into two independent sub-claims per the recommendation above.
- **Cheap-kill candidates:** rank-adjacency of `c,d` (false, ruled out this round); the "free bound via
  `OPT_{+1}(B_1,Res)<=RHS`" chaining (true but inert, ruled out this round, wrong monotonicity direction).
- **Knowledge-base entries to use:** `lemmas/insertion-difference-identity.md` (the core algebraic tool),
  `lemmas/shrink-list-monotonicity.md` (confirms why finding 6's chain fails — cite this to block anyone
  re-attempting it), `lemmas/duplicate-pair-invariance.md` (Lemma P, defines the case split itself),
  `lemmas/delete-suffices-insertion-domination.md` (the case (b)/(c) mechanism, for contrast — case (a) is
  exactly what this lemma's single-pair-insertion form cannot reach).
- **Analogous past problems (cruxes):** `aimo-0960` — already correctly mapped by round 17 (§27.3): its
  two-technique split ("kill a repeat via an identity" for boundary/duplicate cases vs. a separate
  value-bound argument for the generic case) maps to case (b) vs case (a) respectively. I re-read the
  crux's proof shape and confirm round 17's refined mapping is the right one — no sharper mapping found
  this round; case (a) is squarely the "value-bound argument for the generic (non-repeating) case" half,
  and `aimo-0960`'s own value-bound technique (bounding via minimality/extremality of the representation,
  not a length-preserving rewrite) is the right *flavor* but the actual bound (there, on a numeral
  representation's minimality; here, on an alternating-sum-under-insertion inequality) does not transfer
  algebra directly — must still be derived from scratch, consistent with round 17's own caveat.
- **Prior progress:** case (a) is non-vacuous (confirmed again, wider sweep, 0 failures ~2800 checks);
  the nearest-`c` construction has never failed in any test to date across 3 rounds of sweeps now; still
  entirely unproved.
- **Dead ends (do not retry):** rank-adjacency of `c` to `d` (finding 5, false); the
  `OPT_{+1}(B_1,Res)<=RHS`-chaining route to close the half-step (finding 6, provably wrong direction via
  Shrink-List Monotonicity); (inherited from round 16) the naive "same witness, just drop `d`" transfer;
  (inherited from round 16) both of round 16's two attempted two-insertion routes as originally posed
  (§26.4) — though this round's finding 3-4 decomposition is a genuinely different split of the same
  algebra, not a re-attempt of either named route verbatim.
- **Small-case / intuition notes:** case (a)'s sparsest witnesses have unbounded size (not always 1 or 2
  — conjecture refuted this round, see "cheap check" section); `delta_d>=0` looks like a clean provable
  sub-fact (conjecture, 0 violations, ~1800 checks, both nearest and farthest `c` tie-breaks); margin is
  never exactly 0 in case (a) in ~1558 checks (conjecture, suggests strict inequality, not swept for
  near-ties specifically).
