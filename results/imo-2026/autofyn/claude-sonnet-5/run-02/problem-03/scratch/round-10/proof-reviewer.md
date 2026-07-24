# Round 10 proof-review — imo-2026-03

Reviewed both round-10 builds. For every load-bearing new claim I wrote a
**fresh, independent** verification script (not the builders' own), per
`/tmp/memory/proof-reviewer.md`'s standing rule. In two cases my own first
draft had a real bug that produced spurious "violations"; I diagnose those
below and show the corrected checks pass. In one case (Route A's new
lemma) my independent check found a **genuine gap in the statement** (not
in the underlying mechanism) that the builder did not catch.

All scripts are in `/tmp/round-10/*.py`.

---

## 1. `greedy-halving-adversary` — verdict: **CHANGES REQUESTED** (Status: partial)

### What was claimed
- **Lemma 23** (general ladder dominance): $p_i>\sum_{j>i}p_j$ and
  $p_i=2p_{i+1}$ for every level $i$.
- **Lemma 24**: $p_2-s=f(n)$, $s=\mathrm{Total}(\{p_3,\dots,p_{n+1}\})$.
- **Proposition 25**: closes one branch of $(\dagger)$'s $p_2$-cut
  complement **unconditionally** ($\ell=1$ split of $p_2$ with residual
  $w'\ge p_3$, $p_3$ itself untouched).
- **Proposition 24**: closes the $v\in[s,p_2)$, $p_2$-untouched sub-branch
  of the $v<p_2$ case, conditional on $(\star_{n-2})$ (unconditional
  $n\le4$).
- **Sub-target 3** ($\ell(F)$-Collapse Lemma): honestly reported as
  attempted, not proved; only numerically supported (two independent
  search methods, zero violations, $n\le6$).

### Independent verification
- Lemma 23, 24: re-derived from the closed form $p_i=2^{n+1-i}f(n)$ and
  checked exactly for $n=1,\dots,8$ (`verify_ladder_lemmas.py`) — exact
  match, no gap.
- Proposition 25: my first script (`verify_prop25.py`) lumped
  $\{p_4,\dots,p_{n+1}\}$'s total into one arbitrary composition instead of
  independently splitting each original piece — this is **not** a legal
  refinement (Xiang Yu can only cut within existing piece boundaries, never
  create a fragment spanning two original pieces). Once corrected
  (`verify_prop25_v2.py`, per-piece independent partitioning via
  `legal_refinement`), 32,000 trials across $n=3,\dots,6$: **zero
  violations** of $A(G')\le p_2-f(n)$.
- Proposition 24: same piece-boundary bug in my first draft, **plus** a
  second bug — my first draft let the tail refinement $G'$ use up to
  $n-2$ cuts regardless of how many cuts $F$ itself used, but the claim's
  hypothesis is that $G'$'s budget is $n-2$ only in the tightest case
  ($F$ uses its minimum of 2 cuts); if $F$ uses more cuts, the true legal
  tail budget is smaller, and testing an over-generous tail budget produces
  illegal ("cuts exceed $n$ total") instances outside the claim's scope.
  Once both bugs are fixed (`verify_prop24_v3.py`: per-piece partitioning
  + correct $F$-vs-$G'$ cut-budget coupling), 16,000 trials across $n=3,4$:
  **zero violations**. This is exactly the same kind of near-miss the
  builder itself flagged (an earlier uncapped version of its own check
  found spurious violations before capping the budget) — I independently
  rediscovered the same class of pitfall from scratch, which corroborates
  that the cut-budget hypothesis really is load-bearing, not cosmetic.

### Scoping check
Both propositions' "what remains open" sections match what I found: Prop
25 only covers $w'\ge p_3$, $p_3$ untouched, $\ell$(p2-split)$=1$; Prop 24
only covers $s\le v<p_2$, $p_2$ untouched. Neither is overclaimed beyond
its stated branch. Sub-target 3 is correctly reported as unproved (the
attempted "merge the two residuals" exchange move is genuinely not
mass-preserving, as the file explains — I agree this rules out that
specific move, though it does not rule out every possible exchange move).

### Verdict
Real, correctly-scoped, independently-corroborated progress; the central
lower-bound gap (general $\ell(F)\ge2$, the $v<s$ complement, remaining
$p_2$-cut branches) remains open. **Status: partial. CHANGES REQUESTED.**

### Lemma certification
- `general-ladder-dominance` (Lemma 23) — **CERTIFIED**.
- `level-2-dominance-identity` (Lemma 24) — **CERTIFIED**.
- `p2-cut-complement-branch-closure` (Proposition 25) — **CERTIFIED**
  (unconditional, as claimed).
- `v-in-s-p2-closure` (Proposition 24) — **CERTIFIED**, with its
  conditional status preserved (conditional on $(\star_{n-2})$,
  unconditional only for $n\le4$ — do not silently treat as unconditional
  for general $n$).

---

## 2. `lp-duality-certificate` — verdict: **CHANGES REQUESTED** (Status: partial)

### Route B (Iterated Greedy-Peel Construction)
- **Legality + exact-value identity** ($A(M)=v_{\text{final}}$, $\le n$
  cuts): independently re-verified by directly re-simulating the *actual*
  physical cuts (not just the abstract working-set bookkeeping) against a
  direct sort-and-alternating-sum computation of $A$, 3000 random trials,
  $m=2,\dots,7$ — **zero mismatches** (`verify_greedy_peel.py`).
- **Counterexample** ($n=4$ equal-pieces, $\Phi=3/5>16/31=a_4T$):
  independently re-derived exactly, confirmed.
- **Stress-test failure rate**: I ran an independent 2000-trial stress test
  with a *different* sampling method (uniform random compositions rather
  than the builder's integer-ratio markings) and found **62% failure**,
  vs. the builder's reported 48% — different exact percentage (expected,
  different sampling distribution), but the same qualitative conclusion at
  a similarly large scale: "always match top two" is decisively not a
  universal strategy. This corroborates, independently, that the dead end
  is real and not an artifact of the builder's own search.
- **"Equivalent" → "sufficient" correction**: verified the cited witness
  $M'=\{5,4,4,1\}$ directly: sorted alternating sum $A(M')=5-4+4-1=4$, a
  genuine multi-element odd-run-reduced set, confirming the outline's
  "equivalent" framing was indeed an overclaim and the file's correction to
  "sufficient, not equivalent" is correct.

Both Route B results check out. **Certified**: `iterated-greedy-peel-identity`,
`greedy-top-two-matching-insufficiency` (dead-end record).

### Route A (Simplex Exchange-Smoothing Vertex-Maximization, box constraint dropped)
I ran an independent check: enumerate the lemma's claimed finite vertex
family (as literally stated — pins restricted to $\{\tau_1,\dots,\tau_r\}$,
remaining coordinates all tied to one value) versus a continuum optimizer
(Nelder-Mead from many restarts, cross-checked with random search) over 15
random test cases (`verify_routeA.py`).

**Found a genuine gap**: at $\tau=(3.798,1.115)$, $s=3.053$, $k=3$, the
continuum optimizer finds $F=\{2.0315,1.0215,\approx0\}$ with
$E=3.053$, strictly beating the literal-statement vertex family's best
candidate ($E=2.23$). Tracing the actual exchange-smoothing dynamics
(pushing the two tied-parity free coordinates to their boundary) shows the
*true* maximizer is $F^\dagger=\{3.053,0,0\}$ — two coordinates pinned at
$0$. This **is** a legitimate output of the lemma's own *proof* (which
works with reference set $R=\{0,\tau_1,\dots,\tau_r\}$ throughout,
explicitly listing "$f_j$ hits $0$" as a boundary case), but it is **not**
covered by the lemma's *literal statement*, which never adds $0$ to the
allowed pin set — so the statement (and its A.2 restatement in the vertex
family for "cut $p_1$ only") is imprecise/incomplete as written.

I re-ran the same 15 test cases with $0$ added to the candidate pin set
(`verify_routeA_fixed.py`): the corrected vertex family's predicted maximum
matched the continuum optimizer in all 15 cases (differences $\le10^{-15}$,
numerical noise). So the fix is simple and the underlying mechanism is
sound — only the statement needs correcting.

**Action taken**: did **not** certify `simplex-exchange-smoothing-vertex-
maximization` as currently written. Left the file in `lemmas/` with a
detailed correction note (the exact fix: add $0$ to the pin set, and
propagate the same fix to A.2's downstream vertex-family restatement in
the approach file) so the next round can repair and resubmit rather than
re-derive the proof from scratch. This does not retroactively invalidate
anything else in the round — A.3's finite optimization was already
explicitly left open regardless of this lemma's exact statement, and no
claimed-complete result in this round depended on the omitted case.

### Verdict
Real progress on both routes, one genuine dead-end honestly found and
independently corroborated (Route B), and one real statement-level gap
found by the reviewer that the builder missed (Route A) — narrowing but not
closing the general upper bound's $p_1<T/2$ regime. **Status: partial.
CHANGES REQUESTED**, with the explicit correction needed for Lemma A.1 (and
its A.2 restatement) flagged as this approach's most concrete next task.

---

## `current.md` updated

Added the round-10 summary paragraph (before `## Full proof`), Status
remains `partial`. No approach reached `solved` this round; no RETHINK.

## Ranking

Both slugs recorded via `record_outcome` with `outcome=advanced` (round
10) — see notes attached to each ranking entry, summarizing what was
closed/corroborated/found this round for each.

## Files touched
- `/home/agentuser/repo/results/imo-2026-03/current.md` (round-10 summary
  appended, Status unchanged: partial)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/general-ladder-dominance.md` (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/level-2-dominance-identity.md` (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/p2-cut-complement-branch-closure.md` (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/v-in-s-p2-closure.md` (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/iterated-greedy-peel-identity.md` (certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/greedy-top-two-matching-insufficiency.md` (certified, dead-end record)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/simplex-exchange-smoothing-vertex-maximization.md` (NOT certified — correction note appended)
- `/tmp/round-10/verify_ladder_lemmas.py`, `verify_prop25.py`,
  `verify_prop25_v2.py`, `verify_prop24.py`, `verify_prop24_v2.py`,
  `verify_prop24_v3.py`, `verify_greedy_peel.py`, `verify_routeA.py`,
  `verify_routeA_fixed.py` (independent verification scripts)
