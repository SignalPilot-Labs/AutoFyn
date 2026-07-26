from fractions import Fraction
def A_branch2(m1,m2,m3,m4):
    rest=sorted([m1,m2,m3,m4,2,1],reverse=True)
    A=4
    for i,v in enumerate(rest):
        if i%2==0: A-=v
        else: A+=v
    return A
# B2a-i: m2>=2,m3>=2,m4<=2. e.g. (3.5,2.5,2,0) degenerate, m4=0
print("B2a-i (3.5,2.5,2,0):", A_branch2(3.5,2.5,2,0))  # expect >=1
print("B2a-i (3,2,2,1):", A_branch2(3,2,2,1))
# B2a-ii m3>=1, m4>=1: (3.5,2.5,1.5,0.5) -> m4<1
print("B2a-ii m3>=1 m4<1 (3.5,2.5,1.5,0.5):", A_branch2(3.5,2.5,1.5,0.5))
# B2a-ii m3<1 strict: (3.9,2.5,0.8,0.8)
print("B2a-ii m3<1 (3.9,2.5,0.8,0.8):", A_branch2(3.9,2.5,0.8,0.8))
# B2b m3>=1 m4>=1: (3.5,1.8,1.4,1.3) m2<2
print("B2b m3>=1 m4>=1 (3.5,1.8,1.4,1.3):", A_branch2(3.5,1.8,1.4,1.3))
# B2b m3>=1 m4<1: (3.5,1.9,1.5,1.1) m4>=1 actually. try (3.6,1.9,1.5,1.0)
print("B2b m4<1 (3.8,1.9,1.4,0.9):", A_branch2(3.8,1.9,1.4,0.9))
# near boundary m1->4: (3.999, 2.0, 1.0, 1.001) -> ordering? need m2>=m3>=m4. (3.999,2,1.0005,1.0)
print("boundary (3.999,2,1.0005,0.9995):", A_branch2(3.999,2,1.0005,0.9995))
# the impossible sub-case: try m2<2,m3<1 -> should not exist with sum>4
# m1=3.5, m2+m3+m4=4.5, m2<2,m3<1,m4<1 -> m2>2.5 contradiction
