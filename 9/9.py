def neighbours(data, row, column):
    neighbours = []
    if row > 0:
        neighbours.append((row-1, column))
    if row < len(data)-1:
        neighbours.append((row+1, column))
    if column > 0:
        neighbours.append((row, column-1))
    if column < len(data[0])-1:
        neighbours.append((row, column+1))
    return neighbours


def is_low(data, row, column):
    cur = data[row][column]
    for nrow, ncolumn in neighbours(data, row, column):
        if data[nrow][ncolumn] <= cur:
            return False

    return True



def find_low_points(data):

    return [data[row][column]
            for row in range(len(data))
            for column in range(len(data[0]))
            if is_low(data, row, column)]


def parse(data):
    data = data.strip().split("\n")
    data = [[int(data[row][column])
            for column in range(len(data[0]))]
            for row in range(len(data))
            ]
    print(neighbours(data, 0, 0))
    low_points = find_low_points(data)
    print(low_points)
    return sum(int(pos)+1 for pos in low_points)


print(parse("""
2199943210
3987894921
9856789892
8767896789
9899965678
"""))

# print(parse(open("9.txt").read()))
