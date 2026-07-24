import itertools
from fractions import Fraction as F

def set_partitions(collection):
    collection = list(collection)
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in set_partitions(collection[1:]):
        for i, subset in enumerate(smaller):
            yield smaller[:i] + [[first]+subset] + smaller[i+1:]
        yield [[first]] + smaller

def gen_chambers(m=5, n=4):
    """Yield chamber specs: (blocks, host_dict, bisect_set) with legal cut budget."""
    idxs = list(range(m))
    chambers = []
    for partition in set_partitions(idxs):
        r = len(partition)
        struct_cuts = sum(len(B)-1 for B in partition)  # = m - r
        # choose host for each block size>=2
        host_choices_per_block = []
        for B in partition:
            if len(B) >= 2:
                host_choices_per_block.append(list(B))
            else:
                host_choices_per_block.append([None])
        singleton_indices = [i for B in partition for i in B if len(B)==1]
        for hosts in itertools.product(*host_choices_per_block):
            # bisect subsets of singletons, subject to total cuts <=n
            remaining_budget = n - struct_cuts
            if remaining_budget < 0:
                continue
            max_bisect = min(remaining_budget, len(singleton_indices))
            for bcount in range(0, max_bisect+1):
                for bisect_set in itertools.combinations(singleton_indices, bcount):
                    chambers.append((partition, hosts, frozenset(bisect_set)))
    return chambers

if __name__ == "__main__":
    chambers = gen_chambers()
    print("total chamber specs (before feasibility filter, m=5,n=4):", len(chambers))
