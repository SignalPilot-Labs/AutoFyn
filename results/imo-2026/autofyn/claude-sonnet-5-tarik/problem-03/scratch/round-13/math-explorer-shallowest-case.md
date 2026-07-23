## imo-2026-03 (potential-weighting-upper-bound, Gap 1 / Claim A — shallowest-case attack)

### Setup reconstructed by hand (do not guess — traced from §17.2/§18.2/§18.3 exactly)

Base generator (§17.2 item 1, sharpened by §18.3): `B_0` is a **single** value `b_0` (never
`\emptyset`), `Z_0=(z_1\ge\dots\ge z_q)`, trigger `M<A_1` with `M=A_{3,k^*}=\min_l A_{3,l}`, `k^*` a
global argmin. `B_1:=\{b_0,\,d_{k^*}\}` (`d_{k^*}:=z_1-z_{k^*}\ge0`), `Z_1:=Z_0\setminus\{z_1,
z_{k^*}\}`, and `(B_1,Z_1,+1)` is the shallowest (`depth 0`) member of `\mathcal F`. `|B_1|=2`
always (never 0 or 1) by §18.3.

At this node, `w_1:=\max(Z_1)`. Write `h:=|\{x\in B_1: x\ge w_1\}|\in\{0,1,2\}`,
`C_{\mathrm{lo}}:=\{x\in B_1: x<w_1\}`. By the Background-Splitting Corollary (already certified,
`lemmas/empty-background-and-background-splitting.md`), Claim A at `(B_1,Z_1,+1)` holds **iff** it
holds at `(C_{\mathrm{lo}}, Z_1, (-1)^h)`:
- `|C_{\mathrm{lo}}|=0` (`h=2`, both `b_0,d_{k^*}\ge w_1`): **already fully closed** (Empty-Background
  Lemma).
- `|C_{\mathrm{lo}}|=1` (`h=1`, exactly one of `b_0,d_{k^*}\ge w_1`): reduces to Claim A at
  `(\{c\},Z_1,-1)` where `c:=\min(b_0,d_{k^*})<w_1` is whichever of the two is dominated. **This is
  the shallowest genuinely non-trivial node — the object of this report.**
- `|C_{\mathrm{lo}}|=2` (`h=0`, neither dominates `w_1`): reduces to Claim A at `(B_1,Z_1,+1)`
  itself with no size reduction (both elements survive) — the harder, "next depth" case.

So the smallest non-trivial concrete instance is precisely: **single background element `c<w_1:=
\max(W)`, sign `\sigma=-1` (maximize), prove `\mathrm{OPT}_{-1}(\{c\},W)` has an optimal witness not
matching `w_1`.**

### What I found (all computation: exact-integer Python, brute force over the full finite selection
space via `all_selections`, archived in `/tmp/round-13/work/`)

**1. The `|C_{\mathrm{lo}}|=1` case appears to be an UNCONDITIONAL, provenance-free fact — a
genuinely new general lemma candidate, not yet proved.** For **arbitrary** `c\ge0`, **arbitrary**
sorted `W` with `c<w_1:=\max(W)` (no tie to any trigger/argmin provenance at all):
`\mathrm{OPT}_{-1}(\{c\},W)` always has an optimal witness not matching `w_1`. **`0/5961`
violations** (`q=1,\dots,7`, entries `0`–`20`), on top of an earlier `0/2949` run (`q\le6`,
entries `0`–`12`). This is a materially stronger and more useful statement than what Gap 1 strictly
needs (which only requires it for `c\in\{b_0,d_{k^*}\}` under `\mathcal F`-provenance) — if provable
in this fully general form, it unconditionally disposes of the entire `|C_{\mathrm{lo}}|=1` branch
everywhere it occurs in the recursion (base generator and every deeper node), no provenance argument
needed at all.

**2. Sharp, decisive contrast: the analogous `|C_{\mathrm{lo}}|=2` case is FALSE for arbitrary
(non-`\mathcal F`-provenance) dominated backgrounds, at a non-trivial rate.** Testing **exactly**
`|C|=2`, both elements `<w_1=\max(W)` (i.e. genuinely inside the residual `C_{\mathrm{lo}}\ne\emptyset`
regime, at the exact size Gap 1's hardest case needs), `\sigma=-1`: **`75/2996`** (`\approx2.5\%`)
trials have `\mathrm{OPT}_{-1}(C,W)` with **no** optimal witness avoiding a match on `w_1` — i.e.
Claim A genuinely **fails** for generic (non-provenance) 2-element dominated backgrounds. Minimal
example: `C=\{2,4\},W=(5,3)`: `\mathrm{OPT}_{-1}(\{2,4\},(5,3))=4`, achieved only by matching
`w_1=5` to `3` (giving `2`, multiset `\{4,2,2\}`, `e=4`); the only non-matching options are `KEEP`
(`e(\{2,4,5,3\})=5-4+3-2=2`) and `DEL` (`e(\{2,4,3\})=4-3+2=3`), both `<4`. Directly reproduced and
hand-verified (`e(\{4,2,2\})=4-2+2=4`, correct). **This sharpens round 12's own §18.5 finding**
("arbitrary same-size backgrounds violate Claim A readily") to the *exact* residual regime Gap 1
lives in (`C` entirely dominated by `w_1`, the only case left open after Background-Splitting) —
confirming genuine `\mathcal F`-provenance (the `b_0`/`d_{k^*}` global-argmin ancestry) is doing
real, load-bearing work specifically at `|C_{\mathrm{lo}}|=2`, not merely at unrestricted/undominated
background sizes.

**Net structural picture (new, precise, not previously isolated this cleanly):** Gap 1's open content
splits sharply by `|C_{\mathrm{lo}}|`: **`0` closed (old), `1` looks unconditionally true and
provenance-free (new conjecture, strong computational support, no proof yet), `2` is genuinely
provenance-dependent and the sole remaining hard case** — every failure mode found lives at `|C|=2`
(or higher), never at `|C|=1`, in every test I ran (including with `|C|` up to 3, arbitrary
magnitude). This directly answers the dispatch's flagged question about a parallel explorer's
"can `|C_{\mathrm{lo}}|` actually be 1" doubt: **yes, `|C_{\mathrm{lo}}|=1` is a real, reachable case
(`h=1` requires exactly one of `b_0,d_{k^*}` to dominate `w_1:=\max(Z_1)` and the other not — nothing
in the base generator's definition prevents this, and it is the "easy" case, not a vacuous one) —
but it turns out to be the *easier* of the two remaining cases, not the hard one**; the entire hard
content of Gap 1 concentrates at `|C_{\mathrm{lo}}|=2`.

### Attempted proof for `|C_{\mathrm{lo}}|=1` — got partway, then stuck; exact location of the gap

**Promising but ultimately insufficient mechanism (a genuine partial result, not a full proof):**
Whenever the TRUE optimal witness `\eta^*` of `\mathrm{OPT}_{-1}(\{c\},W)` matches `w_1` to some
`w_m`, replacing that one matched pair by *keeping both* `w_1` and `w_m` (leaving `\eta^*`'s
treatment of everything else unchanged) never decreases the value: **`0/4000`** violations
(`q=2,\dots,7`). This alone would give a one-line proof (swap-and-you're-done) **if** the underlying
per-selection inequality held for *every* candidate selection of the rest, not just the actual
optimum — **but I showed by direct counterexample that it does NOT**: for an *arbitrary* (not
necessarily optimal) selection `\tau'` of `W\setminus\{w_1,w_m\}`, writing `R:=\mathrm{vals}(\tau')`,
`N:=\{c\}\cup R`, the pointwise claim `e(N\cup\{w_1,w_m\})\ge e(N\cup\{w_1-w_m\})` is **false in
general**, even restricted to exactly this setting (`w_1=\max(W)`, `N` built from a genuine sorted-list
selection): **`7194/38916`** violations found (e.g. `C=\{6\}`, `W=(37,34,27,5,5,2,1)`, matching index
`m=2` i.e. `w_m=27`: for `\tau'=` keep `\{34,5,5,2\}`, delete `1`, match-value multiset
`\{6,34,5,5,2,10\}` gives `e=28` but keep-keep multiset `\{6,34,27,5,5,2,37\}`... — direct
computation: match-sorted `[34,10,6,5,5,2]\Rightarrow e=28`; keepkeep-sorted
`[37,34,27,6,5,5,2]\Rightarrow e=26<28`). **So the swap only works when applied to the actual
`\mathrm{MATCH}`-branch optimizer's own optimal `\tau'` for that specific sub-problem, not to a
generic candidate — meaning the "obvious" one-line witness-exchange argument does not generalize
into a real proof by itself; a genuinely value-level argument (bounding
`\mathrm{OPT}_{-1}(\{c,w_1-w_m\}, W\setminus\{w_1,w_m\})`, which already optimizes over `\tau'`,
against `\max(\mathrm{DEL},\mathrm{KEEP})`) is still needed, not a pointwise trick.** This is exactly
the same difficulty class the file's own §18.4 diagnosis already identified for the general case
(FSI similarly fails because it's a value/witness-optimum fact, not decomposable pointwise) — this
round's contribution is showing precisely *where* the natural simplification attempt for the
smallest case breaks, not merely re-asserting the general difficulty.

**A partially-worked value-level reduction (recorded for the next attempt, not completed):** Using
the Rank-Extraction identity to pull `w_1` out of the "keep-keep" multiset (valid since, when
`C=\{c\}` with `c<w_1` and `R` arises from `W\setminus\{w_1,w_m\}\subseteq W$, every element of
`\{c\}\cup R\cup\{w_m\}$ is `\le w_2\le w_1`, so `w_1` is the true max), one gets
`e(\{c,w_1,w_m\}\cup R)=w_1-e(\{c,w_m\}\cup R)`. Chaining this against `\mathrm{KEEP}=w_1-
\mathrm{OPT}_{+1}(\{c\},W\setminus\{w_1\})` (a *minimization*, so **any** particular `\{c,w_m\}\cup R`
value is `\ge` that minimum) gives `e(\{c,w_1,w_m\}\cup R)\le\mathrm{KEEP}` for every `R` — true but
useless by itself (it only re-proves keep-keep can't beat the KEEP branch, not that it beats
MATCH). The needed inequality is in the *other* direction and does not fall out of this move; I
tried reducing it to a pure numeric fact `w_1\ge e(N\cup\{w_m\})+e(N\cup\{w_1-w_m\})` for
`N=\{c\}\cup R` (all entries `\le w_1`) — this abstraction is **also false in general**
(`5859/50000` violations, e.g. `w_1=14,w_m=13,N=\{13,14,12,7\}`: `14 < e(N\cup\{13\})+e(N\cup\{1\})
=16`) — confirming the sortedness/matched-pair provenance of `R` (not just its numeric bound by
`w_1`) is doing real work that a purely numeric relaxation destroys; any future proof attempt must
keep `R`'s structural origin (a genuine `K/D/M` selection of a *sorted descending* sub-list) intact,
not abstract it away to "any bounded multiset."

### Recommendation for next round (not a plan, just what the evidence points to)

- Treat `|C_{\mathrm{lo}}|\in\{0,1\}` as the "easy" regime (0 closed; 1 has very strong, seemingly
  provenance-free computational support and deserves a dedicated proof attempt — it may be provable
  as a clean, general, reusable lemma independent of `\mathcal F`, since it held for fully arbitrary
  `c,W`, not just genuine base-generator values).
- Concentrate all remaining proof effort on `|C_{\mathrm{lo}}|=2`, and treat the
  provenance-dependence there as real and unavoidable (§18.5's finding, now sharpened): any proof
  attempt must use the specific relationship `b_0`/`d_{k^*}` (in particular `d_{k^*}$'s *global*
  argmin-over-all-`l`property, per the file's own final remark) rather than any size- or
  domination-only argument.
- Do **not** try to prove `|C_{\mathrm{lo}}|=1` via the naive "swap the matched pair for keep-keep,
  pointwise over all candidate rests" route — it is now shown false at the pointwise level (not just
  "not yet tried"); any proof needs to compare *optimal* values of the MATCH sub-problem against
  `\max(\mathrm{DEL},\mathrm{KEEP})` directly, using the actual `\mathrm{OPT}` structure (e.g. maybe
  by induction on `|W|` restricted to this single-background-element family, treating the
  `|C|=2$-sub-background that MATCH's own recursion produces, `\{c,d_m\}`, as a *fresh* instance of
  the harder `|C_{\mathrm{lo}}|=2$ case — i.e. `|C_{\mathrm{lo}}|=1$'s proof may not be independent of
  `|C_{\mathrm{lo}}|=2$'s after all, since the recursion inside MATCH regenerates a 2-element
  background; this is a real, currently-unresolved circularity concern worth flagging to the
  outliner).

### Cheap-kill / structural note

The `|C_{\mathrm{lo}}|=1\Rightarrow|C_{\mathrm{lo}}|=2$-inside-MATCH observation above (the MATCH
branch of a 1-element-background node has its own background `\{c,d_m\}`, size 2) suggests the
"depth-0 to depth-1" bootstrap the dispatch asked about does **not** trivially work in the direction
hoped (small case first): proving `|C_{\mathrm{lo}}|=1` might *require* already knowing
`|C_{\mathrm{lo}}|=2`'s hard case, at least for the MATCH branch's own sub-values, not the reverse.
This should be checked carefully before committing an outline to a "prove size 1 first, then
bootstrap to size 2" build order.

### Small-case / intuition summary (all labeled as conjecture except where stated proved)

- **Conjecture, strong support (`0/5961`, `0/2949`, two independent runs):** `\mathrm{OPT}_{-1}
  (\{c\},W)` always has a non-`\max(W)`-matching optimal witness, for *any* `c<\max(W)` — no
  provenance needed. Not proved; natural pointwise-swap proof attempt shown to fail.
- **Established by direct counterexample (not conjecture — a fact):** the same statement is FALSE
  for generic (non-`\mathcal F`) `|C|=2` dominated backgrounds (`75/2996`, minimal example
  `C=\{2,4\},W=(5,3)`, value `4` only achievable by matching `5\leftrightarrow3`).
- **Established by direct counterexample (a fact, not conjecture):** the natural pointwise
  relaxations of the swap argument (arbitrary-`\tau'` version, and the fully-abstracted numeric
  version dropping sortedness) are both false, ruling out the two most natural short-cut proof
  routes for even the `|C_{\mathrm{lo}}|=1` case.

All code archived at `/tmp/round-13/work/` (`defs.py`, `test1.py`…`test8.py`) — not modified in
`results/imo-2026-03/`.
