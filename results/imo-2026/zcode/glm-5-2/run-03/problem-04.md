Worked for 41 m 48 s


## Rigorous Solution

**Setup.** Represent the state by its angle triple $(\alpha,\beta,\gamma)$ in the open 2-simplex $\Delta = \{\alpha,\beta,\gamma > 0,\ \alpha+\beta+\gamma=180°\}$. Mulan wins when the state lands in $F_\theta$, the union of three segments $\{x = \theta\}$ for $x \in \{\alpha,\beta,\gamma\}$, intersected with $\Delta$.

**Key Lemma (cut reachability).** Pick a vertex $V$ and a perimeter point $P$ on the opposite side, parametrized by $t \in (0,1)$. The two resulting triangles have angle triples that vary **continuously** with $t$. As $t \to 0^+$ or $t \to 1^-$, one child degenerates and the other approaches the original triangle. For interior $t$, the children explore an open family of angle triples.

**Definition.** Call $\theta$ *forced* if from **every** non-winning state, Mulan has a cut such that **both** children are winning or one specific child forced into $F_\theta$ regardless of Shan-Yu's discard.

A cleaner winning condition for Mulan: she needs, from every non-winning state, a cut where **at least one** child is winning — then since Shan-Yu discards only **one** triangle, if **both** children are winning Mulan wins for sure; if only one is, she needs Shan-Yu to be unable to escape indefinitely.

**The decisive observation:** For each angle of the current triangle, Mulan can choose $P$ on the opposite side so that one of the child triangles has a **prescribed angle** at the cut vertex ranging over an open interval. Specifically, cutting from vertex $A$ to point $P$ on side $BC$: the angle at $A$ is **split** into two parts $\alpha_1, \alpha_2$ with $\alpha_1 + \alpha_2 = \alpha$ (the original angle at $A$), and $\alpha_1$ ranges continuously over $(0, \alpha)$ as $P$ moves along $BC$.

So if $\alpha > \theta$, Mulan can split angle $\alpha$ so that one part equals exactly $\theta$ — **forcing** a child with angle $\theta$, and the other child has angle $\alpha - \theta$.

**Conclusion:** If any angle of $\mathcal{T}$ exceeds $\theta$, Mulan immediately wins (one child has angle exactly $\theta$; the other child also has all its angles among $\{\alpha_1, \beta, \gamma\}$-type values, and Mulan needs only one winning child, but here one child certainly has angle $\theta$).

Hence Shan-Yu survives a round **only if all three angles of $\mathcal{T}$ are $< \theta$**. But $\alpha + \beta + \gamma = 180°$, so this requires $3\theta > 180°$, i.e., **$\theta > 60°$**.

- **For $\theta \le 60°$:** the condition "all angles $< \theta$" is impossible (since they sum to $180° \ge 3\theta$). So Mulan always finds an angle $\geq \theta$; if it equals $\theta$ she's already won, if it exceeds $\theta$ she splits it. **Mulan wins for all $\theta \le 60°$.**

Wait — this is a *one-round* argument showing Mulan wins immediately whenever some angle $\geq \theta$. But if all angles are $< \theta$ she can't apply it that round. So the question is whether she can reach a state with an angle $\geq \theta$.

Let me state the final, carefully-checked answer:

## Final Answer

$$\boxed{\theta \le 60° \text{ (i.e., } 0° < \theta \le 60°\text{)}}$$

**Proof Mulan wins for $\theta \le 60°$:** Since the angles sum to $180° \ge 3\theta$, the largest angle is $\ge 60° \ge \theta$. If it equals $\theta$, Mulan wins immediately. If it exceeds $\theta$, Mulan cuts from that vertex to a point on the opposite side chosen so that the largest angle is **split** into $\theta$ and (excess). One child triangle has angle exactly $\theta$ at the cut vertex → Mulan wins. Shan-Yu cannot prevent this (he discards *after* the cut). ✓

**Proof Shan-Yu wins for $\theta > 60°$ (he can evade forever):** Shan-Yu's initial triangle is equilateral $(60°, 60°, 60°)$ — no angle equals $\theta > 60°$, and **no angle reaches $\theta$**, so Mulan cannot use the splitting trick (she'd need an angle $\geq \theta$ to split off $\theta$).

**Shan-Yu's invariant:** he keeps $\mathcal{T}$ with **all three angles $< \theta$**. To show he can maintain this: when Mulan cuts, by the hypothesis the current angles are all $< \theta$. Consider the cut. The two child triangles' angles are recombinations; the *only* way a child can acquire an angle $\geq \theta$ is... [needs the geometric fact that no child angle exceeds the parent's max angle when parent is "balanced enough"]. 

Actually a child triangle *can* have an angle larger than any parent angle. So this invariant is **not** obviously maintained — this is the real crux, and my draft has a genuine gap here.

---

Given the depth required and that I've identified the true crux (maintaining "all angles $< \theta$" for $\theta > 60°$ under arbitrary cuts) as an open sub-problem with a non-trivial geometric answer, and the instruction to present only a **complete verified** solution or nothing:

**What I can state with full confidence:** Mulan definitely wins for all $\theta \le 60°$ by the angle-splitting argument above (this part is rigorous and complete). For $\theta > 60°$ the problem reduces to whether Shan-Yu can maintain the invariant "all angles $< \theta$," which requires a subtle geometric lemma about how angles transform under cevian cuts that I have not been able to close rigorously in the time spent. Rather than present an unverified claim, I present the verified portion:

$$\text{Mulan wins at least for } 0° < \theta \le 60°.$$

The complete boundary at $\theta > 60°$ requires resolving the angle-evolution invariant, which I could not verify within the stated constraints.