Worked for 51m 53s

# Solution

**Answer:** Mulan can guarantee victory in finitely many steps (for every initial triangle) **if and only if $\dfrac{180°}{\theta}$ is a positive integer $\geq 2$**, that is, $\theta = \dfrac{180°}{n}$ for some integer $n \in \{2,3,4,\dots\}$.

---

## Setup and notation

Write all angles in units of $\theta$, so the three angles of a triangle sum to $n := 180/\theta$. A triangle is described by its (unordered) angle triple $\{A,B,C\}$ with $A,B,C>0$, $A+B+C=n$.

**The move, in angle-language.** Mulan picks a vertex $V$ (with angle, say, $A$) and a point $P$ on the opposite side; the cut $VP$ splits $A=A_1+A_2$ ($A_1,A_2>0$). If the other two angles are $B$ (adjacent to the $A_1$-side) and $C$ (adjacent to the $A_2$-side), the two resulting triangles have angles
$$T_1=\{A_1,\; B,\; A_2+C\}, \qquad T_2=\{A_2,\; C,\; A_1+B\}$$
(each sums to $n$). Shan-Yu discards one; the other is the new $\mathcal T$.

Call an angle a **$\theta$-multiple** if it equals $j\theta$ for some positive integer $j$, i.e. (in $\theta$-units) it is a positive integer. Mulan wins exactly when some angle equals $\theta$ (= "$1$" in our units).

---

## Direction 1: $\theta = 180°/n \Rightarrow$ Mulan wins

Define the **potential** $\Phi(\mathcal T) = $ the smallest $\theta$-multiple angle present, or $+\infty$ if none. Mulan wins once $\Phi = \theta$ (i.e. $\Phi=1$).

**Strategy.** Maintain the triangle. If it already has a $\theta$-angle, stop. Otherwise:

* **Phase A (no $\theta$-multiple is present).** Let $c$ be the *largest* angle, with neighbors $a \le b$. Mulan destroys $c$, choosing the split so that one child's "third" angle is an integer $m$ in the open interval $(a,\, a+c)$. Such an $m$ exists: for $n\ge 3$ we have $c\ge n/3\ge 1 > 1-\{a\}$, so $\lfloor a\rfloor+1 \in (a,a+c)$; for $n=2$ one checks $m=1\in(a,a+c)$ since $a+c=2-b>1$. Taking $A_1=m-a,\; A_2=c-A_1$, child $T_2=\{A_2,b,m\}$ gets the integer angle $m\theta$; child $T_1=\{A_1,a,A_2+b\}$ gets integer angle $A_2+b=n-m$. **Both children now have a $\theta$-multiple.** Whatever Shan-Yu keeps, the potential becomes finite.

* **Phase B (a $\theta$-multiple $k\theta$, $k\ge 2$, is present).** Mulan destroys the angle of size $k\theta$, splitting it as $\theta + (k-1)\theta$. Child $T_1=\{1,\,\cdot\,,\,\cdot\}$ contains a $\theta$-angle (win if kept); child $T_2$ contains the angle $(k-1)\theta$. If Shan-Yu keeps $T_2$, the smallest $\theta$-multiple has dropped from $k$ to $k-1$ (or $T_2$ already contains $\theta$ and Mulan wins).

**Termination.** Phase A runs at most once (creating a finite potential $\le n-1$). Phase B then strictly decreases the integer $\Phi$ by $1$ at each of Shan-Yu's choices, until $\Phi$ reaches $\theta$ — a win. The total is at most $n-1$ steps. $\checkmark$

---

## Direction 2: $\theta\neq 180°/n \Rightarrow$ Shan-Yu wins

Shan-Yu's strategy is to **keep the triangle inside the trap region**
$$R = \{\mathcal T : \text{no angle of }\mathcal T\text{ is a positive-integer multiple of }\theta\}.$$

**$R$ is nonempty.** The set of "forbidden" angle-values $\{j\theta : j\ge1,\; j\theta<180°\}$ is finite; since $180/\theta\notin\mathbb Z$, generic triangles (e.g. one with three algebraically independent angles, or simply one avoiding this finite set) lie in $R$. Shan-Yu chooses such a triangle initially.

**$R$ is closed under Shan-Yu's reply.** Suppose $\mathcal T=\{A,B,C\}\in R$ (so $A,B,C$ are *not* $\theta$-multiples), and Mulan destroys angle $A=A_1+A_2$. We claim **at least one of the two children is still in $R$**. Suppose, for contradiction, that **both** children have a $\theta$-multiple angle. Since $B\in R$ and $C\in R$, the multiples must come from:
$$T_1=\{A_1,\,B,\,A_2{+}C\}:\quad A_1=j\theta \text{ or } A_2{+}C=j\theta,\qquad T_2=\{A_2,\,C,\,A_1{+}B\}:\quad A_2=j'\theta \text{ or } A_1{+}B=j'\theta.$$
Combining the four possibilities:
- $A_1=j\theta,\;A_2=j'\theta \Rightarrow A=(j{+}j')\theta$, a $\theta$-multiple — contradicts $A\in R$.
- $A_1=j\theta,\;A_1{+}B=j'\theta \Rightarrow B=(j'{-}j)\theta$, contradicts $B\in R$.
- $A_2{+}C=j\theta,\;A_2=j'\theta \Rightarrow C=(j{-}j')\theta$, contradicts $C\in R$.
- $A_2{+}C=j\theta,\;A_1{+}B=j'\theta \Rightarrow$ adding: $(A_1{+}A_2){+}(B{+}C)=180°=(j{+}j')\theta$, i.e. $180/\theta=j{+}j'\in\mathbb Z$ — **contradicts the hypothesis** $\theta\neq 180°/n$.

Every case is impossible, so at least one child lies in $R$. Shan-Yu keeps that child.

Since Shan-Yu can start in $R$ and, after *every* cut of Mulan, retain a child still in $R$, no triangle ever reached has a $\theta$-angle. **Mulan never wins.** $\checkmark$

---

## Conclusion

The two directions together give the exact answer:

$$\boxed{\text{Mulan can guarantee victory if and only if } \ \dfrac{180°}{\theta}\in\mathbb Z,\ \text{ i.e. } \theta=\dfrac{180°}{n}\text{ for some integer }n\ge 2.}$$