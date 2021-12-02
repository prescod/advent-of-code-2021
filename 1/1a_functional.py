try:
    from itertools import pairwise
except ImportError:
    from util import pairwise


with open("1.txt") as f:
    as_ints = [int(line) for line in f]
as_pairs = pairwise(as_ints)
deltas = [second > first for first, second in as_pairs]
count = sum(deltas)

print(count)
