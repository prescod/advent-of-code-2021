from itertools import tee, islice


def nwise(iterable, n):
    # triplewise('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    iterables = enumerate(tee(iterable, n))
    slices = (islice(iterbl, num, None) for num, iterbl in iterables)
    return zip(*slices)


def triplewise(iterable):
    # triplewise('ABCDEFG') --> ABC BCD CDE DEF EFG
    return nwise(iterable, 3)


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    return nwise(iterable, 2)
