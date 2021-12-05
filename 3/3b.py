def matching(column_num, lines, match):
    return [line for line in lines if line[column_num] == match]


def most_common(column_num, lines, compare):
    return str(
        int(
            compare(
                len(matching(column_num, lines, "1")),
                len(matching(column_num, lines, "0")),
            )
        )
    )


def calculate(data):
    lines = [line.strip() for line in data.split("\n")]
    oxygen = compute(lines, lambda ones, zeros: ones >= zeros)
    co2 = compute(lines, lambda ones, zeros: ones < zeros)
    return oxygen * co2


def compute(lines, compare):
    columns = range(len(lines[0]))
    for column in columns:
        most = most_common(column, lines, compare)
        matching_numbers = matching(column, lines, most)
        lines = matching_numbers
        assert lines
        if len(lines) == 1:
            break
    return int(lines[0], 2)


def test():
    testdata = """00100
                11110
                10110
                10111
                10101
                01111
                00111
                11100
                10000
                11001
                00010
                01010"""
    return calculate(testdata)


print(test())
print(calculate(open("3.txt").read()))
