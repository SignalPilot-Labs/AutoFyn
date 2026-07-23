start 02:07pm end 03:11pm 
I need to be upfront with you: after extensive further work, I discovered that my original answer **"60° ≤ θ < 90°" was wrong**, and rather than paper over that, let me show you what I can actually verify rigorously, and be honest about where I ran into genuine difficulty.

## What I can prove completely

**Claim 1: If θ > 90°, Mulan cannot win.**

Model each triangle's angles as a triple $(p,q,v)$. If Mulan splits vertex $v$ (angle $v$) with parameter $t\in(0,v)$, the two resulting triangles are
$$T_1=(p,\,t,\,v+q-t), \qquad T_2=(q,\,v-t,\,p+t).$$

Suppose Shan‑Yu starts with the **equilateral triangle** $(60,60,60)$, and maintains the invariant "all three angles are $<\theta$." If this holds for $(p,q,v)$, then $t<v<\theta$ and $p,q<\theta$ automatically. The only way a candidate could fail is if $v+q-t\ge\theta$ **and** $p+t\ge\theta$ simultaneously. Adding these:
$$v+q-t+p+t = p+q+v = 180 \ge 2\theta \implies \theta \le 90,$$
contradicting $\theta>90$. So at least one candidate keeps all angles $<\theta$, and Shan‑Yu can always pick it — forever. Hence $\theta$ is never reached. $\blacksquare$

**Claim 2: θ = 90° always works, in one move.**

If the current triangle has no right angle, exactly one angle is $>90°$ or none is; either way there's a vertex $X$ whose *other two* angles $Y,Z$ satisfy $Y,Z<90°$ (existence: a triangle has at most one angle $\ge 90°$). Cut with $t=90-Y$ (valid since $0<t<X$ follows from $Y<90<X+Y$). Then
$$T_1=(Y,\,90-Y,\,X+Z-90+Y)=(Y,90-Y,90),\qquad T_2=(Z,\,X+Y-90,\,90),$$
using $X+Y+Z=180$. **Both** contain $90°$ — this is just the elementary fact that dropping an altitude from a vertex whose base angles are acute creates two right angles. So Mulan wins in exactly one move, regardless of the starting triangle.

**Corollary (the "doubling" tool).** If a triangle ever has an angle equal to exactly $2\theta$, bisecting it ($t=\theta$) forces $\theta$ into *both* resulting triangles, regardless of the other two angles — since $Y+\theta$ and $Z+\theta$... more precisely the shared value $t=\theta$ appears in both. This is winning in one move.

## Where I got stuck

Using these tools I confirmed $\theta=45°$ (via $90\to45$ bisection), $\theta=60°$ (via a special coincidence where a natural "trap" triangle forces an angle of exactly $120°=2\cdot60°$), and I found strong numerical evidence that values like $\theta=70°$ let Shan‑Yu build a **permanent defensive cycle** (I traced an explicit pair of triangles Shan‑Yu can oscillate between forever against every line of attack I tried). This pointed toward the conjecture that the winning set is exactly
$$\theta \in \left\{\frac{180^\circ}{n} : n = 2,3,4,5,\dots\right\},$$
i.e. divisors of $180°$ — a Euclidean-algorithm-flavored condition. However, when I tried to construct and verify a **uniform general strategy** proving Mulan wins for *every* such $n$ (not just $n=2,3,4$), my constructions kept running into unresolved cycles for larger $n$ that I could not conclusively break or conclusively confirm are unbreakable within the time I spent.

## Honest bottom line

I can rigorously stand behind:
- $\theta > 90°$: **not** achievable (proof above, solid).
- $\theta = 90°, 60°, 45°$: achievable (proofs above/sketched, solid).
- A conjecture that the full answer is $\theta = 180°/n$, $n\ge 2$ — but I do not currently have a complete, gap-free proof of this in general, in either direction.

Given your instruction to only present a complete verified solution, I don't want to hand you a polished-looking writeup of the general $180°/n$ claim while knowing part of it is unverified — that would be worse than telling you plainly where my proof stands. If you'd like, I can keep pushing specifically on constructing (and stress-testing) a clean general strategy for the $180°/n$ direction, or we could sanity-check the problem statement/source together in case there's a detail I'm mis-modeling.