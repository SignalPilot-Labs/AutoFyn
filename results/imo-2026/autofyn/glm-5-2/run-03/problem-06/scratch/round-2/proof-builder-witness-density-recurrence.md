# proof-builder — witness-density-recurrence (round 2)

## Verdict: CIRCULAR (honestly recorded); Status partial; RETHINK candidate.

The dispatch asked me to either find a NON-circular covering-capacity bound for Step 5, or honestly conclude the approach is circular. **I honestly conclude it is circular, and the minimal-criminal induction does not de-circularize it.** No false proof is presented.

## What is proved (sound, non-circular)

**Lemma W1 (witness-index spacing).** *Conditional on Premise W0.* A governing prime $q$'s private-witness indices $i_k$ satisfy $i_{k+1}-i_k\ge q/M_1$, so the re-witnessing density is $\le M_1/q$ (in particular $<1$ when $q>M_1$).

Proof uses only: (a) distinct witnesses are distinct multiples of $q$, so differ by $\ge q$; (b) the certified gap bound $d_n\le M_1$. No covering capacity, no Gap-A assumption. This is the approach's one sound output.

## What is circular (Step 5, the load-bearing lower bound)

The desired density-incompatibility: governance forces re-witnessing density $\ge 1/C$ for some finite $C=C(|P_1|)$, giving $q\le M_1\cdot C$. The mechanism — covering capacity of $T\setminus\{q\}$ — is **unbounded for the greedy-sequence family unless the primes in intermediate supports are bounded**, which IS Gap A. Confirmed structurally.

### Why the minimal-criminal rescue fails (two independent reasons)

The reviewer's suggested angle: take $q$ = smallest governing prime $>M_1$, so other governing primes are $\le M_1$ or $\ge q$; intermediate supports' large primes are then "handled by the same induction." I attempted to make this rigorous. It does NOT close, for two structural reasons:

1. **Transient primes provide unbounded covering capacity, compatibly with Gap A.** The minimal-criminal choice excludes only primes in $(M_1,q)$ from being *governing*. It says nothing about *transient* primes (finite-lived in $G_n$). A transient prime can serve as a hitter in a $q$-free MT during its finite lifetime, and there can be infinitely many distinct transient primes over the sequence while the governing set stays finite (verified for $a_1=145$: transient primes $7,11,\dots,67$ at $n=40$, all dropped by the lock at $n=97$). The covering capacity of $q$-free MTs is therefore unbounded *even when Gap A is true*. Unbounded covering capacity is consistent with Gap A — so no contradiction follows.

2. **Governing primes $\ge q$ are not handled by the descent.** The "induction on the order of governing primes $>M_1$" is a single-step descent (the base is free by minimality of $q$), not a recursion. Primes $\ge q$ invoked in intermediate supports are NOT $<q$, so the induction has no purchase on them. The dispatch's own warning is decisive: witnesses $\ge q$ other than $q$ can carry $q$ as a cofactor and re-witness it; the induction "pushes the problem to the next prime up," not down — not well-founded.

### Bad configuration (concrete)

Intermediate supports of the form $\{q, r_k\}$ with $r_k$ fresh primes (transient or governing $\ge q$): each is hit by $T\ni q$ but NOT by $T\setminus\{q\}$. A $q$-free transversal must include each $r_k$. Covering capacity = number of such supports absorbable without $q$ = unbounded (one fresh prime each). The star $\{\{1,j\}\}$ and projective-plane lines give the abstract shadow.

## Secondary gap (honestly marked)

**Premise W0** (governing $\Rightarrow$ infinitely many distinct private-witness indices) is plausible but unproved. The reduction "governing $\Rightarrow q$ divides infinitely many $a_i$" is itself non-trivial: $q$ could in principle divide only finitely many terms and stay in $\operatorname{MT}(\mathcal F_n)$ for infinitely many $n$ via a fixed finite witness set and a growing $T\setminus\{q\}$ transversing the tail family. Whether minimality of $T$ forbids this indefinitely was not resolved. W1 is recorded as conditional on W0.

## Why W1 alone does not close Gap A

W1 is only an *upper* bound on density ($\le M_1/q$). A prime $q>M_1$ can be re-witnessed infinitely often at arbitrarily low density (e.g. at indices $\lfloor k q/M_1\rfloor$), consistent with both W1 and governance. Without a matching *lower* bound, no contradiction.

## Empirical checks performed

- $a_1=385$: MT primes at $n\in\{11,21,31,40\}$ all in $\{2,3,5,7,11,19\}\le M_1=385$. No large governing prime (consistent with $w_n\equiv+\infty$ in real data — the density argument only lives in a proof-by-contradiction world).
- $a_1=145$: MT-prime set grows with $n$ ($\{2,3,5,7,11,13,29,31,37,41,43,47,53,59,61,67\}$ at $n=40$), all $\le M_1=145$, and **drops to $\{5\}$** at the lock ($n=97$). Each of $7,11,\dots,67$ is transient. Confirms: transient primes are unbounded in number over the sequence, compatible with Gap A.
- $a_1\in\{77,2085,1309\}$: MT primes stay $\le M_1$ throughout (no large governing prime). The hypothetical world ($q>M_1$ governing) cannot be empirically tested; the circularity is a structural argument, not empirical.

## Recommendation for next round

RETHINK / RETIRE this approach. The spacing half is sound but insufficient; the density-incompatibility half is circular and the minimal-criminal rescue fails structurally (transient primes + non-well-founded upward induction). The approach does not provide an independent route to Gap A — it is a third *costume* over the same wall, as the reviewer's diversity-check feared. If the orchestrator wants a genuinely different framing, it must attack from outside the "tame the abstract unboundedness of pairwise-intersecting transversal primes" frame entirely (e.g. a direct residue-map/finite-state periodicity argument, or a structural result on the greedy pick as a function of the $P_1$-support stream).

## Files touched
- Wrote: `/home/agentuser/repo/results/imo-2026-06/approaches/witness-density-recurrence.md` (Status: partial; full proof attempt with circularity honestly marked; no false claim).
- Read: `current.md`, all `lemmas/*.md`, `transversal-saturation.md`, `/tmp/round-2/proof-outliner.md`, `/tmp/round-2/outline-reviewer.md`, `knowledge_base.md`, `crux_moves_documentation.md`.
