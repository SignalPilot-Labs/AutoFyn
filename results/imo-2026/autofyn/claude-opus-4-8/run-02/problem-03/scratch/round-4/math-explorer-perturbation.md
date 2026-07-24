## imo-2026-03 (perturbation / local-move lens on GAP-L residual)

### The gap I was assigned
Show `f ≥ 1` at every non-degenerate minimizer *pinned at a rank tie* (a stable P1 matched
pair `{v,v}`, e.g. `{4/3,4/3,4/3,2,1}`, `f=5/3`). Certified `cut-slide-derivative` (Lemma I)
gives the exact one-sided derivative even at ties: `∂f/∂(increase q)=s^↑(q)=σ_{a_l}`,
`∂f/∂(decrease q)=−s^↓(q)=−σ_{b_l}` where `[a_l,b_l]` are the ranks of `q`'s tie-block.

### Headline finding: **the stated residual example is NOT a stable local minimum — it slides
continuously down to the exact floor f=1.** Verified by direct hand computation from Lemma I
and confirmed numerically (sympy-free arithmetic, exact fractions):

```
base = (4/3,4/3,4/3,2,1), f = 5/3
perturb piece "4" (trisected) as (4/3+eps, 4/3, 4/3-eps):
 eps=0    -> f=5/3   (flat)
 eps=1/3  -> f=5/3   (flat; new tie forms: shrunk sub-piece hits value 1, ties with piece "1")
 eps=0.4  -> f=1.533 (STRICT decrease begins once the new tie is crossed)
 eps=0.6  -> f=1.133
 eps=0.65 -> f=1.033
 eps→2/3  -> f→1     (limit: grown sub-piece hits value 2, ties with top piece "2")
```
So the whole segment from the "stable" tied vertex to the true dyadic floor is a single
continuous, f-non-increasing path, entirely inside the feasible polytope (no new cuts spent).
The vertex in `current.md` was only a *local minimum within one myopic "swap two tied
siblings" view*; it is not a local minimum of `f` on the actual chamber.

### Why this happens — the general structural principle (derived from Lemma I, not yet in
lemma form; I recommend the outliner promote this)
For a tie-block occupying ranks `[a,b]` (size `= b-a+1`):
- `σ_a = σ_b` **iff** the block size is **odd** (since `b-a` is even exactly when parity
  matches). In this case `s^↑ = s^↓` for the block, so **any** slide trading mass between two
  members of the block (holding the rest fixed) has slope `σ_a-σ_b=0` — **exactly flat**, not
  just first-order flat. Verified above (the `eps=0→1/3` leg).
- If the block size is **even**, `σ_a ≠ σ_b`, so a slide has slope `±2 ≠ 0`: one direction
  (shrink the piece currently sitting at the block's top rank, grow the one at the bottom rank)
  is a **strict decrease**, the reverse a strict increase. Verified numerically on an
  independent constructed example: pieces `{5,3,3,2,1,1}` (an *even*, size-2, **cross-piece**
  tie at value 3, from splitting `8→(5,3)` and `4→(3,1)`); sliding piece 8's own internal cut
  toward `(4,4)` — i.e. shrinking the "5" side and growing the "3" side — gives
  `f: 3 → 2.8 → 2.6 → … → 1` (at eps=1, reaching `{4,4,3,2,1,1}`, `f=1`, the exact floor) with
  slope exactly `-2` per unit `eps`, matching `σ_a-σ_b` theory exactly. The reverse direction
  (grow "5", shrink "3") is instead exactly flat here (`f≡3`) because that particular slide only
  moves *singleton* ranks (both sign `+`), not the tie itself — again matching Lemma I with
  block sizes 1.

**Conjectured finishing principle** (this is the terrain, not a finished proof — do NOT treat
as proved): every non-degenerate tied stable point admits a *feasible* direction (feasible
meaning: it trades mass between two sub-pieces of the *same* original piece, which is always
possible whenever that original piece has ≥2 sub-pieces) that is either (a) a strict decrease —
if some tie-block touching that piece is even-sized and both its rank-`a`/rank-`b` members have
a within-piece partner to trade against — or (b) exactly flat, in which case sliding along it
(bounded interval, since the domain is a compact polytope) must terminate at a chamber
boundary: either a sub-piece hits `0` (the already-closed **degenerate** case) or a new tie
forms with a different piece (as in the residual example), at which point the local picture
re-derives from Lemma I on the new configuration. Since there are only finitely many
sort-chambers, and `f` is non-increasing throughout any such walk, iterating this must
terminate at a point already covered by a certified lemma (degenerate ⇒ induction on cut count;
tie-free non-degenerate ⇒ Lemma J's odd-integer floor `f=Σε_k2^k≥1`). This would close the
residual **by monotonicity along the path**: `f(original tied vertex) ≥ f(terminal point) ≥ 1`.

### Where this could still break (the honest obstruction to watch for)
- The argument needs: **every** original piece touching a nontrivial tie either (i) has ≥2
  sub-pieces (so it has *some* internal partner to trade against), enabling the slide; or
  (ii) is a single whole uncut piece. Case (ii) can only participate in a tie if its *partner*
  side has the needed freedom — this always holds, because the original pieces `2^0,…,2^n`
  are pairwise distinct, so two wholly-uncut originals can never tie; hence **any** cross-piece
  tie has at least one side belonging to a cut (≥2-sub-piece) piece, which supplies the needed
  degree of freedom. This is a clean, fully rigorous sub-claim worth stating and proving
  explicitly (it's basically free from "the `2^k` are distinct").
- What is NOT yet nailed down: a rigorous, general (not just spot-checked) proof that the
  flat-slide, when followed to its chamber boundary, cannot loop forever between odd-tie flats
  without ever hitting a degenerate or tie-free-monochromatic terminal point. Finiteness of
  chambers makes an infinite loop impossible in principle (finitely many chambers, `f`
  non-increasing, so a repeat chamber would force exact flatness all the way and hence
  eventual convergence to the polytope boundary in finite chambers) but this needs a clean
  compactness/finiteness argument, not just the two worked examples above.
- Also open: whether the "trade mass with an internal partner" move I used is *always* available
  when the tied piece has ≥2 sub-pieces but the tie member of interest is NOT adjacent to its
  potential partner on the stick (needs the "chain shift" version of Lemma I — moving several
  intermediate cuts together — not just the single-adjacent-pair form currently certified).
  I did not verify this generalization; Lemma I as certified is stated only for *adjacent*
  sub-pieces. This is a genuine possible gap in extending the two worked examples to full
  generality (in both my examples the useful partner happened to be adjacent).

### Distinct openings for the outliner
1. **Direct finish via the flat-slide-then-descend argument above** (my main finding) — likely
   the fastest route to closing GAP-L residual entirely; needs (a) the odd/even tie-block
   dichotomy formalized as a corollary of Lemma I, (b) the "cross-piece tie ⇒ one side is cut"
   sub-claim (easy, from distinctness of `2^k`), and (c) a finiteness/termination argument
   (chambers are finite, `f` monotone non-increasing along the walk) to rule out infinite
   flat-sliding.
2. **Generalize Lemma I to non-adjacent (chain) slides** — needed only if opening 1 hits a tied
   pair with no adjacent partner; likely provable directly (moving several cut endpoints in a
   coordinated affine family is still a legal direction in the polytope, and `f` restricted to
   that 1-parameter family is again piecewise-affine with slope a telescoping sum of the
   traversed ranks' signs) but not yet attempted.
3. **KKT/variational characterization**: reformulate "is `P*` a local min" as "no feasible
   direction in the tangent cone of the (possibly degenerate) polytope has negative directional
   derivative" — this is really what opening 1 is doing informally; making it fully rigorous
   (tangent cone of a product-of-simplices domain at a boundary point) is standard but must be
   written out.

### Candidate technique(s)
Exchange/smoothing argument on a piecewise-affine objective over a compact polytope (cf. KB's
**Piecewise-concavity smoothing** entry — same mechanism: a function affine/concave on
sort-chambers has its min pushed to a chamber boundary; if the value is already flat through
the interior of a chamber, the boundary inherits the same minimal value). Also: Weierstrass
compactness (already used for Lemma J), one-sided directional derivatives (Lemma I).

### Cheap-kill candidates
- Parity/pigeonhole on tie-block size (odd vs even) via `σ_a` vs `σ_b` — a one-line
  observation (`b-a` even iff `σ_a=σ_b`) that immediately classifies every tie as
  "flat-internally-tradeable" (odd) or "strictly-improvable" (even). Cheap and already used
  above to explain both worked examples.
- Distinctness of `2^0,…,2^n` forces every cross-piece tie to touch at least one cut piece —
  free, one line, rules out the worst-case "both sides frozen" scenario entirely.

### Knowledge-base entries to use
- **Piecewise-concavity smoothing** (`knowledge_base.md`, Algebra & Polynomials section) — the
  general "push a flat interior minimizer to the chamber boundary without raising the
  objective" principle; directly analogous even though our objective is piecewise-affine
  rather than piecewise-concave-from-sinusoids (affine is both concave and convex, so the same
  boundary-pushing logic applies, even more simply).
- **Standard inequalities / equality-case pinning** — general framing for why the answer must
  be attained at a specific sparse configuration (here: dyadic `W_n` under the cascade).

### Analogous past problems (cruxes)
- `aimo-0146` (subtopic `extremal-principle`, combinatorics) — genuinely analogous: "Maximize a
  fixed weighted sum of a sorted sequence under a sum constraint by exchange-smoothing weight
  toward higher-coefficient positions until free coordinates equalize and the tail drains" is
  structurally the same move as ours (trade mass between two coordinates of a sorted list to
  move the objective monotonically toward a boundary/equalized profile), and its second crux —
  "when a relaxed optimum exceeds target by a fixed gap attained at one profile, close the gap
  by re-imposing a structural constraint the relaxation discarded" — mirrors exactly our
  situation (odd-integer floor closes the tie-free/dyadic profiles; the residual profile needs
  one more structural constraint, namely the tie-block parity argument above).
- No sinusoid-smoothing crux found that matches piecewise-affine alternating sums directly;
  the KB entry itself (not a crux-corpus problem) is the best textual match for the mechanism.

### Prior progress
GAP-U fully closed (round 3). GAP-L closed on: integer/dyadic placements (Theorem F, parity),
tie-free non-degenerate minimizers (Lemma J, monochromatic ⇒ odd integer ≥ 1), degenerate
minimizers (cut-count induction). Only the tied non-degenerate residual is open — this report's
target.

### Dead ends (do not retry)
- Deleting the P1 matched pair `{v,v}` and inducting on piece count — **breaks dyadic
  conservation** `Σ(sub-pieces of 2^k)=2^k` (confirmed correct dead end, already recorded).
- Parity of pieces (not of the telescoped value) for non-integer cuts — dead (`d=3` gives
  `f=1/3`), already recorded.
- Blanket "cutting a non-max piece never helps XY" — false, 28k counterexamples, already
  recorded; not relevant to this lens but worth reiterating so no builder retries it.

### Small-case / intuition notes (conjecture, not proof)
- The specific stated residual example `{4/3,4/3,4/3,2,1}` is **not** a genuine obstruction —
  it slides exactly to `f=1` (verified above, exact arithmetic, not floating noise: at
  `eps=2/3` the configuration becomes `{2,2,4/3,1,2/3}`... actually check: pieces become
  `(4/3+2/3, 4/3, 4/3-2/3, 2, 1) = (2,4/3,2/3,2,1)`, sorted `(2,2,4/3,1,2/3)`,
  `f=2-2+4/3-1+2/3=0+4/3-1+2/3=1`, exact). This strongly suggests **every** tied
  non-degenerate vertex is dominated by (i.e., slides down to) either a degenerate vertex or a
  tie-free monochromatic vertex, both already closed — i.e., the minimizer set genuinely
  *retracts* onto the already-closed cases, and the residual gap is a proof-writing gap (need
  the general finite-termination argument), not a mathematical obstruction. Recommend the
  outliner attempt opening 1 directly as the primary route to a full solve this round.
