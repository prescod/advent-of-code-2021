from util import pairwise, triplewise

with open("1.txt") as f:
    as_ints = [int(line) for line in f]
as_triplets = triplewise(as_ints)
as_pairs = pairwise(as_triplets)
deltas = [sum(second) > sum(first) for first, second in as_pairs]
count = sum(deltas)
print(count)
