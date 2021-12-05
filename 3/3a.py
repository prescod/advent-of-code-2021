def count(column_num, lines, match):
    return len([line for line in lines if line[column_num] == match])


def most_common(column_num, lines):
    ones = count(column_num, lines, "1")
    zeros = count(column_num, lines, "0")
    return "1" if ones > zeros else "0"


def calculate(data):
    lines = [line.strip() for line in data.split("\n")]
    columns = len(lines[0])
    most_commons = [most_common(column, lines) for column in range(columns)]
    bool_string = "".join(most_commons)
    gamma = int(bool_string, 2)
    inverted = bool_string.translate("".maketrans("01", "10"))
    epsilon = int(inverted, 2)
    return gamma * epsilon


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
