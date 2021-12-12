from functools import reduce

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
    return [(row, column)
            for row in range(len(data))
            for column in range(len(data[0]))
            if is_low(data, row, column)]


def expand_low_point(data, low_point):
    to_explore = [low_point]
    explored = set()
    ignored = set()

    while to_explore:
            point = to_explore.pop()
            explored.add(point)
            for x,y in neighbours(data, *point):
                if data[x][y]==9:
                    ignored.add((x,y))
                elif (x,y) not in explored:
                    to_explore.append((x,y))
    return explored


def parse(data):
    data = data.strip().split("\n")
    data = [[int(data[row][column])
            for column in range(len(data[0]))]
            for row in range(len(data))
            ]
    low_points = find_low_points(data)
    print(low_points)
    basins = [expand_low_point(data, low_point) for low_point in low_points]
    print(basins)
    basin_sizes = [len(basin) for basin in basins]
    biggest_3 = sorted(basin_sizes, reverse=True)[0:3]
    print(basin_sizes)
    return reduce(lambda x,y: x*y, biggest_3)


print(parse("""
2199943210
3987894921
9856789892
8767896789
9899965678
"""))

print(parse(open("9.txt").read()))
