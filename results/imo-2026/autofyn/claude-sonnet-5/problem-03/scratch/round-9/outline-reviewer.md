## imo-2026-03 — outline review, round 9

Scope per dispatch: 3 approach files revised (`dyadic-cascade-induction`, `potential-weighting-upper-bound`,
`concavity-minimax-duality`); `elementary-exchange-smoothing` untouched. Independently re-verified all
claims against the actual files (not the outliner's own summary), plus fresh bounded computation
(`/tmp/round-9/work/verify_p12.py`, `/tmp/round-9/work/verify_p14.py`).

---

### 1. `dyadic-cascade-induction` — scope-correction note (lines 4–38)

**Claim under test:** "general n≥4 is not a separate frontier" — Case (i) and Case (ii) of the
upper-bound induction share one joint strong induction on `m`, so closing the sibling's aggregated
lemma once closes every `m`/`n` simultaneously.

**Independently re-verified, sound, not an overclaim.** Traced §2's induction statement (line
652–663: "Claim (Level m, for every m≥0)... any k≤m+1 pieces a1≥…≥ak≥0" — this is ONE joint claim
covering both cases, not two separate per-case claims) and §2d's proof (line 762–781: "By induction
on m... using the strong induction hypothesis — both forms (A) and (B) — at level m-1... By the
strong induction hypothesis at level m-1 applied to the residual, both forms hold"). This confirms
the residual after a Case-(i) bisection is an *arbitrary* multiset at level m-1 (not guaranteed to
itself be a Case-(i) configuration), so Case (i)'s closure at level m genuinely depends on the FULL
joint IH (forms A and B, i.e. both cases) at level m-1 — exactly as the round-9 note claims. This is
consistent with the round-3 reviewer's original finding (see run_state.md Round 3 entry) that Case
(i) is not independently generalizable.

Critically, the round-9 note does **not** overclaim: it correctly states this only as a conditional
("the moment potential-weighting-upper-bound's aggregated lemma closes... the outer induction closes
for every m simultaneously") and does not assert Case (i)/Case (ii) are closed for all m today. It
correctly identifies `current.md`'s existing "n≥4 remains essentially untouched" item as stale
phrasing to be corrected once the sibling lemma closes — this is a narrative fix, not new math, and
introduces no new gap. No 5th slug was opened (confirmed: only 4 files exist in `approaches/`,
`elementary-exchange-smoothing.md`'s mtime is untouched this round). Verdict: **sound, no overclaim.**

**Verdict: APPROVE** (no new mathematical content to verify beyond the narrative; the narrative
itself is accurate). No concrete builder task exists in this file this round beyond waiting on the
sibling lemma or searching (with zero current lead) for an alternate upper-bound mechanism — see
build-set discussion below.

---

### 2. `potential-weighting-upper-bound` — new §12 (recursive induction on `p` + Full-Slack Insertion
Lemma)

**Independently reimplemented `INSERT_OPT`/`INSERT_NC`** from scratch (exact Python `int`, full
exhaustive enumeration over all (K,D,M) selections, no heuristics — `/tmp/round-9/work/verify_p12.py`)
per §11.1's precise definitions, and tested the new §12.1 **Full-Slack Insertion Lemma**
(`INSERT_OPT(v†,Z,|Z|) = INSERT_NC(v†,Z,|Z|)`, no inside/outside split) on fresh random trials:
- q=0..6: 420 trials, 0 failures.
- q=7 (pushed one level beyond the explorer's own q≤6 sweep per house rule): 30 trials, 0 failures.
- Sanity check: degenerate-split `INSERT_NC` with `s=0` / `s=q` matches no-split `INSERT_NC` exactly
  (confirms the definitions are being read correctly).

This **corroborates** the file's claim (the "unconditional" language in §12.1 refers to "true for
every `v†,Z`", not "already proved" — the file is explicit two lines later, "Key sub-lemma to prove
first (open gap, concrete, bounded)" and again in §12.2's Key-lemmas list, "Open, not proved" — no
overclaim found).

**Well-posedness of §12.2's recursive skeleton:** independently traced the DELETE/KEEP/MATCH
trichotomy one level deeper.
- DELETE and MATCH branches generalize cleanly to a multi-background set (same bijection argument,
  background elements untouched or grown by one) — confirmed by re-deriving the bijections by hand,
  matches the file's claim.
- KEEP branch: re-derived by hand that this does **not** trivially generalize — Fact 3's block
  extraction needs the extracted singleton to dominate everything else, and here `v†` need not
  dominate `z1` (or vice versa), unlike the top-level proof where `y1` is always the global max.
  Worked through both sub-cases (`z1>v†` and `v†>z1`) by hand: both are individually closable via a
  second application of Fact 3 (peeling whichever of `{v†,z1}` is larger, reducing to a "MAXINSERT"
  companion one level down), consistent with the file's own honest framing ("individually tractable
  by the same Fact-3 mechanism... not yet written down"). **One minor wording risk flagged for the
  builder** (not fatal): the "Key lemmas" paragraph's first bullet says the generalized Peeling Lemma
  "should be a direct re-run of the same three proofs" (implying free/costless), which is only true
  for DELETE/MATCH — the very next bullet correctly isolates the KEEP branch's extra case split as a
  distinct, non-free task. A builder skimming only the first bullet could be misled into thinking KEEP
  needs no new argument; tell the builder explicitly that KEEP requires the 2-way order case split
  before Fact 3 applies.
- Termination (`|Z|+b'` strictly decreasing): confirmed correct, MATCH grows background by exactly 1
  and shrinks `|Z|` by 2, DELETE shrinks `|Z|` and `b'` by 1 each, KEEP shrinks `|Z|` by 1 at fixed
  `b'` — always strictly decreasing.

The §12.0 "dead-end confirmed" claim (re-route-to-endpoint fails ~14%, extremes-only fails ~19%) is
independently corroborated by the explorer's own concrete counterexample
(`Y=(463,461,372,291,237,180)`), which I re-read and traced against §11's `INSERT_OPT`/`INSERT_NC`
machinery — consistent, no red flag.

**Verdict: APPROVE.** The skeleton is well-posed, every claimed lemma has a stated mechanism, the
one genuinely new sub-case (KEEP-branch order split) is correctly and honestly flagged as open (not
hidden behind "then it follows"), and the new base-case anchor (Full-Slack Insertion Lemma) is
independently corroborated to q=7 with zero failures. This is the single highest-leverage open item
in the whole population (closing it closes the entire upper bound for every m, hence every n).

---

### 3. `concavity-minimax-duality` — new §14 (Distinct-Bucket Lemma)

**Re-derived the closed form** `g*(t)=bit_length(t-1)+1` against the original piecewise definition
(§12.6) by hand for `t=1,2,3,4,5,8,16` — matches in every case (`g*(1)=1,...,g*(16)=5`), confirms
§14.1 is not a new claim, just a restatement.

**Re-derived the 5-line implication (§14.3) myself, independently, before checking the file's own
argument:** if two elements of a sorted state `v_1>...>v_k` never share a `g*`-bucket, then since
`g*` is nondecreasing and (by definition of "bucket" = level set) constant only within one bucket,
distinct buckets for a sorted pair forces strict inequality `g*(v_i)>g*(v_{i+1})` at every consecutive
pair — this step is in fact trivial (bucket = level set by construction, so "different buckets" and
"different g*-values" are the same statement for consecutive sorted terms — not even really "two
different observations" as the file frames it, but this doesn't affect correctness). Since these are
positive integers (Integer-Preservation), pairing consecutive terms gives each pair `≥1`, and if `k`
is odd, the trailing term `≥g*(1)=1` (monotonicity, since every active value in a reachable state is
a positive integer, hence `≥1`). Summing gives `e_{g*}(M)≥⌈k/2⌉≥1`. **This re-derivation matches the
file's §14.3 exactly — the implication is valid, no gap.**

**Independent BFS verification of the Distinct-Bucket Lemma** (fresh code, not reusing the file's or
explorer's implementation, exact integer D/M-operation BFS from `D_m`):
```
m=0..6: state counts 1, 3, 9, 31, 125, 585, 3117 — matches the file's own reported counts exactly
         (independent cross-check). 0 bucket collisions in every state, every m.
m=7 (pushed one level beyond, matching the explorer's own m=7 extension): 18537 states, 0 collisions.
Also verified: e_{g*}(M) ≥ ⌈|M|/2⌉ holds in every one of these states (direct numerical confirmation
of §14.3's implication on real reachable states, not just an abstract check).
```
No counterexample found; this strongly corroborates (does not prove) the Distinct-Bucket Lemma,
independently confirming the file's own m≤7 claim from a from-scratch implementation.

**§14.4's proof-shape lead** (extend the Superincreasing No-Early-Zero Lemma's token/signed-sum
invariant from "never exactly 0" to "no dyadic level is ever occupied by two simultaneously-active
tokens' highest-surviving power") is honestly flagged as NOT attempted — "a concrete lead, NOT
attempted — the builder's task." No overclaim.

**One structural note for the record (not a flaw):** even if §14 closes in full, it only reproduces
the lower bound `e_{g*}(M)≥1` — a result already fully and unconditionally established by
`dyadic-cascade-induction`'s §5.5 (round-8 milestone) via a different mechanism. This makes
`concavity-minimax-duality`'s remaining work strictly lower-leverage to the overall theorem than
`potential-weighting-upper-bound`'s gap (which unlocks the entire, still-open upper bound + n≥4). It
remains valuable as an independent/alternative proof and as a genuinely different technique (per
CLAUDE.md's diversity-of-thought concern, this is worth keeping alive), but should be weighted
accordingly in the build set.

**Verdict: APPROVE.** Precise statement, valid 5-line implication (independently re-derived, not just
trusted), strong numeric support extended one level further (m=7) than the file's own claim, honest
proof-shape lead with no math attempted yet.

---

### 4. Diversity / shared-gap check

The three approaches are NOT converging onto one shared wall this round: `dyadic-cascade-induction`
is essentially complete on its own front (lower bound, done); `potential-weighting-upper-bound`
targets the upper bound via a combinatorial peeling/induction-on-p mechanism; `concavity-minimax-
duality` targets an independent 1-Lipschitz-certificate re-proof of the lower bound via a distinct
structural (bucket-membership) invariant. These remain genuinely different techniques, not variations
of one framing — no plateau-collapse concern this round.

### 5. Single-gap-trap / 5th-slug check

Confirmed no 5th slug opened. The plateau-break explorer (`math-explorer-n-general.md`) correctly
declined the `c(n)=2c(n-1)/(2c(n-1)+1)` recursion and a "general n" framing as candidates — both
would relabel `potential-weighting-upper-bound`'s existing gap, exactly the trap CLAUDE.md warns
against. Confirmed `elementary-exchange-smoothing.md` is untouched (file mtime older than the other
three; content unchanged; still correctly retired).

---

### Build set discussion

`dyadic-cascade-induction` has **no new mathematical content or open task this round** — its own
remaining work (final joint-induction write-up) is explicitly gated on `potential-weighting-upper-
bound` closing first, and its only other listed option ("a genuinely different upper-bound mechanism")
has zero lead. Dispatching a builder here this round would not produce new proof content (per the
"don't default to building everything" rule — memory round 1). Benching it this round; it should
return to the build set the moment the sibling's aggregated lemma closes, or if the next round
identifies a concrete lead for an alternate mechanism.

`potential-weighting-upper-bound` and `concavity-minimax-duality` both have concrete, well-posed,
independently-verified base cases and honest open gaps with stated mechanisms — both are ready to
build. `potential-weighting-upper-bound`'s gap is higher-leverage (unlocks the entire remaining
theorem), so it should get priority, but `concavity-minimax-duality`'s gap is comparably close to
closing (one structural lemma away) and preserves technique diversity — both belong in this round's
build set.

Ranking updated via `update_ranking` (dyadic-cascade-induction > potential-weighting-upper-bound >
concavity-minimax-duality, anchored on last outcome maturity — verified-milestone > partial/partial,
and potential-weighting-upper-bound ranked above concavity-minimax-duality on leverage to the overall
theorem despite comparable proof-readiness this round). New Elo: dyadic-cascade-induction 1696 (top),
potential-weighting-upper-bound 1476, concavity-minimax-duality 1341.

build set: potential-weighting-upper-bound, concavity-minimax-duality
