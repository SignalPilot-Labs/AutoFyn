## Statement (dead-end record, not a positive lemma)

The Iterated Greedy-Peel Construction (`iterated-greedy-peel-identity`),
run with the specific selection rule "always match the current two largest
elements of the working set," does **not** always achieve $\Phi\le a_nT$
for an arbitrary Liu Bang marking. Concretely:

- **Exact counterexample.** At $n=4$, the equal-pieces marking
  $p_i=1/5$ ($i=1,\dots,5$, $T=1$): every step of the construction is an
  "$a=b$" tie-step (all five pieces equal), using $0$ cuts throughout, and
  the process reduces $\{1/5^5\}\to\{1/5^3\}\to\{1/5\}$, giving
  $v_{\text{final}}=1/5$, $\Phi=(1+1/5)/2=3/5=0.6$. But
  $a_4T=16/31\approx0.5161$, and $3/5>16/31$. The construction fails at
  this point (the correct optimal strategy must actually cut one of the
  equal pieces, not merely match untouched pieces against each other).
- **Broader stress test.** An independent exact-`Fraction` random search
  ($2000$ trials, integer-ratio markings with denominators $\le50$,
  $m=2,\dots,6$ uniformly) finds the naive top-two-matching construction
  fails to meet $a_nT$ in $969/2000\approx48\%$ of trials.

## Diagnosis

The "always match top two" rule is too rigid: it never chooses to cut a
piece against a *smaller*, non-tied target, or to defer a tie in favor of
a more advantageous split elsewhere in the working set. Since the
underlying `iterated-greedy-peel-identity` exactly reproduces the true
optimal value at both on-file hard witnesses (via a different, smarter
sequence of matches than "always top two" would give at those points —
both witnesses happen to have their top-two coincide with a good match at
every step), the failure is specifically in the *selection rule*, not in
the identity/construction framework itself.

## Recommendation for future rounds

Do not re-attempt the literal "always match the current top two" rule as
a standalone universal proof of the general upper bound — it is refuted.
A future round could instead try: (a) a rule that prioritizes cutting a
piece to create a *small* leftover rather than merely matching the largest
available pair, (b) a rule informed by looking ahead (dynamic-programming
style) rather than purely greedy, or (c) combining the construction with
Route A's vertex characterization (this round's companion result) to
search the same finite family more intelligently. The reusable underlying
identity (`iterated-greedy-peel-identity`) remains valid and useful for
evaluating whatever selection rule is eventually chosen.

## Certification note

Recorded in `results/imo-2026-03/approaches/lp-duality-certificate.md`,
§B.5 (round 10), with both the exact counterexample and the random-search
statistics independently computed via `Fraction` arithmetic (no floating
point). This is a genuine, verified negative result about one specific
selection rule, not a report of the underlying identity being wrong.

**Certified by:** proof-reviewer, round 10 — independently re-derived the
exact $n=4$ equal-pieces counterexample ($\Phi=3/5>16/31=a_4T$, exact
match) and ran an independent 2000-trial stress test with a different
sampling method (uniform random compositions rather than the builder's
integer-ratio markings): found a $\approx62\%$ failure rate, corroborating
the same qualitative dead end (a different sampling method naturally gives
a different exact percentage, but both confirm "always match top two" is
not a universal strategy, by a wide margin). CERTIFIED as a dead-end
record.
