# Round 15 proof-review — imo-2026-06 (IMO 2026 P6)

## Headline

**The general problem is SOLVED.** `similarity-dichotomy-crux-adaptation`
gets **APPROVE**. `current.md` Status is now `solved`, with the complete,
self-contained proof written into its `## Full proof` section, and 3 new
lemma files certified into `results/imo-2026-06/lemmas/`. This is the
terminal result for this run.

---

## 1. `similarity-dichotomy-crux-adaptation` — APPROVE (Status: solved)

### What it claims
A from-scratch adaptation of IMO Shortlist 2013 N5's official Solution 1
("Ana and Banana," crux `aimo-0030`) into `imo-2026-06`'s own recursive
vocabulary (terms/non-terms of the sequence itself, not the ISL game's
"good/bad" language), proving the general problem for **every** `a_1>1`:
`a_{n+T}=a_n+L` for every `n\ge1`, with explicit `T,L`.

### Crux fidelity check
Read `aimo-0030` directly in `past_problems_database.json`: confirmed it
is IMO-SL 2013 N5 exactly (problem text, both official solutions, matches
verbatim). The file's Claims 1–3 and Main Dichotomy Theorem are structural
translations of the official Solution 1's Claims 1–3 and final dichotomy
argument — but **crucially they are not imported by citation**: the file
proves Lemma REC (the IN/OUT recursive characterization) directly from
`imo-2026-06`'s own recursive definition of `a_{n+1}`, and then re-derives
every one of Claims 1–3 and the Dichotomy Theorem using only Lemma REC and
the (also re-proven) Corollary P″ — never invoking the ISL game's own
"good/bad" recursive definition or any equivalence between the two
frameworks. This sidesteps the risk of an unproven "terms = good numbers"
identification and is the mathematically correct way to adapt this crux.
Two steps the official solution states without proof (that dividing by
the chosen prime `p` preserves the similarity signature `\sigma`, in both
the `p\le k` and `p>k` cases inside the Dichotomy Theorem) are here proved
explicitly (Section 6, Cases (i)/(ii)) — confirmed by hand re-derivation,
correct in both cases.

### Line-by-line re-derivation (independent, from scratch)
I re-derived every step by hand, not just re-read the text:
- **Lemma REC** (⇐ and ⇒ directions): correct, standard strong-induction-
  style argument directly from the problem's own recursive rule. No gap.
- **Corollary P″**: immediate one-line consequence of the recursive
  definition (`a_j`'s defining property at `l=i`). No gap. Citation to
  `lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`'s
  "Corollary P″" checked against that file directly — matches exactly,
  and the crux-adaptation file *also* reproves it inline for
  self-containedness (satisfies the "no crux-move-only citation" rule).
- **Claim 1** (multiple of a term is a term): correct, direct contradiction
  argument via Lemma REC + Corollary P″.
- **Claim 2** (`rs\ge k` non-term ⟹ `r^2s` non-term): correct algebra
  (`x<rs\le r^2s` since `r\ge1`), correct application of Lemma REC (⇐).
- **Claim 3** (`p>k` prime, `n\ge k` non-term ⟹ `np` non-term): the most
  intricate step (minimal-counterexample, 9-step argument mirroring the
  official solution's Claim 3). Checked every step: `p\mid m` derivation
  (Step 2), `y\ne1` (Step 4, via the base term `k`), minimal `\alpha` and
  the size bound `p^{r-1}y^\alpha<n` (Steps 5–6, correct algebra), the
  induction (Step 8, correctly indexed `i=0,\dots,r-1` producing results
  for `i=1,\dots,r`), and the final contradiction via Claim 1 (Step 9,
  `p^ry^\alpha=m\cdot y^{\alpha-1}` a genuine positive-integer multiple of
  `m` since `\alpha\ge1`). No gap.
- **Main Dichotomy Theorem**: Step A's reduction to the sub-claim is
  correct (checked `\sigma(nn')=\sigma(n)=\sigma(n')` from similarity).
  Step B's minimal-counterexample argument: both cases `p\le k` and
  `p>k` are exhaustive and correctly handled, including the similarity
  -preservation sub-arguments the official solution omits.

### One gap found — cosmetic, not fatal
Claim 2's and Claim 3's *contrapositive* forms, as literally boxed in
Sections 4/5, drop the domain hypothesis (`rs\ge k`, resp. `n\ge k`) that
is needed for "rs is a term"/"n is a term" to even be a meaningful,
in-domain statement. When these contrapositives are actually invoked
(Section 6, Cases (i)/(ii), with `rs=n:=e_0=d_0/p`), the file does not
explicitly verify `e_0\ge k` at the point of use. I checked this by hand:
it **is** unconditionally true and one-line-derivable from facts already
stated earlier in the same proof (`e_0=c_0t_0'` with `t_0'\ge1`, and
`c_0\ge k` from the sub-claim's own hypothesis, so `e_0\ge c_0\ge k`) —
true in *both* cases, no new idea needed. This is a documentation
omission, not a logical error: I found no scenario in which the actual
inference fails. I patched it explicitly into the certified lemma
(`lemmas/theorem-similarity-dichotomy.md`) and into `current.md`'s Full
proof (the phrase `**e_0=c_0t_0'\ge c_0\ge k**` is now spelled out at the
point of first use, before the case split). This is the *only* issue
found after a full adversarial line-by-line pass; per this workspace's
own established practice (see `/tmp/memory/proof-reviewer.md` rule on
repairing genuinely trivial one-line gaps rather than rejecting), I judge
this does not downgrade the Status.

### Periodicity corollary (Section 7 — new content beyond the crux)
This is the part that actually resolves `imo-2026-06` (the official ISL
problem only needs the Dichotomy Theorem itself). Checked carefully:
- Step 1–3: direct consequences of the Dichotomy Theorem + elementary
  residue fact. Correct.
- Step 4 (interleaving lemma): the key combinatorial fact — merging `T`
  arithmetic progressions with common difference `P` and offsets in a
  window of length `P` gives a periodic sorted sequence with `g_{n+T}=
  g_n+P`. I re-derived this abstractly (standard fact about merging APs
  with matching common difference and bounded-spread offsets) — correct,
  no gap; `\beta_T-\beta_1<P` because both lie in a length-`P` half-open
  interval.
- Step 6–7: correctly identifies `g_n=a_n` via uniqueness of the
  increasing enumeration of a set — not circular (the term set was
  independently characterized as an explicit union of APs via the
  Dichotomy Theorem in Step 2, *then* that explicit set's sorted
  enumeration is computed and shown to equal the a-priori-defined `(a_n)`).

### Independent numerical verification (fresh code throughout, not the builder's scripts)
- **Periodicity table**, `a_{n+T}=a_n+L`: reproduced builder's 4 values
  (`a_1=6,10,12,15`) exactly (`T,L` = `(15,30),(105,210),(1155,2310),
  (8008,30030)`), **plus 8 new untested values** `a_1\in\{2,3,4,5,7,9,
  11,14\}` (including edge cases `a_1=2,3`), zero exceptions across
  thousands of checked indices per value.
- **Main Dichotomy Theorem itself** (the true load-bearing final
  ingredient): wrote an exhaustive small-prime-signature-vs-term-status
  scanner and ran it on all 4 of this workspace's historically hardest
  test cases plus the single hardest recurring case:
  `a_1=247` (172,236 integers, 17,731 signatures), `2747` (223,697,
  67,919), `4087` (255,338, 83,760), `4199` (79,442, 31,498), and
  `21528751` (169,436 integers, 159,319 signatures, via `sympy.factorint`
  on every integer in the generated range). **Zero violations in every
  case.**
- **Lemma REC**: random-sample stress test (3000 samples per case) on
  `a_1\in\{247,2747,21528751\}` — zero violations (both directions: no
  term has a coprime earlier-term witness; no non-term lacks one).
- **Claim 2**: 20,000 random `(r,s)` trials on `a_1=247` and `21528751` —
  zero violations. (Claim 3 direct brute-force is infeasible for huge
  `a_1` since `np` quickly exceeds the generated range — but Claim 3's
  hand re-derivation above, plus the Dichotomy Theorem's exhaustive
  numerical confirmation which structurally depends on Claim 3, together
  give strong independent confidence.)

### Verdict
**APPROVE.** Status `solved`, confirmed correct after maximal adversarial
scrutiny (full line-by-line re-derivation + extensive fresh numerical
stress-testing, including this workspace's hardest historical test case).
`current.md` rewritten with the complete self-contained proof; 3 new
lemma files certified (see below).

---

## 2. `forced-primes-well-ordering` (Corollary CRR) — CHANGES REQUESTED (Status: partial, real progress)

### What it claims
Corollary CRR ("Common-Recruiter Reuse"): once a witness `i_0` (with
exactly-computed companion set) closes Lemma WF's conclusion for one
target core `S_0`, the *identical* proof (verbatim) closes it for
**every** other core `S` disjoint from `S(i_0)`, at zero extra cost.
Applied to re-aim 4 already-on-file witnesses of `a_1=21528751` at all
their legal targets, closing 4 more of its 6 disjoint core-pair channels
(now 5/6 closed).

### Re-derivation
Corollary CRR is honestly described by its own author as adding "no new
mathematics" — I confirmed this: Lemma WF's already-certified statement
(`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`) is already
universally quantified over the target core `S` (only `S'`/`i_0` are
fixed), so Corollary CRR is a restatement emphasizing this, not new
content. The proof (re-checking WF's own proof uses only `k\ne i_0`,
Corollary P″, and Lemma XC applied to the disjoint pair — none specific
to which disjoint `S`) is correct.

Independently re-verified all 4 witness factorizations via a fresh
generator + `sympy.factorint`, exact match: `a_{1405}=2^{11}\cdot103^2`,
`a_{11812}=3^7\cdot103^2`, `a_{27832}=7^4\cdot103^2`,
`a_{2575}=2^2\cdot3^4\cdot7^3\cdot197`. Confirmed `a_1=21528751=
103\times197\times1061` (correct). Traced the 4 channel-closure proofs
(§N.4) by hand — each is a straightforward combination of "Fact A" (full
`\{2,3,7\}` containment) and "Fact B" (disjunctive `\{2,3,7\}` hit),
logically valid in every case checked (`(\{103\},\{1061\})`,
`(\{197\},\{1061\})`, `(\{103\},\{197,1061\})`, `(\{197\},\{103,1061\})`).

The remaining 6th channel (`(\{1061\},\{103,197\})`) is honestly and
correctly left open, with a clear structural reason (Lemma WF's hypothesis
requires the witness core disjoint from the *target* core, and no such
witness of core `\{1061\}` or `\{103,197\}` is on file) plus fresh
evidence (a 2nd, structurally distinct escape bundle `\{11,5,23\}` found
at `n=30000`, alongside the already-certified `\{11,97\}`) that a single
fixed `W` may not suffice. No overclaim.

### Verdict
**CHANGES REQUESTED** (Status `partial` for the whole problem, though this
is a real, gap-free instance-progress result). This work's role in the
overall run is now superseded — the general problem is solved by
`similarity-dichotomy-crux-adaptation` without needing FCBC/channels at
all — but the result itself is correct and worth recording.

---

## 3. `intersecting-family-covering-construction` (Theorem EI) — CHANGES REQUESTED (Status: partial, real progress)

### What it claims
Theorem EI (Existence-Insufficiency): closes the "intermediate mechanism"
gap round 14's reviewer left open in Theorem MO/Proposition MO-2. No
bounded-modulus/CRT/pigeonhole mechanism that only ever certifies
*existence* (not universal admissibility) of an admissible type-`S'`
candidate — for any witness combination or window size — can establish
`BRL(S')`/`G`-eventual-periodicity.

### Re-derivation
- **Lemma TS** (Type-Symmetry): the identical CRT/pigeonhole argument that
  certifies a positive fraction of admissible type-`S'` candidates against
  a witness `a_i` equally certifies the same fraction for *every* other
  core type `T` disjoint from `S(i)` — checked the proof is a verbatim
  reuse of Theorem MO's proof with `T` replacing `S'`, valid since `S'`
  played no special role there. Correct.
- **Lemma AA** (Automatic Admissibility for non-disjoint types): trivial,
  correct one-line divisibility argument (a shared `P_1`-prime forces
  `\gcd>1` unconditionally, density 1, no CRT needed).
- **Lemma GM** (Selection Is a Global Minimum): trivial restatement of the
  problem's own recursive definition. Correct.
- **Theorem EI's 3-step proof**: combines these to show any such mechanism
  gives type `S'` **no discriminating advantage** over its competitors
  (every other core in `\mathcal D_S`, and `S` itself with an even
  stronger unconditional guarantee) in the race for the actual global
  minimum — so it cannot imply `G(n+1)=S'`, hence cannot bound run-lengths
  avoiding `S'`. This is logically sound: the argument never assumes what
  it's proving, and it correctly, explicitly disclaims proving
  `\mathrm{BRL}(S')` false (only that this technique family cannot
  establish it) — matching the honest scope of round 14's Theorem MO.
- Checked no hypothesis is smuggled: the formalization of "intermediate
  mechanism" (§14.1) genuinely sits strictly between Theorem MO's
  single-witness case and Proposition MO-2's full-enrichment case, and the
  proof correctly does not require the mechanism to have any specific
  form beyond "bounded modulus + CRT/pigeonhole existence conclusion."

### Verdict
**CHANGES REQUESTED** (Status `partial`, genuine correct negative result,
no gap found). Also now of reduced overall importance since the general
problem is solved by a different, unconditional route this round.

---

## Certified this round (into `results/imo-2026-06/lemmas/`)

- `lemma-REC-recursive-IN-OUT-characterization.md` — Lemma REC.
- `theorem-similarity-dichotomy.md` — Corollary P″ (restated), Claims 1–3,
  Main Dichotomy Theorem (with the domain-check gap patched explicitly).
- `theorem-periodicity-from-dichotomy.md` — the periodicity corollary
  that resolves the whole problem.

Corollary CRR (forced-primes-well-ordering) and Theorem EI
(intersecting-family-covering-construction) do not need new lemma files:
both are correctly certified as-is in their own approach files (Corollary
CRR explicitly adds no new machinery beyond already-certified Lemma WF;
Theorem EI's Lemma TS/AA/GM are narrow-scope results specific to the now
-superseded FCBC apparatus, retained in the approach file for the
historical record rather than promoted to `lemmas/`).

## `current.md`

Rewritten in full: `## Status` = `solved`, complete self-contained
`## Full proof` (Sections 0–9, matching the approach file's proof with the
one gap patched), `## Approaches tried` summarizing all approaches across
15 rounds, and a Round 15 headline documenting the independent
verification performed and the two other builds' honestly-scoped
(superseded but correct) results.

## Ranker outcomes recorded
- `similarity-dichotomy-crux-adaptation`: `verified-milestone`.
- `forced-primes-well-ordering`: `advanced`.
- `intersecting-family-covering-construction`: `advanced`.
