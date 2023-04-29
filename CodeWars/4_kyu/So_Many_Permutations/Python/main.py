
from itertools import permutations as p


def permutations(s):
    lst = list(set(["".join(i) for i in p(s)]))
    return lst
