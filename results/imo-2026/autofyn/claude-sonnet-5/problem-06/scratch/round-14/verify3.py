import sys
sys.path.insert(0, '/tmp/round-14')
from gen import gen_sequence
from sympy import factorint

def check_2747(N=20000):
    a1 = 2747
    P1 = {41,67}
    terms, rads = gen_sequence(a1, N)
    bad = 0
    I67 = []
    I41 = []
    for idx, (v,R) in enumerate(zip(terms, rads), start=1):
        core = R & P1
        comp = R - P1
        if core == {67}:
            I67.append((idx,v,comp))
            if not {2,3,7} <= comp:
                print("VIOLATION I67:", idx, v, comp)
                bad += 1
        elif core == {41}:
            I41.append((idx,v,comp))
            if not (comp & {2,3,7}):
                print("VIOLATION I41:", idx, v, comp)
                bad += 1
    print(f"|I67|={len(I67)}, |I41|={len(I41)}, violations={bad}")
    print("sample I67:", I67[:5])
    print("sample I41:", I41[:5])

def check_4087(N=20000):
    a1 = 4087
    P1 = {61,67}
    terms, rads = gen_sequence(a1, N)
    bad = 0
    I67 = []
    I61 = []
    for idx, (v,R) in enumerate(zip(terms, rads), start=1):
        core = R & P1
        comp = R - P1
        if core == {67}:
            I67.append((idx,v,comp))
            if 2 not in comp:
                print("VIOLATION I67:", idx, v, comp)
                bad += 1
        elif core == {61}:
            I61.append((idx,v,comp))
            if 2 not in comp:
                print("VIOLATION I61:", idx, v, comp)
                bad += 1
    print(f"|I67|={len(I67)}, |I61|={len(I61)}, violations={bad}")
    print("sample I67:", I67[:5])
    print("sample I61:", I61[:5])

check_2747(20000)
print()
check_4087(20000)
