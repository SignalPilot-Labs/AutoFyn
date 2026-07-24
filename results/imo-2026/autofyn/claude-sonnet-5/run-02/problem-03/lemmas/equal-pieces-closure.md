# Equal-Pieces Closure

**Source:** `results/imo-2026-03/approaches/lp-duality-certificate.md`, §R12.1 (round 12).

**Statement.** Fix $n\ge0$, $m=n+1$, and the marking with all $m$ pieces
equal, $p_i=T/m$ for every $i$ (i.e. Liu Bang marks $n$ equally-spaced
points). Then Xiang Yu has a legal response using $\le1$ cut achieving
$\Phi=T/2$ exactly, and $T/2<a_nT$ where $a_n=2^n/(2^{n+1}-1)$. Hence
$\Phi_{\min}\le a_nT$ at this marking, for every $n\ge0$.

**Proof.**

- **$m$ even.** Xiang Yu makes $0$ cuts. The final multiset
  $\{T/m\}^{\times m}$ decomposes into $m/2$ disjoint exact pairs. By the
  certified `pair-cancellation-identity` (applied $m/2$ times, valid
  regardless of order or sorted position), $A=0$, so $\Phi=(T+0)/2=T/2$.
- **$m$ odd, $m\ge3$ (i.e. $n\ge2$).** Xiang Yu bisects any single piece:
  $T/m\to(T/2m,T/2m)$ (1 cut). The final multiset is
  $\{T/m\}^{\times(m-1)}\cup\{T/2m,T/2m\}$: the $m-1$ (even) untouched
  pieces form $(m-1)/2$ exact pairs, plus one more exact pair from the two
  new fragments. By `pair-cancellation-identity` (applied $(m+1)/2$ times),
  $A=0$, so $\Phi=T/2$, using exactly $1\le n$ cut.
- **$m=1$ ($n=0$):** trivial base case, $\Phi=T=a_0T$ ($a_0=1$); no odd
  $m>1$ case arises at $n=0$.

Finally, $a_n>1/2$ for every $n\ge0$: this is the certified Telescoping
Threshold corollary (`results/imo-2026-03/approaches/lp-duality-
certificate.md`, §2: $a_k-1/2 = 1/(2D_k) > 0$ where $D_k=2^{k+1}-1$).
Hence $T/2<a_nT$, giving $\Phi_{\min}\le\Phi=T/2<a_nT$. $\blacksquare$

**Dependencies (all already certified, not re-derived):**
`pair-cancellation-identity`, the Telescoping Threshold fact $a_n>1/2$
(proved in full in `lp-duality-certificate.md` §2, general $n$, not a
finite check).

**Verification.** Independently re-checked by exact `Fraction`
computation for $m=2,\dots,7$ (both parities): the construction gives
$\Phi=1/2\cdot T$ exactly in every case, and $a_n>1/2$ holds by direct
computation for the same range. See round-12 proof-builder transcript.

**Significance / reusability.** Resolves, for every $n$, the equal-pieces
marking — a configuration independently flagged in round 11
(`per-piece-vertex-decomposition-theorem`'s open evaluation gap, R11.5) as
defeating three unrelated crude mechanisms (Theorem D's ceiling, the
naive Iterated Greedy-Peel "match top two" rule, and the crude
$A\le\mathrm{Total}$ bound applied to a joint vertex). This lemma resolves
that specific marking directly, by a mechanism outside the vertex-
evaluation framework, but does **not** extend to markings merely *near*
equal-pieces (its proof uses exact equality $p_i=T/m$ throughout) — a
future round extending this to a neighborhood of equal-pieces would need a
genuinely new continuity/perturbation argument.

**Certified by:** proof-reviewer, round 12 — independently re-verified by a
fresh exact-`Fraction` script (`/tmp/round-12/verify_lpdual.py`, not the
builder's own) for $n=0,\dots,7$: the construction gives $\Phi=T/2$ exactly
in every case (both parities of $m$), and $a_n>1/2$ strictly for every
$n\ge0$ by direct computation, matching the two-line algebraic proof.
CERTIFIED.
