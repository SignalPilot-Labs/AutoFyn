# Lemma — MT depends only on the set-system

**Setting.** For a finite family $\mathcal F$ of finite sets, $\operatorname{MT}(\mathcal F)$ denotes the family of minimal transversals (hitting sets) of $\mathcal F$.

**Lemma.** *If $\mathcal F$ and $\mathcal F'$ have the same distinct member-sets (i.e. they are equal as set-systems, ignoring multiplicities and ordering), then $\operatorname{MT}(\mathcal F)=\operatorname{MT}(\mathcal F')$.*

*Proof.* A transversal of $\mathcal F$ is a set $T$ with $T\cap F\ne\varnothing$ for every $F\in\mathcal F$. Whether $T\cap F\ne\varnothing$ depends only on the set $F$, not on any multiplicity or position of $F$ in a list. Hence the family of transversals of $\mathcal F$ depends only on the set-system $\{F:F\in\mathcal F\}$ (the collection of distinct members). Minimality ("no proper subset is a transversal") is a property of the transversal family, so it too depends only on the set-system. Thus $\operatorname{MT}$ depends only on the distinct member-sets. ∎ *(Reviewer-verified, round 2.)*

**Import.** Standard fact, fully proved here. Importable by any approach that needs to deduce $\operatorname{MT}$-stabilization from set-system stabilization (see `distinct-supports-stabilize`). Replaces the round-1 FALSE claim "$\operatorname{MT}$ is a non-increasing antichain under set addition" — counterexample: $F=\{\{1,2\}\}$ has $\operatorname{MT}=\{\{1\},\{2\}\}$; add $\{2,3\}$ and $\operatorname{MT}=\{\{1,3\},\{2\}\}$ — the new minimal transversal $\{1,3\}$ is *created*.
