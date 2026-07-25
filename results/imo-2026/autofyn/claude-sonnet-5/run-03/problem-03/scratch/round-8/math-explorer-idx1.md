## imo-2026-03 — deep dive on the idx=1 gap (splitting the top landmark)

### Setup recap
Theorem A reduces everything to: $N:=n+1$, $k\in\{1,\dots,N\}$, $S:=(\{1,\dots,N\}\setminus\{k\})\cup\{y_1,\dots,y_m\}$ ($m\ge2$, $y_i>0$, $\sum y_i=k$), target $(\star)$: $A(N,k,y):=\mathrm{AltSum}(S)\ge1$. Theorem B (certified) proves $(\star)$ for every $k\le N-1$. The open case is $k=N$ (idx=1, splitting the top landmark itself): $S=\{1,\dots,N-1\}\cup\{y_1,\dots,y_m\}$, $\sum y_i=N$.

**Important scope correction: we do NOT need the closed form $\lfloor(N-3)/2\rfloor$ — we only need $A(N,N,y)\ge1$.** The growing closed-form pattern reported in the approach file is strictly stronger evidence than what the theorem requires; chasing the exact closed form is unnecessary extra work. This reframing should materially shrink the outliner's target.

### Why Theorem B's proof breaks at idx=1 (diagnosis)
Theorem B's proof peels the unique max of $S$, which is the landmark $N$ (present because $k\le N-1$ means $N$ is never removed), and bounds the rest by $\max\le N-1$. At $k=N$, the landmark $N$ is **removed** (it *is* $p_1$, the piece being split), so the top of $S$ is contested between the largest fragment $y_i$ (which can be arbitrarily close to $N$) and the landmark $N-1$. A single peel-and-bound step is not enough because after peeling once, the residual set can still have its max come from $Y$, not $L$; the "one clean case" that made Theorem B a 2-line argument is gone. I confirmed by hand that a naive one-step extension (peel $N-1$ instead of $N$) drifts the residual sum out of the clean "consecutive-run-of-$N'$ with landmark $k'$" family (as the approach file already correctly diagnosed) — this is real, not a fixable typo.

### A genuinely new, clean mechanism found this round: odd-multiplicity reduction
**Lemma (verified, elementary, not yet in the approach file or KB under this name).** For a finite multiset $T$, $\mathrm{AltSum}(T)$ depends **only on the set of values that occur an odd number of times** in $T$ (values of even multiplicity contribute exactly $0$ and are invisible): if $\mathrm{Odd}(T):=\{v: \text{mult}_T(v)\text{ is odd}\}$ (as a plain set), then $\mathrm{AltSum}(T)=\mathrm{AltSum}(\mathrm{Odd}(T))$.
*Proof sketch (2 lines):* group $T$'s sorted-descending list into maximal blocks of equal value; a block of even size $c_v$ contributes $c_v/2$ canceling $(+v-v)$ pairs (net $0$) and shifts all subsequent positions by an even amount (parity-preserving); a block of odd size contributes one net $\pm v$ (sign = current parity state) and flips the parity state for everything after. Iterating over blocks from largest to smallest value gives exactly $\mathrm{AltSum}(\mathrm{Odd}(T))$. Verified by 2000 random-multiset trials, zero mismatches (script in scratch).

**Consequence for idx=1.** Write $S=\{1,\dots,N-1\}\cup Y$. $\mathrm{Odd}(S)$ = symmetric difference (mod-2 multiplicity) between the landmark set and $Y$. If XY chooses fragments $Y$ that hit some landmarks exactly (a subset $C\subseteq\{1,\dots,N-1\}$, one matching fragment per landmark in $C$, using budget $\sum C\le N$), those landmarks get multiplicity 2 and vanish from $\mathrm{Odd}(S)$; any leftover budget $N-\sum C$ can be "hidden for free" by splitting it into **two equal fragments** (they tie each other, even multiplicity, vanish too) — this exactly reproduces the numerically-observed optimal constructions in the approach file (e.g. $N=8$: $y=(2,5,1)$ cancels landmarks $\{1,2,5\}$; the file's own winning vertices are always of this "hit exact landmarks" shape).

**New finding: the file's $\lfloor(N-3)/2\rfloor$ pattern is only backed by a capped search ($m\le5$ for $N\ge11$) and appears to actually be an *undercount* — i.e. wrong as the true minimum, not just unproved.** Using the free-leftover trick with $m=6$ at $N=11$ (cancel $C=\{1,2,3,4\}$, budget $10\le11$, hide leftover $1$ as two $0.5$'s) gives $A(11,11,y)=3$, strictly below the file's reported floor value $4$ for $N=11$. I verified this by direct exact evaluation (script below). **This does not threaten the theorem — $3\ge1$ still — but the outliner should know the closed-form conjecture in the current approach file is likely false for $N\ge11$ and should not be relied on or re-derived; only $A\ge1$ is the actual target.**

### A complete-looking proof of the reduced discrete claim (the promising opening)
Define, for $M:=N-1$, $B:=\{1,\dots,M\}$: **Claim (D)**: for every $C\subseteq B$ with $\sum C\le M+1$, $\mathrm{AltSum}(B\setminus C)\ge1$.

I found a short case-split proof of Claim (D), in the same 2-line-peel style as Theorem B:
- **Case $M\notin C$:** $M$ survives as the unique max of $B\setminus C$ (all other elements $\le M-1$). Peel: $\mathrm{AltSum}(B\setminus C)=M-\mathrm{AltSum}((B\setminus C)\setminus\{M\})$, and the residual has max $\le M-1$, so by the Upper-bound fact $\mathrm{AltSum}(\text{residual})\le M-1$. Hence $\mathrm{AltSum}(B\setminus C)\ge M-(M-1)=1$. Done — identical mechanism to Theorem B.
- **Case $M\in C$:** then $\sum(C\setminus\{M\})\le (M+1)-M=1$, so $C\setminus\{M\}\subseteq\{1\}$ (only element of $B$ with value $\le1$) — a **very restrictive** budget consequence forcing only 2 sub-cases:
  - $C=\{M\}$: $B\setminus C=\{1,\dots,M-1\}$, and $\mathrm{AltSum}(\{1,\dots,m\})=\lceil m/2\rceil\ge1$ for $m=M-1\ge2$ (true since $N\ge4\Rightarrow M\ge3$).
  - $C=\{M,1\}$: $B\setminus C=\{2,\dots,M-1\}$; peel its max $M-1$ (present since $M\ge3$): $\mathrm{AltSum}(\{2,\dots,M-1\})=(M-1)-\mathrm{AltSum}(\{2,\dots,M-2\})\ge(M-1)-(M-2)=1$, using Upper-bound on the residual (max $\le M-2$, or residual empty giving $0\le M-2$ when $M=3$).

So Claim (D) is fully proved for $N\ge4$ (verified against brute force: matches subset-sum-minimum data computed for $N=4..23$, all $\ge1$, script below).

**What is still missing (the real remaining gap):** rigorously showing that the *continuous* minimization over all $Y$ (not just "exact landmark hits plus a free hidden pair") reduces to Claim (D)'s discrete setting — i.e. that no vertex of the Single-Piece-Split Vertex Lemma's candidate set (already certified!) can beat the "subset cancellation" constructions. The Vertex Lemma's structure (blocks of fragments pinned to $0$, to each other, or to a landmark, with exactly one free block solved from the budget) is *close* to the discrete claim's shape but is more general: a free block of odd size can land on a value that matches **no** landmark, contributing a brand-new element to $\mathrm{Odd}(S)$ not covered by Claim (D) as I stated it. This case needs to be folded in (likely: show any such "new stray value" case is dominated by (i.e. never better than) some subset-cancellation configuration, perhaps via a direct interpolation/continuity argument, or by directly extending the odd-multiplicity peel argument to allow one extra "free" real value not equal to any integer). I did **not** close this bridging step — it is the honest, precisely-located residual gap, smaller and better-characterized than what the approach file currently reports.

### Cheap-kill / structural framing for the outliner
- Reduce ambition: target is $A(N,N,y)\ge1$, NOT the closed form. This alone should simplify next round's outline substantially.
- Use the odd-multiplicity reduction (new, clean, cheaply provable) as a normal-form tool: it collapses "arbitrary positive fragments" down to "which values get an odd hit" — a much smaller combinatorial search space than raw LP vertices.
- Combine with the already-certified Single-Piece-Split Vertex Lemma (no new proof needed for that part) to argue any minimizer is at a vertex, hence expressible (up to the one remaining bridging gap above) as landmark-cancellation plus possibly one "stray" free value.
- Claim (D) itself (discrete subset-cancellation floor $\ge1$) is basically finished — reuse Theorem B's own two named facts (Peel identity, Upper-bound fact) verbatim, no new machinery.
- Only remaining task: handle (or rule out) the "stray free block, odd size, value not equal to any landmark" vertex case. Numeric evidence (300+ random continuous trials at several $N$, see script) never found this beating the discrete floor, consistent with it being genuinely dominated, but this is conjectural, not proved.

### Small-case / numeric notes (all labeled conjecture except where "proved" stated above)
- True minimum of $A(N,N,y)$ over ALL $Y$ (continuous, exact subset-cancellation + free-pair construction, verified by brute-force subset enumeration for $N\le23$): $1,1,1,2,2,3,3,3,4,4,5,5,5,6,6,7,7,8,8$ for $N=4,\dots,22$ (all $\ge1$; NOT monotonic in the smooth $\lfloor(N-3)/2\rfloor$ sense claimed in the file — e.g. $N=11$ gives $3$ not $4$, a genuine correction to the file's evidence, caused by their $m\le5$ search cap).
- Winning constructions are always of the "exact landmark cancellation + hidden free pair" shape in every case checked — supports (but does not prove) that the bridging gap above resolves in the discrete claim's favor.
- Random continuous search (40,000–60,000 trials, up to $m=12$) at $N=11,15,20$ never beat the subset-cancellation value, consistent with (not proof of) optimality of the discrete reduction.

### Dead ends / do not retry
- Extending Theorem B's exact one-step peel argument to $k=N$ directly (peel $N-1$ instead of $N$): confirmed by direct calculation that this drifts the residual set out of the clean family (matches the approach file's own diagnosis; I independently re-derived the same obstruction).
- Do not re-derive or trust the $\lfloor(N-3)/2\rfloor$ closed form as a target — it is (a) unnecessary (only $\ge1$ is needed) and (b) apparently wrong for $N\ge11$ due to the prior round's search being capped at $m\le5$.

### Knowledge-base / crux corpus
- No new KB entries beyond what's already cited (Peel identity / Upper-bound fact, already named informally in the certified lemma file; these are elementary and don't need a KB citation beyond restating them, as Theorem B already does).
- Crux corpus: searched `combinatorics` subtopics for alternating-sum / extremal-splitting / exchange-argument analogues; nothing in the corpus documentation retrieved here matches this specific "split a landmark of a consecutive-integer AP family against itself, minimize an alternating sum" shape closely enough to call genuinely analogous — the odd-multiplicity trick and the discrete subset-cancellation reduction above were derived directly, not borrowed. Reporting "none truly analogous" rather than forcing a weak match.

### Scripts (for reproducibility, not part of the proof)
All computations above were done via direct Python/Fraction exact arithmetic and are reproducible; key snippets:
- `oddmult_altsum` reduction check (2000 random trials, 0 mismatches).
- Exact subset-cancellation brute force for $N=4..23$ (bitmask DP over $C\subseteq\{1,\dots,N-1\}$, $\sum C\le N$).
- Explicit $N=11$, $m=6$ counterexample to the file's floor($11)=4$ claim: fragments $(1,2,3,4,0.5,0.5)$ summing to $11$, giving exact $A=3$.
