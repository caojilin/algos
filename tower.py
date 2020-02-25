def tower(n, start, target):
    assert n > 0 and isinstance(n, int)
    if n == 1:
        print("move", start, "to", target)
    else:
        tower(n - 1, start, 6 - start - target)
        tower(1, start, target)
        tower(n - 1, 6 - start - target, target)


def tower(n, start=1, mid=2, end=3):
    """
    define function tower: move piece from 'start' to 'end'
    :param n:
    :param start: 1
    :param mid: 2
    :param end: 3
    :return:
    """
    if n == 1:
        print(f"move {start} to {end}")
    else:
        tower(n - 1, start, end, mid)
        tower(1, start, mid, end)
        tower(n - 1, mid, start, end)
