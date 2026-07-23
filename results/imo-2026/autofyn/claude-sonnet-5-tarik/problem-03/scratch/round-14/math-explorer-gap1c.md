## imo-2026-03 — Gap 1c (MATCH-vs-DEL/KEEP existence)

### Setup used (verified against the file's own definitions and worked examples)
Implemented `OPT_sigma(C,W)` directly from `potential-weighting-upper-bound.md` §13.2/§17.2's own
recursive trichotomy (DELETE/KEEP/MATCH on `W`'s top element `w1`, full slack, no crossing
restriction anywhere in this framework — confirmed `\mathcal F`'s own Claim A never invokes
`TAGGED`/crossing at all, only raw `OPT_sigma`). Cross-checked this recursive definition against an
independent, from-scratch, fully brute-force enumeration of every `(K,D,M)` selection (no
recursion) — **200/200 exact match** — before trusting it for anything below. Reproduced the file's
own base-generator machinery (`A_1`, `A_{3,l}`, trigger `M<A_1`, global argmin `k^*`) and the
DELETE/KEEP closure that generates `\mathcal F`, from the prose in §17.2, independently coded (not
reusing any prior round's harness). All computation this round: exact Python integers, bounded
`q\le8`, `v_{\max}\le7`, closure depth `\le7` — no unbounded search. Code at `/tmp/round-14/work/`.

### What I found (new, positive)

**1. A strictly sharper, per-partner form of Gap 1c holds within `\mathcal F` (not just the
aggregated min-over-partners form already on file).** Tested directly: for every node
`(C,W,\sigma)\in\mathcal F` with `|W|\ge2`, and for **every individual match partner** `w_m\in
W\setminus\{w_1\}` (not just the value-minimizing one), `\mathrm{MATCH}_m` never strictly beats
`\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})`. Split by sign (the two signs need different
witnessing branches, matching the file's own Sign-Determined DEL/KEEP-Suffices lead, round 13):
- `\sigma=+1`: `\mathrm{DEL}\le\mathrm{MATCH}_m` for **every** `m` — `1336/1336` checks, `0`
  violations (base generators + DELETE/KEEP closure to depth `5`–`7`, several `(v_{\max},q_{\max})`
  batteries).
- `\sigma=-1`: `\mathrm{KEEP}\ge\mathrm{MATCH}_m$ for every `m` — `180/180` checks, `0` violations
  (this sign is much rarer in `\mathcal F`, matching the file's own observation that `\sigma=+1`
  dominates).
This is genuinely stronger than what's needed for Claim A (which only needs the *aggregated*
min-over-`m`), and it removes the need to ever identify or track *which* partner is optimal — a
useful simplification for a direct-construction proof, since "any partner works" as the
non-matching-alternative witness.

**2. A clean two-step decomposition of the `\sigma=+1` case, isolating the ENTIRE hard content into
one much narrower sub-claim.** Writing `d:=w_1-w_m`, `X:=\mathrm{rest}\setminus\{w_m\}` (i.e. `W`
with *both* `w_1` and `w_m` removed):
```
MATCH_m = OPT_{+1}(C\cup\{d\}, X)
        >= OPT_{+1}(C, X)              [Step A: general "shrink-the-list" monotonicity]
        >= OPT_{+1}(C, rest) = DEL     [Step B: same monotonicity lemma, applied to remove w_m]
```
- **Step A/B is a single, fully GENERAL lemma, essentially free to prove**: for *any* background
  `C`, list `W`, sign `\sigma`, and any `x\in W`, `\mathrm{OPT}_{+1}(C,W)\le\mathrm{OPT}_{+1}(C,
  W\setminus\{x\})` (mirror `\ge` at `\sigma=-1`). **One-line bijection proof**: the map "take an
  optimal selection of `W\setminus\{x\}$, additionally delete `x`" is a value-preserving injection
  from selections of `W\setminus\{x\}` into selections of `W`, so the min over the bigger space is
  `\le` the value achieved via this specific subspace. **Verified independently, `0/14160`+
  violations on fully arbitrary `(C,W)`, no `\mathcal F`-restriction needed at all** — this is a
  genuinely new, general, essentially-provable-on-the-spot lemma, reusable well beyond Gap 1c.
- **The remaining "half-step" — `\mathrm{OPT}_{+1}(C\cup\{d\},X)\ge\mathrm{OPT}_{+1}(C,X)` — is
  where ALL of Gap 1c's real difficulty concentrates.** Tested this in isolation, restricted to
  genuine `\mathcal F`-provenance `(C,W,\sigma{=}{+}1)` and the specific `d=w_1-w_m`: **`0`
  violations across `3400+` checks** (multiple independent batteries, `v_{\max}=3,4,6,7`, `q_{\max}
  =5,6,7`, closure depth up to `7`). **Decisively FALSE as a general (non-`\mathcal F`) fact, even
  keeping the exact structural relation `d=w_1-w_m` intact**: `2734/18068` violations (`\sim15\%`)
  on arbitrary `(C,W)` — e.g. `C=[7],W=[5,3]$: `d=2`, `\mathrm{OPT}_{+1}([7],[3])=7$ vs
  `\mathrm{OPT}_{+1}([7,2],[3])=5<7`. So this really is the load-bearing, `\mathcal F`-specific
  content — a clean, much narrower target than the raw MATCH-vs-DEL/KEEP comparison, with the
  "which branch wins" bookkeeping and the DEL-side monotonicity now fully discharged for free.

**3. Ruled out two cheap sufficient conditions for the half-step (both tested, both fail),
narrowing what the real mechanism must be.** (i) "`d` dominates `C`" (`d\ge\max(C)`) is NOT
sufficient — `695/4000` violations even with `d\ge\max(C)` (e.g. `C=[8],d=8`: exact duplicate,
`e([8,8])=0<8=e([8])`, so pure domination doesn't prevent cancellation). (ii) A hand-inspected
counterexample to the general (non-`\mathcal F`) half-step (`C=[7],W=[5,3]`, `d=2`) shows the
failure is NOT a near-cancellation/duplicate-collision phenomenon at all — `d=2` is nowhere near
`C=\{7\}` — rather it is a plain rank/parity-of-insertion effect on the raw alternating sum `e`
(inserting `d` at an odd rank from the top of `C` subtracts it, generically lowering `e`). This
means the correct sufficient condition `\mathcal F` must be supplying is almost certainly a
**positional/ordering constraint on where `d` (and `C`'s other element) falls relative to the
current working list `X`**, not a magnitude-domination or anti-cancellation condition — structurally
the same flavor of fact as the already-flagged **No-Gap Lemma** (Gap 1a) and the **Coincidence
Identity** (`d_i-d_l=z_l-z_i`, §20.1), which also pin down *where* a derived background value can
sit relative to the list. **This is a genuine, previously-unstated structural link between Gap 1a's
mechanism and Gap 1c's real content** — worth testing directly next round (does the No-Gap property,
or a generalization of it propagated through DELETE/KEEP closure, directly imply the half-step
lemma?).

### Cheap-kill / pruning notes
- The per-partner reformulation (finding 1) is a genuine simplification: a proof no longer needs to
  identify the argmin match partner — proving the half-step lemma for an *arbitrary* `w_m\in
  \mathrm{rest}` suffices, symmetric in `m`.
- Step A/B (the general shrink-list monotonicity lemma) should be written up and certified
  immediately — it is free, general-purpose, and reusable (it was NOT on file before this round;
  neither `lemmas/insertion-and-cascade-facts.md`'s Fact 4 nor the Rank-Extraction identity states
  this one-sided monotonicity explicitly, though it is consistent with / easily derivable alongside
  them).
- Ruling out "`d` dominates `C`" as sufficient (finding 3(i)) saves a future builder from trying the
  most obvious shortcut first.

### On the crux-corpus "extremal witness + secondary tie-break + local rewrite" shape
Re-examined `aimo-0960` (minimal-length + lex-least exponent multiset, kill a repeat via the
`2\psi^e=\psi^{e-2}+\psi^{e+1}$ rewrite, contradicting lex-minimality), `aimo-0438` (max a secondary
alignment statistic `N` among edge-maximal partitions, a degree-preserving delete-one/add-one swap
strictly raises `N`, contradiction), `aimo-0666` (leximinimal class-size vector, a recoloring that
would shrink an earlier class is forbidden, giving a local neighbor constraint). **This round's
finding suggests the extremal/contradiction machinery may not be needed for the `\sigma=+1` branch
at all**: the two-step decomposition above (findings 1-2) is a **direct, constructive** argument
(chain two inequalities, no contradiction, no secondary extremal criterion) — closer in flavor to
`aimo-0960`'s own *forward* construction lemmas (the "Recover integer coordinates..." /
"Collapse a linear form..." cruxes for that same problem, which are direct algebraic identities, not
the extremal-rewrite crux) than to the extremal-rewrite crux itself. **Recommendation: attempt the
direct two-step chain (finding 2) to completion first; fall back to an `aimo-0960`/`aimo-0438`-style
extremal-witness argument only if the half-step lemma itself resists direct proof** (e.g. if it turns
out to need its own case split that an extremal secondary criterion would simplify).

### Dead ends this round (do not retry)
- General (provenance-free) per-partner claim at `\sigma=+1` (`\mathrm{DEL}\le\mathrm{MATCH}_m`
  for arbitrary `C,W`) — FALSE, `1572/14245$ (`\sim11\%`) violations, e.g. `C=[10],W=(6,2,3,5,0)`,
  `\mathrm{DEL}=5$, matching to `0` gives `4<5`. Confirms (again) that `\mathcal F`-provenance is
  essential, consistent with every prior round's finding on this problem.
- General background-insertion monotonicity `\mathrm{OPT}_{+1}(C\cup\{d\},W)\ge\mathrm{OPT}_{+1}(C,
  W)` for arbitrary `d` — FALSE, `817/4000` violations (duplicate-cancellation, e.g. `C=[7],d=7`).
  Already somewhat expected from Lemma P, but worth having on record as the reason the naive
  "background monotonicity" shortcut cannot be a free general lemma.
- "`d\ge\max(C)`" as a sufficient condition for the (still-open) half-step lemma — FALSE,
  `695/4000` violations (see finding 3(i)). Do not propose this as a shortcut.

### Recommended next step for the proof-outliner
1. **Certify the general shrink-list monotonicity lemma** (finding 2, Step A/B) — it is free, proven
   by a one-line bijection argument, and should go into `lemmas/` regardless of what happens to Gap
   1c, since it is reusable.
2. **Retarget Gap 1c's `\sigma=+1` build task to the isolated half-step lemma**
   (`\mathrm{OPT}_{+1}(C\cup\{w_1-w_m\},X)\ge\mathrm{OPT}_{+1}(C,X)` for `\mathcal F`-provenance
   `C`, any partner `m`) rather than the raw MATCH-vs-DEL/KEEP comparison — it is a strictly
   narrower, better-isolated, and (per the per-partner corroboration) at least as strong a target.
3. Investigate the flagged **No-Gap/Coincidence-Identity connection** (finding 3(ii)) as the most
   promising proof mechanism — both are positional facts about where a derived background value can
   sit relative to the current list, and both ultimately trace back to `k^*`'s *global* argmin
   property (not yet directly used in either). A single unified positional lemma might close both
   Gap 1a and this half-step form of Gap 1c at once.
4. The `\sigma=-1` mirror (`\mathrm{KEEP}\ge\mathrm{MATCH}_m`) was corroborated (`180/180`) but NOT
   decomposed this round — attempting the analogous two-step chain there is a cheap next probe
   (though the KEEP branch's own recursive form, `w_1-\mathrm{OPT}_{-1}(C,\mathrm{rest})`, does not
   obviously admit the same simple monotonicity chain and may instead connect to the already-flagged
   Sum Bound, §19.5(a) — worth checking directly whether the `\sigma=-1` half-step is literally
   implied by Gap 1b's Sum Bound plus Step A/B, before treating it as independent new content).

### Small-case / intuition notes (all labeled conjecture — computational corroboration only)
- The per-partner strengthening and the two-step decomposition are both **conjectures with strong
  computational support** (3400+ to 18000+ checks per finding, zero violations within `\mathcal F`,
  clear and reproduced violations the instant `\mathcal F`-provenance is dropped) — not proofs.
- The suspected link to No-Gap/Coincidence Identity is a **structural hypothesis**, not yet tested
  directly (no code this round establishes the half-step lemma actually follows from No-Gap) —
  flagged as the concrete next computational/proof experiment, not a finding in itself.
