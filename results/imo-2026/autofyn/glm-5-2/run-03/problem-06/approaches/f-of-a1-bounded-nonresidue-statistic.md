# Approach: `f-of-a1-bounded-nonresidue-statistic` (round 7, NEW)

**Target.** The whole theorem — prove finiteness of the governing-prime set (real Gap A) by exhibiting an $f(a_1)$-bounded (NOT $f(\mathrm{rad})$-bounded) NON-RESIDUE finite statistic whose pigeonhole self-coincidence propagates to $d$-periodicity via the certified `aimo-0907-coincidence-criterion` (part A), clearing both the rad-77 fence (by $f(a_1)$) and the no-fixed-modulus fence (by being non-residue).

**Statistic.** The set-valued **$D_n$-window** $\sigma_n := (D_{n-k+1},\dots,D_n)$ where
$$D_n \;:=\; \{\, d\in\{1,\dots,M_1\}\;:\;\gcd(a_n+d,\,a_i)>1\ \text{for every }i\le n \,\}$$
is the admissible-increment set (certified `D_n-slack-obstruction` Step 1: $d_{n+1}=\min D_n$). This is RICHER than the fenced single-value $d_n$-window of round 4 (since $|D_n|\ge 2$ almost everywhere, by `D_n-slack-obstruction`), and is a non-residue statistic (a tuple of sets of offsets, not $a_n\bmod m$).

## Status

unsolved

## Approaches tried

- `f-of-a1-bounded-nonresidue-statistic` (round 7, NEW) — **DEAD (collapses to round-4 increment-window-automaton fence + circularity).** The skeleton's load-bearing empirical claim — "$D_n$-window forward-deterministic at a finite $k_* \ll T$, bounded by $f(a_1)$ not $f(\mathrm{rad})$" — was tested honestly with the corrected naive $O(N^2)$ gcd-greedy (the round-4 `fast_greedy.py` has an INVERTED subset bug; not used; cross-checked bit-exact vs the corrected `/tmp/round-6/mt_greedy.py` on $a_1\in\{15,385,847\}$). Two findings, both reviewer-gate-relevant:

  **(1) The outline-reviewer's "k_*=1" verification was a TAUTOLOGY.** The reviewer reported $k_*=1$ for $\{15,35,77,91,847,375\}$ and $k_*=16$ for $a_1=175$, claiming to test "$\sigma_n \to d_{n+1}$ (the NEXT increment, NOT the tautological $d_n=\min D_n$)." But $d_{n+1}=\min D_n$ IS the greedy rule (certified `linchpin-and-gap-bound` + `D_n-slack-obstruction` Step 1), so $\sigma_n \to d_{n+1}$ is TRIVIALLY single-valued at $k=1$ for EVERY $a_1$ (a function — the min). The reviewer's $k_*=1$ verdicts are this tautology; they prove nothing. (My probe reproduces $0$ conflicts on this map for every case at $k=1$, exactly as expected from the greedy rule.)

  **(2) The REAL load-bearing claim — the set-to-set forward map $\sigma_n \to \sigma_{n+1}$, which is what `aimo-0907` part A needs to propagate a self-coincidence to periodicity — REFUTED.** Honest probe of the real map (Step 0, mandated by the reviewer) on the rad-77 pair, both refutation witnesses, and $a_1=9375$:

  | $a_1$ | $M_1$ | $T$ | $k_*$ (real, set-to-set) | realized states at $k_*$ | ratio $k_*/T$ | realized$/T$ |
  |---|---|---|---|---|---|---|
  | 15 | 15 | 8 | $1$ | 10 | 0.125 | 1.25 |
  | 35 | 35 | 34 | $2$ | 37 | 0.059 | 1.09 |
  | 77 | 77 | 18 | $1$ | 21 | 0.056 | 1.17 |
  | 91 | 91 | 20 | $1$ | 22 | 0.050 | 1.10 |
  | 175 | 35 | 274 | $\in(17,24]$ (resolves at $24$) | 278 | $\approx 0.073$–$0.088$ | 1.01 |
  | 375 | 15 | 852 | $\in(65,128]$ (resolves by $128$) | 858 | $\approx 0.076$–$0.150$ | 1.01 |
  | 847 | 77 | 1744 | $\in(65,128]$ (resolves by $128$) | 1751 | $\approx 0.037$–$0.073$ | 1.004 |
  | 9375 | 15 | 3108 | $\in(129,512]$ (resolves by $512$) | 3110 | $\approx 0.041$–$0.165$ | 1.00 |

  Three independent obstructions kill the route:

  **(a) $k_*$ grows with $T$ (hence with $a_1$), not with $\mathrm{rad}$.** The rad-77 pair — the fence-clearing test — gives $a_1=77\to k_*=1$ vs $a_1=847\to k_*\in(65,128]$: same $\mathrm{rad}=77$, $k_*$ jumps $\ge 65\times$. So $k_*$ is NOT $f(\mathrm{rad})$-bounded (the rad-77 fence is "respected" in the narrow sense that the bound differs across the pair — but only because $k_*$ itself ballooned). The skeleton's hope that $k_*$ is $f(a_1)$-bounded and $\ll T$ is refuted: $k_*$ tracks $T$ roughly linearly (ratio $\in[0.04,0.17]$) across the stress set.

  **(b) The realized state count at $k=k_*$ is $\approx T$** — the EXACT signature of the round-4 increment-window-automaton fence ("realized $d_n$-window states number $\approx T$, unbounded in $M_1$"). Concretely: $a_1=847$ realizes $1751$ states at $k_*=128$ vs $T=1744$; $a_1=375$ realizes $858$ at $k_*=128$ vs $T=852$; $a_1=9375$ realizes $3110$ at $k_*=512$ vs $T=3108$. The $D_n$-window, though a strict refinement of the $d_n$-window as a PER-STEP symbol, realizes the SAME asymptotic state count $\approx T$ over the orbit. The slack that makes $|D_n|\ge 2$ almost everywhere does NOT translate into a smaller realized state set — it is "used up" by the orbit visiting more distinct $D$-configurations. The round-4 fence applies verbatim.

  **(c) CIRCULARITY (concrete, the reviewer's mandated test — REALIZED).** In the periodic regime with period $(T,L)$, the orbit satisfies $D_{n+T}=D_n$ for every $n$ (periodicity of $a$ + the constraint structure), hence $\sigma_{n+T}=\sigma_n$, so the forward map $\sigma_n\mapsto\sigma_{n+1}$ is single-valued at every $k\ge T$. Therefore **$k_*\le T$ always** (in the periodic regime). The approach's load-bearing claim "$k_*$ is finite" is, in the periodic regime, equivalent to "$T$ is finite" — i.e., to eventual periodicity itself. To prove $k_*$ finite WITHOUT assuming periodicity, one would need a STRUCTURAL argument (the skeleton's proposed "gap bound $d_n\le M_1$ + window-multiple counting") producing an $f(a_1)$-bound on $k_*$ that is independent of $T$. My probe REFUTES the existence of any such structural bound: $k_*$ tracks $T$ linearly across $\{175,375,847,9375\}$, with no hint of an $a_1$-only ceiling. Bounding the realized $\sigma$-state set (which is $\approx T$) IS proving $T$ bounded IS Gap A — the route presupposes exactly what it claims to prove.

  The route is dead. The reviewer's "most promising line in 7 rounds" assessment was an artifact of the tautology-testing error (finding 1): the trivial $\sigma_n\to d_{n+1}=\min D_n$ map gives $0$ conflicts at $k=1$ universally and was misread as empirical confirmation of forward-determinism. The genuine set-to-set map (the one `aimo-0907` part A actually requires) collapses to the round-4 fence + circularity.

  **One reusable negative deliverable (proposed lemma, below):** the **tautology-trap** — $\sigma_n\to d_{n+1}$ is trivially single-valued via $d_{n+1}=\min D_n$; any future "$D_n$-window is forward-deterministic" claim must be tested on the SET-TO-SET map $\sigma_n\to\sigma_{n+1}$ (or equivalently $\sigma_n\to D_{n+1}$), not on the trivial min-projection. This fences the specific error that produced the false-positive "k_*=1" verification this round.

## Current best

**Approach is dead.** The honest empirical finding (the genuine contribution of this round): the $D_n$-window's real forward-deterministic window-length $k_*$ (set-to-set map) is finite in every tested case but GROWS WITH $T$ (roughly linearly, ratio $\in[0.04,0.17]$), with realized-state-count $\approx T$ at $k=k_*$. The rad-77 pair ($a_1=77$: $k_*=1, T=18$ vs $a_1=847$: $k_*\in(65,128], T=1744$) confirms $k_*$ is NOT $f(\mathrm{rad})$-bounded — but it IS $\approx c\cdot T$, and the bound $k_*\le T$ (trivial from periodicity) makes "finiteness of $k_*$" equivalent to "finiteness of $T$" — i.e., to the theorem. The structural $f(a_1)$-bound on $k_*$ independent of $T$ that the skeleton hoped for does not exist empirically. The route collapses to the certified round-4 `ergodic-window-state / increment-window-automaton` fence ("state-size $\approx T$, unbounded in $M_1$, bounding $k_{\min}$ IS Gap A") plus the circularity the outline-reviewer's probe mandated testing. The $D_n$-window is NOT a structurally richer determining state in the sense that would escape the round-4 fence: per-step richness ($|D_n|\ge 2$) is exactly offset by greater orbit-wide variety (realized count $\approx T$).

**Open gap (the wall this approach hits).** The circularity $k_*\le T$ (in the periodic regime) is structural, not an artifact of insufficient probing: any forward-deterministic window statistic on the greedy orbit that refines to a single-valued map at window-length $k$ satisfies $k\le T$ in the periodic regime (by $\sigma_{n+T}=\sigma_n$), so its finiteness cannot be established without first establishing periodicity. This is the round-4 fence restated for the $D_n$-window. A non-circular route via this family of statistics would require a window statistic whose forward-determinism at finite $k$ is provable from the LOCAL greedy dynamics (gap bound, prime-window multiples) WITHOUT invoking global periodicity — and the linear $k_*\approx cT$ tracking across $\{175,375,847,9375\}$ is empirical evidence that no such local-only bound exists.

## Full proof

Not present — the approach is dead (Status `unsolved`). No proof is claimed.

## Promotable lemmas

**Lemma (negative, structural — PROPOSED for certification):** *the $D_n$-window forward-determinism tautology-trap.*

**Statement.** Let $a_1,a_2,\dots$ be the IMO 2026 P6 greedy sequence, $P_1$ the prime divisors of $a_1$, $M_1=\mathrm{rad}(a_1)$, and $D_n=\{d\in\{1,\dots,M_1\}:\gcd(a_n+d,a_i)>1\ \forall i\le n\}$ the admissible-increment set (so $d_{n+1}=\min D_n$ by the greedy rule, certified `linchpin-and-gap-bound` + `D_n-slack-obstruction` Step 1). For window length $k\ge 1$ let $\sigma_n=(D_{n-k+1},\dots,D_n)$. Then:

(a) The "increment-projection" map $\sigma_n\mapsto d_{n+1}$ is **trivially single-valued** at $k=1$ (and every $k\ge 1$) for every $a_1$, because $d_{n+1}=\min D_n$ is a function of $D_n\subseteq\sigma_n$. A "$0$-conflict" probe of this map (as reportedly produced this round) establishes NOTHING — it is a restatement of the greedy rule.

(b) The **load-bearing** map for any `aimo-0907-coincidence-criterion` (part A) pigeonhole route is the set-to-set forward map $\sigma_n\mapsto\sigma_{n+1}$ (equivalently $\sigma_n\mapsto D_{n+1}$, since the retained window entries are determined by $\sigma_n$). A self-coincidence $\sigma_a=\sigma_b$ propagates to $d$-periodicity ONLY through single-valuedness of THIS map.

(c) Empirically (corrected naive $O(N^2)$ gcd-greedy, cross-checked bit-exact vs `/tmp/round-6/mt_greedy.py`; $N>2T$ per case), the minimal forward-deterministic window-length $k_*$ for the set-to-set map and the realized state count at $k_*$ are:

| $a_1$ | $M_1$ | $T$ | $k_*$ (set-to-set) | realized states @ $k_*$ |
|---|---|---|---|---|
| 15 | 15 | 8 | 1 | 10 |
| 35 | 35 | 34 | 2 | 37 |
| 77 | 77 | 18 | 1 | 21 |
| 91 | 91 | 20 | 1 | 22 |
| 175 | 35 | 274 | $\in(17,24]$ | 278 |
| 375 | 15 | 852 | $\in(65,128]$ | 858 |
| 847 | 77 | 1744 | $\in(65,128]$ | 1751 |
| 9375 | 15 | 3108 | $\in(129,512]$ | 3110 |

$k_*$ is finite in every case but tracks $T$ roughly linearly (ratio $\in[0.04,0.17]$); the realized state count at $k_*$ is $\approx T$ in every case (ratio $\in[1.00,1.25]$). This is the round-4 increment-window-automaton fence signature ("realized $d_n$-window states $\approx T$, unbounded in $M_1$"). The rad-77 pair ($a_1=77$: $k_*=1$ vs $a_1=847$: $k_*\in(65,128]$ at the same $\mathrm{rad}=77$) shows $k_*$ is NOT $f(\mathrm{rad})$-bounded, but IS $\approx c\cdot T$.

(d) **Circularity (structural).** In any periodic regime with period $T$, $D_{n+T}=D_n$ (by periodicity of $a$ and the constraint structure), hence $\sigma_{n+T}=\sigma_n$, so the set-to-set forward map is single-valued at every $k\ge T$. Therefore $k_*\le T$ always in the periodic regime, and "finiteness of $k_*$" is equivalent to "finiteness of $T$" (eventual periodicity). A non-circular proof would require a LOCAL structural bound on $k_*$ independent of $T$; the linear $k_*\approx cT$ tracking across $\{175,375,847,9375\}$ is empirical evidence that no such local-only bound exists.

**Fence-conclusion.** The $D_n$-window pigeonhole route to periodicity — and any variant that tests "forward-determinism" only via the increment-projection $\sigma_n\mapsto d_{n+1}=\min D_n$ — is fenced: the increment-projection is a tautology (proves nothing), and the set-to-set map (the one actually needed) collapses to the round-4 increment-window-automaton fence + the $k_*\le T$ circularity. Future "$D_n$-window forward-deterministic at small $k$" claims MUST be tested on the set-to-set map, not the min-projection.

**Proof.** (a) $d_{n+1}=\min D_n$ by `linchpin-and-gap-bound` (gap bound $d_{n+1}\le M_1$) + `D_n-slack-obstruction` Step 1 (greedy rule = smallest admissible increment). Since $D_n\subseteq\sigma_n$ (for $k\ge 1$), $d_{n+1}$ is a function of $\sigma_n$; hence $\sigma_n=\sigma_{n'}\Rightarrow d_{n+1}=d_{n'+1}$ trivially. (b) `aimo-0907-coincidence-criterion` part A requires a single-valued map $F$ on the state with $\alpha(n+1)=F(\alpha(n))$; for $\alpha=\sigma$ this is the set-to-set map $F(\sigma_n)=\sigma_{n+1}$. A self-coincidence $\sigma_a=\sigma_b$ propagates to $\sigma_{a+k}=\sigma_{b+k}$ (all $k\ge 0$) ONLY through single-valuedness of $F$; the increment-projection (a) gives only the single step $d_{a+1}=d_{b+1}$, not full propagation. (c) Computational table (builder-run, cross-checked bit-exact vs the corrected MT-greedy; the round-4 `fast_greedy.py` has an inverted subset bug per run-state rules and was NOT used). Hand-verified $D_0=\{3,5,6,9,10,12,15\}$ for $a_1=15$ (size $7$, matching `D_n-slack-obstruction`). (d) Periodicity $a_{n+T}=a_n+L$ implies $a_{n+T}+d=a_n+d+L$ for each $d$, and the constraint set $\mathcal F_{n+T}$ stabilizes to the periodic admissible structure (every term lies in $\mathcal B_\infty$ by `every-term-in-binfinity`; the stabilized admissible set is $L$-periodic by `distinct-supports-stabilize`'s corollary conditional on Gap A — which the periodic regime presupposes). Hence $D_{n+T}=D_n$ and $\sigma_{n+T}=\sigma_n$, forcing single-valuedness of the forward map at $k\ge T$. $\square$

**Status:** proposed for reviewer certification as a negative structural fence (the tautology-trap + the round-4-fence-restatement for the $D_n$-window). Not yet certified.

## Spec concerns

1. **The outline-reviewer's round-7 "APPROVE for build — most promising line in 7 rounds" verdict was based on a tautology-testing error.** The reviewer's $k_*$ table tested $\sigma_n\to d_{n+1}$ (trivially $\min D_n$, $0$ conflicts universally) and misread it as empirical confirmation of forward-determinism. The honest set-to-set test (the one `aimo-0907` part A requires) refutes the central bet on every hard case ($a_1\in\{175,375,847,9375\}$). The reviewer's own gate ("If $k_*$ grows with rad or equals $T$ — the approach is DEAD") fires on the rad-77 pair ($k_*$ jumps $65\times$ at fixed rad) AND on the $k_*\le T$ circularity. The approach should be retired; the proposed tautology-trap lemma is the deliverable.

2. **The $f(a_1)$-vs-$f(\mathrm{rad})$ distinction is real but does not save the route.** $k_*$ is genuinely NOT $f(\mathrm{rad})$-bounded (rad-77 pair: $k_*=1$ vs $k_*\in(65,128]$), so the rad-77 fence is "respected" in the narrow sense. But $k_*\approx c\cdot T$ means the state-space bound $2^{k_*\cdot M_1}$ is astronomical AND its finiteness is circular with periodicity ($k_*\le T$). The fence-clearing is illusory: clearing the rad-77 fence requires the state bound to be finite AND $\ll T$-independent; only the first half holds, and it holds vacuously (circularly).

3. **Hand-enumeration of $D_0$ for $a_1=15$** (size $7$, set $\{3,5,6,9,10,12,15\}$) was performed first per the round-6 "ALWAYS hand-enumerate the smallest case" rule, and matches `D_n-slack-obstruction`'s table exactly. The computational probe uses the corrected greedy throughout (no round-4 `fast_greedy.py`).
