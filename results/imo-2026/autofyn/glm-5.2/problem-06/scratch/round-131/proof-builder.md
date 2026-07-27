# Proof builder — round 131

**Task.** Package the certified IMO 2026 P6 solution into a single fully self-contained document (packaging, not new proof work).

**File produced.** `/home/agentuser/repo/results/imo-2026-06/self-contained-solution.md`

**Summary.** I assembled one linear, self-contained proof of IMO 2026 Problem 6, top to bottom, with zero imports from any `lemmas/*.md` or `approaches/*.md` file. The document faithfully reproduces the reviewer-certified content:
- §1 Problem statement; §2 Setup (radicals, the index-ordered radical partial order $\prec$, $\prec$-minimality, the strict-increase equivalence $i<n\iff a_i<a_n$, large/small primes, $P_0=\{p\le a_1^2\}$, $\mathcal F$, $\mathcal M$).
- §3 Lemma A (Piece A, unconditional) — proves (i)$\iff$(ii) (no-skip greedy + unboundedness) and (ii)$\iff$(iii) ($\prec$-minimal chain reduction with termination) in full; explicit no-finiteness note (non-circularity).
- §4 Lemma B (Direction B) — first-appearance argument; one-line remark that Direction A is false and unused.
- §5 Theorem (Large-prime descent) — induction on $n$ with all four sub-steps discharged (landing via $a_n/a_1>q$, index-descent, shared-prime transfer via IH, rad-divisibility via $q\mid c$); base case and inductive step; closing of the induction. Corollary $\mathcal M\subseteq 2^{P_0}$ finite.
- §6 The Finish, proved in full inline as six named lemmas in logical order: Pairwise intersection (unconditional, from greedy rule); Transversal residue characterization (CRT cited to knowledge_base.md, free-rider invisibility); Universal membership / no transient (trichotomy on $j$ vs $n$, using pairwise intersection — delivers zero transient, dynamics from $n=1$); Greedy = cyclic successor (both containments $V\subseteq V_n$ and the universal-membership lower bound, plus the $a_{n+1}-a_n\le L$ corollary); Cyclic successor is a single cycle with period-sum $L$ (telescoping increments); Conclusion combining them into $a_{n+T}=a_n+L$ with the constructive pair $(T,L)=(|V|,\prod_{p\in\bigcup\mathcal M}p)$.
- §7 Numerical sanity checks ($a_1=15\to T=8,L=30$; $a_1=429\to T=908,L=4290$; $a_1=30\to T=1,L=2$), stated as confirmations not proof steps.

Every lemma previously imported by name (`post-stabilization-theorem`, `transversal-residue-characterization`, `universal-membership-no-transient`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle`, `pairwise-intersection`) is now proved in full inside this single document. The only external citation is to `knowledge_base.md` for CRT (the repo's generic theorem catalogue, not a proof-step import), as permitted by the spec. Content was reproduced faithfully from the certified sources; no new unverified arguments were introduced.

**Spec concerns.** (none)
