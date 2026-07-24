# Round 29 proof-reviewer report — imo-2026-06

Three slugs built in parallel this round. All three independently
re-verified from scratch (own fresh Python/sympy scripts, own
re-derivation of every table/threshold/witness/quadruple, own greedy
resimulations distinct from every builder's).

## 1. `a1-13q-subfamily-theorem` — APPROVE (Status: solved)

**Claim.** Literal `T=1,L=13` periodicity for `a_1=13q`, all primes `q>13`
outside `Bad(13)={17,19,23,47}`, via direct instantiation of the certified
`p`-uniform machinery (Generalized `K_0`-Boundedness, gcd-difference Witness
Lemma, Legendre Sieve Gap Bound, Primorial Floor Bound, Universal Look-Back
Witness Identity's `r=1` corollary) at `p=13`, mirroring the certified
`a1-5q`/`a1-7q`/`a1-11q` template.

**Independent re-derivation performed:**
- Fresh greedy resimulation (own script, correct "for all prior i"
  legality, not an "exists" bug) for every prime `q∈(13,2000)`: reproduced
  `Bad(13)={17,19,23,47}` exactly, with exact deviation indices/values
  (`a_3=238,266,322` for `q=17,19,23`; `a_5=658` for `q=47`).
- Fresh `(s_0,K_0)` table computation at `p=13` (132 cells,
  `j∈{2,...,12},r∈{1,...,12}`): exact match.
- Fresh `Q_1(j,r)` sufficient-window threshold computation: exactly **112**
  below-threshold `(j,r,q)` `k=0` candidates for `r≠1` — exact match with
  the file's claimed count.
- Fresh witness search over all 112 candidates: found exactly **5**
  no-witness `EXC` cells — `(4,4,17),(6,6,19),(8,8,47),(10,10,23),
  (12,6,19)` — byte-identical to the file's claimed 4 genuine + 1 moot
  duplicate.
- **The `q=19` moot-duplicate-cell claim (the one flagged risk item for
  this build)**, independently checked: `q=19` lands in residue class
  `r=6` (`19 mod 13 = 6`), giving two below-threshold `r=6` cells,
  `(6,6,19)` (`n_0=2`) and `(12,6,19)` (`n_0=3`). Independently resimulated
  `a_1=247=13·19` from scratch: `a_1=247, a_2=260, a_3=266` (not 273) — the
  real sequence genuinely deviates at `n=3` via `(6,6,19)`, so the closed
  form `a_3=13(19+2)=273` (the premise `H(3)` that the `(12,6,19)` cell's
  analysis presupposes) is never realized. The file's argument that
  `(12,6,19)` is therefore vacuous, not a second independent exception, is
  correct and non-circular — confirmed. Also independently confirmed no
  other candidate among the 112 has a duplicate `EXC` cell (only `q=19`
  appears twice among the 5 `EXC` entries).
- Fresh `s^*=5` threshold inequality
  `(s+1)!≥25+(13/17)2^{s+1}(s+2)` checked numerically for `s=5,...,29`:
  holds throughout, matching the file.
- Fresh recomputation of all `132×11=1452` cell/`k` combinations for the
  residual band `k∈{1,...,11}`: found exactly the same **29**
  below-threshold `(j,r,k,q)` quadruples (byte-identical list, same order),
  with the same **19-moot** (`q∈Bad(13)`) **/ 10-non-moot**
  (`q∈{29,31,37,41,43,53,59,61}`) split. Independently verified all 10
  non-moot witnesses by direct integer computation — every `n,K,N,i` value
  reproduced exactly (e.g. `(2,5,2,31): n=70,K=42,N=1302,i=7`).

**No gap found anywhere.** This is a complete, correct, self-contained
instantiation of the certified machinery at `p=13`. **Verdict: APPROVE —
the run's 9th APPROVE.**

## 2. `a1-17q-subfamily-theorem` — APPROVE (Status: solved)

**Claim.** Literal `T=1,L=17` periodicity for `a_1=17q`, all primes `q>17`
outside `Bad(17)={19,23,29,31,37,43,61,67}`, same template scaled to
`p=17`.

**Independent re-derivation performed:**
- Fresh greedy resimulation for every prime `q∈(17,2500)`: reproduced
  `Bad(17)={19,23,29,31,37,43,61,67}` exactly, with exact deviation
  indices/values (`a_3=342,414,522,558` for `q=19,23,29,31`;
  `a_4=666,774` for `q=37,43`; `a_5=1098,1206` for `q=61,67`).
- Fresh `(s_0,K_0)` table computation at `p=17` (240 cells): exact match.
- Fresh `Q_1(j,r)` threshold computation: exactly **209** below-threshold
  `(j,r,q)` `k=0` candidates for `r≠1` — exact match.
- Fresh witness search: found exactly **8** no-witness `EXC` cells, all on
  the diagonal `j=r`, matching `Bad(17)` exactly — `q=19,37,23,43,61,29,
  31,67` at `(j,r)=(2,2),(3,3),(6,6),(9,9),(10,10),(12,12),(14,14),
  (16,16)` respectively. **Confirmed no moot/duplicate pathology** (unlike
  `a1-13q`'s `q=19` case): every non-diagonal below-threshold band for each
  of the 8 exceptional primes independently resolves with an honest
  witness in this reviewer's own scan.
- Fresh `s^*=5` threshold inequality
  `(s+1)!≥33+(17/19)2^{s+1}(s+2)` checked for `s=5,...,29`: holds.
- Fresh recomputation of all `240×10=2400` cell/`k` combinations for
  `k∈{1,...,10}`: found exactly the same **31** below-threshold quadruples
  (byte-identical), with the same **28-moot** (`q∈{19,23,29,31,37,43}`)
  **/ 3-non-moot** (`q∈{41,47,53}`) split. Independently verified all 3
  non-moot witnesses by direct integer computation — exact match.

**No gap found anywhere.** **Verdict: APPROVE — the run's 10th APPROVE.**

## 3. `bipartite-network-invariant-fah` — RETHINK confirmed (Status: unsolved)

**Claim.** A negative result: the "Bipartite-Network Reduction Collapse"
meta-lemma shows both readings of the outline-reviewer's corrected
disambiguation question (Reading α = fixed-core "repair," Reading β =
growing-core "repair") collapse into already-known territory (Proposition
A/B: round-2 Generalized Bounded Witness Lemma, already non-cofinite;
Proposition C: the round-15 Termination Criterion Lemma / H2), plus a
structural mismatch diagnosis versus the crux `aimo-1000` mechanism
(Proposition D: no arithmetic analog of the deterministic toggle rule).

**Independent verification performed:**
- Confirmed the Generalized Bounded Witness Lemma's own Status line reads
  "Does NOT by itself close gap (†)" (`lemmas/generalized-bounded-witness-
  lemma.md`, grepped directly) — matches Proposition B's citation exactly.
- Confirmed the Self-Absorbing Core Theorem's core-enlargement operator
  (`S_k → S_k^+ := S_k ∪ ⋃_{j≤N(S_k)} P(a_j)`) is precisely the operator
  Proposition C identifies as Reading β's "repair" — genuinely the same
  object as H2's termination question, not a relabeling trick with a hidden
  difference.
- Independently retrieved `past_crux_moves_database.json` for
  `problem_id="aimo-1000"` and confirmed Proposition D's quoted toggle-rule
  mechanism ("When network edge A-B closes... Either way C ends joined to
  both") is an accurate, verbatim citation, not a mischaracterization.
- Checked for a missed third reading of the disambiguation question: the
  file's two readings (fixed-core pool-boundedness vs. growing-core
  recruitment-boundedness) are the only two ways to formalize "does the
  pool of linking primes used across repairs stay bounded" given the
  problem's actual machinery (a repair either does or does not enlarge
  `S₀` — there is no third option within the certified toolkit's vocabulary
  of "core" and "linking prime"). No missed reading found.

**This is a genuine, complete, honest negative result, not a hasty
give-up** — it correctly declines to force a positive claim, correctly cites
existing certified content instead of re-deriving it, and correctly
identifies (Prop D) *why* the borrowed crux mechanism doesn't transplant
(existential-only vs. deterministic-toggle mismatch), consistent with the
round-7 Witness Discontinuity Obstruction precedent. **Verdict: RETHINK
confirmed — Status `unsolved`, correctly self-reported.**

## Lemma certification

- `lemmas/bipartite-network-reduction-collapse.md` — **certified** this
  round (new). Toolkit-independent negative screening lemma, same class as
  the certified `same-type-free-facts-vacuity.md` /
  `density-argument-vacuity-corollary.md` precedents. Independently
  verified (see above) — no gap.
- No new lemma files needed for `a1-13q`/`a1-17q` beyond what's already
  certified (per-`p` instantiation tables are documented in-file as
  "Promotable lemmas" but, consistent with the `a1-5q`/`a1-7q`/`a1-11q`
  precedent, are not re-certified as standalone general-purpose lemma
  files — they are `p`-specific numeric data, not new machinery).

## `current.md` updates

Updated `## Status` and inserted a new round-29 narrative entry recording
both APPROVEs and the RETHINK, matching the file's established format.
Floor deliverable now stands at **10 fully certified solved sub-family
theorems** (`2|a_1`; `a_1=p^k`; `a_1=3q`; `a_1=3q^2`; `a_1=3q^3`; `a1-3aq`
(`a=1,...,5`); `a1-5q`; `a1-7q`; `a1-11q`; `a1-13q`; `a1-17q`). H1 (FAH) and
H2 both remain open — 23rd consecutive plateau round (6-29) on the main
crux; overall workspace Status remains `partial`.

## Ranking outcomes recorded

- `a1-13q-subfamily-theorem`: `verified-milestone`
- `a1-17q-subfamily-theorem`: `verified-milestone`
- `bipartite-network-invariant-fah`: `dead-end`
