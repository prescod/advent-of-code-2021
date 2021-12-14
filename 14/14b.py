from collections import Counter
from functools import cache


def gen_counters(template, rules, iterations):
    @cache
    def gen_counters_for_pair(pair, iterations):
        if iterations == 0:
            return Counter({pair[0]: 1})
        else:
            middle = rules[pair]
            counts = Counter()
            counts.update(gen_counters_for_pair(pair[0] + middle, iterations - 1))
            counts.update(gen_counters_for_pair(middle + pair[1], iterations - 1))
            return counts

    counter = Counter({template[-1]: 1})
    for index in range(len(template) - 1):
        char1 = template[index]
        char2 = template[index + 1]
        counter.update(gen_counters_for_pair(char1 + char2, iterations))

    print(gen_counters_for_pair.cache_info())
    return counter


def parse(data):
    lines = data.strip().split("\n")
    template = lines.pop(0)
    assert lines.pop(0) == ""
    pairs = [line.split("->") for line in lines]
    rules = dict([[part.strip() for part in pair] for pair in pairs])
    return template, rules


def doit(data, count):
    template, rules = parse(data)
    counts = gen_counters(template, rules, count)
    print(counts)
    return max(counts.values()) - min(counts.values())


def test():
    assert doit(testdata, 10) == 1588
    assert doit(testdata, 40) == 2188189693529


testdata = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

test()
assert doit(open("14.txt").read(), 10) == 2874
print(doit(open("14.txt").read(), 40))
