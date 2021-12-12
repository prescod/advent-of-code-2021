from typing import NamedTuple

class Line(NamedTuple):
    input: list
    output: list

    def all_chars(self):
        return "".join(sorted(self.input))

def infer_segments_and_digits(line: Line):
    segments = {}
    digits = {}
    digits[1] = next(word for word in line.input if len(word)==2)
    digits[7] = next(word for word in line.input if len(word)==3)
    digits[4] = next(word for word in line.input if len(word)==4)
    digits[8] = next(word for word in line.input if len(word)==7)
    all_chars = line.all_chars()
    segments["a"] = next(iter(set(digits[7]) - set(digits[4])))
    segments["b"] = next(char for char in all_chars if all_chars.count(char)==6)
    segments["e"] = next(char for char in all_chars if all_chars.count(char)==4)
    segments["f"] = next(char for char in all_chars if all_chars.count(char)==9)
    segments["c"] = next(char for char in all_chars if all_chars.count(char)==8 and char!=segments["a"])
    segments["d"] = next(char for char in digits[4] if char not in [segments[x] for x in "bcf"])
    segments["g"] = next(char for char in all_chars if char not in [segments[x] for x in "abcdef"])
    print("XXX",segments)
    digits[0] = "".join(sorted([segments[x] for x in "abcefg"]))
    digits[2] = "".join(sorted([segments[x] for x in "acdeg"]))
    digits[3] = "".join(sorted([segments[x] for x in "acfdg"]))
    digits[5] = "".join(sorted([segments[x] for x in "abdfg"]))
    digits[6] = "".join(sorted([segments[x] for x in "ABDEFG".lower()]))
    digits[9] = "".join(sorted([segments[x] for x in "ABCDFG".lower()]))
    return digits
    
def listify_words(input):
    words = input.strip().split(" ")
    return ["".join(sorted(word)) for word in words]

def subparse(line):
    input, output = line.split("|")
    return Line(listify_words(input), listify_words(output))

def parse(data):
    lines = data.split("\n")
    return [subparse(line) for line in lines]

def infer_digits(line):
    print(line)
    digits = infer_segments_and_digits(line)
    codes_to_digits = {code: str(digit) for digit, code in digits.items()}
    print(codes_to_digits)
    return [codes_to_digits["".join(sorted(string))] for string in line.output]

def doit(data):
    data = parse(data)
    return sum([int("".join(infer_digits(line))) for line in data])


testdata = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

print(doit(testdata))
print(doit(open("8.txt").read()))
