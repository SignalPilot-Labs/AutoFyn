# Scouting report: cross-bucket domination for blocked buckets (round 7)

Scope: scout only, per dispatch. No proof attempted. All numerical claims below
were computed fresh this round (scripts in `/tmp/round-7/*.py`: `sim.py`,
`bucket_analysis.py`, `antichain_track.py`), independent of any prior round's
code. Did NOT modify anything under `results/`.

## 0. What I read

- `results/imo-2026-06/current.md` in full (round 1–6 headlines). Confirmed
  the population has converged on one residual gap — finiteness of `𝓥_S` for
  each proper core `S⊊P_1` — stated in three equivalent languages
  (`(MRS_S)`, `Λ_S`/`Q_S` finiteness, cross-bucket domination).
- `results/imo-2026-06/approaches/forced-primes-well-ordering.md` in full
  (1118 lines): the Companion-Disjointness Coarsening Lemma, Bucket-Exclusion
  Corollary, and their round-6 §F worked examples (`a_1=247,S={13}`:
  4 buckets, 3 realized + 1 blocked; `a_1=2747,S={41}`: no disjoint-companion
  witness pair exists at all). Also the file's own honest diagnosis ("Why the
  Coarsening Lemma alone does not finish the proof") that bare-value blocking
  does not control proper supersets, and that this is "of the same essential
  order of difficulty" as the shared open gap.
- `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
  (first ~700 lines + the Multi-Companion Reduction Proposition, lines
  ~1199–1236): the `Λ_S`-Reduction Lemma, Single-Companion Finiteness Lemma
  (conditional on `J_S` infinite), and the Multi-Companion Reduction
  Proposition proving that bundles of `≥2` new companions reduce to a local,
  restricted instance of FCBC itself — confirmed by the reviewer to be the
  same difficulty as the Coarsening Lemma's residual gap, in different
  notation.

## 1. What "blocked bucket" means, worked out precisely

Fix a proper core `S⊊P_1` and two witnesses `j_1,j_2` with `G_{j_1}\cap S=
G_{j_2}\cap S=\varnothing` and disjoint nonempty companion sets
`\mathrm{comp}(a_{j_1})\cap\mathrm{comp}(a_{j_2})=\varnothing`. The
Coarsening Lemma forces every `i\in I_S` to have `\mathrm{rad}(a_i)\supseteq
S\cup\{p,p'\}` for some `(p,p')\in\mathrm{comp}(a_{j_1})\times
\mathrm{comp}(a_{j_2})` — i.e. a superset of one of at most
`|\mathrm{comp}(a_{j_1})|\cdot|\mathrm{comp}(a_{j_2})|` **coarse bare
values** `\kappa:=S\cup\{p,p'\}`. A bucket `\kappa` is **blocked** if some
third index `j_3` (any index at all) has `\mathrm{rad}(a_{j_3})\cap\kappa=
\varnothing` — then, by the elementary Permanent-Inadmissibility Lemma, no
term can *ever* realize `\kappa` as its **exact** radical past `j_3`. The
open gap: blocking rules out the *exact* bare value, not proper supersets of
it, so a blocked bucket could a priori still harbor an unboundedly growing
"escaped" fan.

**Reproduced `a_1=247,S=\{13\}` exactly** (fresh Python, `n=6000`):
witnesses `j_1=3` (`\mathrm{comp}=\{2,7\}`), `j_2=5` (`\mathrm{comp}=
\{3,5\}`) give 4 buckets `\{2,3,13\},\{2,5,13\},\{3,7,13\},\{5,7,13\}`,
realized at `a_6,a_2,a_4,\text{never}` respectively, with `\{5,7,13\}`
blocked by `j_3=7` (`\mathrm{rad}(a_7)=\{2,3,19\}`) — an exact match to the
file's claim, byte-for-byte on the realized indices.

**New: found there are 74868 valid disjoint witness pairs for this same `S`
through `n=6000`** (not just the one the file uses), and 167665 for
`S=\{19\}` — the file's single chosen pair is far from unique; many
different `(j_1,j_2)` give different (not necessarily compatible-looking)
bucket partitions of the same infinite family. This is a resource the
population has not yet exploited (see §4).

## 2. New finding: the Escape-Confinement Lemma (proved, not just observed)

**Claim.** If bare value `\kappa=S\cup Q` (`Q` companion primes) is blocked
by witness `j_3` (`\mathrm{rad}(a_{j_3})\cap\kappa=\varnothing`), then for
*every* `i\in I_S` with `\mathrm{rad}(a_i)\supsetneq\kappa` (an "escape"),
there exists a prime `p\in\mathrm{comp}(a_{j_3}):=\mathrm{rad}(a_{j_3})
\setminus P_1` with `p\in\mathrm{rad}(a_i)`.

**Proof.** By the unconditional, already-certified Lemma P′,
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{j_3})\ne\varnothing`. Since `i\in I_S`,
`\mathrm{rad}(a_i)\cap P_1=S`. Since `S\subseteq\kappa` and
`\kappa\cap\mathrm{rad}(a_{j_3})=\varnothing`, `S\cap\mathrm{rad}(a_{j_3})=
\varnothing`. So the nonempty intersection `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_{j_3})` cannot come from `S=\mathrm{rad}(a_i)\cap P_1`; it must
come from `\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`, i.e. some
`p\in\mathrm{comp}(a_i)\cap\mathrm{rad}(a_{j_3})`. Since `p\notin P_1` (it is
in `\mathrm{comp}(a_i)`), `p\in\mathrm{rad}(a_{j_3})\setminus P_1=
\mathrm{comp}(a_{j_3})`, as claimed. `∎`

**Why this matters.** The file's own diagnosis ("a term with radical
`S\cup\kappa\cup\{q\}` for some extra prime `q`... is not ruled out by this
mechanism alone, and could in principle recur for infinitely many distinct
`q`") reads as if `q` is unconstrained. This lemma shows it is **not**: any
escape prime is confined to the *specific, fixed, finite* set
`\mathrm{comp}(a_{j_3})` determined by the one witness that blocked
`\kappa`. This converts "unboundedly many possible escape primes" into "a
concrete, small, enumerable finite candidate list" — turning cross-bucket
domination into (at least locally) a finite-branching search rather than an
open-ended one.

**Numerically confirmed on two different `a_1`, non-trivially:**
- `a_1=247,S=\{13\}`: blocked bucket `\{5,7,13\}` (blocked by `a_7`,
  `\mathrm{comp}(a_7)=\{2,3\}`). Checked **all 240** terms of `I_S` (`n\le
  6000`) whose radical properly contains `\{5,7,13\}`: every single one
  contains `2` or `3` (exactly the predicted confinement set), and every one
  is in fact dominated by an already-*realized* bucket (`\{2,5,13\}`,
  `\{3,7,13\}`, or `\{2,3,13\}`) — so here escape depth is exactly 1 and
  lands directly on already-solved territory. Confirmed **all 3228**
  elements of `I_{\{13\}}` (`n\le6000`) are supersets of one of the 3
  realized buckets — zero exceptions.
- `a_1=21528751,S=\{197\}` (`P_1=\{103,197,1061\}`, a genuinely harder,
  3-prime-core case): witnesses `j_1=2` (`\mathrm{comp}=\{2,41,2549\}`),
  `j_2=4` (`\mathrm{comp}=\{3,19,193\}`) give **9** buckets, and — unlike the
  247 case — **all 9 are blocked** (by `j_3\in\{5,8,10\}$, checked
  exhaustively). Yet `|I_{\{197\}}|=102$ through `n=6000`, so *every* term
  must escape. Traced the bucket `\{2,3,197\}` (blocked by `j_3=10`,
  `\mathrm{rad}(a_{10})=\{7,13,103,2297\}`, so `\mathrm{comp}(a_{10})=
  \{7,13,2297\}`): the predicted confinement set is exactly `\{7,13,2297\}`,
  and the escape actually taken uses `p=7` — confirmed by direct computation
  of the full local minimal-radical antichain (see §3), which converges to
  the single value `\{2,3,7,197\}\supsetneq\{2,3,197\}`, with the extra
  prime `7\in\mathrm{comp}(a_{10})` exactly as the lemma predicts.

## 3. Depth of the escape recursion: confirmed depth ≥ 2 occurs, and confirmed it terminates in the cases tested

Applying Escape-Confinement recursively (candidate `\kappa\cup\{p\}` may
itself be blocked, forcing a further escape confined to a new witness's
companion set) is a natural next step. Tested this directly on
`a_1=21528751,S=\{197\}`'s bucket `\{3,41,197\}` (blocked by `j_3=5`,
`\mathrm{comp}(a_5)=\{2,5,7,1493\}`):

- **Depth 1**: all 4 candidates `\{3,41,197\}\cup\{p\}`,
  `p\in\{2,5,7,1493\}`, are themselves **blocked** (by `j_3=7`, `\mathrm{rad}
  (a_7)=\{2,23,71,103\}`, giving new confinement set `\{2,23,71\}$ for all
  of them, since `103\in P_1$) — so depth-1 does **not** resolve this branch,
  confirming depth can exceed 1.
- **Depth 2**: of the depth-2 candidates, `\{2,3,7,41,197\}` (adding `7`) is
  actually **realized** (`a_{1291}` and `a_{20441}`, confirmed both), while
  `\{2,3,13,41,197\}` and `\{2,3,41,197,2297\}` are still blocked (by
  `j_3=20`). So this specific branch resolves at depth 2, not depth 1 — and
  the realized depth-2 value is (as expected) later dominated once the
  much-shorter branch from a *different* original bucket (`\{2,3,197\}`,
  depth 1) produces the smaller value `\{2,3,7,197\}` at `a_{2575}`, which
  is a subset of it.

**This is the key open-ended honest finding: escape recursion depth is not
visibly bounded by any obvious a priori quantity** (it is at least 2 in a
concrete case checked here, and the file's own worked example needed only
depth 1) — whether it is *uniformly* bounded (say, by `\omega(a_1)`, by the
number of buckets, or by some function of the witnesses' indices) is exactly
the sharpened open question this round identifies, not resolved.

## 4. Empirical pattern across 4 independent `a_1` values: an S-independent "recruiter set" `W(a_1)`

Computed the **exact eventual local minimal-radical antichain** (not just
the bucket bare values) for every proper core of four different `a_1`
(`35=5\cdot7`, `2747=41\cdot67`, `4087=61\cdot67`,
`21528751=103\cdot197\cdot1061$), tracking it incrementally to `n=6000`
(`n=30000` for `21528751,S=\{103\}` to reach its later collapse). In every
single case, the final (stable, unconditionally verified with zero further
changes through the tested range) antichain is built entirely from `S`
together with a **small set of primes `W`, always the same across every
proper core of that fixed `a_1`**:

| `a_1` | `P_1` | `W(a_1)` (empirical) | per-core final antichain |
|---|---|---|---|
| `35` | `\{5,7\}` | `\{2,3\}` | `S=\{5\}\to\{\{2,5\},\{3,5\}\}` (froze at `n=4`); `S=\{7\}\to\{\{2,3,7\}\}` (froze at `n=3`) |
| `4087` | `\{61,67\}` | `\{2\}` | `S=\{61\}\to\{\{2,61\}\}` (collapsed at `n=54`, matching the already-certified `n=54` global-antichain collapse); `S=\{67\}\to\{\{2,67\}\}` (collapsed at `n=5`, correcting an initial size-1-but-wrong-value artifact `\{2,31,67\}\to\{2,67\}`) |
| `2747` | `\{41,67\}` | `\{2,3,7\}` | `S=\{41\}\to\{\{2,41\},\{3,41\},\{7,41\}\}` (collapse at `n=163`, matching file); `S=\{67\}\to\{\{2,3,7,67\}\}` (froze at `n=3`) |
| `21528751` | `\{103,197,1061\}` | `\{2,3,7\}` | `S=\{103\}\to\{\{2,103\},\{3,103\},\{7,103\}\}` (collapse at **`n=27832`**, exactly matching the already-certified round-5 corrected finding "1092 elements directly to 3", re-derived independently here); `S=\{197\}\to\{\{2,3,7,197\}\}` (collapse at `n=2575`, new — not previously documented in this file at this level of detail) |

**In every one of these 7 core-instances, `W(a_1)` is exactly the same set
of small primes regardless of which proper core `S` is used**, even though
the final antichain's *shape* varies (sometimes `S` pairs with each element
of `W` separately, sometimes all of `W` merges into one bundle with `S`).
`W(a_1)` always consists of the smallest primes not dividing `a_1` (`2,3`
for `35`; just `2` for `4087`; `2,3,7` for `2747`/`21528751`, skipping `5` in
both — not fully explained, flagged honestly as unexplained rather than
force-fit into "the `k` smallest available primes").

**Candidate reformulation for next round (not proved, a sharpening of the
target, per the dispatch's request for structural insight):** *is there,
for each `a_1`, a single finite set `W(a_1)` of primes disjoint from `P_1`
such that for every proper core `S`, the eventual minimal-radical antichain
of class `S` consists entirely of values `S\cup Q` with `Q\subseteq W(a_1)`?*
If provable, this would replace `2^{|P_1|}-1` separate `(MRS_S)`/`Λ_S`
finiteness questions with **one** global statement about a single set
`W(a_1)` — a much sharper, and structurally different, formulation than
either the per-`S` Coarsening Lemma or the per-`S` `Λ_S`-Reduction Lemma
currently in the workspace. A natural (unproved) mechanism suggesting why
this might be true: small primes divide a much larger density of integers
than any fixed large prime, so by Lemma 1's linear gap bound plus a
density/pigeonhole argument, a term divisible by a small prime `p\notin P_1`
should occur "for free" inside almost every companion set sooner or later,
so that any large-prime-only companion set is eventually dominated once the
corresponding small-prime bare value is itself realized (which is, notably,
*exactly* the same "eventually realized or blocked, no escape" dichotomy
already proved in this workspace as Lemma ER — but Lemma ER alone does not
bound *which* value gets realized first, which is the missing piece). This
is offered as a plausible direction, explicitly **not** a proof sketch with
justified steps — the density argument is not written down rigorously
anywhere and may have the same "pointwise vs. cumulative" flaw that sank the
Markov-bound and Growth-Budget attempts in rounds 3–6.

## 5. Summary / answer to the dispatch's four questions

1. **Blocked bucket, precisely**: worked out and reproduced exactly on
   `a_1=247` (§1); a bucket bare value `S\cup\kappa` blocked by witness
   `j_3` can never be realized *exactly* past `j_3`, but supersets of it are
   not automatically ruled out — that's the open piece.
2. **Is there a finite bound on the number of blocked buckets, or a
   resolution mechanism?** Found a genuinely new, *proved* partial
   mechanism: the **Escape-Confinement Lemma** (§2) — any escape from a
   blocked bucket is confined to the fixed finite companion set of the
   single blocking witness, not arbitrary. This does not by itself bound
   the number of blocked buckets or the recursion depth (confirmed depth
   `\ge2` occurs, §3), but it replaces an apparently unbounded search with a
   finite-branching one at each step — a real (if partial) sharpening.
3. **Computation across `a_1=247,2747,21528751` (and, going further,
   `35,4087`)**: performed (§4). Blocked buckets do not obviously "multiply"
   unboundedly in any case tested — every tested channel (7 core-instances
   across 4 `a_1`) eventually resolves to a small, finite antichain, and
   does so via the *same small recruiter set* `W(a_1)` regardless of which
   core `S` is involved.
4. **Candidate mechanism / sharpened question, reported honestly**: the
   Escape-Confinement Lemma (proved) plus the empirical `W(a_1)`
   S-independence pattern (strong evidence across 7 instances, not proved)
   together suggest reformulating the whole residual gap as: *(a)* prove
   Escape-Confinement recursion always terminates (bounded depth), or
   *(b)* prove existence of a single `a_1`-dependent (not `S`-dependent)
   finite recruiter set `W(a_1)` that eventually absorbs every proper core's
   antichain. Neither is established. No counterexample to either was found
   in any case tested, and no proof mechanism for either was found either —
   this is a scouting report identifying two concrete, checkable new targets
   for a builder, not a solution.

## Reproducibility

All code at `/tmp/round-7/`: `sim.py` (greedy sequence simulator, bitmask
admissibility check via `sympy.factorint`), `bucket_analysis.py` (bucket /
witness / disjoint-pair analysis, reproduces the Coarsening Lemma
mechanically), `antichain_track.py` (incremental minimal-radical antichain
tracker per core). Sequences cached as JSON (`seq_*.json`) for `a_1\in
\{247,2747,4087,35\}` to `n=6000$ and `a_1=21528751$ to both `n=6000` and
`n=30000`.
