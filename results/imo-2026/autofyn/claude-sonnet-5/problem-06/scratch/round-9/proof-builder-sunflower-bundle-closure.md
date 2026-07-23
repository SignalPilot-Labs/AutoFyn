# proof-builder report — sunflower-bundle-closure (round 9)

## Result

**`(UB_S)` is now fully and rigorously refuted** (the FALSE direction, per
dispatch's explicit sanctioning of either outcome as valuable). Status
remains `partial` (this is a "kill" finding retiring a dead-end
sub-target, not a solve of the whole IMO problem — FCBC itself, attacked
by this round's sibling approaches, remains open).

**Theorem proved (§6 of the approach file, new this round).** In Case II
(no prime divides every term of the sequence — the only regime in which
"proper core" is meaningful; Case I is separately and unconditionally
closed by the already-certified Theorem CI): it is impossible for `(UB_S)`
(`sup{|rad(a_i)\S| : i∈I_S} < ∞`) to hold for every proper nonempty core
`S⊊P_1` simultaneously. Equivalently, `sup_{n∉I_{P_1}} ω(a_n) = ∞` always.

## What I did (per the four required tasks in dispatch)

1. **Retargeted Step 3 to the corrected weaker form** and **proved it in
   full** (§6.1, Imprint Periodicity Lemma + Corollary). The real finding:
   this doesn't need an independent, unconditional density argument about
   the raw greedy recursion (which is what stalled rounds 3-8's density
   attempts) — it follows almost for free *from the very assumption being
   refuted*. Assuming `(UB_S)` gives exact periodicity `a_{n+T}=a_n+L` for
   every `n≥1` (already-certified `theorem-UBS-sufficiency.md`/Theorem
   5.1 chain, cited not re-derived). Exact periodicity of `a_n` forces
   exact periodicity (with an explicit finite period `τ`, computed via
   elementary arithmetic-progression divisibility) of "which primes divide
   `a_n`," hence of `n∈I_{P_1}` itself. A periodic set's density is exactly
   `|R|/τ`; `|R|=τ` (density 1) is ruled out because it would make some
   fixed prime of `P_1` a global hub, contradicting the standing Case II
   hypothesis. This gives `∃c=1/(2τ)>0` with `|I_{P_1}∩[1,N]|≤(1-c)N` for
   large `N` — exactly the outline-reviewer's required correction (§1d of
   `/tmp/round-9/outline-reviewer.md`), proved rigorously, not cited from
   numerics.

2. **Proved the Landau Count Lemma from scratch** (§6.2-§6.3): `|{m≤X:
   ω(m)≤k}| = o(X)` for fixed `k`. Used Turán's classical 1934 elementary
   second-moment argument (Chebyshev-type extraction from a variance
   bound), which itself only needed the qualitative divergence
   `Σ_{p≤X}1/p → ∞` (Euler, 1737, also proved from scratch via a
   smooth/rough-number split, §6.2) — deliberately avoided needing the
   full quantitative Mertens' 2nd theorem rate (`log log X + O(1)`), which
   simplified the proof substantially and kept every constant absolute.
   Both are confirmed-new tools for this workspace (absent from
   `knowledge_base.md`/the crux corpus per the round-9 outliner's search).

3. **Assembled the full contradiction** (§6.4): under `(UB_S)`, all
   `a_n` for `n∈I_{P_1}^c∩[1,N]` are `≥cN` distinct integers, each
   `ω(a_n)≤B` (the uniform bound from `(UB_S)`), packed into an `O(N)`
   interval (already-certified Growth Lemma). Landau's Count Lemma caps
   the count of such integers at `o(N)`. So `cN≤o(N)`, contradicting `c>0`
   fixed. `(UB_S)` is false.

4. **Wrote up the honest scope note**: this refutes the round-8 target
   `(UB_S)` and retires the whole `(UB_S)`/`(MRS)`/`𝓥_S`-finiteness-via-
   bundle-size program (rounds 4-8) as a route to the whole problem —
   future rounds should not re-attempt proving `(UB_S)`, `(MRS)`, or
   `𝓥_S`-finiteness for a proper core in any form. It does **not** refute
   FCBC (strictly weaker, per already-certified Lemma W1) or solve the
   whole problem — that remains open, attacked by this round's siblings
   `explicit-window-backbone-construction` and
   `intersecting-family-covering-construction`.

## File changes

- `results/imo-2026-06/approaches/sunflower-bundle-closure.md`: added
  "Round 9 update" headline section, a "Round 9" entry under "Approaches
  tried", a new §6 (four subsections, ~250 lines of full rigorous proof:
  Imprint Periodicity Lemma, Euler's divergence, Landau Count Lemma via
  Turán, contradiction assembly), added a pointer note marking old §5 as
  superseded (kept verbatim per this workspace's append-only convention),
  and 4 new "Promotable lemmas" entries. Status kept `partial`.

## Promotable lemmas (for the reviewer to certify)

- **Imprint Periodicity Lemma + corrected Density Sub-Lemma** (§6.1):
  exact periodicity `a_{n+T}=a_n+L` ⟹ `n∈I_{P_1}` is exactly `τ`-periodic
  for a fixed, explicit `τ`; combined with Case II, gives
  `|I_{P_1}∩[1,N]|≤(1-c)N` for a fixed `c>0`.
- **Euler's classical divergence of `Σ_p1/p`** (§6.2): from-scratch,
  self-contained, general-purpose.
- **Landau Count Lemma via Turán's argument** (§6.3): `|{m≤X:ω(m)≤k}|=
  o(X)`, from-scratch, general-purpose, avoids needing the Mertens rate.
- **Theorem: `(UB_S)` is false in Case II, unconditionally** (§6.4): the
  file's new central result, combining the above with already-certified
  content (Growth Lemma, `theorem-UBS-sufficiency.md`/§4c chain).

## Honest caveats

- This is genuinely a refutation, not a solve — Status is `partial`, as
  it must be per CLAUDE.md (the file's ultimate target, the whole IMO
  problem, remains open).
- The proof relies on citing (not re-deriving) several already-certified
  facts from this file's own round-8 content and other workspace lemmas
  (Growth Lemma, Lemma P, `theorem-UBS-sufficiency.md`'s equivalence
  chain, Theorem 5.1's `T,L≥1` guarantee). These were verified present and
  correctly stated before citing.
- I double-checked (mentally, and partially via a Python sanity check of
  `S(X)` vs `log log X` for `X=100000`, consistent but not part of the
  proof) every algebraic step of the Turán second-moment computation and
  the periodicity argument's "global period, not just within-residue-class"
  subtlety — both hold rigorously as written.
