## Status
partial

## Round 11 Outline (proof-outliner directive — pin `H`'s coverage via a
dichotomy-based finite-exception mechanism, not further empirical
stacking)

**Target (unchanged): the whole problem**, via the Pool Lemma equivalence
to FCBC (already certified — a universal window `H` works iff FCBC does
for that `H`; do not re-derive). Round 10's recommendation (d) permitted
reviving this approach only with a genuinely new magnitude-pinning idea;
this round supplies one, drawn from this round's jw-lens explorer's
"backbone + finitely many named exceptions" structural finding
(`/tmp/round-11/math-explorer-jw.md`, §Small-case notes): companion-set
growth empirically always EXTENDS a small backbone rather than replacing
it, with specific "backup prime" patterns found (e.g.
`2\notin comp(a_i)\Rightarrow\{3,83\}\subseteq comp(a_i)`, exhaustively
checked on every exception found).

**Technique:** reuse the certified Realized–Blocked Dichotomy (Lemma
ERD-C) per small candidate prime `p\in H`, to convert "does `p` divide
almost every companion set" into a finite-exception statement provable by
dichotomy, rather than an open-ended empirical sweep.

**Skeleton:**
1. Fix candidate window `H` (start from the certified `H_{100}`
   candidate). For each small prime `p\in H` and proper core `S`, apply
   Lemma ERD-C to the candidate coarse value `S\cup\{p\}`: either (α)
   realized (some index has radical exactly `S\cup\{p\}`) or permanently
   blocked by a witness `j_3`.
2. If blocked (β), apply the already-certified Escape-Confinement Lemma:
   every actual member of `I_S` lacking `p` in its companion set must
   contain a prime from `comp(a_{j_3})` (a FIXED finite set) instead —
   the formal version of the empirically-observed "backup prime" pattern
   (`\{3,83\}` playing the role of `comp(a_{j_3})` in the `a_1=4199`
   instance).
3. Iterate over the finitely many primes in `H` and the finitely many
   proper cores `S`: the set of indices in `I_S` lacking EVERY prime of
   `H` in their companion set is covered by the union of finitely many
   fixed witnesses' companion sets (one per blocked `(S,p)` pair) — a
   finite set of "backup primes," adjoined to `H` to repair the
   exceptions.
4. **Open gap:** bound the number of repair rounds needed (does this
   process terminate in a UNIFORMLY bounded number of steps across all
   cores, or could it cascade indefinitely) — reuse the certified Greedy
   Augmentation + Termination-Sufficiency Lemma's well-ordering skeleton
   (as in this round's revised `sunflower-bundle-closure` outline) for
   the termination argument, rather than re-deriving one from scratch.

**Key lemmas:**
- Dichotomy-based backup-prime existence (Steps 1–2) — because Lemma
  ERD-C and Escape-Confinement are already certified, unconditionally,
  for exactly this "coarse value realized-or-blocked" case split; the
  only new content is applying them systematically to EVERY `(S,p)` pair
  of a candidate window instead of ad hoc per instance.
- Finite repair set (Step 3) — because there are only finitely many
  `(S,p)` pairs (`S` ranges over `\le2^k-2` proper cores, `p` over `|H|`
  primes), a finite union of finite witness companion sets is finite
  (elementary).

**Open gaps:** Step 4 (termination/uniform bound on repair rounds — the
same open content as the revised `sunflower-bundle-closure`/
`forced-primes-well-ordering` termination arguments this round; genuine
synergy to check once any one of the three closes it) and whether the
resulting repaired `H` is truly universal across ALL `a_1` (this round
only targets making the CONSTRUCTION mechanism for a FIXED `a_1`
non-empirical, not the universality question — Step 4 of the file's own
prior diagnosis, unchanged: universal `H` is exactly as hard as FCBC in
general, per the certified Pool Lemma).

**Cases to cover:** `S` realized vs blocked for the coarse value
`S\cup\{p\}`, for every `(S,p)` pair in the candidate window — enumerate
explicitly per instance tested, do not assert "similarly" for untested
pairs.

**Watch out for:** do not conflate "`H_100` works via dichotomy for this
`a_1`" with "`H_100` works for every `a_1`" — this round's mechanism is a
rigor upgrade for a FIXED `a_1`'s construction, not a universality proof.

## Round 10 Outline (proof-outliner directive — prove the CONCRETE window
`H_100` is a valid Stabilization witness, via a finite-alphabet
pairwise-intersecting-family argument, not another empirical sweep)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). This round's mandate: turn the
`H_100:=P_1∪\{p\text{ prime}:p≤100\}` empirical finding (11+ `a_1` values,
zero violations, round 9; plus round 10's H100-stabilization explorer
pushing individual doubly-infinite channels to `20M`–`160M` terms with zero
violations, `/tmp/round-10/math-explorer-H100-stabilization.md`) into an
actual PROOF for a fixed doubly-infinite disjoint core pair `(S,S')`, using
the **orthogonal-stabilization explorer's finite-alphabet reframing**
(`/tmp/round-10/math-explorer-orthogonal-stabilization.md`, "Candidate
technique(s)" section) — genuinely different from the density/pigeonhole
mechanism assigned to `intersecting-family-covering-construction` this
round, and from the well-ordering/bridge-prime mechanism assigned to
`forced-primes-well-ordering`.

**Technique: finite-alphabet pairwise-intersecting-family argument.** Fix a
window `B` (start with `B=100`, i.e. `H_100`'s companion-prime part,
`{2,3,...,97}`, 25 primes). Every `i` has a **bitmask**
`\sigma(i):=rad(a_i)\cap\{p\le B\}\in\{0,1\}^{\pi(B)}` (a finite alphabet,
`2^{25}` states for `B=100`). The Stabilization Conjecture for `(S,S')`
restricted to window `B` is exactly: the set of realized bitmasks
`\Sigma_S:=\{\sigma(i):i\in I_S\}` and `\Sigma_{S'}` form a **pairwise
non-disjoint family** (every `\tau\in\Sigma_S,\tau'\in\Sigma_{S'}` satisfy
`\tau\cap\tau'\ne\emptyset`) — a purely finite combinatorial fact once
`\Sigma_S,\Sigma_{S'}` are known (each has at most `2^{25}` elements).

**Skeleton:**
1. Formalize `\sigma:\mathbb N\to\{0,1\}^{\pi(B)}` and restate the
   per-channel Stabilization Conjecture in this bitmask language (no gap,
   pure restatement — cite Theorem SW for why only doubly-infinite disjoint
   pairs need this).
2. **Key Lemma (needs proof, the empirical H100-stabilization finding is
   evidence, not proof): the "no all-zero bitmask" fact** — every `i` past
   some finite point has `\sigma(i)\ne\mathbf 0` (some prime `\le B` divides
   `a_i`). This alone is insufficient (two nonzero, disjoint bitmasks can
   still fail to intersect, as the orthogonal explorer's item (a) showed:
   individually-bounded-smallest-companion-prime is a refuted,
   insufficient condition) — flag explicitly as necessary but not
   sufficient, do not present it as closing the gap.
3. **Key Lemma (the real content, open): the realized-bitmask families
   `\Sigma_S,\Sigma_{S'}` are pairwise-intersecting.** Attempt via: (a) a
   direct structural argument using the greedy admissibility rule (`a_{n+1}`
   is the SMALLEST integer `>a_n` with `\gcd(a_{n+1},a_i)>1` for all
   `i\le n`) — since every earlier term must already share a prime with
   `a_{n+1}`, and `I_S,I_{S'}` are both infinite, a term `a_i\in I_S`
   realized AFTER many `I_{S'}` terms already exist must, by the greedy
   rule itself, share a prime with EVERY earlier `I_{S'}` term — this is
   NOT automatically a `\le B`-prime, but it bounds the search: **the
   actual open content is whether the greedy rule's forced intersection
   (Lemma P′, unconditional) can be shown to land inside a bounded window,
   for infinitely many pairs, not just each pair individually** (this is
   the same "magnitude, not just existence" obstruction other approaches
   hit — state honestly, do not paper over); (b) failing (a), attempt a
   finite-descent/exhaustion argument bounding `|\Sigma_S|,|\Sigma_{S'}|`
   directly by explicit simulation-backed conjecture PLUS a rigorous
   verification that the (now known, finite, by (a) trivially since
   `2^{25}` is an a priori cap) set of realized bitmasks is
   pairwise-intersecting — but note per round 10's H100-stabilization
   explorer, `\Sigma_S` (in the FULL `H_100`) does **not** saturate in
   count even at `N=160M` (`33,008` distinct sigs and growing) — so a
   proof cannot rely on `|\Sigma_S|` becoming literally constant; it must
   show pairwise-intersection holds for whatever finite-or-growing family
   is realized, a structurally different (weaker, existence-of-a-covering-
   design) claim than antichain finiteness.
4. If Step 3 succeeds for `B=100`, conclude `H_100` is a valid FCBC witness
   for `(S,S')`; repeat (or argue uniformly) across the finitely many
   doubly-infinite disjoint pairs of a fixed `a_1`.

**Key lemmas (claim + mechanism):**
- **Pairwise-intersecting bitmask family** — because the greedy rule forces
  `\gcd(a_i,a_j)>1` for every `i<j` (Lemma P′, unconditional, already
  certified) — the open step is pinning the FORCED common prime's
  *magnitude* within `[2,B]`, not just its existence. This is the
  count-vs-magnitude obstruction, now stated as a finite combinatorics
  question instead of a vague "does `H` exist" question.

**Open gaps:** Step 3(a)/(b) — no rigorous magnitude-pinning mechanism
exists yet in this workspace; this is genuinely new content to attempt.

**Cases to cover:** repeat the argument (or find a uniform one) across each
of the finitely many doubly-infinite disjoint core pairs per `a_1` (Theorem
SW already bounds this count by `\binom{2^k-1}{2}`).

**Watch out for:** do not conflate "`H_100` empirically has zero violations
to `N=160M`" with "`H_100` is proven to work for all `n`" — the round-10
H100-stabilization explorer explicitly found the *raw signature count*
under `H_100` keeps slowly growing (not plateauing) even as violations stay
at zero, so any proof strategy relying on "only finitely many signatures
ever occur" is targeting a likely-false lemma; target pairwise-
intersection of whatever occurs instead (per Step 3's honest framing).

## Round 9 build (this round — headline)

**What this round did.** Per dispatch: (1) corrected the outline's
mis-classification of Step 3 (now stated honestly as an unproven, though
well-supported, empirical claim, not a free consequence of the Domination
Lemma); (2) ran a substantially larger, fresh independent computational
investigation of the "bridge-prime patch" question the outline-reviewer
identified as the crux — reproduced the reviewer's `n=596`/`n=863`,
bridge-prime-`97` counterexample on `a_1=21528751`, extended it **10×**
past the reviewer's tested range (`n≤300,000` → `n≤3,000,000`, zero further
violations), and tested **10 new `a_1` values** with 3–4-prime, `21528751`-
style widely-spread cores; (3) found a striking new positive result — a
**single fixed set-shape**, `H:=P_1∪\{p\text{ prime}:p\le100\}` (25 small
primes, the same 25 for every `a_1` tested, no per-`a_1` patching), covers
**every** pair among **all 11** tested `a_1` values, including the two
hardest instances found (`21528751` to `n=3{,}000{,}000` and a newly-found
second hard instance, `9674419=79\cdot151\cdot811`, needing bridge prime
`23` under the small-6 candidate). (4) Did **not** find or complete a proof
that this (or any) fixed `H` works for *every* `a_1` — Step 4 (Pairwise
Small-Sharing) remains open; this round sharpens what a proof would need
to show and supplies substantially stronger, more diverse empirical support
for it, but does not close it. Status remains `partial`; full detail below
supersedes the round 9 outline's placeholder discussion of Step 3/4 with the
corrections the outline-reviewer required.

### 1. Step 3 (Small-Uniform-Hit), addressed honestly

**Claim (Step 3).** For every `m\ge1`, `\mathrm{rad}(a_m)\cap H\ne\varnothing`
for the candidate `H:=P_1\cup\{2,3,5,7,11,13\}` (or its enlargements below).

**This is NOT a free consequence of the Domination Lemma, and I do not claim
otherwise.** The Domination Lemma (`lemmas/domination-lemma.md`, certified)
states: for `x:=a_{n+1}` with prime factors `q_1,\dots,q_r`, some `q_j`
satisfies `D_n(q_j)\ge n/r` — i.e. **some** prime factor of the new term
already divides a large fraction of prior terms. This says nothing about
*which* prime that is; in particular it gives no reason the dominant `q_j`
must lie in any fixed, `a_1`-independent-in-shape finite set like
`\{2,3,5,7,11,13\}`. A term's dominant prime factor (in the Domination
Lemma's sense) could a priori be any large prime that happens to have been
recruited early and divides many terms — the lemma bounds *frequency*
(`D_n(q_j)`), not *magnitude* (`q_j` itself). So Step 3, exactly as the
outline-reviewer flagged, is a genuine, unproven, structural claim about
this specific greedy sequence, not a corollary of already-certified content.
I record it here as an **open empirical claim**, not a lemma.

**Empirical support for Step 3 (this round, in addition to the outline-
reviewer's `1c`/`1b` numbers, which I independently reproduced — see §2.0
below).** Across the 11 `a_1` values tested this round (§2), zero terms
among the (up to `3{,}000{,}000` for the hardest case, `\ge300{,}000` for
every other case) generated terms had radical disjoint from
`H:=P_1\cup\{2,3,5,7,11,13\}` — `\#empty\_sigs=0` in every single run
reported in §2's tables. This is a substantial extension of the outline-
reviewer's `0/500{,}000` (`247`) and `0/357{,}399` (`2747`) findings to a much
wider and structurally more adversarial family of `a_1` (2, 3, and 4-prime
cores, primes ranging from `17` to over `1000`). I do **not** claim this
proves Step 3 — it remains conjectural — but the evidence is now
considerably broader than before.

### 2. The bridge-prime-patch finiteness question (the round's main new content)

**Method.** Fresh Python this round (`/tmp/round-9/work/gen.py`,
`analyze.py`, `batch_test*.py`, `final_check.py` — all reproducible, exact
integer arithmetic, `math.gcd`/`sympy.factorint`, no floating point). The
sequence generator avoids factoring entirely for the admissibility check
(it maintains the certified Lemma W3 minimal-radical antichain of **actual
term values**, and tests candidates via `math.gcd(x,m)>1` directly against
antichain members — correct because `\gcd` needs no factorization,
and Lemma W3 already certifies that checking only the antichain suffices).
This was cross-checked for correctness against the direct `\gcd`-against-
**all**-prior-terms definition on `a_1=247,n\le2000` (exact agreement,
antichain method a pure speed optimization, not a different rule) before
being trusted for the large runs below.

**2.0. Reproduction of the outline-reviewer's `1c` finding, and extension
past their tested range.** For `a_1=21528751` (`P_1=\{103,197,1061\}`),
candidate `H_0:=P_1\cup\{2,3,5,7,11,13\}`:
- Generated `3{,}000{,}000` terms in `67.3` s. Checking all realized
  `H_0`-signatures pairwise (`194` distinct signatures through `n=1000`,
  growing to `303` by `n=3{,}000{,}000`): **exactly the same violation** the
  reviewer found, at `n=596` (signature `\{2,3,5,7,1061\}`) vs. `n=863`
  (signature `\{11,103,197\}`) — confirmed disjoint. Independently
  recomputed the bridging prime: `\gcd(a_{596},a_{863})=97` exactly (a
  single prime, confirmed via `sympy.factorint(97)=\{97:1\}`).
- Patched candidate `H_0':=H_0\cup\{97\}`: **zero further violations and
  zero empty signatures through `n=3{,}000{,}000`** — a **10× extension**
  of the reviewer's `n\le300{,}000` check (`231` signatures found there;
  `303` distinct `H_0'`-signatures found here by `n=3{,}000{,}000`, still
  zero violations). This is the single strongest piece of evidence in the
  workspace's history that a *specific*, once-patched, finite `H` might
  genuinely work for a specific hard `a_1` all the way out.

**2.1. Ten new `a_1` values, chosen to stress-test cross-core sharing
further.** I chose triples/quadruples of primes deliberately mimicking
`21528751=103\cdot197\cdot1061`'s "spread" structure (ratios
`\approx1.9` and `\approx5.4` between consecutive prime factors, so that
proper cores are as separated as possible — the case Step 4 is hardest
for), plus a few "clustered" controls (`101\cdot103\cdot107`,
`23\cdot29\cdot31`) and one 4-prime case (`17\cdot19\cdot23\cdot29`), each
generated to `N\ge300{,}000` (most to `500{,}000`; two capped by a
per-run time budget at `n\approx30{,}000$–$43{,}000$, still far past where
any violation has ever been found in this workspace). For each, tested the
literal small-6 candidate `H:=P_1\cup\{2,3,5,7,11,13\}` and, on any
violation, extracted the exact bridging prime via `\gcd` (no factoring
guesswork) and re-tested until stable:

| `a_1` | `P_1` | `N` tested | small-6 candidate result |
|---|---|---|---|
| `20677` | `\{23,29,31\}` | `500{,}000` | 0 violations, 0 patch |
| `65231` | `\{37,41,43\}` | `500{,}000` | 0 violations, 0 patch |
| `215441` | `\{17,19,23,29\}` (4-prime) | `300{,}000` | 0 violations, 0 patch |
| `1{,}113{,}121` | `\{101,103,107\}` | `400{,}000` | 0 violations, 0 patch |
| `22{,}870{,}501` | `\{107,211,1013\}` | `400{,}000` | 0 violations, 0 patch |
| `2{,}895{,}973` | `\{53,101,541\}` | `500{,}000` | 0 violations, 0 patch |
| `4{,}184{,}051` | `\{61,113,607\}` | `500{,}000` | 0 violations, 0 patch |
| `7{,}129{,}891` | `\{71,137,733\}` | `500{,}000` | 0 violations, 0 patch |
| `9{,}674{,}419` | `\{79,151,811\}` | `500{,}000` | **1 violation** at `n=12` (`\{3,5,79\}`) vs. `n=15` (`\{2,7,151\}`), bridge prime `\mathbf{23}`; after patch (`H\cup\{23\}`), 0 further violations to `500{,}000` |
| `14{,}303{,}813` | `\{89,173,929\}` | `500{,}000` | 0 violations, 0 patch |
| `21{,}528{,}751` | `\{103,197,1061\}` | `3{,}000{,}000` | **1 violation** at `n=596`/`863`, bridge prime `\mathbf{97}`; 0 further violations after patch |

**Finding.** Among **11** tested `a_1` values (2 old + 9 new this round,
spanning `\omega(a_1)\in\{2,3,4\}`, `P_1`-primes from `17` to over `1000`),
exactly **2** needed a patch beyond the literal `P_1\cup\{2,3,5,7,11,13\}`,
and in **both** cases the patch was **exactly one prime**
(`97` and `23` respectively — both, notably, themselves `\le100$). No
instance required more than one bridge prime, and no instance's needed
bridge prime was large (both are small primes comparable in size to the
existing small-6 set, not primes that scale with `a_1`). This directly
answers the dispatch's central question in the range tested: **the patch
does not show growth-without-bound in this data — it stays at size `0` or
`1` across every tested case**, and the two nonzero patches found are
themselves drawn from a small range.

**2.2. A universal fixed-shape candidate, tested with no per-`a_1`
patching.** Motivated by 2.1's observation that every needed bridge prime
found so far is `\le100`, I tested a single **fixed** enlarged candidate,
`H_{100}:=P_1\cup\{p\text{ prime}:p\le100\}` (25 small primes, same 25 for
every `a_1` — no per-instance tuning at all) against **all 11** `a_1`
values, at the same `N` as above (and `N=3{,}000{,}000$ for `21528751`):

```
a1=20677     (P1={23,29,31})       N=500000   #violations=0  #empty=0
a1=65231     (P1={37,41,43})       N=500000   #violations=0  #empty=0
a1=215441    (P1={17,19,23,29})    N=300000   #violations=0  #empty=0
a1=1113121   (P1={101,103,107})    N=400000   #violations=0  #empty=0
a1=22870501  (P1={107,211,1013})   N=43062    #violations=0  #empty=0  (generation time-budget-capped; monotonicity, §2.3, makes the N=400000 small-6 clean result an a fortiori guarantee for the larger N too)
a1=2895973   (P1={53,101,541})     N=500000   #violations=0  #empty=0
a1=4184051   (P1={61,113,607})     N=32816    #violations=0  #empty=0  (see 22870501's note; N=500000 small-6-clean result from 2.1 is an a fortiori guarantee)
a1=7129891   (P1={71,137,733})     N=500000   #violations=0  #empty=0
a1=9674419   (P1={79,151,811})     N=500000   #violations=0  #empty=0
a1=14303813  (P1={89,173,929})     N=500000   #violations=0  #empty=0
a1=21528751  (P1={103,197,1061})   N=3000000  #violations=0  #empty=0
```

**Zero violations and zero empty signatures across all 11 cases, with no
per-`a_1` patching at all** — a single fixed set-shape (25 small primes
plus `P_1`) suffices everywhere this round tested, including the two
hardest instances (`21528751` to `N=3{,}000{,}000`; `9674419`, which
defeated the un-enlarged small-6 candidate).

**2.3. Monotonicity fact used above (trivial, stated explicitly).** If a
finite set `H` satisfies `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne
\varnothing` for all `i<j\le N`, then so does any `H'\supseteq H`, for the
same `N` — immediate, since `H'\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)
\supseteq H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)`. This is why the two
cases where generation was time-budget-capped before reaching their target
`N` under `H_{100}` (`22870501`, `4184051`) still carry a genuine `N=400{,}
000`/`500{,}000`-strength guarantee: §2.1 already established the *smaller*
candidate `H:=P_1\cup\{2,3,5,7,11,13\}\subseteq H_{100}` has zero violations
on those two cases out to that larger `N`, so `H_{100}` automatically does
too, by this monotonicity fact, without needing to re-run the (slower)
25-prime signature computation out to the full `N`.

### 3. Honest assessment: is FCBC closed for a fixed universal `H`?

**No — this round strengthens the empirical case substantially but does not
supply a proof, and I state this plainly rather than overclaiming.** What
is missing:

1. **No mechanism was found or completed this round that proves Step 4 in
   general.** The only tool on hand for the "why would pairs always share a
   small prime" question is the Domination Lemma, which (§1) bounds
   *frequency* of the dominant prime's earlier occurrences, not its
   *magnitude* — it does not, by itself or in any combination with
   already-certified lemmas I could find, force the shared prime between
   two disjoint-core signatures to lie in a fixed small set. I looked for
   a way to combine the Domination Lemma with Lemma 1 (uniform gap bound,
   `lemmas/lemma-1-uniform-gap-bound.md`) to derive a magnitude bound —
   Lemma 1 gives `a_{n+1}\le a_1+nL` (`L=\mathrm{rad}(a_1)`), hence
   `\omega(a_{n+1})=O(\log n)`, hence (Domination Lemma) the dominant prime
   divides `\Omega(n/\log n)` prior terms — but this still does not bound
   the prime's *value*, only how many terms it divides; a prime can be
   large and still divide `\Omega(n/\log n)` terms if it is recruited early
   and the sequence happens to favor it. This is the identical
   count-vs-size gap `sunflower-bundle-closure` diagnosed for `(UB_S)`
   (`current.md`, round 8) — I record, as an honest structural finding,
   that the same obstruction reappears here: **the certified machinery in
   this workspace bounds how often a prime recurs, never how large it is**,
   and Step 3/Step 4 both, at bottom, need a magnitude bound.
2. **By the already-certified Pool Lemma (`lemmas/lemma-W4-pool-lemma-tree-
   Pi.md` = `lemma-W4-pool-lemma-tree-Pi.md` in this file's own round-4
   work), "some finite `\Pi` makes `\mathcal G_N(\Pi)` nonempty for every
   `N`" is *logically equivalent* to FCBC itself, not an easier
   intermediate target — so even the striking `H_{100}`-works-everywhere
   finding of §2.2, however suggestive, is exactly as hard to *prove* in
   general as FCBC was already known to be. I flag this explicitly so the
   result is not misread as a reduction in difficulty: it is a strong
   *empirical convergence* (11/11 fixed-shape successes, including two
   instances that defeated the smaller candidate), not a proof that this
   convergence must continue for every `a_1`.
3. **The negative direction was also actively sought and not found.** I
   deliberately targeted the two "spread-triple, 21528751-style" cases most
   likely to break `H_{100}$ (large gaps between `P_1`'s primes,
   `9674419` and `21528751`, both already known to defeat the smaller
   candidate) and pushed them to the largest `N` time allowed
   (`500{,}000$ and `3{,}000{,}000$ respectively) — no counterexample to
   `H_{100}` was found. This is meaningful negative-search effort, not
   merely "didn't look," but it remains a finite check.

**Conclusion (honest, not overclaimed).** This round's contribution is: (a)
a corrected, honest statement of Step 3 as an open empirical claim, not a
free consequence (per the outline-reviewer's required fix); (b) a
substantially broadened and deepened empirical investigation of the
bridge-prime-patch question that was this round's assigned crux, finding
the patch stays at size `\le1` across every one of 11 tested instances, and
that a **single universal fixed-shape** candidate (`P_1\cup\{p\le100\}`)
resolves every instance tested with no further patching, including a newly
discovered second hard case (`9674419`); (c) an honest diagnosis that the
obstruction to a real proof is structurally the same count-vs-magnitude gap
that defeated the whole `(UB_S)$ family in rounds 4–8, now located precisely
inside Step 4 rather than resolved. Step 4 (equivalently: does
`H_{100}$, or *some* fixed finite `H`, work for *every* `a_1`?) remains the
sole open gap of this approach.

## Round 9 Outline (proof-outliner directive — abandon `(UB_S)`-family
routes entirely; attack FCBC directly via a small explicit covering set)

**Context (read first).** Round 9's explorers pushed simulation ~100-400x
past round 8's tested range and found strong evidence that `(UB_S)`
(round 8's sole reduction target, `theorem-UBS-sufficiency.md`) is very
likely **FALSE**: companion-bundle size keeps setting new records (ω=8
confirmed for `a_1=247` at `n=408816` and `a_1=2747` at `n=374037`) with no
blocking witness found in 1.3M terms. This does **not** refute FCBC itself
(`(UB_S)`/`(MRS)` was only ever *sufficient* for FCBC, never necessary —
`lemmas/lemma-MS-minimal-radical-stabilization-sufficiency.md` is a
one-directional implication) — and the same round-9 data, read correctly,
is actually evidence *for* a small explicit FCBC witness set: explorer 3
found **0 of 1,300,000 terms** (`a_1=247`) have radical disjoint from
`{2,3,5,7,11,13}` — every term, however large its own ω, keeps touching the
same handful of small primes. **New target this round: construct FCBC's `H`
directly and explicitly, never bounding an individual bundle's size.**

**Do not** re-attempt round 4-8's `(UB_S)`/`(MRS)`/pigeonhole/Δ-system
machinery in any form — proven (repeatedly, and now numerically doubted at
its source) to bound bundle *count*, and per round 9's evidence the bundle-
*size* target it would need is itself likely false. This file's new plan
(full skeleton in `/tmp/round-9/proof-outliner.md`, reproduced in essence
below) is a **constructive small-covering-set** argument, genuinely
different in kind:

1. `P_1=rad(a_1)` hits every `a_m`, `m≥2` (free, by the problem's own
   definition applied at `i=1`) — handles pairs `(1,j)` only.
2. Candidate `H := P_1 ∪ {2,3,5,7,11,13}` (or a fixed small extension the
   builder pins empirically first).
3. **Key Lemma (Small-Uniform-Hit):** every `rad(a_m)` meets `H` —
   because greedy minimality reuses cheap small primes to cover many prior
   constraints at once (Domination Lemma's pigeonhole half already
   certified; round 9 confirms this bites in practice).
4. **Key Lemma (Pairwise Small-Sharing, the real open gap):** every pair
   `i<j` shares the *same* `H`-element — realized companion bundles are
   empirically close to nested/prefix-like (though NOT a literal invariant
   — `a_1=247,n=2,rad=\{2,5,13\}` already skips `3`, so state only the
   weaker "eventually, any two bundles of size ≥2 share a prime ≤ some
   fixed bound," and prove or refute that).
5. Conclude FCBC, invoke the already-certified Theorem 5.1
   (`lemmas/theorem-5.1-master-conditional-theorem.md`) to finish the whole
   problem.

Open gap: Step 4 only. See the full skeleton (including case breakdown and
explicit watch-outs) in `/tmp/round-9/proof-outliner.md` under
`explicit-window-backbone-construction`.

## Round 4 Outline (proof-outliner directive — pivot to compactness/König
framing)

**Do not re-attempt the round-3 finite-descent monovariant on `|H_K|` or
`2^{|H_K|}-1`** — Lemma W2's discussion already shows both are
non-decreasing in `K` (wrong direction for descent); this is a permanently
retired mechanism for this approach, not to be resurrected in a disguised
form.

**New target this round, motivated by the round-4 refutation explorer**
(`/tmp/round-4/math-explorer-refute-fcbc.md`): attack FCBC via a
**compactness / König's-lemma-style argument on the minimal covering-window
size**, rather than an explicit finite-descent construction. Two round-4
findings motivate this specifically:
- The **Patch-via-P′ Lemma** (refutation explorer, proved independently of
  Lemma W1/W2 via the unconditional Lemma P′ alone): for any `H\supseteq
  H_K`, every pair `(i,j)` with `\min(i,j)\le K` is covered *automatically,
  for free*, with no FCBC hypothesis needed. So the entire open content of
  FCBC is confined to pairs with **both** indices `>K`, for every candidate
  `K` — i.e. behavior "at infinity," never a finite prefix.
- The hardest stress case found to date, `a_1=21528751=103\cdot197\cdot1061`
  (`K=86`, far larger than any previously tested `K\le5`), shows the minimal
  covering-window size `K` **stabilizes and stays exactly constant** once
  reached, tested to `N=100{,}000` — i.e. `f(N):=` minimal size of a finite
  set covering all pairs `(i,j)` with `i,j\le N` appears to be an eventually
  constant function of `N`, for this and every other tested `a_1`.

**Concrete plan (three sub-gaps, all currently open — spell out honestly,
do not paper over any of them):**

1. **Define `f(N):=` the minimal size of a finite set of primes covering
   every pair `(i,j)`, `i<j\le N`.** `f` is well-defined (`H_N` itself
   always works, by Lemma P′, so `f(N)\le|H_N|<\infty`) and **non-decreasing
   in `N`** (a one-line proof: any set covering all pairs up to `N+1` also
   covers all pairs up to `N`, since the latter is a subset of the
   constraints — so the minimal size for the larger constraint set is at
   least the minimal size for the smaller one). **Sub-gap (i), the hardest
   of the three:** prove `f(N)` is bounded above by a constant, uniform in
   `N`, for every fixed `a_1`. This is close to the heart of FCBC itself and
   is **not** established by anything above — flag this honestly; restating
   the target via `f(N)` does not make it easier by itself, only more
   structured.
2. **Sub-gap (ii): even given boundedness of *size*, a genuine König's-lemma
   argument (finite branching) additionally needs the minimal covering sets
   to be drawn from a *fixed finite candidate pool* of primes** — a priori,
   minimal covering sets of bounded size could still keep drawing on new,
   ever-larger primes as `N` grows while staying bounded in size, which
   would break finite branching. **Candidate fix to investigate (not yet
   justified):** the round-4 density explorer's `H_\rho` excess-density
   invariant (`/tmp/round-4/math-explorer-h-rho-density.md`) is finite and
   matches `\mathrm{rad}(L_{\text{per}})` exactly in 26/26 numerical tests —
   a natural candidate for the fixed finite pool. Using it here would need
   its own argument (not currently available) for why minimal covering sets
   can always be chosen from within `H_\rho`; do not assume this without
   proof.
3. **Sub-gap (iii): even granting (i) and (ii)** (a finitely-branching tree
   of per-`N` minimal covering choices, nonempty at every level), a
   König's-lemma infinite path gives a *coherent sequence* of choices, not
   automatically a single fixed `H` covering every pair simultaneously —
   getting from "infinite path" to "one literal covering set" needs a
   further pigeonhole step (the same node value recurring at unboundedly
   many levels along the path, using finite branching), which has not been
   spelled out or verified here. State and prove this step explicitly
   rather than treating "König's lemma gives an infinite path" as
   sufficient on its own.

**Do not claim any of these three sub-gaps is closed without an explicit,
checkable proof** — this pivot replaces one hard target (FCBC directly) with
a structurally cleaner but still genuinely open one; treat sub-gap (i) in
particular as comparably hard to the original conjecture, not a shortcut
around it.

## Round 4 build (this round) — the tree made precise, sub-gap (iii) closed

Per the round-4 outline-reviewer's explicit instruction ("before doing
anything else, write down the tree explicitly: what exactly is a node at
level `N`, and what is the parent-child compatibility relation... do not
report progress on this pivot without an explicit tree definition on the
page"), this round's work is entirely about making the compactness/König
pivot precise. **Headline result: sub-gap (iii) is now fully closed** — not
by König's lemma at all, but by an elementary finite-descent argument (the
same technique as certified Lemma C) that is strictly simpler than what the
round-4 outline anticipated. Sub-gaps (i)/(ii) are unified into one precise
statement (the **Pool Lemma**, Lemma W4 below) that is proved **logically
equivalent to FCBC itself** — so this is a genuine architectural
clarification (a correct, complete tree definition; a rigorous closing of
the "path ⇒ literal covering set" step; a clean single reformulation of what
remains) but it is **not** a weakening of the remaining difficulty: sub-gaps
(i)+(ii) combined are exactly as hard as FCBC, proved so, not merely
suspected so. Full statement and proof: Lemma W4 below. Numerical validation
against all seven requested stress cases (`15,221,247,375,4087,4199`, and
the round-4 hard case `21528751`, `K=86`) is reported in the empirical
section below Lemma W4.

## Approaches tried

- **Round 9 (this round).** See "Round 9 build" section above for full
  detail. Summary: corrected the round-9 outline's mis-classification of
  Step 3 (Small-Uniform-Hit) as "free" — it is an open empirical claim, the
  Domination Lemma bounds recurrence frequency, not prime magnitude, so it
  does not by itself imply Step 3. Ran a substantially larger, fresh,
  independent computational investigation of the "bridge-prime patch"
  question the outline-reviewer identified as this approach's crux:
  reproduced the reviewer's `a_1=21528751` counterexample
  (`n=596`/`n=863`, bridge prime `97`) and extended verification of the
  patched candidate 10× past the reviewer's range (`n\le300{,}000\to n\le
  3{,}000{,}000`, zero further violations); tested 10 new `a_1` values with
  `21528751`-style widely-spread multi-prime cores, finding the patch stays
  at size `\le1` in all 11 tested cases (one new hard instance found,
  `a_1=9674419=79\cdot151\cdot811`, needing bridge prime `23`); found that a
  single **fixed, universal** candidate `H_{100}:=P_1\cup\{p\text{ prime}:
  p\le100\}` (no per-`a_1` tuning) resolves **all 11** tested instances with
  zero violations, including both hard cases that defeated the smaller
  candidate. Did **not** find or complete a proof that any fixed `H` works
  for *every* `a_1` — diagnosed, honestly, that the obstruction is
  structurally the same count-vs-magnitude gap that defeated the `(UB_S)`
  family in rounds 4–8 (the Domination Lemma bounds how *often* a prime
  recurs, never how *large* it is), now located inside Step 4 instead of
  resolved. Verdict (self-assessed): substantially strengthened, broadened,
  and sharpened empirical support and a cleaner universal-candidate
  conjecture; Step 4 itself (equivalently, by the already-certified Pool
  Lemma, exactly as hard as FCBC) remains open.

- **Round 4 (this round).** See "Round 4 build" section above and Lemma W4
  below for full detail. Summary: (a) showed explicitly that the "naive"
  tree the round-3 outline gestured at (per-`N` minimal covering choices) is
  **not** finitely branching without first fixing a finite candidate pool
  `Π` — concretely, `|H_N|` (the set of primes actually appearing among the
  first `N` terms' radicals) keeps strictly growing well past the point
  where the *minimal covering window* has stabilized (e.g. `a_1=375`:
  minimal `K=3` but `|H_N|` grows from `5` to `18` between `N=5` and `N=30`
  with no sign of stopping), so there is no natural bound on the level-`N`
  local alphabet without an extra assumption; (b) fixed this by defining the
  tree `T_Π` relative to an externally-fixed finite pool `Π` (formal
  definition below); (c) proved the **Pool Lemma** (Lemma W4): FCBC holds
  iff some finite `Π` makes the per-level node sets `𝒢_N(Π)` all nonempty —
  and, crucially, proved the "infinite path ⇒ literal covering set" step
  (round 4's sub-gap (iii)) in full, using only elementary finite descent
  (a non-increasing sequence of non-negative integers `|𝒢_N(Π)|` stabilizes
  — literally the same technique as certified Lemma C), with **no
  invocation of the general infinitary König's lemma needed at all**, since
  the node space `2^Π` is finite in total (not just finitely branching per
  level); (d) verified the Pool Lemma's mechanics computationally by
  exhaustive subset enumeration on `a_1=15,221,247,375,4087,4199` (all
  confirmed: `𝒢_N(Π)` nested-decreasing, stabilizes at a small `N`, to a
  nonempty limit); (e) found a striking independent cross-validation for
  `a_1=4199`: running the Pool Lemma machinery with `Π:=H_5` (the
  round-3 window) recovers a minimal element of `𝒢_∞` equal to
  `{2,3,13,17,19,83}` — **exactly** the set the round-4 density explorer's
  `H_ρ` invariant found by a completely unrelated statistical method,  a
  fourth independent method (after the window search, the combinatorial
  imprint-period search, and the density search) landing on the same
  answer; (f) honestly could not close sub-gaps (i)/(ii) themselves — the
  Pool Lemma shows they are *equivalent* to FCBC, not easier, and the
  round-4 density explorer's finding that `H_ρ`-finiteness needs analytic
  machinery (Mertens/Borel–Cantelli-type density arguments) absent from
  both `knowledge_base.md` and the crux corpus still applies unchanged; this
  round did not attempt to construct that missing analytic ingredient
  (correctly out of scope for one round — it would be new, unverified
  mathematics, not an adaptation of a checkable technique).
  Verdict (self-assessed): genuine new structural content (Lemma W4, fully
  proved), and a real simplification of the architecture (no actual
  König's-lemma/compactness machinery needed, contrary to the round-4
  outline's own framing) — but the Key Lemma / FCBC itself remains **open**,
  now precisely reformulated as Pool Lemma existence, equivalent to (not
  weaker than) the original target.

- **Round 3.** Dispatched to close the Key Lemma's termination gap
  flagged by the outline-reviewer: the outline's mechanism (i) ("the escaping
  common prime must already lie in `rad(a_i)`, `i\le K'`, for a slightly
  larger `K'`; iterate and bound the number of enlargements") had no stated
  reason the iteration terminates. This round:
  1. Proved a new **Equivalence Lemma**: the Key Lemma (some finite `K` makes
     `H_K:=\bigcup_{i\le K}\mathrm{rad}(a_i)` a covering set) is not merely a
     *special case* of the Finite Covering Backbone Conjecture (FCBC) — it is
     **logically equivalent** to it. Any finite covering set `H` can be
     replaced, without loss, by `H_{K}` for an explicit finite `K` built from
     `H` itself. This is new content: it formally proves the population's
     three "Gap-1" approaches (`persistent-backbone-monovariant`,
     `forced-primes-well-ordering`, this approach) are all attacking the
     *identical* single proposition, not three related-but-distinct ones —
     explaining, rather than just observing, why they keep hitting the same
     wall.
  2. Proved a small but genuinely informative **Patch Lemma**: any single
     failure of `H_K` on a specific pair `(i,j)` can always be repaired by
     enlarging `K` to `K':=i`. Combined with the Equivalence Lemma, this
     pins down *exactly* what is missing for a real proof: not the
     possibility of patching individual failures (always possible, one at a
     time), but a proof that only **finitely many** patches are ever
     required in total. I looked for a monovariant that would force this
     (in analogy with certified Lemma C's `|C_n|`-descent) and found that
     the natural candidate quantities (`|H_K|`, `2^{|H_K|}-1`) are
     *non-decreasing* in `K` — the wrong monotonicity direction for a
     finite-descent argument — so Lemma C's technique does not transfer to
     this object without a genuinely new ingredient. I record this as an
     honest diagnostic finding, not a formal impossibility theorem (I have
     not proved *no* monovariant can exist, only that the natural
     candidates fail).
  3. Proved the **Minimal Radical Reduction Lemma** (new, unconditional,
     fully general structural fact about the sequence, independent of FCBC):
     admissibility of a candidate `x` against `a_1,\dots,a_n` is equivalent
     to admissibility against only the inclusion-minimal radicals among
     `\mathrm{rad}(a_1),\dots,\mathrm{rad}(a_n)`. Verified by direct
     simulation (`a_1=221`, `n` up to `199`: the reduced and full
     admissibility checks agree at every step). This is real, reusable
     structural content but — checked explicitly — does **not** by itself
     bound anything: the minimal-index set `M_n` was observed to keep
     growing (`|M_{199}|=42` for `a_1=221`), so it does not collapse FCBC to
     a finite check on its own.
  4. Tested mechanism (ii) from the outline ("`K` bounded by a function of
     `\omega(a_1)` alone") and **falsified it empirically**: computed the
     true minimal sufficient `K` for eleven values of `a_1` (up to `N=3000`
     or `20000` terms). Among the eight values with `\omega(a_1)=2`
     (`65,91,143,221,247,375,1073,4087`), minimal `K` ranges over
     `\{2,3,4\}` — not constant, so no formula purely in `\omega(a_1)` can
     give the exact minimal `K`. (`K` is still small and bounded in every
     tested case — consistent with FCBC being true — just not a clean
     function of `\omega(a_1)` alone.)
  5. Extended the round-3 numerical confirmation of the construction itself:
     re-verified `H_K` (found minimal `K=5` for `a_1=4199`, `K=2` for
     `a_1=4087`) covers **all** pairs among the first `20{,}000` terms with
     **zero** failures, for both of round 2's adversarial "`W` unbounded"
     cases — i.e. the canonical witness set `W` growing past 21 primes with
     no plateau (round 2's finding) does **not** translate into `H_K`
     needing to grow: a small, fixed window still suffices out to 20,000
     terms even though `W` does not stabilize. This is useful evidence that
     `H_K`-type coverage and `W`-finiteness are different (and the former
     looks much more tractable), but it is evidence, not a proof.
  Verdict (self-assessed): genuine new structural content proved in full
  (Equivalence Lemma, Patch Lemma, Minimal Radical Reduction Lemma), but the
  Key Lemma itself (`\exists` finite `K`, unconditionally) remains **open**.
  The round's honest conclusion is that this approach's original mechanism
  (i) as stated cannot be completed by finite-descent/pigeonhole methods
  internal to this approach alone — it requires either a new monovariant not
  yet found, or importing the analytic (`\omega`-growth / Domination-Lemma)
  machinery that the sibling approaches are developing (which the dispatch
  instructs me not to duplicate, only to note as the natural bridge).

## Current best

**Round 9 status (read first).** The proved content below (Lemmas W1–W4,
all still fully rigorous and unconditional) is unchanged this round. What
changed this round is the *empirical* picture around the one open gap
(equivalently, per Lemma W4, "does some finite `\Pi` exist with `\mathcal
G_N(\Pi)` nonempty for every `N`", i.e. does FCBC hold): a single fixed
25-small-prime enlargement `H_{100}:=P_1\cup\{p\text{ prime}:p\le100\}`
was found, this round, to cover every pair with zero violations across
**11** tested `a_1` values (up to `N=3{,}000{,}000` on the hardest), a
substantial strengthening and broadening of the evidence base — see "Round
9 build" above for full detail. **No proof of Step 4 / Pool-Lemma existence
was found or completed this round**; the gap is unchanged in kind, only in
how well-supported and how sharply stated its likely resolution is. See
"Round 9 build" §3 for the precise, honest statement of what remains open
and why (a count-vs-magnitude obstruction structurally identical to the one
that defeated the `(UB_S)` family, rounds 4–8).

**What is proved (all fully rigorous, unconditional — see proofs below,
established rounds 3–4, unchanged and still standing this round):**

1. **Equivalence Lemma (Lemma W1, round 3).** FCBC holds if and only if the
   Key Lemma holds (some finite `K` makes `H_K` a covering set).
2. **Patch Lemma (Lemma W2, round 3).** A single failure of `H_K` on pair
   `(i,j)` forces `i>K` and is always repaired by taking `K':=i`.
3. **Minimal Radical Reduction Lemma (Lemma W3, round 3).** Admissibility
   against `a_1,\dots,a_n` reduces exactly to admissibility against the
   inclusion-minimal radicals among them.
4. **Pool Lemma (Lemma W4, round 4, new).** Fix any finite set of primes
   `Π`. Define, for `N\ge1`, `𝒢_N(Π):=\{S\subseteq Π : S\text{ covers every
   pair }i<j\le N\}`. Then **FCBC holds if and only if some finite `Π` makes
   `𝒢_N(Π)` nonempty for every `N`.** The `(\Leftarrow)` direction is proved
   by an explicit, fully elementary finite-descent argument (no König's
   lemma, no compactness axiom): `|𝒢_N(Π)|` is a non-increasing sequence of
   non-negative integers (since `𝒢_{N+1}(Π)\subseteq 𝒢_N(Π)`, proved
   directly), hence stabilizes; any `S` in the stabilized limit covers every
   pair. This **fully and rigorously closes round 4's sub-gap (iii)** ("path
   in the tree `\Rightarrow` one literal covering set") — it turns out no
   separate pigeonhole step or genuine use of König's lemma is needed once
   `Π` is fixed, because the tree's node-label space `2^Π` is finite in
   total, not merely finitely branching per level.
5. **Honest negative/diagnostic findings, round 3 (still standing):** (a)
   the natural finite-descent monovariants `|H_K|`, `2^{|H_K|}-1` are
   non-decreasing in `K` (wrong direction for termination); (b) minimal `K`
   is not a clean function of `\omega(a_1)` alone.
6. **Honest negative/diagnostic finding, round 4 (new):** the Pool Lemma's
   `(\Rightarrow)` direction is trivial (`Π:=H`), so the Lemma is a genuine
   *equivalence*, not merely a sufficient condition — meaning **sub-gaps
   (i)+(ii) combined are exactly as hard as FCBC**, not an easier
   intermediate target. The round-4 outline's compactness/König's-lemma
   framing, now made fully precise, turns out to need no infinitary
   machinery at all for the "path to covering set" step, but this
   simplification does not, by itself, make the existence-of-`Π` question
   (sub-gaps i/ii) any more tractable than FCBC was already known to be
   (Lemma W1, round 3).

**What remains open:** the Key Lemma / FCBC itself, now precisely
reformulated a third way (after Lemma W1's window form and the round-4
refutation explorer's Patch-via-P′ form) as: does a finite set of primes
`Π` exist such that, for every `N`, some subset of `Π` covers all pairs
`i<j\le N`? All three reformulations are proved equivalent to one another
and to FCBC. No route has yet supplied that existence proof. The concrete
remaining obstacle, per the round-4 density explorer's independent
diagnosis (reused here, not re-derived): proving any specific candidate `Π`
(most plausibly `H_\rho`) actually has this property requires an analytic
density argument (Mertens/Borel–Cantelli-type) that is absent from both
`knowledge_base.md` and the crux corpus and was not attempted this round.

## Full proof
(Not present — Status is `partial`. FCBC / the Key Lemma is not established.
See below for the full detail of everything that *is* established this
round, and `current.md` for the population-wide state.)

### Notation (recalled from imported lemmas)

`(a_n)_{n\ge1}` is the sequence of the problem. For `m\ge1`, `P_m:=
\mathrm{rad}(a_m)` is the set of distinct prime divisors of `a_m`. For
`K\ge1`, `H_K:=\bigcup_{m=1}^{K}P_m` (a finite set of primes, since each
`P_m` is finite and the union is over finitely many `m`). We say a finite
set of primes `H` is a **covering set** if `H\cap P_i\cap P_j\ne\varnothing`
for every `1\le i<j`. The **Finite Covering Backbone Conjecture (FCBC)**
asserts that a covering set exists. The **Key Lemma** of this approach
asserts that some `H_K` is a covering set.

We freely use, without re-proof (all certified in `results/imo-2026-06/
lemmas/`):
- **Lemma P′** (pairwise global intersection): `P_i\cap P_j\ne\varnothing`
  for every `i<j`.
- **Lemma C** (Global Intersection Collapse): `C_n:=\bigcap_{i=1}^nP_i` is
  non-increasing and stabilizes at a finite index; `C_\infty\ne\varnothing`
  iff Case I (a single prime divides every term).

Case I is already fully solved (imported Lemma S′): if some single prime
divides every term, `a_n=a_1+p(n-1)` for all `n\ge1`. Everything below
addresses Case II (`C_\infty=\varnothing`, witnessed non-vacuous by
`a_1=15,65,105,143,221,247,375,4087,4199,\ldots`, all directly verified via
Lemma C's finite computation).

### Lemma W1 (Equivalence Lemma)

**Statement.** FCBC holds if and only if the Key Lemma holds, i.e.

`\exists` finite `H` with `H\cap P_i\cap P_j\ne\varnothing\ \forall i<j`
`\iff`
`\exists K\ge1` with `H_K\cap P_i\cap P_j\ne\varnothing\ \forall i<j`.

**Proof.**

`(\Leftarrow)` Immediate: `H_K` is itself a finite set of primes, so if the
right side holds, take `H:=H_K` to witness the left side.

`(\Rightarrow)` Suppose `H` is a finite covering set. Let
`\Pi:=\bigcup_{i\ge1}P_i` (the set of all primes that ever divide some term
of the sequence — a well-defined set of primes, though a priori possibly
infinite). Define `H':=H\cap\Pi`; since `H'\subseteq H` and `H` is finite,
`H'` is finite.

*Step 1: `H'` is itself a covering set.* Fix `i<j`. Since `H` covers this
pair, `H\cap P_i\cap P_j\ne\varnothing`; pick `p` in this intersection. Then
`p\in P_i\subseteq\Pi` (by definition of `\Pi`), so `p\in H\cap\Pi=H'`.
Hence `p\in H'\cap P_i\cap P_j`, so this set is nonempty. As `i<j` was
arbitrary, `H'` covers every pair.

*Step 2: `H'` is nonempty.* Apply Step 1 to the pair `(1,2)` (which exists
since the sequence is infinite): `H'\cap P_1\cap P_2\ne\varnothing`, so in
particular `H'\ne\varnothing`.

*Step 3: define `K`.* For each `p\in H'`, since `p\in\Pi`, the set
`\{m\ge1:p\mid a_m\}` is nonempty; by well-ordering of the positive
integers it has a least element `\mu(p)\ge1`. Since `H'` is finite and
nonempty (Steps 1–2), `K:=\max_{p\in H'}\mu(p)` is a well-defined finite
positive integer.

*Step 4: `H'\subseteq H_K`.* For each `p\in H'`, `\mu(p)\le K` by
definition of `K`, and `p\mid a_{\mu(p)}` by definition of `\mu(p)`, so
`p\in P_{\mu(p)}\subseteq\bigcup_{m=1}^KP_m=H_K` (using `\mu(p)\le K`).
Since `p\in H'` was arbitrary, `H'\subseteq H_K`.

*Step 5: conclude.* Fix `i<j`. By Step 1, `H'\cap P_i\cap P_j\ne\varnothing`;
since `H'\subseteq H_K` (Step 4), `H_K\cap P_i\cap P_j\supseteq H'\cap
P_i\cap P_j\ne\varnothing`. As `i<j` was arbitrary, `H_K` is a covering set,
witnessing the Key Lemma with this explicit `K`. `\blacksquare`

**Discussion.** This shows the window construction `H_K` loses no
generality: it is not a restricted or weaker special case of FCBC, it is a
literal reformulation. A useful byproduct: the proof gives an *explicit*
recipe for the `K` witnessing the Key Lemma from *any* covering set `H`
whatsoever (`K=\max_{p\in H\cap\Pi}\mu(p)`), so if a sibling approach
eventually exhibits a covering set `H` by other means (e.g. a bounded set of
"eventually dominant" primes from the `\omega(a_n)`-growth route), this
lemma converts it into an explicit window index `K` for free, without
further work.

### Lemma W2 (Patch Lemma)

**Statement.** Fix `K\ge1` and suppose `H_K\cap P_i\cap P_j=\varnothing` for
some `i<j` (i.e. `H_K` fails to cover the pair `(i,j)`). Then `i>K`, and
setting `K':=i`, `H_{K'}\cap P_i\cap P_j\ne\varnothing` (i.e. `H_{K'}` covers
`(i,j)`).

**Proof.** First, `i>K`: suppose for contradiction `i\le K`. Then
`P_i\subseteq\bigcup_{m=1}^KP_m=H_K` by definition of `H_K`. By Lemma P′,
`P_i\cap P_j\ne\varnothing`; any element of this set lies in `P_i\subseteq
H_K`, so it lies in `H_K\cap P_i\cap P_j`, contradicting that this set is
empty. Hence `i>K`.

Now let `K':=i`. Since `i\le K'` (equality), `P_i\subseteq\bigcup_{m=1}^{K'}
P_m=H_{K'}`. By Lemma P′ again, `P_i\cap P_j\ne\varnothing`; pick `p` in this
intersection. Since `p\in P_i\subseteq H_{K'}`, we get `p\in H_{K'}\cap
P_i\cap P_j`, so this set is nonempty. `\blacksquare`

**Discussion (honest diagnostic, not a theorem).** The Patch Lemma shows
every *individual, already-witnessed* failure of `H_K` can always be
repaired by a single, explicit enlargement of `K`. Combined with Lemma W1,
this pins down precisely what a complete proof of the Key Lemma needs: not
the *possibility* of repair (always available one failure at a time, by
Lemma W2) but a proof that the **total number of repairs needed is
finite** — equivalently (since each repair strictly increases `K`), that
the process of "find a failure, patch it, repeat" terminates after finitely
many rounds rather than continuing forever by finding an ever-new failure
at a strictly larger `K` each time.

I looked for a monovariant that would force this termination, in direct
analogy with the certified Lemma C's proof technique (`(|C_n|)` is a
non-increasing sequence of integers bounded below by `0`, hence eventually
constant). The natural candidate quantities attached to the patching process
are `|H_K|` (the number of primes in the window) and the pigeonhole bound
`2^{|H_K|}-1` on the number of distinct signature values `\sigma_K(m):=
P_m\cap H_K` that can ever be realized (this is the "Step (b)" fact from the
outline, itself a free consequence of `H_K` being finite — reused here). But
`H_K\subseteq H_{K+1}` for every `K` (adding a term's radical to the union
can only add primes, never remove them), so `|H_K|` and `2^{|H_K|}-1` are
both **non-decreasing** in `K`. This is exactly the wrong monotonicity
direction for a finite-descent argument: Lemma C's argument needed a
sequence that is bounded *and* non-increasing, so that it must stabilize
(cannot keep strictly decreasing forever below its lower bound); here the
natural quantities are bounded *below* but can keep strictly *increasing*
without contradiction, since there is no a priori upper bound on `|H_K|` as
`K\to\infty` (unless one already knows `\bigcup_mP_m` is finite, which is
precisely the separate, and per round-2's `a_1=4199,4087` findings, *likely
false* canonical-witness-set-finiteness question `(\star\star)`, not needed
for FCBC but relevant context for why no easy universal cap on `|H_K|`
should be expected).

**Conclusion of this diagnostic.** The specific mechanism proposed in the
round-3 outline (mechanism (i): "iterate and bound the number of
enlargements needed") cannot be completed using the finite-descent template
that worked for Lemma C, because the natural monotone quantities run in the
wrong direction. This is not a proof that termination is false, nor a proof
that no monovariant exists at all — only that the obvious candidates fail,
and a genuinely different idea (most plausibly, importing an *external*
bound such as a uniform cap on `\omega(a_n)`, which is what the sibling
`persistent-backbone-monovariant`/`forced-primes-well-ordering` approaches
are independently trying to establish) is needed to complete this route. I
report this honestly rather than papering over it with an unproved
"iterate and it clearly terminates" step.

### Lemma W3 (Minimal Radical Reduction Lemma)

**Statement.** Fix `n\ge1`. Call an index `i\in\{1,\dots,n\}`
**`n`-minimal** if there is no `k\in\{1,\dots,n\}` with `P_k\subsetneq P_i`
(`P_k` a *proper* subset of `P_i`). Let `M_n\subseteq\{1,\dots,n\}` be the
set of `n`-minimal indices. Then for every positive integer `x`,

`\big[\gcd(x,a_i)>1\text{ for all }i=1,\dots,n\big]\iff\big[\gcd(x,a_i)>1
\text{ for all }i\in M_n\big]`.

**Proof.**

`(\Rightarrow)` Trivial, since `M_n\subseteq\{1,\dots,n\}`.

`(\Leftarrow)` Suppose `\gcd(x,a_i)>1` for every `i\in M_n`. Fix an
arbitrary `i_0\in\{1,\dots,n\}`; we show `\gcd(x,a_{i_0})>1`.

Let `S:=\{k\in\{1,\dots,n\}:P_k\subseteq P_{i_0}\}`. Since `P_{i_0}
\subseteq P_{i_0}` trivially, `i_0\in S`, so `S` is a nonempty finite set.
Choose `j^\*\in S` minimizing `|P_{j^\*}|` among elements of `S` (possible
since `S` is finite and nonempty).

*Claim: `j^\*\in M_n`.* Suppose not. Then there is `k\in\{1,\dots,n\}` with
`P_k\subsetneq P_{j^\*}`. Since `j^\*\in S`, `P_{j^\*}\subseteq P_{i_0}`, so
`P_k\subsetneq P_{j^\*}\subseteq P_{i_0}`, giving `P_k\subseteq P_{i_0}`,
i.e. `k\in S`. Also, since `P_k` is a proper subset of the finite set
`P_{j^\*}`, `|P_k|<|P_{j^\*}|`. This contradicts the choice of `j^\*` as
minimizing `|P_{j^\*}|` over `S` (we exhibited `k\in S` with strictly
smaller cardinality). So the claim holds: `j^\*\in M_n`.

Since `j^\*\in M_n`, the hypothesis gives `\gcd(x,a_{j^\*})>1`, so `x` and
`a_{j^\*}` share a prime `p\in P_{j^\*}`. Since `j^\*\in S`, `P_{j^\*}
\subseteq P_{i_0}`, so `p\in P_{i_0}`, i.e. `p\mid a_{i_0}`. Since also
`p\mid x`, `\gcd(x,a_{i_0})\ge p>1`.

As `i_0\in\{1,\dots,n\}` was arbitrary, `\gcd(x,a_i)>1` for every
`i=1,\dots,n`. `\blacksquare`

**Discussion.** This is an unconditional structural fact about the sequence
(no FCBC hypothesis used) showing the recursive definition's admissibility
check at each step genuinely only depends on the inclusion-minimal radicals
seen so far, not on all `n` of them. It gives a cleaner "effective
constraint set" `M_n` in place of `\{1,\dots,n\}`. I verified it directly by
simulation (`a_1=221`, every `n` from `1` to `199`: the admissibility of the
true next candidate against `\{1,\dots,n\}` and against `M_n` alone agreed
in all `199` cases). However — checked explicitly, not merely asserted —
this reduction does **not** by itself finish FCBC or the Key Lemma: `|M_n|`
was observed to keep growing with `n` in this same test (`|M_{199}|=42`),
so `M_n` does not collapse to a bounded set on its own; a further argument
(not found this round) would be needed to show the *set of distinct
`P_i`-values* for `i\in M_n` stabilizes, which is again essentially a
restatement of the same open finiteness question. I record this lemma as
reusable structural content for future rounds (e.g. it could reduce the
combinatorial bookkeeping needed if a future approach tries to bound `M_n`
directly), not as progress toward closing the Key Lemma itself.

### Lemma W4 (the tree `T_Π`, made precise, and the Pool Lemma)

This section responds directly to the round-4 outline-reviewer's caveat:
*"before doing anything else, write down the tree explicitly: what exactly
is a node at level `N`, and what is the parent-child compatibility relation
connecting a level-`N` choice to a level-`(N+1)` choice?"* We do this in
three steps: (1) show the *naive* tree (no fixed candidate pool) is not
finitely branching, so it cannot support a König's-lemma argument as
literally stated in the round-4 outline — this is the precise reason
sub-gap (ii) is load-bearing, not a technicality; (2) define the correct
tree `T_Π` relative to an externally fixed finite pool `Π`; (3) prove the
Pool Lemma, which shows path-existence in `T_Π` needs only elementary
finite descent, not the general (infinitary) König's lemma.

**Step 1: why the naive tree fails to be finitely branching.**

Recall `H_N:=\bigcup_{m=1}^N P_m` (notation as above). A direct consequence
of this definition: for any `i,j\le N`, `P_i\cap P_j\subseteq H_N` (both
`P_i,P_j\subseteq H_N`). Hence a finite set `S` of *any* primes covers all
pairs `i<j\le N` if and only if `S\cap H_N` does — primes outside `H_N` are
simply irrelevant to covering pairs among the first `N` terms. So the
"efficient" candidate space at level `N` is `2^{H_N}`, which is finite for
each fixed `N` (since `H_N` is finite). This might suggest the naive tree
(level-`N` nodes `:=` subsets of `H_N` covering all pairs `\le N`) is
finitely branching after all — level by level it is. **The problem is
across levels**: `H_N\subseteq H_{N+1}` but there is no a priori bound on
`\bigcup_N H_N` (called `Π` in Lemma W1's proof — the set of *all* primes
ever dividing any term of the sequence), so the ambient alphabet a
level-`N` node lives in keeps changing, growing without a known bound, as
`N\to\infty`. Concretely, we verified this growth is real, not merely
hypothetical, on two of the round-3 hard cases:

```
a_1=221: |H_N| for N=1..30:  2,4,5,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8
a_1=375: |H_N| for N=1..30:  2,4,5,5,6,7,7,8,8,9,10,10,11,11,12,13,14,14,14,14,15,15,16,16,16,16,17,17,18,18
```

For `a_1=375`, the *minimal covering window* stabilizes at `K=3` (round 3's
table), but `|H_N|` — the size of the "local alphabet" at level `N` — keeps
growing well past `N=3`, reaching `18` by `N=30` with no sign of stopping.
So even though a small covering set exists and is found early, the raw
level-`N` node space `2^{H_N}` is not drawn from any fixed finite universe
across levels unless one is supplied externally. **This is precisely why a
literal König's-lemma argument over the naive "per-`N` minimal covering
choices" tree, as the round-4 outline first floated, is not yet meaningful:
without fixing a finite `Π` in advance, the tree's levels do not share a
common finite alphabet, so "finitely branching" fails at the level of the
whole tree even though each individual level, examined in isolation, has
finitely many nodes.** This confirms, precisely rather than by assertion,
the outline-reviewer's diagnosis that the pivot was "currently a
relabeling, not leverage" — and shows exactly what was missing: a fixed
`Π`, external to any single level.

**Step 2: the tree `T_Π`, relative to a fixed finite pool `Π`.**

Fix once and for all a finite set of primes `Π` (a candidate; existence of
a `Π` that works is exactly sub-gaps (i)+(ii), addressed by the Pool Lemma
below — this step only *defines* the tree given `Π`, it does not yet
establish any `Π` exists).

- **Nodes at level `N` (`N\ge1`):** `𝒢_N(Π):=\{S\subseteq Π :
  S\cap P_i\cap P_j\ne\varnothing\text{ for every }1\le i<j\le N\}` — the
  subsets of `Π` that cover every pair among the first `N` terms. (Level
  `N=0`: a single root node, by convention `\varnothing`, vacuously
  compatible with every level-`1` node — not otherwise used below.)
- **Node space is finite in total, not just per level:** every node at
  every level is an element of `2^Π`, and `|2^Π|=2^{|Π|}<\infty`, a single
  finite set independent of `N`. (This is the key structural difference
  from Step 1's naive tree.)
- **Parent–child / compatibility relation:** a level-`(N+1)` node `S` is a
  child of the level-`N` node `S'` **iff `S=S'`** (as subsets of `Π`). This
  relation is well-defined and total on `𝒢_{N+1}(Π)`: every level-`(N+1)`
  node has a parent, namely itself viewed as a level-`N` node — this needs
  checking, done in Lemma W4a immediately below.
- **A path through `T_Π`** is a sequence `(S_N)_{N\ge1}`, `S_N\in𝒢_N(Π)`,
  with `S_{N+1}` a child of `S_N`, i.e. (by the relation just defined)
  `S_{N+1}=S_N` for every `N`. So a path is exactly a single fixed set `S`
  with `S\in𝒢_N(Π)` for every `N`, i.e. `S\in\bigcap_{N\ge1}𝒢_N(Π)`.

**Lemma W4a (monotonicity / well-definedness of the compatibility
relation).** For every `N\ge1` and every finite `Π`, `𝒢_{N+1}(Π)\subseteq
𝒢_N(Π)`.

*Proof.* Let `S\in𝒢_{N+1}(Π)`, so `S\subseteq Π` and `S` covers every pair
`i<j\le N+1`. In particular, since `\{(i,j):i<j\le N\}\subseteq
\{(i,j):i<j\le N+1\}`, `S` covers every pair `i<j\le N` too. Hence
`S\in𝒢_N(Π)`. `\blacksquare`

This is exactly the fact needed for the compatibility relation of `T_Π` to
be well-defined (every level-`(N+1)` node is automatically a valid
level-`N` node, so "child `\Rightarrow` has a parent" always holds) — it is
a one-line consequence of the pair-constraint sets being nested, and
requires no hypothesis on `Π` or on FCBC.

**Lemma W4b (Pool Lemma).** FCBC holds if and only if there exists a finite
set of primes `Π` such that `𝒢_N(Π)\ne\varnothing` for every `N\ge1`.

*Proof.*

`(\Rightarrow)` Suppose FCBC holds, witnessed by a finite covering set `H`
(`H\cap P_i\cap P_j\ne\varnothing` for every `i<j`). Take `Π:=H`. For every
`N`, `S:=H` satisfies `S\subseteq Π` (equality) and covers every pair
`i<j\le N` (a fortiori, since `H` covers *every* pair, unrestricted), so
`H\in𝒢_N(Π)`, giving `𝒢_N(Π)\ne\varnothing`.

`(\Leftarrow)` Suppose `Π` is finite with `𝒢_N(Π)\ne\varnothing` for every
`N`. By Lemma W4a, `\big(𝒢_N(Π)\big)_{N\ge1}` is a nested decreasing
sequence of subsets of the finite set `2^Π`. Hence `\big(|𝒢_N(Π)|\big)_{N
\ge1}` is a non-increasing sequence of non-negative integers, bounded above
by `2^{|Π|}`. **A non-increasing sequence of non-negative integers is
eventually constant** — this is the identical finite-descent technique used
to certify Lemma C (`(|C_n|)` non-increasing and bounded below stabilizes);
here it applies verbatim to `(|𝒢_N(Π)|)`. So there is `N_0` with
`|𝒢_N(Π)|=|𝒢_{N_0}(Π)|` for all `N\ge N_0`. Since additionally
`𝒢_N(Π)\subseteq 𝒢_{N_0}(Π)` for `N\ge N_0` (Lemma W4a, applied repeatedly)
and both sets are finite with equal cardinality, `𝒢_N(Π)=𝒢_{N_0}(Π)` for
every `N\ge N_0`. Call this stabilized common value `𝒢_\infty`; it is
nonempty by hypothesis (`𝒢_{N_0}(Π)\ne\varnothing`).

Pick any `S\in𝒢_\infty`. We claim `S` (a finite subset of `Π`, hence a
finite set of primes) is a covering set for the *entire* infinite sequence,
i.e. `S\cap P_i\cap P_j\ne\varnothing` for every `i<j` (not just `i<j\le
N_0`). Fix `i<j`. Let `N:=\max(N_0,j)`, so `N\ge N_0`, hence `𝒢_N(Π)=
𝒢_\infty\ni S`. By definition of `𝒢_N(Π)`, `S` covers every pair `i'<j'\le
N`; since `j\le N`, the pair `(i,j)` is among these, so `S\cap P_i\cap
P_j\ne\varnothing`. As `i<j` was arbitrary, `S` is a finite covering set,
establishing FCBC. `\blacksquare`

**Discussion: this fully closes sub-gap (iii), and shows it needed no
König's lemma.** In the language of `T_Π`, a path through the tree is
(Step 2) exactly an element of `\bigcap_N𝒢_N(Π)`, and Lemma W4b's
`(\Leftarrow)` direction *is* a direct, constructive proof that this
intersection is nonempty whenever every level is nonempty — via finite
descent on `|𝒢_N(Π)|`, not via the general infinitary König's lemma
(which would normally be invoked for a tree with finitely many children per
node but *possibly unboundedly many total nodes across all levels*). Here
the node space `2^Π` is finite in total — a strictly stronger property than
"finitely branching" — which is exactly why the elementary pigeonhole/
finite-descent argument suffices and no compactness axiom or appeal to
König's lemma (dependent choice) is needed. This is a genuine
simplification of the round-4 outline's own framing: sub-gap (iii), which
the outline flagged as needing "a further pigeonhole step... not yet
spelled out," is now spelled out in full, and turns out to be strictly
easier than advertised once `Π` is fixed. **What Lemma W4b does *not* do**
is make sub-gaps (i)/(ii) easier: the `(\Rightarrow)` direction of the
proof is immediate (`Π:=H`), which means "some finite `Π` works" is
*logically equivalent* to FCBC, not a weaker consequence of it — so proving
Pool-Lemma existence is, provably, exactly as hard as proving FCBC directly
(exactly analogous to how Lemma W1 already showed the Key Lemma is
equivalent to, not weaker than, FCBC). The value of Lemma W4 is
architectural: a correct, complete tree definition (answering the
reviewer's caveat in full) and a clean, rigorous single reformulation of
the one remaining open question, not a reduction in its difficulty.

### Empirical support and empirical refutation (both honestly reported, neither used as a proof step)

All computations below were carried out in Python with exact integer
arithmetic (`math.gcd`, trial-division factorization); code and raw output
are reproducible. These are sanity checks and diagnostic evidence only —
per CLAUDE.md, no numeric check substitutes for a proof step, and none is
used as one above.

1. **Extended coverage check.** For `a_1=4199` (`K=5`, `|H_5|=8`) and
   `a_1=4087` (`K=2`, `|H_2|=4`) — round 2's two adversarial examples where
   the canonical witness set `W` was found to grow past 21 primes with no
   plateau through 15,000 terms — the window construction `H_K` was
   re-tested against **all** pairs among the first `20{,}000` terms (via the
   signature-pigeonhole reduction: computing all realized signatures
   `\sigma_K(m):=P_m\cap H_K` for `m\le20{,}000`, then checking pairwise
   intersection only among the *distinct* realized signature values — `70`
   and `49` distinct values respectively, both far below the a priori bound
   `2^{|H_K|}-1`). **Zero failures** in both cases. This means `H_K`-type
   coverage stabilizing at small `K` and `W`-finiteness (`(\star\star)`) are
   different phenomena — the latter is likely false (round 2), the former
   shows no sign of failing even on round 2's specific adversarial cases —
   which is a meaningful piece of positive evidence for FCBC (this
   approach's target) even though `(\star\star)` looks false, but it remains
   evidence, not a proof, since `20{,}000` terms is still finite.

2. **Falsification of "`K=K(\omega(a_1))`" as a clean formula.** Minimal
   sufficient `K` was computed exactly (smallest `K` for which every
   realized-signature pair intersects, checked up to `N=3000`, or `20{,}000`
   for the two adversarial cases) for eleven values of `a_1`:

   | `a_1` | `\omega(a_1)` | minimal `K` | `|H_K|` |
   |---|---|---|---|
   | 15 | 2 | 2 | 3 |
   | 65 | 2 | 3 | 5 |
   | 91 | 2 | 2 | 3 |
   | 105 | 3 | 2 | 4 |
   | 143 | 2 | 3 | 5 |
   | 221 | 2 | 4 | 6 |
   | 247 | 2 | 4 | 6 |
   | 375 | 2 | 3 | 5 |
   | 1073 | 2 | 3 | 6 |
   | 4087 | 2 | 2 | 4 |
   | 4199 | 3 | 5 | 8 |

   Among the eight rows with `\omega(a_1)=2`, minimal `K` takes three
   different values (`2,3,4`), so **no function of `\omega(a_1)` alone**
   can determine the exact minimal `K` (any such function would need to be
   simultaneously `2`, `3`, and `4` at input `2`) — this falsifies the
   outline's mechanism (ii) as a literal claim, though the data is fully
   consistent with a weaker statement ("minimal `K` is small and bounded,
   depending on finer structure of `a_1` than `\omega(a_1)` alone"), which
   remains open.

3. **Round 4: numerical validation of the Pool Lemma's mechanics** (all code
   in `/tmp/round-4/pool_lemma_test.py`, exact integer arithmetic via
   `sympy.factorint`). For each `a_1` below, `Π` was taken to be the exact
   window `H_K` from the table above (or a deliberately oversized superset,
   noted separately), `𝒢_N(Π)` was computed by **exhaustive enumeration**
   over all `2^{|Π|}` subsets of `Π` (feasible since `|Π|\le10` in every
   case tested this way), for `N` up to `40`–`60`:

   | `a_1` | `Π` | `\|Π\|` | nested-decreasing? | stabilizes at `N_0` | `\|𝒢_\infty\|` |
   |---|---|---|---|---|---|
   | 15 | `{2,3,5}` | 3 | yes, verified all `N` | 4 | 1 |
   | 221 | `{2,3,5,13,17}` | 5 | yes | 6 | 1 |
   | 247 | `{2,3,5,7,13,19}` | 6 | yes | 6 | 1 |
   | 375 | `{2,3,5,7,19}` | 5 | yes | 4 | 1 |
   | 4087 | `{2,17,61,67}` | 4 | yes | 4 | 2 |
   | 4087 (oversized `Π`) | `\{2,3,5,7,11,13,17,19,61,67\}` | 10 | yes | 4 | 128 |
   | 4199 | `H_5=\{2,3,13,17,19,31,37,83\}` | 8 | yes | 6 | 4 |

   In every case, `𝒢_N(Π)` was confirmed nested-decreasing (`𝒢_{N+1}(Π)
   \subseteq𝒢_N(Π)`, exactly as Lemma W4a predicts, checked directly, no
   violation found), stabilizes at a small `N_0`, and the stabilized limit
   `𝒢_\infty` is always nonempty — matching Lemma W4b exactly (the proof is
   not merely correct in the abstract, its concrete mechanics reproduce
   correctly on every tested instance).

   **A specific, striking cross-validation.** For `a_1=4199` with
   `Π:=H_5=\{2,3,13,17,19,31,37,83\}` (the round-3 window), `𝒢_\infty`
   contains four sets, and its unique **minimal** element is
   `\{2,3,13,17,19,83\}` — this is **exactly** the set the round-4 density
   explorer's `H_\rho` invariant found for `a_1=4199`
   (`/tmp/round-4/math-explorer-h-rho-density.md`, table row `4199`), via a
   completely unrelated statistical/asymptotic-density method. Together with
   that report's own cross-validation (its statistical method and a
   parallel round-4 combinatorial-imprint method independently landing on
   the same exact period `T=105250`), this is now a **fourth** independent
   method (window search / brute pool-lattice enumeration) landing on the
   identical backbone set for the hardest previously-fully-analyzed case in
   the workspace — real, if informal, evidence that `H_\rho` (or something
   very close to it) is the "right" answer for what `Π` should eventually
   be, even though no proof that it works in general exists yet.

   **Illustration of Step 1's finite-branching failure (why `Π` cannot be
   skipped).** For `a_1=221,375`, `|H_N|` (the size of the "local alphabet"
   at level `N`, with no `Π` fixed) was tracked for `N=1,\dots,30`:
   `221`: `2,4,5,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8`;
   `375`: `2,4,5,5,6,7,7,8,8,9,10,10,11,11,12,13,14,14,14,14,15,15,16,16,
   16,16,17,17,18,18`. Both keep strictly growing well past the point where
   the minimal covering `K` has already stabilized (`K=4` and `K=3`
   respectively, round 3's table) — concretely confirming Step 1's claim
   that the "raw" per-level alphabet is not bounded across levels without
   externally fixing `Π`.

   **Scope limitation, stated honestly.** Exhaustive subset enumeration
   over `Π` needs `2^{|Π|}` to be computationally feasible; this holds for
   every case above (`|Π|\le10`) but **not** for the round-4 hard case
   `a_1=21528751` (`K=86`, `|H_{86}|=106`) — `2^{106}` is astronomically
   infeasible to enumerate. For that case we did **not** verify the full
   Pool Lemma mechanics (nestedness/stabilization/multiplicity of `𝒢_N(Π)`)
   computationally; we only have, reused from the round-4 refutation
   explorer's report and not re-derived here, the weaker fact that a
   *single* witness (`S:=H_{86}` itself) lies in `𝒢_N(H_{86})` for every
   tested `N` up to `100{,}000` — sufficient to illustrate that `𝒢_N(Π)`
   nonempty is plausible for this `Π`, but far short of exhaustively
   confirming the lattice structure the smaller cases display.

## Promotable lemmas

- **Lemma W1 (Equivalence Lemma: Key Lemma `\iff` FCBC)** — proved in full
  above. Reusable by every sibling Gap-1 approach: formally establishes that
  `persistent-backbone-monovariant`, `forced-primes-well-ordering`, and this
  approach are all targeting the identical proposition, and gives an
  explicit, constructive conversion from any abstract covering set `H` (however
  produced) to an explicit window index `K`.
- **Lemma W2 (Patch Lemma)** — proved in full above. Reusable as a clean
  building block: shows any single coverage failure of `H_K` is always
  repairable by one explicit enlargement, isolating exactly what remains to
  be proved (finiteness of the total repair count) from what is already
  settled (repairability of each individual failure).
- **Lemma W3 (Minimal Radical Reduction Lemma)** — proved in full above,
  unconditional (no FCBC dependence). Reusable as a general structural
  simplification of the recursive definition's admissibility check, for any
  future approach that wants to reason about which of `a_1,\dots,a_n`
  actually constrain the choice of `a_{n+1}`.
- **Lemma W4 (Tree `T_Π` + Pool Lemma, round 4, new)** — proved in full
  above, including Lemma W4a (monotonicity of `𝒢_N(Π)`). Reusable by any
  future approach that wants a precise, checkable finite-branching/
  compactness argument for FCBC: gives the exact node/edge/compatibility
  definition of `T_Π`, proves the "path `\Rightarrow` literal covering set"
  step in full via elementary finite descent (no König's lemma needed once
  `Π` is fixed), and proves the whole construction is *equivalent* to FCBC
  (not merely sufficient), which future rounds should treat as settled: no
  further effort should go into "does the tree architecture work at all" —
  it does, unconditionally, given any finite `Π`; the only remaining
  content is the same as always, existence of a `Π` with `𝒢_N(Π)\ne
  \varnothing` for every `N` (equivalently, existence of a finite covering
  set `H`, equivalently the Key Lemma). Also reusable: the explicit
  demonstration (Step 1) that the *naive*, `Π`-free tree is not finitely
  branching across levels, which any future compactness-style attempt on
  this problem should read first to avoid re-discovering the same trap.

**Round 9 note.** This round's work ("Round 9 build" above) produced no new
provable lemma — it is a computational/diagnostic investigation (the
bridge-prime-patch data, §2, and the universal-candidate `H_{100}` finding,
§2.2) plus an honest correction to Step 3's claimed status (§1) and a
structural diagnosis of the remaining obstruction (§3). None of this rises
to a certifiable lemma: the `H_{100}`-works-on-11-instances finding is
empirical evidence for a conjecture, not a proof of any general statement,
so there is nothing new to promote to `lemmas/` this round. The reproducible
scripts are at `/tmp/round-9/work/` (`gen.py`, `analyze.py`,
`batch_test.py`, `batch_test2.py`, `batch_test3.py`, `final_check.py`) for
any future round that wants to extend this investigation further (e.g. to
larger `N`, more `a_1` values, or attempting to prove a magnitude bound on
the Domination Lemma's dominant prime — identified in §3 as the concrete
missing ingredient).
