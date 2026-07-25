## imo-2026-03

- **Lens**: given the certified Flat/Kink Parity Lemma, locate/bound the true
  global maximizer $p^*$ of $V(p)$ over the balanced region (including
  Flat-Edge faces), via exact-Fraction sanity checks plus a from-scratch
  high-fidelity multi-restart search (own code, `/tmp/round18_flat/*.py`,
  independent of the builder's prior scripts).

### Distinct openings surfaced

1. **The p_LB / doubling point is a red herring for this residual.** I
   independently reconfirmed the certified Top-Duplication Witness Theorem
   (`lemmas/top-duplication-witness-theorem.md`): $p_{LB}=(2^n,\ldots,2,1)/
   (2^{n+1}-1)$ gives $V(p_{LB})=c(n)$ exactly (matched to $10^{-16}$ for
   $n=2,3$ against the closed form $2^n/(2^{n+1}-1)$). But $p_{LB}$ has
   $p_1=2^n/(2^{n+1}-1)>1/2$ for every $n$ — **it is not in the balanced
   region at all** ($p_1<1/2$ is required). This confirms (does not
   contradict) that the balanced-region residual is a genuinely different,
   harder-to-locate part of the domain; no argument should try to connect
   $p^*$ to $p_{LB}$ by continuity across the $p_1=1/2$ boundary without
   separately handling that wall (Section 4.2's Boundary-Continuity Theorem
   territory).

2. **A from-scratch outer optimizer (random multi-start + hill-climbing,
   nested around a from-scratch brute-force inner $V(p)$ solver over the
   Global Vertex Lemma's finite shape set) finds the balanced-region
   supremum sits well below $c(n)$, with a gap that appears to *shrink* as
   $n$ grows.** Concretely (floats, multi-restart Nelder–Mead, not exact
   arithmetic — flagged as numerical, not a proof):
   - $n=2$: best found $V(p^*)\approx0.5295$ at $p\approx(0.4705,0.3363,
     0.1933)$, vs. $c(2)=4/7\approx0.5714$ — gap $\approx0.042$.
   - $n=3$: best found $V(p^*)\approx0.5210$ at $p\approx(0.4368,0.3106,
     0.1683,0.0842)$, vs. $c(3)=8/15\approx0.5333$ — gap $\approx0.012$.
   - The region-vertex $e_0$ itself gives $V(e_0)\approx0.5238$ ($n=2$) and
     $V(e_0)=0.5$ ($n=3$), both **below** the hill-climbed interior optima
     above — confirming $e_0$/$e_1$ are not the balanced region's
     maximizers (consistent with, and sharpening, round 14–16's finding
     that $e_0$ sits at the universal floor $1/2$, not at $c(n)$).
   - This is genuinely new numerical evidence (not previously reported):
     **the true $\sup V(p)$ over the balanced region looks like it could sit
     strictly below $c(n)$ with real slack**, not near-tight. If this trend
     is real and persists (untested for $n\ge4$ — time did not permit), the
     Existence Theorem in the balanced region might be provable with a much
     cruder bound than an exact vertex/face classification (e.g. a single
     uniform slack estimate), rather than needing the full $\Sigma$-shape
     machinery. **This is the single most actionable new opening**: next
     round should check whether the gap $c(n)-\sup_{\text{balanced}}V(p)$
     is bounded below by an explicit, provable function of $n$ (candidate:
     something like $\Theta(\gamma(n))=\Theta(2^{-n})$, i.e. exponentially
     small but nonzero) — if a *provable* lower bound on this gap can be
     established (even non-tight), the Existence Theorem reduces to
     showing $V(p)\le c(n)-(\text{that slack})$ is what actually needs
     proving, which may be an easier target than $V(p)\le c(n)$ exactly at
     a razor's-edge tie.

3. **The located near-maximizers are NOT Flat-Edge faces.** I reconstructed
   the winning shape at each hill-climbed optimum and applied the certified
   Flat/Kink Parity Lemma directly:
   - $n=3$'s optimum ($m=(1,0,2,0)$: piece 1 bisected into two *distinct*
     values, piece 3 split into three fragments with an exact tie between
     two of them and a third fragment $\approx0$): the tied pair sits at
     ranks 5 (odd) and 6 (even) — **opposite parity**, i.e. by the Parity
     Lemma this is a **sharp-kink (Self-Bisection-Crossover) tie, not a
     Flat-Edge**. The near-zero fragment additionally invokes the certified
     Zero-Removal Invariance Lemma (`lemmas/zero-removal-invariance-lemma.md`).
   - $n=2$'s optimum ($m=(1,0,1)$): all five resulting values came out
     numerically distinct (no exact tie at all) — a **plain, tie-free
     vertex** of the finite-cell arrangement, not even a kink.
   - Contrast with round 17's catalogued hard points (`n3_pt1`,`n3_pt3`,
     `n4_pt1`), which *were* built to exhibit Flat-Edge/kink phenomena but
     all have $V(p)\approx0.51$–$0.511$, **strictly below** the optima this
     search found (0.52–0.53) at comparable $n$ — reinforcing round 17's own
     honest caveat (Section 8.5(b)) that those catalogued points are *not*
     the actual extremizer, just illustrative samples.
   - **Tentative but real reframing**: if the true global maximizer of the
     balanced region generically sits at a tie-free or sharp-kink vertex
     rather than a Flat-Edge continuum face, then **the Flat-Edge
     machinery (Section 8.3–8.4) may not be load-bearing for closing the
     Existence Theorem at all** — the ordinary finite-cell/vertex
     classification of Section 4 (already largely built) might suffice,
     and Flat-Edge could remain a genuine but *non-extremal* curiosity.
     This directly challenges the round-17 framing that Flat-Edge
     classification is a prerequisite; a next approach could instead push
     on classifying only kink/tie-free vertices of $Q$, explicitly
     deferring (not ignoring) the question of whether any Flat-Edge face
     could tie the vertex value (a possible but so-far-unobserved scenario
     at the maximizer).

4. **Concrete candidate shapes for $p^*$'s winning response** (from the
   search, for future exact-arithmetic pursuit): at $n=2$, cut-allocation
   $(1,0,1)$ (split pieces 1 and 3, piece 2 untouched); at $n=3$,
   $(1,0,2,0)$ (split piece 1 into 2, piece 3 into 3, pieces 2,4
   untouched) and a close competitor $(2,1,0,0)$ ($V\approx0.5172$,
   slightly worse). These are concrete, checkable finite shapes — a
   natural next step is to fix one of these shapes' combinatorial type,
   solve its affine formula in closed form (as Section 1 of the approach
   file already provides machinery for), and directly maximize the
   resulting explicit rational function of $p$ over the simplex — a
   tractable finite-dimensional calculus problem, in contrast to
   maximizing the full nonsmooth $\min_\sigma$.

### Candidate technique(s)
- The certified Global Vertex Lemma + finite-cell reduction (Section 4 of
  `global-lp-vertex-sufficiency.md`) — already reduces $V(p)\le c(n)$ over
  a cell to a finite affine-formula comparison; the Flat/Kink Parity Lemma
  is the right tool *if* Flat-Edge faces turn out to matter at $p^*$, but
  opening 3 above suggests checking the tie-free/kink vertex case first as
  the likely load-bearing one.
- Compactness + Lipschitz continuity (already certified, Section 2–3):
  guarantees $p^*$ exists; combined with opening 2's numeric slack finding,
  a genuinely different route is to try to prove a **uniform gap bound**
  (not exact equality) rather than pursuing an exact face-by-face
  classification.

### Cheap-kill candidates
- Re-run the mandatory extremal-selection/transfer cheap-kill (Section 8.1)
  at the *actual* near-maximizers found this round (not just the
  round-17 catalogued samples) — I did not have time to redo this
  systematically; it is a natural, cheap next check since the winning
  shapes are now concretely known ($m=(1,0,1)$ at $n=2$, $m=(1,0,2,0)$ at
  $n=3$).
- Zero-Removal Invariance (already certified) directly explains the
  near-zero fragment observed at $n=3$'s optimum — worth checking whether
  the optimal shape always has exactly one "sacrificial" near-zero
  fragment (a structural pattern that could simplify the shape-set search
  a lot if it holds generally).

### Knowledge-base entries to use
- Nothing new beyond what's already cited in the approach/lemma files
  (Lipschitz/extreme-value theorem, LP vertex characterization) — no
  additional `knowledge_base.md` entry identified as newly relevant this
  lens; the project's own certified lemma stack (Flat/Kink Parity,
  Zero-Removal Invariance, Mass-Constraint, Global Vertex Lemma) is the
  operative toolkit.

### Analogous past problems (cruxes)
Searched `combinatorics` subtopics `games-and-strategy` and
`extremal-principle` (205 cruxes) for stick/interval/cut/vertex/polytope/LP
matches. **None are genuinely analogous** to the specific mechanism here
(maximize-over-adversary-partition of a piecewise-affine min-over-finite-shapes
functional, with parity-of-rank governing flat vs. kink slopes). The closest
surface-level hits (`aimo-0560`, surrogate-adversary replacement in a game;
`aimo-0663`, pigeonhole/component-counting in a pairing game) are standard
combinatorial-game techniques but do not address LP-vertex/polytope-face
classification or rank-parity slope arguments — I would not force these as
crux matches. No crux recommended for direct adaptation.

### Prior progress
- Certified: Flat/Kink Parity Lemma, Zero-Removal Invariance Lemma,
  (Generalized) Mass-Constraint Theorem, Global Vertex Lemma +
  Lipschitz continuity + existence of a maximizer $p^*$ (all cited above).
- Open: the Existence Theorem itself ($V(p)\le c(n)$ for every $p$ in the
  balanced region) — this round's numeric evidence suggests the true
  supremum may have real slack below $c(n)$, and that the maximizer's
  winning shape is (at the two sampled $n$) tie-free or a sharp kink, not
  a Flat-Edge continuum — both new, precise, numerically-grounded (not
  proved) leads.

### Dead ends (do not retry)
- Treating $p_{LB}$ (doubling point) as connected to the balanced-region
  residual by continuity across $p_1=1/2$ — confirmed $p_{LB}\notin$
  balanced region, no new leverage there (consistent with prior rounds).
- Assuming the region vertex $e_0$/$e_1$ is the balanced-region maximizer
  — numerically refuted again this round ($e_0$'s value is below the
  hill-climbed interior optima at both $n=2,3$).

### Small-case / intuition notes (all conjectural, float-based, not exact)
- $\sup_{\text{balanced}}V(p)$ appears to be $<c(n)$ with a gap that
  shrinks with $n$ ($\approx0.042$ at $n=2$, $\approx0.012$ at $n=3$) —
  conjecture only, two data points, no $n=4$ check performed (time
  budget); if this holds, the Existence Theorem might have real slack in
  the balanced region rather than being asymptotically tight there.
- The winning shape at the (numerically located) near-maximizer is
  tie-free or a sharp Self-Bisection-Crossover kink at both tested $n$,
  never a Flat-Edge continuum — conjecture, small sample (2 values of
  $n$, local-search-found optima, not certified global optima).
- All numerics used float Nelder–Mead multi-restart (my own from-scratch
  script, `/tmp/round18_flat/search.py`, `refine.py`, `outer2.py`); the
  $p_{LB}$ exact-match check (matching $c(n)=2^n/(2^{n+1}-1)$ to
  $10^{-16}$) is the only near-exact confirmation performed — everything
  about the balanced-region interior optimum is heuristic local-search
  evidence, not a certified bound, and should be independently
  re-verified (ideally in exact `Fraction` arithmetic on the specific
  shapes $m=(1,0,1)$ and $m=(1,0,2,0)$) before being relied on.
