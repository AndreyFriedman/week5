from typing import Iterable


def bounded_subsets(S: Iterable, C: int):
    count = 0
    tempS = []
    for i in S:
        if i <= C:
            tempS.append(i)
    S = tempS
    S.sort()
    sub = {(): S}

    while count <= len(sub) - 1:
        start = list(sub.keys())[count]
        array = sub[start]
        for i in array:
            if sum(start) + i <= C:
                k = list(start) + i
                k.sort()
                k2 = tuple(k)
                v = array.copy()
                v.remove(i)
                sub[k2] = v
        count = count + 1

    return iter([list(i) for i in sub.keys()])


for s in bounded_subsets([1, 2, 3, 4, 5], 4):
    print(s)
