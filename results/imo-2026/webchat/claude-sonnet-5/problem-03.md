24 mins

## Setting Up the Framework

**Reduction of the claiming phase.** Once the stick is cut into pieces of lengths $a_1\ge a_2\ge\cdots\ge a_m$, the alternating "claim any unclaimed piece" phase is equivalent to greedy selection: taking the largest remaining piece is a dominant strategy for each player (a standard exchange argument), so Liu Bang (moving first) ends up with $a_1+a_3+a_5+\cdots$ and Xiang Yu with $a_2+a_4+\cdots$. Thus the whole problem reduces to a purely combinatorial game about *where to cut*.

**The n = 1 case (fully rigorous).** Liu Bang places one point splitting $[0,1]$ into pieces $p\ge 1-p$. If Xiang Yu splits the piece of length $L$ (leaving the other piece $M$ fixed) into $x,L-x$, a short optimization shows
$$\max_{x}\ \mathrm{median}(x,L-x,M)=\max(L/2,\,M)\quad (M\le L),$$
attained by an even split ($x=L/2$) or a "matching" split ($x=L-M$). Applying this with $L=p,\ M=1-p$, Liu Bang's guaranteed total becomes $\min(p,\,1-p/2)$, which Liu Bang maximizes by choosing $p$ solving $p=1-p/2$, i.e. $p=2/3$. This gives
$$c(1)=\frac23 .$$

**Extending the analysis.** For general $n$, one analyzes Liu Bang's choice of $n{+}1$ pieces $a\ge$ (other pieces) against Xiang Yu's two dominant families of counter‑strategies:
- an "attack the largest piece" strategy, where Xiang Yu spends its points splitting Liu Bang's largest piece to duplicate the other pieces (a generalization of the matching trick above), which forces Liu Bang down to essentially $1-a$;
- an "attack a small piece" strategy, concentrating all points on one smaller piece to extract close to half its value plus neighboring pieces.

Carrying this out carefully for $n=2$ (balancing these attacks against Liu Bang's choice of piece sizes $a\ge b\ge c$) leads, after equalizing the competing worst‑case attacks, to the optimal configuration $a=\tfrac37,\ b=c=\tfrac27$, yielding
$$c(2)=\frac47 .$$

These two values fit the closed form
$$c(n)=\frac{2^n}{2^{n+1}-1},$$
equivalently $\dfrac1{c(n)} = 2-2^{-n}$, satisfying the recursion $\dfrac{1}{c(n)}=\dfrac{1}{c(n-1)}+2^{-n}$ with $c(0)=1$.

## Conclusion

**I was not able to complete a fully rigorous, verified derivation of the general formula for all $n$ within the available reasoning.** I rigorously established $c(1)=2/3$, and gave a careful (but not fully airtight against every conceivable Xiang‑Yu counter‑strategy) derivation of $c(2)=4/7$, consistent with the closed form
$$c(n)=\frac{2^n}{2^{n+1}-1}.$$

Given the problem's explicit instruction to present **only** a complete, rigorously verified solution rather than partial progress, I must be transparent: I could not, within the time invested, produce and independently verify a fully general proof (both a Liu‑Bang strategy achieving the bound and a matching Xiang‑Yu strategy capping it) valid for **all** $n$, despite strong numerical/structural evidence for the formula above. I would need substantially more careful casework (or a cleverer uniform argument) to certify this as a complete solution, and I do not want to present it to you as fully verified when it is not.