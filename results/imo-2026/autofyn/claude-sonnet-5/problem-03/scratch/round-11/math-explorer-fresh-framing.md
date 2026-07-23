# math-explorer — fresh-framing scouting report (round 11, IMO-2026-03)

**Mandate:** find a route to the whole problem that does NOT go through the
D/M-operation-sequence / Lemma-G/P reduction, since all 3 live approaches
(`dyadic-cascade-induction`, `potential-weighting-upper-bound`,
`concavity-minimax-duality`) route through it and have shared the "Match-Recovery
Lemma" wall (`OPT(Y,p-1)=NC(Y,p-1)`) for 3 rounds. Two sibling explorers this round
are patching *that* gap from inside the machinery; I was explicitly asked not to.

**Bottom line up front.** I seriously tried three candidate "fresh" reformulations.
One (concavity/LP-duality) is **already dead** — I independently rediscovered and
extended the existing certified counterexample. Two others (a "layer-cake
toggle-pair" measure-theoretic recasting, and a "merge-tree/pairwise-difference"
recasting) are **new-looking but, on careful analysis, mathematically isomorphic**
to the already-existing D/M + Lemma-P machinery — pursuing either as a "genuinely
different" attack would very likely just re-derive the same wall in new notation,
so I do NOT recommend dispatching a builder on either as a *replacement* framing.
The one candidate I found that is a **genuinely different technique class**, not
tried by any live approach, is a **probabilistic/averaging argument** (crux
`aimo-0198`'s `min(A,B) ≤ (A+B)/2` device) — untested, flagged honestly as a lead,
not a result. I also ran independent computational sanity checks (fresh code, not
reusing the population's harness) confirming Lemma G and the n=1,2,3 target values,
and an external-source search that came back unreliable/unusable (details below,
so nobody wastes a round on it).

---

## 1. Concavity / LP-duality-on-the-opening — ALREADY DEAD, re-confirmed and extended

**Idea tested:** since `h(A,m) := min over D/M sequences of e(final state)` is a
minimum of functionals of the opening `A`, is `h(·,m)` concave on the simplex of
sorted openings? If so, bounding `h(A,m) ≤ e_m·S(A)` for every `A` would reduce to
a KKT/subgradient check at the single point `A=D_m` — a textbook convex-analysis
technique, genuinely different in kind from the population's combinatorial-matching
approach.

**Check performed.** I wrote an independent exact-`Fraction` BFS (`h(A,m)`, full
enumeration of legal D/M sequences up to length `m`, memoized) from scratch and
validated it against the certified values: `h(D_1,1)=1/3`, `h(D_2,2)=1/7`,
`h(D_3,3)=1/15` — exact matches. I then tested concavity directly: for random pairs
`A,B` (`m=1,2,3`), compared `h(midpoint,m)` against `(h(A,m)+h(B,m))/2`.

**Result: concavity is FALSE**, with 10 violations found in 120 trials (`m=2,3`),
e.g. `m=2`: `A=(7/18,1/3,5/18)`, `B=(2/3,2/9,1/9)`, `h(A)=1/18`, `h(B)=1/9`,
`h(midpoint)=1/18 < (1/18+1/9)/2 = 1/12`.

**This is not new** — it is the same phenomenon already certified in
`lemmas/non-concavity-of-g-at-n2.md` (round 3, a different exact counterexample at
`n=2`). My finding independently reconfirms that result and **extends** it to
`m=3`, but provides **no new leverage**: global concavity of the true value
function was already a known, certified dead end. **Do not propose a
concavity/KKT-based approach again in any dressed-up form** — this closes the loop
on that specific idea with fresh evidence.

---

## 2. Layer-cake "toggle-pair" reformulation — verified correct, but isomorphic to existing machinery

**Idea.** The already-certified Layer-cake identity (`lemmas/layer-cake-and-noncrossing-independence.md`)
writes `e(M) = measure{t : N(t) is odd}` where `N(t) = #{pieces > t}`. I found (and
computationally verified, see below) a sharper, previously-unstated refinement:

> **Toggle-pair fact (verified, not previously on file).** If a piece of length `a`
> is cut into `(b, a-b)` with `b ≤ a-b`, then `N(t)` is **unchanged** for
> `t ∈ [b, a-b)`, and its **parity flips** on exactly the two disjoint,
> equal-length intervals `[0,b)` and `[a-b, a)` — nowhere else.

Verified by direct computation (`/tmp/round-11/work/toggle_check.py`): built `N(t)`
explicitly before/after a cut on two concrete configurations and confirmed the
predicted toggle regions match exactly (0 mismatches across all breakpoints
tested). This is a genuinely clean, checkable fact.

**Why it doesn't open new ground.** Chasing the consequence: since every cut's
"bottom" toggle interval `[0,b)` is anchored at the value-axis **origin**
regardless of which piece is cut, the *cumulative* effect of several cuts' bottom
intervals is the XOR (symmetric difference) of several intervals sharing a left
endpoint — and the parity pattern of a union of origin-anchored intervals of
lengths `b_1,...,b_r` is *exactly* `e(b_1,...,b_r)` again (the same alternating-sum
recursion, one level down). This is not a coincidence: it is a re-derivation, via
measure theory, of exactly the Lemma-P cancellation mechanism that the D/M
formalism already encodes combinatorially. The "top" toggle intervals
`[a-b,a)` (anchored at each piece's own current length) reproduce the D/M
"delete/match" bookkeeping the same way. **Conclusion: this reformulation is
elegant but mathematically equivalent in content/power to the existing D/M +
Lemma-P machinery** — a proof built on it would very likely hit the identical
Match-Recovery wall in different notation. I do not recommend it as a
replacement framing; it might be worth keeping as an alternative *expository*
lens if a future round wants a cleaner write-up of already-proved facts, but it is
not a new attack surface.

---

## 3. "Merge-tree / repeated pairwise-difference" reformulation — also isomorphic

**Idea.** In the tight case (`k=m+1`, full budget used), XY's process reduces `k`
active values to exactly 1 via `m=k-1` D/M operations. This looks exactly like the
classical competition trope "repeatedly replace two numbers by their difference
until one remains — what's the extremal/reachable final value" (Euclidean-algorithm/
continuant-polynomial flavor; the dyadic sequence `2^i` is the classic
"worst case" configuration for such processes, structurally resembling why
Fibonacci numbers are worst-case for the Euclidean algorithm's step count). I
checked whether this is a *different* external body of technique to import.

**Finding.** The "always merge/match the top two" and "always delete-or-match by a
threshold rule" policies are precisely Rule 1 / Rule 2, **already built and
falsified** in `potential-weighting-upper-bound.md` (exact counterexamples at
`m=2,3`). The token/signed-subset-sum invariant that would make a
"Euclidean-algorithm-style extremal" argument work is *already* the mechanism
behind the certified Superincreasing No-Early-Zero Lemma
(`lemmas/superincreasing-no-early-zero.md`). So this framing, too, collapses into
already-explored (and partly already-dead) territory. **Not a new lead.**

---

## 4. A genuinely untried technique class: probabilistic / averaging argument

Querying the crux corpus's `probabilistic-method` subtopic (combinatorics; only 4
cruxes exist, so I read all of them) surfaced `aimo-0198` (IMO 2012 P3, the "Liar's
guessing game"), whose load-bearing move is:

> "Bound a greedy minimizer's outcome by the average of its two available options,
> `min(A,B) ≤ (A+B)/2`, to get a clean recursive bound on the potential."

Concretely there: the adversary picks whichever of two successor potentials is
smaller; instead of tracking *which* is smaller (a case split), the proof bounds
the minimum by the **average** of the two, which satisfies a clean **sum identity**
(`φ₁+φ₂ = λφ + (n+1)`) that closes the induction without ever identifying the
adversary's actual choice.

**Why this is a genuinely different technique for our problem, not a relabeling.**
Every live approach's stuck point is of exactly this shape: `OPT(Y,b) = min(DELETE,
KEEP, min_j MATCH_j)`, and the population has repeatedly tried to pin down *which*
branch (or which partner `j`) is optimal — via exact combinatorial recovery
(Match-Recovery Lemma), via greedy rules (Rule 1/2, all falsified), via
lookahead-strengthened induction (also falsified, `potential-weighting-upper-bound`
§5). None of these attempts try the `aimo-0198` move: bound the **minimum** by a
**weighted average over multiple candidate branches** and show the average alone
already satisfies the target via a clean sum/telescoping identity, *without ever
identifying the arg-min*. This is a genuinely different proof architecture
(probabilistic/averaging, not exact-matching or greedy-policy).

**Status: I did not verify this closes the gap** — I only confirmed (a) the
technique is absent from all 3 live approach files and the certified lemma set,
and (b) it is a real, previously-successful IMO-level technique for structurally
analogous "adversary picks the better of several options" recursions. A quick
first computational test to try before committing a full round: for the known
hard instance `Y=(39,36,30,28,22,18,14)` at `b=p-1=6`, compute the exact values of
DELETE, KEEP, and all `MATCH_j` branches and check whether any simple weighted
average of them (not the min) already sits at or below the target via a clean
closed-form identity in `Y`'s entries — analogous to the crux's `φ₁+φ₂` identity.
I ran out of round budget to complete this numerically myself; I flag it as the
single most promising concrete next experiment for a future round that wants a
technique genuinely orthogonal to Match-Recovery-style exact recovery, while still
targeting the same necessary fact (so it is *not* a "same-gap" patch in the sense
CLAUDE.md warns against — it is a different proof *method* aimed at the same
target, which is fine since it doesn't presuppose the exact-matching machinery at
all).

---

## 5. External-source check — inconclusive, flag as unreliable, do not repeat

Per the dispatch's suggestion to check whether the closed form matches a known
named result, I attempted to locate the actual IMO-2026 P3 source/solution
(the `problems.jsonl` entry cites `artofproblemsolving.com/community/
c6h3866199_chu_han_war`, IMO 2026). `WebFetch` on the AoPS URL and on
`artofproblemsolving.com/wiki/...` both returned **HTTP 403** (blocked). A fetch of
`imo-official.org/problems.aspx` returned a suspiciously fluent but **generic,
non-specific** summary that I believe is a hallucinated confabulation by the
fetch-summarizer model (it added no verifiable detail beyond what's already in
`problems.jsonl`, and a follow-up fetch of a plausible Evan Chen notes PDF for
"IMO-2026" 403'd, inconsistent with the first "success"). **Do not trust or cite
this fetch result in any future round** — I am flagging it explicitly so nobody
treats it as a real external solution lead. Net: no usable external confirmation
either way; this avenue is exhausted for now (AoPS blocks scraping).

---

## 6. Computational sanity checks (n=1, 2, 3), independent code

All in `/tmp/round-11/work/` (`dm_bfs.py`, `concavity_test.py`, `toggle_check.py`,
`search_beat_dyadic.py`, `lemma_g_check.py`), fresh implementations, not reusing
any existing harness in `results/imo-2026-03/`.

- **Lemma G (greedy reduction) independently reconfirmed**: brute-force exact
  backward induction on 300 random small multisets (`k=0..6`) vs. the odd-rank-sum
  formula — 0 mismatches. (This lemma is already fully proved and certified; not
  claiming anything new, just directly satisfying the dispatch's "verify
  independently" instruction.)
- **`n=1,2,3` target values reconfirmed** via an independent exact D/M-BFS solver:
  `h(D_1,1)=1/3`, `h(D_2,2)=1/7`, `h(D_3,3)=1/15` — matches
  `c(1)=2/3,c(2)=4/7,c(3)=8/15` exactly.
- **Bounded adversarial search for an opening that beats `D_n`** (the thing that
  would actually refute the conjecture): 400 random trials at `m=2` (max found
  `h=1/9 < 1/7`), 250 random trials at `m=3` (max found `h=1/18 < 1/15`), plus 7
  structured/near-uniform/near-tied configurations at each — **no violation found**
  at either `m`. This is consistent with (and does not exceed) the extensive
  existing population testing (`potential-weighting-upper-bound.md` alone ran
  200,000+ trials at `m=3`); I present it only as an independently-coded
  reconfirmation, not a new result, and note honestly that this uses the D/M
  formalism as a verification *tool* (legitimate per the dispatch's own framing
  — it explicitly permits reusing certified lemmas as tools) even though the
  broader mandate was to avoid it as a *proof strategy*.

---

## Recommendation for next round

1. **Do not** dispatch a builder on concavity/KKT (dead, doubly-confirmed), the
   toggle-pair reformulation, or the merge-tree/Euclidean framing (both isomorphic
   to existing machinery) as "genuinely new" approaches — they would relabel
   existing ground per CLAUDE.md's single-gap-trap warning.
2. **Do** consider a small, targeted experiment (not a full new approach slug yet)
   testing the `aimo-0198`-style averaging bound on the Match-Recovery Lemma's
   DELETE/KEEP/MATCH_j branches, as the one genuinely untried technique class
   surfaced this round. If a future explorer/outliner wants to open a 4th
   approach slug, this — not another D/M variant — is the most defensible
   "genuinely different" candidate I found.
3. Treat the external-source lookup as closed/exhausted (blocked + unreliable);
   don't re-spend a round on it.
