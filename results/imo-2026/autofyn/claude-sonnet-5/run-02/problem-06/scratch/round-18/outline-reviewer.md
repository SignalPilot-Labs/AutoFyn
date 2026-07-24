## imo-2026-06 — Round 18 outline review

Read: `/tmp/round-18/proof-outliner.md`, `results/imo-2026-06/current.md`,
`results/imo-2026-06/approaches/n1-periodicity-reconciliation.md`,
`results/imo-2026-06/approaches/self-absorbing-by-construction.md`,
`results/imo-2026-06/approaches/greedy-exchange-cost-potential.md` (Growing-
Constraint Obstruction), `lemmas/vacuous-self-absorption-lemma.md`,
`/tmp/round-18/math-explorer-fresh-framing.md`,
`/tmp/round-18/math-explorer-ntbt-h2.md`, `/tmp/round-18/math-explorer-audit-insurance.md`.
Ran independent numeric checks (scripts kept at `/tmp/round-18/sim_triangle.py`,
`sim_triangle2.py`, `spotcheck_255255.py`).

---

### 1. `triangle-consistency-pigeonhole` (new) — **CHANGES REQUESTED**

**Not a repackaging of the dead Single-Witness/Growing-Constraint Obstruction
family.** I reread the certified Growing-Constraint Obstruction
(`greedy-exchange-cost-potential.md` lines ~1372-1386, ~2313-2320): its shape
is "the illegality-witness index `i(c)` for a *skipped candidate* ranges over
an unboundedly growing pool" — a fact about the successor-transport reduction,
not about gcd-pigeonholing two fixed witnesses of the same persistent type.
The new mechanism (fix TWO indices `m_A, m_A'` of type A once and for all, then
double-pigeonhole a fixed pair of divisor sets against `X_B`) has no structural
overlap with that obstruction — it neither manufactures a growing witness pool
nor needs the successor-transport machinery at all. This is a genuinely
different mechanism shape, matching the fresh-framing explorer's claim.

**However, the outline's own proposed cheap-kill test is under-specified in a
way that matters, and I ran it myself (per memory rule 21) — the result is
informative but not yet the real test.** I computed `d1, d2` via nested
pigeonhole (using the modal/most-frequent divisor as the infinite-fiber proxy)
on `a_1=175` and `a_1=4807`, using ordinary **base types** (w.r.t. `Q` only).
In both cases `gcd(d1,d2) > 1` held **robustly across every witness pair
tested** (28/28 pairs on 175, 15/15 on 4807) — case (i) of the outline's Step 6
occurs, cleanly. But in both cases the recruited common prime (3 for `a_1=175`,
2 for `a_1=4807`) is a small prime already known, by simpler certified
machinery (Confined-GCD Lemma / Singleton-Side FAH / the Finite Core
Theorem's own collateral-recruitment), to divide most terms generically — this
is testing FAH at the level of **base types**, which is already the *easy*
regime the workspace resolved by round 8-9 (Singleton-Side FAH). It is not
yet a test of the actually-hard **rogue extended-type pairs**
(`|F'|,|F''| ≥ 2`, measured at the *properly recruited* terminal core, per
memory rules 18/19) that the whole crux is stuck on. My test therefore neither
confirms nor refutes the mechanism at the point that matters — it only shows
the pigeonhole *machinery itself* is well-behaved on easy cases, which was
never in doubt.

**Required correction to the outline before the builder proceeds (this is the
actual gap, not a rejection):** the cheap-kill instructions (lines 92-97) name
seeds 175/4807/11305 but do not specify that `m_A, m_A'` and `X_B` must be
drawn from **extended-persistent types at the fully-recruited core S*** (not
raw `Q`-level base types), and specifically from a **rogue pair** — a
disjoint `(A',B')` with `|F'|,|F''|≥2` already on record for that seed (the
workspace already has these identified for prior rogue-pair work; the builder
must reuse them, not rediscover base-type FAH). Additionally, the builder must
explicitly check that any recruited prime found by Step 6/7 is not already
derivable from the certified Confined-GCD Lemma alone — otherwise "progress"
would just be re-deriving already-known content in heavier notation (the
precise failure mode memory rule 14 warns about). Add this as an explicit
required first checkpoint, ahead of the general proof attempt.

**Verdict:** CHANGES REQUESTED, not RETHINK — the mechanism is structurally
new (confirmed against the dead-mechanism list) and the outline is honest
about the open crux (Step 6/7 is correctly left unproved, not hand-waved).
But the pre-build cheap-kill must be re-scoped to genuine rogue pairs at the
recruited core before the builder invests in the general proof, per the
correction above.

### 2. `self-absorbing-by-construction` (revise) — **APPROVE**

Independently re-verified the round-18 headline correction. I re-ran the
greedy-sequence simulation for `a_1=255255` from scratch (per-prime bitmask
method, different script from the explorer's) out to `n=140000` and confirm
**exactly** the reported occurrence list for the flagged type
`{5,7,11,13,17}`: `n = 27184, 135914` — a clean, independent reproduction (not
a re-trust of the explorer's numbers). The round-17 "unresolved candidate
exception" is legitimately resolved in NTBT's favor; the revision's Step 1
write-up instruction is sound. Step 2 (documenting the H2 counting/pigeonhole
corridor as exhausted in all 3 forms) matches the math-explorer-ntbt-h2 Task 2
analysis, which I independently checked reduces correctly to either the
already-proved `N(S_k)`-equivalence (round 17's outline-reviewer one-line
proof) or a circular/vacuous target — no gap found in that reasoning either.
Step 3 (cross-reference only, no duplicate content) is correctly deferred to
the sibling approach. Watch-out clause (don't overclaim "zero counterexamples"
as proof-strength) is present and correct.

**Verdict:** APPROVE — bookkeeping/correction round, low risk, independently
confirmed.

### 3. `prime-power-seed-periodicity-theorem` (new) — **APPROVE**

Checked against the dead/duplicate concern directly: `even-a1-full-periodicity-
theorem.md` proves `a_n=a_1+2(n-1)` for ALL even `a_1` (not just powers of 2),
so it is strictly disjoint in general from odd prime powers `p^k`, `p≥3` — no
overlap except the honestly-disclosed `p=2` case, which the outline correctly
says to cite as a corollary, not re-derive. The round-18 audit-insurance
explorer independently confirmed this exact claim ("already implicit ... never
separately certified") via its own from-Free-Facts derivation, matching the
outline's skeleton line for line. The induction skeleton (steps 1-3) is
elementary and I re-checked it: for `2≤j≤p-1`, `a_n+j ≡ j (mod p)` with `p|a_n`
is correct, and since `Q={p}` is `a_1`'s only prime, `gcd(a_n+j,a_1)=1` follows
immediately from `p∤(a_n+j)` — sound, no gap. This is genuinely new
certifiable content (a previously-unwritten lemma file), not a duplicate.

**Verdict:** APPROVE — complete, self-contained, elementary; low risk, real
content (new certifiable lemma extending the already-solved-subfamily
package).

### 4. `n1-periodicity-reconciliation` (advance) — **APPROVE**

Both new findings are concrete and checkable, and I independently reproduced
the core logic: the "does `p|a_1` trivialize FAH for odd `p`" claim collapses
because the `p=2` mechanism's proof relies on there being **zero** intermediate
residues between "definitely illegal" (`a_n+1`) and "next multiple of p"
(`a_n+p`) — true only when `p=2` (`p-2=0`); this is a correct, checkable
structural fact, not an assertion. The `a_1=15,45` example is exactly the kind
of concrete counterexample memory rule 25 asks for. The `|Q|=2` "not
tractable" finding reproduces the workspace's own long-standing canonical hard
seeds (187, 209, 221, 247) — consistent with 12 prior rounds' data, not a new
risk. Both are honestly filed as negative/documentation findings, not progress
toward H1/H2 themselves, matching the file's own Open-gaps section. No
overclaim.

**Verdict:** APPROVE — genuine permanent narrowing (prevents future rounds
from re-attempting two now-confirmed dead generalizations); Status correctly
stays `partial`.

---

### Diversity check

The four approaches split cleanly across disjoint scopes: (1) is the sole
attack on H1/FAH this round, via a genuinely new mechanism family (confirmed
distinct from all 18+ dead ones); (2) and (4) are bookkeeping/documentation on
H2 and the reduction chain respectively, not new proof routes; (3) is an
elementary, fully independent side-theorem outside the FAH/H2 machinery
entirely. No two approaches share the same open gap this round — the
single-gap-trap concern does not apply. The field is not over-concentrated on
one framing; (1) is appropriately the only live H1 shot, consistent with the
fresh-framing explorer's finding that no second new corridor exists this
round.

---

### Ranking

Registered `triangle-consistency-pigeonhole` and
`prime-power-seed-periodicity-theorem` (both new slugs this round);
`self-absorbing-by-construction` and `n1-periodicity-reconciliation` are
established slugs, updated via `update_ranking` against each other and
anchored to `even-a1-full-periodicity-theorem` (comparable-quality prior
APPROVE) and `core-growth-monotonicity` (comparable-difficulty open H2
attempt). Result (best-first): `n1-periodicity-reconciliation` (1622, most
central/audited this round), `even-a1-full-periodicity-theorem` (1515, held
constant as an anchor), `prime-power-seed-periodicity-theorem` (1514, new,
anchored to its close analogue), `self-absorbing-by-construction` (1514),
`triangle-consistency-pigeonhole` (1457, new and speculative — correctly
below the established approaches given its crux step is still open and its
cheap-kill needs re-scoping), `core-growth-monotonicity` (1453, unchanged
H2 plateau).

---

build set: triangle-consistency-pigeonhole, self-absorbing-by-construction, prime-power-seed-periodicity-theorem, n1-periodicity-reconciliation
