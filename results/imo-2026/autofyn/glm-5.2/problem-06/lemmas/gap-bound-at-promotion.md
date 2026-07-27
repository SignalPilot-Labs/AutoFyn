# Lemma: gap-bound-at-promotion

**Statement (unconditional).** A **promotion** at step $i\ge2$ is a step where $P(a_i)\in\mathcal M_i\setminus\mathcal M_{i-1}$ (a new minimal support is introduced). Let $P_{\mathrm{ess},i-1}=\bigcup\mathcal M_{i-1}$ (the essential primes known through time $i-1$), and partition $P(a_i)=O\sqcup N$ with $N=P(a_i)\setminus P_{\mathrm{ess},i-1}$ (new primes) and $O=P(a_i)\cap P_{\mathrm{ess},i-1}$ (old essential primes). Then:

(i) $O\neq\emptyset$ and $O$ is a transversal of $\mathcal M_{i-1}$;
(ii) $a_i-a_{i-1}\le\prod_{p\in O}p$.

Consequently every new prime $q\in N$ divides $a_i$, so $q\le a_i\le a_{i-1}+\prod_{p\in O}p\le a_{i-1}+\prod_{p\in P_{\mathrm{ess},i-1}}p$.

**Proof.** (i) $P(a_i)$ is a transversal of $\mathcal M_{i-1}$ (admissibility, `transversal-residue-characterization` logic). A prime $q\in N$ lies in no member of $\mathcal M_{i-1}$ (as $q\notin P_{\mathrm{ess},i-1}=\bigcup\mathcal M_{i-1}$), so $q$ contributes nothing to hitting any minimal. Thus all hitting is done by $O$: $O$ intersects every $M\in\mathcal M_{i-1}$, i.e. is a transversal. Since $\mathcal M_{i-1}\neq\emptyset$ (contains $\mathcal M_1=\{P(a_1)\}$), the empty set is not a transversal, so $O\neq\emptyset$.

(ii) Let $L_O=\prod_{p\in O}p$ (squarefree). Any positive multiple $m$ of $L_O$ has $O\subseteq P(m)$; since $O$ is a transversal and supersets of transversals are transversals, $m\in V_{i-1}$. The smallest multiple of $L_O$ strictly above $a_{i-1}$ is at most $a_{i-1}+L_O$ and is a valid candidate. The greedy choice $a_i$ is the smallest valid integer above $a_{i-1}$, so $a_i\le a_{i-1}+L_O$. ∎

*Unconditional — uses only old essential primes, NOT the finiteness of $P_{\mathrm{ess}}$ (non-circular). Note: the bound depends on $a_{i-1}\to\infty$, so it bounds neither prime sizes nor promotion count; it is a partial result toward the wall, insufficient alone to close finiteness.*

**Source.** Approach `bertrand-dickson-eviction` (Lemma 5), round 1. Reviewer-certified.
