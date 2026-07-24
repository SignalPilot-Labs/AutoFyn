from sim_dichotomy import build_seq, primeset
import time

def analyze_all(a1, S0, N):
    t0=time.time()
    a = build_seq(a1, N)
    print("build time", time.time()-t0)
    rho = {}
    for n in range(1, N+1):
        rho[n] = primeset(a[n]) & S0
    branch_b_count = 0
    branch_a_count = 0
    examples_b = []
    for n in range(2, N+1):
        Pn = primeset(a[n])
        outside = Pn - S0
        for qprime in outside:
            e=0; tmp=a[n]
            while tmp % qprime==0:
                tmp//=qprime; e+=1
            c = tmp
            if c <= a[n-1]:
                branch_a_count += 1
                continue
            # branch a fails -> must find rescuer
            found=None
            for i in range(1,n):
                Pi = primeset(a[i])
                if Pi & Pn == {qprime}:
                    found = i
                    break
            if found is not None:
                branch_b_count += 1
                examples_b.append((n, qprime, found, rho[n], rho[found]))
            else:
                print("ERROR: no rescuer found for", n, qprime)
    print("branch_a_count", branch_a_count, "branch_b_count", branch_b_count)
    for ex in examples_b[:30]:
        print(ex)
    return branch_a_count, branch_b_count, examples_b

if __name__=="__main__":
    print("=== a1=4807, N=3000 ===")
    S0 = {2,3,5,11,19,23}
    analyze_all(4807, S0, 3000)
