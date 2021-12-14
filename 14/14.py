from collections import Counter


def transform(template, rules):
    out = []
    for index in range(len(template) - 1):
        char1 = template[index]
        char2 = template[index + 1]
        out.append(char1)
        if char1 + char2 in rules:
            out.append(rules[char1 + char2])
        else:
            assert False, char1 + char2
    out.append(template[-1])
    return "".join(out)


def parse(data):
    lines = data.strip().split("\n")
    template = lines.pop(0)
    assert lines.pop(0) == ""
    pairs = [line.split("->") for line in lines]
    rules = dict([[part.strip() for part in pair] for pair in pairs])
    return template, rules


def expand(data, count):
    template, rules = parse(data)
    for i in range(count):
        template = transform(template, rules)
        print(i, len(template), template)
    return template


def doit(data, count):
    data = expand(data, count)
    counts = Counter(data)
    return max(counts.values()) - min(counts.values())


def test():
    assert expand(testdata, 4) == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    assert doit(testdata, 10) == 1588


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
print(doit(open("14.txt").read(), 4))
