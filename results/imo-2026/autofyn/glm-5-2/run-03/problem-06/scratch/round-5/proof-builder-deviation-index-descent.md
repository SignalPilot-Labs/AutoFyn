# proof-builder — `deviation-index-descent`, imo-2026-06, round 5

## What I proved

Approach file: `/home/agentuser/repo/results/imo-2026-06/approaches/deviation-index-descent.md`. Status: **partial**.

**Rigorous and reusable this round:**
- **B1 (candidate-period existence)** — PROVED cleanly and non-circularly (Step 2). For the increment-word $(d_n)$ over the finite alphabet $\Sigma=\{1,\dots,M_1\}$ (certified by `linchpin-and-gap-bound`), for every window-length $w\ge1$ there exist $i<j$ with $d_{i+k}=d_{j+k}$ for $k=0,\dots,w-1$; the offset $P_0:=j-i$ is a candidate period. Non-circularity verified explicitly: uses only finiteness of $\Sigma$ + infiniteness of the word, presupposes no periodicity, bounds $P_0$ by nothing a priori. Matches the reviewer's certified-sound B1 (option (b)).
- **Mount imported** — Steps 1–6 of `minimal-criminal-schur-contradiction` cited by name (Step 3); well-ordering transfers from governing primes to deviation-indices by the same well-ordering of $\mathbb N$; the Schur Step 7 (fenced dead) is NOT re-walked.
- **Collapse (Step 5)** — clean conditional: IF the descent (B2) succeeds, no deviation exists, $d$ is $P_0$-periodic, and `cyclic-successor-bijection` + `greedy-equals-cyclic-successor` give $a_{n+T}=a_n+L$ from $n=1$.
- **Ported crux templates** (`aimo-0077`, `aimo-0009`) restated precisely (Step 1), with the concrete meaning of "deviation from a candidate period" spelled out (Step 1, last paragraph).

## The load-bearing gap (B2) — explicit, with a SHARP computationally-verified obstruction

The descent step B2 (greedy local rewriting turns a deviation at $n$ into a deviation at $m<n$) is **blocked by TWO independent fences**:

- **(B2-a) Cofactor-bound fence** (the one the reviewer warned about). The shift-by-$C$ ($C:=a_{j_0}-a_{i_0}$) that holds on the coincidence range $[i_0,n_0]$ (proved by telescoping) does NOT preserve the admissibility structure: $\gcd(a_{n_0+1}+C, a_{j-P_0}+C)$ has no forced relation to $\gcd(a_{n_0+1}, a_{j-P_0})$ unless $C$ is divisible by every governing prime — a cofactor-type requirement, fenced by `window-uniqueness-reduces-to-cofactor`, `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime`.

- **(B2-Sharp) Increment-window-automaton fence** (a SECOND fence the reviewer did not flag, but it bites). B2 cannot be a uniform mechanism in the window-length $w$: for small $w$ the pigeonhole offset $P_0(w)$ is NOT a period of $d$, and a real deviation exists (no contradiction is possible). **Computational witness:** $a_1=35$, $M_1=35$, true $T=34$, $L=210$. With $w=2$: $P_0(2)=5$ (NOT $34$), and a real deviation at $n_0=8$ ($d_8=4\neq10=d_{13}$, verified directly). With $w=8$: $P_0(8)=34=T$, no deviation. So if B2 were uniform it would FALSELY conclude periodicity for $w=2$. For B2 to have a chance, $w\ge w_{\min}$ (minimal window-length recovering the true period), and $w_{\min}$ is UNBOUNDED in $M_1$ — the round-4 `ergodic-window-state / increment-window-automaton` fence.

- **The forced-increment identity does NOT rescue B2** (Step 4''). It is FORWARD and LOCAL (determines $d_{m-1}$ at $q$-multiple steps from the residue $a_{m-1}\bmod q$); the descent needs BACKWARD and GLOBAL. The deviation index $n_0$ is set by the d-word coincidence structure, not by the $q$-multiple pattern, so we cannot ensure $a_{n_0+1}$ is a $q$-multiple; even if it were, "$q\nmid C$" is a statement about $C,q$, not a smaller-index deviation.

## Lemma proposals (two, for reviewer certification)

1. **`candidate-period-pigeonhole-existence`** (positive, unconditional). Statement: for $(d_n)$ over $\Sigma=\{1,\dots,M_1\}$, for every $w\ge1$ there exist $i<j$ with matching length-$w$ windows; $P_0:=j-i$ is a candidate period; non-circular. Caveat: $P_0(w)$ not necessarily a period for small $w$. Proved in Step 2.

2. **`deviation-descent-blocked-by-wmin-fence`** (negative, structural). Statement: the deviation-index descent cannot be a uniform mechanism in $w$ (computational witness $a_1=35$); requires $w\ge w_{\min}$, fenced (round-4 increment-window-automaton fence); AND the shift-by-$C$ requires $C$ divisible by all governing primes (cofactor fence). Proved in Steps 4, 4', 4''. Fences off future deviation-descent retries that do not first break one of the two fences.

## Verdict on the approach

CHANGES REQUESTED (partial). B1 + mount + collapse are rigorous and reusable. B2 is a genuine open gap with a sharp, computationally-verified obstruction: it reduces to TWO fences (cofactor-bound AND increment-window-automaton), neither of which is breakable with the tools on the table. The approach does NOT close Gap A. The two proposed lemmas (one positive sound ingredient, one negative structural fence) are the reusable deliverables.

## Honest note on the reviewer's B2 certification

The outline-reviewer certified B2 as the "LOAD-BEARING OPEN mechanism" and approved the build to test it. The build's honest finding: B2 is NOT merely open — it is REFUTED as a uniform mechanism (B2-Sharp, computational witness $a_1=35$), and the only greedy-specific ingredient that could power it (the forced-increment identity) is the wrong shape (forward/local vs backward/global). The reviewer's concern that "B2 must NOT reduce to cofactor-prime bounding" is confirmed (B2-a), and a SECOND fence (B2-Sharp, the increment-window fence) is identified that the reviewer did not flag. The approach is a clean negative result: the deviation-descent framing, while genuinely different, hits the same fenced wall from a new angle.
