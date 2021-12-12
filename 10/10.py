OPENERS = "([{<"
CLOSERS = {")":"(", "]":"[", "}":"{", ">": "<"}
SCORES = {")":3, "]":57, "}":1197, ">": 25137  }
P2SCORES = {"(":1, "[":2, "{":3, "<": 4 }


CORRUPT = True
INCOMPLETE = False

def score(opens):
    score = 0
    for char in reversed(opens):
        score*=5
        score += P2SCORES[char]

    return score

def parse(line):
    opens = []
    errors = []
    for char in line:
        if char in OPENERS:
            opens.append(char)
        else:
            if CLOSERS[char]==opens[-1]:
                opens.pop(-1)
            else:
                return CORRUPT, char

    return INCOMPLETE, score(opens)

def parser(lines):
    lines = lines.strip().split("\n")
    results = [parse(line) for line in lines]
    p1score = sum([SCORES[char] for (status, char) in results if status==CORRUPT])
    p2scores = sorted([score for (status, score) in results if status==INCOMPLETE])
    middle = len(p2scores) // 2
    return p1score, p2scores[middle]

def test():
    print(parser(testcode))

def real():
    print(parser(open("10.txt").read()))

testcode = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

test()

real()