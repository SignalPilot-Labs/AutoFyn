# Scouting report — finite extreme-point evaluation for case (b2)

Lens: the actual finite chamber-vertex enumeration for case (b2)
($T/D_n < p_2 < a_nT/2$, $p_1<T/2$), building on the Chamber-Vertex
Theorem (Lemma R22.1 + Theorem R22.2, in
`results/imo-2026-03/lemmas/p-space-chamber-vertex-theorem.md`) and the
live approach `results/imo-2026-03/approaches/lp-duality-certificate.md`.

## 1. What the vertex machinery actually says (and its exact scope)

Fix $n$, a full type $(\mathbf c,\tau,\pi)$ with $M(\tau)$ invertible.

- **Lemma R22.1**: the chamber $U(\mathbf c,\tau,\pi)\subset p$-space is cut
  out by finitely many affine inequalities in three families: (a)
  feasibility $F^\tau_{i,l}(p)\ge0$, (b) order $F^\tau_s(p)\ge F^\tau_{s'}(p)$
  for every pair of slots ranked by $\pi$, (c) type-optimality
  $\ell_\tau(p)\le\ell_{\tau'}(p)$ against every other full type $\tau'$
  (finitely many at fixed $n$).
- **Theorem R22.2**: on the bounded slice $\overline{U\cap\{T=1\}}$, the
  affine functional $g(p)=a_nT(p)-\Phi_{\min}(p)$ attains its minimum at a
  vertex pinned by $\dim(\mathcal P\cap\{T=1\})=m-1=n$ independent tight
  constraints from (a)/(b)/(c) (or their closures) plus $T=1$.
- **Item 3 (compactness Corollary), reviewer-corrected scope**: case (b2)'s
  box is open, so a vertex of $\overline{U\cap\mathrm{Box}}$ may sit on
  $\overline{\mathrm{Box}}\setminus\mathrm{Box}$. The fix (boundary-sharing
  with the three adjacent already-closed regions) is **only literally
  unconditional at $n\le3$**. Per the round-22 correction note: only the
  $p_2\le T/D_n$ wall (case (b1), via `unconditional-p2-threshold-closure`)
  is unconditionally closed for every $n$; the $p_1\ge T/2$ wall is closed
  unconditionally only for $n\le3$ (extending it needs case (b2) itself
  closed one level down — a real coupling, not a citation slip); case (a)
  $p_2\ge a_nT/2$ is closed only *conditionally* on the same standing
  strong-induction hypothesis this whole project rests on. **So for
  $n\ge4$ the compactness fix is conditional on the induction hypothesis
  one level down — it is not a free general-$n$ closure.**

This matters directly for what a builder should attempt next (§3).

## 2. Concrete candidate vertex list — what exists on file, what doesn't

### 2a. One concrete $n=3$ worked chamber (§R22.1.1)

Composition $(1,1,0,0)$ at $n=3$ ($m=4$): type $\tau^\star$ ties piece 1's
two slots symmetrically ($F_{1,1}=F_{1,2}=p_1/2$), piece 2's slots are
$F_{2,1}=p_2-p_3$ (its own tied value) and $F_{2,2}=p_3$ (pinned to piece
3, untouched). $M(\tau^\star)=\mathrm{diag}(2,1)$, invertible. The two
genuine (non-automatic-in-$\mathcal P$) walls are:
$$\text{(W1) } p_1\ge 2p_3,\qquad \text{(W2) } p_2\le p_3+p_4,$$
with closed form $\Phi_{\min}(p)=p_1/2+p_3+p_4$ on this chamber. This is
**one** non-empty chamber meeting case (b2)'s box, numerically confirmed
(exact-`Fraction` grid, $80\times80$) to be the globally realized type at
a specific point, margin $\approx0.0205$. This is a genuine template for
how a "cut $p_1$ symmetrically + one tail pin" type looks in $p$-space —
but it is **one type out of a combinatorial family that grows with $n$**
(round-20's chamber-density read: $\approx28\%\to64\%$ distinct
compositions sampled from $n=3\to n=4$), not yet an exhaustive list.

### 2b. A genuinely more complete vertex characterization already exists, but only for a *restricted* sub-family

§"Route A" of the same approach file (A.1–A.3) proves, for the restricted
strategy family "Xiang Yu spends his entire budget cutting $p_1$ into $k$
parts, tail $\tau=(p_2,\dots,p_m)$ completely untouched" (a strict
sub-case of case (b2), not the general chamber-vertex family which also
allows tail cuts):

- **A.2**: every vertex has $p$ coordinates pinned to distinct tail values
  $\tau_{l_1},\dots,\tau_{l_p}$, and the remaining $q=k-p$ coordinates tied
  to one common value $v=(p_1-\sum\tau_{l_i})/q$. This *provably* subsumes
  Theorems A/B/C on file as the special cases $p=m-1$, $p=1$, $p=0$
  respectively — i.e. **the vertex-shape enumeration for this restricted
  family is complete and closed-form**, not conjectural.
- **A.3**: reduces evaluation to a genuinely finite combinatorial
  optimization over subsets $X\subseteq\{1,\dots,n\}$ (which tail levels
  are *not* pinned) and a parity bit ($q$ even/odd), with $A(F^\dagger\cup
  \tau)=A(X)$ or $A(X\cup\{v(X,q)\})$ in closed form via the certified
  `odd-run-reduction-lemma`/`pair-cancellation-identity`. **This
  minimization over $(X,q)$ was never actually carried out symbolically**
  (explicitly flagged "not attempted this round due to time" — the file's
  own honest open item).

This is the single most promising concrete lead: A.2/A.3 already do, for
the "cut-$p_1$-only" sub-case, exactly what the assignment is asking for
case (b2) as a whole — a genuinely finite, closed-form vertex family with
an explicit (if unsolved) minimization target. The general case-(b2)
chamber-vertex family (allowing tail cuts too) does **not** yet have an
A.2-style closed vertex-shape enumeration — only the abstract existence
statement (Lemma R22.1/Thm R22.2) and one hand-worked example (§2a).

### 2c. What is NOT yet on file (the actual gap)

- No general-$n$ (or even general small-$n$) enumeration of *all* full
  types $(\mathbf c,\tau,\pi)$ whose chamber meets case (b2)'s box. Only
  one has been worked out explicitly (§2a), plus the restricted A.2 family
  (§2b), which excludes any strategy that cuts the tail.
- No proof (or disproof) that the number of case-(b2)-relevant types stays
  bounded as $n\to\infty$ — the round-20 density read (28%→64%) is flagged
  repeatedly as an open risk signal, not resolved.
- The A.3 finite minimization ($\min_{X,q} A(X)$ / $A(X\cup\{v\})$ subject
  to $v\ge0$) has not been solved even symbolically for general $n$, let
  alone shown $\le T/D_n$.

## 3. What's already ruled out — do not re-attempt

Nine confirmed-dead mechanism families for case (b2) are on file (do not
resubmit any of these in a new guise):

1. Peel/bisect/recurse-plus-full-IH (`peel-zero-slack-dead-end`,
   `bisect-containment-dead-end`, round 14).
2. Weighted/convex-combination of primal values across strategies
   (`convex-combination-futility-theorem`).
3. Naive boundary-continuity across chamber walls (no established
   convexity/concavity of $\Phi_{\min}$ across chamber boundaries).
4. Danskin's-theorem / concavity-in-the-tail-marking smoothing (Tail
   Exchange Lemma) — refuted round 18: $g(t)$ has a genuine interior local
   *minimum*, incompatible with concavity.
5. Surrogate/majorization worst-tail argument (`surrogate-adversary-dead-end`,
   round 19) — the natural ratio-2-ladder surrogate is not even the true
   argmax tail (drifts $\approx1.4$–$2.0$ across sampled points).
6. Constraint-side LP duality (`minimax-lp-response-polytope`'s
   Duality-Direction Impossibility Theorem, round 19) — weak duality is
   structurally one-directional and cannot certify the needed direction,
   for any $n$ or marking.
7–8. Two further mechanisms recorded in rounds 20–21 (see `current.md`
   round-20/21 entries and commit history — "7th mechanism killed",
   "8th mechanism sound"); check `current.md` directly for their exact
   names before proposing anything that resembles them, since I did not
   fully pin down their slugs from this pass.
9. **Box-corner × tail-chamber-vertex dimension reduction**
   (`box-corner-tail-vertex-decomposition-refuted`, round 22) — the
   conjecture that the worst case-(b2) witness sits at the $(p_1,p_2)$
   box corner is **false**: unrestricted search finds strictly worse
   (smaller-margin) witnesses off-corner at both $n=3,4$, confirmed by
   exact-`Fraction` grid search, not just floating point.

**Do not propose**: any surrogate/majorization tail bound, any
convexity/concavity-across-chambers argument, any corner-restricted or
otherwise dimension-reduced search, or constraint-side LP duality.

## 4. Concrete next steps for a builder

1. **Attack $n=3$ (and maybe $n=4$) as a fully unconditional base case
   first, exploiting the corrected scope.** Per the reviewer's
   correction, at $n\le3$ *all three* Box walls really are
   unconditionally closed, so the compactness-fix Corollary applies with
   no induction-hypothesis caveat. Since $n=3$ has a genuinely small,
   finite composition space (cut budget $3$, $m=4$), a builder could
   enumerate *all* full types meeting case (b2)'s box at $n=3$ explicitly
   (§2a already gives one; the rest should be a finite, tractable case
   list — likely a dozen or so once order/tie patterns are accounted
   for), evaluate $g$ at every interior vertex via the same closed-form
   technique as §R22.1.1, and check $g\ge0$ everywhere. This would be a
   genuine, complete, non-numeric closure of case (b2) at $n=3$ — a real
   milestone distinct from (and strictly harder than) the numeric spot
   checks already on file, and it sidesteps the $n\ge4$ conditionality
   entirely.

2. **Finish the already-reduced Route-A finite optimization (§2b/A.3)
   symbolically**, even though it only covers the "cut $p_1$ only, tail
   untouched" sub-family. Solving $\min_{X\subseteq\{1,\dots,n\},\,q}$
   over the two closed-form cases is a concrete, bounded combinatorial
   problem (superincreasing-sequence alternating sums), not a new
   framing — it directly reuses `odd-run-reduction-lemma` and
   `pair-cancellation-identity`, both already certified. Either (i) it
   closes $\le T/D_n$ for this restricted family for every $n$ (real
   partial progress, honestly scoped to "tail untouched"), or (ii) it
   finds a genuine counterexample within the restricted family, which
   would definitively show tail-cutting strategies are *necessary* for
   the general upper bound — itself a valuable structural finding, not a
   dead end.

3. **Use strong induction directly at the vertex-evaluation step, rather
   than needing all three Box walls pre-closed**, to route around the
   $n\ge4$ conditionality flagged in §1. Concretely: assume the full
   upper-bound theorem $P(n-1)$ (all cases, not just (b2)) as the
   induction hypothesis, and show *within the chamber-vertex proof
   itself* that any vertex landing on $\overline{\mathrm{Box}}\setminus
   \mathrm{Box}$ is covered by $P(n-1)$ applied to the *same* marking
   restricted/rescaled appropriately (rather than citing the file's own
   separately-conditional case-(a)/$p_1\ge T/2$ closures, which is where
   the circularity risk actually lives). This is a genuine reframing of
   the compactness fix as an inductive-step lemma rather than a
   free-standing corollary, and would make the whole Chamber-Vertex
   machinery usable at every $n$ under one uniform induction hypothesis,
   matching how every other case in this project's strong induction is
   already structured. Frame this as a fix to the *scope/statement* of
   item 3, not a re-derivation of items 1–2 (which the reviewer confirmed
   sound).

## 5. Crux corpus / knowledge_base check

`knowledge_base.md` has no dedicated entry on LP-vertex/extreme-point
enumeration for combinatorial optimization beyond the generic geometry
note used elsewhere in this project (Minkowski–Weyl, convex-combination
argument for affine functionals on polytopes) — already fully exploited
by `vertex-minimum-theorem` and Theorem R22.2; nothing further to import
from the KB on this specific technique. I did not find a crux-corpus
entry specific to "evaluate all vertices of a polytope cut out by
combinatorial-type constraints" beyond what's already in use; if the
corpus has an `lp_duality`/`polytope` subtopic under `combinatorics` not
yet queried, a future round could check `crux_moves_documentation.md`'s
subtopic index directly, but nothing in this pass's grep of the approach
file or KB suggested an unused applicable crux move — the project's own
machinery (vertex-minimum-theorem → chamber-vertex theorem) is already the
right tool; the missing piece is finishing the finite check, not finding
a new theorem to import.

## Summary for the orchestrator

The Chamber-Vertex Theorem is sound infrastructure (items 1–2 certified
clean); item 3's general-$n$ claim is genuinely over-scoped and needs
restating as "$n\le3$ unconditional, $n\ge4$ conditional on the standing
IH" (round-23 fix, straightforward). The real remaining work is exactly
the finite vertex evaluation, for which two concrete, non-dead-end paths
exist right now: (a) a fully unconditional $n=3$ exhaustive chamber
enumeration (small, tractable, would be a genuine milestone), and (b) the
already-reduced but unsolved Route-A finite optimization over
$(X,q)$-shaped vertices for the "cut-$p_1$-only" restricted family. Both
reuse only already-certified lemmas (`odd-run-reduction-lemma`,
`pair-cancellation-identity`, `vertex-minimum-theorem`, Lemma R22.1/Thm
R22.2) — no new machinery needs to be invented, only the case-check
carried out. Avoid all nine dead mechanisms listed in §3.
