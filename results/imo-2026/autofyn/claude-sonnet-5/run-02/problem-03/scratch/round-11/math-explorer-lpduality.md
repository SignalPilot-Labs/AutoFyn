## imo-2026-03 (lens: lp-duality-certificate — Route A pin-set fix + p1<T/2 mechanism reuse)

- Distinct openings:
  1. **Mechanical pin-set fix for Route A (Lemma A.1 / A.2).** The lemma's
     *proof* already defines the exchange reference set as
     $\mathcal R:=\{0,\tau_1,\dots,\tau_r\}$ (line 786 of the approach file)
     and explicitly uses "$f_j$ hitting $0$" as a genuine boundary case
     throughout the exchange argument — but the lemma's literal *statement*
     (lines 763-769) only allows pinning to
     $\tau_{l_1},\dots,\tau_{l_p}\in\{\tau_1,\dots,\tau_r\}$, omitting 0. This
     is exactly the gap round 10's reviewer found and declined to certify.
     The fix is purely textual: restate Lemma A.1's conclusion as "$p$
     coordinates pinned to values in $\{0,\tau_1,\dots,\tau_r\}$ (repetition
     allowed, including possibly pinning several coordinates to 0), the
     remaining $k-p$ tied to one common value $v$." Downstream, A.2/A.3 need
     one added sentence, not a re-derivation: a coordinate pinned to $0$ is a
     genuinely degenerate/wasted "cut" (see cheap-kill check below) — it
     changes neither $E$ nor $A$ nor $\Phi$, so it is exactly equivalent to
     simply using one fewer real cut at that budget level. Since A.2/A.3
     already range over all budgets $k=1,\dots,n+1$ and characterize by
     $X\subseteq\{1,\dots,n\}$ (unpinned tail levels) and $q$ (free-value
     count), a 0-pin adds no new vertex *shape* to the finite family already
     enumerated in A.3 — it only means some of the "wasted" pin slots do
     literal nothing, which the existing enumeration already implicitly
     allows for (since $p=n-|X|$ can already include pins that don't move
     the needle if $q$, $X$ are otherwise unaffected). **Verified numerically
     (exact `Fraction`, not float)**: for tail $\{1/4,1/4,1/8\}$ and $p_1=3/8$
     split as $\{1/4,1/8\}$ (2 real parts) vs. the same split with an
     explicit inert $0$ fragment inserted (3 parts), $\Phi$ is identical
     ($5/8$ in both cases) — confirms a 0-pinned coordinate is harmless to
     $\Phi$, so adding 0 to the pin set cannot break anything already proved
     in A.2/A.3; it only makes the *statement* match what the *proof* (and
     A.3's actual usage) already needs. **This is a low-risk, mechanical,
     one-round fix — not a new mechanism search.**
  2. **Bigger structural finding (the more important opening this round):**
     Route A's Lemma A.1 is a special case, not a new general result — the
     already-certified, marking-agnostic `vertex-minimum-theorem` (see
     `lemmas/vertex-minimum-theorem.md`) already states the vertex
     characterization for **any** legal composition $(c_1,\dots,c_{n+1})$
     of Xiang Yu's cut budget across **all** pieces, not just "$k-1$ cuts
     spent entirely on $p_1$, tail untouched." Route A chose to restrict to
     the $p_1$-only composition family, and its own honest accounting (§A.3,
     lines 887-889) already flags that this restriction may be
     *structurally* insufficient: "a full-marking strategy touching the
     tail as well remains available and is not covered by this restricted
     family." This is not a hypothetical worry — it is a **confirmed fact**:
     both of this project's own on-file resolutions of hard $p_1<T/2$
     witnesses use tail-touching strategies that a "cut-$p_1$-only" family
     can never express — Theorem D′ (bisect $p_1$ **and** $p_m$
     simultaneously) resolves $(3/8,1/4,1/4,1/8)$, and Theorem B$_k$
     ($k=4$, peel $p_1$ against $p_4$) plus a further bisection of $p_3$
     resolves $(2/5,3/10,1/5,1/10)$ — neither touches only $p_1$. So even
     after Route A's pin-set fix and even after fully solving A.3's finite
     optimization for the $p_1$-only family, Route A **cannot by itself**
     close the $p_1<T/2$ regime — it can at best prove a (possibly empty)
     sufficient sub-condition, structurally analogous to (and no stronger
     in kind than) the already-superseded Theorems A/B/C. The genuinely
     more promising route: apply `vertex-minimum-theorem` **directly, with
     no per-piece restriction**, to an arbitrary marking with $p_1<T/2$ —
     this already gives, for free (already proved, already certified,
     already marking-agnostic per rule "round 10"), the full finite vertex
     family (tie/degenerate-cut constraints spanning fragments of *any*
     piece, not just $p_1$'s). The open content shifts entirely to
     *evaluating* that full family via `odd-run-reduction-lemma` for an
     arbitrary (not ladder-specific) tail — mirroring exactly the recipe
     that closed Case I of Claim (A) on the lower-bound side
     (`exchange-smoothing-vertex-maximization` + `odd-run-reduction-lemma`
     + Ratio-2 Spacing Lemma + Last-Element Bound), except the two
     ladder-specific evaluation lemmas (Ratio-2 Spacing, Last-Element
     Bound) do **not** transfer here (already established, rule 17) since
     the tail is now arbitrary — a genuinely new evaluation argument for
     arbitrary tails is needed, not a re-derivation of Route A's narrower
     lemma.

- Candidate technique(s): (1) mechanical restatement fix of Lemma A.1's pin
  set to include 0 (no new proof needed, the existing proof already
  supports it); (2) drop the "cut-$p_1$-only" restriction and invoke
  `vertex-minimum-theorem` directly over the full composition space for
  arbitrary markings with $p_1<T/2$, then attempt an evaluation argument
  (via `odd-run-reduction-lemma`) analogous to, but not identical to, the
  Case I Closure Theorem's — this is the natural next target, not yet
  attempted in this generality by any approach on file.

- Cheap-kill candidates: the 0-pin-harmlessness fact (exact-`Fraction`
  verified above: inserting an inert 0-length fragment never changes $\Phi$,
  since a zero element sits at the very bottom of the sorted order and
  cannot alter the rank-parity of any positive element above it) is a cheap,
  general structural fact worth stating as a one-line lemma before the pin
  fix — it is exactly what makes the fix safe. No other cheap kill found for
  the harder reframing (2); that one requires real evaluation work.

- Knowledge-base entries to use: none new beyond what's already cited in
  `current.md` — this front is driven entirely by internally-certified
  project lemmas (`vertex-minimum-theorem`, `odd-run-reduction-lemma`,
  `pair-cancellation-identity`, `exchange-smoothing-vertex-maximization`,
  `case-i-closure-theorem`, `telescoping-threshold-identity`), not
  `knowledge_base.md` generic entries. (`knowledge_base.md` was checked; per
  round-1's finding, this problem has no direct external theorem match, and
  nothing new in it bears on this specific pin-set/vertex-reuse question.)

- Analogous past problems (cruxes): none newly relevant for this narrow
  lens beyond what prior rounds already found (round 1 confirmed no strong
  crux-corpus analog for the whole problem). Did not re-query the corpus
  this round since the dispatch scope is a targeted internal fix + internal
  mechanism reuse, not a fresh external-technique search.

- Prior progress: see `current.md` round 10 summary — Route A's Lemma A.1
  proved but not certified (pin-set gap); Route A's A.2/A.3 give a
  characterized-but-unsolved finite optimization for the cut-$p_1$-only
  family; Route B (iterated-greedy-peel) is a confirmed dead end (~62%
  failure rate). The $p_1\ge T/2$ regime is fully closed for $n\le3$
  (Theorem C′ + telescoping-threshold-identity); $p_1<T/2$ remains open for
  $n\ge2$ in general (both on-file hard witnesses resolved individually by
  ad hoc tail-touching strategies, not by a closed-form template).

- Dead ends (do not retry): Route B's iterated-greedy-peel-identity
  construction (confirmed round 10, ~62% random-trial failure rate) — do
  not extend or repair this specific greedy rule, per the dispatch note.
  Also do not re-attempt Theorem D′/E's IH-ceiling mechanism as a
  general-$n$ closed-form sufficient condition — round 9 proved it never
  certifies the equal-pieces marking for any $n\ge2$ (`dprime-equal-
  pieces-insufficiency`).

- Small-case / intuition notes (conjecture, exact-`Fraction`-checked only at
  the instances shown, not proved in general): (i) a 0-pinned coordinate is
  exactly inert to $\Phi$ (verified at one instance, but the argument —
  a zero element cannot sit above any positive element in sorted order, so
  it cannot change any other element's rank parity — is fully general and
  should be written as a one-line lemma, not left as a numeric spot-check,
  in the actual fix); (ii) both known $p_1<T/2$ hard witnesses are resolved
  only by strategies cutting a piece other than $p_1$ (confirmed by direct
  inspection of Theorem D′'s and Theorem B$_4$'s constructions in the
  approach file, not new computation) — this is not a conjecture, it is a
  fact already on file, but its consequence for Route A's scope (that
  restricting to "cut $p_1$ only" cannot possibly close $p_1<T/2$ in
  general) had not been stated this bluntly before and should reorient next
  round's Route A work away from further narrow-family evaluation and
  toward the full, unrestricted `vertex-minimum-theorem` application.
