def product(*iterables, repeat=1):
    pools = [i for i in iterables] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result


def combinations(iterable, r=1):
    result = []
    for i in permutations(iterable, r):
        if sorted(i) == i:
            result.append(i)
    return result


def permutations(iterable, r=1):
    result = []
    for i in product(iterable, repeat=r):
        if len(set(i)) == len(i):
            result.append(i)
    return result
